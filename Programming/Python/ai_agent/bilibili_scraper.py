import json
import asyncio
from datetime import datetime
from bilibili_api import user

class BilibiliScraper:
    """B站动态获取类"""
    
    def __init__(self):
        """初始化B站爬虫"""
        pass
    
    async def get_user_dynamics(self, uid: int, max_pages: int = 0):
        """
        获取用户的所有动态
        
        Args:
            uid: 用户ID
            max_pages: 最大获取页数，0表示获取所有动态
            
        Returns:
            list: 处理后的动态列表
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
                try:
                    dynamics = await u.get_dynamics_new(offset=offset)
                except Exception as e:
                    print(f"连接B站API时发生网络错误: {e}")
                    print("请检查网络连接或稍后再试")
                    import traceback
                    traceback.print_exc()
                    return None
                
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
                await asyncio.sleep(2)
            
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
            
            return processed_dynamics
        except Exception as e:
            print(f"获取用户动态时发生错误: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def get_user_dynamic(self, uid, max_pages=0):
        """
        获取B站用户动态（对外接口）
        
        Args:
            uid (int): B站用户UID
            max_pages (int): 最大获取页数，0表示获取所有动态
            
        Returns:
            list: 动态列表
        """
        try:
            # 使用asyncio运行异步函数
            # 检查是否存在当前事件循环
            try:
                loop = asyncio.get_event_loop()
                if loop.is_closed():
                    raise RuntimeError("Event loop is closed")
            except RuntimeError:
                # 如果没有事件循环或已关闭，创建新的
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            result = loop.run_until_complete(self.get_user_dynamics(uid, max_pages))
            
            # 只有当我们创建了新循环时才关闭它
            if not asyncio.get_event_loop_policy().get_event_loop() is loop:
                loop.close()
                
            return result
        except Exception as e:
            print(f"获取B站用户动态时发生错误: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def get_user_info(self, uid):
        """
        获取B站用户信息
        
        Args:
            uid (int): B站用户UID
            
        Returns:
            dict: 用户信息
        """
        try:
            # 创建用户对象
            u = user.User(uid=uid)
            
            # 使用asyncio运行异步函数
            # 检查是否存在当前事件循环
            try:
                loop = asyncio.get_event_loop()
                if loop.is_closed():
                    raise RuntimeError("Event loop is closed")
            except RuntimeError:
                # 如果没有事件循环或已关闭，创建新的
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            user_info = loop.run_until_complete(u.get_user_info())
            
            # 只有当我们创建了新循环时才关闭它
            if not asyncio.get_event_loop_policy().get_event_loop() is loop:
                loop.close()
            
            if user_info:
                return {
                    'id': user_info.get('mid'),
                    'name': user_info.get('name'),
                    'sign': user_info.get('sign'),
                    'face': user_info.get('face'),
                    'level': user_info.get('level'),
                    'follower_count': user_info.get('follower_count', 0)
                }
            else:
                print("获取B站用户信息失败")
                return None
                
        except Exception as e:
            print(f"获取B站用户信息错误: {e}")
            import traceback
            traceback.print_exc()
            return None