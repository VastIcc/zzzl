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
        O00O0OOO0O0OOO00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O00O0OOO0O0OOO00O)}个账号==========")#line:17
        for O0O0000OOOOO0000O in O00O0OOO0O0OOO00O :#line:18
            OO00OOOO0OOOOOO00 =[]#line:19
            print (f"------------正在执行第{O00O0OOO0O0OOO00O.index(O0O0000OOOOO0000O) + 1}个账号------------")#line:20
            OOOOOOO00OOO0OO0O =CityEarth (O0O0000OOOOO0000O ,OO00OOOO0OOOOOO00 ,O00O0OOO0O0OOO00O .index (O0O0000OOOOO0000O ))#line:21
            def OOOO000OO00000O0O ():#line:23
                if OOOOOOO00OOO0OO0O .base_info ():#line:25
                    OOOOOOO00OOO0OO0O .sealing ()#line:27
                    OOOOOOO00OOO0OO0O .invitenum ()#line:29
                    OOOOOOO00OOO0OO0O .query_to_sell ()#line:31
                    OOOOOOO00OOO0OO0O .friends_invitation ()#line:35
                    OOOOOOO00OOO0OO0O .energy ()#line:37
                    OOOOOOO00OOO0OO0O .add_clover ()#line:39
                    OOOOOOO00OOO0OO0O .propsraffle ()#line:41
                    OOOOOOO00OOO0OO0O .crops_illustrated ()#line:45
                    OOOOOOO00OOO0OO0O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOOOOOO00OOO0OO0O .give_gold ()#line:50
            OOOOO0O00O000000O =threading .Thread (target =OOOO000OO00000O0O )#line:52
            OOOOO0O00O000000O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO00OO0O0O0000OOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO00OO0O0O0000OOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOO000O0OOOOO000 in invited_new :#line:62
            print (OOOO000O0OOOOO000 )#line:63
        print ('开始打印未实名的token')#line:64
        for O000OO0O000OOO0OO in weishim :#line:65
            print (O000OO0O000OOO0OO )#line:66
    except Exception as OO000OO000OOO00O0 :#line:67
        print (OO000OO000OOO00O0 )#line:68
