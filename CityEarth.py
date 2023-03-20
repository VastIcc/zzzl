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
@ 版本  4.7
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.4195543111'#line:1
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
        O0000O00000000O00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0000O00000000O00)}个账号==========")#line:17
        for O0O00OOO000O0OO00 in O0000O00000000O00 :#line:18
            OOOOOOO0O00OO0OOO =[]#line:19
            print (f"------------正在执行第{O0000O00000000O00.index(O0O00OOO000O0OO00) + 1}个账号------------")#line:20
            OO0OO00OO0O00O0OO =CityEarth (O0O00OOO000O0OO00 ,OOOOOOO0O00OO0OOO ,O0000O00000000O00 .index (O0O00OOO000O0OO00 ))#line:21
            def OOO00OOOOO00O0OOO ():#line:23
                if OO0OO00OO0O00O0OO .base_info ():#line:25
                    OO0OO00OO0O00O0OO .sealing ()#line:27
                    OO0OO00OO0O00O0OO .invitenum ()#line:29
                    OO0OO00OO0O00O0OO .query_to_sell ()#line:31
                    OO0OO00OO0O00O0OO .friends_invitation ()#line:35
                    OO0OO00OO0O00O0OO .energy ()#line:37
                    OO0OO00OO0O00O0OO .add_clover ()#line:39
                    OO0OO00OO0O00O0OO .propsraffle ()#line:41
                    OO0OO00OO0O00O0OO .synthetic ()#line:43
                    OO0OO00OO0O00O0OO .crops_illustrated ()#line:45
                    OO0OO00OO0O00O0OO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0OO00OO0O00O0OO .give_gold ()#line:50
            O0O00O0O000O0OO0O =threading .Thread (target =OOO00OOOOO00O0OOO )#line:52
            O0O00O0O000O0OO0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O00O00O0OO0O0O0O0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O00O0OO0O0O0O0 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOOO00O0000OO0O0 in invited_new :#line:62
            print (OOOOO00O0000OO0O0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O0OOO0OOOO00OOO0O in weishim :#line:65
            print (O0OOO0OOOO00OOO0O )#line:66
    except Exception as OO00OO0OOOOOOO000 :#line:67
        print (OO00OO0OOOOOOO000 )#line:68
def give_gold (OO0O00O0O00O0000O ,O0OOOOO000OO0OOOO ):#line:72
    try :#line:73
        O00OOO0OO0O00O0O0 =f'_doneeNo={OO0O00O0O00O0000O}&quantity={int(O0OOOOO000OO0OOOO)}_{timi_new()}'#line:74
        OOO0O000OOOO0OO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO0O00O0O0 ),'signstring':O00OOO0OO0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0OO0OOOO0O0O0OOO ={"quantity":int (O0OOOOO000OO0OOOO ),"doneeNo":OO0O00O0O00O0000O }#line:89
        OOOO000OOO0000OOO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O000OOOO0OO00 ,data =O0OO0OOOO0O0O0OOO ).json ()#line:90
        if 'status'in OOOO000OOO0000OOO :#line:92
            if OOOO000OOO0000OOO ['status']==200 :#line:93
                if OOOO000OOO0000OOO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0OOOOO000OO0OOOO)}种子给{OO0O00O0O00O0000O}成功')#line:95
                    return True #line:96
            if OOOO000OOO0000OOO ['status']==401 :#line:97
                print (f'【赠送种子】:{OOOO000OOO0000OOO["message"]}')#line:98
                return False #line:99
            if OOOO000OOO0000OOO ['status']==500 :#line:100
                print (f'【赠送种子】:{OOOO000OOO0000OOO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00O0OO00O00O0O00 :#line:104
        print (O00O0OO00O00O0O00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O00OO0OOOOO000O00 ):#line:115
    OO0O0O0000OOO0OO0 =hashlib .md5 (O00OO0OOOOO000O00 .encode ()).hexdigest ()#line:116
    OO00OOO00O00OOOOO =sc1 ()#line:117
    OOO000O0OO0000OO0 =sc2 ()#line:118
    OOO00OOOO0000OOO0 =sc3 ()#line:119
    O0000OO0O0000O0OO =OO00OOO00O00OOOOO +OO0O0O0000OOO0OO0 +OOO000O0OO0000OO0 +OOO00OOOO0000OOO0 #line:120
    O00OOO0O00O00OO00 =hashlib .md5 (O0000OO0O0000O0OO .encode ()).hexdigest ()#line:121
    return O00OOO0O00O00OO00 #line:122
def format_msg ():#line:125
    O00OOOOO0OOO00OOO =""#line:126
    for O000OOO0OOO0O00O0 in msg_list :#line:127
        O00OOOOO0OOO00OOO +=str (O000OOO0OOO0O00O0 )+"\r\n"#line:128
    return O00OOOOO0OOO00OOO #line:129
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
def get_json_data (OOO000O0O0000000O ,OOOO0O00000OO0000 ,OO000OO0O0O0O000O ,OOOOO0O0OO0OO0OOO ):#line:153
    with open (OOO000O0O0000000O ,'rb')as O0OOOO0O0O0000O0O :#line:154
        O0OO0000000OOOOO0 =json .load (O0OOOO0O0O0000O0O )#line:155
        O0OO0000000OOOOO0 ['data'][OOOO0O00000OO0000 ][OO000OO0O0O0O000O ]=OOOOO0O0OO0OO0OOO #line:156
        OOO00OOO0O00OOOOO =O0OO0000000OOOOO0 #line:157
    O0OOOO0O0O0000O0O .close ()#line:158
    return OOO00OOO0O00OOOOO #line:159
def write_json_data (O0OO00OOOO00OO0OO ):#line:162
    with open (json_path1 ,'w')as OO0OO00OO00OO00OO :#line:163
        json .dump (O0OO00OOOO00OO0OO ,OO0OO00OO00OO00OO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OO0OO00OO00OO00OO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO000O0O00O0O00O0 ,OO00OOO0OO00OO0O0 ,O0O00OOO00000OOOO ,OOO00OOO00OOOO000 ):#line:171
        try :#line:172
            OO000O0O00O0O00O0 .msg =O0O00OOO00000OOOO #line:173
            OO000O0O00O0O00O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO000O0O00O0O00O0 .token =OO00OOO0OO00OO0O0 ['authorization']#line:175
            OO000O0O00O0O00O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO000O0O00O0O00O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO000O0O00O0O00O0 .elephant_user =OO00OOO0OO00OO0O0 ['elephant_user']#line:178
            OO000O0O00O0O00O0 .elephant_pswd =OO00OOO0OO00OO0O0 ['elephant_pswd']#line:179
            OO000O0O00O0O00O0 .elephant_Task_ID =OO00OOO0OO00OO0O0 ['elephant_Task_ID']#line:180
            OO000O0O00O0O00O0 .len_new =OOO00OOO00OOOO000 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O00O0OOOOO0OOO0 ):#line:186
        try :#line:187
            O0O00O0OOOOO0OOO0 .watched_ad ()#line:189
            O0O0OO00O00OO00OO =f'__{timi_new()}'#line:190
            OO0O0OOO00OO0OOOO ={'source':'scsc','authorization':O0O00O0OOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00OO00OO ),'signstring':O0O0OO00O00OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOO0OO00OO000OO00 =requests .request ('get',f'{host}/user',headers =OO0O0OOO00OO0OOOO ).json ()#line:202
            if 'status'in OOO0OO00OO000OO00 :#line:204
                if OOO0OO00OO000OO00 ['status']==200 :#line:205
                    O0OOOOOO0O0000OOO =OOO0OO00OO000OO00 ['data']['nickname']#line:206
                    OO0OO0OO0OO0OOO00 =OOO0OO00OO000OO00 ['data']['inner_id']#line:207
                    O00O0O000OO0000OO =OOO0OO00OO000OO00 ['data']['assets']['gold']#line:208
                    O000OOOO00OO0OOO0 =OOO0OO00OO000OO00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0OOOOOO0O0000OOO[:5]}丨ID:{OO0OO0OO0OO0OOO00}丨等级:{O000OOOO00OO0OOO0}丨金种子:{str(O00O0O000OO0000OO).split(".")[0]}')#line:211
                    if 'wx_'in O0OOOOOO0O0000OOO :#line:212
                        O0O00O0OOOOO0OOO0 .change_nickname ()#line:213
                if OOO0OO00OO000OO00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O00O0OOOOO0OOO0 .elephant_user =='f':#line:216
                        return False #line:217
                    O00O00OO00000O0O0 =Invalid_login .addtask (elephant_user =O0O00O0OOOOO0OOO0 .elephant_user ,elephant_pswd =O0O00O0OOOOO0OOO0 .elephant_pswd ,elephant_Task_ID =O0O00O0OOOOO0OOO0 .elephant_Task_ID )#line:220
                    OO00O00OO00O0OOO0 =get_json_data (json_path ,O0O00O0OOOOO0OOO0 .len_new ,'authorization',O00O00OO00000O0O0 )#line:221
                    if write_json_data (OO00O00OO00O0OOO0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOO0OO00OO000OO00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO00O000O0000000O :#line:228
            print (OO00O000O0000000O )#line:229
    def sealing (O000OOO000OOOO0OO ):#line:232
        try :#line:233
            OO00OO0OO0O0000O0 =f'__{timi_new()}'#line:234
            OOOO000O0OO00000O ={'source':'scsc','authorization':O000OOO000OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0O0000O0 ),'signstring':OO00OO0OO0O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO000O0OO00000O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOOO000O0OO00000O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO000O0OO00000O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO000O0OO00000O )#line:249
            requests .request ('get',f'{host}/user',headers =OOOO000O0OO00000O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO000O0OO00000O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO000O0OO00000O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO000O0OO00000O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OO00000O )#line:254
            requests .request ('get',f'{host}/assets',headers =OOOO000O0OO00000O )#line:255
        except Exception as O0O0O00O0000OOO00 :#line:256
            print (O0O0O00O0000OOO00 )#line:257
    def ddd (OOOOOOOO0O00OOO00 ):#line:259
        try :#line:260
            OOOOOOOOO00OO00OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0OO0O0O0O0OO0O0O ={'source':'scsc','authorization':OOOOOOOO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO00OO00OO ),'signstring':OOOOOOOOO00OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOOOOO000O000OOO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OO0O0O0O0OO0O0O ).json ()#line:273
            print (OOOOOO000O000OOO0 )#line:274
        except Exception as OO0O0O0O00O00O00O :#line:277
            print (OO0O0O0O00O00O00O )#line:278
    def the_query (O0O000O000O0O00OO ):#line:283
        try :#line:284
            O000OO0OO00O000OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO0000000OOOO0O00 ={'authorization':O0O000O000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OO00O000OO ),'signstring':O000OO0OO00O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOOO00OO0O00OOOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0000000OOOO0O00 ).json ()#line:296
            if 'status'in OOOO00OO0O00OOOO0 :#line:298
                if OOOO00OO0O00OOOO0 ['status']==200 :#line:299
                    return OOOO00OO0O00OOOO0 ['data']['rows'][4 ]['price']#line:300
        except Exception as OOOO00O0OO0OO0O00 :#line:301
            print (OOOO00O0OO0OO0O00 )#line:302
    def market_sale (OO0O0O00OO00OO000 ,O00O0OO00000000O0 ):#line:305
        try :#line:306
            O0O0OO0O0OOOOO0OO =timi_new ()#line:307
            OO00OOOO0OOOOOO0O =f'type=crop__{O0O0OO0O0OOOOO0OO}'#line:308
            O0OOO0000O000OOOO ={'source':'scsc','authorization':OO0O0O00OO00OO000 .token ,'timestamp':str (O0O0OO0O0OOOOO0OO ),'sign':sign (OO00OOOO0OOOOOO0O ),'signstring':OO00OOOO0OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0O0O0O00OO00OO0O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0OOO0000O000OOOO ).json ()#line:320
            if 'status'in O0O0O0O00OO00OO0O :#line:322
                if O0O0O0O00OO00OO0O ['status']==200 :#line:323
                    if O0O0O0O00OO00OO0O ['data']['rows']:#line:324
                        O00O00OOO0OO0000O =O0O0O0O00OO00OO0O ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOO00OOO000O0O00O =O0O0O0O00OO00OO0O ['data']['rows'][0 ]['quantity']#line:326
                        if float (O00O0OO00000000O0 )>9 :#line:327
                            O00OO0O0O0OOO0OO0 =f'_packsackItemId={O00O00OOO0OO0000O}&price={str(O00O0OO00000000O0)[:5]}&quantity={OOO00OOO000O0O00O}_{O0O0OO0O0OOOOO0OO}'#line:328
                            O0O0000OO0O0OOOO0 ={'source':'scsc','authorization':OO0O0O00OO00OO000 .token ,'timestamp':str (O0O0OO0O0OOOOO0OO ),'sign':sign (O00OO0O0O0OOO0OO0 ),'signstring':O00OO0O0O0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOOO00OOO00000000 ={"packsackItemId":O00O00OOO0OO0000O ,"price":str (O00O0OO00000000O0 )[:5 ],"quantity":str (OOO00OOO000O0O00O )}#line:344
                            O0OO00O0O0O0000OO =requests .request ('post',f'{host}/market/sale',headers =O0O0000OO0O0OOOO0 ,data =OOOO00OOO00000000 ).json ()#line:345
                            if 'status'in O0OO00O0O0O0000OO :#line:347
                                if O0OO00O0O0O0000OO ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OOO00OOO000O0O00O}丨价格:{str(O00O0OO00000000O0)[:5]}')#line:349
        except Exception as O000O00O00000000O :#line:350
            print (O000O00O00000000O )#line:351
    def query_to_sell (O0OO00OO00000000O ):#line:354
        global count_list #line:355
        try :#line:356
            O00O000OOOO0OO000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:357
            O0O0O000O000O0O00 ={'source':'scsc','authorization':O0OO00OO00000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOO0OO000 ),'signstring':O00O000OOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0OO00OOOO0OO0OO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O0O000O000O0O00 ).json ()#line:369
            if 'status'in O0OO00OOOO0OO0OO0 :#line:371
                if O0OO00OOOO0OO0OO0 ['status']==200 :#line:372
                    for O000OOO00O0OO00O0 in O0OO00OOOO0OO0OO0 ['data']['rows']:#line:373
                        OOOO0OO0O0OO00O00 =O000OOO00O0OO00O0 ['materialKey']#line:374
                        OO0OOO0OOO0O00000 =O000OOO00O0OO00O0 ['quantity']#line:375
                        O0O00000OOO0O0OOO =O000OOO00O0OO00O0 ['price']#line:376
                        OOOO00OOOOOO00OO0 =O000OOO00O0OO00O0 ['saleState']#line:377
                        if OOOO00OOOOOO00OO0 ==0 :#line:378
                            print (f'【出售订单】:名称:{OOOO0OO0O0OO00O00}丨数量:{OO0OOO0OOO0O00000}丨价格:{O0O00000OOO0O0OOO}')#line:379
                            count_list +=OO0OOO0OOO0O00000 #line:380
                            O00O00OOO0OO00000 =O0OO00OO00000000O .the_query ()#line:382
                            if float (O00O00OOO0OO00000 )!=float (O0O00000OOO0O0OOO ):#line:383
                                OO000OOO00000OO00 =O000OOO00O0OO00O0 ['id']#line:384
                                if float (datetime .datetime .now ().hour )>8 :#line:385
                                    O0OO00OO00000000O .cacel_sale (OO000OOO00000OO00 )#line:386
                    O0OO00OO00000000O .game_map ()#line:388
        except Exception as OO0O00O0O000OOO00 :#line:390
            print (OO0O00O0O000OOO00 )#line:391
    def cacel_sale (O0O00OOO0OOOOOO00 ,O000O00OOOOO000O0 ):#line:394
        try :#line:395
            OOO000OOOOO000OOO =f'_saleId={O000O00OOOOO000O0}_{timi_new()}'#line:396
            O0OO0O0OOO00OO0O0 ={'source':'scsc','authorization':O0O00OOO0OOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOO000OOO ),'signstring':OOO000OOOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:407
            O0O00O00O0O00OOOO ={"saleId":O000O00OOOOO000O0 }#line:408
            OO00O00000O0O00O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OO0O0OOO00OO0O0 ,data =O0O00O00O0O00OOOO ).json ()#line:409
            if 'status'in OO00O00000O0O00O0 :#line:411
                if OO00O00000O0O00O0 ['status']==200 :#line:412
                    print (f'【下架出售】:{OO00O00000O0O00O0["data"]}')#line:413
        except Exception as O00OOO0OO00O00OO0 :#line:414
            print (O00OOO0OO00O00OO0 )#line:415
    def change_nickname (O000O00O00000OO00 ):#line:418
        try :#line:419
            OOOOO00O00O00OO0O =timi_new ()#line:420
            OO00OO00000OOOOO0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:421
            O0O0O00000OO00000 =requests .request ('post','https://www.qmsjmfb.com/',data =OO00OO00000OOOOO0 ).text #line:422
            OOO00000O0O00O00O =re .findall ('<ul><li>(.*?)</li>',O0O0O00000OO00000 )[0 ][:3 ]#line:423
            O000O0O0000O0000O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO00000O0O00O00O}').json ()#line:424
            O0O0O00O0OOOOO0O0 =O000O0O0000O0000O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:425
            O0OOO0O0O0000O00O ={"nickname":O0O0O00O0OOOOO0O0 }#line:426
            OO000OOO0OO000O00 =f'_nickname={O0O0O00O0OOOOO0O0}_{OOOOO00O00O00OO0O}'#line:427
            O000OOO0O0OOO0000 ={'source':'scsc','authorization':O000O00O00000OO00 .token ,'timestamp':OOOOO00O00O00OO0O ,'sign':sign (OO000OOO0OO000O00 ),'signstring':OO000OOO0OO000O00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:438
            O000OO00000O0OOO0 =requests .request ('patch',f'{host}/user/nickname',headers =O000OOO0O0OOO0000 ,data =O0OOO0O0O0000O00O ).json ()#line:439
            if 'status'in O000OO00000O0OOO0 :#line:441
                if O000OO00000O0OOO0 ['status']==200 :#line:442
                    print (f'【修改网名】:网名:{O0O0O00O0OOOOO0O0}丨{O000OO00000O0OOO0["message"]}')#line:443
        except Exception as OO000O0OOO0000OOO :#line:444
            print (OO000O0OOO0000OOO )#line:445
    def withdraw (OOO00O0000O00OOO0 ):#line:448
        try :#line:449
            OO0OOOOO00000O0OO =f'__{timi_new()}'#line:450
            O0000OOOOOOOO0OO0 ={'source':'scsc','authorization':OOO00O0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00000O0OO ),'signstring':OO0OOOOO00000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            OO0OO00OOO0OOO000 =requests .request ('get',f'{host}/assets',headers =O0000OOOOOOOO0OO0 ).json ()#line:462
            if 'status'in OO0OO00OOO0OOO000 :#line:464
                if OO0OO00OOO0OOO000 ['status']==200 :#line:465
                    O000O0O0O000OOOOO =OO0OO00OOO0OOO000 ['data']['cash']#line:466
                    if float (O000O0O0O000OOOOO )>20 :#line:467
                        OO0OOOOO00000O0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:468
                        O0000OOOOOOOO0OO0 ={'authorization':OOO00O0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00000O0OO ),'signstring':OO0OOOOO00000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:478
                        OO00000O0O00O000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:479
                        OOOOOOOO0OOOOO00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000OOOOOOOO0OO0 ,data =OO00000O0O00O000O ).json ()#line:481
                        if 'status'in OOOOOOOO0OOOOO00O :#line:483
                            if OOOOOOOO0OOOOO00O ['status']==200 :#line:484
                                print (f'【余额提现】:{OOOOOOOO0OOOOO00O["data"]}')#line:485
                        if 'status'in OOOOOOOO0OOOOO00O :#line:486
                            if OOOOOOOO0OOOOO00O ['status']==500 :#line:487
                                print (f'【余额提现】:{OOOOOOOO0OOOOO00O["message"]}')#line:488
        except Exception as OOOO0O00O0O000OO0 :#line:489
            print (OOOO0O00O0O000OO0 )#line:490
    def invitenum (O000000OOOOOO0000 ):#line:493
        global invited_new #line:494
        try :#line:495
            OO0OOO0O0OOO00000 =f'__{timi_new()}'#line:496
            O0000O0OOO00O0OO0 ={'source':'scsc','authorization':O000000OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OOO00000 ),'signstring':OO0OOO0O0OOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            O00O0OO0O0O0OO00O =requests .request ('get',f'{host}/invite/invitenum',headers =O0000O0OOO00O0OO0 ).json ()#line:508
            if 'status'in O00O0OO0O0O0OO00O :#line:510
                if O00O0OO0O0O0OO00O ['status']==200 :#line:511
                    OO0OOO00O0O000OO0 =O00O0OO0O0O0OO00O ['data']['invited_count']#line:512
                    OO0000O0OOO0O000O =O00O0OO0O0O0OO00O ['data']['invited_second_count']#line:513
                    print (f'【我的邀请】:直邀好友:{OO0OOO00O0O000OO0}丨间邀好友:{OO0000O0OOO0O000O}')#line:514
                    if OO0OOO00O0O000OO0 <2 :#line:515
                        OOOOO00O0OOO0OO00 =f'__{timi_new()}'#line:516
                        OOO0OO0OO0O00OOO0 ={'source':'scsc','authorization':O000000OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OOO0OO00 ),'signstring':OOOOO00O0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:527
                        O00OO00000O0O00O0 =requests .request ('get',f'{host}/user',headers =OOO0OO0OO0O00OOO0 ).json ()#line:528
                        if 'status'in O00OO00000O0O00O0 :#line:530
                            if O00OO00000O0O00O0 ['status']==200 :#line:531
                                invited_new .append (O00OO00000O0O00O0 ['data']['inner_id'])#line:532
        except Exception as OOO000O0O0OO0O00O :#line:533
            print (OOO000O0O0OO0O00O )#line:534
    def game_map (O0OO0O0000000O000 ):#line:537
        try :#line:538
            O0OOOOOOO0OO00OO0 =f'__{timi_new()}'#line:539
            OOOOO0000OOOO000O ={'source':'scsc','authorization':O0OO0O0000000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0OO00OO0 ),'signstring':O0OOOOOOO0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            O0OO00OOOO0OO0OOO =requests .request ('get',f'{host}/game/map',headers =OOOOO0000OOOO000O ).json ()#line:551
            if 'status'in O0OO00OOOO0OO0OOO :#line:553
                if O0OO00OOOO0OO0OOO ['status']==200 :#line:554
                    for OOOO000O0O0O0O000 in O0OO00OOOO0OO0OOO ['data']['list'][0 ]['crops']:#line:555
                        OO0O0OO0OO0OO0OO0 =OOOO000O0O0O0O000 ['level']#line:557
                        if OO0O0OO0OO0OO0OO0 ==41 :#line:558
                            O0000OO0OO00O000O =OOOO000O0O0O0O000 ['crop_name']#line:559
                            O0O0OOOO00OOOO0OO =OOOO000O0O0O0O000 ['count']#line:560
                            if O0O0OOOO00OOOO0OO >0 :#line:561
                                print (f'【农业资产】:{O0000OO0OO00O000O}丨数量:{O0O0OOOO00OOOO0OO}')#line:562
                                if float (datetime .datetime .now ().hour )>8 :#line:563
                                    O0O000O00000O00OO =O0OO0O0000000O000 .the_query ()#line:564
                                    O0OO0O0000000O000 .market_sale (O0O000O00000O00OO )#line:565
        except Exception as OOO0O00O0000O00O0 :#line:566
            print (OOO0O00O0000O00O0 )#line:567
    def give_gold (OO0OO0OOOOO00OO0O ):#line:570
        try :#line:571
            O00O0000O0OOO0OOO =f'__{timi_new()}'#line:572
            OO0O0O0O000O000O0 ={'source':'scsc','authorization':OO0OO0OOOOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O0OOO0OOO ),'signstring':O00O0000O0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            O000OOO0O000O0O0O =requests .request ('get',f'{host}/user',headers =OO0O0O0O000O000O0 ).json ()#line:584
            if 'status'in O000OOO0O000O0O0O :#line:585
                if O000OOO0O000O0O0O ['status']==200 :#line:586
                    if float (OO0OO0OOOOO00OO0O .doneeNo )!=0 :#line:587
                        OOOO0O00OO0O00O00 =O000OOO0O000O0O0O ['data']['assets']['gold']#line:588
                        if float (OOOO0O00OO0O00O00 )>float (OO0OO0OOOOO00OO0O .innerId ):#line:589
                            OOOOO000O00O0O00O =int (float (OOOO0O00OO0O00O00 )/1.1 )#line:590
                            O00O0000O0OOO0OOO =f'_doneeNo={OO0OO0OOOOO00OO0O.doneeNo}&quantity={OOOOO000O00O0O00O}_{timi_new()}'#line:591
                            OO0O0O0O000O000O0 ={'source':'scsc','authorization':OO0OO0OOOOO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O0OOO0OOO ),'signstring':O00O0000O0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O0O0O0O0O0O0O0O0O ={"quantity":OOOOO000O00O0O00O ,"doneeNo":OO0OO0OOOOO00OO0O .doneeNo }#line:606
                            O0OOO0OO0000O0O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O0O0O000O000O0 ,data =O0O0O0O0O0O0O0O0O ).json ()#line:607
                            if 'status'in O0OOO0OO0000O0O0O :#line:609
                                if O0OOO0OO0000O0O0O ['status']==200 :#line:610
                                    if O0OOO0OO0000O0O0O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OOOOO000O00O0O00O}种子给{OO0OO0OOOOO00OO0O.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OO00O000O0OOOOO0O :#line:615
            print (OO00O000O0OOOOO0O )#line:616
    def invitation (OOO00O0OOO0OO0O00 ):#line:618
        try :#line:619
            _O0O000OO0O000O00O =float (bundled_def ())/4 #line:620
            O000OO000O0OO000O =f'_innerId={int(_O0O000OO0O000O00O)}_{timi_new()}'#line:621
            OOOO00000OOO00OO0 ={'source':'scsc','authorization':OOO00O0OOO0OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O0OO000O ),'signstring':O000OO000O0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:632
            OOO0O00O0O0O000OO ={"innerId":int (_O0O000OO0O000O00O )}#line:633
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00000OOO00OO0 ,data =OOO0O00O0O0O000OO )#line:634
        except Exception as OO00OO0O00OOO00OO :#line:635
            print (OO00OO0O00OOO00OO )#line:636
    def winning_rewards (O000000O000OOO000 ):#line:639
        try :#line:640
            OOO0OO0O0O000OOOO =f'__{timi_new()}'#line:641
            O000OO0O0OOO000OO ={'source':'scsc','authorization':O000000O000OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0O000OOOO ),'signstring':OOO0OO0O0O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:652
            O00OOOO00OO00OO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000OO0O0OOO000OO ).json ()#line:653
            if 'status'in O00OOOO00OO00OO00 :#line:655
                if O00OOOO00OO00OO00 ['status']==200 :#line:656
                    if O00OOOO00OO00OO00 ['data']['amount']:#line:657
                        O00O00O000OOOOO00 =O00OOOO00OO00OO00 ['data']['amount']['gold']#line:658
                        return O00O00O000OOOOO00 #line:659
                    else :#line:660
                        return 0 #line:661
        except Exception as OOOO0OOO000OOOOOO :#line:662
            print (OOOO0OOO000OOOOOO )#line:663
    def certification (O0OO0OOO0O0000O0O ):#line:666
        try :#line:667
            OOOO0O0O00OOO0O00 =f'__{timi_new()}'#line:668
            O0000OOOOO0OOO0OO ={'source':'scsc','authorization':O0OO0OOO0O0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00OOO0O00 ),'signstring':OOOO0O0O00OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O0O00000OO00OOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000OOOOO0OOO0OO ).json ()#line:680
            if 'status'in O0O00000OO00OOOOO :#line:682
                if O0O00000OO00OOOOO ['status']==200 :#line:683
                    if O0O00000OO00OOOOO ['data']['result']:#line:684
                        O00O000OO0O000O00 =O0O00000OO00OOOOO ['data']['nick_name']#line:685
                        return O00O000OO0O000O00 #line:686
                    else :#line:687
                        return '未实名'#line:688
        except Exception as O00000OOO0OO0OOO0 :#line:689
            print (O00000OOO0OO0OOO0 )#line:690
    def crops_illustrated (OO000O0O0O0O0O0OO ):#line:693
        try :#line:694
            OOOO00O0O00O000O0 =f'__{timi_new()}'#line:695
            OOO0OO0O0OOOO00OO ={'source':'scsc','authorization':OO000O0O0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O000O0 ),'signstring':OOOO00O0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:706
            OOO0O0O0OO0O0OO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0OO0O0OOOO00OO ).json ()#line:707
            if 'status'in OOO0O0O0OO0O0OO00 :#line:709
                if OOO0O0O0OO0O0OO00 ['status']==200 :#line:710
                    OOOOOOO000O00O0OO =OOO0O0O0OO0O0OO00 ['data'][0 ]['crops']#line:711
                    for OO0OOOOOOOO00O0O0 in OOOOOOO000O00O0OO :#line:712
                        if OO0OOOOOOOO00O0O0 ['ill_clover_award']:#line:713
                            if float (OO0OOOOOOOO00O0O0 ['ill_clover_award'])>1 :#line:714
                                if OO0OOOOOOOO00O0O0 ['is_finish']:#line:715
                                    if not OO0OOOOOOOO00O0O0 ['is_getit']:#line:716
                                        if OO000O0O0O0O0O0OO .certification ()!='未实名':#line:717
                                            OOOO00O0O00O000O0 =f'_award_level={OO0OOOOOOOO00O0O0["level"]}_{timi_new()}'#line:718
                                            OOO0OO0O0OOOO00OO ={'source':'scsc','authorization':OO000O0O0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00O000O0 ),'signstring':OOOO00O0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:729
                                            OOOOO00000OO00OO0 ={"award_level":OO0OOOOOOOO00O0O0 ['level']}#line:730
                                            O0000O0000O0000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0OO0O0OOOO00OO ,json =OOOOO00000OO00OO0 ).json ()#line:732
                                            if 'status'in O0000O0000O0000O0 :#line:733
                                                if O0000O0000O0000O0 ['status']==200 :#line:734
                                                    OO00OOOOO0OO0OO00 =O0000O0000O0000O0 ['data']['ill_clover_award']#line:735
                                                    print (f'【图鉴奖励】:领取{OO0OOOOOOOO00O0O0["crop_name"]}成就丨奖励{OO00OOOOO0OO0OO00}☘️')#line:737
                                                if O0000O0000O0000O0 ['status']==500 :#line:738
                                                    print (f'【图鉴奖励】:{O0000O0000O0000O0["message"]}')#line:739
        except Exception as OOOOOO0OOOOO00000 :#line:740
            print (OOOOOO0OOOOO00000 )#line:741
    def watched_ad (O000O00O000000OOO ):#line:744
        try :#line:745
            O0O0000OOOO000OO0 =f'__{timi_new()}'#line:746
            O00O0000O0OO0O0O0 ={'source':'scsc','authorization':O000O00O000000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOOO000OO0 ),'signstring':O0O0000OOOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:757
            O00OOO0O000O00000 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0000O0OO0O0O0 ).json ()#line:758
            if 'status'in O00OOO0O000O00000 :#line:760
                if O00OOO0O000O00000 ['status']==200 :#line:761
                    if 'offlineInfo'in O00OOO0O000O00000 ['data']:#line:762
                        time .sleep (random .randint (1 ,3 ))#line:763
                        O0000000OOOOO0OO0 =O00OOO0O000O00000 ['data']['offlineInfo']['off_minute']#line:764
                        O0000OOOOO0OO00O0 =float (O00OOO0O000O00000 ['data']['silver'])/1000000000000 #line:765
                        time .sleep (1 )#line:766
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0000O0OO0O0O0 ).json ()#line:767
                        time .sleep (2 )#line:768
                        O00000O00O00000OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0000O0OO0O0O0 ).json ()#line:769
                        if 'status'in O00000O00O00000OO :#line:771
                            if O00000O00O00000OO ['status']==200 :#line:772
                                OO0OOO00OO00O0O00 =float (O00000O00O00000OO ['data']['silver'])/1000000000000 #line:773
                                O000O000O00O000O0 =str (OO0OOO00OO00O0O00 -O0000OOOOO0OO00O0 )[:6 ]#line:774
                                print (f'【离线奖励】:翻倍离线{O0000000OOOOO0OO0}分钟奖励🌱数量:{O000O000O00O000O0}t粒')#line:775
        except Exception as OOOOOOO0O000O00OO :#line:776
            print (OOOOOOO0O000O00OO )#line:777
    def user_ad (OOOOOO0OO00000O00 ):#line:780
        try :#line:781
            O0OOOOOOO00OO000O =f'__{timi_new()}'#line:782
            OO0O00OOOO00OOO0O ={'source':'scsc','authorization':OOOOOO0OO00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO00OO000O ),'signstring':O0OOOOOOO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:793
            O0O0000OO0O00O0OO =requests .request ('get',f'{host}/user/ad',headers =OO0O00OOOO00OOO0O ).json ()#line:794
            if 'status'in O0O0000OO0O00O0OO :#line:796
                if O0O0000OO0O00O0OO ['status']==200 :#line:797
                    O00000OOOO0OOO000 =O0O0000OO0O00O0OO ['data']['max_time']#line:798
                    O000O00O00OO00000 =O0O0000OO0O00O0OO ['data']['watch_time']#line:799
                    O0O000O0OO0000000 =O0O0000OO0O00O0OO ['data']['added_time']#line:800
                    print (f'【获取种子】:获取🌱剩余{O0O000O0OO0000000 + O00000OOOO0OOO000 - O000O00O00OO00000}次丨好友提供:{O0O000O0OO0000000}次')#line:801
                    if O0O000O0OO0000000 +O00000OOOO0OOO000 -O000O00O00OO00000 >0 :#line:802
                        time .sleep (random .randint (16 ,19 ))#line:803
                        O00OOO00OOOO0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0O00OOOO00OOO0O ).json ()#line:804
                        if 'status'in O00OOO00OOOO0OO00 :#line:806
                            if O00OOO00OOOO0OO00 ['status']==200 :#line:807
                                O0O000OOO0OOO0OO0 =float (O00OOO00OOOO0OO00 ['data']['silver'])/1000000000000 #line:808
                                print (f'【获取种子】:获得🌱:{int(O0O000OOO0OOO0OO0)}t粒')#line:809
                                return True #line:810
                            if O00OOO00OOOO0OO00 ['status']==500 :#line:811
                                OO00O00O000O0O00O =O00OOO00OOOO0OO00 ['message']#line:812
                                print (f'【获取种子】:{OO00O00O000O0O00O}')#line:813
                                return False #line:814
        except Exception as O0O00O00000OOO00O :#line:815
            print (O0O00O00000OOO00O )#line:816
    def synthetic (OOO0O00000OOOO000 ):#line:819
        global id ,g #line:820
        try :#line:821
            O00OOO0OOOO00O0OO =OOO0O00000OOOO000 .level_new ()#line:822
            O0O0OO0O00O0O0OOO =random .randint (9 ,11 )#line:823
            O000O0OOO00O0O0O0 =f'_site=8&targetSite={O0O0OO0O00O0O0OOO}_{timi_new()}'#line:824
            OOOO000O0O0O00O00 ={'source':'scsc','authorization':OOO0O00000OOOO000 .token ,'timestamp':timi_new (),'sign':sign (O000O0OOO00O0O0O0 ),'signstring':O000O0OOO00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:835
            O0O000OOOOOO0000O ={"site":int (8 ),"targetSite":int (O0O0OO0O00O0O0OOO )}#line:836
            requests .request ('post',f'{host}/game/crops/move',headers =OOOO000O0O0O00O00 ,json =O0O000OOOOOO0000O )#line:837
            while True :#line:838
                OO00O000OO000O000 =f'__{timi_new()}'#line:839
                OO0OOOOO00OO0000O ={'source':'scsc','authorization':OOO0O00000OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO000O000 ),'signstring':OO00O000OO000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:850
                O00O0O0O0OOO000OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOO00OO0000O ).json ()#line:851
                if 'status'in O00O0O0O0OOO000OO :#line:853
                    if O00O0O0O0OOO000OO ['status']==200 :#line:854
                        OO0O00OO0OO0000OO =O00O0O0O0OOO000OO ['data']['cropList']#line:855
                        OOOO0000OO0OOO0O0 =O00O0O0O0OOO000OO ['data']['gameCoreDataDBid']#line:856
                        OO0O000OOOOO0O0OO =float (O00O0O0O0OOO000OO ['data']['silver'])/1000000000000 #line:857
                        OO00OOO00000000OO =0 #line:862
                        for O00O00OO000O0OO0O in OO0O00OO0OO0000OO :#line:863
                            if not O00O00OO000O0OO0O :#line:864
                                O00O0000O0OO0000O =f'_crop_id={OOOO0000OO0OOO0O0}&site={OO00OOO00000000OO}_{OOO0O00000OOOO000.time}'#line:865
                                O00O000OOOO0O0OOO ={'source':'scsc','authorization':OOO0O00000OOOO000 .token ,'timestamp':OOO0O00000OOOO000 .time ,'sign':sign (O00O0000O0OO0000O ),'signstring':O00O0000O0OO0000O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:875
                                OOOOOOO0OO00000OO ={"site":OO00OOO00000000OO ,"crop_id":OOOO0000OO0OOO0O0 }#line:876
                                OOOOO0OOO0OOO0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =O00O000OOOO0O0OOO ,data =OOOOOOO0OO00000OO ).json ()#line:877
                                time .sleep (random .randint (1 ,3 )/10 )#line:879
                                if 'status'in OOOOO0OOO0OOO0O0O :#line:880
                                    if OOOOO0OOO0OOO0O0O ['status']==200 :#line:881
                                        if OOOOO0OOO0OOO0O0O ['message']=='种子数量不足':#line:882
                                            O00OOO0OOOO00O0OO =OOO0O00000OOOO000 .level_new ()#line:883
                                            print (f'【种植合成】:{OOOOO0OOO0OOO0O0O["message"]}')#line:884
                                            if not OOO0O00000OOOO000 .user_ad ():#line:885
                                                return False #line:886
                                    if OOOOO0OOO0OOO0O0O ['status']==500 :#line:887
                                        print (f'【种植合成】:{OOOOO0OOO0OOO0O0O["message"]}')#line:888
                                        return False #line:889
                            OO00OOO00000000OO +=1 #line:890
                        OOO0O00O0O0O0000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOOO00OO0000O ).json ()#line:891
                        O0OOOO000O00O0O00 =OOO0O00O0O0O0000O ['data']['cropList']#line:892
                        O0O000O00000OOO00 =False #line:893
                        for O00O00OO000O0OO0O in range (12 ):#line:894
                            id =O0OOOO000O00O0O00 [O00O00OO000O0OO0O ]['level']#line:895
                            if float (O00OOO0OOOO00O0OO )-float (id )>9 :#line:896
                                OOOO0000O0OOO0OO0 =f'_site={O00O00OO000O0OO0O}_{timi_new()}'#line:897
                                OO000O0OOO00OO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O00000OOOO000 .token ,'timestamp':timi_new (),'sign':sign (OOOO0000O0OOO0OO0 ),'signstring':OOOO0000O0OOO0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:908
                                OOOO0OO000OOO0000 ={"site":O00O00OO000O0OO0O }#line:909
                                OO0OO00O00000000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000O0OOO00OO00O ,data =OOOO0OO000OOO0000 ).json ()#line:911
                                if 'status'in OO0OO00O00000000O :#line:912
                                    if OO0OO00O00000000O ['status']==200 :#line:913
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:914
                            if id !=0 :#line:915
                                for OOOOOO00O0OOO0000 in range (11 ):#line:916
                                    OO00O00OOOO00O00O =OOOOOO00O0OOO0000 +1 #line:917
                                    g =O0OOOO000O00O0O00 [OO00O00OOOO00O00O ]['level']#line:918
                                    if id ==g :#line:919
                                        O0OO0OO0O00OO0000 =OOOOOO00O0OOO0000 +2 #line:920
                                        if O0OO0OO0O00OO0000 !=O00O00OO000O0OO0O +1 :#line:921
                                            OO00O00000OOOOOOO =O00O00OO000O0OO0O +1 #line:922
                                            time .sleep (random .randint (1 ,3 )/10 )#line:924
                                            O000O0OOO00O0O0O0 =f'_site={OO00O00000OOOOOOO - 1}&targetSite={O0OO0OO0O00OO0000 - 1}_{timi_new()}'#line:925
                                            OOOO000O0O0O00O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O00000OOOO000 .token ,'timestamp':timi_new (),'sign':sign (O000O0OOO00O0O0O0 ),'signstring':O000O0OOO00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:942
                                            O0OO00O0O0O0O000O ={"site":int (OO00O00000OOOOOOO -1 ),"targetSite":int (O0OO0OO0O00OO0000 -1 )}#line:943
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOO000O0O0O00O00 ,json =O0OO00O0O0O0O000O )#line:944
                                            O0O000O00000OOO00 =True #line:946
                                    if O0O000O00000OOO00 :#line:947
                                        break #line:948
                                if O0O000O00000OOO00 :#line:949
                                    break #line:950
        except :#line:951
            OOO0O00000OOOO000 .synthetic ()#line:952
    def level_new (O0O0O0O0OO00OO000 ):#line:955
        try :#line:956
            O0O0OOO0O000O0OOO =f'__{timi_new()}'#line:957
            O0O0OOO00OO0OOO0O ={'source':'scsc','authorization':O0O0O0O0OO00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O000O0OOO ),'signstring':O0O0OOO0O000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:968
            OO0O00OOO0O00OO00 =requests .request ('get',f'{host}/user',headers =O0O0OOO00OO0OOO0O ).json ()#line:969
            if 'status'in OO0O00OOO0O00OO00 :#line:970
                if OO0O00OOO0O00OO00 ['status']==200 :#line:971
                    return float (OO0O00OOO0O00OO00 ['data']['level'])#line:972
        except Exception as OO00OO000OO0OO00O :#line:973
            print (OO00OO000OO0OO00O )#line:974
    def propsraffle (OO0O0O0000O00O000 ):#line:977
        try :#line:978
            while True :#line:979
                OOO0OOOOO0OOOO0OO =f'__{timi_new()}'#line:980
                OOOO0O0OOO00O0O0O ={'source':'scsc','authorization':OO0O0O0000O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0OOOO0OO ),'signstring':OOO0OOOOO0OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:991
                OOO00000O0OOO00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO0O0OOO00O0O0O ).json ()#line:992
                if 'status'in OOO00000O0OOO00O0 :#line:994
                    if OOO00000O0OOO00O0 ['status']==200 :#line:995
                        O00OOO0OO00OOOO00 =OOO00000O0OOO00O0 ['data']['rows']#line:996
                        O0O0OO0O0000000O0 =OOO00000O0OOO00O0 ['data']['vstate']#line:997
                        if O00OOO0OO00OOOO00 ==5 or O00OOO0OO00OOOO00 ==6 or O00OOO0OO00OOOO00 ==7 :#line:998
                            O0OOO000OO0O00O0O =OOO00000O0OOO00O0 ['data']['silver']#line:999
                            print (f'【转盘抽奖】:获得种子:{O0OOO000OO0O00O0O}')#line:1000
                        if O00OOO0OO00OOOO00 ==1 or O00OOO0OO00OOOO00 ==2 or O00OOO0OO00OOOO00 ==3 :#line:1001
                            O00OOO0OO000O000O =OOO00000O0OOO00O0 ['data']['clover']#line:1002
                            print (f'【转盘抽奖】:获得三叶草:{O00OOO0OO000O000O}')#line:1003
                        if O00OOO0OO00OOOO00 ==4 or O00OOO0OO00OOOO00 ==8 :#line:1004
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1005
                        if O00OOO0OO00OOOO00 =='抽奖次数已用完':#line:1009
                            break #line:1043
                time .sleep (random .randint (8 ,15 )/10 )#line:1044
        except Exception as OOO0OO00OO0OOO0O0 :#line:1045
            print (OOO0OO00OO0OOO0O0 )#line:1046
    def friends_invitation (OO000OO000OO00O0O ):#line:1049
        try :#line:1050
            OOO0OO00O0O00OO00 =f'__{timi_new()}'#line:1051
            OOO0O0O0OO00OO00O ={'source':'scsc','authorization':OO000OO000OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00O0O00OO00 ),'signstring':OOO0OO00O0O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1062
            O00OOOO0OO00O0O00 =requests .request ('get',f'{host}/friends',headers =OOO0O0O0OO00OO00O ).json ()#line:1063
            if 'status'in O00OOOO0OO00O0O00 :#line:1064
                if O00OOOO0OO00O0O00 ['status']==200 :#line:1065
                    OOOOOO0OO0O00OO00 =O00OOOO0OO00O0O00 ['data']['myInviteter']#line:1066
                    if OOOOOO0OO0O00OO00 :#line:1067
                        OO0O00O00O00000OO =OOOOOO0OO0O00OO00 ['user']['nickname']#line:1068
                        O0OO00O000O000O00 =OO000OO000OO00O0O .certification ()#line:1069
                        if O0OO00O000O000O00 =='未实名':#line:1070
                            weishim .append (OO000OO000OO00O0O .token )#line:1071
                        print (f'【查邀请人】:我的邀请人:{OO0O00O00O00000OO}丨实名:{O0OO00O000O000O00}')#line:1072
        except Exception as OO00O0OOO000O0000 :#line:1076
            print (OO00O0OOO000O0000 )#line:1077
    def add_clover (O0OO0O0OOO00O0000 ):#line:1080
        global golden_seed #line:1081
        try :#line:1082
            OOOOOOO00OOOO00OO =f'__{timi_new()}'#line:1083
            OOO0O0OO00O0000OO ={'source':'scsc','authorization':O0OO0O0OOO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO00OOOO00OO ),'signstring':OOOOOOO00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1094
            O00000O0O0OO00OO0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO0O0OO00O0000OO ).json ()#line:1095
            if 'status'in O00000O0O0OO00OO0 :#line:1097
                if O00000O0O0OO00OO0 ['status']==200 :#line:1098
                    O0O0000OO000OOO0O =O00000O0O0OO00OO0 ['data']['clover']#line:1099
                    O0O0O00OOO000O0O0 =O00000O0O0OO00OO0 ['data']['used_clover']#line:1100
                    OOO0OOOO0O000OO0O =float (O0O0000OO000OOO0O )-float (O0O0O00OOO000O0O0 )#line:1101
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O00OOO000O0O0}')#line:1102
                    if O0OO0O0OOO00O0000 .certification ()!='未实名':#line:1103
                        if OOO0OOOO0O000OO0O >1 :#line:1104
                            OOOOOOO00OOOO00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0OOOO0O000OO0O)}_{timi_new()}'#line:1105
                            O00OO0O000O0OOO0O ={'source':'scsc','authorization':O0OO0O0OOO00O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO00OOOO00OO ),'signstring':OOOOOOO00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1116
                            O000O000O0OOOOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0OOOO0O000OO0O )}#line:1117
                            OOO00O0OOO00O00OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO0O000O0OOO0O ,data =O000O000O0OOOOO00 ).json ()#line:1118
                            if 'status'in OOO00O0OOO00O00OO :#line:1120
                                if OOO00O0OOO00O00OO ['status']==200 :#line:1121
                                    print (f'【参与抽奖】:添加☘️:{OOO00O0OOO00O00OO["data"]["isSuccess"]}丨数量:{OOO0OOOO0O000OO0O}')#line:1122
                                if OOO00O0OOO00O00OO ['status']==500 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{OOO00O0OOO00O00OO["message"]}')#line:1124
            O0OO0OOOO000OO000 =requests .request ('get',f'{host}/lottery',headers =OOO0O0OO00O0000OO ).json ()#line:1125
            O000000O0OOO00OOO =O0OO0O0OOO00O0000 .winning_rewards ()#line:1127
            if 'status'in O0OO0OOOO000OO000 :#line:1128
                if O0OO0OOOO000OO000 ['status']==200 :#line:1129
                    OOOO000000O0000O0 =O0OO0OOOO000OO000 ['data'][0 ]['day_get_gold_quantity']#line:1130
                    golden_seed +=float (OOOO000000O0000O0 )#line:1131
                    OOO0O000OO0OO0000 =O0OO0OOOO000OO000 ['data'][1 ]['value']#line:1132
                    O0OOOO000O0OOO0OO =O0OO0OOOO000OO000 ['data'][0 ]['join_number']#line:1133
                    O00OOOOO0OO0O00OO =int (float (O0OO0OOOO000OO000 ['data'][0 ]['totalValue']))#line:1134
                    O000OOOO0OOOOOOOO =float (OOO0O000OO0OO0000 /O00OOOOO0OO0O00OO )*10000 #line:1135
                    O0O00OO0O0OOO0O0O =O00OOOOO0OO0O00OO /O0OOOO000O0OOO0OO #line:1136
                    print (f'【参与抽奖】:预计每天中{str(OOOO000000O0000O0)[:6]}颗金种子丨好友收益:{str(O000000O0OOO00OOO)[:6]}')#line:1137
                    print (f'【抽奖统计】:每1万☘️中{str(O000OOOO0OOOOOOOO)[:6]}颗金种子丨☘️人均:{str(O0O00OO0O0OOO0O0O)[:7]}️')#line:1138
        except Exception as O00O0O00000O00O00 :#line:1139
            print (O00O0O00000O00O00 )#line:1140
    def energy (O0OOO00OO0000O0O0 ):#line:1143
        try :#line:1144
            while True :#line:1145
                OOOO0OO0000O00000 =f'__{timi_new()}'#line:1146
                O000O00000OOOOO0O ={'source':'scsc','authorization':O0OOO00OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0000O00000 ),'signstring':OOOO0OO0000O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1157
                O00OOOOO0O000O000 =requests .request ('get',f'{host}/energy/general',headers =O000O00000OOOOO0O ).json ()#line:1158
                if 'status'in O00OOOOO0O000O000 :#line:1160
                    if O00OOOOO0O000O000 ['status']==200 :#line:1161
                        O0OOOO00O000O0000 =O00OOOOO0O000O000 ['data']['ordinary_water']#line:1162
                        O000OOO000O00000O =O00OOOOO0O000O000 ['data']['ordinary_fertilizer']#line:1163
                        O0O00000O0OOO00O0 =O00OOOOO0O000O000 ['data']['videoStatus']#line:1164
                        O0OO00OO0O00OOOO0 =O00OOOOO0O000O000 ['data']['waterVideoKey']#line:1165
                        print (f'【我的营养】:肥料:{str(O000OOO000O00000O).split(".")[0]}丨水滴:{str(O0OOOO00O000O0000).split(".")[0]}')#line:1167
                        if float (O000OOO000O00000O )<96 :#line:1168
                            if O0O00000O0OOO00O0 :#line:1169
                                time .sleep (random .randint (160 ,180 )/10 )#line:1170
                                O0OO000O0OOOOO0OO =99 -float (O000OOO000O00000O )#line:1171
                                OO00OO000OOOOOO0O ={"fertilizer":str (O0OO000O0OOOOO0OO ).split ('.')[0 ]}#line:1172
                                O0000O0O0OO000OO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000O00000OOOOO0O ).json ()#line:1174
                                if 'status'in O0000O0O0OO000OO0 :#line:1176
                                    if O0000O0O0OO000OO0 ['status']==200 :#line:1177
                                        print (f'【购买肥料】:看广告获取肥料:{O0000O0O0OO000OO0["message"]}')#line:1178
                                    if O0000O0O0OO000OO0 ['status']==500 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O0000O0O0OO000OO0["message"]}')#line:1180
                                        break #line:1181
                                if float (O000OOO000O00000O )<78 :#line:1183
                                    O0OO000O0OOOOO0OO =80 -float (O000OOO000O00000O )#line:1184
                                    OO0OOO0OOO0OOOOOO =f'_fertilizer={int(O0OO000O0OOOOO0OO)}_{timi_new()}'#line:1185
                                    O0OOO0OOOO000OOO0 ={'source':'scsc','authorization':O0OOO00OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OOO0OOOOOO ),'signstring':OO0OOO0OOO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1196
                                    OO0OO0000OOOO0OOO ={"fertilizer":int (O0OO000O0OOOOO0OO )}#line:1197
                                    O0OOO000O0OOOOO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOO0OOOO000OOO0 ,data =OO0OO0000OOOO0OOO ).json ()#line:1199
                                    if 'status'in O0OOO000O0OOOOO00 :#line:1201
                                        if O0OOO000O0OOOOO00 ['status']==200 :#line:1202
                                            print (f'【购买肥料】:购买肥料:{O0OOO000O0OOOOO00["message"]}丨数量:{int(O0OO000O0OOOOO0OO)}')#line:1203
                                        if O0OOO000O0OOOOO00 ['status']==500 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{O0OOO000O0OOOOO00["message"]}丨数量:{int(O0OO000O0OOOOO0OO)}')#line:1205
                                            O00O0OOOOOO0OO00O =O0OOO000O0OOOOO00 ["message"].split ('-')[1 ]#line:1206
                                            O0OO000O000O0OO0O =f'__{timi_new()}'#line:1207
                                            O0O0O00OOO0OO0000 ={'source':'scsc','authorization':O0OOO00OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O000O0OO0O ),'signstring':O0OO000O000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1218
                                            O00O000O0O00OOO0O =requests .request ('get',f'{host}/user',headers =O0O0O00OOO0OO0000 ).json ()#line:1219
                                            if 'status'in O00O000O0O00OOO0O :#line:1220
                                                if O00O000O0O00OOO0O ['status']==200 :#line:1221
                                                    OOO0OOOOO00O0OO0O =O00O000O0O00OOO0O ['data']['inner_id']#line:1222
                                                    if give_gold (OOO0OOOOO00O0OO0O ,float (O00O0OOOOOO0OO00O )+1 ):#line:1223
                                                        O0OOO00OO0000O0O0 .energy ()#line:1224
                        if float (O0OOOO00O000O0000 )<880 :#line:1225
                            if O0OO00OO0O00OOOO0 :#line:1226
                                time .sleep (random .randint (160 ,180 )/10 )#line:1227
                                OOO0OOOOO0O0O0OOO =999 -float (O0OOOO00O000O0000 )#line:1228
                                O0OOOOOOO000O0000 ={"water":str (OOO0OOOOO0O0O0OOO ).split ('.')[0 ]}#line:1229
                                O0OOO00OO0O0OO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000O00000OOOOO0O ).json ()#line:1231
                                if 'status'in O0OOO00OO0O0OO0OO :#line:1233
                                    if O0OOO00OO0O0OO0OO ['status']==200 :#line:1234
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO00OO0O0OO0OO["message"]}')#line:1235
                                    if O0OOO00OO0O0OO0OO ['status']==500 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOO00OO0O0OO0OO["message"]}')#line:1237
                                        break #line:1238
                                if float (O0OOOO00O000O0000 )<780 :#line:1239
                                    OOO0OOOOO0O0O0OOO =800 -float (O0OOOO00O000O0000 )#line:1240
                                    OO00O00OO0000O0OO =f'_water={int(OOO0OOOOO0O0O0OOO)}_{timi_new()}'#line:1241
                                    OOOOOOOO0O000O0OO ={'source':'scsc','authorization':O0OOO00OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0000O0OO ),'signstring':OO00O00OO0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1252
                                    OO0OO000OOOO0OOO0 ={"water":int (OOO0OOOOO0O0O0OOO )}#line:1253
                                    OO0OOO0OO0OO00O0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOOOOOO0O000O0OO ,data =OO0OO000OOOO0OOO0 ).json ()#line:1255
                                    if 'status'in OO0OOO0OO0OO00O0O :#line:1257
                                        if OO0OOO0OO0OO00O0O ['status']==200 :#line:1258
                                            print (f'【购买水滴】:购买水滴:{OO0OOO0OO0OO00O0O["message"]}丨数量:{int(OOO0OOOOO0O0O0OOO)}')#line:1259
                                        if OO0OOO0OO0OO00O0O ['status']==500 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{OO0OOO0OO0OO00O0O["message"]}丨数量:{int(OOO0OOOOO0O0O0OOO)}')#line:1261
                                            O00O0OOOOOO0OO00O =OO0OOO0OO0OO00O0O ["message"].split ('-')[1 ]#line:1262
                                            O0OO000O000O0OO0O =f'__{timi_new()}'#line:1263
                                            O0O0O00OOO0OO0000 ={'source':'scsc','authorization':O0OOO00OO0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O000O0OO0O ),'signstring':O0OO000O000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1274
                                            O00O000O0O00OOO0O =requests .request ('get',f'{host}/user',headers =O0O0O00OOO0OO0000 ).json ()#line:1275
                                            if 'status'in O00O000O0O00OOO0O :#line:1276
                                                if O00O000O0O00OOO0O ['status']==200 :#line:1277
                                                    OOO0OOOOO00O0OO0O =O00O000O0O00OOO0O ['data']['inner_id']#line:1278
                                                    if give_gold (OOO0OOOOO00O0OO0O ,float (O00O0OOOOOO0OO00O )+1 ):#line:1279
                                                        O0OOO00OO0000O0O0 .energy ()#line:1280
                        break #line:1281
        except Exception as OO0OOOOOOOO00O00O :#line:1282
            print (OO0OOOOOOOO00O00O )#line:1283
