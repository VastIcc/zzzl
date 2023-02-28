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
            O000O0000000O0OO0 =os_qinglong ()#line:10
            print (f"==========共找到{len(O000O0000000O0OO0)}个账号==========")#line:11
            for OO0OO0OO00OO0OO0O in O000O0000000O0OO0 :#line:12
                OO0O00OO0O0O000O0 =[]#line:13
                print (f"------------正在执行第{O000O0000000O0OO0.index(OO0OO0OO00OO0OO0O) + 1}个账号------------")#line:14
                O000O00OO0O0OO00O =CityEarth (OO0OO0OO00OO0OO0O ,OO0O00OO0O0O000O0 )#line:15
                if O000O00OO0O0OO00O .base_info ():#line:17
                    O000O00OO0O0OO00O .sealing ()#line:19
                    O000O00OO0O0OO00O .query_to_sell ()#line:21
                    O000O00OO0O0OO00O .game_map ()#line:23
                    O000O00OO0O0OO00O .market_sale ()#line:25
    except Exception as OO00O00O0O000O0OO :#line:27
        print (OO00O00O0O000O0OO )#line:28
def sign (O0O000000OO0O0O00 ):#line:31
    O00OOO0000OO00O00 =hashlib .md5 (O0O000000OO0O0O00 .encode ()).hexdigest ()#line:32
    O0O0OO00OOO00OO0O ="scsc%^&*"+O00OOO0000OO00O00 +"19319#$%^&*((*&^%$#@#RFGHJ%^KAfghfg"#line:33
    O0O0OOO0000O0OO0O =hashlib .md5 (O0O0OO00OOO00OO0O .encode ()).hexdigest ()#line:34
    return O0O0OOO0000O0OO0O #line:35
def timi_new ():#line:37
    return str (int (time .time ()*1000 ))#line:38
