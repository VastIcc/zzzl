# coding: utf-8
try:
    import threading, re, os, sys, time, hashlib, json, requests, random, socket, uuid, datetime
    import Invalid_login
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 6 1-23/2 * * *
@ new Env('生城世朝')       
@ 项目地址  https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/prod/1.9.3.1.S4195.apk
@ 抓取  http://scsc.sc19319.com 的authorization值
@ 配置文件和脚本要放同一目录
@ 版本  4.6
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
count_list =0 #line:5
msg_list =[]#line:6
invited_new =[]#line:7
weishim =[]#line:8
def start ():#line:11
    try :#line:12
        O000OO000O0O00OOO00 ()#line:13
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:14
        O000OO0O00OO00O00 ()#line:15
        OO00O00O0OO0OO000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO00O00O0OO0OO000)}个账号==========")#line:17
        for OOO0O0O0000000OO0 in OO00O00O0OO0OO000 :#line:18
            O000OO000OO0O00OO =[]#line:19
            print (f"------------正在执行第{OO00O00O0OO0OO000.index(OOO0O0O0000000OO0) + 1}个账号------------")#line:20
            O0O0O0000O0OO0OOO =CityEarth (OOO0O0O0000000OO0 ,O000OO000OO0O00OO ,OO00O00O0OO0OO000 .index (OOO0O0O0000000OO0 ))#line:21
            def OOOOOO000000OO0OO ():#line:23
                if O0O0O0000O0OO0OOO .base_info ():#line:25
                    O0O0O0000O0OO0OOO .sealing ()#line:27
                    O0O0O0000O0OO0OOO .invitenum ()#line:29
                    O0O0O0000O0OO0OOO .query_to_sell ()#line:31
                    O0O0O0000O0OO0OOO .friends_invitation ()#line:35
                    O0O0O0000O0OO0OOO .energy ()#line:37
                    O0O0O0000O0OO0OOO .add_clover ()#line:39
                    O0O0O0000O0OO0OOO .propsraffle ()#line:41
                    O0O0O0000O0OO0OOO .synthetic ()#line:43
                    O0O0O0000O0OO0OOO .crops_illustrated ()#line:45
                    O0O0O0000O0OO0OOO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0O0O0000O0OO0OOO .give_gold ()#line:50
            OO000OO0OOO00O00O =threading .Thread (target =OOOOOO000000OO0OO )#line:52
            OO000OO0OOO00O00O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0OO0OO00O00OOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OO0OO00O00OOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O0O0OOOO00O0OOO in invited_new :#line:62
            print (O0O0O0OOOO00O0OOO )#line:63
        print ('开始打印未实名的token')#line:64
        for O0O00OO0OO0OOO00O in weishim :#line:65
            print (O0O00OO0OO0OOO00O )#line:66
    except Exception as O0O00OO0O0000O00O :#line:67
        print (O0O00OO0O0000O00O )#line:68
