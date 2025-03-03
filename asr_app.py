import base64
import os
from threading import Thread
import pyaudio
import wave
from pydub import AudioSegment
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.asr.v20190614 import asr_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException
)


def monitor_performance(func):
    """性能监控装饰器"""
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.2f} 秒")
        return result
    return wrapper


def convert_audio(
    input_path, 
    output_format="wav", 
    frame_rate=16000, 
    channels=1
):
    """转换音频格式和参数"""
    try:
        # 读取音频文件
        audio = AudioSegment.from_file(input_path)
        
        # 设置音频参数
        audio = audio.set_frame_rate(frame_rate)
        audio = audio.set_channels(channels)
        audio = audio.set_sample_width(2)
        
        # 导出为WAV格式
        output_path = os.path.splitext(input_path)[0] + "." + output_format
        audio.export(output_path, format=output_format)
        return output_path
    except Exception as e:
        print(f"音频转换失败: {str(e)}")
        return None


@monitor_performance
def tencent_asr(audio_data, secret_id, secret_key):
    """腾讯云语音识别"""
    try:
        # 实例化认证对象
        cred = credential.Credential(secret_id, secret_key)
        
        # 实例化http选项
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"
        
        # 实例化client选项
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        
        # 实例化client对象
        client = asr_client.AsrClient(cred, "ap-guangzhou", clientProfile)
        
        # 实例化请求对象
        req = models.SentenceRecognitionRequest()
        
        # 设置请求参数
        req.ProjectId = 0
        req.SubServiceType = 2
        req.EngSerViceType = "16k_zh"
        req.SourceType = 1
        req.VoiceFormat = "wav"
        req.UsrAudioKey = "test"
        req.Data = audio_data
        
        # 发起请求
        resp = client.SentenceRecognition(req)
        return resp.Result
    
    except TencentCloudSDKException as err:
        print(f"腾讯云API调用失败: {err}")
        return None


def split_audio(audio, chunk_length=59000):  # 59秒分块
    """分割音频为小块"""
    return [
        audio[i:i + chunk_length]
        for i in range(0, len(audio), chunk_length)
    ]


def main():
    """主函数 - 文件处理模式"""
    # 设置音频文件路径
    input_file = "test_recording.wav"
    
    # 转换音频格式
    wav_file = convert_audio(input_file)
    if not wav_file:
        print("音频转换失败")
        return
    
    # 读取音频文件
    with open(wav_file, "rb") as f:
        audio_data = f.read()
    
    # 进行语音识别
    result = tencent_asr(
        base64.b64encode(audio_data).decode(),
        os.getenv("TENCENT_SECRET_ID"),
        os.getenv("TENCENT_SECRET_KEY")
    )
    
    if result:
        print(f"识别结果: {result}")
    else:
        print("识别失败")


def real_time_asr():
    """实时语音识别模式"""
    # 初始化PyAudio
    p = pyaudio.PyAudio()
    
    # 打开音频流
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1024
    )
    
    print("开始录音...")
    frames = []
    
    try:
        while True:
            # 读取音频数据
            data = stream.read(1024)
            frames.append(data)
            
            # 每3秒处理一次
            if len(frames) >= 48:  # 16000Hz采样率，每秒16帧
                # 合并音频数据
                combined = b''.join(frames)
                
                # 创建WAV文件
                with wave.open("temp.wav", 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(16000)
                    wf.writeframes(combined)
                
                # 计算音频时长
                duration = len(combined) / (16000 * 2)
                print(f"处理音频片段，时长: {duration:.2f}秒")
                
                # 读取WAV文件
                with open("temp.wav", "rb") as f:
                    wav_data = f.read()
                
                # Base64编码
                base64_data = base64.b64encode(wav_data).decode()
                
                # 创建新线程处理识别请求
                Thread(
                    target=send_asr_request,
                    args=(
                        base64_data,
                        os.getenv("TENCENT_SECRET_ID"),
                        os.getenv("TENCENT_SECRET_KEY")
                    )
                ).start()
                
                # 清空缓冲区
                frames = []
    
    except KeyboardInterrupt:
        print("\n停止录音")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        if os.path.exists("temp.wav"):
            os.remove("temp.wav")


def send_asr_request(data, secret_id, secret_key):
    """发送语音识别请求"""
    result = tencent_asr(data, secret_id, secret_key)
    if result:
        print(f"识别结果: {result}")


def input_non_blocking():
    """非阻塞输入检测"""
    import sys
    import select
    return sys.stdin in select.select([sys.stdin], [], [], 0)[0]


if __name__ == "__main__":
    print("请选择模式：")
    print("1. 文件处理")
    print("2. 实时识别")
    
    choice = input("请输入选项（1或2）：")
    
    if choice == "1":
        main()
    elif choice == "2":
        real_time_asr()
    else:
        print("无效选项")
