import threading #line:2
try :#line:4
    import re #line:5
    import os #line:6
    import sys #line:7
    import time #line:8
    import hashlib #line:9
    import requests #line:10
    import random #line:11
    import json #line:12
    import socket #line:13
except Exception as E :#line:14
    t =re .findall ("d '(.*?)'",str (E ))[0 ]#line:15
    print (f'{t}依赖未安装')#line:16
    sys .exit ()#line:17
"""
@ cron: * * * 8 *
@ new Env('手动出售芦荟')
@ 脚本会取消上架的农作物再出售芦荟
"""#line:23
application ='ce_token'#line:26
version ='3.1.419554351111'#line:27
git ='https://gitee.com'#line:28
host ='http://scsc.sc19319.com'#line:29
golden_seed =0 #line:30
msg_list =[]#line:31
def O000OO0O00OO00O00 ():#line:34
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:35
        pass #line:36
    else :#line:37
        exit (1 )#line:38
def kvkv ():#line:39
    return '/vastzzzl/vastzzzl/raw/master'#line:40
def OO00OO0OO0OO00OO00o0 ():#line:43
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:44
def get_ip ():#line:46
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:47
def gitee_validation ():#line:49
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:50
def sign (OOOOO0O0O000O0O00 ):#line:53
    O0O00OOOO0O0OO000 =hashlib .md5 (OOOOO0O0O000O0O00 .encode ()).hexdigest ()#line:54
    OOOOO000O00OOO000 ="scsc%^&*"+O0O00OOOO0O0OO000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    OOOO0OOO0O0OO00O0 =hashlib .md5 (OOOOO000O00OOO000 .encode ()).hexdigest ()#line:56
    return OOOO0OOO0O0OO00O0 #line:57
def timi_new ():#line:59
    return str (int (time .time ()*1000 ))#line:60
