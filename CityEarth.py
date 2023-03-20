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
@ 版本  4.9
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
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
        O0OOOO0O0000OO0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OOOO0O0000OO0O0)}个账号==========")#line:17
        for OOOO0OO000O0OO0O0 in O0OOOO0O0000OO0O0 :#line:18
            OO00O0O000O000000 =[]#line:19
            print (f"------------正在执行第{O0OOOO0O0000OO0O0.index(OOOO0OO000O0OO0O0) + 1}个账号------------")#line:20
            O0000O0OOOO00O0OO =CityEarth (OOOO0OO000O0OO0O0 ,OO00O0O000O000000 ,O0OOOO0O0000OO0O0 .index (OOOO0OO000O0OO0O0 ))#line:21
            def OOOO0OO0OOO0OO000 ():#line:23
                if O0000O0OOOO00O0OO .base_info ():#line:25
                    O0000O0OOOO00O0OO .sealing ()#line:27
                    O0000O0OOOO00O0OO .invitenum ()#line:29
                    O0000O0OOOO00O0OO .query_to_sell ()#line:31
                    O0000O0OOOO00O0OO .friends_invitation ()#line:35
                    O0000O0OOOO00O0OO .energy ()#line:37
                    O0000O0OOOO00O0OO .add_clover ()#line:39
                    O0000O0OOOO00O0OO .propsraffle ()#line:41
                    O0000O0OOOO00O0OO .synthetic ()#line:43
                    O0000O0OOOO00O0OO .crops_illustrated ()#line:45
                    O0000O0OOOO00O0OO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0000O0OOOO00O0OO .give_gold ()#line:50
            OOOO0OOO00O000OOO =threading .Thread (target =OOOO0OO0OOO0OO000 )#line:52
            OOOO0OOO00O000OOO .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0O00O0OOO000000 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O00O0OOO000000 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO0O0OOO00000O00 in invited_new :#line:62
            print (OOO0O0OOO00000O00 )#line:63
        print ('开始打印未实名的token')#line:64
        for O0OOO0000OO0O00O0 in weishim :#line:65
            print (O0OOO0000OO0O00O0 )#line:66
    except Exception as O00OOOOOOO0OOO0O0 :#line:67
        print (O00OOOOOOO0OOO0O0 )#line:68
