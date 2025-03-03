import os
from pydub import AudioSegment


class AudioPreprocessor:
    """音频预处理器类"""

    def __init__(
        self,
        sample_rate=16000,
        channels=1,
        target_format="wav"
    ):
        """
        初始化音频预处理器
        
        Args:
            sample_rate (int): 目标采样率
            channels (int): 目标通道数
            target_format (str): 目标音频格式
        """
        self.sample_rate = sample_rate
        self.channels = channels
        self.target_format = target_format

    def process(self, input_path, output_dir=None):
        """
        处理音频文件
        
        Args:
            input_path (str): 输入音频文件路径
            output_dir (str): 输出目录
            
        Returns:
            str: 处理后的文件路径
        """
        try:
            # 检查输入文件是否存在
            if not os.path.exists(input_path):
                print(f"输入文件不存在: {input_path}")
                return None

            # 读取音频文件
            audio = AudioSegment.from_file(input_path)
            
            # 标准化音频参数
            audio = self._normalize_audio(audio)
            
            # 生成输出路径
            output_path = self._generate_output_path(input_path, output_dir)
            
            # 导出处理后的音频
            audio.export(output_path, format=self.target_format)
            return output_path
            
        except Exception as e:
            print(f"音频处理失败: {str(e)}")
            return None

    def _normalize_audio(self, audio):
        """
        标准化音频参数
        
        Args:
            audio (AudioSegment): 音频段
            
        Returns:
            AudioSegment: 处理后的音频
        """
        return (
            audio
            .set_frame_rate(self.sample_rate)
            .set_channels(self.channels)
            .set_sample_width(2)
        )

    def _generate_output_path(self, input_path, output_dir):
        """
        生成输出文件路径
        
        Args:
            input_path (str): 输入文件路径
            output_dir (str): 输出目录
            
        Returns:
            str: 输出文件路径
        """
        if output_dir is None:
            output_dir = os.path.dirname(input_path)

        filename = os.path.splitext(os.path.basename(input_path))[0]
        return os.path.join(
            output_dir,
            f"{filename}_processed.{self.target_format}"
        )
