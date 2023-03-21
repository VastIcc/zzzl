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
def sign (OO000O0OO000OO0OO ):#line:52
    OO0O00OOO0O00OOOO =hashlib .md5 (OO000O0OO000OO0OO .encode ()).hexdigest ()#line:53
    OOOOOOO00000O00OO ="scsc%^&*"+OO0O00OOO0O00OOOO +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OOO0O0O0000O0000O =hashlib .md5 (OOOOOOO00000O00OO .encode ()).hexdigest ()#line:55
    return OOO0O0O0000O0000O #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0OO00O000000O0OO ,OOO0OO00O0OO00OOO ,O00O0O00OO0O0000O ):#line:64
        try :#line:65
            O0OO00O000000O0OO .msg =O00O0O00OO0O0000O #line:66
            O0OO00O000000O0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0OO00O000000O0OO .token =OOO0OO00O0OO00OOO ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (OOO000000O0OOO0O0 ):#line:73
        try :#line:74
            O0OOOOOO0000OO00O =f'__{timi_new()}'#line:75
            OOOO00000OOO00O00 ={'source':'scsc','authorization':OOO000000O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0000OO00O ),'signstring':O0OOOOOO0000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O00O000OO0O0O0OO0 =requests .request ('get',f'{host}/user',headers =OOOO00000OOO00O00 ).json ()#line:87
            if 'status'in O00O000OO0O0O0OO0 :#line:89
                if O00O000OO0O0O0OO0 ['status']==200 :#line:90
                    O00O0O00OO0OO0OOO =O00O000OO0O0O0OO0 ['data']['nickname']#line:91
                    O0OO0OOO00O0O000O =O00O000OO0O0O0OO0 ['data']['inner_id']#line:92
                    OOO00O0O0O00O0OO0 =O00O000OO0O0O0OO0 ['data']['assets']['gold']#line:93
                    O0O000O000O0OOO0O =O00O000OO0O0O0OO0 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{O00O0O00OO0OO0OOO[:5]}丨ID:{O0OO0OOO00O0O000O}丨等级:{O0O000O000O0OOO0O}丨金种子:{str(OOO00O0O0O00O0OO0).split(".")[0]}')#line:95
                if O00O000OO0O0O0OO0 ['status']==401 :#line:96
                    print (O00O000OO0O0O0OO0 ['message'])#line:97
                    OOO000000O0OOO0O0 .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O00O000OO0O0O0OO0 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as O00O00O00O00OOOO0 :#line:103
            print (O00O00O00O00OOOO0 )#line:104
    def sealing (OOOOO000OOOOO000O ):#line:107
        try :#line:108
            OOOOOOO0OOOOOO000 =f'__{timi_new()}'#line:109
            O0OOOO000O0O00OOO ={'authorization':OOOOO000OOOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOOOOO000 ),'signstring':OOOOOOO0OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOOO000O0O00OOO )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =O0OOOO000O0O00OOO )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOOO000O0O00OOO )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOOO000O0O00OOO )#line:123
            requests .request ('get',f'{host}/user',headers =O0OOOO000O0O00OOO )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOOO000O0O00OOO )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOOO000O0O00OOO )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOOO000O0O00OOO )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO000O0O00OOO )#line:128
            requests .request ('get',f'{host}/assets',headers =O0OOOO000O0O00OOO )#line:129
        except Exception as OO00OOOO0O0OOOOOO :#line:130
            print (OO00OOOO0O0OOOOOO )#line:131
    def market_sale_buy (O00O0OO0O0O00000O ,_O0OO000O0OOO0000O ,OOO00OOO0O0O0O00O ):#line:139
        try :#line:140
            OO0OO0OOOOO00000O =timi_new ()#line:141
            OOO0O0O00O00O0OO0 =f'_askToBuyId={_O0OO000O0OOO0000O}&quantity={OOO00OOO0O0O0O00O}_{OO0OO0OOOOO00000O}'#line:142
            O0OOOOOO000OO000O ={'source':'scsc','authorization':O00O0OO0O0O00000O .token ,'timestamp':str (OO0OO0OOOOO00000O ),'sign':sign (OOO0O0O00O00O0OO0 ),'signstring':OOO0O0O00O00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O0000O00O0O0000O0 ={"askToBuyId":_O0OO000O0OOO0000O ,"quantity":OOO00OOO0O0O0O00O }#line:154
            O00O00OOO00O000O0 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O0OOOOOO000OO000O ,data =O0000O00O0O0000O0 ).json ()#line:155
            if 'status'in O00O00OOO00O000O0 :#line:157
                if O00O00OOO00O000O0 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                else :#line:160
                    print (O00O00OOO00O000O0 )#line:161
                    exit ()#line:162
        except Exception as O0OOOO0O0OO0O0O0O :#line:163
            print (O0OOOO0O0OO0O0O0O )#line:164
    def game_map (OOO0O0OO00OO00OOO ,_O000OOOOO0OOOO0OO ):#line:167
        try :#line:168
            OOOO0O00000OOO0OO =f'__{timi_new()}'#line:169
            OO0O0OOOOOOO0OO0O ={'source':'scsc','authorization':OOO0O0OO00OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00000OOO0OO ),'signstring':OOOO0O00000OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:180
            O00O000OO000O0000 =requests .request ('get',f'{host}/game/map',headers =OO0O0OOOOOOO0OO0O ).json ()#line:181
            if 'status'in O00O000OO000O0000 :#line:183
                if O00O000OO000O0000 ['status']==200 :#line:184
                    for O00000OO000O00O0O in O00O000OO000O0000 ['data']['list'][0 ]['crops']:#line:185
                        OOOO0OO0OO000OO0O =O00000OO000O00O0O ['level']#line:187
                        if OOOO0OO0OO000OO0O ==41 :#line:188
                            OO0OO0OOOO00O0000 =O00000OO000O00O0O ['crop_name']#line:189
                            OO00O000OOOO0OOOO =O00000OO000O00O0O ['count']#line:190
                            if OO00O000OOOO0OOOO >0 :#line:191
                                print (f'【农业资产】:{OO0OO0OOOO00O0000}丨数量:{OO00O000OOOO0OOOO}')#line:192
                                OOO0O0OO00OO00OOO .market_sale_buy (_O000OOOOO0OOOO0OO ,OO00O000OOOO0OOOO )#line:193
        except Exception as OOO0OOO00O0OOOOOO :#line:194
            print (OOO0OOO00O0OOOOOO )#line:195
    def query_to_sell (O00000OO0O0OO00OO ):#line:199
        try :#line:200
            O0O00OO00O0000O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:201
            OOO0OOOO0OOOO000O ={'source':'scsc','authorization':O00000OO0O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00O0000O0O ),'signstring':O0O00OO00O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O00O0O0OO000000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0OOOO0OOOO000O ).json ()#line:213
            if 'status'in O00O0O0OO000000O0 :#line:215
                if O00O0O0OO000000O0 ['status']==200 :#line:216
                    for O00O0000OOO000O00 in O00O0O0OO000000O0 ['data']['rows']:#line:217
                        O00OO0O0O00000OOO =O00O0000OOO000O00 ['materialKey']#line:218
                        OO00O00000OO0OO00 =O00O0000OOO000O00 ['quantity']#line:219
                        O0OO0O0OO0OOOOOO0 =O00O0000OOO000O00 ['price']#line:220
                        O0OOOOOO000000OO0 =O00O0000OOO000O00 ['saleState']#line:221
                        if O0OOOOOO000000OO0 ==0 :#line:222
                            print (f'【出售订单】:名称:{O00OO0O0O00000OOO}丨数量:{OO00O00000OO0OO00}丨价格:{O0OO0O0OO0OOOOOO0}')#line:223
                            O0OO0O0OOOO000000 =O00O0000OOO000O00 ['id']#line:224
                            O00000OO0O0OO00OO .cacel_sale (O0OO0O0OOOO000000 )#line:225
        except Exception as O0OO00O00OO00OOOO :#line:231
            print (O0OO00O00OO00OOOO )#line:232
    def cacel_sale (O0OO0O0000OO0O0O0 ,OO0OO00000OO0000O ):#line:236
        try :#line:237
            OOO00OO000OOOO00O =f'_saleId={OO0OO00000OO0000O}_{timi_new()}'#line:238
            OO000O0OOO00000OO ={'source':'scsc','authorization':O0OO0O0000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO000OOOO00O ),'signstring':OOO00OO000OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            OOOO00O00O0OO00OO ={"saleId":OO0OO00000OO0000O }#line:252
            O0000OOO0000O0O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO000O0OOO00000OO ,data =OOOO00O00O0OO00OO ).json ()#line:253
            if 'status'in O0000OOO0000O0O00 :#line:255
                if O0000OOO0000O0O00 ['status']==200 :#line:256
                    print (f'【下架出售】:{O0000OOO0000O0O00["data"]}')#line:257
        except Exception as O000000OO0O00O0OO :#line:258
            print (O000000OO0O00O0OO )#line:259
