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
def sign (OO0O00O00O00OO0O0 ):#line:52
    OO0O00O0000O000O0 =hashlib .md5 (OO0O00O00O00OO0O0 .encode ()).hexdigest ()#line:53
    O00O000000OOOO0OO ="scsc%^&*"+OO0O00O0000O000O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOO000O000OO0OO0O =hashlib .md5 (O00O000000OOOO0OO .encode ()).hexdigest ()#line:55
    return OOO000O000OO0OO0O #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0O0O0O00OOO00OO0 ,OOO0O0O00O0O000O0 ,OO0000O000OOOO000 ):#line:64
        try :#line:65
            O0O0O0O00OOO00OO0 .msg =OO0000O000OOOO000 #line:66
            O0O0O0O00OOO00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0O0O0O00OOO00OO0 .token =OOO0O0O00O0O000O0 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OOO00OO0O0O0O0000 ):#line:73
        try :#line:74
            OO0OOO000OOO0OOOO =f'__{timi_new()}'#line:75
            OO00O0000O00000O0 ={'source':'scsc','authorization':OOO00OO0O0O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000OOO0OOOO ),'signstring':OO0OOO000OOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O000O00OO00000O00 =requests .request ('get',f'{host}/user',headers =OO00O0000O00000O0 ).json ()#line:87
            if 'status'in O000O00OO00000O00 :#line:89
                if O000O00OO00000O00 ['status']==200 :#line:90
                    OO0OO0O00OO0OO0OO =O000O00OO00000O00 ['data']['nickname']#line:91
                    O00OO000OO00OOO0O =O000O00OO00000O00 ['data']['inner_id']#line:92
                    O00OO0OOO00O00OO0 =O000O00OO00000O00 ['data']['assets']['gold']#line:93
                    OO0OO000000000O00 =O000O00OO00000O00 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO0OO0O00OO0OO0OO[:5]}丨ID:{O00OO000OO00OOO0O}丨等级:{OO0OO000000000O00}丨金种子:{str(O00OO0OOO00O00OO0).split(".")[0]}')#line:95
                if O000O00OO00000O00 ['status']==401 :#line:96
                    print (O000O00OO00000O00 ['message'])#line:97
                    OOO00OO0O0O0O0000 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O000O00OO00000O00 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as OOO00000OOO0O00O0 :#line:103
            print (OOO00000OOO0O00O0 )#line:104
    def sealing (O0O00O000OO000OOO ):#line:107
        try :#line:108
            OO00OOO0OOOO00OO0 =f'__{timi_new()}'#line:109
            O000OO0OOOO0O00OO ={'authorization':O0O00O000OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOOO00OO0 ),'signstring':OO00OOO0OOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O000OO0OOOO0O00OO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O000OO0OOOO0O00OO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O000OO0OOOO0O00OO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O000OO0OOOO0O00OO )#line:123
            requests .request ('get',f'{host}/user',headers =O000OO0OOOO0O00OO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O000OO0OOOO0O00OO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O000OO0OOOO0O00OO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O000OO0OOOO0O00OO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O000OO0OOOO0O00OO )#line:128
            requests .request ('get',f'{host}/assets',headers =O000OO0OOOO0O00OO )#line:129
        except Exception as O0OOO0OO0O00OO00O :#line:130
            print (O0OOO0OO0O00OO00O )#line:131
    def market_sale_buy (OO00O00000OOO0O0O ,_OO0OOO00O0OO0OO0O ,OO0O00OOO00O00OO0 ):#line:139
        try :#line:140
            OO0OO000000O0O000 =timi_new ()#line:141
            O00OOOOOO0OOO0000 =f'_askToBuyId={_OO0OOO00O0OO0OO0O}&quantity={OO0O00OOO00O00OO0}_{OO0OO000000O0O000}'#line:142
            OOO000O000000OO0O ={'source':'scsc','authorization':OO00O00000OOO0O0O .token ,'timestamp':str (OO0OO000000O0O000 ),'sign':sign (O00OOOOOO0OOO0000 ),'signstring':O00OOOOOO0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            OO00O0O0O0O0000OO ={"askToBuyId":_OO0OOO00O0OO0OO0O ,"quantity":OO0O00OOO00O00OO0 }#line:154
            O0OO00OO00OOOO00O =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOO000O000000OO0O ,data =OO00O0O0O0O0000OO ).json ()#line:155
            if 'status'in O0OO00OO00OOOO00O :#line:157
                if O0OO00OO00OOOO00O ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif O0OO00OO00OOOO00O ['']==500 :#line:160
                    if O0OO00OO00OOOO00O ['message']=='请求超时':#line:161
                        OO00O00000OOO0O0O .market_sale_buy (OO00O00000OOO0O0O ,_OO0OOO00O0OO0OO0O ,OO0O00OOO00O00OO0 )#line:162
                else :#line:163
                    print (O0OO00OO00OOOO00O )#line:164
                    exit ()#line:165
        except Exception as O0O00O00OO00OOOOO :#line:166
            print (O0O00O00OO00OOOOO )#line:167
    def game_map (OOO00000O000O00OO ,_O00000O00OO0O0OOO ):#line:170
        try :#line:171
            OO00OO00OO000000O =f'__{timi_new()}'#line:172
            OO0O00O0O00O00O0O ={'source':'scsc','authorization':OOO00000O000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OO000000O ),'signstring':OO00OO00OO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:183
            OOOO000OOOO0OOOOO =requests .request ('get',f'{host}/game/map',headers =OO0O00O0O00O00O0O ).json ()#line:184
            if 'status'in OOOO000OOOO0OOOOO :#line:186
                if OOOO000OOOO0OOOOO ['status']==200 :#line:187
                    for O0000O0O0O00OOO0O in OOOO000OOOO0OOOOO ['data']['list'][0 ]['crops']:#line:188
                        OO00OOOOO00O0O000 =O0000O0O0O00OOO0O ['level']#line:190
                        if OO00OOOOO00O0O000 ==41 :#line:191
                            O0OOOOOOOO0O0OO00 =O0000O0O0O00OOO0O ['crop_name']#line:192
                            OOO0O00O0OOOOOO00 =O0000O0O0O00OOO0O ['count']#line:193
                            if OOO0O00O0OOOOOO00 >0 :#line:194
                                print (f'【农业资产】:{O0OOOOOOOO0O0OO00}丨数量:{OOO0O00O0OOOOOO00}')#line:195
                                OOO00000O000O00OO .market_sale_buy (_O00000O00OO0O0OOO ,OOO0O00O0OOOOOO00 )#line:196
        except Exception as OOOO00O0O000OO00O :#line:197
            print (OOOO00O0O000OO00O )#line:198
    def query_to_sell (OOOO0O0O0OO000OO0 ):#line:202
        try :#line:203
            O0OOO00O0O0OO0O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:204
            OO0OOOOO0OOO0O000 ={'source':'scsc','authorization':OOOO0O0O0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0OO0O0O ),'signstring':O0OOO00O0O0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
            OOO0O00OO0OOO0O00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0OOOOO0OOO0O000 ).json ()#line:216
            if 'status'in OOO0O00OO0OOO0O00 :#line:218
                if OOO0O00OO0OOO0O00 ['status']==200 :#line:219
                    for O0OO0O000O0O0OOO0 in OOO0O00OO0OOO0O00 ['data']['rows']:#line:220
                        O0O0000OOO00O00O0 =O0OO0O000O0O0OOO0 ['materialKey']#line:221
                        OOO000O0OOOOOO000 =O0OO0O000O0O0OOO0 ['quantity']#line:222
                        OOOOO0000O00OO000 =O0OO0O000O0O0OOO0 ['price']#line:223
                        O00000OOOO000O00O =O0OO0O000O0O0OOO0 ['saleState']#line:224
                        if O00000OOOO000O00O ==0 :#line:225
                            print (f'【出售订单】:名称:{O0O0000OOO00O00O0}丨数量:{OOO000O0OOOOOO000}丨价格:{OOOOO0000O00OO000}')#line:226
                            OOOO0OO0O000OO0O0 =O0OO0O000O0O0OOO0 ['id']#line:227
                            OOOO0O0O0OO000OO0 .cacel_sale (OOOO0OO0O000OO0O0 )#line:228
        except Exception as O0OO0O0OOOOOOOO0O :#line:234
            print (O0OO0O0OOOOOOOO0O )#line:235
    def cacel_sale (O0000OOOO00OO0OOO ,O0O000O0O000O0OO0 ):#line:239
        try :#line:240
            OO0O0OOOOOOOOOO0O =f'_saleId={O0O000O0O000O0OO0}_{timi_new()}'#line:241
            OO0O0O0OO0OO000O0 ={'source':'scsc','authorization':O0000OOOO00OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOOOOOOO0O ),'signstring':OO0O0OOOOOOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:252
            OO0OOO0OO00O000O0 ={"saleId":O0O000O0O000O0OO0 }#line:255
            O000O000OO00O0O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0O0O0OO0OO000O0 ,data =OO0OOO0OO00O000O0 ).json ()#line:256
            if 'status'in O000O000OO00O0O00 :#line:258
                if O000O000OO00O0O00 ['status']==200 :#line:259
                    print (f'【下架出售】:{O000O000OO00O0O00["data"]}')#line:260
        except Exception as O0000OO0OOOOO00O0 :#line:261
            print (O0000OO0OOOOO00O0 )#line:262
def start ():#line:264
    try :#line:265
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:266
        O000OO0O00OO00O00 ()#line:267
        O000OO0O00O0O0O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:268
        print (f"==========共找到{len(O000OO0O00O0O0O0O)}个账号==========")#line:269
        for OOOO000OOO0OOO00O in O000OO0O00O0O0O0O :#line:270
            OO0O0000OO00OOO00 =[]#line:271
            print (f"------------正在执行第{O000OO0O00O0O0O0O.index(OOOO000OOO0OOO00O) + 1}个账号------------")#line:272
            OOOO0O00OO00O0000 =CityEarth (OOOO000OOO0OOO00O ,OO0O0000OO00OOO00 )#line:273
            if OOOO0O00OO00O0000 .base_info ():#line:275
                OOOO0O00OO00O0000 .sealing ()#line:277
                OOOO0O00OO00O0000 .query_to_sell ()#line:279
                _OO00O0OO0O00OO00O =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:282
                OOOO0O00OO00O0000 .game_map (_OO00O0OO0O00OO00O )#line:283
    except Exception as O000OO0000O0OOO00 :#line:285
        print (O000OO0000O0OOO00 )#line:286
if __name__ =='__main__':#line:289
    start ()#line:290
