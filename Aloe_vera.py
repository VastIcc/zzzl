# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
    import random
    from notify import send
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: * * * 12 *
@ new Env('生城世朝手动上架芦荟')
@ 脚本会取消上架的农作物再出售芦荟
@ 变量示范    export ce_token="557b8069-1234-4ae7-9e29-b7871f91541b&999999&999999"  用&符号分开数据
@ 价格设置错了重新运行一次脚本    一定看好价格再运行脚本
"""
##################################配置区##################################
price = '50'                    # 设置芦荟价格
price_floating = 99     # 设置芦荟价格浮动价格 上面价格加随机加-0.001到-0.099之间
##################################配置区##################################

##################################下面不要动##################################
application ='ce_token'#line:1
token =''''''#line:2
version ='3.1.41954131'#line:3
git ='https://gitee.com'#line:4
host ='http://scsc.sc19319.com'#line:5
golden_seed =0 #line:6
msg_list =[]#line:7
def start ():#line:9
    try :#line:10
        O000OO00O00OOO0O0 =os_qinglong ()#line:11
        print (f"==========共找到{len(O000OO00O00OOO0O0)}个账号==========")#line:12
        for O00O00O000OO00O00 in O000OO00O00OOO0O0 :#line:13
            OO000OOO00OO0O0O0 =[]#line:14
            print (f"------------正在执行第{O000OO00O00OOO0O0.index(O00O00O000OO00O00) + 1}个账号------------")#line:15
            OO0O000OOOO00O00O =CityEarth (O00O00O000OO00O00 ,OO000OOO00OO0O0O0 )#line:16
            if OO0O000OOOO00O00O .base_info ():#line:18
                OO0O000OOOO00O00O .sealing ()#line:21
                OO0O000OOOO00O00O .query_to_sell ()#line:23
                OO0O000OOOO00O00O .game_map ()#line:25
                OO0O000OOOO00O00O .market_sale ()#line:27
    except Exception as OO0O00O0OO0OO0000 :#line:29
        print (OO0O00O0OO0OO0000 )#line:30
def sign (O0O00O00OO00O0O0O ):#line:36
    O0O0OO0O00O0O0000 =hashlib .md5 (O0O00O00OO00O0O0O .encode ()).hexdigest ()#line:37
    O0O0OO00O000O00OO ="scsc%^&*"+O0O0OO0O00O0O0000 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:38
    O00OOOO00O0O0O0O0 =hashlib .md5 (O0O0OO00O000O00OO .encode ()).hexdigest ()#line:39
    return O00OOOO00O0O0O0O0 #line:40
def timi_new ():#line:42
    return str (int (time .time ()*1000 ))#line:43
class CityEarth :#line:46
    def __init__ (O000O00O0OO000OOO ,OOOO00OOOO000OOOO ,O0O00OO000O0O00O0 ):#line:48
        try :#line:49
            O000O00O0OO000OOO .msg =O0O00OO000O0O00O0 #line:50
            O000O00O0OO000OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:51
            O000O00O0OO000OOO .token =OOOO00OOOO000OOOO .split ('&')[0 ]#line:52
        except :#line:53
            print ('变量格式错误')#line:54
    def base_info (O0OO00000OOO0O0O0 ):#line:57
        try :#line:58
            O0O0OO00OO0000000 =f'__{timi_new()}'#line:59
            OO0000000O0O00O00 ={'source':'scsc','authorization':O0OO00000OOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OO0000000 ),'signstring':O0O0OO00OO0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:70
            O00000OOO000O00OO =requests .request ('get',f'{host}/user',headers =OO0000000O0O00O00 ).json ()#line:71
            if 'status'in O00000OOO000O00OO :#line:73
                if O00000OOO000O00OO ['status']==200 :#line:74
                    O00OO00OO0O000OOO =O00000OOO000O00OO ['data']['nickname']#line:75
                    OO00O0OO00OOO000O =O00000OOO000O00OO ['data']['inner_id']#line:76
                    O00OO000OOO0OO00O =O00000OOO000O00OO ['data']['assets']['gold']#line:77
                    OO0O000OO000000OO =O00000OOO000O00OO ['data']['level']#line:78
                    print (f'【账号信息】:昵称:{O00OO00OO0O000OOO[:5]}丨ID:{OO00O0OO00OOO000O}丨等级:{OO0O000OO000000OO}丨金种子:{str(O00OO000OOO0OO00O).split(".")[0]}')#line:79
                if O00000OOO000O00OO ['status']==401 :#line:80
                    print (O00000OOO000O00OO ['message'])#line:81
                    O0OO00000OOO0O0O0 .msg .append ('有账号失效了')#line:82
                    return False #line:83
                if O00000OOO000O00OO ['status']==500 :#line:84
                    return False #line:85
            return True #line:86
        except Exception as OOO00O0O0000O0000 :#line:87
            print (OOO00O0O0000O0000 )#line:88
    def sealing (OOO0O00OOOOO0OO0O ):#line:91
        try :#line:92
            O00OOOOO00OO000OO =f'__{timi_new()}'#line:93
            O0000OOOOOOOO0O0O ={'authorization':OOO0O00OOOOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO00OO000OO ),'signstring':O00OOOOO00OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:103
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000OOOOOOOO0O0O )#line:104
            requests .request ('get',f'{host}/packsack/list',headers =O0000OOOOOOOO0O0O )#line:105
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000OOOOOOOO0O0O )#line:106
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000OOOOOOOO0O0O )#line:107
            requests .request ('get',f'{host}/user',headers =O0000OOOOOOOO0O0O )#line:108
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000OOOOOOOO0O0O )#line:109
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000OOOOOOOO0O0O )#line:110
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000OOOOOOOO0O0O )#line:111
            requests .request ('get',f'{host}/game/getAllData',headers =O0000OOOOOOOO0O0O )#line:112
            requests .request ('get',f'{host}/assets',headers =O0000OOOOOOOO0O0O )#line:113
        except Exception as O0O0O00OO00O0OO0O :#line:114
            print (O0O0O00OO00O0OO0O )#line:115
    def market_sale (OOO0OOO00O0OO0O00 ):#line:118
        try :#line:119
            OOO00OO000O0OOOOO =timi_new ()#line:120
            O0O0OOO0000O0O00O =f'type=crop__{OOO00OO000O0OOOOO}'#line:121
            OOO0O0O0OO000OOOO ={'source':'scsc','authorization':OOO0OOO00O0OO0O00 .token ,'timestamp':str (OOO00OO000O0OOOOO ),'sign':sign (O0O0OOO0000O0O00O ),'signstring':O0O0OOO0000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:132
            O0OOO0O0O0O0O000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOO0O0O0OO000OOOO ).json ()#line:133
            if 'status'in O0OOO0O0O0O0O000O :#line:135
                if O0OOO0O0O0O0O000O ['status']==200 :#line:136
                    if O0OOO0O0O0O0O000O ['data']['rows']:#line:137
                        OO0O0OOOOOOO0OO0O =O0OOO0O0O0O0O000O ['data']['rows'][0 ]['packsackItemId']#line:138
                        OO00O000OO00O000O =O0OOO0O0O0O0O000O ['data']['rows'][0 ]['quantity']#line:139
                        OOO0000OOOOOOO00O =float (price )-float (random .randint (1 ,price_floating )*0.001 )#line:140
                        O0OOOOO0OO0O0OOO0 =f'_packsackItemId={OO0O0OOOOOOO0OO0O}&price={str(OOO0000OOOOOOO00O)[:8]}&quantity={OO00O000OO00O000O}_{OOO00OO000O0OOOOO}'#line:141
                        OO00O00O00O0000OO ={'source':'scsc','authorization':OOO0OOO00O0OO0O00 .token ,'timestamp':str (OOO00OO000O0OOOOO ),'sign':sign (O0OOOOO0OO0O0OOO0 ),'signstring':O0OOOOO0OO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:152
                        O00OOOOO000O0O0O0 ={"packsackItemId":OO0O0OOOOOOO0OO0O ,"price":str (OOO0000OOOOOOO00O )[:8 ],"quantity":str (OO00O000OO00O000O )}#line:157
                        O00O00OOO0OOOO00O =requests .request ('post',f'{host}/market/sale',headers =OO00O00O00O0000OO ,data =O00OOOOO000O0O0O0 ).json ()#line:158
                        if 'status'in O00O00OOO0OOOO00O :#line:160
                            if O00O00OOO0OOOO00O ['status']==200 :#line:161
                                print (f'【上架芦荟】:数量:{OO00O000OO00O000O}丨价格:{str(OOO0000OOOOOOO00O)[:8]}')#line:162
        except Exception as OO0O00O0O000O0O00 :#line:163
            print (OO0O00O0O000O0O00 )#line:164
    def game_map (OOO00OO0O0O0O0O0O ):#line:167
        try :#line:168
            OO0OOO00OO0OOOO0O =f'__{timi_new()}'#line:169
            O0O00OOO000O0OOO0 ={'source':'scsc','authorization':OOO00OO0O0O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00OO0OOOO0O ),'signstring':OO0OOO00OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:180
            OOO00OO0OO0O0O00O =requests .request ('get',f'{host}/game/map',headers =O0O00OOO000O0OOO0 ).json ()#line:181
            if 'status'in OOO00OO0OO0O0O00O :#line:183
                if OOO00OO0OO0O0O00O ['status']==200 :#line:184
                    for OOOOO0O0O0O0OO000 in OOO00OO0OO0O0O00O ['data']['list'][0 ]['crops']:#line:185
                        OO000OO00O0OOOO0O =OOOOO0O0O0O0OO000 ['level']#line:187
                        if OO000OO00O0OOOO0O ==41 :#line:188
                            O000OOO0O0OOO00O0 =OOOOO0O0O0O0OO000 ['crop_name']#line:189
                            OO00O0OO00O0OOOOO =OOOOO0O0O0O0OO000 ['count']#line:190
                            if OO00O0OO00O0OOOOO >0 :#line:191
                                print (f'【农业资产】:{O000OOO0O0OOO00O0}丨数量:{OO00O0OO00O0OOOOO}')#line:192
        except Exception as OOOO000000O0OO0O0 :#line:193
            print (OOOO000000O0OO0O0 )#line:194
    def query_to_sell (OO0OO000OOOO0000O ):#line:198
        try :#line:199
            O0OOOO0OOOO0O0O00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:200
            O00OOO00000O00000 ={'source':'scsc','authorization':OO0OO000OOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOOO0O0O00 ),'signstring':O0OOOO0OOOO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:211
            OOO0O000OO0O0OO00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OOO00000O00000 ).json ()#line:212
            if 'status'in OOO0O000OO0O0OO00 :#line:214
                if OOO0O000OO0O0OO00 ['status']==200 :#line:215
                    for O000OO00O000OO0O0 in OOO0O000OO0O0OO00 ['data']['rows']:#line:216
                        O00OOO00OOOOOO00O =O000OO00O000OO0O0 ['materialKey']#line:217
                        O0O0OOOOO0OO000O0 =O000OO00O000OO0O0 ['quantity']#line:218
                        O0O00O0O000OO0OOO =O000OO00O000OO0O0 ['price']#line:219
                        OO0O00O00O0OO00OO =O000OO00O000OO0O0 ['saleState']#line:220
                        if OO0O00O00O0OO00OO ==0 :#line:221
                            print (f'【出售订单】:名称:{O00OOO00OOOOOO00O}丨数量:{O0O0OOOOO0OO000O0}丨价格:{O0O00O0O000OO0OOO}')#line:222
                            O0O0000OOOOO0OO00 =O000OO00O000OO0O0 ['id']#line:223
                            OO0OO000OOOO0000O .cacel_sale (O0O0000OOOOO0OO00 )#line:224
        except Exception as O00OO0O000OOOOO0O :#line:230
            print (O00OO0O000OOOOO0O )#line:231
    def cacel_sale (OO0OOOO0OO00O0OO0 ,OOOO0O000OOO000OO ):#line:235
        try :#line:236
            OO00O0OOO00OO000O =f'_saleId={OOOO0O000OOO000OO}_{timi_new()}'#line:237
            O0OO000O000O0OO0O ={'source':'scsc','authorization':OO0OOOO0OO00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OOO00OO000O ),'signstring':OO00O0OOO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:248
            O00OOOO0O0O0O00O0 ={"saleId":OOOO0O000OOO000OO }#line:251
            O00000OOO00O000O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OO000O000O0OO0O ,data =O00OOOO0O0O0O00O0 ).json ()#line:252
            if 'status'in O00000OOO00O000O0 :#line:254
                if O00000OOO00O000O0 ['status']==200 :#line:255
                    print (f'【下架出售】:{O00000OOO00O000O0["data"]}')#line:256
        except Exception as OOOOO0OO0OOOO0OO0 :#line:257
            print (OOOOO0OO0OOOO0OO0 )#line:258
def os_qinglong ():#line:261
    if application in os .environ :#line:262
        O0OO000O0OOO0OO0O =os .environ [application ].split ('\n')#line:263
        if len (O0OO000O0OOO0OO0O )>0 :#line:264
            return O0OO000O0OOO0OO0O #line:265
        else :#line:266
            print (f"{application}变量未启用")#line:267
            print ('脚本退出')#line:268
            sys .exit (1 )#line:269
    else :#line:270
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:271
        if token :#line:272
            O0OO000O0OOO0OO0O =token .split ('\n')#line:273
            if len (O0OO000O0OOO0OO0O )>0 :#line:274
                return O0OO000O0OOO0OO0O #line:275
        else :#line:276
            print (f"内置变量为空")#line:277
            print ('脚本结束')#line:278
            sys .exit (0 )#line:279
if __name__ =='__main__':#line:282
    start ()#line:283
