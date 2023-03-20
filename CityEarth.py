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
        OO00O0O00O0OOOO00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO00O0O00O0OOOO00)}个账号==========")#line:17
        for OOO0OOO0O0O0OOOO0 in OO00O0O00O0OOOO00 :#line:18
            O0O0O0OOOOOO0O0O0 =[]#line:19
            print (f"------------正在执行第{OO00O0O00O0OOOO00.index(OOO0OOO0O0O0OOOO0) + 1}个账号------------")#line:20
            OO0OOO0O000O0O00O =CityEarth (OOO0OOO0O0O0OOOO0 ,O0O0O0OOOOOO0O0O0 ,OO00O0O00O0OOOO00 .index (OOO0OOO0O0O0OOOO0 ))#line:21
            def OOOOOOO0OO0000OOO ():#line:23
                if OO0OOO0O000O0O00O .base_info ():#line:25
                    OO0OOO0O000O0O00O .sealing ()#line:27
                    OO0OOO0O000O0O00O .invitenum ()#line:29
                    OO0OOO0O000O0O00O .query_to_sell ()#line:31
                    OO0OOO0O000O0O00O .friends_invitation ()#line:35
                    OO0OOO0O000O0O00O .energy ()#line:37
                    OO0OOO0O000O0O00O .add_clover ()#line:39
                    OO0OOO0O000O0O00O .propsraffle ()#line:41
                    OO0OOO0O000O0O00O .crops_illustrated ()#line:45
                    OO0OOO0O000O0O00O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0OOO0O000O0O00O .give_gold ()#line:50
            OO0OO000O0OO00OO0 =threading .Thread (target =OOOOOOO0OO0000OOO )#line:52
            OO0OO000O0OO00OO0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0OOO0OOO000OOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OOO0OOO000OOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO00O0OOO0OO0000O in invited_new :#line:62
            print (OO00O0OOO0OO0000O )#line:63
        print ('开始打印未实名的token')#line:64
        for O000000O000OOOOOO in weishim :#line:65
            print (O000000O000OOOOOO )#line:66
    except Exception as O00O0O0O0OOO0O0OO :#line:67
        print (O00O0O0O0OOO0O0OO )#line:68
