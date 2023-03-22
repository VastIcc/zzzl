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
def sign (OOOOO0OOOO000OOO0 ):#line:52
    O00OO0OOO00OOO0O0 =hashlib .md5 (OOOOO0OOOO000OOO0 .encode ()).hexdigest ()#line:53
    OO00O000000OOO00O ="scsc%^&*"+O00OO0OOO00OOO0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    O00OOO00O0O0OO00O =hashlib .md5 (OO00O000000OOO00O .encode ()).hexdigest ()#line:55
    return O00OOO00O0O0OO00O #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0OO00OO00000O0O0 ,O000O0OOOOO0OO0O0 ,OOOOO0O0OO0000OOO ):#line:64
        try :#line:65
            O0OO00OO00000O0O0 .msg =OOOOO0O0OO0000OOO #line:66
            O0OO00OO00000O0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0OO00OO00000O0O0 .token =O000O0OOOOO0OO0O0 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OO0OO0O0OO0OOO00O ):#line:73
        try :#line:74
            O0000O000O0OO00O0 =f'__{timi_new()}'#line:75
            OOOOOOOO00OO0OO00 ={'source':'scsc','authorization':OO0OO0O0OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000O0OO00O0 ),'signstring':O0000O000O0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            OO0OOOO0OOOO0O0O0 =requests .request ('get',f'{host}/user',headers =OOOOOOOO00OO0OO00 ).json ()#line:87
            if 'status'in OO0OOOO0OOOO0O0O0 :#line:89
                if OO0OOOO0OOOO0O0O0 ['status']==200 :#line:90
                    O00OO00OOOOOO00OO =OO0OOOO0OOOO0O0O0 ['data']['nickname']#line:91
                    OO00O0O0OOO0OO0O0 =OO0OOOO0OOOO0O0O0 ['data']['inner_id']#line:92
                    OOOO00OOO0O0OO00O =OO0OOOO0OOOO0O0O0 ['data']['assets']['gold']#line:93
                    OO0O00O000OOO0OOO =OO0OOOO0OOOO0O0O0 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O00OO00OOOOOO00OO[:5]}丨ID:{OO00O0O0OOO0OO0O0}丨等级:{OO0O00O000OOO0OOO}丨金种子:{str(OOOO00OOO0O0OO00O).split(".")[0]}')#line:95
                if OO0OOOO0OOOO0O0O0 ['status']==401 :#line:96
                    print (OO0OOOO0OOOO0O0O0 ['message'])#line:97
                    OO0OO0O0OO0OOO00O .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if OO0OOOO0OOOO0O0O0 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0000O00O00O0OO0O :#line:103
            print (O0000O00O00O0OO0O )#line:104
    def sealing (OO0OO0OOOO000O000 ):#line:107
        try :#line:108
            OOOOOO00000000OOO =f'__{timi_new()}'#line:109
            O00O00000O00OOO00 ={'authorization':OO0OO0OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00000000OOO ),'signstring':OOOOOO00000000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O00000O00OOO00 )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O00O00000O00OOO00 )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O00000O00OOO00 )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O00000O00OOO00 )#line:123
            requests .request ('get',f'{host}/user',headers =O00O00000O00OOO00 )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O00000O00OOO00 )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O00000O00OOO00 )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O00000O00OOO00 )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O00O00000O00OOO00 )#line:128
            requests .request ('get',f'{host}/assets',headers =O00O00000O00OOO00 )#line:129
        except Exception as OOOO00OOOOOO00O00 :#line:130
            print (OOOO00OOOOOO00O00 )#line:131
    def market_sale_buy (OO000O0OO000OO0O0 ,_O0OO0O0O000OO000O ,O0OOO00O00000O0O0 ):#line:139
        try :#line:140
            O0O0OOOOOOO00OO00 =timi_new ()#line:141
            OO00O00000000OOOO =f'_askToBuyId={_O0OO0O0O000OO000O}&quantity={O0OOO00O00000O0O0}_{O0O0OOOOOOO00OO00}'#line:142
            O000O0OO00OOO0OO0 ={'source':'scsc','authorization':OO000O0OO000OO0O0 .token ,'timestamp':str (O0O0OOOOOOO00OO00 ),'sign':sign (OO00O00000000OOOO ),'signstring':OO00O00000000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            OOOOOOOOOOO00000O ={"askToBuyId":_O0OO0O0O000OO000O ,"quantity":O0OOO00O00000O0O0 }#line:154
            OOO00OO00O0OOOOOO =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O000O0OO00OOO0OO0 ,data =OOOOOOOOOOO00000O ).json ()#line:155
            if 'status'in OOO00OO00O0OOOOOO :#line:157
                if OOO00OO00O0OOOOOO ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OOO00OO00O0OOOOOO ['message']=='请求超时':#line:160
                    OO000O0OO000OO0O0 .market_sale_buy (_O0OO0O0O000OO000O ,O0OOO00O00000O0O0 )#line:161
                else :#line:162
                    print (OOO00OO00O0OOOOOO )#line:163
                    exit ()#line:164
        except Exception as O0000O000O00OOOO0 :#line:165
            print (O0000O000O00OOOO0 )#line:166
    def game_map (OOO0O00000OO0O0OO ,_OOO00000O0O0000O0 ):#line:169
        try :#line:170
            O00O0O00O0O000O0O =f'__{timi_new()}'#line:171
            O000000OOO0O0OOO0 ={'source':'scsc','authorization':OOO0O00000OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00O0O000O0O ),'signstring':O00O0O00O0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:182
            O000000000OOO0O00 =requests .request ('get',f'{host}/game/map',headers =O000000OOO0O0OOO0 ).json ()#line:183
            if 'status'in O000000000OOO0O00 :#line:185
                if O000000000OOO0O00 ['status']==200 :#line:186
                    for O00O0O00O0OOOO000 in O000000000OOO0O00 ['data']['list'][0 ]['crops']:#line:187
                        OO0O0OO0OO000O00O =O00O0O00O0OOOO000 ['level']#line:189
                        if OO0O0OO0OO000O00O ==41 :#line:190
                            O0OO0O00000OOO0OO =O00O0O00O0OOOO000 ['crop_name']#line:191
                            OOOOOOOOOOOO0OO0O =O00O0O00O0OOOO000 ['count']#line:192
                            if OOOOOOOOOOOO0OO0O >0 :#line:193
                                print (f'【农业资产】:{O0OO0O00000OOO0OO}丨数量:{OOOOOOOOOOOO0OO0O}')#line:194
                                OOO0O00000OO0O0OO .market_sale_buy (_OOO00000O0O0000O0 ,OOOOOOOOOOOO0OO0O )#line:195
        except Exception as O0OO000OO00O0O0OO :#line:196
            print (O0OO000OO00O0O0OO )#line:197
    def query_to_sell (OOOOOO000O00OOO0O ):#line:201
        try :#line:202
            O0000OO000OOOOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:203
            O0OOO00000OOO0O0O ={'source':'scsc','authorization':OOOOOO000O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO000OOOOOOO ),'signstring':O0000OO000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            O0O00O00000OOO000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OOO00000OOO0O0O ).json ()#line:215
            if 'status'in O0O00O00000OOO000 :#line:217
                if O0O00O00000OOO000 ['status']==200 :#line:218
                    for O0O0O00OO00000OO0 in O0O00O00000OOO000 ['data']['rows']:#line:219
                        O0OO000O0OOO00O00 =O0O0O00OO00000OO0 ['materialKey']#line:220
                        OO000O0OO000OOOO0 =O0O0O00OO00000OO0 ['quantity']#line:221
                        OO00OO0OO000000O0 =O0O0O00OO00000OO0 ['price']#line:222
                        O0OO000000OOOOO0O =O0O0O00OO00000OO0 ['saleState']#line:223
                        if O0OO000000OOOOO0O ==0 :#line:224
                            print (f'【出售订单】:名称:{O0OO000O0OOO00O00}丨数量:{OO000O0OO000OOOO0}丨价格:{OO00OO0OO000000O0}')#line:225
                            OOOO0OO00OOO0O00O =O0O0O00OO00000OO0 ['id']#line:226
                            OOOOOO000O00OOO0O .cacel_sale (OOOO0OO00OOO0O00O )#line:227
        except Exception as O0OO0OOO00OOOO000 :#line:233
            print (O0OO0OOO00OOOO000 )#line:234
    def cacel_sale (O0O0OOO0OO000O000 ,O0OOO0000000O00O0 ):#line:238
        try :#line:239
            OOOO00OOO000O0O00 =f'_saleId={O0OOO0000000O00O0}_{timi_new()}'#line:240
            O0O0OOOO0O00OO00O ={'source':'scsc','authorization':O0O0OOO0OO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO000O0O00 ),'signstring':OOOO00OOO000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            OO0000000000O0OO0 ={"saleId":O0OOO0000000O00O0 }#line:254
            OOO0O00O00OO0O0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0OOOO0O00OO00O ,data =OO0000000000O0OO0 ).json ()#line:255
            if 'status'in OOO0O00O00OO0O0OO :#line:257
                if OOO0O00O00OO0O0OO ['status']==200 :#line:258
                    print (f'【下架出售】:{OOO0O00O00OO0O0OO["data"]}')#line:259
        except Exception as O00OOOO0O0O0O0OO0 :#line:260
            print (O00OOOO0O0O0O0OO0 )#line:261
    def market_buy (OO00OOO0000OO0O00 ,OO0O00OOOOOOO0O00 ):#line:265
        try :#line:266
            OOO0OOO0O00O000O0 ='page=1&pageSize=20&queryField=__1679487573414'#line:267
            OO0OO0O0OO0O0OO00 ={'authorization':OO0O00OOOOOOO0O00 ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OOO0OOO0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:277
            O000OOO000O000000 =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OO0O0OO0O0OO00 ).json ()#line:278
            if 'status'in O000OOO000O000000 :#line:280
                if O000OOO000O000000 ['status']==200 :#line:281
                    for OO0O0O0O00OO00000 in O000OOO000O000000 ['data']['rows']:#line:282
                        OOOO000OOO00OO000 =OO0O0O0O00OO00000 ['id']#line:284
                        OO0O0000OO0O0OOO0 =OO0O0O0O00OO00000 ['price']#line:285
                        OO0O00000O000OO00 =OO0O0O0O00OO00000 ['remainQuantity']#line:286
                        print (f'求购价格:{OO0O0000OO0O0OOO0}丨求购数量:{OO0O00000O000OO00}丨任务ID:{OOOO000OOO00OO000}')#line:287
                        return OOOO000OOO00OO000 #line:288
        except Exception as OO0OOO0OO0O00O000 :#line:289
            print (OO0OOO0OO0O00O000 )#line:290
