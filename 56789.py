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
def sign (O00O00OOO0O0O000O ):#line:52
    OO000O000O00OOO00 =hashlib .md5 (O00O00OOO0O0O000O .encode ()).hexdigest ()#line:53
    O0O000O000OO0OOO0 ="scsc%^&*"+OO000O000O00OOO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOO000O00O0O00OO0 =hashlib .md5 (O0O000O000OO0OOO0 .encode ()).hexdigest ()#line:55
    return OOO000O00O0O00OO0 #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O00OOO0OO000O0O0O ,OO0OO000OO0OO0O0O ,O00O0O0OO00OOO0OO ):#line:64
        try :#line:65
            O00OOO0OO000O0O0O .msg =O00O0O0OO00OOO0OO #line:66
            O00OOO0OO000O0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O00OOO0OO000O0O0O .token =OO0OO000OO0OO0O0O ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O00OOOO0OOOO00OO0 ):#line:73
        try :#line:74
            OOOOO00OOO0OOOO00 =f'__{timi_new()}'#line:75
            OO0O00OO00O00OOOO ={'source':'scsc','authorization':O00OOOO0OOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOO0OOOO00 ),'signstring':OOOOO00OOO0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            OO00OO00O0O0OOO00 =requests .request ('get',f'{host}/user',headers =OO0O00OO00O00OOOO ).json ()#line:87
            if 'status'in OO00OO00O0O0OOO00 :#line:89
                if OO00OO00O0O0OOO00 ['status']==200 :#line:90
                    O0000OO0O0O00OO0O =OO00OO00O0O0OOO00 ['data']['nickname']#line:91
                    OOOO00OO0O0000000 =OO00OO00O0O0OOO00 ['data']['inner_id']#line:92
                    O0O0OO000OO0OO00O =OO00OO00O0O0OOO00 ['data']['assets']['gold']#line:93
                    OO0000O0O0O0000OO =OO00OO00O0O0OOO00 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O0000OO0O0O00OO0O[:5]}丨ID:{OOOO00OO0O0000000}丨等级:{OO0000O0O0O0000OO}丨金种子:{str(O0O0OO000OO0OO00O).split(".")[0]}')#line:95
                if OO00OO00O0O0OOO00 ['status']==401 :#line:96
                    print (OO00OO00O0O0OOO00 ['message'])#line:97
                    O00OOOO0OOOO00OO0 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if OO00OO00O0O0OOO00 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O00OO0O00O00OOOOO :#line:103
            print (O00OO0O00O00OOOOO )#line:104
    def sealing (O0OO0OOOOO0OO0O0O ):#line:107
        try :#line:108
            O000O0O00000O00O0 =f'__{timi_new()}'#line:109
            O00OO0OOO000000O0 ={'authorization':O0OO0OOOOO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O00000O00O0 ),'signstring':O000O0O00000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO0OOO000000O0 )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O00OO0OOO000000O0 )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO0OOO000000O0 )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO0OOO000000O0 )#line:123
            requests .request ('get',f'{host}/user',headers =O00OO0OOO000000O0 )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO0OOO000000O0 )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO0OOO000000O0 )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO0OOO000000O0 )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO0OOO000000O0 )#line:128
            requests .request ('get',f'{host}/assets',headers =O00OO0OOO000000O0 )#line:129
        except Exception as O0000O000O0O0O0OO :#line:130
            print (O0000O000O0O0O0OO )#line:131
    def market_sale_buy (O0O000O0OO0OOOO0O ,_OO0O0O0O0OO00000O ,OO0OO00O00O00OO0O ):#line:139
        try :#line:140
            OOO0OOO00O0O0O00O =timi_new ()#line:141
            O00OO0O000O0O0O00 =f'_askToBuyId={_OO0O0O0O0OO00000O}&quantity={OO0OO00O00O00OO0O}_{OOO0OOO00O0O0O00O}'#line:142
            OOO0OOOOO0O00OO0O ={'source':'scsc','authorization':O0O000O0OO0OOOO0O .token ,'timestamp':str (OOO0OOO00O0O0O00O ),'sign':sign (O00OO0O000O0O0O00 ),'signstring':O00OO0O000O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            OO00000000000OOO0 ={"askToBuyId":_OO0O0O0O0OO00000O ,"quantity":OO0OO00O00O00OO0O }#line:154
            OO00000OO0000O00O =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOO0OOOOO0O00OO0O ,data =OO00000000000OOO0 ).json ()#line:155
            if 'status'in OO00000OO0000O00O :#line:157
                if OO00000OO0000O00O ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif OO00000OO0000O00O ['message']=='请求超时':#line:160
                    O0O000O0OO0OOOO0O .market_sale_buy (_OO0O0O0O0OO00000O ,OO0OO00O00O00OO0O )#line:161
                else :#line:162
                    print (OO00000OO0000O00O )#line:163
                    if OO00000OO0000O00O ['message']=='库存不足':#line:164
                        O0O000O0OO0OOOO0O .market_sale_buy (_OO0O0O0O0OO00000O ,OO0OO00O00O00OO0O -1 )#line:165
                    if OO00000OO0000O00O ['message']=='更新求购单失败':#line:166
                        exit ()#line:167
                    if OO00000OO0000O00O ['message']=='购买数量不足':#line:168
                        exit ()#line:169
                    if OO00000OO0000O00O ['message']=='商品不存在或取消求购':#line:170
                        exit ()#line:171
                    if OO00000OO0000O00O ['message']=='购买数量不足':#line:172
                        exit ()#line:173
        except Exception as O0OOO00000OOOO0O0 :#line:175
            print (O0OOO00000OOOO0O0 )#line:176
    def game_map (OOO0OO0OO0O0O00O0 ,_O0OOO0OO0O00000OO ):#line:179
        try :#line:180
            O00O00000OO00OOOO =f'__{timi_new()}'#line:181
            O0O0O0OO000O00O0O ={'source':'scsc','authorization':OOO0OO0OO0O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OO00OOOO ),'signstring':O00O00000OO00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
            OO00O00OOOO0O0O00 =requests .request ('get',f'{host}/game/map',headers =O0O0O0OO000O00O0O ).json ()#line:193
            if 'status'in OO00O00OOOO0O0O00 :#line:195
                if OO00O00OOOO0O0O00 ['status']==200 :#line:196
                    for O000O0O0OO0O0OO0O in OO00O00OOOO0O0O00 ['data']['list'][0 ]['crops']:#line:197
                        O00O00OO00000O00O =O000O0O0OO0O0OO0O ['level']#line:199
                        if O00O00OO00000O00O ==41 :#line:200
                            O0O000O000O00O00O =O000O0O0OO0O0OO0O ['crop_name']#line:201
                            O0O000O0O0000O000 =O000O0O0OO0O0OO0O ['count']#line:202
                            if O0O000O0O0000O000 >0 :#line:203
                                print (f'【农业资产】:{O0O000O000O00O00O}丨数量:{O0O000O0O0000O000}')#line:204
                                OOO0OO0OO0O0O00O0 .market_sale_buy (_O0OOO0OO0O00000OO ,O0O000O0O0000O000 )#line:205
        except Exception as OOOO000O0O0OO00O0 :#line:206
            print (OOOO000O0O0OO00O0 )#line:207
    def query_to_sell (OO0OO000O000O0OOO ):#line:211
        try :#line:212
            O000OOOO0OOO0OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:213
            O0OO00OO0OO00OOOO ={'source':'scsc','authorization':OO0OO000O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0OOO0OO00 ),'signstring':O000OOOO0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:224
            O00O0O00O000OOO00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00OO0OO00OOOO ).json ()#line:225
            if 'status'in O00O0O00O000OOO00 :#line:227
                if O00O0O00O000OOO00 ['status']==200 :#line:228
                    for OO00O0O0OO0O00O0O in O00O0O00O000OOO00 ['data']['rows']:#line:229
                        O0OO0OOOOOO00000O =OO00O0O0OO0O00O0O ['materialKey']#line:230
                        OO00O000O0O00O00O =OO00O0O0OO0O00O0O ['quantity']#line:231
                        O00000O0OO00O0OOO =OO00O0O0OO0O00O0O ['price']#line:232
                        OO0O000O00OO000O0 =OO00O0O0OO0O00O0O ['saleState']#line:233
                        if OO0O000O00OO000O0 ==0 :#line:234
                            print (f'【出售订单】:名称:{O0OO0OOOOOO00000O}丨数量:{OO00O000O0O00O00O}丨价格:{O00000O0OO00O0OOO}')#line:235
                            O00OO0O0O0OO00O00 =OO00O0O0OO0O00O0O ['id']#line:236
                            OO0OO000O000O0OOO .cacel_sale (O00OO0O0O0OO00O00 )#line:237
        except Exception as OO0O0OOOO0OO0O0OO :#line:243
            print (OO0O0OOOO0OO0O0OO )#line:244
    def cacel_sale (O0OO0OOO0O0OO0OOO ,O0OOOO0O0O00OOOOO ):#line:248
        try :#line:249
            O000O00O0000O00O0 =f'_saleId={O0OOOO0O0O00OOOOO}_{timi_new()}'#line:250
            OO000000OOO0000O0 ={'source':'scsc','authorization':O0OO0OOO0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0000O00O0 ),'signstring':O000O00O0000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:261
            O0OOOO00O0O00OO0O ={"saleId":O0OOOO0O0O00OOOOO }#line:264
            OO0OOO0O00000OOO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO000000OOO0000O0 ,data =O0OOOO00O0O00OO0O ).json ()#line:265
            if 'status'in OO0OOO0O00000OOO0 :#line:267
                if OO0OOO0O00000OOO0 ['status']==200 :#line:268
                    print (f'【下架出售】:{OO0OOO0O00000OOO0["data"]}')#line:269
        except Exception as O0O00O00000O0O0OO :#line:270
            print (O0O00O00000O0O0OO )#line:271
    def market_buy (O00000OO00OOOO000 ,OOO00O0OO0OOO00OO ):#line:275
        try :#line:276
            OOOO0O0O0O00OOOOO ='page=1&pageSize=20&queryField=__1679487573414'#line:277
            OO00OO0OO0000OO0O ={'authorization':OOO00O0OO0OOO00OO ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OOOO0O0O0O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:287
            O0000O000OO0OOOOO =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO00OO0OO0000OO0O ).json ()#line:288
            if 'status'in O0000O000OO0OOOOO :#line:290
                if O0000O000OO0OOOOO ['status']==200 :#line:291
                    for O00O0O0OOOO000O00 in O0000O000OO0OOOOO ['data']['rows']:#line:292
                        OOO000OOOOOOOO000 =O00O0O0OOOO000O00 ['id']#line:294
                        OOO0000OO0O0OO00O =O00O0O0OOOO000O00 ['price']#line:295
                        OO00000O00O00O0OO =O00O0O0OOOO000O00 ['remainQuantity']#line:296
                        print (f'求购价格:{OOO0000OO0O0OO00O}丨求购数量:{OO00000O00O00O0OO}丨任务ID:{OOO000OOOOOOOO000}')#line:297
                        return OOO000OOOOOOOO000 #line:298
        except Exception as OO0000O00000OO000 :#line:299
            print (OO0000O00000OO000 )#line:300
