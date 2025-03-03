0s
Run flake8 . --count --show-source --statistics
./asr_app.py:14:80: E501 line too long (94 > 79 characters)
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
                                                                               ^
./asr_app.py:27:1: E302 expected 2 blank lines, found 1
def monitor_performance(func):
^
./asr_app.py:37:1: E302 expected 2 blank lines, found 1
def convert_audio(input_path, output_format="wav", frame_rate=16000, channels=1):
^
./asr_app.py:37:80: E501 line too long (81 > 79 characters)
def convert_audio(input_path, output_format="wav", frame_rate=16000, channels=1):
                                                                               ^
./asr_app.py:53:38: W291 trailing whitespace
    audio = audio.set_sample_width(2) 
                                     ^
./asr_app.py:58:1: E302 expected 2 blank lines, found 1
@monitor_performance
^
./asr_app.py:70:1: W293 blank line contains whitespace
        
^
./asr_app.py:73:1: W293 blank line contains whitespace
        
^
./asr_app.py:93:1: W293 blank line contains whitespace
        
^
./asr_app.py:97:1: W293 blank line contains whitespace
            
^
./asr_app.py:109:1: E302 expected 2 blank lines, found 1
def split_audio(audio, chunk_length=59000):  # 59秒分块
^
./asr_app.py:112:1: E302 expected 2 blank lines, found 1
def main():
^
./asr_app.py:116:1: W293 blank line contains whitespace
    
^
./asr_app.py:125:1: W293 blank line contains whitespace
    
^
./asr_app.py:129:1: W293 blank line contains whitespace
    
^
./asr_app.py:140:1: E302 expected 2 blank lines, found 1
def real_time_asr():
^
./asr_app.py:144:1: W293 blank line contains whitespace
    
^
./asr_app.py:159:1: W293 blank line contains whitespace
    
^
./asr_app.py:167:1: W293 blank line contains whitespace
        
^
./asr_app.py:185:80: E501 line too long (83 > 79 characters)
                    duration = len(combined) / (16000 * 2)  # 采样率16kHz，16bit=2bytes
                                                                               ^
./asr_app.py:196:80: E501 line too long (82 > 79 characters)
                    base64_data = base64.b64encode(wav_data).decode()  # 编码完整WAV文件
                                                                               ^
./asr_app.py:197:80: E501 line too long (102 > 79 characters)
                    Thread(target=send_asr_request, args=(base64_data, SECRET_ID, SECRET_KEY)).start()
                                                                               ^
./asr_app.py:214:1: E302 expected 2 blank lines, found 1
def send_asr_request(data, secret_id, secret_key):
^
./asr_app.py:221:1: E302 expected 2 blank lines, found 1
def input_non_blocking():
^
./asr_app.py:222:15: E401 multiple imports on one line
    import sys, select
              ^
./asr_app.py:227:1: E305 expected 2 blank lines after class or function definition, found 1
if __name__ == "__main__":
^
./asr_app.py:233:1: W293 blank line contains whitespace
    
^
./asr_app.py:239:22: W292 no newline at end of file
        print("无效选项")                     ^
./recorder.py:2:1: F401 'wave' imported but unused
import wave
^
./recorder.py:3:1: F401 'audioop' imported but unused
import audioop
^
./recorder.py:4:1: F401 'time' imported but unused
import time
^
./recorder.py:5:1: F401 'threading.Thread' imported but unused
from threading import Thread, Event
^
./recorder.py:6:1: F401 'pydub.utils.get_array_type' imported but unused
from pydub.utils import get_array_type
^
./recorder.py:10:1: E302 expected 2 blank lines, found 1
class AudioRecorder:
^
./recorder.py:11:80: E501 line too long (83 > 79 characters)
    def __init__(self, rate=16000, chunk=1024, channels=1, format=pyaudio.paInt16):
                                                                               ^
./recorder.py:57:27: W291 trailing whitespace
        return max(1, rms)                           ^
./recorder.py:57:28: W292 no newline at end of file
        return max(1, rms)                            ^
./report_generator.py:15:6: E999 SyntaxError: invalid syntax
echo "生成今日报告..."
     ^
