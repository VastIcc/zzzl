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
        O000000OOOOOOO0OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O000000OOOOOOO0OO)}个账号==========")#line:17
        for OO00O00OO0O0O0OO0 in O000000OOOOOOO0OO :#line:18
            OOO0OOOO0OOO0OOO0 =[]#line:19
            print (f"------------正在执行第{O000000OOOOOOO0OO.index(OO00O00OO0O0O0OO0) + 1}个账号------------")#line:20
            O00OOOO000O0O000O =CityEarth (OO00O00OO0O0O0OO0 ,OOO0OOOO0OOO0OOO0 ,O000000OOOOOOO0OO .index (OO00O00OO0O0O0OO0 ))#line:21
            def O0OOO00O00OO000O0 ():#line:23
                if O00OOOO000O0O000O .base_info ():#line:25
                    O00OOOO000O0O000O .sealing ()#line:27
                    O00OOOO000O0O000O .invitenum ()#line:29
                    O00OOOO000O0O000O .query_to_sell ()#line:31
                    O00OOOO000O0O000O .friends_invitation ()#line:35
                    O00OOOO000O0O000O .energy ()#line:37
                    O00OOOO000O0O000O .add_clover ()#line:39
                    O00OOOO000O0O000O .propsraffle ()#line:41
                    O00OOOO000O0O000O .synthetic ()#line:43
                    O00OOOO000O0O000O .crops_illustrated ()#line:45
                    O00OOOO000O0O000O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O00OOOO000O0O000O .give_gold ()#line:50
            OOO0OOO00O00OO000 =threading .Thread (target =O0OOO00O00OO000O0 )#line:52
            OOO0OOO00O00OO000 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O00OOOOO00O00OOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OOOOO00O00OOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O000O0OO0OO00OOOO in invited_new :#line:62
            print (O000O0OO0OO00OOOO )#line:63
        print ('开始打印未实名的token')#line:64
        for O00OO000OOO00OO00 in weishim :#line:65
            print (O00OO000OOO00OO00 )#line:66
    except Exception as O0O0O00OO0O0OOO0O :#line:67
        print (O0O0O00OO0O0OOO0O )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (OOO0O0O00O00O0O0O ,O0000000OOO00O00O ):#line:78
    try :#line:79
        OOOO00000000OOO0O =f'_doneeNo={OOO0O0O00O00O0O0O}&quantity={int(O0000000OOO00O00O)}_{timi_new()}'#line:80
        O000OO0O0O0O00O0O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO00000000OOO0O ),'signstring':OOOO00000000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        OOOOO0O00O0O00OO0 ={"quantity":int (O0000000OOO00O00O ),"doneeNo":OOO0O0O00O00O0O0O }#line:95
        O0OO0000O0OOOO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O000OO0O0O0O00O0O ,data =OOOOO0O00O0O00OO0 ).json ()#line:96
        if 'status'in O0OO0000O0OOOO0OO :#line:98
            if O0OO0000O0OOOO0OO ['status']==200 :#line:99
                if O0OO0000O0OOOO0OO ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(O0000000OOO00O00O)}种子给{OOO0O0O00O00O0O0O}成功')#line:101
                    return True #line:102
            if O0OO0000O0OOOO0OO ['status']==401 :#line:103
                print (f'【赠送种子】:{O0OO0000O0OOOO0OO["message"]}')#line:104
                return False #line:105
            if O0OO0000O0OOOO0OO ['status']==500 :#line:106
                print (f'【赠送种子】:{O0OO0000O0OOOO0OO["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as O00O0OO0O0O000OO0 :#line:110
        print (O00O0OO0O0O000OO0 )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (O00OO0OO0OO0O00O0 ):#line:121
    O0OO0O0O00000OO00 =hashlib .md5 (O00OO0OO0OO0O00O0 .encode ()).hexdigest ()#line:122
    O00O000000000OOO0 =sc1 ()#line:123
    O0O00000OO0OO00O0 =sc2 ()#line:124
    OOO0O0OO00OOOOO00 =sc3 ()#line:125
    O0O000O0000OO0O00 =O00O000000000OOO0 +O0OO0O0O00000OO00 +O0O00000OO0OO00O0 +OOO0O0OO00OOOOO00 #line:126
    OOO0O00000OOOO00O =hashlib .md5 (O0O000O0000OO0O00 .encode ()).hexdigest ()#line:127
    return OOO0O00000OOOO00O #line:128
def format_msg ():#line:131
    O000O00O0O0OO00O0 =""#line:132
    for OO00OOOOO0OO0OO00 in msg_list :#line:133
        O000O00O0O0OO00O0 +=str (OO00OOOOO0OO0OO00 )+"\r\n"#line:134
    return O000O00O0O0OO00O0 #line:135
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
def get_json_data (O0OOO0O0O0000000O ,OO0O0OO0OO0O00OO0 ,OOOO00OOO0OO000O0 ,OO0O00O0O0000OOOO ):#line:159
    with open (O0OOO0O0O0000000O ,'rb')as OOO0000O00OO00OOO :#line:160
        OO0O00OOOOOOO00OO =json .load (OOO0000O00OO00OOO )#line:161
        OO0O00OOOOOOO00OO ['data'][OO0O0OO0OO0O00OO0 ][OOOO00OOO0OO000O0 ]=OO0O00O0O0000OOOO #line:162
        O0O00O0OO00O0O00O =OO0O00OOOOOOO00OO #line:163
    OOO0000O00OO00OOO .close ()#line:164
    return O0O00O0OO00O0O00O #line:165
def write_json_data (OO00OO0O0O00O0000 ):#line:168
    with open (json_path1 ,'w')as O000OOOOOO00O0000 :#line:169
        json .dump (OO00OO0O0O00O0000 ,O000OOOOOO00O0000 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    O000OOOOOO00O0000 .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (O00OO0OO000O0OOO0 ,OOOO0OOOOO0O000OO ,O0OOOO00000O00O00 ,OO0OOOOO0OO0O00O0 ):#line:177
        try :#line:178
            O00OO0OO000O0OOO0 .msg =O0OOOO00000O00O00 #line:179
            O00OO0OO000O0OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            O00OO0OO000O0OOO0 .token =OOOO0OOOOO0O000OO ['authorization']#line:181
            O00OO0OO000O0OOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            O00OO0OO000O0OOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            O00OO0OO000O0OOO0 .elephant_user =OOOO0OOOOO0O000OO ['elephant_user']#line:184
            O00OO0OO000O0OOO0 .elephant_pswd =OOOO0OOOOO0O000OO ['elephant_pswd']#line:185
            O00OO0OO000O0OOO0 .elephant_Task_ID =OOOO0OOOOO0O000OO ['elephant_Task_ID']#line:186
            O00OO0OO000O0OOO0 .len_new =OO0OOOOO0OO0O00O0 #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (OOO00O00OOOOO0O00 ):#line:192
        try :#line:193
            OOO00O00OOOOO0O00 .watched_ad ()#line:195
            O000O0000O0O0OOO0 =f'__{timi_new()}'#line:196
            OOOO0OOO000OO00OO ={'source':'scsc','authorization':OOO00O00OOOOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000O0O0OOO0 ),'signstring':O000O0000O0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O000OOOOOO0OO00 =requests .request ('get',f'{host}/user',headers =OOOO0OOO000OO00OO ).json ()#line:208
            if 'status'in O0O000OOOOOO0OO00 :#line:210
                if O0O000OOOOOO0OO00 ['status']==200 :#line:211
                    O0000O00OOO00OO00 =O0O000OOOOOO0OO00 ['data']['nickname']#line:212
                    OO00OOOO0OOOOO00O =O0O000OOOOOO0OO00 ['data']['inner_id']#line:213
                    O0OO0000O0O0OOO00 =O0O000OOOOOO0OO00 ['data']['assets']['gold']#line:214
                    OOOOO0O00O00OOOO0 =O0O000OOOOOO0OO00 ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{O0000O00OOO00OO00[:5]}丨ID:{OO00OOOO0OOOOO00O}丨等级:{OOOOO0O00O00OOOO0}丨金种子:{str(O0OO0000O0O0OOO00).split(".")[0]}')#line:217
                    if 'wx_'in O0000O00OOO00OO00 :#line:218
                        OOO00O00OOOOO0O00 .change_nickname ()#line:219
                if O0O000OOOOOO0OO00 ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if OOO00O00OOOOO0O00 .elephant_user =='f':#line:222
                        return False #line:223
                    O0OO0O0O0O0OO0OOO =Invalid_login .addtask (elephant_user =OOO00O00OOOOO0O00 .elephant_user ,elephant_pswd =OOO00O00OOOOO0O00 .elephant_pswd ,elephant_Task_ID =OOO00O00OOOOO0O00 .elephant_Task_ID )#line:226
                    O0OOOOOO00O00O0OO =get_json_data (json_path ,OOO00O00OOOOO0O00 .len_new ,'authorization',O0OO0O0O0O0OO0OOO )#line:227
                    if write_json_data (O0OOOOOO00O00O0OO ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if O0O000OOOOOO0OO00 ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as OO000O00O00OO000O :#line:234
            print (OO000O00O00OO000O )#line:235
    def sealing (O00OO00O00O00O00O ):#line:238
        try :#line:239
            OO000OO0000OO00OO =f'__{timi_new()}'#line:240
            O0000O0O0OOOO0OO0 ={'source':'scsc','authorization':O00OO00O00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0000OO00OO ),'signstring':OO000OO0000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000O0O0OOOO0OO0 )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =O0000O0O0OOOO0OO0 )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000O0O0OOOO0OO0 )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000O0O0OOOO0OO0 )#line:255
            requests .request ('get',f'{host}/user',headers =O0000O0O0OOOO0OO0 )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000O0O0OOOO0OO0 )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000O0O0OOOO0OO0 )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000O0O0OOOO0OO0 )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =O0000O0O0OOOO0OO0 )#line:260
            requests .request ('get',f'{host}/assets',headers =O0000O0O0OOOO0OO0 )#line:261
        except Exception as OOO00OO0OOO0OO0O0 :#line:262
            print (OOO00OO0OOO0OO0O0 )#line:263
    def ddd (OO0OO000000OO000O ):#line:265
        try :#line:266
            OO00OOOO0OO00O0OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            OO00OO0O0000OO0OO ={'source':'scsc','authorization':OO0OO000000OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0OO00O0OO ),'signstring':OO00OOOO0OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            OOO00OOOO0O0OO0OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO00OO0O0000OO0OO ).json ()#line:279
            print (OOO00OOOO0O0OO0OO )#line:280
        except Exception as OO0O00O0O00O0000O :#line:283
            print (OO0O00O0O00O0000O )#line:284
    def the_query (OOO00OOOO0O0OO0O0 ):#line:289
        try :#line:290
            O0O0O0O0OO0000O00 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            OOO00OOO0OOO0O0OO ={'authorization':OOO00OOOO0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO0000O00 ),'signstring':O0O0O0O0OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O000000OOOO000000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO00OOO0OOO0O0OO ).json ()#line:302
            if 'status'in O000000OOOO000000 :#line:304
                if O000000OOOO000000 ['status']==200 :#line:305
                    return O000000OOOO000000 ['data']['rows'][4 ]['price']#line:306
        except Exception as OOO000OOOO0000OOO :#line:307
            print (OOO000OOOO0000OOO )#line:308
    def market_sale (OOOO00OOOOO0O0000 ,O000O00OO00000O00 ):#line:311
        try :#line:312
            OO0OO0O00O0O000OO =timi_new ()#line:313
            O0O0O00OOO00000OO =f'type=crop__{OO0OO0O00O0O000OO}'#line:314
            O00O0O0O00OO0O000 ={'source':'scsc','authorization':OOOO00OOOOO0O0000 .token ,'timestamp':str (OO0OO0O00O0O000OO ),'sign':sign (O0O0O00OOO00000OO ),'signstring':O0O0O00OOO00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            OOO0OOOO000OO000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00O0O0O00OO0O000 ).json ()#line:326
            if 'status'in OOO0OOOO000OO000O :#line:328
                if OOO0OOOO000OO000O ['status']==200 :#line:329
                    if OOO0OOOO000OO000O ['data']['rows']:#line:330
                        O000O00O0OO00000O =OOO0OOOO000OO000O ['data']['rows'][0 ]['packsackItemId']#line:331
                        O000OOO0OO00O0OOO =OOO0OOOO000OO000O ['data']['rows'][0 ]['quantity']#line:332
                        O0O0OO000O0O0OO00 =O000O00OO00000O00 #line:333
                        if float (O000O00OO00000O00 )>5 :#line:334
                            OO0O0000OOOOOO000 =f'_packsackItemId={O000O00O0OO00000O}&price={str(O0O0OO000O0O0OO00)[:5]}&quantity={O000OOO0OO00O0OOO}_{OO0OO0O00O0O000OO}'#line:335
                            OO0OOOO0000OO00OO ={'source':'scsc','authorization':OOOO00OOOOO0O0000 .token ,'timestamp':str (OO0OO0O00O0O000OO ),'sign':sign (OO0O0000OOOOOO000 ),'signstring':OO0O0000OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OOO0O0OOOO0O00O00 ={"packsackItemId":O000O00O0OO00000O ,"price":str (O0O0OO000O0O0OO00 )[:5 ],"quantity":str (O000OOO0OO00O0OOO )}#line:351
                            O0O0000O00OO0O00O =requests .request ('post',f'{host}/market/sale',headers =OO0OOOO0000OO00OO ,data =OOO0O0OOOO0O00O00 ).json ()#line:352
                            if 'status'in O0O0000O00OO0O00O :#line:354
                                if O0O0000O00OO0O00O ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{O000OOO0OO00O0OOO}丨价格:{str(O0O0OO000O0O0OO00)[:5]}')#line:356
                                if O0O0000O00OO0O00O ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{O0O0000O00OO0O00O["message"]}')#line:358
        except Exception as O00OOOO00000OOO0O :#line:359
            print (O00OOOO00000OOO0O )#line:360
    def query_to_sell (O0O00O0O0000OOO0O ):#line:363
        global count_list #line:364
        try :#line:365
            OOOOO00O0OO000O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:366
            OO0OO0OOOO00OOOO0 ={'source':'scsc','authorization':O0O00O0O0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OO000O0O ),'signstring':OOOOO00O0OO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:377
            O0O0O0O000OO00O0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0OO0OOOO00OOOO0 ).json ()#line:378
            if 'status'in O0O0O0O000OO00O0O :#line:380
                if O0O0O0O000OO00O0O ['status']==200 :#line:381
                    for O00O0000O00000OOO in O0O0O0O000OO00O0O ['data']['rows']:#line:382
                        OOO00O0OOO0O00OOO =O00O0000O00000OOO ['materialKey']#line:383
                        O0OO000O00O0000O0 =O00O0000O00000OOO ['quantity']#line:384
                        OOOOOOOOOOOO00OOO =O00O0000O00000OOO ['price']#line:385
                        OO0000O000000O0OO =O00O0000O00000OOO ['saleState']#line:386
                        if OO0000O000000O0OO ==0 :#line:387
                            print (f'【出售订单】:名称:{OOO00O0OOO0O00OOO}丨数量:{O0OO000O00O0000O0}丨价格:{OOOOOOOOOOOO00OOO}')#line:388
                            count_list +=O0OO000O00O0000O0 #line:389
                            OO000OO00O0000000 =O0O00O0O0000OOO0O .the_query ()#line:391
                            if float (OO000OO00O0000000 )!=float (OOOOOOOOOOOO00OOO ):#line:392
                                O0OO00O0O00OO0O0O =O00O0000O00000OOO ['id']#line:393
                                O0O00O0O0000OOO0O .cacel_sale (O0OO00O0O00OO0O0O )#line:394
                    O0O00O0O0000OOO0O .game_map ()#line:396
        except Exception as O00000O0O0O00OOOO :#line:398
            print (O00000O0O0O00OOOO )#line:399
    def cacel_sale (OOO00OO0OO0O00O00 ,OOO0OO00OOOOO0O00 ):#line:402
        try :#line:403
            O0O0OO0OO0OO0O00O =f'_saleId={OOO0OO00OOOOO0O00}_{timi_new()}'#line:404
            OOO0O00OO0O0O00OO ={'source':'scsc','authorization':OOO00OO0OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO0OO0O00O ),'signstring':O0O0OO0OO0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            O0OO000O0O0OOOO00 ={"saleId":OOO0OO00OOOOO0O00 }#line:416
            O000000OO0O00O0O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO0O00OO0O0O00OO ,data =O0OO000O0O0OOOO00 ).json ()#line:417
            if 'status'in O000000OO0O00O0O0 :#line:419
                if O000000OO0O00O0O0 ['status']==200 :#line:420
                    print (f'【下架出售】:{O000000OO0O00O0O0["data"]}')#line:421
        except Exception as O0000OOO000000000 :#line:422
            print (O0000OOO000000000 )#line:423
    def change_nickname (OOOO0OOO00OOOO0O0 ):#line:426
        try :#line:427
            OOOOO00O0OO00000O =timi_new ()#line:428
            O00OOOO0000O0O000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:429
            OOOO0O000O0000O00 =requests .request ('post','https://www.qmsjmfb.com/',data =O00OOOO0000O0O000 ).text #line:430
            O00OOOO0O00O0OO0O =re .findall ('<ul><li>(.*?)</li>',OOOO0O000O0000O00 )[0 ][:3 ]#line:431
            OOO00O0OO000OO00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00OOOO0O00O0OO0O}').json ()#line:432
            OO00OO0OO0O0O00OO =OOO00O0OO000OO00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:433
            O0OOOO0OO00O00O00 ={"nickname":OO00OO0OO0O0O00OO }#line:434
            OO000O0O0OO00O00O =f'_nickname={OO00OO0OO0O0O00OO}_{OOOOO00O0OO00000O}'#line:435
            O0O00O0O000OO0000 ={'source':'scsc','authorization':OOOO0OOO00OOOO0O0 .token ,'timestamp':OOOOO00O0OO00000O ,'sign':sign (OO000O0O0OO00O00O ),'signstring':OO000O0O0OO00O00O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:446
            OO0OO000O000OOOOO =requests .request ('patch',f'{host}/user/nickname',headers =O0O00O0O000OO0000 ,data =O0OOOO0OO00O00O00 ).json ()#line:447
            if 'status'in OO0OO000O000OOOOO :#line:449
                if OO0OO000O000OOOOO ['status']==200 :#line:450
                    print (f'【修改网名】:网名:{OO00OO0OO0O0O00OO}丨{OO0OO000O000OOOOO["message"]}')#line:451
        except Exception as O0OOO0OOO00OO0O0O :#line:452
            print (O0OOO0OOO00OO0O0O )#line:453
    def withdraw (OO00OO0OO0O00OOO0 ):#line:456
        try :#line:457
            OOO0OO000O00O000O =f'__{timi_new()}'#line:458
            OO00OOO0OOO0OO0O0 ={'source':'scsc','authorization':OO00OO0OO0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O00O000O ),'signstring':OOO0OO000O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:469
            O000OOO0000O0OOO0 =requests .request ('get',f'{host}/assets',headers =OO00OOO0OOO0OO0O0 ).json ()#line:470
            if 'status'in O000OOO0000O0OOO0 :#line:472
                if O000OOO0000O0OOO0 ['status']==200 :#line:473
                    OOOO00O0OO0O0OO00 =O000OOO0000O0OOO0 ['data']['cash']#line:474
                    if float (OOOO00O0OO0O0OO00 )>20 :#line:475
                        OOO0OO000O00O000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:476
                        OO00OOO0OOO0OO0O0 ={'authorization':OO00OO0OO0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O00O000O ),'signstring':OOO0OO000O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:486
                        O00OO0OOOOOOOOO0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:487
                        O0O000OOOOO0O0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO00OOO0OOO0OO0O0 ,data =O00OO0OOOOOOOOO0O ).json ()#line:489
                        if 'status'in O0O000OOOOO0O0000 :#line:491
                            if O0O000OOOOO0O0000 ['status']==200 :#line:492
                                print (f'【余额提现】:{O0O000OOOOO0O0000["data"]}')#line:493
                        if 'status'in O0O000OOOOO0O0000 :#line:494
                            if O0O000OOOOO0O0000 ['status']==500 :#line:495
                                print (f'【余额提现】:{O0O000OOOOO0O0000["message"]}')#line:496
        except Exception as OO0OO0OOO0000OO00 :#line:497
            print (OO0OO0OOO0000OO00 )#line:498
    def invitenum (OOOO0OOO00OO000O0 ):#line:501
        global invited_new #line:502
        try :#line:503
            OOO0OOOOO0OOO000O =f'__{timi_new()}'#line:504
            OO0O000O0O0OOO000 ={'source':'scsc','authorization':OOOO0OOO00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0OOO000O ),'signstring':OOO0OOOOO0OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:515
            OO0OOOO0000O00000 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0O000O0O0OOO000 ).json ()#line:516
            if 'status'in OO0OOOO0000O00000 :#line:518
                if OO0OOOO0000O00000 ['status']==200 :#line:519
                    OO0OOOO0000OO0000 =OO0OOOO0000O00000 ['data']['invited_count']#line:520
                    OO0O0OOOOO00OOOOO =OO0OOOO0000O00000 ['data']['invited_second_count']#line:521
                    print (f'【我的邀请】:直邀好友:{OO0OOOO0000OO0000}丨间邀好友:{OO0O0OOOOO00OOOOO}')#line:522
                    if OO0OOOO0000OO0000 <2 :#line:523
                        OOO0OOOOO0O00000O =f'__{timi_new()}'#line:524
                        O00O0000OO0O0OOOO ={'source':'scsc','authorization':OOOO0OOO00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O00000O ),'signstring':OOO0OOOOO0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:535
                        O0OO0OO0O00O000O0 =requests .request ('get',f'{host}/user',headers =O00O0000OO0O0OOOO ).json ()#line:536
                        if 'status'in O0OO0OO0O00O000O0 :#line:538
                            if O0OO0OO0O00O000O0 ['status']==200 :#line:539
                                invited_new .append (O0OO0OO0O00O000O0 ['data']['inner_id'])#line:540
        except Exception as O0OOOOOO000OO0OO0 :#line:541
            print (O0OOOOOO000OO0OO0 )#line:542
    def game_map (O0OO000O000OO0O00 ):#line:545
        try :#line:546
            O00O0OO000000OOOO =f'__{timi_new()}'#line:547
            O0OO0O0O0O0OO00O0 ={'source':'scsc','authorization':O0OO000O000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO000000OOOO ),'signstring':O00O0OO000000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:558
            OOO000OO0OOO00O0O =requests .request ('get',f'{host}/game/map',headers =O0OO0O0O0O0OO00O0 ).json ()#line:559
            if 'status'in OOO000OO0OOO00O0O :#line:561
                if OOO000OO0OOO00O0O ['status']==200 :#line:562
                    for OOO0OOO0000OOO00O in OOO000OO0OOO00O0O ['data']['list'][0 ]['crops']:#line:563
                        O0OO00O00000000OO =OOO0OOO0000OOO00O ['level']#line:565
                        if O0OO00O00000000OO ==41 :#line:566
                            OO0000O00O00OO0O0 =OOO0OOO0000OOO00O ['crop_name']#line:567
                            OOOO00OO0OO0OO000 =OOO0OOO0000OOO00O ['count']#line:568
                            if OOOO00OO0OO0OO000 >0 :#line:569
                                print (f'【农业资产】:{OO0000O00O00OO0O0}丨数量:{OOOO00OO0OO0OO000}')#line:570
                                O00O0O000OOO00OOO =O0OO000O000OO0O00 .the_query ()#line:571
                                O0OO000O000OO0O00 .market_sale (O00O0O000OOO00OOO )#line:572
        except Exception as OO00OOO000OO00OOO :#line:573
            print (OO00OOO000OO00OOO )#line:574
    def give_gold (OOO000OO00O00O0O0 ):#line:577
        try :#line:578
            O000OO00O00O0O0O0 =f'__{timi_new()}'#line:579
            O0O0OOO0O0OOOO00O ={'source':'scsc','authorization':OOO000OO00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00O0O0O0 ),'signstring':O000OO00O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            OO0O00O0OO0OO0OOO =requests .request ('get',f'{host}/user',headers =O0O0OOO0O0OOOO00O ).json ()#line:591
            if 'status'in OO0O00O0OO0OO0OOO :#line:592
                if OO0O00O0OO0OO0OOO ['status']==200 :#line:593
                    if float (OOO000OO00O00O0O0 .doneeNo )!=0 :#line:594
                        O0OOO00OO000000OO =OO0O00O0OO0OO0OOO ['data']['assets']['gold']#line:595
                        if float (O0OOO00OO000000OO )>float (OOO000OO00O00O0O0 .innerId ):#line:596
                            O0OOO0OOO0OO0O0O0 =int (float (O0OOO00OO000000OO )/1.1 )#line:597
                            O000OO00O00O0O0O0 =f'_doneeNo={OOO000OO00O00O0O0.doneeNo}&quantity={O0OOO0OOO0OO0O0O0}_{timi_new()}'#line:598
                            O0O0OOO0O0OOOO00O ={'source':'scsc','authorization':OOO000OO00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O00O0O0O0 ),'signstring':O000OO00O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            OOO00O000O000OOOO ={"quantity":O0OOO0OOO0OO0O0O0 ,"doneeNo":OOO000OO00O00O0O0 .doneeNo }#line:613
                            OO00OO00O0O0O000O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OOO0O0OOOO00O ,data =OOO00O000O000OOOO ).json ()#line:614
                            if 'status'in OO00OO00O0O0O000O :#line:616
                                if OO00OO00O0O0O000O ['status']==200 :#line:617
                                    if OO00OO00O0O0O000O ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O0OOO0OOO0OO0O0O0}种子给{OOO000OO00O00O0O0.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as O0OO000OOO0O000O0 :#line:622
            print (O0OO000OOO0O000O0 )#line:623
    def invitation (O000OOOO00OOO0000 ):#line:625
        try :#line:626
            _O0O00OOOO0OO0O0O0 =float (bundled_def ())/4 #line:627
            OOO0OO0OO0O0OOOO0 =f'_innerId={int(_O0O00OOOO0OO0O0O0)}_{timi_new()}'#line:629
            OO00O000000O000OO ={'source':'scsc','authorization':O000OOOO00OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO0O0OOOO0 ),'signstring':OOO0OO0OO0O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            OOO0O00O0O0OO0O0O ={"innerId":int (_O0O00OOOO0OO0O0O0 )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00O000000O000OO ,data =OOO0O00O0O0OO0O0O )#line:642
        except Exception as O000OO00O00O0O000 :#line:643
            print (O000OO00O00O0O000 )#line:644
    def winning_rewards (OO00OOOO00O0OOOOO ):#line:647
        try :#line:648
            OOO0OOOO0OO0O0000 =f'__{timi_new()}'#line:649
            OOO00O00OOOO000OO ={'source':'scsc','authorization':OO00OOOO00O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0OO0O0000 ),'signstring':OOO0OOOO0OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            O00O00OOO00000O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO00O00OOOO000OO ).json ()#line:661
            if 'status'in O00O00OOO00000O0O :#line:663
                if O00O00OOO00000O0O ['status']==200 :#line:664
                    if O00O00OOO00000O0O ['data']['amount']:#line:665
                        OO00O00OOOO00OO0O =O00O00OOO00000O0O ['data']['amount']['gold']#line:666
                        return OO00O00OOOO00OO0O #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as OO0O0O000O0OOO00O :#line:670
            print (OO0O0O000O0OOO00O )#line:671
    def certification (O0O0O0O0000OO000O ):#line:674
        try :#line:675
            OOO0OO00OO00OO0OO =f'__{timi_new()}'#line:676
            O00OO0OOOOOO00000 ={'source':'scsc','authorization':O0O0O0O0000OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00OO00OO0OO ),'signstring':OOO0OO00OO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O0O0O0OO000O0OOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0OOOOOO00000 ).json ()#line:688
            if 'status'in O0O0O0OO000O0OOOO :#line:690
                if O0O0O0OO000O0OOOO ['status']==200 :#line:691
                    if O0O0O0OO000O0OOOO ['data']['result']:#line:692
                        O00OOO0OOOOOO0O0O =O0O0O0OO000O0OOOO ['data']['nick_name']#line:693
                        return O00OOO0OOOOOO0O0O #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as OOOOOOO000000O0O0 :#line:697
            print (OOOOOOO000000O0O0 )#line:698
    def crops_illustrated (OOOO0O0OOOO0OO00O ):#line:701
        try :#line:702
            O0OOO00OO000OO00O =f'__{timi_new()}'#line:703
            O00000O0O0OO00000 ={'source':'scsc','authorization':OOOO0O0OOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO000OO00O ),'signstring':O0OOO00OO000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            OOO0OOO0O0O0O000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00000O0O0OO00000 ).json ()#line:715
            if 'status'in OOO0OOO0O0O0O000O :#line:717
                if OOO0OOO0O0O0O000O ['status']==200 :#line:718
                    OOO00OOO00OOOO0O0 =OOO0OOO0O0O0O000O ['data'][0 ]['crops']#line:719
                    for OOOO00OOO000000OO in OOO00OOO00OOOO0O0 :#line:720
                        if OOOO00OOO000000OO ['ill_clover_award']:#line:721
                            if float (OOOO00OOO000000OO ['ill_clover_award'])>1 :#line:722
                                if OOOO00OOO000000OO ['is_finish']:#line:723
                                    if not OOOO00OOO000000OO ['is_getit']:#line:724
                                        if OOOO0O0OOOO0OO00O .certification ()!='未实名':#line:725
                                            O0OOO00OO000OO00O =f'_award_level={OOOO00OOO000000OO["level"]}_{timi_new()}'#line:726
                                            O00000O0O0OO00000 ={'source':'scsc','authorization':OOOO0O0OOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO000OO00O ),'signstring':O0OOO00OO000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            OOO0OO0OO00OO0OOO ={"award_level":OOOO00OOO000000OO ['level']}#line:738
                                            O0OOOO0O0OO0O00O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00000O0O0OO00000 ,json =OOO0OO0OO00OO0OOO ).json ()#line:740
                                            if 'status'in O0OOOO0O0OO0O00O0 :#line:741
                                                if O0OOOO0O0OO0O00O0 ['status']==200 :#line:742
                                                    O000OOO0OO00000O0 =O0OOOO0O0OO0O00O0 ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{OOOO00OOO000000OO["crop_name"]}成就丨奖励{O000OOO0OO00000O0}☘️')#line:745
                                                if O0OOOO0O0OO0O00O0 ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{O0OOOO0O0OO0O00O0["message"]}')#line:747
        except Exception as OO000O000OOOOO0O0 :#line:748
            print (OO000O000OOOOO0O0 )#line:749
    def watched_ad (O000OOO000000000O ):#line:752
        try :#line:753
            OOO00O0000O0O0000 =f'__{timi_new()}'#line:754
            OOO000OO0OOO00O00 ={'source':'scsc','authorization':O000OOO000000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0000O0O0000 ),'signstring':OOO00O0000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            O0OO00O0000O0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0OOO00O00 ).json ()#line:766
            if 'status'in O0OO00O0000O0OO0O :#line:768
                if O0OO00O0000O0OO0O ['status']==200 :#line:769
                    if 'offlineInfo'in O0OO00O0000O0OO0O ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        O000OO0O0000O0O0O =O0OO00O0000O0OO0O ['data']['offlineInfo']['off_minute']#line:772
                        O0OOOOOO000O00OOO =float (O0OO00O0000O0OO0O ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OO0OOO00O00 ).json ()#line:775
                        time .sleep (2 )#line:776
                        O0O0O000O00O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0OOO00O00 ).json ()#line:777
                        if 'status'in O0O0O000O00O0OOOO :#line:779
                            if O0O0O000O00O0OOOO ['status']==200 :#line:780
                                OOO00OO00O0OOOOO0 =float (O0O0O000O00O0OOOO ['data']['silver'])/1000000000000 #line:781
                                O0O00O0OO0O0OOOOO =str (OOO00OO00O0OOOOO0 -O0OOOOOO000O00OOO )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{O000OO0O0000O0O0O}分钟奖励🌱数量:{O0O00O0OO0O0OOOOO}t粒')#line:783
        except Exception as O0000OO0O0O0OOOO0 :#line:784
            print (O0000OO0O0O0OOOO0 )#line:785
    def user_ad (OO00O0O0OO0O00000 ):#line:788
        try :#line:789
            OOO0O000O00O00000 =f'__{timi_new()}'#line:790
            OOOO0O00OOO0OO0OO ={'source':'scsc','authorization':OO00O0O0OO0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00O00000 ),'signstring':OOO0O000O00O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            OO0O0O000O00O000O =requests .request ('get',f'{host}/user/ad',headers =OOOO0O00OOO0OO0OO ).json ()#line:802
            if 'status'in OO0O0O000O00O000O :#line:804
                if OO0O0O000O00O000O ['status']==200 :#line:805
                    O0OOOO0O0OOOOO000 =OO0O0O000O00O000O ['data']['max_time']#line:806
                    O000OOO0O000O0OOO =OO0O0O000O00O000O ['data']['watch_time']#line:807
                    OO0O00OO0000OO00O =OO0O0O000O00O000O ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{OO0O00OO0000OO00O + O0OOOO0O0OOOOO000 - O000OOO0O000O0OOO}次丨好友提供:{OO0O00OO0000OO00O}次')#line:809
                    if OO0O00OO0000OO00O +O0OOOO0O0OOOOO000 -O000OOO0O000O0OOO >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        O0OOO000OOOO000O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOO0O00OOO0OO0OO ).json ()#line:812
                        if 'status'in O0OOO000OOOO000O0 :#line:814
                            if O0OOO000OOOO000O0 ['status']==200 :#line:815
                                O00O0OOOOO0OOOO00 =float (O0OOO000OOOO000O0 ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(O00O0OOOOO0OOOO00)}t粒')#line:817
                                return True #line:818
                            if O0OOO000OOOO000O0 ['status']==500 :#line:819
                                O00O0O000OOOOOOO0 =O0OOO000OOOO000O0 ['message']#line:820
                                print (f'【获取种子】:{O00O0O000OOOOOOO0}')#line:821
                                return False #line:822
        except Exception as OOOO0O0OOO0OOOOO0 :#line:823
            print (OOOO0O0OOO0OOOOO0 )#line:824
    def synthetic (OOOOOO00OO0OO00OO ):#line:827
        global id ,g #line:828
        try :#line:829
            OO0O00OO00OO0OOOO =OOOOOO00OO0OO00OO .level_new ()#line:830
            OOOOO0O0OOOOO0OO0 =random .randint (9 ,11 )#line:831
            O000OO0OOOO0OO0OO =f'_site=8&targetSite={OOOOO0O0OOOOO0OO0}_{timi_new()}'#line:832
            OO0OOOO000O00000O ={'source':'scsc','authorization':OOOOOO00OO0OO00OO .token ,'timestamp':timi_new (),'sign':sign (O000OO0OOOO0OO0OO ),'signstring':O000OO0OOOO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            O0OO00OO0O000OOOO ={"site":int (8 ),"targetSite":int (OOOOO0O0OOOOO0OO0 )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOOO000O00000O ,json =O0OO00OO0O000OOOO )#line:845
            while True :#line:846
                OO00O00O000000000 =f'__{timi_new()}'#line:847
                O0000O0OO00O00O00 ={'source':'scsc','authorization':OOOOOO00OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O000000000 ),'signstring':OO00O00O000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                OO0OO000OO0O0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0OO00O00O00 ).json ()#line:859
                if 'status'in OO0OO000OO0O0O0O0 :#line:861
                    if OO0OO000OO0O0O0O0 ['status']==200 :#line:862
                        OO0O0O00OOO000OOO =OO0OO000OO0O0O0O0 ['data']['cropList']#line:863
                        O0OO0OOOOO0OOOO0O =OO0OO000OO0O0O0O0 ['data']['gameCoreDataDBid']#line:864
                        O0OO00O0000000O0O =float (OO0OO000OO0O0O0O0 ['data']['silver'])/1000000000000 #line:865
                        OO0OOOOOO0O00000O =0 #line:870
                        for O0O00O00O0O0OO0O0 in OO0O0O00OOO000OOO :#line:871
                            if not O0O00O00O0O0OO0O0 :#line:872
                                O00OOOOOO0OOO00O0 =f'_crop_id={O0OO0OOOOO0OOOO0O}&site={OO0OOOOOO0O00000O}_{OOOOOO00OO0OO00OO.time}'#line:873
                                O0O0OO0OOO00O0000 ={'source':'scsc','authorization':OOOOOO00OO0OO00OO .token ,'timestamp':OOOOOO00OO0OO00OO .time ,'sign':sign (O00OOOOOO0OOO00O0 ),'signstring':O00OOOOOO0OOO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                O0O000OO00OOOO0OO ={"site":OO0OOOOOO0O00000O ,"crop_id":O0OO0OOOOO0OOOO0O }#line:884
                                O0O0O00O00000OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0OO0OOO00O0000 ,data =O0O000OO00OOOO0OO ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in O0O0O00O00000OOOO :#line:888
                                    if O0O0O00O00000OOOO ['status']==200 :#line:889
                                        if O0O0O00O00000OOOO ['message']=='种子数量不足':#line:890
                                            OO0O00OO00OO0OOOO =OOOOOO00OO0OO00OO .level_new ()#line:891
                                            print (f'【种植合成】:{O0O0O00O00000OOOO["message"]}')#line:892
                                            if not OOOOOO00OO0OO00OO .user_ad ():#line:893
                                                return False #line:894
                                    if O0O0O00O00000OOOO ['status']==500 :#line:895
                                        print (f'【种植合成】:{O0O0O00O00000OOOO["message"]}')#line:896
                                        return False #line:897
                            OO0OOOOOO0O00000O +=1 #line:898
                        O000O000O00OO0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O0OO00O00O00 ).json ()#line:899
                        O00O0OOOO0000OOOO =O000O000O00OO0OO0 ['data']['cropList']#line:900
                        O0O0OO0OO0OOO0OO0 =False #line:901
                        for O0O00O00O0O0OO0O0 in range (12 ):#line:902
                            id =O00O0OOOO0000OOOO [O0O00O00O0O0OO0O0 ]['level']#line:903
                            if float (OO0O00OO00OO0OOOO )-float (id )>9 :#line:904
                                OO000OO0OOOOOOO00 =f'_site={O0O00O00O0O0OO0O0}_{timi_new()}'#line:905
                                O00OO00OOO0OOO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOO00OO0OO00OO .token ,'timestamp':timi_new (),'sign':sign (OO000OO0OOOOOOO00 ),'signstring':OO000OO0OOOOOOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                OO00O00OO0OO0OOOO ={"site":O0O00O00O0O0OO0O0 }#line:917
                                OOOO00OO00OOOO00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO00OOO0OOO00O ,data =OO00O00OO0OO0OOOO ).json ()#line:919
                                if 'status'in OOOO00OO00OOOO00O :#line:920
                                    if OOOO00OO00OOOO00O ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for O0OO0O0O00O0O0OO0 in range (11 ):#line:924
                                    O00OOOOOO000OO0OO =O0OO0O0O00O0O0OO0 +1 #line:925
                                    g =O00O0OOOO0000OOOO [O00OOOOOO000OO0OO ]['level']#line:926
                                    if id ==g :#line:927
                                        OOO00OO0OO000000O =O0OO0O0O00O0O0OO0 +2 #line:928
                                        if OOO00OO0OO000000O !=O0O00O00O0O0OO0O0 +1 :#line:929
                                            O00OO00OOOO000OO0 =O0O00O00O0O0OO0O0 +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            O000OO0OOOO0OO0OO =f'_site={O00OO00OOOO000OO0 - 1}&targetSite={OOO00OO0OO000000O - 1}_{timi_new()}'#line:933
                                            OO0OOOO000O00000O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOO00OO0OO00OO .token ,'timestamp':timi_new (),'sign':sign (O000OO0OOOO0OO0OO ),'signstring':O000OO0OOOO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            O00OOOO000000O0OO ={"site":int (O00OO00OOOO000OO0 -1 ),"targetSite":int (OOO00OO0OO000000O -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOOO000O00000O ,json =O00OOOO000000O0OO )#line:952
                                            O0O0OO0OO0OOO0OO0 =True #line:954
                                    if O0O0OO0OO0OOO0OO0 :#line:955
                                        break #line:956
                                if O0O0OO0OO0OOO0OO0 :#line:957
                                    break #line:958
        except :#line:959
            OOOOOO00OO0OO00OO .synthetic ()#line:960
    def level_new (O0OOO000OO0000000 ):#line:963
        try :#line:964
            O0OO0O0O000OO0O0O =f'__{timi_new()}'#line:965
            O00O00O0O000OOO0O ={'source':'scsc','authorization':O0OOO000OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O000OO0O0O ),'signstring':O0OO0O0O000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            O00O0OO00OO0000OO =requests .request ('get',f'{host}/user',headers =O00O00O0O000OOO0O ).json ()#line:977
            if 'status'in O00O0OO00OO0000OO :#line:978
                if O00O0OO00OO0000OO ['status']==200 :#line:979
                    return float (O00O0OO00OO0000OO ['data']['level'])#line:980
        except Exception as OOO0OO00O0O0OO00O :#line:981
            print (OOO0OO00O0O0OO00O )#line:982
    def propsraffle (O0OOOO0OO0O0O0O00 ):#line:985
        try :#line:986
            while True :#line:987
                O00000OOO0O000O0O =f'__{timi_new()}'#line:988
                O0O0OOOO000O0OO00 ={'source':'scsc','authorization':O0OOOO0OO0O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO0O000O0O ),'signstring':O00000OOO0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                OO00OO0O0OOOOO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0OOOO000O0OO00 ).json ()#line:1000
                if 'status'in OO00OO0O0OOOOO0O0 :#line:1002
                    if OO00OO0O0OOOOO0O0 ['status']==200 :#line:1003
                        O0OO0O0OO00000OOO =OO00OO0O0OOOOO0O0 ['data']['rows']#line:1004
                        OO0O000O0000OOO00 =OO00OO0O0OOOOO0O0 ['data']['vstate']#line:1005
                        if O0OO0O0OO00000OOO ==5 or O0OO0O0OO00000OOO ==6 or O0OO0O0OO00000OOO ==7 :#line:1006
                            O00O0OO0O0O0O0000 =OO00OO0O0OOOOO0O0 ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{O00O0OO0O0O0O0000}')#line:1008
                        if O0OO0O0OO00000OOO ==1 or O0OO0O0OO00000OOO ==2 or O0OO0O0OO00000OOO ==3 :#line:1009
                            OO00O0OOO00OOOO00 =OO00OO0O0OOOOO0O0 ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{OO00O0OOO00OOOO00}')#line:1011
                        if O0OO0O0OO00000OOO ==4 or O0OO0O0OO00000OOO ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if O0OO0O0OO00000OOO =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as O00O00O0O00O00O0O :#line:1053
            print (O00O00O0O00O00O0O )#line:1054
    def friends_invitation (O0OO0OO00000O0O0O ):#line:1057
        try :#line:1058
            O00OOOO0O0O000O00 =f'__{timi_new()}'#line:1059
            O00OOO0O000OOO000 ={'source':'scsc','authorization':O0OO0OO00000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0O0O000O00 ),'signstring':O00OOOO0O0O000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            OO00OOOOO00O0000O =requests .request ('get',f'{host}/friends',headers =O00OOO0O000OOO000 ).json ()#line:1071
            if 'status'in OO00OOOOO00O0000O :#line:1072
                if OO00OOOOO00O0000O ['status']==200 :#line:1073
                    OO0O0O0OOOO00OOOO =OO00OOOOO00O0000O ['data']['myInviteter']#line:1074
                    if OO0O0O0OOOO00OOOO :#line:1075
                        O0O00OO00OO0O0O0O =OO0O0O0OOOO00OOOO ['user']['nickname']#line:1076
                        O0OO000OO00O0O000 =O0OO0OO00000O0O0O .certification ()#line:1077
                        if O0OO000OO00O0O000 =='未实名':#line:1078
                            weishim .append (O0OO0OO00000O0O0O .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{O0O00OO00OO0O0O0O}丨实名:{O0OO000OO00O0O000}')#line:1080
                    else :#line:1081
                        if O0OO0OO00000O0O0O .innerId !='0':#line:1082
                            O0OO0OO00000O0O0O .invitation ()#line:1083
        except Exception as OO0O0OO00000OO00O :#line:1084
            print (OO0O0OO00000OO00O )#line:1085
    def add_clover (O0OOO000OOO0O00OO ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            O0OOOO0O00O0OO0OO =f'__{timi_new()}'#line:1091
            OOO00OOOOO00O000O ={'source':'scsc','authorization':O0OOO000OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O00O0OO0OO ),'signstring':O0OOOO0O00O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O0O0O00OO00OOO0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00OOOOO00O000O ).json ()#line:1103
            if 'status'in O0O0O00OO00OOO0O0 :#line:1105
                if O0O0O00OO00OOO0O0 ['status']==200 :#line:1106
                    OOOOO0OO0OOO000OO =O0O0O00OO00OOO0O0 ['data']['clover']#line:1107
                    O000OO0O0OO00O00O =O0O0O00OO00OOO0O0 ['data']['used_clover']#line:1108
                    OOOO00OOO0O000OOO =float (OOOOO0OO0OOO000OO )-float (O000OO0O0OO00O00O )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000OO0O0OO00O00O}')#line:1110
                    if O0OOO000OOO0O00OO .certification ()!='未实名':#line:1111
                        if OOOO00OOO0O000OOO >1 :#line:1112
                            O0OOOO0O00O0OO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO00OOO0O000OOO)}_{timi_new()}'#line:1113
                            O00OO00O0O0O00OO0 ={'source':'scsc','authorization':O0OOO000OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O00O0OO0OO ),'signstring':O0OOOO0O00O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            O00OOOO0OOOOO00O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO00OOO0O000OOO )}#line:1125
                            O0000O0000000OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO00O0O0O00OO0 ,data =O00OOOO0OOOOO00O0 ).json ()#line:1126
                            if 'status'in O0000O0000000OO00 :#line:1128
                                if O0000O0000000OO00 ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{O0000O0000000OO00["data"]["isSuccess"]}丨数量:{OOOO00OOO0O000OOO}')#line:1130
                                if O0000O0000000OO00 ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{O0000O0000000OO00["message"]}')#line:1132
            O000O000000O0O0O0 =requests .request ('get',f'{host}/lottery',headers =OOO00OOOOO00O000O ).json ()#line:1133
            O0000OOOOO0000000 =O0OOO000OOO0O00OO .winning_rewards ()#line:1135
            if 'status'in O000O000000O0O0O0 :#line:1136
                if O000O000000O0O0O0 ['status']==200 :#line:1137
                    O00O00OO000O00O0O =O000O000000O0O0O0 ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (O00O00OO000O00O0O )#line:1139
                    O0000OO0OOO000OOO =O000O000000O0O0O0 ['data'][1 ]['value']#line:1140
                    OOOOOOO00OO00O0OO =O000O000000O0O0O0 ['data'][0 ]['join_number']#line:1141
                    OO0O0O00O0OOO00OO =int (float (O000O000000O0O0O0 ['data'][0 ]['totalValue']))#line:1142
                    OO0OO0OOOOOO000O0 =float (O0000OO0OOO000OOO /OO0O0O00O0OOO00OO )*10000 #line:1143
                    O0OOOOOO0O0OOO0OO =OO0O0O00O0OOO00OO /OOOOOOO00OO00O0OO #line:1144
                    print (f'【参与抽奖】:预计每天中{str(O00O00OO000O00O0O)[:6]}颗金种子丨好友收益:{str(O0000OOOOO0000000)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(OO0OO0OOOOOO000O0)[:6]}颗金种子丨☘️人均:{str(O0OOOOOO0O0OOO0OO)[:7]}️')#line:1146
        except Exception as O0OO000OO0OO0O00O :#line:1147
            print (O0OO000OO0OO0O00O )#line:1148
    def energy (O0OO00OOOO000O000 ):#line:1151
        try :#line:1152
            while True :#line:1153
                OOOO00OO00O00O000 =f'__{timi_new()}'#line:1154
                OOO00O00OOO00O0OO ={'source':'scsc','authorization':O0OO00OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00O00O000 ),'signstring':OOOO00OO00O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                OOOO000OOOOOOO00O =requests .request ('get',f'{host}/energy/general',headers =OOO00O00OOO00O0OO ).json ()#line:1166
                if 'status'in OOOO000OOOOOOO00O :#line:1168
                    if OOOO000OOOOOOO00O ['status']==200 :#line:1169
                        O00O00OO0O000O0OO =OOOO000OOOOOOO00O ['data']['ordinary_water']#line:1170
                        O00OOO0O00OO0OOOO =OOOO000OOOOOOO00O ['data']['ordinary_fertilizer']#line:1171
                        O0OOO0000OOOOO000 =OOOO000OOOOOOO00O ['data']['videoStatus']#line:1172
                        OOO0OO0O00OO000OO =OOOO000OOOOOOO00O ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(O00OOO0O00OO0OOOO).split(".")[0]}丨水滴:{str(O00O00OO0O000O0OO).split(".")[0]}')#line:1175
                        if float (O00OOO0O00OO0OOOO )<96 :#line:1176
                            if O0OOO0000OOOOO000 :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                OOOO0OOO0OOO0000O =99 -float (O00OOO0O00OO0OOOO )#line:1179
                                O00O00O0O0O0O0OO0 ={"fertilizer":str (OOOO0OOO0OOO0000O ).split ('.')[0 ]}#line:1180
                                O00O0OOOO0000O0OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00O00OOO00O0OO ).json ()#line:1182
                                if 'status'in O00O0OOOO0000O0OO :#line:1184
                                    if O00O0OOOO0000O0OO ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0OOOO0000O0OO["message"]}')#line:1186
                                    if O00O0OOOO0000O0OO ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0OOOO0000O0OO["message"]}')#line:1188
                                        break #line:1189
                                if float (O00OOO0O00OO0OOOO )<78 :#line:1191
                                    OOOO0OOO0OOO0000O =80 -float (O00OOO0O00OO0OOOO )#line:1192
                                    O000O0O00O0000OOO =f'_fertilizer={int(OOOO0OOO0OOO0000O)}_{timi_new()}'#line:1193
                                    O00OO0O00O0OO0OOO ={'source':'scsc','authorization':O0OO00OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O00O0000OOO ),'signstring':O000O0O00O0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    OO000O0OO0000O000 ={"fertilizer":int (OOOO0OOO0OOO0000O )}#line:1205
                                    OO0O0OO00OO000O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00OO0O00O0OO0OOO ,data =OO000O0OO0000O000 ).json ()#line:1207
                                    if 'status'in OO0O0OO00OO000O0O :#line:1209
                                        if OO0O0OO00OO000O0O ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{OO0O0OO00OO000O0O["message"]}丨数量:{int(OOOO0OOO0OOO0000O)}')#line:1211
                                        if OO0O0OO00OO000O0O ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{OO0O0OO00OO000O0O["message"]}丨数量:{int(OOOO0OOO0OOO0000O)}')#line:1213
                                            O00OOOO00OOO0OO00 =OO0O0OO00OO000O0O ["message"].split ('-')[1 ]#line:1214
                                            OOO0OOO00OO00OOO0 =f'__{timi_new()}'#line:1215
                                            OOO00OOOOOOOOO00O ={'source':'scsc','authorization':O0OO00OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO00OO00OOO0 ),'signstring':OOO0OOO00OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            OOO0000O0O000O00O =requests .request ('get',f'{host}/user',headers =OOO00OOOOOOOOO00O ).json ()#line:1227
                                            if 'status'in OOO0000O0O000O00O :#line:1228
                                                if OOO0000O0O000O00O ['status']==200 :#line:1229
                                                    O0O0O0O00OOO0O000 =OOO0000O0O000O00O ['data']['inner_id']#line:1230
                                                    if give_gold (O0O0O0O00OOO0O000 ,float (O00OOOO00OOO0OO00 )+1 ):#line:1231
                                                        O0OO00OOOO000O000 .energy ()#line:1232
                        if float (O00O00OO0O000O0OO )<880 :#line:1233
                            if OOO0OO0O00OO000OO :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                O0O00OO00O0O000O0 =999 -float (O00O00OO0O000O0OO )#line:1236
                                O000O00OOO00000OO ={"water":str (O0O00OO00O0O000O0 ).split ('.')[0 ]}#line:1237
                                OOO0000OOOO0OO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00O00OOO00O0OO ).json ()#line:1239
                                if 'status'in OOO0000OOOO0OO0OO :#line:1241
                                    if OOO0000OOOO0OO0OO ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0000OOOO0OO0OO["message"]}')#line:1243
                                    if OOO0000OOOO0OO0OO ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0000OOOO0OO0OO["message"]}')#line:1245
                                        break #line:1246
                                if float (O00O00OO0O000O0OO )<780 :#line:1247
                                    O0O00OO00O0O000O0 =800 -float (O00O00OO0O000O0OO )#line:1248
                                    O0O000O00000O0OOO =f'_water={int(O0O00OO00O0O000O0)}_{timi_new()}'#line:1249
                                    O0O000OO000OO0OO0 ={'source':'scsc','authorization':O0OO00OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O00000O0OOO ),'signstring':O0O000O00000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    OOO00OO0000OOO000 ={"water":int (O0O00OO00O0O000O0 )}#line:1261
                                    OO0OOO0OOOO0OOO00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O000OO000OO0OO0 ,data =OOO00OO0000OOO000 ).json ()#line:1263
                                    if 'status'in OO0OOO0OOOO0OOO00 :#line:1265
                                        if OO0OOO0OOOO0OOO00 ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{OO0OOO0OOOO0OOO00["message"]}丨数量:{int(O0O00OO00O0O000O0)}')#line:1267
                                        if OO0OOO0OOOO0OOO00 ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{OO0OOO0OOOO0OOO00["message"]}丨数量:{int(O0O00OO00O0O000O0)}')#line:1269
                                            O00OOOO00OOO0OO00 =OO0OOO0OOOO0OOO00 ["message"].split ('-')[1 ]#line:1270
                                            OOO0OOO00OO00OOO0 =f'__{timi_new()}'#line:1271
                                            OOO00OOOOOOOOO00O ={'source':'scsc','authorization':O0OO00OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO00OO00OOO0 ),'signstring':OOO0OOO00OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            OOO0000O0O000O00O =requests .request ('get',f'{host}/user',headers =OOO00OOOOOOOOO00O ).json ()#line:1283
                                            if 'status'in OOO0000O0O000O00O :#line:1284
                                                if OOO0000O0O000O00O ['status']==200 :#line:1285
                                                    O0O0O0O00OOO0O000 =OOO0000O0O000O00O ['data']['inner_id']#line:1286
                                                    if give_gold (O0O0O0O00OOO0O000 ,float (O00OOOO00OOO0OO00 )+1 ):#line:1287
                                                        O0OO00OOOO000O000 .energy ()#line:1288
                        break #line:1289
        except Exception as O0O000O0O0OOOOO00 :#line:1290
            print (O0O000O0O0OOOOO00 )#line:1291
def bundled_def ():#line:1293
    OOOOO0OO00000OO0O =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return OOOOO0OO00000OO0O .split ("\n")[random .randint (0 ,len (OOOOO0OO00000OO0O .split ("\n"))-1 )]#line:1295
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
        OO00O00OO0O0OO000 =gitee_edition ()#line:1334
        if version_of_the_validation ()<OO00O00OO0O0OO000 ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O00OO0O0OO000["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{OO00O00OO0O0OO000["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00O00OO0O0OO000["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {OO00O00OO0O0OO000["CityEarth"]["content"]}')#line:1340
    except Exception as O0O0OO00O00O0000O :#line:1341
        print (O0O0OO00O00O0000O )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350