class CityEarth :#line:63
    def __init__ (OOO00O0O0O0O00O0O ,O00OOOO0O00O000OO ,OOOO00OO0OOOOOOOO ):#line:65
        try :#line:66
            OOO00O0O0O0O00O0O .msg =OOOO00OO0OOOOOOOO #line:67
            OOO00O0O0O0O00O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:68
            OOO00O0O0O0O00O0O .token =O00OOOO0O00O000OO ['authorization']#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (O0OO0OOO0O00OOO0O ):#line:74
        try :#line:75
            OOOOOOOOOO0000000 =f'__{timi_new()}'#line:76
            OO00O0O00OOOOO000 ={'source':'scsc','authorization':O0OO0OOO0O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOO0000000 ),'signstring':OOOOOOOOOO0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:87
            OO0O0O0O0OO0O0000 =requests .request ('get',f'{host}/user',headers =OO00O0O00OOOOO000 ).json ()#line:88
            if 'status'in OO0O0O0O0OO0O0000 :#line:90
                if OO0O0O0O0OO0O0000 ['status']==200 :#line:91
                    O0O000OO00O00O00O =OO0O0O0O0OO0O0000 ['data']['nickname']#line:92
                    O0OO0OO0O00O00O00 =OO0O0O0O0OO0O0000 ['data']['inner_id']#line:93
                    O000OOO000O000O00 =OO0O0O0O0OO0O0000 ['data']['assets']['gold']#line:94
                    O0OOO000O00O00OO0 =OO0O0O0O0OO0O0000 ['data']['level']#line:95
                    print (f'【账号信息】:昵称:{O0O000OO00O00O00O[:5]}丨ID:{O0OO0OO0O00O00O00}丨等级:{O0OOO000O00O00OO0}丨金种子:{str(O000OOO000O000O00).split(".")[0]}')#line:96
                if OO0O0O0O0OO0O0000 ['status']==401 :#line:97
                    print (OO0O0O0O0OO0O0000 ['message'])#line:98
                    O0OO0OOO0O00OOO0O .msg .append ('有账号失效了')#line:99
                    return False #line:100
                if OO0O0O0O0OO0O0000 ['status']==500 :#line:101
                    return False #line:102
            return True #line:103
        except Exception as OOO0000O0O000OO00 :#line:104
            print (OOO0000O0O000OO00 )#line:105
    def sealing (O0000O00OO00O00O0 ):#line:108
        try :#line:109
            O00O0000OO000OO0O =f'__{timi_new()}'#line:110
            OO0000OOOOOO00O00 ={'authorization':O0000O00OO00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000OO000OO0O ),'signstring':O00O0000OO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:120
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0000OOOOOO00O00 )#line:121
            requests .request ('get',f'{host}/packsack/list',headers =OO0000OOOOOO00O00 )#line:122
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0000OOOOOO00O00 )#line:123
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0000OOOOOO00O00 )#line:124
            requests .request ('get',f'{host}/user',headers =OO0000OOOOOO00O00 )#line:125
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0000OOOOOO00O00 )#line:126
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0000OOOOOO00O00 )#line:127
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0000OOOOOO00O00 )#line:128
            requests .request ('get',f'{host}/game/getAllData',headers =OO0000OOOOOO00O00 )#line:129
            requests .request ('get',f'{host}/assets',headers =OO0000OOOOOO00O00 )#line:130
        except Exception as O0O0O0OO0OO0O0OOO :#line:131
            print (O0O0O0OO0OO0O0OOO )#line:132
    def market_sale_buy (OOOO00O0OO0OOOOO0 ,_OO00OOO0OOO0O0OO0 ,O0OOO0OOO0OO0000O ):#line:140
        try :#line:141
            OO0OOO00O00OOOOOO =timi_new ()#line:142
            O0OOO00OOO00O0000 =f'_askToBuyId={_OO00OOO0OOO0O0OO0}&quantity={O0OOO0OOO0OO0000O}_{OO0OOO00O00OOOOOO}'#line:143
            O0O0OO00O00OOOO0O ={'source':'scsc','authorization':OOOO00O0OO0OOOOO0 .token ,'timestamp':str (OO0OOO00O00OOOOOO ),'sign':sign (O0OOO00OOO00O0000 ),'signstring':O0OOO00OOO00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            OOOO0O00O0000000O ={"askToBuyId":_OO00OOO0OOO0O0OO0 ,"quantity":O0OOO0OOO0OO0000O }#line:155
            O0O000O0000O0O00O =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0O0OO00O00OOOO0O ,data =OOOO0O00O0000000O ).json ()#line:156
            if 'status'in O0O000O0000O0O00O :#line:158
                if O0O000O0000O0O00O ['status']==200 :#line:159
                    print ('【出售求购】:出售成功')#line:160
                elif O0O000O0000O0O00O ['message']=='请求超时':#line:161
                    OOOO00O0OO0OOOOO0 .market_sale_buy (_OO00OOO0OOO0O0OO0 ,O0OOO0OOO0OO0000O )#line:162
                else :#line:163
                    print (O0O000O0000O0O00O )#line:164
                    if O0O000O0000O0O00O ['message']=='库存不足':#line:165
                        OOOO00O0OO0OOOOO0 .market_sale_buy (_OO00OOO0OOO0O0OO0 ,O0OOO0OOO0OO0000O -1 )#line:166
                    if O0O000O0000O0O00O ['message']=='更新求购单失败':#line:167
                        exit ()#line:168
                    if O0O000O0000O0O00O ['message']=='购买数量不足':#line:169
                        exit ()#line:170
                    if O0O000O0000O0O00O ['message']=='商品不存在或取消求购':#line:171
                        exit ()#line:172
                    if O0O000O0000O0O00O ['message']=='购买数量不足':#line:173
                        exit ()#line:174
        except Exception as OOOOO00OO00000OOO :#line:176
            print (OOOOO00OO00000OOO )#line:177
    def game_map (OOO0O0OOO0O0OOOOO ,_OO0OO0000OOO000OO ):#line:180
        try :#line:181
            O0OO0O0OOO0000000 =f'__{timi_new()}'#line:182
            O0O00OO0O0O0O00OO ={'source':'scsc','authorization':OOO0O0OOO0O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOO0000000 ),'signstring':O0OO0O0OOO0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:193
            O0O00OOO00O0O0O0O =requests .request ('get',f'{host}/game/map',headers =O0O00OO0O0O0O00OO ).json ()#line:194
            if 'status'in O0O00OOO00O0O0O0O :#line:196
                if O0O00OOO00O0O0O0O ['status']==200 :#line:197
                    for O00O00O000000O000 in O0O00OOO00O0O0O0O ['data']['list'][0 ]['crops']:#line:198
                        O0O000OO0O0OOOOOO =O00O00O000000O000 ['level']#line:200
                        if O0O000OO0O0OOOOOO ==41 :#line:201
                            OO00OOOOO000O00OO =O00O00O000000O000 ['crop_name']#line:202
                            O00000O00O0OO0000 =O00O00O000000O000 ['count']#line:203
                            if O00000O00O0OO0000 >0 :#line:204
                                print (f'【农业资产】:{OO00OOOOO000O00OO}丨数量:{O00000O00O0OO0000}')#line:205
                                OOO0O0OOO0O0OOOOO .market_sale_buy (_OO0OO0000OOO000OO ,O00000O00O0OO0000 )#line:206
        except Exception as O00OOO00O0O00O00O :#line:207
            print (O00OOO00O0O00O00O )#line:208
    def query_to_sell (OO00OO00O0000O0O0 ):#line:212
        try :#line:213
            OOO0OO00O0OO0000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:214
            OOO0O000OOOO00O00 ={'source':'scsc','authorization':OO00OO00O0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0OO0000O ),'signstring':OOO0OO00O0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:225
            O00000OO0O000O0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0O000OOOO00O00 ).json ()#line:226
            if 'status'in O00000OO0O000O0O0 :#line:228
                if O00000OO0O000O0O0 ['status']==200 :#line:229
                    for OOO0O0O0OOO0000OO in O00000OO0O000O0O0 ['data']['rows']:#line:230
                        OOO0000OOOOOO00O0 =OOO0O0O0OOO0000OO ['materialKey']#line:231
                        O0O0OOO00O0OOO00O =OOO0O0O0OOO0000OO ['quantity']#line:232
                        OOO00O000OOOO0O00 =OOO0O0O0OOO0000OO ['price']#line:233
                        O00O00OOOO0O00O0O =OOO0O0O0OOO0000OO ['saleState']#line:234
                        if O00O00OOOO0O00O0O ==0 :#line:235
                            print (f'【出售订单】:名称:{OOO0000OOOOOO00O0}丨数量:{O0O0OOO00O0OOO00O}丨价格:{OOO00O000OOOO0O00}')#line:236
                            OOOOOOO0OO00O0OOO =OOO0O0O0OOO0000OO ['id']#line:237
                            OO00OO00O0000O0O0 .cacel_sale (OOOOOOO0OO00O0OOO )#line:238
        except Exception as OO0O00OO0OO00O00O :#line:244
            print (OO0O00OO0OO00O00O )#line:245
    def cacel_sale (OOOO000OO0O000OO0 ,OOO0O0O0O00O00OOO ):#line:249
        try :#line:250
            OO000OOOO0O0O0O0O =f'_saleId={OOO0O0O0O00O00OOO}_{timi_new()}'#line:251
            OO0OO0OOOOOOO0O0O ={'source':'scsc','authorization':OOOO000OO0O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO0O0O0O0O ),'signstring':OO000OOOO0O0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:262
            O0O00OOOOO0OO0O00 ={"saleId":OOO0O0O0O00O00OOO }#line:265
            O0O00O0O00OOOOO0O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO0OOOOOOO0O0O ,data =O0O00OOOOO0OO0O00 ).json ()#line:266
            if 'status'in O0O00O0O00OOOOO0O :#line:268
                if O0O00O0O00OOOOO0O ['status']==200 :#line:269
                    print (f'【下架出售】:{O0O00O0O00OOOOO0O["data"]}')#line:270
        except Exception as OO00O0O000OOOOOOO :#line:271
            print (OO00O0O000OOOOOOO )#line:272
    def market_buy (OO000O00OOO000O0O ,OOO00O0OOOOOO000O ):#line:276
        try :#line:277
            OO0OO000OO0OO0O0O ='page=1&pageSize=20&queryField=__1679487573414'#line:278
            O0O000OO000O00000 ={'authorization':OOO00O0OOOOOO000O ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OO0OO000OO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:288
            O00OOO0000OO00O00 =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O000OO000O00000 ).json ()#line:289
            if 'status'in O00OOO0000OO00O00 :#line:291
                if O00OOO0000OO00O00 ['status']==200 :#line:292
                    for OOO0O00O0O00O0OOO in O00OOO0000OO00O00 ['data']['rows']:#line:293
                        OOOOO0000O0000OO0 =OOO0O00O0O00O0OOO ['id']#line:295
                        O0OO00OOO0OO00OO0 =OOO0O00O0O00O0OOO ['price']#line:296
                        OOO0OOOOOOOOO0OOO =OOO0O00O0O00O0OOO ['remainQuantity']#line:297
                        print (f'求购价格:{O0OO00OOO0OO00OO0}丨求购数量:{OOO0OOOOOOOOO0OOO}丨任务ID:{OOOOO0000O0000OO0}')#line:298
                        return OOOOO0000O0000OO0 #line:299
        except Exception as O0O00OOO00OOO0OOO :#line:300
            print (O0O00OOO00OOO0OOO )#line:301
