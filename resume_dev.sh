# 在现有脚本中添加以下功能

# 7. 同步开发日志到Cursor聊天记录
LOG_PATH="$HOME/asr_tencent_v224/chat_logs/$(date +%Y%m%d).log"
echo "[$(date +%H:%M)] 项目启动" >> $LOG_PATH

# 8. 自动关联腾讯云凭证（安全存储）
export TENCENTCLOUD_SECRET_ID="您的API_ID"
export TENCENTCLOUD_SECRET_KEY="您的API_KEY" 