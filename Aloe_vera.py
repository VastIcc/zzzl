# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import hashlib
    import requests
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
price = '50'           # 设置芦荟价格
##################################配置区##################################

##################################下面不要动##################################
application ='ce_token'#line:1
token =''#line:2
version ='3.1.41954131'#line:3
git ='https://gitee.com'#line:4
host ='http://scsc.sc19319.com'#line:5
golden_seed =0 #line:6
msg_list =[]#line:7
def start ():#line:9
    try :#line:10
        OO0OOOOOOOO0OO0OO =os_qinglong ()#line:11
        print (f"==========共找到{len(OO0OOOOOOOO0OO0OO)}个账号==========")#line:12
        for O000O00O00OO0O0O0 in OO0OOOOOOOO0OO0OO :#line:13
            OOO00O00O00OO0000 =[]#line:14
            print (f"------------正在执行第{OO0OOOOOOOO0OO0OO.index(O000O00O00OO0O0O0) + 1}个账号------------")#line:15
            O0O0000O00O0OOOO0 =CityEarth (O000O00O00OO0O0O0 ,OOO00O00O00OO0000 )#line:16
            if O0O0000O00O0OOOO0 .base_info ():#line:18
                O0O0000O00O0OOOO0 .sealing ()#line:20
                O0O0000O00O0OOOO0 .query_to_sell ()#line:22
                O0O0000O00O0OOOO0 .game_map ()#line:24
                O0O0000O00O0OOOO0 .market_sale ()#line:26
    except Exception as OO0O0OOO00O00OO00 :#line:28
        print (OO0O0OOO00O00OO00 )#line:29
def sign (O00OO0OO0O00O0O00 ):#line:35
    O0O0O000OO00O0O0O =hashlib .md5 (O00OO0OO0O00O0O00 .encode ()).hexdigest ()#line:36
    O00OO000O0OOOO00O ="scsc%^&*"+O0O0O000OO00O0O0O +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:37
    OOOO000O00OO0OO0O =hashlib .md5 (O00OO000O0OOOO00O .encode ()).hexdigest ()#line:38
    return OOOO000O00OO0OO0O #line:39
def timi_new ():#line:41
    return str (int (time .time ()*1000 ))#line:42
