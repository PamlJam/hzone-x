import requests
# 请求
from lxml import etree
# 解析文本
def getInfos():
    infos = []
    # 返回结果
    response = requests.get(url = "http://oa.hnu.cn:808/Search/Zhbg_Tztg.aspx")
    # 获取响应
    response.encoding = 'gbk'
    # 编码
    data = etree.HTML(response.text)
    # 转换对象
    linkList = data.xpath('//*[@id="bt"]/@href')
    # 链接
    textList = data.xpath('//*[@id="bt"]/@title')
    # 标题
    for i in range(15):
        infos.append((
        # 生成二维数组
            'http://oa.hnu.cn:808/' + linkList[i],
            # 拼接网址
            textList[i],
            data.xpath('//*[@id="ContentPlaceHolder1_TztgGridView_Label2_%d"]/text()' % i)[0],
            # 拼接路径
        ))
    return infos