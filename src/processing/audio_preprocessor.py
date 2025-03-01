import os
import logging
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

class AudioPreprocessor:
    """音频预处理模块，负责格式转换和标准化"""
    
    def __init__(self, target_format='wav', sample_rate=16000, channels=1):
        self.target_format = target_format.lower()
        self.sample_rate = sample_rate
        self.channels = channels
        self.logger = logging.getLogger(__name__)

    def process(self, input_path: str) -> str:
        """
        处理音频文件至符合ASR要求的格式
        :param input_path: 输入音频文件路径
        :return: 处理后的文件路径
        """
        try:
            self.logger.info(f"开始处理音频文件: {input_path}")
            
            # 验证输入文件存在
            if not os.path.exists(input_path):
                raise FileNotFoundError(f"输入文件不存在: {input_path}")

            # 加载音频文件
            audio = AudioSegment.from_file(input_path)

            # 格式转换处理
            audio = self._convert_audio(audio)

            # 生成输出路径
            output_path = self._generate_output_path(input_path)
            
            # 导出处理后的音频
            audio.export(output_path, format=self.target_format)
            self.logger.info(f"音频处理完成，保存至: {output_path}")
            
            return output_path

        except CouldntDecodeError as e:
            self.logger.error(f"音频解码失败: {str(e)}")
            raise ValueError(f"不支持的音频格式: {os.path.splitext(input_path)[1]}")
        except Exception as e:
            self.logger.error(f"音频处理异常: {str(e)}")
            raise

    def _convert_audio(self, audio: AudioSegment) -> AudioSegment:
        """执行音频转换操作"""
        return audio.set_frame_rate(self.sample_rate)\
                   .set_channels(self.channels)\
                   .set_sample_width(2)  # 16bit

    def _generate_output_path(self, input_path: str) -> str:
        """生成输出路径"""
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_dir = os.path.join(os.path.dirname(input_path), "processed")
        os.makedirs(output_dir, exist_ok=True)
        return os.path.join(output_dir, f"{base_name}_processed.{self.target_format}") 