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
def sign (O0O0O00O0O000000O ):#line:52
    O0O0OOO0O0OO0000O =hashlib .md5 (O0O0O00O0O000000O .encode ()).hexdigest ()#line:53
    OO000OOOOO0OO0OO0 ="scsc%^&*"+O0O0OOO0O0OO0000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OO00000O00O0OO0OO =hashlib .md5 (OO000OOOOO0OO0OO0 .encode ()).hexdigest ()#line:55
    return OO00000O00O0OO0OO #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (OOOOO0OO00000O000 ,O00O0O00OO0OOO0O0 ,O0OO0O0000O0OOO00 ):#line:64
        try :#line:65
            OOOOO0OO00000O000 .msg =O0OO0O0000O0OOO00 #line:66
            OOOOO0OO00000O000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            OOOOO0OO00000O000 .token =O00O0O00OO0OOO0O0 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OOO0OO0O00000OOOO ):#line:73
        try :#line:74
            OO0OO0OO00OOO0000 =f'__{timi_new()}'#line:75
            OO0O00000000O0O0O ={'source':'scsc','authorization':OOO0OO0O00000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00OOO0000 ),'signstring':OO0OO0OO00OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            OO00OOO00OO000O0O =requests .request ('get',f'{host}/user',headers =OO0O00000000O0O0O ).json ()#line:87
            if 'status'in OO00OOO00OO000O0O :#line:89
                if OO00OOO00OO000O0O ['status']==200 :#line:90
                    O0O0OOOO000000OOO =OO00OOO00OO000O0O ['data']['nickname']#line:91
                    O0O00O0O0OOO00O0O =OO00OOO00OO000O0O ['data']['inner_id']#line:92
                    O0OOO0O0OO0O00O0O =OO00OOO00OO000O0O ['data']['assets']['gold']#line:93
                    OO000OOOOO0000000 =OO00OOO00OO000O0O ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O0O0OOOO000000OOO[:5]}丨ID:{O0O00O0O0OOO00O0O}丨等级:{OO000OOOOO0000000}丨金种子:{str(O0OOO0O0OO0O00O0O).split(".")[0]}')#line:95
                if OO00OOO00OO000O0O ['status']==401 :#line:96
                    print (OO00OOO00OO000O0O ['message'])#line:97
                    OOO0OO0O00000OOOO .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if OO00OOO00OO000O0O ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O00O0000O0O0OOOO0 :#line:103
            print (O00O0000O0O0OOOO0 )#line:104
    def sealing (OO0O00O0OO0O0O0O0 ):#line:107
        try :#line:108
            OOOO00O00OOOOO000 =f'__{timi_new()}'#line:109
            OO00O00O0OO0OOOOO ={'authorization':OO0O00O0OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OOOOO000 ),'signstring':OOOO00O00OOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O00O0OO0OOOOO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OO00O00O0OO0OOOOO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O00O0OO0OOOOO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O00O0OO0OOOOO )#line:123
            requests .request ('get',f'{host}/user',headers =OO00O00O0OO0OOOOO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O00O0OO0OOOOO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O00O0OO0OOOOO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O00O0OO0OOOOO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O00O0OO0OOOOO )#line:128
            requests .request ('get',f'{host}/assets',headers =OO00O00O0OO0OOOOO )#line:129
        except Exception as OOOO0OO00OO00000O :#line:130
            print (OOOO0OO00OO00000O )#line:131
    def market_sale_buy (OOOOO0000OO0O0OO0 ,_O0O0000O0000OO00O ,O0O0OO00OOOOO00O0 ):#line:139
        try :#line:140
            OO0OOO0OOO00O0O0O =timi_new ()#line:141
            OO0O0OO000O00OOOO =f'_askToBuyId={_O0O0000O0000OO00O}&quantity={O0O0OO00OOOOO00O0}_{OO0OOO0OOO00O0O0O}'#line:142
            O0000OO00OO0O000O ={'source':'scsc','authorization':OOOOO0000OO0O0OO0 .token ,'timestamp':str (OO0OOO0OOO00O0O0O ),'sign':sign (OO0O0OO000O00OOOO ),'signstring':OO0O0OO000O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O00O0OOOO00O0000O ={"askToBuyId":_O0O0000O0000OO00O ,"quantity":O0O0OO00OOOOO00O0 }#line:154
            OOO000OO00O0O0OO0 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0000OO00OO0O000O ,data =O00O0OOOO00O0000O ).json ()#line:155
            if 'status'in OOO000OO00O0O0OO0 :#line:157
                if OOO000OO00O0O0OO0 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OOO000OO00O0O0OO0 ['message']=='请求超时':#line:160
                    OOOOO0000OO0O0OO0 .market_sale_buy (_O0O0000O0000OO00O ,O0O0OO00OOOOO00O0 )#line:161
                else :#line:162
                    print (OOO000OO00O0O0OO0 )#line:163
                    if OOO000OO00O0O0OO0 ['message']=='库存不足':#line:164
                        OOOOO0000OO0O0OO0 .market_sale_buy (_O0O0000O0000OO00O ,O0O0OO00OOOOO00O0 -1 )#line:165
                    exit ()#line:166
        except Exception as O0OO0000OOO0O0OO0 :#line:167
            print (O0OO0000OOO0O0OO0 )#line:168
    def game_map (OO00O000OO0000O00 ,_OOOO0O0O0OO00OO0O ):#line:171
        try :#line:172
            O000OOOOO00O00O00 =f'__{timi_new()}'#line:173
            OO0O00OOOOOO0O0O0 ={'source':'scsc','authorization':OO00O000OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO00O00O00 ),'signstring':O000OOOOO00O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:184
            O000OOOOO00O0O0OO =requests .request ('get',f'{host}/game/map',headers =OO0O00OOOOOO0O0O0 ).json ()#line:185
            print (O000OOOOO00O0O0OO )#line:186
            if 'status'in O000OOOOO00O0O0OO :#line:187
                if O000OOOOO00O0O0OO ['status']==200 :#line:188
                    for OO0OO00O00OOOOOOO in O000OOOOO00O0O0OO ['data']['list'][0 ]['crops']:#line:189
                        OO000O0000OOOO0OO =OO0OO00O00OOOOOOO ['level']#line:191
                        if OO000O0000OOOO0OO ==41 :#line:192
                            OO00O000OOOOOOO00 =OO0OO00O00OOOOOOO ['crop_name']#line:193
                            OO0O000OO00O00O00 =OO0OO00O00OOOOOOO ['count']#line:194
                            if OO0O000OO00O00O00 >0 :#line:195
                                print (f'【农业资产】:{OO00O000OOOOOOO00}丨数量:{OO0O000OO00O00O00}')#line:196
                                OO00O000OO0000O00 .market_sale_buy (_OOOO0O0O0OO00OO0O ,OO0O000OO00O00O00 )#line:197
        except Exception as O0OO0OOO000OOOO0O :#line:198
            print (O0OO0OOO000OOOO0O )#line:199
    def query_to_sell (O0OO0O000OOO00OO0 ):#line:203
        try :#line:204
            O0O00000000OO00OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:205
            O00O0OOOOOO0OO00O ={'source':'scsc','authorization':O0OO0O000OOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000000OO00OO ),'signstring':O0O00000000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:216
            O0O000O00O0OOOO00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00O0OOOOOO0OO00O ).json ()#line:217
            if 'status'in O0O000O00O0OOOO00 :#line:219
                if O0O000O00O0OOOO00 ['status']==200 :#line:220
                    for OO000OO000OO0O00O in O0O000O00O0OOOO00 ['data']['rows']:#line:221
                        O0OO000O00OOOO000 =OO000OO000OO0O00O ['materialKey']#line:222
                        OOO0O000O000O00O0 =OO000OO000OO0O00O ['quantity']#line:223
                        OO0000O0O0O0O0O0O =OO000OO000OO0O00O ['price']#line:224
                        O0O00OO00OO00OO00 =OO000OO000OO0O00O ['saleState']#line:225
                        if O0O00OO00OO00OO00 ==0 :#line:226
                            print (f'【出售订单】:名称:{O0OO000O00OOOO000}丨数量:{OOO0O000O000O00O0}丨价格:{OO0000O0O0O0O0O0O}')#line:227
                            O00OOO000OO0OOO0O =OO000OO000OO0O00O ['id']#line:228
                            O0OO0O000OOO00OO0 .cacel_sale (O00OOO000OO0OOO0O )#line:229
        except Exception as O0O0O00O0OO000O0O :#line:235
            print (O0O0O00O0OO000O0O )#line:236
    def cacel_sale (OOO00O0O0OOOO00O0 ,O0OO0000O00O0O0OO ):#line:240
        try :#line:241
            OO0OOOO0OOOOO0OO0 =f'_saleId={O0OO0000O00O0O0OO}_{timi_new()}'#line:242
            O000O0O0O0000O0O0 ={'source':'scsc','authorization':OOO00O0O0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0OOOOO0OO0 ),'signstring':OO0OOOO0OOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:253
            OO00OO0O00000O000 ={"saleId":O0OO0000O00O0O0OO }#line:256
            O0O0OO000O0000OO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O000O0O0O0000O0O0 ,data =OO00OO0O00000O000 ).json ()#line:257
            if 'status'in O0O0OO000O0000OO0 :#line:259
                if O0O0OO000O0000OO0 ['status']==200 :#line:260
                    print (f'【下架出售】:{O0O0OO000O0000OO0["data"]}')#line:261
        except Exception as OOOOOO0OO00OOO0OO :#line:262
            print (OOOOOO0OO00OOO0OO )#line:263
    def market_buy (OOO0OO00O00O0O0O0 ,O00OO0OOO00OOOO0O ):#line:267
        try :#line:268
            O000000O0OOOOO0O0 ='page=1&pageSize=20&queryField=__1679487573414'#line:269
            OO0O0000OO0000000 ={'authorization':O00OO0OOO00OOOO0O ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':O000000O0OOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:279
            OOOO0O00000OO0O00 =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0O0000OO0000000 ).json ()#line:280
            if 'status'in OOOO0O00000OO0O00 :#line:282
                if OOOO0O00000OO0O00 ['status']==200 :#line:283
                    for OOO00OO00O0O00O00 in OOOO0O00000OO0O00 ['data']['rows']:#line:284
                        O0000OO00O00O0OOO =OOO00OO00O0O00O00 ['id']#line:286
                        OO00O0O00000OOOOO =OOO00OO00O0O00O00 ['price']#line:287
                        OO00OO000OO0O0OO0 =OOO00OO00O0O00O00 ['remainQuantity']#line:288
                        print (f'求购价格:{OO00O0O00000OOOOO}丨求购数量:{OO00OO000OO0O0OO0}丨任务ID:{O0000OO00O00O0OOO}')#line:289
                        return O0000OO00O00O0OOO #line:290
        except Exception as OOO0000OO0000OOO0 :#line:291
            print (OOO0000OO0000OOO0 )#line:292
