from pydub import AudioSegment
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.asr.v20190614 import asr_client, models
import os
import sys
from dotenv import load_dotenv
import base64  # 在文件顶部添加导入
from pydub.utils import make_chunks
from recorder import AudioRecorder
import time
from threading import Thread
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
import wave
import threading
import io
import pyaudio
from functools import wraps

# 在文件顶部添加环境变量加载
load_dotenv()  # 加载.env文件中的环境变量

# 在文件顶部添加区域配置
REGION = "ap-shanghai"  # 与你的腾讯云账户区域一致

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} executed in {duration:.2f}s")
        return result
    return wrapper

def convert_audio(input_path, output_format="wav", frame_rate=16000, channels=1):
    """将音频文件转换为符合腾讯ASR要求的格式
    参数要求:trg
    - 格式:wav/pcm
    - 采样率:16000 Hz
    - 声道:单声道
    - 位深:16bit
    """
    # 添加文件存在性检查
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"音频文件 {input_path} 不存在")

    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(frame_rate)
    audio = audio.set_channels(channels)
    # 添加位深设置（16bit = 2 bytes）
    audio = audio.set_sample_width(2) 
    if len(audio) > 60000:  # 60秒限制（单位：毫秒）
        raise ValueError("音频时长不能超过60秒")
    return base64.b64encode(audio.raw_data).decode('utf-8')  # 修改返回值为Base64字符串