./src/processing/audio_preprocessor.py:6:1: E302 expected 2 blank lines, found 1
class AudioPreprocessor:
^
./src/processing/audio_preprocessor.py:8:1: W293 blank line contains whitespace
    
^
./src/processing/audio_preprocessor.py:23:1: W293 blank line contains whitespace
            
^
./src/processing/audio_preprocessor.py:36:1: W293 blank line contains whitespace
            
^
./src/processing/audio_preprocessor.py:40:1: W293 blank line contains whitespace
            
^
./src/processing/audio_preprocessor.py:53:20: E127 continuation line over-indented for visual indent
        return audio.set_frame_rate(self.sample_rate)\
                   .set_channels(self.channels)\
                   .set_sample_width(2)  # 16bit
                   ^
./src/processing/audio_preprocessor.py:61:80: E501 line too long (86 > 79 characters)
        return os.path.join(output_dir, f"{base_name}_processed.{self.target_format}")                                                                                ^
./src/processing/audio_preprocessor.py:61:87: W291 trailing whitespace
        return os.path.join(output_dir, f"{base_name}_processed.{self.target_format}")                                                                                       ^
./src/processing/audio_preprocessor.py:61:88: W292 no newline at end of file
        return os.path.join(output_dir, f"{base_name}_processed.{self.target_format}")                                                                                        ^
./test_recording.py:36:11: W291 trailing whitespace
wf.close()           ^
./test_recording.py:36:12: W292 no newline at end of file
wf.close()            ^
./tests/test_audio_preprocessor.py:5:1: E302 expected 2 blank lines, found 1
@pytest.fixture
^
./tests/test_audio_preprocessor.py:9:1: E302 expected 2 blank lines, found 1
def test_audio_conversion(preprocessor):
^
./tests/test_audio_preprocessor.py:11:42: W291 trailing whitespace
    input_path = "test_data/original.mp3" 
                                         ^
./tests/test_audio_preprocessor.py:13:1: W293 blank line contains whitespace
    
^
./tests/test_audio_preprocessor.py:16:1: W293 blank line contains whitespace
    
^
./tests/test_audio_preprocessor.py:19:1: W293 blank line contains whitespace
    
^
./tests/test_audio_preprocessor.py:23:1: E302 expected 2 blank lines, found 1
def test_invalid_file(preprocessor):
^
./tests/test_audio_preprocessor.py:27:1: E302 expected 2 blank lines, found 1
def test_unsupported_format(preprocessor):
^
./tests/test_audio_preprocessor.py:29:56: W291 trailing whitespace
        preprocessor.process("test_data/corrupted.ogg")                                                        ^
./tests/test_audio_preprocessor.py:29:57: W292 no newline at end of file
        preprocessor.process("test_data/corrupted.ogg")                                                         ^
./tests/test_basic.py:3:1: E302 expected 2 blank lines, found 1
class TestBasicSetup(unittest.TestCase):
^
./tests/test_basic.py:7:13: F401 'pyaudio' imported but unused
            import pyaudio
            ^
./tests/test_basic.py:8:13: F401 'tencentcloud.common.credential' imported but unused
            from tencentcloud.common import credential
            ^
./tests/test_basic.py:20:1: E305 expected 2 blank lines after class or function definition, found 1
if __name__ == '__main__':
^
./tests/test_basic.py:21:20: W291 trailing whitespace
    unittest.main()                    ^
./tests/test_basic.py:21:21: W292 no newline at end of file
    unittest.main()                     ^
./utils/logger.py:4:1: E302 expected 2 blank lines, found 1
def setup_logger():
^
./utils/logger.py:7:1: W293 blank line contains whitespace
    
^
./utils/logger.py:24:18: W291 trailing whitespace
    return logger                  ^
./utils/logger.py:24:19: W292 no newline at end of file
    return logger                   ^
1     E127 continuation line over-indented for visual indent
16    E302 expected 2 blank lines, found 1
2     E305 expected 2 blank lines after class or function definition, found 1
1     E401 multiple imports on one line
7     E501 line too long (94 > 79 characters)
1     E999 SyntaxError: invalid syntax
7     F401 'wave' imported but unused
8     W291 trailing whitespace
7     W292 no newline at end of file
19    W293 blank line contains whitespace
69
Error: Process completed with exit code 1.