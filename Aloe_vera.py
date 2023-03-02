# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
    import random
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: * * * 12 *
@ new Env('生城世朝手动上架芦荟')
@ 脚本会取消上架的农作物再出售芦荟
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 价格设置错了重新运行一次脚本    一定看好价格再运行脚本
"""
##################################配置区##################################
price = '50'           # 设置芦荟价格
##################################配置区##################################

##################################下面不要动##################################
application = 'ce_token'  # 变量名
token = ''              # 内置变量 非必要不要填
version = '3.1.41954131'
git = 'https://gitee.com'
host = 'http://scsc.sc19319.com'
golden_seed = 0
msg_list = []

def start():
    try:
        ce_token = os_qinglong()
        print(f"==========共找到{len(ce_token)}个账号==========")
        for i in ce_token:
            msg = []
            print(f"------------正在执行第{ce_token.index(i) + 1}个账号------------")
            ce = CityEarth(i, msg)
            # 账号信息
            if ce.base_info():
                # 防封
                ce.sealing()
                # 出售中
                ce.query_to_sell()
                # 查芦荟个数
                ce.game_map()
                # 查芦荟
                ce.market_sale()

    except Exception as E:
        print(E)





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
            self.token = i.split('&')[0]
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
    def market_sale(self):
        try:
            timi_s = timi_new()
            signstring2 = f'type=crop__{timi_s}'
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
            r2 = requests.request('get', f'{host}/market/get-allow-sale-material-list?type=crop', headers=headers2).json()
            # print(r2)
            if 'status' in r2:
                if r2['status'] == 200:
                    if r2['data']['rows']:
                        packsackItemId = r2['data']['rows'][0]['packsackItemId']
                        quantity = r2['data']['rows'][0]['quantity']
                        price_new = float(price) + float(random.randint(1,99) * 0.00001)
                        signstring1 = f'_packsackItemId={packsackItemId}&price={str(price_new)[:8]}&quantity={quantity}_{timi_s}'
                        headers1 = {
                            'source': 'scsc',
                            'authorization': self.token,
                            'timestamp': str(timi_s),
                            'sign': sign(signstring1),
                            'signstring': signstring1,
                            'version': version,
                'janalytics':'c167f56858dc424ee3d617c9',
                            'Host': 'scsc.sc19319.com',
                            'User-Agent': 'okhttp/4.9.1',
                        }
                        b1 = {
                          "packsackItemId": packsackItemId,
                          "price": str(price_new)[:8],
                          "quantity": str(quantity)
                        }
                        r1 = requests.request('post', f'{host}/market/sale', headers=headers1, data=b1).json()
                        # print(r1)
                        if 'status' in r1:
                            if r1['status'] == 200:
                                print(f'【上架芦荟】:数量:{quantity}丨价格:{str(price_new)[:8]}')
        except Exception as e:
            print(e)

    # 查41级建筑物
    def game_map(self):
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
            # print(r1)
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


def os_qinglong():
    if application in os.environ:
        token_list = os.environ[application].split('\n')
        if len(token_list) > 0:
            return token_list
        else:
            print(f"{application}变量未启用")
            print('脚本退出')
            sys.exit(1)
    else:
        print(f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")
        if token:
            token_list = token.split('\n')
            if len(token_list) > 0:
                return token_list
        else:
            print(f"内置变量为空")
            print('脚本结束')
            sys.exit(0)


if __name__ == '__main__':
    start()
