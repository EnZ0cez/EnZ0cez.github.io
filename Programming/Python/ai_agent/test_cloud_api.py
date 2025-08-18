import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import (
    USE_OLLAMA, CLOUD_API_TYPE, CLOUD_API_KEY, CLOUD_BASE_URL, CLOUD_MODEL_NAME
)
from ai_analyzer import AIAnalyzer

def test_cloud_api():
    '''测试云端API功能'''
    print("=== 云端API测试 ===")
    print(f"USE_OLLAMA: {USE_OLLAMA}")
    print(f"CLOUD_API_TYPE: {CLOUD_API_TYPE}")
    print(f"CLOUD_API_KEY: {'*' * len(CLOUD_API_KEY) if CLOUD_API_KEY else '未设置'}")
    print(f"CLOUD_BASE_URL: {CLOUD_BASE_URL}")
    print(f"CLOUD_MODEL_NAME: {CLOUD_MODEL_NAME}")
    
    if USE_OLLAMA:
        print("\n当前配置为使用本地Ollama，无法测试云端API")
        return
    
    if not CLOUD_API_KEY:
        print("\n错误: 未设置CLOUD_API_KEY")
        return
    
    # 创建AIAnalyzer实例
    print("\n正在初始化AIAnalyzer...")
    try:
        ai_analyzer = AIAnalyzer()
        print("AIAnalyzer初始化成功")
        
        # 检查云端API是否正确初始化
        if hasattr(ai_analyzer, 'llm') and ai_analyzer.llm is not None:
            print("云端API客户端已初始化")
        else:
            print("云端API客户端未正确初始化")
            return
            
        # 测试简单的分析
        test_dynamics = [
            {
                "timestamp": "08-01 10:00",
                "content": "明天要去参加广州万菱汇重返未来1999快闪活动"
            },
            {
                "timestamp": "08-02 14:00",
                "content": "准备去上海明日方舟：集成映射展览"
            }
        ]
        
        print("\n正在测试分析功能...")
        result = ai_analyzer.analyze_schedule("测试博主", test_dynamics)
        print("\n分析结果:")
        print("=" * 50)
        print(result)
        
    except Exception as e:
        print(f"测试过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_cloud_api()