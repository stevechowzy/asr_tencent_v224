import pyaudio
import wave
import audioop
import time
from threading import Thread, Event
from pydub.utils import get_array_type
from array import array
import math  # 添加math模块导入

class AudioRecorder:
    def __init__(self, rate=16000, chunk=1024, channels=1, format=pyaudio.paInt16):
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.format = format
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = Event()
        self.silence_threshold = 500  # 静音阈值
        self.silence_timeout = 2  # 秒

    def start(self):
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
        if self.is_recording.is_set():
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            return data
        return None

    def stop(self):
        self.is_recording.clear()
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.audio.terminate()
        print("录音已停止")

    @staticmethod
    def calculate_rms(data):
        """使用array和math替代audioop的RMS计算"""
        samples = array('h')  # 'h' 表示有符号短整型（16-bit）
        samples.frombytes(data)
        if not samples:
            return 0
        sum_squares = sum(s**2 for s in samples)
        rms = math.sqrt(sum_squares / len(samples))
        return max(1, rms) 