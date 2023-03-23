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
@ 版本  5.1
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554351111'#line:1
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
        O0O00OO00000O0O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0O00OO00000O0O0O)}个账号==========")#line:17
        for OOOO00OO00O00000O in O0O00OO00000O0O0O :#line:18
            O0OO0OOOO0O0OO0O0 =[]#line:19
            print (f"------------正在执行第{O0O00OO00000O0O0O.index(OOOO00OO00O00000O) + 1}个账号------------")#line:20
            O000OO0O0O0000OO0 =CityEarth (OOOO00OO00O00000O ,O0OO0OOOO0O0OO0O0 ,O0O00OO00000O0O0O .index (OOOO00OO00O00000O ))#line:21
            def OO0000O00O0O0O00O ():#line:23
                if O000OO0O0O0000OO0 .base_info ():#line:25
                    O000OO0O0O0000OO0 .sealing ()#line:27
                    O000OO0O0O0000OO0 .invitenum ()#line:29
                    O000OO0O0O0000OO0 .query_to_sell ()#line:31
                    O000OO0O0O0000OO0 .friends_invitation ()#line:35
                    O000OO0O0O0000OO0 .energy ()#line:37
                    O000OO0O0O0000OO0 .add_clover ()#line:39
                    O000OO0O0O0000OO0 .propsraffle ()#line:41
                    O000OO0O0O0000OO0 .synthetic ()#line:43
                    O000OO0O0O0000OO0 .crops_illustrated ()#line:45
                    O000OO0O0O0000OO0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O000OO0O0O0000OO0 .give_gold ()#line:50
            O00O0OO00OOO00OOO =threading .Thread (target =OO0000O00O0O0O00O )#line:52
            O00O0OO00OOO00OOO .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO000O0OO000OO00O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO000O0OO000OO00O )#line:58
        time .sleep (3 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOOO00OOOO00OO00 in invited_new :#line:62
            print (OOOOO00OOOO00OO00 )#line:63
        print ('开始打印未实名的token')#line:64
        for O000OOOO00O0O0OO0 in weishim :#line:65
            print (O000OOOO00O0O0OO0 )#line:66
    except Exception as OOOOO0000OO00O000 :#line:67
        print (OOOOO0000OO00O000 )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (O00O000O00O00OO00 ,O0OOO00OO00O0OOO0 ):#line:78
    try :#line:79
        OO0O00OOO0OO0OO0O =f'_doneeNo={O00O000O00O00OO00}&quantity={int(O0OOO00OO00O0OOO0)}_{timi_new()}'#line:80
        OOO0OO00OO0O0O0OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0OO0OO0O ),'signstring':OO0O00OOO0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        O000OO0O0000O00O0 ={"quantity":int (O0OOO00OO00O0OOO0 ),"doneeNo":O00O000O00O00OO00 }#line:95
        OOO0O0000O000000O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OO00OO0O0O0OO ,data =O000OO0O0000O00O0 ).json ()#line:96
        if 'status'in OOO0O0000O000000O :#line:98
            if OOO0O0000O000000O ['status']==200 :#line:99
                if OOO0O0000O000000O ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(O0OOO00OO00O0OOO0)}种子给{O00O000O00O00OO00}成功')#line:101
                    return True #line:102
            if OOO0O0000O000000O ['status']==401 :#line:103
                print (f'【赠送种子】:{OOO0O0000O000000O["message"]}')#line:104
                return False #line:105
            if OOO0O0000O000000O ['status']==500 :#line:106
                print (f'【赠送种子】:{OOO0O0000O000000O["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as OOOO00O0O00O00O00 :#line:110
        print (OOOO00O0O00O00O00 )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (O0OOO0OOO0O000O0O ):#line:121
    OO00OOO0OO00O00OO =hashlib .md5 (O0OOO0OOO0O000O0O .encode ()).hexdigest ()#line:122
    OO0OOO0O0O00O0O00 =sc1 ()#line:123
    O0O000000OOOO00O0 =sc2 ()#line:124
    OO0O0O00O0OOO0O00 =sc3 ()#line:125
    OO000OO00OOOO000O =OO0OOO0O0O00O0O00 +OO00OOO0OO00O00OO +O0O000000OOOO00O0 +OO0O0O00O0OOO0O00 #line:126
    OO00OO000OOOOOOOO =hashlib .md5 (OO000OO00OOOO000O .encode ()).hexdigest ()#line:127
    return OO00OO000OOOOOOOO #line:128
def format_msg ():#line:131
    OOO000O000OOO00O0 =""#line:132
    for O000OOOO0O00OOOO0 in msg_list :#line:133
        OOO000O000OOO00O0 +=str (O000OOOO0O00OOOO0 )+"\r\n"#line:134
    return OOO000O000OOO00O0 #line:135
def sc1 ():#line:138
    return "scsc%^&*"#line:139
def O000OO0O00OO00O00 ():#line:142
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:143
        ubbbf ()#line:144
    else :#line:145
        print (oyoy ())#line:146
        exit (1 )#line:147
def timi_new ():#line:150
    return str (int (time .time ()*1000 ))#line:151
json_path ="CityEarth_data.json"#line:154
json_path1 ="CityEarth_data.json"#line:155
dict ={}#line:156
def get_json_data (OOOOO000OOOOO0000 ,O0O00O0000O0O00O0 ,O00O000OOOO00OOO0 ,OOO0OOO00OOO00O00 ):#line:159
    with open (OOOOO000OOOOO0000 ,'rb')as O00O00OO00O00OOO0 :#line:160
        O0O0O0OO00OO0OOO0 =json .load (O00O00OO00O00OOO0 )#line:161
        O0O0O0OO00OO0OOO0 ['data'][O0O00O0000O0O00O0 ][O00O000OOOO00OOO0 ]=OOO0OOO00OOO00O00 #line:162
        O0OOO0OOO0OO0OO00 =O0O0O0OO00OO0OOO0 #line:163
    O00O00OO00O00OOO0 .close ()#line:164
    return O0OOO0OOO0OO0OO00 #line:165
def write_json_data (O000O00O00000OOO0 ):#line:168
    with open (json_path1 ,'w')as O0O000000O00O00OO :#line:169
        json .dump (O000O00O00000OOO0 ,O0O000000O00O00OO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    O0O000000O00O00OO .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (OOO0O0O00O0O00O00 ,OO000O00000OOOO0O ,O0000OOOO00OOOOOO ,O00OOOOOOOOO0OOOO ):#line:177
        try :#line:178
            OOO0O0O00O0O00O00 .msg =O0000OOOO00OOOOOO #line:179
            OOO0O0O00O0O00O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            OOO0O0O00O0O00O00 .token =OO000O00000OOOO0O ['authorization']#line:181
            OOO0O0O00O0O00O00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            OOO0O0O00O0O00O00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            OOO0O0O00O0O00O00 .elephant_user =OO000O00000OOOO0O ['elephant_user']#line:184
            OOO0O0O00O0O00O00 .elephant_pswd =OO000O00000OOOO0O ['elephant_pswd']#line:185
            OOO0O0O00O0O00O00 .elephant_Task_ID =OO000O00000OOOO0O ['elephant_Task_ID']#line:186
            OOO0O0O00O0O00O00 .len_new =O00OOOOOOOOO0OOOO #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (OOO0OO0OOO000OOO0 ):#line:192
        try :#line:193
            OOO0OO0OOO000OOO0 .watched_ad ()#line:195
            O0OOO0O0OO000O0OO =f'__{timi_new()}'#line:196
            OO000000O0OOOOO00 ={'source':'scsc','authorization':OOO0OO0OOO000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0OO000O0OO ),'signstring':O0OOO0O0OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O0O0000OO000000 =requests .request ('get',f'{host}/user',headers =OO000000O0OOOOO00 ).json ()#line:208
            if 'status'in O0O0O0000OO000000 :#line:210
                if O0O0O0000OO000000 ['status']==200 :#line:211
                    O0OOO0OO0O0000O0O =O0O0O0000OO000000 ['data']['nickname']#line:212
                    OO0O0OO0O00OO0000 =O0O0O0000OO000000 ['data']['inner_id']#line:213
                    OO0O00OO00O00O0O0 =O0O0O0000OO000000 ['data']['assets']['gold']#line:214
                    OOOO000O0O0O000OO =O0O0O0000OO000000 ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{O0OOO0OO0O0000O0O[:5]}丨ID:{OO0O0OO0O00OO0000}丨等级:{OOOO000O0O0O000OO}丨金种子:{str(OO0O00OO00O00O0O0).split(".")[0]}')#line:217
                    if 'wx_'in O0OOO0OO0O0000O0O :#line:218
                        OOO0OO0OOO000OOO0 .change_nickname ()#line:219
                if O0O0O0000OO000000 ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if OOO0OO0OOO000OOO0 .elephant_user =='f':#line:222
                        return False #line:223
                    O0O0O0O0OO0OOOOOO =Invalid_login .addtask (elephant_user =OOO0OO0OOO000OOO0 .elephant_user ,elephant_pswd =OOO0OO0OOO000OOO0 .elephant_pswd ,elephant_Task_ID =OOO0OO0OOO000OOO0 .elephant_Task_ID )#line:226
                    O00OOO000OO00O0O0 =get_json_data (json_path ,OOO0OO0OOO000OOO0 .len_new ,'authorization',O0O0O0O0OO0OOOOOO )#line:227
                    if write_json_data (O00OOO000OO00O0O0 ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if O0O0O0000OO000000 ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as O000000000O00O000 :#line:234
            print (O000000000O00O000 )#line:235
    def sealing (OOO000OOOOOOOO0O0 ):#line:238
        try :#line:239
            OO0OO00O0OOO000O0 =f'__{timi_new()}'#line:240
            OO00O0OOOO0O000OO ={'source':'scsc','authorization':OOO000OOOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O0OOO000O0 ),'signstring':OO0OO00O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O0OOOO0O000OO )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =OO00O0OOOO0O000OO )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O0OOOO0O000OO )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O0OOOO0O000OO )#line:255
            requests .request ('get',f'{host}/user',headers =OO00O0OOOO0O000OO )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O0OOOO0O000OO )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O0OOOO0O000OO )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O0OOOO0O000OO )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OOOO0O000OO )#line:260
            requests .request ('get',f'{host}/assets',headers =OO00O0OOOO0O000OO )#line:261
        except Exception as OOOO0O0O00OO000OO :#line:262
            print (OOOO0O0O00OO000OO )#line:263
    def ddd (O000000O0OOO0OO0O ):#line:265
        try :#line:266
            O0O0OO000O0O00OOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            O00OOO0O00OO0O00O ={'source':'scsc','authorization':O000000O0OOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000O0O00OOO ),'signstring':O0O0OO000O0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            O0O0O0O00OOO0OO00 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00OOO0O00OO0O00O ).json ()#line:279
            print (O0O0O0O00OOO0OO00 )#line:280
        except Exception as OOO0OOOO00O00O0O0 :#line:283
            print (OOO0OOOO00O00O0O0 )#line:284
    def the_query (OO00OO0O0OO00O000 ):#line:289
        try :#line:290
            OOOOOOO0OO0OO0000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            OOOOOOO0OOO0O0OOO ={'authorization':OO00OO0O0OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OO0OO0000 ),'signstring':OOOOOOO0OO0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            OOOO00000O0OO000O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOOOOOO0OOO0O0OOO ).json ()#line:302
            if 'status'in OOOO00000O0OO000O :#line:304
                if OOOO00000O0OO000O ['status']==200 :#line:305
                    return OOOO00000O0OO000O ['data']['rows'][4 ]['price']#line:306
        except Exception as OOOO00OOO00O0OOO0 :#line:307
            print (OOOO00OOO00O0OOO0 )#line:308
    def market_sale (OOO0OOOOOOO0O00O0 ,O00OO00OOOOO00OO0 ):#line:311
        try :#line:312
            OOO000OO0OO00OO00 =timi_new ()#line:313
            O00O0O0OOO0OOO0OO =f'type=crop__{OOO000OO0OO00OO00}'#line:314
            OOO00O00OOOO0O0O0 ={'source':'scsc','authorization':OOO0OOOOOOO0O00O0 .token ,'timestamp':str (OOO000OO0OO00OO00 ),'sign':sign (O00O0O0OOO0OOO0OO ),'signstring':O00O0O0OOO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            O0OO000O00OO00O0O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOO00O00OOOO0O0O0 ).json ()#line:326
            if 'status'in O0OO000O00OO00O0O :#line:328
                if O0OO000O00OO00O0O ['status']==200 :#line:329
                    if O0OO000O00OO00O0O ['data']['rows']:#line:330
                        OOOO0OOO0OOO00000 =O0OO000O00OO00O0O ['data']['rows'][0 ]['packsackItemId']#line:331
                        OO0OOO00O00000000 =O0OO000O00OO00O0O ['data']['rows'][0 ]['quantity']#line:332
                        O0OO0OO00O0OOOOO0 =O00OO00OOOOO00OO0 #line:333
                        if float (O00OO00OOOOO00OO0 )>5 :#line:334
                            OO0OO0O0OOO000OO0 =f'_packsackItemId={OOOO0OOO0OOO00000}&price={str(O0OO0OO00O0OOOOO0)[:5]}&quantity={OO0OOO00O00000000}_{OOO000OO0OO00OO00}'#line:335
                            O0OO0OO0O0OOOO00O ={'source':'scsc','authorization':OOO0OOOOOOO0O00O0 .token ,'timestamp':str (OOO000OO0OO00OO00 ),'sign':sign (OO0OO0O0OOO000OO0 ),'signstring':OO0OO0O0OOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OO0O00000OOOO0OOO ={"packsackItemId":OOOO0OOO0OOO00000 ,"price":str (O0OO0OO00O0OOOOO0 )[:5 ],"quantity":str (OO0OOO00O00000000 )}#line:351
                            O000OOO0OOOOO0O0O =requests .request ('post',f'{host}/market/sale',headers =O0OO0OO0O0OOOO00O ,data =OO0O00000OOOO0OOO ).json ()#line:352
                            if 'status'in O000OOO0OOOOO0O0O :#line:354
                                if O000OOO0OOOOO0O0O ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{OO0OOO00O00000000}丨价格:{str(O0OO0OO00O0OOOOO0)[:5]}')#line:356
                                if O000OOO0OOOOO0O0O ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{O000OOO0OOOOO0O0O["message"]}')#line:358
        except Exception as OOOOOOO0OOO00O0O0 :#line:359
            print (OOOOOOO0OOO00O0O0 )#line:360
    def query_to_sell (OO0O0OOO0O00OOOOO ):#line:363
        try :#line:364
            OO0O00OO0000000O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:365
            O0OO000OOOO0OO000 ={'source':'scsc','authorization':OO0O0OOO0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0000000O0 ),'signstring':OO0O00OO0000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:376
            O00O00000OO000OOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO000OOOO0OO000 ).json ()#line:377
            if 'status'in O00O00000OO000OOO :#line:379
                if O00O00000OO000OOO ['status']==200 :#line:380
                    for O0000000OO00000OO in O00O00000OO000OOO ['data']['rows']:#line:381
                        OO0O0O0O0OOOOO0OO =O0000000OO00000OO ['materialKey']#line:382
                        O0OO0OOOOOO000OOO =O0000000OO00000OO ['quantity']#line:383
                        O0OO0OOOOO0O0OOO0 =O0000000OO00000OO ['price']#line:384
                        OO00OO00O0O0OOOO0 =O0000000OO00000OO ['saleState']#line:385
                        if OO00OO00O0O0OOOO0 ==0 :#line:386
                            print (f'【出售订单】:名称:{OO0O0O0O0OOOOO0OO}丨数量:{O0OO0OOOOOO000OOO}丨价格:{O0OO0OOOOO0O0OOO0}')#line:387
                            O00OOO0OOOO0OO0O0 =OO0O0OOO0O00OOOOO .the_query ()#line:389
                            if float (O00OOO0OOOO0OO0O0 )!=float (O0OO0OOOOO0O0OOO0 ):#line:390
                                O0OO0OOOOO0OOO0OO =O0000000OO00000OO ['id']#line:391
                                OO0O0OOO0O00OOOOO .cacel_sale (O0OO0OOOOO0OOO0OO )#line:392
                    OO0O0OOO0O00OOOOO .game_map ()#line:394
        except Exception as OO00OOO0OO0000O00 :#line:396
            print (OO00OOO0OO0000O00 )#line:397
    def cacel_sale (O000O0O0OOO0000OO ,O0O0OOO0O0O00O00O ):#line:400
        try :#line:401
            O0O00O0OOO0OOOO00 =f'_saleId={O0O0OOO0O0O00O00O}_{timi_new()}'#line:402
            OOO00OOO0OOO000OO ={'source':'scsc','authorization':O000O0O0OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO0OOOO00 ),'signstring':O0O00O0OOO0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            O0O00000000O0OO00 ={"saleId":O0O0OOO0O0O00O00O }#line:414
            O00000OOOOOOO0OOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO00OOO0OOO000OO ,data =O0O00000000O0OO00 ).json ()#line:415
            if 'status'in O00000OOOOOOO0OOO :#line:417
                if O00000OOOOOOO0OOO ['status']==200 :#line:418
                    print (f'【下架出售】:{O00000OOOOOOO0OOO["data"]}')#line:419
        except Exception as O000O00000O0O00O0 :#line:420
            print (O000O00000O0O00O0 )#line:421
    def change_nickname (O000O0O00O00O0000 ):#line:424
        try :#line:425
            OO0O000O0O0000OOO =timi_new ()#line:426
            O0OOO00O0000OO00O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOO0000OOO00OOO0O =requests .request ('post','https://www.qmsjmfb.com/',data =O0OOO00O0000OO00O ).text #line:428
            O0000OOO0OO00000O =re .findall ('<ul><li>(.*?)</li>',OOO0000OOO00OOO0O )[0 ][:3 ]#line:429
            OO00000O00O000000 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0000OOO0OO00000O}').json ()#line:430
            OOO000OO0O00O0O0O =OO00000O00O000000 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:431
            OOOO0OOOO00O0O0OO ={"nickname":OOO000OO0O00O0O0O }#line:432
            O00OOOOO00O0000OO =f'_nickname={OOO000OO0O00O0O0O}_{OO0O000O0O0000OOO}'#line:433
            OO0O0O000OOOO00O0 ={'source':'scsc','authorization':O000O0O00O00O0000 .token ,'timestamp':OO0O000O0O0000OOO ,'sign':sign (O00OOOOO00O0000OO ),'signstring':O00OOOOO00O0000OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O0OO0OO0000O0O0O0 =requests .request ('patch',f'{host}/user/nickname',headers =OO0O0O000OOOO00O0 ,data =OOOO0OOOO00O0O0OO ).json ()#line:445
            if 'status'in O0OO0OO0000O0O0O0 :#line:447
                if O0OO0OO0000O0O0O0 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{OOO000OO0O00O0O0O}丨{O0OO0OO0000O0O0O0["message"]}')#line:449
        except Exception as O0O0O00O0OOO00O00 :#line:450
            print (O0O0O00O0OOO00O00 )#line:451
    def withdraw (OO0O00OOO00000OO0 ):#line:454
        try :#line:455
            O0000O0OOO0O000O0 =f'__{timi_new()}'#line:456
            OOOO000000OOOOOOO ={'source':'scsc','authorization':OO0O00OOO00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOO0O000O0 ),'signstring':O0000O0OOO0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O0O00O0OOOO00O0O0 =requests .request ('get',f'{host}/assets',headers =OOOO000000OOOOOOO ).json ()#line:468
            if 'status'in O0O00O0OOOO00O0O0 :#line:470
                if O0O00O0OOOO00O0O0 ['status']==200 :#line:471
                    OOOOO00OO0OOOO0OO =O0O00O0OOOO00O0O0 ['data']['cash']#line:472
                    if float (OOOOO00OO0OOOO0OO )>20 :#line:473
                        O0000O0OOO0O000O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        OOOO000000OOOOOOO ={'authorization':OO0O00OOO00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOO0O000O0 ),'signstring':O0000O0OOO0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OO0OOO000OO0OOOO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        O00OOO00000OO00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO000000OOOOOOO ,data =OO0OOO000OO0OOOO0 ).json ()#line:487
                        if 'status'in O00OOO00000OO00O0 :#line:489
                            if O00OOO00000OO00O0 ['status']==200 :#line:490
                                print (f'【余额提现】:{O00OOO00000OO00O0["data"]}')#line:491
                        if 'status'in O00OOO00000OO00O0 :#line:492
                            if O00OOO00000OO00O0 ['status']==500 :#line:493
                                print (f'【余额提现】:{O00OOO00000OO00O0["message"]}')#line:494
        except Exception as OO0O0OOOOO0OOO000 :#line:495
            print (OO0O0OOOOO0OOO000 )#line:496
    def invitenum (O0OOO00000O00O0O0 ):#line:499
        global invited_new #line:500
        try :#line:501
            O0OOOOO0000OOO00O =f'__{timi_new()}'#line:502
            OOOO00O0O00OOOO0O ={'source':'scsc','authorization':O0OOO00000O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0000OOO00O ),'signstring':O0OOOOO0000OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            OOOOOO0OOOOO000OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO00O0O00OOOO0O ).json ()#line:514
            if 'status'in OOOOOO0OOOOO000OO :#line:516
                if OOOOOO0OOOOO000OO ['status']==200 :#line:517
                    O00000O0OO0OOO0OO =OOOOOO0OOOOO000OO ['data']['invited_count']#line:518
                    O00OOO0O00O0O0OOO =OOOOOO0OOOOO000OO ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O00000O0OO0OOO0OO}丨间邀好友:{O00OOO0O00O0O0OOO}')#line:520
                    if O00000O0OO0OOO0OO <2 :#line:521
                        O000OO0OO000O00OO =f'__{timi_new()}'#line:522
                        OOO0O00O000OOOO0O ={'source':'scsc','authorization':O0OOO00000O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OO000O00OO ),'signstring':O000OO0OO000O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OO0OO00000OOO000O =requests .request ('get',f'{host}/user',headers =OOO0O00O000OOOO0O ).json ()#line:534
                        if 'status'in OO0OO00000OOO000O :#line:536
                            if OO0OO00000OOO000O ['status']==200 :#line:537
                                invited_new .append (OO0OO00000OOO000O ['data']['inner_id'])#line:538
        except Exception as OOO00O000OO000OOO :#line:539
            print (OOO00O000OO000OOO )#line:540
    def game_map (O000OOO0O000OO0O0 ):#line:543
        global count_list #line:544
        try :#line:545
            OO0000O0OOO0O000O =f'__{timi_new()}'#line:546
            O00O0O0O00O0O0O00 ={'source':'scsc','authorization':O000OOO0O000OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0OOO0O000O ),'signstring':OO0000O0OOO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
            OO0000O0O000OOO0O =requests .request ('get',f'{host}/game/map',headers =O00O0O0O00O0O0O00 ).json ()#line:558
            if 'status'in OO0000O0O000OOO0O :#line:560
                if OO0000O0O000OOO0O ['status']==200 :#line:561
                    for OO0O00O0OOO0000O0 in OO0000O0O000OOO0O ['data']['list'][0 ]['crops']:#line:562
                        OOO000000O0OO000O =OO0O00O0OOO0000O0 ['level']#line:564
                        if OOO000000O0OO000O ==41 :#line:565
                            OOO0OOO0OOOOO000O =OO0O00O0OOO0000O0 ['crop_name']#line:566
                            O0O00O0OOO0O00000 =OO0O00O0OOO0000O0 ['count']#line:567
                            if O0O00O0OOO0O00000 >0 :#line:568
                                print (f'【农业资产】:{OOO0OOO0OOOOO000O}丨数量:{O0O00O0OOO0O00000}')#line:569
                                count_list +=float (O0O00O0OOO0O00000 )#line:570
                                OO000O00OOOO000OO =O000OOO0O000OO0O0 .the_query ()#line:571
                                O000OOO0O000OO0O0 .market_sale (OO000O00OOOO000OO )#line:572
        except Exception as OO0O000O0O0O00O0O :#line:573
            print (OO0O000O0O0O00O0O )#line:574
    def give_gold (O0O0O000O00OO0000 ):#line:577
        try :#line:578
            OO0OO00000O00O000 =f'__{timi_new()}'#line:579
            O0000O00OOO00000O ={'source':'scsc','authorization':O0O0O000O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000O00O000 ),'signstring':OO0OO00000O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            O0O00O0O000OOOOO0 =requests .request ('get',f'{host}/user',headers =O0000O00OOO00000O ).json ()#line:591
            if 'status'in O0O00O0O000OOOOO0 :#line:592
                if O0O00O0O000OOOOO0 ['status']==200 :#line:593
                    if float (O0O0O000O00OO0000 .doneeNo )!=0 :#line:594
                        OOOOOO000O0OO0OOO =O0O00O0O000OOOOO0 ['data']['assets']['gold']#line:595
                        if float (OOOOOO000O0OO0OOO )>float (O0O0O000O00OO0000 .innerId ):#line:596
                            O0OO0OO0OOO00O0OO =int (float (OOOOOO000O0OO0OOO )/1.1 )#line:597
                            OO0OO00000O00O000 =f'_doneeNo={O0O0O000O00OO0000.doneeNo}&quantity={O0OO0OO0OOO00O0OO}_{timi_new()}'#line:598
                            O0000O00OOO00000O ={'source':'scsc','authorization':O0O0O000O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000O00O000 ),'signstring':OO0OO00000O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O000OOO0O00000OOO ={"quantity":O0OO0OO0OOO00O0OO ,"doneeNo":O0O0O000O00OO0000 .doneeNo }#line:613
                            O00000OOOO0000O0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0000O00OOO00000O ,data =O000OOO0O00000OOO ).json ()#line:614
                            if 'status'in O00000OOOO0000O0O :#line:616
                                if O00000OOOO0000O0O ['status']==200 :#line:617
                                    if O00000OOOO0000O0O ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O0OO0OO0OOO00O0OO}种子给{O0O0O000O00OO0000.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as OOOO0O0O0OOOOO0OO :#line:622
            print (OOOO0O0O0OOOOO0OO )#line:623
    def invitation (OOOOOOOO00OOO00OO ):#line:625
        try :#line:626
            _O0OO00OO0OOO0OO0O =float (bundled_def ())/4 #line:627
            OO000000OOO000OO0 =f'_innerId={int(_O0OO00OO0OOO0OO0O)}_{timi_new()}'#line:629
            O0O00OOOOOO0O0O0O ={'source':'scsc','authorization':OOOOOOOO00OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OOO000OO0 ),'signstring':OO000000OOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            O0O0O0OO0O000OO0O ={"innerId":int (_O0OO00OO0OOO0OO0O )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00OOOOOO0O0O0O ,data =O0O0O0OO0O000OO0O )#line:642
        except Exception as OOO00000000O0000O :#line:643
            print (OOO00000000O0000O )#line:644
    def winning_rewards (OOO0O00OO0OOOOOOO ):#line:647
        try :#line:648
            O00O0OO0O0OO00O0O =f'__{timi_new()}'#line:649
            O00OOOOOO0000OOO0 ={'source':'scsc','authorization':OOO0O00OO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0O0OO00O0O ),'signstring':O00O0OO0O0OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            O0000OOO000O00O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OOOOOO0000OOO0 ).json ()#line:661
            if 'status'in O0000OOO000O00O0O :#line:663
                if O0000OOO000O00O0O ['status']==200 :#line:664
                    if O0000OOO000O00O0O ['data']['amount']:#line:665
                        O000O0000OOOO0O00 =O0000OOO000O00O0O ['data']['amount']['gold']#line:666
                        return O000O0000OOOO0O00 #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as OOO00O0O000O0OO0O :#line:670
            print (OOO00O0O000O0OO0O )#line:671
    def certification (OO0OO0O0O0O0OO0OO ):#line:674
        try :#line:675
            OO0O00000O0OO0O00 =f'__{timi_new()}'#line:676
            OOO000OOOO00000O0 ={'source':'scsc','authorization':OO0OO0O0O0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00000O0OO0O00 ),'signstring':OO0O00000O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O0O0OO0O00O0O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO000OOOO00000O0 ).json ()#line:688
            if 'status'in O0O0OO0O00O0O00O0 :#line:690
                if O0O0OO0O00O0O00O0 ['status']==200 :#line:691
                    if O0O0OO0O00O0O00O0 ['data']['result']:#line:692
                        OOOOOOOOOO0OOOOO0 =O0O0OO0O00O0O00O0 ['data']['nick_name']#line:693
                        return OOOOOOOOOO0OOOOO0 #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as O000OO0O00O00OO00 :#line:697
            print (O000OO0O00O00OO00 )#line:698
    def crops_illustrated (OOOO00OOOOO0OO00O ):#line:701
        try :#line:702
            OO0OOO0O00O0OOOOO =f'__{timi_new()}'#line:703
            OOO0O000O000OO00O ={'source':'scsc','authorization':OOOO00OOOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O00O0OOOOO ),'signstring':OO0OOO0O00O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            OO0OOOOO000O00000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O000O000OO00O ).json ()#line:715
            if 'status'in OO0OOOOO000O00000 :#line:717
                if OO0OOOOO000O00000 ['status']==200 :#line:718
                    O0O0O0O0OOO0O0O00 =OO0OOOOO000O00000 ['data'][0 ]['crops']#line:719
                    for OOOO00OOO000OO000 in O0O0O0O0OOO0O0O00 :#line:720
                        if OOOO00OOO000OO000 ['ill_clover_award']:#line:721
                            if float (OOOO00OOO000OO000 ['ill_clover_award'])>1 :#line:722
                                if OOOO00OOO000OO000 ['is_finish']:#line:723
                                    if not OOOO00OOO000OO000 ['is_getit']:#line:724
                                        if OOOO00OOOOO0OO00O .certification ()!='未实名':#line:725
                                            OO0OOO0O00O0OOOOO =f'_award_level={OOOO00OOO000OO000["level"]}_{timi_new()}'#line:726
                                            OOO0O000O000OO00O ={'source':'scsc','authorization':OOOO00OOOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O00O0OOOOO ),'signstring':OO0OOO0O00O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            OOO00000000OO0OO0 ={"award_level":OOOO00OOO000OO000 ['level']}#line:738
                                            O0O00000000O00000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O000O000OO00O ,json =OOO00000000OO0OO0 ).json ()#line:740
                                            if 'status'in O0O00000000O00000 :#line:741
                                                if O0O00000000O00000 ['status']==200 :#line:742
                                                    OO00O000OO00O0O00 =O0O00000000O00000 ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{OOOO00OOO000OO000["crop_name"]}成就丨奖励{OO00O000OO00O0O00}☘️')#line:745
                                                if O0O00000000O00000 ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{O0O00000000O00000["message"]}')#line:747
        except Exception as OO00OOO000OOO000O :#line:748
            print (OO00OOO000OOO000O )#line:749
    def watched_ad (OOO00OO00O0OOO000 ):#line:752
        try :#line:753
            OO0OO0000O00OOOOO =f'__{timi_new()}'#line:754
            O0O0O0OOO0000000O ={'source':'scsc','authorization':OOO00OO00O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000O00OOOOO ),'signstring':OO0OO0000O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            O0OOOOO0O0OOO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO0000000O ).json ()#line:766
            if 'status'in O0OOOOO0O0OOO0O00 :#line:768
                if O0OOOOO0O0OOO0O00 ['status']==200 :#line:769
                    if 'offlineInfo'in O0OOOOO0O0OOO0O00 ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        O00OO00O0O00O00O0 =O0OOOOO0O0OOO0O00 ['data']['offlineInfo']['off_minute']#line:772
                        O0O000O000OO0O00O =float (O0OOOOO0O0OOO0O00 ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O0OOO0000000O ).json ()#line:775
                        time .sleep (2 )#line:776
                        OO00OOO0O0O000O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO0000000O ).json ()#line:777
                        if 'status'in OO00OOO0O0O000O00 :#line:779
                            if OO00OOO0O0O000O00 ['status']==200 :#line:780
                                O0OOO0OOOOO000O0O =float (OO00OOO0O0O000O00 ['data']['silver'])/1000000000000 #line:781
                                OOOO000OO00OOO0O0 =str (O0OOO0OOOOO000O0O -O0O000O000OO0O00O )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{O00OO00O0O00O00O0}分钟奖励🌱数量:{OOOO000OO00OOO0O0}t粒')#line:783
        except Exception as OOO0O0OOO0O0O0O0O :#line:784
            print (OOO0O0OOO0O0O0O0O )#line:785
    def user_ad (OOOOO0000O0O000OO ):#line:788
        try :#line:789
            O0O0OOO0O0O0O000O =f'__{timi_new()}'#line:790
            O0O00O0000O0O00OO ={'source':'scsc','authorization':OOOOO0000O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O0O0O000O ),'signstring':O0O0OOO0O0O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            O0OO000O0O00OOO0O =requests .request ('get',f'{host}/user/ad',headers =O0O00O0000O0O00OO ).json ()#line:802
            if 'status'in O0OO000O0O00OOO0O :#line:804
                if O0OO000O0O00OOO0O ['status']==200 :#line:805
                    OO00O0O0OOO0O0O00 =O0OO000O0O00OOO0O ['data']['max_time']#line:806
                    O00OO0OOOOO00O00O =O0OO000O0O00OOO0O ['data']['watch_time']#line:807
                    O00O000O00OOOOO0O =O0OO000O0O00OOO0O ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{O00O000O00OOOOO0O + OO00O0O0OOO0O0O00 - O00OO0OOOOO00O00O}次丨好友提供:{O00O000O00OOOOO0O}次')#line:809
                    if O00O000O00OOOOO0O +OO00O0O0OOO0O0O00 -O00OO0OOOOO00O00O >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        OOOOO0O0O0OOOO0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00O0000O0O00OO ).json ()#line:812
                        if 'status'in OOOOO0O0O0OOOO0OO :#line:814
                            if OOOOO0O0O0OOOO0OO ['status']==200 :#line:815
                                OO0OOOOO0OOOOO0OO =float (OOOOO0O0O0OOOO0OO ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(OO0OOOOO0OOOOO0OO)}t粒')#line:817
                                return True #line:818
                            if OOOOO0O0O0OOOO0OO ['status']==500 :#line:819
                                OO00O0O0000000O00 =OOOOO0O0O0OOOO0OO ['message']#line:820
                                print (f'【获取种子】:{OO00O0O0000000O00}')#line:821
                                return False #line:822
        except Exception as OOO0O00O0000OO00O :#line:823
            print (OOO0O00O0000OO00O )#line:824
    def synthetic (OOOOO00O0OOOOO0O0 ):#line:827
        global id ,g #line:828
        try :#line:829
            OO000O0O000O00OOO =OOOOO00O0OOOOO0O0 .level_new ()#line:830
            O0OO0O0O0OOOOO000 =random .randint (9 ,11 )#line:831
            OOO00OOO00OOO0000 =f'_site=8&targetSite={O0OO0O0O0OOOOO000}_{timi_new()}'#line:832
            OO00OOO00O00O0OO0 ={'source':'scsc','authorization':OOOOO00O0OOOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO00OOO00OOO0000 ),'signstring':OOO00OOO00OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            OO0OO00OO00OO0OO0 ={"site":int (8 ),"targetSite":int (O0OO0O0O0OOOOO000 )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =OO00OOO00O00O0OO0 ,json =OO0OO00OO00OO0OO0 )#line:845
            while True :#line:846
                O0OOOOOOO0000O0OO =f'__{timi_new()}'#line:847
                O0OOOOOOO00OOOO0O ={'source':'scsc','authorization':OOOOO00O0OOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0000O0OO ),'signstring':O0OOOOOOO0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                OOO00O00OOO0OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOOOO00OOOO0O ).json ()#line:859
                if 'status'in OOO00O00OOO0OO0OO :#line:861
                    if OOO00O00OOO0OO0OO ['status']==200 :#line:862
                        O00OOO000000OOOOO =OOO00O00OOO0OO0OO ['data']['cropList']#line:863
                        O0OO000O0OO00O0OO =OOO00O00OOO0OO0OO ['data']['gameCoreDataDBid']#line:864
                        OO00O00O0OO0O00OO =float (OOO00O00OOO0OO0OO ['data']['silver'])/1000000000000 #line:865
                        O0O0OO00OO0O00O00 =0 #line:870
                        for O0O0O0O0O0O0000OO in O00OOO000000OOOOO :#line:871
                            if not O0O0O0O0O0O0000OO :#line:872
                                O0OO0000OO0OOO00O =f'_crop_id={O0OO000O0OO00O0OO}&site={O0O0OO00OO0O00O00}_{OOOOO00O0OOOOO0O0.time}'#line:873
                                O0OO00OOO0000O0O0 ={'source':'scsc','authorization':OOOOO00O0OOOOO0O0 .token ,'timestamp':OOOOO00O0OOOOO0O0 .time ,'sign':sign (O0OO0000OO0OOO00O ),'signstring':O0OO0000OO0OOO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                OOO0OOO0OO00OOO0O ={"site":O0O0OO00OO0O00O00 ,"crop_id":O0OO000O0OO00O0OO }#line:884
                                O00O0OOO0O0O0O00O =requests .request ('post',f'{host}/game/crops/buy',headers =O0OO00OOO0000O0O0 ,data =OOO0OOO0OO00OOO0O ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in O00O0OOO0O0O0O00O :#line:888
                                    if O00O0OOO0O0O0O00O ['status']==200 :#line:889
                                        if O00O0OOO0O0O0O00O ['message']=='种子数量不足':#line:890
                                            OO000O0O000O00OOO =OOOOO00O0OOOOO0O0 .level_new ()#line:891
                                            print (f'【种植合成】:{O00O0OOO0O0O0O00O["message"]}')#line:892
                                            if not OOOOO00O0OOOOO0O0 .user_ad ():#line:893
                                                return False #line:894
                                    if O00O0OOO0O0O0O00O ['status']==500 :#line:895
                                        print (f'【种植合成】:{O00O0OOO0O0O0O00O["message"]}')#line:896
                                        return False #line:897
                            O0O0OO00OO0O00O00 +=1 #line:898
                        O00O000OO00OO0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOOOO00OOOO0O ).json ()#line:899
                        O0OOO0000OOOOO000 =O00O000OO00OO0OO0 ['data']['cropList']#line:900
                        O00OO0O0OO0000OO0 =False #line:901
                        for O0O0O0O0O0O0000OO in range (12 ):#line:902
                            id =O0OOO0000OOOOO000 [O0O0O0O0O0O0000OO ]['level']#line:903
                            if float (OO000O0O000O00OOO )-float (id )>9 :#line:904
                                OOOO0OO000O000OO0 =f'_site={O0O0O0O0O0O0000OO}_{timi_new()}'#line:905
                                O00OO000OOO00OOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOO00O0OOOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO000O000OO0 ),'signstring':OOOO0OO000O000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                OO00OOO0O0OO0O00O ={"site":O0O0O0O0O0O0000OO }#line:917
                                O00000OOOOOO00OO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO000OOO00OOO0 ,data =OO00OOO0O0OO0O00O ).json ()#line:919
                                if 'status'in O00000OOOOOO00OO0 :#line:920
                                    if O00000OOOOOO00OO0 ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for OOO00OOO0OOO00OO0 in range (11 ):#line:924
                                    OOOOO0O00OO0OO000 =OOO00OOO0OOO00OO0 +1 #line:925
                                    g =O0OOO0000OOOOO000 [OOOOO0O00OO0OO000 ]['level']#line:926
                                    if id ==g :#line:927
                                        O000O00000OOOOOOO =OOO00OOO0OOO00OO0 +2 #line:928
                                        if O000O00000OOOOOOO !=O0O0O0O0O0O0000OO +1 :#line:929
                                            O00O0000O000OO0O0 =O0O0O0O0O0O0000OO +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            OOO00OOO00OOO0000 =f'_site={O00O0000O000OO0O0 - 1}&targetSite={O000O00000OOOOOOO - 1}_{timi_new()}'#line:933
                                            OO00OOO00O00O0OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOO00O0OOOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO00OOO00OOO0000 ),'signstring':OOO00OOO00OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            OO0OOO00O0OOOOO00 ={"site":int (O00O0000O000OO0O0 -1 ),"targetSite":int (O000O00000OOOOOOO -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00OOO00O00O0OO0 ,json =OO0OOO00O0OOOOO00 )#line:952
                                            O00OO0O0OO0000OO0 =True #line:954
                                    if O00OO0O0OO0000OO0 :#line:955
                                        break #line:956
                                if O00OO0O0OO0000OO0 :#line:957
                                    break #line:958
        except :#line:959
            OOOOO00O0OOOOO0O0 .synthetic ()#line:960
    def level_new (OOO0O0O0OO000OO00 ):#line:963
        try :#line:964
            OOO0OO00000000O0O =f'__{timi_new()}'#line:965
            OOOO0000OO0OOOOO0 ={'source':'scsc','authorization':OOO0O0O0OO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00000000O0O ),'signstring':OOO0OO00000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            O000OOO0O0OOO0OO0 =requests .request ('get',f'{host}/user',headers =OOOO0000OO0OOOOO0 ).json ()#line:977
            if 'status'in O000OOO0O0OOO0OO0 :#line:978
                if O000OOO0O0OOO0OO0 ['status']==200 :#line:979
                    return float (O000OOO0O0OOO0OO0 ['data']['level'])#line:980
        except Exception as OO00OO00000OO0O0O :#line:981
            print (OO00OO00000OO0O0O )#line:982
    def propsraffle (O0OO0O0OO0OOOO00O ):#line:985
        try :#line:986
            while True :#line:987
                O000O0O000000OO0O =f'__{timi_new()}'#line:988
                O00000O00O00O0O00 ={'source':'scsc','authorization':O0OO0O0OO0OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O000000OO0O ),'signstring':O000O0O000000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                O00OOOOO0O00O0OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00000O00O00O0O00 ).json ()#line:1000
                if 'status'in O00OOOOO0O00O0OOO :#line:1002
                    if O00OOOOO0O00O0OOO ['status']==200 :#line:1003
                        O00OOOO0O0O0O00O0 =O00OOOOO0O00O0OOO ['data']['rows']#line:1004
                        OOO0O0O0O0OO00000 =O00OOOOO0O00O0OOO ['data']['vstate']#line:1005
                        if O00OOOO0O0O0O00O0 ==5 or O00OOOO0O0O0O00O0 ==6 or O00OOOO0O0O0O00O0 ==7 :#line:1006
                            O0000000OOOO00O00 =O00OOOOO0O00O0OOO ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{O0000000OOOO00O00}')#line:1008
                        if O00OOOO0O0O0O00O0 ==1 or O00OOOO0O0O0O00O0 ==2 or O00OOOO0O0O0O00O0 ==3 :#line:1009
                            O0000O0O0OO0O0000 =O00OOOOO0O00O0OOO ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{O0000O0O0OO0O0000}')#line:1011
                        if O00OOOO0O0O0O00O0 ==4 or O00OOOO0O0O0O00O0 ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if O00OOOO0O0O0O00O0 =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as OO0O0OO000OO00OOO :#line:1053
            print (OO0O0OO000OO00OOO )#line:1054
    def friends_invitation (O0OO0OO000O00O000 ):#line:1057
        try :#line:1058
            O0O0O0O0OO000OO00 =f'__{timi_new()}'#line:1059
            O0OO00O0OO000OO00 ={'source':'scsc','authorization':O0OO0OO000O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO000OO00 ),'signstring':O0O0O0O0OO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            OO00OOOOO000O0O00 =requests .request ('get',f'{host}/friends',headers =O0OO00O0OO000OO00 ).json ()#line:1071
            if 'status'in OO00OOOOO000O0O00 :#line:1072
                if OO00OOOOO000O0O00 ['status']==200 :#line:1073
                    OOOOOOOO0O000O0OO =OO00OOOOO000O0O00 ['data']['myInviteter']#line:1074
                    if OOOOOOOO0O000O0OO :#line:1075
                        OO0OOOOOOO000000O =OOOOOOOO0O000O0OO ['user']['nickname']#line:1076
                        OO00O00000OO00OOO =O0OO0OO000O00O000 .certification ()#line:1077
                        if OO00O00000OO00OOO =='未实名':#line:1078
                            weishim .append (O0OO0OO000O00O000 .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{OO0OOOOOOO000000O}丨实名:{OO00O00000OO00OOO}')#line:1080
                    else :#line:1081
                        if O0OO0OO000O00O000 .innerId !='0':#line:1082
                            O0OO0OO000O00O000 .invitation ()#line:1083
        except Exception as O0OOO0OOO0OO00OO0 :#line:1084
            print (O0OOO0OOO0OO00OO0 )#line:1085
    def add_clover (OOOO0O000O0OOO0OO ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            O00OO0O0O00O0O0O0 =f'__{timi_new()}'#line:1091
            O00O0O0OOOOO00OO0 ={'source':'scsc','authorization':OOOO0O000O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O00O0O0O0 ),'signstring':O00OO0O0O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O000OO000OOO00O00 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0O0OOOOO00OO0 ).json ()#line:1103
            if 'status'in O000OO000OOO00O00 :#line:1105
                if O000OO000OOO00O00 ['status']==200 :#line:1106
                    OOO0OOOO0OOO000OO =O000OO000OOO00O00 ['data']['clover']#line:1107
                    O0OOOO000O000O000 =O000OO000OOO00O00 ['data']['used_clover']#line:1108
                    O00O000OO00000OO0 =float (OOO0OOOO0OOO000OO )-float (O0OOOO000O000O000 )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOOO000O000O000}')#line:1110
                    if OOOO0O000O0OOO0OO .certification ()!='未实名':#line:1111
                        if O00O000OO00000OO0 >1 :#line:1112
                            O00OO0O0O00O0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O000OO00000OO0)}_{timi_new()}'#line:1113
                            O0OOO0O0OO00OO00O ={'source':'scsc','authorization':OOOO0O000O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O00O0O0O0 ),'signstring':O00OO0O0O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            OOO0O000OO000OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O000OO00000OO0 )}#line:1125
                            OOO00OOOO0O0O000O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOO0O0OO00OO00O ,data =OOO0O000OO000OO00 ).json ()#line:1126
                            if 'status'in OOO00OOOO0O0O000O :#line:1128
                                if OOO00OOOO0O0O000O ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{OOO00OOOO0O0O000O["data"]["isSuccess"]}丨数量:{O00O000OO00000OO0}')#line:1130
                                if OOO00OOOO0O0O000O ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{OOO00OOOO0O0O000O["message"]}')#line:1132
            OO0O0OOOOO0OOO0OO =requests .request ('get',f'{host}/lottery',headers =O00O0O0OOOOO00OO0 ).json ()#line:1133
            OO000OO0OO000OOO0 =OOOO0O000O0OOO0OO .winning_rewards ()#line:1135
            if 'status'in OO0O0OOOOO0OOO0OO :#line:1136
                if OO0O0OOOOO0OOO0OO ['status']==200 :#line:1137
                    OO0OOOO0O0O000000 =OO0O0OOOOO0OOO0OO ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (OO0OOOO0O0O000000 )#line:1139
                    OOO0000000000OOOO =OO0O0OOOOO0OOO0OO ['data'][1 ]['value']#line:1140
                    OO0O0OOOO00OO0O0O =OO0O0OOOOO0OOO0OO ['data'][0 ]['join_number']#line:1141
                    OO00OO0000OO0OO00 =int (float (OO0O0OOOOO0OOO0OO ['data'][0 ]['totalValue']))#line:1142
                    OOO0O00O00O0O0OO0 =float (OOO0000000000OOOO /OO00OO0000OO0OO00 )*10000 #line:1143
                    O0OOO00000O00OO00 =OO00OO0000OO0OO00 /OO0O0OOOO00OO0O0O #line:1144
                    print (f'【参与抽奖】:预计每天中{str(OO0OOOO0O0O000000)[:6]}颗金种子丨好友收益:{str(OO000OO0OO000OOO0)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0O00O00O0O0OO0)[:6]}颗金种子丨☘️人均:{str(O0OOO00000O00OO00)[:7]}️')#line:1146
        except Exception as OO0OOOO000OOO0O00 :#line:1147
            print (OO0OOOO000OOO0O00 )#line:1148
    def energy (OOOO00O0O0O0OO000 ):#line:1151
        try :#line:1152
            while True :#line:1153
                O000OOOOOO00O0000 =f'__{timi_new()}'#line:1154
                O00OOOOO0OO000OOO ={'source':'scsc','authorization':OOOO00O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOOO00O0000 ),'signstring':O000OOOOOO00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                OOO0OOO0O0OOOO0OO =requests .request ('get',f'{host}/energy/general',headers =O00OOOOO0OO000OOO ).json ()#line:1166
                if 'status'in OOO0OOO0O0OOOO0OO :#line:1168
                    if OOO0OOO0O0OOOO0OO ['status']==200 :#line:1169
                        O00O0OO0OO000O000 =OOO0OOO0O0OOOO0OO ['data']['ordinary_water']#line:1170
                        O000000O0OOO00OOO =OOO0OOO0O0OOOO0OO ['data']['ordinary_fertilizer']#line:1171
                        O0O00OOOOO0OO000O =OOO0OOO0O0OOOO0OO ['data']['videoStatus']#line:1172
                        OOOO000O0OO0O0O00 =OOO0OOO0O0OOOO0OO ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(O000000O0OOO00OOO).split(".")[0]}丨水滴:{str(O00O0OO0OO000O000).split(".")[0]}')#line:1175
                        if float (O000000O0OOO00OOO )<96 :#line:1176
                            if O0O00OOOOO0OO000O :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                O0O000OOOO000O0O0 =99 -float (O000000O0OOO00OOO )#line:1179
                                O00OOO00OO000OOOO ={"fertilizer":str (O0O000OOOO000O0O0 ).split ('.')[0 ]}#line:1180
                                OOOOO0OO000OOO000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OOOOO0OO000OOO ).json ()#line:1182
                                if 'status'in OOOOO0OO000OOO000 :#line:1184
                                    if OOOOO0OO000OOO000 ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0OO000OOO000["message"]}')#line:1186
                                    if OOOOO0OO000OOO000 ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0OO000OOO000["message"]}')#line:1188
                                        break #line:1189
                                if float (O000000O0OOO00OOO )<78 :#line:1191
                                    O0O000OOOO000O0O0 =80 -float (O000000O0OOO00OOO )#line:1192
                                    OO0O0O0OO0OO0O000 =f'_fertilizer={int(O0O000OOOO000O0O0)}_{timi_new()}'#line:1193
                                    OOOO00OO00O0O0OO0 ={'source':'scsc','authorization':OOOO00O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO0OO0O000 ),'signstring':OO0O0O0OO0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    O0O0OO0O00O0OO00O ={"fertilizer":int (O0O000OOOO000O0O0 )}#line:1205
                                    O0OO0OOOOO000O0O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO00OO00O0O0OO0 ,data =O0O0OO0O00O0OO00O ).json ()#line:1207
                                    if 'status'in O0OO0OOOOO000O0O0 :#line:1209
                                        if O0OO0OOOOO000O0O0 ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOOOO000O0O0["message"]}丨数量:{int(O0O000OOOO000O0O0)}')#line:1211
                                        if O0OO0OOOOO000O0O0 ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOOOO000O0O0["message"]}丨数量:{int(O0O000OOOO000O0O0)}')#line:1213
                                            O00O0O0OO0OOO000O =O0OO0OOOOO000O0O0 ["message"].split ('-')[1 ]#line:1214
                                            O0O00O00O000OO0O0 =f'__{timi_new()}'#line:1215
                                            OOOOOO0OO0000OOOO ={'source':'scsc','authorization':OOOO00O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O000OO0O0 ),'signstring':O0O00O00O000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            O0OOO0000O0OOO00O =requests .request ('get',f'{host}/user',headers =OOOOOO0OO0000OOOO ).json ()#line:1227
                                            if 'status'in O0OOO0000O0OOO00O :#line:1228
                                                if O0OOO0000O0OOO00O ['status']==200 :#line:1229
                                                    O0O0O00O0OOOOO00O =O0OOO0000O0OOO00O ['data']['inner_id']#line:1230
                                                    if give_gold (O0O0O00O0OOOOO00O ,float (O00O0O0OO0OOO000O )+1 ):#line:1231
                                                        OOOO00O0O0O0OO000 .energy ()#line:1232
                        if float (O00O0OO0OO000O000 )<880 :#line:1233
                            if OOOO000O0OO0O0O00 :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                OO00OOO00O00000OO =999 -float (O00O0OO0OO000O000 )#line:1236
                                O0O0000O00O0000OO ={"water":str (OO00OOO00O00000OO ).split ('.')[0 ]}#line:1237
                                O0OO000O0000000OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OOOOO0OO000OOO ).json ()#line:1239
                                if 'status'in O0OO000O0000000OO :#line:1241
                                    if O0OO000O0000000OO ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO000O0000000OO["message"]}')#line:1243
                                    if O0OO000O0000000OO ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO000O0000000OO["message"]}')#line:1245
                                        break #line:1246
                                if float (O00O0OO0OO000O000 )<780 :#line:1247
                                    OO00OOO00O00000OO =800 -float (O00O0OO0OO000O000 )#line:1248
                                    OO0000OOO00OO00OO =f'_water={int(OO00OOO00O00000OO)}_{timi_new()}'#line:1249
                                    O00000000OO0O0O0O ={'source':'scsc','authorization':OOOO00O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOO00OO00OO ),'signstring':OO0000OOO00OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    OOOOOOO0O00OO0O00 ={"water":int (OO00OOO00O00000OO )}#line:1261
                                    OOOO00OO000OOOO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00000000OO0O0O0O ,data =OOOOOOO0O00OO0O00 ).json ()#line:1263
                                    if 'status'in OOOO00OO000OOOO0O :#line:1265
                                        if OOOO00OO000OOOO0O ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{OOOO00OO000OOOO0O["message"]}丨数量:{int(OO00OOO00O00000OO)}')#line:1267
                                        if OOOO00OO000OOOO0O ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{OOOO00OO000OOOO0O["message"]}丨数量:{int(OO00OOO00O00000OO)}')#line:1269
                                            O00O0O0OO0OOO000O =OOOO00OO000OOOO0O ["message"].split ('-')[1 ]#line:1270
                                            O0O00O00O000OO0O0 =f'__{timi_new()}'#line:1271
                                            OOOOOO0OO0000OOOO ={'source':'scsc','authorization':OOOO00O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O000OO0O0 ),'signstring':O0O00O00O000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            O0OOO0000O0OOO00O =requests .request ('get',f'{host}/user',headers =OOOOOO0OO0000OOOO ).json ()#line:1283
                                            if 'status'in O0OOO0000O0OOO00O :#line:1284
                                                if O0OOO0000O0OOO00O ['status']==200 :#line:1285
                                                    O0O0O00O0OOOOO00O =O0OOO0000O0OOO00O ['data']['inner_id']#line:1286
                                                    if give_gold (O0O0O00O0OOOOO00O ,float (O00O0O0OO0OOO000O )+1 ):#line:1287
                                                        OOOO00O0O0O0OO000 .energy ()#line:1288
                        break #line:1289
        except Exception as O00O000OOOO000OO0 :#line:1290
            print (O00O000OOOO000OO0 )#line:1291
