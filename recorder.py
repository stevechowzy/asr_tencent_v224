import pyaudio
import time

class AudioRecorder:
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.chunk = 1024
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False

    def start(self):
        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        self.is_recording = True
        print("录音已开始...")

    def read_chunk(self):
        if self.is_recording:
            return self.stream.read(self.chunk)
        return None

    def stop(self):
        if self.is_recording:
            self.is_recording = False
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            print("录音已停止") 