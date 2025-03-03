import pyaudio
import wave
import audioop
import time
from threading import Thread, Event
from pydub.utils import get_array_type
from array import array
import math  # 添加math模块导入


class AudioRecorder:
    """音频录制器类"""

    def __init__(
        self,
        rate=16000,
        chunk=1024,
        channels=1,
        format_type=pyaudio.paInt16
    ):
        """
        初始化录音器
        
        Args:
            rate (int): 采样率，默认16000Hz
            chunk (int): 缓冲区大小，默认1024
            channels (int): 通道数，默认1（单声道）
            format_type: 音频格式，默认16位PCM
        """
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.format = format_type
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = Event()
        self.silence_threshold = 500  # 静音阈值
        self.silence_timeout = 2  # 秒

    def start(self):
        """开始录音"""
        self.stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        self.is_recording.set()
        print("录音已开始...")

    def read_chunk(self):
        """
        读取一个音频块
        
        Returns:
            bytes: 音频数据
        """
        if self.stream and self.is_recording.is_set():
            return self.stream.read(self.chunk)
        return None

    def stop(self):
        """停止录音"""
        self.is_recording.clear()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        print("录音已停止")

    def calculate_rms(self, data):
        """
        计算音频数据的均方根值（音量）
        
        Args:
            data (bytes): 音频数据

        Returns:
            float: RMS值
        """
        if not data:
            return 0

        # 将字节数据转换为短整型数组
        count = len(data) // 2
        shorts = array.array('h', data)
        sum_squares = sum(s * s for s in shorts)
        rms = (sum_squares / count) ** 0.5

        return max(1, rms)
