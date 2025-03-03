0s
Run flake8 . --count --show-source --statistics
./asr_app.py:29:16: W291 trailing whitespace
    input_path, 
               ^
./asr_app.py:30:25: W291 trailing whitespace
    output_format="wav", 
                        ^
./asr_app.py:31:22: W291 trailing whitespace
    frame_rate=16000, 
                     ^
./asr_app.py:38:1: W293 blank line contains whitespace
        
^
./asr_app.py:43:1: W293 blank line contains whitespace
        
^
./asr_app.py:59:1: W293 blank line contains whitespace
        
^
./asr_app.py:63:1: W293 blank line contains whitespace
        
^
./asr_app.py:67:1: W293 blank line contains whitespace
        
^
./asr_app.py:70:1: W293 blank line contains whitespace
        
^
./asr_app.py:73:1: W293 blank line contains whitespace
        
^
./asr_app.py:82:1: W293 blank line contains whitespace
        
^
./asr_app.py:86:1: W293 blank line contains whitespace
    
^
./asr_app.py:94:80: E501 line too long (82 > 79 characters)
    return [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]
                                                                               ^
./asr_app.py:101:1: W293 blank line contains whitespace
    
^
./asr_app.py:107:1: W293 blank line contains whitespace
    
^
./asr_app.py:111:1: W293 blank line contains whitespace
    
^
./asr_app.py:118:1: W293 blank line contains whitespace
    
^
./asr_app.py:129:1: W293 blank line contains whitespace
    
^
./asr_app.py:138:1: W293 blank line contains whitespace
    
^
./asr_app.py:141:1: W293 blank line contains whitespace
    
^
./asr_app.py:147:1: W293 blank line contains whitespace
            
^
./asr_app.py:152:1: W293 blank line contains whitespace
                
^
./asr_app.py:159:1: W293 blank line contains whitespace
                
^
./asr_app.py:163:1: W293 blank line contains whitespace
                
^
./asr_app.py:167:1: W293 blank line contains whitespace
                
^
./asr_app.py:170:1: W293 blank line contains whitespace
                
^
./asr_app.py:174:71: W291 trailing whitespace
                    args=(base64_data, os.getenv("TENCENT_SECRET_ID"), 
                                                                      ^
./asr_app.py:177:1: W293 blank line contains whitespace
                
^
./asr_app.py:180:1: W293 blank line contains whitespace
    
^
./asr_app.py:209:1: W293 blank line contains whitespace
    
^
./asr_app.py:211:1: W293 blank line contains whitespace
    
^
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
8     E302 expected 2 blank lines, found 1
1     E305 expected 2 blank lines after class or function definition, found 1
3     E501 line too long (82 > 79 characters)
1     E999 SyntaxError: invalid syntax
7     F401 'wave' imported but unused
11    W291 trailing whitespace
6     W292 no newline at end of file