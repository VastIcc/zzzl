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
        O00O0OO0OO0OO0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O00O0OO0OO0OO0OOO)}个账号==========")#line:17
        for O0OO0O000OOO0OO00 in O00O0OO0OO0OO0OOO :#line:18
            OO00OOO000O0OO0OO =[]#line:19
            print (f"------------正在执行第{O00O0OO0OO0OO0OOO.index(O0OO0O000OOO0OO00) + 1}个账号------------")#line:20
            OO0O0O0000OOO0O00 =CityEarth (O0OO0O000OOO0OO00 ,OO00OOO000O0OO0OO ,O00O0OO0OO0OO0OOO .index (O0OO0O000OOO0OO00 ))#line:21
            def O0O0000O00OOO000O ():#line:23
                if OO0O0O0000OOO0O00 .base_info ():#line:25
                    OO0O0O0000OOO0O00 .sealing ()#line:27
                    OO0O0O0000OOO0O00 .invitenum ()#line:29
                    OO0O0O0000OOO0O00 .query_to_sell ()#line:31
                    OO0O0O0000OOO0O00 .friends_invitation ()#line:35
                    OO0O0O0000OOO0O00 .energy ()#line:37
                    OO0O0O0000OOO0O00 .add_clover ()#line:39
                    OO0O0O0000OOO0O00 .propsraffle ()#line:41
                    OO0O0O0000OOO0O00 .synthetic ()#line:43
                    OO0O0O0000OOO0O00 .crops_illustrated ()#line:45
                    OO0O0O0000OOO0O00 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0O0O0000OOO0O00 .give_gold ()#line:50
            OOOOOO0O0OO0OOOOO =threading .Thread (target =O0O0000O00OOO000O )#line:52
            OOOOOO0O0OO0OOOOO .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0O000O0OOOOOO00 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O000O0OOOOOO00 )#line:58
        time .sleep (3 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0OOO00OOO0000OO0 in invited_new :#line:62
            print (O0OOO00OOO0000OO0 )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0OOOOOO0OOO0OO0 in weishim :#line:65
            print (OO0OOOOOO0OOO0OO0 )#line:66
    except Exception as O00OO000OOOOO0OO0 :#line:67
        print (O00OO000OOOOO0OO0 )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (O0O000OO0000OO000 ,O00000OO0000O0OO0 ):#line:78
    try :#line:79
        O0O0O0OO0O0OO00OO =f'_doneeNo={O0O000OO0000OO000}&quantity={int(O00000OO0000O0OO0)}_{timi_new()}'#line:80
        O0O0O00000O0O00OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0O0OO00OO ),'signstring':O0O0O0OO0O0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        OOOOOO0O0O00O0OO0 ={"quantity":int (O00000OO0000O0OO0 ),"doneeNo":O0O000OO0000OO000 }#line:95
        O0OO0OO00OOOOOOOO =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O00000O0O00OO ,data =OOOOOO0O0O00O0OO0 ).json ()#line:96
        if 'status'in O0OO0OO00OOOOOOOO :#line:98
            if O0OO0OO00OOOOOOOO ['status']==200 :#line:99
                if O0OO0OO00OOOOOOOO ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(O00000OO0000O0OO0)}种子给{O0O000OO0000OO000}成功')#line:101
                    return True #line:102
            if O0OO0OO00OOOOOOOO ['status']==401 :#line:103
                print (f'【赠送种子】:{O0OO0OO00OOOOOOOO["message"]}')#line:104
                return False #line:105
            if O0OO0OO00OOOOOOOO ['status']==500 :#line:106
                print (f'【赠送种子】:{O0OO0OO00OOOOOOOO["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as O0OO0O0O00OO0O00O :#line:110
        print (O0OO0O0O00OO0O00O )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (OO00O00OO0O0OO0O0 ):#line:121
    O0OO000OOOO0OO00O =hashlib .md5 (OO00O00OO0O0OO0O0 .encode ()).hexdigest ()#line:122
    O00000000O000O000 =sc1 ()#line:123
    O00O000000000O000 =sc2 ()#line:124
    OO00OOO0OO000O00O =sc3 ()#line:125
    O0000OO000OO00O00 =O00000000O000O000 +O0OO000OOOO0OO00O +O00O000000000O000 +OO00OOO0OO000O00O #line:126
    O0OO0O00O00O0OO0O =hashlib .md5 (O0000OO000OO00O00 .encode ()).hexdigest ()#line:127
    return O0OO0O00O00O0OO0O #line:128
def format_msg ():#line:131
    OO0O0000O000O0OOO =""#line:132
    for O0000OO00O0000OO0 in msg_list :#line:133
        OO0O0000O000O0OOO +=str (O0000OO00O0000OO0 )+"\r\n"#line:134
    return OO0O0000O000O0OOO #line:135
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
def get_json_data (OO0OO0OOO0O00O00O ,O0OOO00OO00OO0O0O ,O0O00OO0O0O00O0O0 ,O0OO0OO000O0OO0OO ):#line:159
    with open (OO0OO0OOO0O00O00O ,'rb')as OOO00OOOO0O0O0000 :#line:160
        O0OO0000O000O0O00 =json .load (OOO00OOOO0O0O0000 )#line:161
        O0OO0000O000O0O00 ['data'][O0OOO00OO00OO0O0O ][O0O00OO0O0O00O0O0 ]=O0OO0OO000O0OO0OO #line:162
        OO000OOO0OOO0O000 =O0OO0000O000O0O00 #line:163
    OOO00OOOO0O0O0000 .close ()#line:164
    return OO000OOO0OOO0O000 #line:165
def write_json_data (OO00O0O00OO0OOOO0 ):#line:168
    with open (json_path1 ,'w')as O0OOO00O000OOO00O :#line:169
        json .dump (OO00O0O00OO0OOOO0 ,O0OOO00O000OOO00O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    O0OOO00O000OOO00O .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (O00O000OOO0O00OO0 ,O0OOOOOO0O00OO000 ,OOO0OO0OOO0000OO0 ,OO000O000OOOO00OO ):#line:177
        try :#line:178
            O00O000OOO0O00OO0 .msg =OOO0OO0OOO0000OO0 #line:179
            O00O000OOO0O00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            O00O000OOO0O00OO0 .token =O0OOOOOO0O00OO000 ['authorization']#line:181
            O00O000OOO0O00OO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            O00O000OOO0O00OO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            O00O000OOO0O00OO0 .elephant_user =O0OOOOOO0O00OO000 ['elephant_user']#line:184
            O00O000OOO0O00OO0 .elephant_pswd =O0OOOOOO0O00OO000 ['elephant_pswd']#line:185
            O00O000OOO0O00OO0 .elephant_Task_ID =O0OOOOOO0O00OO000 ['elephant_Task_ID']#line:186
            O00O000OOO0O00OO0 .len_new =OO000O000OOOO00OO #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (OO000O00O0O0O000O ):#line:192
        try :#line:193
            OO000O00O0O0O000O .watched_ad ()#line:195
            O00000OOO000OOOOO =f'__{timi_new()}'#line:196
            O00000OO00O00O0O0 ={'source':'scsc','authorization':OO000O00O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO000OOOOO ),'signstring':O00000OOO000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOOO0OOOOOOOOOO00 =requests .request ('get',f'{host}/user',headers =O00000OO00O00O0O0 ).json ()#line:208
            if 'status'in OOOO0OOOOOOOOOO00 :#line:210
                if OOOO0OOOOOOOOOO00 ['status']==200 :#line:211
                    O0O000OOO000O0OOO =OOOO0OOOOOOOOOO00 ['data']['nickname']#line:212
                    O00000OOOOOOO0000 =OOOO0OOOOOOOOOO00 ['data']['inner_id']#line:213
                    OO0OO0OO000000O00 =OOOO0OOOOOOOOOO00 ['data']['assets']['gold']#line:214
                    O0000OO0OOO0OOO00 =OOOO0OOOOOOOOOO00 ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{O0O000OOO000O0OOO[:5]}丨ID:{O00000OOOOOOO0000}丨等级:{O0000OO0OOO0OOO00}丨金种子:{str(OO0OO0OO000000O00).split(".")[0]}')#line:217
                    if 'wx_'in O0O000OOO000O0OOO :#line:218
                        OO000O00O0O0O000O .change_nickname ()#line:219
                if OOOO0OOOOOOOOOO00 ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if OO000O00O0O0O000O .elephant_user =='f':#line:222
                        return False #line:223
                    OO0O0O000O00OO0OO =Invalid_login .addtask (elephant_user =OO000O00O0O0O000O .elephant_user ,elephant_pswd =OO000O00O0O0O000O .elephant_pswd ,elephant_Task_ID =OO000O00O0O0O000O .elephant_Task_ID )#line:226
                    O0O0OOO0OO0O0O0OO =get_json_data (json_path ,OO000O00O0O0O000O .len_new ,'authorization',OO0O0O000O00OO0OO )#line:227
                    if write_json_data (O0O0OOO0OO0O0O0OO ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if OOOO0OOOOOOOOOO00 ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as O00000O00000000OO :#line:234
            print (O00000O00000000OO )#line:235
    def sealing (OOOOOOOOO0000O00O ):#line:238
        try :#line:239
            O0O00OOO000O00O0O =f'__{timi_new()}'#line:240
            O0O0O000O000OOOO0 ={'source':'scsc','authorization':OOOOOOOOO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO000O00O0O ),'signstring':O0O00OOO000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0O000O000OOOO0 )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =O0O0O000O000OOOO0 )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0O000O000OOOO0 )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0O000O000OOOO0 )#line:255
            requests .request ('get',f'{host}/user',headers =O0O0O000O000OOOO0 )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0O000O000OOOO0 )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0O000O000OOOO0 )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0O000O000OOOO0 )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0O000O000OOOO0 )#line:260
            requests .request ('get',f'{host}/assets',headers =O0O0O000O000OOOO0 )#line:261
        except Exception as OOOO00OOOO000O00O :#line:262
            print (OOOO00OOOO000O00O )#line:263
    def ddd (O00OO0O0OO0O00OO0 ):#line:265
        try :#line:266
            OOOOOOOOO000O0OOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            O0OOO000O00O0O00O ={'source':'scsc','authorization':O00OO0O0OO0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO000O0OOO ),'signstring':OOOOOOOOO000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            O0000O000OO00O0O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OOO000O00O0O00O ).json ()#line:279
            print (O0000O000OO00O0O0 )#line:280
        except Exception as OO0O0000O00OOO00O :#line:283
            print (OO0O0000O00OOO00O )#line:284
    def the_query (O000O0000OOO0O00O ):#line:289
        try :#line:290
            OO000OOOOOOOO00O0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            OOOO00O0OO00OO000 ={'authorization':O000O0000OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOOOOO00O0 ),'signstring':OO000OOOOOOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            OO0OO0O00O0OOO0OO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOOO00O0OO00OO000 ).json ()#line:302
            if 'status'in OO0OO0O00O0OOO0OO :#line:304
                if OO0OO0O00O0OOO0OO ['status']==200 :#line:305
                    return OO0OO0O00O0OOO0OO ['data']['rows'][4 ]['price']#line:306
        except Exception as O0O00OOO0O00O0OO0 :#line:307
            print (O0O00OOO0O00O0OO0 )#line:308
    def market_sale (OO0OOOOO0O00OO0O0 ,O0OOO0O00O0OO00OO ):#line:311
        try :#line:312
            OOOO0OOO000O0OO0O =timi_new ()#line:313
            O000O0000OOOOO00O =f'type=crop__{OOOO0OOO000O0OO0O}'#line:314
            OO0O0O0000O0O0O0O ={'source':'scsc','authorization':OO0OOOOO0O00OO0O0 .token ,'timestamp':str (OOOO0OOO000O0OO0O ),'sign':sign (O000O0000OOOOO00O ),'signstring':O000O0000OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            OOO0OOO0OO000OOOO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O0O0000O0O0O0O ).json ()#line:326
            if 'status'in OOO0OOO0OO000OOOO :#line:328
                if OOO0OOO0OO000OOOO ['status']==200 :#line:329
                    if OOO0OOO0OO000OOOO ['data']['rows']:#line:330
                        O000O000O00O00O00 =OOO0OOO0OO000OOOO ['data']['rows'][0 ]['packsackItemId']#line:331
                        O000OOO0000OOO0O0 =OOO0OOO0OO000OOOO ['data']['rows'][0 ]['quantity']#line:332
                        O0OOO0OOOOO0O0O0O =O0OOO0O00O0OO00OO #line:333
                        if float (O0OOO0O00O0OO00OO )>4.5 :#line:334
                            OO00OOOO0O000000O =f'_packsackItemId={O000O000O00O00O00}&price={str(O0OOO0OOOOO0O0O0O)[:5]}&quantity={O000OOO0000OOO0O0}_{OOOO0OOO000O0OO0O}'#line:335
                            OO00O0OOO0OOOO00O ={'source':'scsc','authorization':OO0OOOOO0O00OO0O0 .token ,'timestamp':str (OOOO0OOO000O0OO0O ),'sign':sign (OO00OOOO0O000000O ),'signstring':OO00OOOO0O000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OO0OOO00OOO00O00O ={"packsackItemId":O000O000O00O00O00 ,"price":str (O0OOO0OOOOO0O0O0O )[:5 ],"quantity":str (O000OOO0000OOO0O0 )}#line:351
                            OOO0O0OO0OOO00O00 =requests .request ('post',f'{host}/market/sale',headers =OO00O0OOO0OOOO00O ,data =OO0OOO00OOO00O00O ).json ()#line:352
                            if 'status'in OOO0O0OO0OOO00O00 :#line:354
                                if OOO0O0OO0OOO00O00 ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{O000OOO0000OOO0O0}丨价格:{str(O0OOO0OOOOO0O0O0O)[:5]}')#line:356
                                if OOO0O0OO0OOO00O00 ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{OOO0O0OO0OOO00O00["message"]}')#line:358
        except Exception as O00O00OOO0OOOOOOO :#line:359
            print (O00O00OOO0OOOOOOO )#line:360
    def query_to_sell (O0OOOO00O00000O0O ):#line:363
        try :#line:364
            OO00OOOO000O0OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:365
            O0OOO0O000O0OOO0O ={'source':'scsc','authorization':O0OOOO00O00000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO000O0OO00 ),'signstring':OO00OOOO000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:376
            O00OO0O0O0O0OOOO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OOO0O000O0OOO0O ).json ()#line:377
            if 'status'in O00OO0O0O0O0OOOO0 :#line:379
                if O00OO0O0O0O0OOOO0 ['status']==200 :#line:380
                    for O0000O000OO0OOO0O in O00OO0O0O0O0OOOO0 ['data']['rows']:#line:381
                        O0OOOOO00OO0OOOOO =O0000O000OO0OOO0O ['materialKey']#line:382
                        OO00OOOO0OO0OOO0O =O0000O000OO0OOO0O ['quantity']#line:383
                        O0OO00OOO00OOOOO0 =O0000O000OO0OOO0O ['price']#line:384
                        O0O00000O0OOOO0OO =O0000O000OO0OOO0O ['saleState']#line:385
                        if O0O00000O0OOOO0OO ==0 :#line:386
                            print (f'【出售订单】:名称:{O0OOOOO00OO0OOOOO}丨数量:{OO00OOOO0OO0OOO0O}丨价格:{O0OO00OOO00OOOOO0}')#line:387
                            O0000OOO000OOOOO0 =O0OOOO00O00000O0O .the_query ()#line:389
                            if float (O0000OOO000OOOOO0 )!=float (O0OO00OOO00OOOOO0 ):#line:390
                                O00O0O0OO0O0O0OO0 =O0000O000OO0OOO0O ['id']#line:391
                                O0OOOO00O00000O0O .cacel_sale (O00O0O0OO0O0O0OO0 )#line:392
                    O0OOOO00O00000O0O .game_map ()#line:394
        except Exception as OO00O0O0OO0000000 :#line:396
            print (OO00O0O0OO0000000 )#line:397
    def cacel_sale (O0OOO0OO00OO0000O ,O0000O0O000OO00O0 ):#line:400
        try :#line:401
            OOOOO00000OOO0O0O =f'_saleId={O0000O0O000OO00O0}_{timi_new()}'#line:402
            O00OO0OO00O00O0O0 ={'source':'scsc','authorization':O0OOO0OO00OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00000OOO0O0O ),'signstring':OOOOO00000OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            OO0O0000OOO00000O ={"saleId":O0000O0O000OO00O0 }#line:414
            OOOOOO0OO0O0000OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OO0OO00O00O0O0 ,data =OO0O0000OOO00000O ).json ()#line:415
            if 'status'in OOOOOO0OO0O0000OO :#line:417
                if OOOOOO0OO0O0000OO ['status']==200 :#line:418
                    print (f'【下架出售】:{OOOOOO0OO0O0000OO["data"]}')#line:419
        except Exception as O0OO0OO0O00OO00OO :#line:420
            print (O0OO0OO0O00OO00OO )#line:421
    def change_nickname (O000000OOO0O0OO0O ):#line:424
        try :#line:425
            O00O0OOO0OO0000OO =timi_new ()#line:426
            O0O00OOO0OOO0000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOOO00000O00OOO0O =requests .request ('post','https://www.qmsjmfb.com/',data =O0O00OOO0OOO0000O ).text #line:428
            OO0O0OOOO0OO0O00O =re .findall ('<ul><li>(.*?)</li>',OOOO00000O00OOO0O )[0 ][:3 ]#line:429
            OOOOO00OO0OO000O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0OOOO0OO0O00O}').json ()#line:430
            O0O0O00OO0OO00000 =OOOOO00OO0OO000O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:431
            O0O00O0O0O00OOO00 ={"nickname":O0O0O00OO0OO00000 }#line:432
            OOOOOOOOOOOO00OO0 =f'_nickname={O0O0O00OO0OO00000}_{O00O0OOO0OO0000OO}'#line:433
            OOOOOO0O0O0OO0OO0 ={'source':'scsc','authorization':O000000OOO0O0OO0O .token ,'timestamp':O00O0OOO0OO0000OO ,'sign':sign (OOOOOOOOOOOO00OO0 ),'signstring':OOOOOOOOOOOO00OO0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O0OO0OO0OOO0OO0O0 =requests .request ('patch',f'{host}/user/nickname',headers =OOOOOO0O0O0OO0OO0 ,data =O0O00O0O0O00OOO00 ).json ()#line:445
            if 'status'in O0OO0OO0OOO0OO0O0 :#line:447
                if O0OO0OO0OOO0OO0O0 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O0O0O00OO0OO00000}丨{O0OO0OO0OOO0OO0O0["message"]}')#line:449
        except Exception as O0000OO00OO0OO000 :#line:450
            print (O0000OO00OO0OO000 )#line:451
    def withdraw (O0O00OOO0OO0O0O00 ):#line:454
        try :#line:455
            OOO0000O0OO0OO0OO =f'__{timi_new()}'#line:456
            OOOO00OOOO000OOOO ={'source':'scsc','authorization':O0O00OOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OO0OO0OO ),'signstring':OOO0000O0OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O00000000OO0O0OO0 =requests .request ('get',f'{host}/assets',headers =OOOO00OOOO000OOOO ).json ()#line:468
            if 'status'in O00000000OO0O0OO0 :#line:470
                if O00000000OO0O0OO0 ['status']==200 :#line:471
                    OOO0OOO00O00000OO =O00000000OO0O0OO0 ['data']['cash']#line:472
                    if float (OOO0OOO00O00000OO )>20 :#line:473
                        OOO0000O0OO0OO0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        OOOO00OOOO000OOOO ={'authorization':O0O00OOO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OO0OO0OO ),'signstring':OOO0000O0OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        O00000OOOOO000000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        O0O00000OOOOO0O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO00OOOO000OOOO ,data =O00000OOOOO000000 ).json ()#line:487
                        if 'status'in O0O00000OOOOO0O0O :#line:489
                            if O0O00000OOOOO0O0O ['status']==200 :#line:490
                                print (f'【余额提现】:{O0O00000OOOOO0O0O["data"]}')#line:491
                        if 'status'in O0O00000OOOOO0O0O :#line:492
                            if O0O00000OOOOO0O0O ['status']==500 :#line:493
                                print (f'【余额提现】:{O0O00000OOOOO0O0O["message"]}')#line:494
        except Exception as OO0O0000OO0OO00OO :#line:495
            print (OO0O0000OO0OO00OO )#line:496
    def invitenum (O00OO000000O00O0O ):#line:499
        global invited_new #line:500
        try :#line:501
            OO0OOOO0OOOO0OO00 =f'__{timi_new()}'#line:502
            OO00O0O0O0OO0000O ={'source':'scsc','authorization':O00OO000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0OOOO0OO00 ),'signstring':OO0OOOO0OOOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O0O00OOO0O0000OO0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O0O0O0OO0000O ).json ()#line:514
            if 'status'in O0O00OOO0O0000OO0 :#line:516
                if O0O00OOO0O0000OO0 ['status']==200 :#line:517
                    O0000000OO00O00O0 =O0O00OOO0O0000OO0 ['data']['invited_count']#line:518
                    OOO0O00O000OO0OO0 =O0O00OOO0O0000OO0 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O0000000OO00O00O0}丨间邀好友:{OOO0O00O000OO0OO0}')#line:520
                    if O0000000OO00O00O0 <2 :#line:521
                        OOOO0OO00O00O00OO =f'__{timi_new()}'#line:522
                        O0OO000OOOOOO0O0O ={'source':'scsc','authorization':O00OO000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00O00O00OO ),'signstring':OOOO0OO00O00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O00OOO0OO0O00OOO0 =requests .request ('get',f'{host}/user',headers =O0OO000OOOOOO0O0O ).json ()#line:534
                        if 'status'in O00OOO0OO0O00OOO0 :#line:536
                            if O00OOO0OO0O00OOO0 ['status']==200 :#line:537
                                invited_new .append (O00OOO0OO0O00OOO0 ['data']['inner_id'])#line:538
        except Exception as O00O0OO000O0O0OO0 :#line:539
            print (O00O0OO000O0O0OO0 )#line:540
    def game_map (OOOO0O0OOO00OOO00 ):#line:543
        global count_list #line:544
        try :#line:545
            O00OOOO00OO00000O =f'__{timi_new()}'#line:546
            OOO000OOO0OO0OOOO ={'source':'scsc','authorization':OOOO0O0OOO00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OO00000O ),'signstring':O00OOOO00OO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
            O0OO0000000OO0O00 =requests .request ('get',f'{host}/game/map',headers =OOO000OOO0OO0OOOO ).json ()#line:558
            if 'status'in O0OO0000000OO0O00 :#line:560
                if O0OO0000000OO0O00 ['status']==200 :#line:561
                    for OOOO0OOO0OOOOOOO0 in O0OO0000000OO0O00 ['data']['list'][0 ]['crops']:#line:562
                        O0OOOOOO0OOOOO000 =OOOO0OOO0OOOOOOO0 ['level']#line:564
                        if O0OOOOOO0OOOOO000 ==41 :#line:565
                            OOOO0OO00OOO00000 =OOOO0OOO0OOOOOOO0 ['crop_name']#line:566
                            OOO00000OO0OO00O0 =OOOO0OOO0OOOOOOO0 ['count']#line:567
                            if OOO00000OO0OO00O0 >0 :#line:568
                                print (f'【农业资产】:{OOOO0OO00OOO00000}丨数量:{OOO00000OO0OO00O0}')#line:569
                                count_list +=OOO00000OO0OO00O0 #line:570
                                O00OO0OOOOOO000OO =OOOO0O0OOO00OOO00 .the_query ()#line:571
                                OOOO0O0OOO00OOO00 .market_sale (O00OO0OOOOOO000OO )#line:572
        except Exception as O0OO0O0OOOOO0O0OO :#line:573
            print (O0OO0O0OOOOO0O0OO )#line:574
    def give_gold (OOO00O0OO0OO0000O ):#line:577
        try :#line:578
            O00OOO0OOOOO00OOO =f'__{timi_new()}'#line:579
            OOOOO0O0O0OO00000 ={'source':'scsc','authorization':OOO00O0OO0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOO00OOO ),'signstring':O00OOO0OOOOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            O00O000O00OOOO00O =requests .request ('get',f'{host}/user',headers =OOOOO0O0O0OO00000 ).json ()#line:591
            if 'status'in O00O000O00OOOO00O :#line:592
                if O00O000O00OOOO00O ['status']==200 :#line:593
                    if float (OOO00O0OO0OO0000O .doneeNo )!=0 :#line:594
                        OO0O0000O00O0OO0O =O00O000O00OOOO00O ['data']['assets']['gold']#line:595
                        if float (OO0O0000O00O0OO0O )>float (OOO00O0OO0OO0000O .innerId ):#line:596
                            O0OO00O0O00OOO000 =int (float (OO0O0000O00O0OO0O )/1.1 )#line:597
                            O00OOO0OOOOO00OOO =f'_doneeNo={OOO00O0OO0OO0000O.doneeNo}&quantity={O0OO00O0O00OOO000}_{timi_new()}'#line:598
                            OOOOO0O0O0OO00000 ={'source':'scsc','authorization':OOO00O0OO0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOO00OOO ),'signstring':O00OOO0OOOOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O0OO000O0OOOO00OO ={"quantity":O0OO00O0O00OOO000 ,"doneeNo":OOO00O0OO0OO0000O .doneeNo }#line:613
                            OOOOOO0000O00O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO0O0O0OO00000 ,data =O0OO000O0OOOO00OO ).json ()#line:614
                            if 'status'in OOOOOO0000O00O000 :#line:616
                                if OOOOOO0000O00O000 ['status']==200 :#line:617
                                    if OOOOOO0000O00O000 ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O0OO00O0O00OOO000}种子给{OOO00O0OO0OO0000O.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as O0OO000OO0O0OO0OO :#line:622
            print (O0OO000OO0O0OO0OO )#line:623
    def invitation (OO0O0O0O0O0OOOO0O ):#line:625
        try :#line:626
            _O0O0OO000O0000OOO =float (bundled_def ())/4 #line:627
            OO00O000O00O0OOOO =f'_innerId={int(_O0O0OO000O0000OOO)}_{timi_new()}'#line:629
            OO00O0O00O00O0OOO ={'source':'scsc','authorization':OO0O0O0O0O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O00O0OOOO ),'signstring':OO00O000O00O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            O0O0O000OO000O0OO ={"innerId":int (_O0O0OO000O0000OOO )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00O0O00O00O0OOO ,data =O0O0O000OO000O0OO )#line:642
        except Exception as O00O0OO00O00O00O0 :#line:643
            print (O00O0OO00O00O00O0 )#line:644
    def winning_rewards (O000OO000O0OOO000 ):#line:647
        try :#line:648
            O0000OO000000O0OO =f'__{timi_new()}'#line:649
            O00O0OOO0000OOO0O ={'source':'scsc','authorization':O000OO000O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO000000O0OO ),'signstring':O0000OO000000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            O0O00OO0O0O0O000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O0OOO0000OOO0O ).json ()#line:661
            if 'status'in O0O00OO0O0O0O000O :#line:663
                if O0O00OO0O0O0O000O ['status']==200 :#line:664
                    if O0O00OO0O0O0O000O ['data']['amount']:#line:665
                        O00OO00000000OO0O =O0O00OO0O0O0O000O ['data']['amount']['gold']#line:666
                        return O00OO00000000OO0O #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as OOO0O00OO0OO00O0O :#line:670
            print (OOO0O00OO0OO00O0O )#line:671
    def certification (OOOOO0OOOO00000O0 ):#line:674
        try :#line:675
            O0OOOO00000OOOO00 =f'__{timi_new()}'#line:676
            OO0O0O000O000OO00 ={'source':'scsc','authorization':OOOOO0OOOO00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00000OOOO00 ),'signstring':O0OOOO00000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O00000O000OO00000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0O0O000O000OO00 ).json ()#line:688
            if 'status'in O00000O000OO00000 :#line:690
                if O00000O000OO00000 ['status']==200 :#line:691
                    if O00000O000OO00000 ['data']['result']:#line:692
                        OOOOOO00OO000O0O0 =O00000O000OO00000 ['data']['nick_name']#line:693
                        return OOOOOO00OO000O0O0 #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as O00OOOOOO00O000OO :#line:697
            print (O00OOOOOO00O000OO )#line:698
    def crops_illustrated (O0000O000000O0OO0 ):#line:701
        try :#line:702
            OO00O00OO0OO000OO =f'__{timi_new()}'#line:703
            O00O0OO0OOOO00O00 ={'source':'scsc','authorization':O0000O000000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0OO000OO ),'signstring':OO00O00OO0OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            O0000OO00OOOO0OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0OO0OOOO00O00 ).json ()#line:715
            if 'status'in O0000OO00OOOO0OOO :#line:717
                if O0000OO00OOOO0OOO ['status']==200 :#line:718
                    O0OO000OOOO0O000O =O0000OO00OOOO0OOO ['data'][0 ]['crops']#line:719
                    for O0O0000O0O0O0OOOO in O0OO000OOOO0O000O :#line:720
                        if O0O0000O0O0O0OOOO ['ill_clover_award']:#line:721
                            if float (O0O0000O0O0O0OOOO ['ill_clover_award'])>1 :#line:722
                                if O0O0000O0O0O0OOOO ['is_finish']:#line:723
                                    if not O0O0000O0O0O0OOOO ['is_getit']:#line:724
                                        if O0000O000000O0OO0 .certification ()!='未实名':#line:725
                                            OO00O00OO0OO000OO =f'_award_level={O0O0000O0O0O0OOOO["level"]}_{timi_new()}'#line:726
                                            O00O0OO0OOOO00O00 ={'source':'scsc','authorization':O0000O000000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0OO000OO ),'signstring':OO00O00OO0OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            O00OO000O000OOO0O ={"award_level":O0O0000O0O0O0OOOO ['level']}#line:738
                                            O0OOOOOOOOOO00O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0OO0OOOO00O00 ,json =O00OO000O000OOO0O ).json ()#line:740
                                            if 'status'in O0OOOOOOOOOO00O0O :#line:741
                                                if O0OOOOOOOOOO00O0O ['status']==200 :#line:742
                                                    O0O00O00O00O00OOO =O0OOOOOOOOOO00O0O ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{O0O0000O0O0O0OOOO["crop_name"]}成就丨奖励{O0O00O00O00O00OOO}☘️')#line:745
                                                if O0OOOOOOOOOO00O0O ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{O0OOOOOOOOOO00O0O["message"]}')#line:747
        except Exception as O00OOOOO0O00OO00O :#line:748
            print (O00OOOOO0O00OO00O )#line:749
    def watched_ad (OOO0O0OOOOO0O000O ):#line:752
        try :#line:753
            O00OOO00OO0O0O000 =f'__{timi_new()}'#line:754
            OOO000O0OOO0000OO ={'source':'scsc','authorization':OOO0O0OOOOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OO0O0O000 ),'signstring':O00OOO00OO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            OOO00OOOO00O0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0OOO0000OO ).json ()#line:766
            if 'status'in OOO00OOOO00O0O0OO :#line:768
                if OOO00OOOO00O0O0OO ['status']==200 :#line:769
                    if 'offlineInfo'in OOO00OOOO00O0O0OO ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        O00OOO00000OOO00O =OOO00OOOO00O0O0OO ['data']['offlineInfo']['off_minute']#line:772
                        O0OOO0OO0O00O0OO0 =float (OOO00OOOO00O0O0OO ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000O0OOO0000OO ).json ()#line:775
                        time .sleep (2 )#line:776
                        OOOOO0O0O0000OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000O0OOO0000OO ).json ()#line:777
                        if 'status'in OOOOO0O0O0000OO00 :#line:779
                            if OOOOO0O0O0000OO00 ['status']==200 :#line:780
                                OO00O000OOO0O0OO0 =float (OOOOO0O0O0000OO00 ['data']['silver'])/1000000000000 #line:781
                                O0OOOOO00O0O000O0 =str (OO00O000OOO0O0OO0 -O0OOO0OO0O00O0OO0 )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{O00OOO00000OOO00O}分钟奖励🌱数量:{O0OOOOO00O0O000O0}t粒')#line:783
        except Exception as OOOO0O0O000OOOO00 :#line:784
            print (OOOO0O0O000OOOO00 )#line:785
    def user_ad (OO0000OOOOOOOO000 ):#line:788
        try :#line:789
            OO0OO00O0OOO0OOO0 =f'__{timi_new()}'#line:790
            OOOO0O0O00O0OO0O0 ={'source':'scsc','authorization':OO0000OOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O0OOO0OOO0 ),'signstring':OO0OO00O0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            O0OOOO00O0OOO00O0 =requests .request ('get',f'{host}/user/ad',headers =OOOO0O0O00O0OO0O0 ).json ()#line:802
            if 'status'in O0OOOO00O0OOO00O0 :#line:804
                if O0OOOO00O0OOO00O0 ['status']==200 :#line:805
                    OO00O0O0OOOO0O0OO =O0OOOO00O0OOO00O0 ['data']['max_time']#line:806
                    OOO000OOOO0OOOOO0 =O0OOOO00O0OOO00O0 ['data']['watch_time']#line:807
                    OO0OOOO000O00O0OO =O0OOOO00O0OOO00O0 ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{OO0OOOO000O00O0OO + OO00O0O0OOOO0O0OO - OOO000OOOO0OOOOO0}次丨好友提供:{OO0OOOO000O00O0OO}次')#line:809
                    if OO0OOOO000O00O0OO +OO00O0O0OOOO0O0OO -OOO000OOOO0OOOOO0 >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        O0O0000OO0OO00O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO0O0O00O0OO0O0 ).json ()#line:812
                        if 'status'in O0O0000OO0OO00O0O :#line:814
                            if O0O0000OO0OO00O0O ['status']==200 :#line:815
                                O00O000O000OOOOO0 =float (O0O0000OO0OO00O0O ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(O00O000O000OOOOO0)}t粒')#line:817
                                return True #line:818
                            if O0O0000OO0OO00O0O ['status']==500 :#line:819
                                OO0OOO0000000O0OO =O0O0000OO0OO00O0O ['message']#line:820
                                print (f'【获取种子】:{OO0OOO0000000O0OO}')#line:821
                                return False #line:822
        except Exception as O0O0OOO0O00OO0O00 :#line:823
            print (O0O0OOO0O00OO0O00 )#line:824
    def synthetic (O000OOOO00O00OOO0 ):#line:827
        global id ,g #line:828
        try :#line:829
            O0OOO00OOOOO0OOO0 =O000OOOO00O00OOO0 .level_new ()#line:830
            OO0000OO0OO0O0OOO =random .randint (9 ,11 )#line:831
            O0O00000O00O0O0O0 =f'_site=8&targetSite={OO0000OO0OO0O0OOO}_{timi_new()}'#line:832
            OO0O0O00O00O0O000 ={'source':'scsc','authorization':O000OOOO00O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (O0O00000O00O0O0O0 ),'signstring':O0O00000O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            OOO00O0O0O0O000O0 ={"site":int (8 ),"targetSite":int (OO0000OO0OO0O0OOO )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0O00O00O0O000 ,json =OOO00O0O0O0O000O0 )#line:845
            while True :#line:846
                O0OOO00O0O0OOO0OO =f'__{timi_new()}'#line:847
                O00O000OO0OOO00O0 ={'source':'scsc','authorization':O000OOOO00O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0OOO0OO ),'signstring':O0OOO00O0O0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                OO0OO000O0O0O00OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O000OO0OOO00O0 ).json ()#line:859
                if 'status'in OO0OO000O0O0O00OO :#line:861
                    if OO0OO000O0O0O00OO ['status']==200 :#line:862
                        O00000O0000OO0O0O =OO0OO000O0O0O00OO ['data']['cropList']#line:863
                        OOO0O00O0O00OO0OO =OO0OO000O0O0O00OO ['data']['gameCoreDataDBid']#line:864
                        OOOO0OO00O000OO00 =float (OO0OO000O0O0O00OO ['data']['silver'])/1000000000000 #line:865
                        OO00O0OOOOO0O0O0O =0 #line:870
                        for OOOOO0OOO000000OO in O00000O0000OO0O0O :#line:871
                            if not OOOOO0OOO000000OO :#line:872
                                O0OO0O0OOO00OO0OO =f'_crop_id={OOO0O00O0O00OO0OO}&site={OO00O0OOOOO0O0O0O}_{O000OOOO00O00OOO0.time}'#line:873
                                OO00O0O0000O0OOOO ={'source':'scsc','authorization':O000OOOO00O00OOO0 .token ,'timestamp':O000OOOO00O00OOO0 .time ,'sign':sign (O0OO0O0OOO00OO0OO ),'signstring':O0OO0O0OOO00OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                OOOO000OO0OOO00OO ={"site":OO00O0OOOOO0O0O0O ,"crop_id":OOO0O00O0O00OO0OO }#line:884
                                OO0O0OO00OOOO0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO00O0O0000O0OOOO ,data =OOOO000OO0OOO00OO ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in OO0O0OO00OOOO0OOO :#line:888
                                    if OO0O0OO00OOOO0OOO ['status']==200 :#line:889
                                        if OO0O0OO00OOOO0OOO ['message']=='种子数量不足':#line:890
                                            O0OOO00OOOOO0OOO0 =O000OOOO00O00OOO0 .level_new ()#line:891
                                            print (f'【种植合成】:{OO0O0OO00OOOO0OOO["message"]}')#line:892
                                            if not O000OOOO00O00OOO0 .user_ad ():#line:893
                                                return False #line:894
                                    if OO0O0OO00OOOO0OOO ['status']==500 :#line:895
                                        print (f'【种植合成】:{OO0O0OO00OOOO0OOO["message"]}')#line:896
                                        return False #line:897
                            OO00O0OOOOO0O0O0O +=1 #line:898
                        OOO0OO0O00O00O00O =requests .request ('get',f'{host}/game/getAllData',headers =O00O000OO0OOO00O0 ).json ()#line:899
                        OOO0OO0O0O0O0OOOO =OOO0OO0O00O00O00O ['data']['cropList']#line:900
                        O0O0O00O0O0000O0O =False #line:901
                        for OOOOO0OOO000000OO in range (12 ):#line:902
                            id =OOO0OO0O0O0O0OOOO [OOOOO0OOO000000OO ]['level']#line:903
                            if float (O0OOO00OOOOO0OOO0 )-float (id )>9 :#line:904
                                O0O0O0O00OOOOO000 =f'_site={OOOOO0OOO000000OO}_{timi_new()}'#line:905
                                OO00O000O00OO000O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOOO00O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (O0O0O0O00OOOOO000 ),'signstring':O0O0O0O00OOOOO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                OO000O00O000OOO0O ={"site":OOOOO0OOO000000OO }#line:917
                                O000OO0O0OO000OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00O000O00OO000O ,data =OO000O00O000OOO0O ).json ()#line:919
                                if 'status'in O000OO0O0OO000OOO :#line:920
                                    if O000OO0O0OO000OOO ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for O0O0O0O00000000OO in range (11 ):#line:924
                                    OO0000OO0O0O0OO0O =O0O0O0O00000000OO +1 #line:925
                                    g =OOO0OO0O0O0O0OOOO [OO0000OO0O0O0OO0O ]['level']#line:926
                                    if id ==g :#line:927
                                        OO0OOOOOO00OOO000 =O0O0O0O00000000OO +2 #line:928
                                        if OO0OOOOOO00OOO000 !=OOOOO0OOO000000OO +1 :#line:929
                                            O0O00000OO0OOOO0O =OOOOO0OOO000000OO +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            O0O00000O00O0O0O0 =f'_site={O0O00000OO0OOOO0O - 1}&targetSite={OO0OOOOOO00OOO000 - 1}_{timi_new()}'#line:933
                                            OO0O0O00O00O0O000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOOO00O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (O0O00000O00O0O0O0 ),'signstring':O0O00000O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            OO0OO0O0OO0OOOO0O ={"site":int (O0O00000OO0OOOO0O -1 ),"targetSite":int (OO0OOOOOO00OOO000 -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0O00O00O0O000 ,json =OO0OO0O0OO0OOOO0O )#line:952
                                            O0O0O00O0O0000O0O =True #line:954
                                    if O0O0O00O0O0000O0O :#line:955
                                        break #line:956
                                if O0O0O00O0O0000O0O :#line:957
                                    break #line:958
        except :#line:959
            O000OOOO00O00OOO0 .synthetic ()#line:960
    def level_new (OOOO00OOOOO0OOO0O ):#line:963
        try :#line:964
            OOO00OOOOOO0O0OOO =f'__{timi_new()}'#line:965
            O0OO0000000OOO0O0 ={'source':'scsc','authorization':OOOO00OOOOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOOOO0O0OOO ),'signstring':OOO00OOOOOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            OOO00O0O000OO00OO =requests .request ('get',f'{host}/user',headers =O0OO0000000OOO0O0 ).json ()#line:977
            if 'status'in OOO00O0O000OO00OO :#line:978
                if OOO00O0O000OO00OO ['status']==200 :#line:979
                    return float (OOO00O0O000OO00OO ['data']['level'])#line:980
        except Exception as OOOO00OO00O0OOO0O :#line:981
            print (OOOO00OO00O0OOO0O )#line:982
    def propsraffle (OOO00O000O0OO000O ):#line:985
        try :#line:986
            while True :#line:987
                OOO0O0OOOOO00O00O =f'__{timi_new()}'#line:988
                O0O00OO0O0O00000O ={'source':'scsc','authorization':OOO00O000O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOOOO00O00O ),'signstring':OOO0O0OOOOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                OOOO00O0OO0OO00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00OO0O0O00000O ).json ()#line:1000
                if 'status'in OOOO00O0OO0OO00O0 :#line:1002
                    if OOOO00O0OO0OO00O0 ['status']==200 :#line:1003
                        OO000OO00O0O00000 =OOOO00O0OO0OO00O0 ['data']['rows']#line:1004
                        O0OO0000OOO00OOOO =OOOO00O0OO0OO00O0 ['data']['vstate']#line:1005
                        if OO000OO00O0O00000 ==5 or OO000OO00O0O00000 ==6 or OO000OO00O0O00000 ==7 :#line:1006
                            O0OO0O0OO00O0O0O0 =OOOO00O0OO0OO00O0 ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{O0OO0O0OO00O0O0O0}')#line:1008
                        if OO000OO00O0O00000 ==1 or OO000OO00O0O00000 ==2 or OO000OO00O0O00000 ==3 :#line:1009
                            O000O00OOOOO0O0O0 =OOOO00O0OO0OO00O0 ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{O000O00OOOOO0O0O0}')#line:1011
                        if OO000OO00O0O00000 ==4 or OO000OO00O0O00000 ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if OO000OO00O0O00000 =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as O000O00OOOO000O00 :#line:1053
            print (O000O00OOOO000O00 )#line:1054
    def friends_invitation (O0000OOOO0O0OO0O0 ):#line:1057
        try :#line:1058
            O0OO0O0O00OOO000O =f'__{timi_new()}'#line:1059
            OO0OOO000000O0O00 ={'source':'scsc','authorization':O0000OOOO0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O00OOO000O ),'signstring':O0OO0O0O00OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            O000O0OOO0OOOOOOO =requests .request ('get',f'{host}/friends',headers =OO0OOO000000O0O00 ).json ()#line:1071
            if 'status'in O000O0OOO0OOOOOOO :#line:1072
                if O000O0OOO0OOOOOOO ['status']==200 :#line:1073
                    OOOO00OOOOO000000 =O000O0OOO0OOOOOOO ['data']['myInviteter']#line:1074
                    if OOOO00OOOOO000000 :#line:1075
                        O0OOO0O00O00OO00O =OOOO00OOOOO000000 ['user']['nickname']#line:1076
                        O00O0OOOOO0O0000O =O0000OOOO0O0OO0O0 .certification ()#line:1077
                        if O00O0OOOOO0O0000O =='未实名':#line:1078
                            weishim .append (O0000OOOO0O0OO0O0 .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{O0OOO0O00O00OO00O}丨实名:{O00O0OOOOO0O0000O}')#line:1080
                    else :#line:1081
                        if O0000OOOO0O0OO0O0 .innerId !='0':#line:1082
                            O0000OOOO0O0OO0O0 .invitation ()#line:1083
        except Exception as OO000O0O00OO00OO0 :#line:1084
            print (OO000O0O00OO00OO0 )#line:1085
    def add_clover (OOO000O00000OO000 ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            OOO0O0O00OO000OO0 =f'__{timi_new()}'#line:1091
            O0OOOO00OO0OO00O0 ={'source':'scsc','authorization':OOO000O00000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00OO000OO0 ),'signstring':OOO0O0O00OO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O0O0000OO000O0OOO =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOO00OO0OO00O0 ).json ()#line:1103
            if 'status'in O0O0000OO000O0OOO :#line:1105
                if O0O0000OO000O0OOO ['status']==200 :#line:1106
                    O00000000000000O0 =O0O0000OO000O0OOO ['data']['clover']#line:1107
                    OOOOOO0O0O000000O =O0O0000OO000O0OOO ['data']['used_clover']#line:1108
                    OO000OO0O0OOOO000 =float (O00000000000000O0 )-float (OOOOOO0O0O000000O )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOOO0O0O000000O}')#line:1110
                    if OOO000O00000OO000 .certification ()!='未实名':#line:1111
                        if OO000OO0O0OOOO000 >1 :#line:1112
                            OOO0O0O00OO000OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO000OO0O0OOOO000)}_{timi_new()}'#line:1113
                            OOOOO0OOOO000OO00 ={'source':'scsc','authorization':OOO000O00000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00OO000OO0 ),'signstring':OOO0O0O00OO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            OOOO0000000000OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO000OO0O0OOOO000 )}#line:1125
                            OOO00O0O0000O0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO0OOOO000OO00 ,data =OOOO0000000000OOO ).json ()#line:1126
                            if 'status'in OOO00O0O0000O0OOO :#line:1128
                                if OOO00O0O0000O0OOO ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{OOO00O0O0000O0OOO["data"]["isSuccess"]}丨数量:{OO000OO0O0OOOO000}')#line:1130
                                if OOO00O0O0000O0OOO ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{OOO00O0O0000O0OOO["message"]}')#line:1132
            OO00OOOO00OO0O000 =requests .request ('get',f'{host}/lottery',headers =O0OOOO00OO0OO00O0 ).json ()#line:1133
            O0OO0OOOO00OOO0OO =OOO000O00000OO000 .winning_rewards ()#line:1135
            if 'status'in OO00OOOO00OO0O000 :#line:1136
                if OO00OOOO00OO0O000 ['status']==200 :#line:1137
                    OO000O0OO00O00O0O =OO00OOOO00OO0O000 ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (OO000O0OO00O00O0O )#line:1139
                    OO0000O0OO000OOOO =OO00OOOO00OO0O000 ['data'][1 ]['value']#line:1140
                    OO000O00OO000OOO0 =OO00OOOO00OO0O000 ['data'][0 ]['join_number']#line:1141
                    O0OO0OO0O00OOOO00 =int (float (OO00OOOO00OO0O000 ['data'][0 ]['totalValue']))#line:1142
                    O00O0O00OO0OOOO00 =float (OO0000O0OO000OOOO /O0OO0OO0O00OOOO00 )*10000 #line:1143
                    OOOOO0OO0OOO0OO00 =O0OO0OO0O00OOOO00 /OO000O00OO000OOO0 #line:1144
                    print (f'【参与抽奖】:预计每天中{str(OO000O0OO00O00O0O)[:6]}颗金种子丨好友收益:{str(O0OO0OOOO00OOO0OO)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(O00O0O00OO0OOOO00)[:6]}颗金种子丨☘️人均:{str(OOOOO0OO0OOO0OO00)[:7]}️')#line:1146
        except Exception as O00O0OO00OO0O0000 :#line:1147
            print (O00O0OO00OO0O0000 )#line:1148
    def energy (OOOO0O00OO0O0O0O0 ):#line:1151
        try :#line:1152
            while True :#line:1153
                O00OOO00000O0O0OO =f'__{timi_new()}'#line:1154
                O0OO000OOO0O00OOO ={'source':'scsc','authorization':OOOO0O00OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00000O0O0OO ),'signstring':O00OOO00000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                O0OO000000000O000 =requests .request ('get',f'{host}/energy/general',headers =O0OO000OOO0O00OOO ).json ()#line:1166
                if 'status'in O0OO000000000O000 :#line:1168
                    if O0OO000000000O000 ['status']==200 :#line:1169
                        O0OO0OOOOOO0OOOOO =O0OO000000000O000 ['data']['ordinary_water']#line:1170
                        O0OO00OOO0OOOO000 =O0OO000000000O000 ['data']['ordinary_fertilizer']#line:1171
                        O00O00O00O0O0000O =O0OO000000000O000 ['data']['videoStatus']#line:1172
                        OO0O000O0O0OO0O00 =O0OO000000000O000 ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(O0OO00OOO0OOOO000).split(".")[0]}丨水滴:{str(O0OO0OOOOOO0OOOOO).split(".")[0]}')#line:1175
                        if float (O0OO00OOO0OOOO000 )<96 :#line:1176
                            if O00O00O00O0O0000O :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                O00O00O0O0O0O0OO0 =99 -float (O0OO00OOO0OOOO000 )#line:1179
                                OOOO00O000O0O0O00 ={"fertilizer":str (O00O00O0O0O0O0OO0 ).split ('.')[0 ]}#line:1180
                                O00O00O0OOO000000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO000OOO0O00OOO ).json ()#line:1182
                                if 'status'in O00O00O0OOO000000 :#line:1184
                                    if O00O00O0OOO000000 ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O0OOO000000["message"]}')#line:1186
                                    if O00O00O0OOO000000 ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O0OOO000000["message"]}')#line:1188
                                        break #line:1189
                                if float (O0OO00OOO0OOOO000 )<78 :#line:1191
                                    O00O00O0O0O0O0OO0 =80 -float (O0OO00OOO0OOOO000 )#line:1192
                                    OO0O000OOOO00O00O =f'_fertilizer={int(O00O00O0O0O0O0OO0)}_{timi_new()}'#line:1193
                                    O0O0O0O00OOO0OO0O ={'source':'scsc','authorization':OOOO0O00OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OOOO00O00O ),'signstring':OO0O000OOOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    O00O00O0O0O00OOO0 ={"fertilizer":int (O00O00O0O0O0O0OO0 )}#line:1205
                                    O0OO0OOO0OOO00OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0O0O00OOO0OO0O ,data =O00O00O0O0O00OOO0 ).json ()#line:1207
                                    if 'status'in O0OO0OOO0OOO00OO0 :#line:1209
                                        if O0OO0OOO0OOO00OO0 ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOO0OOO00OO0["message"]}丨数量:{int(O00O00O0O0O0O0OO0)}')#line:1211
                                        if O0OO0OOO0OOO00OO0 ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{O0OO0OOO0OOO00OO0["message"]}丨数量:{int(O00O00O0O0O0O0OO0)}')#line:1213
                                            O0O00000000OOOOOO =O0OO0OOO0OOO00OO0 ["message"].split ('-')[1 ]#line:1214
                                            OOO00OOOOOOOOOOOO =f'__{timi_new()}'#line:1215
                                            O0000OO00OOOOOOOO ={'source':'scsc','authorization':OOOO0O00OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOOOOOOOOOO ),'signstring':OOO00OOOOOOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            OOOO0O000OO0O00O0 =requests .request ('get',f'{host}/user',headers =O0000OO00OOOOOOOO ).json ()#line:1227
                                            if 'status'in OOOO0O000OO0O00O0 :#line:1228
                                                if OOOO0O000OO0O00O0 ['status']==200 :#line:1229
                                                    OOOO000OO0O000000 =OOOO0O000OO0O00O0 ['data']['inner_id']#line:1230
                                                    if give_gold (OOOO000OO0O000000 ,float (O0O00000000OOOOOO )+1 ):#line:1231
                                                        OOOO0O00OO0O0O0O0 .energy ()#line:1232
                        if float (O0OO0OOOOOO0OOOOO )<880 :#line:1233
                            if OO0O000O0O0OO0O00 :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                O0000O0O0O0OOOO0O =999 -float (O0OO0OOOOOO0OOOOO )#line:1236
                                O00O0OO0000OO0OOO ={"water":str (O0000O0O0O0OOOO0O ).split ('.')[0 ]}#line:1237
                                OO0O0OO00O00O0OOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO000OOO0O00OOO ).json ()#line:1239
                                if 'status'in OO0O0OO00O00O0OOO :#line:1241
                                    if OO0O0OO00O00O0OOO ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0OO00O00O0OOO["message"]}')#line:1243
                                    if OO0O0OO00O00O0OOO ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0OO00O00O0OOO["message"]}')#line:1245
                                        break #line:1246
                                if float (O0OO0OOOOOO0OOOOO )<780 :#line:1247
                                    O0000O0O0O0OOOO0O =800 -float (O0OO0OOOOOO0OOOOO )#line:1248
                                    O0O0OO0O0OOOO0O00 =f'_water={int(O0000O0O0O0OOOO0O)}_{timi_new()}'#line:1249
                                    OOOOO00OO000OOOOO ={'source':'scsc','authorization':OOOO0O00OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOOO0O00 ),'signstring':O0O0OO0O0OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    O00O0000O00O0O000 ={"water":int (O0000O0O0O0OOOO0O )}#line:1261
                                    OOO00O0O0000O0000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOOO00OO000OOOOO ,data =O00O0000O00O0O000 ).json ()#line:1263
                                    if 'status'in OOO00O0O0000O0000 :#line:1265
                                        if OOO00O0O0000O0000 ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{OOO00O0O0000O0000["message"]}丨数量:{int(O0000O0O0O0OOOO0O)}')#line:1267
                                        if OOO00O0O0000O0000 ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{OOO00O0O0000O0000["message"]}丨数量:{int(O0000O0O0O0OOOO0O)}')#line:1269
                                            O0O00000000OOOOOO =OOO00O0O0000O0000 ["message"].split ('-')[1 ]#line:1270
                                            OOO00OOOOOOOOOOOO =f'__{timi_new()}'#line:1271
                                            O0000OO00OOOOOOOO ={'source':'scsc','authorization':OOOO0O00OO0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOOOOOOOOOO ),'signstring':OOO00OOOOOOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            OOOO0O000OO0O00O0 =requests .request ('get',f'{host}/user',headers =O0000OO00OOOOOOOO ).json ()#line:1283
                                            if 'status'in OOOO0O000OO0O00O0 :#line:1284
                                                if OOOO0O000OO0O00O0 ['status']==200 :#line:1285
                                                    OOOO000OO0O000000 =OOOO0O000OO0O00O0 ['data']['inner_id']#line:1286
                                                    if give_gold (OOOO000OO0O000000 ,float (O0O00000000OOOOOO )+1 ):#line:1287
                                                        OOOO0O00OO0O0O0O0 .energy ()#line:1288
                        break #line:1289
        except Exception as O00000O00O0O00OOO :#line:1290
            print (O00000O00O0O00OOO )#line:1291
def bundled_def ():#line:1293
    OO0OO0O00O000OOOO =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return OO0OO0O00O000OOOO .split ("\n")[random .randint (0 ,len (OO0OO0O00O000OOOO .split ("\n"))-1 )]#line:1295
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
        O0OO00O0000OOO0O0 =gitee_edition ()#line:1334
        if version_of_the_validation ()<O0OO00O0000OOO0O0 ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00O0000OOO0O0["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{O0OO00O0000OOO0O0["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00O0000OOO0O0["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {O0OO00O0000OOO0O0["CityEarth"]["content"]}')#line:1340
    except Exception as O0O0O00O00O0000O0 :#line:1341
        print (O0O0O00O00O0000O0 )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350
