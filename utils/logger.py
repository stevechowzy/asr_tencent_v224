import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger():
    """配置日志记录器

    Returns:
        logging.Logger: 配置好的日志记录器
    """
    logger = logging.getLogger("ASR")
    logger.setLevel(logging.DEBUG)

    # 创建日志目录
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # 配置文件处理器
    file_handler = RotatingFileHandler(
        "logs/asr.log",
        maxBytes=1024 * 1024,
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    # 配置控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 设置日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
