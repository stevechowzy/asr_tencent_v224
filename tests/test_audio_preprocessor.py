import pytest
from src.processing.audio_preprocessor import AudioPreprocessor


@pytest.fixture
def preprocessor():
    return AudioPreprocessor()


def test_audio_conversion(preprocessor):
    input_path = "test_data/original.mp3"
    result = preprocessor.process(input_path)
    assert result is not None
    assert result.endswith(".wav")


def test_invalid_file(preprocessor):
    result = preprocessor.process("nonexistent.mp3")
    assert result is None


def test_unsupported_format(preprocessor):
    with pytest.raises(Exception):
        preprocessor.process("test_data/corrupted.ogg")
