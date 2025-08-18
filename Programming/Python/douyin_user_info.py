import requests
from bs4 import BeautifulSoup
from douyin_tiktok_scraper.scraper import Scraper

def get_douyin_user_info(user_id):
    """
    获取抖音用户主页信息
    
    Args:
        user_id (str): 抖音用户ID
        
    Returns:
        dict: 包含用户信息的字典
    """
    # 抖音用户主页URL
    url = f"https://www.douyin.com/user/{user_id}"
    
    # 设置请求头，模拟浏览器访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }
    
    try:
        # 发送GET请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取用户信息（注意：抖音页面结构可能会变化，以下选择器可能需要调整）
        # 用户名
        username_elem = soup.find('h1', {'class': 'user-title'})
        username = username_elem.text.strip() if username_elem else "未找到用户名"
        
        # 简介
        desc_elem = soup.find('p', {'class': 'user-desc'})
        description = desc_elem.text.strip() if desc_elem else "未找到简介"
        
        # 关注数
        follow_elem = soup.find('span', {'class': 'follow-count'})
        follow_count = follow_elem.text.strip() if follow_elem else "未找到关注数"
        
        # 粉丝数
        follower_elem = soup.find('span', {'class': 'follower-count'})
        follower_count = follower_elem.text.strip() if follower_elem else "未找到粉丝数"
        
        # 获赞数
        like_elem = soup.find('span', {'class': 'like-count'})
        like_count = like_elem.text.strip() if like_elem else "未找到获赞数"
        
        # 返回用户信息字典
        return {
            "username": username,
            "description": description,
            "follow_count": follow_count,
            "follower_count": follower_count,
            "like_count": like_count
        }
        
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None
    except Exception as e:
        print(f"解析错误: {e}")
        return None

# 示例用法
if __name__ == "__main__":
    # 这里需要替换为实际的抖音用户ID
    # 注意：直接使用网页URL中的ID可能无法工作，因为抖音有反爬虫机制
    user_id = "MS4wLjABAAAA6HbMv58OBeuWT8NnuFkqrVzDZUmhHWhorr8vI_W51AE"
    user_info = get_douyin_user_info(user_id)
    
    if user_info:
        print("抖音用户信息:")
        print(f"用户名: {user_info['username']}")
        print(f"简介: {user_info['description']}")
        print(f"关注数: {user_info['follow_count']}")
        print(f"粉丝数: {user_info['follower_count']}")
        print(f"获赞数: {user_info['like_count']}")
    else:
        print("获取用户信息失败")