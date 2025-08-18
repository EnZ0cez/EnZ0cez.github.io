import os
import sys
import json
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import USE_OLLAMA, CLOUD_API_KEY
from blogger_manager import BloggerManager
from bilibili_scraper import BilibiliScraper
from weibo_scraper import WeiboScraper
from ai_analyzer import AIAnalyzer

def convert_bilibili_dynamics(bilibili_dynamics):
    """转换B站动态数据格式以匹配微博动态格式"""
    converted_dynamics = []
    
    for dynamic in bilibili_dynamics:
        # 转换时间戳为微博格式
        timestamp = dynamic.get('timestamp', '')
        if timestamp:
            # 将 'YYYY-MM-DD HH:MM:SS' 转换为微博的 'MM-DD HH:MM' 格式
            try:
                dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                timestamp = dt.strftime('%m-%d %H:%M')
            except ValueError:
                pass  # 如果转换失败，保持原样
        
        converted_dynamic = {
            'id': dynamic.get('id'),
            'created_at': timestamp,
            'text': dynamic.get('content', ''),
            'reposts_count': 0,  # B站动态不提供这些信息
            'comments_count': 0,
            'attitudes_count': 0
        }
        converted_dynamics.append(converted_dynamic)
    
    return converted_dynamics

def main():
    """主函数"""
    # 检查API配置
    if USE_OLLAMA:
        print("使用本地Ollama模型进行分析")
    else:
        if not CLOUD_API_KEY:
            print("错误: 请在.env文件中设置CLOUD_API_KEY")
            return
        print(f"使用云端API进行分析 (类型: {os.getenv('CLOUD_API_TYPE', 'unknown')})")
    
    # 初始化各个模块
    blogger_manager = BloggerManager()
    bilibili_scraper = BilibiliScraper()
    weibo_scraper = WeiboScraper()
    ai_analyzer = AIAnalyzer()  # 不再需要传递API密钥
    
    # 添加示例博主（实际使用时应从输入获取）
    # 这里使用一些示例博主ID
    blogger_manager.add_blogger("浅九ninth", bilibili_uid="365654312", weibo_id="6413437934")
    
    # 获取所有博主
    bloggers = blogger_manager.get_all_bloggers()
    
    # 为每个博主获取动态并分析行程
    for blogger_id in bloggers:
        print(f"\n正在处理博主: {blogger_id}")
        print("=" * 50)
        
        # 获取博主信息
        blogger_info = blogger_manager.get_blogger_info(blogger_id)
        bilibili_uid = blogger_info.get('bilibili_uid')
        weibo_id = blogger_info.get('weibo_id')
        
        # 收集动态数据
        all_dynamics = []
        
        # 获取B站动态
        if bilibili_uid:
            print(f"正在获取B站动态 (UID: {bilibili_uid})...")
            bilibili_dynamics = bilibili_scraper.get_user_dynamic(bilibili_uid, max_pages=3)
            if bilibili_dynamics:
                # 转换B站动态格式以匹配微博动态格式
                converted_dynamics = convert_bilibili_dynamics(bilibili_dynamics)
                all_dynamics.extend(converted_dynamics)
                print(f"获取到 {len(converted_dynamics)} 条B站动态")
            else:
                print("未获取到B站动态")
        
        # 获取微博动态
        if weibo_id:
            print(f"正在获取微博动态 (ID: {weibo_id})...")
            weibo_dynamics = weibo_scraper.get_user_tweets(weibo_id)
            if weibo_dynamics:
                all_dynamics.extend(weibo_dynamics)
                print(f"获取到 {len(weibo_dynamics)} 条微博动态")
            else:
                print("未获取到微博动态")
        
        # 如果获取到动态数据，进行AI分析
        if all_dynamics:
            print(f"\n正在分析 {blogger_id} 的 {len(all_dynamics)} 条动态...")
            # 获取博主名称（这里简化处理，实际应从用户信息中获取）
            blogger_name = blogger_id
            
            # 进行AI分析
            schedule_summary = ai_analyzer.analyze_schedule(blogger_name, all_dynamics)
            
            # 输出结果
            print(f"\n{blogger_id} 的线下行程分析结果:")
            print("-" * 50)
            print(schedule_summary)
        else:
            print(f"未获取到 {blogger_id} 的任何动态数据")

if __name__ == "__main__":
    main()