def start ():#line:295
    try :#line:296
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:297
        O000OO0O00OO00O00 ()#line:298
        O00OO00OO0000O00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:299
        _OO0O0OOO000O0O0OO =CityEarth .market_buy (O00OO00OO0000O00O ,O00OO00OO0000O00O [0 ]['authorization'])#line:300
        print (f"==========共找到{len(O00OO00OO0000O00O)}个账号==========")#line:301
        for O000OO000O00O0O0O in O00OO00OO0000O00O :#line:302
            OO000OO0O00OO00O0 =[]#line:303
            print (f"------------正在执行第{O00OO00OO0000O00O.index(O000OO000O00O0O0O) + 1}个账号------------")#line:304
            OO00OO0O0O00000O0 =CityEarth (O000OO000O00O0O0O ,OO000OO0O00OO00O0 )#line:305
            if OO00OO0O0O00000O0 .base_info ():#line:307
                OO00OO0O0O00000O0 .sealing ()#line:309
                OO00OO0O0O00000O0 .query_to_sell ()#line:311
                OO00OO0O0O00000O0 .game_map (_OO0O0OOO000O0O0OO )#line:315
    except Exception as O00O00OOOO0O0O0OO :#line:317
        print (O00O00OOOO0O0O0OO )#line:318
if __name__ =='__main__':#line:321
    start ()#line:322
