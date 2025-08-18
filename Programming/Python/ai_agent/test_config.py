import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import (
    USE_OLLAMA, OLLAMA_URL, OLLAMA_MODEL, OLLAMA_STREAM,
    CLOUD_API_TYPE, CLOUD_API_KEY, CLOUD_BASE_URL, CLOUD_MODEL_NAME
)

def test_config():
    """测试配置加载"""
    print("=== 配置信息 ===")
    print(f"USE_OLLAMA: {USE_OLLAMA}")
    print(f"OLLAMA_URL: {OLLAMA_URL}")
    print(f"OLLAMA_MODEL: {OLLAMA_MODEL}")
    print(f"OLLAMA_STREAM: {OLLAMA_STREAM}")
    print(f"CLOUD_API_TYPE: {CLOUD_API_TYPE}")
    print(f"CLOUD_API_KEY: {'*' * len(CLOUD_API_KEY) if CLOUD_API_KEY else ''}")
    print(f"CLOUD_BASE_URL: {CLOUD_BASE_URL}")
    print(f"CLOUD_MODEL_NAME: {CLOUD_MODEL_NAME}")
    
    # 检查当前工作目录
    print(f"\n=== 路径信息 ===")
    print(f"当前工作目录: {os.getcwd()}")
    print(f"脚本目录: {os.path.dirname(os.path.abspath(__file__))}")
    
    # 检查.env文件是否存在
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    print(f".env文件路径: {env_path}")
    print(f".env文件存在: {os.path.exists(env_path)}")
    
    # 如果.env文件存在，读取并显示内容
    if os.path.exists(env_path):
        print("\n=== .env文件内容 ===")
        with open(env_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)

if __name__ == "__main__":
    test_config()