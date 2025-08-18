import json
import time
import traceback
import requests
from datetime import datetime

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from config import (
    USE_OLLAMA, OLLAMA_URL, OLLAMA_MODEL, OLLAMA_STREAM,
    CLOUD_API_TYPE, CLOUD_API_KEY, CLOUD_BASE_URL, CLOUD_MODEL_NAME, CLOUD_STREAM
)

class AIAnalyzer:
    """AI分析和总结类"""
    
    def __init__(self):
        """初始化AI分析器"""
        # 创建Prompt模板
        self.prompt_template = PromptTemplate(
            input_variables=["blogger_name", "dynamics"],
            template="""
            你是一个专业的社交媒体分析师。请分析以下博主的社交媒体动态，并总结其近期的线下行程安排。

            博主名称: {blogger_name}
            
            社交媒体动态:
            {dynamics}
            
            请根据以上动态内容，总结该博主近期的线下行程安排。要求：
            1. 只提取与线下活动相关的信息
            2. 包括活动时间、地点、活动类型
            3. 如果没有线下活动信息，请明确说明
            4. 以简洁明了的方式呈现
            5. 按时间顺序排列
            
            请按照以下格式输出：
            
            博主 {blogger_name} 近期线下行程安排：
            
            [时间] [地点] [活动类型]
            [具体描述]
            
            [时间] [地点] [活动类型]
            [具体描述]
            
            ...
            
            总结：
            [总体总结]
            """
        )
        
        # 初始化云端API客户端（如果需要）
        self.llm = None
        self.chain = None
        if not USE_OLLAMA:
            self._init_cloud_api()
    
    def _init_cloud_api(self):
        """初始化云端API客户端"""
        try:
            print(f"正在初始化云端API: type={CLOUD_API_TYPE}, model={CLOUD_MODEL_NAME}, stream={CLOUD_STREAM}")
            if CLOUD_API_TYPE == "openai" or CLOUD_API_TYPE == "dashscope":
                # 使用Langchain的ChatOpenAI来支持OpenAI兼容的API
                # 创建一个禁用代理的HTTP客户端
                from openai import OpenAI
                import httpx
                
                # 创建禁用代理的httpx客户端
                http_client = httpx.Client(
                    trust_env=False  # 禁用环境变量中的代理设置
                )
                
                self.llm = ChatOpenAI(
                    openai_api_key=CLOUD_API_KEY,
                    openai_api_base=CLOUD_BASE_URL,
                    model_name=CLOUD_MODEL_NAME,
                    temperature=0.7,
                    request_timeout=30,
                    http_client=http_client,  # 使用自定义HTTP客户端
                    streaming=CLOUD_STREAM  # 启用流式模式
                )
                self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
                print("云端API初始化成功")
            else:
                raise ValueError(f"不支持的云端API类型: {CLOUD_API_TYPE}")
        except Exception as e:
            print(f"初始化云端API失败: {e}")
            traceback.print_exc()
            raise
    
    def analyze_schedule(self, blogger_name, dynamics):
        """
        分析博主的线下行程
        
        Args:
            blogger_name (str): 博主名称
            dynamics (list): 动态列表
            
        Returns:
            str: 行程总结
        """
        # 将动态内容转换为文本
        dynamics_text = "\n\n".join([
            f"时间: {dynamic.get('timestamp', dynamic.get('created_at', '未知'))}\n内容: {dynamic.get('content', dynamic.get('text', '无内容'))}"
            for dynamic in dynamics
        ])

        # 生成用于模型的完整 prompt 文本（直接使用 prompt_template 的模板）
        try:
            prompt_text = self.prompt_template.template.format(blogger_name=blogger_name, dynamics=dynamics_text)
        except Exception:
            # 保险回退：手工拼接
            prompt_text = f"博主名称: {blogger_name}\n\n社交媒体动态:\n{dynamics_text}"

        # 重试策略：最多尝试3次，指数退避，每次增加超时时间
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                # 设置超时时间
                timeout_seconds = 30 * attempt
                
                result = None
                
                # 根据配置选择使用本地Ollama还是云端API
                if USE_OLLAMA:
                    # 使用本地 Ollama 模型
                    print("正在调用本地Ollama模型...")
                    result = self.ollama_generate(prompt_text, timeout=timeout_seconds)
                else:
                    # 使用云端 API
                    print("正在调用云端API...")
                    print(f"  API类型: {CLOUD_API_TYPE}")
                    print(f"  模型名称: {CLOUD_MODEL_NAME}")
                    print(f"  API基础URL: {CLOUD_BASE_URL}")
                    
                    if self.chain is not None:
                        try:
                            result = self.chain.invoke({
                                "blogger_name": blogger_name,
                                "dynamics": dynamics_text
                            })
                            print("云端API调用成功")
                        except Exception as e:
                            print(f"云端API调用失败: {e}")
                            print("错误详情:")
                            traceback.print_exc()
                            result = None
                    else:
                        print("云端API未正确初始化")
                        result = None

                if isinstance(result, dict):
                    # langchain 有时返回带 key 的 dict
                    result = result.get("text") or result.get("content") or ""

                return result

            except Exception as e:
                # 简洁信息 + 详细回溯
                err_msg = str(e)
                print(f"AI分析错误 (尝试 {attempt}/{max_attempts}): {err_msg}")
                traceback.print_exc()

                # 常见超时提示
                if "timed out" in err_msg.lower() or "timeout" in err_msg.lower() or "readtimeout" in err_msg.lower():
                    if USE_OLLAMA:
                        print("提示: 请求超时。请检查Ollama服务是否运行正常，或增大 request_timeout。")
                    else:
                        print("提示: 请求超时。请检查网络连接或API服务状态。")

                # 如果不是最后一次，则等待后重试
                if attempt < max_attempts:
                    backoff = 2 ** (attempt - 1)
                    print(f"将在 {backoff}s 后重试...")
                    time.sleep(backoff)
                    continue
                else:
                    return f"分析失败: {err_msg} (已重试 {max_attempts} 次)"

    def ollama_generate(self, prompt_text, timeout=30):
        """调用本地 Ollama 服务生成文本。返回生成的字符串或抛出异常。"""
        url = OLLAMA_URL.rstrip('/') + '/api/generate'
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt_text,
            "max_tokens": 1024,
            "temperature": 0.7,
            "stream": False
        }
        headers = {"Content-Type": "application/json"}
        
        # 打印调试信息
        print(f"发送到Ollama的prompt: {prompt_text[:200]}...")  # 只打印前200个字符

        resp = requests.post(url, json=payload, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            raise Exception(f"Ollama 返回状态码 {resp.status_code}: {resp.text}")

        j = resp.json()
        # 优先提取常见的文本字段，返回纯文本
        if isinstance(j, dict):
            # 直接的 response 字段（你示例中使用的是 response）
            if 'response' in j and isinstance(j['response'], str):
                return j['response']

            # 常见的 results -> content -> output_text
            if 'results' in j:
                parts = []
                for r in j.get('results', []):
                    for c in r.get('content', []):
                        if isinstance(c, dict) and c.get('type') in ('output_text', 'text'):
                            parts.append(c.get('text', ''))
                        elif isinstance(c, str):
                            parts.append(c)
                if parts:
                    return ''.join(parts)

            # 直接的 text 字段
            if 'text' in j and isinstance(j['text'], str):
                return j['text']

            # choices 格式（类似 OpenAI）
            if 'choices' in j and isinstance(j['choices'], list) and len(j['choices']) > 0:
                first = j['choices'][0]
                # gpt-style
                if isinstance(first, dict):
                    if 'message' in first and isinstance(first['message'], dict) and 'content' in first['message']:
                        content = first['message']['content']
                        if isinstance(content, str):
                            return content
                    if 'text' in first and isinstance(first['text'], str):
                        return first['text']

            # generated_text 回退
            if 'generated_text' in j and isinstance(j['generated_text'], str):
                return j['generated_text']

        # 最后回退：把整个 json 转为文本
        try:
            return json.dumps(j, ensure_ascii=False)
        except Exception:
            return str(j)