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
        OOOOO00000O00OOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOOOO00000O00OOO0)}个账号==========")#line:17
        for O00O0OOO000OO00OO in OOOOO00000O00OOO0 :#line:18
            OO0OOO0O0000O0O0O =[]#line:19
            print (f"------------正在执行第{OOOOO00000O00OOO0.index(O00O0OOO000OO00OO) + 1}个账号------------")#line:20
            OO0O00O0OOO0O0OO0 =CityEarth (O00O0OOO000OO00OO ,OO0OOO0O0000O0O0O ,OOOOO00000O00OOO0 .index (O00O0OOO000OO00OO ))#line:21
            def OOO0O00O00000OOOO ():#line:23
                if OO0O00O0OOO0O0OO0 .base_info ():#line:25
                    OO0O00O0OOO0O0OO0 .sealing ()#line:27
                    OO0O00O0OOO0O0OO0 .invitenum ()#line:29
                    OO0O00O0OOO0O0OO0 .query_to_sell ()#line:31
                    OO0O00O0OOO0O0OO0 .friends_invitation ()#line:35
                    OO0O00O0OOO0O0OO0 .energy ()#line:37
                    OO0O00O0OOO0O0OO0 .add_clover ()#line:39
                    OO0O00O0OOO0O0OO0 .propsraffle ()#line:41
                    OO0O00O0OOO0O0OO0 .synthetic ()#line:43
                    OO0O00O0OOO0O0OO0 .crops_illustrated ()#line:45
                    OO0O00O0OOO0O0OO0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0O00O0OOO0O0OO0 .give_gold ()#line:50
            OO0OOOOOO0OOO000O =threading .Thread (target =OOO0O00O00000OOOO )#line:52
            OO0OOOOOO0OOO000O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0OO0O0O00OO0O00 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OO0O0O00OO0O00 )#line:58
        time .sleep (3 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O0OOO0O0O0O00O0 in invited_new :#line:62
            print (O0O0OOO0O0O0O00O0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O00O00O0O0OOO0O00 in weishim :#line:65
            print (O00O00O0O0OOO0O00 )#line:66
    except Exception as OO0OO0OO0000O00O0 :#line:67
        print (OO0OO0OO0000O00O0 )#line:68
def appoo ():#line:70
    return f'vastzzzl/vastzzzl/{ppl()}'#line:71
def ppl ():#line:73
    return 'raw/master/superior'#line:74
def give_gold (OO000O000OO0OOOO0 ,OO000OO00OOO00O00 ):#line:78
    try :#line:79
        O0O0O0O0OO00OO0O0 =f'_doneeNo={OO000O000OO0OOOO0}&quantity={int(OO000OO00OOO00O00)}_{timi_new()}'#line:80
        OOOO00O0000O0OO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0OO00OO0O0 ),'signstring':O0O0O0O0OO00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:91
        O0000OO000OOOO0OO ={"quantity":int (OO000OO00OOO00O00 ),"doneeNo":OO000O000OO0OOOO0 }#line:95
        OOO0OO0OO0OO0OO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO00O0000O0OO00 ,data =O0000OO000OOOO0OO ).json ()#line:96
        if 'status'in OOO0OO0OO0OO0OO0O :#line:98
            if OOO0OO0OO0OO0OO0O ['status']==200 :#line:99
                if OOO0OO0OO0OO0OO0O ['data']:#line:100
                    print (f'【赠送种子】:赠送{int(OO000OO00OOO00O00)}种子给{OO000O000OO0OOOO0}成功')#line:101
                    return True #line:102
            if OOO0OO0OO0OO0OO0O ['status']==401 :#line:103
                print (f'【赠送种子】:{OOO0OO0OO0OO0OO0O["message"]}')#line:104
                return False #line:105
            if OOO0OO0OO0OO0OO0O ['status']==500 :#line:106
                print (f'【赠送种子】:{OOO0OO0OO0OO0OO0O["message"]}')#line:107
                return False #line:108
        return False #line:109
    except Exception as O0OO0O00O0OOO00O0 :#line:110
        print (O0OO0O00O0OOO00O0 )#line:111
def kvkv ():#line:114
    return '/vastzzzl/vastzzzl/raw/master'#line:115
def oyoy ():#line:117
    return '卡密未激活   ❌'#line:118
def sign (O00OOO000OO0OOOO0 ):#line:121
    O0O000O00OO000OO0 =hashlib .md5 (O00OOO000OO0OOOO0 .encode ()).hexdigest ()#line:122
    O0O00OO000O000OO0 =sc1 ()#line:123
    OO0O0OO0O0OO0O00O =sc2 ()#line:124
    O0O0000000OOOOO0O =sc3 ()#line:125
    O0OO00O0000OOO00O =O0O00OO000O000OO0 +O0O000O00OO000OO0 +OO0O0OO0O0OO0O00O +O0O0000000OOOOO0O #line:126
    OOO0O0000OOO0O0OO =hashlib .md5 (O0OO00O0000OOO00O .encode ()).hexdigest ()#line:127
    return OOO0O0000OOO0O0OO #line:128
def format_msg ():#line:131
    O000OO0000OOO0O00 =""#line:132
    for O00OO00O00OO000O0 in msg_list :#line:133
        O000OO0000OOO0O00 +=str (O00OO00O00OO000O0 )+"\r\n"#line:134
    return O000OO0000OOO0O00 #line:135
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
def get_json_data (OO00O0000O00O0OOO ,OO0O00OOOOO00OOO0 ,OO000O00000000O0O ,O0OO00O0OO0O00OOO ):#line:159
    with open (OO00O0000O00O0OOO ,'rb')as OO00OOOO00OO000O0 :#line:160
        OO0O000OO0O0O00OO =json .load (OO00OOOO00OO000O0 )#line:161
        OO0O000OO0O0O00OO ['data'][OO0O00OOOOO00OOO0 ][OO000O00000000O0O ]=O0OO00O0OO0O00OOO #line:162
        O0OOO0000OOOO0000 =OO0O000OO0O0O00OO #line:163
    OO00OOOO00OO000O0 .close ()#line:164
    return O0OOO0000OOOO0000 #line:165
