from websocket import create_connection
import gzip
import time

# https://github.com/huobiapi/WebSocket-API-demos/blob/master/Websocket-Python3-demo/huobi.py

if __name__ == '__main__':
    while True:

        # noinspection PyBroadException
        try:
            ws = create_connection("ws://api.huobi.pro/ws")
            break
        except Exception as e:
            print('connect ws error,retry...')
            time.sleep(2)

    # 订阅 KLine 数据
    # tradeStr = """{"sub": "market.btcusdt.kline.1min","id": "id10","freq-ms":5000}"""
    tradeStr = """{"sub": "market.btcusdt.kline.5min","id": "id10"}"""
    ws.send(tradeStr)

    tradeStr = """{"sub": "market.btcusdt.kline.4hour","id": "id10"}"""
    ws.send(tradeStr)

    # 请求 KLine 数据
    # tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""

    # 订阅 Market Depth 数据
    # tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 请求 Market Depth 数据
    # tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 订阅 Trade Detail 数据
    # tradeStr="""{"sub": "market.ethusdt.trade.detail", "id": "id10"}"""

    # 请求 Trade Detail 数据
    # tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

    # 请求 Market Detail 数据
    # tradeStr = """{"req": "market.ethusdt.detail", "id": "id12"}"""
    # ws.send(tradeStr)

    while True:
        compressData = ws.recv()
        result = gzip.decompress(compressData).decode('utf-8')

        # 检查是否是心跳，{"ping":1530240555766}
        if result[:7] == '{"ping"':
            # print(len(result), result)
            ts = result[8:21]
            pong = '{"pong":%s}' % ts
            ws.send(pong)
            # ws.send(tradeStr)
        # 如果不是心跳，那直接输出
        else:
            print(result)
