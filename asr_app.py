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

# 在文件顶部添加环境变量加载
load_dotenv()  # 加载.env文件

# 在文件顶部添加区域配置
REGION = "ap-shanghai"  # 与你的腾讯云账户区域一致

def convert_audio(input_path, output_format="wav", frame_rate=16000, channels=1):
    """将音频文件转换为符合腾讯ASR要求的格式
    参数要求：
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

def tencent_asr(pcm_data_base64, secret_id, secret_key):
    """调用腾讯云语音识别API"""
    try:
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
        req.EngSerViceType = "16k_zh"  # 修正参数名（注意V大写）
        req.SourceType = 1  # 语音数据直接上传
        req.VoiceFormat = "pcm"  # 修改为实际音频格式（根据文件类型）
        req.FilterDirty = 0  # 新增参数：过滤脏词
        req.FilterModal = 0  # 新增参数：过滤语气词
        req.UsrAudioKey = "session-123"
        req.Data = pcm_data_base64  # 这里现在传入Base64字符串
        
        # 添加参数验证
        if len(pcm_data_base64) > 1048576:  # 1MB限制
            raise ValueError("音频数据超过1MB限制")
            
        resp = client.SentenceRecognition(req)
        return resp.Result
    except Exception as e:
        print(f"ASR请求失败: {str(e)}")
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

if __name__ == "__main__":
    main() 