def give_gold (OOO0000OOO000O0OO ,O00OOOO0O000O0000 ):#line:72
    try :#line:73
        O0000O00O0OO00000 =f'_doneeNo={OOO0000OOO000O0OO}&quantity={int(O00OOOO0O000O0000)}_{timi_new()}'#line:74
        O0000OOOO0000O0OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000O00O0OO00000 ),'signstring':O0000O00O0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOO0000O00OOOOO0O ={"quantity":int (O00OOOO0O000O0000 ),"doneeNo":OOO0000OOO000O0OO }#line:89
        O000OOO0O0O0OOO00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0000OOOO0000O0OO ,data =OOO0000O00OOOOO0O ).json ()#line:90
        if 'status'in O000OOO0O0O0OOO00 :#line:92
            if O000OOO0O0O0OOO00 ['status']==200 :#line:93
                if O000OOO0O0O0OOO00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00OOOO0O000O0000)}种子给{OOO0000OOO000O0OO}成功')#line:95
                    return True #line:96
            if O000OOO0O0O0OOO00 ['status']==401 :#line:97
                print (f'【赠送种子】:{O000OOO0O0O0OOO00["message"]}')#line:98
                return False #line:99
            if O000OOO0O0O0OOO00 ['status']==500 :#line:100
                print (f'【赠送种子】:{O000OOO0O0O0OOO00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0O00OOOO000000O0 :#line:104
        print (O0O00OOOO000000O0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OOOO00OOO000O000O ):#line:115
    O0000OOO0OOO0O0OO =hashlib .md5 (OOOO00OOO000O000O .encode ()).hexdigest ()#line:116
    OOO00O0O0O0O0O0O0 =sc1 ()#line:117
    O00OOOO00OO0000O0 =sc2 ()#line:118
    O0O0O0O0O0O00O00O =sc3 ()#line:119
    OOOOO00OOO0OO00O0 =OOO00O0O0O0O0O0O0 +O0000OOO0OOO0O0OO +O00OOOO00OO0000O0 +O0O0O0O0O0O00O00O #line:120
    OOO0000O0OOO00OO0 =hashlib .md5 (OOOOO00OOO0OO00O0 .encode ()).hexdigest ()#line:121
    return OOO0000O0OOO00OO0 #line:122
def format_msg ():#line:125
    O0OO0O00OOO000O0O =""#line:126
    for OOOO00OOOOOO000O0 in msg_list :#line:127
        O0OO0O00OOO000O0O +=str (OOOO00OOOOOO000O0 )+"\r\n"#line:128
    return O0OO0O00OOO000O0O #line:129
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
def get_json_data (O0O000O0OO0OO0O00 ,O0O0O0OOOO00O0OO0 ,O000O0OOO00O0000O ,OO000OO00OO0OO0O0 ):#line:153
    with open (O0O000O0OO0OO0O00 ,'rb')as O00O0O0O00OOO00O0 :#line:154
        O0O000O000O0OO00O =json .load (O00O0O0O00OOO00O0 )#line:155
        O0O000O000O0OO00O ['data'][O0O0O0OOOO00O0OO0 ][O000O0OOO00O0000O ]=OO000OO00OO0OO0O0 #line:156
        OOOO0OO000000O000 =O0O000O000O0OO00O #line:157
    O00O0O0O00OOO00O0 .close ()#line:158
    return OOOO0OO000000O000 #line:159
def write_json_data (OOOOO000O00OO000O ):#line:162
    with open (json_path1 ,'w')as O00O0OOO0O0OOOOOO :#line:163
        json .dump (OOOOO000O00OO000O ,O00O0OOO0O0OOOOOO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O00O0OOO0O0OOOOOO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO00OO0O0OOOO0O0O ,OO0OOOO0000OOO000 ,O0O0O000O0O00OOO0 ,OOO0OOOOO000O0O00 ):#line:171
        try :#line:172
            OO00OO0O0OOOO0O0O .msg =O0O0O000O0O00OOO0 #line:173
            OO00OO0O0OOOO0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO00OO0O0OOOO0O0O .token =OO0OOOO0000OOO000 ['authorization']#line:175
            OO00OO0O0OOOO0O0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO00OO0O0OOOO0O0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO00OO0O0OOOO0O0O .elephant_user =OO0OOOO0000OOO000 ['elephant_user']#line:178
            OO00OO0O0OOOO0O0O .elephant_pswd =OO0OOOO0000OOO000 ['elephant_pswd']#line:179
            OO00OO0O0OOOO0O0O .elephant_Task_ID =OO0OOOO0000OOO000 ['elephant_Task_ID']#line:180
            OO00OO0O0OOOO0O0O .len_new =OOO0OOOOO000O0O00 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO000O0O0OO000OOO ):#line:186
        try :#line:187
            OO000O0O0OO000OOO .watched_ad ()#line:189
            OOOOOO0OOO000OOOO =f'__{timi_new()}'#line:190
            O00OO0OO0O0OO00O0 ={'source':'scsc','authorization':OO000O0O0OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOO000OOOO ),'signstring':OOOOOO0OOO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOO0OOOOO0OOOOOO =requests .request ('get',f'{host}/user',headers =O00OO0OO0O0OO00O0 ).json ()#line:202
            if 'status'in OOOO0OOOOO0OOOOOO :#line:204
                if OOOO0OOOOO0OOOOOO ['status']==200 :#line:205
                    O0O0O00OOOOO000OO =OOOO0OOOOO0OOOOOO ['data']['nickname']#line:206
                    O000OO00O00OOOO00 =OOOO0OOOOO0OOOOOO ['data']['inner_id']#line:207
                    O0OOO00O0O000OO0O =OOOO0OOOOO0OOOOOO ['data']['assets']['gold']#line:208
                    OO000O0OO0O0O0OO0 =OOOO0OOOOO0OOOOOO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0O0O00OOOOO000OO[:5]}丨ID:{O000OO00O00OOOO00}丨等级:{OO000O0OO0O0O0OO0}丨金种子:{str(O0OOO00O0O000OO0O).split(".")[0]}')#line:211
                    if 'wx_'in O0O0O00OOOOO000OO :#line:212
                        OO000O0O0OO000OOO .change_nickname ()#line:213
                if OOOO0OOOOO0OOOOOO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO000O0O0OO000OOO .elephant_user =='f':#line:216
                        return False #line:217
                    O0OOOOOO0OO00O0OO =Invalid_login .addtask (elephant_user =OO000O0O0OO000OOO .elephant_user ,elephant_pswd =OO000O0O0OO000OOO .elephant_pswd ,elephant_Task_ID =OO000O0O0OO000OOO .elephant_Task_ID )#line:220
                    O0O0OO0O0OOO0000O =get_json_data (json_path ,OO000O0O0OO000OOO .len_new ,'authorization',O0OOOOOO0OO00O0OO )#line:221
                    if write_json_data (O0O0OO0O0OOO0000O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOO0OOOOO0OOOOOO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO00O0O000OOOOOO :#line:228
            print (OOO00O0O000OOOOOO )#line:229
    def sealing (O00OOO0OOO0OOO0O0 ):#line:232
        try :#line:233
            O00OOO00O0O0OOO00 =f'__{timi_new()}'#line:234
            OOO0O00OO0O00000O ={'source':'scsc','authorization':O00OOO0OOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00O0O0OOO00 ),'signstring':O00OOO00O0O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0O00OO0O00000O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO0O00OO0O00000O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0O00OO0O00000O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0O00OO0O00000O )#line:249
            requests .request ('get',f'{host}/user',headers =OOO0O00OO0O00000O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0O00OO0O00000O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0O00OO0O00000O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0O00OO0O00000O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00OO0O00000O )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO0O00OO0O00000O )#line:255
        except Exception as O0O00O000000O0OOO :#line:256
            print (O0O00O000000O0OOO )#line:257
    def ddd (OOOO0OOOO0O00OO0O ):#line:259
        try :#line:260
            OO0O0O000O0O000O0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0OOOO00O000O000O ={'source':'scsc','authorization':OOOO0OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000O0O000O0 ),'signstring':OO0O0O000O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0OO0O0OO0O00OOO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OOOO00O000O000O ).json ()#line:273
            print (OO0OO0O0OO0O00OOO )#line:274
        except Exception as OO00000OOO0OO0OO0 :#line:277
            print (OO00000OOO0OO0OO0 )#line:278
    def the_query (O00OOO000O00OOO00 ):#line:283
        try :#line:284
            O0OO0O00OO00O0O0O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO00O0000O0000OO0 ={'authorization':O00OOO000O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00OO00O0O0O ),'signstring':O0OO0O00OO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO0O0OO0OO0000OOO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00O0000O0000OO0 ).json ()#line:296
            if 'status'in OO0O0OO0OO0000OOO :#line:298
                if OO0O0OO0OO0000OOO ['status']==200 :#line:299
                    return OO0O0OO0OO0000OOO ['data']['rows'][4 ]['price']#line:300
        except Exception as OOO0OOOOO0O000000 :#line:301
            print (OOO0OOOOO0O000000 )#line:302
    def market_sale (O00O00OO0000OO000 ,OOOO0O0O000000O0O ):#line:305
        try :#line:306
            OO0000OO000OO0OO0 =timi_new ()#line:307
            OO0OO000OO0OOOOOO =f'type=crop__{OO0000OO000OO0OO0}'#line:308
            OO0O00OOOO0O00000 ={'source':'scsc','authorization':O00O00OO0000OO000 .token ,'timestamp':str (OO0000OO000OO0OO0 ),'sign':sign (OO0OO000OO0OOOOOO ),'signstring':OO0OO000OO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            OOOO0O0O0OOOOOO0O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O00OOOO0O00000 ).json ()#line:320
            if 'status'in OOOO0O0O0OOOOOO0O :#line:322
                if OOOO0O0O0OOOOOO0O ['status']==200 :#line:323
                    if OOOO0O0O0OOOOOO0O ['data']['rows']:#line:324
                        O00O0OO00000O0O0O =OOOO0O0O0OOOOOO0O ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0OO0000O000O0O00 =OOOO0O0O0OOOOOO0O ['data']['rows'][0 ]['quantity']#line:326
                        if float (OOOO0O0O000000O0O )>6 :#line:327
                            OO0OOO0OO0OO0OO0O =f'_packsackItemId={O00O0OO00000O0O0O}&price={str(OOOO0O0O000000O0O)[:5]}&quantity={O0OO0000O000O0O00}_{OO0000OO000OO0OO0}'#line:328
                            O0000O0OOO0OOO0OO ={'source':'scsc','authorization':O00O00OO0000OO000 .token ,'timestamp':str (OO0000OO000OO0OO0 ),'sign':sign (OO0OOO0OO0OO0OO0O ),'signstring':OO0OOO0OO0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            O0O00OO000O0OO0O0 ={"packsackItemId":O00O0OO00000O0O0O ,"price":str (OOOO0O0O000000O0O )[:5 ],"quantity":str (O0OO0000O000O0O00 )}#line:344
                            OO00O000O0O00O0O0 =requests .request ('post',f'{host}/market/sale',headers =O0000O0OOO0OOO0OO ,data =O0O00OO000O0OO0O0 ).json ()#line:345
                            if 'status'in OO00O000O0O00O0O0 :#line:347
                                if OO00O000O0O00O0O0 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O0OO0000O000O0O00}丨价格:{str(OOOO0O0O000000O0O)[:5]}')#line:349
                                if OO00O000O0O00O0O0 ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{OO00O000O0O00O0O0["message"]}')#line:351
        except Exception as O000O0OO00O000O0O :#line:352
            print (O000O0OO00O000O0O )#line:353
    def query_to_sell (OOOO0OOO0O0000O0O ):#line:356
        global count_list #line:357
        try :#line:358
            O0O00O000OO00000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOOOO0000O0O00000 ={'source':'scsc','authorization':OOOO0OOO0O0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O000OO00000O ),'signstring':O0O00O000OO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            OOO0000OO000OOOOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOOO0000O0O00000 ).json ()#line:371
            if 'status'in OOO0000OO000OOOOO :#line:373
                if OOO0000OO000OOOOO ['status']==200 :#line:374
                    for OOOOOO000OOOO00O0 in OOO0000OO000OOOOO ['data']['rows']:#line:375
                        O0O00O0000O00O0O0 =OOOOOO000OOOO00O0 ['materialKey']#line:376
                        O0OO0OOO0OO00O000 =OOOOOO000OOOO00O0 ['quantity']#line:377
                        O0O0OO00O0O0O0OOO =OOOOOO000OOOO00O0 ['price']#line:378
                        OO0O00O0000OOOOO0 =OOOOOO000OOOO00O0 ['saleState']#line:379
                        if OO0O00O0000OOOOO0 ==0 :#line:380
                            print (f'【出售订单】:名称:{O0O00O0000O00O0O0}丨数量:{O0OO0OOO0OO00O000}丨价格:{O0O0OO00O0O0O0OOO}')#line:381
                            count_list +=O0OO0OOO0OO00O000 #line:382
                            O0O0OO0O00OOO00OO =OOOO0OOO0O0000O0O .the_query ()#line:384
                            if float (O0O0OO0O00OOO00OO )!=float (O0O0OO00O0O0O0OOO ):#line:385
                                OOOO000O000OOOOO0 =OOOOOO000OOOO00O0 ['id']#line:386
                                OOOO0OOO0O0000O0O .cacel_sale (OOOO000O000OOOOO0 )#line:387
                    OOOO0OOO0O0000O0O .game_map ()#line:389
        except Exception as OOOO0OOO000000000 :#line:391
            print (OOOO0OOO000000000 )#line:392
    def cacel_sale (OOO000O0O000OO0OO ,OOOO0000O00O000OO ):#line:395
        try :#line:396
            OO000O00O0OOOOOO0 =f'_saleId={OOOO0000O00O000OO}_{timi_new()}'#line:397
            O0O00O0000O00000O ={'source':'scsc','authorization':OOO000O0O000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0OOOOOO0 ),'signstring':OO000O00O0OOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O00OOOO0OOO0O0O0O ={"saleId":OOOO0000O00O000OO }#line:409
            O000O0OOOO00OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O00O0000O00000O ,data =O00OOOO0OOO0O0O0O ).json ()#line:410
            if 'status'in O000O0OOOO00OOOOO :#line:412
                if O000O0OOOO00OOOOO ['status']==200 :#line:413
                    print (f'【下架出售】:{O000O0OOOO00OOOOO["data"]}')#line:414
        except Exception as OO00OO0OO0O0OOOOO :#line:415
            print (OO00OO0OO0O0OOOOO )#line:416
    def change_nickname (OOO00O0OOOOO000O0 ):#line:419
        try :#line:420
            O000000OOO00OO0O0 =timi_new ()#line:421
            O0OO0OO000O0OOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O000O000O000O0O0O =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO0OO000O0OOO00 ).text #line:423
            O00OOOOOO0O0O0OOO =re .findall ('<ul><li>(.*?)</li>',O000O000O000O0O0O )[0 ][:3 ]#line:424
            OO0O0000O0000OO0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00OOOOOO0O0O0OOO}').json ()#line:425
            OOO0OOOO000OO0000 =OO0O0000O0000OO0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            O00O0OO00O0000000 ={"nickname":OOO0OOOO000OO0000 }#line:427
            O00000OOOO0OO00OO =f'_nickname={OOO0OOOO000OO0000}_{O000000OOO00OO0O0}'#line:428
            O00000O0O00OO00O0 ={'source':'scsc','authorization':OOO00O0OOOOO000O0 .token ,'timestamp':O000000OOO00OO0O0 ,'sign':sign (O00000OOOO0OO00OO ),'signstring':O00000OOOO0OO00OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO0O0OO0OO0OOO000 =requests .request ('patch',f'{host}/user/nickname',headers =O00000O0O00OO00O0 ,data =O00O0OO00O0000000 ).json ()#line:440
            if 'status'in OO0O0OO0OO0OOO000 :#line:442
                if OO0O0OO0OO0OOO000 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OOO0OOOO000OO0000}丨{OO0O0OO0OO0OOO000["message"]}')#line:444
        except Exception as OOO00O0OOO0O00O00 :#line:445
            print (OOO00O0OOO0O00O00 )#line:446
    def withdraw (O000O00O0O00OOOO0 ):#line:449
        try :#line:450
            O0O00O0OO0O00OO0O =f'__{timi_new()}'#line:451
            O0000O00O0OO00O00 ={'source':'scsc','authorization':O000O00O0O00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0O00OO0O ),'signstring':O0O00O0OO0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            O00OOOO0OO00O0000 =requests .request ('get',f'{host}/assets',headers =O0000O00O0OO00O00 ).json ()#line:463
            if 'status'in O00OOOO0OO00O0000 :#line:465
                if O00OOOO0OO00O0000 ['status']==200 :#line:466
                    OO00000OO0OO0O0OO =O00OOOO0OO00O0000 ['data']['cash']#line:467
                    if float (OO00000OO0OO0O0OO )>20 :#line:468
                        O0O00O0OO0O00OO0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O0000O00O0OO00O00 ={'authorization':O000O00O0O00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO0O00OO0O ),'signstring':O0O00O0OO0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O00O00000OOOOO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OOO000OOO0OO000O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000O00O0OO00O00 ,data =O00O00000OOOOO0OO ).json ()#line:482
                        if 'status'in OOO000OOO0OO000O0 :#line:484
                            if OOO000OOO0OO000O0 ['status']==200 :#line:485
                                print (f'【余额提现】:{OOO000OOO0OO000O0["data"]}')#line:486
                        if 'status'in OOO000OOO0OO000O0 :#line:487
                            if OOO000OOO0OO000O0 ['status']==500 :#line:488
                                print (f'【余额提现】:{OOO000OOO0OO000O0["message"]}')#line:489
        except Exception as OO0O0O0O0O000OOO0 :#line:490
            print (OO0O0O0O0O000OOO0 )#line:491
    def invitenum (O000000O0OOO0O00O ):#line:494
        global invited_new #line:495
        try :#line:496
            O000O000OO0OOO0OO =f'__{timi_new()}'#line:497
            OO00O0O0OOOOOO0OO ={'source':'scsc','authorization':O000000O0OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OO0OOO0OO ),'signstring':O000O000OO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OO00O0O00OO00O00O =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O0O0OOOOOO0OO ).json ()#line:509
            if 'status'in OO00O0O00OO00O00O :#line:511
                if OO00O0O00OO00O00O ['status']==200 :#line:512
                    OO000OO0O0OOO00O0 =OO00O0O00OO00O00O ['data']['invited_count']#line:513
                    OOO0O0OOO0OOO0O0O =OO00O0O00OO00O00O ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OO000OO0O0OOO00O0}丨间邀好友:{OOO0O0OOO0OOO0O0O}')#line:515
                    if OO000OO0O0OOO00O0 <2 :#line:516
                        O000OOO0O0000O00O =f'__{timi_new()}'#line:517
                        O0O0OO0000O00O0O0 ={'source':'scsc','authorization':O000000O0OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O0000O00O ),'signstring':O000OOO0O0000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OOO0OO00000OO00OO =requests .request ('get',f'{host}/user',headers =O0O0OO0000O00O0O0 ).json ()#line:529
                        if 'status'in OOO0OO00000OO00OO :#line:531
                            if OOO0OO00000OO00OO ['status']==200 :#line:532
                                invited_new .append (OOO0OO00000OO00OO ['data']['inner_id'])#line:533
        except Exception as O0O0OO00OOO0OOOO0 :#line:534
            print (O0O0OO00OOO0OOOO0 )#line:535
    def game_map (OOOO00OO00O000O0O ):#line:538
        try :#line:539
            OO0O0OOO0OOOOO00O =f'__{timi_new()}'#line:540
            O0OOOOOO0O000O0OO ={'source':'scsc','authorization':OOOO00OO00O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO0OOOOO00O ),'signstring':OO0O0OOO0OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O00O00OOO000O0000 =requests .request ('get',f'{host}/game/map',headers =O0OOOOOO0O000O0OO ).json ()#line:552
            if 'status'in O00O00OOO000O0000 :#line:554
                if O00O00OOO000O0000 ['status']==200 :#line:555
                    for O0OOOO00OOO0O000O in O00O00OOO000O0000 ['data']['list'][0 ]['crops']:#line:556
                        O0OOOO00000O0O0O0 =O0OOOO00OOO0O000O ['level']#line:558
                        if O0OOOO00000O0O0O0 ==41 :#line:559
                            OOOO0O0000OOOO00O =O0OOOO00OOO0O000O ['crop_name']#line:560
                            O0OOOOO0O000OOOOO =O0OOOO00OOO0O000O ['count']#line:561
                            if O0OOOOO0O000OOOOO >0 :#line:562
                                print (f'【农业资产】:{OOOO0O0000OOOO00O}丨数量:{O0OOOOO0O000OOOOO}')#line:563
                                OO0OOOOOOOOO0O00O =OOOO00OO00O000O0O .the_query ()#line:564
                                OOOO00OO00O000O0O .market_sale (OO0OOOOOOOOO0O00O )#line:565
        except Exception as OO000OOO00000000O :#line:566
            print (OO000OOO00000000O )#line:567
    def give_gold (O0OOO0OO000O0O00O ):#line:570
        try :#line:571
            O00OOO0O0O0O0O0O0 =f'__{timi_new()}'#line:572
            O000OO00O0OO0O0OO ={'source':'scsc','authorization':O0OOO0OO000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0O0O0O0O0 ),'signstring':O00OOO0O0O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OO00O0O0OO0O0OOOO =requests .request ('get',f'{host}/user',headers =O000OO00O0OO0O0OO ).json ()#line:584
            if 'status'in OO00O0O0OO0O0OOOO :#line:585
                if OO00O0O0OO0O0OOOO ['status']==200 :#line:586
                    if float (O0OOO0OO000O0O00O .doneeNo )!=0 :#line:587
                        OOOOO0O0O0OO0OOO0 =OO00O0O0OO0O0OOOO ['data']['assets']['gold']#line:588
                        if float (OOOOO0O0O0OO0OOO0 )>float (O0OOO0OO000O0O00O .innerId ):#line:589
                            O00OO0000OO00O0O0 =int (float (OOOOO0O0O0OO0OOO0 )/1.1 )#line:590
                            O00OOO0O0O0O0O0O0 =f'_doneeNo={O0OOO0OO000O0O00O.doneeNo}&quantity={O00OO0000OO00O0O0}_{timi_new()}'#line:591
                            O000OO00O0OO0O0OO ={'source':'scsc','authorization':O0OOO0OO000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0O0O0O0O0 ),'signstring':O00OOO0O0O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OOOO0O00O0OOOO00O ={"quantity":O00OO0000OO00O0O0 ,"doneeNo":O0OOO0OO000O0O00O .doneeNo }#line:606
                            OO00OOOO0O0O00O0O =requests .request ('post',f'{host}/finance/give-gold',headers =O000OO00O0OO0O0OO ,data =OOOO0O00O0OOOO00O ).json ()#line:607
                            if 'status'in OO00OOOO0O0O00O0O :#line:609
                                if OO00OOOO0O0O00O0O ['status']==200 :#line:610
                                    if OO00OOOO0O0O00O0O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{O00OO0000OO00O0O0}种子给{O0OOO0OO000O0O00O.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O0O00O0O0OOOOO0OO :#line:615
            print (O0O00O0O0OOOOO0OO )#line:616
    def invitation (O0O00000O0000OOOO ):#line:618
        try :#line:619
            _OOOO000000O00O0OO =float (bundled_def ())/4 #line:620
            OO000OO00O000O0O0 =f'_innerId={int(_OOOO000000O00O0OO)}_{timi_new()}'#line:622
            OOO0000O0O00OOOOO ={'source':'scsc','authorization':O0O00000O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O000O0O0 ),'signstring':OO000OO00O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            OO0O0OO0OOOOOO00O ={"innerId":int (_OOOO000000O00O0OO )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0000O0O00OOOOO ,data =OO0O0OO0OOOOOO00O )#line:635
        except Exception as OO0OOO0OO0O0OOOO0 :#line:636
            print (OO0OOO0OO0O0OOOO0 )#line:637
    def winning_rewards (OOOO00000O0OO00OO ):#line:640
        try :#line:641
            O00OO0000000O0O00 =f'__{timi_new()}'#line:642
            OO0OOO0O0O0O0O0OO ={'source':'scsc','authorization':OOOO00000O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000000O0O00 ),'signstring':O00OO0000000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OOO0000O0OOO0O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0OOO0O0O0O0O0OO ).json ()#line:654
            if 'status'in OOO0000O0OOO0O000 :#line:656
                if OOO0000O0OOO0O000 ['status']==200 :#line:657
                    if OOO0000O0OOO0O000 ['data']['amount']:#line:658
                        OOOOOO00OOOOO0O00 =OOO0000O0OOO0O000 ['data']['amount']['gold']#line:659
                        return OOOOOO00OOOOO0O00 #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOOOOO0O0OO0O0O0O :#line:663
            print (OOOOOO0O0OO0O0O0O )#line:664
    def certification (O0O0OO000OOOO0OOO ):#line:667
        try :#line:668
            O0OO000OOOO0O0000 =f'__{timi_new()}'#line:669
            OOO0O0O0OO0000OO0 ={'source':'scsc','authorization':O0O0OO000OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOO0O0000 ),'signstring':O0OO000OOOO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            OOOO0OO0000OOOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0O0O0OO0000OO0 ).json ()#line:681
            if 'status'in OOOO0OO0000OOOO0O :#line:683
                if OOOO0OO0000OOOO0O ['status']==200 :#line:684
                    if OOOO0OO0000OOOO0O ['data']['result']:#line:685
                        OOO0OO000OOO0O00O =OOOO0OO0000OOOO0O ['data']['nick_name']#line:686
                        return OOO0OO000OOO0O00O #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0000OO00000OOO00 :#line:690
            print (O0000OO00000OOO00 )#line:691
    def crops_illustrated (OO0OO0O00OOOOO00O ):#line:694
        try :#line:695
            O0OO0O0O0O0000000 =f'__{timi_new()}'#line:696
            O0OOO00O0OOO000OO ={'source':'scsc','authorization':OO0OO0O00OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0O0000000 ),'signstring':O0OO0O0O0O0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            OOO0OO00OO0O0OOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO00O0OOO000OO ).json ()#line:708
            if 'status'in OOO0OO00OO0O0OOO0 :#line:710
                if OOO0OO00OO0O0OOO0 ['status']==200 :#line:711
                    OO0OO00O000OOO000 =OOO0OO00OO0O0OOO0 ['data'][0 ]['crops']#line:712
                    for O00OO0OOOO0O0000O in OO0OO00O000OOO000 :#line:713
                        if O00OO0OOOO0O0000O ['ill_clover_award']:#line:714
                            if float (O00OO0OOOO0O0000O ['ill_clover_award'])>1 :#line:715
                                if O00OO0OOOO0O0000O ['is_finish']:#line:716
                                    if not O00OO0OOOO0O0000O ['is_getit']:#line:717
                                        if OO0OO0O00OOOOO00O .certification ()!='未实名':#line:718
                                            O0OO0O0O0O0000000 =f'_award_level={O00OO0OOOO0O0000O["level"]}_{timi_new()}'#line:719
                                            O0OOO00O0OOO000OO ={'source':'scsc','authorization':OO0OO0O00OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0O0000000 ),'signstring':O0OO0O0O0O0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0O000OO0O0OO0000 ={"award_level":O00OO0OOOO0O0000O ['level']}#line:731
                                            OOOOO0OO0O00O0OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO00O0OOO000OO ,json =O0O000OO0O0OO0000 ).json ()#line:733
                                            if 'status'in OOOOO0OO0O00O0OOO :#line:734
                                                if OOOOO0OO0O00O0OOO ['status']==200 :#line:735
                                                    O000000O0OO0000OO =OOOOO0OO0O00O0OOO ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O00OO0OOOO0O0000O["crop_name"]}成就丨奖励{O000000O0OO0000OO}☘️')#line:738
                                                if OOOOO0OO0O00O0OOO ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OOOOO0OO0O00O0OOO["message"]}')#line:740
        except Exception as O0O0OOOOO00OOO00O :#line:741
            print (O0O0OOOOO00OOO00O )#line:742
    def watched_ad (O000OOO00OO0OO000 ):#line:745
        try :#line:746
            O0OOOO00O000OO00O =f'__{timi_new()}'#line:747
            O000OO0O0OO000O00 ={'source':'scsc','authorization':O000OOO00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00O000OO00O ),'signstring':O0OOOO00O000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            O0O000O0OO0OO0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO0O0OO000O00 ).json ()#line:759
            if 'status'in O0O000O0OO0OO0OO0 :#line:761
                if O0O000O0OO0OO0OO0 ['status']==200 :#line:762
                    if 'offlineInfo'in O0O000O0OO0OO0OO0 ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        O0OO00O0O00O0O0OO =O0O000O0OO0OO0OO0 ['data']['offlineInfo']['off_minute']#line:765
                        OO000O00OO00OO0O0 =float (O0O000O0OO0OO0OO0 ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000OO0O0OO000O00 ).json ()#line:768
                        time .sleep (2 )#line:769
                        O0OO0OO00OOOOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO0O0OO000O00 ).json ()#line:770
                        if 'status'in O0OO0OO00OOOOO000 :#line:772
                            if O0OO0OO00OOOOO000 ['status']==200 :#line:773
                                O00O0OOO00O00O0O0 =float (O0OO0OO00OOOOO000 ['data']['silver'])/1000000000000 #line:774
                                O0O0O0O0000O0000O =str (O00O0OOO00O00O0O0 -OO000O00OO00OO0O0 )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{O0OO00O0O00O0O0OO}分钟奖励🌱数量:{O0O0O0O0000O0000O}t粒')#line:776
        except Exception as O00O0OO000OOOO000 :#line:777
            print (O00O0OO000OOOO000 )#line:778
    def user_ad (OOO000OO0O00O0000 ):#line:781
        try :#line:782
            OO0O0O0OOO00OO0OO =f'__{timi_new()}'#line:783
            OO000O00OO0OOO000 ={'source':'scsc','authorization':OOO000OO0O00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO00OO0OO ),'signstring':OO0O0O0OOO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O00O0OOO000O0O000 =requests .request ('get',f'{host}/user/ad',headers =OO000O00OO0OOO000 ).json ()#line:795
            if 'status'in O00O0OOO000O0O000 :#line:797
                if O00O0OOO000O0O000 ['status']==200 :#line:798
                    OOOO000O000OO000O =O00O0OOO000O0O000 ['data']['max_time']#line:799
                    O00OO0OOO0OOO0OOO =O00O0OOO000O0O000 ['data']['watch_time']#line:800
                    OO0OO0O0OOOOO0000 =O00O0OOO000O0O000 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{OO0OO0O0OOOOO0000 + OOOO000O000OO000O - O00OO0OOO0OOO0OOO}次丨好友提供:{OO0OO0O0OOOOO0000}次')#line:802
                    if OO0OO0O0OOOOO0000 +OOOO000O000OO000O -O00OO0OOO0OOO0OOO >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        O0O000O0OOOOOOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000O00OO0OOO000 ).json ()#line:805
                        if 'status'in O0O000O0OOOOOOO00 :#line:807
                            if O0O000O0OOOOOOO00 ['status']==200 :#line:808
                                O00000OO0OO0000O0 =float (O0O000O0OOOOOOO00 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(O00000OO0OO0000O0)}t粒')#line:810
                                return True #line:811
                            if O0O000O0OOOOOOO00 ['status']==500 :#line:812
                                OOOO0OO000OOOOO00 =O0O000O0OOOOOOO00 ['message']#line:813
                                print (f'【获取种子】:{OOOO0OO000OOOOO00}')#line:814
                                return False #line:815
        except Exception as OO0O0OO0OO000O00O :#line:816
            print (OO0O0OO0OO000O00O )#line:817
    def synthetic (O0O00OOOO00000O00 ):#line:820
        global id ,g #line:821
        try :#line:822
            O00OOOO00O00O0OOO =O0O00OOOO00000O00 .level_new ()#line:823
            OO0O0O0OO000000O0 =random .randint (9 ,11 )#line:824
            O0000O0OO0OO00OOO =f'_site=8&targetSite={OO0O0O0OO000000O0}_{timi_new()}'#line:825
            OOOO00000OO0OO0O0 ={'source':'scsc','authorization':O0O00OOOO00000O00 .token ,'timestamp':timi_new (),'sign':sign (O0000O0OO0OO00OOO ),'signstring':O0000O0OO0OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            O000000OOOO00OOO0 ={"site":int (8 ),"targetSite":int (OO0O0O0OO000000O0 )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OOOO00000OO0OO0O0 ,json =O000000OOOO00OOO0 )#line:838
            while True :#line:839
                O0OO000OO00OO00O0 =f'__{timi_new()}'#line:840
                OOOO00000O0O0OO0O ={'source':'scsc','authorization':O0O00OOOO00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OO00OO00O0 ),'signstring':O0OO000OO00OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                OOOOO0O00000O0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00000O0O0OO0O ).json ()#line:852
                if 'status'in OOOOO0O00000O0O00 :#line:854
                    if OOOOO0O00000O0O00 ['status']==200 :#line:855
                        O0OO000OOO0000OO0 =OOOOO0O00000O0O00 ['data']['cropList']#line:856
                        OO0OO0000OO0O0000 =OOOOO0O00000O0O00 ['data']['gameCoreDataDBid']#line:857
                        O0O00OO0O0OO0O0O0 =float (OOOOO0O00000O0O00 ['data']['silver'])/1000000000000 #line:858
                        O0000O0O00O00OO0O =0 #line:863
                        for OOO0000O00OO00OO0 in O0OO000OOO0000OO0 :#line:864
                            if not OOO0000O00OO00OO0 :#line:865
                                OO000OO000OO00O00 =f'_crop_id={OO0OO0000OO0O0000}&site={O0000O0O00O00OO0O}_{O0O00OOOO00000O00.time}'#line:866
                                O0OO000OOOOO000OO ={'source':'scsc','authorization':O0O00OOOO00000O00 .token ,'timestamp':O0O00OOOO00000O00 .time ,'sign':sign (OO000OO000OO00O00 ),'signstring':OO000OO000OO00O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                O000OOO0OOOO0OO00 ={"site":O0000O0O00O00OO0O ,"crop_id":OO0OO0000OO0O0000 }#line:877
                                OOO0O00O0O000O00O =requests .request ('post',f'{host}/game/crops/buy',headers =O0OO000OOOOO000OO ,data =O000OOO0OOOO0OO00 ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOO0O00O0O000O00O :#line:881
                                    if OOO0O00O0O000O00O ['status']==200 :#line:882
                                        if OOO0O00O0O000O00O ['message']=='种子数量不足':#line:883
                                            O00OOOO00O00O0OOO =O0O00OOOO00000O00 .level_new ()#line:884
                                            print (f'【种植合成】:{OOO0O00O0O000O00O["message"]}')#line:885
                                            if not O0O00OOOO00000O00 .user_ad ():#line:886
                                                return False #line:887
                                    if OOO0O00O0O000O00O ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOO0O00O0O000O00O["message"]}')#line:889
                                        return False #line:890
                            O0000O0O00O00OO0O +=1 #line:891
                        OOOOO0OOO0000O00O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00000O0O0OO0O ).json ()#line:892
                        O0OO0O0OOOOOO0O0O =OOOOO0OOO0000O00O ['data']['cropList']#line:893
                        OOOOOOO00OO00OOOO =False #line:894
                        for OOO0000O00OO00OO0 in range (12 ):#line:895
                            id =O0OO0O0OOOOOO0O0O [OOO0000O00OO00OO0 ]['level']#line:896
                            if float (O00OOOO00O00O0OOO )-float (id )>9 :#line:897
                                OOOOO0OOO00O000OO =f'_site={OOO0000O00OO00OO0}_{timi_new()}'#line:898
                                OOOOOOOOO0O0O0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00OOOO00000O00 .token ,'timestamp':timi_new (),'sign':sign (OOOOO0OOO00O000OO ),'signstring':OOOOO0OOO00O000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O00OOO00O00OOOOO0 ={"site":OOO0000O00OO00OO0 }#line:910
                                OO00O0OOOOO0O0000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOOOOO0O0O0O00 ,data =O00OOO00O00OOOOO0 ).json ()#line:912
                                if 'status'in OO00O0OOOOO0O0000 :#line:913
                                    if OO00O0OOOOO0O0000 ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OOO0OO0O00OOO0OO0 in range (11 ):#line:917
                                    OO00O0O00O00OO00O =OOO0OO0O00OOO0OO0 +1 #line:918
                                    g =O0OO0O0OOOOOO0O0O [OO00O0O00O00OO00O ]['level']#line:919
                                    if id ==g :#line:920
                                        O00O00O0OOOOOO0O0 =OOO0OO0O00OOO0OO0 +2 #line:921
                                        if O00O00O0OOOOOO0O0 !=OOO0000O00OO00OO0 +1 :#line:922
                                            OOOOOO000O0O0O0OO =OOO0000O00OO00OO0 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O0000O0OO0OO00OOO =f'_site={OOOOOO000O0O0O0OO - 1}&targetSite={O00O00O0OOOOOO0O0 - 1}_{timi_new()}'#line:926
                                            OOOO00000OO0OO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00OOOO00000O00 .token ,'timestamp':timi_new (),'sign':sign (O0000O0OO0OO00OOO ),'signstring':O0000O0OO0OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            O00OO0OOO00O0O00O ={"site":int (OOOOOO000O0O0O0OO -1 ),"targetSite":int (O00O00O0OOOOOO0O0 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOO00000OO0OO0O0 ,json =O00OO0OOO00O0O00O )#line:945
                                            OOOOOOO00OO00OOOO =True #line:947
                                    if OOOOOOO00OO00OOOO :#line:948
                                        break #line:949
                                if OOOOOOO00OO00OOOO :#line:950
                                    break #line:951
        except :#line:952
            O0O00OOOO00000O00 .synthetic ()#line:953
    def level_new (O0O0O0O00OO00OOOO ):#line:956
        try :#line:957
            O00000OO0O0O00OOO =f'__{timi_new()}'#line:958
            O0O0OOO0O000OO0O0 ={'source':'scsc','authorization':O0O0O0O00OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0O0O00OOO ),'signstring':O00000OO0O0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O000OOOOO00O0O0OO =requests .request ('get',f'{host}/user',headers =O0O0OOO0O000OO0O0 ).json ()#line:970
            if 'status'in O000OOOOO00O0O0OO :#line:971
                if O000OOOOO00O0O0OO ['status']==200 :#line:972
                    return float (O000OOOOO00O0O0OO ['data']['level'])#line:973
        except Exception as O0O00O0OOOO00OO0O :#line:974
            print (O0O00O0OOOO00OO0O )#line:975
    def propsraffle (O0O00OO0OO00OO0O0 ):#line:978
        try :#line:979
            while True :#line:980
                O0O0OOO0OOO000O0O =f'__{timi_new()}'#line:981
                OOOO0O0O000OOO0O0 ={'source':'scsc','authorization':O0O00OO0OO00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0OOO000O0O ),'signstring':O0O0OOO0OOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                O0OOOO00OO0OO00OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO0O0O000OOO0O0 ).json ()#line:993
                if 'status'in O0OOOO00OO0OO00OO :#line:995
                    if O0OOOO00OO0OO00OO ['status']==200 :#line:996
                        OOOOO00000OOOOOOO =O0OOOO00OO0OO00OO ['data']['rows']#line:997
                        OOO0O00O0O00O0000 =O0OOOO00OO0OO00OO ['data']['vstate']#line:998
                        if OOOOO00000OOOOOOO ==5 or OOOOO00000OOOOOOO ==6 or OOOOO00000OOOOOOO ==7 :#line:999
                            O0OO0O00O0OO00OOO =O0OOOO00OO0OO00OO ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O0OO0O00O0OO00OOO}')#line:1001
                        if OOOOO00000OOOOOOO ==1 or OOOOO00000OOOOOOO ==2 or OOOOO00000OOOOOOO ==3 :#line:1002
                            O00O0O0O0O0O0OO0O =O0OOOO00OO0OO00OO ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{O00O0O0O0O0O0OO0O}')#line:1004
                        if OOOOO00000OOOOOOO ==4 or OOOOO00000OOOOOOO ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OOOOO00000OOOOOOO =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OO00OOOO00OO00 :#line:1046
            print (OO0OO00OOOO00OO00 )#line:1047
    def friends_invitation (OO0000OOOOOOOOO00 ):#line:1050
        try :#line:1051
            O0O0000OO00OO0O0O =f'__{timi_new()}'#line:1052
            O0O000OOOOO0O000O ={'source':'scsc','authorization':OO0000OOOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO00OO0O0O ),'signstring':O0O0000OO00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O00OO000O00OO0O0O =requests .request ('get',f'{host}/friends',headers =O0O000OOOOO0O000O ).json ()#line:1064
            if 'status'in O00OO000O00OO0O0O :#line:1065
                if O00OO000O00OO0O0O ['status']==200 :#line:1066
                    OOOO0OO000OO0OOOO =O00OO000O00OO0O0O ['data']['myInviteter']#line:1067
                    if OOOO0OO000OO0OOOO :#line:1068
                        O00O00O00OO0OOO00 =OOOO0OO000OO0OOOO ['user']['nickname']#line:1069
                        O0OO00OO0OOOO0OOO =OO0000OOOOOOOOO00 .certification ()#line:1070
                        if O0OO00OO0OOOO0OOO =='未实名':#line:1071
                            weishim .append (OO0000OOOOOOOOO00 .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O00O00O00OO0OOO00}丨实名:{O0OO00OO0OOOO0OOO}')#line:1073
        except Exception as O00OO00OOOOO0O0OO :#line:1077
            print (O00OO00OOOOO0O0OO )#line:1078
    def add_clover (O0O0O0OO0000OO00O ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            OO00O00OO0O0O0OO0 =f'__{timi_new()}'#line:1084
            O000OOO0O0OO000O0 ={'source':'scsc','authorization':O0O0O0OO0000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0O0O0OO0 ),'signstring':OO00O00OO0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            O00O000O0000OOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O000OOO0O0OO000O0 ).json ()#line:1096
            if 'status'in O00O000O0000OOOOO :#line:1098
                if O00O000O0000OOOOO ['status']==200 :#line:1099
                    O0O000O000O00O000 =O00O000O0000OOOOO ['data']['clover']#line:1100
                    O000000OO000O0O0O =O00O000O0000OOOOO ['data']['used_clover']#line:1101
                    OO00OO0OOOOOOOOOO =float (O0O000O000O00O000 )-float (O000000OO000O0O0O )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000000OO000O0O0O}')#line:1103
                    if O0O0O0OO0000OO00O .certification ()!='未实名':#line:1104
                        if OO00OO0OOOOOOOOOO >1 :#line:1105
                            OO00O00OO0O0O0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00OO0OOOOOOOOOO)}_{timi_new()}'#line:1106
                            O0OO0OO00OO00O000 ={'source':'scsc','authorization':O0O0O0OO0000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0O0O0OO0 ),'signstring':OO00O00OO0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            O000O000O0000OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00OO0OOOOOOOOOO )}#line:1118
                            OO00OOOO0O00OOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0OO00OO00O000 ,data =O000O000O0000OOO0 ).json ()#line:1119
                            if 'status'in OO00OOOO0O00OOOOO :#line:1121
                                if OO00OOOO0O00OOOOO ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{OO00OOOO0O00OOOOO["data"]["isSuccess"]}丨数量:{OO00OO0OOOOOOOOOO}')#line:1123
                                if OO00OOOO0O00OOOOO ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{OO00OOOO0O00OOOOO["message"]}')#line:1125
            O0O0O0000OO0O0OOO =requests .request ('get',f'{host}/lottery',headers =O000OOO0O0OO000O0 ).json ()#line:1126
            OO0O0O0O0O0OO0000 =O0O0O0OO0000OO00O .winning_rewards ()#line:1128
            if 'status'in O0O0O0000OO0O0OOO :#line:1129
                if O0O0O0000OO0O0OOO ['status']==200 :#line:1130
                    OO0OOOOOOO0000OO0 =O0O0O0000OO0O0OOO ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OO0OOOOOOO0000OO0 )#line:1132
                    O0O00OOO00OO0000O =O0O0O0000OO0O0OOO ['data'][1 ]['value']#line:1133
                    OO00O00OOOO0O0O00 =O0O0O0000OO0O0OOO ['data'][0 ]['join_number']#line:1134
                    OOO0O00O0O00O0O00 =int (float (O0O0O0000OO0O0OOO ['data'][0 ]['totalValue']))#line:1135
                    OO000000OO000O000 =float (O0O00OOO00OO0000O /OOO0O00O0O00O0O00 )*10000 #line:1136
                    O0O00OO0O00OO00O0 =OOO0O00O0O00O0O00 /OO00O00OOOO0O0O00 #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OO0OOOOOOO0000OO0)[:6]}颗金种子丨好友收益:{str(OO0O0O0O0O0OO0000)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OO000000OO000O000)[:6]}颗金种子丨☘️人均:{str(O0O00OO0O00OO00O0)[:7]}️')#line:1139
        except Exception as O0O000OO000OO0O00 :#line:1140
            print (O0O000OO000OO0O00 )#line:1141
    def energy (O00OOOOO0O0O000O0 ):#line:1144
        try :#line:1145
            while True :#line:1146
                O0O0O0000OO0OOO0O =f'__{timi_new()}'#line:1147
                O00O0OO00OOO000OO ={'source':'scsc','authorization':O00OOOOO0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OO0OOO0O ),'signstring':O0O0O0000OO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OO000OO0O00O000O0 =requests .request ('get',f'{host}/energy/general',headers =O00O0OO00OOO000OO ).json ()#line:1159
                if 'status'in OO000OO0O00O000O0 :#line:1161
                    if OO000OO0O00O000O0 ['status']==200 :#line:1162
                        O00O00O0OO000O0O0 =OO000OO0O00O000O0 ['data']['ordinary_water']#line:1163
                        OOO00O0OOOOOO000O =OO000OO0O00O000O0 ['data']['ordinary_fertilizer']#line:1164
                        OOOOO000O0OOOO000 =OO000OO0O00O000O0 ['data']['videoStatus']#line:1165
                        O00O0O00O000O000O =OO000OO0O00O000O0 ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(OOO00O0OOOOOO000O).split(".")[0]}丨水滴:{str(O00O00O0OO000O0O0).split(".")[0]}')#line:1168
                        if float (OOO00O0OOOOOO000O )<96 :#line:1169
                            if OOOOO000O0OOOO000 :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                O0O000O00O0O00OOO =99 -float (OOO00O0OOOOOO000O )#line:1172
                                OOO0OOOO00O0O0O0O ={"fertilizer":str (O0O000O00O0O00OOO ).split ('.')[0 ]}#line:1173
                                OO000O000OO000000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0OO00OOO000OO ).json ()#line:1175
                                if 'status'in OO000O000OO000000 :#line:1177
                                    if OO000O000OO000000 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O000OO000000["message"]}')#line:1179
                                    if OO000O000OO000000 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O000OO000000["message"]}')#line:1181
                                        break #line:1182
                                if float (OOO00O0OOOOOO000O )<78 :#line:1184
                                    O0O000O00O0O00OOO =80 -float (OOO00O0OOOOOO000O )#line:1185
                                    OOO000O00O0OO0OO0 =f'_fertilizer={int(O0O000O00O0O00OOO)}_{timi_new()}'#line:1186
                                    OOOO0OO0OO00000OO ={'source':'scsc','authorization':O00OOOOO0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O0OO0OO0 ),'signstring':OOO000O00O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    O0O00OO00O0OOOOOO ={"fertilizer":int (O0O000O00O0O00OOO )}#line:1198
                                    OO000O0O000OOOO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0OO0OO00000OO ,data =O0O00OO00O0OOOOOO ).json ()#line:1200
                                    if 'status'in OO000O0O000OOOO0O :#line:1202
                                        if OO000O0O000OOOO0O ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OO000O0O000OOOO0O["message"]}丨数量:{int(O0O000O00O0O00OOO)}')#line:1204
                                        if OO000O0O000OOOO0O ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OO000O0O000OOOO0O["message"]}丨数量:{int(O0O000O00O0O00OOO)}')#line:1206
                                            O000O000O0OOO0000 =OO000O0O000OOOO0O ["message"].split ('-')[1 ]#line:1207
                                            O0O0O0O00O0O00OO0 =f'__{timi_new()}'#line:1208
                                            OO0O0OOO0OOOOOOOO ={'source':'scsc','authorization':O00OOOOO0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0O00OO0 ),'signstring':O0O0O0O00O0O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OO00OO0000OO00O00 =requests .request ('get',f'{host}/user',headers =OO0O0OOO0OOOOOOOO ).json ()#line:1220
                                            if 'status'in OO00OO0000OO00O00 :#line:1221
                                                if OO00OO0000OO00O00 ['status']==200 :#line:1222
                                                    O0O00OO0000000O0O =OO00OO0000OO00O00 ['data']['inner_id']#line:1223
                                                    if give_gold (O0O00OO0000000O0O ,float (O000O000O0OOO0000 )+1 ):#line:1224
                                                        O00OOOOO0O0O000O0 .energy ()#line:1225
                        if float (O00O00O0OO000O0O0 )<880 :#line:1226
                            if O00O0O00O000O000O :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                O00O000O00OOO00OO =999 -float (O00O00O0OO000O0O0 )#line:1229
                                O0OO00O0O0000OOOO ={"water":str (O00O000O00OOO00OO ).split ('.')[0 ]}#line:1230
                                OOO0OO00O00OOO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0OO00OOO000OO ).json ()#line:1232
                                if 'status'in OOO0OO00O00OOO0OO :#line:1234
                                    if OOO0OO00O00OOO0OO ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OO00O00OOO0OO["message"]}')#line:1236
                                    if OOO0OO00O00OOO0OO ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OO00O00OOO0OO["message"]}')#line:1238
                                        break #line:1239
                                if float (O00O00O0OO000O0O0 )<780 :#line:1240
                                    O00O000O00OOO00OO =800 -float (O00O00O0OO000O0O0 )#line:1241
                                    O000OOOO0OOO00O0O =f'_water={int(O00O000O00OOO00OO)}_{timi_new()}'#line:1242
                                    OOOO0OO0OOO0OO000 ={'source':'scsc','authorization':O00OOOOO0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0OOO00O0O ),'signstring':O000OOOO0OOO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O000OOOOOO0O00000 ={"water":int (O00O000O00OOO00OO )}#line:1254
                                    O0000O0O0O000O0O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0OO0OOO0OO000 ,data =O000OOOOOO0O00000 ).json ()#line:1256
                                    if 'status'in O0000O0O0O000O0O0 :#line:1258
                                        if O0000O0O0O000O0O0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O0000O0O0O000O0O0["message"]}丨数量:{int(O00O000O00OOO00OO)}')#line:1260
                                        if O0000O0O0O000O0O0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O0000O0O0O000O0O0["message"]}丨数量:{int(O00O000O00OOO00OO)}')#line:1262
                                            O000O000O0OOO0000 =O0000O0O0O000O0O0 ["message"].split ('-')[1 ]#line:1263
                                            O0O0O0O00O0O00OO0 =f'__{timi_new()}'#line:1264
                                            OO0O0OOO0OOOOOOOO ={'source':'scsc','authorization':O00OOOOO0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0O00OO0 ),'signstring':O0O0O0O00O0O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OO00OO0000OO00O00 =requests .request ('get',f'{host}/user',headers =OO0O0OOO0OOOOOOOO ).json ()#line:1276
                                            if 'status'in OO00OO0000OO00O00 :#line:1277
                                                if OO00OO0000OO00O00 ['status']==200 :#line:1278
                                                    O0O00OO0000000O0O =OO00OO0000OO00O00 ['data']['inner_id']#line:1279
                                                    if give_gold (O0O00OO0000000O0O ,float (O000O000O0OOO0000 )+1 ):#line:1280
                                                        O00OOOOO0O0O000O0 .energy ()#line:1281
                        break #line:1282
        except Exception as OO00O00OOOO0O0OO0 :#line:1283
            print (OO00O00OOOO0O0OO0 )#line:1284
def bundled_def ():#line:1287
    OOOOOOO00OOOOO00O =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OOOOOOO00OOOOO00O [random .randint (0 ,len (OOOOOOO00OOOOO00O )-1 )]#line:1289
def version_of_the_validation ():#line:1293
    return str ((103 -56 )/10 )#line:1294
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
        O00OO0OO0O0OO00OO =gitee_edition ()#line:1328
        if version_of_the_validation ()<O00OO0OO0O0OO00OO ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0OO0O0OO00OO["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O00OO0OO0O0OO00OO["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0OO0O0OO00OO["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O00OO0OO0O0OO00OO["CityEarth"]["content"]}')#line:1334
    except Exception as OOOOO00OOOOOO0OOO :#line:1335
        print (OOOOO00OOOOOO0OOO )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
