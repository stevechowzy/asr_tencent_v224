import logging
from datetime import datetime

def setup_logger():
    logger = logging.getLogger('ASR_APP')
    logger.setLevel(logging.DEBUG)
    
    # 文件日志
    file_handler = logging.FileHandler(
        f"logs/asr_{datetime.now().strftime('%Y%m%d')}.log"
    )
    file_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)

    # 控制台日志
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger 