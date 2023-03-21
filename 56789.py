try :#line:2
    import re #line:3
    import os #line:4
    import sys #line:5
    import time #line:6
    import hashlib #line:7
    import requests #line:8
    import random #line:9
    import json #line:10
    import socket #line:11
    from notify import send #line:12
except Exception as E :#line:13
    t =re .findall ("d '(.*?)'",str (E ))[0 ]#line:14
    print (f'{t}依赖未安装')#line:15
    sys .exit ()#line:16
"""
@ cron: * * * 8 *
@ new Env('手动出售芦荟')
@ 脚本会取消上架的农作物再出售芦荟
"""#line:22
application ='ce_token'#line:25
version ='3.1.4195543511'#line:26
git ='https://gitee.com'#line:27
host ='http://scsc.sc19319.com'#line:28
golden_seed =0 #line:29
msg_list =[]#line:30
def O000OO0O00OO00O00 ():#line:33
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:34
        pass #line:35
    else :#line:36
        exit (1 )#line:37
def kvkv ():#line:38
    return '/vastzzzl/vastzzzl/raw/master'#line:39
def OO00OO0OO0OO00OO00o0 ():#line:42
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:43
def get_ip ():#line:45
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:46
def gitee_validation ():#line:48
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:49
def sign (O00OO0O000O0O00O0 ):#line:52
    OO0000OOO00O0O000 =hashlib .md5 (O00OO0O000O0O00O0 .encode ()).hexdigest ()#line:53
    OO000O0000O0O0O0O ="scsc%^&*"+OO0000OOO00O0O000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOO0O00OO00000OOO =hashlib .md5 (OO000O0000O0O0O0O .encode ()).hexdigest ()#line:55
    return OOO0O00OO00000OOO #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0O00OOOOOOOO000O ,O0OOO0OO0O0000000 ,OO00O0O0O000O000O ):#line:64
        try :#line:65
            O0O00OOOOOOOO000O .msg =OO00O0O0O000O000O #line:66
            O0O00OOOOOOOO000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0O00OOOOOOOO000O .token =O0OOO0OO0O0000000 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O000O0O00000OO0O0 ):#line:73
        try :#line:74
            O0O000OOOOO0O0OOO =f'__{timi_new()}'#line:75
            O00000OOOO0OO000O ={'source':'scsc','authorization':O000O0O00000OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOOO0O0OOO ),'signstring':O0O000OOOOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O0OO00O0OO0O0O0O0 =requests .request ('get',f'{host}/user',headers =O00000OOOO0OO000O ).json ()#line:87
            if 'status'in O0OO00O0OO0O0O0O0 :#line:89
                if O0OO00O0OO0O0O0O0 ['status']==200 :#line:90
                    O0OOOO0O000O0O0O0 =O0OO00O0OO0O0O0O0 ['data']['nickname']#line:91
                    OOOO0OO0OOO0000OO =O0OO00O0OO0O0O0O0 ['data']['inner_id']#line:92
                    OOO00O0O000000OO0 =O0OO00O0OO0O0O0O0 ['data']['assets']['gold']#line:93
                    OO0O00O00O0OOO000 =O0OO00O0OO0O0O0O0 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O0OOOO0O000O0O0O0[:5]}丨ID:{OOOO0OO0OOO0000OO}丨等级:{OO0O00O00O0OOO000}丨金种子:{str(OOO00O0O000000OO0).split(".")[0]}')#line:95
                if O0OO00O0OO0O0O0O0 ['status']==401 :#line:96
                    print (O0OO00O0OO0O0O0O0 ['message'])#line:97
                    O000O0O00000OO0O0 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O0OO00O0OO0O0O0O0 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0OOOOOOOOOO0OO00 :#line:103
            print (O0OOOOOOOOOO0OO00 )#line:104
    def sealing (OOO00OO0OOOOO000O ):#line:107
        try :#line:108
            O0O0OOOOOOOO0O0OO =f'__{timi_new()}'#line:109
            O000OOOO0OOO0OOOO ={'authorization':OOO00OO0OOOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOOOOO0O0OO ),'signstring':O0O0OOOOOOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O000OOOO0OOO0OOOO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O000OOOO0OOO0OOOO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O000OOOO0OOO0OOOO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O000OOOO0OOO0OOOO )#line:123
            requests .request ('get',f'{host}/user',headers =O000OOOO0OOO0OOOO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O000OOOO0OOO0OOOO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O000OOOO0OOO0OOOO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O000OOOO0OOO0OOOO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O000OOOO0OOO0OOOO )#line:128
            requests .request ('get',f'{host}/assets',headers =O000OOOO0OOO0OOOO )#line:129
        except Exception as O0000O00OOOOOOO00 :#line:130
            print (O0000O00OOOOOOO00 )#line:131
    def market_sale_buy (O0O00O0O0000000OO ,_OOOO0OOO0OOOOOOOO ,O0OO0O00O0OO0OOOO ):#line:139
        try :#line:140
            O000O00OO00O000O0 =timi_new ()#line:141
            O00O0O000OOO000OO =f'_askToBuyId={_OOOO0OOO0OOOOOOOO}&quantity={O0OO0O00O0OO0OOOO}_{O000O00OO00O000O0}'#line:142
            OO0O000O00000O0O0 ={'source':'scsc','authorization':O0O00O0O0000000OO .token ,'timestamp':str (O000O00OO00O000O0 ),'sign':sign (O00O0O000OOO000OO ),'signstring':O00O0O000OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O000OOOOOOO000000 ={"askToBuyId":_OOOO0OOO0OOOOOOOO ,"quantity":O0OO0O00O0OO0OOOO }#line:154
            O0000O0O0OOOO0O00 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OO0O000O00000O0O0 ,data =O000OOOOOOO000000 ).json ()#line:155
            if 'status'in O0000O0O0OOOO0O00 :#line:157
                if O0000O0O0OOOO0O00 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                else :#line:160
                    print (O0000O0O0OOOO0O00 )#line:161
                    exit ()#line:162
        except Exception as OOO00OOOOOOO0O0O0 :#line:163
            print (OOO00OOOOOOO0O0O0 )#line:164
    def game_map (OO00OO000O0OOOOO0 ,_O00000OO0000O0OO0 ):#line:167
        try :#line:168
            O000OO0O00OO0O0OO =f'__{timi_new()}'#line:169
            O0000000O0000O0O0 ={'source':'scsc','authorization':OO00OO000O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O00OO0O0OO ),'signstring':O000OO0O00OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:180
            OOOOOOOO0OOO0O00O =requests .request ('get',f'{host}/game/map',headers =O0000000O0000O0O0 ).json ()#line:181
            if 'status'in OOOOOOOO0OOO0O00O :#line:183
                if OOOOOOOO0OOO0O00O ['status']==200 :#line:184
                    for O00OOOO0OO00OOOO0 in OOOOOOOO0OOO0O00O ['data']['list'][0 ]['crops']:#line:185
                        OOOO0OO00000000OO =O00OOOO0OO00OOOO0 ['level']#line:187
                        if OOOO0OO00000000OO ==41 :#line:188
                            O00O000OO000OO00O =O00OOOO0OO00OOOO0 ['crop_name']#line:189
                            OOOOOOOO0OO00OOOO =O00OOOO0OO00OOOO0 ['count']#line:190
                            if OOOOOOOO0OO00OOOO >0 :#line:191
                                print (f'【农业资产】:{O00O000OO000OO00O}丨数量:{OOOOOOOO0OO00OOOO}')#line:192
                                OO00OO000O0OOOOO0 .market_sale_buy (_O00000OO0000O0OO0 ,OOOOOOOO0OO00OOOO )#line:193
        except Exception as OO0OOOO00O00O0O00 :#line:194
            print (OO0OOOO00O00O0O00 )#line:195
    def query_to_sell (O00OO00OOOOO00O00 ):#line:199
        try :#line:200
            O000OOO00O0OOO000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:201
            O0OO0OOOOO00OO000 ={'source':'scsc','authorization':O00OO00OOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O0OOO000 ),'signstring':O000OOO00O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            OO0O000OO000O0OOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO0OOOOO00OO000 ).json ()#line:213
            if 'status'in OO0O000OO000O0OOO :#line:215
                if OO0O000OO000O0OOO ['status']==200 :#line:216
                    for O0OO0O00O00O0O000 in OO0O000OO000O0OOO ['data']['rows']:#line:217
                        OO0O00O000O0O0O0O =O0OO0O00O00O0O000 ['materialKey']#line:218
                        OO00OOO0OOOOOOOO0 =O0OO0O00O00O0O000 ['quantity']#line:219
                        O00OO00OO0OO0OOOO =O0OO0O00O00O0O000 ['price']#line:220
                        OOOO0O000OOO00O0O =O0OO0O00O00O0O000 ['saleState']#line:221
                        if OOOO0O000OOO00O0O ==0 :#line:222
                            print (f'【出售订单】:名称:{OO0O00O000O0O0O0O}丨数量:{OO00OOO0OOOOOOOO0}丨价格:{O00OO00OO0OO0OOOO}')#line:223
                            O0O00OO0OOOO0OOOO =O0OO0O00O00O0O000 ['id']#line:224
                            O00OO00OOOOO00O00 .cacel_sale (O0O00OO0OOOO0OOOO )#line:225
        except Exception as OO0000OO00O0OO0OO :#line:231
            print (OO0000OO00O0OO0OO )#line:232
    def cacel_sale (O0000O00O0O00OO00 ,OOO0OO0OO0O0O0OOO ):#line:236
        try :#line:237
            O0O0000O00OOOO00O =f'_saleId={OOO0OO0OO0O0O0OOO}_{timi_new()}'#line:238
            OOOO0OOO00O00OOO0 ={'source':'scsc','authorization':O0000O00O0O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O00OOOO00O ),'signstring':O0O0000O00OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            OO0O0OOO0OOOOO0O0 ={"saleId":OOO0OO0OO0O0O0OOO }#line:252
            OO0000OO0O0000O0O =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOO0OOO00O00OOO0 ,data =OO0O0OOO0OOOOO0O0 ).json ()#line:253
            if 'status'in OO0000OO0O0000O0O :#line:255
                if OO0000OO0O0000O0O ['status']==200 :#line:256
                    print (f'【下架出售】:{OO0000OO0O0000O0O["data"]}')#line:257
        except Exception as OO0OOO0O00O0OO00O :#line:258
            print (OO0OOO0O00O0OO00O )#line:259
