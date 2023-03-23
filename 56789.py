# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
    import random
    import json
    import socket
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: * * * 8 *
@ new Env('手动出售芦荟')
@ 脚本会取消上架的农作物再出售芦荟
"""

##################################下面不要动##################################
application = 'ce_token'  # 变量名
version = '3.1.41955435111'
git = 'https://gitee.com'
host = 'http://scsc.sc19319.com'
golden_seed = 0
msg_list = []


def O000OO0O00OO00O00():
    if OO00OO0OO0OO00OO00o0() in gitee_validation()['validation']:
        pass
    else:
        exit(1)
def kvkv():
    return '/vastzzzl/vastzzzl/raw/master'


def OO00OO0OO0OO00OO00o0():
    return hashlib.md5((socket.gethostbyname(get_ip()) + socket.getfqdn(socket.gethostname())).encode('utf-8')).hexdigest().upper()

def get_ip():
    return requests.request('get', 'https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text

def gitee_validation():
    return requests.request('get', f'{git}{kvkv()}/validation').json()


def sign(text):
    md5str1 = hashlib.md5(text.encode()).hexdigest()
    md5str2 = "scsc%^&*" + md5str1 + "19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"
    md5str = hashlib.md5(md5str2.encode()).hexdigest()
    return md5str

def timi_new():
    return str(int(time.time() * 1000))


class CityEarth:

    def __init__(self, i, msg):
        try:
            self.msg = msg
            self.time = str(time.time() * 1000).split('.')[0]
            self.token = i['authorization']
        except:
            print('变量格式错误')

    # 账号信息
    def base_info(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source':'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            resp = requests.request('get', f'{host}/user', headers=headers).json()
            # print(resp)
            if 'status' in resp:
                if resp['status'] == 200:
                    nickname = resp['data']['nickname']
                    inner_id = resp['data']['inner_id']
                    gold = resp['data']['assets']['gold']
                    level = resp['data']['level']
                    print(f'【账号信息】:昵称:{nickname[:5]}丨ID:{inner_id}丨等级:{level}丨金种子:{str(gold).split(".")[0]}')
                if resp['status'] == 401:
                    print(resp['message'])
                    self.msg.append('有账号失效了')
                    return False
                if resp['status'] == 500:
                    return False
            return True
        except Exception as E:
            print(E)

    # 防封  效果未知
    def sealing(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            requests.request('get', f'{host}/friends/cash-rewards/rank', headers=headers)
            requests.request('get', f'{host}/packsack/list', headers=headers)
            requests.request('get', f'{host}/friends/invited/ad', headers=headers)
            requests.request('get', f'{host}/assets/gold/rank', headers=headers)
            requests.request('get', f'{host}/user', headers=headers)
            requests.request('get', f'{host}/propsraffle/lucky/number', headers=headers)
            requests.request('get', f'{host}/finance/get-power-list', headers=headers)
            requests.request('post', f'{host}/announcement/announcement', headers=headers)
            requests.request('get', f'{host}/game/getAllData', headers=headers)
            requests.request('get', f'{host}/assets', headers=headers)
        except Exception as e:
            print(e)






    # 卖芦荟
    def market_sale_buy(self, _askToBuyId, quantity):
        try:
            timi_s = timi_new()
            signstring2 = f'_askToBuyId={_askToBuyId}&quantity={quantity}_{timi_s}'
            headers2 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_s),
                'sign': sign(signstring2),
                'signstring': signstring2,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            b2 = {"askToBuyId":_askToBuyId,"quantity":quantity}
            r2 = requests.request('post', f'{host}/market/sale-for-ask-to-buy', headers=headers2, data=b2).json()
            # print(r2)
            if 'status' in r2:
                if r2['status'] == 200:
                    print('【出售求购】:出售成功')
                elif r2['message'] == '请求超时':
                    self.market_sale_buy(_askToBuyId, quantity)
                else:
                    print(r2)
                    if r2['message'] == '库存不足':
                        self.market_sale_buy(_askToBuyId, quantity - 1)
                    if r2['message'] == '更新求购单失败':
                        exit()
                    if r2['message'] == '购买数量不足':
                        exit()
                    if r2['message'] == '商品不存在或取消求购':
                        exit()
                    if r2['message'] == '购买数量不足':
                        exit()

        except Exception as e:
            print(e)

    # 查41级建筑物
    def game_map(self, _askToBuyId):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/game/map', headers=headers).json()
            print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    for i in r1['data']['list'][0]['crops']:
                        # print(i)
                        level1 = i['level']
                        if level1 == 41:
                            crop_name = i['crop_name']
                            count = i['count']
                            if count > 0:
                                print(f'【农业资产】:{crop_name}丨数量:{count}')
                                self.market_sale_buy(_askToBuyId, count)
        except Exception as e:
            print(e)


    # 查询出售中的芦荟
    def query_to_sell(self):
        try:
            signstring = f'page=1&pageSize=10&type=crop__{timi_new()}'
            headers1 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop', headers=headers1).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    for i in r1['data']['rows']:
                        materialKey = i['materialKey']
                        quantity = i['quantity']
                        price = i['price']
                        saleState = i['saleState']
                        if saleState == 0:
                            print(f'【出售订单】:名称:{materialKey}丨数量:{quantity}丨价格:{price}')
                            id_new = i['id']
                            self.cacel_sale(id_new)
                        # if saleState == 1:
                        #     print(f'【出售订单】:名称:{materialKey}丨数量:{quantity}丨价格:{price}')
                        # if saleState == 2:
                        #     print(f'【出售订单】:名称:{materialKey}丨数量:{quantity}丨价格:{price}')

        except Exception as e:
            print(e)


    # 取消订单
    def cacel_sale(self, id_new):
        try:
            signstring = f'_saleId={id_new}_{timi_new()}'
            headers1 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            b1 = {
              "saleId": id_new
            }
            r1 = requests.request('post', f'{host}/market/cacel-sale', headers=headers1, data=b1).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    print(f'【下架出售】:{r1["data"]}')
        except Exception as e:
            print(e)


    # 查询芦荟价格
    def market_buy(self, token):
        try:
            signstring = 'page=1&pageSize=20&queryField=__1679487573414'
            headers = {
                'authorization': token,
                'timestamp': '1679487573414',
                'sign': '6b71dc53c645c9e115a97e8f1fe2586b',
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', 'http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    for i in r1['data']['rows']:
                        # print(i)
                        id_new = i['id']
                        price = i['price']
                        remainQuantity = i['remainQuantity']
                        print(f'求购价格:{price}丨求购数量:{remainQuantity}丨任务ID:{id_new}')
                        return id_new
        except Exception as e:
            print(e)




def start():
    try:
        print(f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')
        O000OO0O00OO00O00()
        ce_token_new = json.load(open("CityEarth_data.json", 'r'))['data']
        _askToBuyId = CityEarth.market_buy(ce_token_new, ce_token_new[0]['authorization'])
        print(f"==========共找到{len(ce_token_new)}个账号==========")
        for i in ce_token_new:
            msg = []
            print(f"------------正在执行第{ce_token_new.index(i) + 1}个账号------------")
            ce = CityEarth(i, msg)
            # 账号信息
            if ce.base_info():
                # 防封
                ce.sealing()
                # # 出售中
                ce.query_to_sell()
                # 查芦荟个数
                # _askToBuyId = requests.request('get', 'https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json()['_askToBuyId']
                ce.game_map(_askToBuyId)

    except Exception as E:
        print(E)


if __name__ == '__main__':
    start()
