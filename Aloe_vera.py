# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
    import random
    import json
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: * * * 12 *
@ new Env('生城世朝手动上架芦荟')
@ 脚本会取消上架的农作物再出售芦荟
@ 价格设置错了重新运行一次脚本    一定看好价格再运行脚本
"""
##################################配置区##################################
price = '50'                    # 设置芦荟价格
price_floating = 99     # 设置芦荟价格浮动价格 上面价格加随机加-0.001到-0.099之间
##################################配置区##################################

##################################下面不要动##################################
application ='ce_token'#line:1
token =''''''#line:2
version ='3.1.419541311'#line:3
git ='https://gitee.com'#line:4
host ='http://scsc.sc19319.com'#line:5
golden_seed =0 #line:6
msg_list =[]#line:7
def start ():#line:9
    try :#line:10
        O00OO000OO0OOOOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:11
        print (f"==========共找到{len(O00OO000OO0OOOOO0)}个账号==========")#line:12
        for OO0OOOO00O0O0OOOO in O00OO000OO0OOOOO0 :#line:13
            OOO0O000OO000O0O0 =[]#line:14
            print (f"------------正在执行第{O00OO000OO0OOOOO0.index(OO0OOOO00O0O0OOOO) + 1}个账号------------")#line:15
            OO000O0OOO0O00O0O =CityEarth (OO0OOOO00O0O0OOOO ,OOO0O000OO000O0O0 )#line:16
            if OO000O0OOO0O00O0O .base_info ():#line:18
                OO000O0OOO0O00O0O .sealing ()#line:20
                OO000O0OOO0O00O0O .query_to_sell ()#line:22
                OO000O0OOO0O00O0O .game_map ()#line:24
                OO000O0OOO0O00O0O .market_sale ()#line:26
    except Exception as OO0OO0O0O0OO0OO00 :#line:28
        print (OO0OO0O0O0OO0OO00 )#line:29
def sign (O0O0O00OOO00000O0 ):#line:35
    OO0O000000OOOOO00 =hashlib .md5 (O0O0O00OOO00000O0 .encode ()).hexdigest ()#line:36
    O0O0OO000O00000OO ="scsc%^&*"+OO0O000000OOOOO00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:37
    OOO0OOOOO00OO0O00 =hashlib .md5 (O0O0OO000O00000OO .encode ()).hexdigest ()#line:38
    return OOO0OOOOO00OO0O00 #line:39
def timi_new ():#line:41
    return str (int (time .time ()*1000 ))#line:42
class CityEarth :#line:45
    def __init__ (OO000O0O0O0OOOO0O ,OOOOOO0000000000O ,OO000O0000OO00OOO ):#line:47
        try :#line:48
            OO000O0O0O0OOOO0O .msg =OO000O0000OO00OOO #line:49
            OO000O0O0O0OOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            OO000O0O0O0OOOO0O .token =OOOOOO0000000000O ['authorization']#line:51
        except :#line:52
            print ('变量格式错误')#line:53
    def base_info (OO0OO0OOOOOO00OOO ):#line:56
        try :#line:57
            OO00O0O0OO00O0000 =f'__{timi_new()}'#line:58
            O0OO000O0O0O0OOOO ={'source':'scsc','authorization':OO0OO0OOOOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO00O0000 ),'signstring':OO00O0O0OO00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OO000O0OOOOO00OOO =requests .request ('get',f'{host}/user',headers =O0OO000O0O0O0OOOO ).json ()#line:70
            if 'status'in OO000O0OOOOO00OOO :#line:72
                if OO000O0OOOOO00OOO ['status']==200 :#line:73
                    O0000O0O0O0000OOO =OO000O0OOOOO00OOO ['data']['nickname']#line:74
                    OO0OOO000O0000OOO =OO000O0OOOOO00OOO ['data']['inner_id']#line:75
                    OO0O0000O00O0OO00 =OO000O0OOOOO00OOO ['data']['assets']['gold']#line:76
                    O000O000O000O0O00 =OO000O0OOOOO00OOO ['data']['level']#line:77
                    print (f'【账号信息】:昵称:{O0000O0O0O0000OOO[:5]}丨ID:{OO0OOO000O0000OOO}丨等级:{O000O000O000O0O00}丨金种子:{str(OO0O0000O00O0OO00).split(".")[0]}')#line:78
                if OO000O0OOOOO00OOO ['status']==401 :#line:79
                    print (OO000O0OOOOO00OOO ['message'])#line:80
                    OO0OO0OOOOOO00OOO .msg .append ('有账号失效了')#line:81
                    return False #line:82
                if OO000O0OOOOO00OOO ['status']==500 :#line:83
                    return False #line:84
            return True #line:85
        except Exception as O0OOO0O00O0O0000O :#line:86
            print (O0OOO0O00O0O0000O )#line:87
    def sealing (OOO0O000O00OOO00O ):#line:90
        try :#line:91
            OO0OOOO00O0OO0OO0 =f'__{timi_new()}'#line:92
            O0OOO0000O00O0OOO ={'authorization':OOO0O000O00OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00O0OO0OO0 ),'signstring':OO0OOOO00O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:102
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0000O00O0OOO )#line:103
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0000O00O0OOO )#line:104
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0000O00O0OOO )#line:105
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0000O00O0OOO )#line:106
            requests .request ('get',f'{host}/user',headers =O0OOO0000O00O0OOO )#line:107
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0000O00O0OOO )#line:108
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0000O00O0OOO )#line:109
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0000O00O0OOO )#line:110
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0000O00O0OOO )#line:111
            requests .request ('get',f'{host}/assets',headers =O0OOO0000O00O0OOO )#line:112
        except Exception as O0OO00O0O0O0O0O00 :#line:113
            print (O0OO00O0O0O0O0O00 )#line:114
    def market_sale (OOO00OO0OO0000OOO ):#line:117
        try :#line:118
            OOOOOOOO0OOO000OO =timi_new ()#line:119
            OO000OO0O0OO0O00O =f'type=crop__{OOOOOOOO0OOO000OO}'#line:120
            O00O0O0O00O00O0O0 ={'source':'scsc','authorization':OOO00OO0OO0000OOO .token ,'timestamp':str (OOOOOOOO0OOO000OO ),'sign':sign (OO000OO0O0OO0O00O ),'signstring':OO000OO0O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:131
            O000OO00O00O00000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00O0O0O00O00O0O0 ).json ()#line:132
            if 'status'in O000OO00O00O00000 :#line:134
                if O000OO00O00O00000 ['status']==200 :#line:135
                    if O000OO00O00O00000 ['data']['rows']:#line:136
                        OOO0OOOOO0000OO00 =O000OO00O00O00000 ['data']['rows'][0 ]['packsackItemId']#line:137
                        O00O00O00O0O0O0O0 =O000OO00O00O00000 ['data']['rows'][0 ]['quantity']#line:138
                        O0OOO0O00000O000O =float (price )-float (random .randint (1 ,price_floating )*0.001 )#line:139
                        OO0000O00O0OO0OO0 =f'_packsackItemId={OOO0OOOOO0000OO00}&price={str(O0OOO0O00000O000O)[:8]}&quantity={O00O00O00O0O0O0O0}_{OOOOOOOO0OOO000OO}'#line:140
                        OOO0O0OOO000O0O00 ={'source':'scsc','authorization':OOO00OO0OO0000OOO .token ,'timestamp':str (OOOOOOOO0OOO000OO ),'sign':sign (OO0000O00O0OO0OO0 ),'signstring':OO0000O00O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:151
                        OO0O0OOOOOOOOO00O ={"packsackItemId":OOO0OOOOO0000OO00 ,"price":str (O0OOO0O00000O000O )[:8 ],"quantity":str (O00O00O00O0O0O0O0 )}#line:156
                        OOO0OOOO0O00OO00O =requests .request ('post',f'{host}/market/sale',headers =OOO0O0OOO000O0O00 ,data =OO0O0OOOOOOOOO00O ).json ()#line:157
                        if 'status'in OOO0OOOO0O00OO00O :#line:159
                            if OOO0OOOO0O00OO00O ['status']==200 :#line:160
                                print (f'【上架芦荟】:数量:{O00O00O00O0O0O0O0}丨价格:{str(O0OOO0O00000O000O)[:8]}')#line:161
        except Exception as O00O0OOO000OO000O :#line:162
            print (O00O0OOO000OO000O )#line:163
    def game_map (O0O0OOOO000O0O000 ):#line:166
        try :#line:167
            O000OOO000OO0O000 =f'__{timi_new()}'#line:168
            OOO0000O0000OO000 ={'source':'scsc','authorization':O0O0OOOO000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO000OO0O000 ),'signstring':O000OOO000OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:179
            O0O00OO00O000O00O =requests .request ('get',f'{host}/game/map',headers =OOO0000O0000OO000 ).json ()#line:180
            if 'status'in O0O00OO00O000O00O :#line:182
                if O0O00OO00O000O00O ['status']==200 :#line:183
                    for O0O0O00000OOOOOO0 in O0O00OO00O000O00O ['data']['list'][0 ]['crops']:#line:184
                        OO000O0O0OOO0O0O0 =O0O0O00000OOOOOO0 ['level']#line:186
                        if OO000O0O0OOO0O0O0 ==41 :#line:187
                            O00O0OO0O000OOO0O =O0O0O00000OOOOOO0 ['crop_name']#line:188
                            O00OOOOO0OO000O0O =O0O0O00000OOOOOO0 ['count']#line:189
                            if O00OOOOO0OO000O0O >0 :#line:190
                                print (f'【农业资产】:{O00O0OO0O000OOO0O}丨数量:{O00OOOOO0OO000O0O}')#line:191
        except Exception as OOO0OOO0O0O0OO00O :#line:192
            print (OOO0OOO0O0O0OO00O )#line:193
    def query_to_sell (OOOO00000000000O0 ):#line:197
        try :#line:198
            O000OO00OO00OOO0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:199
            O00OO0O0OO0O0OOOO ={'source':'scsc','authorization':OOOO00000000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OO00OOO0O ),'signstring':O000OO00OO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:210
            OOO0OOOOOOOO0O00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OO0O0OO0O0OOOO ).json ()#line:211
            if 'status'in OOO0OOOOOOOO0O00O :#line:213
                if OOO0OOOOOOOO0O00O ['status']==200 :#line:214
                    for O00O0O00OOOO0O0O0 in OOO0OOOOOOOO0O00O ['data']['rows']:#line:215
                        OOO000OO00OOOO0OO =O00O0O00OOOO0O0O0 ['materialKey']#line:216
                        OO00000OOO0OO0OO0 =O00O0O00OOOO0O0O0 ['quantity']#line:217
                        OOOOOOOOOO0000OOO =O00O0O00OOOO0O0O0 ['price']#line:218
                        O0O0OO00OOO0O0O00 =O00O0O00OOOO0O0O0 ['saleState']#line:219
                        if O0O0OO00OOO0O0O00 ==0 :#line:220
                            print (f'【出售订单】:名称:{OOO000OO00OOOO0OO}丨数量:{OO00000OOO0OO0OO0}丨价格:{OOOOOOOOOO0000OOO}')#line:221
                            O00OO0000000000OO =O00O0O00OOOO0O0O0 ['id']#line:222
                            OOOO00000000000O0 .cacel_sale (O00OO0000000000OO )#line:223
        except Exception as OO0O0OOOO00OO000O :#line:229
            print (OO0O0OOOO00OO000O )#line:230
    def cacel_sale (OO000O0OO0OO0OO00 ,O0OOO00OO00O00OOO ):#line:234
        try :#line:235
            OOO0O000O00O00O0O =f'_saleId={O0OOO00OO00O00OOO}_{timi_new()}'#line:236
            O000OO00000OOOO00 ={'source':'scsc','authorization':OO000O0OO0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00O00O0O ),'signstring':OOO0O000O00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:247
            OO00O00OO00O00O00 ={"saleId":O0OOO00OO00O00OOO }#line:250
            O00OOOO00O0000OO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O000OO00000OOOO00 ,data =OO00O00OO00O00O00 ).json ()#line:251
            if 'status'in O00OOOO00O0000OO0 :#line:253
                if O00OOOO00O0000OO0 ['status']==200 :#line:254
                    print (f'【下架出售】:{O00OOOO00O0000OO0["data"]}')#line:255
        except Exception as O000OO00000OO000O :#line:256
            print (O000OO00000OO000O )#line:257
def os_qinglong ():#line:260
    if application in os .environ :#line:261
        O0O000O0000O0O00O =os .environ [application ].split ('\n')#line:262
        if len (O0O000O0000O0O00O )>0 :#line:263
            return O0O000O0000O0O00O #line:264
        else :#line:265
            print (f"{application}变量未启用")#line:266
            print ('脚本退出')#line:267
            sys .exit (1 )#line:268
    else :#line:269
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:270
        if token :#line:271
            O0O000O0000O0O00O =token .split ('\n')#line:272
            if len (O0O000O0000O0O00O )>0 :#line:273
                return O0O000O0000O0O00O #line:274
        else :#line:275
            print (f"内置变量为空")#line:276
            print ('脚本结束')#line:277
            sys .exit (0 )#line:278
if __name__ =='__main__':#line:281
    start ()#line:282
