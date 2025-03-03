import unittest

class TestBasicSetup(unittest.TestCase):
    def test_imports(self):
        """测试基本导入"""
        import pyaudio
        from tencentcloud.common import credential
        self.assertTrue(True, "基本导入成功")

    def test_audio_setup(self):
        """测试音频设置"""
        import pyaudio
        p = pyaudio.PyAudio()
        self.assertGreater(p.get_device_count(), 0, "至少有一个音频设备")
        p.terminate()

if __name__ == '__main__':
    unittest.main() 