def give_gold (OO000O0OOOOO0000O ,OOO000OO000O000OO ):#line:72
    try :#line:73
        O0O00O0O00OO0OO00 =f'_doneeNo={OO000O0OOOOO0000O}&quantity={int(OOO000OO000O000OO)}_{timi_new()}'#line:74
        O0O00OOOO0O0O00OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O00O0O00OO0OO00 ),'signstring':O0O00O0O00OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0000000000OO0000 ={"quantity":int (OOO000OO000O000OO ),"doneeNo":OO000O0OOOOO0000O }#line:89
        O0OOO0O0OOOOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OOOO0O0O00OO ,data =O0000000000OO0000 ).json ()#line:90
        if 'status'in O0OOO0O0OOOOO0000 :#line:92
            if O0OOO0O0OOOOO0000 ['status']==200 :#line:93
                if O0OOO0O0OOOOO0000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO000OO000O000OO)}种子给{OO000O0OOOOO0000O}成功')#line:95
                    return True #line:96
            if O0OOO0O0OOOOO0000 ['status']==401 :#line:97
                print (f'【赠送种子】:{O0OOO0O0OOOOO0000["message"]}')#line:98
                return False #line:99
            if O0OOO0O0OOOOO0000 ['status']==500 :#line:100
                print (f'【赠送种子】:{O0OOO0O0OOOOO0000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0OO0O0OOOO0O0OO0 :#line:104
        print (O0OO0O0OOOO0O0OO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OO000OOOOOO0OOO ):#line:115
    O000O0OO0OOO000O0 =hashlib .md5 (O0OO000OOOOOO0OOO .encode ()).hexdigest ()#line:116
    OO00O00000OO00OOO =sc1 ()#line:117
    O0O0OO000OO0OO0O0 =sc2 ()#line:118
    OOOOO0OOO0O0O00OO =sc3 ()#line:119
    O000OOO0OOO0O0O00 =OO00O00000OO00OOO +O000O0OO0OOO000O0 +O0O0OO000OO0OO0O0 +OOOOO0OOO0O0O00OO #line:120
    O000O00000O0OO0O0 =hashlib .md5 (O000OOO0OOO0O0O00 .encode ()).hexdigest ()#line:121
    return O000O00000O0OO0O0 #line:122
def format_msg ():#line:125
    OO00OOO00O0O0O0O0 =""#line:126
    for OO00OO00OO000000O in msg_list :#line:127
        OO00OOO00O0O0O0O0 +=str (OO00OO00OO000000O )+"\r\n"#line:128
    return OO00OOO00O0O0O0O0 #line:129
def sc1 ():#line:132
    return "scsc%^&*"#line:133
def O000OO0O00OO00O00 ():#line:136
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:137
        ubbbf ()#line:138
    else :#line:139
        print (oyoy ())#line:140
        exit (1 )#line:141
def timi_new ():#line:144
    return str (int (time .time ()*1000 ))#line:145
json_path ="CityEarth_data.json"#line:148
json_path1 ="CityEarth_data.json"#line:149
dict ={}#line:150
def get_json_data (OOO0OO00O00O0OOOO ,OO0O0OO00OO0O0OO0 ,O0OO0O0OOOOO000OO ,OOO000O000O0O00OO ):#line:153
    with open (OOO0OO00O00O0OOOO ,'rb')as OOO00O000OOO000OO :#line:154
        O0O0OOO0O0OOOOOOO =json .load (OOO00O000OOO000OO )#line:155
        O0O0OOO0O0OOOOOOO ['data'][OO0O0OO00OO0O0OO0 ][O0OO0O0OOOOO000OO ]=OOO000O000O0O00OO #line:156
        OO0O0O000000OO000 =O0O0OOO0O0OOOOOOO #line:157
    OOO00O000OOO000OO .close ()#line:158
    return OO0O0O000000OO000 #line:159
def write_json_data (O00OOO000O000OO0O ):#line:162
    with open (json_path1 ,'w')as OO00O0OOO000OO000 :#line:163
        json .dump (O00OOO000O000OO0O ,OO00O0OOO000OO000 )#line:164
    OO00O0OOO000OO000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O00OO00O000O00000 ,O000O0OOO0O00OO00 ,OO0O0OO00O0000000 ,O0OOO0O00O0OO00O0 ):#line:171
        try :#line:172
            O00OO00O000O00000 .msg =OO0O0OO00O0000000 #line:173
            O00OO00O000O00000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O00OO00O000O00000 .token =O000O0OOO0O00OO00 ['authorization']#line:175
            O00OO00O000O00000 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O00OO00O000O00000 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O00OO00O000O00000 .elephant_user =O000O0OOO0O00OO00 ['elephant_user']#line:178
            O00OO00O000O00000 .elephant_pswd =O000O0OOO0O00OO00 ['elephant_pswd']#line:179
            O00OO00O000O00000 .elephant_Task_ID =O000O0OOO0O00OO00 ['elephant_Task_ID']#line:180
            O00OO00O000O00000 .len_new =O0OOO0O00O0OO00O0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO00O0OO000000O0O ):#line:186
        try :#line:187
            OO00O0OO000000O0O .watched_ad ()#line:189
            OOO0OOO0000O0OO00 =f'__{timi_new()}'#line:190
            OOOO0O00O00O00O00 ={'source':'scsc','authorization':OO00O0OO000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0000O0OO00 ),'signstring':OOO0OOO0000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0O000OOOOOOO0O0O =requests .request ('get',f'{host}/user',headers =OOOO0O00O00O00O00 ).json ()#line:202
            if 'status'in O0O000OOOOOOO0O0O :#line:204
                if O0O000OOOOOOO0O0O ['status']==200 :#line:205
                    OO0OO00OOOOOOO00O =O0O000OOOOOOO0O0O ['data']['nickname']#line:206
                    O00OOOO0OOOO00O00 =O0O000OOOOOOO0O0O ['data']['inner_id']#line:207
                    O0OOO000OOOO0O0OO =O0O000OOOOOOO0O0O ['data']['assets']['gold']#line:208
                    O0OOO000OO000O00O =O0O000OOOOOOO0O0O ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OO0OO00OOOOOOO00O[:5]}丨ID:{O00OOOO0OOOO00O00}丨等级:{O0OOO000OO000O00O}丨金种子:{str(O0OOO000OOOO0O0OO).split(".")[0]}')#line:211
                    if 'wx_'in OO0OO00OOOOOOO00O :#line:212
                        OO00O0OO000000O0O .change_nickname ()#line:213
                if O0O000OOOOOOO0O0O ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO00O0OO000000O0O .elephant_user =='f':#line:216
                        return False #line:217
                    OO0OO0O0O0O00OOO0 =Invalid_login .addtask (elephant_user =OO00O0OO000000O0O .elephant_user ,elephant_pswd =OO00O0OO000000O0O .elephant_pswd ,elephant_Task_ID =OO00O0OO000000O0O .elephant_Task_ID )#line:220
                    OOO0O0O00O000O0O0 =get_json_data (json_path ,OO00O0OO000000O0O .len_new ,'authorization',OO0OO0O0O0O00OOO0 )#line:221
                    if write_json_data (OOO0O0O00O000O0O0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0O000OOOOOOO0O0O ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO00OOO000OOO000 :#line:228
            print (OOO00OOO000OOO000 )#line:229
    def sealing (OO0O00O000OOO00O0 ):#line:232
        try :#line:233
            O0000OOOO00OOOO00 =f'__{timi_new()}'#line:234
            OO0OO0000O00O0O00 ={'source':'scsc','authorization':OO0O00O000OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO00OOOO00 ),'signstring':O0000OOOO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OO0000O00O0O00 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO0OO0000O00O0O00 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OO0000O00O0O00 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OO0000O00O0O00 )#line:249
            requests .request ('get',f'{host}/user',headers =OO0OO0000O00O0O00 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OO0000O00O0O00 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OO0000O00O0O00 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OO0000O00O0O00 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0000O00O0O00 )#line:254
            requests .request ('get',f'{host}/assets',headers =OO0OO0000O00O0O00 )#line:255
        except Exception as OOOOOOOOOO0000OO0 :#line:256
            print (OOOOOOOOOO0000OO0 )#line:257
    def ddd (OOO00OOOOOOOOOO00 ):#line:259
        try :#line:260
            O0000OOOO0O0OO0O0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00000OOO0OOOOOOO ={'source':'scsc','authorization':OOO00OOOOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0O0OO0O0 ),'signstring':O0000OOOO0O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0O00000OO00O000 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00000OOO0OOOOOOO ).json ()#line:273
            print (OO0O00000OO00O000 )#line:274
        except Exception as OO0OO0OOOOO0O0000 :#line:277
            print (OO0OO0OOOOO0O0000 )#line:278
    def the_query (OOOOO0OOOO0O0O00O ):#line:283
        try :#line:284
            OOOO0O00OO0O0O00O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OOO000OOOO00OO00O ={'authorization':OOOOO0OOOO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00OO0O0O00O ),'signstring':OOOO0O00OO0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O000000O0OO0OOOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO000OOOO00OO00O ).json ()#line:296
            if 'status'in O000000O0OO0OOOO0 :#line:298
                if O000000O0OO0OOOO0 ['status']==200 :#line:299
                    O000O00OO0OOOOO0O =O000000O0OO0OOOO0 ['data']['rows'][4 ]['price']#line:300
                    return O000O00OO0OOOOO0O #line:301
        except Exception as O000O0000000O00OO :#line:302
            print (O000O0000000O00OO )#line:303
    def market_sale (O00000OO00O00OO00 ,OO0OOOOOOOOO000O0 ):#line:306
        try :#line:307
            OOO00OOOO00OO0OO0 =timi_new ()#line:308
            OOOO00O0OOOOO0O0O =f'type=crop__{OOO00OOOO00OO0OO0}'#line:309
            OO0O00O0O0000OO00 ={'source':'scsc','authorization':O00000OO00O00OO00 .token ,'timestamp':str (OOO00OOOO00OO0OO0 ),'sign':sign (OOOO00O0OOOOO0O0O ),'signstring':OOOO00O0OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:320
            O00O000O0O000O0OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O00O0O0000OO00 ).json ()#line:321
            if 'status'in O00O000O0O000O0OO :#line:323
                if O00O000O0O000O0OO ['status']==200 :#line:324
                    if O00O000O0O000O0OO ['data']['rows']:#line:325
                        OO00OOOOOO0O000O0 =O00O000O0O000O0OO ['data']['rows'][0 ]['packsackItemId']#line:326
                        O0OO0OO000O0O0OOO =O00O000O0O000O0OO ['data']['rows'][0 ]['quantity']#line:327
                        OOOOOO00O0O00O000 =float (OO0OOOOOOOOO000O0 )-0.001 #line:328
                        if OOOOOO00O0O00O000 >9 :#line:329
                            O000OO00OOOO000OO =f'_packsackItemId={OO00OOOOOO0O000O0}&price={str(OO0OOOOOOOOO000O0)[:5]}&quantity={O0OO0OO000O0O0OOO}_{OOO00OOOO00OO0OO0}'#line:330
                            O0O000OO0O0OO00O0 ={'source':'scsc','authorization':O00000OO00O00OO00 .token ,'timestamp':str (OOO00OOOO00OO0OO0 ),'sign':sign (O000OO00OOOO000OO ),'signstring':O000OO00OOOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
                            OO00OOO0OOOOO00O0 ={"packsackItemId":OO00OOOOOO0O000O0 ,"price":str (OO0OOOOOOOOO000O0 )[:5 ],"quantity":str (O0OO0OO000O0O0OOO )}#line:346
                            O0O0OO00OO0000000 =requests .request ('post',f'{host}/market/sale',headers =O0O000OO0O0OO00O0 ,data =OO00OOO0OOOOO00O0 ).json ()#line:347
                            if 'status'in O0O0OO00OO0000000 :#line:349
                                if O0O0OO00OO0000000 ['status']==200 :#line:350
                                    print (f'【上架芦荟】:数量:{O0OO0OO000O0O0OOO}丨价格:{str(OO0OOOOOOOOO000O0)[:5]}')#line:351
        except Exception as O000O0O0000O00OOO :#line:352
            print (O000O0O0000O00OOO )#line:353
    def query_to_sell (O0OO0O000000O00OO ):#line:356
        global count_list #line:357
        try :#line:358
            OO0OOOO0000O0000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOO00OO00O00OOOO0 ={'source':'scsc','authorization':O0OO0O000000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0000O0000O ),'signstring':OO0OOOO0000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O0OO000000O0OO00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00OO00O00OOOO0 ).json ()#line:371
            if 'status'in O0OO000000O0OO00O :#line:373
                if O0OO000000O0OO00O ['status']==200 :#line:374
                    for O00000OO000OOO00O in O0OO000000O0OO00O ['data']['rows']:#line:375
                        OO0OO00000000O00O =O00000OO000OOO00O ['materialKey']#line:376
                        OO0OOOOOOO0O0O00O =O00000OO000OOO00O ['quantity']#line:377
                        OOO0O0O00OOO0OOO0 =O00000OO000OOO00O ['price']#line:378
                        OOOO00O000OOO00O0 =O00000OO000OOO00O ['saleState']#line:379
                        if OOOO00O000OOO00O0 ==0 :#line:380
                            print (f'【出售订单】:名称:{OO0OO00000000O00O}丨数量:{OO0OOOOOOO0O0O00O}丨价格:{OOO0O0O00OOO0OOO0}')#line:381
                            count_list +=OO0OOOOOOO0O0O00O #line:382
                            O0OO00O0OOOOO0O00 =O0OO0O000000O00OO .the_query ()#line:384
                            if float (O0OO00O0OOOOO0O00 )!=float (OOO0O0O00OOO0OOO0 ):#line:385
                                OOOO0O0O00O0OO0OO =O00000OO000OOO00O ['id']#line:386
                                if float (datetime .datetime .now ().hour )>8 :#line:387
                                    O0OO0O000000O00OO .cacel_sale (OOOO0O0O00O0OO0OO )#line:388
                                    O0OO0O000000O00OO .market_sale (OOO0O0O00OOO0OOO0 )#line:389
                    O0OO0O000000O00OO .game_map ()#line:391
        except Exception as OOO0O0000OO0OO0OO :#line:393
            print (OOO0O0000OO0OO0OO )#line:394
    def cacel_sale (OO00OO0O0OO00O00O ,OOO000O00OOO0OO00 ):#line:397
        try :#line:398
            OO0OO0O0O0OO00000 =f'_saleId={OOO000O00OOO0OO00}_{timi_new()}'#line:399
            O0OOOOOOOO0O0000O ={'source':'scsc','authorization':OO00OO0O0OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O0OO00000 ),'signstring':OO0OO0O0O0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:410
            O00000OOOOOOOOOO0 ={"saleId":OOO000O00OOO0OO00 }#line:411
            O00O0OOO0O0000OO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OOOOOOOO0O0000O ,data =O00000OOOOOOOOOO0 ).json ()#line:412
            if 'status'in O00O0OOO0O0000OO0 :#line:414
                if O00O0OOO0O0000OO0 ['status']==200 :#line:415
                    print (f'【下架出售】:{O00O0OOO0O0000OO0["data"]}')#line:416
        except Exception as O0O000O00O0O0OO00 :#line:417
            print (O0O000O00O0O0OO00 )#line:418
    def change_nickname (O0O00OOO000O0O0O0 ):#line:421
        try :#line:422
            O000O0OOOO00OOOOO =timi_new ()#line:423
            O00OO00OO0OO00O0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:424
            OO00O0OOO0OOOOO0O =requests .request ('post','https://www.qmsjmfb.com/',data =O00OO00OO0OO00O0O ).text #line:425
            OOO0OO0OO00O0O00O =re .findall ('<ul><li>(.*?)</li>',OO00O0OOO0OOOOO0O )[0 ][:3 ]#line:426
            O00O0OO0OO0O0O0O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO0OO0OO00O0O00O}').json ()#line:427
            OO00OOO0OOOO000OO =O00O0OO0OO0O0O0O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:428
            OO00OO0OOOOOOOO0O ={"nickname":OO00OOO0OOOO000OO }#line:429
            O00O000000OOO0O00 =f'_nickname={OO00OOO0OOOO000OO}_{O000O0OOOO00OOOOO}'#line:430
            O00O0O000OOOO0000 ={'source':'scsc','authorization':O0O00OOO000O0O0O0 .token ,'timestamp':O000O0OOOO00OOOOO ,'sign':sign (O00O000000OOO0O00 ),'signstring':O00O000000OOO0O00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:441
            OO0O0OO0000OO0000 =requests .request ('patch',f'{host}/user/nickname',headers =O00O0O000OOOO0000 ,data =OO00OO0OOOOOOOO0O ).json ()#line:442
            if 'status'in OO0O0OO0000OO0000 :#line:444
                if OO0O0OO0000OO0000 ['status']==200 :#line:445
                    print (f'【修改网名】:网名:{OO00OOO0OOOO000OO}丨{OO0O0OO0000OO0000["message"]}')#line:446
        except Exception as O0O0O000OOO0OOOO0 :#line:447
            print (O0O0O000OOO0OOOO0 )#line:448
    def withdraw (O00OOOO0OOOOOO000 ):#line:451
        try :#line:452
            OO0O0OO0OOOO0O00O =f'__{timi_new()}'#line:453
            OO0000OOO0O0000OO ={'source':'scsc','authorization':O00OOOO0OOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OOOO0O00O ),'signstring':OO0O0OO0OOOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:464
            OO0OO0OO0O0OO00OO =requests .request ('get',f'{host}/assets',headers =OO0000OOO0O0000OO ).json ()#line:465
            if 'status'in OO0OO0OO0O0OO00OO :#line:467
                if OO0OO0OO0O0OO00OO ['status']==200 :#line:468
                    OOO0000O000OO0OO0 =OO0OO0OO0O0OO00OO ['data']['cash']#line:469
                    if float (OOO0000O000OO0OO0 )>20 :#line:470
                        OO0O0OO0OOOO0O00O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:471
                        OO0000OOO0O0000OO ={'authorization':O00OOOO0OOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OOOO0O00O ),'signstring':OO0O0OO0OOOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
                        OOO0OO00000O0000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:482
                        OO00O0OOOO000O00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0000OOO0O0000OO ,data =OOO0OO00000O0000O ).json ()#line:484
                        if 'status'in OO00O0OOOO000O00O :#line:486
                            if OO00O0OOOO000O00O ['status']==200 :#line:487
                                print (f'【余额提现】:{OO00O0OOOO000O00O["data"]}')#line:488
                        if 'status'in OO00O0OOOO000O00O :#line:489
                            if OO00O0OOOO000O00O ['status']==500 :#line:490
                                print (f'【余额提现】:{OO00O0OOOO000O00O["message"]}')#line:491
        except Exception as O000O0O00OOOO0OOO :#line:492
            print (O000O0O00OOOO0OOO )#line:493
    def invitenum (O000O000O0O0OO00O ):#line:496
        global invited_new #line:497
        try :#line:498
            O0000OOOOO0OOO0OO =f'__{timi_new()}'#line:499
            OOOO0000O0OO00000 ={'source':'scsc','authorization':O000O000O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO0OOO0OO ),'signstring':O0000OOOOO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
            OO0O000000OOOO000 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0000O0OO00000 ).json ()#line:511
            if 'status'in OO0O000000OOOO000 :#line:513
                if OO0O000000OOOO000 ['status']==200 :#line:514
                    OOOOO0OOO00O00O0O =OO0O000000OOOO000 ['data']['invited_count']#line:515
                    O0OOO00OOOO000OO0 =OO0O000000OOOO000 ['data']['invited_second_count']#line:516
                    print (f'【我的邀请】:直邀好友:{OOOOO0OOO00O00O0O}丨间邀好友:{O0OOO00OOOO000OO0}')#line:517
                    if OOOOO0OOO00O00O0O <2 :#line:518
                        OO00O00000OO0O0OO =f'__{timi_new()}'#line:519
                        O0OOO000OOOOOO000 ={'source':'scsc','authorization':O000O000O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00000OO0O0OO ),'signstring':OO00O00000OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:530
                        OO0O0000OOOOOO0OO =requests .request ('get',f'{host}/user',headers =O0OOO000OOOOOO000 ).json ()#line:531
                        if 'status'in OO0O0000OOOOOO0OO :#line:533
                            if OO0O0000OOOOOO0OO ['status']==200 :#line:534
                                invited_new .append (OO0O0000OOOOOO0OO ['data']['inner_id'])#line:535
        except Exception as OO0O000000OOO00O0 :#line:536
            print (OO0O000000OOO00O0 )#line:537
    def game_map (OOO00O000O0OO00OO ):#line:540
        try :#line:541
            O0000OOOO0O0O0O00 =f'__{timi_new()}'#line:542
            O00000O00O00OO000 ={'source':'scsc','authorization':OOO00O000O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0O0O0O00 ),'signstring':O0000OOOO0O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:553
            OOO00OOOOOOOO0OO0 =requests .request ('get',f'{host}/game/map',headers =O00000O00O00OO000 ).json ()#line:554
            if 'status'in OOO00OOOOOOOO0OO0 :#line:556
                if OOO00OOOOOOOO0OO0 ['status']==200 :#line:557
                    for OOO0OOO00O0000OO0 in OOO00OOOOOOOO0OO0 ['data']['list'][0 ]['crops']:#line:558
                        O000O0O0000O0OO00 =OOO0OOO00O0000OO0 ['level']#line:560
                        if O000O0O0000O0OO00 ==41 :#line:561
                            OOO000O0O00OO0OO0 =OOO0OOO00O0000OO0 ['crop_name']#line:562
                            O0000O000O0OOOOO0 =OOO0OOO00O0000OO0 ['count']#line:563
                            if O0000O000O0OOOOO0 >0 :#line:564
                                print (f'【农业资产】:{OOO000O0O00OO0OO0}丨数量:{O0000O000O0OOOOO0}')#line:565
                                if float (datetime .datetime .now ().hour )>8 :#line:566
                                    OOOOO0O00000000OO =OOO00O000O0OO00OO .the_query ()#line:567
                                    OOO00O000O0OO00OO .market_sale (OOOOO0O00000000OO )#line:568
        except Exception as OO00OO0O00OOOOO0O :#line:569
            print (OO00OO0O00OOOOO0O )#line:570
    def give_gold (OOOOO000OOOOOO0OO ):#line:573
        try :#line:574
            OO0O0OOO000000O0O =f'__{timi_new()}'#line:575
            O000000OO0O0OOO0O ={'source':'scsc','authorization':OOOOO000OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000000O0O ),'signstring':OO0O0OOO000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:586
            OO0OO0OO00O00O00O =requests .request ('get',f'{host}/user',headers =O000000OO0O0OOO0O ).json ()#line:587
            if 'status'in OO0OO0OO00O00O00O :#line:588
                if OO0OO0OO00O00O00O ['status']==200 :#line:589
                    if float (OOOOO000OOOOOO0OO .doneeNo )!=0 :#line:590
                        O000000O0OO0OO000 =OO0OO0OO00O00O00O ['data']['assets']['gold']#line:591
                        if float (O000000O0OO0OO000 )>float (OOOOO000OOOOOO0OO .innerId ):#line:592
                            O000OO0OO0O0OOO0O =int (float (O000000O0OO0OO000 )/1.1 )#line:593
                            OO0O0OOO000000O0O =f'_doneeNo={OOOOO000OOOOOO0OO.doneeNo}&quantity={O000OO0OO0O0OOO0O}_{timi_new()}'#line:594
                            O000000OO0O0OOO0O ={'source':'scsc','authorization':OOOOO000OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000000O0O ),'signstring':OO0O0OOO000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:605
                            O00OO00000O0000O0 ={"quantity":O000OO0OO0O0OOO0O ,"doneeNo":OOOOO000OOOOOO0OO .doneeNo }#line:609
                            OOO0OOOO0O0O0O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O000000OO0O0OOO0O ,data =O00OO00000O0000O0 ).json ()#line:610
                            if 'status'in OOO0OOOO0O0O0O0O0 :#line:612
                                if OOO0OOOO0O0O0O0O0 ['status']==200 :#line:613
                                    if OOO0OOOO0O0O0O0O0 ['data']:#line:614
                                        print (f'【赠送种子】:赠送{O000OO0OO0O0OOO0O}种子给{OOOOO000OOOOOO0OO.doneeNo}成功')#line:615
                    else :#line:616
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:617
        except Exception as O0O0000O00OOOO000 :#line:618
            print (O0O0000O00OOOO000 )#line:619
    def invitation (OOO000O00O0O00O0O ):#line:621
        try :#line:622
            _O00O0000OOO00000O =float (bundled_def ())/4 #line:623
            O0OO000OO000OOO0O =f'_innerId={int(_O00O0000OOO00000O)}_{timi_new()}'#line:624
            O00OOOOOOOO0OOO00 ={'source':'scsc','authorization':OOO000O00O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OO000OOO0O ),'signstring':O0OO000OO000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:635
            O00O0O0OOO0O0000O ={"innerId":int (_O00O0000OOO00000O )}#line:636
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00OOOOOOOO0OOO00 ,data =O00O0O0OOO0O0000O )#line:637
        except Exception as O00000OO0OOO0000O :#line:638
            print (O00000OO0OOO0000O )#line:639
    def winning_rewards (O0000000O00O0O000 ):#line:642
        try :#line:643
            O00OO0O00O0OO0000 =f'__{timi_new()}'#line:644
            O0OOO000OOOO00O0O ={'source':'scsc','authorization':O0000000O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00O0OO0000 ),'signstring':O00OO0O00O0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:655
            O00O0O000OOO0O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO000OOOO00O0O ).json ()#line:656
            if 'status'in O00O0O000OOO0O000 :#line:658
                if O00O0O000OOO0O000 ['status']==200 :#line:659
                    if O00O0O000OOO0O000 ['data']['amount']:#line:660
                        OOOOOO0000OO0000O =O00O0O000OOO0O000 ['data']['amount']['gold']#line:661
                        return OOOOOO0000OO0000O #line:662
                    else :#line:663
                        return 0 #line:664
        except Exception as O0O0OOOO0O000OOOO :#line:665
            print (O0O0OOOO0O000OOOO )#line:666
    def certification (O0OO00OOO0O0OO00O ):#line:669
        try :#line:670
            OOOOOOO0O0OO00000 =f'__{timi_new()}'#line:671
            O000OO000O0O00O00 ={'source':'scsc','authorization':O0OO00OOO0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O0OO00000 ),'signstring':OOOOOOO0O0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:682
            OO00OO00O0OO00O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000OO000O0O00O00 ).json ()#line:683
            if 'status'in OO00OO00O0OO00O0O :#line:685
                if OO00OO00O0OO00O0O ['status']==200 :#line:686
                    if OO00OO00O0OO00O0O ['data']['result']:#line:687
                        OO000O00O0OO00000 =OO00OO00O0OO00O0O ['data']['nick_name']#line:688
                        return OO000O00O0OO00000 #line:689
                    else :#line:690
                        return '未实名'#line:691
        except Exception as OOOOO0O0O0OO0O0O0 :#line:692
            print (OOOOO0O0O0OO0O0O0 )#line:693
    def crops_illustrated (OOO000OOO00O0O00O ):#line:696
        try :#line:697
            OOO0OO00O0000OOO0 =f'__{timi_new()}'#line:698
            O0O00O0OO000O0O0O ={'source':'scsc','authorization':OOO000OOO00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0000OOO0 ),'signstring':OOO0OO00O0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:709
            O0O0O0OO0OOOO0O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00O0OO000O0O0O ).json ()#line:710
            if 'status'in O0O0O0OO0OOOO0O00 :#line:712
                if O0O0O0OO0OOOO0O00 ['status']==200 :#line:713
                    O00OO0O00O0OOO000 =O0O0O0OO0OOOO0O00 ['data'][0 ]['crops']#line:714
                    for O0000000O000O0OO0 in O00OO0O00O0OOO000 :#line:715
                        if O0000000O000O0OO0 ['ill_clover_award']:#line:716
                            if float (O0000000O000O0OO0 ['ill_clover_award'])>1 :#line:717
                                if O0000000O000O0OO0 ['is_finish']:#line:718
                                    if not O0000000O000O0OO0 ['is_getit']:#line:719
                                        if OOO000OOO00O0O00O .certification ()!='未实名':#line:720
                                            OOO0OO00O0000OOO0 =f'_award_level={O0000000O000O0OO0["level"]}_{timi_new()}'#line:721
                                            O0O00O0OO000O0O0O ={'source':'scsc','authorization':OOO000OOO00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0000OOO0 ),'signstring':OOO0OO00O0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:732
                                            O0OO0OOOOO0O00000 ={"award_level":O0000000O000O0OO0 ['level']}#line:733
                                            OOO000OOOO00O0OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00O0OO000O0O0O ,json =O0OO0OOOOO0O00000 ).json ()#line:735
                                            if 'status'in OOO000OOOO00O0OO0 :#line:736
                                                if OOO000OOOO00O0OO0 ['status']==200 :#line:737
                                                    OOO0000O00O0000OO =OOO000OOOO00O0OO0 ['data']['ill_clover_award']#line:738
                                                    print (f'【图鉴奖励】:领取{O0000000O000O0OO0["crop_name"]}成就丨奖励{OOO0000O00O0000OO}☘️')#line:740
                                                if OOO000OOOO00O0OO0 ['status']==500 :#line:741
                                                    print (f'【图鉴奖励】:{OOO000OOOO00O0OO0["message"]}')#line:742
        except Exception as O000OOO0O00O0O000 :#line:743
            print (O000OOO0O00O0O000 )#line:744
    def watched_ad (O0OOOO0OO0OO0OO00 ):#line:747
        try :#line:748
            OO0OO0O0O0OOO0O00 =f'__{timi_new()}'#line:749
            OO0O00000OOO0OO0O ={'source':'scsc','authorization':O0OOOO0OO0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O0OOO0O00 ),'signstring':OO0OO0O0O0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:760
            OOO0OOOOOO00OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00000OOO0OO0O ).json ()#line:761
            if 'status'in OOO0OOOOOO00OOO0O :#line:763
                if OOO0OOOOOO00OOO0O ['status']==200 :#line:764
                    if 'offlineInfo'in OOO0OOOOOO00OOO0O ['data']:#line:765
                        time .sleep (random .randint (1 ,3 ))#line:766
                        OOOO000OOOOOO0OOO =OOO0OOOOOO00OOO0O ['data']['offlineInfo']['off_minute']#line:767
                        OOO0O000O0OOO0OOO =float (OOO0OOOOOO00OOO0O ['data']['silver'])/1000000000000 #line:768
                        time .sleep (1 )#line:769
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O00000OOO0OO0O ).json ()#line:770
                        time .sleep (2 )#line:771
                        OO00O000000O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00000OOO0OO0O ).json ()#line:772
                        if 'status'in OO00O000000O0O00O :#line:774
                            if OO00O000000O0O00O ['status']==200 :#line:775
                                OO0OOO00OO00OOO00 =float (OO00O000000O0O00O ['data']['silver'])/1000000000000 #line:776
                                O000000O0OOOO0OOO =str (OO0OOO00OO00OOO00 -OOO0O000O0OOO0OOO )[:6 ]#line:777
                                print (f'【离线奖励】:翻倍离线{OOOO000OOOOOO0OOO}分钟奖励🌱数量:{O000000O0OOOO0OOO}t粒')#line:778
        except Exception as O0000O0OOOO00OOO0 :#line:779
            print (O0000O0OOOO00OOO0 )#line:780
    def user_ad (O000O00OOOOO0O00O ):#line:783
        try :#line:784
            OOO000O00O00OOOO0 =f'__{timi_new()}'#line:785
            OO0OO00O0OOOO0O0O ={'source':'scsc','authorization':O000O00OOOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O00OOOO0 ),'signstring':OOO000O00O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:796
            OOO0O0O00OO0O0OOO =requests .request ('get',f'{host}/user/ad',headers =OO0OO00O0OOOO0O0O ).json ()#line:797
            if 'status'in OOO0O0O00OO0O0OOO :#line:799
                if OOO0O0O00OO0O0OOO ['status']==200 :#line:800
                    OO0OO0O00O0O00O00 =OOO0O0O00OO0O0OOO ['data']['max_time']#line:801
                    OOO0O0OOO00O00000 =OOO0O0O00OO0O0OOO ['data']['watch_time']#line:802
                    OOO00000O0000O0OO =OOO0O0O00OO0O0OOO ['data']['added_time']#line:803
                    print (f'【获取种子】:获取🌱剩余{OOO00000O0000O0OO + OO0OO0O00O0O00O00 - OOO0O0OOO00O00000}次丨好友提供:{OOO00000O0000O0OO}次')#line:804
                    if OOO00000O0000O0OO +OO0OO0O00O0O00O00 -OOO0O0OOO00O00000 >0 :#line:805
                        time .sleep (random .randint (16 ,19 ))#line:806
                        O0O0O00OOOOO0O000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0OO00O0OOOO0O0O ).json ()#line:807
                        if 'status'in O0O0O00OOOOO0O000 :#line:809
                            if O0O0O00OOOOO0O000 ['status']==200 :#line:810
                                OOOOO000OO0000O0O =float (O0O0O00OOOOO0O000 ['data']['silver'])/1000000000000 #line:811
                                print (f'【获取种子】:获得🌱:{int(OOOOO000OO0000O0O)}t粒')#line:812
                                return True #line:813
                            if O0O0O00OOOOO0O000 ['status']==500 :#line:814
                                O0OO00OO000000OOO =O0O0O00OOOOO0O000 ['message']#line:815
                                print (f'【获取种子】:{O0OO00OO000000OOO}')#line:816
                                return False #line:817
        except Exception as O0OOOOO0OO00OOOO0 :#line:818
            print (O0OOOOO0OO00OOOO0 )#line:819
    def synthetic (O0000000OOO00OO00 ):#line:822
        global id ,g #line:823
        try :#line:824
            OOO0OO0OO0O0OOO0O =O0000000OOO00OO00 .level_new ()#line:825
            OOO0OOOOOO0OOOOOO =random .randint (9 ,11 )#line:826
            OO0000O00OO0OO000 =f'_site=8&targetSite={OOO0OOOOOO0OOOOOO}_{timi_new()}'#line:827
            O00OOOO0O0O0OO00O ={'source':'scsc','authorization':O0000000OOO00OO00 .token ,'timestamp':timi_new (),'sign':sign (OO0000O00OO0OO000 ),'signstring':OO0000O00OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:838
            OO0OO00O0OOO0O000 ={"site":int (8 ),"targetSite":int (OOO0OOOOOO0OOOOOO )}#line:839
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO0O0O0OO00O ,json =OO0OO00O0OOO0O000 )#line:840
            while True :#line:841
                OOO0O00O00O000OO0 =f'__{timi_new()}'#line:842
                OO0O0O0OOOO00OOOO ={'source':'scsc','authorization':O0000000OOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00O000OO0 ),'signstring':OOO0O00O00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:853
                O0OOOO0OOO0OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0OOOO00OOOO ).json ()#line:854
                if 'status'in O0OOOO0OOO0OO0O0O :#line:856
                    if O0OOOO0OOO0OO0O0O ['status']==200 :#line:857
                        O0O0000000OO000O0 =O0OOOO0OOO0OO0O0O ['data']['cropList']#line:858
                        O00O00O0OOOO0OOO0 =O0OOOO0OOO0OO0O0O ['data']['gameCoreDataDBid']#line:859
                        OOO00O0OO000OOOO0 =float (O0OOOO0OOO0OO0O0O ['data']['silver'])/1000000000000 #line:860
                        O0O000O0OOOO000OO =0 #line:865
                        for O00OOOOOO0OO0O0OO in O0O0000000OO000O0 :#line:866
                            if not O00OOOOOO0OO0O0OO :#line:867
                                O0OOO0O000O00OO0O =f'_crop_id={O00O00O0OOOO0OOO0}&site={O0O000O0OOOO000OO}_{O0000000OOO00OO00.time}'#line:868
                                OO0000O00000O00O0 ={'source':'scsc','authorization':O0000000OOO00OO00 .token ,'timestamp':O0000000OOO00OO00 .time ,'sign':sign (O0OOO0O000O00OO0O ),'signstring':O0OOO0O000O00OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:878
                                OOO0OOO00OOOO000O ={"site":O0O000O0OOOO000OO ,"crop_id":O00O00O0OOOO0OOO0 }#line:879
                                O0O0O0OOO0O0O0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO0000O00000O00O0 ,data =OOO0OOO00OOOO000O ).json ()#line:880
                                time .sleep (random .randint (1 ,3 )/10 )#line:882
                                if 'status'in O0O0O0OOO0O0O0O0O :#line:883
                                    if O0O0O0OOO0O0O0O0O ['status']==200 :#line:884
                                        if O0O0O0OOO0O0O0O0O ['message']=='种子数量不足':#line:885
                                            OOO0OO0OO0O0OOO0O =O0000000OOO00OO00 .level_new ()#line:886
                                            print (f'【种植合成】:{O0O0O0OOO0O0O0O0O["message"]}')#line:887
                                            if not O0000000OOO00OO00 .user_ad ():#line:888
                                                return False #line:889
                                    if O0O0O0OOO0O0O0O0O ['status']==500 :#line:890
                                        print (f'【种植合成】:{O0O0O0OOO0O0O0O0O["message"]}')#line:891
                                        return False #line:892
                            O0O000O0OOOO000OO +=1 #line:893
                        OO00O0O0OOOO0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O0OOOO00OOOO ).json ()#line:894
                        O000000000OO00OO0 =OO00O0O0OOOO0O0O0 ['data']['cropList']#line:895
                        O0OO0OO0OO00OO0O0 =False #line:896
                        for O00OOOOOO0OO0O0OO in range (12 ):#line:897
                            id =O000000000OO00OO0 [O00OOOOOO0OO0O0OO ]['level']#line:898
                            if float (OOO0OO0OO0O0OOO0O )-float (id )>9 :#line:899
                                OOO0000O0OO00OOO0 =f'_site={O00OOOOOO0OO0O0OO}_{timi_new()}'#line:900
                                OOOO00O0OOOOOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000000OOO00OO00 .token ,'timestamp':timi_new (),'sign':sign (OOO0000O0OO00OOO0 ),'signstring':OOO0000O0OO00OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:911
                                OO00OO00O0OOO0O00 ={"site":O00OOOOOO0OO0O0OO }#line:912
                                OO00O0O0O0OOO0O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO00O0OOOOOOOO0 ,data =OO00OO00O0OOO0O00 ).json ()#line:914
                                if 'status'in OO00O0O0O0OOO0O00 :#line:915
                                    if OO00O0O0O0OOO0O00 ['status']==200 :#line:916
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:917
                            if id !=0 :#line:918
                                for O0000O00OO0OOOO0O in range (11 ):#line:919
                                    OO000OOO00O0O00OO =O0000O00OO0OOOO0O +1 #line:920
                                    g =O000000000OO00OO0 [OO000OOO00O0O00OO ]['level']#line:921
                                    if id ==g :#line:922
                                        O000000O00O0O0OO0 =O0000O00OO0OOOO0O +2 #line:923
                                        if O000000O00O0O0OO0 !=O00OOOOOO0OO0O0OO +1 :#line:924
                                            OOOO00OO0OO00OOO0 =O00OOOOOO0OO0O0OO +1 #line:925
                                            time .sleep (random .randint (1 ,3 )/10 )#line:927
                                            OO0000O00OO0OO000 =f'_site={OOOO00OO0OO00OOO0 - 1}&targetSite={O000000O00O0O0OO0 - 1}_{timi_new()}'#line:928
                                            O00OOOO0O0O0OO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000000OOO00OO00 .token ,'timestamp':timi_new (),'sign':sign (OO0000O00OO0OO000 ),'signstring':OO0000O00OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:945
                                            O0OOOOOO00OO000O0 ={"site":int (OOOO00OO0OO00OOO0 -1 ),"targetSite":int (O000000O00O0O0OO0 -1 )}#line:946
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOO0O0O0OO00O ,json =O0OOOOOO00OO000O0 )#line:947
                                            O0OO0OO0OO00OO0O0 =True #line:949
                                    if O0OO0OO0OO00OO0O0 :#line:950
                                        break #line:951
                                if O0OO0OO0OO00OO0O0 :#line:952
                                    break #line:953
        except :#line:954
            O0000000OOO00OO00 .synthetic ()#line:955
    def level_new (O00O0O0OOO0OOOOO0 ):#line:958
        try :#line:959
            O00000O000O000O0O =f'__{timi_new()}'#line:960
            O00O0OOOOO0OOOO00 ={'source':'scsc','authorization':O00O0O0OOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O000O000O0O ),'signstring':O00000O000O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:971
            OO0OO0OOO0OO000OO =requests .request ('get',f'{host}/user',headers =O00O0OOOOO0OOOO00 ).json ()#line:972
            if 'status'in OO0OO0OOO0OO000OO :#line:973
                if OO0OO0OOO0OO000OO ['status']==200 :#line:974
                    return float (OO0OO0OOO0OO000OO ['data']['level'])#line:975
        except Exception as O000OO0OOO0OOOOOO :#line:976
            print (O000OO0OOO0OOOOOO )#line:977
    def propsraffle (O0O0O00OO0O00OOOO ):#line:980
        try :#line:981
            while True :#line:982
                OOO00O0OO0000OOOO =f'__{timi_new()}'#line:983
                O0OOO0O0000O0OOO0 ={'source':'scsc','authorization':O0O0O00OO0O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO0000OOOO ),'signstring':OOO00O0OO0000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:994
                O0OO0O0O0O00OO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOO0O0000O0OOO0 ).json ()#line:995
                if 'status'in O0OO0O0O0O00OO0O0 :#line:997
                    if O0OO0O0O0O00OO0O0 ['status']==200 :#line:998
                        OOOOOO000000O0O0O =O0OO0O0O0O00OO0O0 ['data']['rows']#line:999
                        OOO00000O00O00O00 =O0OO0O0O0O00OO0O0 ['data']['vstate']#line:1000
                        if OOOOOO000000O0O0O ==5 or OOOOOO000000O0O0O ==6 or OOOOOO000000O0O0O ==7 :#line:1001
                            O0O00OO0OO0O00OOO =O0OO0O0O0O00OO0O0 ['data']['silver']#line:1002
                            print (f'【转盘抽奖】:获得种子:{O0O00OO0OO0O00OOO}')#line:1003
                        if OOOOOO000000O0O0O ==1 or OOOOOO000000O0O0O ==2 or OOOOOO000000O0O0O ==3 :#line:1004
                            O0OOOOO000O0000OO =O0OO0O0O0O00OO0O0 ['data']['clover']#line:1005
                            print (f'【转盘抽奖】:获得三叶草:{O0OOOOO000O0000OO}')#line:1006
                        if OOOOOO000000O0O0O ==4 or OOOOOO000000O0O0O ==8 :#line:1007
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1008
                        if OOOOOO000000O0O0O =='抽奖次数已用完':#line:1012
                            break #line:1046
                time .sleep (random .randint (8 ,15 )/10 )#line:1047
        except Exception as OO0OOO000O00OO0O0 :#line:1048
            print (OO0OOO000O00OO0O0 )#line:1049
    def friends_invitation (O0OO00OOOOOO0OOO0 ):#line:1052
        try :#line:1053
            OOO00OO0OOOO0OO0O =f'__{timi_new()}'#line:1054
            OOO00OOOOOOOOOOO0 ={'source':'scsc','authorization':O0OO00OOOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOOO0OO0O ),'signstring':OOO00OO0OOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1065
            OOOO0O000O0O0O0O0 =requests .request ('get',f'{host}/friends',headers =OOO00OOOOOOOOOOO0 ).json ()#line:1066
            if 'status'in OOOO0O000O0O0O0O0 :#line:1067
                if OOOO0O000O0O0O0O0 ['status']==200 :#line:1068
                    OO0OOO0OO0O0O00OO =OOOO0O000O0O0O0O0 ['data']['myInviteter']#line:1069
                    if OO0OOO0OO0O0O00OO :#line:1070
                        O000O0O0OOOO0OO00 =OO0OOO0OO0O0O00OO ['user']['nickname']#line:1071
                        O0O000O0O0O0O0OO0 =O0OO00OOOOOO0OOO0 .certification ()#line:1072
                        if O0O000O0O0O0O0OO0 =='未实名':#line:1073
                            weishim .append (O0OO00OOOOOO0OOO0 .token )#line:1074
                        print (f'【查邀请人】:我的邀请人:{O000O0O0OOOO0OO00}丨实名:{O0O000O0O0O0O0OO0}')#line:1075
        except Exception as OOOOOOOOO0O0O000O :#line:1079
            print (OOOOOOOOO0O0O000O )#line:1080
    def add_clover (OOO0OO00000O0O00O ):#line:1083
        global golden_seed #line:1084
        try :#line:1085
            O0O00O0O000O000OO =f'__{timi_new()}'#line:1086
            O00OOO0OO00O00OOO ={'source':'scsc','authorization':OOO0OO00000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000O000OO ),'signstring':O0O00O0O000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1097
            O0O0O000000O0000O =requests .request ('get',f'{host}/assets/clovers',headers =O00OOO0OO00O00OOO ).json ()#line:1098
            if 'status'in O0O0O000000O0000O :#line:1100
                if O0O0O000000O0000O ['status']==200 :#line:1101
                    OOOOOOO0000O00O0O =O0O0O000000O0000O ['data']['clover']#line:1102
                    O0OO0O0OOOO0OO000 =O0O0O000000O0000O ['data']['used_clover']#line:1103
                    OO0OO0O0OO00OOO00 =float (OOOOOOO0000O00O0O )-float (O0OO0O0OOOO0OO000 )#line:1104
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0O0OOOO0OO000}')#line:1105
                    if OOO0OO00000O0O00O .certification ()!='未实名':#line:1106
                        if OO0OO0O0OO00OOO00 >1 :#line:1107
                            O0O00O0O000O000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO0O0OO00OOO00)}_{timi_new()}'#line:1108
                            OO0OOO0OO0O00OOO0 ={'source':'scsc','authorization':OOO0OO00000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000O000OO ),'signstring':O0O00O0O000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1119
                            OO00O00000000O0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO0O0OO00OOO00 )}#line:1120
                            O00O0O0OO00OO00O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0OO0O00OOO0 ,data =OO00O00000000O0OO ).json ()#line:1121
                            if 'status'in O00O0O0OO00OO00O0 :#line:1123
                                if O00O0O0OO00OO00O0 ['status']==200 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O00O0O0OO00OO00O0["data"]["isSuccess"]}丨数量:{OO0OO0O0OO00OOO00}')#line:1125
                                if O00O0O0OO00OO00O0 ['status']==500 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O00O0O0OO00OO00O0["message"]}')#line:1127
            O000OOOO00O000O0O =requests .request ('get',f'{host}/lottery',headers =O00OOO0OO00O00OOO ).json ()#line:1128
            O0OOOO00OO0OOOO0O =OOO0OO00000O0O00O .winning_rewards ()#line:1130
            if 'status'in O000OOOO00O000O0O :#line:1131
                if O000OOOO00O000O0O ['status']==200 :#line:1132
                    O0O0OO00O00OOO0OO =O000OOOO00O000O0O ['data'][0 ]['day_get_gold_quantity']#line:1133
                    golden_seed +=float (O0O0OO00O00OOO0OO )#line:1134
                    OOOO000O0OO000OO0 =O000OOOO00O000O0O ['data'][1 ]['value']#line:1135
                    O0000OO000O0000OO =O000OOOO00O000O0O ['data'][0 ]['join_number']#line:1136
                    OOO0000000OO0OOOO =int (float (O000OOOO00O000O0O ['data'][0 ]['totalValue']))#line:1137
                    O0O0O0OO00000O000 =float (OOOO000O0OO000OO0 /OOO0000000OO0OOOO )*10000 #line:1138
                    OO000OO0OO0OO0O00 =OOO0000000OO0OOOO /O0000OO000O0000OO #line:1139
                    print (f'【参与抽奖】:预计每天中{str(O0O0OO00O00OOO0OO)[:6]}颗金种子丨好友收益:{str(O0OOOO00OO0OOOO0O)[:6]}')#line:1140
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0O0OO00000O000)[:6]}颗金种子丨☘️人均:{str(OO000OO0OO0OO0O00)[:7]}️')#line:1141
        except Exception as OO00OOO0O00OO00OO :#line:1142
            print (OO00OOO0O00OO00OO )#line:1143
    def energy (OOOOOOO0O00OOO0O0 ):#line:1146
        try :#line:1147
            while True :#line:1148
                O0O0OO00OO00O0O00 =f'__{timi_new()}'#line:1149
                OOOO00O00O000O00O ={'source':'scsc','authorization':OOOOOOO0O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OO00O0O00 ),'signstring':O0O0OO00OO00O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1160
                OOO0O0OOOO0000O0O =requests .request ('get',f'{host}/energy/general',headers =OOOO00O00O000O00O ).json ()#line:1161
                if 'status'in OOO0O0OOOO0000O0O :#line:1163
                    if OOO0O0OOOO0000O0O ['status']==200 :#line:1164
                        O0O0O00O0OOOOO00O =OOO0O0OOOO0000O0O ['data']['ordinary_water']#line:1165
                        OOOOO00O0OOO00000 =OOO0O0OOOO0000O0O ['data']['ordinary_fertilizer']#line:1166
                        OOO000000OOOO0OOO =OOO0O0OOOO0000O0O ['data']['videoStatus']#line:1167
                        OO00OOOOOOOO0000O =OOO0O0OOOO0000O0O ['data']['waterVideoKey']#line:1168
                        print (f'【我的营养】:肥料:{str(OOOOO00O0OOO00000).split(".")[0]}丨水滴:{str(O0O0O00O0OOOOO00O).split(".")[0]}')#line:1170
                        if float (OOOOO00O0OOO00000 )<96 :#line:1171
                            if OOO000000OOOO0OOO :#line:1172
                                time .sleep (random .randint (160 ,180 )/10 )#line:1173
                                OO0O0OOO000OOO00O =99 -float (OOOOO00O0OOO00000 )#line:1174
                                O0OO00OOO00OOOOOO ={"fertilizer":str (OO0O0OOO000OOO00O ).split ('.')[0 ]}#line:1175
                                OO000O0O00OOOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO00O00O000O00O ).json ()#line:1177
                                if 'status'in OO000O0O00OOOOOO0 :#line:1179
                                    if OO000O0O00OOOOOO0 ['status']==200 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O0O00OOOOOO0["message"]}')#line:1181
                                    if OO000O0O00OOOOOO0 ['status']==500 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O0O00OOOOOO0["message"]}')#line:1183
                                        break #line:1184
                                if float (OOOOO00O0OOO00000 )<78 :#line:1186
                                    OO0O0OOO000OOO00O =80 -float (OOOOO00O0OOO00000 )#line:1187
                                    OOOOO0OO0OO0O0O00 =f'_fertilizer={int(OO0O0OOO000OOO00O)}_{timi_new()}'#line:1188
                                    OO0O0OO00OO000OO0 ={'source':'scsc','authorization':OOOOOOO0O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0OO0O0O00 ),'signstring':OOOOO0OO0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1199
                                    O00000O00OO00OOOO ={"fertilizer":int (OO0O0OOO000OOO00O )}#line:1200
                                    O0O00OOOOOO00O00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O0OO00OO000OO0 ,data =O00000O00OO00OOOO ).json ()#line:1202
                                    if 'status'in O0O00OOOOOO00O00O :#line:1204
                                        if O0O00OOOOOO00O00O ['status']==200 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{O0O00OOOOOO00O00O["message"]}丨数量:{int(OO0O0OOO000OOO00O)}')#line:1206
                                        if O0O00OOOOOO00O00O ['status']==500 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O0O00OOOOOO00O00O["message"]}丨数量:{int(OO0O0OOO000OOO00O)}')#line:1208
                                            OO0O0OOOOOO0O0000 =O0O00OOOOOO00O00O ["message"].split ('-')[1 ]#line:1209
                                            OOO0O0000OO000000 =f'__{timi_new()}'#line:1210
                                            O00OOO000OOOO0000 ={'source':'scsc','authorization':OOOOOOO0O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OO000000 ),'signstring':OOO0O0000OO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1221
                                            O00O0O0OOOO00000O =requests .request ('get',f'{host}/user',headers =O00OOO000OOOO0000 ).json ()#line:1222
                                            if 'status'in O00O0O0OOOO00000O :#line:1223
                                                if O00O0O0OOOO00000O ['status']==200 :#line:1224
                                                    O00OO0OOO0000OOOO =O00O0O0OOOO00000O ['data']['inner_id']#line:1225
                                                    if give_gold (O00OO0OOO0000OOOO ,float (OO0O0OOOOOO0O0000 )+1 ):#line:1226
                                                        OOOOOOO0O00OOO0O0 .energy ()#line:1227
                        if float (O0O0O00O0OOOOO00O )<880 :#line:1228
                            if OO00OOOOOOOO0000O :#line:1229
                                time .sleep (random .randint (160 ,180 )/10 )#line:1230
                                O0O0O0OOO00OO0O0O =999 -float (O0O0O00O0OOOOO00O )#line:1231
                                OOO0O0O000OO0OO00 ={"water":str (O0O0O0OOO00OO0O0O ).split ('.')[0 ]}#line:1232
                                OO00OO00O0000OO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO00O00O000O00O ).json ()#line:1234
                                if 'status'in OO00OO00O0000OO0O :#line:1236
                                    if OO00OO00O0000OO0O ['status']==200 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OO00OO00O0000OO0O["message"]}')#line:1238
                                    if OO00OO00O0000OO0O ['status']==500 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OO00OO00O0000OO0O["message"]}')#line:1240
                                        break #line:1241
                                if float (O0O0O00O0OOOOO00O )<780 :#line:1242
                                    O0O0O0OOO00OO0O0O =800 -float (O0O0O00O0OOOOO00O )#line:1243
                                    OOO00O0OOOO0000OO =f'_water={int(O0O0O0OOO00OO0O0O)}_{timi_new()}'#line:1244
                                    O0OOOOO00O00O0O00 ={'source':'scsc','authorization':OOOOOOO0O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO0000OO ),'signstring':OOO00O0OOOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1255
                                    OO0OOO0OOOO00O0OO ={"water":int (O0O0O0OOO00OO0O0O )}#line:1256
                                    OOO00OO000OO00000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOOOO00O00O0O00 ,data =OO0OOO0OOOO00O0OO ).json ()#line:1258
                                    if 'status'in OOO00OO000OO00000 :#line:1260
                                        if OOO00OO000OO00000 ['status']==200 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{OOO00OO000OO00000["message"]}丨数量:{int(O0O0O0OOO00OO0O0O)}')#line:1262
                                        if OOO00OO000OO00000 ['status']==500 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{OOO00OO000OO00000["message"]}丨数量:{int(O0O0O0OOO00OO0O0O)}')#line:1264
                                            OO0O0OOOOOO0O0000 =OOO00OO000OO00000 ["message"].split ('-')[1 ]#line:1265
                                            OOO0O0000OO000000 =f'__{timi_new()}'#line:1266
                                            O00OOO000OOOO0000 ={'source':'scsc','authorization':OOOOOOO0O00OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OO000000 ),'signstring':OOO0O0000OO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1277
                                            O00O0O0OOOO00000O =requests .request ('get',f'{host}/user',headers =O00OOO000OOOO0000 ).json ()#line:1278
                                            if 'status'in O00O0O0OOOO00000O :#line:1279
                                                if O00O0O0OOOO00000O ['status']==200 :#line:1280
                                                    O00OO0OOO0000OOOO =O00O0O0OOOO00000O ['data']['inner_id']#line:1281
                                                    if give_gold (O00OO0OOO0000OOOO ,float (OO0O0OOOOOO0O0000 )+1 ):#line:1282
                                                        OOOOOOO0O00OOO0O0 .energy ()#line:1283
                        break #line:1284
        except Exception as O0O00O000O0OOOOO0 :#line:1285
            print (O0O00O000O0OOOOO0 )#line:1286
