import pytest
from src.processing.audio_preprocessor import AudioPreprocessor
import os

@pytest.fixture
def preprocessor():
    return AudioPreprocessor()

def test_audio_conversion(preprocessor):
    # 准备测试文件（需要实际存在的测试音频）
    input_path = "test_data/original.mp3" 
    output_path = preprocessor.process(input_path)
    
    # 验证输出文件存在
    assert os.path.exists(output_path)
    
    # 验证文件格式
    assert output_path.endswith(".wav")
    
    # 清理测试文件
    os.remove(output_path)

def test_invalid_file(preprocessor):
    with pytest.raises(FileNotFoundError):
        preprocessor.process("non_existent_file.wav")

def test_unsupported_format(preprocessor):
    with pytest.raises(ValueError):
        preprocessor.process("test_data/corrupted.ogg") 