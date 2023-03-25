# coding: utf-8
import threading

try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
    import random
    import json
    import socket
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: */30 * * * *
@ new Env('手动出售芦荟')
@ 脚本会取消上架的农作物再出售芦荟
"""
##################################配置区##################################
pica_aa = '3.95'  # 价格低于就不出售给求购
##################################配置区##################################
##################################下面不要动##################################
application ='ce_token'#line:1
version ='3.1.419554351111'#line:2
git ='https://gitee.com'#line:3
host ='http://scsc.sc19319.com'#line:4
golden_seed =0 #line:5
msg_list =[]#line:6
def O000OO0O00OO00O00 ():#line:9
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:10
        pass #line:11
    else :#line:12
        exit (1 )#line:13
def kvkv ():#line:14
    return '/vastzzzl/vastzzzl/raw/master'#line:15
def OO00OO0OO0OO00OO00o0 ():#line:18
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:19
def get_ip ():#line:21
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:22
def gitee_validation ():#line:24
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:25
def sign (OO0OOOO0000OO00O0 ):#line:28
    OOOO00O00O0OO0000 =hashlib .md5 (OO0OOOO0000OO00O0 .encode ()).hexdigest ()#line:29
    OO000000OOOO0OO0O ="scsc%^&*"+OOOO00O00O0OO0000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:30
    O00OO0OO000OOO0OO =hashlib .md5 (OO000000OOOO0OO0O .encode ()).hexdigest ()#line:31
    return O00OO0OO000OOO0OO #line:32
def timi_new ():#line:34
    return str (int (time .time ()*1000 ))#line:35
class CityEarth :#line:38
    def __init__ (O000O000O0O0O0OOO ,OOOO0OO00000OO000 ,O000O00O00000OOO0 ):#line:40
        try :#line:41
            O000O000O0O0O0OOO .msg =O000O00O00000OOO0 #line:42
            O000O000O0O0O0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:43
            O000O000O0O0O0OOO .token =OOOO0OO00000OO000 ['authorization']#line:44
        except :#line:45
            print ('变量格式错误')#line:46
    def base_info (O0000000000OOOOOO ):#line:49
        try :#line:50
            OO0OOO0O0OOOO0OOO =f'__{timi_new()}'#line:51
            OO00OOOOOO000000O ={'source':'scsc','authorization':O0000000000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OOOO0OOO ),'signstring':OO0OOO0O0OOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:62
            O00OO0O000OOO00OO =requests .request ('get',f'{host}/user',headers =OO00OOOOOO000000O ).json ()#line:63
            if 'status'in O00OO0O000OOO00OO :#line:65
                if O00OO0O000OOO00OO ['status']==200 :#line:66
                    OOO0O0OOO0O0O000O =O00OO0O000OOO00OO ['data']['nickname']#line:67
                    O00O0OOO000OOO000 =O00OO0O000OOO00OO ['data']['inner_id']#line:68
                    O0OOO000OO0O0O000 =O00OO0O000OOO00OO ['data']['assets']['gold']#line:69
                    OOO0O000OOOO0000O =O00OO0O000OOO00OO ['data']['level']#line:70
                    print (f'【账号信息】:昵称:{OOO0O0OOO0O0O000O[:5]}丨ID:{O00O0OOO000OOO000}丨等级:{OOO0O000OOOO0000O}丨金种子:{str(O0OOO000OO0O0O000).split(".")[0]}')#line:71
                if O00OO0O000OOO00OO ['status']==401 :#line:72
                    print (O00OO0O000OOO00OO ['message'])#line:73
                    O0000000000OOOOOO .msg .append ('有账号失效了')#line:74
                    return False #line:75
                if O00OO0O000OOO00OO ['status']==500 :#line:76
                    return False #line:77
            return True #line:78
        except Exception as OO00000O0OOOO00OO :#line:79
            print (OO00000O0OOOO00OO )#line:80
    def sealing (O0O000O0O0OO0000O ):#line:83
        try :#line:84
            OO0O00O00OOO00000 =f'__{timi_new()}'#line:85
            OOO00O00OO0OOOOOO ={'authorization':O0O000O0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OOO00000 ),'signstring':OO0O00O00OOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO00O00OO0OOOOOO )#line:96
            requests .request ('get',f'{host}/packsack/list',headers =OOO00O00OO0OOOOOO )#line:97
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO00O00OO0OOOOOO )#line:98
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO00O00OO0OOOOOO )#line:99
            requests .request ('get',f'{host}/user',headers =OOO00O00OO0OOOOOO )#line:100
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO00O00OO0OOOOOO )#line:101
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO00O00OO0OOOOOO )#line:102
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO00O00OO0OOOOOO )#line:103
            requests .request ('get',f'{host}/game/getAllData',headers =OOO00O00OO0OOOOOO )#line:104
            requests .request ('get',f'{host}/assets',headers =OOO00O00OO0OOOOOO )#line:105
        except Exception as O0OO0O00OOO000O0O :#line:106
            print (O0OO0O00OOO000O0O )#line:107
    def market_sale_buy (O0O00O0O000OO0000 ,_O00OOOOO00O0OOOOO ,OO00OOO00O0000OOO ):#line:115
        try :#line:116
            O0O0OOOOOO0O0O0O0 =timi_new ()#line:117
            O0O0OO0000OO000O0 =f'_askToBuyId={_O00OOOOO00O0OOOOO}&quantity={OO00OOO00O0000OOO}_{O0O0OOOOOO0O0O0O0}'#line:118
            OOO000OOO0O00OO0O ={'source':'scsc','authorization':O0O00O0O000OO0000 .token ,'timestamp':str (O0O0OOOOOO0O0O0O0 ),'sign':sign (O0O0OO0000OO000O0 ),'signstring':O0O0OO0000OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:129
            OOO0O00OOO000OO00 ={"askToBuyId":_O00OOOOO00O0OOOOO ,"quantity":OO00OOO00O0000OOO }#line:130
            OO000OOO0OOOO0000 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOO000OOO0O00OO0O ,data =OOO0O00OOO000OO00 ).json ()#line:131
            if 'status'in OO000OOO0OOOO0000 :#line:133
                if OO000OOO0OOOO0000 ['status']==200 :#line:134
                    print ('【出售求购】:出售成功')#line:135
                elif OO000OOO0OOOO0000 ['message']=='请求超时':#line:136
                    O0O00O0O000OO0000 .market_sale_buy (_O00OOOOO00O0OOOOO ,OO00OOO00O0000OOO )#line:137
                else :#line:138
                    print (OO000OOO0OOOO0000 )#line:139
                    if OO000OOO0OOOO0000 ['message']=='库存不足':#line:140
                        O0O00O0O000OO0000 .market_sale_buy (_O00OOOOO00O0OOOOO ,OO00OOO00O0000OOO -1 )#line:141
                    if OO000OOO0OOOO0000 ['message']=='更新求购单失败':#line:142
                        exit (2 )#line:143
                    if OO000OOO0OOOO0000 ['message']=='购买数量不足':#line:144
                        exit (3 )#line:145
                    if OO000OOO0OOOO0000 ['message']=='商品不存在或取消求购':#line:146
                        exit (4 )#line:147
                    if OO000OOO0OOOO0000 ['message']=='购买数量不足':#line:148
                        exit (5 )#line:149
        except Exception as O0000000000O0000O :#line:151
            print (O0000000000O0000O )#line:152
    def game_map (OOO000O0OO00O0OO0 ,_OOO0OO0O0O0OO0O0O ):#line:155
        try :#line:156
            O0O000OOO0OO0000O =f'__{timi_new()}'#line:157
            O0OO00O00000OOO00 ={'source':'scsc','authorization':OOO000O0OO00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO0OO0000O ),'signstring':O0O000OOO0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
            OO0O00000OOOO0O0O =requests .request ('get',f'{host}/game/map',headers =O0OO00O00000OOO00 ).json ()#line:169
            if 'status'in OO0O00000OOOO0O0O :#line:171
                if OO0O00000OOOO0O0O ['status']==200 :#line:172
                    for O0O0O000O000O00OO in OO0O00000OOOO0O0O ['data']['list'][0 ]['crops']:#line:173
                        OOO000OO000OO0OOO =O0O0O000O000O00OO ['level']#line:175
                        if OOO000OO000OO0OOO ==41 :#line:176
                            O000O0OO00OOO0O0O =O0O0O000O000O00OO ['crop_name']#line:177
                            OO0OO0O0OO0OO00O0 =O0O0O000O000O00OO ['count']#line:178
                            if OO0OO0O0OO0OO00O0 >0 :#line:179
                                print (f'【农业资产】:{O000O0OO00OOO0O0O}丨数量:{OO0OO0O0OO0OO00O0}')#line:180
                                OOO000O0OO00O0OO0 .market_sale_buy (_OOO0OO0O0O0OO0O0O ,OO0OO0O0OO0OO00O0 )#line:181
        except Exception as OOOOO0O0OOO0OO0OO :#line:182
            print (OOOOO0O0OOO0OO0OO )#line:183
    def query_to_sell (OOOOO0OOO00OOOO0O ):#line:187
        try :#line:188
            OOO0OO00O0O0O000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:189
            OOO0O000OOOO00O0O ={'source':'scsc','authorization':OOOOO0OOO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0O0O000O ),'signstring':OOO0OO00O0O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
            OO00O00OO0OO0O0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0O000OOOO00O0O ).json ()#line:201
            if 'status'in OO00O00OO0OO0O0O0 :#line:203
                if OO00O00OO0OO0O0O0 ['status']==200 :#line:204
                    for OOO0OO00O0O0OOO00 in OO00O00OO0OO0O0O0 ['data']['rows']:#line:205
                        O0OO000000O0OO00O =OOO0OO00O0O0OOO00 ['materialKey']#line:206
                        OO0000O00OOOOOO0O =OOO0OO00O0O0OOO00 ['quantity']#line:207
                        O000O0OOO0O00OO00 =OOO0OO00O0O0OOO00 ['price']#line:208
                        OOOOO000O0OO000OO =OOO0OO00O0O0OOO00 ['saleState']#line:209
                        if OOOOO000O0OO000OO ==0 :#line:210
                            print (f'【出售订单】:名称:{O0OO000000O0OO00O}丨数量:{OO0000O00OOOOOO0O}丨价格:{O000O0OOO0O00OO00}')#line:211
                            OOO0O0OOO000OO0O0 =OOO0OO00O0O0OOO00 ['id']#line:212
                            OOOOO0OOO00OOOO0O .cacel_sale (OOO0O0OOO000OO0O0 )#line:213
        except Exception as O0O00O000OO0000OO :#line:219
            print (O0O00O000OO0000OO )#line:220
    def cacel_sale (O000O00O000O00O00 ,O0O0OO0O000O0OOO0 ):#line:224
        try :#line:225
            O000OO0O00OOO0OOO =f'_saleId={O0O0OO0O000O0OOO0}_{timi_new()}'#line:226
            O00OOO00O0OO00OOO ={'source':'scsc','authorization':O000O00O000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O00OOO0OOO ),'signstring':O000OO0O00OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:237
            O00OO0OOOOO0OO0O0 ={"saleId":O0O0OO0O000O0OOO0 }#line:240
            O0O0000OO0OOO0000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OOO00O0OO00OOO ,data =O00OO0OOOOO0OO0O0 ).json ()#line:241
            if 'status'in O0O0000OO0OOO0000 :#line:243
                if O0O0000OO0OOO0000 ['status']==200 :#line:244
                    print (f'【下架出售】:{O0O0000OO0OOO0000["data"]}')#line:245
        except Exception as O0OOOO0O0O00O0OO0 :#line:246
            print (O0OOOO0O0O00O0OO0 )#line:247
    def market_buy (O00O0OOO00OOOO0OO ,OO00O0O00O00O0000 ):#line:251
        try :#line:252
            O0OO0000OO0OOOO00 ='page=1&pageSize=20&queryField=__1679487573414'#line:253
            O0O0O00O0OOO000O0 ={'authorization':OO00O0O00O00O0000 ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':O0OO0000OO0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:263
            O00O0O0OOOO0O000O =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O0O00O0OOO000O0 ).json ()#line:264
            if 'status'in O00O0O0OOOO0O000O :#line:266
                if O00O0O0OOOO0O000O ['status']==200 :#line:267
                    for OOOOO0O000O00OOOO in O00O0O0OOOO0O000O ['data']['rows']:#line:268
                        O0OO00O0O000OO0O0 =OOOOO0O000O00OOOO ['id']#line:270
                        OOOOOO0OO0O00O0OO =OOOOO0O000O00OOOO ['price']#line:271
                        O0O00O00OO0000000 =OOOOO0O000O00OOOO ['remainQuantity']#line:272
                        print (f'求购价格:{OOOOOO0OO0O00O0OO}丨求购数量:{O0O00O00OO0000000}丨任务ID:{O0OO00O0O000OO0O0}')#line:273
                        if float (OOOOOO0OO0O00O0OO )<float (pica_aa ):#line:274
                            exit (1 )#line:275
                        return O0OO00O0O000OO0O0 #line:276
        except Exception as OOOOOOOOO0OOO0000 :#line:277
            print (OOOOOOOOO0OOO0000 )#line:278
def start ():#line:283
    try :#line:284
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:285
        O000OO0O00OO00O00 ()#line:286
        OO0000000000O00OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:287
        _OOO0OO0000O00OO0O =CityEarth .market_buy (OO0000000000O00OO ,OO0000000000O00OO [0 ]['authorization'])#line:288
        print (f"==========共找到{len(OO0000000000O00OO)}个账号==========")#line:289
        for O0O00O00O00OO00OO in OO0000000000O00OO :#line:290
            OO000OOO0O0O0OOO0 =[]#line:291
            print (f"------------正在执行第{OO0000000000O00OO.index(O0O00O00O00OO00OO) + 1}个账号------------")#line:292
            O000O0OO00OOOO0OO =CityEarth (O0O00O00O00OO00OO ,OO000OOO0O0O0OOO0 )#line:293
            if O000O0OO00OOOO0OO .base_info ():#line:295
                def OOOO0OO0O000O000O ():#line:296
                    O000O0OO00OOOO0OO .sealing ()#line:298
                    O000O0OO00OOOO0OO .query_to_sell ()#line:300
                O0OOOOOO00O0OOO0O =threading .Thread (target =OOOO0OO0O000O000O )#line:301
                O0OOOOOO00O0OOO0O .start ()#line:302
                O000O0OO00OOOO0OO .game_map (_OOO0OO0000O00OO0O )#line:305
    except Exception as OOOOOO00OOO0OOOOO :#line:307
        print (OOOOOO00OOO0OOOOO )#line:308
if __name__ =='__main__':#line:311
    start ()#line:312
