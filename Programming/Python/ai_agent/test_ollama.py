import sys
import os
import json

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_analyzer import AIAnalyzer

def test_ollama_analysis():
    """测试Ollama分析功能"""
    # 读取测试数据
    test_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'bilibili_dynamics_2.json')
    # 如果上面的路径不正确，尝试直接在项目根目录查找
    if not os.path.exists(test_data_path):
        test_data_path = 'bilibili_dynamics_2.json'
    
    with open(test_data_path, 'r', encoding='utf-8') as f:
        dynamics = json.load(f)
    
    # 创建AIAnalyzer实例
    ai_analyzer = AIAnalyzer()
    
    # 测试分析
    print("正在分析动态数据...")
    result = ai_analyzer.analyze_schedule("测试博主", dynamics[:5])  # 只取前5条动态进行测试
    
    print("\n分析结果:")
    print("=" * 50)
    print(result)

if __name__ == "__main__":
    test_ollama_analysis()