from urllib import request
import ssl
# import re
from bs4 import BeautifulSoup

# 去掉ssl的验证
ssl._create_default_https_context = ssl._create_unverified_context

# html = request.urlopen('https://etherscan.io/tokens?p=2')
# print(html)

req = request.Request('https://etherscan.io/tokens?p=2')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
                             'AppleWebKit/536.26 (KHTML, like Gecko) '
                             'Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    # print(data)

    bs_obj = BeautifulSoup(data, 'html.parser')

    # find_all 寻找所有的a标签，而且href属性是/token开头
    # token_list = bs_obj.find_all('a', href=re.compile("^/token/"))

    # select 类别下的标签
    token_list = bs_obj.select('.hidden-xs h5 a')
    print("total token count = ", len(token_list))
    for i in range(len(token_list)):
        # print(i, token_list[i])
        print(i, token_list[i].string)


"""

/usr/local/bin/python3.6 /Users/dirk/IdeaProjects/learn-python3/samples/web/spider/HelloSpider.py
total token count =  50
0 Dragon (DRGN)
1 Storm (STORM)
2 Gifto (GTO)
3 WAX Token (WAX)
4 MATRIX AI Network (MAN)
5 SONM (SNM)
6 Storj (STORJ)
7 Revain (R)
8 Salt (SALT)
9 ChainLink Token (LINK)
10 Civic (CVC)
11 ICONOMI (ICN)
12 RLC (RLC)
13 SingularityNET (AGI)
14 HPBCoin (HPB)
15 DATAcoin (DATA)
16 TenXPay (PAY)
17 Nexo (NEXO)
18 HoloToken (HOT)
19 NucleusVision (nCash)
20 Request (REQ)
21 Aragon (ANT)
22 Gnosis (GNO)
23 CyberVeinToken (CVT)
24 All Sports Coin (SOC)
25 RUFF (RUFF)
26 ArcBlock (ABT)
27 Cindicator (CND)
28 SAN (SAN)
29 Bluzelle (BLZ)
30 Dai Stablecoin v1.0 (DAI)
31 Storiqa (STQ)
32 ODEM Token (ODEM)
33 EDUCare (EKT)
34 DENT (DENT)
35 EnjinCoin (ENJ)
36 Crypterium (CRPT)
37 CREDITS (CS)
38 Quantstamp (QSP)
39 Genaro X (GNX)
40 Crypto20 (C20)
41 Raiden (RDN)
42 Amber (AMB)
43 PILLAR (PLR)
44 QuarkChain Token (QKC)
45 Bread (BRD)
46 Trade (TIO)
47 POA ERC20 on Foundation (POA20)
48 OCoin (OCN)
49 SIRIN (SRN)

Process finished with exit code 0


"""