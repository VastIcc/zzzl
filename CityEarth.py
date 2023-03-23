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
        OO0OOO0OO000O0000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO0OOO0OO000O0000)}个账号==========")#line:17
        for OOOO0OOO00O0000O0 in OO0OOO0OO000O0000 :#line:18
            OO0OOO0O0O0OOOOOO =[]#line:19
            print (f"------------正在执行第{OO0OOO0OO000O0000.index(OOOO0OOO00O0000O0) + 1}个账号------------")#line:20
            O0OO00OOO0OO00O00 =CityEarth (OOOO0OOO00O0000O0 ,OO0OOO0O0O0OOOOOO ,OO0OOO0OO000O0000 .index (OOOO0OOO00O0000O0 ))#line:21
            def O0O00OO0OOOOOO0O0 ():#line:23
                if O0OO00OOO0OO00O00 .base_info ():#line:25
                    O0OO00OOO0OO00O00 .sealing ()#line:27
                    O0OO00OOO0OO00O00 .invitenum ()#line:29
                    O0OO00OOO0OO00O00 .query_to_sell ()#line:31
                    O0OO00OOO0OO00O00 .friends_invitation ()#line:35
                    O0OO00OOO0OO00O00 .energy ()#line:37
                    O0OO00OOO0OO00O00 .add_clover ()#line:39
                    O0OO00OOO0OO00O00 .propsraffle ()#line:41
                    O0OO00OOO0OO00O00 .synthetic ()#line:43
                    O0OO00OOO0OO00O00 .crops_illustrated ()#line:45
                    O0OO00OOO0OO00O00 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0OO00OOO0OO00O00 .give_gold ()#line:50
            OOOOO0OO000O0O0O0 =threading .Thread (target =O0O00OO0OOOOOO0O0 )#line:52
            OOOOO0OO000O0O0O0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO000OOO0O00O0OO0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO000OOO0O00O0OO0 )#line:58
        time .sleep (3 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0OOO0OOO0000O0OO in invited_new :#line:62
            print (O0OOO0OOO0000O0OO )#line:63
        print ('开始打印未实名的token')#line:64
        for O0000OOO0O0OO0O0O in weishim :#line:65
            print (O0000OOO0O0OO0O0O )#line:66
    except Exception as O00000OOOO000O000 :#line:67
        print (O00000OOOO000O000 )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (O0OO00000O0OOO00O ,OOO0OOO0OO000OO0O ):#line:78
    try :#line:79
        OO000000OOO0OOO00 =f'_doneeNo={O0OO00000O0OOO00O}&quantity={int(OOO0OOO0OO000OO0O)}_{timi_new()}'#line:80
        O0O00OOO00O00OO0O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO000000OOO0OOO00 ),'signstring':OO000000OOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        O0OOOOO0000O00O00 ={"quantity":int (OOO0OOO0OO000OO0O ),"doneeNo":O0OO00000O0OOO00O }#line:95
        O000O0O0O00O0OO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OOO00O00OO0O ,data =O0OOOOO0000O00O00 ).json ()#line:96
        if 'status'in O000O0O0O00O0OO0O :#line:98
            if O000O0O0O00O0OO0O ['status']==200 :#line:99
                if O000O0O0O00O0OO0O ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(OOO0OOO0OO000OO0O)}种子给{O0OO00000O0OOO00O}成功')#line:101
                    return True #line:102
            if O000O0O0O00O0OO0O ['status']==401 :#line:103
                print (f'【赠送种子】:{O000O0O0O00O0OO0O["message"]}')#line:104
                return False #line:105
            if O000O0O0O00O0OO0O ['status']==500 :#line:106
                print (f'【赠送种子】:{O000O0O0O00O0OO0O["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as O0O0O0O00OOOO0O0O :#line:110
        print (O0O0O0O00OOOO0O0O )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (OO00O00OO0000OO0O ):#line:121
    OO000000OO0O00OOO =hashlib .md5 (OO00O00OO0000OO0O .encode ()).hexdigest ()#line:122
    O00OO0O0OOOO0000O =sc1 ()#line:123
    O0O0000000O00000O =sc2 ()#line:124
    O00OOO0OOOOOO0OOO =sc3 ()#line:125
    OOOO0OO0000O0OO00 =O00OO0O0OOOO0000O +OO000000OO0O00OOO +O0O0000000O00000O +O00OOO0OOOOOO0OOO #line:126
    OO00OOOO000OOO0O0 =hashlib .md5 (OOOO0OO0000O0OO00 .encode ()).hexdigest ()#line:127
    return OO00OOOO000OOO0O0 #line:128
def format_msg ():#line:131
    O00000OOOO00O0O00 =""#line:132
    for O0OO0OOO0O00O00OO in msg_list :#line:133
        O00000OOOO00O0O00 +=str (O0OO0OOO0O00O00OO )+"\r\n"#line:134
    return O00000OOOO00O0O00 #line:135
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
def get_json_data (O0O00OOO00OO0OOOO ,OOOO00O000O00O0OO ,OO0O000000000O0OO ,OOOO00000000O0OO0 ):#line:159
    with open (O0O00OOO00OO0OOOO ,'rb')as OOO0O0000O0O0OO0O :#line:160
        O0OO0O0OO0OOO000O =json .load (OOO0O0000O0O0OO0O )#line:161
        O0OO0O0OO0OOO000O ['data'][OOOO00O000O00O0OO ][OO0O000000000O0OO ]=OOOO00000000O0OO0 #line:162
        OO0OO0OOOO0000OO0 =O0OO0O0OO0OOO000O #line:163
    OOO0O0000O0O0OO0O .close ()#line:164
    return OO0OO0OOOO0000OO0 #line:165
def write_json_data (O0O000O0OOO00OOOO ):#line:168
    with open (json_path1 ,'w')as OO0000O0OO0OOOOO0 :#line:169
        json .dump (O0O000O0OOO00OOOO ,OO0000O0OO0OOOOO0 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    OO0000O0OO0OOOOO0 .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (OO0O00000000O0O0O ,OO0O00OOOOO0O0O00 ,O0O0O00000000OO0O ,O00OO0000OOOO0O0O ):#line:177
        try :#line:178
            OO0O00000000O0O0O .msg =O0O0O00000000OO0O #line:179
            OO0O00000000O0O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            OO0O00000000O0O0O .token =OO0O00OOOOO0O0O00 ['authorization']#line:181
            OO0O00000000O0O0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            OO0O00000000O0O0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            OO0O00000000O0O0O .elephant_user =OO0O00OOOOO0O0O00 ['elephant_user']#line:184
            OO0O00000000O0O0O .elephant_pswd =OO0O00OOOOO0O0O00 ['elephant_pswd']#line:185
            OO0O00000000O0O0O .elephant_Task_ID =OO0O00OOOOO0O0O00 ['elephant_Task_ID']#line:186
            OO0O00000000O0O0O .len_new =O00OO0000OOOO0O0O #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (OO0O0O0000O0O0O0O ):#line:192
        try :#line:193
            OO0O0O0000O0O0O0O .watched_ad ()#line:195
            OO0000OOOO0OO0OOO =f'__{timi_new()}'#line:196
            O0OO0OOOO0000000O ={'source':'scsc','authorization':OO0O0O0000O0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO0OO0OOO ),'signstring':OO0000OOOO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O000OOO00OO0O00O0 =requests .request ('get',f'{host}/user',headers =O0OO0OOOO0000000O ).json ()#line:208
            if 'status'in O000OOO00OO0O00O0 :#line:210
                if O000OOO00OO0O00O0 ['status']==200 :#line:211
                    O0OO0OO0OOO0OOOOO =O000OOO00OO0O00O0 ['data']['nickname']#line:212
                    OO0O00OOO0000O00O =O000OOO00OO0O00O0 ['data']['inner_id']#line:213
                    O00O0OO0OO000O000 =O000OOO00OO0O00O0 ['data']['assets']['gold']#line:214
                    OOO0OOO0O0O00000O =O000OOO00OO0O00O0 ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{O0OO0OO0OOO0OOOOO[:5]}丨ID:{OO0O00OOO0000O00O}丨等级:{OOO0OOO0O0O00000O}丨金种子:{str(O00O0OO0OO000O000).split(".")[0]}')#line:217
                    if 'wx_'in O0OO0OO0OOO0OOOOO :#line:218
                        OO0O0O0000O0O0O0O .change_nickname ()#line:219
                if O000OOO00OO0O00O0 ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if OO0O0O0000O0O0O0O .elephant_user =='f':#line:222
                        return False #line:223
                    O0OO0000OO0OO0000 =Invalid_login .addtask (elephant_user =OO0O0O0000O0O0O0O .elephant_user ,elephant_pswd =OO0O0O0000O0O0O0O .elephant_pswd ,elephant_Task_ID =OO0O0O0000O0O0O0O .elephant_Task_ID )#line:226
                    OO00000OO0O0OO000 =get_json_data (json_path ,OO0O0O0000O0O0O0O .len_new ,'authorization',O0OO0000OO0OO0000 )#line:227
                    if write_json_data (OO00000OO0O0OO000 ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if O000OOO00OO0O00O0 ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as OOO0O000O0O0OO0OO :#line:234
            print (OOO0O000O0O0OO0OO )#line:235
    def sealing (OOO0O0OOOOO0OO0OO ):#line:238
        try :#line:239
            O000OOO00000O0OO0 =f'__{timi_new()}'#line:240
            O0OO0OO0OOOO0O0O0 ={'source':'scsc','authorization':OOO0O0OOOOO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00000O0OO0 ),'signstring':O000OOO00000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0OO0OOOO0O0O0 )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0OO0OOOO0O0O0 )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0OO0OOOO0O0O0 )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0OO0OOOO0O0O0 )#line:255
            requests .request ('get',f'{host}/user',headers =O0OO0OO0OOOO0O0O0 )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0OO0OOOO0O0O0 )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0OO0OOOO0O0O0 )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0OO0OOOO0O0O0 )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO0OOOO0O0O0 )#line:260
            requests .request ('get',f'{host}/assets',headers =O0OO0OO0OOOO0O0O0 )#line:261
        except Exception as OO0000OOOOOO000OO :#line:262
            print (OO0000OOOOOO000OO )#line:263
    def ddd (O0O000O0OO0OOOO00 ):#line:265
        try :#line:266
            OOO0OO0O0OOOOOOOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            OO0OO00O0OOOOO000 ={'source':'scsc','authorization':O0O000O0OO0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0OOOOOOOO ),'signstring':OOO0OO0O0OOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            O000O00OO0OOOOOOO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OO00O0OOOOO000 ).json ()#line:279
            print (O000O00OO0OOOOOOO )#line:280
        except Exception as OOO0OO0O00OO00OO0 :#line:283
            print (OOO0OO0O00OO00OO0 )#line:284
    def the_query (OOO0OOO0O000O0OOO ):#line:289
        try :#line:290
            OO0O0O0O0O0O0O000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            O000O0OOO00OOOO0O ={'authorization':OOO0OOO0O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0O0O0O000 ),'signstring':OO0O0O0O0O0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0000O00OO00O0OOO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O000O0OOO00OOOO0O ).json ()#line:302
            if 'status'in O0000O00OO00O0OOO :#line:304
                if O0000O00OO00O0OOO ['status']==200 :#line:305
                    return O0000O00OO00O0OOO ['data']['rows'][4 ]['price']#line:306
        except Exception as OOOO0O00O000O00OO :#line:307
            print (OOOO0O00O000O00OO )#line:308
    def market_sale (OOO000OO00O00OOOO ,OOO000OO0O0OO0O00 ):#line:311
        try :#line:312
            O00O0O0OOO0OO0O00 =timi_new ()#line:313
            O00OO0OO0O00000O0 =f'type=crop__{O00O0O0OOO0OO0O00}'#line:314
            OO0O0OOO0OO00OO0O ={'source':'scsc','authorization':OOO000OO00O00OOOO .token ,'timestamp':str (O00O0O0OOO0OO0O00 ),'sign':sign (O00OO0OO0O00000O0 ),'signstring':O00OO0OO0O00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            OO00O0O0OO0O00OO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O0OOO0OO00OO0O ).json ()#line:326
            if 'status'in OO00O0O0OO0O00OO0 :#line:328
                if OO00O0O0OO0O00OO0 ['status']==200 :#line:329
                    if OO00O0O0OO0O00OO0 ['data']['rows']:#line:330
                        OOOOOO00OOO0O0O00 =OO00O0O0OO0O00OO0 ['data']['rows'][0 ]['packsackItemId']#line:331
                        OO00OOOOO0O00000O =OO00O0O0OO0O00OO0 ['data']['rows'][0 ]['quantity']#line:332
                        O000O00O0O0O00OOO =OOO000OO0O0OO0O00 #line:333
                        if float (OOO000OO0O0OO0O00 )>5 :#line:334
                            O00O0O0O000O00000 =f'_packsackItemId={OOOOOO00OOO0O0O00}&price={str(O000O00O0O0O00OOO)[:5]}&quantity={OO00OOOOO0O00000O}_{O00O0O0OOO0OO0O00}'#line:335
                            OOOO0OOOOO000OOOO ={'source':'scsc','authorization':OOO000OO00O00OOOO .token ,'timestamp':str (O00O0O0OOO0OO0O00 ),'sign':sign (O00O0O0O000O00000 ),'signstring':O00O0O0O000O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OO0OO0OO00O0OO0OO ={"packsackItemId":OOOOOO00OOO0O0O00 ,"price":str (O000O00O0O0O00OOO )[:5 ],"quantity":str (OO00OOOOO0O00000O )}#line:351
                            O00O0OO00O0OOO000 =requests .request ('post',f'{host}/market/sale',headers =OOOO0OOOOO000OOOO ,data =OO0OO0OO00O0OO0OO ).json ()#line:352
                            if 'status'in O00O0OO00O0OOO000 :#line:354
                                if O00O0OO00O0OOO000 ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{OO00OOOOO0O00000O}丨价格:{str(O000O00O0O0O00OOO)[:5]}')#line:356
                                if O00O0OO00O0OOO000 ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{O00O0OO00O0OOO000["message"]}')#line:358
        except Exception as O000000O0OOOO00O0 :#line:359
            print (O000000O0OOOO00O0 )#line:360
    def query_to_sell (O00OO000OO00O000O ):#line:363
        try :#line:364
            OO0O0OOOOO000OOO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:365
            O0OO0OOOOOO0OO0O0 ={'source':'scsc','authorization':O00OO000OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOO000OOO0 ),'signstring':OO0O0OOOOO000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:376
            OOOO00O00OOO0OOOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO0OOOOOO0OO0O0 ).json ()#line:377
            if 'status'in OOOO00O00OOO0OOOO :#line:379
                if OOOO00O00OOO0OOOO ['status']==200 :#line:380
                    for OOO0OOO000O0OO000 in OOOO00O00OOO0OOOO ['data']['rows']:#line:381
                        OOO0O0O0OO0OOOO00 =OOO0OOO000O0OO000 ['materialKey']#line:382
                        O0000OOO000OO000O =OOO0OOO000O0OO000 ['quantity']#line:383
                        O00O00O00O0OOOOO0 =OOO0OOO000O0OO000 ['price']#line:384
                        O000O000O00O0000O =OOO0OOO000O0OO000 ['saleState']#line:385
                        if O000O000O00O0000O ==0 :#line:386
                            print (f'【出售订单】:名称:{OOO0O0O0OO0OOOO00}丨数量:{O0000OOO000OO000O}丨价格:{O00O00O00O0OOOOO0}')#line:387
                            OO0O00OOO00000OO0 =O00OO000OO00O000O .the_query ()#line:389
                            if float (OO0O00OOO00000OO0 )!=float (O00O00O00O0OOOOO0 ):#line:390
                                OOOOOO0O00O00OOO0 =OOO0OOO000O0OO000 ['id']#line:391
                                O00OO000OO00O000O .cacel_sale (OOOOOO0O00O00OOO0 )#line:392
                    O00OO000OO00O000O .game_map ()#line:394
        except Exception as OO0OO00O000OOO0OO :#line:396
            print (OO0OO00O000OOO0OO )#line:397
    def cacel_sale (O000O0OOOOO00O000 ,OOOO0OOO0OO0O00OO ):#line:400
        try :#line:401
            O0O00OO00000OO00O =f'_saleId={OOOO0OOO0OO0O00OO}_{timi_new()}'#line:402
            OOOO0OOO0000OOOO0 ={'source':'scsc','authorization':O000O0OOOOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00000OO00O ),'signstring':O0O00OO00000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            OOO0OO0O0OOO00OOO ={"saleId":OOOO0OOO0OO0O00OO }#line:414
            O0O0OO000O0000OOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOO0OOO0000OOOO0 ,data =OOO0OO0O0OOO00OOO ).json ()#line:415
            if 'status'in O0O0OO000O0000OOO :#line:417
                if O0O0OO000O0000OOO ['status']==200 :#line:418
                    print (f'【下架出售】:{O0O0OO000O0000OOO["data"]}')#line:419
        except Exception as OOO00OOO0000OO00O :#line:420
            print (OOO00OOO0000OO00O )#line:421
    def change_nickname (O00OOO000O0O0O00O ):#line:424
        try :#line:425
            O0000000O0OO0OO0O =timi_new ()#line:426
            OO0OO0O0OOOOO00OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            O000OO00OOOOOO0O0 =requests .request ('post','https://www.qmsjmfb.com/',data =OO0OO0O0OOOOO00OO ).text #line:428
            O00OOOO0OO0O00OO0 =re .findall ('<ul><li>(.*?)</li>',O000OO00OOOOOO0O0 )[0 ][:3 ]#line:429
            O000O0O0O0O000OO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00OOOO0OO0O00OO0}').json ()#line:430
            OOO00000000OOO0OO =O000O0O0O0O000OO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:431
            O00O00OO0O00O0000 ={"nickname":OOO00000000OOO0OO }#line:432
            OO000O000OO0O0O0O =f'_nickname={OOO00000000OOO0OO}_{O0000000O0OO0OO0O}'#line:433
            OOO000OOOOO0OO000 ={'source':'scsc','authorization':O00OOO000O0O0O00O .token ,'timestamp':O0000000O0OO0OO0O ,'sign':sign (OO000O000OO0O0O0O ),'signstring':OO000O000OO0O0O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            OO0O00OO0000O0O00 =requests .request ('patch',f'{host}/user/nickname',headers =OOO000OOOOO0OO000 ,data =O00O00OO0O00O0000 ).json ()#line:445
            if 'status'in OO0O00OO0000O0O00 :#line:447
                if OO0O00OO0000O0O00 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{OOO00000000OOO0OO}丨{OO0O00OO0000O0O00["message"]}')#line:449
        except Exception as O000OOO00O0O0OOOO :#line:450
            print (O000OOO00O0O0OOOO )#line:451
    def withdraw (OOO000OO00OO0OO0O ):#line:454
        try :#line:455
            OO000OOO0O0OOO000 =f'__{timi_new()}'#line:456
            O0O0000O0O0O00OOO ={'source':'scsc','authorization':OOO000OO00OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0O0OOO000 ),'signstring':OO000OOO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OO0O0OO00OOOOO0O0 =requests .request ('get',f'{host}/assets',headers =O0O0000O0O0O00OOO ).json ()#line:468
            if 'status'in OO0O0OO00OOOOO0O0 :#line:470
                if OO0O0OO00OOOOO0O0 ['status']==200 :#line:471
                    OO0O0OOOO000OO000 =OO0O0OO00OOOOO0O0 ['data']['cash']#line:472
                    if float (OO0O0OOOO000OO000 )>20 :#line:473
                        OO000OOO0O0OOO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O0O0000O0O0O00OOO ={'authorization':OOO000OO00OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0O0OOO000 ),'signstring':OO000OOO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OOOOOO0O00O0O0O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        O0OO000O00000OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0000O0O0O00OOO ,data =OOOOOO0O00O0O0O0O ).json ()#line:487
                        if 'status'in O0OO000O00000OOOO :#line:489
                            if O0OO000O00000OOOO ['status']==200 :#line:490
                                print (f'【余额提现】:{O0OO000O00000OOOO["data"]}')#line:491
                        if 'status'in O0OO000O00000OOOO :#line:492
                            if O0OO000O00000OOOO ['status']==500 :#line:493
                                print (f'【余额提现】:{O0OO000O00000OOOO["message"]}')#line:494
        except Exception as OOO0OO0OOOO00OOOO :#line:495
            print (OOO0OO0OOOO00OOOO )#line:496
    def invitenum (O00OOOO000000OO00 ):#line:499
        global invited_new #line:500
        try :#line:501
            O0O0OO0O0O000O00O =f'__{timi_new()}'#line:502
            OO00O000O000000OO ={'source':'scsc','authorization':O00OOOO000000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0O000O00O ),'signstring':O0O0OO0O0O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O0OO00O000OOOO0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O000O000000OO ).json ()#line:514
            if 'status'in O0OO00O000OOOO0O0 :#line:516
                if O0OO00O000OOOO0O0 ['status']==200 :#line:517
                    O00OOOOO00O0O0000 =O0OO00O000OOOO0O0 ['data']['invited_count']#line:518
                    OOOO000OOO00000O0 =O0OO00O000OOOO0O0 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O00OOOOO00O0O0000}丨间邀好友:{OOOO000OOO00000O0}')#line:520
                    if O00OOOOO00O0O0000 <2 :#line:521
                        O0OOO0000O00000OO =f'__{timi_new()}'#line:522
                        O0000OO0OO0O0000O ={'source':'scsc','authorization':O00OOOO000000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000O00000OO ),'signstring':O0OOO0000O00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O0O00O0OO0OO00O00 =requests .request ('get',f'{host}/user',headers =O0000OO0OO0O0000O ).json ()#line:534
                        if 'status'in O0O00O0OO0OO00O00 :#line:536
                            if O0O00O0OO0OO00O00 ['status']==200 :#line:537
                                invited_new .append (O0O00O0OO0OO00O00 ['data']['inner_id'])#line:538
        except Exception as O0OO00OO0OO000O0O :#line:539
            print (O0OO00OO0OO000O0O )#line:540
    def game_map (OO00OO000O00O0OOO ):#line:543
        global count_list #line:544
        try :#line:545
            O00OOOO00O00O0000 =f'__{timi_new()}'#line:546
            O0OOO0OO0OOOO0O00 ={'source':'scsc','authorization':OO00OO000O00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00O00O0000 ),'signstring':O00OOOO00O00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
            O000OO00O0O0OO00O =requests .request ('get',f'{host}/game/map',headers =O0OOO0OO0OOOO0O00 ).json ()#line:558
            if 'status'in O000OO00O0O0OO00O :#line:560
                if O000OO00O0O0OO00O ['status']==200 :#line:561
                    for OOOOO00OOOO0OO00O in O000OO00O0O0OO00O ['data']['list'][0 ]['crops']:#line:562
                        OO00000O000000OOO =OOOOO00OOOO0OO00O ['level']#line:564
                        if OO00000O000000OOO ==41 :#line:565
                            OOO0OOOO000O000O0 =OOOOO00OOOO0OO00O ['crop_name']#line:566
                            O00000OO00OO00000 =OOOOO00OOOO0OO00O ['count']#line:567
                            if O00000OO00OO00000 >0 :#line:568
                                print (f'【农业资产】:{OOO0OOOO000O000O0}丨数量:{O00000OO00OO00000}')#line:569
                                count_list +=O00000OO00OO00000 #line:570
                                O0O00O00OO0O000O0 =OO00OO000O00O0OOO .the_query ()#line:571
                                OO00OO000O00O0OOO .market_sale (O0O00O00OO0O000O0 )#line:572
        except Exception as OO0O00O000O00OOO0 :#line:573
            print (OO0O00O000O00OOO0 )#line:574
    def give_gold (O0OO0000O0O000OOO ):#line:577
        try :#line:578
            OO000O0O0OOOO0000 =f'__{timi_new()}'#line:579
            OOO000O0O00OOO0OO ={'source':'scsc','authorization':O0OO0000O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OOOO0000 ),'signstring':OO000O0O0OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            OOO0OOO0OOOOO0O0O =requests .request ('get',f'{host}/user',headers =OOO000O0O00OOO0OO ).json ()#line:591
            if 'status'in OOO0OOO0OOOOO0O0O :#line:592
                if OOO0OOO0OOOOO0O0O ['status']==200 :#line:593
                    if float (O0OO0000O0O000OOO .doneeNo )!=0 :#line:594
                        O000OOO00O00OOO00 =OOO0OOO0OOOOO0O0O ['data']['assets']['gold']#line:595
                        if float (O000OOO00O00OOO00 )>float (O0OO0000O0O000OOO .innerId ):#line:596
                            O0000O00O00OO0OOO =int (float (O000OOO00O00OOO00 )/1.1 )#line:597
                            OO000O0O0OOOO0000 =f'_doneeNo={O0OO0000O0O000OOO.doneeNo}&quantity={O0000O00O00OO0OOO}_{timi_new()}'#line:598
                            OOO000O0O00OOO0OO ={'source':'scsc','authorization':O0OO0000O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OOOO0000 ),'signstring':OO000O0O0OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O0O0O0O0OOOO00000 ={"quantity":O0000O00O00OO0OOO ,"doneeNo":O0OO0000O0O000OOO .doneeNo }#line:613
                            OO00O0000O0O0000O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO000O0O00OOO0OO ,data =O0O0O0O0OOOO00000 ).json ()#line:614
                            if 'status'in OO00O0000O0O0000O :#line:616
                                if OO00O0000O0O0000O ['status']==200 :#line:617
                                    if OO00O0000O0O0000O ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O0000O00O00OO0OOO}种子给{O0OO0000O0O000OOO.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as O00OOOOO0OO000OO0 :#line:622
            print (O00OOOOO0OO000OO0 )#line:623
    def invitation (O00O0OOO000OO0000 ):#line:625
        try :#line:626
            _OOO000OO0000O0O00 =float (bundled_def ())/4 #line:627
            O0O0OO00O00O0O0O0 =f'_innerId={int(_OOO000OO0000O0O00)}_{timi_new()}'#line:629
            OOOO00O00OO000O00 ={'source':'scsc','authorization':O00O0OOO000OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00O0O0O0 ),'signstring':O0O0OO00O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            OOO0O0O0O0OO0O000 ={"innerId":int (_OOO000OO0000O0O00 )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00O00OO000O00 ,data =OOO0O0O0O0OO0O000 )#line:642
        except Exception as OOO0000O0O0O0OOOO :#line:643
            print (OOO0000O0O0O0OOOO )#line:644
    def winning_rewards (OOOOOOOO00000OO00 ):#line:647
        try :#line:648
            O00O0OOO00O0O00OO =f'__{timi_new()}'#line:649
            O0OOOO0OOO0O0OO00 ={'source':'scsc','authorization':OOOOOOOO00000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO00O0O00OO ),'signstring':O00O0OOO00O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            OO000OO0O000OO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOO0OOO0O0OO00 ).json ()#line:661
            if 'status'in OO000OO0O000OO00O :#line:663
                if OO000OO0O000OO00O ['status']==200 :#line:664
                    if OO000OO0O000OO00O ['data']['amount']:#line:665
                        O0OOO0O000O0OOOOO =OO000OO0O000OO00O ['data']['amount']['gold']#line:666
                        return O0OOO0O000O0OOOOO #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as O0OOO0O0O000OO000 :#line:670
            print (O0OOO0O0O000OO000 )#line:671
    def certification (OOOOO00000000O00O ):#line:674
        try :#line:675
            O0OOOO00000O0OO0O =f'__{timi_new()}'#line:676
            O000O0OOO000O0O0O ={'source':'scsc','authorization':OOOOO00000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00000O0OO0O ),'signstring':O0OOOO00000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            OOO0O00O0OO0O000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000O0OOO000O0O0O ).json ()#line:688
            if 'status'in OOO0O00O0OO0O000O :#line:690
                if OOO0O00O0OO0O000O ['status']==200 :#line:691
                    if OOO0O00O0OO0O000O ['data']['result']:#line:692
                        OO00OO0000OO00OOO =OOO0O00O0OO0O000O ['data']['nick_name']#line:693
                        return OO00OO0000OO00OOO #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as OOO000O00OOOOO00O :#line:697
            print (OOO000O00OOOOO00O )#line:698
    def crops_illustrated (O00O0O0OOOOOOOOO0 ):#line:701
        try :#line:702
            OO000OO00O0O000O0 =f'__{timi_new()}'#line:703
            O00OOOOO00OO0OO00 ={'source':'scsc','authorization':O00O0O0OOOOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O0O000O0 ),'signstring':OO000OO00O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            OOOOOOO0O0O0O0O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OOOOO00OO0OO00 ).json ()#line:715
            if 'status'in OOOOOOO0O0O0O0O0O :#line:717
                if OOOOOOO0O0O0O0O0O ['status']==200 :#line:718
                    OOOO00O0O000OOO00 =OOOOOOO0O0O0O0O0O ['data'][0 ]['crops']#line:719
                    for O0O000O00OOO0OO00 in OOOO00O0O000OOO00 :#line:720
                        if O0O000O00OOO0OO00 ['ill_clover_award']:#line:721
                            if float (O0O000O00OOO0OO00 ['ill_clover_award'])>1 :#line:722
                                if O0O000O00OOO0OO00 ['is_finish']:#line:723
                                    if not O0O000O00OOO0OO00 ['is_getit']:#line:724
                                        if O00O0O0OOOOOOOOO0 .certification ()!='未实名':#line:725
                                            OO000OO00O0O000O0 =f'_award_level={O0O000O00OOO0OO00["level"]}_{timi_new()}'#line:726
                                            O00OOOOO00OO0OO00 ={'source':'scsc','authorization':O00O0O0OOOOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O0O000O0 ),'signstring':OO000OO00O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            OOO0000O0O00O000O ={"award_level":O0O000O00OOO0OO00 ['level']}#line:738
                                            O00O0O0O00O00000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OOOOO00OO0OO00 ,json =OOO0000O0O00O000O ).json ()#line:740
                                            if 'status'in O00O0O0O00O00000O :#line:741
                                                if O00O0O0O00O00000O ['status']==200 :#line:742
                                                    OOOO0OOOO0OO0000O =O00O0O0O00O00000O ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{O0O000O00OOO0OO00["crop_name"]}成就丨奖励{OOOO0OOOO0OO0000O}☘️')#line:745
                                                if O00O0O0O00O00000O ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{O00O0O0O00O00000O["message"]}')#line:747
        except Exception as OO0OOO00000OO0O0O :#line:748
            print (OO0OOO00000OO0O0O )#line:749
    def watched_ad (O0O0O0OO0OOOOO00O ):#line:752
        try :#line:753
            OOOO00OO0OO00O00O =f'__{timi_new()}'#line:754
            O00O0O0O0OOO0O0OO ={'source':'scsc','authorization':O0O0O0OO0OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0OO00O00O ),'signstring':OOOO00OO0OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            OO0O00O00O000OOOO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O0OOO0O0OO ).json ()#line:766
            if 'status'in OO0O00O00O000OOOO :#line:768
                if OO0O00O00O000OOOO ['status']==200 :#line:769
                    if 'offlineInfo'in OO0O00O00O000OOOO ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        O000O0OO00O000OO0 =OO0O00O00O000OOOO ['data']['offlineInfo']['off_minute']#line:772
                        OO00O0O0OOOO0OOOO =float (OO0O00O00O000OOOO ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0O0O0OOO0O0OO ).json ()#line:775
                        time .sleep (2 )#line:776
                        O0O000O0O000O0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O0OOO0O0OO ).json ()#line:777
                        if 'status'in O0O000O0O000O0O00 :#line:779
                            if O0O000O0O000O0O00 ['status']==200 :#line:780
                                OO00000OO0O000OO0 =float (O0O000O0O000O0O00 ['data']['silver'])/1000000000000 #line:781
                                O00000OOO0OOOO0OO =str (OO00000OO0O000OO0 -OO00O0O0OOOO0OOOO )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{O000O0OO00O000OO0}分钟奖励🌱数量:{O00000OOO0OOOO0OO}t粒')#line:783
        except Exception as OO000O0O0OOOO00OO :#line:784
            print (OO000O0O0OOOO00OO )#line:785
    def user_ad (OOO00OOOOO0OOO000 ):#line:788
        try :#line:789
            OO0O0000O0OOOO0OO =f'__{timi_new()}'#line:790
            OO000O0OOOOOO0OOO ={'source':'scsc','authorization':OOO00OOOOO0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0OOOO0OO ),'signstring':OO0O0000O0OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            O0OOO000000O0OOO0 =requests .request ('get',f'{host}/user/ad',headers =OO000O0OOOOOO0OOO ).json ()#line:802
            if 'status'in O0OOO000000O0OOO0 :#line:804
                if O0OOO000000O0OOO0 ['status']==200 :#line:805
                    OO00OO0OOO000O0OO =O0OOO000000O0OOO0 ['data']['max_time']#line:806
                    OO0000000OOOOO0OO =O0OOO000000O0OOO0 ['data']['watch_time']#line:807
                    O0O0OOO0000OO0O00 =O0OOO000000O0OOO0 ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{O0O0OOO0000OO0O00 + OO00OO0OOO000O0OO - OO0000000OOOOO0OO}次丨好友提供:{O0O0OOO0000OO0O00}次')#line:809
                    if O0O0OOO0000OO0O00 +OO00OO0OOO000O0OO -OO0000000OOOOO0OO >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        OO00OOO0OOOOOO000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000O0OOOOOO0OOO ).json ()#line:812
                        if 'status'in OO00OOO0OOOOOO000 :#line:814
                            if OO00OOO0OOOOOO000 ['status']==200 :#line:815
                                OO0OOO0OOOOOO00OO =float (OO00OOO0OOOOOO000 ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(OO0OOO0OOOOOO00OO)}t粒')#line:817
                                return True #line:818
                            if OO00OOO0OOOOOO000 ['status']==500 :#line:819
                                O000OOOO000OOO00O =OO00OOO0OOOOOO000 ['message']#line:820
                                print (f'【获取种子】:{O000OOOO000OOO00O}')#line:821
                                return False #line:822
        except Exception as OOO0OO0O0OO00OO0O :#line:823
            print (OOO0OO0O0OO00OO0O )#line:824
    def synthetic (OO0O00OO00O0O0O00 ):#line:827
        global id ,g #line:828
        try :#line:829
            OOOOO0O0O000O00OO =OO0O00OO00O0O0O00 .level_new ()#line:830
            OOOOOOOO00O000O0O =random .randint (9 ,11 )#line:831
            O00O0OOO00OOO00OO =f'_site=8&targetSite={OOOOOOOO00O000O0O}_{timi_new()}'#line:832
            OO00O00O00OOOO000 ={'source':'scsc','authorization':OO0O00OO00O0O0O00 .token ,'timestamp':timi_new (),'sign':sign (O00O0OOO00OOO00OO ),'signstring':O00O0OOO00OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            OO0OO00O0OOO0000O ={"site":int (8 ),"targetSite":int (OOOOOOOO00O000O0O )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =OO00O00O00OOOO000 ,json =OO0OO00O0OOO0000O )#line:845
            while True :#line:846
                OO00OO00O0O0OOOO0 =f'__{timi_new()}'#line:847
                OOOO0OO0O0OOOOO0O ={'source':'scsc','authorization':OO0O00OO00O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O0O0OOOO0 ),'signstring':OO00OO00O0O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                O0OO00O00OOO0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OO0O0OOOOO0O ).json ()#line:859
                if 'status'in O0OO00O00OOO0OO0O :#line:861
                    if O0OO00O00OOO0OO0O ['status']==200 :#line:862
                        OO00O00O00OO0O000 =O0OO00O00OOO0OO0O ['data']['cropList']#line:863
                        O00OOO0O000OO00OO =O0OO00O00OOO0OO0O ['data']['gameCoreDataDBid']#line:864
                        OO000OO00OO0O0000 =float (O0OO00O00OOO0OO0O ['data']['silver'])/1000000000000 #line:865
                        O0O0O00O0O0O0OO00 =0 #line:870
                        for OO00OO0000OO0OOO0 in OO00O00O00OO0O000 :#line:871
                            if not OO00OO0000OO0OOO0 :#line:872
                                OOOO000OO000OO000 =f'_crop_id={O00OOO0O000OO00OO}&site={O0O0O00O0O0O0OO00}_{OO0O00OO00O0O0O00.time}'#line:873
                                OO0OOO00O00OO0OOO ={'source':'scsc','authorization':OO0O00OO00O0O0O00 .token ,'timestamp':OO0O00OO00O0O0O00 .time ,'sign':sign (OOOO000OO000OO000 ),'signstring':OOOO000OO000OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                O00OO000OOO00O0OO ={"site":O0O0O00O0O0O0OO00 ,"crop_id":O00OOO0O000OO00OO }#line:884
                                O0OO0O0O0OO00O0O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOO00O00OO0OOO ,data =O00OO000OOO00O0OO ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in O0OO0O0O0OO00O0O0 :#line:888
                                    if O0OO0O0O0OO00O0O0 ['status']==200 :#line:889
                                        if O0OO0O0O0OO00O0O0 ['message']=='种子数量不足':#line:890
                                            OOOOO0O0O000O00OO =OO0O00OO00O0O0O00 .level_new ()#line:891
                                            print (f'【种植合成】:{O0OO0O0O0OO00O0O0["message"]}')#line:892
                                            if not OO0O00OO00O0O0O00 .user_ad ():#line:893
                                                return False #line:894
                                    if O0OO0O0O0OO00O0O0 ['status']==500 :#line:895
                                        print (f'【种植合成】:{O0OO0O0O0OO00O0O0["message"]}')#line:896
                                        return False #line:897
                            O0O0O00O0O0O0OO00 +=1 #line:898
                        OOO0OO00OO00OOO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OO0O0OOOOO0O ).json ()#line:899
                        OOOOO000O00000OO0 =OOO0OO00OO00OOO00 ['data']['cropList']#line:900
                        OOOOOOOOOO0OO00O0 =False #line:901
                        for OO00OO0000OO0OOO0 in range (12 ):#line:902
                            id =OOOOO000O00000OO0 [OO00OO0000OO0OOO0 ]['level']#line:903
                            if float (OOOOO0O0O000O00OO )-float (id )>9 :#line:904
                                OOOOOO00O00OOOO0O =f'_site={OO00OO0000OO0OOO0}_{timi_new()}'#line:905
                                O0O0O0OO0OO0O0O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O00OO00O0O0O00 .token ,'timestamp':timi_new (),'sign':sign (OOOOOO00O00OOOO0O ),'signstring':OOOOOO00O00OOOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                O0000OOOOOO00000O ={"site":OO00OO0000OO0OOO0 }#line:917
                                O000OOOO0O0OOOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O0OO0OO0O0O0O ,data =O0000OOOOOO00000O ).json ()#line:919
                                if 'status'in O000OOOO0O0OOOOOO :#line:920
                                    if O000OOOO0O0OOOOOO ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for OO0OOOOO00OOOO00O in range (11 ):#line:924
                                    O00OOO0000OOOO0OO =OO0OOOOO00OOOO00O +1 #line:925
                                    g =OOOOO000O00000OO0 [O00OOO0000OOOO0OO ]['level']#line:926
                                    if id ==g :#line:927
                                        O0OO000OO0O0OOOOO =OO0OOOOO00OOOO00O +2 #line:928
                                        if O0OO000OO0O0OOOOO !=OO00OO0000OO0OOO0 +1 :#line:929
                                            O00O00OO000OO0O0O =OO00OO0000OO0OOO0 +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            O00O0OOO00OOO00OO =f'_site={O00O00OO000OO0O0O - 1}&targetSite={O0OO000OO0O0OOOOO - 1}_{timi_new()}'#line:933
                                            OO00O00O00OOOO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O00OO00O0O0O00 .token ,'timestamp':timi_new (),'sign':sign (O00O0OOO00OOO00OO ),'signstring':O00O0OOO00OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            O0O0OO000OOOOO0O0 ={"site":int (O00O00OO000OO0O0O -1 ),"targetSite":int (O0OO000OO0O0OOOOO -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00O00O00OOOO000 ,json =O0O0OO000OOOOO0O0 )#line:952
                                            OOOOOOOOOO0OO00O0 =True #line:954
                                    if OOOOOOOOOO0OO00O0 :#line:955
                                        break #line:956
                                if OOOOOOOOOO0OO00O0 :#line:957
                                    break #line:958
        except :#line:959
            OO0O00OO00O0O0O00 .synthetic ()#line:960
    def level_new (OO00OO00000O00OOO ):#line:963
        try :#line:964
            OO0O00OOOO00O0O0O =f'__{timi_new()}'#line:965
            OOO00000OO0OO000O ={'source':'scsc','authorization':OO00OO00000O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOO00O0O0O ),'signstring':OO0O00OOOO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            OOOOOOO00OO0O00O0 =requests .request ('get',f'{host}/user',headers =OOO00000OO0OO000O ).json ()#line:977
            if 'status'in OOOOOOO00OO0O00O0 :#line:978
                if OOOOOOO00OO0O00O0 ['status']==200 :#line:979
                    return float (OOOOOOO00OO0O00O0 ['data']['level'])#line:980
        except Exception as OO000O00OOO00OO0O :#line:981
            print (OO000O00OOO00OO0O )#line:982
    def propsraffle (O00OO0OO0O0000000 ):#line:985
        try :#line:986
            while True :#line:987
                O00O0O0OO0O00O000 =f'__{timi_new()}'#line:988
                OOO0O0OOO0O0O00OO ={'source':'scsc','authorization':O00OO0OO0O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO0O00O000 ),'signstring':O00O0O0OO0O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                OOO00000O0000O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O0OOO0O0O00OO ).json ()#line:1000
                if 'status'in OOO00000O0000O00O :#line:1002
                    if OOO00000O0000O00O ['status']==200 :#line:1003
                        OO000O0O000O0O0OO =OOO00000O0000O00O ['data']['rows']#line:1004
                        O0OOOOO0O000O00OO =OOO00000O0000O00O ['data']['vstate']#line:1005
                        if OO000O0O000O0O0OO ==5 or OO000O0O000O0O0OO ==6 or OO000O0O000O0O0OO ==7 :#line:1006
                            OO000000000000O00 =OOO00000O0000O00O ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{OO000000000000O00}')#line:1008
                        if OO000O0O000O0O0OO ==1 or OO000O0O000O0O0OO ==2 or OO000O0O000O0O0OO ==3 :#line:1009
                            O000O000O0O00O00O =OOO00000O0000O00O ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{O000O000O0O00O00O}')#line:1011
                        if OO000O0O000O0O0OO ==4 or OO000O0O000O0O0OO ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if OO000O0O000O0O0OO =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as O0OO0OOOOO0OOOO00 :#line:1053
            print (O0OO0OOOOO0OOOO00 )#line:1054
    def friends_invitation (OOOOO00OOO0O00000 ):#line:1057
        try :#line:1058
            OO00O00OOOOO0O000 =f'__{timi_new()}'#line:1059
            OOO0O0O0OO00OO000 ={'source':'scsc','authorization':OOOOO00OOO0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOO0O000 ),'signstring':OO00O00OOOOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            OO0OO0O0O0000OO00 =requests .request ('get',f'{host}/friends',headers =OOO0O0O0OO00OO000 ).json ()#line:1071
            if 'status'in OO0OO0O0O0000OO00 :#line:1072
                if OO0OO0O0O0000OO00 ['status']==200 :#line:1073
                    O00O000O0O000OOO0 =OO0OO0O0O0000OO00 ['data']['myInviteter']#line:1074
                    if O00O000O0O000OOO0 :#line:1075
                        O000OO000O0O000OO =O00O000O0O000OOO0 ['user']['nickname']#line:1076
                        OO00O0O000OO0O0O0 =OOOOO00OOO0O00000 .certification ()#line:1077
                        if OO00O0O000OO0O0O0 =='未实名':#line:1078
                            weishim .append (OOOOO00OOO0O00000 .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{O000OO000O0O000OO}丨实名:{OO00O0O000OO0O0O0}')#line:1080
                    else :#line:1081
                        if OOOOO00OOO0O00000 .innerId !='0':#line:1082
                            OOOOO00OOO0O00000 .invitation ()#line:1083
        except Exception as OO0OOOO000O00000O :#line:1084
            print (OO0OOOO000O00000O )#line:1085
    def add_clover (O0OO00OO0OOOO00O0 ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            O0OO00O0000O00OO0 =f'__{timi_new()}'#line:1091
            OOO00OOOOO0OO0OO0 ={'source':'scsc','authorization':O0OO00OO0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0000O00OO0 ),'signstring':O0OO00O0000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O00O0OOO00OO000OO =requests .request ('get',f'{host}/assets/clovers',headers =OOO00OOOOO0OO0OO0 ).json ()#line:1103
            if 'status'in O00O0OOO00OO000OO :#line:1105
                if O00O0OOO00OO000OO ['status']==200 :#line:1106
                    O0O00O00OO0000000 =O00O0OOO00OO000OO ['data']['clover']#line:1107
                    O000OO0OOOO000000 =O00O0OOO00OO000OO ['data']['used_clover']#line:1108
                    OOO0000O0000OO0OO =float (O0O00O00OO0000000 )-float (O000OO0OOOO000000 )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000OO0OOOO000000}')#line:1110
                    if O0OO00OO0OOOO00O0 .certification ()!='未实名':#line:1111
                        if OOO0000O0000OO0OO >1 :#line:1112
                            O0OO00O0000O00OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0000O0000OO0OO)}_{timi_new()}'#line:1113
                            O00OOO00OOOO0OO0O ={'source':'scsc','authorization':O0OO00OO0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0000O00OO0 ),'signstring':O0OO00O0000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            O0000OO00000O0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0000O0000OO0OO )}#line:1125
                            O00000O00OO00OOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OOO00OOOO0OO0O ,data =O0000OO00000O0O00 ).json ()#line:1126
                            if 'status'in O00000O00OO00OOO0 :#line:1128
                                if O00000O00OO00OOO0 ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{O00000O00OO00OOO0["data"]["isSuccess"]}丨数量:{OOO0000O0000OO0OO}')#line:1130
                                if O00000O00OO00OOO0 ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{O00000O00OO00OOO0["message"]}')#line:1132
            OOOO0000O0O0O000O =requests .request ('get',f'{host}/lottery',headers =OOO00OOOOO0OO0OO0 ).json ()#line:1133
            O00O00O0000OOO0O0 =O0OO00OO0OOOO00O0 .winning_rewards ()#line:1135
            if 'status'in OOOO0000O0O0O000O :#line:1136
                if OOOO0000O0O0O000O ['status']==200 :#line:1137
                    OOO00OO000OOOO000 =OOOO0000O0O0O000O ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (OOO00OO000OOOO000 )#line:1139
                    O0000OO00OO000OOO =OOOO0000O0O0O000O ['data'][1 ]['value']#line:1140
                    OOOO0000O0O00O000 =OOOO0000O0O0O000O ['data'][0 ]['join_number']#line:1141
                    OOOO0O0OO00OO00OO =int (float (OOOO0000O0O0O000O ['data'][0 ]['totalValue']))#line:1142
                    O0O00O0OO0OOOOOOO =float (O0000OO00OO000OOO /OOOO0O0OO00OO00OO )*10000 #line:1143
                    OOOOOOO0O00OOO000 =OOOO0O0OO00OO00OO /OOOO0000O0O00O000 #line:1144
                    print (f'【参与抽奖】:预计每天中{str(OOO00OO000OOOO000)[:6]}颗金种子丨好友收益:{str(O00O00O0000OOO0O0)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(O0O00O0OO0OOOOOOO)[:6]}颗金种子丨☘️人均:{str(OOOOOOO0O00OOO000)[:7]}️')#line:1146
        except Exception as OO00OOOOO000O0000 :#line:1147
            print (OO00OOOOO000O0000 )#line:1148
    def energy (OOOOOO00OO0000000 ):#line:1151
        try :#line:1152
            while True :#line:1153
                O0O0O00000O0O00O0 =f'__{timi_new()}'#line:1154
                OOO00O0OOOO000OOO ={'source':'scsc','authorization':OOOOOO00OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00000O0O00O0 ),'signstring':O0O0O00000O0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                OO0O00OOO000O000O =requests .request ('get',f'{host}/energy/general',headers =OOO00O0OOOO000OOO ).json ()#line:1166
                if 'status'in OO0O00OOO000O000O :#line:1168
                    if OO0O00OOO000O000O ['status']==200 :#line:1169
                        O0O00O00OO00OO0O0 =OO0O00OOO000O000O ['data']['ordinary_water']#line:1170
                        OOO0OO0O000O000O0 =OO0O00OOO000O000O ['data']['ordinary_fertilizer']#line:1171
                        OO0OOO0OOO0O00O00 =OO0O00OOO000O000O ['data']['videoStatus']#line:1172
                        OO0OOO000OOO0O00O =OO0O00OOO000O000O ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(OOO0OO0O000O000O0).split(".")[0]}丨水滴:{str(O0O00O00OO00OO0O0).split(".")[0]}')#line:1175
                        if float (OOO0OO0O000O000O0 )<96 :#line:1176
                            if OO0OOO0OOO0O00O00 :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                OOO0OO00O00000O0O =99 -float (OOO0OO0O000O000O0 )#line:1179
                                O0000O00O0OO0O0OO ={"fertilizer":str (OOO0OO00O00000O0O ).split ('.')[0 ]}#line:1180
                                OOO0O000O0OOO0OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00O0OOOO000OOO ).json ()#line:1182
                                if 'status'in OOO0O000O0OOO0OOO :#line:1184
                                    if OOO0O000O0OOO0OOO ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{OOO0O000O0OOO0OOO["message"]}')#line:1186
                                    if OOO0O000O0OOO0OOO ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{OOO0O000O0OOO0OOO["message"]}')#line:1188
                                        break #line:1189
                                if float (OOO0OO0O000O000O0 )<78 :#line:1191
                                    OOO0OO00O00000O0O =80 -float (OOO0OO0O000O000O0 )#line:1192
                                    OO0OOO0000O0OO0O0 =f'_fertilizer={int(OOO0OO00O00000O0O)}_{timi_new()}'#line:1193
                                    OOOOOOO00OOOOO000 ={'source':'scsc','authorization':OOOOOO00OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000O0OO0O0 ),'signstring':OO0OOO0000O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    O0O0O000O000O0O0O ={"fertilizer":int (OOO0OO00O00000O0O )}#line:1205
                                    OOOO0O0OO0000OOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOOOO00OOOOO000 ,data =O0O0O000O000O0O0O ).json ()#line:1207
                                    if 'status'in OOOO0O0OO0000OOO0 :#line:1209
                                        if OOOO0O0OO0000OOO0 ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{OOOO0O0OO0000OOO0["message"]}丨数量:{int(OOO0OO00O00000O0O)}')#line:1211
                                        if OOOO0O0OO0000OOO0 ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{OOOO0O0OO0000OOO0["message"]}丨数量:{int(OOO0OO00O00000O0O)}')#line:1213
                                            O0O00OO000O0O0OOO =OOOO0O0OO0000OOO0 ["message"].split ('-')[1 ]#line:1214
                                            OO0000O0OOOO000OO =f'__{timi_new()}'#line:1215
                                            O0000O0OO00O0000O ={'source':'scsc','authorization':OOOOOO00OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0OOOO000OO ),'signstring':OO0000O0OOOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            OO0000O00OOOO00O0 =requests .request ('get',f'{host}/user',headers =O0000O0OO00O0000O ).json ()#line:1227
                                            if 'status'in OO0000O00OOOO00O0 :#line:1228
                                                if OO0000O00OOOO00O0 ['status']==200 :#line:1229
                                                    O0O000OO000O0OOOO =OO0000O00OOOO00O0 ['data']['inner_id']#line:1230
                                                    if give_gold (O0O000OO000O0OOOO ,float (O0O00OO000O0O0OOO )+1 ):#line:1231
                                                        OOOOOO00OO0000000 .energy ()#line:1232
                        if float (O0O00O00OO00OO0O0 )<880 :#line:1233
                            if OO0OOO000OOO0O00O :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                O0OOO00OOOO00OO00 =999 -float (O0O00O00OO00OO0O0 )#line:1236
                                OO0000OOO00O0O0OO ={"water":str (O0OOO00OOOO00OO00 ).split ('.')[0 ]}#line:1237
                                OO00O0OO0OO00O0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00O0OOOO000OOO ).json ()#line:1239
                                if 'status'in OO00O0OO0OO00O0O0 :#line:1241
                                    if OO00O0OO0OO00O0O0 ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{OO00O0OO0OO00O0O0["message"]}')#line:1243
                                    if OO00O0OO0OO00O0O0 ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{OO00O0OO0OO00O0O0["message"]}')#line:1245
                                        break #line:1246
                                if float (O0O00O00OO00OO0O0 )<780 :#line:1247
                                    O0OOO00OOOO00OO00 =800 -float (O0O00O00OO00OO0O0 )#line:1248
                                    OOO000O0O0O00OOO0 =f'_water={int(O0OOO00OOOO00OO00)}_{timi_new()}'#line:1249
                                    OOO0OOOO00O000000 ={'source':'scsc','authorization':OOOOOO00OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0O00OOO0 ),'signstring':OOO000O0O0O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    O00O00O00O00O0000 ={"water":int (O0OOO00OOOO00OO00 )}#line:1261
                                    OO0O0OOOO0O0O0O00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0OOOO00O000000 ,data =O00O00O00O00O0000 ).json ()#line:1263
                                    if 'status'in OO0O0OOOO0O0O0O00 :#line:1265
                                        if OO0O0OOOO0O0O0O00 ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{OO0O0OOOO0O0O0O00["message"]}丨数量:{int(O0OOO00OOOO00OO00)}')#line:1267
                                        if OO0O0OOOO0O0O0O00 ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{OO0O0OOOO0O0O0O00["message"]}丨数量:{int(O0OOO00OOOO00OO00)}')#line:1269
                                            O0O00OO000O0O0OOO =OO0O0OOOO0O0O0O00 ["message"].split ('-')[1 ]#line:1270
                                            OO0000O0OOOO000OO =f'__{timi_new()}'#line:1271
                                            O0000O0OO00O0000O ={'source':'scsc','authorization':OOOOOO00OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0OOOO000OO ),'signstring':OO0000O0OOOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            OO0000O00OOOO00O0 =requests .request ('get',f'{host}/user',headers =O0000O0OO00O0000O ).json ()#line:1283
                                            if 'status'in OO0000O00OOOO00O0 :#line:1284
                                                if OO0000O00OOOO00O0 ['status']==200 :#line:1285
                                                    O0O000OO000O0OOOO =OO0000O00OOOO00O0 ['data']['inner_id']#line:1286
                                                    if give_gold (O0O000OO000O0OOOO ,float (O0O00OO000O0O0OOO )+1 ):#line:1287
                                                        OOOOOO00OO0000000 .energy ()#line:1288
                        break #line:1289
        except Exception as O0O0OOOOOOO00O0OO :#line:1290
            print (O0O0OOOOOOO00O0OO )#line:1291
def bundled_def ():#line:1293
    O0OOOOOOOO00000OO =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return O0OOOOOOOO00000OO .split ("\n")[random .randint (0 ,len (O0OOOOOOOO00000OO .split ("\n"))-1 )]#line:1295
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
        O0O0OOO000O0O0O00 =gitee_edition ()#line:1334
        if version_of_the_validation ()<O0O0OOO000O0O0O00 ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO000O0O0O00["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{O0O0OOO000O0O0O00["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO000O0O0O00["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {O0O0OOO000O0O0O00["CityEarth"]["content"]}')#line:1340
    except Exception as O000OO00O0OOO0OOO :#line:1341
        print (O000OO00O0OOO0OOO )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350

