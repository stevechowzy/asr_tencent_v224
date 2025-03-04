import pyaudio
from threading import Event
from pydub.utils import get_array_type


class AudioRecorder:
    """音频录制类"""

    def __init__(self, rate=16000, chunk=1024, channels=1, format=pyaudio.paInt16):
        """初始化音频录制器

        Args:
            rate (int): 采样率
            chunk (int): 每次读取的帧数
            channels (int): 通道数
            format (int): 音频格式
        """
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.format = format
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False
        self.stop_event = Event()

    def start(self):
        """开始录音"""
        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )
        self.frames = []
        self.is_recording = True
        self.stop_event.clear()

    def read_chunk(self):
        """读取一个音频块"""
        if self.is_recording and not self.stop_event.is_set():
            data = self.stream.read(self.chunk)
            self.frames.append(data)
            return data
        return None

    def stop(self):
        """停止录音"""
        self.stop_event.set()
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None
        return b"".join(self.frames)

    def calculate_rms(self, data):
        """计算音频数据的RMS值

        Args:
            data (bytes): 音频数据

        Returns:
            float: RMS值
        """
        array_type = get_array_type(16)
        count = len(data) // 2
        shorts = array_type("h")
        shorts.frombytes(data)
        sum_squares = sum(s * s for s in shorts)
        rms = (sum_squares / count) ** 0.5
        return max(1, rms)
