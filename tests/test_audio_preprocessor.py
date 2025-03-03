import pytest
import os
from src.processing.audio_preprocessor import AudioPreprocessor


@pytest.fixture
def preprocessor():
    """创建音频预处理器实例"""
    return AudioPreprocessor()


def test_audio_conversion(preprocessor):
    """测试音频转换功能"""
    input_path = "test_data/original.mp3"
    output_dir = "test_data/processed"

    # 确保测试目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 处理音频文件
    output_path = preprocessor.process(input_path, output_dir)

    # 验证输出文件
    assert output_path is not None
    assert os.path.exists(output_path)
    assert output_path.endswith(".wav")


def test_invalid_file(preprocessor):
    """测试无效文件处理"""
    output_path = preprocessor.process("nonexistent.mp3")
    assert output_path is None


def test_unsupported_format(preprocessor):
    """测试不支持的音频格式"""
    output_path = preprocessor.process("test_data/corrupted.ogg")
    assert output_path is None