def give_gold (O00O00OO0OOO00OOO ,O00OO0O000OOOOO0O ):#line:72
    try :#line:73
        OO0O00O0O00O0OO00 =f'_doneeNo={O00O00OO0OOO00OOO}&quantity={int(O00OO0O000OOOOO0O)}_{timi_new()}'#line:74
        OO0000OO0O00OOOO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O00O0O00O0OO00 ),'signstring':OO0O00O0O00O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0OOOO0O0OO000OO0 ={"quantity":int (O00OO0O000OOOOO0O ),"doneeNo":O00O00OO0OOO00OOO }#line:89
        OO000000OOOOOOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OO0000OO0O00OOOO0 ,data =O0OOOO0O0OO000OO0 ).json ()#line:90
        if 'status'in OO000000OOOOOOO0O :#line:92
            if OO000000OOOOOOO0O ['status']==200 :#line:93
                if OO000000OOOOOOO0O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00OO0O000OOOOO0O)}种子给{O00O00OO0OOO00OOO}成功')#line:95
                    return True #line:96
            if OO000000OOOOOOO0O ['status']==401 :#line:97
                print (f'【赠送种子】:{OO000000OOOOOOO0O["message"]}')#line:98
                return False #line:99
            if OO000000OOOOOOO0O ['status']==500 :#line:100
                print (f'【赠送种子】:{OO000000OOOOOOO0O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO000O00OOOOOOO0 :#line:104
        print (OOO000O00OOOOOOO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O000O0OOO00O0O00O ):#line:115
    O0OO000OO0O000000 =hashlib .md5 (O000O0OOO00O0O00O .encode ()).hexdigest ()#line:116
    OO00O0O000O00OOO0 =sc1 ()#line:117
    O0000OOO0O0O0O0OO =sc2 ()#line:118
    OOO00OO0000000000 =sc3 ()#line:119
    O0OO0O00OO0O00O0O =OO00O0O000O00OOO0 +O0OO000OO0O000000 +O0000OOO0O0O0O0OO +OOO00OO0000000000 #line:120
    O000000OO0OO00O00 =hashlib .md5 (O0OO0O00OO0O00O0O .encode ()).hexdigest ()#line:121
    return O000000OO0OO00O00 #line:122
def format_msg ():#line:125
    OOO0OO00OOOO0OOO0 =""#line:126
    for OOO00O0O000000O0O in msg_list :#line:127
        OOO0OO00OOOO0OOO0 +=str (OOO00O0O000000O0O )+"\r\n"#line:128
    return OOO0OO00OOOO0OOO0 #line:129
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
def get_json_data (O0O0OOOO00OO0000O ,OOO0OO0OO00O0000O ,O00O000O0000O0OOO ,OOOOOOO000O00OOOO ):#line:153
    with open (O0O0OOOO00OO0000O ,'rb')as OOOOO00O00O00O000 :#line:154
        O00OOOO000OOO0OO0 =json .load (OOOOO00O00O00O000 )#line:155
        O00OOOO000OOO0OO0 ['data'][OOO0OO0OO00O0000O ][O00O000O0000O0OOO ]=OOOOOOO000O00OOOO #line:156
        OO00O00O0000O0OOO =O00OOOO000OOO0OO0 #line:157
    OOOOO00O00O00O000 .close ()#line:158
    return OO00O00O0000O0OOO #line:159
def write_json_data (OO00OO0OOO00000OO ):#line:162
    with open (json_path1 ,'w')as O00OOOO00000O0000 :#line:163
        json .dump (OO00OO0OOO00000OO ,O00OOOO00000O0000 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O00OOOO00000O0000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OOO0OOOOO00OOOO0O ,O0000OOOO0OO0OO00 ,OO000OO00OO0OOOOO ,O0OOOO0OOO00O0O00 ):#line:171
        try :#line:172
            OOO0OOOOO00OOOO0O .msg =OO000OO00OO0OOOOO #line:173
            OOO0OOOOO00OOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OOO0OOOOO00OOOO0O .token =O0000OOOO0OO0OO00 ['authorization']#line:175
            OOO0OOOOO00OOOO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OOO0OOOOO00OOOO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OOO0OOOOO00OOOO0O .elephant_user =O0000OOOO0OO0OO00 ['elephant_user']#line:178
            OOO0OOOOO00OOOO0O .elephant_pswd =O0000OOOO0OO0OO00 ['elephant_pswd']#line:179
            OOO0OOOOO00OOOO0O .elephant_Task_ID =O0000OOOO0OO0OO00 ['elephant_Task_ID']#line:180
            OOO0OOOOO00OOOO0O .len_new =O0OOOO0OOO00O0O00 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOO00000O0O000OOO ):#line:186
        try :#line:187
            OOO00000O0O000OOO .watched_ad ()#line:189
            OOO00OO00O0OO0000 =f'__{timi_new()}'#line:190
            OOO0OO00O0000O0OO ={'source':'scsc','authorization':OOO00000O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00O0OO0000 ),'signstring':OOO00OO00O0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0OOO0OO000OO0O00 =requests .request ('get',f'{host}/user',headers =OOO0OO00O0000O0OO ).json ()#line:202
            if 'status'in O0OOO0OO000OO0O00 :#line:204
                if O0OOO0OO000OO0O00 ['status']==200 :#line:205
                    O0O0000000O0O00O0 =O0OOO0OO000OO0O00 ['data']['nickname']#line:206
                    O000O0O00O00000OO =O0OOO0OO000OO0O00 ['data']['inner_id']#line:207
                    O000OOOO0O00OO000 =O0OOO0OO000OO0O00 ['data']['assets']['gold']#line:208
                    OO0O0O00OO00OOOO0 =O0OOO0OO000OO0O00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0O0000000O0O00O0[:5]}丨ID:{O000O0O00O00000OO}丨等级:{OO0O0O00OO00OOOO0}丨金种子:{str(O000OOOO0O00OO000).split(".")[0]}')#line:211
                    if 'wx_'in O0O0000000O0O00O0 :#line:212
                        OOO00000O0O000OOO .change_nickname ()#line:213
                if O0OOO0OO000OO0O00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOO00000O0O000OOO .elephant_user =='f':#line:216
                        return False #line:217
                    O0O0O0OO0OOOOOO00 =Invalid_login .addtask (elephant_user =OOO00000O0O000OOO .elephant_user ,elephant_pswd =OOO00000O0O000OOO .elephant_pswd ,elephant_Task_ID =OOO00000O0O000OOO .elephant_Task_ID )#line:220
                    O0000000OOOOOOOO0 =get_json_data (json_path ,OOO00000O0O000OOO .len_new ,'authorization',O0O0O0OO0OOOOOO00 )#line:221
                    if write_json_data (O0000000OOOOOOOO0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0OOO0OO000OO0O00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O00OOOOOOO0O00O00 :#line:228
            print (O00OOOOOOO0O00O00 )#line:229
    def sealing (O00OO0000O00OOOOO ):#line:232
        try :#line:233
            OO0000000O0OO0O00 =f'__{timi_new()}'#line:234
            OO0000O0OOOOO0OOO ={'source':'scsc','authorization':O00OO0000O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O0OO0O00 ),'signstring':OO0000000O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0000O0OOOOO0OOO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO0000O0OOOOO0OOO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0000O0OOOOO0OOO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0000O0OOOOO0OOO )#line:249
            requests .request ('get',f'{host}/user',headers =OO0000O0OOOOO0OOO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0000O0OOOOO0OOO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0000O0OOOOO0OOO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0000O0OOOOO0OOO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO0000O0OOOOO0OOO )#line:254
            requests .request ('get',f'{host}/assets',headers =OO0000O0OOOOO0OOO )#line:255
        except Exception as OO000OO00O0O0000O :#line:256
            print (OO000OO00O0O0000O )#line:257
    def ddd (OO0OOO0O00O0O0OOO ):#line:259
        try :#line:260
            OOOO00OO00000OO00 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO0OOO0OOO00OO00O ={'source':'scsc','authorization':OO0OOO0O00O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00000OO00 ),'signstring':OOOO00OO00000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0OOO00O000OOOO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OOO0OOO00OO00O ).json ()#line:273
            print (OO0OOO00O000OOOO0 )#line:274
        except Exception as OOO00O000OO0000O0 :#line:277
            print (OOO00O000OO0000O0 )#line:278
    def the_query (OOO0000OOO0000O0O ):#line:283
        try :#line:284
            O00O0O0O00O00OOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OOOO000O000OO000O ={'authorization':OOO0000OOO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O00O00OOOO ),'signstring':O00O0O0O00O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O000OOOOO0O00OO0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOOO000O000OO000O ).json ()#line:296
            if 'status'in O000OOOOO0O00OO0O :#line:298
                if O000OOOOO0O00OO0O ['status']==200 :#line:299
                    return O000OOOOO0O00OO0O ['data']['rows'][4 ]['price']#line:300
        except Exception as OOOO00OOO0O0OOO0O :#line:301
            print (OOOO00OOO0O0OOO0O )#line:302
    def market_sale (O0O00O0000OO00000 ,OO000O00OOOO0OO0O ):#line:305
        try :#line:306
            O0OO0O000OOO0OOO0 =timi_new ()#line:307
            OOO0O0OOOOOOO0OOO =f'type=crop__{O0OO0O000OOO0OOO0}'#line:308
            OOO00OO0OO0O0OOOO ={'source':'scsc','authorization':O0O00O0000OO00000 .token ,'timestamp':str (O0OO0O000OOO0OOO0 ),'sign':sign (OOO0O0OOOOOOO0OOO ),'signstring':OOO0O0OOOOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OO000O00O0O00OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOO00OO0OO0O0OOOO ).json ()#line:320
            if 'status'in O0OO000O00O0O00OO :#line:322
                if O0OO000O00O0O00OO ['status']==200 :#line:323
                    if O0OO000O00O0O00OO ['data']['rows']:#line:324
                        OO0O0OO0O0O0O0OOO =O0OO000O00O0O00OO ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0O00OOO0OO00OO0O =O0OO000O00O0O00OO ['data']['rows'][0 ]['quantity']#line:326
                        if float (OO000O00OOOO0OO0O )>6 :#line:327
                            O0O0O00O000O0OOO0 =f'_packsackItemId={OO0O0OO0O0O0O0OOO}&price={str(OO000O00OOOO0OO0O)[:5]}&quantity={O0O00OOO0OO00OO0O}_{O0OO0O000OOO0OOO0}'#line:328
                            OOOO0OO0O0OO00O00 ={'source':'scsc','authorization':O0O00O0000OO00000 .token ,'timestamp':str (O0OO0O000OOO0OOO0 ),'sign':sign (O0O0O00O000O0OOO0 ),'signstring':O0O0O00O000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOO000OO0O0OOO0OO ={"packsackItemId":OO0O0OO0O0O0O0OOO ,"price":str (OO000O00OOOO0OO0O )[:5 ],"quantity":str (O0O00OOO0OO00OO0O )}#line:344
                            OOOOO000O00O0O00O =requests .request ('post',f'{host}/market/sale',headers =OOOO0OO0O0OO00O00 ,data =OOO000OO0O0OOO0OO ).json ()#line:345
                            if 'status'in OOOOO000O00O0O00O :#line:347
                                if OOOOO000O00O0O00O ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O0O00OOO0OO00OO0O}丨价格:{str(OO000O00OOOO0OO0O)[:5]}')#line:349
                                if OOOOO000O00O0O00O ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{OOOOO000O00O0O00O["message"]}')#line:351
        except Exception as OOO0OO000O00O0000 :#line:352
            print (OOO0OO000O00O0000 )#line:353
    def query_to_sell (O0OO000OO0O000OOO ):#line:356
        global count_list #line:357
        try :#line:358
            O0OO00OO00O0O0OOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOO0O00O0OO000O00 ={'source':'scsc','authorization':O0OO000OO0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00O0O0OOO ),'signstring':O0OO00OO00O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O000OOOOO0O00OO00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0O00O0OO000O00 ).json ()#line:371
            if 'status'in O000OOOOO0O00OO00 :#line:373
                if O000OOOOO0O00OO00 ['status']==200 :#line:374
                    for OO0OOOOO000000OO0 in O000OOOOO0O00OO00 ['data']['rows']:#line:375
                        O0O00O0OO0O00OO0O =OO0OOOOO000000OO0 ['materialKey']#line:376
                        OO0O0OO0OO000O0OO =OO0OOOOO000000OO0 ['quantity']#line:377
                        OO00OOO00O000OO00 =OO0OOOOO000000OO0 ['price']#line:378
                        O00OO0O0OO00OOO0O =OO0OOOOO000000OO0 ['saleState']#line:379
                        if O00OO0O0OO00OOO0O ==0 :#line:380
                            print (f'【出售订单】:名称:{O0O00O0OO0O00OO0O}丨数量:{OO0O0OO0OO000O0OO}丨价格:{OO00OOO00O000OO00}')#line:381
                            count_list +=OO0O0OO0OO000O0OO #line:382
                            OOO0O0OO0O00O0O0O =O0OO000OO0O000OOO .the_query ()#line:384
                            if float (OOO0O0OO0O00O0O0O )!=float (OO00OOO00O000OO00 ):#line:385
                                O0O0OOO0O0O0000O0 =OO0OOOOO000000OO0 ['id']#line:386
                                O0OO000OO0O000OOO .cacel_sale (O0O0OOO0O0O0000O0 )#line:387
                    O0OO000OO0O000OOO .game_map ()#line:389
        except Exception as OO00O0O0O0O000000 :#line:391
            print (OO00O0O0O0O000000 )#line:392
    def cacel_sale (OOOO000O0O0O00000 ,OOO0O00O00OO0OO00 ):#line:395
        try :#line:396
            OOOO00O0O0OO0O0OO =f'_saleId={OOO0O00O00OO0OO00}_{timi_new()}'#line:397
            O00O000OO00O000O0 ={'source':'scsc','authorization':OOOO000O0O0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O0OO0O0OO ),'signstring':OOOO00O0O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O0O0OOOOOOO000000 ={"saleId":OOO0O00O00OO0OO00 }#line:409
            O000OOOOOO00O0OOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00O000OO00O000O0 ,data =O0O0OOOOOOO000000 ).json ()#line:410
            if 'status'in O000OOOOOO00O0OOO :#line:412
                if O000OOOOOO00O0OOO ['status']==200 :#line:413
                    print (f'【下架出售】:{O000OOOOOO00O0OOO["data"]}')#line:414
        except Exception as OO000O0OOO0O0OO00 :#line:415
            print (OO000O0OOO0O0OO00 )#line:416
    def change_nickname (O0O0OO00O0OO0O0O0 ):#line:419
        try :#line:420
            O000000OO0OO0OOO0 =timi_new ()#line:421
            OO000OOOOO00O00OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O000O00O0O0OO0O00 =requests .request ('post','https://www.qmsjmfb.com/',data =OO000OOOOO00O00OO ).text #line:423
            OO0000000OOO0O0O0 =re .findall ('<ul><li>(.*?)</li>',O000O00O0O0OO0O00 )[0 ][:3 ]#line:424
            OOO0O0O00O0O0O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0000000OOO0O0O0}').json ()#line:425
            O0O0000OO0000000O =OOO0O0O00O0O0O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            OO00O0O00OOOOO000 ={"nickname":O0O0000OO0000000O }#line:427
            O0O0OOO0O0OOOOOO0 =f'_nickname={O0O0000OO0000000O}_{O000000OO0OO0OOO0}'#line:428
            OO0O00OOO000O00OO ={'source':'scsc','authorization':O0O0OO00O0OO0O0O0 .token ,'timestamp':O000000OO0OO0OOO0 ,'sign':sign (O0O0OOO0O0OOOOOO0 ),'signstring':O0O0OOO0O0OOOOOO0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OOO0000O0OO0O000O =requests .request ('patch',f'{host}/user/nickname',headers =OO0O00OOO000O00OO ,data =OO00O0O00OOOOO000 ).json ()#line:440
            if 'status'in OOO0000O0OO0O000O :#line:442
                if OOO0000O0OO0O000O ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O0O0000OO0000000O}丨{OOO0000O0OO0O000O["message"]}')#line:444
        except Exception as O0000O000000O0000 :#line:445
            print (O0000O000000O0000 )#line:446
    def withdraw (OO0O0O0OO0OOO0O00 ):#line:449
        try :#line:450
            OOOOO0O0O0OOO00OO =f'__{timi_new()}'#line:451
            O0OO000O000OOO000 ={'source':'scsc','authorization':OO0O0O0OO0OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0O0OOO00OO ),'signstring':OOOOO0O0O0OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOOO0O000O0OOO000 =requests .request ('get',f'{host}/assets',headers =O0OO000O000OOO000 ).json ()#line:463
            if 'status'in OOOO0O000O0OOO000 :#line:465
                if OOOO0O000O0OOO000 ['status']==200 :#line:466
                    OOOOOOOOOOOOOOO00 =OOOO0O000O0OOO000 ['data']['cash']#line:467
                    if float (OOOOOOOOOOOOOOO00 )>20 :#line:468
                        OOOOO0O0O0OOO00OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O0OO000O000OOO000 ={'authorization':OO0O0O0OO0OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0O0OOO00OO ),'signstring':OOOOO0O0O0OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OOO0O000OOO0OO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OO0O000000000O000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OO000O000OOO000 ,data =OOO0O000OOO0OO0O0 ).json ()#line:482
                        if 'status'in OO0O000000000O000 :#line:484
                            if OO0O000000000O000 ['status']==200 :#line:485
                                print (f'【余额提现】:{OO0O000000000O000["data"]}')#line:486
                        if 'status'in OO0O000000000O000 :#line:487
                            if OO0O000000000O000 ['status']==500 :#line:488
                                print (f'【余额提现】:{OO0O000000000O000["message"]}')#line:489
        except Exception as O00OO00OO000OOOOO :#line:490
            print (O00OO00OO000OOOOO )#line:491
    def invitenum (OOO0O0OOOOO000000 ):#line:494
        global invited_new #line:495
        try :#line:496
            O0OOO0OO0OO00OOO0 =f'__{timi_new()}'#line:497
            O0OOO0O00O0000O0O ={'source':'scsc','authorization':OOO0O0OOOOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0OO00OOO0 ),'signstring':O0OOO0OO0OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OOO0OO000OO0000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOO0O00O0000O0O ).json ()#line:509
            if 'status'in OOO0OO000OO0000O0 :#line:511
                if OOO0OO000OO0000O0 ['status']==200 :#line:512
                    O000000OO0OOO0000 =OOO0OO000OO0000O0 ['data']['invited_count']#line:513
                    OO00000O0O00OOO0O =OOO0OO000OO0000O0 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{O000000OO0OOO0000}丨间邀好友:{OO00000O0O00OOO0O}')#line:515
                    if O000000OO0OOO0000 <2 :#line:516
                        OOO0O00OO00O00O0O =f'__{timi_new()}'#line:517
                        OO000OOO0OO00O000 ={'source':'scsc','authorization':OOO0O0OOOOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO00O00O0O ),'signstring':OOO0O00OO00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        O00O0OOOO0O00000O =requests .request ('get',f'{host}/user',headers =OO000OOO0OO00O000 ).json ()#line:529
                        if 'status'in O00O0OOOO0O00000O :#line:531
                            if O00O0OOOO0O00000O ['status']==200 :#line:532
                                invited_new .append (O00O0OOOO0O00000O ['data']['inner_id'])#line:533
        except Exception as OOO0OO000OO0OOOO0 :#line:534
            print (OOO0OO000OO0OOOO0 )#line:535
    def game_map (OO0OO00O0O00O000O ):#line:538
        try :#line:539
            O0O0O0OOOO0000OOO =f'__{timi_new()}'#line:540
            O00O0O0OOO0O000OO ={'source':'scsc','authorization':OO0OO00O0O00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO0000OOO ),'signstring':O0O0O0OOOO0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OO0OO00O0OO0O000O =requests .request ('get',f'{host}/game/map',headers =O00O0O0OOO0O000OO ).json ()#line:552
            if 'status'in OO0OO00O0OO0O000O :#line:554
                if OO0OO00O0OO0O000O ['status']==200 :#line:555
                    for O000O0O0OO000OO00 in OO0OO00O0OO0O000O ['data']['list'][0 ]['crops']:#line:556
                        OOO0O000O00000000 =O000O0O0OO000OO00 ['level']#line:558
                        if OOO0O000O00000000 ==41 :#line:559
                            O000000OO0000000O =O000O0O0OO000OO00 ['crop_name']#line:560
                            O0OO00O00OOOOOOO0 =O000O0O0OO000OO00 ['count']#line:561
                            if O0OO00O00OOOOOOO0 >0 :#line:562
                                print (f'【农业资产】:{O000000OO0000000O}丨数量:{O0OO00O00OOOOOOO0}')#line:563
                                OOOOOOO0OO0O0O000 =OO0OO00O0O00O000O .the_query ()#line:564
                                OO0OO00O0O00O000O .market_sale (OOOOOOO0OO0O0O000 )#line:565
        except Exception as O0OOOOO0OOOOOO000 :#line:566
            print (O0OOOOO0OOOOOO000 )#line:567
    def give_gold (OO0OO0OOO0O000OOO ):#line:570
        try :#line:571
            O00O0O000OO0OOO00 =f'__{timi_new()}'#line:572
            OO0OOO000O0O00O00 ={'source':'scsc','authorization':OO0OO0OOO0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000OO0OOO00 ),'signstring':O00O0O000OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOOO0OO0O000O0O00 =requests .request ('get',f'{host}/user',headers =OO0OOO000O0O00O00 ).json ()#line:584
            if 'status'in OOOO0OO0O000O0O00 :#line:585
                if OOOO0OO0O000O0O00 ['status']==200 :#line:586
                    if float (OO0OO0OOO0O000OOO .doneeNo )!=0 :#line:587
                        OOOO0OOO0O0O0O0OO =OOOO0OO0O000O0O00 ['data']['assets']['gold']#line:588
                        if float (OOOO0OOO0O0O0O0OO )>float (OO0OO0OOO0O000OOO .innerId ):#line:589
                            O0O0O00OO0OOOO0O0 =int (float (OOOO0OOO0O0O0O0OO )/1.1 )#line:590
                            O00O0O000OO0OOO00 =f'_doneeNo={OO0OO0OOO0O000OOO.doneeNo}&quantity={O0O0O00OO0OOOO0O0}_{timi_new()}'#line:591
                            OO0OOO000O0O00O00 ={'source':'scsc','authorization':OO0OO0OOO0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000OO0OOO00 ),'signstring':O00O0O000OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OOOOO0O0O00OOOO0O ={"quantity":O0O0O00OO0OOOO0O0 ,"doneeNo":OO0OO0OOO0O000OOO .doneeNo }#line:606
                            O000000OOOO000O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OOO000O0O00O00 ,data =OOOOO0O0O00OOOO0O ).json ()#line:607
                            if 'status'in O000000OOOO000O00 :#line:609
                                if O000000OOOO000O00 ['status']==200 :#line:610
                                    if O000000OOOO000O00 ['data']:#line:611
                                        print (f'【赠送种子】:赠送{O0O0O00OO0OOOO0O0}种子给{OO0OO0OOO0O000OOO.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O0O0000OO00000OO0 :#line:615
            print (O0O0000OO00000OO0 )#line:616
    def invitation (O0O0O00O00OO00O00 ):#line:618
        try :#line:619
            _O0OOO0O0O000O000O =float (bundled_def ())/4 #line:620
            OO00000OOO0OOO000 =f'_innerId={int(_O0OOO0O0O000O000O)}_{timi_new()}'#line:622
            O000O000OO00O000O ={'source':'scsc','authorization':O0O0O00O00OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOO0OOO000 ),'signstring':OO00000OOO0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            O000O00OO0O00O00O ={"innerId":int (_O0OOO0O0O000O000O )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000O000OO00O000O ,data =O000O00OO0O00O00O )#line:635
        except Exception as O0OOOO00OO0OOO00O :#line:636
            print (O0OOOO00OO0OOO00O )#line:637
    def winning_rewards (OO000OO0O0OOOO000 ):#line:640
        try :#line:641
            OOO00OO0OO0OO000O =f'__{timi_new()}'#line:642
            O0OOO0OOO0O00O00O ={'source':'scsc','authorization':OO000OO0O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OO0OO000O ),'signstring':OOO00OO0OO0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OOOOO0OO00O000000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOO0OOO0O00O00O ).json ()#line:654
            if 'status'in OOOOO0OO00O000000 :#line:656
                if OOOOO0OO00O000000 ['status']==200 :#line:657
                    if OOOOO0OO00O000000 ['data']['amount']:#line:658
                        OOO0000000O0OO00O =OOOOO0OO00O000000 ['data']['amount']['gold']#line:659
                        return OOO0000000O0OO00O #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OO000O0OOO0O00O00 :#line:663
            print (OO000O0OOO0O00O00 )#line:664
    def certification (O0O0O00O0000OOO00 ):#line:667
        try :#line:668
            OO00O0OOOOOO0O000 =f'__{timi_new()}'#line:669
            O00OO0O000OOO0000 ={'source':'scsc','authorization':O0O0O00O0000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OOOOOO0O000 ),'signstring':OO00O0OOOOOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O000OOO0OOO0O0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O000OOO0000 ).json ()#line:681
            if 'status'in O000OOO0OOO0O0O00 :#line:683
                if O000OOO0OOO0O0O00 ['status']==200 :#line:684
                    if O000OOO0OOO0O0O00 ['data']['result']:#line:685
                        OOO0OO0OOO0OO000O =O000OOO0OOO0O0O00 ['data']['nick_name']#line:686
                        return OOO0OO0OOO0OO000O #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O00OOOOO0000OO000 :#line:690
            print (O00OOOOO0000OO000 )#line:691
    def crops_illustrated (O00O0000O0O0OO00O ):#line:694
        try :#line:695
            O0000OO0OOOOO0O0O =f'__{timi_new()}'#line:696
            O000000OOOOOOO0OO ={'source':'scsc','authorization':O00O0000O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0OOOOO0O0O ),'signstring':O0000OO0OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O0OOO0O000000O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000000OOOOOOO0OO ).json ()#line:708
            if 'status'in O0OOO0O000000O0O0 :#line:710
                if O0OOO0O000000O0O0 ['status']==200 :#line:711
                    O0O000000O0OO00OO =O0OOO0O000000O0O0 ['data'][0 ]['crops']#line:712
                    for O0O000OOO0OOO00O0 in O0O000000O0OO00OO :#line:713
                        if O0O000OOO0OOO00O0 ['ill_clover_award']:#line:714
                            if float (O0O000OOO0OOO00O0 ['ill_clover_award'])>1 :#line:715
                                if O0O000OOO0OOO00O0 ['is_finish']:#line:716
                                    if not O0O000OOO0OOO00O0 ['is_getit']:#line:717
                                        if O00O0000O0O0OO00O .certification ()!='未实名':#line:718
                                            O0000OO0OOOOO0O0O =f'_award_level={O0O000OOO0OOO00O0["level"]}_{timi_new()}'#line:719
                                            O000000OOOOOOO0OO ={'source':'scsc','authorization':O00O0000O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0OOOOO0O0O ),'signstring':O0000OO0OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            OOO0000OOO0O000O0 ={"award_level":O0O000OOO0OOO00O0 ['level']}#line:731
                                            O0OO00O0O00OOO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000000OOOOOOO0OO ,json =OOO0000OOO0O000O0 ).json ()#line:733
                                            if 'status'in O0OO00O0O00OOO0O0 :#line:734
                                                if O0OO00O0O00OOO0O0 ['status']==200 :#line:735
                                                    O00O0OO0000O0OO00 =O0OO00O0O00OOO0O0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O0O000OOO0OOO00O0["crop_name"]}成就丨奖励{O00O0OO0000O0OO00}☘️')#line:738
                                                if O0OO00O0O00OOO0O0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{O0OO00O0O00OOO0O0["message"]}')#line:740
        except Exception as O0000O00000OOO00O :#line:741
            print (O0000O00000OOO00O )#line:742
    def watched_ad (O00OO0O000OO0O00O ):#line:745
        try :#line:746
            O000OOO000OO0000O =f'__{timi_new()}'#line:747
            OO0000O00O00000O0 ={'source':'scsc','authorization':O00OO0O000OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO000OO0000O ),'signstring':O000OOO000OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            O000OOO00OOOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0000O00O00000O0 ).json ()#line:759
            if 'status'in O000OOO00OOOOOOOO :#line:761
                if O000OOO00OOOOOOOO ['status']==200 :#line:762
                    if 'offlineInfo'in O000OOO00OOOOOOOO ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OOO0OOO0O000OOO00 =O000OOO00OOOOOOOO ['data']['offlineInfo']['off_minute']#line:765
                        O0OOOOOOOO00OO0OO =float (O000OOO00OOOOOOOO ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0000O00O00000O0 ).json ()#line:768
                        time .sleep (2 )#line:769
                        OOOO00OOOO0000000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0000O00O00000O0 ).json ()#line:770
                        if 'status'in OOOO00OOOO0000000 :#line:772
                            if OOOO00OOOO0000000 ['status']==200 :#line:773
                                OO0OOO00000OO0OOO =float (OOOO00OOOO0000000 ['data']['silver'])/1000000000000 #line:774
                                O00O000O0OOOO00O0 =str (OO0OOO00000OO0OOO -O0OOOOOOOO00OO0OO )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OOO0OOO0O000OOO00}分钟奖励🌱数量:{O00O000O0OOOO00O0}t粒')#line:776
        except Exception as O0OOO0O0O0OO00O00 :#line:777
            print (O0OOO0O0O0OO00O00 )#line:778
    def user_ad (OO00O000O0OO0OOOO ):#line:781
        try :#line:782
            OO00O00O0OOO0O0O0 =f'__{timi_new()}'#line:783
            OO0O0O0O0OO0O0O0O ={'source':'scsc','authorization':OO00O000O0OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O0OOO0O0O0 ),'signstring':OO00O00O0OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            OOO00O00OOOOO0O00 =requests .request ('get',f'{host}/user/ad',headers =OO0O0O0O0OO0O0O0O ).json ()#line:795
            if 'status'in OOO00O00OOOOO0O00 :#line:797
                if OOO00O00OOOOO0O00 ['status']==200 :#line:798
                    OO0O00O0O00OOOO00 =OOO00O00OOOOO0O00 ['data']['max_time']#line:799
                    OO0O0OO000OOO000O =OOO00O00OOOOO0O00 ['data']['watch_time']#line:800
                    OO00OOOO0O0000000 =OOO00O00OOOOO0O00 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{OO00OOOO0O0000000 + OO0O00O0O00OOOO00 - OO0O0OO000OOO000O}次丨好友提供:{OO00OOOO0O0000000}次')#line:802
                    if OO00OOOO0O0000000 +OO0O00O0O00OOOO00 -OO0O0OO000OOO000O >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OOOO00OO000000OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0O0O0O0OO0O0O0O ).json ()#line:805
                        if 'status'in OOOO00OO000000OO0 :#line:807
                            if OOOO00OO000000OO0 ['status']==200 :#line:808
                                OO000O0O00OOOOO0O =float (OOOO00OO000000OO0 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OO000O0O00OOOOO0O)}t粒')#line:810
                                return True #line:811
                            if OOOO00OO000000OO0 ['status']==500 :#line:812
                                O0OO00O0OO0OOOO00 =OOOO00OO000000OO0 ['message']#line:813
                                print (f'【获取种子】:{O0OO00O0OO0OOOO00}')#line:814
                                return False #line:815
        except Exception as OOOO0O000O000OOO0 :#line:816
            print (OOOO0O000O000OOO0 )#line:817
    def synthetic (O0O000000OO0O0000 ):#line:820
        global id ,g #line:821
        try :#line:822
            OO0OOOO0O0OOOO00O =O0O000000OO0O0000 .level_new ()#line:823
            OO000O00OO0OO0OO0 =random .randint (9 ,11 )#line:824
            OO00OO00O000OOO00 =f'_site=8&targetSite={OO000O00OO0OO0OO0}_{timi_new()}'#line:825
            OO00OO000O0000000 ={'source':'scsc','authorization':O0O000000OO0O0000 .token ,'timestamp':timi_new (),'sign':sign (OO00OO00O000OOO00 ),'signstring':OO00OO00O000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OOOOOOO00O0OO0OO0 ={"site":int (8 ),"targetSite":int (OO000O00OO0OO0OO0 )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO00OO000O0000000 ,json =OOOOOOO00O0OO0OO0 )#line:838
            while True :#line:839
                OOOOO0000OOO00OO0 =f'__{timi_new()}'#line:840
                OO000OO00O0O0OO0O ={'source':'scsc','authorization':O0O000000OO0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0000OOO00OO0 ),'signstring':OOOOO0000OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O0O00OOOO000O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OO000OO00O0O0OO0O ).json ()#line:852
                if 'status'in O0O00OOOO000O0000 :#line:854
                    if O0O00OOOO000O0000 ['status']==200 :#line:855
                        O0OO0O0OOO0000O0O =O0O00OOOO000O0000 ['data']['cropList']#line:856
                        O000OO000OO000OOO =O0O00OOOO000O0000 ['data']['gameCoreDataDBid']#line:857
                        OO0OO0O0O0O0OOO00 =float (O0O00OOOO000O0000 ['data']['silver'])/1000000000000 #line:858
                        O0OOOOO000O0OO0O0 =0 #line:863
                        for OO0O000O0O00OOOOO in O0OO0O0OOO0000O0O :#line:864
                            if not OO0O000O0O00OOOOO :#line:865
                                OO00O0000O00OOO00 =f'_crop_id={O000OO000OO000OOO}&site={O0OOOOO000O0OO0O0}_{O0O000000OO0O0000.time}'#line:866
                                OOOOOO000O0OOO0O0 ={'source':'scsc','authorization':O0O000000OO0O0000 .token ,'timestamp':O0O000000OO0O0000 .time ,'sign':sign (OO00O0000O00OOO00 ),'signstring':OO00O0000O00OOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                OOOO000OO000O000O ={"site":O0OOOOO000O0OO0O0 ,"crop_id":O000OO000OO000OOO }#line:877
                                OOO00OO0O00OO0O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOO000O0OOO0O0 ,data =OOOO000OO000O000O ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOO00OO0O00OO0O0O :#line:881
                                    if OOO00OO0O00OO0O0O ['status']==200 :#line:882
                                        if OOO00OO0O00OO0O0O ['message']=='种子数量不足':#line:883
                                            OO0OOOO0O0OOOO00O =O0O000000OO0O0000 .level_new ()#line:884
                                            print (f'【种植合成】:{OOO00OO0O00OO0O0O["message"]}')#line:885
                                            if not O0O000000OO0O0000 .user_ad ():#line:886
                                                return False #line:887
                                    if OOO00OO0O00OO0O0O ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOO00OO0O00OO0O0O["message"]}')#line:889
                                        return False #line:890
                            O0OOOOO000O0OO0O0 +=1 #line:891
                        O00O000O00O0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO000OO00O0O0OO0O ).json ()#line:892
                        OOOOO000O00OO0OOO =O00O000O00O0OOOO0 ['data']['cropList']#line:893
                        O0000O00OOOO00OO0 =False #line:894
                        for OO0O000O0O00OOOOO in range (12 ):#line:895
                            id =OOOOO000O00OO0OOO [OO0O000O0O00OOOOO ]['level']#line:896
                            if float (OO0OOOO0O0OOOO00O )-float (id )>9 :#line:897
                                OOOO00O0O000OO00O =f'_site={OO0O000O0O00OOOOO}_{timi_new()}'#line:898
                                OO0O0OOOO0000O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000000OO0O0000 .token ,'timestamp':timi_new (),'sign':sign (OOOO00O0O000OO00O ),'signstring':OOOO00O0O000OO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                OOO000OOO0OOO00O0 ={"site":OO0O000O0O00OOOOO }#line:910
                                O00000OOO0O0OOO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O0OOOO0000O0OO ,data =OOO000OOO0OOO00O0 ).json ()#line:912
                                if 'status'in O00000OOO0O0OOO0O :#line:913
                                    if O00000OOO0O0OOO0O ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for O00000OO0OOO0OO0O in range (11 ):#line:917
                                    OOO00O0O0000O00OO =O00000OO0OOO0OO0O +1 #line:918
                                    g =OOOOO000O00OO0OOO [OOO00O0O0000O00OO ]['level']#line:919
                                    if id ==g :#line:920
                                        OOOOO0OOOO0OO0OO0 =O00000OO0OOO0OO0O +2 #line:921
                                        if OOOOO0OOOO0OO0OO0 !=OO0O000O0O00OOOOO +1 :#line:922
                                            OO0OO0000O0000O00 =OO0O000O0O00OOOOO +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            OO00OO00O000OOO00 =f'_site={OO0OO0000O0000O00 - 1}&targetSite={OOOOO0OOOO0OO0OO0 - 1}_{timi_new()}'#line:926
                                            OO00OO000O0000000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000000OO0O0000 .token ,'timestamp':timi_new (),'sign':sign (OO00OO00O000OOO00 ),'signstring':OO00OO00O000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            O0000OO0OO0000000 ={"site":int (OO0OO0000O0000O00 -1 ),"targetSite":int (OOOOO0OOOO0OO0OO0 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00OO000O0000000 ,json =O0000OO0OO0000000 )#line:945
                                            O0000O00OOOO00OO0 =True #line:947
                                    if O0000O00OOOO00OO0 :#line:948
                                        break #line:949
                                if O0000O00OOOO00OO0 :#line:950
                                    break #line:951
        except :#line:952
            O0O000000OO0O0000 .synthetic ()#line:953
    def level_new (O000O0O00OO0O0OO0 ):#line:956
        try :#line:957
            O000O00000000OOOO =f'__{timi_new()}'#line:958
            OO0OO0OOOO0O0OOO0 ={'source':'scsc','authorization':O000O0O00OO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00000000OOOO ),'signstring':O000O00000000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            OOO0OO0O0O0O00OO0 =requests .request ('get',f'{host}/user',headers =OO0OO0OOOO0O0OOO0 ).json ()#line:970
            if 'status'in OOO0OO0O0O0O00OO0 :#line:971
                if OOO0OO0O0O0O00OO0 ['status']==200 :#line:972
                    return float (OOO0OO0O0O0O00OO0 ['data']['level'])#line:973
        except Exception as O000O0O00O00O00OO :#line:974
            print (O000O0O00O00O00OO )#line:975
    def propsraffle (O00OO00O000OOO0O0 ):#line:978
        try :#line:979
            while True :#line:980
                OOOO0OOOOOO0OOOO0 =f'__{timi_new()}'#line:981
                OOO0000OOOO00000O ={'source':'scsc','authorization':O00OO00O000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOO0OOOO0 ),'signstring':OOOO0OOOOOO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OO0OOOO00OO00OO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0000OOOO00000O ).json ()#line:993
                if 'status'in OO0OOOO00OO00OO00 :#line:995
                    if OO0OOOO00OO00OO00 ['status']==200 :#line:996
                        OO00O0OO0O0O0OOOO =OO0OOOO00OO00OO00 ['data']['rows']#line:997
                        O000O0OOOO00000OO =OO0OOOO00OO00OO00 ['data']['vstate']#line:998
                        if OO00O0OO0O0O0OOOO ==5 or OO00O0OO0O0O0OOOO ==6 or OO00O0OO0O0O0OOOO ==7 :#line:999
                            O00OO00O000O00000 =OO0OOOO00OO00OO00 ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O00OO00O000O00000}')#line:1001
                        if OO00O0OO0O0O0OOOO ==1 or OO00O0OO0O0O0OOOO ==2 or OO00O0OO0O0O0OOOO ==3 :#line:1002
                            OO00OO0O0O0O0O0O0 =OO0OOOO00OO00OO00 ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{OO00OO0O0O0O0O0O0}')#line:1004
                        if OO00O0OO0O0O0OOOO ==4 or OO00O0OO0O0O0OOOO ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OO00O0OO0O0O0OOOO =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OOO00000OOOOOO00O :#line:1046
            print (OOO00000OOOOOO00O )#line:1047
    def friends_invitation (OOO0O00OOO000O00O ):#line:1050
        try :#line:1051
            O000O00O0OOOO0OO0 =f'__{timi_new()}'#line:1052
            OOOO0OO0O00O00O0O ={'source':'scsc','authorization':OOO0O00OOO000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0OOOO0OO0 ),'signstring':O000O00O0OOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O00OO0O0O0OO0O000 =requests .request ('get',f'{host}/friends',headers =OOOO0OO0O00O00O0O ).json ()#line:1064
            if 'status'in O00OO0O0O0OO0O000 :#line:1065
                if O00OO0O0O0OO0O000 ['status']==200 :#line:1066
                    O00O0O00OO000OOOO =O00OO0O0O0OO0O000 ['data']['myInviteter']#line:1067
                    if O00O0O00OO000OOOO :#line:1068
                        O000O00OOOO0O0000 =O00O0O00OO000OOOO ['user']['nickname']#line:1069
                        OO0OO0O0OO00O00OO =OOO0O00OOO000O00O .certification ()#line:1070
                        if OO0OO0O0OO00O00OO =='未实名':#line:1071
                            weishim .append (OOO0O00OOO000O00O .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O000O00OOOO0O0000}丨实名:{OO0OO0O0OO00O00OO}')#line:1073
        except Exception as OOO00OO0OOO00OO00 :#line:1077
            print (OOO00OO0OOO00OO00 )#line:1078
    def add_clover (O0OOO0OOOOOO0OOO0 ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            OO000O00OO000OOOO =f'__{timi_new()}'#line:1084
            O0OO0000OOO00OO0O ={'source':'scsc','authorization':O0OOO0OOOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO000OOOO ),'signstring':OO000O00OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO0OOO0O000OO0000 =requests .request ('get',f'{host}/assets/clovers',headers =O0OO0000OOO00OO0O ).json ()#line:1096
            if 'status'in OO0OOO0O000OO0000 :#line:1098
                if OO0OOO0O000OO0000 ['status']==200 :#line:1099
                    O00OOO0OO0OOOO000 =OO0OOO0O000OO0000 ['data']['clover']#line:1100
                    O0OOOOOOOOO00O00O =OO0OOO0O000OO0000 ['data']['used_clover']#line:1101
                    O0O0O00OO00O0OOOO =float (O00OOO0OO0OOOO000 )-float (O0OOOOOOOOO00O00O )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOOOOOOOO00O00O}')#line:1103
                    if O0OOO0OOOOOO0OOO0 .certification ()!='未实名':#line:1104
                        if O0O0O00OO00O0OOOO >1 :#line:1105
                            OO000O00OO000OOOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0O00OO00O0OOOO)}_{timi_new()}'#line:1106
                            OOOOO00OO00OO0OOO ={'source':'scsc','authorization':O0OOO0OOOOOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO000OOOO ),'signstring':OO000O00OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OO0OO0O00OO000OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0O00OO00O0OOOO )}#line:1118
                            OO000O000O0O0OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO00OO00OO0OOO ,data =OO0OO0O00OO000OOO ).json ()#line:1119
                            if 'status'in OO000O000O0O0OO00 :#line:1121
                                if OO000O000O0O0OO00 ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{OO000O000O0O0OO00["data"]["isSuccess"]}丨数量:{O0O0O00OO00O0OOOO}')#line:1123
                                if OO000O000O0O0OO00 ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{OO000O000O0O0OO00["message"]}')#line:1125
            OOOOO0O000OOOOO0O =requests .request ('get',f'{host}/lottery',headers =O0OO0000OOO00OO0O ).json ()#line:1126
            OO000OO0000O0O0OO =O0OOO0OOOOOO0OOO0 .winning_rewards ()#line:1128
            if 'status'in OOOOO0O000OOOOO0O :#line:1129
                if OOOOO0O000OOOOO0O ['status']==200 :#line:1130
                    OO00OOO00OOO0000O =OOOOO0O000OOOOO0O ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OO00OOO00OOO0000O )#line:1132
                    OOOOO0O000O00OOO0 =OOOOO0O000OOOOO0O ['data'][1 ]['value']#line:1133
                    OO0O0O000O00OO0OO =OOOOO0O000OOOOO0O ['data'][0 ]['join_number']#line:1134
                    OO00O00OO0O0O0OOO =int (float (OOOOO0O000OOOOO0O ['data'][0 ]['totalValue']))#line:1135
                    OOOOO0OO00O00OO0O =float (OOOOO0O000O00OOO0 /OO00O00OO0O0O0OOO )*10000 #line:1136
                    O00OOOOO000OO00O0 =OO00O00OO0O0O0OOO /OO0O0O000O00OO0OO #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OO00OOO00OOO0000O)[:6]}颗金种子丨好友收益:{str(OO000OO0000O0O0OO)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOO0OO00O00OO0O)[:6]}颗金种子丨☘️人均:{str(O00OOOOO000OO00O0)[:7]}️')#line:1139
        except Exception as OO0OO00OO00O0O0O0 :#line:1140
            print (OO0OO00OO00O0O0O0 )#line:1141
    def energy (OOOO0O000OO0O00O0 ):#line:1144
        try :#line:1145
            while True :#line:1146
                O0OO000000OO00OOO =f'__{timi_new()}'#line:1147
                O000000O0O0O000O0 ={'source':'scsc','authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000000OO00OOO ),'signstring':O0OO000000OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                O00OO0OO0OOOOO000 =requests .request ('get',f'{host}/energy/general',headers =O000000O0O0O000O0 ).json ()#line:1159
                if 'status'in O00OO0OO0OOOOO000 :#line:1161
                    if O00OO0OO0OOOOO000 ['status']==200 :#line:1162
                        OOO00OOOOOOO0OO0O =O00OO0OO0OOOOO000 ['data']['ordinary_water']#line:1163
                        O0000O00O0000O0OO =O00OO0OO0OOOOO000 ['data']['ordinary_fertilizer']#line:1164
                        O0OOOO0O0OO0O0OO0 =O00OO0OO0OOOOO000 ['data']['videoStatus']#line:1165
                        O00OO0O0O00O00OOO =O00OO0OO0OOOOO000 ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0000O00O0000O0OO).split(".")[0]}丨水滴:{str(OOO00OOOOOOO0OO0O).split(".")[0]}')#line:1168
                        if float (O0000O00O0000O0OO )<96 :#line:1169
                            if O0OOOO0O0OO0O0OO0 :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                O00O00O0O0O000OOO =99 -float (O0000O00O0000O0OO )#line:1172
                                OO00000OOO0OO0OOO ={"fertilizer":str (O00O00O0O0O000OOO ).split ('.')[0 ]}#line:1173
                                OO0O00OO00OO0OO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000000O0O0O000O0 ).json ()#line:1175
                                if 'status'in OO0O00OO00OO0OO0O :#line:1177
                                    if OO0O00OO00OO0OO0O ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{OO0O00OO00OO0OO0O["message"]}')#line:1179
                                    if OO0O00OO00OO0OO0O ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OO0O00OO00OO0OO0O["message"]}')#line:1181
                                        break #line:1182
                                if float (O0000O00O0000O0OO )<78 :#line:1184
                                    O00O00O0O0O000OOO =80 -float (O0000O00O0000O0OO )#line:1185
                                    OOO0O0OO0OOOO000O =f'_fertilizer={int(O00O00O0O0O000OOO)}_{timi_new()}'#line:1186
                                    OO00O0OO0O00OO000 ={'source':'scsc','authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0OOOO000O ),'signstring':OOO0O0OO0OOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    OO00OOO0000O00O00 ={"fertilizer":int (O00O00O0O0O000OOO )}#line:1198
                                    OO0O000000O000O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00O0OO0O00OO000 ,data =OO00OOO0000O00O00 ).json ()#line:1200
                                    if 'status'in OO0O000000O000O0O :#line:1202
                                        if OO0O000000O000O0O ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OO0O000000O000O0O["message"]}丨数量:{int(O00O00O0O0O000OOO)}')#line:1204
                                        if OO0O000000O000O0O ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OO0O000000O000O0O["message"]}丨数量:{int(O00O00O0O0O000OOO)}')#line:1206
                                            OOOO0O0OO00O0000O =OO0O000000O000O0O ["message"].split ('-')[1 ]#line:1207
                                            O00OOO0OO000O0O00 =f'__{timi_new()}'#line:1208
                                            OO0O0000O00OO0O00 ={'source':'scsc','authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO000O0O00 ),'signstring':O00OOO0OO000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OO00000000OO00O0O =requests .request ('get',f'{host}/user',headers =OO0O0000O00OO0O00 ).json ()#line:1220
                                            if 'status'in OO00000000OO00O0O :#line:1221
                                                if OO00000000OO00O0O ['status']==200 :#line:1222
                                                    OOO0O0O0O0O0000O0 =OO00000000OO00O0O ['data']['inner_id']#line:1223
                                                    if give_gold (OOO0O0O0O0O0000O0 ,float (OOOO0O0OO00O0000O )+1 ):#line:1224
                                                        OOOO0O000OO0O00O0 .energy ()#line:1225
                        if float (OOO00OOOOOOO0OO0O )<880 :#line:1226
                            if O00OO0O0O00O00OOO :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                OOOO000OOO0OO0OOO =999 -float (OOO00OOOOOOO0OO0O )#line:1229
                                OOO0OOO00O0000O00 ={"water":str (OOOO000OOO0OO0OOO ).split ('.')[0 ]}#line:1230
                                OO0OOO00O0000O0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000000O0O0O000O0 ).json ()#line:1232
                                if 'status'in OO0OOO00O0000O0O0 :#line:1234
                                    if OO0OOO00O0000O0O0 ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOO00O0000O0O0["message"]}')#line:1236
                                    if OO0OOO00O0000O0O0 ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOO00O0000O0O0["message"]}')#line:1238
                                        break #line:1239
                                if float (OOO00OOOOOOO0OO0O )<780 :#line:1240
                                    OOOO000OOO0OO0OOO =800 -float (OOO00OOOOOOO0OO0O )#line:1241
                                    O0000O0O0OO0OOO0O =f'_water={int(OOOO000OOO0OO0OOO)}_{timi_new()}'#line:1242
                                    O000OO0OO000OOO0O ={'source':'scsc','authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0OO0OOO0O ),'signstring':O0000O0O0OO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    OO00OO0O0OOOO000O ={"water":int (OOOO000OOO0OO0OOO )}#line:1254
                                    O00OOO0OOOOO0OO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000OO0OO000OOO0O ,data =OO00OO0O0OOOO000O ).json ()#line:1256
                                    if 'status'in O00OOO0OOOOO0OO0O :#line:1258
                                        if O00OOO0OOOOO0OO0O ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O00OOO0OOOOO0OO0O["message"]}丨数量:{int(OOOO000OOO0OO0OOO)}')#line:1260
                                        if O00OOO0OOOOO0OO0O ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O00OOO0OOOOO0OO0O["message"]}丨数量:{int(OOOO000OOO0OO0OOO)}')#line:1262
                                            OOOO0O0OO00O0000O =O00OOO0OOOOO0OO0O ["message"].split ('-')[1 ]#line:1263
                                            O00OOO0OO000O0O00 =f'__{timi_new()}'#line:1264
                                            OO0O0000O00OO0O00 ={'source':'scsc','authorization':OOOO0O000OO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO000O0O00 ),'signstring':O00OOO0OO000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OO00000000OO00O0O =requests .request ('get',f'{host}/user',headers =OO0O0000O00OO0O00 ).json ()#line:1276
                                            if 'status'in OO00000000OO00O0O :#line:1277
                                                if OO00000000OO00O0O ['status']==200 :#line:1278
                                                    OOO0O0O0O0O0000O0 =OO00000000OO00O0O ['data']['inner_id']#line:1279
                                                    if give_gold (OOO0O0O0O0O0000O0 ,float (OOOO0O0OO00O0000O )+1 ):#line:1280
                                                        OOOO0O000OO0O00O0 .energy ()#line:1281
                        break #line:1282
        except Exception as O00OOOO0OOO00OOOO :#line:1283
            print (O00OOOO0OOO00OOOO )#line:1284
def bundled_def ():#line:1287
    OO00O00O0OOO0O000 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OO00O00O0OOO0O000 [random .randint (0 ,len (OO00O00O0OOO0O000 )-1 )]#line:1289
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
        OOOO0O0O0O000000O =gitee_edition ()#line:1328
        if version_of_the_validation ()<OOOO0O0O0O000000O ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0O0O0O000000O["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{OOOO0O0O0O000000O["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOO0O0O0O000000O["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {OOOO0O0O0O000000O["CityEarth"]["content"]}')#line:1334
    except Exception as OOOO000O00000OO0O :#line:1335
        print (OOOO000O00000OO0O )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
