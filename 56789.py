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
def sign (O0OOOO0OO000O0O0O ):#line:52
    OOO00OOOO0O0OOO00 =hashlib .md5 (O0OOOO0OO000O0O0O .encode ()).hexdigest ()#line:53
    O0O00O0O00OO000OO ="scsc%^&*"+OOO00OOOO0O0OOO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    O0000O0000O00000O =hashlib .md5 (O0O00O0O00OO000OO .encode ()).hexdigest ()#line:55
    return O0000O0000O00000O #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (OOOO0OOOOOO00000O ,OOOOO0OOOOOOOO00O ,O0OOOOOOO00OO0OOO ):#line:64
        try :#line:65
            OOOO0OOOOOO00000O .msg =O0OOOOOOO00OO0OOO #line:66
            OOOO0OOOOOO00000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            OOOO0OOOOOO00000O .token =OOOOO0OOOOOOOO00O ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O0O0000O000OO0OOO ):#line:73
        try :#line:74
            OO0O0000OO00O00O0 =f'__{timi_new()}'#line:75
            O0O0OOO0O00OOO00O ={'source':'scsc','authorization':O0O0000O000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO00O00O0 ),'signstring':OO0O0000OO00O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O0OOO0O00OOOOO0O0 =requests .request ('get',f'{host}/user',headers =O0O0OOO0O00OOO00O ).json ()#line:87
            if 'status'in O0OOO0O00OOOOO0O0 :#line:89
                if O0OOO0O00OOOOO0O0 ['status']==200 :#line:90
                    O0OOO0O0O000O0000 =O0OOO0O00OOOOO0O0 ['data']['nickname']#line:91
                    OOOOO000OOOOOOOO0 =O0OOO0O00OOOOO0O0 ['data']['inner_id']#line:92
                    OO000000O0OO0000O =O0OOO0O00OOOOO0O0 ['data']['assets']['gold']#line:93
                    O0OO00O0O00000O00 =O0OOO0O00OOOOO0O0 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O0OOO0O0O000O0000[:5]}丨ID:{OOOOO000OOOOOOOO0}丨等级:{O0OO00O0O00000O00}丨金种子:{str(OO000000O0OO0000O).split(".")[0]}')#line:95
                if O0OOO0O00OOOOO0O0 ['status']==401 :#line:96
                    print (O0OOO0O00OOOOO0O0 ['message'])#line:97
                    O0O0000O000OO0OOO .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O0OOO0O00OOOOO0O0 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as OOOOOO0O0000O00O0 :#line:103
            print (OOOOOO0O0000O00O0 )#line:104
    def sealing (OOO000O0000O0O0OO ):#line:107
        try :#line:108
            OO000OO0OO000O0OO =f'__{timi_new()}'#line:109
            OOOO00OOOOOO0OO00 ={'authorization':OOO000O0000O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OO000O0OO ),'signstring':OO000OO0OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO00OOOOOO0OO00 )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OOOO00OOOOOO0OO00 )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO00OOOOOO0OO00 )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO00OOOOOO0OO00 )#line:123
            requests .request ('get',f'{host}/user',headers =OOOO00OOOOOO0OO00 )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO00OOOOOO0OO00 )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO00OOOOOO0OO00 )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO00OOOOOO0OO00 )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OOOOOO0OO00 )#line:128
            requests .request ('get',f'{host}/assets',headers =OOOO00OOOOOO0OO00 )#line:129
        except Exception as O00O00OOOO0O0OO00 :#line:130
            print (O00O00OOOO0O0OO00 )#line:131
    def market_sale_buy (OOOOOO00O0O00OO0O ,_O0000OOO0O000O0O0 ,O00O00OO0O00OOO0O ):#line:139
        try :#line:140
            O0O0OOO0O00OOO000 =timi_new ()#line:141
            OO000O0O0OOOOO000 =f'_askToBuyId={_O0000OOO0O000O0O0}&quantity={O00O00OO0O00OOO0O}_{O0O0OOO0O00OOO000}'#line:142
            O0O000000O00OOOO0 ={'source':'scsc','authorization':OOOOOO00O0O00OO0O .token ,'timestamp':str (O0O0OOO0O00OOO000 ),'sign':sign (OO000O0O0OOOOO000 ),'signstring':OO000O0O0OOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O0O0O00O00OOO0O0O ={"askToBuyId":_O0000OOO0O000O0O0 ,"quantity":O00O00OO0O00OOO0O }#line:154
            O0OO00OO0O0O00O0O =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0O000000O00OOOO0 ,data =O0O0O00O00OOO0O0O ).json ()#line:155
            if 'status'in O0OO00OO0O0O00O0O :#line:157
                if O0OO00OO0O0O00O0O ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif O0OO00OO0O0O00O0O ['message']=='请求超时':#line:160
                    OOOOOO00O0O00OO0O .market_sale_buy (_O0000OOO0O000O0O0 ,O00O00OO0O00OOO0O )#line:161
                else :#line:162
                    print (O0OO00OO0O0O00O0O )#line:163
                    if O0OO00OO0O0O00O0O ['message']=='库存不足':#line:164
                        OOOOOO00O0O00OO0O .market_sale_buy (_O0000OOO0O000O0O0 ,O00O00OO0O00OOO0O -1 )#line:165
                    if O0OO00OO0O0O00O0O ['message']=='更新求购单失败':#line:166
                        exit ()#line:167
                    if O0OO00OO0O0O00O0O ['message']=='购买数量不足':#line:168
                        exit ()#line:169
                    if O0OO00OO0O0O00O0O ['message']=='商品不存在或取消求购':#line:170
                        exit ()#line:171
                    if O0OO00OO0O0O00O0O ['message']=='购买数量不足':#line:172
                        exit ()#line:173
        except Exception as O0O0O0O0O0OOOOO00 :#line:175
            print (O0O0O0O0O0OOOOO00 )#line:176
    def game_map (OO000OO0O00OOOOO0 ,_O000O0O0OOOOO0OO0 ):#line:179
        try :#line:180
            OO000OO00OO0OOOO0 =f'__{timi_new()}'#line:181
            OOOOOOO0O0O000O0O ={'source':'scsc','authorization':OO000OO0O00OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00OO0OOOO0 ),'signstring':OO000OO00OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
            OOOOO00OO0OO0000O =requests .request ('get',f'{host}/game/map',headers =OOOOOOO0O0O000O0O ).json ()#line:193
            print (OOOOO00OO0OO0000O )#line:194
            if 'status'in OOOOO00OO0OO0000O :#line:195
                if OOOOO00OO0OO0000O ['status']==200 :#line:196
                    for O00O0OOO00O0OOOO0 in OOOOO00OO0OO0000O ['data']['list'][0 ]['crops']:#line:197
                        OOO0OO0O0O0OOOOOO =O00O0OOO00O0OOOO0 ['level']#line:199
                        if OOO0OO0O0O0OOOOOO ==41 :#line:200
                            OO00O0000000OO0O0 =O00O0OOO00O0OOOO0 ['crop_name']#line:201
                            O00O000O00O0OOOO0 =O00O0OOO00O0OOOO0 ['count']#line:202
                            if O00O000O00O0OOOO0 >0 :#line:203
                                print (f'【农业资产】:{OO00O0000000OO0O0}丨数量:{O00O000O00O0OOOO0}')#line:204
                                OO000OO0O00OOOOO0 .market_sale_buy (_O000O0O0OOOOO0OO0 ,O00O000O00O0OOOO0 )#line:205
        except Exception as OO0OOO0O000OO00OO :#line:206
            print (OO0OOO0O000OO00OO )#line:207
    def query_to_sell (OO0O00OO0OOO0OO0O ):#line:211
        try :#line:212
            OOOO00O0OO0O00O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:213
            O0OO00O0OOO0OOO00 ={'source':'scsc','authorization':OO0O00OO0OOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0OO0O00O0O ),'signstring':OOOO00O0OO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:224
            O0OOOOOO0O0O0O000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00O0OOO0OOO00 ).json ()#line:225
            if 'status'in O0OOOOOO0O0O0O000 :#line:227
                if O0OOOOOO0O0O0O000 ['status']==200 :#line:228
                    for OO00O0O00O0O00000 in O0OOOOOO0O0O0O000 ['data']['rows']:#line:229
                        OOOO0OOOOOOO0O0O0 =OO00O0O00O0O00000 ['materialKey']#line:230
                        O0000O0O00000OOO0 =OO00O0O00O0O00000 ['quantity']#line:231
                        OOO000OO00O0O0O00 =OO00O0O00O0O00000 ['price']#line:232
                        O0O000OOO000O000O =OO00O0O00O0O00000 ['saleState']#line:233
                        if O0O000OOO000O000O ==0 :#line:234
                            print (f'【出售订单】:名称:{OOOO0OOOOOOO0O0O0}丨数量:{O0000O0O00000OOO0}丨价格:{OOO000OO00O0O0O00}')#line:235
                            O00O0OO000000OOO0 =OO00O0O00O0O00000 ['id']#line:236
                            OO0O00OO0OOO0OO0O .cacel_sale (O00O0OO000000OOO0 )#line:237
        except Exception as O0OO0O0OO0OOOOO00 :#line:243
            print (O0OO0O0OO0OOOOO00 )#line:244
    def cacel_sale (O00O00OOO0OOOOO00 ,O000O00OOOOOO00O0 ):#line:248
        try :#line:249
            O0O00OOO0OO0O0O00 =f'_saleId={O000O00OOOOOO00O0}_{timi_new()}'#line:250
            O00OO0000OO000000 ={'source':'scsc','authorization':O00O00OOO0OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO0OO0O0O00 ),'signstring':O0O00OOO0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:261
            OO00O0000000O00OO ={"saleId":O000O00OOOOOO00O0 }#line:264
            OOOOOO000O0000O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OO0000OO000000 ,data =OO00O0000000O00OO ).json ()#line:265
            if 'status'in OOOOOO000O0000O00 :#line:267
                if OOOOOO000O0000O00 ['status']==200 :#line:268
                    print (f'【下架出售】:{OOOOOO000O0000O00["data"]}')#line:269
        except Exception as O0O0O00O000O0O0OO :#line:270
            print (O0O0O00O000O0O0OO )#line:271
    def market_buy (OOO00OOOOO0OOOOOO ,O0OOO0O00O0O0O000 ):#line:275
        try :#line:276
            OOOOO0OOO0OO0OOO0 ='page=1&pageSize=20&queryField=__1679487573414'#line:277
            OO0O00OO00O0O00OO ={'authorization':O0OOO0O00O0O0O000 ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OOOOO0OOO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:287
            OOOOOOOOO0OO0000O =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0O00OO00O0O00OO ).json ()#line:288
            if 'status'in OOOOOOOOO0OO0000O :#line:290
                if OOOOOOOOO0OO0000O ['status']==200 :#line:291
                    for OOO00O00O00OO00OO in OOOOOOOOO0OO0000O ['data']['rows']:#line:292
                        O00OOOO0O0OOOO0O0 =OOO00O00O00OO00OO ['id']#line:294
                        OOOOOO00OOOO0000O =OOO00O00O00OO00OO ['price']#line:295
                        OO0OO000O0O000O0O =OOO00O00O00OO00OO ['remainQuantity']#line:296
                        print (f'求购价格:{OOOOOO00OOOO0000O}丨求购数量:{OO0OO000O0O000O0O}丨任务ID:{O00OOOO0O0OOOO0O0}')#line:297
                        return O00OOOO0O0OOOO0O0 #line:298
        except Exception as O0OO0O0OO00O0O00O :#line:299
            print (O0OO0O0OO00O0O00O )#line:300