def bundled_def ():#line:1289
    O0OOOOO000O00O000 =['5570536','7750212','7911652','7911680','7805624']#line:1290
    return O0OOOOO000O00O000 [random .randint (0 ,len (O0OOOOO000O00O000 )-1 )]#line:1291
def version_of_the_validation ():#line:1295
    return str ((102 -56 )/10 )#line:1296
def ubbbf ():#line:1298
    print ('卡密验证通过   ✅')#line:1299
def sc2 ():#line:1302
    return "19319#$%^&*((*"#line:1303
def OO00OO0OO0OO00OO00o0 ():#line:1306
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1308
def get_ip ():#line:1311
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1313
def gitee_validation ():#line:1316
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1317
def gitee_edition ():#line:1320
    try :#line:1321
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1322
    except :#line:1323
        sys .exit (0 )#line:1324
def O000OO000O0O00OOO00 ():#line:1328
    try :#line:1329
        OOO0OOOO000OOOOOO =gitee_edition ()#line:1330
        if version_of_the_validation ()<OOO0OOOO000OOOOOO ['CityEarth']['edition']:#line:1331
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOOO000OOOOOO["CityEarth"]["edition"]}   ❌')#line:1332
            print (f'更新内容=>>{OOO0OOOO000OOOOOO["CityEarth"]["content"]}')#line:1333
        else :#line:1334
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOOO000OOOOOO["CityEarth"]["edition"]}   ✅')#line:1335
            print (f'更新内容=>> {OOO0OOOO000OOOOOO["CityEarth"]["content"]}')#line:1336
    except Exception as O0000OO00O0O000OO :#line:1337
        print (O0000OO00O0O000OO )#line:1338
def sc3 ():#line:1341
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1342
if __name__ =='__main__':#line:1345
    start ()#line:1346
