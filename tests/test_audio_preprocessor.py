import pytest
import os
import shutil
from src.processing.audio_preprocessor import AudioPreprocessor


@pytest.fixture
def preprocessor():
    """创建音频预处理器实例"""
    return AudioPreprocessor()


@pytest.fixture
def test_data_dir():
    """创建测试数据目录"""
    test_dir = os.path.join(os.path.dirname(__file__), '..', 'test_data')
    os.makedirs(test_dir, exist_ok=True)
    return test_dir


def test_audio_conversion(preprocessor, test_data_dir):
    """测试音频转换功能"""
    # 使用项目中的测试音频文件
    original_test_file = os.path.join(os.path.dirname(__file__), '..', 'test.wav')
    input_path = os.path.join(test_data_dir, "original.wav")
    output_dir = os.path.join(test_data_dir, "processed")

    # 确保测试目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 复制测试音频文件到测试目录
    shutil.copy2(original_test_file, input_path)

    # 处理音频文件
    output_path = preprocessor.process(input_path, output_dir)

    # 验证输出文件
    assert output_path is not None
    assert os.path.exists(output_path)
    assert output_path.endswith(".wav")

    # 清理测试文件
    os.remove(input_path)
    shutil.rmtree(output_dir)


def test_invalid_file(preprocessor):
    """测试无效文件处理"""
    output_path = preprocessor.process("nonexistent.mp3")
    assert output_path is None


def test_unsupported_format(preprocessor, test_data_dir):
    """测试不支持的音频格式"""
    input_path = os.path.join(test_data_dir, "corrupted.ogg")
    with open(input_path, 'wb') as f:
        f.write(b'dummy audio data')
    output_path = preprocessor.process(input_path)
    assert output_path is None
