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
pica_aa = '4.01'  # 价格低于就不出售给求购
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
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:22
def gitee_validation ():#line:24
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:25
def sign (O00OOO0OOOO0O00OO ):#line:28
    OOOO0OOOOOO00O0O0 =hashlib .md5 (O00OOO0OOOO0O00OO .encode ()).hexdigest ()#line:29
    O00OO00O0OOOOO00O ="scsc%^&*"+OOOO0OOOOOO00O0O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:30
    O0000000O00O0OO00 =hashlib .md5 (O00OO00O0OOOOO00O .encode ()).hexdigest ()#line:31
    return O0000000O00O0OO00 #line:32
def timi_new ():#line:34
    return str (int (time .time ()*1000 ))#line:35
class CityEarth :#line:38
    def __init__ (OOOOO00O0O00O0OOO ,O0O000OO0OOO00O00 ,OOOO0OO00O000O0OO ):#line:40
        try :#line:41
            OOOOO00O0O00O0OOO .msg =OOOO0OO00O000O0OO #line:42
            OOOOO00O0O00O0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:43
            OOOOO00O0O00O0OOO .token =O0O000OO0OOO00O00 ['authorization']#line:44
        except :#line:45
            print ('变量格式错误')#line:46
    def base_info (OOOOO0O0OO0OOO000 ):#line:49
        try :#line:50
            O0O0OO0OO00O0O00O =f'__{timi_new()}'#line:51
            OOO000000O00O0O00 ={'source':'scsc','authorization':OOOOO0O0OO0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO00O0O00O ),'signstring':O0O0OO0OO00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:62
            OO0OO00O00OO0O00O =requests .request ('get',f'{host}/user',headers =OOO000000O00O0O00 ).json ()#line:63
            if 'status'in OO0OO00O00OO0O00O :#line:65
                if OO0OO00O00OO0O00O ['status']==200 :#line:66
                    OOO0OOO0O00O0OOOO =OO0OO00O00OO0O00O ['data']['nickname']#line:67
                    O0O00O0OOOO0O0O0O =OO0OO00O00OO0O00O ['data']['inner_id']#line:68
                    O0O0OO000O0O00000 =OO0OO00O00OO0O00O ['data']['assets']['gold']#line:69
                    OO0OOO0000OO00O0O =OO0OO00O00OO0O00O ['data']['level']#line:70
                    print (f'【账号信息】:昵称:{OOO0OOO0O00O0OOOO[:5]}丨ID:{O0O00O0OOOO0O0O0O}丨等级:{OO0OOO0000OO00O0O}丨金种子:{str(O0O0OO000O0O00000).split(".")[0]}')#line:71
                if OO0OO00O00OO0O00O ['status']==401 :#line:72
                    print (OO0OO00O00OO0O00O ['message'])#line:73
                    OOOOO0O0OO0OOO000 .msg .append ('有账号失效了')#line:74
                    return False #line:75
                if OO0OO00O00OO0O00O ['status']==500 :#line:76
                    return False #line:77
            return True #line:78
        except Exception as OO0OO0OO0OO0O0000 :#line:79
            print (OO0OO0OO0OO0O0000 )#line:80
    def sealing (OO0O000O000000OO0 ):#line:83
        try :#line:84
            O0O00O00O0O0000O0 =f'__{timi_new()}'#line:85
            O00000000000OO00O ={'authorization':OO0O000O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O0O0000O0 ),'signstring':O0O00O00O0O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:95
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00000000000OO00O )#line:96
            requests .request ('get',f'{host}/packsack/list',headers =O00000000000OO00O )#line:97
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00000000000OO00O )#line:98
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00000000000OO00O )#line:99
            requests .request ('get',f'{host}/user',headers =O00000000000OO00O )#line:100
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00000000000OO00O )#line:101
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00000000000OO00O )#line:102
            requests .request ('post',f'{host}/announcement/announcement',headers =O00000000000OO00O )#line:103
            requests .request ('get',f'{host}/game/getAllData',headers =O00000000000OO00O )#line:104
            requests .request ('get',f'{host}/assets',headers =O00000000000OO00O )#line:105
        except Exception as O000O0000O0O00O0O :#line:106
            print (O000O0000O0O00O0O )#line:107
    def market_sale_buy (OOOOOOO0000000000 ,_O0OO000OOOO0O0OO0 ,O0O000O0O000OOO0O ):#line:115
        try :#line:116
            O0O0O0000O0O00O0O =timi_new ()#line:117
            O00O000OO00OOOO0O =f'_askToBuyId={_O0OO000OOOO0O0OO0}&quantity={O0O000O0O000OOO0O}_{O0O0O0000O0O00O0O}'#line:118
            OOOO0O0OO0OOO00O0 ={'source':'scsc','authorization':OOOOOOO0000000000 .token ,'timestamp':str (O0O0O0000O0O00O0O ),'sign':sign (O00O000OO00OOOO0O ),'signstring':O00O000OO00OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:129
            OO0OO0O0O0OO0OO0O ={"askToBuyId":_O0OO000OOOO0O0OO0 ,"quantity":O0O000O0O000OOO0O }#line:130
            O0OO0O0OO00OOOOOO =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOOO0O0OO0OOO00O0 ,data =OO0OO0O0O0OO0OO0O ).json ()#line:131
            if 'status'in O0OO0O0OO00OOOOOO :#line:133
                if O0OO0O0OO00OOOOOO ['status']==200 :#line:134
                    print ('【出售求购】:出售成功')#line:135
                elif O0OO0O0OO00OOOOOO ['message']=='请求超时':#line:136
                    OOOOOOO0000000000 .market_sale_buy (_O0OO000OOOO0O0OO0 ,O0O000O0O000OOO0O )#line:137
                else :#line:138
                    print (O0OO0O0OO00OOOOOO )#line:139
                    if O0OO0O0OO00OOOOOO ['message']=='库存不足':#line:140
                        OOOOOOO0000000000 .market_sale_buy (_O0OO000OOOO0O0OO0 ,O0O000O0O000OOO0O -1 )#line:141
                    if O0OO0O0OO00OOOOOO ['message']=='更新求购单失败':#line:142
                        exit (2 )#line:143
                    if O0OO0O0OO00OOOOOO ['message']=='购买数量不足':#line:144
                        exit (3 )#line:145
                    if O0OO0O0OO00OOOOOO ['message']=='商品不存在或取消求购':#line:146
                        exit (4 )#line:147
                    if O0OO0O0OO00OOOOOO ['message']=='购买数量不足':#line:148
                        exit (5 )#line:149
        except Exception as O0OO000OO000O0000 :#line:151
            print (O0OO000OO000O0000 )#line:152
    def game_map (O0000000000O000OO ,_OOOOOO00OO0000000 ):#line:155
        try :#line:156
            OO0O00O00O0O00O00 =f'__{timi_new()}'#line:157
            O00O000O000O0O000 ={'source':'scsc','authorization':O0000000000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00O0O00O00 ),'signstring':OO0O00O00O0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:168
            O0000000O0OO00OO0 =requests .request ('get',f'{host}/game/map',headers =O00O000O000O0O000 ).json ()#line:169
            if 'status'in O0000000O0OO00OO0 :#line:171
                if O0000000O0OO00OO0 ['status']==200 :#line:172
                    for OO0O0OOOO0OO00O00 in O0000000O0OO00OO0 ['data']['list'][0 ]['crops']:#line:173
                        O000OO00OO0000OO0 =OO0O0OOOO0OO00O00 ['level']#line:175
                        if O000OO00OO0000OO0 ==41 :#line:176
                            OO0OOOOO0OOO00O0O =OO0O0OOOO0OO00O00 ['crop_name']#line:177
                            OO0O00000O0O0OOO0 =OO0O0OOOO0OO00O00 ['count']#line:178
                            if OO0O00000O0O0OOO0 >0 :#line:179
                                print (f'【农业资产】:{OO0OOOOO0OOO00O0O}丨数量:{OO0O00000O0O0OOO0}')#line:180
                                O0000000000O000OO .market_sale_buy (_OOOOOO00OO0000000 ,OO0O00000O0O0OOO0 )#line:181
        except Exception as O00000O00000O00OO :#line:182
            print (O00000O00000O00OO )#line:183
    def query_to_sell (O0O00O0O0OOOO00O0 ):#line:187
        try :#line:188
            O0OOO00O0O0O0O00O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:189
            O0O0OO00000O0000O ={'source':'scsc','authorization':O0O00O0O0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0O0O00O ),'signstring':O0OOO00O0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:200
            OO00O0000O00O0000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O0OO00000O0000O ).json ()#line:201
            if 'status'in OO00O0000O00O0000 :#line:203
                if OO00O0000O00O0000 ['status']==200 :#line:204
                    for O00O00OOO0O0O0OO0 in OO00O0000O00O0000 ['data']['rows']:#line:205
                        O00O0000O00O000O0 =O00O00OOO0O0O0OO0 ['materialKey']#line:206
                        OOO00O0OOO0000O0O =O00O00OOO0O0O0OO0 ['quantity']#line:207
                        O0O0O0OO0O0OOO0O0 =O00O00OOO0O0O0OO0 ['price']#line:208
                        O0O0O0O00000O000O =O00O00OOO0O0O0OO0 ['saleState']#line:209
                        if O0O0O0O00000O000O ==0 :#line:210
                            print (f'【出售订单】:名称:{O00O0000O00O000O0}丨数量:{OOO00O0OOO0000O0O}丨价格:{O0O0O0OO0O0OOO0O0}')#line:211
                            O0O00O00OOO0000O0 =O00O00OOO0O0O0OO0 ['id']#line:212
                            O0O00O0O0OOOO00O0 .cacel_sale (O0O00O00OOO0000O0 )#line:213
        except Exception as OO00OO0O00OO00OO0 :#line:219
            print (OO00OO0O00OO00OO0 )#line:220
    def cacel_sale (O000O0OO0O0OO0OO0 ,O00OOOO00O0OOO00O ):#line:224
        try :#line:225
            OO000O00OOO00O00O =f'_saleId={O00OOOO00O0OOO00O}_{timi_new()}'#line:226
            O0O00O00O000OO0O0 ={'source':'scsc','authorization':O000O0OO0O0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OOO00O00O ),'signstring':OO000O00OOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:237
            OO0000000O0OO0OOO ={"saleId":O00OOOO00O0OOO00O }#line:240
            O000OOOO000O0000O =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O00O00O000OO0O0 ,data =OO0000000O0OO0OOO ).json ()#line:241
            if 'status'in O000OOOO000O0000O :#line:243
                if O000OOOO000O0000O ['status']==200 :#line:244
                    print (f'【下架出售】:{O000OOOO000O0000O["data"]}')#line:245
        except Exception as OOOOOO0O00OO0OOOO :#line:246
            print (OOOOOO0O00OO0OOOO )#line:247
    def market_buy (OOO0O0OOOO0O00O0O ,OOO00O0O00OOOOOOO ):#line:251
        try :#line:252
            OO00O000OO0O00OO0 ='page=1&pageSize=20&queryField=__1679487573414'#line:253
            O000OOOO00OO0O0OO ={'authorization':OOO00O0O00OOOOOOO ,'timestamp':'1679487573414','sign':'6b71dc53c645c9e115a97e8f1fe2586b','signstring':OO00O000OO0O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:263
            OOOOO00OOO00O00O0 =requests .request ('get','http://scsc.sc19319.com/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O000OOOO00OO0O0OO ).json ()#line:264
            if 'status'in OOOOO00OOO00O00O0 :#line:266
                if OOOOO00OOO00O00O0 ['status']==200 :#line:267
                    for OOOO0OOO00OOOO0O0 in OOOOO00OOO00O00O0 ['data']['rows']:#line:268
                        O0O00OOO0O0O0OO0O =OOOO0OOO00OOOO0O0 ['id']#line:270
                        O0O0O00OO0OO000O0 =OOOO0OOO00OOOO0O0 ['price']#line:271
                        OO0000OOOO0OO0OO0 =OOOO0OOO00OOOO0O0 ['remainQuantity']#line:272
                        print (f'求购价格:{O0O0O00OO0OO000O0}丨求购数量:{OO0000OOOO0OO0OO0}丨任务ID:{O0O00OOO0O0O0OO0O}')#line:273
                        if float (O0O0O00OO0OO000O0 )<float (pica_aa ):#line:274
                            exit (1 )#line:275
                        return O0O00OOO0O0O0OO0O #line:276
        except Exception as OO0O00OOOOOOOOOO0 :#line:277
            print (OO0O00OOOOOOOOOO0 )#line:278
def start ():#line:283
    try :#line:284
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:285
        O000OO0O00OO00O00 ()#line:286
        O0OO0OO0OOOOOO00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:287
        _O0OO0000O0O00O000 =CityEarth .market_buy (O0OO0OO0OOOOOO00O ,O0OO0OO0OOOOOO00O [0 ]['authorization'])#line:288
        print (f"==========共找到{len(O0OO0OO0OOOOOO00O)}个账号==========")#line:289
        for O000OOOOOO0000000 in O0OO0OO0OOOOOO00O :#line:290
            O0OOOOOOOO00O0O0O =[]#line:291
            print (f"------------正在执行第{O0OO0OO0OOOOOO00O.index(O000OOOOOO0000000) + 1}个账号------------")#line:292
            OOO00OO0OOO00OO0O =CityEarth (O000OOOOOO0000000 ,O0OOOOOOOO00O0O0O )#line:293
            if OOO00OO0OOO00OO0O .base_info ():#line:295
                def OOOO000O0OOOOO000 ():#line:296
                    OOO00OO0OOO00OO0O .sealing ()#line:298
                    OOO00OO0OOO00OO0O .query_to_sell ()#line:300
                O00O00OOO0O0O0O00 =threading .Thread (target =OOOO000O0OOOOO000 )#line:301
                O00O00OOO0O0O0O00 .start ()#line:302
                OOO00OO0OOO00OO0O .game_map (_O0OO0000O0O00O000 )#line:305
    except Exception as OO000OOO00O0O0O0O :#line:307
        print (OO000OOO00O0O0O0O )#line:308
if __name__ =='__main__':#line:311
    start ()#line:312
