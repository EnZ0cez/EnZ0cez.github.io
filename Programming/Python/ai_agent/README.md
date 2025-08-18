# AI Agent项目

这个项目实现了一个AI Agent，能够：
1. 从输入的博主ID列表获取B站UID和微博ID
2. 获取这些博主的动态内容
3. 根据动态内容总结博主近期的线下行程

## 项目结构

- `main.py` - 主程序入口
- `blogger_manager.py` - 博主ID管理模块
- `bilibili_scraper.py` - B站动态获取模块
- `weibo_scraper.py` - 微博动态获取模块（复用现有代码）
- `ai_analyzer.py` - AI分析和总结模块
- `config.py` - 配置文件
- `requirements.txt` - 依赖包列表
- `.env` - 环境变量配置文件

## 功能模块说明

### BloggerManager (blogger_manager.py)
管理博主ID信息，包括B站UID和微博ID的映射关系。

### BilibiliScraper (bilibili_scraper.py)
负责从B站获取用户动态信息。

### WeiboScraper (weibo_scraper.py)
负责从微博获取用户动态信息。

### AIAnalyzer (ai_analyzer.py)
使用本地Ollama模型或云端API（如阿里云百炼、OpenAI等）分析动态内容，总结博主的线下行程安排。

## 配置说明

在使用之前，需要在`.env`文件中配置使用本地Ollama还是云端API：

### 选项1：使用本地Ollama（推荐）
```
USE_OLLAMA=true
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=your_preferred_model
```

确保已安装并运行Ollama服务，并且已拉取所需的模型。

### 选项2：使用云端API
```
USE_OLLAMA=false
CLOUD_API_TYPE=dashscope  # 或 openai
CLOUD_API_KEY=your_api_key_here
CLOUD_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
CLOUD_MODEL_NAME=qwen-plus
```

支持多种云端API：
- 阿里云百炼平台（dashscope）
- OpenAI兼容的API（openai）

## 使用方法

1. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

2. 选择AI模型提供方式：

   ### 方式一：使用本地Ollama（推荐）
   - 访问 https://ollama.ai 下载并安装Ollama
   - 运行Ollama服务
   - 拉取所需的模型，例如：`ollama pull gemma3:270m`

   ### 方式二：使用云端API
   - 获取相应平台的API密钥（如阿里云百炼、OpenAI等）
   - 确保网络可以访问对应的API服务
   - 详细配置说明请参考 [CLOUD_API_GUIDE.md](CLOUD_API_GUIDE.md)

3. 配置模型设置：
   编辑`.env`文件，根据选择的方式设置相应参数：
   - 使用本地Ollama：设置`USE_OLLAMA=true`并配置Ollama相关参数
   - 使用云端API：设置`USE_OLLAMA=false`并配置云端API相关参数

4. 运行程序：
   ```
   python main.py
   ```

## 自定义博主列表

要分析特定的博主列表，需要修改`main.py`文件中的博主添加部分：
```python
# 添加示例博主（实际使用时应从输入获取）
blogger_manager.add_blogger("博主名称", bilibili_uid="B站UID", weibo_id="微博ID")
```

## 注意事项

1. 如果使用本地Ollama，需要安装并运行Ollama服务
2. 如果使用云端API，需要有效的API密钥和网络连接
3. 请确保已拉取并配置了合适的模型
4. 请遵守各平台的使用条款，不要频繁请求数据
5. B站和微博的API可能会有变化，需要根据实际情况调整代码