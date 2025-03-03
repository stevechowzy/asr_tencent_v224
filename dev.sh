#!/bin/zsh
# ASR项目开发环境设置

# 1. 导航至项目目录
cd ~/asr_tencent_v224

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 检查并安装依赖
pip install -r requirements.txt --no-warn-script-location

# 4. 打开 VSCode
code .

# 5. 显示项目状态
echo "=== ASR 项目开发环境 ==="
echo "Python 虚拟环境: 已激活"
echo "依赖检查: 已完成"
echo "编辑器: VSCode 已启动"
