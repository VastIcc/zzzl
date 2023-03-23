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
version ='3.1.419554351111'#line:26
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
def sign (O0O0OO000OOO000OO ):#line:52
    OOOOOO0OOO0O0OO00 =hashlib .md5 (O0O0OO000OOO000OO .encode ()).hexdigest ()#line:53
    O0OOOO0O0O00OO0OO ="scsc%^&*"+OOOOOO0OOO0O0OO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    O00000OOO0O00OO0O =hashlib .md5 (O0OOOO0O0O00OO0OO .encode ()).hexdigest ()#line:55
    return O00000OOO0O00OO0O #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0000OO00OOOOOOOO ,OO000000OOOO000O0 ,O0OOO00OO0000O0O0 ):#line:64
        try :#line:65
            O0000OO00OOOOOOOO .msg =O0OOO00OO0000O0O0 #line:66
            O0000OO00OOOOOOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0000OO00OOOOOOOO .token =OO000000OOOO000O0 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OO00O0000OO00OOO0 ):#line:73
        try :#line:74
            OO0OO0O00000O0OOO =f'__{timi_new()}'#line:75
            OO0000000OOO00O00 ={'source':'scsc','authorization':OO00O0000OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00000O0OOO ),'signstring':OO0OO0O00000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            OOO0O0OOO0000O000 =requests .request ('get',f'{host}/user',headers =OO0000000OOO00O00 ).json ()#line:87
            if 'status'in OOO0O0OOO0000O000 :#line:89
                if OOO0O0OOO0000O000 ['status']==200 :#line:90
                    OO000OO000O00O000 =OOO0O0OOO0000O000 ['data']['nickname']#line:91
                    OOOO000OOO000OOOO =OOO0O0OOO0000O000 ['data']['inner_id']#line:92
                    OO00OOO0OOO00OOO0 =OOO0O0OOO0000O000 ['data']['assets']['gold']#line:93
                    O0OO000O0O00OO00O =OOO0O0OOO0000O000 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO000OO000O00O000[:5]}丨ID:{OOOO000OOO000OOOO}丨等级:{O0OO000O0O00OO00O}丨金种子:{str(OO00OOO0OOO00OOO0).split(".")[0]}')#line:95
                if OOO0O0OOO0000O000 ['status']==401 :#line:96
                    print (OOO0O0OOO0000O000 ['message'])#line:97
                    OO00O0000OO00OOO0 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if OOO0O0OOO0000O000 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as OOO0OOO0OO0O0O0O0 :#line:103
            print (OOO0OOO0OO0O0O0O0 )#line:104
    def sealing (OOO000OOOO0O0O000 ):#line:107
        try :#line:108
            OO0OO0OO0OO00O0O0 =f'__{timi_new()}'#line:109
            OOOO0OO0OO0O0O0OO ={'authorization':OOO000OOOO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0OO00O0O0 ),'signstring':OO0OO0OO0OO00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO0OO0OO0O0O0OO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OOOO0OO0OO0O0O0OO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO0OO0OO0O0O0OO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO0OO0OO0O0O0OO )#line:123
            requests .request ('get',f'{host}/user',headers =OOOO0OO0OO0O0O0OO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO0OO0OO0O0O0OO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO0OO0OO0O0O0OO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO0OO0OO0O0O0OO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OO0OO0O0O0OO )#line:128
            requests .request ('get',f'{host}/assets',headers =OOOO0OO0OO0O0O0OO )#line:129
        except Exception as O00O0O00OOOO0O0OO :#line:130
            print (O00O0O00OOOO0O0OO )#line:131
    def market_sale_buy (O0O0000000OOOOO00 ,_O00O00O0OOO0O00OO ,O0O0O0OO000O0O00O ):#line:139
        try :#line:140
            O00OOO0O00OO000O0 =timi_new ()#line:141
            O0000O0000O0O0O0O =f'_askToBuyId={_O00O00O0OOO0O00OO}&quantity={O0O0O0OO000O0O00O}_{O00OOO0O00OO000O0}'#line:142
            OOOO000OOOOOOOO0O ={'source':'scsc','authorization':O0O0000000OOOOO00 .token ,'timestamp':str (O00OOO0O00OO000O0 ),'sign':sign (O0000O0000O0O0O0O ),'signstring':O0000O0000O0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            OOO000OO00O0OOOOO ={"askToBuyId":_O00O00O0OOO0O00OO ,"quantity":O0O0O0OO000O0O00O }#line:154
            O00OOO000OOOOO0OO =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOOO000OOOOOOOO0O ,data =OOO000OO00O0OOOOO ).json ()#line:155
            if 'status'in O00OOO000OOOOO0OO :#line:157
                if O00OOO000OOOOO0OO ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif O00OOO000OOOOO0OO ['message']=='请求超时':#line:160
                    O0O0000000OOOOO00 .market_sale_buy (_O00O00O0OOO0O00OO ,O0O0O0OO000O0O00O )#line:161
                else :#line:162
                    print (O00OOO000OOOOO0OO )#line:163
                    if O00OOO000OOOOO0OO ['message']=='库存不足':#line:164
                        O0O0000000OOOOO00 .market_sale_buy (_O00O00O0OOO0O00OO ,O0O0O0OO000O0O00O -1 )#line:165
                    if O00OOO000OOOOO0OO ['message']=='更新求购单失败':#line:166
                        exit ()#line:167
                    if O00OOO000OOOOO0OO ['message']=='购买数量不足':#line:168
                        exit ()#line:169
                    if O00OOO000OOOOO0OO ['message']=='商品不存在或取消求购':#line:170
                        exit ()#line:171
                    if O00OOO000OOOOO0OO ['message']=='购买数量不足':#line:172
                        exit ()#line:173
        except Exception as OOO0000OOO00OO00O :#line:175
            print (OOO0000OOO00OO00O )#line:176
    def game_map (OO000OO0O000O00O0 ,_OOO0OOOO00O00O00O ):#line:179
        try :#line:180
            OO0000O000OOO0OOO =f'__{timi_new()}'#line:181
            O000O00OOOO000O00 ={'source':'scsc','authorization':OO000OO0O000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O000OOO0OOO ),'signstring':OO0000O000OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
            OO0OO00O00OOOOO0O =requests .request ('get',f'{host}/game/map',headers =O000O00OOOO000O00 ).json ()#line:193
            if 'status'in OO0OO00O00OOOOO0O :#line:195
                if OO0OO00O00OOOOO0O ['status']==200 :#line:196
                    for O00O0000OOO0O0000 in OO0OO00O00OOOOO0O ['data']['list'][0 ]['crops']:#line:197
                        OO00OOO000OOO0OO0 =O00O0000OOO0O0000 ['level']#line:199
                        if OO00OOO000OOO0OO0 ==41 :#line:200
                            OOO000O0O0O00000O =O00O0000OOO0O0000 ['crop_name']#line:201
                            O0OOO0OO00OOOOO0O =O00O0000OOO0O0000 ['count']#line:202
                            if O0OOO0OO00OOOOO0O >0 :#line:203
                                print (f'【农业资产】:{OOO000O0O0O00000O}丨数量:{O0OOO0OO00OOOOO0O}')#line:204
                                OO000OO0O000O00O0 .market_sale_buy (_OOO0OOOO00O00O00O ,O0OOO0OO00OOOOO0O )#line:205
        except Exception as OO00O0OO00O00OO0O :#line:206
            print (OO00O0OO00O00OO0O )#line:207
    def query_to_sell (O000O0O0O000O000O ):#line:211
        try :#line:212
            O000OOO0O0000O0OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:213
            OOO00OO0000O0O0OO ={'source':'scsc','authorization':O000O0O0O000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O0000O0OO ),'signstring':O000OOO0O0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:224
            O000OOO0O0O00O00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00OO0000O0O0OO ).json ()#line:225
            if 'status'in O000OOO0O0O00O00O :#line:227
                if O000OOO0O0O00O00O ['status']==200 :#line:228
                    for O00O0OOOO0OO0O00O in O000OOO0O0O00O00O ['data']['rows']:#line:229
                        OO0OO0O000O0O0O0O =O00O0OOOO0OO0O00O ['materialKey']#line:230
                        O00OOO0O0O0O00O0O =O00O0OOOO0OO0O00O ['quantity']#line:231
                        OOOO0O0OOOOO0OO0O =O00O0OOOO0OO0O00O ['price']#line:232
                        OOOO0OO0OO00O0O0O =O00O0OOOO0OO0O00O ['saleState']#line:233
                        if OOOO0OO0OO00O0O0O ==0 :#line:234
                            print (f'【出售订单】:名称:{OO0OO0O000O0O0O0O}丨数量:{O00OOO0O0O0O00O0O}丨价格:{OOOO0O0OOOOO0OO0O}')#line:235
                            OO0OO00O000OOO000 =O00O0OOOO0OO0O00O ['id']#line:236
                            O000O0O0O000O000O .cacel_sale (OO0OO00O000OOO000 )#line:237
        except Exception as OOO00000OOO00O000 :#line:243
            print (OOO00000OOO00O000 )#line:244
    def cacel_sale (OO0OO00000OOO000O ,O0O0OO0OOOOOO0O00 ):#line:248
        try :#line:249
            OO00OO0O0O0O000O0 =f'_saleId={O0O0OO0OOOOOO0O00}_{timi_new()}'#line:250
            O00000O0OO00O0O0O ={'source':'scsc','authorization':OO0OO00000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O0O0O000O0 ),'signstring':OO00OO0O0O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:261
            O00O000000000O00O ={"saleId":O0O0OO0OOOOOO0O00 }#line:264
            O000OO0OOO0OOO0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00000O0OO00O0O0O ,data =O00O000000000O00O ).json ()#line:265
            if 'status'in O000OO0OOO0OOO0OO :#line:267
                if O000OO0OOO0OOO0OO ['status']==200 :#line:268
                    print (f'【下架出售】:{O000OO0OOO0OOO0OO["data"]}')#line:269
        except Exception as O0O0OO0OO00OOO0OO :#line:270
            print (O0O0OO0OO00OOO0OO )#line:271
    def market_buy (OO000O0000000O000 ,O0OOOOOO000O0O00O ):#line:275
        try :#line:276
            O0OOO00O0O0OO0O00 ='page=1&pageSize=20&queryField=__1679487573414'#line:277
            O0OO00OOO0000OO0O ={'authorization':O0OOOOOO000O0O00O ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':O0OOO00O0O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:287
            OOO00OOO0OOO0000O =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OO00OOO0000OO0O ).json ()#line:288
            if 'status'in OOO00OOO0OOO0000O :#line:290
                if OOO00OOO0OOO0000O ['status']==200 :#line:291
                    for OOOOOO000O0O0OOO0 in OOO00OOO0OOO0000O ['data']['rows']:#line:292
                        OOO000O000OO00OO0 =OOOOOO000O0O0OOO0 ['id']#line:294
                        OOO0OOO0OOO0O00O0 =OOOOOO000O0O0OOO0 ['price']#line:295
                        O00OOOOOOO000O00O =OOOOOO000O0O0OOO0 ['remainQuantity']#line:296
                        print (f'求购价格:{OOO0OOO0OOO0O00O0}丨求购数量:{O00OOOOOOO000O00O}丨任务ID:{OOO000O000OO00OO0}')#line:297
                        return OOO000O000OO00OO0 #line:298
        except Exception as O0OOOOOOO0000OOOO :#line:299
            print (O0OOOOOOO0000OOOO )#line:300
