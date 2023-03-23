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
def sign (OOOO0OOO000000O0O ):#line:52
    OOO0OOOO0O000O000 =hashlib .md5 (OOOO0OOO000000O0O .encode ()).hexdigest ()#line:53
    OO0O0O0O00O00OO00 ="scsc%^&*"+OOO0OOOO0O000O000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOOOO00O00000O0OO =hashlib .md5 (OO0O0O0O00O00OO00 .encode ()).hexdigest ()#line:55
    return OOOOO00O00000O0OO #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (OOO0OOO0O000O0O0O ,OO00OO0O00OO00000 ,OOOOOO000OOOOOO0O ):#line:64
        try :#line:65
            OOO0OOO0O000O0O0O .msg =OOOOOO000OOOOOO0O #line:66
            OOO0OOO0O000O0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            OOO0OOO0O000O0O0O .token =OO00OO0O00OO00000 ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OOO0OO0OOOOO00O00 ):#line:73
        try :#line:74
            OO00O0OO0O00O0OOO =f'__{timi_new()}'#line:75
            O0000000O0OO0OOOO ={'source':'scsc','authorization':OOO0OO0OOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO0O00O0OOO ),'signstring':OO00O0OO0O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O00OOOO00OOO00O00 =requests .request ('get',f'{host}/user',headers =O0000000O0OO0OOOO ).json ()#line:87
            if 'status'in O00OOOO00OOO00O00 :#line:89
                if O00OOOO00OOO00O00 ['status']==200 :#line:90
                    OO0O00OO00000O000 =O00OOOO00OOO00O00 ['data']['nickname']#line:91
                    O0OOOO0OOO00O000O =O00OOOO00OOO00O00 ['data']['inner_id']#line:92
                    OOO0OO00O0O00O00O =O00OOOO00OOO00O00 ['data']['assets']['gold']#line:93
                    OO0OOOO00O00OOOOO =O00OOOO00OOO00O00 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO0O00OO00000O000[:5]}丨ID:{O0OOOO0OOO00O000O}丨等级:{OO0OOOO00O00OOOOO}丨金种子:{str(OOO0OO00O0O00O00O).split(".")[0]}')#line:95
                if O00OOOO00OOO00O00 ['status']==401 :#line:96
                    print (O00OOOO00OOO00O00 ['message'])#line:97
                    OOO0OO0OOOOO00O00 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O00OOOO00OOO00O00 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O0OO000O0O0000OOO :#line:103
            print (O0OO000O0O0000OOO )#line:104
    def sealing (OOOO00OOOOO0OO0O0 ):#line:107
        try :#line:108
            OOOO0OO00O00OOOOO =f'__{timi_new()}'#line:109
            OO0OOOO0OO000OOOO ={'authorization':OOOO00OOOOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O00OOOOO ),'signstring':OOOO0OO00O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOOO0OO000OOOO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOOO0OO000OOOO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOOO0OO000OOOO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOOO0OO000OOOO )#line:123
            requests .request ('get',f'{host}/user',headers =OO0OOOO0OO000OOOO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOOO0OO000OOOO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOOO0OO000OOOO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOOO0OO000OOOO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOO0OO000OOOO )#line:128
            requests .request ('get',f'{host}/assets',headers =OO0OOOO0OO000OOOO )#line:129
        except Exception as OOOO00O0OOOOOOOO0 :#line:130
            print (OOOO00O0OOOOOOOO0 )#line:131
    def market_sale_buy (OOO00O0O00O0OOOOO ,_O00O000O00OOO0OOO ,OO000OOO0O00OOO0O ):#line:139
        try :#line:140
            OOO000OO0OO000OOO =timi_new ()#line:141
            O0OO0OO0O0OO0OO0O =f'_askToBuyId={_O00O000O00OOO0OOO}&quantity={OO000OOO0O00OOO0O}_{OOO000OO0OO000OOO}'#line:142
            OO000OO0O000O0O00 ={'source':'scsc','authorization':OOO00O0O00O0OOOOO .token ,'timestamp':str (OOO000OO0OO000OOO ),'sign':sign (O0OO0OO0O0OO0OO0O ),'signstring':O0OO0OO0O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            OOOO00O000000O000 ={"askToBuyId":_O00O000O00OOO0OOO ,"quantity":OO000OOO0O00OOO0O }#line:154
            O00000OO000000O00 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OO000OO0O000O0O00 ,data =OOOO00O000000O000 ).json ()#line:155
            if 'status'in O00000OO000000O00 :#line:157
                if O00000OO000000O00 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                elif O00000OO000000O00 ['message']=='请求超时':#line:160
                    OOO00O0O00O0OOOOO .market_sale_buy (_O00O000O00OOO0OOO ,OO000OOO0O00OOO0O )#line:161
                else :#line:162
                    print (O00000OO000000O00 )#line:163
                    if O00000OO000000O00 ['message']=='库存不足':#line:164
                        OOO00O0O00O0OOOOO .market_sale_buy (_O00O000O00OOO0OOO ,OO000OOO0O00OOO0O -1 )#line:165
                    if O00000OO000000O00 ['message']=='更新求购单失败':#line:166
                        exit ()#line:167
                    if O00000OO000000O00 ['message']=='购买数量不足':#line:168
                        exit ()#line:169
                    if O00000OO000000O00 ['message']=='商品不存在或取消求购':#line:170
                        exit ()#line:171
                    if O00000OO000000O00 ['message']=='购买数量不足':#line:172
                        exit ()#line:173
        except Exception as O00000O0OOOOOOO0O :#line:175
            print (O00000O0OOOOOOO0O )#line:176
    def game_map (O0O0OOO0OO0OOO00O ,_OO000OOOO0O0OOO0O ):#line:179
        try :#line:180
            OO0O00O00O00OO00O =f'__{timi_new()}'#line:181
            OOOO00OO0000O0000 ={'source':'scsc','authorization':O0O0OOO0OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00O00OO00O ),'signstring':OO0O00O00O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:192
            O000OOOO000O0OO00 =requests .request ('get',f'{host}/game/map',headers =OOOO00OO0000O0000 ).json ()#line:193
            if 'status'in O000OOOO000O0OO00 :#line:195
                if O000OOOO000O0OO00 ['status']==200 :#line:196
                    for OO00OO0OO00OO0OOO in O000OOOO000O0OO00 ['data']['list'][0 ]['crops']:#line:197
                        OO0000O0O00OO00O0 =OO00OO0OO00OO0OOO ['level']#line:199
                        if OO0000O0O00OO00O0 ==41 :#line:200
                            O0O00OO00OO000000 =OO00OO0OO00OO0OOO ['crop_name']#line:201
                            OO00O0OOOOO0OOO00 =OO00OO0OO00OO0OOO ['count']#line:202
                            if OO00O0OOOOO0OOO00 >0 :#line:203
                                print (f'【农业资产】:{O0O00OO00OO000000}丨数量:{OO00O0OOOOO0OOO00}')#line:204
                                O0O0OOO0OO0OOO00O .market_sale_buy (_OO000OOOO0O0OOO0O ,OO00O0OOOOO0OOO00 )#line:205
        except Exception as O00O00000OO00OOO0 :#line:206
            print (O00O00000OO00OOO0 )#line:207
    def query_to_sell (O00O0OOOOO0OOO0O0 ):#line:211
        try :#line:212
            OOOO0OO0OO0O00000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:213
            OO000O00000O0O0OO ={'source':'scsc','authorization':O00O0OOOOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0OO0O00000 ),'signstring':OOOO0OO0OO0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:224
            OO0O0OO0OOOOOO0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO000O00000O0O0OO ).json ()#line:225
            if 'status'in OO0O0OO0OOOOOO0O0 :#line:227
                if OO0O0OO0OOOOOO0O0 ['status']==200 :#line:228
                    for OO0OOO0O0O00O000O in OO0O0OO0OOOOOO0O0 ['data']['rows']:#line:229
                        O0OO0OO00O00OO00O =OO0OOO0O0O00O000O ['materialKey']#line:230
                        OOO0O0O0OO000OOO0 =OO0OOO0O0O00O000O ['quantity']#line:231
                        O000O0O0O00O000O0 =OO0OOO0O0O00O000O ['price']#line:232
                        O0000O00O0O00000O =OO0OOO0O0O00O000O ['saleState']#line:233
                        if O0000O00O0O00000O ==0 :#line:234
                            print (f'【出售订单】:名称:{O0OO0OO00O00OO00O}丨数量:{OOO0O0O0OO000OOO0}丨价格:{O000O0O0O00O000O0}')#line:235
                            OO00OOOO0O0000O00 =OO0OOO0O0O00O000O ['id']#line:236
                            O00O0OOOOO0OOO0O0 .cacel_sale (OO00OOOO0O0000O00 )#line:237
        except Exception as OOOO00O0O000OOOO0 :#line:243
            print (OOOO00O0O000OOOO0 )#line:244
    def cacel_sale (O00OO0000OO0OO0OO ,OO000O00OO00O0O00 ):#line:248
        try :#line:249
            OOOOOOOO00OO0O0OO =f'_saleId={OO000O00OO00O0O00}_{timi_new()}'#line:250
            OO0OOO0O0OOO0O0O0 ={'source':'scsc','authorization':O00OO0000OO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO00OO0O0OO ),'signstring':OOOOOOOO00OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:261
            O0OOOOOO0OOO0OO0O ={"saleId":OO000O00OO00O0O00 }#line:264
            OO0000O0O0O00O0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OOO0O0OOO0O0O0 ,data =O0OOOOOO0OOO0OO0O ).json ()#line:265
            if 'status'in OO0000O0O0O00O0OO :#line:267
                if OO0000O0O0O00O0OO ['status']==200 :#line:268
                    print (f'【下架出售】:{OO0000O0O0O00O0OO["data"]}')#line:269
        except Exception as O000OOOOO000000OO :#line:270
            print (O000OOOOO000000OO )#line:271
    def market_buy (O0OO0OO00O0O0OO00 ,O0OO0O0OO0OO0OO00 ):#line:275
        try :#line:276
            OO0000OOOO0000OO0 ='page=1&pageSize=20&queryField=__1679487573414'#line:277
            OO0000000000OO0O0 ={'authorization':O0OO0O0OO0OO0OO00 ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OO0000OOOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:287
            OO000O0000O00OO00 =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0000000000OO0O0 ).json ()#line:288
            if 'status'in OO000O0000O00OO00 :#line:290
                if OO000O0000O00OO00 ['status']==200 :#line:291
                    for OOO0OO0O0O00O0000 in OO000O0000O00OO00 ['data']['rows']:#line:292
                        O0O00O00OO00000OO =OOO0OO0O0O00O0000 ['id']#line:294
                        O0O00O0O0O000O000 =OOO0OO0O0O00O0000 ['price']#line:295
                        O00O0OOOOOO000OOO =OOO0OO0O0O00O0000 ['remainQuantity']#line:296
                        print (f'求购价格:{O0O00O0O0O000O000}丨求购数量:{O00O0OOOOOO000OOO}丨任务ID:{O0O00O00OO00000OO}')#line:297
                        return O0O00O00OO00000OO #line:298
        except Exception as O0000OOOO0OO0O0O0 :#line:299
            print (O0000OOOO0OO0O0O0 )#line:300
