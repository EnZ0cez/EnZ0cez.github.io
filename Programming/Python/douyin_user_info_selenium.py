import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_douyin_user_info(user_id):
    """
    使用Selenium获取抖音用户主页信息
    
    Args:
        user_id (str): 抖音用户ID
        
    Returns:
        dict: 包含用户信息的字典
    """
    # 配置Chrome选项
    chrome_options = Options()
    # 移除--headless选项，使用有头浏览器
    # chrome_options.add_argument("--headless")  # 无头模式
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.184 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    # 重新启用图片加载
    # chrome_options.add_argument("--disable-images")
    # 重新启用JavaScript以加载动态内容
    # chrome_options.add_argument("--disable-javascript")
    chrome_options.add_argument("--lang=zh-CN")
    chrome_options.add_argument("--disable-webrtc")
    chrome_options.add_argument("--disable-remote-fonts")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 初始化WebDriver
    driver = None
    try:
        # 使用指定路径的ChromeDriver
        chromedriver_path = "C:/Program Files/Google/Chrome/Application/chromedriver-win64/chromedriver.exe"
        
        if os.path.exists(chromedriver_path):
            service = Service(chromedriver_path)
            print(f"使用ChromeDriver: {chromedriver_path}")
        else:
            print(f"ChromeDriver路径不存在: {chromedriver_path}")
            return None
            
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("成功初始化ChromeDriver")
        
        # 执行CDP命令来隐藏webdriver属性
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                })
            """
        })
        
        # 添加更多反检测脚本
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                window.chrome = {
                    runtime: {}
                };
            """
        })
        
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['zh-CN', 'zh', 'en']
                });
            """
        })
        
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5]
                });
            """
        })
    except Exception as e:
        print(f"初始化ChromeDriver失败: {e}")
        return None
    
    try:
        # 抖音用户主页URL
        url = f"https://www.douyin.com/user/{user_id}"
        
        # 访问页面
        driver.get(url)
        
        # 随机等待5-15秒
        time.sleep(random.uniform(5, 15))
        
        # 模拟人类行为：随机鼠标移动
        actions = ActionChains(driver)
        for _ in range(5):
            x = random.randint(0, driver.execute_script("return window.innerWidth"))
            y = random.randint(0, driver.execute_script("return window.innerHeight"))
            actions.move_by_offset(x, y)
            actions.perform()
            time.sleep(random.uniform(0.5, 2))
        
        # 检查页面标题
        print(f"页面标题: {driver.title}")
        
        # 如果页面标题包含"验证码"，则等待一段时间
        if "验证码" in driver.title:
            print("检测到验证码页面，等待60秒...")
            time.sleep(60)
        
        # 等待页面加载完成
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # 再次等待，确保动态内容加载完成
        time.sleep(random.uniform(5, 10))
        
        # 打印页面URL和部分源码以便调试
        print(f"当前页面URL: {driver.current_url}")
        
        # 提取用户信息
        # 用户名
        try:
            # 等待用户名元素出现
            username_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//h1[@data-e2e="user-title"]'))
            )
            username = username_elem.text
        except:
            # 尝试其他可能的选择器
            try:
                username_elem = driver.find_element(By.XPATH, '//h1[contains(@class, "user-title")]')
                username = username_elem.text
            except:
                username = "未找到用户名"
        
        # 简介
        try:
            # 等待简介元素出现
            desc_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[@data-e2e="user-desc"]'))
            )
            description = desc_elem.text
        except:
            try:
                desc_elem = driver.find_element(By.XPATH, '//p[contains(@class, "user-desc")]')
                description = desc_elem.text
            except:
                description = "未找到简介"
        
        # 关注数
        try:
            # 等待关注数元素出现
            follow_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@data-e2e="follow-count"]'))
            )
            follow_count = follow_elem.text
        except:
            try:
                follow_elem = driver.find_element(By.XPATH, '//span[contains(@class, "follow-count")]')
                follow_count = follow_elem.text
            except:
                follow_count = "未找到关注数"
        
        # 粉丝数
        try:
            # 等待粉丝数元素出现
            follower_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@data-e2e="follower-count"]'))
            )
            follower_count = follower_elem.text
        except:
            try:
                follower_elem = driver.find_element(By.XPATH, '//span[contains(@class, "follower-count")]')
                follower_count = follower_elem.text
            except:
                follower_count = "未找到粉丝数"
        
        # 获赞数
        try:
            # 等待获赞数元素出现
            like_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[@data-e2e="like-count"]'))
            )
            like_count = like_elem.text
        except:
            try:
                like_elem = driver.find_element(By.XPATH, '//span[contains(@class, "like-count")]')
                like_count = like_elem.text
            except:
                like_count = "未找到获赞数"
        
        # 返回用户信息字典
        return {
            "username": username,
            "description": description,
            "follow_count": follow_count,
            "follower_count": follower_count,
            "like_count": like_count
        }
        
    except Exception as e:
        print(f"错误: {e}")
        # 打印页面源码以便调试
        print("页面源码:")
        print(driver.page_source[:5000])  # 打印前5000个字符
        return None
    finally:
        # 关闭浏览器
        if driver:
            driver.quit()

# 示例用法
if __name__ == "__main__":
    # 这里需要替换为实际的抖音用户ID
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