def start ():#line:305
    try :#line:306
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:307
        O000OO0O00OO00O00 ()#line:308
        OOO000OO0OOOOOOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:309
        _O00OO0O0OO0OOOO00 =CityEarth .market_buy (OOO000OO0OOOOOOO0 ,OOO000OO0OOOOOOO0 [0 ]['authorization'])#line:310
        print (f"==========共找到{len(OOO000OO0OOOOOOO0)}个账号==========")#line:311
        for O00OOO0OOOO0000OO in OOO000OO0OOOOOOO0 :#line:312
            O0O00000O000O00OO =[]#line:313
            print (f"------------正在执行第{OOO000OO0OOOOOOO0.index(O00OOO0OOOO0000OO) + 1}个账号------------")#line:314
            O000OOO00O0O0O0OO =CityEarth (O00OOO0OOOO0000OO ,O0O00000O000O00OO )#line:315
            if O000OOO00O0O0O0OO .base_info ():#line:317
                O000OOO00O0O0O0OO .sealing ()#line:319
                O000OOO00O0O0O0OO .query_to_sell ()#line:321
                O000OOO00O0O0O0OO .game_map (_O00OO0O0OO0OOOO00 )#line:324
    except Exception as O0OOOO000O00O0OO0 :#line:326
        print (O0OOOO000O00O0OO0 )#line:327
if __name__ =='__main__':#line:330
    start ()#line:331
