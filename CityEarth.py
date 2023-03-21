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
@ 版本  5.0
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
        O0OOO0O00OOOOO0OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OOO0O00OOOOO0OO)}个账号==========")#line:17
        for O0OO00OO00000000O in O0OOO0O00OOOOO0OO :#line:18
            OOO0O0000OO0000OO =[]#line:19
            print (f"------------正在执行第{O0OOO0O00OOOOO0OO.index(O0OO00OO00000000O) + 1}个账号------------")#line:20
            OOO0O0000O0O0O0OO =CityEarth (O0OO00OO00000000O ,OOO0O0000OO0000OO ,O0OOO0O00OOOOO0OO .index (O0OO00OO00000000O ))#line:21
            def OOO00O00OOOOOOO0O ():#line:23
                if OOO0O0000O0O0O0OO .base_info ():#line:25
                    OOO0O0000O0O0O0OO .sealing ()#line:27
                    OOO0O0000O0O0O0OO .invitenum ()#line:29
                    OOO0O0000O0O0O0OO .query_to_sell ()#line:31
                    OOO0O0000O0O0O0OO .friends_invitation ()#line:35
                    OOO0O0000O0O0O0OO .energy ()#line:37
                    OOO0O0000O0O0O0OO .add_clover ()#line:39
                    OOO0O0000O0O0O0OO .propsraffle ()#line:41
                    OOO0O0000O0O0O0OO .synthetic ()#line:43
                    OOO0O0000O0O0O0OO .crops_illustrated ()#line:45
                    OOO0O0000O0O0O0OO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO0O0000O0O0O0OO .give_gold ()#line:50
            OOOO0O0O00OO00O0O =threading .Thread (target =OOO00O00OOOOOOO0O )#line:52
            OOOO0O0O00OO00O0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0000000OOO0O000O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0000000OOO0O000O +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO0O00OOOOOOO00OO in invited_new :#line:62
            print (OO0O00OOOOOOO00OO )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0O0O0O0OO0OOO00 in weishim :#line:65
            print (OO0O0O0O0OO0OOO00 )#line:66
    except Exception as OOO0OOO00OOO0OO00 :#line:67
        print (OOO0OOO00OOO0OO00 )#line:68
def give_gold (OO00OOOO0OOOOOO00 ,O0OO0OO00OO0O000O ):#line:72
    try :#line:73
        OO00000OO0O000OOO =f'_doneeNo={OO00OOOO0OOOOOO00}&quantity={int(O0OO0OO00OO0O000O)}_{timi_new()}'#line:74
        O0O00O000OOOOO00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO00000OO0O000OOO ),'signstring':OO00000OO0O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOOOOOOO0O00O0000 ={"quantity":int (O0OO0OO00OO0O000O ),"doneeNo":OO00OOOO0OOOOOO00 }#line:89
        OOOO0OO0OO000O000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00O000OOOOO00O ,data =OOOOOOOO0O00O0000 ).json ()#line:90
        if 'status'in OOOO0OO0OO000O000 :#line:92
            if OOOO0OO0OO000O000 ['status']==200 :#line:93
                if OOOO0OO0OO000O000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0OO0OO00OO0O000O)}种子给{OO00OOOO0OOOOOO00}成功')#line:95
                    return True #line:96
            if OOOO0OO0OO000O000 ['status']==401 :#line:97
                print (f'【赠送种子】:{OOOO0OO0OO000O000["message"]}')#line:98
                return False #line:99
            if OOOO0OO0OO000O000 ['status']==500 :#line:100
                print (f'【赠送种子】:{OOOO0OO0OO000O000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00OOOO0O0OO0OO0O :#line:104
        print (O00OOOO0O0OO0OO0O )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OO00OOOOO000O0O ):#line:115
    OOO000O0OOOO000OO =hashlib .md5 (O0OO00OOOOO000O0O .encode ()).hexdigest ()#line:116
    OOOOO0000OOOOOO00 =sc1 ()#line:117
    OOO0O00OO000O000O =sc2 ()#line:118
    OO0OO0000O0000OO0 =sc3 ()#line:119
    OO00000O0000O000O =OOOOO0000OOOOOO00 +OOO000O0OOOO000OO +OOO0O00OO000O000O +OO0OO0000O0000OO0 #line:120
    O00O00O0O0O000OOO =hashlib .md5 (OO00000O0000O000O .encode ()).hexdigest ()#line:121
    return O00O00O0O0O000OOO #line:122
def format_msg ():#line:125
    O0OO0O0OO0000000O =""#line:126
    for OOO0OO0O0OO00OOOO in msg_list :#line:127
        O0OO0O0OO0000000O +=str (OOO0OO0O0OO00OOOO )+"\r\n"#line:128
    return O0OO0O0OO0000000O #line:129
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
def get_json_data (O0O00000OO0OO0O0O ,OOOO00000OO00OOO0 ,O0O000O0O0O0O000O ,O000O00OO0O0OO0OO ):#line:153
    with open (O0O00000OO0OO0O0O ,'rb')as O000O0OOOOO0OO000 :#line:154
        O000OO0OO0O000O0O =json .load (O000O0OOOOO0OO000 )#line:155
        O000OO0OO0O000O0O ['data'][OOOO00000OO00OOO0 ][O0O000O0O0O0O000O ]=O000O00OO0O0OO0OO #line:156
        OOOOOOOOOO00OOOOO =O000OO0OO0O000O0O #line:157
    O000O0OOOOO0OO000 .close ()#line:158
    return OOOOOOOOOO00OOOOO #line:159
