# 云端API配置说明

## 支持的云端API平台

本项目支持以下云端API平台：
1. 阿里云百炼平台 (dashscope)
2. OpenAI兼容的API (openai)

## 配置步骤

### 1. 获取API密钥
- **阿里云百炼**: 访问 https://dashscope.console.aliyun.com/ 注册账号并获取API密钥
- **OpenAI**: 访问 https://platform.openai.com/ 注册账号并获取API密钥

### 2. 修改.env文件配置

在 `.env` 文件中设置以下参数：

```
# 选择使用本地Ollama还是云端API
# 设置为true使用本地Ollama，设置为false使用云端API
USE_OLLAMA=false

# === 云端API配置（当 USE_OLLAMA=false 时使用） ===
# 云端API类型：openai（OpenAI/Claude等兼容API）或 dashscope（阿里云百炼）
CLOUD_API_TYPE=dashscope
# 云端API密钥（替换为你的实际密钥）
CLOUD_API_KEY=your_actual_api_key_here
# 云端API基础URL（阿里云百炼示例）
CLOUD_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
# 模型名称（阿里云百炼常用模型：qwen-plus, qwen-turbo, qwen-max）
CLOUD_MODEL_NAME=qwen-plus
# 是否使用流式输出模式（某些模型需要启用流式模式）
CLOUD_STREAM=false
```

### 3. 常见问题及解决方案

#### 问题1：连接错误（ProxyError）
**现象**: 出现 `ProxyError('Unable to connect to proxy', FileNotFoundError(2, 'No such file or directory'))`
**解决方案**: 
- 检查系统代理设置是否正确
- 或在代码中禁用代理（已默认处理）

#### 问题2：认证错误（401 Unauthorized）
**现象**: 出现 `Incorrect API key provided`
**解决方案**: 
- 检查API密钥是否正确
- 确认API密钥未过期

#### 问题3：模型不存在错误
**现象**: 出现 `The model does not exist`
**解决方案**: 
- 检查模型名称是否正确
- 确认该模型在所选平台上可用

#### 问题4：流式模式错误
**现象**: 出现 `This model only support stream mode`
**解决方案**: 
- 将 `CLOUD_STREAM=true` 设置为启用流式模式

### 4. 阿里云百炼平台常用模型

- `qwen-turbo`: 快速响应，适合简单任务
- `qwen-plus`: 平衡性能和成本，推荐使用
- `qwen-max`: 最高性能，适合复杂任务
- `glm-4.5`: 需要启用流式模式 (`CLOUD_STREAM=true`)

### 5. 测试配置

可以运行以下命令测试配置是否正确：
```bash
python test_cloud_api.py
```

或者运行主程序：
```bash
python main.py
```