def start ():#line:297
    try :#line:298
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:299
        O000OO0O00OO00O00 ()#line:300
        O0OO0O0O00O00O00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:301
        _OOOO00O0000O0OOO0 =CityEarth .market_buy (O0OO0O0O00O00O00O ,O0OO0O0O00O00O00O [0 ]['authorization'])#line:302
        print (f"==========共找到{len(O0OO0O0O00O00O00O)}个账号==========")#line:303
        for O000O00O0O0OOO0OO in O0OO0O0O00O00O00O :#line:304
            O0OO0O0OOO0OO000O =[]#line:305
            print (f"------------正在执行第{O0OO0O0O00O00O00O.index(O000O00O0O0OOO0OO) + 1}个账号------------")#line:306
            OOO00000OOO0O00OO =CityEarth (O000O00O0O0OOO0OO ,O0OO0O0OOO0OO000O )#line:307
            if OOO00000OOO0O00OO .base_info ():#line:309
                OOO00000OOO0O00OO .sealing ()#line:311
                OOO00000OOO0O00OO .query_to_sell ()#line:313
                OOO00000OOO0O00OO .game_map (_OOOO00O0000O0OOO0 )#line:316
    except Exception as OO0000O0OOO00O00O :#line:318
        print (OO0000O0OOO00O00O )#line:319
if __name__ =='__main__':#line:322
    start ()#line:323