def start ():#line:305
    try :#line:306
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:307
        O000OO0O00OO00O00 ()#line:308
        O00OO000OOOOO0OO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:309
        _OOO0OO00000O0O00O =CityEarth .market_buy (O00OO000OOOOO0OO0 ,O00OO000OOOOO0OO0 [0 ]['authorization'])#line:310
        print (f"==========共找到{len(O00OO000OOOOO0OO0)}个账号==========")#line:311
        for O000O000000O0O0OO in O00OO000OOOOO0OO0 :#line:312
            O000OOO0O000OO0OO =[]#line:313
            print (f"------------正在执行第{O00OO000OOOOO0OO0.index(O000O000000O0O0OO) + 1}个账号------------")#line:314
            O00O0OO00000O0OOO =CityEarth (O000O000000O0O0OO ,O000OOO0O000OO0OO )#line:315
            if O00O0OO00000O0OOO .base_info ():#line:317
                O00O0OO00000O0OOO .sealing ()#line:319
                O00O0OO00000O0OOO .query_to_sell ()#line:321
                O00O0OO00000O0OOO .game_map (_OOO0OO00000O0O00O )#line:324
    except Exception as O0O00OOO000000OO0 :#line:326
        print (O0O00OOO000000OO0 )#line:327
if __name__ =='__main__':#line:330
    start ()#line:331