def start ():#line:261
    try :#line:262
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:263
        O000OO0O00OO00O00 ()#line:264
        OOOOO0OO0000O0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:265
        print (f"==========共找到{len(OOOOO0OO0000O0OOO)}个账号==========")#line:266
        for O00O0000O0OOO0O00 in OOOOO0OO0000O0OOO :#line:267
            OO0OO0O00OOO00OO0 =[]#line:268
            print (f"------------正在执行第{OOOOO0OO0000O0OOO.index(O00O0000O0OOO0O00) + 1}个账号------------")#line:269
            OOO0O00O0OOO0OOOO =CityEarth (O00O0000O0OOO0O00 ,OO0OO0O00OOO00OO0 )#line:270
            if OOO0O00O0OOO0OOOO .base_info ():#line:272
                OOO0O00O0OOO0OOOO .sealing ()#line:274
                OOO0O00O0OOO0OOOO .query_to_sell ()#line:276
                _OOO0O00O0O00OOO0O =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:279
                OOO0O00O0OOO0OOOO .game_map (_OOO0O00O0O00OOO0O )#line:280
    except Exception as O0000OOO0OOO0OOO0 :#line:282
        print (O0000OOO0OOO0OOO0 )#line:283
if __name__ =='__main__':#line:286
    start ()#line:287
