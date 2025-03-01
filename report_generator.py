from datetime import datetime

def generate_daily_report():
    return f"""
# 腾讯云ASR开发日报 {datetime.today().strftime('%Y-%m-%d')}
## 当前进展
- [ ] 核心语音处理模块完成度:75%
- [ ] API调用成功率:{get_api_success_rate()}%

## 今日重点
{open('resume_dev.sh').readlines()[15].strip().split('echo ')[1]}
"""

# 在resume_dev.sh末尾追加
echo "生成今日报告..."
python3 report_generator.py >> $LOG_PATH 