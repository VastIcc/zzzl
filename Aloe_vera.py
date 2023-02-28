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
@ cron: * * * 7 *
@ new Env('生城世朝手动上架芦荟')
@ 价格设置错了重新运行一次脚本    一定看好价格再运行脚本
"""

start_s = False             # 写 True 则开启出售芦荟
price = '50'                # 设置芦荟价格    支持小数点



application = 'ce_token'  # 变量名
token = ''              # 内置变量 非必要不要填

##################################下面不要动##################################
version ='3.1.41954131'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        if start_s :#line:9
            OOO0OOOO0OOOO0OOO =os_qinglong ()#line:10
            print (f"==========共找到{len(OOO0OOOO0OOOO0OOO)}个账号==========")#line:11
            for OO0O000O00OOO00O0 in OOO0OOOO0OOOO0OOO :#line:12
                O000O0O0OO000000O =[]#line:13
                print (f"------------正在执行第{OOO0OOOO0OOOO0OOO.index(OO0O000O00OOO00O0) + 1}个账号------------")#line:14
                O0000O0O000O00O0O =CityEarth (OO0O000O00OOO00O0 ,O000O0O0OO000000O )#line:15
                if O0000O0O000O00O0O .base_info ():#line:17
                    O0000O0O000O00O0O .sealing ()#line:19
                    O0000O0O000O00O0O .query_to_sell ()#line:21
                    O0000O0O000O00O0O .game_map ()#line:23
                    O0000O0O000O00O0O .market_sale ()#line:25
    except Exception as O0O0O0OO0OO0O00O0 :#line:27
        print (O0O0O0OO0OO0O00O0 )#line:28
def sign (O0O0OO0OOO00O0OO0 ):#line:31
    O0000OO0OOOO000O0 =hashlib .md5 (O0O0OO0OOO00O0OO0 .encode ()).hexdigest ()#line:32
    OOOOO0OOOOOO000O0 ="scsc%^&*"+O0000OO0OOOO000O0 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:33
    O0OO0OOO0OO00O0O0 =hashlib .md5 (OOOOO0OOOOOO000O0 .encode ()).hexdigest ()#line:34
    return O0OO0OOO0OO00O0O0 #line:35
def timi_new ():#line:37
    return str (int (time .time ()*1000 ))#line:38
class CityEarth :#line:41
    def __init__ (OO0O000OOOOO0O00O ,OO00O000OO0O00OOO ,O0OO0OO00O0OOO00O ):#line:43
        try :#line:44
            OO0O000OOOOO0O00O .msg =O0OO0OO00O0OOO00O #line:45
            OO0O000OOOOO0O00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:46
            OO0O000OOOOO0O00O .token =OO00O000OO0O00OOO .split ('&')[0 ]#line:47
        except :#line:48
            print ('变量格式错误')#line:49
    def base_info (O000OO00OOO0OOO0O ):#line:52
        try :#line:53
            O0OO0O00OOO0OOO0O =f'__{timi_new()}'#line:54
            OO0O000OOO00000O0 ={'source':'scsc','authorization':O000OO00OOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00OOO0OOO0O ),'signstring':O0OO0O00OOO0OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:64
            O00O0OO0OO0O0OOOO =requests .request ('get',f'{host}/user',headers =OO0O000OOO00000O0 ).json ()#line:65
            if 'status'in O00O0OO0OO0O0OOOO :#line:67
                if O00O0OO0OO0O0OOOO ['status']==200 :#line:68
                    OO0OOOOOOOO00O0OO =O00O0OO0OO0O0OOOO ['data']['nickname']#line:69
                    OOOOO0OOO00O0O00O =O00O0OO0OO0O0OOOO ['data']['inner_id']#line:70
                    O0O0OO00OO0OOOOOO =O00O0OO0OO0O0OOOO ['data']['assets']['gold']#line:71
                    OO0OO00O00O0OO0O0 =O00O0OO0OO0O0OOOO ['data']['level']#line:72
                    print (f'【账号信息】:昵称:{OO0OOOOOOOO00O0OO[:5]}丨ID:{OOOOO0OOO00O0O00O}丨等级:{OO0OO00O00O0OO0O0}丨金种子:{str(O0O0OO00OO0OOOOOO).split(".")[0]}')#line:73
                if O00O0OO0OO0O0OOOO ['status']==401 :#line:74
                    print (O00O0OO0OO0O0OOOO ['message'])#line:75
                    O000OO00OOO0OOO0O .msg .append ('有账号失效了')#line:76
                    return False #line:77
                if O00O0OO0OO0O0OOOO ['status']==500 :#line:78
                    return False #line:79
            return True #line:80
        except Exception as OO00000OOO0OO0OOO :#line:81
            print (OO00000OOO0OO0OOO )#line:82
    def sealing (O000OO0O0OO0O0OOO ):#line:85
        try :#line:86
            O0O0OO0OO00O000O0 =f'__{timi_new()}'#line:87
            OO00OO00O0O0O0000 ={'authorization':O000OO0O0OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO00O000O0 ),'signstring':O0O0OO0OO00O000O0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00OO00O0O0O0000 )#line:97
            requests .request ('get',f'{host}/packsack/list',headers =OO00OO00O0O0O0000 )#line:98
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00OO00O0O0O0000 )#line:99
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00OO00O0O0O0000 )#line:100
            requests .request ('get',f'{host}/user',headers =OO00OO00O0O0O0000 )#line:101
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00OO00O0O0O0000 )#line:102
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00OO00O0O0O0000 )#line:103
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00OO00O0O0O0000 )#line:104
            requests .request ('get',f'{host}/game/getAllData',headers =OO00OO00O0O0O0000 )#line:105
            requests .request ('get',f'{host}/assets',headers =OO00OO00O0O0O0000 )#line:106
        except Exception as O0O0O000O0OO00000 :#line:107
            print (O0O0O000O0OO00000 )#line:108
    def market_sale (O000O0O00O0O0OOO0 ):#line:111
        try :#line:112
            OOOOOOO00OOO0OOOO =timi_new ()#line:113
            O00O0O00O0OOO0000 =f'type=crop__{OOOOOOO00OOO0OOOO}'#line:114
            OO00OOOOO00000O0O ={'source':'scsc','authorization':O000O0O00O0O0OOO0 .token ,'timestamp':str (OOOOOOO00OOO0OOOO ),'sign':sign (O00O0O00O0OOO0000 ),'signstring':O00O0O00O0OOO0000 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:124
            OO0OOOOO00O000OO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00OOOOO00000O0O ).json ()#line:125
            if 'status'in OO0OOOOO00O000OO0 :#line:127
                if OO0OOOOO00O000OO0 ['status']==200 :#line:128
                    if OO0OOOOO00O000OO0 ['data']['rows']:#line:129
                        O0000000OOOOOOO0O =OO0OOOOO00O000OO0 ['data']['rows'][0 ]['packsackItemId']#line:130
                        O000OO00O00O00OOO =OO0OOOOO00O000OO0 ['data']['rows'][0 ]['quantity']#line:131
                        OO000OO00OO0OOO0O =f'_packsackItemId={O0000000OOOOOOO0O}&price={price}&quantity={O000OO00O00O00OOO}_{OOOOOOO00OOO0OOOO}'#line:132
                        O0O0000O000O00000 ={'source':'scsc','authorization':O000O0O00O0O0OOO0 .token ,'timestamp':str (OOOOOOO00OOO0OOOO ),'sign':sign (OO000OO00OO0OOO0O ),'signstring':OO000OO00OO0OOO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:142
                        O0O0000O0O00000OO ={"packsackItemId":O0000000OOOOOOO0O ,"price":str (price ),"quantity":str (O000OO00O00O00OOO )}#line:147
                        OO00O00OOO0OOOO00 =requests .request ('post',f'{host}/market/sale',headers =O0O0000O000O00000 ,data =O0O0000O0O00000OO ).json ()#line:148
                        if 'status'in OO00O00OOO0OOOO00 :#line:150
                            if OO00O00OOO0OOOO00 ['status']==200 :#line:151
                                print (f'【上架芦荟】:数量:{O000OO00O00O00OOO}丨价格:{price}')#line:152
        except Exception as O00OOOO0OO000OO00 :#line:153
            print (O00OOOO0OO000OO00 )#line:154
    def game_map (O00OOOOO0O00OOO00 ):#line:157
        try :#line:158
            OOOOO0O000000000O =f'__{timi_new()}'#line:159
            OO0OOO0OO0OO000OO ={'source':'scsc','authorization':O00OOOOO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O000000000O ),'signstring':OOOOO0O000000000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
            O00OOO000OO0O00OO =requests .request ('get',f'{host}/game/map',headers =OO0OOO0OO0OO000OO ).json ()#line:170
            if 'status'in O00OOO000OO0O00OO :#line:172
                if O00OOO000OO0O00OO ['status']==200 :#line:173
                    for O0O0O0OO00O00OOOO in O00OOO000OO0O00OO ['data']['list'][0 ]['crops']:#line:174
                        OOO00000OOOOO0OO0 =O0O0O0OO00O00OOOO ['level']#line:176
                        if OOO00000OOOOO0OO0 ==41 :#line:177
                            O000OOO0OOOO0OO0O =O0O0O0OO00O00OOOO ['crop_name']#line:178
                            O0O0OOO00OO000OOO =O0O0O0OO00O00OOOO ['count']#line:179
                            if O0O0OOO00OO000OOO >0 :#line:180
                                print (f'【农业资产】:{O000OOO0OOOO0OO0O}丨数量:{O0O0OOO00OO000OOO}')#line:181
        except Exception as O00OO0O0OO00O000O :#line:182
            print (O00OO0O0OO00O000O )#line:183
    def query_to_sell (OO0000O00OOO0O000 ):#line:187
        try :#line:188
            O0OO0OO0O00O0OO0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:189
            O00000OO0O0000OOO ={'source':'scsc','authorization':OO0000O00OOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O00O0OO0O ),'signstring':O0OO0OO0O00O0OO0O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
            OOO0O0OOOOOO0O00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00000OO0O0000OOO ).json ()#line:200
            if 'status'in OOO0O0OOOOOO0O00O :#line:202
                if OOO0O0OOOOOO0O00O ['status']==200 :#line:203
                    for OOOO0O000O00O0OO0 in OOO0O0OOOOOO0O00O ['data']['rows']:#line:204
                        O0O00OO0OO0O00O00 =OOOO0O000O00O0OO0 ['materialKey']#line:205
                        OO00O00O000OO0OO0 =OOOO0O000O00O0OO0 ['quantity']#line:206
                        OO0O000OOOO0OOOO0 =OOOO0O000O00O0OO0 ['price']#line:207
                        OO0OOOOO00OOO00OO =OOOO0O000O00O0OO0 ['saleState']#line:208
                        if OO0OOOOO00OOO00OO ==0 :#line:209
                            print (f'【出售订单】:名称:{O0O00OO0OO0O00O00}丨数量:{OO00O00O000OO0OO0}丨价格:{OO0O000OOOO0OOOO0}')#line:210
                            O000O0O0OOO000O00 =OOOO0O000O00O0OO0 ['id']#line:211
                            OO0000O00OOO0O000 .cacel_sale (O000O0O0OOO000O00 )#line:212
        except Exception as OOO00OO0OO0OO0000 :#line:220
            print (OOO00OO0OO0OO0000 )#line:221
    def cacel_sale (OOO00O00OOOOO00OO ,OO0O0OO0OO00O0000 ):#line:225
        try :#line:226
            OO00000OO0O00O0OO =f'_saleId={OO0O0OO0OO00O0000}_{timi_new()}'#line:227
            O0OOO0O0000O00OO0 ={'source':'scsc','authorization':OOO00O00OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0O00O0OO ),'signstring':OO00000OO0O00O0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:237
            OO0OO00OO0000OO0O ={"saleId":OO0O0OO0OO00O0000 }#line:240
            OOOO0OO0000000O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OOO0O0000O00OO0 ,data =OO0OO00OO0000OO0O ).json ()#line:241
            if 'status'in OOOO0OO0000000O00 :#line:243
                if OOOO0OO0000000O00 ['status']==200 :#line:244
                    print (f'【下架出售】:{OOOO0OO0000000O00["data"]}')#line:245
        except Exception as O0OO00O0OOOO000O0 :#line:246
            print (O0OO00O0OOOO000O0 )#line:247
def os_qinglong ():#line:252
    if application in os .environ :#line:253
        O00000OO00O00O0OO =os .environ [application ].split ('\n')#line:254
        if len (O00000OO00O00O0OO )>0 :#line:255
            return O00000OO00O00O0OO #line:256
        else :#line:257
            print (f"{application}变量未启用")#line:258
            print ('脚本退出')#line:259
            sys .exit (1 )#line:260
    else :#line:261
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:263
        return os_built ()#line:264
def os_built ():#line:267
    if token :#line:268
        O00O0O000O00OO0OO =token .split ('\n')#line:269
        if len (O00O0O000O00OO0OO )>0 :#line:270
            return O00O0O000O00OO0OO #line:271
    else :#line:272
        print (f"内置变量为空")#line:273
        print ('脚本结束')#line:274
        sys .exit (0 )#line:275
if __name__ =='__main__':#line:278
    start ()#line:279
