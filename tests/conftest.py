import os
import sys

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 创建测试数据目录
os.makedirs('test_data', exist_ok=True) 