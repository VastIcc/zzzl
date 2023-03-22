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
def sign (OOO0000O00OOOOOO0 ):#line:52
    OO0000O0OOO0O00OO =hashlib .md5 (OOO0000O00OOOOOO0 .encode ()).hexdigest ()#line:53
    OO0O0OOOO00O0O0O0 ="scsc%^&*"+OO0000O0OOO0O00OO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OO0OOO0OOO0000000 =hashlib .md5 (OO0O0OOOO00O0O0O0 .encode ()).hexdigest ()#line:55
    return OO0OOO0OOO0000000 #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (OO0OO0OO0O00O0O0O ,OOOOOOO000000O000 ,OOOOOOO000OO000OO ):#line:64
        try :#line:65
            OO0OO0OO0O00O0O0O .msg =OOOOOOO000OO000OO #line:66
            OO0OO0OO0O00O0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            OO0OO0OO0O00O0O0O .token =OOOOOOO000000O000 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O0OO0OOOO0OOO0OOO ):#line:73
        try :#line:74
            O00OOOO000OOO0O00 =f'__{timi_new()}'#line:75
            OOO0OOOO00OOO0OO0 ={'source':'scsc','authorization':O0OO0OOOO0OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000OOO0O00 ),'signstring':O00OOOO000OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O00OOO000OO0O000O =requests .request ('get',f'{host}/user',headers =OOO0OOOO00OOO0OO0 ).json ()#line:87
            if 'status'in O00OOO000OO0O000O :#line:89
                if O00OOO000OO0O000O ['status']==200 :#line:90
                    OO0OO0O000O00000O =O00OOO000OO0O000O ['data']['nickname']#line:91
                    O0O000O0OO00OOO0O =O00OOO000OO0O000O ['data']['inner_id']#line:92
                    OO000O00OO000OOOO =O00OOO000OO0O000O ['data']['assets']['gold']#line:93
                    OOO0OO0O0OOO00OOO =O00OOO000OO0O000O ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO0OO0O000O00000O[:5]}丨ID:{O0O000O0OO00OOO0O}丨等级:{OOO0OO0O0OOO00OOO}丨金种子:{str(OO000O00OO000OOOO).split(".")[0]}')#line:95
                if O00OOO000OO0O000O ['status']==401 :#line:96
                    print (O00OOO000OO0O000O ['message'])#line:97
                    O0OO0OOOO0OOO0OOO .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O00OOO000OO0O000O ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0OOOOOO00OOO00OO :#line:103
            print (O0OOOOOO00OOO00OO )#line:104
    def sealing (O0OOO00OOOO0O0OOO ):#line:107
        try :#line:108
            O000OO00O00OO0OO0 =f'__{timi_new()}'#line:109
            OOOOOOOOOOO0O00OO ={'authorization':O0OOO00OOOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00OO0OO0 ),'signstring':O000OO00O00OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOOOOOOO0O00OO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOOOOOOO0O00OO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOOOOOOO0O00OO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOOOOOOO0O00OO )#line:123
            requests .request ('get',f'{host}/user',headers =OOOOOOOOOOO0O00OO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOOOOOOO0O00OO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOOOOOOO0O00OO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOOOOOOO0O00OO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOOOOOO0O00OO )#line:128
            requests .request ('get',f'{host}/assets',headers =OOOOOOOOOOO0O00OO )#line:129
        except Exception as OOOOO0O0000OOOOOO :#line:130
            print (OOOOO0O0000OOOOOO )#line:131
    def market_sale_buy (O000O0O000OOO0O0O ,_O00OO00000O0OOOO0 ,OO00OOOO00O00O0O0 ):#line:139
        try :#line:140
            O0OO0000O0O0O0OOO =timi_new ()#line:141
            OO0OO0O0O000O00O0 =f'_askToBuyId={_O00OO00000O0OOOO0}&quantity={OO00OOOO00O00O0O0}_{O0OO0000O0O0O0OOO}'#line:142
            OOOOOO0000O0O00OO ={'source':'scsc','authorization':O000O0O000OOO0O0O .token ,'timestamp':str (O0OO0000O0O0O0OOO ),'sign':sign (OO0OO0O0O000O00O0 ),'signstring':OO0OO0O0O000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O0OOOOO0O00O000OO ={"askToBuyId":_O00OO00000O0OOOO0 ,"quantity":OO00OOOO00O00O0O0 }#line:154
            O0OOOOOO0OO0OO0OO =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOOOOO0000O0O00OO ,data =O0OOOOO0O00O000OO ).json ()#line:155
            if 'status'in O0OOOOOO0OO0OO0OO :#line:157
                if O0OOOOOO0OO0OO0OO ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif O0OOOOOO0OO0OO0OO ['message']=='请求超时':#line:160
                    O000O0O000OOO0O0O .market_sale_buy (O000O0O000OOO0O0O ,_O00OO00000O0OOOO0 ,OO00OOOO00O00O0O0 )#line:161
                else :#line:162
                    print (O0OOOOOO0OO0OO0OO )#line:163
                    exit ()#line:164
        except Exception as OOOOO00OO0O0OOO00 :#line:165
            print (OOOOO00OO0O0OOO00 )#line:166
    def game_map (O00O0000O0OOOOOO0 ,_OO00OOOOO0OO0OO0O ):#line:169
        try :#line:170
            OOOOO0O000OOOOO0O =f'__{timi_new()}'#line:171
            O000OOOO00000O0OO ={'source':'scsc','authorization':O00O0000O0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O000OOOOO0O ),'signstring':OOOOO0O000OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
            OOOOOO0O0OOO0O000 =requests .request ('get',f'{host}/game/map',headers =O000OOOO00000O0OO ).json ()#line:183
            if 'status'in OOOOOO0O0OOO0O000 :#line:185
                if OOOOOO0O0OOO0O000 ['status']==200 :#line:186
                    for OO0OO0O0OO0OO0O00 in OOOOOO0O0OOO0O000 ['data']['list'][0 ]['crops']:#line:187
                        OOO0OOOOO0O0O0O00 =OO0OO0O0OO0OO0O00 ['level']#line:189
                        if OOO0OOOOO0O0O0O00 ==41 :#line:190
                            O000000OOOOOO0O00 =OO0OO0O0OO0OO0O00 ['crop_name']#line:191
                            OOO0O000O0OOO0OOO =OO0OO0O0OO0OO0O00 ['count']#line:192
                            if OOO0O000O0OOO0OOO >0 :#line:193
                                print (f'【农业资产】:{O000000OOOOOO0O00}丨数量:{OOO0O000O0OOO0OOO}')#line:194
                                O00O0000O0OOOOOO0 .market_sale_buy (_OO00OOOOO0OO0OO0O ,OOO0O000O0OOO0OOO )#line:195
        except Exception as OO00O0O0OO0OOOOO0 :#line:196
            print (OO00O0O0OO0OOOOO0 )#line:197
    def query_to_sell (OOO0OO0O00OOO0OOO ):#line:201
        try :#line:202
            OOOOOO0OO00OOO0O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:203
            O0OO000O0O000OO00 ={'source':'scsc','authorization':OOO0OO0O00OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO00OOO0O0 ),'signstring':OOOOOO0OO00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            OOO00O0000O0OO0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO000O0O000OO00 ).json ()#line:215
            if 'status'in OOO00O0000O0OO0O0 :#line:217
                if OOO00O0000O0OO0O0 ['status']==200 :#line:218
                    for O0O0O00O0OOOO0O00 in OOO00O0000O0OO0O0 ['data']['rows']:#line:219
                        O0OOOO0O0OO0000OO =O0O0O00O0OOOO0O00 ['materialKey']#line:220
                        O00O0OO0OO0000000 =O0O0O00O0OOOO0O00 ['quantity']#line:221
                        O00O0OO0OO0OO00OO =O0O0O00O0OOOO0O00 ['price']#line:222
                        O0O00OOO0O0000O00 =O0O0O00O0OOOO0O00 ['saleState']#line:223
                        if O0O00OOO0O0000O00 ==0 :#line:224
                            print (f'【出售订单】:名称:{O0OOOO0O0OO0000OO}丨数量:{O00O0OO0OO0000000}丨价格:{O00O0OO0OO0OO00OO}')#line:225
                            O0O000OOO0O00O000 =O0O0O00O0OOOO0O00 ['id']#line:226
                            OOO0OO0O00OOO0OOO .cacel_sale (O0O000OOO0O00O000 )#line:227
        except Exception as OOO00O0OOO000OOO0 :#line:233
            print (OOO00O0OOO000OOO0 )#line:234
    def cacel_sale (O0OOO0O000000O000 ,O000O0OO0O00OO000 ):#line:238
        try :#line:239
            OO0O0OOO0000OO00O =f'_saleId={O000O0OO0O00OO000}_{timi_new()}'#line:240
            OO0OO0OO0OOOOO0O0 ={'source':'scsc','authorization':O0OOO0O000000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO0000OO00O ),'signstring':OO0O0OOO0000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            OOOOOOO0O0000O0OO ={"saleId":O000O0OO0O00OO000 }#line:254
            O0OO000000OO000OO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO0OO0OOOOO0O0 ,data =OOOOOOO0O0000O0OO ).json ()#line:255
            if 'status'in O0OO000000OO000OO :#line:257
                if O0OO000000OO000OO ['status']==200 :#line:258
                    print (f'【下架出售】:{O0OO000000OO000OO["data"]}')#line:259
        except Exception as OO0O0OO00000O0O00 :#line:260
            print (OO0O0OO00000O0O00 )#line:261
