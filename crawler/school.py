"""import time
from selenium.webdriver import Edge

options = {
    "ms:edgeOptions": {
        'args': [
        # 设置参数
            '--headless',
            # 无头模式
            '--disable-gpu',
            # 禁用显卡
        ]
    }
}
path = 'crawler\msedgedriver.exe'
# 路径
driver = Edge(executable_path=path,capabilities=options)
# 浏览器声明
url = "http://cas.hnu.edu.cn/cas/login"
# 网页链接
driver.get(url)
# 访问网址
username_box = driver.find_element_by_xpath('//*[@id="username"]')
password_box = driver.find_element_by_xpath('//*[@id="password"]')
login_button = driver.find_element_by_xpath('//*[@id="dl"]')
# 定位元素
username_box.send_keys('201907010226')
password_box.send_keys('Hj---')
# 输入内容
login_button.click() 
# 鼠标左击
time.sleep(1)
# 等待加载
def get_infos():
    infos = []
    # 二维列表
    ulist = driver.find_element_by_xpath("""//*[@id="News"]/div/div[2]/div/div/ul""")
    # 一级查找 列表
    items = ulist.find_elements_by_xpath('li')
    # 二级查找 项目
    for item in items:
    # 遍历
        anchor = item.find_element_by_xpath('a')
        # 三次查找
        link = anchor.get_attribute("href")
        # 获取链接
        text = anchor.find_element_by_xpath("span[@class='text']").get_attribute("title")
        # 四次查找 获取标题->属性
        date = anchor.find_element_by_xpath("span[@class='date']").text
        # 四次查找 获取日期->文本
        infos.append([link,text,date])
    return infos

    """