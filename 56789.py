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
def sign (O00OOO0000O000OO0 ):#line:52
    OOOOO0OOO00O00OOO =hashlib .md5 (O00OOO0000O000OO0 .encode ()).hexdigest ()#line:53
    O0O0OOOOOOOOO00OO ="scsc%^&*"+OOOOO0OOO00O00OOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    O0OO0O0O00O0O0OOO =hashlib .md5 (O0O0OOOOOOOOO00OO .encode ()).hexdigest ()#line:55
    return O0OO0O0O00O0O0OOO #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O00O0OOO00OOO0O0O ,OOOOO0O000OOOOOO0 ,O0000O0000OO00000 ):#line:64
        try :#line:65
            O00O0OOO00OOO0O0O .msg =O0000O0000OO00000 #line:66
            O00O0OOO00OOO0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O00O0OOO00OOO0O0O .token =OOOOO0O000OOOOOO0 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O00OOO0O00O0O000O ):#line:73
        try :#line:74
            OO00O0OO0OOOO0O00 =f'__{timi_new()}'#line:75
            O0O0000O00O000OO0 ={'source':'scsc','authorization':O00OOO0O00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO0OOOO0O00 ),'signstring':OO00O0OO0OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O0OOOO000OO0O000O =requests .request ('get',f'{host}/user',headers =O0O0000O00O000OO0 ).json ()#line:87
            if 'status'in O0OOOO000OO0O000O :#line:89
                if O0OOOO000OO0O000O ['status']==200 :#line:90
                    OOO00O0000OOOO000 =O0OOOO000OO0O000O ['data']['nickname']#line:91
                    OO0OO0O0OO0OO00O0 =O0OOOO000OO0O000O ['data']['inner_id']#line:92
                    OO0O0000OOOOO0OOO =O0OOOO000OO0O000O ['data']['assets']['gold']#line:93
                    OO0O000OOOOOOOOOO =O0OOOO000OO0O000O ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OOO00O0000OOOO000[:5]}丨ID:{OO0OO0O0OO0OO00O0}丨等级:{OO0O000OOOOOOOOOO}丨金种子:{str(OO0O0000OOOOO0OOO).split(".")[0]}')#line:95
                if O0OOOO000OO0O000O ['status']==401 :#line:96
                    print (O0OOOO000OO0O000O ['message'])#line:97
                    O00OOO0O00O0O000O .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O0OOOO000OO0O000O ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as OO0000O0OO00O0O00 :#line:103
            print (OO0000O0OO00O0O00 )#line:104
    def sealing (O0O00O0O0OOO00OOO ):#line:107
        try :#line:108
            O00OOO0O0O0OO0OO0 =f'__{timi_new()}'#line:109
            O0O0OOO0000O0O0O0 ={'authorization':O0O00O0O0OOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0O0OO0OO0 ),'signstring':O00OOO0O0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0OOO0000O0O0O0 )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O0O0OOO0000O0O0O0 )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0OOO0000O0O0O0 )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0OOO0000O0O0O0 )#line:123
            requests .request ('get',f'{host}/user',headers =O0O0OOO0000O0O0O0 )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0OOO0000O0O0O0 )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0OOO0000O0O0O0 )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0OOO0000O0O0O0 )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOO0000O0O0O0 )#line:128
            requests .request ('get',f'{host}/assets',headers =O0O0OOO0000O0O0O0 )#line:129
        except Exception as O000OO0OO000O0O0O :#line:130
            print (O000OO0OO000O0O0O )#line:131
    def market_sale_buy (O0OO00O0000OOOOO0 ,_O0000OO0000O00OO0 ,O00OO000000OOOOO0 ):#line:139
        try :#line:140
            OOOO00O0000O0OOO0 =timi_new ()#line:141
            O0OO0OOOOOO0000O0 =f'_askToBuyId={_O0000OO0000O00OO0}&quantity={O00OO000000OOOOO0}_{OOOO00O0000O0OOO0}'#line:142
            O0OO00OO0OO000000 ={'source':'scsc','authorization':O0OO00O0000OOOOO0 .token ,'timestamp':str (OOOO00O0000O0OOO0 ),'sign':sign (O0OO0OOOOOO0000O0 ),'signstring':O0OO0OOOOOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O0OO0000000OOOOOO ={"askToBuyId":_O0000OO0000O00OO0 ,"quantity":O00OO000000OOOOO0 }#line:154
            OO000OO0OOOOO00O0 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0OO00OO0OO000000 ,data =O0OO0000000OOOOOO ).json ()#line:155
            if 'status'in OO000OO0OOOOO00O0 :#line:157
                if OO000OO0OOOOO00O0 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OO000OO0OOOOO00O0 ['']==500 :#line:160
                    if OO000OO0OOOOO00O0 ['message']=='请求超时':#line:161
                        O0OO00O0000OOOOO0 .market_sale_buy (O0OO00O0000OOOOO0 ,_O0000OO0000O00OO0 ,O00OO000000OOOOO0 )#line:162
                    else :#line:163
                        print (OO000OO0OOOOO00O0 )#line:164
                        exit ()#line:165
                else :#line:166
                    print (OO000OO0OOOOO00O0 )#line:167
                    exit ()#line:168
        except Exception as OOO00O000O0OOO0OO :#line:169
            print (OOO00O000O0OOO0OO )#line:170
    def game_map (OOO00O000O0O0OOOO ,_OO0OOO00OO00O0O0O ):#line:173
        try :#line:174
            O00000OO000O0O00O =f'__{timi_new()}'#line:175
            OO00000OOOO000OO0 ={'source':'scsc','authorization':OOO00O000O0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO000O0O00O ),'signstring':O00000OO000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:186
            O00OO000O0O0000O0 =requests .request ('get',f'{host}/game/map',headers =OO00000OOOO000OO0 ).json ()#line:187
            if 'status'in O00OO000O0O0000O0 :#line:189
                if O00OO000O0O0000O0 ['status']==200 :#line:190
                    for OOO00O0O000O0OOO0 in O00OO000O0O0000O0 ['data']['list'][0 ]['crops']:#line:191
                        O0OO00O0000OO0OOO =OOO00O0O000O0OOO0 ['level']#line:193
                        if O0OO00O0000OO0OOO ==41 :#line:194
                            O0OOO0000OO0000OO =OOO00O0O000O0OOO0 ['crop_name']#line:195
                            O00O0OO0O00OOOOO0 =OOO00O0O000O0OOO0 ['count']#line:196
                            if O00O0OO0O00OOOOO0 >0 :#line:197
                                print (f'【农业资产】:{O0OOO0000OO0000OO}丨数量:{O00O0OO0O00OOOOO0}')#line:198
                                OOO00O000O0O0OOOO .market_sale_buy (_OO0OOO00OO00O0O0O ,O00O0OO0O00OOOOO0 )#line:199
        except Exception as OO0OO0O0O0OOO0000 :#line:200
            print (OO0OO0O0O0OOO0000 )#line:201
    def query_to_sell (OOO00O00OO00O0000 ):#line:205
        try :#line:206
            O00O0O0OOO0OOOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:207
            OOOO0O0O0OOOOOOO0 ={'source':'scsc','authorization':OOO00O00OO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OOO0OOOOOO ),'signstring':O00O0O0OOO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:218
            O0OOOOO0O0OO0OOO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOO0O0O0OOOOOOO0 ).json ()#line:219
            if 'status'in O0OOOOO0O0OO0OOO0 :#line:221
                if O0OOOOO0O0OO0OOO0 ['status']==200 :#line:222
                    for O000OO00O0O0O0000 in O0OOOOO0O0OO0OOO0 ['data']['rows']:#line:223
                        O00O0O00O0OOOO0O0 =O000OO00O0O0O0000 ['materialKey']#line:224
                        O00000O0OOOOO0O0O =O000OO00O0O0O0000 ['quantity']#line:225
                        O0000O00O00OO00O0 =O000OO00O0O0O0000 ['price']#line:226
                        O00OOOO00OOOO000O =O000OO00O0O0O0000 ['saleState']#line:227
                        if O00OOOO00OOOO000O ==0 :#line:228
                            print (f'【出售订单】:名称:{O00O0O00O0OOOO0O0}丨数量:{O00000O0OOOOO0O0O}丨价格:{O0000O00O00OO00O0}')#line:229
                            OO00O0O00O000O0O0 =O000OO00O0O0O0000 ['id']#line:230
                            OOO00O00OO00O0000 .cacel_sale (OO00O0O00O000O0O0 )#line:231
        except Exception as OO0OOOOO000OO0OO0 :#line:237
            print (OO0OOOOO000OO0OO0 )#line:238
    def cacel_sale (OOOO0O0O0O0O0OO0O ,OO0OO0OO0O0OOO00O ):#line:242
        try :#line:243
            O0O0O00O0O000OOO0 =f'_saleId={OO0OO0OO0O0OOO00O}_{timi_new()}'#line:244
            OOOOOOOO00OO000OO ={'source':'scsc','authorization':OOOO0O0O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0O000OOO0 ),'signstring':O0O0O00O0O000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:255
            O0O0O0OOOOO0O000O ={"saleId":OO0OO0OO0O0OOO00O }#line:258
            O00O000OOO000O00O =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOOOOOO00OO000OO ,data =O0O0O0OOOOO0O000O ).json ()#line:259
            if 'status'in O00O000OOO000O00O :#line:261
                if O00O000OOO000O00O ['status']==200 :#line:262
                    print (f'【下架出售】:{O00O000OOO000O00O["data"]}')#line:263
        except Exception as OO0O000000OO00O00 :#line:264
            print (OO0O000000OO00O00 )#line:265