def start ():#line:306
    try :#line:307
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:308
        O000OO0O00OO00O00 ()#line:309
        OOO0O00000O00OOOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:310
        _O00O0OO0OO0O00O00 =CityEarth .market_buy (OOO0O00000O00OOOO ,OOO0O00000O00OOOO [0 ]['authorization'])#line:311
        print (f"==========共找到{len(OOO0O00000O00OOOO)}个账号==========")#line:312
        for OO000O00OO0000O0O in OOO0O00000O00OOOO :#line:313
            O00OOO0000OOO0O00 =[]#line:314
            print (f"------------正在执行第{OOO0O00000O00OOOO.index(OO000O00OO0000O0O) + 1}个账号------------")#line:315
            O0000000OO0O0OOOO =CityEarth (OO000O00OO0000O0O ,O00OOO0000OOO0O00 )#line:316
            if O0000000OO0O0OOOO .base_info ():#line:318
                def O000O000O0OOO0O0O ():#line:319
                    O0000000OO0O0OOOO .sealing ()#line:321
                    O0000000OO0O0OOOO .query_to_sell ()#line:323
                OO0000OOO00000OO0 =threading .Thread (target =O000O000O0OOO0O0O )#line:324
                OO0000OOO00000OO0 .start ()#line:325
                O0000000OO0O0OOOO .game_map (_O00O0OO0OO0O00O00 )#line:328
    except Exception as O0OOO0OO000000O0O :#line:330
        print (O0OOO0OO000000O0O )#line:331
if __name__ =='__main__':#line:334
    start ()#line:335
