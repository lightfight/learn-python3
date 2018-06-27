from urllib import request
import ssl
# import re
from bs4 import BeautifulSoup

# 去掉ssl的验证
ssl._create_default_https_context = ssl._create_unverified_context


# 查询一页
def page(p):
    req = request.Request('https://etherscan.io/tokens?p={0}'.format(p))
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                                 'AppleWebKit/536.26 (KHTML, like Gecko) '
                                 'Version/8.0 Mobile/10A5376e Safari/8536.25')

    with request.urlopen(req) as f:
        data = f.read()

        bs_obj = BeautifulSoup(data, 'html.parser')

        # find_all 寻找所有的a标签，而且href属性是/token开头
        # token_list = bs_obj.find_all('a', href=re.compile("^/token/"))

        # select 类别下的标签
        token_list = bs_obj.select('.hidden-xs h5 a')
        print("total token count = ", len(token_list))
        for i in range(len(token_list)):
            # print(i, token_list[i])
            print(((p - 1) * 50) + i + 1, token_list[i].string)


# 抓取
def crawl():

    # 假设1000页
    for i in range(100, 1000):
        print("抓取的页数 =", i)
        page(i)


# 程序入口
crawl()