def start ():#line:263
    try :#line:264
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:265
        O000OO0O00OO00O00 ()#line:266
        OOOO0OOO000O00OO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:267
        print (f"==========共找到{len(OOOO0OOO000O00OO0)}个账号==========")#line:268
        for OO0OO0OO0O00O0O00 in OOOO0OOO000O00OO0 :#line:269
            O0O0O00O0OO0O0O00 =[]#line:270
            print (f"------------正在执行第{OOOO0OOO000O00OO0.index(OO0OO0OO0O00O0O00) + 1}个账号------------")#line:271
            O00OOOOO00OOOO0OO =CityEarth (OO0OO0OO0O00O0O00 ,O0O0O00O0OO0O0O00 )#line:272
            if O00OOOOO00OOOO0OO .base_info ():#line:274
                O00OOOOO00OOOO0OO .sealing ()#line:276
                O00OOOOO00OOOO0OO .query_to_sell ()#line:278
                _OOO0O0OO0000OOOO0 =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:281
                O00OOOOO00OOOO0OO .game_map (_OOO0O0OO0000OOOO0 )#line:282
    except Exception as OOOO0OO0O0O0OO0O0 :#line:284
        print (OOOO0OO0O0O0OO0O0 )#line:285
if __name__ =='__main__':#line:288
    start ()#line:289
