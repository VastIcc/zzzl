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
version ='3.1.41955435111'#line:26
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
def sign (OO0000O0O0OO00OO0 ):#line:52
    O00O0O0OO0OOOO0OO =hashlib .md5 (OO0000O0O0OO00OO0 .encode ()).hexdigest ()#line:53
    O000OO0O000OOOO00 ="scsc%^&*"+O00O0O0OO0OOOO0OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOOO00O00O0OO0O00 =hashlib .md5 (O000OO0O000OOOO00 .encode ()).hexdigest ()#line:55
    return OOOO00O00O0OO0O00 #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0000OO0000OOO0O0 ,OOOOOO0O0OOO00000 ,OO0O00000O0O00OOO ):#line:64
        try :#line:65
            O0000OO0000OOO0O0 .msg =OO0O00000O0O00OOO #line:66
            O0000OO0000OOO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0000OO0000OOO0O0 .token =OOOOOO0O0OOO00000 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O0O0OOO0O0000O00O ):#line:73
        try :#line:74
            O0OO0OOO00OO0O0O0 =f'__{timi_new()}'#line:75
            OOOO000O0OO00O0OO ={'source':'scsc','authorization':O0O0OOO0O0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00OO0O0O0 ),'signstring':O0OO0OOO00OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O000000000O000000 =requests .request ('get',f'{host}/user',headers =OOOO000O0OO00O0OO ).json ()#line:87
            if 'status'in O000000000O000000 :#line:89
                if O000000000O000000 ['status']==200 :#line:90
                    OO00O0OOO00000O0O =O000000000O000000 ['data']['nickname']#line:91
                    OO0000OOOO000O0OO =O000000000O000000 ['data']['inner_id']#line:92
                    OO0O0000OOO0OO000 =O000000000O000000 ['data']['assets']['gold']#line:93
                    O0O0O0OO00O0O00O0 =O000000000O000000 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO00O0OOO00000O0O[:5]}丨ID:{OO0000OOOO000O0OO}丨等级:{O0O0O0OO00O0O00O0}丨金种子:{str(OO0O0000OOO0OO000).split(".")[0]}')#line:95
                if O000000000O000000 ['status']==401 :#line:96
                    print (O000000000O000000 ['message'])#line:97
                    O0O0OOO0O0000O00O .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O000000000O000000 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0O0000OO000OOO0O :#line:103
            print (O0O0000OO000OOO0O )#line:104
    def sealing (O000OOO000O000000 ):#line:107
        try :#line:108
            OOO0OOO0000OO0O0O =f'__{timi_new()}'#line:109
            O00OO0OOO00000OOO ={'authorization':O000OOO000O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0000OO0O0O ),'signstring':OOO0OOO0000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO0OOO00000OOO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O00OO0OOO00000OOO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO0OOO00000OOO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO0OOO00000OOO )#line:123
            requests .request ('get',f'{host}/user',headers =O00OO0OOO00000OOO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO0OOO00000OOO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO0OOO00000OOO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO0OOO00000OOO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO0OOO00000OOO )#line:128
            requests .request ('get',f'{host}/assets',headers =O00OO0OOO00000OOO )#line:129
        except Exception as OO00OOO0OOO00O00O :#line:130
            print (OO00OOO0OOO00O00O )#line:131
    def market_sale_buy (OOOOO000O0OO000OO ,_O00OO00OO00OOOO00 ,OOO000000O0O0O0OO ):#line:139
        try :#line:140
            OO0OO000OOO00OO00 =timi_new ()#line:141
            OOO00OO0OO0000O00 =f'_askToBuyId={_O00OO00OO00OOOO00}&quantity={OOO000000O0O0O0OO}_{OO0OO000OOO00OO00}'#line:142
            O0OOO00O0O0000OOO ={'source':'scsc','authorization':OOOOO000O0OO000OO .token ,'timestamp':str (OO0OO000OOO00OO00 ),'sign':sign (OOO00OO0OO0000O00 ),'signstring':OOO00OO0OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O00O0OOO000OO0OO0 ={"askToBuyId":_O00OO00OO00OOOO00 ,"quantity":OOO000000O0O0O0OO }#line:154
            OOO0O0000OOO00OOO =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0OOO00O0O0000OOO ,data =O00O0OOO000OO0OO0 ).json ()#line:155
            if 'status'in OOO0O0000OOO00OOO :#line:157
                if OOO0O0000OOO00OOO ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OOO0O0000OOO00OOO ['']==500 :#line:160
                    if OOO0O0000OOO00OOO ['message']=='请求超时':#line:161
                        OOOOO000O0OO000OO .market_sale_buy (OOOOO000O0OO000OO ,_O00OO00OO00OOOO00 ,OOO000000O0O0O0OO )#line:162
                    else :#line:163
                        print (OOO0O0000OOO00OOO )#line:164
                        exit ()#line:165
        except Exception as O000O0O00O0000OO0 :#line:166
            print (O000O0O00O0000OO0 )#line:167
    def game_map (OOOO00O0OO0O00000 ,_O0O0000O0OOO0O00O ):#line:170
        try :#line:171
            O00000O00OO0O0O0O =f'__{timi_new()}'#line:172
            OO00OOOO00OO0O0OO ={'source':'scsc','authorization':OOOO00O0OO0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00OO0O0O0O ),'signstring':O00000O00OO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:183
            O000OOOO00OO0OO00 =requests .request ('get',f'{host}/game/map',headers =OO00OOOO00OO0O0OO ).json ()#line:184
            if 'status'in O000OOOO00OO0OO00 :#line:186
                if O000OOOO00OO0OO00 ['status']==200 :#line:187
                    for O0O0OOOOOO0OO0O0O in O000OOOO00OO0OO00 ['data']['list'][0 ]['crops']:#line:188
                        O00OO00O0O000000O =O0O0OOOOOO0OO0O0O ['level']#line:190
                        if O00OO00O0O000000O ==41 :#line:191
                            O000O000OOOOOO0O0 =O0O0OOOOOO0OO0O0O ['crop_name']#line:192
                            OOO00OO0OO000OO0O =O0O0OOOOOO0OO0O0O ['count']#line:193
                            if OOO00OO0OO000OO0O >0 :#line:194
                                print (f'【农业资产】:{O000O000OOOOOO0O0}丨数量:{OOO00OO0OO000OO0O}')#line:195
                                OOOO00O0OO0O00000 .market_sale_buy (_O0O0000O0OOO0O00O ,OOO00OO0OO000OO0O )#line:196
        except Exception as O0OO00OOO000O0OOO :#line:197
            print (O0OO00OOO000O0OOO )#line:198
    def query_to_sell (O0OOO0OO0OO000O0O ):#line:202
        try :#line:203
            O0O0O00OOOOOOO00O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:204
            O0O00OO0O00OOO000 ={'source':'scsc','authorization':O0OOO0OO0OO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOOOOO00O ),'signstring':O0O0O00OOOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
            OO0OOO0O00OOOO00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O00OO0O00OOO000 ).json ()#line:216
            if 'status'in OO0OOO0O00OOOO00O :#line:218
                if OO0OOO0O00OOOO00O ['status']==200 :#line:219
                    for O0O0O0O00O0O00O0O in OO0OOO0O00OOOO00O ['data']['rows']:#line:220
                        O0O00O0O000000OOO =O0O0O0O00O0O00O0O ['materialKey']#line:221
                        O00OO0OOO00000O0O =O0O0O0O00O0O00O0O ['quantity']#line:222
                        OOO00OOO0O00OO000 =O0O0O0O00O0O00O0O ['price']#line:223
                        OO00OOOO0OO0O0O0O =O0O0O0O00O0O00O0O ['saleState']#line:224
                        if OO00OOOO0OO0O0O0O ==0 :#line:225
                            print (f'【出售订单】:名称:{O0O00O0O000000OOO}丨数量:{O00OO0OOO00000O0O}丨价格:{OOO00OOO0O00OO000}')#line:226
                            O0O0O00O00000O000 =O0O0O0O00O0O00O0O ['id']#line:227
                            O0OOO0OO0OO000O0O .cacel_sale (O0O0O00O00000O000 )#line:228
        except Exception as O0000000OO000OO0O :#line:234
            print (O0000000OO000OO0O )#line:235
    def cacel_sale (OO000OO0O0O0OOOOO ,OOOO0O00OOOOOO0OO ):#line:239
        try :#line:240
            OO00O00O0OOO00O00 =f'_saleId={OOOO0O00OOOOOO0OO}_{timi_new()}'#line:241
            O000O0000O0OOOOOO ={'source':'scsc','authorization':OO000OO0O0O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O0OOO00O00 ),'signstring':OO00O00O0OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
            O0O0O0OOO0O0O0000 ={"saleId":OOOO0O00OOOOOO0OO }#line:255
            O00OO000O0OOO0O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O000O0000O0OOOOOO ,data =O0O0O0OOO0O0O0000 ).json ()#line:256
            if 'status'in O00OO000O0OOO0O00 :#line:258
                if O00OO000O0OOO0O00 ['status']==200 :#line:259
                    print (f'【下架出售】:{O00OO000O0OOO0O00["data"]}')#line:260
        except Exception as OOO00O0000OO0000O :#line:261
            print (OOO00O0000OO0000O )#line:262
