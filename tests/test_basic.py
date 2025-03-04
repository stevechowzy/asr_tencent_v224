import unittest
import os


class TestBasicSetup(unittest.TestCase):
    """基本设置测试类"""

    def test_imports(self):
        """测试必要的导入"""
        try:
            # 这些导入是必需的，用于测试环境配置
            import pyaudio  # noqa: F401
            from tencentcloud.common import credential  # noqa: F401
        except ImportError as e:
            self.fail(f"导入失败: {str(e)}")

    @unittest.skipIf(os.getenv('CI') == 'true', "在 CI 环境中跳过音频设备测试")
    def test_audio_setup(self):
        """测试音频设置"""
        import pyaudio

        p = pyaudio.PyAudio()
        self.assertGreater(p.get_device_count(), 0, "至少有一个音频设备")
        p.terminate()


if __name__ == "__main__":
    unittest.main()
