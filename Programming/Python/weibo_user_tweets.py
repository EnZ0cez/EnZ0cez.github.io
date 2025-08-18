import urllib.request
import urllib.parse
import json
import time
import re
import ssl
import gzip
from io import BytesIO
import os
from datetime import datetime

# 创建不验证SSL证书的上下文（仅用于测试，生产环境中应谨慎使用）
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

class WeiboAPI:
    def __init__(self):
        """
        初始化微博API客户端
        """
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://m.weibo.cn/',
        }
    
    def _make_request(self, url, params=None):
        """
        发起HTTP请求
        
        Args:
            url (str): 请求URL
            params (dict): 请求参数
            
        Returns:
            dict: 响应数据
        """
        try:
            # 构造完整URL
            if params:
                query_string = urllib.parse.urlencode(params)
                full_url = f"{url}?{query_string}"
            else:
                full_url = url
            
            print(f"正在请求: {full_url}")
            
            # 创建请求对象
            req = urllib.request.Request(full_url, headers=self.headers)
            
            # 发起请求
            response = urllib.request.urlopen(req, context=ssl_context, timeout=10)
            
            # 读取响应数据
            data = response.read()
            
            # 检查内容编码并解压
            content_encoding = response.headers.get('Content-Encoding')
            if content_encoding == 'gzip':
                print("检测到gzip压缩，正在解压...")
                data = gzip.decompress(data)
            
            # 解码并解析JSON
            json_data = json.loads(data.decode('utf-8'))
            
            print(f"响应状态码: {response.getcode()}")
            return json_data
            
        except Exception as e:
            print(f"请求错误: {e}")
            return None
    
    def get_user_info(self, uid):
        """
        获取用户信息
        
        Args:
            uid (str): 用户ID
            
        Returns:
            dict: 用户信息
        """
        url = "https://m.weibo.cn/api/container/getIndex"
        params = {
            'type': 'uid',
            'value': uid
        }
        
        try:
            data = self._make_request(url, params)
            
            if data and data.get('ok') == 1:
                user_info = data.get('data', {}).get('userInfo', {})
                return {
                    'id': user_info.get('id'),
                    'screen_name': user_info.get('screen_name'),
                    'description': user_info.get('description'),
                    'followers_count': user_info.get('followers_count'),
                    'follow_count': user_info.get('follow_count'),
                    'statuses_count': user_info.get('statuses_count')
                }
            else:
                print(f"获取用户信息失败: {data.get('msg', '未知错误') if data else '无响应数据'}")
                return None
                
        except Exception as e:
            print(f"解析错误: {e}")
            return None
    
    def get_user_tweets(self, uid, page=1):
        """
        获取用户微博动态
        
        Args:
            uid (str): 用户ID
            page (int): 页码
            
        Returns:
            list: 微博动态列表
        """
        # 首先获取用户主页信息，获取containerid
        user_url = "https://m.weibo.cn/api/container/getIndex"
        user_params = {
            'type': 'uid',
            'value': uid
        }
        
        try:
            user_data = self._make_request(user_url, user_params)
            
            if not user_data or user_data.get('ok') != 1:
                print(f"获取用户信息失败: {user_data.get('msg', '未知错误') if user_data else '无响应数据'}")
                return None
                
            # 获取containerid
            tabs = user_data.get('data', {}).get('tabsInfo', {}).get('tabs', [])
            containerid = None
            for tab in tabs:
                if tab.get('tab_type') == 'weibo':
                    containerid = tab.get('containerid')
                    break
            
            if not containerid:
                print("未找到微博动态containerid")
                return None
                
            # 获取微博动态
            tweets_url = "https://m.weibo.cn/api/container/getIndex"
            tweets_params = {
                'containerid': containerid,
                'page': page
            }
            
            tweets_data = self._make_request(tweets_url, tweets_params)
            
            if tweets_data and tweets_data.get('ok') == 1:
                cards = tweets_data.get('data', {}).get('cards', [])
                tweets = []
                
                for card in cards:
                    # 只处理微博动态卡片
                    if card.get('card_type') == 9:
                        mblog = card.get('mblog', {})
                        tweet = {
                            'id': mblog.get('id'),
                            'created_at': mblog.get('created_at'),
                            'text': self._clean_html_tags(mblog.get('text', '')),
                            'reposts_count': mblog.get('reposts_count'),
                            'comments_count': mblog.get('comments_count'),
                            'attitudes_count': mblog.get('attitudes_count'),
                            'source': mblog.get('source')
                        }
                        tweets.append(tweet)
                
                return tweets
            else:
                print(f"获取微博动态失败: {tweets_data.get('msg', '未知错误') if tweets_data else '无响应数据'}")
                return None
                
        except Exception as e:
            print(f"解析错误: {e}")
            return None
    
    def _clean_html_tags(self, text):
        """
        清理HTML标签
        
        Args:
            text (str): 包含HTML标签的文本
            
        Returns:
            str: 清理后的文本
        """
        # 移除HTML标签
        clean_text = re.sub(r'<[^>]+>', '', text)
        # 处理HTML实体
        clean_text = re.sub(r'&nbsp;', ' ', clean_text)
        clean_text = re.sub(r'&lt;', '<', clean_text)
        clean_text = re.sub(r'&gt;', '>', clean_text)
        clean_text = re.sub(r'&amp;', '&', clean_text)
        return clean_text.strip()

