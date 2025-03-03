import unittest


class TestBasicSetup(unittest.TestCase):
    def test_imports(self):
        """测试基本导入"""
        try:
            import pyaudio  # noqa: F401
            from tencentcloud.common import credential  # noqa: F401
            self.assertTrue(True, "基本导入成功")
        except ImportError as e:
            self.fail(f"导入失败: {str(e)}")

    def test_audio_setup(self):
        """测试音频设置"""
        import pyaudio

        p = pyaudio.PyAudio()
        self.assertGreater(p.get_device_count(), 0, "至少有一个音频设备")
        p.terminate()


if __name__ == "__main__":
    unittest.main()
