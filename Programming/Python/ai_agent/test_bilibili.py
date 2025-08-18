import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bilibili_scraper import BilibiliScraper

def test_bilibili_scraper():
    # 测试B站动态获取功能
    # 创建B站爬虫实例
    scraper = BilibiliScraper()
    
    # 测试用户UID（这里使用浅九ninth的UID）
    test_uid = 365654312
    
    print(f"正在测试获取B站用户 {test_uid} 的动态...")
    
    # 获取用户信息
    print("正在获取用户信息...")
    user_info = scraper.get_user_info(test_uid)
    if user_info:
        print(f"用户信息获取成功:")
        print(f"  ID: {user_info['id']}")
        print(f"  名称: {user_info['name']}")
        print(f"  签名: {user_info['sign']}")
        print(f"  等级: {user_info['level']}")
        print(f"  粉丝数: {user_info['follower_count']}")
    else:
        print("用户信息获取失败")
    
    # 获取用户动态
    print("\n正在获取用户动态...")
    dynamics = scraper.get_user_dynamic(test_uid, max_pages=2)  # 只获取前2页
    if dynamics:
        print(f"成功获取到 {len(dynamics)} 条动态")
        # 显示前3条动态作为示例
        for i, dynamic in enumerate(dynamics[:3]):
            print(f"\n动态 {i+1}:")
            print(f"  ID: {dynamic['id']}")
            print(f"  类型: {dynamic['type']}")
            print(f"  时间: {dynamic['timestamp']}")
            content = dynamic['content']
            if content and len(content) > 100:
                print(f"  内容: {content[:100]}...")
            else:
                print(f"  内容: {content}")
    else:
        print("动态获取失败")

if __name__ == "__main__":
    test_bilibili_scraper()