def start ():#line:305
    try :#line:306
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:307
        O000OO0O00OO00O00 ()#line:308
        O0O0OO0O0OO0O0000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:309
        _O0OO00O0O0000OOOO =CityEarth .market_buy (O0O0OO0O0OO0O0000 ,O0O0OO0O0OO0O0000 [0 ]['authorization'])#line:310
        print (f"==========共找到{len(O0O0OO0O0OO0O0000)}个账号==========")#line:311
        for OOOO0O0O000O0OO0O in O0O0OO0O0OO0O0000 :#line:312
            O000OOOO0OOOOOOO0 =[]#line:313
            print (f"------------正在执行第{O0O0OO0O0OO0O0000.index(OOOO0O0O000O0OO0O) + 1}个账号------------")#line:314
            OOO0O00OOO0000000 =CityEarth (OOOO0O0O000O0OO0O ,O000OOOO0OOOOOOO0 )#line:315
            if OOO0O00OOO0000000 .base_info ():#line:317
                OOO0O00OOO0000000 .sealing ()#line:319
                OOO0O00OOO0000000 .query_to_sell ()#line:321
                OOO0O00OOO0000000 .game_map (_O0OO00O0O0000OOOO )#line:324
    except Exception as OOOOO00OOOO00O000 :#line:326
        print (OOOOO00OOOO00O000 )#line:327
if __name__ =='__main__':#line:330
    start ()#line:331
