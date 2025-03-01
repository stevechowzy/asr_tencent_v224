# 1. 创建自动化脚本（包含动态生成功能）
cat > $HOME/asr_daily_reminder.sh <<'EOF'
#!/bin/zsh

# 确保目录存在
mkdir -p "$HOME/Documents/asr_plans"

CURRENT_DATE=$(date +%Y-%m-%d)
prev_date=$(date -v-1d +%Y-%m-%d)
prev_file="$HOME/Documents/asr_plans/${prev_date}.md"
new_file="$HOME/Documents/asr_plans/${CURRENT_DATE}.md"

# 生成新文件头部
echo "# ASR 项目每日计划（${CURRENT_DATE}）" > "$new_file"

# 继承未完成的任务
echo "\n## 昨日进度" >> "$new_file"
if [ -f "$prev_file" ]; then
    awk '/^## 今日目标/{flag=1;next} /^## /{flag=0} flag' "$prev_file" | 
    grep -E '^- \[ ]' >> "$new_file"
else
    echo "- [ ] 无未完成工作" >> "$new_file"
fi

# 追加预设模板
cat <<EOF_INNER >> "$new_file"

## 今日目标
- [ ] 音频预处理模块开发
  - 格式自动转换
  - 采样率统一处理
- [ ] 命令行界面设计

## 会议记录
EOF_INNER

# 系统通知
osascript -e 'display notification "ASR 项目开发时间到！" with title "每日开发提醒" sound name "Ping"'

# 打开开发环境
open -a "Visual Studio Code" "$HOME/asr_tencent_v224"
EOF

# 2. 设置launchd定时任务
cat > $HOME/Library/LaunchAgents/com.asr.reminder.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.asr.reminder</string>
    <key>ProgramArguments</key>
    <array>
        <string>$HOME/asr_daily_reminder.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>10</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/asr_reminder.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/asr_reminder.err</string>
</dict>
</plist>
EOF

# 3. 设置权限
chmod +x $HOME/asr_daily_reminder.sh
chmod 644 $HOME/Library/LaunchAgents/com.asr.reminder.plist

# 4. 激活定时任务
launchctl load $HOME/Library/LaunchAgents/com.asr.reminder.plist
