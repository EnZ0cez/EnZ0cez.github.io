import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import USE_OLLAMA
from ai_analyzer import AIAnalyzer

def test_api_selection():
    """测试API选择功能"""
    if USE_OLLAMA:
        print("当前配置为使用本地Ollama模型")
    else:
        print("当前配置为使用云端API")
    
    # 创建AIAnalyzer实例
    ai_analyzer = AIAnalyzer()
    
    # 检查初始化状态
    if hasattr(ai_analyzer, 'llm') and ai_analyzer.llm is not None:
        print("云端API客户端已初始化")
    else:
        print("云端API客户端未初始化或使用本地Ollama")

if __name__ == "__main__":
    test_api_selection()