def start ():#line:264
    try :#line:265
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:266
        O000OO0O00OO00O00 ()#line:267
        OOO0OO00O0OOOO0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:268
        print (f"==========共找到{len(OOO0OO00O0OOOO0O0)}个账号==========")#line:269
        for OOO0OO00O000O0000 in OOO0OO00O0OOOO0O0 :#line:270
            O0OO0OO0OOOOOOO00 =[]#line:271
            print (f"------------正在执行第{OOO0OO00O0OOOO0O0.index(OOO0OO00O000O0000) + 1}个账号------------")#line:272
            OOO0OO00O00OOO0O0 =CityEarth (OOO0OO00O000O0000 ,O0OO0OO0OOOOOOO00 )#line:273
            if OOO0OO00O00OOO0O0 .base_info ():#line:275
                OOO0OO00O00OOO0O0 .sealing ()#line:277
                OOO0OO00O00OOO0O0 .query_to_sell ()#line:279
                _O0O00O0000000O000 =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:282
                OOO0OO00O00OOO0O0 .game_map (_O0O00O0000000O000 )#line:283
    except Exception as OOO00O0OO0O0OOOO0 :#line:285
        print (OOO00O0OO0O0OOOO0 )#line:286
if __name__ =='__main__':#line:289
    start ()#line:290
