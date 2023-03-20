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
@ 版本  4.8
"""
##################################配置区##################################
time_xx = random.randint(8, 15)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.4195543511'#line:1
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
        OOO00O0O0O0O0OO0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOO00O0O0O0O0OO0O)}个账号==========")#line:17
        for OO0000O0OO00O00O0 in OOO00O0O0O0O0OO0O :#line:18
            OOO0OOO0OO00O000O =[]#line:19
            print (f"------------正在执行第{OOO00O0O0O0O0OO0O.index(OO0000O0OO00O00O0) + 1}个账号------------")#line:20
            O0000O0O0O00O000O =CityEarth (OO0000O0OO00O00O0 ,OOO0OOO0OO00O000O ,OOO00O0O0O0O0OO0O .index (OO0000O0OO00O00O0 ))#line:21
            def O00O0OO0OOOOOO00O ():#line:23
                if O0000O0O0O00O000O .base_info ():#line:25
                    O0000O0O0O00O000O .sealing ()#line:27
                    O0000O0O0O00O000O .invitenum ()#line:29
                    O0000O0O0O00O000O .query_to_sell ()#line:31
                    O0000O0O0O00O000O .friends_invitation ()#line:35
                    O0000O0O0O00O000O .energy ()#line:37
                    O0000O0O0O00O000O .add_clover ()#line:39
                    O0000O0O0O00O000O .propsraffle ()#line:41
                    O0000O0O0O00O000O .synthetic ()#line:43
                    O0000O0O0O00O000O .crops_illustrated ()#line:45
                    O0000O0O0O00O000O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0000O0O0O00O000O .give_gold ()#line:50
            O0OO0000O0OO00O00 =threading .Thread (target =O00O0OO0OOOOOO00O )#line:52
            O0OO0000O0OO00O00 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0O00000000OO0O00 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O00000000OO0O00 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO000OO00O0OOOOO in invited_new :#line:62
            print (OOO000OO00O0OOOOO )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0O000O000O0O00O in weishim :#line:65
            print (OO0O000O000O0O00O )#line:66
    except Exception as OOO0O00O00O000O00 :#line:67
        print (OOO0O00O00O000O00 )#line:68
def give_gold (OO0OO0O00OOOOO0OO ,OOO0OOO00O00O00O0 ):#line:72
    try :#line:73
        OO0OO00O000O0O0OO =f'_doneeNo={OO0OO0O00OOOOO0OO}&quantity={int(OOO0OOO00O00O00O0)}_{timi_new()}'#line:74
        OOOO0OO00O000000O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0OO00O000O0O0OO ),'signstring':OO0OO00O000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O00OOOO00O00O0000 ={"quantity":int (OOO0OOO00O00O00O0 ),"doneeNo":OO0OO0O00OOOOO0OO }#line:89
        O0O0O0000000OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0OO00O000000O ,data =O00OOOO00O00O0000 ).json ()#line:90
        if 'status'in O0O0O0000000OO00O :#line:92
            if O0O0O0000000OO00O ['status']==200 :#line:93
                if O0O0O0000000OO00O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO0OOO00O00O00O0)}种子给{OO0OO0O00OOOOO0OO}成功')#line:95
                    return True #line:96
            if O0O0O0000000OO00O ['status']==401 :#line:97
                print (f'【赠送种子】:{O0O0O0000000OO00O["message"]}')#line:98
                return False #line:99
            if O0O0O0000000OO00O ['status']==500 :#line:100
                print (f'【赠送种子】:{O0O0O0000000OO00O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O000O0OOO0OO0OO0O :#line:104
        print (O000O0OOO0OO0OO0O )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OO00O00O000000O ):#line:115
    OOOOO00000O00O00O =hashlib .md5 (O0OO00O00O000000O .encode ()).hexdigest ()#line:116
    OOOO00O00O0O0OO00 =sc1 ()#line:117
    O0O00O0OOOOOO0O0O =sc2 ()#line:118
    O00OOOOO0OO0OO0O0 =sc3 ()#line:119
    OO0O0O0000000O000 =OOOO00O00O0O0OO00 +OOOOO00000O00O00O +O0O00O0OOOOOO0O0O +O00OOOOO0OO0OO0O0 #line:120
    O0O0000000000000O =hashlib .md5 (OO0O0O0000000O000 .encode ()).hexdigest ()#line:121
    return O0O0000000000000O #line:122
def format_msg ():#line:125
    OOOO0O0OOO0O0OO0O =""#line:126
    for O0O0OOO00O00O0O0O in msg_list :#line:127
        OOOO0O0OOO0O0OO0O +=str (O0O0OOO00O00O0O0O )+"\r\n"#line:128
    return OOOO0O0OOO0O0OO0O #line:129
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
def get_json_data (O0OOOO000000O0O0O ,O00O000000OO0O0O0 ,OOOOOOO0O0OOOO0O0 ,OOO0OOO00O00OOOOO ):#line:153
    with open (O0OOOO000000O0O0O ,'rb')as O0O0OOO0OOOO0O00O :#line:154
        OOO0000000O00000O =json .load (O0O0OOO0OOOO0O00O )#line:155
        OOO0000000O00000O ['data'][O00O000000OO0O0O0 ][OOOOOOO0O0OOOO0O0 ]=OOO0OOO00O00OOOOO #line:156
        O0OO0O000OOOO0OOO =OOO0000000O00000O #line:157
    O0O0OOO0OOOO0O00O .close ()#line:158
    return O0OO0O000OOOO0OOO #line:159
def write_json_data (OO0OOOO0OOO0O0000 ):#line:162
    with open (json_path1 ,'w')as OOO00O0O0O0000O0O :#line:163
        json .dump (OO0OOOO0OOO0O0000 ,OOO00O0O0O0000O0O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OOO00O0O0O0000O0O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O00O00OO0O000O00O ,O000000OO0O000O00 ,O0OO00O00O000OOO0 ,O0O00O0O0OO0O0OO0 ):#line:171
        try :#line:172
            O00O00OO0O000O00O .msg =O0OO00O00O000OOO0 #line:173
            O00O00OO0O000O00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O00O00OO0O000O00O .token =O000000OO0O000O00 ['authorization']#line:175
            O00O00OO0O000O00O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O00O00OO0O000O00O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O00O00OO0O000O00O .elephant_user =O000000OO0O000O00 ['elephant_user']#line:178
            O00O00OO0O000O00O .elephant_pswd =O000000OO0O000O00 ['elephant_pswd']#line:179
            O00O00OO0O000O00O .elephant_Task_ID =O000000OO0O000O00 ['elephant_Task_ID']#line:180
            O00O00OO0O000O00O .len_new =O0O00O0O0OO0O0OO0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O0O0O00O0OOO00O ):#line:186
        try :#line:187
            O0O0O0O00O0OOO00O .watched_ad ()#line:189
            O0O0O0O0000O0O0O0 =f'__{timi_new()}'#line:190
            OOOO00000O000O0O0 ={'source':'scsc','authorization':O0O0O0O00O0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0000O0O0O0 ),'signstring':O0O0O0O0000O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOO00O000O0O0O00 =requests .request ('get',f'{host}/user',headers =OOOO00000O000O0O0 ).json ()#line:202
            if 'status'in OOOO00O000O0O0O00 :#line:204
                if OOOO00O000O0O0O00 ['status']==200 :#line:205
                    O00O0O00O00O0OOO0 =OOOO00O000O0O0O00 ['data']['nickname']#line:206
                    O00OOOO000O00O0O0 =OOOO00O000O0O0O00 ['data']['inner_id']#line:207
                    O0O0O00OO0O000O00 =OOOO00O000O0O0O00 ['data']['assets']['gold']#line:208
                    OOOOO0OOO0000O0O0 =OOOO00O000O0O0O00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00O0O00O00O0OOO0[:5]}丨ID:{O00OOOO000O00O0O0}丨等级:{OOOOO0OOO0000O0O0}丨金种子:{str(O0O0O00OO0O000O00).split(".")[0]}')#line:211
                    if 'wx_'in O00O0O00O00O0OOO0 :#line:212
                        O0O0O0O00O0OOO00O .change_nickname ()#line:213
                if OOOO00O000O0O0O00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O0O0O00O0OOO00O .elephant_user =='f':#line:216
                        return False #line:217
                    OO0OO00O0O00O00O0 =Invalid_login .addtask (elephant_user =O0O0O0O00O0OOO00O .elephant_user ,elephant_pswd =O0O0O0O00O0OOO00O .elephant_pswd ,elephant_Task_ID =O0O0O0O00O0OOO00O .elephant_Task_ID )#line:220
                    OO0O0OO00O00OOO00 =get_json_data (json_path ,O0O0O0O00O0OOO00O .len_new ,'authorization',OO0OO00O0O00O00O0 )#line:221
                    if write_json_data (OO0O0OO00O00OOO00 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOO00O000O0O0O00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O00O0O0O0O00000OO :#line:228
            print (O00O0O0O0O00000OO )#line:229
    def sealing (O0OO0OOO00OO00O00 ):#line:232
        try :#line:233
            O0O000OOOOO00000O =f'__{timi_new()}'#line:234
            O0OO00O0O0000OOOO ={'source':'scsc','authorization':O0OO0OOO00OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOOO00000O ),'signstring':O0O000OOOOO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO00O0O0000OOOO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OO00O0O0000OOOO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO00O0O0000OOOO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO00O0O0000OOOO )#line:249
            requests .request ('get',f'{host}/user',headers =O0OO00O0O0000OOOO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO00O0O0000OOOO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO00O0O0000OOOO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO00O0O0000OOOO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O0O0000OOOO )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OO00O0O0000OOOO )#line:255
        except Exception as O0O00OO0OOO0O0O0O :#line:256
            print (O0O00OO0OOO0O0O0O )#line:257
    def ddd (OO0OOO000OO00OO00 ):#line:259
        try :#line:260
            O0OO0O0OOO0O000O0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0O00O0OO000O0O00 ={'source':'scsc','authorization':OO0OOO000OO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOO0O000O0 ),'signstring':O0OO0O0OOO0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0O0000O00O0O0OO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O00O0OO000O0O00 ).json ()#line:273
            print (O0O0000O00O0O0OO0 )#line:274
        except Exception as OO000O0O0OO0OO0OO :#line:277
            print (OO000O0O0OO0OO0OO )#line:278
    def the_query (OO000O0000O000O0O ):#line:283
        try :#line:284
            OO000O0O0OOOO00OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O00O00O0000O00OO0 ={'authorization':OO000O0000O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OOOO00OO ),'signstring':OO000O0O0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO0000O000OOO0O00 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00O00O0000O00OO0 ).json ()#line:296
            if 'status'in OO0000O000OOO0O00 :#line:298
                if OO0000O000OOO0O00 ['status']==200 :#line:299
                    return OO0000O000OOO0O00 ['data']['rows'][4 ]['price']#line:300
        except Exception as O0O00000O0OOOO00O :#line:301
            print (O0O00000O0OOOO00O )#line:302
    def market_sale (O0OO0000OOOO00000 ,O0OO0O0000OOOOOO0 ):#line:305
        try :#line:306
            OOOOOO0OOO0OOOO00 =timi_new ()#line:307
            O0OO00000O00O0O00 =f'type=crop__{OOOOOO0OOO0OOOO00}'#line:308
            OO0000OOO0OOOO00O ={'source':'scsc','authorization':O0OO0000OOOO00000 .token ,'timestamp':str (OOOOOO0OOO0OOOO00 ),'sign':sign (O0OO00000O00O0O00 ),'signstring':O0OO00000O00O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OO0OO00OOOO000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0000OOO0OOOO00O ).json ()#line:320
            if 'status'in O0OO0OO00OOOO000O :#line:322
                if O0OO0OO00OOOO000O ['status']==200 :#line:323
                    if O0OO0OO00OOOO000O ['data']['rows']:#line:324
                        OOOOO0O00OO0O0O00 =O0OO0OO00OOOO000O ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOO00000000OOOO0O =O0OO0OO00OOOO000O ['data']['rows'][0 ]['quantity']#line:326
                        if float (O0OO0O0000OOOOOO0 )>6 :#line:327
                            O0O000OOO0OOOO000 =f'_packsackItemId={OOOOO0O00OO0O0O00}&price={str(O0OO0O0000OOOOOO0)[:5]}&quantity={OOO00000000OOOO0O}_{OOOOOO0OOO0OOOO00}'#line:328
                            O0OO00O0000O00O0O ={'source':'scsc','authorization':O0OO0000OOOO00000 .token ,'timestamp':str (OOOOOO0OOO0OOOO00 ),'sign':sign (O0O000OOO0OOOO000 ),'signstring':O0O000OOO0OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            O0OOOOO0OO0OOOOOO ={"packsackItemId":OOOOO0O00OO0O0O00 ,"price":str (O0OO0O0000OOOOOO0 )[:5 ],"quantity":str (OOO00000000OOOO0O )}#line:344
                            O0O00O0OOO000OO00 =requests .request ('post',f'{host}/market/sale',headers =O0OO00O0000O00O0O ,data =O0OOOOO0OO0OOOOOO ).json ()#line:345
                            if 'status'in O0O00O0OOO000OO00 :#line:347
                                if O0O00O0OOO000OO00 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OOO00000000OOOO0O}丨价格:{str(O0OO0O0000OOOOOO0)[:5]}')#line:349
                                if O0O00O0OOO000OO00 ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O0O00O0OOO000OO00["message"]}')#line:351
        except Exception as OOO0OOO00O0OO0O0O :#line:352
            print (OOO0OOO00O0OO0O0O )#line:353
    def query_to_sell (O0O00O0OO0O0OOO00 ):#line:356
        global count_list #line:357
        try :#line:358
            O0O00OOO00OOOOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOOO0OOO0O000OOO0 ={'source':'scsc','authorization':O0O00O0OO0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OOOOOOO ),'signstring':O0O00OOO00OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O00O00OO0O0O000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOO0OOO0O000OOO0 ).json ()#line:371
            if 'status'in O00O00OO0O0O000O0 :#line:373
                if O00O00OO0O0O000O0 ['status']==200 :#line:374
                    for OO0OOOO000OO00000 in O00O00OO0O0O000O0 ['data']['rows']:#line:375
                        OO0O00O0O0O00OOOO =OO0OOOO000OO00000 ['materialKey']#line:376
                        O000OOO0O0000O00O =OO0OOOO000OO00000 ['quantity']#line:377
                        O00OOOO00O0OOO00O =OO0OOOO000OO00000 ['price']#line:378
                        O0OO000O00OO0OOO0 =OO0OOOO000OO00000 ['saleState']#line:379
                        if O0OO000O00OO0OOO0 ==0 :#line:380
                            print (f'【出售订单】:名称:{OO0O00O0O0O00OOOO}丨数量:{O000OOO0O0000O00O}丨价格:{O00OOOO00O0OOO00O}')#line:381
                            count_list +=O000OOO0O0000O00O #line:382
                            O0O000OOO0OO0OO0O =O0O00O0OO0O0OOO00 .the_query ()#line:384
                            if float (O0O000OOO0OO0OO0O )!=float (O00OOOO00O0OOO00O ):#line:385
                                O000O0000000OO00O =OO0OOOO000OO00000 ['id']#line:386
                                O0O00O0OO0O0OOO00 .cacel_sale (O000O0000000OO00O )#line:387
                    O0O00O0OO0O0OOO00 .game_map ()#line:389
        except Exception as OOOO000OOO00OO0O0 :#line:391
            print (OOOO000OOO00OO0O0 )#line:392
    def cacel_sale (O0O0O00O0O0O00000 ,O0O00O00OO0OOOO00 ):#line:395
        try :#line:396
            O0O0OOOOO00OOO0OO =f'_saleId={O0O00O00OO0OOOO00}_{timi_new()}'#line:397
            O00000O0OO0000O00 ={'source':'scsc','authorization':O0O0O00O0O0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOO00OOO0OO ),'signstring':O0O0OOOOO00OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OO00O00O0O000O0OO ={"saleId":O0O00O00OO0OOOO00 }#line:409
            OOOOO00O0OOOO0OOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00000O0OO0000O00 ,data =OO00O00O0O000O0OO ).json ()#line:410
            if 'status'in OOOOO00O0OOOO0OOO :#line:412
                if OOOOO00O0OOOO0OOO ['status']==200 :#line:413
                    print (f'【下架出售】:{OOOOO00O0OOOO0OOO["data"]}')#line:414
        except Exception as O000000OO0O0OOOO0 :#line:415
            print (O000000OO0O0OOOO0 )#line:416
    def change_nickname (OO000O00O000OOO00 ):#line:419
        try :#line:420
            OO0OO0O00OOOO0OOO =timi_new ()#line:421
            O0O00O0000OO0OO0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OO00O0OOOOOOO0O00 =requests .request ('post','https://www.qmsjmfb.com/',data =O0O00O0000OO0OO0O ).text #line:423
            OO0000OOO00OOO0O0 =re .findall ('<ul><li>(.*?)</li>',OO00O0OOOOOOO0O00 )[0 ][:3 ]#line:424
            OOOOO0O00O0O0OO0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0000OOO00OOO0O0}').json ()#line:425
            OO0OOOOOOOO0OOOO0 =OOOOO0O00O0O0OO0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            OO0000O00O000O0O0 ={"nickname":OO0OOOOOOOO0OOOO0 }#line:427
            O0OOOOO0O00OO00OO =f'_nickname={OO0OOOOOOOO0OOOO0}_{OO0OO0O00OOOO0OOO}'#line:428
            O0OO0OOOOOOO0O0O0 ={'source':'scsc','authorization':OO000O00O000OOO00 .token ,'timestamp':OO0OO0O00OOOO0OOO ,'sign':sign (O0OOOOO0O00OO00OO ),'signstring':O0OOOOO0O00OO00OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OOO0O00000OO0OO0O =requests .request ('patch',f'{host}/user/nickname',headers =O0OO0OOOOOOO0O0O0 ,data =OO0000O00O000O0O0 ).json ()#line:440
            if 'status'in OOO0O00000OO0OO0O :#line:442
                if OOO0O00000OO0OO0O ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OO0OOOOOOOO0OOOO0}丨{OOO0O00000OO0OO0O["message"]}')#line:444
        except Exception as O0OO0O0O0O000OO0O :#line:445
            print (O0OO0O0O0O000OO0O )#line:446
    def withdraw (OO000O0O00O00OO0O ):#line:449
        try :#line:450
            OO000000000OO0000 =f'__{timi_new()}'#line:451
            OO0OOOOOO000OOO0O ={'source':'scsc','authorization':OO000O0O00O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000000OO0000 ),'signstring':OO000000000OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OO000O000OO0OOOOO =requests .request ('get',f'{host}/assets',headers =OO0OOOOOO000OOO0O ).json ()#line:463
            if 'status'in OO000O000OO0OOOOO :#line:465
                if OO000O000OO0OOOOO ['status']==200 :#line:466
                    O0OOO00O0000OOO0O =OO000O000OO0OOOOO ['data']['cash']#line:467
                    if float (O0OOO00O0000OOO0O )>20 :#line:468
                        OO000000000OO0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        OO0OOOOOO000OOO0O ={'authorization':OO000O0O00O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000000OO0000 ),'signstring':OO000000000OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O0O00OO0O0OO0O000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OOOO000OOO0OO000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OOOOOO000OOO0O ,data =O0O00OO0O0OO0O000 ).json ()#line:482
                        if 'status'in OOOO000OOO0OO000O :#line:484
                            if OOOO000OOO0OO000O ['status']==200 :#line:485
                                print (f'【余额提现】:{OOOO000OOO0OO000O["data"]}')#line:486
                        if 'status'in OOOO000OOO0OO000O :#line:487
                            if OOOO000OOO0OO000O ['status']==500 :#line:488
                                print (f'【余额提现】:{OOOO000OOO0OO000O["message"]}')#line:489
        except Exception as OO00000O0O000O00O :#line:490
            print (OO00000O0O000O00O )#line:491
    def invitenum (OOO0OOOO000OOO0O0 ):#line:494
        global invited_new #line:495
        try :#line:496
            OOOO0OOO00O00000O =f'__{timi_new()}'#line:497
            O0OO0O0O000OOO0O0 ={'source':'scsc','authorization':OOO0OOOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00O00000O ),'signstring':OOOO0OOO00O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            O0000OO000O0OOOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO0O0O000OOO0O0 ).json ()#line:509
            if 'status'in O0000OO000O0OOOOO :#line:511
                if O0000OO000O0OOOOO ['status']==200 :#line:512
                    OO000000000OOO00O =O0000OO000O0OOOOO ['data']['invited_count']#line:513
                    OOOOOO0O00O0OO000 =O0000OO000O0OOOOO ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OO000000000OOO00O}丨间邀好友:{OOOOOO0O00O0OO000}')#line:515
                    if OO000000000OOO00O <2 :#line:516
                        OOOOO00O0OOOOOOO0 =f'__{timi_new()}'#line:517
                        O00OO0OO0O0OO0O00 ={'source':'scsc','authorization':OOO0OOOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OOOOOOO0 ),'signstring':OOOOO00O0OOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        O00OOOO00O0OOOOOO =requests .request ('get',f'{host}/user',headers =O00OO0OO0O0OO0O00 ).json ()#line:529
                        if 'status'in O00OOOO00O0OOOOOO :#line:531
                            if O00OOOO00O0OOOOOO ['status']==200 :#line:532
                                invited_new .append (O00OOOO00O0OOOOOO ['data']['inner_id'])#line:533
        except Exception as OOO0O00O0OO0OO0OO :#line:534
            print (OOO0O00O0OO0OO0OO )#line:535
    def game_map (OO0OOOO0OOO0OO0O0 ):#line:538
        try :#line:539
            OOOOOOOOO0OOOO0O0 =f'__{timi_new()}'#line:540
            O0OOOOOOOO0O000OO ={'source':'scsc','authorization':OO0OOOO0OOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO0OOOO0O0 ),'signstring':OOOOOOOOO0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OOO0O0O000O0O0O0O =requests .request ('get',f'{host}/game/map',headers =O0OOOOOOOO0O000OO ).json ()#line:552
            if 'status'in OOO0O0O000O0O0O0O :#line:554
                if OOO0O0O000O0O0O0O ['status']==200 :#line:555
                    for OOOO000O000000OO0 in OOO0O0O000O0O0O0O ['data']['list'][0 ]['crops']:#line:556
                        O000OOOO00O00000O =OOOO000O000000OO0 ['level']#line:558
                        if O000OOOO00O00000O ==41 :#line:559
                            OO0O0O0O00OOO0O00 =OOOO000O000000OO0 ['crop_name']#line:560
                            OO00OOOO0OO000O00 =OOOO000O000000OO0 ['count']#line:561
                            if OO00OOOO0OO000O00 >0 :#line:562
                                print (f'【农业资产】:{OO0O0O0O00OOO0O00}丨数量:{OO00OOOO0OO000O00}')#line:563
                                O0OO0O000OOOO000O =OO0OOOO0OOO0OO0O0 .the_query ()#line:564
                                OO0OOOO0OOO0OO0O0 .market_sale (O0OO0O000OOOO000O )#line:565
        except Exception as O0O0OOO0OOO00OO0O :#line:566
            print (O0O0OOO0OOO00OO0O )#line:567
    def give_gold (OOO000OOOOOO0OO00 ):#line:570
        try :#line:571
            O00OOOOO00OOOO0O0 =f'__{timi_new()}'#line:572
            OOO00O0OOOO0OOO0O ={'source':'scsc','authorization':OOO000OOOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO00OOOO0O0 ),'signstring':O00OOOOO00OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOOOOOO00O000000O =requests .request ('get',f'{host}/user',headers =OOO00O0OOOO0OOO0O ).json ()#line:584
            if 'status'in OOOOOOO00O000000O :#line:585
                if OOOOOOO00O000000O ['status']==200 :#line:586
                    if float (OOO000OOOOOO0OO00 .doneeNo )!=0 :#line:587
                        OOO0OOOO00O0O0OOO =OOOOOOO00O000000O ['data']['assets']['gold']#line:588
                        if float (OOO0OOOO00O0O0OOO )>float (OOO000OOOOOO0OO00 .innerId ):#line:589
                            OOO00O0OO0OO0OO0O =int (float (OOO0OOOO00O0O0OOO )/1.1 )#line:590
                            O00OOOOO00OOOO0O0 =f'_doneeNo={OOO000OOOOOO0OO00.doneeNo}&quantity={OOO00O0OO0OO0OO0O}_{timi_new()}'#line:591
                            OOO00O0OOOO0OOO0O ={'source':'scsc','authorization':OOO000OOOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO00OOOO0O0 ),'signstring':O00OOOOO00OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OOO00O0OOO0000000 ={"quantity":OOO00O0OO0OO0OO0O ,"doneeNo":OOO000OOOOOO0OO00 .doneeNo }#line:606
                            OOOO000OOO00OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00O0OOOO0OOO0O ,data =OOO00O0OOO0000000 ).json ()#line:607
                            if 'status'in OOOO000OOO00OO00O :#line:609
                                if OOOO000OOO00OO00O ['status']==200 :#line:610
                                    if OOOO000OOO00OO00O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OOO00O0OO0OO0OO0O}种子给{OOO000OOOOOO0OO00.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OOOOO0O00O0O0OOOO :#line:615
            print (OOOOO0O00O0O0OOOO )#line:616
    def invitation (O0OO0OOOO00O0O0OO ):#line:618
        try :#line:619
            _O0OO0000O0OOOOOOO =float (bundled_def ())/4 #line:620
            O0OO000O00O000O00 =f'_innerId={int(_O0OO0000O0OOOOOOO)}_{timi_new()}'#line:622
            OO0O00O0O0O0O00OO ={'source':'scsc','authorization':O0OO0OOOO00O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O00O000O00 ),'signstring':O0OO000O00O000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            OO0O0OOOO0OOO0000 ={"innerId":int (_O0OO0000O0OOOOOOO )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O00O0O0O0O00OO ,data =OO0O0OOOO0OOO0000 )#line:635
        except Exception as OO00OO0000OOO0OOO :#line:636
            print (OO00OO0000OOO0OOO )#line:637
    def winning_rewards (O0OOO00O0O00OO000 ):#line:640
        try :#line:641
            OO0OOO0O0OO0OOO00 =f'__{timi_new()}'#line:642
            O0O00O0OO0OOOO0OO ={'source':'scsc','authorization':O0OOO00O0O00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OO0OOO00 ),'signstring':OO0OOO0O0OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OOO0000O000OO0O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O00O0OO0OOOO0OO ).json ()#line:654
            if 'status'in OOO0000O000OO0O00 :#line:656
                if OOO0000O000OO0O00 ['status']==200 :#line:657
                    if OOO0000O000OO0O00 ['data']['amount']:#line:658
                        O00O0OO0OOO000OOO =OOO0000O000OO0O00 ['data']['amount']['gold']#line:659
                        return O00O0OO0OOO000OOO #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as O000O0O00O0OOOO00 :#line:663
            print (O000O0O00O0OOOO00 )#line:664
    def certification (OOO0OO0O00OO0OOO0 ):#line:667
        try :#line:668
            OO00OOOO0O0OO00OO =f'__{timi_new()}'#line:669
            O000O0OOOOOOOO000 ={'source':'scsc','authorization':OOO0OO0O00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0O0OO00OO ),'signstring':OO00OOOO0O0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O000O00OO0O0OOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0OOOOOOOO000 ).json ()#line:681
            if 'status'in O000O00OO0O0OOO00 :#line:683
                if O000O00OO0O0OOO00 ['status']==200 :#line:684
                    if O000O00OO0O0OOO00 ['data']['result']:#line:685
                        OOO0OOOOOO00OOOO0 =O000O00OO0O0OOO00 ['data']['nick_name']#line:686
                        return OOO0OOOOOO00OOOO0 #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0O0OOO0O0000OOO0 :#line:690
            print (O0O0OOO0O0000OOO0 )#line:691
    def crops_illustrated (O0OO0O00OO0OO0OOO ):#line:694
        try :#line:695
            OOOOO0O0OO00OO000 =f'__{timi_new()}'#line:696
            O00OOOO0OO000O0OO ={'source':'scsc','authorization':O0OO0O00OO0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0OO00OO000 ),'signstring':OOOOO0O0OO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O0O000O00OOOO0OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OOOO0OO000O0OO ).json ()#line:708
            if 'status'in O0O000O00OOOO0OO0 :#line:710
                if O0O000O00OOOO0OO0 ['status']==200 :#line:711
                    OO00O0000OO000OOO =O0O000O00OOOO0OO0 ['data'][0 ]['crops']#line:712
                    for OO00OOO000O000OO0 in OO00O0000OO000OOO :#line:713
                        if OO00OOO000O000OO0 ['ill_clover_award']:#line:714
                            if float (OO00OOO000O000OO0 ['ill_clover_award'])>1 :#line:715
                                if OO00OOO000O000OO0 ['is_finish']:#line:716
                                    if not OO00OOO000O000OO0 ['is_getit']:#line:717
                                        if O0OO0O00OO0OO0OOO .certification ()!='未实名':#line:718
                                            OOOOO0O0OO00OO000 =f'_award_level={OO00OOO000O000OO0["level"]}_{timi_new()}'#line:719
                                            O00OOOO0OO000O0OO ={'source':'scsc','authorization':O0OO0O00OO0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0OO00OO000 ),'signstring':OOOOO0O0OO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0OOOOOO00OO00OOO ={"award_level":OO00OOO000O000OO0 ['level']}#line:731
                                            OOOO00O00OO000O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OOOO0OO000O0OO ,json =O0OOOOOO00OO00OOO ).json ()#line:733
                                            if 'status'in OOOO00O00OO000O0O :#line:734
                                                if OOOO00O00OO000O0O ['status']==200 :#line:735
                                                    O0O000O00O0000O0O =OOOO00O00OO000O0O ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{OO00OOO000O000OO0["crop_name"]}成就丨奖励{O0O000O00O0000O0O}☘️')#line:738
                                                if OOOO00O00OO000O0O ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OOOO00O00OO000O0O["message"]}')#line:740
        except Exception as O0000O0OO00O0O0OO :#line:741
            print (O0000O0OO00O0O0OO )#line:742
    def watched_ad (OO00O0OO00OOOO00O ):#line:745
        try :#line:746
            O0O0O0OOOO0OO0O0O =f'__{timi_new()}'#line:747
            OOO00O00O0O0O0O0O ={'source':'scsc','authorization':OO00O0OO00OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO0OO0O0O ),'signstring':O0O0O0OOOO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OO0O0OO00O0O0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O00O0O0O0O0O ).json ()#line:759
            if 'status'in OO0O0OO00O0O0OO00 :#line:761
                if OO0O0OO00O0O0OO00 ['status']==200 :#line:762
                    if 'offlineInfo'in OO0O0OO00O0O0OO00 ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OO0OO0O00000OO000 =OO0O0OO00O0O0OO00 ['data']['offlineInfo']['off_minute']#line:765
                        OOOO0OOO0OOO0O00O =float (OO0O0OO00O0O0OO00 ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO00O00O0O0O0O0O ).json ()#line:768
                        time .sleep (2 )#line:769
                        OOO00OOO0OO0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O00O0O0O0O0O ).json ()#line:770
                        if 'status'in OOO00OOO0OO0OOOO0 :#line:772
                            if OOO00OOO0OO0OOOO0 ['status']==200 :#line:773
                                OOO00OOO0O00OO000 =float (OOO00OOO0OO0OOOO0 ['data']['silver'])/1000000000000 #line:774
                                OO0O0O0O0OOOO0OOO =str (OOO00OOO0O00OO000 -OOOO0OOO0OOO0O00O )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OO0OO0O00000OO000}分钟奖励🌱数量:{OO0O0O0O0OOOO0OOO}t粒')#line:776
        except Exception as OOOOOOOO0OO0OO0O0 :#line:777
            print (OOOOOOOO0OO0OO0O0 )#line:778
    def user_ad (OO00O00OO000O00O0 ):#line:781
        try :#line:782
            O000O00OOOO0000O0 =f'__{timi_new()}'#line:783
            O0O00000O00O000OO ={'source':'scsc','authorization':OO00O00OO000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOOO0000O0 ),'signstring':O000O00OOOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O00O0O00O000OO000 =requests .request ('get',f'{host}/user/ad',headers =O0O00000O00O000OO ).json ()#line:795
            if 'status'in O00O0O00O000OO000 :#line:797
                if O00O0O00O000OO000 ['status']==200 :#line:798
                    O0000OOO00000000O =O00O0O00O000OO000 ['data']['max_time']#line:799
                    O0000OOO00O0O00OO =O00O0O00O000OO000 ['data']['watch_time']#line:800
                    O00O00O0OO0000000 =O00O0O00O000OO000 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O00O00O0OO0000000 + O0000OOO00000000O - O0000OOO00O0O00OO}次丨好友提供:{O00O00O0OO0000000}次')#line:802
                    if O00O00O0OO0000000 +O0000OOO00000000O -O0000OOO00O0O00OO >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        O0000OOOOOOO0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00000O00O000OO ).json ()#line:805
                        if 'status'in O0000OOOOOOO0OO00 :#line:807
                            if O0000OOOOOOO0OO00 ['status']==200 :#line:808
                                O0000OOOO000OO00O =float (O0000OOOOOOO0OO00 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(O0000OOOO000OO00O)}t粒')#line:810
                                return True #line:811
                            if O0000OOOOOOO0OO00 ['status']==500 :#line:812
                                OO00OO0O00OO00000 =O0000OOOOOOO0OO00 ['message']#line:813
                                print (f'【获取种子】:{OO00OO0O00OO00000}')#line:814
                                return False #line:815
        except Exception as O000O0O00000OOOOO :#line:816
            print (O000O0O00000OOOOO )#line:817
    def synthetic (O000OO000O0O000OO ):#line:820
        global id ,g #line:821
        try :#line:822
            O00O0OOO0OOOO0000 =O000OO000O0O000OO .level_new ()#line:823
            O00OOOO0O0O00OOO0 =random .randint (9 ,11 )#line:824
            O000OO0OO0000O0O0 =f'_site=8&targetSite={O00OOOO0O0O00OOO0}_{timi_new()}'#line:825
            OO0OOO00OO0OOOO00 ={'source':'scsc','authorization':O000OO000O0O000OO .token ,'timestamp':timi_new (),'sign':sign (O000OO0OO0000O0O0 ),'signstring':O000OO0OO0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            O0O0OOO00OOOOO00O ={"site":int (8 ),"targetSite":int (O00OOOO0O0O00OOO0 )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOO00OO0OOOO00 ,json =O0O0OOO00OOOOO00O )#line:838
            while True :#line:839
                O0OOOOO00O000OO0O =f'__{timi_new()}'#line:840
                OO00OO0O0O00O0O00 ={'source':'scsc','authorization':O000OO000O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00O000OO0O ),'signstring':O0OOOOO00O000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                OO0OO0OOOOO00OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O0O00O0O00 ).json ()#line:852
                if 'status'in OO0OO0OOOOO00OO00 :#line:854
                    if OO0OO0OOOOO00OO00 ['status']==200 :#line:855
                        OO000O000O000OO00 =OO0OO0OOOOO00OO00 ['data']['cropList']#line:856
                        O0000OO0000O0OOO0 =OO0OO0OOOOO00OO00 ['data']['gameCoreDataDBid']#line:857
                        OO00000OOOO00OO00 =float (OO0OO0OOOOO00OO00 ['data']['silver'])/1000000000000 #line:858
                        O00000000OOOO00O0 =0 #line:863
                        for OO000OOO00OO0OOO0 in OO000O000O000OO00 :#line:864
                            if not OO000OOO00OO0OOO0 :#line:865
                                OO0O000OO0O0O00OO =f'_crop_id={O0000OO0000O0OOO0}&site={O00000000OOOO00O0}_{O000OO000O0O000OO.time}'#line:866
                                OO0O0O0000O00OO0O ={'source':'scsc','authorization':O000OO000O0O000OO .token ,'timestamp':O000OO000O0O000OO .time ,'sign':sign (OO0O000OO0O0O00OO ),'signstring':OO0O000OO0O0O00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                OO000O00O0OO0OOOO ={"site":O00000000OOOO00O0 ,"crop_id":O0000OO0000O0OOO0 }#line:877
                                O00OO00O000O00O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O0O0000O00OO0O ,data =OO000O00O0OO0OOOO ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in O00OO00O000O00O00 :#line:881
                                    if O00OO00O000O00O00 ['status']==200 :#line:882
                                        if O00OO00O000O00O00 ['message']=='种子数量不足':#line:883
                                            O00O0OOO0OOOO0000 =O000OO000O0O000OO .level_new ()#line:884
                                            print (f'【种植合成】:{O00OO00O000O00O00["message"]}')#line:885
                                            if not O000OO000O0O000OO .user_ad ():#line:886
                                                return False #line:887
                                    if O00OO00O000O00O00 ['status']==500 :#line:888
                                        print (f'【种植合成】:{O00OO00O000O00O00["message"]}')#line:889
                                        return False #line:890
                            O00000000OOOO00O0 +=1 #line:891
                        O0OO0000O0O00O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O0O00O0O00 ).json ()#line:892
                        O00000OO0000O0OOO =O0OO0000O0O00O0O0 ['data']['cropList']#line:893
                        O0O00OO0OO000O0O0 =False #line:894
                        for OO000OOO00OO0OOO0 in range (12 ):#line:895
                            id =O00000OO0000O0OOO [OO000OOO00OO0OOO0 ]['level']#line:896
                            if float (O00O0OOO0OOOO0000 )-float (id )>9 :#line:897
                                O00OOO0O000OO0O0O =f'_site={OO000OOO00OO0OOO0}_{timi_new()}'#line:898
                                OO0O00OO000OOO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OO000O0O000OO .token ,'timestamp':timi_new (),'sign':sign (O00OOO0O000OO0O0O ),'signstring':O00OOO0O000OO0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O0000O0O0O00O0000 ={"site":OO000OOO00OO0OOO0 }#line:910
                                OOOOOO000O000OO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O00OO000OOO00O ,data =O0000O0O0O00O0000 ).json ()#line:912
                                if 'status'in OOOOOO000O000OO0O :#line:913
                                    if OOOOOO000O000OO0O ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OOO0OOO0000O00O00 in range (11 ):#line:917
                                    OO0OO0O00000O0OOO =OOO0OOO0000O00O00 +1 #line:918
                                    g =O00000OO0000O0OOO [OO0OO0O00000O0OOO ]['level']#line:919
                                    if id ==g :#line:920
                                        O000OO0OO0O0OOO00 =OOO0OOO0000O00O00 +2 #line:921
                                        if O000OO0OO0O0OOO00 !=OO000OOO00OO0OOO0 +1 :#line:922
                                            OO0O00O0000000OO0 =OO000OOO00OO0OOO0 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O000OO0OO0000O0O0 =f'_site={OO0O00O0000000OO0 - 1}&targetSite={O000OO0OO0O0OOO00 - 1}_{timi_new()}'#line:926
                                            OO0OOO00OO0OOOO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OO000O0O000OO .token ,'timestamp':timi_new (),'sign':sign (O000OO0OO0000O0O0 ),'signstring':O000OO0OO0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            O0O0000000OO0O0O0 ={"site":int (OO0O00O0000000OO0 -1 ),"targetSite":int (O000OO0OO0O0OOO00 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOO00OO0OOOO00 ,json =O0O0000000OO0O0O0 )#line:945
                                            O0O00OO0OO000O0O0 =True #line:947
                                    if O0O00OO0OO000O0O0 :#line:948
                                        break #line:949
                                if O0O00OO0OO000O0O0 :#line:950
                                    break #line:951
        except :#line:952
            O000OO000O0O000OO .synthetic ()#line:953
    def level_new (O0000O0O0OOOO0OO0 ):#line:956
        try :#line:957
            O00000O00O00O0000 =f'__{timi_new()}'#line:958
            OOOO0000000OOO0OO ={'source':'scsc','authorization':O0000O0O0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00O00O0000 ),'signstring':O00000O00O00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O000O00OO00000OO0 =requests .request ('get',f'{host}/user',headers =OOOO0000000OOO0OO ).json ()#line:970
            if 'status'in O000O00OO00000OO0 :#line:971
                if O000O00OO00000OO0 ['status']==200 :#line:972
                    return float (O000O00OO00000OO0 ['data']['level'])#line:973
        except Exception as O00OO00O00O0OOOO0 :#line:974
            print (O00OO00O00O0OOOO0 )#line:975
    def propsraffle (O0OO0000OOOOOOO00 ):#line:978
        try :#line:979
            while True :#line:980
                O0000OOOOO0O0O000 =f'__{timi_new()}'#line:981
                O0OO00O00OO0OOOO0 ={'source':'scsc','authorization':O0OO0000OOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO0O0O000 ),'signstring':O0000OOOOO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OOO0000O00OOO0O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO00O00OO0OOOO0 ).json ()#line:993
                if 'status'in OOO0000O00OOO0O0O :#line:995
                    if OOO0000O00OOO0O0O ['status']==200 :#line:996
                        O00O00O00O00O0OO0 =OOO0000O00OOO0O0O ['data']['rows']#line:997
                        OOOO0OOO000O000O0 =OOO0000O00OOO0O0O ['data']['vstate']#line:998
                        if O00O00O00O00O0OO0 ==5 or O00O00O00O00O0OO0 ==6 or O00O00O00O00O0OO0 ==7 :#line:999
                            OOOO00OO00O00OOOO =OOO0000O00OOO0O0O ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{OOOO00OO00O00OOOO}')#line:1001
                        if O00O00O00O00O0OO0 ==1 or O00O00O00O00O0OO0 ==2 or O00O00O00O00O0OO0 ==3 :#line:1002
                            OOO0O0000O00O0O0O =OOO0000O00OOO0O0O ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{OOO0O0000O00O0O0O}')#line:1004
                        if O00O00O00O00O0OO0 ==4 or O00O00O00O00O0OO0 ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if O00O00O00O00O0OO0 =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OO0O000O0OO000 :#line:1046
            print (OO0OO0O000O0OO000 )#line:1047
    def friends_invitation (OOOOOO0O0OO0OOO0O ):#line:1050
        try :#line:1051
            OOO0O0O00O0000O0O =f'__{timi_new()}'#line:1052
            OO0OO0O0OO0OOOO0O ={'source':'scsc','authorization':OOOOOO0O0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00O0000O0O ),'signstring':OOO0O0O00O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            OOO0OOO0O0OO00O0O =requests .request ('get',f'{host}/friends',headers =OO0OO0O0OO0OOOO0O ).json ()#line:1064
            if 'status'in OOO0OOO0O0OO00O0O :#line:1065
                if OOO0OOO0O0OO00O0O ['status']==200 :#line:1066
                    O000OOOOO000O00O0 =OOO0OOO0O0OO00O0O ['data']['myInviteter']#line:1067
                    if O000OOOOO000O00O0 :#line:1068
                        O00O000O00OO0O0O0 =O000OOOOO000O00O0 ['user']['nickname']#line:1069
                        O0O0O0OO0O000000O =OOOOOO0O0OO0OOO0O .certification ()#line:1070
                        if O0O0O0OO0O000000O =='未实名':#line:1071
                            weishim .append (OOOOOO0O0OO0OOO0O .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O00O000O00OO0O0O0}丨实名:{O0O0O0OO0O000000O}')#line:1073
        except Exception as O000OO00OO0O00O0O :#line:1077
            print (O000OO00OO0O00O0O )#line:1078
    def add_clover (OOO0O00O0O0O00000 ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O00OO0O0OOO0O0OOO =f'__{timi_new()}'#line:1084
            OO000OOOOOOOO00O0 ={'source':'scsc','authorization':OOO0O00O0O0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOO0O0OOO ),'signstring':O00OO0O0OOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO0O00O00O00O0O00 =requests .request ('get',f'{host}/assets/clovers',headers =OO000OOOOOOOO00O0 ).json ()#line:1096
            if 'status'in OO0O00O00O00O0O00 :#line:1098
                if OO0O00O00O00O0O00 ['status']==200 :#line:1099
                    O00000O000O0O00OO =OO0O00O00O00O0O00 ['data']['clover']#line:1100
                    O00OO0O0O0O0000OO =OO0O00O00O00O0O00 ['data']['used_clover']#line:1101
                    OOOOOOO0O0OO0O0OO =float (O00000O000O0O00OO )-float (O00OO0O0O0O0000OO )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00OO0O0O0O0000OO}')#line:1103
                    if OOO0O00O0O0O00000 .certification ()!='未实名':#line:1104
                        if OOOOOOO0O0OO0O0OO >1 :#line:1105
                            O00OO0O0OOO0O0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOOOO0O0OO0O0OO)}_{timi_new()}'#line:1106
                            O0OOOOO00O0O0OOOO ={'source':'scsc','authorization':OOO0O00O0O0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOO0O0OOO ),'signstring':O00OO0O0OOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            O0O0OO0OOOO0OO0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOOOO0O0OO0O0OO )}#line:1118
                            O00O00O0OOO000O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOOOO00O0O0OOOO ,data =O0O0OO0OOOO0OO0O0 ).json ()#line:1119
                            if 'status'in O00O00O0OOO000O0O :#line:1121
                                if O00O00O0OOO000O0O ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O00O00O0OOO000O0O["data"]["isSuccess"]}丨数量:{OOOOOOO0O0OO0O0OO}')#line:1123
                                if O00O00O0OOO000O0O ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O00O00O0OOO000O0O["message"]}')#line:1125
            O0OO0000O0000OOO0 =requests .request ('get',f'{host}/lottery',headers =OO000OOOOOOOO00O0 ).json ()#line:1126
            OOOO000000O00OO00 =OOO0O00O0O0O00000 .winning_rewards ()#line:1128
            if 'status'in O0OO0000O0000OOO0 :#line:1129
                if O0OO0000O0000OOO0 ['status']==200 :#line:1130
                    OOO0000OOOOO0OOO0 =O0OO0000O0000OOO0 ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OOO0000OOOOO0OOO0 )#line:1132
                    OO0000000OOO0O00O =O0OO0000O0000OOO0 ['data'][1 ]['value']#line:1133
                    O00O00O00O0OO0OOO =O0OO0000O0000OOO0 ['data'][0 ]['join_number']#line:1134
                    OO000O0O0OO000000 =int (float (O0OO0000O0000OOO0 ['data'][0 ]['totalValue']))#line:1135
                    OOOOOO00000OO0OO0 =float (OO0000000OOO0O00O /OO000O0O0OO000000 )*10000 #line:1136
                    OOO0000O00000O0O0 =OO000O0O0OO000000 /O00O00O00O0OO0OOO #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OOO0000OOOOO0OOO0)[:6]}颗金种子丨好友收益:{str(OOOO000000O00OO00)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOOO00000OO0OO0)[:6]}颗金种子丨☘️人均:{str(OOO0000O00000O0O0)[:7]}️')#line:1139
        except Exception as O0O000O00O00O0OOO :#line:1140
            print (O0O000O00O00O0OOO )#line:1141
    def energy (OOO0OOOO0O0OOOOO0 ):#line:1144
        try :#line:1145
            while True :#line:1146
                O0000O000OO00OOO0 =f'__{timi_new()}'#line:1147
                O000OO000OOO00OOO ={'source':'scsc','authorization':OOO0OOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000OO00OOO0 ),'signstring':O0000O000OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OOO0OO000OO00O000 =requests .request ('get',f'{host}/energy/general',headers =O000OO000OOO00OOO ).json ()#line:1159
                if 'status'in OOO0OO000OO00O000 :#line:1161
                    if OOO0OO000OO00O000 ['status']==200 :#line:1162
                        O0OO0OO00OO0OO0O0 =OOO0OO000OO00O000 ['data']['ordinary_water']#line:1163
                        O0OO0O0O0000000O0 =OOO0OO000OO00O000 ['data']['ordinary_fertilizer']#line:1164
                        O0OO00OOO00O0000O =OOO0OO000OO00O000 ['data']['videoStatus']#line:1165
                        OOOO0OOO0OO0OO000 =OOO0OO000OO00O000 ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0OO0O0O0000000O0).split(".")[0]}丨水滴:{str(O0OO0OO00OO0OO0O0).split(".")[0]}')#line:1168
                        if float (O0OO0O0O0000000O0 )<96 :#line:1169
                            if O0OO00OOO00O0000O :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OOO0O0OO000OOO0OO =99 -float (O0OO0O0O0000000O0 )#line:1172
                                O0OOO0OOO0OO0OOO0 ={"fertilizer":str (OOO0O0OO000OOO0OO ).split ('.')[0 ]}#line:1173
                                O000OOO00O00O00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000OO000OOO00OOO ).json ()#line:1175
                                if 'status'in O000OOO00O00O00O0 :#line:1177
                                    if O000OOO00O00O00O0 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO00O00O00O0["message"]}')#line:1179
                                    if O000OOO00O00O00O0 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO00O00O00O0["message"]}')#line:1181
                                        break #line:1182
                                if float (O0OO0O0O0000000O0 )<78 :#line:1184
                                    OOO0O0OO000OOO0OO =80 -float (O0OO0O0O0000000O0 )#line:1185
                                    OO0OOO00000OOOO0O =f'_fertilizer={int(OOO0O0OO000OOO0OO)}_{timi_new()}'#line:1186
                                    OO00OOO0OOO000O00 ={'source':'scsc','authorization':OOO0OOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00000OOOO0O ),'signstring':OO0OOO00000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    OO00O00O0O0O0O000 ={"fertilizer":int (OOO0O0OO000OOO0OO )}#line:1198
                                    O0OO0O0OO0O0O0000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00OOO0OOO000O00 ,data =OO00O00O0O0O0O000 ).json ()#line:1200
                                    if 'status'in O0OO0O0OO0O0O0000 :#line:1202
                                        if O0OO0O0OO0O0O0000 ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{O0OO0O0OO0O0O0000["message"]}丨数量:{int(OOO0O0OO000OOO0OO)}')#line:1204
                                        if O0OO0O0OO0O0O0000 ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{O0OO0O0OO0O0O0000["message"]}丨数量:{int(OOO0O0OO000OOO0OO)}')#line:1206
                                            O00000O00OOOO000O =O0OO0O0OO0O0O0000 ["message"].split ('-')[1 ]#line:1207
                                            O0O0O000OO0O00O00 =f'__{timi_new()}'#line:1208
                                            O000OOOOOO0O00OOO ={'source':'scsc','authorization':OOO0OOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO0O00O00 ),'signstring':O0O0O000OO0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            O00OOOOO00O0OO0O0 =requests .request ('get',f'{host}/user',headers =O000OOOOOO0O00OOO ).json ()#line:1220
                                            if 'status'in O00OOOOO00O0OO0O0 :#line:1221
                                                if O00OOOOO00O0OO0O0 ['status']==200 :#line:1222
                                                    O00OOOO0OO0OOO00O =O00OOOOO00O0OO0O0 ['data']['inner_id']#line:1223
                                                    if give_gold (O00OOOO0OO0OOO00O ,float (O00000O00OOOO000O )+1 ):#line:1224
                                                        OOO0OOOO0O0OOOOO0 .energy ()#line:1225
                        if float (O0OO0OO00OO0OO0O0 )<880 :#line:1226
                            if OOOO0OOO0OO0OO000 :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                OOO0O000O000OO000 =999 -float (O0OO0OO00OO0OO0O0 )#line:1229
                                O0OO0O0O0O0OO000O ={"water":str (OOO0O000O000OO000 ).split ('.')[0 ]}#line:1230
                                O00O00000OOO0000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000OO000OOO00OOO ).json ()#line:1232
                                if 'status'in O00O00000OOO0000O :#line:1234
                                    if O00O00000OOO0000O ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{O00O00000OOO0000O["message"]}')#line:1236
                                    if O00O00000OOO0000O ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{O00O00000OOO0000O["message"]}')#line:1238
                                        break #line:1239
                                if float (O0OO0OO00OO0OO0O0 )<780 :#line:1240
                                    OOO0O000O000OO000 =800 -float (O0OO0OO00OO0OO0O0 )#line:1241
                                    OO0OOO0OO0OO0000O =f'_water={int(OOO0O000O000OO000)}_{timi_new()}'#line:1242
                                    O0OOO0OO00O0O00OO ={'source':'scsc','authorization':OOO0OOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO0OO0000O ),'signstring':OO0OOO0OO0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O00O0000000OOO0OO ={"water":int (OOO0O000O000OO000 )}#line:1254
                                    OO0OO0O000O000O0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOO0OO00O0O00OO ,data =O00O0000000OOO0OO ).json ()#line:1256
                                    if 'status'in OO0OO0O000O000O0O :#line:1258
                                        if OO0OO0O000O000O0O ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{OO0OO0O000O000O0O["message"]}丨数量:{int(OOO0O000O000OO000)}')#line:1260
                                        if OO0OO0O000O000O0O ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{OO0OO0O000O000O0O["message"]}丨数量:{int(OOO0O000O000OO000)}')#line:1262
                                            O00000O00OOOO000O =OO0OO0O000O000O0O ["message"].split ('-')[1 ]#line:1263
                                            O0O0O000OO0O00O00 =f'__{timi_new()}'#line:1264
                                            O000OOOOOO0O00OOO ={'source':'scsc','authorization':OOO0OOOO0O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OO0O00O00 ),'signstring':O0O0O000OO0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            O00OOOOO00O0OO0O0 =requests .request ('get',f'{host}/user',headers =O000OOOOOO0O00OOO ).json ()#line:1276
                                            if 'status'in O00OOOOO00O0OO0O0 :#line:1277
                                                if O00OOOOO00O0OO0O0 ['status']==200 :#line:1278
                                                    O00OOOO0OO0OOO00O =O00OOOOO00O0OO0O0 ['data']['inner_id']#line:1279
                                                    if give_gold (O00OOOO0OO0OOO00O ,float (O00000O00OOOO000O )+1 ):#line:1280
                                                        OOO0OOOO0O0OOOOO0 .energy ()#line:1281
                        break #line:1282
        except Exception as O0OOOO0O0O0OO0O0O :#line:1283
            print (O0OOOO0O0O0OO0O0O )#line:1284
def bundled_def ():#line:1287
    OO0000O00OOOO0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OO0000O00OOOO0OO0 [random .randint (0 ,len (OO0000O00OOOO0OO0 )-1 )]#line:1289
def version_of_the_validation ():#line:1293
    return str ((104 -56 )/10 )#line:1294
def ubbbf ():#line:1296
    print ('卡密验证通过   ✅')#line:1297
def sc2 ():#line:1300
    return "19319#$%^&*((*"#line:1301
def OO00OO0OO0OO00OO00o0 ():#line:1304
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1306
def get_ip ():#line:1309
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1311
def gitee_validation ():#line:1314
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1315
def gitee_edition ():#line:1318
    try :#line:1319
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1320
    except :#line:1321
        sys .exit (0 )#line:1322
def O000OO000O0O00OOO00 ():#line:1326
    try :#line:1327
        O0O0OO0OO0OO00O0O =gitee_edition ()#line:1328
        if version_of_the_validation ()<O0O0OO0OO0OO00O0O ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO0OO0OO00O0O["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O0O0OO0OO0OO00O0O["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO0OO0OO00O0O["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O0O0OO0OO0OO00O0O["CityEarth"]["content"]}')#line:1334
    except Exception as O0O0O000000000O00 :#line:1335
        print (O0O0O000000000O00 )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
