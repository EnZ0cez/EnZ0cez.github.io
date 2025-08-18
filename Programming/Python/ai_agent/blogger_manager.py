# 博主信息管理模块

class BloggerManager:
    """管理博主ID信息的类"""
    
    def __init__(self):
        # 博主信息字典，格式：{博主ID: {bilibili_uid: ..., weibo_id: ...}}
        self.blogger_info = {}
    
    def add_blogger(self, blogger_id, bilibili_uid=None, weibo_id=None):
        """添加博主信息"""
        self.blogger_info[blogger_id] = {
            'bilibili_uid': bilibili_uid,
            'weibo_id': weibo_id
        }
    
    def get_blogger_info(self, blogger_id):
        """获取博主信息"""
        return self.blogger_info.get(blogger_id, {})
    
    def get_all_bloggers(self):
        """获取所有博主ID"""
        return list(self.blogger_info.keys())
    
    def update_blogger_info(self, blogger_id, bilibili_uid=None, weibo_id=None):
        """更新博主信息"""
        if blogger_id in self.blogger_info:
            if bilibili_uid:
                self.blogger_info[blogger_id]['bilibili_uid'] = bilibili_uid
            if weibo_id:
                self.blogger_info[blogger_id]['weibo_id'] = weibo_id