def give_gold (O00OOOO0O000OOO00 ,OOO0O000O0OO000OO ):#line:72
    try :#line:73
        OO0O00O0O00O00O0O =f'_doneeNo={O00OOOO0O000OOO00}&quantity={int(OOO0O000O0OO000OO)}_{timi_new()}'#line:74
        O0O0O0OOO000OO00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O00O0O00O00O0O ),'signstring':OO0O00O0O00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOO0OO0O0000000OO ={"quantity":int (OOO0O000O0OO000OO ),"doneeNo":O00OOOO0O000OOO00 }#line:89
        O0OO0O0OO0OO0OO00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0OOO000OO00O ,data =OOO0OO0O0000000OO ).json ()#line:90
        if 'status'in O0OO0O0OO0OO0OO00 :#line:92
            if O0OO0O0OO0OO0OO00 ['status']==200 :#line:93
                if O0OO0O0OO0OO0OO00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO0O000O0OO000OO)}种子给{O00OOOO0O000OOO00}成功')#line:95
                    return True #line:96
            if O0OO0O0OO0OO0OO00 ['status']==401 :#line:97
                print (f'【赠送种子】:{O0OO0O0OO0OO0OO00["message"]}')#line:98
                return False #line:99
            if O0OO0O0OO0OO0OO00 ['status']==500 :#line:100
                print (f'【赠送种子】:{O0OO0O0OO0OO0OO00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OO0O0O0O0O0O0OOO0 :#line:104
        print (OO0O0O0O0O0O0OOO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0000OO0OO000O00 ):#line:115
    OOO0OO0OOOO0O00OO =hashlib .md5 (OO0000OO0OO000O00 .encode ()).hexdigest ()#line:116
    OOOO0000OO0OO0000 =sc1 ()#line:117
    OOOOOO000O0OOO00O =sc2 ()#line:118
    OOO000000OO00OO00 =sc3 ()#line:119
    OO0O0O000OOOO0000 =OOOO0000OO0OO0000 +OOO0OO0OOOO0O00OO +OOOOOO000O0OOO00O +OOO000000OO00OO00 #line:120
    OO0O00O00000OO0O0 =hashlib .md5 (OO0O0O000OOOO0000 .encode ()).hexdigest ()#line:121
    return OO0O00O00000OO0O0 #line:122
def format_msg ():#line:125
    OO000OOO0OOO0OO00 =""#line:126
    for OOOOOOOOO00O0O000 in msg_list :#line:127
        OO000OOO0OOO0OO00 +=str (OOOOOOOOO00O0O000 )+"\r\n"#line:128
    return OO000OOO0OOO0OO00 #line:129
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
def get_json_data (O0O00OOOO00OO0OO0 ,O000OO0O0000000OO ,O0OOO000OO00OOOOO ,O0OO0OOOOO0O00000 ):#line:153
    with open (O0O00OOOO00OO0OO0 ,'rb')as O0O00O00O000000OO :#line:154
        OOOO000O0O00OO0OO =json .load (O0O00O00O000000OO )#line:155
        OOOO000O0O00OO0OO ['data'][O000OO0O0000000OO ][O0OOO000OO00OOOOO ]=O0OO0OOOOO0O00000 #line:156
        O0OOO0O0OOOO00O0O =OOOO000O0O00OO0OO #line:157
    O0O00O00O000000OO .close ()#line:158
    return O0OOO0O0OOOO00O0O #line:159
def write_json_data (OOOOO0O00O0OO00O0 ):#line:162
    with open (json_path1 ,'w')as OO0O00000OOO0O00O :#line:163
        json .dump (OOOOO0O00O0OO00O0 ,OO0O00000OOO0O00O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OO0O00000OOO0O00O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OOOO0OOO000OOOO0O ,OOOOO0OOOOO00O000 ,O0O0OO0O0OOO0O0OO ,O00O00O0O0O0000O0 ):#line:171
        try :#line:172
            OOOO0OOO000OOOO0O .msg =O0O0OO0O0OOO0O0OO #line:173
            OOOO0OOO000OOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OOOO0OOO000OOOO0O .token =OOOOO0OOOOO00O000 ['authorization']#line:175
            OOOO0OOO000OOOO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OOOO0OOO000OOOO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OOOO0OOO000OOOO0O .elephant_user =OOOOO0OOOOO00O000 ['elephant_user']#line:178
            OOOO0OOO000OOOO0O .elephant_pswd =OOOOO0OOOOO00O000 ['elephant_pswd']#line:179
            OOOO0OOO000OOOO0O .elephant_Task_ID =OOOOO0OOOOO00O000 ['elephant_Task_ID']#line:180
            OOOO0OOO000OOOO0O .len_new =O00O00O0O0O0000O0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOO00O0OO0OOOOO0 ):#line:186
        try :#line:187
            OOOO00O0OO0OOOOO0 .watched_ad ()#line:189
            OO0O00OOO00OOO00O =f'__{timi_new()}'#line:190
            O00OO0OO0OO0OO00O ={'source':'scsc','authorization':OOOO00O0OO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO00OOO00O ),'signstring':OO0O00OOO00OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OO0OOO0OO00OO00O0 =requests .request ('get',f'{host}/user',headers =O00OO0OO0OO0OO00O ).json ()#line:202
            if 'status'in OO0OOO0OO00OO00O0 :#line:204
                if OO0OOO0OO00OO00O0 ['status']==200 :#line:205
                    OOO00O0O0O0O0OOO0 =OO0OOO0OO00OO00O0 ['data']['nickname']#line:206
                    O0000O0OO00OO0OOO =OO0OOO0OO00OO00O0 ['data']['inner_id']#line:207
                    O000OO000000000O0 =OO0OOO0OO00OO00O0 ['data']['assets']['gold']#line:208
                    OOO0O0O0O0O0O00OO =OO0OOO0OO00OO00O0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOO00O0O0O0O0OOO0[:5]}丨ID:{O0000O0OO00OO0OOO}丨等级:{OOO0O0O0O0O0O00OO}丨金种子:{str(O000OO000000000O0).split(".")[0]}')#line:211
                    if 'wx_'in OOO00O0O0O0O0OOO0 :#line:212
                        OOOO00O0OO0OOOOO0 .change_nickname ()#line:213
                if OO0OOO0OO00OO00O0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOO00O0OO0OOOOO0 .elephant_user =='f':#line:216
                        return False #line:217
                    OOOOOOOOO00000O0O =Invalid_login .addtask (elephant_user =OOOO00O0OO0OOOOO0 .elephant_user ,elephant_pswd =OOOO00O0OO0OOOOO0 .elephant_pswd ,elephant_Task_ID =OOOO00O0OO0OOOOO0 .elephant_Task_ID )#line:220
                    OO00O0OOO00O000OO =get_json_data (json_path ,OOOO00O0OO0OOOOO0 .len_new ,'authorization',OOOOOOOOO00000O0O )#line:221
                    if write_json_data (OO00O0OOO00O000OO ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OO0OOO0OO00OO00O0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O0O0000OOO0OO000O :#line:228
            print (O0O0000OOO0OO000O )#line:229
    def sealing (O0O000OO0O0OO0OOO ):#line:232
        try :#line:233
            OOOO0000OO000O0OO =f'__{timi_new()}'#line:234
            O00OO0OO0O000O00O ={'source':'scsc','authorization':O0O000OO0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OO000O0OO ),'signstring':OOOO0000OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO0OO0O000O00O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O00OO0OO0O000O00O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO0OO0O000O00O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO0OO0O000O00O )#line:249
            requests .request ('get',f'{host}/user',headers =O00OO0OO0O000O00O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO0OO0O000O00O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO0OO0O000O00O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO0OO0O000O00O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO0OO0O000O00O )#line:254
            requests .request ('get',f'{host}/assets',headers =O00OO0OO0O000O00O )#line:255
        except Exception as OOOOOOO000OOO00O0 :#line:256
            print (OOOOOOO000OOO00O0 )#line:257
    def ddd (OOOO000O0O000OO00 ):#line:259
        try :#line:260
            O00O0O0OOOOOO00OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO0OOOO0O0000OO0O ={'source':'scsc','authorization':OOOO000O0O000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OOOOOO00OO ),'signstring':O00O0O0OOOOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO0OO0000OOO0O0O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OOOO0O0000OO0O ).json ()#line:273
            print (OOO0OO0000OOO0O0O )#line:274
        except Exception as O000OO0O0000000O0 :#line:277
            print (O000OO0O0000000O0 )#line:278
    def the_query (O000O0OOOOOO0OO00 ):#line:283
        try :#line:284
            OO000O0O00OOOOOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO00000O0O0OO0OOO ={'authorization':O000O0OOOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O00OOOOOOO ),'signstring':OO000O0O00OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O0O0000O0OO0O0O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00000O0O0OO0OOO ).json ()#line:296
            if 'status'in O0O0000O0OO0O0O0O :#line:298
                if O0O0000O0OO0O0O0O ['status']==200 :#line:299
                    return O0O0000O0OO0O0O0O ['data']['rows'][4 ]['price']#line:300
        except Exception as O00000O0O0OO000O0 :#line:301
            print (O00000O0O0OO000O0 )#line:302
    def market_sale (O0OOOOO00OO00O00O ,O000OOO0OO0000000 ):#line:305
        try :#line:306
            O0O0OO0OOOO00OOO0 =timi_new ()#line:307
            OO0O0OO00OOO0OOOO =f'type=crop__{O0O0OO0OOOO00OOO0}'#line:308
            O0O00O000000OOO00 ={'source':'scsc','authorization':O0OOOOO00OO00O00O .token ,'timestamp':str (O0O0OO0OOOO00OOO0 ),'sign':sign (OO0O0OO00OOO0OOOO ),'signstring':OO0O0OO00OOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OOO0O000OOOOOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O00O000000OOO00 ).json ()#line:320
            if 'status'in O0OOO0O000OOOOOO0 :#line:322
                if O0OOO0O000OOOOOO0 ['status']==200 :#line:323
                    if O0OOO0O000OOOOOO0 ['data']['rows']:#line:324
                        OOOO0OOO00000OOO0 =O0OOO0O000OOOOOO0 ['data']['rows'][0 ]['packsackItemId']#line:325
                        OO00000O0000O00OO =O0OOO0O000OOOOOO0 ['data']['rows'][0 ]['quantity']#line:326
                        if float (O000OOO0OO0000000 )>6 :#line:327
                            O00OOO0O0OO0O0000 =f'_packsackItemId={OOOO0OOO00000OOO0}&price={str(O000OOO0OO0000000)[:5]}&quantity={OO00000O0000O00OO}_{O0O0OO0OOOO00OOO0}'#line:328
                            OOO0O0O0O000O0OO0 ={'source':'scsc','authorization':O0OOOOO00OO00O00O .token ,'timestamp':str (O0O0OO0OOOO00OOO0 ),'sign':sign (O00OOO0O0OO0O0000 ),'signstring':O00OOO0O0OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOOO00000OO00OOOO ={"packsackItemId":OOOO0OOO00000OOO0 ,"price":str (O000OOO0OO0000000 )[:5 ],"quantity":str (OO00000O0000O00OO )}#line:344
                            OO0OOO0000000O00O =requests .request ('post',f'{host}/market/sale',headers =OOO0O0O0O000O0OO0 ,data =OOOO00000OO00OOOO ).json ()#line:345
                            if 'status'in OO0OOO0000000O00O :#line:347
                                if OO0OOO0000000O00O ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OO00000O0000O00OO}丨价格:{str(O000OOO0OO0000000)[:5]}')#line:349
                                if OO0OOO0000000O00O ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{OO0OOO0000000O00O["message"]}')#line:351
        except Exception as OOO0OO0O0O0OOO00O :#line:352
            print (OOO0OO0O0O0OOO00O )#line:353
    def query_to_sell (OO0O0O000OOOOO0O0 ):#line:356
        global count_list #line:357
        try :#line:358
            OOO0O00O00000000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOOOOOOO0O000000O ={'source':'scsc','authorization':OO0O0O000OOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00000000O ),'signstring':OOO0O00O00000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            OOOOO00OOOOO0OOOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOOOOOO0O000000O ).json ()#line:371
            if 'status'in OOOOO00OOOOO0OOOO :#line:373
                if OOOOO00OOOOO0OOOO ['status']==200 :#line:374
                    for O0OOOO0O0O0OOOO0O in OOOOO00OOOOO0OOOO ['data']['rows']:#line:375
                        OOOO0OOO0O0O00O00 =O0OOOO0O0O0OOOO0O ['materialKey']#line:376
                        O0OOOO0O0O000O0OO =O0OOOO0O0O0OOOO0O ['quantity']#line:377
                        O0O00OOO0OOOO0OOO =O0OOOO0O0O0OOOO0O ['price']#line:378
                        O000OOO0OOO00OO00 =O0OOOO0O0O0OOOO0O ['saleState']#line:379
                        if O000OOO0OOO00OO00 ==0 :#line:380
                            print (f'【出售订单】:名称:{OOOO0OOO0O0O00O00}丨数量:{O0OOOO0O0O000O0OO}丨价格:{O0O00OOO0OOOO0OOO}')#line:381
                            count_list +=O0OOOO0O0O000O0OO #line:382
                            O00O000O00OO000O0 =OO0O0O000OOOOO0O0 .the_query ()#line:384
                            if float (O00O000O00OO000O0 )!=float (O0O00OOO0OOOO0OOO ):#line:385
                                O00000OO0O00O0O0O =O0OOOO0O0O0OOOO0O ['id']#line:386
                                OO0O0O000OOOOO0O0 .cacel_sale (O00000OO0O00O0O0O )#line:387
        except Exception as OO0O00O0OOOO00O00 :#line:391
            print (OO0O00O0OOOO00O00 )#line:392
    def cacel_sale (OOO0OO0O00O0OOOO0 ,O0000O0O00OOO0O0O ):#line:395
        try :#line:396
            OO00O00OOO0O0O00O =f'_saleId={O0000O0O00OOO0O0O}_{timi_new()}'#line:397
            O00O00OOOO0000000 ={'source':'scsc','authorization':OOO0OO0O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOO0O0O00O ),'signstring':OO00O00OOO0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OOOO0000OO0O0OO0O ={"saleId":O0000O0O00OOO0O0O }#line:409
            O00OO0OO00OOOO0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00O00OOOO0000000 ,data =OOOO0000OO0O0OO0O ).json ()#line:410
            if 'status'in O00OO0OO00OOOO0OO :#line:412
                if O00OO0OO00OOOO0OO ['status']==200 :#line:413
                    print (f'【下架出售】:{O00OO0OO00OOOO0OO["data"]}')#line:414
        except Exception as O0O0OO0OO0000OOO0 :#line:415
            print (O0O0OO0OO0000OOO0 )#line:416
    def change_nickname (OO0O0OOOOOOO00O00 ):#line:419
        try :#line:420
            O0O000O0OO00OOO0O =timi_new ()#line:421
            OO000O0O0O0O0OOOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OOOO00OO0000OO0OO =requests .request ('post','https://www.qmsjmfb.com/',data =OO000O0O0O0O0OOOO ).text #line:423
            OO0O0O0O0O00OOOO0 =re .findall ('<ul><li>(.*?)</li>',OOOO00OO0000OO0OO )[0 ][:3 ]#line:424
            O0O000OOOO0O000OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0O0O0O00OOOO0}').json ()#line:425
            O0OOOO0000O0000OO =O0O000OOOO0O000OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            O000O0OOOOO0O000O ={"nickname":O0OOOO0000O0000OO }#line:427
            OOO00OOO0OOOO00OO =f'_nickname={O0OOOO0000O0000OO}_{O0O000O0OO00OOO0O}'#line:428
            OO00000O000O0OOOO ={'source':'scsc','authorization':OO0O0OOOOOOO00O00 .token ,'timestamp':O0O000O0OO00OOO0O ,'sign':sign (OOO00OOO0OOOO00OO ),'signstring':OOO00OOO0OOOO00OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO0O0000O000000O0 =requests .request ('patch',f'{host}/user/nickname',headers =OO00000O000O0OOOO ,data =O000O0OOOOO0O000O ).json ()#line:440
            if 'status'in OO0O0000O000000O0 :#line:442
                if OO0O0000O000000O0 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O0OOOO0000O0000OO}丨{OO0O0000O000000O0["message"]}')#line:444
        except Exception as O0OOO0O0O00OOO00O :#line:445
            print (O0OOO0O0O00OOO00O )#line:446
    def withdraw (O00OOOO0O00O0O000 ):#line:449
        try :#line:450
            O0000O0O00OOOOO0O =f'__{timi_new()}'#line:451
            O0O0OO00000OOO0OO ={'source':'scsc','authorization':O00OOOO0O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O00OOOOO0O ),'signstring':O0000O0O00OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOOO0OOOOOO00O0OO =requests .request ('get',f'{host}/assets',headers =O0O0OO00000OOO0OO ).json ()#line:463
            if 'status'in OOOO0OOOOOO00O0OO :#line:465
                if OOOO0OOOOOO00O0OO ['status']==200 :#line:466
                    OOO0OO0OOO0OO0000 =OOOO0OOOOOO00O0OO ['data']['cash']#line:467
                    if float (OOO0OO0OOO0OO0000 )>20 :#line:468
                        O0000O0O00OOOOO0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O0O0OO00000OOO0OO ={'authorization':O00OOOO0O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O00OOOOO0O ),'signstring':O0000O0O00OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OOOOOOO0OO0OOOOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OO0O000O0OO00OOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO00000OOO0OO ,data =OOOOOOO0OO0OOOOOO ).json ()#line:482
                        if 'status'in OO0O000O0OO00OOOO :#line:484
                            if OO0O000O0OO00OOOO ['status']==200 :#line:485
                                print (f'【余额提现】:{OO0O000O0OO00OOOO["data"]}')#line:486
                        if 'status'in OO0O000O0OO00OOOO :#line:487
                            if OO0O000O0OO00OOOO ['status']==500 :#line:488
                                print (f'【余额提现】:{OO0O000O0OO00OOOO["message"]}')#line:489
        except Exception as OOOO000O0OO000OO0 :#line:490
            print (OOOO000O0OO000OO0 )#line:491
    def invitenum (O0O00OO000OOO000O ):#line:494
        global invited_new #line:495
        try :#line:496
            OO0000OO00OO000O0 =f'__{timi_new()}'#line:497
            OOOO000OOOOO00000 ={'source':'scsc','authorization':O0O00OO000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO00OO000O0 ),'signstring':OO0000OO00OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            O00OOO0OO0OO0OOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO000OOOOO00000 ).json ()#line:509
            if 'status'in O00OOO0OO0OO0OOO0 :#line:511
                if O00OOO0OO0OO0OOO0 ['status']==200 :#line:512
                    O0OOO00OOO000OOO0 =O00OOO0OO0OO0OOO0 ['data']['invited_count']#line:513
                    O000O0OOOOO000O0O =O00OOO0OO0OO0OOO0 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{O0OOO00OOO000OOO0}丨间邀好友:{O000O0OOOOO000O0O}')#line:515
                    if O0OOO00OOO000OOO0 <2 :#line:516
                        OO000O0OO0O00O0O0 =f'__{timi_new()}'#line:517
                        OO0OOO0OOO0O0OOOO ={'source':'scsc','authorization':O0O00OO000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OO0O00O0O0 ),'signstring':OO000O0OO0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OO00000OO0O00OOOO =requests .request ('get',f'{host}/user',headers =OO0OOO0OOO0O0OOOO ).json ()#line:529
                        if 'status'in OO00000OO0O00OOOO :#line:531
                            if OO00000OO0O00OOOO ['status']==200 :#line:532
                                invited_new .append (OO00000OO0O00OOOO ['data']['inner_id'])#line:533
        except Exception as OO0O0OO00O0000O00 :#line:534
            print (OO0O0OO00O0000O00 )#line:535
    def game_map (OOOO000O0000O0O00 ):#line:538
        try :#line:539
            O00OOOO0OO00O00OO =f'__{timi_new()}'#line:540
            OO00O0O0OO00OO000 ={'source':'scsc','authorization':OOOO000O0000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0OO00O00OO ),'signstring':O00OOOO0OO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O0O000000O0O00000 =requests .request ('get',f'{host}/game/map',headers =OO00O0O0OO00OO000 ).json ()#line:552
            if 'status'in O0O000000O0O00000 :#line:554
                if O0O000000O0O00000 ['status']==200 :#line:555
                    for OO0OO00OO000O000O in O0O000000O0O00000 ['data']['list'][0 ]['crops']:#line:556
                        O0OOOOO000OO00O00 =OO0OO00OO000O000O ['level']#line:558
                        if O0OOOOO000OO00O00 ==41 :#line:559
                            OO0000O0O0OO0O0OO =OO0OO00OO000O000O ['crop_name']#line:560
                            OOOOOO000O00OO0OO =OO0OO00OO000O000O ['count']#line:561
                            if OOOOOO000O00OO0OO >0 :#line:562
                                print (f'【农业资产】:{OO0000O0O0OO0O0OO}丨数量:{OOOOOO000O00OO0OO}')#line:563
                                O0OOOO0OO00O0O000 =OOOO000O0000O0O00 .the_query ()#line:564
                                OOOO000O0000O0O00 .market_sale (O0OOOO0OO00O0O000 )#line:565
        except Exception as OO00O00OO000OO000 :#line:566
            print (OO00O00OO000OO000 )#line:567
    def give_gold (OOOO0O000OOOO0OOO ):#line:570
        try :#line:571
            O0O0O0000OOOO0O0O =f'__{timi_new()}'#line:572
            OO00OOOO00O0OO00O ={'source':'scsc','authorization':OOOO0O000OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OOOO0O0O ),'signstring':O0O0O0000OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OO0O0000OOO00OOO0 =requests .request ('get',f'{host}/user',headers =OO00OOOO00O0OO00O ).json ()#line:584
            if 'status'in OO0O0000OOO00OOO0 :#line:585
                if OO0O0000OOO00OOO0 ['status']==200 :#line:586
                    if float (OOOO0O000OOOO0OOO .doneeNo )!=0 :#line:587
                        OO00OO00000OOOOO0 =OO0O0000OOO00OOO0 ['data']['assets']['gold']#line:588
                        if float (OO00OO00000OOOOO0 )>float (OOOO0O000OOOO0OOO .innerId ):#line:589
                            OO0O0O000OOO000OO =int (float (OO00OO00000OOOOO0 )/1.1 )#line:590
                            O0O0O0000OOOO0O0O =f'_doneeNo={OOOO0O000OOOO0OOO.doneeNo}&quantity={OO0O0O000OOO000OO}_{timi_new()}'#line:591
                            OO00OOOO00O0OO00O ={'source':'scsc','authorization':OOOO0O000OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OOOO0O0O ),'signstring':O0O0O0000OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OO0O00OO000OOOO0O ={"quantity":OO0O0O000OOO000OO ,"doneeNo":OOOO0O000OOOO0OOO .doneeNo }#line:606
                            O0O0000000OO00O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OO00OOOO00O0OO00O ,data =OO0O00OO000OOOO0O ).json ()#line:607
                            if 'status'in O0O0000000OO00O00 :#line:609
                                if O0O0000000OO00O00 ['status']==200 :#line:610
                                    if O0O0000000OO00O00 ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OO0O0O000OOO000OO}种子给{OOOO0O000OOOO0OOO.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OO00O000OO00OO0O0 :#line:615
            print (OO00O000OO00OO0O0 )#line:616
    def invitation (O00OO0O0O0O0OOO00 ):#line:618
        try :#line:619
            _O00O0O0OO0OO0OOO0 =float (bundled_def ())/4 #line:620
            OOO0O000O000O000O =f'_innerId={int(_O00O0O0OO0OO0OOO0)}_{timi_new()}'#line:622
            O0O0OOOOOO0O000O0 ={'source':'scsc','authorization':O00OO0O0O0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O000O000O ),'signstring':OOO0O000O000O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            O00O000OOOO0O0O00 ={"innerId":int (_O00O0O0OO0OO0OOO0 )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OOOOOO0O000O0 ,data =O00O000OOOO0O0O00 )#line:635
        except Exception as O000OOO000OOO0OOO :#line:636
            print (O000OOO000OOO0OOO )#line:637
    def winning_rewards (O000OOOOO0OOO00O0 ):#line:640
        try :#line:641
            O0OO00000O0O0OO00 =f'__{timi_new()}'#line:642
            O0OOO0OOO0OOO00O0 ={'source':'scsc','authorization':O000OOOOO0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000O0O0OO00 ),'signstring':O0OO00000O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OO00000O0OO00OOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO0OOO0OOO00O0 ).json ()#line:654
            if 'status'in OO00000O0OO00OOOO :#line:656
                if OO00000O0OO00OOOO ['status']==200 :#line:657
                    if OO00000O0OO00OOOO ['data']['amount']:#line:658
                        OOOO000O0O000OOOO =OO00000O0OO00OOOO ['data']['amount']['gold']#line:659
                        return OOOO000O0O000OOOO #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OO0OO000O0OOOOO00 :#line:663
            print (OO0OO000O0OOOOO00 )#line:664
    def certification (O000O00OOOOO0O000 ):#line:667
        try :#line:668
            OO0000O0O0OO00O0O =f'__{timi_new()}'#line:669
            OO0OO0O0O000O00OO ={'source':'scsc','authorization':O000O00OOOOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O0OO00O0O ),'signstring':OO0000O0O0OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            OO0O0000OO00000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OO0O0O000O00OO ).json ()#line:681
            if 'status'in OO0O0000OO00000O0 :#line:683
                if OO0O0000OO00000O0 ['status']==200 :#line:684
                    if OO0O0000OO00000O0 ['data']['result']:#line:685
                        O0O0000OOO0000O00 =OO0O0000OO00000O0 ['data']['nick_name']#line:686
                        return O0O0000OOO0000O00 #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0O00O0000OO0000O :#line:690
            print (O0O00O0000OO0000O )#line:691
    def crops_illustrated (OOOOOO0O00O0OO0O0 ):#line:694
        try :#line:695
            OOO0O0000OO00O00O =f'__{timi_new()}'#line:696
            O00OO0OOO0O000000 ={'source':'scsc','authorization':OOOOOO0O00O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OO00O00O ),'signstring':OOO0O0000OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O00000O00000OO000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OO0OOO0O000000 ).json ()#line:708
            if 'status'in O00000O00000OO000 :#line:710
                if O00000O00000OO000 ['status']==200 :#line:711
                    OO0O00O0OOO0OOOO0 =O00000O00000OO000 ['data'][0 ]['crops']#line:712
                    for OOO0OOOOO0O0O0O00 in OO0O00O0OOO0OOOO0 :#line:713
                        if OOO0OOOOO0O0O0O00 ['ill_clover_award']:#line:714
                            if float (OOO0OOOOO0O0O0O00 ['ill_clover_award'])>1 :#line:715
                                if OOO0OOOOO0O0O0O00 ['is_finish']:#line:716
                                    if not OOO0OOOOO0O0O0O00 ['is_getit']:#line:717
                                        if OOOOOO0O00O0OO0O0 .certification ()!='未实名':#line:718
                                            OOO0O0000OO00O00O =f'_award_level={OOO0OOOOO0O0O0O00["level"]}_{timi_new()}'#line:719
                                            O00OO0OOO0O000000 ={'source':'scsc','authorization':OOOOOO0O00O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OO00O00O ),'signstring':OOO0O0000OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            OO000O0O000OOOOOO ={"award_level":OOO0OOOOO0O0O0O00 ['level']}#line:731
                                            OOO000O0000OOOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OO0OOO0O000000 ,json =OO000O0O000OOOOOO ).json ()#line:733
                                            if 'status'in OOO000O0000OOOOO0 :#line:734
                                                if OOO000O0000OOOOO0 ['status']==200 :#line:735
                                                    O00O00OOOOOOOO000 =OOO000O0000OOOOO0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{OOO0OOOOO0O0O0O00["crop_name"]}成就丨奖励{O00O00OOOOOOOO000}☘️')#line:738
                                                if OOO000O0000OOOOO0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OOO000O0000OOOOO0["message"]}')#line:740
        except Exception as OOO0OO0000OO0OO0O :#line:741
            print (OOO0OO0000OO0OO0O )#line:742
    def watched_ad (O0000000OO000OOO0 ):#line:745
        try :#line:746
            OOOOOOO0OOOO0O0O0 =f'__{timi_new()}'#line:747
            OO0OOOO00OO0OOOOO ={'source':'scsc','authorization':O0000000OO000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOOO0O0O0 ),'signstring':OOOOOOO0OOOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OOO00O0O0OO0OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOO00OO0OOOOO ).json ()#line:759
            if 'status'in OOO00O0O0OO0OO0OO :#line:761
                if OOO00O0O0OO0OO0OO ['status']==200 :#line:762
                    if 'offlineInfo'in OOO00O0O0OO0OO0OO ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OOOOOO0O0O0OO00OO =OOO00O0O0OO0OO0OO ['data']['offlineInfo']['off_minute']#line:765
                        O0OOOOO0O0OO00OO0 =float (OOO00O0O0OO0OO0OO ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OOOO00OO0OOOOO ).json ()#line:768
                        time .sleep (2 )#line:769
                        OOO0OO0OO00O0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOO00OO0OOOOO ).json ()#line:770
                        if 'status'in OOO0OO0OO00O0OO00 :#line:772
                            if OOO0OO0OO00O0OO00 ['status']==200 :#line:773
                                O0O00O00000OOOOO0 =float (OOO0OO0OO00O0OO00 ['data']['silver'])/1000000000000 #line:774
                                O0OO0O00O00O0O000 =str (O0O00O00000OOOOO0 -O0OOOOO0O0OO00OO0 )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OOOOOO0O0O0OO00OO}分钟奖励🌱数量:{O0OO0O00O00O0O000}t粒')#line:776
        except Exception as OOO0O00O0O00O0OO0 :#line:777
            print (OOO0O00O0O00O0OO0 )#line:778
    def user_ad (OOO00000000O000OO ):#line:781
        try :#line:782
            O00OOO000O0O0OOOO =f'__{timi_new()}'#line:783
            O0O00O0O000OO0O0O ={'source':'scsc','authorization':OOO00000000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000O0O0OOOO ),'signstring':O00OOO000O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            OOOOOO00O00OOOOO0 =requests .request ('get',f'{host}/user/ad',headers =O0O00O0O000OO0O0O ).json ()#line:795
            if 'status'in OOOOOO00O00OOOOO0 :#line:797
                if OOOOOO00O00OOOOO0 ['status']==200 :#line:798
                    OOOOO0O0OOO00OO00 =OOOOOO00O00OOOOO0 ['data']['max_time']#line:799
                    OO00O0O0O0O0O0O0O =OOOOOO00O00OOOOO0 ['data']['watch_time']#line:800
                    O00OO00OO0O00000O =OOOOOO00O00OOOOO0 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O00OO00OO0O00000O + OOOOO0O0OOO00OO00 - OO00O0O0O0O0O0O0O}次丨好友提供:{O00OO00OO0O00000O}次')#line:802
                    if O00OO00OO0O00000O +OOOOO0O0OOO00OO00 -OO00O0O0O0O0O0O0O >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OOOO00OOOO0000OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00O0O000OO0O0O ).json ()#line:805
                        if 'status'in OOOO00OOOO0000OO0 :#line:807
                            if OOOO00OOOO0000OO0 ['status']==200 :#line:808
                                OO0000OO0O0O00OOO =float (OOOO00OOOO0000OO0 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OO0000OO0O0O00OOO)}t粒')#line:810
                                return True #line:811
                            if OOOO00OOOO0000OO0 ['status']==500 :#line:812
                                OOO0000OO000OOOOO =OOOO00OOOO0000OO0 ['message']#line:813
                                print (f'【获取种子】:{OOO0000OO000OOOOO}')#line:814
                                return False #line:815
        except Exception as O0O0OOO00OOOOOOOO :#line:816
            print (O0O0OOO00OOOOOOOO )#line:817
    def synthetic (OOOOOO000O000O00O ):#line:820
        global id ,g #line:821
        try :#line:822
            OO0OO0O0OO0OO000O =OOOOOO000O000O00O .level_new ()#line:823
            O0O00OO0OO0O0OO0O =random .randint (9 ,11 )#line:824
            OOO0OO00OOOOOO000 =f'_site=8&targetSite={O0O00OO0OO0O0OO0O}_{timi_new()}'#line:825
            OO0O00O00000000O0 ={'source':'scsc','authorization':OOOOOO000O000O00O .token ,'timestamp':timi_new (),'sign':sign (OOO0OO00OOOOOO000 ),'signstring':OOO0OO00OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OOO00000OOOO0OOO0 ={"site":int (8 ),"targetSite":int (O0O00OO0OO0O0OO0O )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00O00000000O0 ,json =OOO00000OOOO0OOO0 )#line:838
            while True :#line:839
                O0000OOOOO000O0OO =f'__{timi_new()}'#line:840
                OOOOOO0O0O000OO00 ={'source':'scsc','authorization':OOOOOO000O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO000O0OO ),'signstring':O0000OOOOO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O00OO0000O0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO0O0O000OO00 ).json ()#line:852
                if 'status'in O00OO0000O0OOO000 :#line:854
                    if O00OO0000O0OOO000 ['status']==200 :#line:855
                        O0OO0OO000O0O0OOO =O00OO0000O0OOO000 ['data']['cropList']#line:856
                        O00000000O0O0OOO0 =O00OO0000O0OOO000 ['data']['gameCoreDataDBid']#line:857
                        O0OO00OOO0OO0OOOO =float (O00OO0000O0OOO000 ['data']['silver'])/1000000000000 #line:858
                        OOOOO0000000O00OO =0 #line:863
                        for O00OO0O000O0OO0OO in O0OO0OO000O0O0OOO :#line:864
                            if not O00OO0O000O0OO0OO :#line:865
                                OOOOO0O00000OO00O =f'_crop_id={O00000000O0O0OOO0}&site={OOOOO0000000O00OO}_{OOOOOO000O000O00O.time}'#line:866
                                OO0O00OO0O0000OOO ={'source':'scsc','authorization':OOOOOO000O000O00O .token ,'timestamp':OOOOOO000O000O00O .time ,'sign':sign (OOOOO0O00000OO00O ),'signstring':OOOOO0O00000OO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                OO0000OOO0OO00OOO ={"site":OOOOO0000000O00OO ,"crop_id":O00000000O0O0OOO0 }#line:877
                                OOOOOOOO000O0O0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O00OO0O0000OOO ,data =OO0000OOO0OO00OOO ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOOOOOOO000O0O0OO :#line:881
                                    if OOOOOOOO000O0O0OO ['status']==200 :#line:882
                                        if OOOOOOOO000O0O0OO ['message']=='种子数量不足':#line:883
                                            OO0OO0O0OO0OO000O =OOOOOO000O000O00O .level_new ()#line:884
                                            print (f'【种植合成】:{OOOOOOOO000O0O0OO["message"]}')#line:885
                                            if not OOOOOO000O000O00O .user_ad ():#line:886
                                                return False #line:887
                                    if OOOOOOOO000O0O0OO ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOOOOOOO000O0O0OO["message"]}')#line:889
                                        return False #line:890
                            OOOOO0000000O00OO +=1 #line:891
                        O00O000O00000OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO0O0O000OO00 ).json ()#line:892
                        O00O0OOO000OO0O00 =O00O000O00000OOOO ['data']['cropList']#line:893
                        OO000O0000O000000 =False #line:894
                        for O00OO0O000O0OO0OO in range (12 ):#line:895
                            id =O00O0OOO000OO0O00 [O00OO0O000O0OO0OO ]['level']#line:896
                            if float (OO0OO0O0OO0OO000O )-float (id )>9 :#line:897
                                O0OO0O000000O0OOO =f'_site={O00OO0O000O0OO0OO}_{timi_new()}'#line:898
                                OOO00OO0OOO0OO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOO000O000O00O .token ,'timestamp':timi_new (),'sign':sign (O0OO0O000000O0OOO ),'signstring':O0OO0O000000O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O00OOO000OOOO0OOO ={"site":O00OO0O000O0OO0OO }#line:910
                                OO0OO0000O0O0OO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO00OO0OOO0OO0OO ,data =O00OOO000OOOO0OOO ).json ()#line:912
                                if 'status'in OO0OO0000O0O0OO00 :#line:913
                                    if OO0OO0000O0O0OO00 ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OO000O00O00OOO0OO in range (11 ):#line:917
                                    O0000O0OO0000O000 =OO000O00O00OOO0OO +1 #line:918
                                    g =O00O0OOO000OO0O00 [O0000O0OO0000O000 ]['level']#line:919
                                    if id ==g :#line:920
                                        OO0O0000000OOO000 =OO000O00O00OOO0OO +2 #line:921
                                        if OO0O0000000OOO000 !=O00OO0O000O0OO0OO +1 :#line:922
                                            O0000O0O0O0O0OO00 =O00OO0O000O0OO0OO +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            OOO0OO00OOOOOO000 =f'_site={O0000O0O0O0O0OO00 - 1}&targetSite={OO0O0000000OOO000 - 1}_{timi_new()}'#line:926
                                            OO0O00O00000000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOO000O000O00O .token ,'timestamp':timi_new (),'sign':sign (OOO0OO00OOOOOO000 ),'signstring':OOO0OO00OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            O0OOO000O00OOO0O0 ={"site":int (O0000O0O0O0O0OO00 -1 ),"targetSite":int (OO0O0000000OOO000 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00O00000000O0 ,json =O0OOO000O00OOO0O0 )#line:945
                                            OO000O0000O000000 =True #line:947
                                    if OO000O0000O000000 :#line:948
                                        break #line:949
                                if OO000O0000O000000 :#line:950
                                    break #line:951
        except :#line:952
            OOOOOO000O000O00O .synthetic ()#line:953
    def level_new (OOOOO00OOOO0000OO ):#line:956
        try :#line:957
            O000000000000O000 =f'__{timi_new()}'#line:958
            OOO0OOOOOOO000O00 ={'source':'scsc','authorization':OOOOO00OOOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000000000O000 ),'signstring':O000000000000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            OO0O00OOOOOOOO0OO =requests .request ('get',f'{host}/user',headers =OOO0OOOOOOO000O00 ).json ()#line:970
            if 'status'in OO0O00OOOOOOOO0OO :#line:971
                if OO0O00OOOOOOOO0OO ['status']==200 :#line:972
                    return float (OO0O00OOOOOOOO0OO ['data']['level'])#line:973
        except Exception as OOO0OOOOOO00O0O0O :#line:974
            print (OOO0OOOOOO00O0O0O )#line:975
    def propsraffle (OO0OOO0OO0OO0O0OO ):#line:978
        try :#line:979
            while True :#line:980
                O0OO00O0OOOOO0OO0 =f'__{timi_new()}'#line:981
                OO0000OOO0O0O00OO ={'source':'scsc','authorization':OO0OOO0OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OOOOO0OO0 ),'signstring':O0OO00O0OOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                O00O00OO000O00OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0000OOO0O0O00OO ).json ()#line:993
                if 'status'in O00O00OO000O00OOO :#line:995
                    if O00O00OO000O00OOO ['status']==200 :#line:996
                        OOOO00OOOOOO0OO0O =O00O00OO000O00OOO ['data']['rows']#line:997
                        O0000O0O00O00000O =O00O00OO000O00OOO ['data']['vstate']#line:998
                        if OOOO00OOOOOO0OO0O ==5 or OOOO00OOOOOO0OO0O ==6 or OOOO00OOOOOO0OO0O ==7 :#line:999
                            O00OO0O00OOO0O000 =O00O00OO000O00OOO ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O00OO0O00OOO0O000}')#line:1001
                        if OOOO00OOOOOO0OO0O ==1 or OOOO00OOOOOO0OO0O ==2 or OOOO00OOOOOO0OO0O ==3 :#line:1002
                            O0O000OOOOOOOOO0O =O00O00OO000O00OOO ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{O0O000OOOOOOOOO0O}')#line:1004
                        if OOOO00OOOOOO0OO0O ==4 or OOOO00OOOOOO0OO0O ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OOOO00OOOOOO0OO0O =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OO00OO00O0OO0O :#line:1046
            print (OO0OO00OO00O0OO0O )#line:1047
    def friends_invitation (OOO0OOO0O0O0O000O ):#line:1050
        try :#line:1051
            OO0O00O00OO00O0OO =f'__{timi_new()}'#line:1052
            O0OO00O0OOOOO0O00 ={'source':'scsc','authorization':OOO0OOO0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OO00O0OO ),'signstring':OO0O00O00OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O0OO0OOO0OOO0OOO0 =requests .request ('get',f'{host}/friends',headers =O0OO00O0OOOOO0O00 ).json ()#line:1064
            if 'status'in O0OO0OOO0OOO0OOO0 :#line:1065
                if O0OO0OOO0OOO0OOO0 ['status']==200 :#line:1066
                    OOO0OOO00O0OO0O0O =O0OO0OOO0OOO0OOO0 ['data']['myInviteter']#line:1067
                    if OOO0OOO00O0OO0O0O :#line:1068
                        O0OOO000000O000OO =OOO0OOO00O0OO0O0O ['user']['nickname']#line:1069
                        O0OO0OO00OOOO0O00 =OOO0OOO0O0O0O000O .certification ()#line:1070
                        if O0OO0OO00OOOO0O00 =='未实名':#line:1071
                            weishim .append (OOO0OOO0O0O0O000O .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O0OOO000000O000OO}丨实名:{O0OO0OO00OOOO0O00}')#line:1073
        except Exception as OO0OOO0O0OO00OOOO :#line:1077
            print (OO0OOO0O0OO00OOOO )#line:1078
    def add_clover (O00000O0OO0O000O0 ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O00O0OOO00000O000 =f'__{timi_new()}'#line:1084
            O00OO00O0O0000O0O ={'source':'scsc','authorization':O00000O0OO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO00000O000 ),'signstring':O00O0OOO00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OOO0000O00O0O00O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00OO00O0O0000O0O ).json ()#line:1096
            if 'status'in OOO0000O00O0O00O0 :#line:1098
                if OOO0000O00O0O00O0 ['status']==200 :#line:1099
                    OO0OOO000OO0OOOO0 =OOO0000O00O0O00O0 ['data']['clover']#line:1100
                    OOOO0000O0O000OO0 =OOO0000O00O0O00O0 ['data']['used_clover']#line:1101
                    OOOOO0O0O00OO0OOO =float (OO0OOO000OO0OOOO0 )-float (OOOO0000O0O000OO0 )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOO0000O0O000OO0}')#line:1103
                    if O00000O0OO0O000O0 .certification ()!='未实名':#line:1104
                        if OOOOO0O0O00OO0OOO >1 :#line:1105
                            O00O0OOO00000O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOO0O0O00OO0OOO)}_{timi_new()}'#line:1106
                            OOOOO0O000OOOOO00 ={'source':'scsc','authorization':O00000O0OO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO00000O000 ),'signstring':O00O0OOO00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OO00OOOO00OOOOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOO0O0O00OO0OOO )}#line:1118
                            OO0OOO0O00O0O0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO0O000OOOOO00 ,data =OO00OOOO00OOOOO00 ).json ()#line:1119
                            if 'status'in OO0OOO0O00O0O0OOO :#line:1121
                                if OO0OOO0O00O0O0OOO ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{OO0OOO0O00O0O0OOO["data"]["isSuccess"]}丨数量:{OOOOO0O0O00OO0OOO}')#line:1123
                                if OO0OOO0O00O0O0OOO ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{OO0OOO0O00O0O0OOO["message"]}')#line:1125
            OO0OO000OO0OO0000 =requests .request ('get',f'{host}/lottery',headers =O00OO00O0O0000O0O ).json ()#line:1126
            O00OOOOOO000OO0O0 =O00000O0OO0O000O0 .winning_rewards ()#line:1128
            if 'status'in OO0OO000OO0OO0000 :#line:1129
                if OO0OO000OO0OO0000 ['status']==200 :#line:1130
                    O000O00OOO0OOO00O =OO0OO000OO0OO0000 ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (O000O00OOO0OOO00O )#line:1132
                    O0OO0000O0O0O00OO =OO0OO000OO0OO0000 ['data'][1 ]['value']#line:1133
                    O0OOO0OOOO0O0O00O =OO0OO000OO0OO0000 ['data'][0 ]['join_number']#line:1134
                    O0OO0OOO00000OOO0 =int (float (OO0OO000OO0OO0000 ['data'][0 ]['totalValue']))#line:1135
                    O00OOO0OOOO000000 =float (O0OO0000O0O0O00OO /O0OO0OOO00000OOO0 )*10000 #line:1136
                    OOO0O0O00O0OO0OOO =O0OO0OOO00000OOO0 /O0OOO0OOOO0O0O00O #line:1137
                    print (f'【参与抽奖】:预计每天中{str(O000O00OOO0OOO00O)[:6]}颗金种子丨好友收益:{str(O00OOOOOO000OO0O0)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(O00OOO0OOOO000000)[:6]}颗金种子丨☘️人均:{str(OOO0O0O00O0OO0OOO)[:7]}️')#line:1139
        except Exception as O0000O0O0OOOOO00O :#line:1140
            print (O0000O0O0OOOOO00O )#line:1141
    def energy (OOOO000O00O0OOO00 ):#line:1144
        try :#line:1145
            while True :#line:1146
                O000OO00O0O000O0O =f'__{timi_new()}'#line:1147
                OOO0OOO0OOO0O0000 ={'source':'scsc','authorization':OOOO000O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O0O000O0O ),'signstring':O000OO00O0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                O00O0O00O00OOO00O =requests .request ('get',f'{host}/energy/general',headers =OOO0OOO0OOO0O0000 ).json ()#line:1159
                if 'status'in O00O0O00O00OOO00O :#line:1161
                    if O00O0O00O00OOO00O ['status']==200 :#line:1162
                        O00OOO0O0OO00OOOO =O00O0O00O00OOO00O ['data']['ordinary_water']#line:1163
                        O0000O00OO0OOO00O =O00O0O00O00OOO00O ['data']['ordinary_fertilizer']#line:1164
                        O00O0O000OO0O000O =O00O0O00O00OOO00O ['data']['videoStatus']#line:1165
                        OOOO000OO000OOO0O =O00O0O00O00OOO00O ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0000O00OO0OOO00O).split(".")[0]}丨水滴:{str(O00OOO0O0OO00OOOO).split(".")[0]}')#line:1168
                        if float (O0000O00OO0OOO00O )<96 :#line:1169
                            if O00O0O000OO0O000O :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OO00000OO0OO0OO0O =99 -float (O0000O00OO0OOO00O )#line:1172
                                O0OOOO0O00000O0OO ={"fertilizer":str (OO00000OO0OO0OO0O ).split ('.')[0 ]}#line:1173
                                O0OO0O00OOOOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO0OOO0OOO0O0000 ).json ()#line:1175
                                if 'status'in O0OO0O00OOOOO00O0 :#line:1177
                                    if O0OO0O00OOOOO00O0 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0O00OOOOO00O0["message"]}')#line:1179
                                    if O0OO0O00OOOOO00O0 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0O00OOOOO00O0["message"]}')#line:1181
                                        break #line:1182
                                if float (O0000O00OO0OOO00O )<78 :#line:1184
                                    OO00000OO0OO0OO0O =80 -float (O0000O00OO0OOO00O )#line:1185
                                    OO000O0000O0O000O =f'_fertilizer={int(OO00000OO0OO0OO0O)}_{timi_new()}'#line:1186
                                    OOO0OOOOO0OOOOOO0 ={'source':'scsc','authorization':OOOO000O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0000O0O000O ),'signstring':OO000O0000O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    O00000O0OOO0O0O0O ={"fertilizer":int (OO00000OO0OO0OO0O )}#line:1198
                                    OOO0OOO00O00O0O00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0OOOOO0OOOOOO0 ,data =O00000O0OOO0O0O0O ).json ()#line:1200
                                    if 'status'in OOO0OOO00O00O0O00 :#line:1202
                                        if OOO0OOO00O00O0O00 ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OOO0OOO00O00O0O00["message"]}丨数量:{int(OO00000OO0OO0OO0O)}')#line:1204
                                        if OOO0OOO00O00O0O00 ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OOO0OOO00O00O0O00["message"]}丨数量:{int(OO00000OO0OO0OO0O)}')#line:1206
                                            O00OOOOO000OO00O0 =OOO0OOO00O00O0O00 ["message"].split ('-')[1 ]#line:1207
                                            OOOOO0OO0O0O0OO00 =f'__{timi_new()}'#line:1208
                                            O000O000O000O0OO0 ={'source':'scsc','authorization':OOOO000O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0O0O0OO00 ),'signstring':OOOOO0OO0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OO0O0OO0O0OOOOOO0 =requests .request ('get',f'{host}/user',headers =O000O000O000O0OO0 ).json ()#line:1220
                                            if 'status'in OO0O0OO0O0OOOOOO0 :#line:1221
                                                if OO0O0OO0O0OOOOOO0 ['status']==200 :#line:1222
                                                    O00O0OO0O0O00O000 =OO0O0OO0O0OOOOOO0 ['data']['inner_id']#line:1223
                                                    if give_gold (O00O0OO0O0O00O000 ,float (O00OOOOO000OO00O0 )+1 ):#line:1224
                                                        OOOO000O00O0OOO00 .energy ()#line:1225
                        if float (O00OOO0O0OO00OOOO )<880 :#line:1226
                            if OOOO000OO000OOO0O :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                O000000OOOOO00000 =999 -float (O00OOO0O0OO00OOOO )#line:1229
                                O0000O0OO0OOOOOOO ={"water":str (O000000OOOOO00000 ).split ('.')[0 ]}#line:1230
                                OOOO0O00O0OO0O00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO0OOO0OOO0O0000 ).json ()#line:1232
                                if 'status'in OOOO0O00O0OO0O00O :#line:1234
                                    if OOOO0O00O0OO0O00O ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O00O0OO0O00O["message"]}')#line:1236
                                    if OOOO0O00O0OO0O00O ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O00O0OO0O00O["message"]}')#line:1238
                                        break #line:1239
                                if float (O00OOO0O0OO00OOOO )<780 :#line:1240
                                    O000000OOOOO00000 =800 -float (O00OOO0O0OO00OOOO )#line:1241
                                    OOO0OOOOOO000OO0O =f'_water={int(O000000OOOOO00000)}_{timi_new()}'#line:1242
                                    OOO0O0O00OO0O00OO ={'source':'scsc','authorization':OOOO000O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOO000OO0O ),'signstring':OOO0OOOOOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O0OO0O00000O0O0OO ={"water":int (O000000OOOOO00000 )}#line:1254
                                    O0OO0OOO0OO00OO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO0O0O00OO0O00OO ,data =O0OO0O00000O0O0OO ).json ()#line:1256
                                    if 'status'in O0OO0OOO0OO00OO0O :#line:1258
                                        if O0OO0OOO0OO00OO0O ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O0OO0OOO0OO00OO0O["message"]}丨数量:{int(O000000OOOOO00000)}')#line:1260
                                        if O0OO0OOO0OO00OO0O ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O0OO0OOO0OO00OO0O["message"]}丨数量:{int(O000000OOOOO00000)}')#line:1262
                                            O00OOOOO000OO00O0 =O0OO0OOO0OO00OO0O ["message"].split ('-')[1 ]#line:1263
                                            OOOOO0OO0O0O0OO00 =f'__{timi_new()}'#line:1264
                                            O000O000O000O0OO0 ={'source':'scsc','authorization':OOOO000O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0O0O0OO00 ),'signstring':OOOOO0OO0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OO0O0OO0O0OOOOOO0 =requests .request ('get',f'{host}/user',headers =O000O000O000O0OO0 ).json ()#line:1276
                                            if 'status'in OO0O0OO0O0OOOOOO0 :#line:1277
                                                if OO0O0OO0O0OOOOOO0 ['status']==200 :#line:1278
                                                    O00O0OO0O0O00O000 =OO0O0OO0O0OOOOOO0 ['data']['inner_id']#line:1279
                                                    if give_gold (O00O0OO0O0O00O000 ,float (O00OOOOO000OO00O0 )+1 ):#line:1280
                                                        OOOO000O00O0OOO00 .energy ()#line:1281
                        break #line:1282
        except Exception as OO0O0O0O0OO0O0000 :#line:1283
            print (OO0O0O0O0OO0O0000 )#line:1284
def bundled_def ():#line:1287
    O0000OOO0O00O0O00 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return O0000OOO0O00O0O00 [random .randint (0 ,len (O0000OOO0O00O0O00 )-1 )]#line:1289
def version_of_the_validation ():#line:1293
    return str ((105 -56 )/10 )#line:1294
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
        OOO0OOOOOOOOO0OO0 =gitee_edition ()#line:1328
        if version_of_the_validation ()<OOO0OOOOOOOOO0OO0 ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOOOOOOOO0OO0["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{OOO0OOOOOOOOO0OO0["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOOOOOOOO0OO0["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {OOO0OOOOOOOOO0OO0["CityEarth"]["content"]}')#line:1334
    except Exception as OO0000O00OO0000OO :#line:1335
        print (OO0000O00OO0000OO )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
