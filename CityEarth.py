# coding: utf-8
try:
    import threading, re, os, sys, time, hashlib, json, requests, random, socket, uuid, datetime
    import Invalid_login
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 6 1-23/2 * * *
@ new Env('生城世朝')       
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 配置文件和脚本要放同一目录
@ 版本  4.2
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version = '3.1.419554311'
git = 'https://gitee.com'
host = 'http://scsc.sc19319.com'
golden_seed = 0
msg_list = []
invited_new = []
weishim = []


def start():
    try:
        O000OO000O0O00OOO00()
        print(f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')
        O000OO0O00OO00O00()
        ce_token = json.load(open("CityEarth_data.json", 'r'))['data']
        print(f"==========共找到{len(ce_token)}个账号==========")
        for i in ce_token:
            msg = []
            print(f"------------正在执行第{ce_token.index(i) + 1}个账号------------")
            ce = CityEarth(i, msg, ce_token.index(i))

            def vastlcc():
                # 账号信息
                if ce.base_info():
                    # 防封
                    ce.sealing()
                    # 查好友数量
                    ce.invitenum()
                    # 查询出售中的芦荟
                    ce.query_to_sell()
                    # 农业资产
                    ce.game_map()
                    # 直接出售芦荟
                    # ce.ddd()
                    # 绑定邀请码
                    ce.friends_invitation()
                    # 添加营养
                    ce.energy()
                    # 添加三叶草
                    ce.add_clover()
                    # 转盘抽奖
                    ce.propsraffle()
                    # # 购买合成
                    ce.synthetic()
                    # # 领取图鉴
                    ce.crops_illustrated()
                    # 提现
                    ce.withdraw()
                    if float(datetime.datetime.now().hour) > 8:
                        # 赠送金种子
                        ce.give_gold()

            t1 = threading.Thread(target=vastlcc)
            t1.start()
            time.sleep(time_xx)
        print(f"------------正在处理数据------------")
        time.sleep(0.5)
        content = format_msg()
        print(f'预计每日收益：{str(golden_seed)[:6]}金种子', content + ' ')
        time.sleep(100)
        print('开始打印好友数量不足2的ID')
        for d in invited_new:
            print(d)
        print('开始打印未实名的token')
        for o in weishim:
            print(o)
    except Exception as E:
        print(E)


# 赠送金种子
def give_gold(doneeNo, quantity):
    try:
        signstring = f'_doneeNo={doneeNo}&quantity={int(quantity)}_{timi_new()}'
        headers = {
            'source': 'scsc',
            'authorization': json.load(open("CityEarth_data.json", 'r'))['data'][0]['authorization'],
            'timestamp': str(timi_new()),
            'sign': sign(signstring),
            'signstring': signstring,
            'version': version,
            'janalytics': 'c167f56858dc424ee3d617c9',
            'Host': 'scsc.sc19319.com',
            'User-Agent': 'okhttp/4.9.1',
        }
        b1 = {
            "quantity": int(quantity),
            "doneeNo": doneeNo
        }
        r1 = requests.request('post', f'{host}/finance/give-gold', headers=headers, data=b1).json()
        # print(r1)
        if 'status' in r1:
            if r1['status'] == 200:
                if r1['data']:
                    print(f'【赠送种子】:赠送{int(quantity)}种子给{doneeNo}成功')
                    return True
            if r1['status'] == 401:
                print(f'【赠送种子】:{r1["message"]}')
                return False
            if r1['status'] == 500:
                print(f'【赠送种子】:{r1["message"]}')
                return False
        return False
    except Exception as e:
        print(e)


def kvkv():
    return '/vastzzzl/vastzzzl/raw/master'

def oyoy():
    return '卡密未激活   ❌'


def sign(text):
    md5str1 = hashlib.md5(text.encode()).hexdigest()
    sca = sc1()
    scb = sc2()
    scc = sc3()
    md5str2 = sca + md5str1 + scb + scc
    md5str = hashlib.md5(md5str2.encode()).hexdigest()
    return md5str


def format_msg():
    str1 = ""
    for item in msg_list:
        str1 += str(item) + "\r\n"
    return str1


def sc1():
    return "scsc%^&*"


def O000OO0O00OO00O00():
    if OO00OO0OO0OO00OO00o0() in gitee_validation()['validation']:
        ubbbf()
    else:
        oyoy()
        exit(1)


def timi_new():
    return str(int(time.time() * 1000))


json_path = "CityEarth_data.json"
json_path1 = "CityEarth_data.json"
dict = {}


def get_json_data(json_path, len_new, key, authorization):
    with open(json_path, 'rb') as f:
        params = json.load(f)
        params['data'][len_new][key] = authorization
        dict = params
    f.close()
    return dict


def write_json_data(dict):
    with open(json_path1, 'w') as r:
        json.dump(dict, r)
    r.close()
    return True


class CityEarth:

    def __init__(self, i, msg, len_new):
        try:
            self.msg = msg
            self.time = str(time.time() * 1000).split('.')[0]
            self.token = i['authorization']
            self.innerId = json.load(open("CityEarth_data.json", 'r'))['unified_data']['innerId']
            self.doneeNo = json.load(open("CityEarth_data.json", 'r'))['unified_data']['doneeNo']
            self.elephant_user = i['elephant_user']
            self.elephant_pswd = i['elephant_pswd']
            self.elephant_Task_ID = i['elephant_Task_ID']
            self.len_new = len_new
        except:
            print('变量格式错误')

    # 账号信息
    def base_info(self):
        try:
            # 离线
            self.watched_ad()
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
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
                    print(
                        f'【账号信息】:昵称:{nickname[:5]}丨ID:{inner_id}丨等级:{level}丨金种子:{str(gold).split(".")[0]}')
                    if 'wx_' in nickname:
                        self.change_nickname()
                if resp['status'] == 401:
                    print('【账号信息】:账号失效正在尝试登录')
                    if self.elephant_user == 'f':
                        return False
                    authorization = Invalid_login.addtask(elephant_user=self.elephant_user,
                                                          elephant_pswd=self.elephant_pswd,
                                                          elephant_Task_ID=self.elephant_Task_ID)
                    the_revised_dict = get_json_data(json_path, self.len_new, 'authorization', authorization)
                    if write_json_data(the_revised_dict):
                        print('正在写入账号配置文件')
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
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
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

    def ddd(self):
        try:
            signstring = f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20', headers=headers).json()
            print(r1)




        except Exception as e:
            print(e)








    # 查询芦荟价格
    def the_query(self):
        try:
            signstring = f'page=1&pageSize=20&queryField=__{timi_new()}'
            headers = {
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',
                                  headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    price = r1['data']['rows'][3]['price']
                    self.market_sale(price)
        except Exception as e:
            print(e)

    # 卖芦荟
    def market_sale(self, price):
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
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r2 = requests.request('get', f'{host}/market/get-allow-sale-material-list?type=crop',
                                  headers=headers2).json()
            # print(r2)
            if 'status' in r2:
                if r2['status'] == 200:
                    if r2['data']['rows']:
                        packsackItemId = r2['data']['rows'][0]['packsackItemId']
                        quantity = r2['data']['rows'][0]['quantity']
                        price_new = float(price) - 0.00001
                        if price_new > 8:
                            signstring1 = f'_packsackItemId={packsackItemId}&price={str(price_new)[:9]}&quantity={quantity}_{timi_s}'
                            headers1 = {
                                'source': 'scsc',
                                'authorization': self.token,
                                'timestamp': str(timi_s),
                                'sign': sign(signstring1),
                                'signstring': signstring1,
                                'version': version,
                                'janalytics': 'c167f56858dc424ee3d617c9',
                                'Host': 'scsc.sc19319.com',
                                'User-Agent': 'okhttp/4.9.1',
                            }
                            b1 = {
                                "packsackItemId": packsackItemId,
                                "price": str(price_new)[:9],
                                "quantity": str(quantity)
                            }
                            r1 = requests.request('post', f'{host}/market/sale', headers=headers1, data=b1).json()
                            # print(r1)
                            if 'status' in r1:
                                if r1['status'] == 200:
                                    print(f'【上架芦荟】:数量:{quantity}丨价格:{str(price_new)[:9]}')
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
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',
                                  headers=headers1).json()
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
                            if float(datetime.datetime.now().hour) > 8:
                                self.cacel_sale(id_new)
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
                'janalytics': 'c167f56858dc424ee3d617c9',
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

    # 修改网名
    def change_nickname(self):
        try:
            time_aaa = timi_new()
            data = {'xing': '', 'xinglength': 'all', 'minglength': 'all', 'sex': 'all', 'dic': 'default', 'num': '1', }
            r1 = requests.request('post', 'https://www.qmsjmfb.com/', data=data).text
            names = re.findall('<ul><li>(.*?)</li>', r1)[0][:3]
            response = requests.post(f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={names}').json()
            name = response['translateResult'][0][0]['tgt'].replace(' ', '')[:5]
            b2 = {"nickname": name}
            signstring1 = f'_nickname={name}_{time_aaa}'
            head2 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': time_aaa,
                'sign': sign(signstring1),
                'signstring': signstring1,
                'version': '3.1.41954131',
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1'
            }
            r2 = requests.request('patch', f'{host}/user/nickname', headers=head2, data=b2).json()
            # print(r2)
            if 'status' in r2:
                if r2['status'] == 200:
                    print(f'【修改网名】:网名:{name}丨{r2["message"]}')
        except Exception as e:
            print(e)

    # 提现
    def withdraw(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/assets', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    cash = r1['data']['cash']
                    if float(cash) > 20:
                        signstring = f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'
                        headers = {
                            'authorization': self.token,
                            'timestamp': str(timi_new()),
                            'sign': sign(signstring),
                            'signstring': signstring,
                            'version': version,
                            'janalytics': 'c167f56858dc424ee3d617c9',
                            'Host': 'scsc.sc19319.com',
                            'User-Agent': 'okhttp/4.9.1',
                        }
                        b2 = {"withdrawId": "48c9478f-275e-4df8-b102-09b6e02f8a36"}
                        r2 = requests.request('post', 'http://scsc.sc19319.com/finance/withdraw', headers=headers,
                                              data=b2).json()
                        # print(r2)
                        if 'status' in r2:
                            if r2['status'] == 200:
                                print(f'【余额提现】:{r2["data"]}')
                        if 'status' in r2:
                            if r2['status'] == 500:
                                print(f'【余额提现】:{r2["message"]}')
        except Exception as e:
            print(e)

    # 好友数量
    def invitenum(self):
        global invited_new
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/invite/invitenum', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    invited_count = r1['data']['invited_count']
                    invited_second_count = r1['data']['invited_second_count']
                    print(f'【我的邀请】:直邀好友:{invited_count}丨间邀好友:{invited_second_count}')
                    if invited_count < 2:
                        signstring2 = f'__{timi_new()}'
                        headers2 = {
                            'source': 'scsc',
                            'authorization': self.token,
                            'timestamp': str(timi_new()),
                            'sign': sign(signstring2),
                            'signstring': signstring2,
                            'version': version,
                            'janalytics': 'c167f56858dc424ee3d617c9',
                            'Host': 'scsc.sc19319.com',
                            'User-Agent': 'okhttp/4.9.1',
                        }
                        r2 = requests.request('get', f'{host}/user', headers=headers2).json()
                        # print(resp)
                        if 'status' in r2:
                            if r2['status'] == 200:
                                invited_new.append(r2['data']['inner_id'])
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
                'janalytics': 'c167f56858dc424ee3d617c9',
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
                                if float(datetime.datetime.now().hour) > 8:
                                    self.the_query()
        except Exception as e:
            print(e)

    # 赠送金种子
    def give_gold(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r2 = requests.request('get', f'{host}/user', headers=headers).json()
            if 'status' in r2:
                if r2['status'] == 200:
                    if float(self.doneeNo) != 0:
                        gold = r2['data']['assets']['gold']
                        if float(gold) > float(self.innerId):
                            quantity = int(float(gold) / 1.1)
                            signstring = f'_doneeNo={self.doneeNo}&quantity={quantity}_{timi_new()}'
                            headers = {
                                'source': 'scsc',
                                'authorization': self.token,
                                'timestamp': str(timi_new()),
                                'sign': sign(signstring),
                                'signstring': signstring,
                                'version': version,
                                'janalytics': 'c167f56858dc424ee3d617c9',
                                'Host': 'scsc.sc19319.com',
                                'User-Agent': 'okhttp/4.9.1',
                            }
                            b1 = {
                                "quantity": quantity,
                                "doneeNo": self.doneeNo
                            }
                            r1 = requests.request('post', f'{host}/finance/give-gold', headers=headers, data=b1).json()
                            # print(r1)
                            if 'status' in r1:
                                if r1['status'] == 200:
                                    if r1['data']:
                                        print(f'【赠送种子】:赠送{quantity}种子给{self.doneeNo}成功')
                    else:
                        print(f'【赠送种子】:此账号未启动赠送功能')
        except Exception as e:
            print(e)

    def invitation(self):
        try:
            _innerId = float(bundled_def()) / 4
            signstring = f'_innerId={int(_innerId)}_{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            b1 = {"innerId": int(_innerId)}
            requests.request('post', f'{host}/friends/my-invitation', headers=headers, data=b1)
        except Exception as e:
            print(e)

    # 好友收益
    def winning_rewards(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/friends/winning-rewards/amount', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    if r1['data']['amount']:
                        gold = r1['data']['amount']['gold']
                        return gold
                    else:
                        return 0
        except Exception as e:
            print(e)

    # 查询实名
    def certification(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/certification/get-auth-status', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    if r1['data']['result']:
                        nick_name = r1['data']['nick_name']
                        return nick_name
                    else:
                        return '未实名'
        except Exception as e:
            print(e)

    # 图鉴奖励
    def crops_illustrated(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/game/crops/illustrated', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    crops = r1['data'][0]['crops']
                    for i in crops:
                        if i['ill_clover_award']:
                            if float(i['ill_clover_award']) > 1:
                                if i['is_finish']:
                                    if not i['is_getit']:
                                        if self.certification() != '未实名':
                                            signstring = f'_award_level={i["level"]}_{timi_new()}'
                                            headers = {
                                                'source': 'scsc',
                                                'authorization': self.token,
                                                'timestamp': str(timi_new()),
                                                'sign': sign(signstring),
                                                'signstring': signstring,
                                                'version': version,
                                                'janalytics': 'c167f56858dc424ee3d617c9',
                                                'Host': 'scsc.sc19319.com',
                                                'User-Agent': 'okhttp/4.9.1',
                                            }
                                            b2 = {"award_level": i['level']}
                                            r2 = requests.request('post', f'{host}/game/crops/illustrated/award',
                                                                  headers=headers, json=b2).json()
                                            if 'status' in r2:
                                                if r2['status'] == 200:
                                                    ill_clover_award = r2['data']['ill_clover_award']
                                                    print(
                                                        f'【图鉴奖励】:领取{i["crop_name"]}成就丨奖励{ill_clover_award}☘️')
                                                if r2['status'] == 500:
                                                    print(f'【图鉴奖励】:{r2["message"]}')
        except Exception as e:
            print(e)

    # 离线奖励
    def watched_ad(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r2 = requests.request('get', f'{host}/game/getAllData', headers=headers).json()
            # print(r2)
            if 'status' in r2:
                if r2['status'] == 200:
                    if 'offlineInfo' in r2['data']:
                        time.sleep(random.randint(1, 3))
                        off_minute = r2['data']['offlineInfo']['off_minute']
                        silver2 = float(r2['data']['silver']) / 1000000000000
                        time.sleep(1)
                        requests.request('post', f'{host}/game/watched-ad', headers=headers).json()
                        time.sleep(2)
                        r1 = requests.request('get', f'{host}/game/getAllData', headers=headers).json()
                        # print(r1)
                        if 'status' in r1:
                            if r1['status'] == 200:
                                silver1 = float(r1['data']['silver']) / 1000000000000
                                silver = str(silver1 - silver2)[:6]
                                print(f'【离线奖励】:翻倍离线{off_minute}分钟奖励🌱数量:{silver}t粒')
        except Exception as e:
            print(e)

    # 获取种子
    def user_ad(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/user/ad', headers=headers).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    max_time = r1['data']['max_time']
                    watch_time = r1['data']['watch_time']
                    added_time = r1['data']['added_time']
                    print(f'【获取种子】:获取🌱剩余{added_time + max_time - watch_time}次丨好友提供:{added_time}次')
                    if added_time + max_time - watch_time > 0:
                        time.sleep(random.randint(16, 19))
                        r2 = requests.request('post', f'{host}/game/watched-ad-forSilver', headers=headers).json()
                        # print(r2)
                        if 'status' in r2:
                            if r2['status'] == 200:
                                silver = float(r2['data']['silver']) / 1000000000000
                                print(f'【获取种子】:获得🌱:{int(silver)}t粒')
                                return True
                            if r2['status'] == 500:
                                message = r2['message']
                                print(f'【获取种子】:{message}')
                                return False
        except Exception as e:
            print(e)

    # 购买合成
    def synthetic(self):
        global id, g
        try:
            level = self.level_new()
            targetSite1 = random.randint(9, 11)
            signstring3 = f'_site=8&targetSite={targetSite1}_{timi_new()}'
            head3 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': timi_new(),
                'sign': sign(signstring3),
                'signstring': signstring3,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1'
            }
            b6 = {"site": int(8), "targetSite": int(targetSite1)}
            requests.request('post', f'{host}/game/crops/move', headers=head3, json=b6)
            while True:
                signstring1 = f'__{timi_new()}'
                h1 = {
                    'source': 'scsc',
                    'authorization': self.token,
                    'timestamp': str(timi_new()),
                    'sign': sign(signstring1),
                    'signstring': signstring1,
                    'version': version,
                    'janalytics': 'c167f56858dc424ee3d617c9',
                    'Host': 'scsc.sc19319.com',
                    'User-Agent': 'okhttp/4.9.1',
                }
                r1 = requests.request('get', f'{host}/game/getAllData', headers=h1).json()
                # print(r1)
                if 'status' in r1:
                    if r1['status'] == 200:
                        cropList = r1['data']['cropList']
                        crop_id = r1['data']['gameCoreDataDBid']
                        silver = float(r1['data']['silver']) / 1000000000000
                        # if silver < 6750:
                        #     print(f'【种植合成】:🌱不足6750t')
                        #     if not self.user_ad():
                        #         return False
                        site = 0
                        for i in cropList:
                            if not i:
                                signstring2 = f'_crop_id={crop_id}&site={site}_{self.time}'
                                head2 = {
                                    'source': 'scsc',
                                    'authorization': self.token,
                                    'timestamp': self.time,
                                    'sign': sign(signstring2),
                                    'signstring': signstring2,
                                    'version': '3.1.9',
                                    'Host': 'scsc.sc19319.com',
                                    'User-Agent': 'okhttp/4.9.1',
                                }
                                b2 = {"site": site, "crop_id": crop_id}
                                r2 = requests.request('post', f'{host}/game/crops/buy', headers=head2, data=b2).json()
                                # print(r2)
                                time.sleep(random.randint(1, 3) / 10)
                                if 'status' in r2:
                                    if r2['status'] == 200:
                                        if r2['message'] == '种子数量不足':
                                            level = self.level_new()
                                            print(f'【种植合成】:{r2["message"]}')
                                            if not self.user_ad():
                                                return False
                                    if r2['status'] == 500:
                                        print(f'【种植合成】:{r2["message"]}')
                                        return False
                            site += 1
                        r4 = requests.request('get', f'{host}/game/getAllData', headers=h1).json()
                        id_all = r4['data']['cropList']
                        break_flag = False
                        for i in range(12):
                            id = id_all[i]['level']  # 建筑物等级
                            if float(level) - float(id) > 9:
                                signstring5 = f'_site={i}_{timi_new()}'
                                head5 = {
                                    'source': 'scsc',
                                    'accept': 'application/json, text/plain, */*',
                                    'authorization': self.token,
                                    'timestamp': timi_new(),
                                    'sign': sign(signstring5),
                                    'signstring': signstring5,
                                    'version': '3.1.9',
                                    'Host': 'scsc.sc19319.com',
                                    'User-Agent': 'okhttp/4.9.1'
                                }
                                b5 = {"site": i}
                                r5 = requests.request('post', f'{host}/game/crops/sellForSilver', headers=head5,
                                                      data=b5).json()
                                if 'status' in r5:
                                    if r5['status'] == 200:
                                        print(f'【出售植物】:低级农作物卖出成功丨等级:{id}')
                            if id != 0:
                                for u in range(11):
                                    o = u + 1
                                    g = id_all[o]['level']  # 剩余建筑物等级
                                    if id == g:  # 剩余建筑物跟第一个建筑物
                                        xm = u + 2
                                        if xm != i + 1:
                                            xpp = i + 1
                                            # # 合成
                                            time.sleep(random.randint(1, 3) / 10)
                                            signstring3 = f'_site={xpp - 1}&targetSite={xm - 1}_{timi_new()}'
                                            head3 = {
                                                'source': 'scsc',
                                                'accept': 'application/json, text/plain, */*',
                                                'authorization': self.token,
                                                'timestamp': timi_new(),
                                                'sign': sign(signstring3),
                                                'signstring': signstring3,
                                                'version': version,
                                                'janalytics': 'c167f56858dc424ee3d617c9',
                                                'Content-Type': 'application/json',
                                                'Content-Length': '25',
                                                'Host': 'scsc.sc19319.com',
                                                'Connection': 'Keep-Alive',
                                                'Accept-Encoding': 'gzip',
                                                'Cookie': 'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b',
                                                'User-Agent': 'okhttp/4.9.1'
                                            }
                                            b3 = {"site": int(xpp - 1), "targetSite": int(xm - 1)}
                                            requests.request('post', f'{host}/game/crops/move', headers=head3, json=b3)
                                            # print(f'【种植合成】:位置{xpp}和位置{xm}合出{int(id) + 1}级农作物')
                                            break_flag = True
                                    if break_flag:
                                        break
                                if break_flag:
                                    break
        except:
            self.synthetic()

    # 农作物等级
    def level_new(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            resp = requests.request('get', f'{host}/user', headers=headers).json()
            if 'status' in resp:
                if resp['status'] == 200:
                    return float(resp['data']['level'])
        except Exception as e:
            print(e)

    # 转盘抽奖
    def propsraffle(self):
        try:
            while True:
                signstring = f'__{timi_new()}'
                headers = {
                    'source': 'scsc',
                    'authorization': self.token,
                    'timestamp': str(timi_new()),
                    'sign': sign(signstring),
                    'signstring': signstring,
                    'version': version,
                    'janalytics': 'c167f56858dc424ee3d617c9',
                    'Host': 'scsc.sc19319.com',
                    'User-Agent': 'okhttp/4.9.1',
                }
                r1 = requests.request('get', f'{host}/propsraffle/lucky', headers=headers).json()
                # print(r1)
                if 'status' in r1:
                    if r1['status'] == 200:
                        rows = r1['data']['rows']
                        vstate = r1['data']['vstate']
                        if rows == 5 or rows == 6 or rows == 7:
                            silver = r1['data']['silver']
                            print(f'【转盘抽奖】:获得种子:{silver}')
                        if rows == 1 or rows == 2 or rows == 3:
                            clover = r1['data']['clover']
                            print(f'【转盘抽奖】:获得三叶草:{clover}')
                        if rows == 4 or rows == 8:
                            print(f'【转盘抽奖】:翻倍奖励 未写')
                        # if 'get_game_lucky_LargeTurntables' in r1['data']:
                        #     get_game_lucky_LargeTurntables = r1['data']['get_game_lucky_LargeTurntables']
                        #     print(f'【转盘抽奖】:剩余抽奖次数:{get_game_lucky_LargeTurntables}')
                        if rows == '抽奖次数已用完':
                            # if vstate:

                            # signstring = f'__{timi_new()}'
                            # headers = {
                            #     'authorization': self.token,
                            #     'timestamp': str(timi_new()),
                            #     'sign': sign(signstring),
                            #     'signstring': signstring,
                            #     'version': version,
                            # 'janalytics':'c167f56858dc424ee3d617c9',
                            #     'Host': 'scsc.sc19319.com',
                            #     'User-Agent': 'okhttp/4.9.1',
                            # }
                            # r3 = requests.request('get', f'{host}/user', headers=headers).json()
                            # if 'status' in r3:
                            #     if r3['status'] == 200:
                            #         level = r3['data']['level']
                            #         if float(level) > 39:
                            #             time_oo = random.randint(160, 190) / 10
                            #             print(f'【转盘抽奖】:抽奖次数已用完丨等待{time_oo}秒获取抽奖机会')
                            #             time.sleep(time_oo)
                            #             r2 = requests.request('get', f'{host}/propsraffle/lucky/adverti/restore',headers=headers).json()
                            #             # print(r2)
                            #             if 'status' in r2:
                            #                 if r2['status'] == 200:
                            #                     print(f'【转盘抽奖】:{r2["message"]}')
                            #                 if r2['status'] == 500:
                            #                     print(f'【转盘抽奖】:{r2["message"]}')
                            #                     break
                            #             time.sleep(random.randint(10, 15) / 10)
                            #         else:
                            #             break
                            # else:
                            break
                time.sleep(random.randint(8, 15) / 10)
        except Exception as e:
            print(e)

    # 绑定邀请码
    def friends_invitation(self):
        try:
            signstring = f'__{timi_new()}'
            headers = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/friends', headers=headers).json()
            if 'status' in r1:
                if r1['status'] == 200:
                    myInviteter = r1['data']['myInviteter']
                    if myInviteter:
                        nickname = myInviteter['user']['nickname']
                        name = self.certification()
                        if name == '未实名':
                            weishim.append(self.token)
                        print(f'【查邀请人】:我的邀请人:{nickname}丨实名:{name}')
                    else:
                        if self.innerId != '0':
                            self.invitation()
        except Exception as e:
            print(e)

    # 添加三叶草
    def add_clover(self):
        global golden_seed
        try:
            signstring = f'__{timi_new()}'
            headers1 = {
                'source': 'scsc',
                'authorization': self.token,
                'timestamp': str(timi_new()),
                'sign': sign(signstring),
                'signstring': signstring,
                'version': version,
                'janalytics': 'c167f56858dc424ee3d617c9',
                'Host': 'scsc.sc19319.com',
                'User-Agent': 'okhttp/4.9.1',
            }
            r1 = requests.request('get', f'{host}/assets/clovers', headers=headers1).json()
            # print(r1)
            if 'status' in r1:
                if r1['status'] == 200:
                    clover = r1['data']['clover']
                    used_clover = r1['data']['used_clover']
                    quantity = float(clover) - float(used_clover)
                    print(f'【参与抽奖】:参与抽奖的☘️:{used_clover}')
                    if self.certification() != '未实名':
                        if quantity > 1:
                            signstring = f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(quantity)}_{timi_new()}'
                            headers2 = {
                                'source': 'scsc',
                                'authorization': self.token,
                                'timestamp': str(timi_new()),
                                'sign': sign(signstring),
                                'signstring': signstring,
                                'version': version,
                                'janalytics': 'c167f56858dc424ee3d617c9',
                                'Host': 'scsc.sc19319.com',
                                'User-Agent': 'okhttp/4.9.1',
                            }
                            b2 = {"lotteryId": "13f02ff5-f8db-4ddc-9e9a-3d328a211fff", "quantity": int(quantity)}
                            r2 = requests.request('post', f'{host}/lottery/add-stake', headers=headers2, data=b2).json()
                            # print(r2)
                            if 'status' in r2:
                                if r2['status'] == 200:
                                    print(f'【参与抽奖】:添加☘️:{r2["data"]["isSuccess"]}丨数量:{quantity}')
                                if r2['status'] == 500:
                                    print(f'【参与抽奖】:添加☘️:{r2["message"]}')
            r3 = requests.request('get', f'{host}/lottery', headers=headers1).json()
            # print(r3)
            gold = self.winning_rewards()
            if 'status' in r3:
                if r3['status'] == 200:
                    day_get_gold_quantity = r3['data'][0]['day_get_gold_quantity']
                    golden_seed += float(day_get_gold_quantity)
                    value = r3['data'][1]['value']
                    join_number = r3['data'][0]['join_number']
                    totalValue = int(float(r3['data'][0]['totalValue']))  # 参与三叶草
                    det = float(value / totalValue) * 10000
                    cvy = totalValue / join_number
                    print(f'【参与抽奖】:预计每天中{str(day_get_gold_quantity)[:6]}颗金种子丨好友收益:{str(gold)[:6]}')
                    print(f'【抽奖统计】:每1万☘️中{str(det)[:6]}颗金种子丨☘️人均:{str(cvy)[:7]}️')
        except Exception as e:
            print(e)

    # 添加营养
    def energy(self):
        try:
            while True:
                signstring = f'__{timi_new()}'
                headers = {
                    'source': 'scsc',
                    'authorization': self.token,
                    'timestamp': str(timi_new()),
                    'sign': sign(signstring),
                    'signstring': signstring,
                    'version': version,
                    'janalytics': 'c167f56858dc424ee3d617c9',
                    'Host': 'scsc.sc19319.com',
                    'User-Agent': 'okhttp/4.9.1',
                }
                r1 = requests.request('get', f'{host}/energy/general', headers=headers).json()
                # print(r1)
                if 'status' in r1:
                    if r1['status'] == 200:
                        ordinary_water = r1['data']['ordinary_water']
                        ordinary_fertilizer = r1['data']['ordinary_fertilizer']
                        videoStatus = r1['data']['videoStatus']
                        waterVideoKey = r1['data']['waterVideoKey']
                        print(
                            f'【我的营养】:肥料:{str(ordinary_fertilizer).split(".")[0]}丨水滴:{str(ordinary_water).split(".")[0]}')
                        if float(ordinary_fertilizer) < 96:
                            if videoStatus:
                                time.sleep(random.randint(160, 180) / 10)
                                fertilizer = 99 - float(ordinary_fertilizer)
                                b2 = {"fertilizer": str(fertilizer).split('.')[0]}
                                r2 = requests.request('post', f'{host}/video/general/nutrition/fadverti',
                                                      headers=headers).json()
                                # print(r2)
                                if 'status' in r2:
                                    if r2['status'] == 200:
                                        print(f'【购买肥料】:看广告获取肥料:{r2["message"]}')
                                    if r2['status'] == 500:
                                        print(f'【购买肥料】:看广告获取肥料:{r2["message"]}')
                                        break

                                if float(ordinary_fertilizer) < 78:
                                    fertilizer = 80 - float(ordinary_fertilizer)
                                    signstring4 = f'_fertilizer={int(fertilizer)}_{timi_new()}'
                                    headers4 = {
                                        'source': 'scsc',
                                        'authorization': self.token,
                                        'timestamp': str(timi_new()),
                                        'sign': sign(signstring4),
                                        'signstring': signstring4,
                                        'version': version,
                                        'janalytics': 'c167f56858dc424ee3d617c9',
                                        'Host': 'scsc.sc19319.com',
                                        'User-Agent': 'okhttp/4.9.1',
                                    }
                                    b4 = {"fertilizer": int(fertilizer)}
                                    r4 = requests.request('post', f'{host}/energy/general/buy/fertilizer',
                                                          headers=headers4, data=b4).json()
                                    # print(r4)
                                    if 'status' in r4:
                                        if r4['status'] == 200:
                                            print(f'【购买肥料】:购买肥料:{r4["message"]}丨数量:{int(fertilizer)}')
                                        if r4['status'] == 500:
                                            print(f'【购买肥料】:购买肥料:{r4["message"]}丨数量:{int(fertilizer)}')
                                            quantity = r4["message"].split('-')[1]
                                            signstring6 = f'__{timi_new()}'
                                            headers6 = {
                                                'source': 'scsc',
                                                'authorization': self.token,
                                                'timestamp': str(timi_new()),
                                                'sign': sign(signstring6),
                                                'signstring': signstring6,
                                                'version': version,
                                                'janalytics': 'c167f56858dc424ee3d617c9',
                                                'Host': 'scsc.sc19319.com',
                                                'User-Agent': 'okhttp/4.9.1',
                                            }
                                            r6 = requests.request('get', f'{host}/user', headers=headers6).json()
                                            if 'status' in r6:
                                                if r6['status'] == 200:
                                                    inner_id = r6['data']['inner_id']
                                                    if give_gold(inner_id, float(quantity) + 1):
                                                        self.energy()
                        if float(ordinary_water) < 880:
                            if waterVideoKey:
                                time.sleep(random.randint(160, 180) / 10)
                                water = 999 - float(ordinary_water)
                                b3 = {"water": str(water).split('.')[0]}
                                r3 = requests.request('post', f'{host}/video/general/nutrition/wadverti',
                                                      headers=headers).json()
                                # print(r3)     waterVideoKey
                                if 'status' in r3:
                                    if r3['status'] == 200:
                                        print(f'【购买水滴】:看广告获取水滴:{r3["message"]}')
                                    if r3['status'] == 500:
                                        print(f'【购买水滴】:看广告获取水滴:{r3["message"]}')
                                        break
                                if float(ordinary_water) < 780:
                                    water = 800 - float(ordinary_water)
                                    signstring5 = f'_water={int(water)}_{timi_new()}'
                                    headers5 = {
                                        'source': 'scsc',
                                        'authorization': self.token,
                                        'timestamp': str(timi_new()),
                                        'sign': sign(signstring5),
                                        'signstring': signstring5,
                                        'version': version,
                                        'janalytics': 'c167f56858dc424ee3d617c9',
                                        'Host': 'scsc.sc19319.com',
                                        'User-Agent': 'okhttp/4.9.1',
                                    }
                                    b5 = {"water": int(water)}
                                    r5 = requests.request('post', f'{host}/energy/general/buy/water', headers=headers5,
                                                          data=b5).json()
                                    # print(r5)
                                    if 'status' in r5:
                                        if r5['status'] == 200:
                                            print(f'【购买水滴】:购买水滴:{r5["message"]}丨数量:{int(water)}')
                                        if r5['status'] == 500:
                                            print(f'【购买水滴】:购买水滴:{r5["message"]}丨数量:{int(water)}')
                                            quantity = r5["message"].split('-')[1]
                                            signstring6 = f'__{timi_new()}'
                                            headers6 = {
                                                'source': 'scsc',
                                                'authorization': self.token,
                                                'timestamp': str(timi_new()),
                                                'sign': sign(signstring6),
                                                'signstring': signstring6,
                                                'version': version,
                                                'janalytics': 'c167f56858dc424ee3d617c9',
                                                'Host': 'scsc.sc19319.com',
                                                'User-Agent': 'okhttp/4.9.1',
                                            }
                                            r6 = requests.request('get', f'{host}/user', headers=headers6).json()
                                            if 'status' in r6:
                                                if r6['status'] == 200:
                                                    inner_id = r6['data']['inner_id']
                                                    if give_gold(inner_id, float(quantity) + 1):
                                                        self.energy()
                        break
        except Exception as e:
            print(e)


def bundled_def():
    bundled_id_new = ['5570536', '7750212', '7911652', '7911680', '7805624']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]


# 版本验证
def version_of_the_validation():
    return str((98 - 56) / 10)

def ubbbf():
    print('卡密验证通过   ✅')


def sc2():
    return "19319#$%^&*((*"


def OO00OO0OO0OO00OO00o0():
    return hashlib.md5(
        (socket.gethostbyname(get_ip()) + socket.getfqdn(socket.gethostname())).encode('utf-8')).hexdigest().upper()


def get_ip():
    return re.findall('ip: (.*) ', requests.request('get', 'https://dev.kdlapi.com/testproxy',
                                                    headers={"Accept-Encoding": "Gzip"}).text)[0]


def gitee_validation():
    return requests.request('get', f'{git}{kvkv()}/validation').json()


def gitee_edition():
    try:
        return requests.get(f'{git}{kvkv()}/edition').json()
    except:
        sys.exit(0)


# 更新验证
def O000OO000O0O00OOO00():
    try:
        edition = gitee_edition()
        if version_of_the_validation() < edition['CityEarth']['edition']:
            print(f'当前版本=>> {version_of_the_validation()}' + f'丨远程版本=>> {edition["CityEarth"]["edition"]}   ❌')
            print(f'更新内容=>>{edition["CityEarth"]["content"]}')
        else:
            print(f'当前版本=>> {version_of_the_validation()}' + f'丨远程版本=>> {edition["CityEarth"]["edition"]}   ✅')
            print(f'更新内容=>> {edition["CityEarth"]["content"]}')
    except Exception as e:
        print(e)


def sc3():
    return "&^%$#@#RFGHJ%^KAfghfg"


if __name__ == '__main__':
    start()