def write_json_data (OOO000000O00O0000 ):#line:162
    with open (json_path1 ,'w')as O00000O0O0OOOOOO0 :#line:163
        json .dump (OOO000000O00O0000 ,O00000O0O0OOOOOO0 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O00000O0O0OOOOOO0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O000O0000OOOOOO0O ,O0O000OO000OOO0O0 ,O00O00O0OOO0O000O ,OO00000O00OO0O0O0 ):#line:171
        try :#line:172
            O000O0000OOOOOO0O .msg =O00O00O0OOO0O000O #line:173
            O000O0000OOOOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O000O0000OOOOOO0O .token =O0O000OO000OOO0O0 ['authorization']#line:175
            O000O0000OOOOOO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O000O0000OOOOOO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O000O0000OOOOOO0O .elephant_user =O0O000OO000OOO0O0 ['elephant_user']#line:178
            O000O0000OOOOOO0O .elephant_pswd =O0O000OO000OOO0O0 ['elephant_pswd']#line:179
            O000O0000OOOOOO0O .elephant_Task_ID =O0O000OO000OOO0O0 ['elephant_Task_ID']#line:180
            O000O0000OOOOOO0O .len_new =OO00000O00OO0O0O0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOO0O00OOO00OOOOO ):#line:186
        try :#line:187
            OOO0O00OOO00OOOOO .watched_ad ()#line:189
            OOO0OOOOO0OOO0OOO =f'__{timi_new()}'#line:190
            O00O0O000O000OOO0 ={'source':'scsc','authorization':OOO0O00OOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0OOO0OOO ),'signstring':OOO0OOOOO0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OO00O0OOOO0O000OO =requests .request ('get',f'{host}/user',headers =O00O0O000O000OOO0 ).json ()#line:202
            if 'status'in OO00O0OOOO0O000OO :#line:204
                if OO00O0OOOO0O000OO ['status']==200 :#line:205
                    OO0O0O0OO0000000O =OO00O0OOOO0O000OO ['data']['nickname']#line:206
                    OO000OOO000OO0O00 =OO00O0OOOO0O000OO ['data']['inner_id']#line:207
                    O0000O0O00O00OOOO =OO00O0OOOO0O000OO ['data']['assets']['gold']#line:208
                    O00000O000000O00O =OO00O0OOOO0O000OO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OO0O0O0OO0000000O[:5]}丨ID:{OO000OOO000OO0O00}丨等级:{O00000O000000O00O}丨金种子:{str(O0000O0O00O00OOOO).split(".")[0]}')#line:211
                    if 'wx_'in OO0O0O0OO0000000O :#line:212
                        OOO0O00OOO00OOOOO .change_nickname ()#line:213
                if OO00O0OOOO0O000OO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOO0O00OOO00OOOOO .elephant_user =='f':#line:216
                        return False #line:217
                    OOO0O0O0OOO0000O0 =Invalid_login .addtask (elephant_user =OOO0O00OOO00OOOOO .elephant_user ,elephant_pswd =OOO0O00OOO00OOOOO .elephant_pswd ,elephant_Task_ID =OOO0O00OOO00OOOOO .elephant_Task_ID )#line:220
                    OOOOOOO0O000000OO =get_json_data (json_path ,OOO0O00OOO00OOOOO .len_new ,'authorization',OOO0O0O0OOO0000O0 )#line:221
                    if write_json_data (OOOOOOO0O000000OO ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OO00O0OOOO0O000OO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOOO00OOO0O0OO000 :#line:228
            print (OOOO00OOO0O0OO000 )#line:229
    def sealing (OOO000000OO00O00O ):#line:232
        try :#line:233
            O0O0O00OOOO0O0000 =f'__{timi_new()}'#line:234
            O00OOOOO0O0000000 ={'source':'scsc','authorization':OOO000000OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO0O0000 ),'signstring':O0O0O00OOOO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOOO0O0000000 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOOO0O0000000 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOOO0O0000000 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOOO0O0000000 )#line:249
            requests .request ('get',f'{host}/user',headers =O00OOOOO0O0000000 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOOO0O0000000 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOOO0O0000000 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOOO0O0000000 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOO0O0000000 )#line:254
            requests .request ('get',f'{host}/assets',headers =O00OOOOO0O0000000 )#line:255
        except Exception as O0O0OO0O0O0OO0O00 :#line:256
            print (O0O0OO0O0O0OO0O00 )#line:257
    def ddd (O00O00O0O00O0OO00 ):#line:259
        try :#line:260
            OOO00OOOO000OOOOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00O0OO0OOO0000O0 ={'source':'scsc','authorization':O00O00O0O00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO000OOOOO ),'signstring':OOO00OOOO000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0OOOO000OO000OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00O0OO0OOO0000O0 ).json ()#line:273
            print (OO0OOOO000OO000OO )#line:274
        except Exception as O0OOOO0OOO0000O0O :#line:277
            print (O0OOOO0OOO0000O0O )#line:278
    def the_query (OOO00O0OOOOOOO00O ):#line:283
        try :#line:284
            OOOO0O000OOO0O00O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O00OOO00O000O00O0 ={'authorization':OOO00O0OOOOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000OOO0O00O ),'signstring':OOOO0O000OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOO00OO00O0OOO0O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00OOO00O000O00O0 ).json ()#line:296
            if 'status'in OOO00OO00O0OOO0O0 :#line:298
                if OOO00OO00O0OOO0O0 ['status']==200 :#line:299
                    return OOO00OO00O0OOO0O0 ['data']['rows'][4 ]['price']#line:300
        except Exception as OO0O0OO0OO0OO00OO :#line:301
            print (OO0O0OO0OO0OO00OO )#line:302
    def market_sale (O0OO0O00O0000O0OO ,O00OOOOOO00O00OOO ):#line:305
        try :#line:306
            O0OO000OO0O0OOO0O =timi_new ()#line:307
            O0OOO0O0OOOOOO0OO =f'type=crop__{O0OO000OO0O0OOO0O}'#line:308
            O0OOOO0O00O0O0OO0 ={'source':'scsc','authorization':O0OO0O00O0000O0OO .token ,'timestamp':str (O0OO000OO0O0OOO0O ),'sign':sign (O0OOO0O0OOOOOO0OO ),'signstring':O0OOO0O0OOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            OOO0O0OO00OOOOO00 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0OOOO0O00O0O0OO0 ).json ()#line:320
            if 'status'in OOO0O0OO00OOOOO00 :#line:322
                if OOO0O0OO00OOOOO00 ['status']==200 :#line:323
                    if OOO0O0OO00OOOOO00 ['data']['rows']:#line:324
                        OOO0000OO0O00OO0O =OOO0O0OO00OOOOO00 ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0O0O000OOOO0OOO0 =OOO0O0OO00OOOOO00 ['data']['rows'][0 ]['quantity']#line:326
                        O0O0OOO00O0OO0OO0 =O00OOOOOO00O00OOO #line:327
                        if float (O00OOOOOO00O00OOO )>5 :#line:328
                            O0OO00O0O0OOOO0O0 =f'_packsackItemId={OOO0000OO0O00OO0O}&price={str(O0O0OOO00O0OO0OO0)[:5]}&quantity={O0O0O000OOOO0OOO0}_{O0OO000OO0O0OOO0O}'#line:329
                            O0OO0000O00OOO00O ={'source':'scsc','authorization':O0OO0O00O0000O0OO .token ,'timestamp':str (O0OO000OO0O0OOO0O ),'sign':sign (O0OO00O0O0OOOO0O0 ),'signstring':O0OO00O0O0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
                            OO0OO0O000OOO0000 ={"packsackItemId":OOO0000OO0O00OO0O ,"price":str (O0O0OOO00O0OO0OO0 )[:5 ],"quantity":str (O0O0O000OOOO0OOO0 )}#line:345
                            O0O0O0000OOOOOO0O =requests .request ('post',f'{host}/market/sale',headers =O0OO0000O00OOO00O ,data =OO0OO0O000OOO0000 ).json ()#line:346
                            if 'status'in O0O0O0000OOOOOO0O :#line:348
                                if O0O0O0000OOOOOO0O ['status']==200 :#line:349
                                    print (f'【上架芦荟】:数量:{O0O0O000OOOO0OOO0}丨价格:{str(O0O0OOO00O0OO0OO0)[:5]}')#line:350
                                if O0O0O0000OOOOOO0O ['status']==500 :#line:351
                                    print (f'【上架芦荟】:{O0O0O0000OOOOOO0O["message"]}')#line:352
        except Exception as OOOO0000OOOO00000 :#line:353
            print (OOOO0000OOOO00000 )#line:354
    def query_to_sell (O00O0OOO0000O0000 ):#line:357
        global count_list #line:358
        try :#line:359
            OO0OOOO00OO0OO0O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:360
            O0O00O000OO0OO00O ={'source':'scsc','authorization':O00O0OOO0000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00OO0OO0O0 ),'signstring':OO0OOOO00OO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:371
            OOO000O00O0O0O0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O00O000OO0OO00O ).json ()#line:372
            if 'status'in OOO000O00O0O0O0O0 :#line:374
                if OOO000O00O0O0O0O0 ['status']==200 :#line:375
                    for OO00000OOO0O0O00O in OOO000O00O0O0O0O0 ['data']['rows']:#line:376
                        O00O0OOO0OO0OOOO0 =OO00000OOO0O0O00O ['materialKey']#line:377
                        OOOO0O000OOO0OOOO =OO00000OOO0O0O00O ['quantity']#line:378
                        O000O00O0O00O00O0 =OO00000OOO0O0O00O ['price']#line:379
                        O00O0OOO00O0OOO0O =OO00000OOO0O0O00O ['saleState']#line:380
                        if O00O0OOO00O0OOO0O ==0 :#line:381
                            print (f'【出售订单】:名称:{O00O0OOO0OO0OOOO0}丨数量:{OOOO0O000OOO0OOOO}丨价格:{O000O00O0O00O00O0}')#line:382
                            count_list +=OOOO0O000OOO0OOOO #line:383
                            OO0O0OO0O00OO000O =O00O0OOO0000O0000 .the_query ()#line:385
                            if float (OO0O0OO0O00OO000O )!=float (O000O00O0O00O00O0 ):#line:386
                                OOOO000O0O00O0O00 =OO00000OOO0O0O00O ['id']#line:387
                                O00O0OOO0000O0000 .cacel_sale (OOOO000O0O00O0O00 )#line:388
                    O00O0OOO0000O0000 .game_map ()#line:390
        except Exception as OOOO0OO0OO0OO000O :#line:392
            print (OOOO0OO0OO0OO000O )#line:393
    def cacel_sale (OO000OOO000OO000O ,OO0OOO0O00O0000OO ):#line:396
        try :#line:397
            OOOOO0OO00O000OO0 =f'_saleId={OO0OOO0O00O0000OO}_{timi_new()}'#line:398
            O00OOOO000OO0O0OO ={'source':'scsc','authorization':OO000OOO000OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO00O000OO0 ),'signstring':OOOOO0OO00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            OOO000OOO00OOOO0O ={"saleId":OO0OOO0O00O0000OO }#line:410
            O0OOO0O0O0000OO00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OOOO000OO0O0OO ,data =OOO000OOO00OOOO0O ).json ()#line:411
            if 'status'in O0OOO0O0O0000OO00 :#line:413
                if O0OOO0O0O0000OO00 ['status']==200 :#line:414
                    print (f'【下架出售】:{O0OOO0O0O0000OO00["data"]}')#line:415
        except Exception as OO0O0O000000OO0OO :#line:416
            print (OO0O0O000000OO0OO )#line:417
    def change_nickname (O0000OOO000O0O0OO ):#line:420
        try :#line:421
            O0OO00O00O0000OO0 =timi_new ()#line:422
            OOOOO0OOO00O00000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:423
            O0O0OOOO0O0OO00O0 =requests .request ('post','https://www.qmsjmfb.com/',data =OOOOO0OOO00O00000 ).text #line:424
            O00000OO000OOO0O0 =re .findall ('<ul><li>(.*?)</li>',O0O0OOOO0O0OO00O0 )[0 ][:3 ]#line:425
            OO0O00O00000O00O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00000OO000OOO0O0}').json ()#line:426
            OOOOO0O00000000O0 =OO0O00O00000O00O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:427
            O00000OO0OO000000 ={"nickname":OOOOO0O00000000O0 }#line:428
            OOOOOO00OOO00O0OO =f'_nickname={OOOOO0O00000000O0}_{O0OO00O00O0000OO0}'#line:429
            OOO000OOOO0OO0OOO ={'source':'scsc','authorization':O0000OOO000O0O0OO .token ,'timestamp':O0OO00O00O0000OO0 ,'sign':sign (OOOOOO00OOO00O0OO ),'signstring':OOOOOO00OOO00O0OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:440
            O0OO0O0000O00O0OO =requests .request ('patch',f'{host}/user/nickname',headers =OOO000OOOO0OO0OOO ,data =O00000OO0OO000000 ).json ()#line:441
            if 'status'in O0OO0O0000O00O0OO :#line:443
                if O0OO0O0000O00O0OO ['status']==200 :#line:444
                    print (f'【修改网名】:网名:{OOOOO0O00000000O0}丨{O0OO0O0000O00O0OO["message"]}')#line:445
        except Exception as O0OOOOO0OO0O00OOO :#line:446
            print (O0OOOOO0OO0O00OOO )#line:447
    def withdraw (OOO0OO00O00O00OOO ):#line:450
        try :#line:451
            O0O00O0O000OOOOOO =f'__{timi_new()}'#line:452
            O00O00OOO0O00000O ={'source':'scsc','authorization':OOO0OO00O00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000OOOOOO ),'signstring':O0O00O0O000OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            OO0O0O0O0000O00O0 =requests .request ('get',f'{host}/assets',headers =O00O00OOO0O00000O ).json ()#line:464
            if 'status'in OO0O0O0O0000O00O0 :#line:466
                if OO0O0O0O0000O00O0 ['status']==200 :#line:467
                    OOOOOO0OO0O0OO0O0 =OO0O0O0O0000O00O0 ['data']['cash']#line:468
                    if float (OOOOOO0OO0O0OO0O0 )>20 :#line:469
                        O0O00O0O000OOOOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:470
                        O00O00OOO0O00000O ={'authorization':OOO0OO00O00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000OOOOOO ),'signstring':O0O00O0O000OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
                        O0O0OOO00O0O00000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:481
                        OOO0OO000000OO0O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O00OOO0O00000O ,data =O0O0OOO00O0O00000 ).json ()#line:483
                        if 'status'in OOO0OO000000OO0O0 :#line:485
                            if OOO0OO000000OO0O0 ['status']==200 :#line:486
                                print (f'【余额提现】:{OOO0OO000000OO0O0["data"]}')#line:487
                        if 'status'in OOO0OO000000OO0O0 :#line:488
                            if OOO0OO000000OO0O0 ['status']==500 :#line:489
                                print (f'【余额提现】:{OOO0OO000000OO0O0["message"]}')#line:490
        except Exception as OOO0O0000OOO0OO00 :#line:491
            print (OOO0O0000OOO0OO00 )#line:492
    def invitenum (OOO0OO000O0000OOO ):#line:495
        global invited_new #line:496
        try :#line:497
            O0000O0O00OO00OO0 =f'__{timi_new()}'#line:498
            O000O0000OOOOOO00 ={'source':'scsc','authorization':OOO0OO000O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O00OO00OO0 ),'signstring':O0000O0O00OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:509
            OO0000OOOO000000O =requests .request ('get',f'{host}/invite/invitenum',headers =O000O0000OOOOOO00 ).json ()#line:510
            if 'status'in OO0000OOOO000000O :#line:512
                if OO0000OOOO000000O ['status']==200 :#line:513
                    O0OO000OOOOOO000O =OO0000OOOO000000O ['data']['invited_count']#line:514
                    O00000O00OOO00O0O =OO0000OOOO000000O ['data']['invited_second_count']#line:515
                    print (f'【我的邀请】:直邀好友:{O0OO000OOOOOO000O}丨间邀好友:{O00000O00OOO00O0O}')#line:516
                    if O0OO000OOOOOO000O <2 :#line:517
                        O000O0O0000O000OO =f'__{timi_new()}'#line:518
                        O0OO0O00O0000O0O0 ={'source':'scsc','authorization':OOO0OO000O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0000O000OO ),'signstring':O000O0O0000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                        OO0OOOO00O0OO00OO =requests .request ('get',f'{host}/user',headers =O0OO0O00O0000O0O0 ).json ()#line:530
                        if 'status'in OO0OOOO00O0OO00OO :#line:532
                            if OO0OOOO00O0OO00OO ['status']==200 :#line:533
                                invited_new .append (OO0OOOO00O0OO00OO ['data']['inner_id'])#line:534
        except Exception as O00O0OO00O0O000OO :#line:535
            print (O00O0OO00O0O000OO )#line:536
    def game_map (O00000OO0O00OOOO0 ):#line:539
        try :#line:540
            O0O000OO0OOO0000O =f'__{timi_new()}'#line:541
            OO0OOOOOOO000O00O ={'source':'scsc','authorization':O00000OO0O00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OO0OOO0000O ),'signstring':O0O000OO0OOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            OOO0O00O00OO0O000 =requests .request ('get',f'{host}/game/map',headers =OO0OOOOOOO000O00O ).json ()#line:553
            if 'status'in OOO0O00O00OO0O000 :#line:555
                if OOO0O00O00OO0O000 ['status']==200 :#line:556
                    for OOOO0O0O0OO000OO0 in OOO0O00O00OO0O000 ['data']['list'][0 ]['crops']:#line:557
                        O00000OO000000OOO =OOOO0O0O0OO000OO0 ['level']#line:559
                        if O00000OO000000OOO ==41 :#line:560
                            OOO00O0OO0OO00O00 =OOOO0O0O0OO000OO0 ['crop_name']#line:561
                            O00OO0O00O0O000OO =OOOO0O0O0OO000OO0 ['count']#line:562
                            if O00OO0O00O0O000OO >0 :#line:563
                                print (f'【农业资产】:{OOO00O0OO0OO00O00}丨数量:{O00OO0O00O0O000OO}')#line:564
                                OO0OO0OO0OO0OOOOO =O00000OO0O00OOOO0 .the_query ()#line:565
                                O00000OO0O00OOOO0 .market_sale (OO0OO0OO0OO0OOOOO )#line:566
        except Exception as OO000OO0OO0OO0O0O :#line:567
            print (OO000OO0OO0OO0O0O )#line:568
    def give_gold (O0OO00O00OO00O00O ):#line:571
        try :#line:572
            O000OO0O0OOOO0O00 =f'__{timi_new()}'#line:573
            O000O0OOO0OOO0OOO ={'source':'scsc','authorization':O0OO00O00OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0OOOO0O00 ),'signstring':O000OO0O0OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
            OO0OOOO0O00OO0OOO =requests .request ('get',f'{host}/user',headers =O000O0OOO0OOO0OOO ).json ()#line:585
            if 'status'in OO0OOOO0O00OO0OOO :#line:586
                if OO0OOOO0O00OO0OOO ['status']==200 :#line:587
                    if float (O0OO00O00OO00O00O .doneeNo )!=0 :#line:588
                        OO000O0OOO000O000 =OO0OOOO0O00OO0OOO ['data']['assets']['gold']#line:589
                        if float (OO000O0OOO000O000 )>float (O0OO00O00OO00O00O .innerId ):#line:590
                            OO00OO00O0O00OO00 =int (float (OO000O0OOO000O000 )/1.1 )#line:591
                            O000OO0O0OOOO0O00 =f'_doneeNo={O0OO00O00OO00O00O.doneeNo}&quantity={OO00OO00O0O00OO00}_{timi_new()}'#line:592
                            O000O0OOO0OOO0OOO ={'source':'scsc','authorization':O0OO00O00OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0OOOO0O00 ),'signstring':O000OO0O0OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:603
                            O00OOO00O00O00OOO ={"quantity":OO00OO00O0O00OO00 ,"doneeNo":O0OO00O00OO00O00O .doneeNo }#line:607
                            O0OOOO0000OOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0OOO0OOO0OOO ,data =O00OOO00O00O00OOO ).json ()#line:608
                            if 'status'in O0OOOO0000OOO0000 :#line:610
                                if O0OOOO0000OOO0000 ['status']==200 :#line:611
                                    if O0OOOO0000OOO0000 ['data']:#line:612
                                        print (f'【赠送种子】:赠送{OO00OO00O0O00OO00}种子给{O0OO00O00OO00O00O.doneeNo}成功')#line:613
                    else :#line:614
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:615
        except Exception as O0O00O0O000O00OO0 :#line:616
            print (O0O00O0O000O00OO0 )#line:617
    def invitation (OO00O0O0OOOO0OO00 ):#line:619
        try :#line:620
            _O0OO00000OO0O0000 =float (bundled_def ())/4 #line:621
            OOO0000O000OOOO00 =f'_innerId={int(_O0OO00000OO0O0000)}_{timi_new()}'#line:623
            O00O00OO0O000OO0O ={'source':'scsc','authorization':OO00O0O0OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O000OOOO00 ),'signstring':OOO0000O000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OOOOOO0OOO0O000O0 ={"innerId":int (_O0OO00000OO0O0000 )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O00OO0O000OO0O ,data =OOOOOO0OOO0O000O0 )#line:636
        except Exception as O00O00OO0OOO0OO0O :#line:637
            print (O00O00OO0OOO0OO0O )#line:638
    def winning_rewards (O00O0O0000O000OOO ):#line:641
        try :#line:642
            O0OOOOOO0O0OOO00O =f'__{timi_new()}'#line:643
            OOO0O00O00OOOO0O0 ={'source':'scsc','authorization':O00O0O0000O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0O0OOO00O ),'signstring':O0OOOOOO0O0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            OO000OOOOOOOOO0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O00O00OOOO0O0 ).json ()#line:655
            if 'status'in OO000OOOOOOOOO0OO :#line:657
                if OO000OOOOOOOOO0OO ['status']==200 :#line:658
                    if OO000OOOOOOOOO0OO ['data']['amount']:#line:659
                        O0OOOO0O00OOO0O00 =OO000OOOOOOOOO0OO ['data']['amount']['gold']#line:660
                        return O0OOOO0O00OOO0O00 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as OO0O0000O0O000000 :#line:664
            print (OO0O0000O0O000000 )#line:665
    def certification (OO00OO000OOOO0OOO ):#line:668
        try :#line:669
            O0O00O0OOO0O0OO0O =f'__{timi_new()}'#line:670
            OOOO0OO00000000O0 ={'source':'scsc','authorization':OO00OO000OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO0O0OO0O ),'signstring':O0O00O0OOO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            O0O00O00000000OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOO0OO00000000O0 ).json ()#line:682
            if 'status'in O0O00O00000000OOO :#line:684
                if O0O00O00000000OOO ['status']==200 :#line:685
                    if O0O00O00000000OOO ['data']['result']:#line:686
                        OOOO000000OOOO0O0 =O0O00O00000000OOO ['data']['nick_name']#line:687
                        return OOOO000000OOOO0O0 #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as O0000O0OO0OOOOO0O :#line:691
            print (O0000O0OO0OOOOO0O )#line:692
    def crops_illustrated (OO00000O0O0O0O0O0 ):#line:695
        try :#line:696
            O00000OOOO0O0OOOO =f'__{timi_new()}'#line:697
            OO0OO0OOO0000O00O ={'source':'scsc','authorization':OO00000O0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO0O0OOOO ),'signstring':O00000OOOO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            O00O0OOOOOO0O0OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OO0OOO0000O00O ).json ()#line:709
            if 'status'in O00O0OOOOOO0O0OO0 :#line:711
                if O00O0OOOOOO0O0OO0 ['status']==200 :#line:712
                    O0O0OOOOOO00O00OO =O00O0OOOOOO0O0OO0 ['data'][0 ]['crops']#line:713
                    for O00OOOO0O0O0OO0O0 in O0O0OOOOOO00O00OO :#line:714
                        if O00OOOO0O0O0OO0O0 ['ill_clover_award']:#line:715
                            if float (O00OOOO0O0O0OO0O0 ['ill_clover_award'])>1 :#line:716
                                if O00OOOO0O0O0OO0O0 ['is_finish']:#line:717
                                    if not O00OOOO0O0O0OO0O0 ['is_getit']:#line:718
                                        if OO00000O0O0O0O0O0 .certification ()!='未实名':#line:719
                                            O00000OOOO0O0OOOO =f'_award_level={O00OOOO0O0O0OO0O0["level"]}_{timi_new()}'#line:720
                                            OO0OO0OOO0000O00O ={'source':'scsc','authorization':OO00000O0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO0O0OOOO ),'signstring':O00000OOOO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            O0O00OO0OO00O00OO ={"award_level":O00OOOO0O0O0OO0O0 ['level']}#line:732
                                            O00OOOOOO0OO00O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OO0OOO0000O00O ,json =O0O00OO0OO00O00OO ).json ()#line:734
                                            if 'status'in O00OOOOOO0OO00O0O :#line:735
                                                if O00OOOOOO0OO00O0O ['status']==200 :#line:736
                                                    O0O000OO0O0O0OOOO =O00OOOOOO0OO00O0O ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{O00OOOO0O0O0OO0O0["crop_name"]}成就丨奖励{O0O000OO0O0O0OOOO}☘️')#line:739
                                                if O00OOOOOO0OO00O0O ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{O00OOOOOO0OO00O0O["message"]}')#line:741
        except Exception as O0O0000000O0O0O00 :#line:742
            print (O0O0000000O0O0O00 )#line:743
    def watched_ad (OO0OOO0O0O000O0OO ):#line:746
        try :#line:747
            O0OO000O0OO0OO0O0 =f'__{timi_new()}'#line:748
            O000OO00OOOO00OOO ={'source':'scsc','authorization':OO0OOO0O0O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0OO0OO0O0 ),'signstring':O0OO000O0OO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            O0OO0O0OO00O00O0O =requests .request ('get',f'{host}/game/getAllData',headers =O000OO00OOOO00OOO ).json ()#line:760
            if 'status'in O0OO0O0OO00O00O0O :#line:762
                if O0OO0O0OO00O00O0O ['status']==200 :#line:763
                    if 'offlineInfo'in O0OO0O0OO00O00O0O ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        OOO00O0O00OOO00O0 =O0OO0O0OO00O00O0O ['data']['offlineInfo']['off_minute']#line:766
                        O0000OOOO0O00OO0O =float (O0OO0O0OO00O00O0O ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000OO00OOOO00OOO ).json ()#line:769
                        time .sleep (2 )#line:770
                        OOO0O0OOOO00O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO00OOOO00OOO ).json ()#line:771
                        if 'status'in OOO0O0OOOO00O0OO0 :#line:773
                            if OOO0O0OOOO00O0OO0 ['status']==200 :#line:774
                                OOOOOO0O00OO000OO =float (OOO0O0OOOO00O0OO0 ['data']['silver'])/1000000000000 #line:775
                                OO0O00000O0OO0OO0 =str (OOOOOO0O00OO000OO -O0000OOOO0O00OO0O )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{OOO00O0O00OOO00O0}分钟奖励🌱数量:{OO0O00000O0OO0OO0}t粒')#line:777
        except Exception as O00OO0O000OO00OOO :#line:778
            print (O00OO0O000OO00OOO )#line:779
    def user_ad (O0000O000OO00OOO0 ):#line:782
        try :#line:783
            O00O0OOO0O000OO00 =f'__{timi_new()}'#line:784
            OO000OO00O0O00OO0 ={'source':'scsc','authorization':O0000O000OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0O000OO00 ),'signstring':O00O0OOO0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            O00OOO0OOO0OOO00O =requests .request ('get',f'{host}/user/ad',headers =OO000OO00O0O00OO0 ).json ()#line:796
            if 'status'in O00OOO0OOO0OOO00O :#line:798
                if O00OOO0OOO0OOO00O ['status']==200 :#line:799
                    O00000O00OOOO0O00 =O00OOO0OOO0OOO00O ['data']['max_time']#line:800
                    O0O000O0O0OOO0000 =O00OOO0OOO0OOO00O ['data']['watch_time']#line:801
                    O00OOO00OOOOO00OO =O00OOO0OOO0OOO00O ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{O00OOO00OOOOO00OO + O00000O00OOOO0O00 - O0O000O0O0OOO0000}次丨好友提供:{O00OOO00OOOOO00OO}次')#line:803
                    if O00OOO00OOOOO00OO +O00000O00OOOO0O00 -O0O000O0O0OOO0000 >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        OO000O0OOO0OOOO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000OO00O0O00OO0 ).json ()#line:806
                        if 'status'in OO000O0OOO0OOOO0O :#line:808
                            if OO000O0OOO0OOOO0O ['status']==200 :#line:809
                                OOOO000O0O0OO00OO =float (OO000O0OOO0OOOO0O ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(OOOO000O0O0OO00OO)}t粒')#line:811
                                return True #line:812
                            if OO000O0OOO0OOOO0O ['status']==500 :#line:813
                                O0OOOOOO00O0O00OO =OO000O0OOO0OOOO0O ['message']#line:814
                                print (f'【获取种子】:{O0OOOOOO00O0O00OO}')#line:815
                                return False #line:816
        except Exception as OO0OOO0OO0OOOO000 :#line:817
            print (OO0OOO0OO0OOOO000 )#line:818
    def synthetic (OO0OOO00O0OOO0OOO ):#line:821
        global id ,g #line:822
        try :#line:823
            O00O0O00OO000OO00 =OO0OOO00O0OOO0OOO .level_new ()#line:824
            O00OO0OO00O0O00O0 =random .randint (9 ,11 )#line:825
            O0OO000OO00O0O0O0 =f'_site=8&targetSite={O00OO0OO00O0O00O0}_{timi_new()}'#line:826
            OOO0OOOO0O000O000 ={'source':'scsc','authorization':OO0OOO00O0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0OO000OO00O0O0O0 ),'signstring':O0OO000OO00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            OOO000OOOOOO0000O ={"site":int (8 ),"targetSite":int (O00OO0OO00O0O00O0 )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0OOOO0O000O000 ,json =OOO000OOOOOO0000O )#line:839
            while True :#line:840
                OO00O0O00000000OO =f'__{timi_new()}'#line:841
                OOO000OOO00OO0O0O ={'source':'scsc','authorization':OO0OOO00O0OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00000000OO ),'signstring':OO00O0O00000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                O0OO00O00O0OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO00OO0O0O ).json ()#line:853
                if 'status'in O0OO00O00O0OO0O0O :#line:855
                    if O0OO00O00O0OO0O0O ['status']==200 :#line:856
                        OO000O0000OO000OO =O0OO00O00O0OO0O0O ['data']['cropList']#line:857
                        O0OOO0OO0OO0OO000 =O0OO00O00O0OO0O0O ['data']['gameCoreDataDBid']#line:858
                        O0O0000O00000OO00 =float (O0OO00O00O0OO0O0O ['data']['silver'])/1000000000000 #line:859
                        O0000000OOOO00O0O =0 #line:864
                        for OOOO000OO000OOO00 in OO000O0000OO000OO :#line:865
                            if not OOOO000OO000OOO00 :#line:866
                                OOO0OO00OOOO00000 =f'_crop_id={O0OOO0OO0OO0OO000}&site={O0000000OOOO00O0O}_{OO0OOO00O0OOO0OOO.time}'#line:867
                                OOOOOO000O0O0OOO0 ={'source':'scsc','authorization':OO0OOO00O0OOO0OOO .token ,'timestamp':OO0OOO00O0OOO0OOO .time ,'sign':sign (OOO0OO00OOOO00000 ),'signstring':OOO0OO00OOOO00000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                OO0OOO000O000OO0O ={"site":O0000000OOOO00O0O ,"crop_id":O0OOO0OO0OO0OO000 }#line:878
                                O000O0O000O00OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOO000O0O0OOO0 ,data =OO0OOO000O000OO0O ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in O000O0O000O00OOO0 :#line:882
                                    if O000O0O000O00OOO0 ['status']==200 :#line:883
                                        if O000O0O000O00OOO0 ['message']=='种子数量不足':#line:884
                                            O00O0O00OO000OO00 =OO0OOO00O0OOO0OOO .level_new ()#line:885
                                            print (f'【种植合成】:{O000O0O000O00OOO0["message"]}')#line:886
                                            if not OO0OOO00O0OOO0OOO .user_ad ():#line:887
                                                return False #line:888
                                    if O000O0O000O00OOO0 ['status']==500 :#line:889
                                        print (f'【种植合成】:{O000O0O000O00OOO0["message"]}')#line:890
                                        return False #line:891
                            O0000000OOOO00O0O +=1 #line:892
                        OOO000O0OO0O00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO00OO0O0O ).json ()#line:893
                        O0O00OOO0O00O0O00 =OOO000O0OO0O00OO0 ['data']['cropList']#line:894
                        OO0OO00OOO00000OO =False #line:895
                        for OOOO000OO000OOO00 in range (12 ):#line:896
                            id =O0O00OOO0O00O0O00 [OOOO000OO000OOO00 ]['level']#line:897
                            if float (O00O0O00OO000OO00 )-float (id )>9 :#line:898
                                OOOO000OO00O00O0O =f'_site={OOOO000OO000OOO00}_{timi_new()}'#line:899
                                OO000000000OOO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO00O0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (OOOO000OO00O00O0O ),'signstring':OOOO000OO00O00O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                OOOO0OOOOOOOOOO0O ={"site":OOOO000OO000OOO00 }#line:911
                                OO000O0000O00O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000000000OOO000 ,data =OOOO0OOOOOOOOOO0O ).json ()#line:913
                                if 'status'in OO000O0000O00O00O :#line:914
                                    if OO000O0000O00O00O ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O0OOOOO0O000000O0 in range (11 ):#line:918
                                    OOOOO00OOO0OOO000 =O0OOOOO0O000000O0 +1 #line:919
                                    g =O0O00OOO0O00O0O00 [OOOOO00OOO0OOO000 ]['level']#line:920
                                    if id ==g :#line:921
                                        O0OOO00OOO0OO0000 =O0OOOOO0O000000O0 +2 #line:922
                                        if O0OOO00OOO0OO0000 !=OOOO000OO000OOO00 +1 :#line:923
                                            OOO0O0OO0O000OO00 =OOOO000OO000OOO00 +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            O0OO000OO00O0O0O0 =f'_site={OOO0O0OO0O000OO00 - 1}&targetSite={O0OOO00OOO0OO0000 - 1}_{timi_new()}'#line:927
                                            OOO0OOOO0O000O000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO00O0OOO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0OO000OO00O0O0O0 ),'signstring':O0OO000OO00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            O000000OO0OOO00OO ={"site":int (OOO0O0OO0O000OO00 -1 ),"targetSite":int (O0OOO00OOO0OO0000 -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0OOOO0O000O000 ,json =O000000OO0OOO00OO )#line:946
                                            OO0OO00OOO00000OO =True #line:948
                                    if OO0OO00OOO00000OO :#line:949
                                        break #line:950
                                if OO0OO00OOO00000OO :#line:951
                                    break #line:952
        except :#line:953
            OO0OOO00O0OOO0OOO .synthetic ()#line:954
    def level_new (O0000O0OO0000OO00 ):#line:957
        try :#line:958
            O0OOOOO00O000OOOO =f'__{timi_new()}'#line:959
            O0000O0O0O000O0O0 ={'source':'scsc','authorization':O0000O0OO0000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00O000OOOO ),'signstring':O0OOOOO00O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            OOO0O0O0000OO0OO0 =requests .request ('get',f'{host}/user',headers =O0000O0O0O000O0O0 ).json ()#line:971
            if 'status'in OOO0O0O0000OO0OO0 :#line:972
                if OOO0O0O0000OO0OO0 ['status']==200 :#line:973
                    return float (OOO0O0O0000OO0OO0 ['data']['level'])#line:974
        except Exception as OO0000OOOOO00O0OO :#line:975
            print (OO0000OOOOO00O0OO )#line:976
    def propsraffle (O0O00OOO0OOOOO0OO ):#line:979
        try :#line:980
            while True :#line:981
                OO0OO0OO0O00OOO00 =f'__{timi_new()}'#line:982
                OO0OO000OO00OO00O ={'source':'scsc','authorization':O0O00OOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0O00OOO00 ),'signstring':OO0OO0OO0O00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                OO0000OOOOO0O0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OO000OO00OO00O ).json ()#line:994
                if 'status'in OO0000OOOOO0O0OO0 :#line:996
                    if OO0000OOOOO0O0OO0 ['status']==200 :#line:997
                        O0OO00O0OOOO0O00O =OO0000OOOOO0O0OO0 ['data']['rows']#line:998
                        OO00O0OO00OOO0000 =OO0000OOOOO0O0OO0 ['data']['vstate']#line:999
                        if O0OO00O0OOOO0O00O ==5 or O0OO00O0OOOO0O00O ==6 or O0OO00O0OOOO0O00O ==7 :#line:1000
                            OO0000000O0000OOO =OO0000OOOOO0O0OO0 ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{OO0000000O0000OOO}')#line:1002
                        if O0OO00O0OOOO0O00O ==1 or O0OO00O0OOOO0O00O ==2 or O0OO00O0OOOO0O00O ==3 :#line:1003
                            O000OOO000O0O0O00 =OO0000OOOOO0O0OO0 ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O000OOO000O0O0O00}')#line:1005
                        if O0OO00O0OOOO0O00O ==4 or O0OO00O0OOOO0O00O ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if O0OO00O0OOOO0O00O =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as OOOO00OOOO0O0OO0O :#line:1047
            print (OOOO00OOOO0O0OO0O )#line:1048
    def friends_invitation (O0O0OO0O0O0O0000O ):#line:1051
        try :#line:1052
            O0OO0OOOOOOO00O00 =f'__{timi_new()}'#line:1053
            O00O0O00O00O00OOO ={'source':'scsc','authorization':O0O0OO0O0O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOOOOO00O00 ),'signstring':O0OO0OOOOOOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            O0OO0000O0OO00O00 =requests .request ('get',f'{host}/friends',headers =O00O0O00O00O00OOO ).json ()#line:1065
            if 'status'in O0OO0000O0OO00O00 :#line:1066
                if O0OO0000O0OO00O00 ['status']==200 :#line:1067
                    O0OOOO0OOO000000O =O0OO0000O0OO00O00 ['data']['myInviteter']#line:1068
                    if O0OOOO0OOO000000O :#line:1069
                        O00OO0OOOO00OO000 =O0OOOO0OOO000000O ['user']['nickname']#line:1070
                        O0OOOO00O0OO00OO0 =O0O0OO0O0O0O0000O .certification ()#line:1071
                        if O0OOOO00O0OO00OO0 =='未实名':#line:1072
                            weishim .append (O0O0OO0O0O0O0000O .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{O00OO0OOOO00OO000}丨实名:{O0OOOO00O0OO00OO0}')#line:1074
        except Exception as OO00O00O0OO0OO00O :#line:1078
            print (OO00O00O0OO0OO00O )#line:1079
    def add_clover (O0O0O0OO000O00O0O ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            O00OOOOOO0000O000 =f'__{timi_new()}'#line:1085
            OOO00000OOO00O0O0 ={'source':'scsc','authorization':O0O0O0OO000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO0000O000 ),'signstring':O00OOOOOO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OOOO0000O00O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00000OOO00O0O0 ).json ()#line:1097
            if 'status'in OOOO0000O00O0O0O0 :#line:1099
                if OOOO0000O00O0O0O0 ['status']==200 :#line:1100
                    O0OOOOOOOO00O0OOO =OOOO0000O00O0O0O0 ['data']['clover']#line:1101
                    O0O00O0OOO0O0O0O0 =OOOO0000O00O0O0O0 ['data']['used_clover']#line:1102
                    OOO0O00000OOOO0O0 =float (O0OOOOOOOO00O0OOO )-float (O0O00O0OOO0O0O0O0 )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O00O0OOO0O0O0O0}')#line:1104
                    if O0O0O0OO000O00O0O .certification ()!='未实名':#line:1105
                        if OOO0O00000OOOO0O0 >1 :#line:1106
                            O00OOOOOO0000O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0O00000OOOO0O0)}_{timi_new()}'#line:1107
                            O0OO0OO00OOO000OO ={'source':'scsc','authorization':O0O0O0OO000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO0000O000 ),'signstring':O00OOOOOO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            O0O0OO00O00OO0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0O00000OOOO0O0 )}#line:1119
                            OOO000O0O00OOO000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0OO00OOO000OO ,data =O0O0OO00O00OO0O00 ).json ()#line:1120
                            if 'status'in OOO000O0O00OOO000 :#line:1122
                                if OOO000O0O00OOO000 ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{OOO000O0O00OOO000["data"]["isSuccess"]}丨数量:{OOO0O00000OOOO0O0}')#line:1124
                                if OOO000O0O00OOO000 ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{OOO000O0O00OOO000["message"]}')#line:1126
            O0O0OOOO00O0O0O0O =requests .request ('get',f'{host}/lottery',headers =OOO00000OOO00O0O0 ).json ()#line:1127
            OO0OOOOOOO00OO00O =O0O0O0OO000O00O0O .winning_rewards ()#line:1129
            if 'status'in O0O0OOOO00O0O0O0O :#line:1130
                if O0O0OOOO00O0O0O0O ['status']==200 :#line:1131
                    O00OOOOO0OOOO00OO =O0O0OOOO00O0O0O0O ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (O00OOOOO0OOOO00OO )#line:1133
                    OO0OO0OOOOOO0O0OO =O0O0OOOO00O0O0O0O ['data'][1 ]['value']#line:1134
                    OOOO00OOOOO0O0OO0 =O0O0OOOO00O0O0O0O ['data'][0 ]['join_number']#line:1135
                    O00O000OO0O0OOOO0 =int (float (O0O0OOOO00O0O0O0O ['data'][0 ]['totalValue']))#line:1136
                    O00OO000OOOOO000O =float (OO0OO0OOOOOO0O0OO /O00O000OO0O0OOOO0 )*10000 #line:1137
                    O00OOOOO00O00O00O =O00O000OO0O0OOOO0 /OOOO00OOOOO0O0OO0 #line:1138
                    print (f'【参与抽奖】:预计每天中{str(O00OOOOO0OOOO00OO)[:6]}颗金种子丨好友收益:{str(OO0OOOOOOO00OO00O)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O00OO000OOOOO000O)[:6]}颗金种子丨☘️人均:{str(O00OOOOO00O00O00O)[:7]}️')#line:1140
        except Exception as OO0O0O0OO0OOO0O00 :#line:1141
            print (OO0O0O0OO0OOO0O00 )#line:1142
    def energy (O0OOO0O0000OO0O00 ):#line:1145
        try :#line:1146
            while True :#line:1147
                OO0OO000OOOOO00OO =f'__{timi_new()}'#line:1148
                OOO0OOOO000O0O0O0 ={'source':'scsc','authorization':O0OOO0O0000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOOOO00OO ),'signstring':OO0OO000OOOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                O0OOO000O0O0O00OO =requests .request ('get',f'{host}/energy/general',headers =OOO0OOOO000O0O0O0 ).json ()#line:1160
                if 'status'in O0OOO000O0O0O00OO :#line:1162
                    if O0OOO000O0O0O00OO ['status']==200 :#line:1163
                        O000O0OO000OOO000 =O0OOO000O0O0O00OO ['data']['ordinary_water']#line:1164
                        OOO0O0O0OO0O0O0O0 =O0OOO000O0O0O00OO ['data']['ordinary_fertilizer']#line:1165
                        OO00OOO00O0O00O0O =O0OOO000O0O0O00OO ['data']['videoStatus']#line:1166
                        O0O0OO0OO0OOOOOOO =O0OOO000O0O0O00OO ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(OOO0O0O0OO0O0O0O0).split(".")[0]}丨水滴:{str(O000O0OO000OOO000).split(".")[0]}')#line:1169
                        if float (OOO0O0O0OO0O0O0O0 )<96 :#line:1170
                            if OO00OOO00O0O00O0O :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OO0O0O0OO0OOO0OO0 =99 -float (OOO0O0O0OO0O0O0O0 )#line:1173
                                O0OO00O000OOO000O ={"fertilizer":str (OO0O0O0OO0OOO0OO0 ).split ('.')[0 ]}#line:1174
                                O0O00OOO0000O0O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO0OOOO000O0O0O0 ).json ()#line:1176
                                if 'status'in O0O00OOO0000O0O0O :#line:1178
                                    if O0O00OOO0000O0O0O ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00OOO0000O0O0O["message"]}')#line:1180
                                    if O0O00OOO0000O0O0O ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00OOO0000O0O0O["message"]}')#line:1182
                                        break #line:1183
                                if float (OOO0O0O0OO0O0O0O0 )<78 :#line:1185
                                    OO0O0O0OO0OOO0OO0 =80 -float (OOO0O0O0OO0O0O0O0 )#line:1186
                                    O0OO000OOO00OOOO0 =f'_fertilizer={int(OO0O0O0OO0OOO0OO0)}_{timi_new()}'#line:1187
                                    OO00OO0OO0000000O ={'source':'scsc','authorization':O0OOO0O0000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOO00OOOO0 ),'signstring':O0OO000OOO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    O00OO0O000OOO0O0O ={"fertilizer":int (OO0O0O0OO0OOO0OO0 )}#line:1199
                                    OOOO000OOO0OOO000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00OO0OO0000000O ,data =O00OO0O000OOO0O0O ).json ()#line:1201
                                    if 'status'in OOOO000OOO0OOO000 :#line:1203
                                        if OOOO000OOO0OOO000 ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OOOO000OOO0OOO000["message"]}丨数量:{int(OO0O0O0OO0OOO0OO0)}')#line:1205
                                        if OOOO000OOO0OOO000 ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OOOO000OOO0OOO000["message"]}丨数量:{int(OO0O0O0OO0OOO0OO0)}')#line:1207
                                            O0000OOO0OOO00000 =OOOO000OOO0OOO000 ["message"].split ('-')[1 ]#line:1208
                                            O0O0O000O00O00O0O =f'__{timi_new()}'#line:1209
                                            O00OO00O00O00O000 ={'source':'scsc','authorization':O0OOO0O0000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00O00O0O ),'signstring':O0O0O000O00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            OO0O0O00OOOOOO00O =requests .request ('get',f'{host}/user',headers =O00OO00O00O00O000 ).json ()#line:1221
                                            if 'status'in OO0O0O00OOOOOO00O :#line:1222
                                                if OO0O0O00OOOOOO00O ['status']==200 :#line:1223
                                                    O0O00OO00O00OOO0O =OO0O0O00OOOOOO00O ['data']['inner_id']#line:1224
                                                    if give_gold (O0O00OO00O00OOO0O ,float (O0000OOO0OOO00000 )+1 ):#line:1225
                                                        O0OOO0O0000OO0O00 .energy ()#line:1226
                        if float (O000O0OO000OOO000 )<880 :#line:1227
                            if O0O0OO0OO0OOOOOOO :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O0O0000000OOO00OO =999 -float (O000O0OO000OOO000 )#line:1230
                                OO0O00OOOOO0000OO ={"water":str (O0O0000000OOO00OO ).split ('.')[0 ]}#line:1231
                                O0O0OOO0O0OO000O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO0OOOO000O0O0O0 ).json ()#line:1233
                                if 'status'in O0O0OOO0O0OO000O0 :#line:1235
                                    if O0O0OOO0O0OO000O0 ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OOO0O0OO000O0["message"]}')#line:1237
                                    if O0O0OOO0O0OO000O0 ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OOO0O0OO000O0["message"]}')#line:1239
                                        break #line:1240
                                if float (O000O0OO000OOO000 )<780 :#line:1241
                                    O0O0000000OOO00OO =800 -float (O000O0OO000OOO000 )#line:1242
                                    OOOOO0O0OO000000O =f'_water={int(O0O0000000OOO00OO)}_{timi_new()}'#line:1243
                                    O0OOOOO000000OO0O ={'source':'scsc','authorization':O0OOO0O0000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0OO000000O ),'signstring':OOOOO0O0OO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    O0O00OOO0OOOO0O0O ={"water":int (O0O0000000OOO00OO )}#line:1255
                                    OO0OO00OO0O0O00O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOOOO000000OO0O ,data =O0O00OOO0OOOO0O0O ).json ()#line:1257
                                    if 'status'in OO0OO00OO0O0O00O0 :#line:1259
                                        if OO0OO00OO0O0O00O0 ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{OO0OO00OO0O0O00O0["message"]}丨数量:{int(O0O0000000OOO00OO)}')#line:1261
                                        if OO0OO00OO0O0O00O0 ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{OO0OO00OO0O0O00O0["message"]}丨数量:{int(O0O0000000OOO00OO)}')#line:1263
                                            O0000OOO0OOO00000 =OO0OO00OO0O0O00O0 ["message"].split ('-')[1 ]#line:1264
                                            O0O0O000O00O00O0O =f'__{timi_new()}'#line:1265
                                            O00OO00O00O00O000 ={'source':'scsc','authorization':O0OOO0O0000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00O00O0O ),'signstring':O0O0O000O00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            OO0O0O00OOOOOO00O =requests .request ('get',f'{host}/user',headers =O00OO00O00O00O000 ).json ()#line:1277
                                            if 'status'in OO0O0O00OOOOOO00O :#line:1278
                                                if OO0O0O00OOOOOO00O ['status']==200 :#line:1279
                                                    O0O00OO00O00OOO0O =OO0O0O00OOOOOO00O ['data']['inner_id']#line:1280
                                                    if give_gold (O0O00OO00O00OOO0O ,float (O0000OOO0OOO00000 )+1 ):#line:1281
                                                        O0OOO0O0000OO0O00 .energy ()#line:1282
                        break #line:1283
        except Exception as OO0OO000O0OO00O00 :#line:1284
            print (OO0OO000O0OO00O00 )#line:1285
