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

```bash
# 识别单个音频文件
python src/asr_app.py "path/to/audio.wav"

# 示例输出
音频文件大小: 256 KB
识别结果: 你好，欢迎使用语音识别系统...
```

## 开发指南

### 项目结构