def save_to_json(data, filename):
    """
    将数据保存到JSON文件
    
    Args:
        data (dict): 要保存的数据
        filename (str): 文件名
    """
    try:
        # 确保文件路径存在
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # 保存数据到JSON文件
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已保存到 {filename}")
    except Exception as e:
        print(f"保存数据到JSON文件时出错: {e}")

def test_network():
    """
    测试网络连接
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        req = urllib.request.Request('https://httpbin.org/get', headers=headers)
        response = urllib.request.urlopen(req, context=ssl_context, timeout=5)
        
        print("网络连接测试成功")
        print(f"响应状态码: {response.getcode()}")
        return True
    except Exception as e:
        print(f"网络连接测试失败: {e}")
        return False

def main():
    """
    主函数，演示如何使用WeiboAPI获取用户微博动态并保存到JSON文件
    """
    # 测试网络连接
    print("正在测试网络连接...")
    # 暂时跳过网络测试，因为可能存在系统级代理问题
    # if not test_network():
    #     print("网络连接失败，请检查网络设置")
    #     return
    
    # 创建WeiboAPI实例
    weibo_api = WeiboAPI()
    
    # 用户ID（需要替换为实际的用户ID）
    # 这里使用的是微博官方账号的ID作为示例
    user_id = "6413437934"
    
    # 获取用户信息
    print("正在获取用户信息...")
    user_info = weibo_api.get_user_info(user_id)
    
    if user_info:
        print("用户信息:")
        print(f"昵称: {user_info['screen_name']}")
        print(f"简介: {user_info['description']}")
        print(f"粉丝数: {user_info['followers_count']}")
        print(f"关注数: {user_info['follow_count']}")
        print(f"微博数: {user_info['statuses_count']}")
        print("-" * 50)
    else:
        print("获取用户信息失败")
        return
    
    # 获取用户微博动态
    print("正在获取用户微博动态...")
    tweets = weibo_api.get_user_tweets(user_id, page=1)
    
    if tweets:
        print(f"获取到 {len(tweets)} 条微博动态:")
        print("-" * 50)
        
        # 创建要保存的数据结构
        data_to_save = {
            "user_info": user_info,
            "tweets": tweets,
            "fetch_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # 生成文件名
        filename = f"data/weibo_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # 保存数据到JSON文件
        save_to_json(data_to_save, filename)
        
        # 打印前几条微博动态作为示例
        for i, tweet in enumerate(tweets[:3], 1):  # 只显示前3条
            print(f"微博 {i}:")
            print(f"发布时间: {tweet['created_at']}")
            print(f"内容: {tweet['text'][:100]}{'...' if len(tweet['text']) > 100 else ''}")
            print(f"转发数: {tweet['reposts_count']}")
            print(f"评论数: {tweet['comments_count']}")
            print(f"点赞数: {tweet['attitudes_count']}")
            print(f"来源: {tweet['source']}")
            print("-" * 30)
            
        if len(tweets) > 3:
            print(f"... 还有 {len(tweets) - 3} 条微博动态")
    else:
        print("获取微博动态失败")

if __name__ == "__main__":
    main()