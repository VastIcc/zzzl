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
        O000OO000OO0O0000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O000OO000OO0O0000)}个账号==========")#line:17
        for O0O0000OO00000O00 in O000OO000OO0O0000 :#line:18
            O000O000OO00O0OO0 =[]#line:19
            print (f"------------正在执行第{O000OO000OO0O0000.index(O0O0000OO00000O00) + 1}个账号------------")#line:20
            OOO0O0O00O0OOO0O0 =CityEarth (O0O0000OO00000O00 ,O000O000OO00O0OO0 ,O000OO000OO0O0000 .index (O0O0000OO00000O00 ))#line:21
            def OO00OOOOO000O000O ():#line:23
                if OOO0O0O00O0OOO0O0 .base_info ():#line:25
                    OOO0O0O00O0OOO0O0 .sealing ()#line:27
                    OOO0O0O00O0OOO0O0 .invitenum ()#line:29
                    OOO0O0O00O0OOO0O0 .query_to_sell ()#line:31
                    OOO0O0O00O0OOO0O0 .friends_invitation ()#line:35
                    OOO0O0O00O0OOO0O0 .energy ()#line:37
                    OOO0O0O00O0OOO0O0 .add_clover ()#line:39
                    OOO0O0O00O0OOO0O0 .propsraffle ()#line:41
                    OOO0O0O00O0OOO0O0 .synthetic ()#line:43
                    OOO0O0O00O0OOO0O0 .crops_illustrated ()#line:45
                    OOO0O0O00O0OOO0O0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO0O0O00O0OOO0O0 .give_gold ()#line:50
            OOOOOOO0000000O0O =threading .Thread (target =OO00OOOOO000O000O )#line:52
            OOOOOOO0000000O0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0O0OO0OO0O000O0O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0OO0OO0O000O0O +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOO0O0O0O000OO00 in invited_new :#line:62
            print (OOOO0O0O0O000OO00 )#line:63
        print ('开始打印未实名的token')#line:64
        for OOO000O00OOOO00O0 in weishim :#line:65
            print (OOO000O00OOOO00O0 )#line:66
    except Exception as O0OOO00O0O0OO00O0 :#line:67
        print (O0OOO00O0O0OO00O0 )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (O00000OO000OOO0OO ,O000OO0OOO0O0OOOO ):#line:78
    try :#line:79
        O0000OOO0OOO0O000 =f'_doneeNo={O00000OO000OOO0OO}&quantity={int(O000OO0OOO0O0OOOO)}_{timi_new()}'#line:80
        OO00O000O00OO0000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OOO0O000 ),'signstring':O0000OOO0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        OO0OO0OOO00OO0O0O ={"quantity":int (O000OO0OOO0O0OOOO ),"doneeNo":O00000OO000OOO0OO }#line:95
        O00OO000O0O0O000O =requests .request ('post',f'{host}/finance/give-gold',headers =OO00O000O00OO0000 ,data =OO0OO0OOO00OO0O0O ).json ()#line:96
        if 'status'in O00OO000O0O0O000O :#line:98
            if O00OO000O0O0O000O ['status']==200 :#line:99
                if O00OO000O0O0O000O ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(O000OO0OOO0O0OOOO)}种子给{O00000OO000OOO0OO}成功')#line:101
                    return True #line:102
            if O00OO000O0O0O000O ['status']==401 :#line:103
                print (f'【赠送种子】:{O00OO000O0O0O000O["message"]}')#line:104
                return False #line:105
            if O00OO000O0O0O000O ['status']==500 :#line:106
                print (f'【赠送种子】:{O00OO000O0O0O000O["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as OOO00OOO0000000O0 :#line:110
        print (OOO00OOO0000000O0 )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (OO00OO0OO00O0O000 ):#line:121
    O000OO0000O00O00O =hashlib .md5 (OO00OO0OO00O0O000 .encode ()).hexdigest ()#line:122
    OO00000O00OO000OO =sc1 ()#line:123
    OO00OO00OO0OO00OO =sc2 ()#line:124
    OO000OOO0O0OO000O =sc3 ()#line:125
    O0OO000OO0OO0O000 =OO00000O00OO000OO +O000OO0000O00O00O +OO00OO00OO0OO00OO +OO000OOO0O0OO000O #line:126
    OOOOO0O0000OOOOOO =hashlib .md5 (O0OO000OO0OO0O000 .encode ()).hexdigest ()#line:127
    return OOOOO0O0000OOOOOO #line:128
def format_msg ():#line:131
    O0O000000000OOOO0 =""#line:132
    for O000000OO00OO0OOO in msg_list :#line:133
        O0O000000000OOOO0 +=str (O000000OO00OO0OOO )+"\r\n"#line:134
    return O0O000000000OOOO0 #line:135
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
def get_json_data (OO0OOO0000O0OO0OO ,O0OO0O0OO0O00OOO0 ,O000OO0OO00OO0000 ,O0OO0O0O00OOOO0OO ):#line:159
    with open (OO0OOO0000O0OO0OO ,'rb')as OO00O0O0OO0000O00 :#line:160
        OOO0OO00O0000000O =json .load (OO00O0O0OO0000O00 )#line:161
        OOO0OO00O0000000O ['data'][O0OO0O0OO0O00OOO0 ][O000OO0OO00OO0000 ]=O0OO0O0O00OOOO0OO #line:162
        OOOO0OO00000000OO =OOO0OO00O0000000O #line:163
    OO00O0O0OO0000O00 .close ()#line:164
    return OOOO0OO00000000OO #line:165
def write_json_data (O000OOO00O000O000 ):#line:168
    with open (json_path1 ,'w')as O00000O00O000O0OO :#line:169
        json .dump (O000OOO00O000O000 ,O00000O00O000O0OO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    O00000O00O000O0OO .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (OOO0O0O0OOO0OOO00 ,O00OOO00O0O0OO0OO ,OO00OOO00O0OO00OO ,OOO00O000000OO0OO ):#line:177
        try :#line:178
            OOO0O0O0OOO0OOO00 .msg =OO00OOO00O0OO00OO #line:179
            OOO0O0O0OOO0OOO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            OOO0O0O0OOO0OOO00 .token =O00OOO00O0O0OO0OO ['authorization']#line:181
            OOO0O0O0OOO0OOO00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            OOO0O0O0OOO0OOO00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            OOO0O0O0OOO0OOO00 .elephant_user =O00OOO00O0O0OO0OO ['elephant_user']#line:184
            OOO0O0O0OOO0OOO00 .elephant_pswd =O00OOO00O0O0OO0OO ['elephant_pswd']#line:185
            OOO0O0O0OOO0OOO00 .elephant_Task_ID =O00OOO00O0O0OO0OO ['elephant_Task_ID']#line:186
            OOO0O0O0OOO0OOO00 .len_new =OOO00O000000OO0OO #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (O0O0O0OO000O00O00 ):#line:192
        try :#line:193
            O0O0O0OO000O00O00 .watched_ad ()#line:195
            O0O00O0OO00OO0OOO =f'__{timi_new()}'#line:196
            O000000O0OOO0OOO0 ={'source':'scsc','authorization':O0O0O0OO000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO00OO0OOO ),'signstring':O0O00O0OO00OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            OOO000OO0000O00O0 =requests .request ('get',f'{host}/user',headers =O000000O0OOO0OOO0 ).json ()#line:208
            if 'status'in OOO000OO0000O00O0 :#line:210
                if OOO000OO0000O00O0 ['status']==200 :#line:211
                    O0OO0O00O0OOOOO00 =OOO000OO0000O00O0 ['data']['nickname']#line:212
                    OOO00O00OO0000O00 =OOO000OO0000O00O0 ['data']['inner_id']#line:213
                    O000OO0OOOOO00O0O =OOO000OO0000O00O0 ['data']['assets']['gold']#line:214
                    OO00O0O0OOO0O0OOO =OOO000OO0000O00O0 ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{O0OO0O00O0OOOOO00[:5]}丨ID:{OOO00O00OO0000O00}丨等级:{OO00O0O0OOO0O0OOO}丨金种子:{str(O000OO0OOOOO00O0O).split(".")[0]}')#line:217
                    if 'wx_'in O0OO0O00O0OOOOO00 :#line:218
                        O0O0O0OO000O00O00 .change_nickname ()#line:219
                if OOO000OO0000O00O0 ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if O0O0O0OO000O00O00 .elephant_user =='f':#line:222
                        return False #line:223
                    O0O00O0O0OOO0O0O0 =Invalid_login .addtask (elephant_user =O0O0O0OO000O00O00 .elephant_user ,elephant_pswd =O0O0O0OO000O00O00 .elephant_pswd ,elephant_Task_ID =O0O0O0OO000O00O00 .elephant_Task_ID )#line:226
                    OO0O0OO00000OOO0O =get_json_data (json_path ,O0O0O0OO000O00O00 .len_new ,'authorization',O0O00O0O0OOO0O0O0 )#line:227
                    if write_json_data (OO0O0OO00000OOO0O ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if OOO000OO0000O00O0 ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as OOO000O00OO00O000 :#line:234
            print (OOO000O00OO00O000 )#line:235
    def sealing (O0O0OO0OO0OOOO0O0 ):#line:238
        try :#line:239
            OO000000O0OOOOOO0 =f'__{timi_new()}'#line:240
            O00OOOOO0O0O0OOO0 ={'source':'scsc','authorization':O0O0OO0OO0OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0OOOOOO0 ),'signstring':OO000000O0OOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOOO0O0O0OOO0 )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOOO0O0O0OOO0 )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOOO0O0O0OOO0 )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOOO0O0O0OOO0 )#line:255
            requests .request ('get',f'{host}/user',headers =O00OOOOO0O0O0OOO0 )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOOO0O0O0OOO0 )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOOO0O0O0OOO0 )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOOO0O0O0OOO0 )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOO0O0O0OOO0 )#line:260
            requests .request ('get',f'{host}/assets',headers =O00OOOOO0O0O0OOO0 )#line:261
        except Exception as O000OOO00O000OOOO :#line:262
            print (O000OOO00O000OOOO )#line:263
    def ddd (O00O0000O000O0O00 ):#line:265
        try :#line:266
            O0OO000O0OO0O0OOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            O000O00O0000O00OO ={'source':'scsc','authorization':O00O0000O000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0OO0O0OOO ),'signstring':O0OO000O0OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            OO000OOOOO00OO000 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O000O00O0000O00OO ).json ()#line:279
            print (OO000OOOOO00OO000 )#line:280
        except Exception as O0O00OOOOO000OOO0 :#line:283
            print (O0O00OOOOO000OOO0 )#line:284
    def the_query (OO0O0OOO00O00O0OO ):#line:289
        try :#line:290
            O0O0OO0OO0OO0OOO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            O00000000OO000OO0 ={'authorization':OO0O0OOO00O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO0OO0OOO0 ),'signstring':O0O0OO0OO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            OO00OO0OOO0OOOO0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00000000OO000OO0 ).json ()#line:302
            if 'status'in OO00OO0OOO0OOOO0O :#line:304
                if OO00OO0OOO0OOOO0O ['status']==200 :#line:305
                    return OO00OO0OOO0OOOO0O ['data']['rows'][4 ]['price']#line:306
        except Exception as O0OO00O0O000O0O00 :#line:307
            print (O0OO00O0O000O0O00 )#line:308
    def market_sale (O0OOO0OO0OO00OOOO ,O0OO0000O0O0O0OO0 ):#line:311
        try :#line:312
            OO0OOOOO00OO00OO0 =timi_new ()#line:313
            OOO0O0OO000O00O0O =f'type=crop__{OO0OOOOO00OO00OO0}'#line:314
            O00O0O00OO0O00000 ={'source':'scsc','authorization':O0OOO0OO0OO00OOOO .token ,'timestamp':str (OO0OOOOO00OO00OO0 ),'sign':sign (OOO0O0OO000O00O0O ),'signstring':OOO0O0OO000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            O00O0OO0OO00OO00O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00O0O00OO0O00000 ).json ()#line:326
            if 'status'in O00O0OO0OO00OO00O :#line:328
                if O00O0OO0OO00OO00O ['status']==200 :#line:329
                    if O00O0OO0OO00OO00O ['data']['rows']:#line:330
                        OO0OO00O00O00OOOO =O00O0OO0OO00OO00O ['data']['rows'][0 ]['packsackItemId']#line:331
                        O0O000OO000OOO0OO =O00O0OO0OO00OO00O ['data']['rows'][0 ]['quantity']#line:332
                        OO0OOOOO00O0OO00O =O0OO0000O0O0O0OO0 #line:333
                        if float (O0OO0000O0O0O0OO0 )>5 :#line:334
                            O0O00O0O000OO00O0 =f'_packsackItemId={OO0OO00O00O00OOOO}&price={str(OO0OOOOO00O0OO00O)[:5]}&quantity={O0O000OO000OOO0OO}_{OO0OOOOO00OO00OO0}'#line:335
                            O0OOO0OOOO0O00O00 ={'source':'scsc','authorization':O0OOO0OO0OO00OOOO .token ,'timestamp':str (OO0OOOOO00OO00OO0 ),'sign':sign (O0O00O0O000OO00O0 ),'signstring':O0O00O0O000OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OOOOO0O00OOO00O0O ={"packsackItemId":OO0OO00O00O00OOOO ,"price":str (OO0OOOOO00O0OO00O )[:5 ],"quantity":str (O0O000OO000OOO0OO )}#line:351
                            O0O0O00OO0000000O =requests .request ('post',f'{host}/market/sale',headers =O0OOO0OOOO0O00O00 ,data =OOOOO0O00OOO00O0O ).json ()#line:352
                            if 'status'in O0O0O00OO0000000O :#line:354
                                if O0O0O00OO0000000O ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{O0O000OO000OOO0OO}丨价格:{str(OO0OOOOO00O0OO00O)[:5]}')#line:356
                                if O0O0O00OO0000000O ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{O0O0O00OO0000000O["message"]}')#line:358
        except Exception as OO0OO0000OOOOOO00 :#line:359
            print (OO0OO0000OOOOOO00 )#line:360
    def query_to_sell (O0OO00OOO00O00O00 ):#line:363
        try :#line:364
            OOOOO000OO00OOO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:365
            O0000O0O000OOO00O ={'source':'scsc','authorization':O0OO00OOO00O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000OO00OOO00 ),'signstring':OOOOO000OO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:376
            OO0OO00O00O0O0OO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0000O0O000OOO00O ).json ()#line:377
            if 'status'in OO0OO00O00O0O0OO0 :#line:379
                if OO0OO00O00O0O0OO0 ['status']==200 :#line:380
                    for O0O0O0OO00O0OOOO0 in OO0OO00O00O0O0OO0 ['data']['rows']:#line:381
                        OO00000O0OO00000O =O0O0O0OO00O0OOOO0 ['materialKey']#line:382
                        O0000OO00O0O0O00O =O0O0O0OO00O0OOOO0 ['quantity']#line:383
                        OO0O0000OO00O00OO =O0O0O0OO00O0OOOO0 ['price']#line:384
                        OO00O0OO0O0OO00O0 =O0O0O0OO00O0OOOO0 ['saleState']#line:385
                        if OO00O0OO0O0OO00O0 ==0 :#line:386
                            print (f'【出售订单】:名称:{OO00000O0OO00000O}丨数量:{O0000OO00O0O0O00O}丨价格:{OO0O0000OO00O00OO}')#line:387
                            O00O00OO00OO00O00 =O0OO00OOO00O00O00 .the_query ()#line:389
                            if float (O00O00OO00OO00O00 )!=float (OO0O0000OO00O00OO ):#line:390
                                OO0000O00OOO0O0O0 =O0O0O0OO00O0OOOO0 ['id']#line:391
                                O0OO00OOO00O00O00 .cacel_sale (OO0000O00OOO0O0O0 )#line:392
                    O0OO00OOO00O00O00 .game_map ()#line:394
        except Exception as OOO000O0O000000O0 :#line:396
            print (OOO000O0O000000O0 )#line:397
    def cacel_sale (O0OOO000OOOOO0O0O ,OOOOOO0OOOOO0OO0O ):#line:400
        try :#line:401
            O0OO0O00O0OO0O0O0 =f'_saleId={OOOOOO0OOOOO0OO0O}_{timi_new()}'#line:402
            O000O00OO000O0OOO ={'source':'scsc','authorization':O0OOO000OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0OO0O0O0 ),'signstring':O0OO0O00O0OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            O000000O000OO000O ={"saleId":OOOOOO0OOOOO0OO0O }#line:414
            OO0000OO0O0O00000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O000O00OO000O0OOO ,data =O000000O000OO000O ).json ()#line:415
            if 'status'in OO0000OO0O0O00000 :#line:417
                if OO0000OO0O0O00000 ['status']==200 :#line:418
                    print (f'【下架出售】:{OO0000OO0O0O00000["data"]}')#line:419
        except Exception as O0OO00000OO000OO0 :#line:420
            print (O0OO00000OO000OO0 )#line:421
    def change_nickname (OOO0OOO00000O0OOO ):#line:424
        try :#line:425
            O0O0OO0O0OOO00O00 =timi_new ()#line:426
            OO0O00000O0O0O000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOOO0000O0OO0000O =requests .request ('post','https://www.qmsjmfb.com/',data =OO0O00000O0O0O000 ).text #line:428
            O0O0OOOO00OOOOO0O =re .findall ('<ul><li>(.*?)</li>',OOOO0000O0OO0000O )[0 ][:3 ]#line:429
            O00O0O0OOOOO0O0O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0OOOO00OOOOO0O}').json ()#line:430
            O000000OO00OO0O0O =O00O0O0OOOOO0O0O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:431
            O0O00OO00OOOO0O0O ={"nickname":O000000OO00OO0O0O }#line:432
            OOOO0O0O00OOOO0O0 =f'_nickname={O000000OO00OO0O0O}_{O0O0OO0O0OOO00O00}'#line:433
            O000O00OO0OO0O000 ={'source':'scsc','authorization':OOO0OOO00000O0OOO .token ,'timestamp':O0O0OO0O0OOO00O00 ,'sign':sign (OOOO0O0O00OOOO0O0 ),'signstring':OOOO0O0O00OOOO0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O00OOOO000OOO0OOO =requests .request ('patch',f'{host}/user/nickname',headers =O000O00OO0OO0O000 ,data =O0O00OO00OOOO0O0O ).json ()#line:445
            if 'status'in O00OOOO000OOO0OOO :#line:447
                if O00OOOO000OOO0OOO ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O000000OO00OO0O0O}丨{O00OOOO000OOO0OOO["message"]}')#line:449
        except Exception as O000O0O0O0OOOO0OO :#line:450
            print (O000O0O0O0OOOO0OO )#line:451
    def withdraw (OO00OO0O0O00OOO00 ):#line:454
        try :#line:455
            O0O00000O0O0OOOOO =f'__{timi_new()}'#line:456
            OO0000O000O0OO0OO ={'source':'scsc','authorization':OO00OO0O0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O0O0OOOOO ),'signstring':O0O00000O0O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OO0O0OOO0O0O0OO00 =requests .request ('get',f'{host}/assets',headers =OO0000O000O0OO0OO ).json ()#line:468
            if 'status'in OO0O0OOO0O0O0OO00 :#line:470
                if OO0O0OOO0O0O0OO00 ['status']==200 :#line:471
                    O0O0O00O000OOOO0O =OO0O0OOO0O0O0OO00 ['data']['cash']#line:472
                    if float (O0O0O00O000OOOO0O )>20 :#line:473
                        O0O00000O0O0OOOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        OO0000O000O0OO0OO ={'authorization':OO00OO0O0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O0O0OOOOO ),'signstring':O0O00000O0O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OOOOOOOO000000000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        O0O0000OOO0OOOOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0000O000O0OO0OO ,data =OOOOOOOO000000000 ).json ()#line:487
                        if 'status'in O0O0000OOO0OOOOOO :#line:489
                            if O0O0000OOO0OOOOOO ['status']==200 :#line:490
                                print (f'【余额提现】:{O0O0000OOO0OOOOOO["data"]}')#line:491
                        if 'status'in O0O0000OOO0OOOOOO :#line:492
                            if O0O0000OOO0OOOOOO ['status']==500 :#line:493
                                print (f'【余额提现】:{O0O0000OOO0OOOOOO["message"]}')#line:494
        except Exception as OO000OO0OO0OOO000 :#line:495
            print (OO000OO0OO0OOO000 )#line:496
    def invitenum (O0O0OO00OO0O0O00O ):#line:499
        global invited_new #line:500
        try :#line:501
            O0O0OOOO0000OOOOO =f'__{timi_new()}'#line:502
            O0OOOOOOO00O00O00 ={'source':'scsc','authorization':O0O0OO00OO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0000OOOOO ),'signstring':O0O0OOOO0000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O0O0000O0O00O0O00 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOOOOOO00O00O00 ).json ()#line:514
            if 'status'in O0O0000O0O00O0O00 :#line:516
                if O0O0000O0O00O0O00 ['status']==200 :#line:517
                    OO000O00OO0O0OOO0 =O0O0000O0O00O0O00 ['data']['invited_count']#line:518
                    OOOOO0OO00OOOO0O0 =O0O0000O0O00O0O00 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OO000O00OO0O0OOO0}丨间邀好友:{OOOOO0OO00OOOO0O0}')#line:520
                    if OO000O00OO0O0OOO0 <2 :#line:521
                        OOOOO00O0000OOO0O =f'__{timi_new()}'#line:522
                        OO0O00O000OOO0OOO ={'source':'scsc','authorization':O0O0OO00OO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0000OOO0O ),'signstring':OOOOO00O0000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O0OO00OO0000OOOO0 =requests .request ('get',f'{host}/user',headers =OO0O00O000OOO0OOO ).json ()#line:534
                        if 'status'in O0OO00OO0000OOOO0 :#line:536
                            if O0OO00OO0000OOOO0 ['status']==200 :#line:537
                                invited_new .append (O0OO00OO0000OOOO0 ['data']['inner_id'])#line:538
        except Exception as OO00OOO00000OOO00 :#line:539
            print (OO00OOO00000OOO00 )#line:540
    def game_map (O00O0O0O0O0OO00OO ):#line:543
        global count_list #line:544
        try :#line:545
            O0OO0OO00OO0O0OOO =f'__{timi_new()}'#line:546
            OO00O00O0O0O0OO0O ={'source':'scsc','authorization':O00O0O0O0O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00OO0O0OOO ),'signstring':O0OO0OO00OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
            O0OOOOOOOOOOOO0O0 =requests .request ('get',f'{host}/game/map',headers =OO00O00O0O0O0OO0O ).json ()#line:558
            if 'status'in O0OOOOOOOOOOOO0O0 :#line:560
                if O0OOOOOOOOOOOO0O0 ['status']==200 :#line:561
                    for OO0000OO0O0O0O000 in O0OOOOOOOOOOOO0O0 ['data']['list'][0 ]['crops']:#line:562
                        O0OOOOOOO0OOO0000 =OO0000OO0O0O0O000 ['level']#line:564
                        if O0OOOOOOO0OOO0000 ==41 :#line:565
                            O000O0000OOO0O000 =OO0000OO0O0O0O000 ['crop_name']#line:566
                            OOOOO0OO0000OO0O0 =OO0000OO0O0O0O000 ['count']#line:567
                            if OOOOO0OO0000OO0O0 >0 :#line:568
                                print (f'【农业资产】:{O000O0000OOO0O000}丨数量:{OOOOO0OO0000OO0O0}')#line:569
                                count_list +=OOOOO0OO0000OO0O0 #line:570
                                O00OO00OO0OOOO0OO =O00O0O0O0O0OO00OO .the_query ()#line:571
                                O00O0O0O0O0OO00OO .market_sale (O00OO00OO0OOOO0OO )#line:572
        except Exception as O00OOOOOOO00O0OOO :#line:573
            print (O00OOOOOOO00O0OOO )#line:574
    def give_gold (O0O0O0O0OO00OO00O ):#line:577
        try :#line:578
            O0OOO0O000000O00O =f'__{timi_new()}'#line:579
            O0OO000O0OO0O0O0O ={'source':'scsc','authorization':O0O0O0O0OO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O000000O00O ),'signstring':O0OOO0O000000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            OO0000OOO0O000OOO =requests .request ('get',f'{host}/user',headers =O0OO000O0OO0O0O0O ).json ()#line:591
            if 'status'in OO0000OOO0O000OOO :#line:592
                if OO0000OOO0O000OOO ['status']==200 :#line:593
                    if float (O0O0O0O0OO00OO00O .doneeNo )!=0 :#line:594
                        OOOOOO0OOO0O0O000 =OO0000OOO0O000OOO ['data']['assets']['gold']#line:595
                        if float (OOOOOO0OOO0O0O000 )>float (O0O0O0O0OO00OO00O .innerId ):#line:596
                            O00O00O000OO000OO =int (float (OOOOOO0OOO0O0O000 )/1.1 )#line:597
                            O0OOO0O000000O00O =f'_doneeNo={O0O0O0O0OO00OO00O.doneeNo}&quantity={O00O00O000OO000OO}_{timi_new()}'#line:598
                            O0OO000O0OO0O0O0O ={'source':'scsc','authorization':O0O0O0O0OO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O000000O00O ),'signstring':O0OOO0O000000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            OOO0OO0O0O000000O ={"quantity":O00O00O000OO000OO ,"doneeNo":O0O0O0O0OO00OO00O .doneeNo }#line:613
                            O00000OO0OO00O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO000O0OO0O0O0O ,data =OOO0OO0O0O000000O ).json ()#line:614
                            if 'status'in O00000OO0OO00O0O0 :#line:616
                                if O00000OO0OO00O0O0 ['status']==200 :#line:617
                                    if O00000OO0OO00O0O0 ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O00O00O000OO000OO}种子给{O0O0O0O0OO00OO00O.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as O0OOOOO0O0000O00O :#line:622
            print (O0OOOOO0O0000O00O )#line:623
    def invitation (OOO0O0OO00O0OOOOO ):#line:625
        try :#line:626
            _O0O0O0OOOO0O0O0O0 =float (bundled_def ())/4 #line:627
            O0OOOO0OOO0000OO0 =f'_innerId={int(_O0O0O0OOOO0O0O0O0)}_{timi_new()}'#line:629
            O00OO00OOO00O0O00 ={'source':'scsc','authorization':OOO0O0OO00O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOO0000OO0 ),'signstring':O0OOOO0OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            O00OOO00OOO0O0O00 ={"innerId":int (_O0O0O0OOOO0O0O0O0 )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00OO00OOO00O0O00 ,data =O00OOO00OOO0O0O00 )#line:642
        except Exception as OOO0OO0O0000OO0OO :#line:643
            print (OOO0OO0O0000OO0OO )#line:644
    def winning_rewards (OO00OO0OOO0O000OO ):#line:647
        try :#line:648
            O000O00OO0OOOO0O0 =f'__{timi_new()}'#line:649
            O00OO0000OO00O0O0 ={'source':'scsc','authorization':OO00OO0OOO0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OO0OOOO0O0 ),'signstring':O000O00OO0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            OOO0OO000O0O0OOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0000OO00O0O0 ).json ()#line:661
            if 'status'in OOO0OO000O0O0OOOO :#line:663
                if OOO0OO000O0O0OOOO ['status']==200 :#line:664
                    if OOO0OO000O0O0OOOO ['data']['amount']:#line:665
                        OO00OO0O00O0OO0O0 =OOO0OO000O0O0OOOO ['data']['amount']['gold']#line:666
                        return OO00OO0O00O0OO0O0 #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as OOO000O0OO000O0OO :#line:670
            print (OOO000O0OO000O0OO )#line:671
    def certification (OO00O00O0OOOOO0OO ):#line:674
        try :#line:675
            O0O0OO0OO000O0O00 =f'__{timi_new()}'#line:676
            O000OOO00O00O0O0O ={'source':'scsc','authorization':OO00O00O0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO000O0O00 ),'signstring':O0O0OO0OO000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O0OO0O0O00OOO00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000OOO00O00O0O0O ).json ()#line:688
            if 'status'in O0OO0O0O00OOO00O0 :#line:690
                if O0OO0O0O00OOO00O0 ['status']==200 :#line:691
                    if O0OO0O0O00OOO00O0 ['data']['result']:#line:692
                        O0O0OOOO00OOO0O00 =O0OO0O0O00OOO00O0 ['data']['nick_name']#line:693
                        return O0O0OOOO00OOO0O00 #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as OO0OOOO000OOOO0O0 :#line:697
            print (OO0OOOO000OOOO0O0 )#line:698
    def crops_illustrated (O00OOO0O0O00OO0OO ):#line:701
        try :#line:702
            OOOOOO00OOOOOO00O =f'__{timi_new()}'#line:703
            O0O0O0OOOO000O0OO ={'source':'scsc','authorization':O00OOO0O0O00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOOOO00O ),'signstring':OOOOOO00OOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            OO00OOO0O0O0000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O0OOOO000O0OO ).json ()#line:715
            if 'status'in OO00OOO0O0O0000O0 :#line:717
                if OO00OOO0O0O0000O0 ['status']==200 :#line:718
                    OO0OO0OOOOO0OOO00 =OO00OOO0O0O0000O0 ['data'][0 ]['crops']#line:719
                    for O00O0O0O0000OO00O in OO0OO0OOOOO0OOO00 :#line:720
                        if O00O0O0O0000OO00O ['ill_clover_award']:#line:721
                            if float (O00O0O0O0000OO00O ['ill_clover_award'])>1 :#line:722
                                if O00O0O0O0000OO00O ['is_finish']:#line:723
                                    if not O00O0O0O0000OO00O ['is_getit']:#line:724
                                        if O00OOO0O0O00OO0OO .certification ()!='未实名':#line:725
                                            OOOOOO00OOOOOO00O =f'_award_level={O00O0O0O0000OO00O["level"]}_{timi_new()}'#line:726
                                            O0O0O0OOOO000O0OO ={'source':'scsc','authorization':O00OOO0O0O00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOOOOO00O ),'signstring':OOOOOO00OOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            O0OO0O0OO00O0O000 ={"award_level":O00O0O0O0000OO00O ['level']}#line:738
                                            O00OO0O0000OO0OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O0OOOO000O0OO ,json =O0OO0O0OO00O0O000 ).json ()#line:740
                                            if 'status'in O00OO0O0000OO0OOO :#line:741
                                                if O00OO0O0000OO0OOO ['status']==200 :#line:742
                                                    OOO000O000000O0OO =O00OO0O0000OO0OOO ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{O00O0O0O0000OO00O["crop_name"]}成就丨奖励{OOO000O000000O0OO}☘️')#line:745
                                                if O00OO0O0000OO0OOO ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{O00OO0O0000OO0OOO["message"]}')#line:747
        except Exception as OOO0OO0OOOO0O0000 :#line:748
            print (OOO0OO0OOOO0O0000 )#line:749
    def watched_ad (OO00O0O00OOO0OO0O ):#line:752
        try :#line:753
            OOO0OO0OO00O0O00O =f'__{timi_new()}'#line:754
            OOO0OO0O000O0OOOO ={'source':'scsc','authorization':OO00O0O00OOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O0O00O ),'signstring':OOO0OO0OO00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            OOO00O0OOO0O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0O000O0OOOO ).json ()#line:766
            if 'status'in OOO00O0OOO0O0OOOO :#line:768
                if OOO00O0OOO0O0OOOO ['status']==200 :#line:769
                    if 'offlineInfo'in OOO00O0OOO0O0OOOO ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        OO0OOOOO00O0OOOOO =OOO00O0OOO0O0OOOO ['data']['offlineInfo']['off_minute']#line:772
                        O00OOO0O0O0O0OO0O =float (OOO00O0OOO0O0OOOO ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO0OO0O000O0OOOO ).json ()#line:775
                        time .sleep (2 )#line:776
                        OOO0OO00O0O0000OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO0O000O0OOOO ).json ()#line:777
                        if 'status'in OOO0OO00O0O0000OO :#line:779
                            if OOO0OO00O0O0000OO ['status']==200 :#line:780
                                OOOOOOOO000OOO0O0 =float (OOO0OO00O0O0000OO ['data']['silver'])/1000000000000 #line:781
                                OOOOO0000OOOO00O0 =str (OOOOOOOO000OOO0O0 -O00OOO0O0O0O0OO0O )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{OO0OOOOO00O0OOOOO}分钟奖励🌱数量:{OOOOO0000OOOO00O0}t粒')#line:783
        except Exception as OOOOOO0O000000000 :#line:784
            print (OOOOOO0O000000000 )#line:785
    def user_ad (O00000OO00000O0OO ):#line:788
        try :#line:789
            OO00000OO000OO0OO =f'__{timi_new()}'#line:790
            OO0OO000O000OO00O ={'source':'scsc','authorization':O00000OO00000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO000OO0OO ),'signstring':OO00000OO000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            OO00OO0O0000OOO0O =requests .request ('get',f'{host}/user/ad',headers =OO0OO000O000OO00O ).json ()#line:802
            if 'status'in OO00OO0O0000OOO0O :#line:804
                if OO00OO0O0000OOO0O ['status']==200 :#line:805
                    O000OOOOO0O0OOOO0 =OO00OO0O0000OOO0O ['data']['max_time']#line:806
                    O000O00OOO00OO0OO =OO00OO0O0000OOO0O ['data']['watch_time']#line:807
                    O0OO00OOO0OOOO00O =OO00OO0O0000OOO0O ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{O0OO00OOO0OOOO00O + O000OOOOO0O0OOOO0 - O000O00OOO00OO0OO}次丨好友提供:{O0OO00OOO0OOOO00O}次')#line:809
                    if O0OO00OOO0OOOO00O +O000OOOOO0O0OOOO0 -O000O00OOO00OO0OO >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        OO00O0000OOOOOO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0OO000O000OO00O ).json ()#line:812
                        if 'status'in OO00O0000OOOOOO00 :#line:814
                            if OO00O0000OOOOOO00 ['status']==200 :#line:815
                                O0O0O0OOOOOOO00OO =float (OO00O0000OOOOOO00 ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(O0O0O0OOOOOOO00OO)}t粒')#line:817
                                return True #line:818
                            if OO00O0000OOOOOO00 ['status']==500 :#line:819
                                OO0O00OO0OOO0000O =OO00O0000OOOOOO00 ['message']#line:820
                                print (f'【获取种子】:{OO0O00OO0OOO0000O}')#line:821
                                return False #line:822
        except Exception as OOOO0O00O00O0OO00 :#line:823
            print (OOOO0O00O00O0OO00 )#line:824
    def synthetic (O00O000OOOO0O0O00 ):#line:827
        global id ,g #line:828
        try :#line:829
            OO000000000OOOO00 =O00O000OOOO0O0O00 .level_new ()#line:830
            O00000O0OOO0OO000 =random .randint (9 ,11 )#line:831
            OO0000O00O0O0O0OO =f'_site=8&targetSite={O00000O0OOO0OO000}_{timi_new()}'#line:832
            O00OO0O0000O00OO0 ={'source':'scsc','authorization':O00O000OOOO0O0O00 .token ,'timestamp':timi_new (),'sign':sign (OO0000O00O0O0O0OO ),'signstring':OO0000O00O0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            OOOO0O00O0OO0O0OO ={"site":int (8 ),"targetSite":int (O00000O0OOO0OO000 )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O0000O00OO0 ,json =OOOO0O00O0OO0O0OO )#line:845
            while True :#line:846
                OO0O00O0000O0OOO0 =f'__{timi_new()}'#line:847
                O0OOOO0000O00OOO0 ={'source':'scsc','authorization':O00O000OOOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0000O0OOO0 ),'signstring':OO0O00O0000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                O0O0O0000OO00OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO0000O00OOO0 ).json ()#line:859
                if 'status'in O0O0O0000OO00OO0O :#line:861
                    if O0O0O0000OO00OO0O ['status']==200 :#line:862
                        OO00OO0O0OO00OOOO =O0O0O0000OO00OO0O ['data']['cropList']#line:863
                        O0O0OO0OOO000O00O =O0O0O0000OO00OO0O ['data']['gameCoreDataDBid']#line:864
                        OO0O000OOO0O0OOO0 =float (O0O0O0000OO00OO0O ['data']['silver'])/1000000000000 #line:865
                        OO000OOOOOOOO0O00 =0 #line:870
                        for O00OO0O0OOO0O0OOO in OO00OO0O0OO00OOOO :#line:871
                            if not O00OO0O0OOO0O0OOO :#line:872
                                O000OO0000O000O0O =f'_crop_id={O0O0OO0OOO000O00O}&site={OO000OOOOOOOO0O00}_{O00O000OOOO0O0O00.time}'#line:873
                                O00O00O00O00OO0OO ={'source':'scsc','authorization':O00O000OOOO0O0O00 .token ,'timestamp':O00O000OOOO0O0O00 .time ,'sign':sign (O000OO0000O000O0O ),'signstring':O000OO0000O000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                O0O0O00000OOO00OO ={"site":OO000OOOOOOOO0O00 ,"crop_id":O0O0OO0OOO000O00O }#line:884
                                O0OO0O0OOO0O0OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O00O00O00O00OO0OO ,data =O0O0O00000OOO00OO ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in O0OO0O0OOO0O0OOO0 :#line:888
                                    if O0OO0O0OOO0O0OOO0 ['status']==200 :#line:889
                                        if O0OO0O0OOO0O0OOO0 ['message']=='种子数量不足':#line:890
                                            OO000000000OOOO00 =O00O000OOOO0O0O00 .level_new ()#line:891
                                            print (f'【种植合成】:{O0OO0O0OOO0O0OOO0["message"]}')#line:892
                                            if not O00O000OOOO0O0O00 .user_ad ():#line:893
                                                return False #line:894
                                    if O0OO0O0OOO0O0OOO0 ['status']==500 :#line:895
                                        print (f'【种植合成】:{O0OO0O0OOO0O0OOO0["message"]}')#line:896
                                        return False #line:897
                            OO000OOOOOOOO0O00 +=1 #line:898
                        O0000000OOO0OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO0000O00OOO0 ).json ()#line:899
                        OO00OOO0O00000000 =O0000000OOO0OOOOO ['data']['cropList']#line:900
                        OOOO0OO00O0OOOOO0 =False #line:901
                        for O00OO0O0OOO0O0OOO in range (12 ):#line:902
                            id =OO00OOO0O00000000 [O00OO0O0OOO0O0OOO ]['level']#line:903
                            if float (OO000000000OOOO00 )-float (id )>9 :#line:904
                                O0O0OO0000OO0O0O0 =f'_site={O00OO0O0OOO0O0OOO}_{timi_new()}'#line:905
                                OOO0OO00OOOOO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000OOOO0O0O00 .token ,'timestamp':timi_new (),'sign':sign (O0O0OO0000OO0O0O0 ),'signstring':O0O0OO0000OO0O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                O00OO0O000O0000OO ={"site":O00OO0O0OOO0O0OOO }#line:917
                                O00O000O00O00OO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0OO00OOOOO0OOO ,data =O00OO0O000O0000OO ).json ()#line:919
                                if 'status'in O00O000O00O00OO0O :#line:920
                                    if O00O000O00O00OO0O ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for OOOO00OO0O000OO00 in range (11 ):#line:924
                                    O0OOO0O0O0OOOOOO0 =OOOO00OO0O000OO00 +1 #line:925
                                    g =OO00OOO0O00000000 [O0OOO0O0O0OOOOOO0 ]['level']#line:926
                                    if id ==g :#line:927
                                        O0O0O0OO000OOO0OO =OOOO00OO0O000OO00 +2 #line:928
                                        if O0O0O0OO000OOO0OO !=O00OO0O0OOO0O0OOO +1 :#line:929
                                            O000O00O00000OO00 =O00OO0O0OOO0O0OOO +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            OO0000O00O0O0O0OO =f'_site={O000O00O00000OO00 - 1}&targetSite={O0O0O0OO000OOO0OO - 1}_{timi_new()}'#line:933
                                            O00OO0O0000O00OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O000OOOO0O0O00 .token ,'timestamp':timi_new (),'sign':sign (OO0000O00O0O0O0OO ),'signstring':OO0000O00O0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            O0OOOOOOO000OOOOO ={"site":int (O000O00O00000OO00 -1 ),"targetSite":int (O0O0O0OO000OOO0OO -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O0000O00OO0 ,json =O0OOOOOOO000OOOOO )#line:952
                                            OOOO0OO00O0OOOOO0 =True #line:954
                                    if OOOO0OO00O0OOOOO0 :#line:955
                                        break #line:956
                                if OOOO0OO00O0OOOOO0 :#line:957
                                    break #line:958
        except :#line:959
            O00O000OOOO0O0O00 .synthetic ()#line:960
    def level_new (OO000OOOO0O0OOOO0 ):#line:963
        try :#line:964
            OOOOO000OOOOOO0O0 =f'__{timi_new()}'#line:965
            OOOO0O0OOO0000O00 ={'source':'scsc','authorization':OO000OOOO0O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000OOOOOO0O0 ),'signstring':OOOOO000OOOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            OOOOOOO0O0O0O0000 =requests .request ('get',f'{host}/user',headers =OOOO0O0OOO0000O00 ).json ()#line:977
            if 'status'in OOOOOOO0O0O0O0000 :#line:978
                if OOOOOOO0O0O0O0000 ['status']==200 :#line:979
                    return float (OOOOOOO0O0O0O0000 ['data']['level'])#line:980
        except Exception as O0OO000OO0OO00O0O :#line:981
            print (O0OO000OO0OO00O0O )#line:982
    def propsraffle (OOO00O0OOOOO0000O ):#line:985
        try :#line:986
            while True :#line:987
                O000OO00O0OOO0O0O =f'__{timi_new()}'#line:988
                OO00O00OO000OO000 ={'source':'scsc','authorization':OOO00O0OOOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O0OOO0O0O ),'signstring':O000OO00O0OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                OOO000OO00O000000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O00OO000OO000 ).json ()#line:1000
                if 'status'in OOO000OO00O000000 :#line:1002
                    if OOO000OO00O000000 ['status']==200 :#line:1003
                        OO00O0O0000O00O00 =OOO000OO00O000000 ['data']['rows']#line:1004
                        O00000OOO00O0O0OO =OOO000OO00O000000 ['data']['vstate']#line:1005
                        if OO00O0O0000O00O00 ==5 or OO00O0O0000O00O00 ==6 or OO00O0O0000O00O00 ==7 :#line:1006
                            OO0OOOO00000O00O0 =OOO000OO00O000000 ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{OO0OOOO00000O00O0}')#line:1008
                        if OO00O0O0000O00O00 ==1 or OO00O0O0000O00O00 ==2 or OO00O0O0000O00O00 ==3 :#line:1009
                            O00000OOOO0000000 =OOO000OO00O000000 ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{O00000OOOO0000000}')#line:1011
                        if OO00O0O0000O00O00 ==4 or OO00O0O0000O00O00 ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if OO00O0O0000O00O00 =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as O00O0OOO00OO00OO0 :#line:1053
            print (O00O0OOO00OO00OO0 )#line:1054
    def friends_invitation (OO00O0O0OO0OOO00O ):#line:1057
        try :#line:1058
            O00O000O0O0OO0O0O =f'__{timi_new()}'#line:1059
            OOOO00OO0000O00OO ={'source':'scsc','authorization':OO00O0O0OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O0O0OO0O0O ),'signstring':O00O000O0O0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            O00O0OOOOO0OO0OOO =requests .request ('get',f'{host}/friends',headers =OOOO00OO0000O00OO ).json ()#line:1071
            if 'status'in O00O0OOOOO0OO0OOO :#line:1072
                if O00O0OOOOO0OO0OOO ['status']==200 :#line:1073
                    OOO0OO000O0000OO0 =O00O0OOOOO0OO0OOO ['data']['myInviteter']#line:1074
                    if OOO0OO000O0000OO0 :#line:1075
                        O0000OO000OOO00O0 =OOO0OO000O0000OO0 ['user']['nickname']#line:1076
                        OO00O0000O00OOO0O =OO00O0O0OO0OOO00O .certification ()#line:1077
                        if OO00O0000O00OOO0O =='未实名':#line:1078
                            weishim .append (OO00O0O0OO0OOO00O .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{O0000OO000OOO00O0}丨实名:{OO00O0000O00OOO0O}')#line:1080
                    else :#line:1081
                        if OO00O0O0OO0OOO00O .innerId !='0':#line:1082
                            OO00O0O0OO0OOO00O .invitation ()#line:1083
        except Exception as OOO00000OO0O0OO00 :#line:1084
            print (OOO00000OO0O0OO00 )#line:1085
    def add_clover (O0OOOO00O0OOOO000 ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            OO000O00O00000OOO =f'__{timi_new()}'#line:1091
            OO0O00000000000O0 ={'source':'scsc','authorization':O0OOOO00O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00000OOO ),'signstring':OO000O00O00000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O000000O0OO0OO000 =requests .request ('get',f'{host}/assets/clovers',headers =OO0O00000000000O0 ).json ()#line:1103
            if 'status'in O000000O0OO0OO000 :#line:1105
                if O000000O0OO0OO000 ['status']==200 :#line:1106
                    OOO00OOO0O00OOOO0 =O000000O0OO0OO000 ['data']['clover']#line:1107
                    OO0OOO0O0O0OO0O0O =O000000O0OO0OO000 ['data']['used_clover']#line:1108
                    OO0OO0O0OO00OOOO0 =float (OOO00OOO0O00OOOO0 )-float (OO0OOO0O0O0OO0O0O )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OOO0O0O0OO0O0O}')#line:1110
                    if O0OOOO00O0OOOO000 .certification ()!='未实名':#line:1111
                        if OO0OO0O0OO00OOOO0 >1 :#line:1112
                            OO000O00O00000OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO0O0OO00OOOO0)}_{timi_new()}'#line:1113
                            O0O000OO0000O00OO ={'source':'scsc','authorization':O0OOOO00O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O00000OOO ),'signstring':OO000O00O00000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            OOOO0O0OO000OO0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO0O0OO00OOOO0 )}#line:1125
                            OO0OO00OO0O00O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O000OO0000O00OO ,data =OOOO0O0OO000OO0O0 ).json ()#line:1126
                            if 'status'in OO0OO00OO0O00O000 :#line:1128
                                if OO0OO00OO0O00O000 ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{OO0OO00OO0O00O000["data"]["isSuccess"]}丨数量:{OO0OO0O0OO00OOOO0}')#line:1130
                                if OO0OO00OO0O00O000 ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{OO0OO00OO0O00O000["message"]}')#line:1132
            OO0OOOOO0OO0OO00O =requests .request ('get',f'{host}/lottery',headers =OO0O00000000000O0 ).json ()#line:1133
            OOOO000OO0OO00OOO =O0OOOO00O0OOOO000 .winning_rewards ()#line:1135
            if 'status'in OO0OOOOO0OO0OO00O :#line:1136
                if OO0OOOOO0OO0OO00O ['status']==200 :#line:1137
                    O00OOOO00O0O00O0O =OO0OOOOO0OO0OO00O ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (O00OOOO00O0O00O0O )#line:1139
                    OO0000OO000O0OOO0 =OO0OOOOO0OO0OO00O ['data'][1 ]['value']#line:1140
                    O0OOO00OO0OO000OO =OO0OOOOO0OO0OO00O ['data'][0 ]['join_number']#line:1141
                    OO0O0O000OO00OOOO =int (float (OO0OOOOO0OO0OO00O ['data'][0 ]['totalValue']))#line:1142
                    OOOOOO0OOOO0OOOO0 =float (OO0000OO000O0OOO0 /OO0O0O000OO00OOOO )*10000 #line:1143
                    O0O00O00OO0OOOO00 =OO0O0O000OO00OOOO /O0OOO00OO0OO000OO #line:1144
                    print (f'【参与抽奖】:预计每天中{str(O00OOOO00O0O00O0O)[:6]}颗金种子丨好友收益:{str(OOOO000OO0OO00OOO)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOOO0OOOO0OOOO0)[:6]}颗金种子丨☘️人均:{str(O0O00O00OO0OOOO00)[:7]}️')#line:1146
        except Exception as OOOOOOO0OOOOOOO00 :#line:1147
            print (OOOOOOO0OOOOOOO00 )#line:1148
    def energy (OOOO0O0OOO0OO000O ):#line:1151
        try :#line:1152
            while True :#line:1153
                OOOOOO000OOO0O0OO =f'__{timi_new()}'#line:1154
                O0OO0OO0O0OOOO0O0 ={'source':'scsc','authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000OOO0O0OO ),'signstring':OOOOOO000OOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                O000OOOO000O00O00 =requests .request ('get',f'{host}/energy/general',headers =O0OO0OO0O0OOOO0O0 ).json ()#line:1166
                if 'status'in O000OOOO000O00O00 :#line:1168
                    if O000OOOO000O00O00 ['status']==200 :#line:1169
                        OO0000O00OO000000 =O000OOOO000O00O00 ['data']['ordinary_water']#line:1170
                        O0O00O000OOOO0O0O =O000OOOO000O00O00 ['data']['ordinary_fertilizer']#line:1171
                        OOOOOO0OO0O00000O =O000OOOO000O00O00 ['data']['videoStatus']#line:1172
                        OO000000O00O00O00 =O000OOOO000O00O00 ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(O0O00O000OOOO0O0O).split(".")[0]}丨水滴:{str(OO0000O00OO000000).split(".")[0]}')#line:1175
                        if float (O0O00O000OOOO0O0O )<96 :#line:1176
                            if OOOOOO0OO0O00000O :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                O0O00OO0OOO0OOO00 =99 -float (O0O00O000OOOO0O0O )#line:1179
                                O0OOOO00OOOOOOO00 ={"fertilizer":str (O0O00OO0OOO0OOO00 ).split ('.')[0 ]}#line:1180
                                O0O00O0OOOO000O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0OO0O0OOOO0O0 ).json ()#line:1182
                                if 'status'in O0O00O0OOOO000O0O :#line:1184
                                    if O0O00O0OOOO000O0O ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00O0OOOO000O0O["message"]}')#line:1186
                                    if O0O00O0OOOO000O0O ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00O0OOOO000O0O["message"]}')#line:1188
                                        break #line:1189
                                if float (O0O00O000OOOO0O0O )<78 :#line:1191
                                    O0O00OO0OOO0OOO00 =80 -float (O0O00O000OOOO0O0O )#line:1192
                                    OOOO0000OOOOOO0OO =f'_fertilizer={int(O0O00OO0OOO0OOO00)}_{timi_new()}'#line:1193
                                    O0OOO0000O00OO00O ={'source':'scsc','authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OOOOOO0OO ),'signstring':OOOO0000OOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    OO0OO0O0OOOOOO00O ={"fertilizer":int (O0O00OO0OOO0OOO00 )}#line:1205
                                    O0O0OOO0OO0OOO00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOO0000O00OO00O ,data =OO0OO0O0OOOOOO00O ).json ()#line:1207
                                    if 'status'in O0O0OOO0OO0OOO00O :#line:1209
                                        if O0O0OOO0OO0OOO00O ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{O0O0OOO0OO0OOO00O["message"]}丨数量:{int(O0O00OO0OOO0OOO00)}')#line:1211
                                        if O0O0OOO0OO0OOO00O ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{O0O0OOO0OO0OOO00O["message"]}丨数量:{int(O0O00OO0OOO0OOO00)}')#line:1213
                                            OO000OOOOOOO0O0OO =O0O0OOO0OO0OOO00O ["message"].split ('-')[1 ]#line:1214
                                            O0O000OO00O000O0O =f'__{timi_new()}'#line:1215
                                            OO000000O0O00000O ={'source':'scsc','authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO00O000O0O ),'signstring':O0O000OO00O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            O0000000O0O0O0OO0 =requests .request ('get',f'{host}/user',headers =OO000000O0O00000O ).json ()#line:1227
                                            if 'status'in O0000000O0O0O0OO0 :#line:1228
                                                if O0000000O0O0O0OO0 ['status']==200 :#line:1229
                                                    OOO0000O0O0O0OOOO =O0000000O0O0O0OO0 ['data']['inner_id']#line:1230
                                                    if give_gold (OOO0000O0O0O0OOOO ,float (OO000OOOOOOO0O0OO )+1 ):#line:1231
                                                        OOOO0O0OOO0OO000O .energy ()#line:1232
                        if float (OO0000O00OO000000 )<880 :#line:1233
                            if OO000000O00O00O00 :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                OO000O0O00000OOO0 =999 -float (OO0000O00OO000000 )#line:1236
                                O0000OO0O00O0O000 ={"water":str (OO000O0O00000OOO0 ).split ('.')[0 ]}#line:1237
                                O0O0O0OO0OOO0OOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0OO0O0OOOO0O0 ).json ()#line:1239
                                if 'status'in O0O0O0OO0OOO0OOO0 :#line:1241
                                    if O0O0O0OO0OOO0OOO0 ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O0OO0OOO0OOO0["message"]}')#line:1243
                                    if O0O0O0OO0OOO0OOO0 ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O0OO0OOO0OOO0["message"]}')#line:1245
                                        break #line:1246
                                if float (OO0000O00OO000000 )<780 :#line:1247
                                    OO000O0O00000OOO0 =800 -float (OO0000O00OO000000 )#line:1248
                                    O0O0OOO00O0000O00 =f'_water={int(OO000O0O00000OOO0)}_{timi_new()}'#line:1249
                                    O000O0OO00OO0000O ={'source':'scsc','authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00O0000O00 ),'signstring':O0O0OOO00O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    OO00O000O0000O0OO ={"water":int (OO000O0O00000OOO0 )}#line:1261
                                    O0OOO0O000O000O0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000O0OO00OO0000O ,data =OO00O000O0000O0OO ).json ()#line:1263
                                    if 'status'in O0OOO0O000O000O0O :#line:1265
                                        if O0OOO0O000O000O0O ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{O0OOO0O000O000O0O["message"]}丨数量:{int(OO000O0O00000OOO0)}')#line:1267
                                        if O0OOO0O000O000O0O ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{O0OOO0O000O000O0O["message"]}丨数量:{int(OO000O0O00000OOO0)}')#line:1269
                                            OO000OOOOOOO0O0OO =O0OOO0O000O000O0O ["message"].split ('-')[1 ]#line:1270
                                            O0O000OO00O000O0O =f'__{timi_new()}'#line:1271
                                            OO000000O0O00000O ={'source':'scsc','authorization':OOOO0O0OOO0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO00O000O0O ),'signstring':O0O000OO00O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            O0000000O0O0O0OO0 =requests .request ('get',f'{host}/user',headers =OO000000O0O00000O ).json ()#line:1283
                                            if 'status'in O0000000O0O0O0OO0 :#line:1284
                                                if O0000000O0O0O0OO0 ['status']==200 :#line:1285
                                                    OOO0000O0O0O0OOOO =O0000000O0O0O0OO0 ['data']['inner_id']#line:1286
                                                    if give_gold (OOO0000O0O0O0OOOO ,float (OO000OOOOOOO0O0OO )+1 ):#line:1287
                                                        OOOO0O0OOO0OO000O .energy ()#line:1288
                        break #line:1289
        except Exception as O0O0000OO0O00OOO0 :#line:1290
            print (O0O0000OO0O00OOO0 )#line:1291
def bundled_def ():#line:1293
    OOOO000OO0O0OO000 =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return OOOO000OO0O0OO000 .split ("\n")[random .randint (0 ,len (OOOO000OO0O0OO000 .split ("\n"))-1 )]#line:1295
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
        OO00OOO0O000O00OO =gitee_edition ()#line:1334
        if version_of_the_validation ()<OO00OOO0O000O00OO ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0O000O00OO["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{OO00OOO0O000O00OO["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOO0O000O00OO["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {OO00OOO0O000O00OO["CityEarth"]["content"]}')#line:1340
    except Exception as OO0OOO00O00OO0OO0 :#line:1341
        print (OO0OOO00O00OO0OO0 )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350