def start ():#line:261
    try :#line:262
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:263
        O000OO0O00OO00O00 ()#line:264
        OO0O0O0O000OOOOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:265
        print (f"==========共找到{len(OO0O0O0O000OOOOO0)}个账号==========")#line:266
        for OOO00O00O00O00000 in OO0O0O0O000OOOOO0 :#line:267
            OOOOOO0OOO0O00OOO =[]#line:268
            print (f"------------正在执行第{OO0O0O0O000OOOOO0.index(OOO00O00O00O00000) + 1}个账号------------")#line:269
            OOO0OO00O0OO0OO0O =CityEarth (OOO00O00O00O00000 ,OOOOOO0OOO0O00OOO )#line:270
            if OOO0OO00O0OO0OO0O .base_info ():#line:272
                OOO0OO00O0OO0OO0O .sealing ()#line:274
                OOO0OO00O0OO0OO0O .query_to_sell ()#line:276
                _OOO000OO0OOOOO00O =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:279
                OOO0OO00O0OO0OO0O .game_map (_OOO000OO0OOOOO00O )#line:280
    except Exception as O0OOOOOO0O0OOOOOO :#line:282
        print (O0OOOOOO0O0OOOOOO )#line:283
if __name__ =='__main__':#line:286
    start ()#line:287
