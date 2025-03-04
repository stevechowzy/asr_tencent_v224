import pytest
import pyaudio
import wave
import os

@pytest.fixture
def audio_setup():
    """设置音频录制环境"""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "test_data/test_recording.wav"
    
    # 确保测试数据目录存在
    os.makedirs('test_data', exist_ok=True)
    
    return {
        'format': FORMAT,
        'channels': CHANNELS,
        'rate': RATE,
        'record_seconds': RECORD_SECONDS,
        'output_filename': WAVE_OUTPUT_FILENAME
    }

def test_audio_recording(audio_setup):
    """测试音频录制功能"""
    p = pyaudio.PyAudio()
    
    stream = p.open(
        format=audio_setup['format'],
        channels=audio_setup['channels'],
        rate=audio_setup['rate'],
        input=True,
        frames_per_buffer=1024
    )
    
    frames = []
    for _ in range(0, int(audio_setup['rate'] / 1024 * audio_setup['record_seconds'])):
        data = stream.read(1024)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # 保存录音文件
    wf = wave.open(audio_setup['output_filename'], "wb")
    wf.setnchannels(audio_setup['channels'])
    wf.setsampwidth(p.get_sample_size(audio_setup['format']))
    wf.setframerate(audio_setup['rate'])
    wf.writeframes(b"".join(frames))
    wf.close()
    
    # 验证文件是否创建成功
    assert os.path.exists(audio_setup['output_filename'])
    assert os.path.getsize(audio_setup['output_filename']) > 0 