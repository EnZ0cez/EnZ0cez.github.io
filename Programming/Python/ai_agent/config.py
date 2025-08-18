import os
from dotenv import load_dotenv
from dotenv import find_dotenv

# 加载环境变量
dotenv_path = find_dotenv()
if dotenv_path:
	load_dotenv(dotenv_path)
else:
	# fallback: .env next to this file
	env_file = os.path.join(os.path.dirname(__file__), ".env")
	if os.path.exists(env_file):
		load_dotenv(env_file)

# API选择配置
# USE_OLLAMA: 开启本地 Ollama 模式（true/1/yes）
USE_OLLAMA = os.getenv("USE_OLLAMA", "true").lower() in ("1", "true", "yes")

# Ollama 本地模型配置（当 USE_OLLAMA=true 时使用）
# 本地 Ollama 服务地址，默认本机 11434 端口
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
# 要使用的本地模型名称（例如 llama2、qwen或其他已安装模型）
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:270m")
# 是否使用 Ollama 的流式输出（stream）。可在 .env 中设置为 true/false
OLLAMA_STREAM = os.getenv("OLLAMA_STREAM", "false").lower() in ("1", "true", "yes")

# 云端API配置（当 USE_OLLAMA=false 时使用）
# 支持多种云端API，如阿里云百炼、OpenAI等
CLOUD_API_TYPE = os.getenv("CLOUD_API_TYPE", "openai")  # 可选: openai, dashscope
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY", "")
CLOUD_BASE_URL = os.getenv("CLOUD_BASE_URL", "")  # 例如: https://dashscope.aliyuncs.com/compatible-mode/v1
CLOUD_MODEL_NAME = os.getenv("CLOUD_MODEL_NAME", "qwen-plus")  # 例如: qwen-plus, gpt-3.5-turbo
# 是否使用流式输出模式
CLOUD_STREAM = os.getenv("CLOUD_STREAM", "false").lower() in ("1", "true", "yes")

# 其他配置
DATA_DIR = "data"