def bundled_def ():#line:1293
    O0OO00O0OOO00000O =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return O0OO00O0OOO00000O .split ("\n")[random .randint (0 ,len (O0OO00O0OOO00000O .split ("\n"))-1 )]#line:1295
def version_of_the_validation ():#line:1299
    return str ((107 -56 )/10 )#line:1300
def ubbbf ():#line:1302
    print ('卡密验证通过   ✅')#line:1303
def sc2 ():#line:1306
    return "19319#$%^&*((*"#line:1307
def OO00OO0OO0OO00OO00o0 ():#line:1310
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1312
def get_ip ():#line:1315
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1317
def gitee_validation ():#line:1320
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1321
def gitee_edition ():#line:1324
    try :#line:1325
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1326
    except :#line:1327
        sys .exit (0 )#line:1328
def O000OO000O0O00OOO00 ():#line:1332
    try :#line:1333
        OOO00O0OOOO0OOO0O =gitee_edition ()#line:1334
        if version_of_the_validation ()<OOO00O0OOOO0OOO0O ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O0OOOO0OOO0O["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{OOO00O0OOOO0OOO0O["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00O0OOOO0OOO0O["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {OOO00O0OOOO0OOO0O["CityEarth"]["content"]}')#line:1340
    except Exception as OO0O0OOO0000OO0O0 :#line:1341
        print (OO0O0OOO0000OO0O0 )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350
