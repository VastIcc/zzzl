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
version ='3.1.4195543511'#line:26
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
def sign (OOOO0O0O0O0OOOOOO ):#line:52
    O0O000O000O0O000O =hashlib .md5 (OOOO0O0O0O0OOOOOO .encode ()).hexdigest ()#line:53
    OO0O000O0O0OO00OO ="scsc%^&*"+O0O000O000O0O000O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:54
    OO0O0O00OO0O0O0O0 =hashlib .md5 (OO0O000O0O0OO00OO .encode ()).hexdigest ()#line:55
    return OO0O0O00OO0O0O0O0 #line:56
def timi_new ():#line:58
    return str (int (time .time ()*1000 ))#line:59
class CityEarth :#line:62
    def __init__ (O0OO0OO00OOO0O000 ,OOOO000O00O00O0OO ,OOO000O0O000O00OO ):#line:64
        try :#line:65
            O0OO0OO00OOO0O000 .msg =OOO000O0O000O00OO #line:66
            O0OO0OO00OOO0O000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:67
            O0OO0OO00OOO0O000 .token =OOOO000O00O00O0OO ['authorization']#line:68
        except :#line:69
            print ('变量格式错误')#line:70
    def base_info (O000O00OO0O0O0O0O ):#line:73
        try :#line:74
            OOOO0OOO00OO0OOOO =f'__{timi_new()}'#line:75
            OOOOO0O0O0O00OO00 ={'source':'scsc','authorization':O000O00OO0O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00OO0OOOO ),'signstring':OOOO0OOO00OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
            O00O0000000OO0000 =requests .request ('get',f'{host}/user',headers =OOOOO0O0O0O00OO00 ).json ()#line:87
            if 'status'in O00O0000000OO0000 :#line:89
                if O00O0000000OO0000 ['status']==200 :#line:90
                    OO00O000O0OOOO000 =O00O0000000OO0000 ['data']['nickname']#line:91
                    OOOO0OO0OOOO0O0OO =O00O0000000OO0000 ['data']['inner_id']#line:92
                    O00O0OOOO000O00OO =O00O0000000OO0000 ['data']['assets']['gold']#line:93
                    O0O00OO000OOO0O0O =O00O0000000OO0000 ['data']['level']#line:94
                    print (f'【账号信息】:昵称:{OO00O000O0OOOO000[:5]}丨ID:{OOOO0OO0OOOO0O0OO}丨等级:{O0O00OO000OOO0O0O}丨金种子:{str(O00O0OOOO000O00OO).split(".")[0]}')#line:95
                if O00O0000000OO0000 ['status']==401 :#line:96
                    print (O00O0000000OO0000 ['message'])#line:97
                    O000O00OO0O0O0O0O .msg .append ('有账号失效了')#line:98
                    return False #line:99
                if O00O0000000OO0000 ['status']==500 :#line:100
                    return False #line:101
            return True #line:102
        except Exception as OO000000O000000O0 :#line:103
            print (OO000000O000000O0 )#line:104
    def sealing (OOOO0OOO00OOO00O0 ):#line:107
        try :#line:108
            OOO0000O0OO0O0O00 =f'__{timi_new()}'#line:109
            OOO000O0000OO000O ={'authorization':OOOO0OOO00OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OO0O0O00 ),'signstring':OOO0000O0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:119
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000O0000OO000O )#line:120
            requests .request ('get',f'{host}/packsack/list',headers =OOO000O0000OO000O )#line:121
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000O0000OO000O )#line:122
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000O0000OO000O )#line:123
            requests .request ('get',f'{host}/user',headers =OOO000O0000OO000O )#line:124
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000O0000OO000O )#line:125
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000O0000OO000O )#line:126
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000O0000OO000O )#line:127
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0000OO000O )#line:128
            requests .request ('get',f'{host}/assets',headers =OOO000O0000OO000O )#line:129
        except Exception as O0OO00OOO0OOO0000 :#line:130
            print (O0OO00OOO0OOO0000 )#line:131
    def market_sale_buy (OO000O00OOOOOO00O ,_OO0O0O000OO0O0O0O ,O00000000OO0OO0O0 ):#line:139
        try :#line:140
            O000OO0000OO00000 =timi_new ()#line:141
            OO0OOO0OO00OO0OO0 =f'_askToBuyId={_OO0O0O000OO0O0O0O}&quantity={O00000000OO0OO0O0}_{O000OO0000OO00000}'#line:142
            O00O0OOO0O00O0O0O ={'source':'scsc','authorization':OO000O00OOOOOO00O .token ,'timestamp':str (O000OO0000OO00000 ),'sign':sign (OO0OOO0OO00OO0OO0 ),'signstring':OO0OOO0OO00OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:153
            O0OO000OO0OO00O0O ={"askToBuyId":_OO0O0O000OO0O0O0O ,"quantity":O00000000OO0OO0O0 }#line:154
            OO00OOO00O0O0OOO0 =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =O00O0OOO0O00O0O0O ,data =O0OO000OO0OO00O0O ).json ()#line:155
            if 'status'in OO00OOO00O0O0OOO0 :#line:157
                if OO00OOO00O0O0OOO0 ['status']==200 :#line:158
                    print ('【出售求购】:出售成功')#line:159
                else :#line:160
                    print (OO00OOO00O0O0OOO0 )#line:161
                    exit ()#line:162
        except Exception as O0O0000O0OOO000O0 :#line:163
            print (O0O0000O0OOO000O0 )#line:164
    def game_map (OOOOOO0000000O0O0 ,_OO000000000OOOOO0 ):#line:167
        try :#line:168
            OOOO000OO000OO0O0 =f'__{timi_new()}'#line:169
            OOOOOOOO000O0OO00 ={'source':'scsc','authorization':OOOOOO0000000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OO000OO0O0 ),'signstring':OOOO000OO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:180
            OO0OO0OOOO000O000 =requests .request ('get',f'{host}/game/map',headers =OOOOOOOO000O0OO00 ).json ()#line:181
            if 'status'in OO0OO0OOOO000O000 :#line:183
                if OO0OO0OOOO000O000 ['status']==200 :#line:184
                    for OO0000OO0O0OOO000 in OO0OO0OOOO000O000 ['data']['list'][0 ]['crops']:#line:185
                        O0OO0O00000OOOOO0 =OO0000OO0O0OOO000 ['level']#line:187
                        if O0OO0O00000OOOOO0 ==41 :#line:188
                            O0OOOOOOOO0OO00O0 =OO0000OO0O0OOO000 ['crop_name']#line:189
                            O0O0OOOO0O0OOO00O =OO0000OO0O0OOO000 ['count']#line:190
                            if O0O0OOOO0O0OOO00O >0 :#line:191
                                print (f'【农业资产】:{O0OOOOOOOO0OO00O0}丨数量:{O0O0OOOO0O0OOO00O}')#line:192
                                OOOOOO0000000O0O0 .market_sale_buy (_OO000000000OOOOO0 ,O0O0OOOO0O0OOO00O )#line:193
        except Exception as OOO0OOOO0OO000O00 :#line:194
            print (OOO0OOOO0OO000O00 )#line:195
    def query_to_sell (OO0OOOOOOOO00OO00 ):#line:199
        try :#line:200
            O00O00OO0OOOOO0O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:201
            O0O0O00O0000OOO0O ={'source':'scsc','authorization':OO0OOOOOOOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO0OOOOO0O0 ),'signstring':O00O00OO0OOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:212
            O00O0OO00O0O00000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O0O00O0000OOO0O ).json ()#line:213
            if 'status'in O00O0OO00O0O00000 :#line:215
                if O00O0OO00O0O00000 ['status']==200 :#line:216
                    for O0OO00OO0OO00O000 in O00O0OO00O0O00000 ['data']['rows']:#line:217
                        O0OO0OOO00OOO000O =O0OO00OO0OO00O000 ['materialKey']#line:218
                        OO000O0O0OO00000O =O0OO00OO0OO00O000 ['quantity']#line:219
                        O0OO00OO0000OO0O0 =O0OO00OO0OO00O000 ['price']#line:220
                        O00000OOOO00O0000 =O0OO00OO0OO00O000 ['saleState']#line:221
                        if O00000OOOO00O0000 ==0 :#line:222
                            print (f'【出售订单】:名称:{O0OO0OOO00OOO000O}丨数量:{OO000O0O0OO00000O}丨价格:{O0OO00OO0000OO0O0}')#line:223
                            O000O0O0O0O0OO0O0 =O0OO00OO0OO00O000 ['id']#line:224
                            OO0OOOOOOOO00OO00 .cacel_sale (O000O0O0O0O0OO0O0 )#line:225
        except Exception as OOOOO0O0OO00OOO0O :#line:231
            print (OOOOO0O0OO00OOO0O )#line:232
    def cacel_sale (OOO000OO0000000O0 ,OO0OO0OOO0OOOO0O0 ):#line:236
        try :#line:237
            OO000O00OOO0O0O00 =f'_saleId={OO0OO0OOO0OOOO0O0}_{timi_new()}'#line:238
            O0000OO00OOOO0OO0 ={'source':'scsc','authorization':OOO000OO0000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OOO0O0O00 ),'signstring':OO000O00OOO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            O00OO00000OO0OO00 ={"saleId":OO0OO0OOO0OOOO0O0 }#line:252
            O0OO00000O00O0000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0000OO00OOOO0OO0 ,data =O00OO00000OO0OO00 ).json ()#line:253
            if 'status'in O0OO00000O00O0000 :#line:255
                if O0OO00000O00O0000 ['status']==200 :#line:256
                    print (f'【下架出售】:{O0OO00000O00O0000["data"]}')#line:257
        except Exception as OO000000OOO000OOO :#line:258
            print (OO000000OOO000OOO )#line:259
def start ():#line:261
    try :#line:262
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:263
        O000OO0O00OO00O00 ()#line:264
        O00OO00000O0OOOOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:265
        print (f"==========共找到{len(O00OO00000O0OOOOO)}个账号==========")#line:266
        for OO0OO00OO000O0OO0 in O00OO00000O0OOOOO :#line:267
            OOOOOOOO00O0OO0OO =[]#line:268
            print (f"------------正在执行第{O00OO00000O0OOOOO.index(OO0OO00OO000O0OO0) + 1}个账号------------")#line:269
            OO0O00000O0O00000 =CityEarth (OO0OO00OO000O0OO0 ,OOOOOOOO00O0OO0OO )#line:270
            if OO0O00000O0O00000 .base_info ():#line:272
                OO0O00000O0O00000 .sealing ()#line:274
                OO0O00000O0O00000 .query_to_sell ()#line:276
                _OOO0OOO0O00O000O0 =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:279
                OO0O00000O0O00000 .game_map (_OOO0OOO0O00O000O0 )#line:280
    except Exception as OO0O00O00OOOOOOO0 :#line:282
        print (OO0O00O00OOOOOOO0 )#line:283
if __name__ =='__main__':#line:286
    start ()#line:287