class CityEarth :#line:41
    def __init__ (OOOO00OOOOO0O000O ,O00O0OOOOO0O0OOOO ,O0OOOO00OOO00OOO0 ):#line:43
        try :#line:44
            OOOO00OOOOO0O000O .msg =O0OOOO00OOO00OOO0 #line:45
            OOOO00OOOOO0O000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:46
            OOOO00OOOOO0O000O .token =O00O0OOOOO0O0OOOO .split ('&')[0 ]#line:47
        except :#line:48
            print ('变量格式错误')#line:49
    def base_info (OOO0O0OO0OO0OOOOO ):#line:52
        try :#line:53
            OO000000O000OO0OO =f'__{timi_new()}'#line:54
            O00OOOO00O0O00O0O ={'source':'scsc','authorization':OOO0O0OO0OO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O000OO0OO ),'signstring':OO000000O000OO0OO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:64
            O00O00000OOOO0000 =requests .request ('get',f'{host}/user',headers =O00OOOO00O0O00O0O ).json ()#line:65
            if 'status'in O00O00000OOOO0000 :#line:67
                if O00O00000OOOO0000 ['status']==200 :#line:68
                    OO0OO0O00O0OO0O00 =O00O00000OOOO0000 ['data']['nickname']#line:69
                    O0OOO00000000OOOO =O00O00000OOOO0000 ['data']['inner_id']#line:70
                    O0O00000OOOOOOOO0 =O00O00000OOOO0000 ['data']['assets']['gold']#line:71
                    OO0OO000OO00OO000 =O00O00000OOOO0000 ['data']['level']#line:72
                    print (f'【账号信息】:昵称:{OO0OO0O00O0OO0O00[:5]}丨ID:{O0OOO00000000OOOO}丨等级:{OO0OO000OO00OO000}丨金种子:{str(O0O00000OOOOOOOO0).split(".")[0]}')#line:73
                if O00O00000OOOO0000 ['status']==401 :#line:74
                    print (O00O00000OOOO0000 ['message'])#line:75
                    OOO0O0OO0OO0OOOOO .msg .append ('有账号失效了')#line:76
                    return False #line:77
                if O00O00000OOOO0000 ['status']==500 :#line:78
                    return False #line:79
            return True #line:80
        except Exception as O000OOO000OO000O0 :#line:81
            print (O000OOO000OO000O0 )#line:82
    def sealing (OO0OO00O0OO0OO000 ):#line:85
        try :#line:86
            O000OOOO000OO000O =f'__{timi_new()}'#line:87
            OOO000000O00O000O ={'authorization':OO0OO00O0OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO000OO000O ),'signstring':O000OOOO000OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:96
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000000O00O000O )#line:97
            requests .request ('get',f'{host}/packsack/list',headers =OOO000000O00O000O )#line:98
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000000O00O000O )#line:99
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000000O00O000O )#line:100
            requests .request ('get',f'{host}/user',headers =OOO000000O00O000O )#line:101
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000000O00O000O )#line:102
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000000O00O000O )#line:103
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000000O00O000O )#line:104
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000000O00O000O )#line:105
            requests .request ('get',f'{host}/assets',headers =OOO000000O00O000O )#line:106
        except Exception as O0O0O000OO000O0OO :#line:107
            print (O0O0O000OO000O0OO )#line:108
    def market_sale (O00OO0O0O0OOOOO0O ):#line:111
        try :#line:112
            OOOOO0O000O0OO0O0 =timi_new ()#line:113
            O0OO000OO0OO0OOOO =f'type=crop__{OOOOO0O000O0OO0O0}'#line:114
            OO00O0OOO000O000O ={'source':'scsc','authorization':O00OO0O0O0OOOOO0O .token ,'timestamp':str (OOOOO0O000O0OO0O0 ),'sign':sign (O0OO000OO0OO0OOOO ),'signstring':O0OO000OO0OO0OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:124
            O00OOOOO00O00O000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00O0OOO000O000O ).json ()#line:125
            if 'status'in O00OOOOO00O00O000 :#line:127
                if O00OOOOO00O00O000 ['status']==200 :#line:128
                    if O00OOOOO00O00O000 ['data']['rows']:#line:129
                        OO0OO0OO0O00OO00O =O00OOOOO00O00O000 ['data']['rows'][0 ]['packsackItemId']#line:130
                        O0OOO0O0OOO000000 =O00OOOOO00O00O000 ['data']['rows'][0 ]['quantity']#line:131
                        OO0O0O0OOO0OO000O =f'_packsackItemId={OO0OO0OO0O00OO00O}&price={price}&quantity={O0OOO0O0OOO000000}_{OOOOO0O000O0OO0O0}'#line:132
                        OOO0OOO00OOO0O00O ={'source':'scsc','authorization':O00OO0O0O0OOOOO0O .token ,'timestamp':str (OOOOO0O000O0OO0O0 ),'sign':sign (OO0O0O0OOO0OO000O ),'signstring':OO0O0O0OOO0OO000O ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:142
                        O0OOOOO00O00OOOO0 ={"packsackItemId":OO0OO0OO0O00OO00O ,"price":str (price ),"quantity":str (O0OOO0O0OOO000000 )}#line:147
                        O0OOO0O000OO0O0OO =requests .request ('post',f'{host}/market/sale',headers =OOO0OOO00OOO0O00O ,data =O0OOOOO00O00OOOO0 ).json ()#line:148
                        if 'status'in O0OOO0O000OO0O0OO :#line:150
                            if O0OOO0O000OO0O0OO ['status']==200 :#line:151
                                print (f'【上架芦荟】:数量:{O0OOO0O0OOO000000}丨价格:{price}')#line:152
        except Exception as OO0OOO000O0OOOOO0 :#line:153
            print (OO0OOO000O0OOOOO0 )#line:154
    def game_map (OO000O0000OOO0000 ):#line:157
        try :#line:158
            O00O000OOOOOOOO00 =f'__{timi_new()}'#line:159
            OO0O00OOOO0OO0000 ={'source':'scsc','authorization':OO000O0000OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOOOOOO00 ),'signstring':O00O000OOOOOOOO00 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:169
            O0OOO000O000OO00O =requests .request ('get',f'{host}/game/map',headers =OO0O00OOOO0OO0000 ).json ()#line:170
            if 'status'in O0OOO000O000OO00O :#line:172
                if O0OOO000O000OO00O ['status']==200 :#line:173
                    for OO0000OO0000OO0OO in O0OOO000O000OO00O ['data']['list'][0 ]['crops']:#line:174
                        O0000OO000000O0O0 =OO0000OO0000OO0OO ['level']#line:176
                        if O0000OO000000O0O0 ==41 :#line:177
                            OO000OOOO0O000OO0 =OO0000OO0000OO0OO ['crop_name']#line:178
                            O000000OO00OO0O00 =OO0000OO0000OO0OO ['count']#line:179
                            if O000000OO00OO0O00 >0 :#line:180
                                print (f'【农业资产】:{OO000OOOO0O000OO0}丨数量:{O000000OO00OO0O00}')#line:181
        except Exception as O000OO0OO0O0OO0O0 :#line:182
            print (O000OO0OO0O0OO0O0 )#line:183
    def query_to_sell (OOO00OOOOO00OO00O ):#line:187
        try :#line:188
            OOOO000OOO000OOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:189
            O00OO0O00O0O00OOO ={'source':'scsc','authorization':OOO00OOOOO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOO000OOOO ),'signstring':OOOO000OOO000OOOO ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
            O0OOOO0000OO0O000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OO0O00O0O00OOO ).json ()#line:200
            if 'status'in O0OOOO0000OO0O000 :#line:202
                if O0OOOO0000OO0O000 ['status']==200 :#line:203
                    for O0O0OO0OO0000O000 in O0OOOO0000OO0O000 ['data']['rows']:#line:204
                        O00OO0OO0O00O0OOO =O0O0OO0OO0000O000 ['materialKey']#line:205
                        O0OO0OO00OOOO000O =O0O0OO0OO0000O000 ['quantity']#line:206
                        OO00OO0OOOOOO0OO0 =O0O0OO0OO0000O000 ['price']#line:207
                        O0OO00O00OO0OOOO0 =O0O0OO0OO0000O000 ['saleState']#line:208
                        if O0OO00O00OO0OOOO0 ==0 :#line:209
                            print (f'【出售订单】:名称:{O00OO0OO0O00O0OOO}丨数量:{O0OO0OO00OOOO000O}丨价格:{OO00OO0OOOOOO0OO0}')#line:210
                            OOO0O0OO00OOO0OOO =O0O0OO0OO0000O000 ['id']#line:211
                            OOO00OOOOO00OO00O .cacel_sale (OOO0O0OO00OOO0OOO )#line:212
        except Exception as O00OOOO000O0O0OO0 :#line:220
            print (O00OOOO000O0O0OO0 )#line:221
    def cacel_sale (O0O000O0O0O000O00 ,OOO00OO000OOO0OOO ):#line:225
        try :#line:226
            O00OOO000OOO00OO0 =f'_saleId={OOO00OO000OOO0OOO}_{timi_new()}'#line:227
            OOO00O000OO00OOOO ={'source':'scsc','authorization':O0O000O0O0O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000OOO00OO0 ),'signstring':O00OOO000OOO00OO0 ,'version':version ,'Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:237
            OO0OO0O000OO0O00O ={"saleId":OOO00OO000OOO0OOO }#line:240
            OO0O0000O0OOOOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO00O000OO00OOOO ,data =OO0OO0O000OO0O00O ).json ()#line:241
            if 'status'in OO0O0000O0OOOOOOO :#line:243
                if OO0O0000O0OOOOOOO ['status']==200 :#line:244
                    print (f'【下架出售】:{OO0O0000O0OOOOOOO["data"]}')#line:245
        except Exception as O0OOOOO00000OO0O0 :#line:246
            print (O0OOOOO00000OO0O0 )#line:247
def os_qinglong ():#line:252
    if application in os .environ :#line:253
        OO0OO0OOOOO00OOO0 =os .environ [application ].split ('\n')#line:254
        if len (OO0OO0OOOOO00OOO0 )>0 :#line:255
            return OO0OO0OOOOO00OOO0 #line:256
        else :#line:257
            print (f"{application}变量未启用")#line:258
            print ('脚本退出')#line:259
            sys .exit (1 )#line:260
    else :#line:261
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:263
        return os_built ()#line:264
def os_built ():#line:267
    if token :#line:268
        OO0O0000000OO0000 =token .split ('\n')#line:269
        if len (OO0O0000000OO0000 )>0 :#line:270
            return OO0O0000000OO0000 #line:271
    else :#line:272
        print (f"内置变量为空")#line:273
        print ('脚本结束')#line:274
        sys .exit (0 )#line:275
if __name__ =='__main__':#line:278
    start ()#line:279
