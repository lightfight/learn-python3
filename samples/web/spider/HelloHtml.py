from urllib import request
import ssl

"""
主要测试对一个url的访问
"""

# 去掉ssl的验证
ssl._create_default_https_context = ssl._create_unverified_context

_url = "https://etherscan.io/tokens?p=2"
# _url = "https://www.huobi.pro/zh-cn/coin_coin/exchange/#s=btc_usdt"

req = request.Request(_url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                             'AppleWebKit/536.26 (KHTML, like Gecko) '
                             'Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print(data.decode('utf-8'))


