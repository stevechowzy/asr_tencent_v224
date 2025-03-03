## 常见问题解决方案

### 音频处理问题
1. **WAV文件头缺失**：
   ```python
   # 使用BytesIO创建完整WAV文件
   import wave
   import io

   def create_wav_header(data):
       buffer = io.BytesIO()
       with wave.open(buffer, 'wb') as wf:
           wf.setnchannels(1)
           wf.setsampwidth(2)
           wf.setframerate(16000)
           wf.writeframes(data)
       return buffer.getvalue()
   ```

### SDK错误处理
| 错误代码 | 解决方案 |
|---------|----------|
| FailedOperation.ServiceIsolate | 检查腾讯云账户余额 |
| InvalidParameterValue | 验证音频参数格式 |
| ResourceNotFound | 确认SecretId/Key有效性 |

### 性能优化
- 启用音频缓存池
- 使用线程池管理ASR请求 