class CityEarth :#line:45
    def __init__ (O0O0OO0OO0O0O00O0 ,OOO000000O0OOOO00 ,OOO00OO0000O00O0O ):#line:47
        try :#line:48
            O0O0OO0OO0O0O00O0 .msg =OOO00OO0000O00O0O #line:49
            O0O0OO0OO0O0O00O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:50
            O0O0OO0OO0O0O00O0 .token =OOO000000O0OOOO00 .split ('&')[0 ]#line:51
        except :#line:52
            print ('变量格式错误')#line:53
    def base_info (OO0O0OO0000O0OOOO ):#line:56
        try :#line:57
            O0O00O0000O00OOOO =f'__{timi_new()}'#line:58
            OO0OOO0000OO0OOOO ={'source':'scsc','authorization':OO0O0OO0000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000O00OOOO ),'signstring':O0O00O0000O00OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:68
            O00000OOOO00O0O0O =requests .request ('get',f'{host}/user',headers =OO0OOO0000OO0OOOO ).json ()#line:69
            if 'status'in O00000OOOO00O0O0O :#line:71
                if O00000OOOO00O0O0O ['status']==200 :#line:72
                    O0OOO0OO000000OOO =O00000OOOO00O0O0O ['data']['nickname']#line:73
                    OOO00O00OO0000OO0 =O00000OOOO00O0O0O ['data']['inner_id']#line:74
                    O0OO00OOOOOO000OO =O00000OOOO00O0O0O ['data']['assets']['gold']#line:75
                    OO0OOO00O00O00OO0 =O00000OOOO00O0O0O ['data']['level']#line:76
                    print (f'【账号信息】:昵称:{O0OOO0OO000000OOO[:5]}丨ID:{OOO00O00OO0000OO0}丨等级:{OO0OOO00O00O00OO0}丨金种子:{str(O0OO00OOOOOO000OO).split(".")[0]}')#line:77
                if O00000OOOO00O0O0O ['status']==401 :#line:78
                    print (O00000OOOO00O0O0O ['message'])#line:79
                    OO0O0OO0000O0OOOO .msg .append ('有账号失效了')#line:80
                    return False #line:81
                if O00000OOOO00O0O0O ['status']==500 :#line:82
                    return False #line:83
            return True #line:84
        except Exception as O000000OOOO0OO0OO :#line:85
            print (O000000OOOO0OO0OO )#line:86
    def sealing (OO000O000OO0O0OOO ):#line:89
        try :#line:90
            OO0O0O0OOOO00O0O0 =f'__{timi_new()}'#line:91
            OO0OOO00OO00OOO00 ={'authorization':OO000O000OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOOO00O0O0 ),'signstring':OO0O0O0OOOO00O0O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:100
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOO00OO00OOO00 )#line:101
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOO00OO00OOO00 )#line:102
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOO00OO00OOO00 )#line:103
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOO00OO00OOO00 )#line:104
            requests .request ('get',f'{host}/user',headers =OO0OOO00OO00OOO00 )#line:105
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOO00OO00OOO00 )#line:106
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOO00OO00OOO00 )#line:107
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOO00OO00OOO00 )#line:108
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO00OO00OOO00 )#line:109
            requests .request ('get',f'{host}/assets',headers =OO0OOO00OO00OOO00 )#line:110
        except Exception as OOOO0OOO000O00OO0 :#line:111
            print (OOOO0OOO000O00OO0 )#line:112
    def market_sale (OOO0OOO0O0OOO0000 ):#line:115
        try :#line:116
            OOO0OOOOO00OO0O0O =timi_new ()#line:117
            OO0OOO00000O0O000 =f'type=crop__{OOO0OOOOO00OO0O0O}'#line:118
            O0O0OO00000OOO00O ={'source':'scsc','authorization':OOO0OOO0O0OOO0000 .token ,'timestamp':str (OOO0OOOOO00OO0O0O ),'sign':sign (OO0OOO00000O0O000 ),'signstring':OO0OOO00000O0O000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:128
            O0O0O00OO000OOO0O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0OO00000OOO00O ).json ()#line:129
            if 'status'in O0O0O00OO000OOO0O :#line:131
                if O0O0O00OO000OOO0O ['status']==200 :#line:132
                    if O0O0O00OO000OOO0O ['data']['rows']:#line:133
                        OO000OO00OOOO0O0O =O0O0O00OO000OOO0O ['data']['rows'][0 ]['packsackItemId']#line:134
                        O0OOOOOOO0000000O =O0O0O00OO000OOO0O ['data']['rows'][0 ]['quantity']#line:135
                        OO0O00000O0O0OOO0 =f'_packsackItemId={OO000OO00OOOO0O0O}&price={price}&quantity={O0OOOOOOO0000000O}_{OOO0OOOOO00OO0O0O}'#line:136
                        OO0O0OO00OO0OOO0O ={'source':'scsc','authorization':OOO0OOO0O0OOO0000 .token ,'timestamp':str (OOO0OOOOO00OO0O0O ),'sign':sign (OO0O00000O0O0OOO0 ),'signstring':OO0O00000O0O0OOO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:146
                        OOOOO000O0OO0O0O0 ={"packsackItemId":OO000OO00OOOO0O0O ,"price":price ,"quantity":str (O0OOOOOOO0000000O )}#line:151
                        O0OOOOOO00O0O0OO0 =requests .request ('post',f'{host}/market/sale',headers =OO0O0OO00OO0OOO0O ,data =OOOOO000O0OO0O0O0 ).json ()#line:152
                        if 'status'in O0OOOOOO00O0O0OO0 :#line:154
                            if O0OOOOOO00O0O0OO0 ['status']==200 :#line:155
                                print (f'【上架芦荟】:数量:{O0OOOOOOO0000000O}丨价格:{price}')#line:156
        except Exception as O0O0O0O0O00OO0OOO :#line:157
            print (O0O0O0O0O00OO0OOO )#line:158
    def game_map (O0O00OOO000OO0000 ):#line:161
        try :#line:162
            OOO0OO0OOOO00000O =f'__{timi_new()}'#line:163
            OOO00OOOOOOO000OO ={'source':'scsc','authorization':O0O00OOO000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOOO00000O ),'signstring':OOO0OO0OOOO00000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:173
            O0000OOO0O0O0O000 =requests .request ('get',f'{host}/game/map',headers =OOO00OOOOOOO000OO ).json ()#line:174
            if 'status'in O0000OOO0O0O0O000 :#line:176
                if O0000OOO0O0O0O000 ['status']==200 :#line:177
                    for O0O000OOO0OO00O00 in O0000OOO0O0O0O000 ['data']['list'][0 ]['crops']:#line:178
                        O0OO0O0O00O00OO00 =O0O000OOO0OO00O00 ['level']#line:180
                        if O0OO0O0O00O00OO00 ==41 :#line:181
                            OO0OO0O0OO0OOO0O0 =O0O000OOO0OO00O00 ['crop_name']#line:182
                            O0O00OOO0O0O000O0 =O0O000OOO0OO00O00 ['count']#line:183
                            if O0O00OOO0O0O000O0 >0 :#line:184
                                print (f'【农业资产】:{OO0OO0O0OO0OOO0O0}丨数量:{O0O00OOO0O0O000O0}')#line:185
        except Exception as O0000O00OO0O00OOO :#line:186
            print (O0000O00OO0O00OOO )#line:187
    def query_to_sell (OO000OO000OOOOO0O ):#line:191
        try :#line:192
            OO0OO00OO0O0OOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:193
            O0000O0000000O00O ={'source':'scsc','authorization':OO000OO000OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00OO0O0OOOOO ),'signstring':OO0OO00OO0O0OOOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:203
            O00O0O00O000O0O0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0000O0000000O00O ).json ()#line:204
            if 'status'in O00O0O00O000O0O0O :#line:206
                if O00O0O00O000O0O0O ['status']==200 :#line:207
                    for O0OOOO0O0OOOO0OO0 in O00O0O00O000O0O0O ['data']['rows']:#line:208
                        OO0O0OOO0O0OOOO00 =O0OOOO0O0OOOO0OO0 ['materialKey']#line:209
                        O0O0OO0O00O0OOOO0 =O0OOOO0O0OOOO0OO0 ['quantity']#line:210
                        OOOOO0O0O000O00O0 =O0OOOO0O0OOOO0OO0 ['price']#line:211
                        OOOOOOOOOOO000000 =O0OOOO0O0OOOO0OO0 ['saleState']#line:212
                        if OOOOOOOOOOO000000 ==0 :#line:213
                            print (f'【出售订单】:名称:{OO0O0OOO0O0OOOO00}丨数量:{O0O0OO0O00O0OOOO0}丨价格:{OOOOO0O0O000O00O0}')#line:214
                            O0OOO0OO0O00O000O =O0OOOO0O0OOOO0OO0 ['id']#line:215
                            OO000OO000OOOOO0O .cacel_sale (O0OOO0OO0O00O000O )#line:216
        except Exception as O000O00O00OOOO0OO :#line:222
            print (O000O00O00OOOO0OO )#line:223
    def cacel_sale (OOOO00OOOOOO00O00 ,O00OOOO0O0000O0OO ):#line:227
        try :#line:228
            OOO0000O0OOO00OOO =f'_saleId={O00OOOO0O0000O0OO}_{timi_new()}'#line:229
            OO00O000O0OO0OO00 ={'source':'scsc','authorization':OOOO00OOOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OOO00OOO ),'signstring':OOO0000O0OOO00OOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            O0O0OOO000O000OOO ={"saleId":O00OOOO0O0000O0OO }#line:242
            O0OOOOOO00O0O000O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO00O000O0OO0OO00 ,data =O0O0OOO000O000OOO ).json ()#line:243
            if 'status'in O0OOOOOO00O0O000O :#line:245
                if O0OOOOOO00O0O000O ['status']==200 :#line:246
                    print (f'【下架出售】:{O0OOOOOO00O0O000O["data"]}')#line:247
        except Exception as OO0000O0000O0OO0O :#line:248
            print (OO0000O0000O0OO0O )#line:249
def os_qinglong ():#line:252
    if application in os .environ :#line:253
        OO00OO0OOO00O0OOO =os .environ [application ].split ('\n')#line:254
        if len (OO00OO0OOO00O0OOO )>0 :#line:255
            return OO00OO0OOO00O0OOO #line:256
        else :#line:257
            print (f"{application}变量未启用")#line:258
            print ('脚本退出')#line:259
            sys .exit (1 )#line:260
    else :#line:261
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:262
        if token :#line:263
            OO00OO0OOO00O0OOO =token .split ('\n')#line:264
            if len (OO00OO0OOO00O0OOO )>0 :#line:265
                return OO00OO0OOO00O0OOO #line:266
        else :#line:267
            print (f"内置变量为空")#line:268
            print ('脚本结束')#line:269
            sys .exit (0 )#line:270
if __name__ =='__main__':#line:273
    start ()#line:274
