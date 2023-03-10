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
@ cron: * * * 12 *
@ new Env('生城世朝手动上架芦荟')
@ 脚本会取消上架的农作物再出售芦荟
@ 价格设置错了重新运行一次脚本    一定看好价格再运行脚本
"""
##################################配置区##################################
price = '50'                    # 设置芦荟价格
price_floating = 99     # 设置芦荟价格浮动价格 上面价格加随机加-0.001到-0.099之间
##################################配置区##################################

##################################下面不要动##################################
application ='ce_token'#line:1
token =''''''#line:2
version ='3.1.419541311'#line:3
git ='https://gitee.com'#line:4
host ='http://scsc.sc19319.com'#line:5
golden_seed =0 #line:6
msg_list =[]#line:7
def start ():#line:9
    try :#line:10
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:11
        O000OO0O00OO00O00 ()#line:12
        O00O0OOOOO0O00000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:13
        print (f"==========共找到{len(O00O0OOOOO0O00000)}个账号==========")#line:14
        for OOOO00O00O00OOOOO in O00O0OOOOO0O00000 :#line:15
            OO0O0O0O0OOOO00OO =[]#line:16
            print (f"------------正在执行第{O00O0OOOOO0O00000.index(OOOO00O00O00OOOOO) + 1}个账号------------")#line:17
            O00O00OO0O00O0O00 =CityEarth (OOOO00O00O00OOOOO ,OO0O0O0O0OOOO00OO )#line:18
            if O00O00OO0O00O0O00 .base_info ():#line:20
                O00O00OO0O00O0O00 .sealing ()#line:22
                O00O00OO0O00O0O00 .query_to_sell ()#line:24
                O00O00OO0O00O0O00 .game_map ()#line:26
                O00O00OO0O00O0O00 .market_sale ()#line:28
    except Exception as OO00OO0O0OOOOO0O0 :#line:30
        print (OO00OO0O0OOOOO0O0 )#line:31
def O000OO0O00OO00O00 ():#line:34
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:35
        pass #line:36
    else :#line:37
        exit (1 )#line:38
def kvkv ():#line:39
    return '/vastzzzl/vastzzzl/raw/master'#line:40
def sign (O0OOO0OOOO0O00000 ):#line:43
    OO0O000O0OO0OO0OO =hashlib .md5 (O0OOO0OOOO0O00000 .encode ()).hexdigest ()#line:44
    O000O00OO0OOO0O0O ="scsc%^&*"+OO0O000O0OO0OO0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:45
    OO0O00000OOO0O00O =hashlib .md5 (O000O00OO0OOO0O0O .encode ()).hexdigest ()#line:46
    return OO0O00000OOO0O00O #line:47
def timi_new ():#line:49
    return str (int (time .time ()*1000 ))#line:50
class CityEarth :#line:53
    def __init__ (OO0O0OOO0000OO0OO ,OO00OOOOO000OOO00 ,O0O00O0O0000OOOO0 ):#line:55
        try :#line:56
            OO0O0OOO0000OO0OO .msg =O0O00O0O0000OOOO0 #line:57
            OO0O0OOO0000OO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:58
            OO0O0OOO0000OO0OO .token =OO00OOOOO000OOO00 ['authorization']#line:59
        except :#line:60
            print ('变量格式错误')#line:61
    def base_info (OOOOO0000OOO0O000 ):#line:64
        try :#line:65
            OO0O00OO0O0OO0OO0 =f'__{timi_new()}'#line:66
            OOO000O0OO0OOOOO0 ={'source':'scsc','authorization':OOOOO0000OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0O0OO0OO0 ),'signstring':OO0O00OO0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:77
            OO00O0O00O0OO0000 =requests .request ('get',f'{host}/user',headers =OOO000O0OO0OOOOO0 ).json ()#line:78
            if 'status'in OO00O0O00O0OO0000 :#line:80
                if OO00O0O00O0OO0000 ['status']==200 :#line:81
                    OO00O0O0O000O0OOO =OO00O0O00O0OO0000 ['data']['nickname']#line:82
                    OO00OO0O000O0O00O =OO00O0O00O0OO0000 ['data']['inner_id']#line:83
                    O0OO0O0O0OOOOOO00 =OO00O0O00O0OO0000 ['data']['assets']['gold']#line:84
                    O00O0OOOO0O0O00O0 =OO00O0O00O0OO0000 ['data']['level']#line:85
                    print (f'【账号信息】:昵称:{OO00O0O0O000O0OOO[:5]}丨ID:{OO00OO0O000O0O00O}丨等级:{O00O0OOOO0O0O00O0}丨金种子:{str(O0OO0O0O0OOOOOO00).split(".")[0]}')#line:86
                if OO00O0O00O0OO0000 ['status']==401 :#line:87
                    print (OO00O0O00O0OO0000 ['message'])#line:88
                    OOOOO0000OOO0O000 .msg .append ('有账号失效了')#line:89
                    return False #line:90
                if OO00O0O00O0OO0000 ['status']==500 :#line:91
                    return False #line:92
            return True #line:93
        except Exception as O000OO0OOO0OO00O0 :#line:94
            print (O000OO0OOO0OO00O0 )#line:95
    def sealing (O0OO00OO00OOOOO00 ):#line:98
        try :#line:99
            O0O00O000000OO0O0 =f'__{timi_new()}'#line:100
            OO000OO0O0OO00O00 ={'authorization':O0OO00OO00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000000OO0O0 ),'signstring':O0O00O000000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:110
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO000OO0O0OO00O00 )#line:111
            requests .request ('get',f'{host}/packsack/list',headers =OO000OO0O0OO00O00 )#line:112
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO000OO0O0OO00O00 )#line:113
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO000OO0O0OO00O00 )#line:114
            requests .request ('get',f'{host}/user',headers =OO000OO0O0OO00O00 )#line:115
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO000OO0O0OO00O00 )#line:116
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO000OO0O0OO00O00 )#line:117
            requests .request ('post',f'{host}/announcement/announcement',headers =OO000OO0O0OO00O00 )#line:118
            requests .request ('get',f'{host}/game/getAllData',headers =OO000OO0O0OO00O00 )#line:119
            requests .request ('get',f'{host}/assets',headers =OO000OO0O0OO00O00 )#line:120
        except Exception as OO0OO00O0O00OOOO0 :#line:121
            print (OO0OO00O0O00OOOO0 )#line:122
    def market_sale (OO0000O0OO000OO0O ):#line:125
        try :#line:126
            O0000O0000O00OO0O =timi_new ()#line:127
            O0O00O00O00O0OO0O =f'type=crop__{O0000O0000O00OO0O}'#line:128
            OO000O0OO000000OO ={'source':'scsc','authorization':OO0000O0OO000OO0O .token ,'timestamp':str (O0000O0000O00OO0O ),'sign':sign (O0O00O00O00O0OO0O ),'signstring':O0O00O00O00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:139
            O000OOOOO0OOOOOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO000O0OO000000OO ).json ()#line:140
            if 'status'in O000OOOOO0OOOOOO0 :#line:142
                if O000OOOOO0OOOOOO0 ['status']==200 :#line:143
                    if O000OOOOO0OOOOOO0 ['data']['rows']:#line:144
                        O0O0OO0OO0O0OO0OO =O000OOOOO0OOOOOO0 ['data']['rows'][0 ]['packsackItemId']#line:145
                        OOOOO00O00O0OO0OO =O000OOOOO0OOOOOO0 ['data']['rows'][0 ]['quantity']#line:146
                        O0O00000O000OOOOO =float (price )-float (random .randint (1 ,price_floating )*0.001 )#line:147
                        O00O00OO00O000OO0 =f'_packsackItemId={O0O0OO0OO0O0OO0OO}&price={str(O0O00000O000OOOOO)[:8]}&quantity={OOOOO00O00O0OO0OO}_{O0000O0000O00OO0O}'#line:148
                        OOOOO0O00O0000O00 ={'source':'scsc','authorization':OO0000O0OO000OO0O .token ,'timestamp':str (O0000O0000O00OO0O ),'sign':sign (O00O00OO00O000OO0 ),'signstring':O00O00OO00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:159
                        OO0OOOO00O0O0OO00 ={"packsackItemId":O0O0OO0OO0O0OO0OO ,"price":str (O0O00000O000OOOOO )[:8 ],"quantity":str (OOOOO00O00O0OO0OO )}#line:164
                        O0O00OO00O0O00O00 =requests .request ('post',f'{host}/market/sale',headers =OOOOO0O00O0000O00 ,data =OO0OOOO00O0O0OO00 ).json ()#line:165
                        if 'status'in O0O00OO00O0O00O00 :#line:167
                            if O0O00OO00O0O00O00 ['status']==200 :#line:168
                                print (f'【上架芦荟】:数量:{OOOOO00O00O0OO0OO}丨价格:{str(O0O00000O000OOOOO)[:8]}')#line:169
        except Exception as OOO0O00O0000OO0O0 :#line:170
            print (OOO0O00O0000OO0O0 )#line:171
    def game_map (OO0O0OO0000OOO0OO ):#line:174
        try :#line:175
            OOOO000OOOO0O00O0 =f'__{timi_new()}'#line:176
            O0000O0O00O0000O0 ={'source':'scsc','authorization':OO0O0OO0000OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOOO0O00O0 ),'signstring':OOOO000OOOO0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:187
            OOO0OO0O0OOOOOO0O =requests .request ('get',f'{host}/game/map',headers =O0000O0O00O0000O0 ).json ()#line:188
            if 'status'in OOO0OO0O0OOOOOO0O :#line:190
                if OOO0OO0O0OOOOOO0O ['status']==200 :#line:191
                    for OOO0000OO0O00OO0O in OOO0OO0O0OOOOOO0O ['data']['list'][0 ]['crops']:#line:192
                        O00OOOOOOO000O0OO =OOO0000OO0O00OO0O ['level']#line:194
                        if O00OOOOOOO000O0OO ==41 :#line:195
                            O000OO0000O0O00OO =OOO0000OO0O00OO0O ['crop_name']#line:196
                            OO00O0O000000O0OO =OOO0000OO0O00OO0O ['count']#line:197
                            if OO00O0O000000O0OO >0 :#line:198
                                print (f'【农业资产】:{O000OO0000O0O00OO}丨数量:{OO00O0O000000O0OO}')#line:199
        except Exception as OOOOOO0O000OOO0OO :#line:200
            print (OOOOOO0O000OOO0OO )#line:201
    def query_to_sell (O00000O0O0O00OOOO ):#line:205
        try :#line:206
            OO00000OO000O0OO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:207
            OOOOOO0O00OO0OO00 ={'source':'scsc','authorization':O00000O0O0O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO000O0OO0 ),'signstring':OO00000OO000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:218
            OO0OOO0OOO0OO0OOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOOOO0O00OO0OO00 ).json ()#line:219
            if 'status'in OO0OOO0OOO0OO0OOO :#line:221
                if OO0OOO0OOO0OO0OOO ['status']==200 :#line:222
                    for OO00OO00O0OO0OOOO in OO0OOO0OOO0OO0OOO ['data']['rows']:#line:223
                        OO0O0O0O00O0O0O0O =OO00OO00O0OO0OOOO ['materialKey']#line:224
                        OOOO0OOO00OO000OO =OO00OO00O0OO0OOOO ['quantity']#line:225
                        O0000O0O00OO0OO0O =OO00OO00O0OO0OOOO ['price']#line:226
                        OOOOO0000O0OO0OO0 =OO00OO00O0OO0OOOO ['saleState']#line:227
                        if OOOOO0000O0OO0OO0 ==0 :#line:228
                            print (f'【出售订单】:名称:{OO0O0O0O00O0O0O0O}丨数量:{OOOO0OOO00OO000OO}丨价格:{O0000O0O00OO0OO0O}')#line:229
                            O0OOO0000O0O0O000 =OO00OO00O0OO0OOOO ['id']#line:230
                            O00000O0O0O00OOOO .cacel_sale (O0OOO0000O0O0O000 )#line:231
        except Exception as O0O000O0OO0OOOOOO :#line:237
            print (O0O000O0OO0OOOOOO )#line:238
    def cacel_sale (OOOOO000OO00OO00O ,O00O00O0000000OO0 ):#line:242
        try :#line:243
            O00O000O00O00OOO0 =f'_saleId={O00O00O0000000OO0}_{timi_new()}'#line:244
            O0O000OOOO00O000O ={'source':'scsc','authorization':OOOOO000OO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O00O00OOO0 ),'signstring':O00O000O00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            OOO000O0OOOO00O00 ={"saleId":O00O00O0000000OO0 }#line:258
            OOOO0O000000OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O000OOOO00O000O ,data =OOO000O0OOOO00O00 ).json ()#line:259
            if 'status'in OOOO0O000000OOOOO :#line:261
                if OOOO0O000000OOOOO ['status']==200 :#line:262
                    print (f'【下架出售】:{OOOO0O000000OOOOO["data"]}')#line:263
        except Exception as OOOOOO0OO0OO0O0O0 :#line:264
            print (OOOOOO0OO0OO0O0O0 )#line:265
def OO00OO0OO0OO00OO00o0 ():#line:266
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:267
def get_ip ():#line:269
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:270
def gitee_validation ():#line:272
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:273
if __name__ =='__main__':#line:278
    start ()#line:279