@monitor_performance
def tencent_asr(pcm_data_base64, secret_id, secret_key):
    """调用腾讯云语音识别API"""
    try:
        # 创建临时内存文件
        header = io.BytesIO()
        with wave.open(header, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
        header.seek(0)
        wav_data = header.getvalue() + base64.b64decode(pcm_data_base64)
        
        # 初始化认证对象
        cred = credential.Credential(secret_id, secret_key)
        
        # 配置HTTP和客户端
        http_profile = HttpProfile()
        http_profile.endpoint = "asr.tencentcloudapi.com"
        client_profile = ClientProfile()
        client_profile.httpProfile = http_profile

        # 创建客户端并发送请求
        client = asr_client.AsrClient(cred, REGION, client_profile)
        req = models.SentenceRecognitionRequest()
        req.ProjectId = 0
        req.SubServiceType = 2  # 实时语音识别
        req.EngSerViceType = "16k_zh"  # 修改引擎类型
        req.SourceType = 1  # 语音数据直接上传
        req.VoiceFormat = "wav"  # 明确指定格式
        req.FilterDirty = 0  # 新增参数：过滤脏词
        req.FilterModal = 0  # 新增参数：过滤语气词
        req.FilterPunc = 0  # 添加标点符号过滤参数
        req.UsrAudioKey = "session-123"
        req.Data = base64.b64encode(wav_data).decode()
        
        # 添加参数验证
        if len(pcm_data_base64) > 1048576:  # 1MB限制
            raise ValueError("音频数据超过1MB限制")
            
        print(f"请求数据大小: {len(pcm_data_base64)} bytes")  # 添加调试输出
        resp = client.SentenceRecognition(req)
        print(f"原始响应: {resp}")  # 打印完整响应
        return resp.Result
    except TencentCloudSDKException as e:
        print(f"SDK错误: {e.get_code()} {e.get_message()}")
        return None
    except Exception as e:
        print(f"未知错误: {str(e)}")
        return None

def split_audio(audio, chunk_length=59000):  # 59秒分块
    return make_chunks(audio, chunk_length)

def main():
    # 从环境变量获取凭证
    SECRET_ID = os.getenv("TENCENT_SECRET_ID")
    SECRET_KEY = os.getenv("TENCENT_SECRET_KEY")
    
    if not SECRET_ID or not SECRET_KEY:
        print("错误：请在.env文件中配置TENCENT_SECRET_ID和TENCENT_SECRET_KEY")
        return

    # 处理拖放文件路径（支持包含空格的路径）
    if len(sys.argv) < 2:
        print("请拖放音频文件到脚本上运行")
        return
    
    # 处理可能带空格的路径（用引号包裹的情况）
    INPUT_FILE = ' '.join(sys.argv[1:])
    INPUT_FILE = os.path.abspath(os.path.expanduser(INPUT_FILE))  # 处理~符号和相对路径
    
    try:
        audio = AudioSegment.from_file(INPUT_FILE)
        chunks = split_audio(audio)
        for i, chunk in enumerate(chunks):
            chunk_data = base64.b64encode(chunk.raw_data).decode('utf-8')
            result = tencent_asr(chunk_data, SECRET_ID, SECRET_KEY)
            print(f"分段{i+1}结果:", result)
    except Exception as e:
        print(f"处理失败: {str(e)}")

def real_time_asr():
    # 获取凭证
    SECRET_ID = os.getenv("TENCENT_SECRET_ID")
    SECRET_KEY = os.getenv("TENCENT_SECRET_KEY")
    
    if not SECRET_ID or not SECRET_KEY:
        print("错误：请在.env文件中配置TENCENT_SECRET_ID和TENCENT_SECRET_KEY")
        return

    # 添加录音器初始化
    recorder = AudioRecorder(
        rate=16000,
        chunk=1600,  # 调整为每块1600采样点（100ms）
        channels=1,
        format=pyaudio.paInt16
    )
    buffer = []
    MAX_BUFFER_SIZE = 10  # 10块 = 1秒
    MIN_AUDIO_DURATION = 1.0  # 最小音频时长（秒）
    
    try:
        recorder.start()
        # 添加测试录音保存
        test_file = wave.open("test_input.wav", 'wb')
        test_file.setnchannels(1)
        test_file.setsampwidth(2)
        test_file.setframerate(16000)
        
        while True:
            data = recorder.read_chunk()
            if data:
                test_file.writeframes(data)
                buffer.append(data)
                if len(buffer) >= MAX_BUFFER_SIZE:
                    combined = b''.join(buffer)
                    # 使用pydub处理音频增益
                    audio_segment = AudioSegment(
                        data=combined,
                        sample_width=2,
                        frame_rate=16000,
                        channels=1
                    )
                    audio_segment = audio_segment + 6  # 增加6dB增益
                    combined = audio_segment.raw_data
                    # 计算实际音频时长
                    duration = len(combined) / (16000 * 2)  # 采样率16kHz，16bit=2bytes
                    if duration < MIN_AUDIO_DURATION:
                        continue  # 跳过不足时长的音频
                    # 添加WAV头信息
                    wav_buffer = io.BytesIO()
                    with wave.open(wav_buffer, 'wb') as wf:
                        wf.setnchannels(1)
                        wf.setsampwidth(2)
                        wf.setframerate(16000)
                        wf.writeframes(combined)
                    wav_data = wav_buffer.getvalue()
                    base64_data = base64.b64encode(wav_data).decode()  # 编码完整WAV文件
                    Thread(target=send_asr_request, args=(base64_data, SECRET_ID, SECRET_KEY)).start()
                    buffer = []
            # 添加退出检测
            if input_non_blocking() == 'q':
                break
            time.sleep(0.01)  # 减少CPU占用
    except KeyboardInterrupt:
        print("\n正在清理资源...")
        recorder.stop()
        # 等待所有线程完成
        for thread in threading.enumerate():
            if thread != threading.main_thread():
                thread.join(timeout=1)
        print("程序已安全退出")
    finally:
        test_file.close()

def send_asr_request(data, secret_id, secret_key):
    try:
        result = tencent_asr(data, secret_id, secret_key)
        print("实时结果:", result)
    except Exception as e:
        print(f"请求失败: {str(e)}")

def input_non_blocking():
    import sys, select
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None

if __name__ == "__main__":
    print("提示：在实时识别模式下，按 Control+C 退出")
    print("请选择模式：")
    print("1. 文件识别")
    print("2. 实时识别")
    choice = input("输入选项 (1/2): ")
    
    if choice == "1":
        main()
    elif choice == "2":
        real_time_asr()
    else:
        print("无效选项")