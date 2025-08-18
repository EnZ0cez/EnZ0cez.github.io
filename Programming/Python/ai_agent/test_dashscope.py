import requests
import json
import os

# 从环境变量获取配置
api_key = os.environ.get('CLOUD_API_KEY') or 'your_api_key_here'
base_url = os.environ.get('CLOUD_BASE_URL') or 'https://dashscope.aliyuncs.com/compatible-mode/v1'
model_name = os.environ.get('CLOUD_MODEL_NAME') or 'qwen-plus'

def test_dashscope_api():
    '''测试阿里云百炼API连接'''
    print("=== 阿里云百炼API连接测试 ===")
    print(f"API密钥: {'*' * len(api_key) if api_key != 'your_api_key_here' else '未设置'}")
    print(f"基础URL: {base_url}")
    print(f"模型名称: {model_name}")
    
    # 构造测试请求
    url = f"{base_url}/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": "你好，这只是一个简单的测试。"}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    print(f"\n正在发送测试请求到: {url}")
    
    # 禁用代理的会话
    session = requests.Session()
    session.trust_env = False  # 禁用环境变量中的代理设置
    
    try:
        response = session.post(url, headers=headers, json=payload, timeout=30)
        print(f"响应状态码: {response.status_code}")
        if response.status_code == 200:
            print("API连接测试成功！")
            print(f"响应内容: {response.text[:200]}...")  # 只显示前200个字符
        else:
            print("API连接测试失败！")
            print(f"错误响应: {response.text}")
            
    except Exception as e:
        print(f"请求过程中出现错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_dashscope_api()