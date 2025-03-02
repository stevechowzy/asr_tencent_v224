# 腾讯云语音识别应用

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

基于腾讯云ASR API实现的语音转文字工具，支持长音频自动分段处理。

## 功能特性

- 🎙️ 支持常见音频格式转换（MP3/WAV等）
- ⚡ 实时语音识别（60秒内音频）
- 🔄 自动分块处理长音频
- 🔒 安全凭证管理（.env文件）

## 快速开始

### 前置要求

- Python 3.8+
- 腾讯云账号（获取SecretId/SecretKey）
- FFmpeg（音频处理依赖）

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourname/asr-tencent-project.git

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.sample .env
```

### 使用说明

#### 环境配置
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 安装音频依赖
brew install portaudio  # macOS
sudo apt-get install portaudio19-dev  # Linux
```

#### 配置文件
创建 `.env` 文件：
```ini
TENCENT_SECRET_ID=your_secret_id
TENCENT_SECRET_KEY=your_secret_key
```

#### 运行方式
```bash
# 文件模式
python asr_app.py audio.wav

# 实时模式
python asr_app.py
选择模式2
```

## 开发指南

### 项目结构
