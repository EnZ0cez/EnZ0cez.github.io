# 抖音用户信息获取工具

这个工具可以获取抖音用户的公开信息，包括用户名、简介、关注数、粉丝数和获赞数。

## 使用方法

1. 安装依赖：
   ```
   pip install selenium webdriver-manager
   ```

2. 安装Chrome浏览器和ChromeDriver：
   - 下载Chrome浏览器并安装：https://www.google.com/chrome/
   - 下载ChromeDriver：https://chromedriver.chromium.org/
   - 将ChromeDriver.exe文件放在Chrome浏览器的安装目录下（通常是`C:\\Program Files\\Google\\Chrome\\Application\\`）
   - 将Chrome浏览器的安装目录添加到系统PATH环境变量中

3. 运行脚本：
   ```
   python douyin_user_info_selenium.py
   ```

## 代码说明

- `douyin_user_info.py`：使用requests和BeautifulSoup尝试获取抖音用户信息（由于反爬虫机制，此方法无法正常工作）
- `douyin_user_info_selenium.py`：使用Selenium模拟浏览器访问抖音用户主页，获取用户信息（需要正确配置ChromeDriver）

## 注意事项

- 抖音有严格的反爬虫机制，直接使用requests库无法获取到数据
- 使用Selenium可以更好地模拟浏览器行为，但抖音仍然可能检测到自动化访问并要求验证码验证
- 在测试过程中，我们发现抖音会检测到Selenium自动化访问并显示验证码页面
- 即使使用了多种反检测技术，仍然难以稳定绕过抖音的验证码机制

## 建议

1. 如果需要稳定获取抖音用户信息，建议使用抖音开放平台的官方API：
   - 注册抖音开放平台账号：https://open.douyin.com/
   - 创建应用并获取ClientKey和ClientSecret
   - 通过OAuth授权流程获取access_token
   - 使用access_token调用API获取用户信息

2. 如果只是偶尔需要获取用户信息，可以考虑手动访问页面并复制信息

3. 如果需要批量获取信息，可以考虑使用专门的爬虫服务或与抖音官方联系获取数据访问权限

# 微博用户动态获取工具

这个工具可以获取微博用户的公开信息和微博动态，并将数据保存到JSON文件中。

## 使用方法

直接运行脚本：
```
python weibo_user_tweets.py
```

## 代码说明

- `weibo_user_tweets.py`：使用urllib库获取微博用户信息和动态，并将数据保存到JSON文件

## 功能特点

- 获取微博用户的基本信息（昵称、简介、粉丝数、关注数、微博数）
- 获取用户的微博动态（发布时间、内容、转发数、评论数、点赞数、来源）
- 自动处理gzip压缩的数据
- 清理HTML标签和实体
- 将获取的数据保存到JSON文件中，文件名包含用户ID和时间戳

## 数据保存

工具会自动将获取到的微博用户信息和动态保存到`data`目录下的JSON文件中，文件名格式为：
```
data/weibo_{用户ID}_{日期时间}.json
```

JSON文件包含以下结构：
```json
{
  "user_info": {
    "id": "用户ID",
    "screen_name": "昵称",
    "description": "简介",
    "followers_count": "粉丝数",
    "follow_count": "关注数",
    "statuses_count": "微博数"
  },
  "tweets": [
    {
      "id": "微博ID",
      "created_at": "发布时间",
      "text": "微博内容",
      "reposts_count": "转发数",
      "comments_count": "评论数",
      "attitudes_count": "点赞数",
      "source": "来源"
    }
    // ... 更多微博动态
  ],
  "fetch_time": "数据获取时间"
}
```

## 注意事项

- 该工具使用微博移动端API，无需登录即可获取公开信息
- 请遵守微博的使用条款，不要频繁请求数据
- 工具会自动创建`data`目录用于存储JSON文件

## 自定义用户

要获取其他用户的微博动态，只需修改`weibo_user_tweets.py`文件中的`user_id`变量：
```python
# 用户ID（需要替换为实际的用户ID）
user_id = "目标用户的ID"
```

用户ID可以通过以下方式获取：
1. 在微博用户主页URL中找到，例如：`https://weibo.com/u/1642909335`中的`1642909335`
2. 在微博移动端页面URL中找到，例如：`https://m.weibo.cn/u/1642909335`中的`1642909335`

## 项目结构

- `douyin_user_info.py`：使用requests和BeautifulSoup的抖音初始实现
- `douyin_user_info_selenium.py`：使用Selenium的抖音改进实现
- `weibo_user_tweets.py`：使用urllib的微博实现
- `README.md`：项目说明文档
- `data/`：存储获取的微博数据JSON文件