def bundled_def ():#line:1288
    OO0OOOOO00O0O0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return OO0OOOOO00O0O0OO0 [random .randint (0 ,len (OO0OOOOO00O0O0OO0 )-1 )]#line:1290
def version_of_the_validation ():#line:1294
    return str ((106 -56 )/10 )#line:1295
def ubbbf ():#line:1297
    print ('卡密验证通过   ✅')#line:1298
def sc2 ():#line:1301
    return "19319#$%^&*((*"#line:1302
def OO00OO0OO0OO00OO00o0 ():#line:1305
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1307
def get_ip ():#line:1310
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1312
def gitee_validation ():#line:1315
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1316
def gitee_edition ():#line:1319
    try :#line:1320
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1321
    except :#line:1322
        sys .exit (0 )#line:1323
def O000OO000O0O00OOO00 ():#line:1327
    try :#line:1328
        O00O00OOOOO0OOOOO =gitee_edition ()#line:1329
        if version_of_the_validation ()<O00O00OOOOO0OOOOO ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OOOOO0OOOOO["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{O00O00OOOOO0OOOOO["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OOOOO0OOOOO["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {O00O00OOOOO0OOOOO["CityEarth"]["content"]}')#line:1335
    except Exception as O00O0000OO0OOOOOO :#line:1336
        print (O00O0000OO0OOOOOO )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
