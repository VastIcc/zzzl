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
@ cron: * * * 12 *
@ new Env('生城世朝手动出售芦荟')
@ 脚本会取消上架的农作物再出售芦荟
"""#line:22
application ='ce_token'#line:26
version ='3.1.4195543511'#line:27
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
def sign (O0OOOOOOO00O0OO00 ):#line:53
    O0000OOO0OO00OO0O =hashlib .md5 (O0OOOOOOO00O0OO00 .encode ()).hexdigest ()#line:54
    OO0OO0O00OO0O00OO ="scsc%^&*"+O0000OOO0OO00OO0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:55
    O00O00O000OO0O00O =hashlib .md5 (OO0OO0O00OO0O00OO .encode ()).hexdigest ()#line:56
    return O00O00O000OO0O00O #line:57
def timi_new ():#line:59
    return str (int (time .time ()*1000 ))#line:60
class CityEarth :#line:63
    def __init__ (O00O00000OOOOOO0O ,O00OO0000O00OO00O ,O00OOO0OOOOOO0O0O ):#line:65
        try :#line:66
            O00O00000OOOOOO0O .msg =O00OOO0OOOOOO0O0O #line:67
            O00O00000OOOOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:68
            O00O00000OOOOOO0O .token =O00OO0000O00OO00O ['authorization']#line:69
        except :#line:70
            print ('变量格式错误')#line:71
    def base_info (OO0000OOOO0O0OOO0 ):#line:74
        try :#line:75
            OO0O0O00OO000OO00 =f'__{timi_new()}'#line:76
            OO0O0OO0OO0000O00 ={'source':'scsc','authorization':OO0000OOOO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00OO000OO00 ),'signstring':OO0O0O00OO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:87
            O0000OOO000OO0000 =requests .request ('get',f'{host}/user',headers =OO0O0OO0OO0000O00 ).json ()#line:88
            if 'status'in O0000OOO000OO0000 :#line:90
                if O0000OOO000OO0000 ['status']==200 :#line:91
                    O00O00OOO0O0O00OO =O0000OOO000OO0000 ['data']['nickname']#line:92
                    O0OO0O0OOOOOO0O00 =O0000OOO000OO0000 ['data']['inner_id']#line:93
                    OOOOOOO0O0OOOO00O =O0000OOO000OO0000 ['data']['assets']['gold']#line:94
                    O0OOOOO00OO00OOO0 =O0000OOO000OO0000 ['data']['level']#line:95
                    print (f'【账号信息】:昵称:{O00O00OOO0O0O00OO[:5]}丨ID:{O0OO0O0OOOOOO0O00}丨等级:{O0OOOOO00OO00OOO0}丨金种子:{str(OOOOOOO0O0OOOO00O).split(".")[0]}')#line:96
                if O0000OOO000OO0000 ['status']==401 :#line:97
                    print (O0000OOO000OO0000 ['message'])#line:98
                    OO0000OOOO0O0OOO0 .msg .append ('有账号失效了')#line:99
                    return False #line:100
                if O0000OOO000OO0000 ['status']==500 :#line:101
                    return False #line:102
            return True #line:103
        except Exception as OO00000OOO0O00O00 :#line:104
            print (OO00000OOO0O00O00 )#line:105
    def sealing (O000O000000OOOO0O ):#line:108
        try :#line:109
            OO0OOOOO00OOO0000 =f'__{timi_new()}'#line:110
            OOO00O0O0O00O000O ={'authorization':O000O000000OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00OOO0000 ),'signstring':OO0OOOOO00OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:120
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO00O0O0O00O000O )#line:121
            requests .request ('get',f'{host}/packsack/list',headers =OOO00O0O0O00O000O )#line:122
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO00O0O0O00O000O )#line:123
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO00O0O0O00O000O )#line:124
            requests .request ('get',f'{host}/user',headers =OOO00O0O0O00O000O )#line:125
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO00O0O0O00O000O )#line:126
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO00O0O0O00O000O )#line:127
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO00O0O0O00O000O )#line:128
            requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0O0O00O000O )#line:129
            requests .request ('get',f'{host}/assets',headers =OOO00O0O0O00O000O )#line:130
        except Exception as OOOO0OO00OO00OO00 :#line:131
            print (OOOO0OO00OO00OO00 )#line:132
    def market_sale_buy (O00O000OO0000OO0O ,_O0OOOOO00O0OO0O0O ,OOO0OO0O0OO0O00OO ):#line:140
        try :#line:141
            O000OO000O0O00OOO =timi_new ()#line:142
            O00OOOO0O000000OO =f'_askToBuyId={_O0OOOOO00O0OO0O0O}&quantity={OOO0OO0O0OO0O00OO}_{O000OO000O0O00OOO}'#line:143
            OOOOO00O0OOOOOOO0 ={'source':'scsc','authorization':O00O000OO0000OO0O .token ,'timestamp':str (O000OO000O0O00OOO ),'sign':sign (O00OOOO0O000000OO ),'signstring':O00OOOO0O000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:154
            O00O0OOOO00O00O0O ={"askToBuyId":_O0OOOOO00O0OO0O0O ,"quantity":OOO0OO0O0OO0O00OO }#line:155
            OO0OO0000OOO0O00O =requests .request ('post',f'{host}/market/sale-for-ask-to-buy',headers =OOOOO00O0OOOOOOO0 ,data =O00O0OOOO00O00O0O ).json ()#line:156
            if 'status'in OO0OO0000OOO0O00O :#line:158
                if OO0OO0000OOO0O00O ['status']==200 :#line:159
                    print ('【出售求购】:出售成功')#line:160
                else :#line:161
                    print (OO0OO0000OOO0O00O )#line:162
                    exit ()#line:163
        except Exception as OO0O000O0OO0OOOOO :#line:164
            print (OO0O000O0OO0OOOOO )#line:165
    def game_map (OOOO000O00OOOO0OO ,_OOOO000OOOO0OO00O ):#line:168
        try :#line:169
            O0OOOO000OO0OOO0O =f'__{timi_new()}'#line:170
            O00OO0OOO0O00O0O0 ={'source':'scsc','authorization':OOOO000O00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO000OO0OOO0O ),'signstring':O0OOOO000OO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:181
            OO0O0O0OO00OO0O0O =requests .request ('get',f'{host}/game/map',headers =O00OO0OOO0O00O0O0 ).json ()#line:182
            if 'status'in OO0O0O0OO00OO0O0O :#line:184
                if OO0O0O0OO00OO0O0O ['status']==200 :#line:185
                    for OO0OO00OOOOOO0000 in OO0O0O0OO00OO0O0O ['data']['list'][0 ]['crops']:#line:186
                        O0O0000O000OO00OO =OO0OO00OOOOOO0000 ['level']#line:188
                        if O0O0000O000OO00OO ==41 :#line:189
                            O0O0O00O000OO00O0 =OO0OO00OOOOOO0000 ['crop_name']#line:190
                            OOO0OO000O0OO00O0 =OO0OO00OOOOOO0000 ['count']#line:191
                            if OOO0OO000O0OO00O0 >0 :#line:192
                                print (f'【农业资产】:{O0O0O00O000OO00O0}丨数量:{OOO0OO000O0OO00O0}')#line:193
                                OOOO000O00OOOO0OO .market_sale_buy (_OOOO000OOOO0OO00O ,OOO0OO000O0OO00O0 )#line:194
        except Exception as OO0OO0OO0O000O0O0 :#line:195
            print (OO0OO0OO0O000O0O0 )#line:196
    def query_to_sell (O00O000O0O0000OOO ):#line:200
        try :#line:201
            OOOOO00O0OOO000O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:202
            OO000O00OO0OO00O0 ={'source':'scsc','authorization':O00O000O0O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OOO000O0 ),'signstring':OOOOO00O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:213
            OOO00OOO0OOOOOO0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO000O00OO0OO00O0 ).json ()#line:214
            if 'status'in OOO00OOO0OOOOOO0O :#line:216
                if OOO00OOO0OOOOOO0O ['status']==200 :#line:217
                    for O0OO0O00000OOO000 in OOO00OOO0OOOOOO0O ['data']['rows']:#line:218
                        O000000O0O000000O =O0OO0O00000OOO000 ['materialKey']#line:219
                        OOO0OOO0OOOO0000O =O0OO0O00000OOO000 ['quantity']#line:220
                        OOO0OOOO0OO0OOOOO =O0OO0O00000OOO000 ['price']#line:221
                        OOOOO000OOO0OO000 =O0OO0O00000OOO000 ['saleState']#line:222
                        if OOOOO000OOO0OO000 ==0 :#line:223
                            print (f'【出售订单】:名称:{O000000O0O000000O}丨数量:{OOO0OOO0OOOO0000O}丨价格:{OOO0OOOO0OO0OOOOO}')#line:224
                            O0OO0O0O0O000O0O0 =O0OO0O00000OOO000 ['id']#line:225
                            O00O000O0O0000OOO .cacel_sale (O0OO0O0O0O000O0O0 )#line:226
        except Exception as O0O0O0O00OO00O0OO :#line:232
            print (O0O0O0O00OO00O0OO )#line:233
    def cacel_sale (OOO0O00O0OOO0O000 ,OOOOO0OOOO00OOO00 ):#line:237
        try :#line:238
            O000OOOO0O00OOO0O =f'_saleId={OOOOO0OOOO00OOO00}_{timi_new()}'#line:239
            O0O0O0O0OOOOOOOOO ={'source':'scsc','authorization':OOO0O00O0OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0O00OOO0O ),'signstring':O000OOOO0O00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:250
            OOO0OO00OOO000OOO ={"saleId":OOOOO0OOOO00OOO00 }#line:253
            OOO0OOO0OOO0OO000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0O0O0OOOOOOOOO ,data =OOO0OO00OOO000OOO ).json ()#line:254
            if 'status'in OOO0OOO0OOO0OO000 :#line:256
                if OOO0OOO0OOO0OO000 ['status']==200 :#line:257
                    print (f'【下架出售】:{OOO0OOO0OOO0OO000["data"]}')#line:258
        except Exception as OO0000O00OO0O0O00 :#line:259
            print (OO0000O00OO0O0O00 )#line:260
def start ():#line:262
    try :#line:263
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:264
        O000OO0O00OO00O00 ()#line:265
        O0O0000000O00OO00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:266
        print (f"==========共找到{len(O0O0000000O00OO00)}个账号==========")#line:267
        for O000O0O0OO000000O in O0O0000000O00OO00 :#line:268
            O00OOOOO00OOO00OO =[]#line:269
            print (f"------------正在执行第{O0O0000000O00OO00.index(O000O0O0OO000000O) + 1}个账号------------")#line:270
            O0OOO0O0OO0OOOOO0 =CityEarth (O000O0O0OO000000O ,O00OOOOO00OOO00OO )#line:271
            if O0OOO0O0OO0OOOOO0 .base_info ():#line:273
                O0OOO0O0OO0OOOOO0 .sealing ()#line:275
                O0OOO0O0OO0OOOOO0 .query_to_sell ()#line:277
                _O00OO0O0O000O0O0O =requests .request ('get','https://gitee.com/vastzzzl/vastzzzl/raw/master/_askToBuyId').json ()['_askToBuyId']#line:280
                O0OOO0O0OO0OOOOO0 .game_map (_O00OO0O0O000O0O0O )#line:281
    except Exception as OO0O00O00O0O00O00 :#line:283
        print (OO0O00O00O0O00O00 )#line:284
if __name__ =='__main__':#line:287
    start ()#line:288