def bundled_def ():#line:1286
    O0OO0000OO0O0O00O =['5570536','7750212','7911652','7911680','7805624']#line:1287
    return O0OO0000OO0O0O00O [random .randint (0 ,len (O0OO0000OO0O0O00O )-1 )]#line:1288
def version_of_the_validation ():#line:1292
    return str ((103 -56 )/10 )#line:1293
def ubbbf ():#line:1295
    print ('卡密验证通过   ✅')#line:1296
def sc2 ():#line:1299
    return "19319#$%^&*((*"#line:1300
def OO00OO0OO0OO00OO00o0 ():#line:1303
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1305
def get_ip ():#line:1308
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1310
def gitee_validation ():#line:1313
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1314
def gitee_edition ():#line:1317
    try :#line:1318
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1319
    except :#line:1320
        sys .exit (0 )#line:1321
def O000OO000O0O00OOO00 ():#line:1325
    try :#line:1326
        O0000OOO000O0O000 =gitee_edition ()#line:1327
        if version_of_the_validation ()<O0000OOO000O0O000 ['CityEarth']['edition']:#line:1328
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OOO000O0O000["CityEarth"]["edition"]}   ❌')#line:1329
            print (f'更新内容=>>{O0000OOO000O0O000["CityEarth"]["content"]}')#line:1330
        else :#line:1331
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OOO000O0O000["CityEarth"]["edition"]}   ✅')#line:1332
            print (f'更新内容=>> {O0000OOO000O0O000["CityEarth"]["content"]}')#line:1333
    except Exception as O0O000000O00OO00O :#line:1334
        print (O0O000000O00OO00O )#line:1335
def sc3 ():#line:1338
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1339
if __name__ =='__main__':#line:1342
    start ()#line:1343
