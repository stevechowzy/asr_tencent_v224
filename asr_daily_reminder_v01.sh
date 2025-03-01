cat > $HOME/asr_daily_reminder.sh <<'EOF'
#!/bin/zsh

DAILY_LOG="$HOME/Documents/asr_daily_log.md"
CURRENT_DATE=$(date +%Y-%m-%d)
prev_date=$(date -v-1d +%Y-%m-%d)

# 创建文件（如果不存在）并添加初始标记
[ -f "$DAILY_LOG" ] || echo "# ASR 项目日志档案\n" > "$DAILY_LOG"

# 分割线 + 新日期标题
echo -e "\n## --- [${CURRENT_DATE}] ---" >> "$DAILY_LOG"

# 自动继承昨日未完成任务
echo "### 昨日进度" >> "$DAILY_LOG"
if grep -q "## --- \[${prev_date}\]" "$DAILY_LOG"; then
    awk -v prev="## --- \\[${prev_date}\\]" '
        $0 ~ prev {flag=1; next}
        flag && /^### 今日目标/ {task=1; next}
        flag && task && /^### / {exit}
        flag && task {print}
    ' "$DAILY_LOG" | grep -E '^- \[ ]' >> "$DAILY_LOG"
else
    echo "- [ ] 无昨日未完成任务" >> "$DAILY_LOG"
fi

# 添加今日模板
cat <<EOF_INNER >> "$DAILY_LOG"

### 今日目标
- [ ] 音频预处理模块开发
  - 格式自动转换
  - 采样率统一处理
- [ ] 命令行界面设计

### 会议记录
EOF_INNER

# 系统通知
osascript -e 'display notification "ASR 项目开发时间到！" with title "每日开发提醒" sound name "Ping"'

# 打开开发环境和日志文件
open -a "Visual Studio Code" "$HOME/asr_tencent_v224"
open -a "Visual Studio Code" "$DAILY_LOG"
EOF
