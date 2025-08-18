import asyncio
import argparse
import json
from datetime import datetime
from bilibili_api import user, Credential

async def get_all_user_dynamics(uid: int, save_to_file: bool = True, max_pages: int = 0):
    """
    获取用户的所有动态
    
    Args:
        uid: 用户ID
        save_to_file: 是否保存到文件
        max_pages: 最大获取页数，0表示获取所有动态
    """
    try:
        # 创建用户对象
        u = user.User(uid=uid)
        
        # 存储所有动态
        all_dynamics = []
        offset = ""  # 初始offset为空字符串
        has_more = True  # 是否还有更多动态
        page = 1
        
        print(f"正在获取用户 {uid} 的动态...")
        
        while has_more:
            print(f"正在获取第 {page} 页动态...")
            
            # 获取用户动态（使用新接口）
            dynamics = await u.get_dynamics_new(offset=offset)
            
            # 检查返回的数据是否为空
            if dynamics is None:
                print("未能获取到用户动态信息")
                break
            
            # 检查是否有'items'键
            items = dynamics.get('items', [])
            if not items:
                print("没有更多动态了")
                break
                
            print(f"第 {page} 页获取到 {len(items)} 条动态")
            
            # 添加到所有动态列表
            all_dynamics.extend(items)
            
            # 检查是否还有更多动态
            has_more = dynamics.get('has_more', False)
            offset = dynamics.get('offset', "")
            
            # 如果没有更多动态或offset为空，则停止
            if not has_more or not offset:
                break
                
            # 检查是否达到最大页数限制
            if max_pages > 0 and page >= max_pages:
                print(f"已达到最大页数限制 {max_pages}")
                break
                
            page += 1
            
            # 为了避免请求过于频繁，添加一个小延迟
            await asyncio.sleep(1)
        
        print(f"共获取到 {len(all_dynamics)} 条动态")
        
        # 处理和显示动态
        processed_dynamics = []
        for i, item in enumerate(all_dynamics):
            dynamic_info = {
                "id": item.get('id_str', 'N/A'),
                "type": item.get('type', 'N/A'),
                "timestamp": None,
                "content": None
            }
            
            # 获取发布时间
            modules = item.get('modules', {})
            module_author = modules.get('module_author', {})
            pub_ts = module_author.get('pub_ts')
            if pub_ts:
                # 转换时间戳为可读格式
                dynamic_info["timestamp"] = datetime.fromtimestamp(pub_ts).strftime('%Y-%m-%d %H:%M:%S')
            else:
                dynamic_info["timestamp"] = 'N/A'
            
            # 提取动态内容
            if 'module_dynamic' in modules:
                dynamic_content = modules['module_dynamic']
                
                # 处理文本内容
                if 'desc' in dynamic_content and dynamic_content['desc'] is not None:
                    text = dynamic_content['desc'].get('text', 'N/A')
                    dynamic_info["content"] = text
                # 处理图文内容
                elif 'major' in dynamic_content and dynamic_content['major'] is not None:
                    major = dynamic_content['major']
                    if 'opus' in major and major['opus'] is not None:
                        opus = major['opus']
                        if 'summary' in opus and opus['summary'] is not None:
                            text = opus['summary'].get('text', 'N/A')
                            dynamic_info["content"] = text
                        else:
                            dynamic_info["content"] = "图文动态"
                    elif 'archive' in major and major['archive'] is not None:
                        archive = major['archive']
                        title = archive.get('title', 'N/A')
                        dynamic_info["content"] = f"视频 - {title}"
                    else:
                        dynamic_info["content"] = "其他类型动态"
                else:
                    dynamic_info["content"] = "无文字内容"
            else:
                dynamic_info["content"] = "无内容"
            
            processed_dynamics.append(dynamic_info)
            
            # 显示前10条动态作为示例
            if i < 10:
                print(f"动态ID: {dynamic_info['id']}")
                print(f"动态类型: {dynamic_info['type']}")
                print(f"发布时间: {dynamic_info['timestamp']}")
                print(f"动态内容: {dynamic_info['content']}")
                print("-" * 50)
        
        # 如果需要保存到文件
        if save_to_file:
            filename = f"bilibili_dynamics_{uid}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(processed_dynamics, f, ensure_ascii=False, indent=2)
            print(f"已将动态数据保存到 {filename}")
        
        return processed_dynamics
    except Exception as e:
        print(f"获取用户动态时发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None

async def main():
    parser = argparse.ArgumentParser(description='获取B站用户动态')
    parser.add_argument('uid', type=int, help='用户UID')
    parser.add_argument('--max-pages', type=int, default=0, help='最大获取页数，0表示获取所有动态')
    parser.add_argument('--no-save', action='store_true', help='不保存到文件')
    
    args = parser.parse_args()
    
    result = await get_all_user_dynamics(
        uid=args.uid, 
        save_to_file=not args.no_save,
        max_pages=args.max_pages
    )
    
    return result

if __name__ == "__main__":
    asyncio.run(main())