def start ():#line:305
    try :#line:306
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:307
        O000OO0O00OO00O00 ()#line:308
        O0000OOO00OOO0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:309
        _OOO0O0OO0000O0OO0 =CityEarth .market_buy (O0000OOO00OOO0OOO ,O0000OOO00OOO0OOO [0 ]['authorization'])#line:310
        print (f"==========共找到{len(O0000OOO00OOO0OOO)}个账号==========")#line:311
        for OO0OOOO00OOOOOO0O in O0000OOO00OOO0OOO :#line:312
            O000OO0O0OO000OO0 =[]#line:313
            print (f"------------正在执行第{O0000OOO00OOO0OOO.index(OO0OOOO00OOOOOO0O) + 1}个账号------------")#line:314
            OOOO0O00O000OOOO0 =CityEarth (OO0OOOO00OOOOOO0O ,O000OO0O0OO000OO0 )#line:315
            if OOOO0O00O000OOOO0 .base_info ():#line:317
                OOOO0O00O000OOOO0 .sealing ()#line:319
                OOOO0O00O000OOOO0 .query_to_sell ()#line:321
                OOOO0O00O000OOOO0 .game_map (_OOO0O0OO0000O0OO0 )#line:324
    except Exception as O000OO0O000O0OO0O :#line:326
        print (O000OO0O000O0OO0O )#line:327
if __name__ =='__main__':#line:330
    start ()#line:331