def start ():#line:267
    try :#line:268
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:269
        O000OO0O00OO00O00 ()#line:270
        O0O0OOOO00O00OO0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:271
        print (f"==========共找到{len(O0O0OOOO00O00OO0O)}个账号==========")#line:272
        for O0O00OOO0000000O0 in O0O0OOOO00O00OO0O :#line:273
            O0OO0O0OOO0000O00 =[]#line:274
            print (f"------------正在执行第{O0O0OOOO00O00OO0O.index(O0O00OOO0000000O0) + 1}个账号------------")#line:275
            OO0O0O0O0O00O00O0 =CityEarth (O0O00OOO0000000O0 ,O0OO0O0OOO0000O00 )#line:276
            if OO0O0O0O0O00O00O0 .base_info ():#line:278
                OO0O0O0O0O00O00O0 .sealing ()#line:280
                OO0O0O0O0O00O00O0 .query_to_sell ()#line:282
                _O0OOO0OOOO0OOO0OO =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:285
                OO0O0O0O0O00O00O0 .game_map (_O0OOO0OOOO0OOO0OO )#line:286
    except Exception as O0O0OOOOOO0OOOO00 :#line:288
        print (O0O0OOOOOO0OOOO00 )#line:289
if __name__ =='__main__':#line:292
    start ()#line:293