def write_json_data (OO00OO00O00OO0O0O ):#line:168
    with open (json_path1 ,'w')as O00O00O00OOO0O00O :#line:169
        json .dump (OO00OO00O00OO0O0O ,O00O00O00OOO0O00O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:170
    O00O00O00OOO0O00O .close ()#line:171
    return True #line:172
class CityEarth :#line:175
    def __init__ (OO0O00O000OO0O0OO ,O00OO0O0OO0OOOO00 ,O0O0000OO000O0O0O ,O00OOOO0O0O00O000 ):#line:177
        try :#line:178
            OO0O00O000OO0O0OO .msg =O0O0000OO000O0O0O #line:179
            OO0O00O000OO0O0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:180
            OO0O00O000OO0O0OO .token =O00OO0O0OO0OOOO00 ['authorization']#line:181
            OO0O00O000OO0O0OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:182
            OO0O00O000OO0O0OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:183
            OO0O00O000OO0O0OO .elephant_user =O00OO0O0OO0OOOO00 ['elephant_user']#line:184
            OO0O00O000OO0O0OO .elephant_pswd =O00OO0O0OO0OOOO00 ['elephant_pswd']#line:185
            OO0O00O000OO0O0OO .elephant_Task_ID =O00OO0O0OO0OOOO00 ['elephant_Task_ID']#line:186
            OO0O00O000OO0O0OO .len_new =O00OOOO0O0O00O000 #line:187
        except :#line:188
            print ('变量格式错误')#line:189
    def base_info (O0OOOOOOOO00O0O00 ):#line:192
        try :#line:193
            O0OOOOOOOO00O0O00 .watched_ad ()#line:195
            O0OOO0O00O00OO0OO =f'__{timi_new()}'#line:196
            O0000O00000OO00O0 ={'source':'scsc','authorization':O0OOOOOOOO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O00OO0OO ),'signstring':O0OOO0O00O00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:207
            O0O00O0OO00000OOO =requests .request ('get',f'{host}/user',headers =O0000O00000OO00O0 ).json ()#line:208
            if 'status'in O0O00O0OO00000OOO :#line:210
                if O0O00O0OO00000OOO ['status']==200 :#line:211
                    OO0OO00OOO000OO00 =O0O00O0OO00000OOO ['data']['nickname']#line:212
                    O0O00OO000O00O0O0 =O0O00O0OO00000OOO ['data']['inner_id']#line:213
                    O0O0O00OOOOO0000O =O0O00O0OO00000OOO ['data']['assets']['gold']#line:214
                    O000O0OOO0O0O00O0 =O0O00O0OO00000OOO ['data']['level']#line:215
                    print (f'【账号信息】:昵称:{OO0OO00OOO000OO00[:5]}丨ID:{O0O00OO000O00O0O0}丨等级:{O000O0OOO0O0O00O0}丨金种子:{str(O0O0O00OOOOO0000O).split(".")[0]}')#line:217
                    if 'wx_'in OO0OO00OOO000OO00 :#line:218
                        O0OOOOOOOO00O0O00 .change_nickname ()#line:219
                if O0O00O0OO00000OOO ['status']==401 :#line:220
                    print ('【账号信息】:账号失效正在尝试登录')#line:221
                    if O0OOOOOOOO00O0O00 .elephant_user =='f':#line:222
                        return False #line:223
                    OO00OO00000OOO0O0 =Invalid_login .addtask (elephant_user =O0OOOOOOOO00O0O00 .elephant_user ,elephant_pswd =O0OOOOOOOO00O0O00 .elephant_pswd ,elephant_Task_ID =O0OOOOOOOO00O0O00 .elephant_Task_ID )#line:226
                    OOOOOOO00OO0OO00O =get_json_data (json_path ,O0OOOOOOOO00O0O00 .len_new ,'authorization',OO00OO00000OOO0O0 )#line:227
                    if write_json_data (OOOOOOO00OO0OO00O ):#line:228
                        print ('正在写入账号配置文件')#line:229
                    return False #line:230
                if O0O00O0OO00000OOO ['status']==500 :#line:231
                    return False #line:232
            return True #line:233
        except Exception as O0O00O00OOOOOOOO0 :#line:234
            print (O0O00O00OOOOOOOO0 )#line:235
    def sealing (OOOO000OO0OO0O0OO ):#line:238
        try :#line:239
            O0O0O0O00OO00OO00 =f'__{timi_new()}'#line:240
            O0O0OOO0O00OO0000 ={'source':'scsc','authorization':OOOO000OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00OO00OO00 ),'signstring':O0O0O0O00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:251
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0OOO0O00OO0000 )#line:252
            requests .request ('get',f'{host}/packsack/list',headers =O0O0OOO0O00OO0000 )#line:253
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0OOO0O00OO0000 )#line:254
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0OOO0O00OO0000 )#line:255
            requests .request ('get',f'{host}/user',headers =O0O0OOO0O00OO0000 )#line:256
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0OOO0O00OO0000 )#line:257
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0OOO0O00OO0000 )#line:258
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0OOO0O00OO0000 )#line:259
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOO0O00OO0000 )#line:260
            requests .request ('get',f'{host}/assets',headers =O0O0OOO0O00OO0000 )#line:261
        except Exception as OO0OOO000O0O0OO00 :#line:262
            print (OO0OOO000O0O0OO00 )#line:263
    def ddd (OO0000OOOO0OOO0O0 ):#line:265
        try :#line:266
            OOO0O000OO00O0OO0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:267
            O0O0O00OOOO0O0O0O ={'source':'scsc','authorization':OO0000OOOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000OO00O0OO0 ),'signstring':OOO0O000OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
            O00O0O0O0O0OOO0OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O0O00OOOO0O0O0O ).json ()#line:279
            print (O00O0O0O0O0OOO0OO )#line:280
        except Exception as O0O0O0000O00O00O0 :#line:283
            print (O0O0O0000O00O00O0 )#line:284
    def the_query (OOO0OOOOOO00000OO ):#line:289
        try :#line:290
            O00OO0O0OO00O0OO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:291
            OO0000O0OO0OOO000 ={'authorization':OOO0OOOOOO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OO00O0OO0 ),'signstring':O00OO0O0OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O00O0O0O0OO0O0O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0000O0OO0OOO000 ).json ()#line:302
            if 'status'in O00O0O0O0OO0O0O0O :#line:304
                if O00O0O0O0OO0O0O0O ['status']==200 :#line:305
                    return O00O0O0O0OO0O0O0O ['data']['rows'][4 ]['price']#line:306
        except Exception as O00O000O0O00O0OOO :#line:307
            print (O00O000O0O00O0OOO )#line:308
    def market_sale (O00OO00O0OO0OO000 ,OO000O00O0OO000OO ):#line:311
        try :#line:312
            O00OO0O0O00OO0OOO =timi_new ()#line:313
            O0OO0O0O0OOO000OO =f'type=crop__{O00OO0O0O00OO0OOO}'#line:314
            O0O0O0OOO000OOO00 ={'source':'scsc','authorization':O00OO00O0OO0OO000 .token ,'timestamp':str (O00OO0O0O00OO0OOO ),'sign':sign (O0OO0O0O0OOO000OO ),'signstring':O0OO0O0O0OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:325
            O00O00OO0O000O0OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O0OOO000OOO00 ).json ()#line:326
            if 'status'in O00O00OO0O000O0OO :#line:328
                if O00O00OO0O000O0OO ['status']==200 :#line:329
                    if O00O00OO0O000O0OO ['data']['rows']:#line:330
                        OO0O0O0OOOO00OOO0 =O00O00OO0O000O0OO ['data']['rows'][0 ]['packsackItemId']#line:331
                        OO0OOO0O0O0O000OO =O00O00OO0O000O0OO ['data']['rows'][0 ]['quantity']#line:332
                        OOOO0000O0000000O =OO000O00O0OO000OO #line:333
                        if float (OO000O00O0OO000OO )>4 :#line:334
                            OO00OO0O000OO0O00 =f'_packsackItemId={OO0O0O0OOOO00OOO0}&price={str(OOOO0000O0000000O)[:5]}&quantity={OO0OOO0O0O0O000OO}_{O00OO0O0O00OO0OOO}'#line:335
                            O0OO00O00O00OO0OO ={'source':'scsc','authorization':O00OO00O0OO0OO000 .token ,'timestamp':str (O00OO0O0O00OO0OOO ),'sign':sign (OO00OO0O000OO0O00 ),'signstring':OO00OO0O000OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            OO00OOO000O000OO0 ={"packsackItemId":OO0O0O0OOOO00OOO0 ,"price":str (OOOO0000O0000000O )[:5 ],"quantity":str (OO0OOO0O0O0O000OO )}#line:351
                            OO0000OOO000O000O =requests .request ('post',f'{host}/market/sale',headers =O0OO00O00O00OO0OO ,data =OO00OOO000O000OO0 ).json ()#line:352
                            if 'status'in OO0000OOO000O000O :#line:354
                                if OO0000OOO000O000O ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{OO0OOO0O0O0O000OO}丨价格:{str(OOOO0000O0000000O)[:5]}')#line:356
                                if OO0000OOO000O000O ['status']==500 :#line:357
                                    print (f'【上架芦荟】:{OO0000OOO000O000O["message"]}')#line:358
        except Exception as OOOO0O0OO0O0O0000 :#line:359
            print (OOOO0O0OO0O0O0000 )#line:360
    def query_to_sell (OOOO0OOO0OO0OOOO0 ):#line:363
        try :#line:364
            OOO0000OO0OO00OO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:365
            O000O0OO0000OO0O0 ={'source':'scsc','authorization':OOOO0OOO0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0OO00OO0 ),'signstring':OOO0000OO0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:376
            OO00OO000OOO00000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O000O0OO0000OO0O0 ).json ()#line:377
            if 'status'in OO00OO000OOO00000 :#line:379
                if OO00OO000OOO00000 ['status']==200 :#line:380
                    for O0OO0O00OO00O0O00 in OO00OO000OOO00000 ['data']['rows']:#line:381
                        OOOO0O0O0O00OOO0O =O0OO0O00OO00O0O00 ['materialKey']#line:382
                        O0OO0O000O0O00OOO =O0OO0O00OO00O0O00 ['quantity']#line:383
                        OOO0000000O0OO000 =O0OO0O00OO00O0O00 ['price']#line:384
                        OOOOOO0O0O0O0O0OO =O0OO0O00OO00O0O00 ['saleState']#line:385
                        if OOOOOO0O0O0O0O0OO ==0 :#line:386
                            print (f'【出售订单】:名称:{OOOO0O0O0O00OOO0O}丨数量:{O0OO0O000O0O00OOO}丨价格:{OOO0000000O0OO000}')#line:387
                            O000000OO00OOO000 =OOOO0OOO0OO0OOOO0 .the_query ()#line:389
                            if float (O000000OO00OOO000 )!=float (OOO0000000O0OO000 ):#line:390
                                O0OOO0O000OOO0000 =O0OO0O00OO00O0O00 ['id']#line:391
                                OOOO0OOO0OO0OOOO0 .cacel_sale (O0OOO0O000OOO0000 )#line:392
                    OOOO0OOO0OO0OOOO0 .game_map ()#line:394
        except Exception as OO0OO0O0OO00O0O0O :#line:396
            print (OO0OO0O0OO00O0O0O )#line:397
    def cacel_sale (O00O0OO000OOO0O0O ,OO00OO0OOO0OO0O00 ):#line:400
        try :#line:401
            O00O0OO00O0O00OOO =f'_saleId={OO00OO0OOO0OO0O00}_{timi_new()}'#line:402
            OOO00OOOOOOOOOOOO ={'source':'scsc','authorization':O00O0OO000OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O0O00OOO ),'signstring':O00O0OO00O0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            O00O0O000OO00OOO0 ={"saleId":OO00OO0OOO0OO0O00 }#line:414
            O0000O0OO0O0000OO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO00OOOOOOOOOOOO ,data =O00O0O000OO00OOO0 ).json ()#line:415
            if 'status'in O0000O0OO0O0000OO :#line:417
                if O0000O0OO0O0000OO ['status']==200 :#line:418
                    print (f'【下架出售】:{O0000O0OO0O0000OO["data"]}')#line:419
        except Exception as O0OOO0OOO00O0OO00 :#line:420
            print (O0OOO0OOO00O0OO00 )#line:421
    def change_nickname (O0OO0000000O00OOO ):#line:424
        try :#line:425
            O000OO0O000OO0OO0 =timi_new ()#line:426
            OO000O0OO00OO000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            O0O0O0OOO00OO0OO0 =requests .request ('post','https://www.qmsjmfb.com/',data =OO000O0OO00OO000O ).text #line:428
            O0O0O0O0OOO0O00OO =re .findall ('<ul><li>(.*?)</li>',O0O0O0OOO00OO0OO0 )[0 ][:3 ]#line:429
            OO0O0OOO0O000OOO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0O0O0OOO0O00OO}').json ()#line:430
            O00OOO0O00O000OO0 =OO0O0OOO0O000OOO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:431
            O0OO0OOOO000OO0O0 ={"nickname":O00OOO0O00O000OO0 }#line:432
            OO0000OO00O0000OO =f'_nickname={O00OOO0O00O000OO0}_{O000OO0O000OO0OO0}'#line:433
            OO0O0OO0OO00O0O0O ={'source':'scsc','authorization':O0OO0000000O00OOO .token ,'timestamp':O000OO0O000OO0OO0 ,'sign':sign (OO0000OO00O0000OO ),'signstring':OO0000OO00O0000OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O0000OOOO00OO00O0 =requests .request ('patch',f'{host}/user/nickname',headers =OO0O0OO0OO00O0O0O ,data =O0OO0OOOO000OO0O0 ).json ()#line:445
            if 'status'in O0000OOOO00OO00O0 :#line:447
                if O0000OOOO00OO00O0 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O00OOO0O00O000OO0}丨{O0000OOOO00OO00O0["message"]}')#line:449
        except Exception as OOOO0OOO0O0O0000O :#line:450
            print (OOOO0OOO0O0O0000O )#line:451
    def withdraw (OOOO0000OO00O0O0O ):#line:454
        try :#line:455
            OOO0000O0O0OOOOOO =f'__{timi_new()}'#line:456
            O0000O00O0OO000OO ={'source':'scsc','authorization':OOOO0000OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O0OOOOOO ),'signstring':OOO0000O0O0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OOOO0000OO00O00OO =requests .request ('get',f'{host}/assets',headers =O0000O00O0OO000OO ).json ()#line:468
            if 'status'in OOOO0000OO00O00OO :#line:470
                if OOOO0000OO00O00OO ['status']==200 :#line:471
                    O000O00OO0OOOO0OO =OOOO0000OO00O00OO ['data']['cash']#line:472
                    if float (O000O00OO0OOOO0OO )>20 :#line:473
                        OOO0000O0O0OOOOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O0000O00O0OO000OO ={'authorization':OOOO0000OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O0OOOOOO ),'signstring':OOO0000O0O0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        O00O0OOOOO00O0OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OO0OO000OOOOO00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000O00O0OO000OO ,data =O00O0OOOOO00O0OOO ).json ()#line:487
                        if 'status'in OO0OO000OOOOO00O0 :#line:489
                            if OO0OO000OOOOO00O0 ['status']==200 :#line:490
                                print (f'【余额提现】:{OO0OO000OOOOO00O0["data"]}')#line:491
                        if 'status'in OO0OO000OOOOO00O0 :#line:492
                            if OO0OO000OOOOO00O0 ['status']==500 :#line:493
                                print (f'【余额提现】:{OO0OO000OOOOO00O0["message"]}')#line:494
        except Exception as O0O0000000OOOOOOO :#line:495
            print (O0O0000000OOOOOOO )#line:496
    def invitenum (O000O0000OO0OOOO0 ):#line:499
        global invited_new #line:500
        try :#line:501
            O0OO0O000O0O0O00O =f'__{timi_new()}'#line:502
            O00O0O0O0OOO00000 ={'source':'scsc','authorization':O000O0000OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O000O0O0O00O ),'signstring':O0OO0O000O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O00O0OO0000O00000 =requests .request ('get',f'{host}/invite/invitenum',headers =O00O0O0O0OOO00000 ).json ()#line:514
            if 'status'in O00O0OO0000O00000 :#line:516
                if O00O0OO0000O00000 ['status']==200 :#line:517
                    O00O0O0OOOO0O00OO =O00O0OO0000O00000 ['data']['invited_count']#line:518
                    OOOO00OOOO0OOO0OO =O00O0OO0000O00000 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O00O0O0OOOO0O00OO}丨间邀好友:{OOOO00OOOO0OOO0OO}')#line:520
                    if O00O0O0OOOO0O00OO <2 :#line:521
                        O0000O000000O0O0O =f'__{timi_new()}'#line:522
                        O0OO00O000OOOO000 ={'source':'scsc','authorization':O000O0000OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000000O0O0O ),'signstring':O0000O000000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OO0OO0OOOOOO0OOOO =requests .request ('get',f'{host}/user',headers =O0OO00O000OOOO000 ).json ()#line:534
                        if 'status'in OO0OO0OOOOOO0OOOO :#line:536
                            if OO0OO0OOOOOO0OOOO ['status']==200 :#line:537
                                invited_new .append (OO0OO0OOOOOO0OOOO ['data']['inner_id'])#line:538
        except Exception as O0000OO0OO00000O0 :#line:539
            print (O0000OO0OO00000O0 )#line:540
    def game_map (O0O0OOO00OOOOO000 ):#line:543
        global count_list #line:544
        try :#line:545
            O0000O0O0O000O000 =f'__{timi_new()}'#line:546
            O0OOO0O0O0OOOOOOO ={'source':'scsc','authorization':O0O0OOO00OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0O000O000 ),'signstring':O0000O0O0O000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
            O0O00O0000OO0OOO0 =requests .request ('get',f'{host}/game/map',headers =O0OOO0O0O0OOOOOOO ).json ()#line:558
            if 'status'in O0O00O0000OO0OOO0 :#line:560
                if O0O00O0000OO0OOO0 ['status']==200 :#line:561
                    for O0OO0O0OOOOOOO000 in O0O00O0000OO0OOO0 ['data']['list'][0 ]['crops']:#line:562
                        OO0OOOOO0O0O000OO =O0OO0O0OOOOOOO000 ['level']#line:564
                        if OO0OOOOO0O0O000OO ==41 :#line:565
                            OO00O00OOOO000OO0 =O0OO0O0OOOOOOO000 ['crop_name']#line:566
                            OOOO00O0OOOO00OO0 =O0OO0O0OOOOOOO000 ['count']#line:567
                            if OOOO00O0OOOO00OO0 >0 :#line:568
                                print (f'【农业资产】:{OO00O00OOOO000OO0}丨数量:{OOOO00O0OOOO00OO0}')#line:569
                                count_list +=OOOO00O0OOOO00OO0 #line:570
                                OO000O000OOO0000O =O0O0OOO00OOOOO000 .the_query ()#line:571
                                O0O0OOO00OOOOO000 .market_sale (OO000O000OOO0000O )#line:572
        except Exception as O0O0O0000OO00OO00 :#line:573
            print (O0O0O0000OO00OO00 )#line:574
    def give_gold (O000O0O0000OOOO00 ):#line:577
        try :#line:578
            O0O00O0O0OOO000O0 =f'__{timi_new()}'#line:579
            O0O00O0O0000O0O0O ={'source':'scsc','authorization':O000O0O0000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0OOO000O0 ),'signstring':O0O00O0O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:590
            OO0OO0O0OOO0O0O00 =requests .request ('get',f'{host}/user',headers =O0O00O0O0000O0O0O ).json ()#line:591
            if 'status'in OO0OO0O0OOO0O0O00 :#line:592
                if OO0OO0O0OOO0O0O00 ['status']==200 :#line:593
                    if float (O000O0O0000OOOO00 .doneeNo )!=0 :#line:594
                        O0O0O0000O00OO000 =OO0OO0O0OOO0O0O00 ['data']['assets']['gold']#line:595
                        if float (O0O0O0000O00OO000 )>float (O000O0O0000OOOO00 .innerId ):#line:596
                            O00OO0000OOO00OO0 =int (float (O0O0O0000O00OO000 )/1.1 )#line:597
                            O0O00O0O0OOO000O0 =f'_doneeNo={O000O0O0000OOOO00.doneeNo}&quantity={O00OO0000OOO00OO0}_{timi_new()}'#line:598
                            O0O00O0O0000O0O0O ={'source':'scsc','authorization':O000O0O0000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0OOO000O0 ),'signstring':O0O00O0O0OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:609
                            O0O000000OO000000 ={"quantity":O00OO0000OOO00OO0 ,"doneeNo":O000O0O0000OOOO00 .doneeNo }#line:613
                            O00OO0OOOOOOOO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00O0O0000O0O0O ,data =O0O000000OO000000 ).json ()#line:614
                            if 'status'in O00OO0OOOOOOOO0O0 :#line:616
                                if O00OO0OOOOOOOO0O0 ['status']==200 :#line:617
                                    if O00OO0OOOOOOOO0O0 ['data']:#line:618
                                        print (f'【赠送种子】:赠送{O00OO0000OOO00OO0}种子给{O000O0O0000OOOO00.doneeNo}成功')#line:619
                    else :#line:620
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:621
        except Exception as OO0OOOO000O00O0OO :#line:622
            print (OO0OOOO000O00O0OO )#line:623
    def invitation (OO000O0000OOOOOOO ):#line:625
        try :#line:626
            _OOOO0OO0O0OO0OO0O =float (bundled_def ())/4 #line:627
            OOO0O0O000OOOOOOO =f'_innerId={int(_OOOO0OO0O0OO0OO0O)}_{timi_new()}'#line:629
            OO000OOO000000OO0 ={'source':'scsc','authorization':OO000O0000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000OOOOOOO ),'signstring':OOO0O0O000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:640
            O000000OO0O00000O ={"innerId":int (_OOOO0OO0O0OO0OO0O )}#line:641
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO000OOO000000OO0 ,data =O000000OO0O00000O )#line:642
        except Exception as OO0000OOOOOO0OOOO :#line:643
            print (OO0000OOOOOO0OOOO )#line:644
    def winning_rewards (OOO00O0O00O0OOO0O ):#line:647
        try :#line:648
            O0O0OO0OOO00O00OO =f'__{timi_new()}'#line:649
            OO0O000OOO00O00OO ={'source':'scsc','authorization':OOO00O0O00O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOO00O00OO ),'signstring':O0O0OO0OOO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:660
            OO0O0OOO00OO0000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O000OOO00O00OO ).json ()#line:661
            if 'status'in OO0O0OOO00OO0000O :#line:663
                if OO0O0OOO00OO0000O ['status']==200 :#line:664
                    if OO0O0OOO00OO0000O ['data']['amount']:#line:665
                        OO0OOO0OO0OOOOO00 =OO0O0OOO00OO0000O ['data']['amount']['gold']#line:666
                        return OO0OOO0OO0OOOOO00 #line:667
                    else :#line:668
                        return 0 #line:669
        except Exception as O0OO00O0000OO00OO :#line:670
            print (O0OO00O0000OO00OO )#line:671
    def certification (O0O0O0O0OO0O0OOO0 ):#line:674
        try :#line:675
            OO0OOOOOO000O00O0 =f'__{timi_new()}'#line:676
            OO000OOO0OO0OO00O ={'source':'scsc','authorization':O0O0O0O0OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO000O00O0 ),'signstring':OO0OOOOOO000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:687
            O00O00OO0O0OO00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO000OOO0OO0OO00O ).json ()#line:688
            if 'status'in O00O00OO0O0OO00O0 :#line:690
                if O00O00OO0O0OO00O0 ['status']==200 :#line:691
                    if O00O00OO0O0OO00O0 ['data']['result']:#line:692
                        O00OOOOOO0O00O00O =O00O00OO0O0OO00O0 ['data']['nick_name']#line:693
                        return O00OOOOOO0O00O00O #line:694
                    else :#line:695
                        return '未实名'#line:696
        except Exception as O0OO0000O00O0O00O :#line:697
            print (O0OO0000O00O0O00O )#line:698
    def crops_illustrated (OO000OOO000OO0OOO ):#line:701
        try :#line:702
            O0OO00000OO0000OO =f'__{timi_new()}'#line:703
            O000OOO000O00OOOO ={'source':'scsc','authorization':OO000OOO000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000OO0000OO ),'signstring':O0OO00000OO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:714
            OO000OOO00O0OOOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000OOO000O00OOOO ).json ()#line:715
            if 'status'in OO000OOO00O0OOOOO :#line:717
                if OO000OOO00O0OOOOO ['status']==200 :#line:718
                    OO00O000OO0O00000 =OO000OOO00O0OOOOO ['data'][0 ]['crops']#line:719
                    for OO0OO000O00OOO0OO in OO00O000OO0O00000 :#line:720
                        if OO0OO000O00OOO0OO ['ill_clover_award']:#line:721
                            if float (OO0OO000O00OOO0OO ['ill_clover_award'])>1 :#line:722
                                if OO0OO000O00OOO0OO ['is_finish']:#line:723
                                    if not OO0OO000O00OOO0OO ['is_getit']:#line:724
                                        if OO000OOO000OO0OOO .certification ()!='未实名':#line:725
                                            O0OO00000OO0000OO =f'_award_level={OO0OO000O00OOO0OO["level"]}_{timi_new()}'#line:726
                                            O000OOO000O00OOOO ={'source':'scsc','authorization':OO000OOO000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000OO0000OO ),'signstring':O0OO00000OO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:737
                                            O0OOOO00OOOO00000 ={"award_level":OO0OO000O00OOO0OO ['level']}#line:738
                                            OO0O0O0OOOO0OO00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000OOO000O00OOOO ,json =O0OOOO00OOOO00000 ).json ()#line:740
                                            if 'status'in OO0O0O0OOOO0OO00O :#line:741
                                                if OO0O0O0OOOO0OO00O ['status']==200 :#line:742
                                                    OOO00OO00O00OOO0O =OO0O0O0OOOO0OO00O ['data']['ill_clover_award']#line:743
                                                    print (f'【图鉴奖励】:领取{OO0OO000O00OOO0OO["crop_name"]}成就丨奖励{OOO00OO00O00OOO0O}☘️')#line:745
                                                if OO0O0O0OOOO0OO00O ['status']==500 :#line:746
                                                    print (f'【图鉴奖励】:{OO0O0O0OOOO0OO00O["message"]}')#line:747
        except Exception as O0O0O0OO0O000OOOO :#line:748
            print (O0O0O0OO0O000OOOO )#line:749
    def watched_ad (OOO0OOO00O0O00O00 ):#line:752
        try :#line:753
            O00O000O0OO00OOO0 =f'__{timi_new()}'#line:754
            OOO00OO0OO0000OOO ={'source':'scsc','authorization':OOO0OOO00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O0OO00OOO0 ),'signstring':O00O000O0OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            O00O0OO000O0000OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO00OO0OO0000OOO ).json ()#line:766
            if 'status'in O00O0OO000O0000OO :#line:768
                if O00O0OO000O0000OO ['status']==200 :#line:769
                    if 'offlineInfo'in O00O0OO000O0000OO ['data']:#line:770
                        time .sleep (random .randint (1 ,3 ))#line:771
                        O0O000OO0000OO0OO =O00O0OO000O0000OO ['data']['offlineInfo']['off_minute']#line:772
                        O0OO00O0O00O00O0O =float (O00O0OO000O0000OO ['data']['silver'])/1000000000000 #line:773
                        time .sleep (1 )#line:774
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO00OO0OO0000OOO ).json ()#line:775
                        time .sleep (2 )#line:776
                        O0OO000000OO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00OO0OO0000OOO ).json ()#line:777
                        if 'status'in O0OO000000OO0OO00 :#line:779
                            if O0OO000000OO0OO00 ['status']==200 :#line:780
                                O0OOO0OOO0OO00O0O =float (O0OO000000OO0OO00 ['data']['silver'])/1000000000000 #line:781
                                OOOOO00OO0O00O000 =str (O0OOO0OOO0OO00O0O -O0OO00O0O00O00O0O )[:6 ]#line:782
                                print (f'【离线奖励】:翻倍离线{O0O000OO0000OO0OO}分钟奖励🌱数量:{OOOOO00OO0O00O000}t粒')#line:783
        except Exception as OOOO0O0000OO00OOO :#line:784
            print (OOOO0O0000OO00OOO )#line:785
    def user_ad (OOOOO00O000O00OO0 ):#line:788
        try :#line:789
            O0O00O0O000OO00OO =f'__{timi_new()}'#line:790
            OOOOOO0O00OOOOOO0 ={'source':'scsc','authorization':OOOOO00O000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000OO00OO ),'signstring':O0O00O0O000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:801
            O0OO0OO0O00O0O0OO =requests .request ('get',f'{host}/user/ad',headers =OOOOOO0O00OOOOOO0 ).json ()#line:802
            if 'status'in O0OO0OO0O00O0O0OO :#line:804
                if O0OO0OO0O00O0O0OO ['status']==200 :#line:805
                    OOO0OO0000OO00OOO =O0OO0OO0O00O0O0OO ['data']['max_time']#line:806
                    O0OOO000000OOOOOO =O0OO0OO0O00O0O0OO ['data']['watch_time']#line:807
                    OO0000OOOOO00O0OO =O0OO0OO0O00O0O0OO ['data']['added_time']#line:808
                    print (f'【获取种子】:获取🌱剩余{OO0000OOOOO00O0OO + OOO0OO0000OO00OOO - O0OOO000000OOOOOO}次丨好友提供:{OO0000OOOOO00O0OO}次')#line:809
                    if OO0000OOOOO00O0OO +OOO0OO0000OO00OOO -O0OOO000000OOOOOO >0 :#line:810
                        time .sleep (random .randint (16 ,19 ))#line:811
                        O000O0O00000OO0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOOOO0O00OOOOOO0 ).json ()#line:812
                        if 'status'in O000O0O00000OO0OO :#line:814
                            if O000O0O00000OO0OO ['status']==200 :#line:815
                                OOOOOO0O00O000O0O =float (O000O0O00000OO0OO ['data']['silver'])/1000000000000 #line:816
                                print (f'【获取种子】:获得🌱:{int(OOOOOO0O00O000O0O)}t粒')#line:817
                                return True #line:818
                            if O000O0O00000OO0OO ['status']==500 :#line:819
                                O0OO000OO00OOOO00 =O000O0O00000OO0OO ['message']#line:820
                                print (f'【获取种子】:{O0OO000OO00OOOO00}')#line:821
                                return False #line:822
        except Exception as OOOOOO0O0O00O0O00 :#line:823
            print (OOOOOO0O0O00O0O00 )#line:824
    def synthetic (OOO00O0O0O0OO0000 ):#line:827
        global id ,g #line:828
        try :#line:829
            O0OOO000OO000OOO0 =OOO00O0O0O0OO0000 .level_new ()#line:830
            OO0OOOO00O0000OO0 =random .randint (9 ,11 )#line:831
            OOO000O0000000O0O =f'_site=8&targetSite={OO0OOOO00O0000OO0}_{timi_new()}'#line:832
            O000OOOO00OOOOOOO ={'source':'scsc','authorization':OOO00O0O0O0OO0000 .token ,'timestamp':timi_new (),'sign':sign (OOO000O0000000O0O ),'signstring':OOO000O0000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:843
            OOOOOO0O000OOOOOO ={"site":int (8 ),"targetSite":int (OO0OOOO00O0000OO0 )}#line:844
            requests .request ('post',f'{host}/game/crops/move',headers =O000OOOO00OOOOOOO ,json =OOOOOO0O000OOOOOO )#line:845
            while True :#line:846
                O0O00O0000OO0O0O0 =f'__{timi_new()}'#line:847
                O0O0O0OOO00OOOO00 ={'source':'scsc','authorization':OOO00O0O0O0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000OO0O0O0 ),'signstring':O0O00O0000OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:858
                O00OOOO00000OOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00OOOO00 ).json ()#line:859
                if 'status'in O00OOOO00000OOO00 :#line:861
                    if O00OOOO00000OOO00 ['status']==200 :#line:862
                        O00OO000OO0OOO0OO =O00OOOO00000OOO00 ['data']['cropList']#line:863
                        O000O0000O0OOO00O =O00OOOO00000OOO00 ['data']['gameCoreDataDBid']#line:864
                        O00O0000OO00OOOO0 =float (O00OOOO00000OOO00 ['data']['silver'])/1000000000000 #line:865
                        OO0OOOO0OOOO000OO =0 #line:870
                        for O0O0O0O00O0OOO00O in O00OO000OO0OOO0OO :#line:871
                            if not O0O0O0O00O0OOO00O :#line:872
                                OO000OO0O0O000O0O =f'_crop_id={O000O0000O0OOO00O}&site={OO0OOOO0OOOO000OO}_{OOO00O0O0O0OO0000.time}'#line:873
                                O00OOO000O0O00OOO ={'source':'scsc','authorization':OOO00O0O0O0OO0000 .token ,'timestamp':OOO00O0O0O0OO0000 .time ,'sign':sign (OO000OO0O0O000O0O ),'signstring':OO000OO0O0O000O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:883
                                O000O000OO0OO0OOO ={"site":OO0OOOO0OOOO000OO ,"crop_id":O000O0000O0OOO00O }#line:884
                                O00O0OO00OO00000O =requests .request ('post',f'{host}/game/crops/buy',headers =O00OOO000O0O00OOO ,data =O000O000OO0OO0OOO ).json ()#line:885
                                time .sleep (random .randint (1 ,3 )/10 )#line:887
                                if 'status'in O00O0OO00OO00000O :#line:888
                                    if O00O0OO00OO00000O ['status']==200 :#line:889
                                        if O00O0OO00OO00000O ['message']=='种子数量不足':#line:890
                                            O0OOO000OO000OOO0 =OOO00O0O0O0OO0000 .level_new ()#line:891
                                            print (f'【种植合成】:{O00O0OO00OO00000O["message"]}')#line:892
                                            if not OOO00O0O0O0OO0000 .user_ad ():#line:893
                                                return False #line:894
                                    if O00O0OO00OO00000O ['status']==500 :#line:895
                                        print (f'【种植合成】:{O00O0OO00OO00000O["message"]}')#line:896
                                        return False #line:897
                            OO0OOOO0OOOO000OO +=1 #line:898
                        O000OOOOOO0O0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00OOOO00 ).json ()#line:899
                        OO00O0O00O0O0OOOO =O000OOOOOO0O0O0OO ['data']['cropList']#line:900
                        OOO00OOO00000OO0O =False #line:901
                        for O0O0O0O00O0OOO00O in range (12 ):#line:902
                            id =OO00O0O00O0O0OOOO [O0O0O0O00O0OOO00O ]['level']#line:903
                            if float (O0OOO000OO000OOO0 )-float (id )>9 :#line:904
                                OO0OO0O00OO0OO0OO =f'_site={O0O0O0O00O0OOO00O}_{timi_new()}'#line:905
                                O0O0O0OOOO0OOO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00O0O0O0OO0000 .token ,'timestamp':timi_new (),'sign':sign (OO0OO0O00OO0OO0OO ),'signstring':OO0OO0O00OO0OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:916
                                O0000O0OOOOO00O00 ={"site":O0O0O0O00O0OOO00O }#line:917
                                OOOO0OOO0OOO0000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O0OOOO0OOO00O ,data =O0000O0OOOOO00O00 ).json ()#line:919
                                if 'status'in OOOO0OOO0OOO0000O :#line:920
                                    if OOOO0OOO0OOO0000O ['status']==200 :#line:921
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:922
                            if id !=0 :#line:923
                                for O00O00000O00O00OO in range (11 ):#line:924
                                    OOOOOOOOOOOO00O0O =O00O00000O00O00OO +1 #line:925
                                    g =OO00O0O00O0O0OOOO [OOOOOOOOOOOO00O0O ]['level']#line:926
                                    if id ==g :#line:927
                                        O000OOO0O0O0O0000 =O00O00000O00O00OO +2 #line:928
                                        if O000OOO0O0O0O0000 !=O0O0O0O00O0OOO00O +1 :#line:929
                                            OOOOO0O000OOO0O00 =O0O0O0O00O0OOO00O +1 #line:930
                                            time .sleep (random .randint (1 ,3 )/10 )#line:932
                                            OOO000O0000000O0O =f'_site={OOOOO0O000OOO0O00 - 1}&targetSite={O000OOO0O0O0O0000 - 1}_{timi_new()}'#line:933
                                            O000OOOO00OOOOOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00O0O0O0OO0000 .token ,'timestamp':timi_new (),'sign':sign (OOO000O0000000O0O ),'signstring':OOO000O0000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:950
                                            O0O0O0O0OO00OO0OO ={"site":int (OOOOO0O000OOO0O00 -1 ),"targetSite":int (O000OOO0O0O0O0000 -1 )}#line:951
                                            requests .request ('post',f'{host}/game/crops/move',headers =O000OOOO00OOOOOOO ,json =O0O0O0O0OO00OO0OO )#line:952
                                            OOO00OOO00000OO0O =True #line:954
                                    if OOO00OOO00000OO0O :#line:955
                                        break #line:956
                                if OOO00OOO00000OO0O :#line:957
                                    break #line:958
        except :#line:959
            OOO00O0O0O0OO0000 .synthetic ()#line:960
    def level_new (OO0OO0O0OOOO00O0O ):#line:963
        try :#line:964
            OO00OOO0OOOOOOO00 =f'__{timi_new()}'#line:965
            O00O00O0OO0OO0000 ={'source':'scsc','authorization':OO0OO0O0OOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOOOOOO00 ),'signstring':OO00OOO0OOOOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:976
            O0OO0O0OOOOOO0OO0 =requests .request ('get',f'{host}/user',headers =O00O00O0OO0OO0000 ).json ()#line:977
            if 'status'in O0OO0O0OOOOOO0OO0 :#line:978
                if O0OO0O0OOOOOO0OO0 ['status']==200 :#line:979
                    return float (O0OO0O0OOOOOO0OO0 ['data']['level'])#line:980
        except Exception as OOOOOOOOOOO0O0OOO :#line:981
            print (OOOOOOOOOOO0O0OOO )#line:982
    def propsraffle (OO0O000000O0000OO ):#line:985
        try :#line:986
            while True :#line:987
                OOO0OO0OO0OO0O000 =f'__{timi_new()}'#line:988
                O00O00O00OOOOOO00 ={'source':'scsc','authorization':OO0O000000O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO0OO0O000 ),'signstring':OOO0OO0OO0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:999
                O000OOO00OOO00O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O00O00OOOOOO00 ).json ()#line:1000
                if 'status'in O000OOO00OOO00O0O :#line:1002
                    if O000OOO00OOO00O0O ['status']==200 :#line:1003
                        O0OOO00000OOO00O0 =O000OOO00OOO00O0O ['data']['rows']#line:1004
                        O0O0OOOO0O0OO00OO =O000OOO00OOO00O0O ['data']['vstate']#line:1005
                        if O0OOO00000OOO00O0 ==5 or O0OOO00000OOO00O0 ==6 or O0OOO00000OOO00O0 ==7 :#line:1006
                            OO00OOOOO0000O00O =O000OOO00OOO00O0O ['data']['silver']#line:1007
                            print (f'【转盘抽奖】:获得种子:{OO00OOOOO0000O00O}')#line:1008
                        if O0OOO00000OOO00O0 ==1 or O0OOO00000OOO00O0 ==2 or O0OOO00000OOO00O0 ==3 :#line:1009
                            O0O0O00OOO0O0000O =O000OOO00OOO00O0O ['data']['clover']#line:1010
                            print (f'【转盘抽奖】:获得三叶草:{O0O0O00OOO0O0000O}')#line:1011
                        if O0OOO00000OOO00O0 ==4 or O0OOO00000OOO00O0 ==8 :#line:1012
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1013
                        if O0OOO00000OOO00O0 =='抽奖次数已用完':#line:1017
                            break #line:1051
                time .sleep (random .randint (8 ,15 )/10 )#line:1052
        except Exception as OO0OOOO000O00O0O0 :#line:1053
            print (OO0OOOO000O00O0O0 )#line:1054
    def friends_invitation (O0OOOO000O0000OOO ):#line:1057
        try :#line:1058
            O000O0OOOO0O0OOO0 =f'__{timi_new()}'#line:1059
            OOO000000OOOO000O ={'source':'scsc','authorization':O0OOOO000O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0O0OOO0 ),'signstring':O000O0OOOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1070
            OO00OO000OO0O00O0 =requests .request ('get',f'{host}/friends',headers =OOO000000OOOO000O ).json ()#line:1071
            if 'status'in OO00OO000OO0O00O0 :#line:1072
                if OO00OO000OO0O00O0 ['status']==200 :#line:1073
                    OO0O0O0OOOO000000 =OO00OO000OO0O00O0 ['data']['myInviteter']#line:1074
                    if OO0O0O0OOOO000000 :#line:1075
                        OOOO0O0O000O0O00O =OO0O0O0OOOO000000 ['user']['nickname']#line:1076
                        OO0O00O000000O0OO =O0OOOO000O0000OOO .certification ()#line:1077
                        if OO0O00O000000O0OO =='未实名':#line:1078
                            weishim .append (O0OOOO000O0000OOO .token )#line:1079
                        print (f'【查邀请人】:我的邀请人:{OOOO0O0O000O0O00O}丨实名:{OO0O00O000000O0OO}')#line:1080
                    else :#line:1081
                        if O0OOOO000O0000OOO .innerId !='0':#line:1082
                            O0OOOO000O0000OOO .invitation ()#line:1083
        except Exception as OO0OO0OOOO0O0000O :#line:1084
            print (OO0OO0OOOO0O0000O )#line:1085
    def add_clover (OOOO0OO0OOO00OOOO ):#line:1088
        global golden_seed #line:1089
        try :#line:1090
            OOO0OOOOO000O0OOO =f'__{timi_new()}'#line:1091
            O000000OO00OO000O ={'source':'scsc','authorization':OOOO0OO0OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO000O0OOO ),'signstring':OOO0OOOOO000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1102
            O00O0OOOO00000O00 =requests .request ('get',f'{host}/assets/clovers',headers =O000000OO00OO000O ).json ()#line:1103
            if 'status'in O00O0OOOO00000O00 :#line:1105
                if O00O0OOOO00000O00 ['status']==200 :#line:1106
                    O00OO0OO0OO0OOOO0 =O00O0OOOO00000O00 ['data']['clover']#line:1107
                    OO000000O0OOOO000 =O00O0OOOO00000O00 ['data']['used_clover']#line:1108
                    O0000O000OOOO00O0 =float (O00OO0OO0OO0OOOO0 )-float (OO000000O0OOOO000 )#line:1109
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO000000O0OOOO000}')#line:1110
                    if OOOO0OO0OOO00OOOO .certification ()!='未实名':#line:1111
                        if O0000O000OOOO00O0 >1 :#line:1112
                            OOO0OOOOO000O0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000O000OOOO00O0)}_{timi_new()}'#line:1113
                            O0O0OOO00O0O00O0O ={'source':'scsc','authorization':OOOO0OO0OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO000O0OOO ),'signstring':OOO0OOOOO000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                            O0OO0OOOO0O0OOOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000O000OOOO00O0 )}#line:1125
                            OO00000OO0OOO0000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0OOO00O0O00O0O ,data =O0OO0OOOO0O0OOOOO ).json ()#line:1126
                            if 'status'in OO00000OO0OOO0000 :#line:1128
                                if OO00000OO0OOO0000 ['status']==200 :#line:1129
                                    print (f'【参与抽奖】:添加☘️:{OO00000OO0OOO0000["data"]["isSuccess"]}丨数量:{O0000O000OOOO00O0}')#line:1130
                                if OO00000OO0OOO0000 ['status']==500 :#line:1131
                                    print (f'【参与抽奖】:添加☘️:{OO00000OO0OOO0000["message"]}')#line:1132
            OOO0OOO00OO000000 =requests .request ('get',f'{host}/lottery',headers =O000000OO00OO000O ).json ()#line:1133
            O00O000O000O0000O =OOOO0OO0OOO00OOOO .winning_rewards ()#line:1135
            if 'status'in OOO0OOO00OO000000 :#line:1136
                if OOO0OOO00OO000000 ['status']==200 :#line:1137
                    OOO0000OOO000O00O =OOO0OOO00OO000000 ['data'][0 ]['day_get_gold_quantity']#line:1138
                    golden_seed +=float (OOO0000OOO000O00O )#line:1139
                    OO0O00O0OO0O000OO =OOO0OOO00OO000000 ['data'][1 ]['value']#line:1140
                    O0OO000O00OO0OOOO =OOO0OOO00OO000000 ['data'][0 ]['join_number']#line:1141
                    OOOOOO00000OOO000 =int (float (OOO0OOO00OO000000 ['data'][0 ]['totalValue']))#line:1142
                    O0O0OO0O0O00OO0OO =float (OO0O00O0OO0O000OO /OOOOOO00000OOO000 )*10000 #line:1143
                    OOO0000OOO0OOO000 =OOOOOO00000OOO000 /O0OO000O00OO0OOOO #line:1144
                    print (f'【参与抽奖】:预计每天中{str(OOO0000OOO000O00O)[:6]}颗金种子丨好友收益:{str(O00O000O000O0000O)[:6]}')#line:1145
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0OO0O0O00OO0OO)[:6]}颗金种子丨☘️人均:{str(OOO0000OOO0OOO000)[:7]}️')#line:1146
        except Exception as OOO00O000OO00O0OO :#line:1147
            print (OOO00O000OO00O0OO )#line:1148
    def energy (O0OOO0OOO00OOOOOO ):#line:1151
        try :#line:1152
            while True :#line:1153
                O000OOO0OO0O00000 =f'__{timi_new()}'#line:1154
                OO0OOO000O0O0O0O0 ={'source':'scsc','authorization':O0OOO0OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0O00000 ),'signstring':O000OOO0OO0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1165
                O0O00O0000O00OO0O =requests .request ('get',f'{host}/energy/general',headers =OO0OOO000O0O0O0O0 ).json ()#line:1166
                if 'status'in O0O00O0000O00OO0O :#line:1168
                    if O0O00O0000O00OO0O ['status']==200 :#line:1169
                        OOO00O0O0O000O000 =O0O00O0000O00OO0O ['data']['ordinary_water']#line:1170
                        O000OO00OOOOO0OOO =O0O00O0000O00OO0O ['data']['ordinary_fertilizer']#line:1171
                        O0O0OOO0OOOOO00OO =O0O00O0000O00OO0O ['data']['videoStatus']#line:1172
                        O0O0000O00OO0O0O0 =O0O00O0000O00OO0O ['data']['waterVideoKey']#line:1173
                        print (f'【我的营养】:肥料:{str(O000OO00OOOOO0OOO).split(".")[0]}丨水滴:{str(OOO00O0O0O000O000).split(".")[0]}')#line:1175
                        if float (O000OO00OOOOO0OOO )<96 :#line:1176
                            if O0O0OOO0OOOOO00OO :#line:1177
                                time .sleep (random .randint (160 ,180 )/10 )#line:1178
                                OO0O0OO00O0OO0000 =99 -float (O000OO00OOOOO0OOO )#line:1179
                                O00OO000OO00OO0O0 ={"fertilizer":str (OO0O0OO00O0OO0000 ).split ('.')[0 ]}#line:1180
                                O000O0O00OO00OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOO000O0O0O0O0 ).json ()#line:1182
                                if 'status'in O000O0O00OO00OO00 :#line:1184
                                    if O000O0O00OO00OO00 ['status']==200 :#line:1185
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O00OO00OO00["message"]}')#line:1186
                                    if O000O0O00OO00OO00 ['status']==500 :#line:1187
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O00OO00OO00["message"]}')#line:1188
                                        break #line:1189
                                if float (O000OO00OOOOO0OOO )<78 :#line:1191
                                    OO0O0OO00O0OO0000 =80 -float (O000OO00OOOOO0OOO )#line:1192
                                    OO00OOO00000O0O00 =f'_fertilizer={int(OO0O0OO00O0OO0000)}_{timi_new()}'#line:1193
                                    OOO00000O00OO0OOO ={'source':'scsc','authorization':O0OOO0OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00000O0O00 ),'signstring':OO00OOO00000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1204
                                    OOO0O0O0O0OOOO00O ={"fertilizer":int (OO0O0OO00O0OO0000 )}#line:1205
                                    OOO00O0O0O0O0O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO00000O00OO0OOO ,data =OOO0O0O0O0OOOO00O ).json ()#line:1207
                                    if 'status'in OOO00O0O0O0O0O000 :#line:1209
                                        if OOO00O0O0O0O0O000 ['status']==200 :#line:1210
                                            print (f'【购买肥料】:购买肥料:{OOO00O0O0O0O0O000["message"]}丨数量:{int(OO0O0OO00O0OO0000)}')#line:1211
                                        if OOO00O0O0O0O0O000 ['status']==500 :#line:1212
                                            print (f'【购买肥料】:购买肥料:{OOO00O0O0O0O0O000["message"]}丨数量:{int(OO0O0OO00O0OO0000)}')#line:1213
                                            O0OOOO0OO000O0000 =OOO00O0O0O0O0O000 ["message"].split ('-')[1 ]#line:1214
                                            OOOOOO00000O000OO =f'__{timi_new()}'#line:1215
                                            OOO0OO0O0OOOO0O0O ={'source':'scsc','authorization':O0OOO0OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00000O000OO ),'signstring':OOOOOO00000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1226
                                            O00OO00OO00OO0000 =requests .request ('get',f'{host}/user',headers =OOO0OO0O0OOOO0O0O ).json ()#line:1227
                                            if 'status'in O00OO00OO00OO0000 :#line:1228
                                                if O00OO00OO00OO0000 ['status']==200 :#line:1229
                                                    OO0O0O00O0OOO0OO0 =O00OO00OO00OO0000 ['data']['inner_id']#line:1230
                                                    if give_gold (OO0O0O00O0OOO0OO0 ,float (O0OOOO0OO000O0000 )+1 ):#line:1231
                                                        O0OOO0OOO00OOOOOO .energy ()#line:1232
                        if float (OOO00O0O0O000O000 )<880 :#line:1233
                            if O0O0000O00OO0O0O0 :#line:1234
                                time .sleep (random .randint (160 ,180 )/10 )#line:1235
                                O00OO000OO000OO00 =999 -float (OOO00O0O0O000O000 )#line:1236
                                OO00O0OO0OOOOOO00 ={"water":str (O00OO000OO000OO00 ).split ('.')[0 ]}#line:1237
                                O00000O00OOOOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOO000O0O0O0O0 ).json ()#line:1239
                                if 'status'in O00000O00OOOOOOO0 :#line:1241
                                    if O00000O00OOOOOOO0 ['status']==200 :#line:1242
                                        print (f'【购买水滴】:看广告获取水滴:{O00000O00OOOOOOO0["message"]}')#line:1243
                                    if O00000O00OOOOOOO0 ['status']==500 :#line:1244
                                        print (f'【购买水滴】:看广告获取水滴:{O00000O00OOOOOOO0["message"]}')#line:1245
                                        break #line:1246
                                if float (OOO00O0O0O000O000 )<780 :#line:1247
                                    O00OO000OO000OO00 =800 -float (OOO00O0O0O000O000 )#line:1248
                                    OOOOOOOO0O0000O00 =f'_water={int(O00OO000OO000OO00)}_{timi_new()}'#line:1249
                                    O0OO000000O0OOO00 ={'source':'scsc','authorization':O0OOO0OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0O0000O00 ),'signstring':OOOOOOOO0O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1260
                                    OO0000OO0OO000000 ={"water":int (O00OO000OO000OO00 )}#line:1261
                                    O0O000O0OOOO0000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OO000000O0OOO00 ,data =OO0000OO0OO000000 ).json ()#line:1263
                                    if 'status'in O0O000O0OOOO0000O :#line:1265
                                        if O0O000O0OOOO0000O ['status']==200 :#line:1266
                                            print (f'【购买水滴】:购买水滴:{O0O000O0OOOO0000O["message"]}丨数量:{int(O00OO000OO000OO00)}')#line:1267
                                        if O0O000O0OOOO0000O ['status']==500 :#line:1268
                                            print (f'【购买水滴】:购买水滴:{O0O000O0OOOO0000O["message"]}丨数量:{int(O00OO000OO000OO00)}')#line:1269
                                            O0OOOO0OO000O0000 =O0O000O0OOOO0000O ["message"].split ('-')[1 ]#line:1270
                                            OOOOOO00000O000OO =f'__{timi_new()}'#line:1271
                                            OOO0OO0O0OOOO0O0O ={'source':'scsc','authorization':O0OOO0OOO00OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00000O000OO ),'signstring':OOOOOO00000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1282
                                            O00OO00OO00OO0000 =requests .request ('get',f'{host}/user',headers =OOO0OO0O0OOOO0O0O ).json ()#line:1283
                                            if 'status'in O00OO00OO00OO0000 :#line:1284
                                                if O00OO00OO00OO0000 ['status']==200 :#line:1285
                                                    OO0O0O00O0OOO0OO0 =O00OO00OO00OO0000 ['data']['inner_id']#line:1286
                                                    if give_gold (OO0O0O00O0OOO0OO0 ,float (O0OOOO0OO000O0000 )+1 ):#line:1287
                                                        O0OOO0OOO00OOOOOO .energy ()#line:1288
                        break #line:1289
        except Exception as O00OOOOOO00000OOO :#line:1290
            print (O00OOOOOO00000OOO )#line:1291
def bundled_def ():#line:1293
    OOOO0OOO0OOO0OO0O =requests .request ('get',f'{git}/{appoo()}').text #line:1294
    return OOOO0OOO0OOO0OO0O .split ("\n")[random .randint (0 ,len (OOOO0OOO0OOO0OO0O .split ("\n"))-1 )]#line:1295
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
        OOOOOO0O000O00O00 =gitee_edition ()#line:1334
        if version_of_the_validation ()<OOOOOO0O000O00O00 ['CityEarth']['edition']:#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0O000O00O00["CityEarth"]["edition"]}   ❌')#line:1336
            print (f'更新内容=>>{OOOOOO0O000O00O00["CityEarth"]["content"]}')#line:1337
        else :#line:1338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0O000O00O00["CityEarth"]["edition"]}   ✅')#line:1339
            print (f'更新内容=>> {OOOOOO0O000O00O00["CityEarth"]["content"]}')#line:1340
    except Exception as O0000O0OOOO000O0O :#line:1341
        print (O0000O0OOOO000O0O )#line:1342
def sc3 ():#line:1345
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1346
if __name__ =='__main__':#line:1349
    start ()#line:1350

