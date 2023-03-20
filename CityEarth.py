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
        OOO0OO0OO0OO00OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOO0OO0OO0OO00OOO)}个账号==========")#line:17
        for O0O00O000000OOOOO in OOO0OO0OO0OO00OOO :#line:18
            OO000OOOOO00O000O =[]#line:19
            print (f"------------正在执行第{OOO0OO0OO0OO00OOO.index(O0O00O000000OOOOO) + 1}个账号------------")#line:20
            O0O0O00OOO00OO0O0 =CityEarth (O0O00O000000OOOOO ,OO000OOOOO00O000O ,OOO0OO0OO0OO00OOO .index (O0O00O000000OOOOO ))#line:21
            def O00OOO00OO00O000O ():#line:23
                if O0O0O00OOO00OO0O0 .base_info ():#line:25
                    O0O0O00OOO00OO0O0 .sealing ()#line:27
                    O0O0O00OOO00OO0O0 .invitenum ()#line:29
                    O0O0O00OOO00OO0O0 .query_to_sell ()#line:31
                    O0O0O00OOO00OO0O0 .friends_invitation ()#line:35
                    O0O0O00OOO00OO0O0 .energy ()#line:37
                    O0O0O00OOO00OO0O0 .add_clover ()#line:39
                    O0O0O00OOO00OO0O0 .propsraffle ()#line:41
                    O0O0O00OOO00OO0O0 .synthetic ()#line:43
                    O0O0O00OOO00OO0O0 .crops_illustrated ()#line:45
                    O0O0O00OOO00OO0O0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0O0O00OOO00OO0O0 .give_gold ()#line:50
            OOO0OOO0O0O0O0000 =threading .Thread (target =O00OOO00OO00O000O )#line:52
            OOO0OOO0O0O0O0000 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OOO0OO0OOO00OOOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0OO0OOO00OOOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOOOOOO00OO0OOOO in invited_new :#line:62
            print (OOOOOOOO00OO0OOOO )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0OO00000O0O000O in weishim :#line:65
            print (OO0OO00000O0O000O )#line:66
    except Exception as OOOO00O0O0OO0OO0O :#line:67
        print (OOOO00O0O0OO0OO0O )#line:68
def give_gold (O0OO00OO0000OOOOO ,O0O000O0OOOO0O000 ):#line:72
    try :#line:73
        OOOOOOOO0000OO00O =f'_doneeNo={O0OO00OO0000OOOOO}&quantity={int(O0O000O0OOOO0O000)}_{timi_new()}'#line:74
        O000OOO000O0O0000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0000OO00O ),'signstring':OOOOOOOO0000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOO0O00O00OO000O0 ={"quantity":int (O0O000O0OOOO0O000 ),"doneeNo":O0OO00OO0000OOOOO }#line:89
        OO0OO0OO0OOO00O00 =requests .request ('post',f'{host}/finance/give-gold',headers =O000OOO000O0O0000 ,data =OOO0O00O00OO000O0 ).json ()#line:90
        if 'status'in OO0OO0OO0OOO00O00 :#line:92
            if OO0OO0OO0OOO00O00 ['status']==200 :#line:93
                if OO0OO0OO0OOO00O00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0O000O0OOOO0O000)}种子给{O0OO00OO0000OOOOO}成功')#line:95
                    return True #line:96
            if OO0OO0OO0OOO00O00 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0OO0OO0OOO00O00["message"]}')#line:98
                return False #line:99
            if OO0OO0OO0OOO00O00 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0OO0OO0OOO00O00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00O00O0O0OOOO0OO :#line:104
        print (O00O00O0O0OOOO0OO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0000OO0OOOOO000O ):#line:115
    OO00000O00000OO0O =hashlib .md5 (O0000OO0OOOOO000O .encode ()).hexdigest ()#line:116
    OOO0OO0OO000O0O00 =sc1 ()#line:117
    OOO0OOO00O0OO0OOO =sc2 ()#line:118
    OOOO0OOO00O000O0O =sc3 ()#line:119
    OO0OO0O00O0O00OOO =OOO0OO0OO000O0O00 +OO00000O00000OO0O +OOO0OOO00O0OO0OOO +OOOO0OOO00O000O0O #line:120
    OOO0000O0OO0OO000 =hashlib .md5 (OO0OO0O00O0O00OOO .encode ()).hexdigest ()#line:121
    return OOO0000O0OO0OO000 #line:122
def format_msg ():#line:125
    O00OOOOOO0O0OO0OO =""#line:126
    for OO0OOOOOO0OO0000O in msg_list :#line:127
        O00OOOOOO0O0OO0OO +=str (OO0OOOOOO0OO0000O )+"\r\n"#line:128
    return O00OOOOOO0O0OO0OO #line:129
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
def get_json_data (O0O00OOO0OO00O000 ,OOOOOOO0O00O00O0O ,O0O0OO0O000O00OOO ,O0O0O0OOO00OO0OOO ):#line:153
    with open (O0O00OOO0OO00O000 ,'rb')as O0000OO00OOO0OO0O :#line:154
        OOOO0OO0OOO0O00OO =json .load (O0000OO00OOO0OO0O )#line:155
        OOOO0OO0OOO0O00OO ['data'][OOOOOOO0O00O00O0O ][O0O0OO0O000O00OOO ]=O0O0O0OOO00OO0OOO #line:156
        O0O000O0O00OO0O00 =OOOO0OO0OOO0O00OO #line:157
    O0000OO00OOO0OO0O .close ()#line:158
    return O0O000O0O00OO0O00 #line:159
def write_json_data (OOOOOO00OO0OOO000 ):#line:162
    with open (json_path1 ,'w')as OOO0OO00000OOOOOO :#line:163
        json .dump (OOOOOO00OO0OOO000 ,OOO0OO00000OOOOOO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OOO0OO00000OOOOOO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O00OO0000O0OO0OOO ,OOO0OO000O0O0OOO0 ,O0O0000O00OO0OO00 ,O00000000O00OO00O ):#line:171
        try :#line:172
            O00OO0000O0OO0OOO .msg =O0O0000O00OO0OO00 #line:173
            O00OO0000O0OO0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O00OO0000O0OO0OOO .token =OOO0OO000O0O0OOO0 ['authorization']#line:175
            O00OO0000O0OO0OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O00OO0000O0OO0OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O00OO0000O0OO0OOO .elephant_user =OOO0OO000O0O0OOO0 ['elephant_user']#line:178
            O00OO0000O0OO0OOO .elephant_pswd =OOO0OO000O0O0OOO0 ['elephant_pswd']#line:179
            O00OO0000O0OO0OOO .elephant_Task_ID =OOO0OO000O0O0OOO0 ['elephant_Task_ID']#line:180
            O00OO0000O0OO0OOO .len_new =O00000000O00OO00O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOO00O0OO00O0OO0 ):#line:186
        try :#line:187
            OOOO00O0OO00O0OO0 .watched_ad ()#line:189
            OO0OO0OO0OO00O000 =f'__{timi_new()}'#line:190
            O0000O0OOOOOO0O00 ={'source':'scsc','authorization':OOOO00O0OO00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0OO00O000 ),'signstring':OO0OO0OO0OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOOOO0OOO0OO0O0O =requests .request ('get',f'{host}/user',headers =O0000O0OOOOOO0O00 ).json ()#line:202
            if 'status'in OOOOOO0OOO0OO0O0O :#line:204
                if OOOOOO0OOO0OO0O0O ['status']==200 :#line:205
                    OOO0O0O000OO0OO00 =OOOOOO0OOO0OO0O0O ['data']['nickname']#line:206
                    OOO0000OOO0OO0OO0 =OOOOOO0OOO0OO0O0O ['data']['inner_id']#line:207
                    O0OOOO000000O0OO0 =OOOOOO0OOO0OO0O0O ['data']['assets']['gold']#line:208
                    OO0O00OOO0O00OOO0 =OOOOOO0OOO0OO0O0O ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOO0O0O000OO0OO00[:5]}丨ID:{OOO0000OOO0OO0OO0}丨等级:{OO0O00OOO0O00OOO0}丨金种子:{str(O0OOOO000000O0OO0).split(".")[0]}')#line:211
                    if 'wx_'in OOO0O0O000OO0OO00 :#line:212
                        OOOO00O0OO00O0OO0 .change_nickname ()#line:213
                if OOOOOO0OOO0OO0O0O ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOO00O0OO00O0OO0 .elephant_user =='f':#line:216
                        return False #line:217
                    O00OO0O0000O000O0 =Invalid_login .addtask (elephant_user =OOOO00O0OO00O0OO0 .elephant_user ,elephant_pswd =OOOO00O0OO00O0OO0 .elephant_pswd ,elephant_Task_ID =OOOO00O0OO00O0OO0 .elephant_Task_ID )#line:220
                    O000OOO0OOO0000O0 =get_json_data (json_path ,OOOO00O0OO00O0OO0 .len_new ,'authorization',O00OO0O0000O000O0 )#line:221
                    if write_json_data (O000OOO0OOO0000O0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOOOO0OOO0OO0O0O ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO0OOOO00O0000OO :#line:228
            print (OOO0OOOO00O0000OO )#line:229
    def sealing (O0000000O0OO0O000 ):#line:232
        try :#line:233
            OOO0O0000OOOO0O00 =f'__{timi_new()}'#line:234
            OOOOO000O000O0O0O ={'source':'scsc','authorization':O0000000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OOOO0O00 ),'signstring':OOO0O0000OOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOO000O000O0O0O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOOOO000O000O0O0O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOO000O000O0O0O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOO000O000O0O0O )#line:249
            requests .request ('get',f'{host}/user',headers =OOOOO000O000O0O0O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOO000O000O0O0O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOO000O000O0O0O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOO000O000O0O0O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOO000O000O0O0O )#line:254
            requests .request ('get',f'{host}/assets',headers =OOOOO000O000O0O0O )#line:255
        except Exception as O0O00OOOO00O000O0 :#line:256
            print (O0O00OOOO00O000O0 )#line:257
    def ddd (OO0OOO00O0O0O0OO0 ):#line:259
        try :#line:260
            OO000OOOOOO0OOO00 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO0000O0O0O00OOOO ={'source':'scsc','authorization':OO0OOO00O0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOOO0OOO00 ),'signstring':OO000OOOOOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOOOOOOOO00000000 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0000O0O0O00OOOO ).json ()#line:273
            print (OOOOOOOOO00000000 )#line:274
        except Exception as OOOOOO00000000OOO :#line:277
            print (OOOOOO00000000OOO )#line:278
    def the_query (OO0O0O0000O0O0O00 ):#line:283
        try :#line:284
            O00O00000O00O0000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0O00O0OOOO000000 ={'authorization':OO0O0O0000O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000O00O0000 ),'signstring':O00O00000O00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOO0OO00OOO000OO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0O00O0OOOO000000 ).json ()#line:296
            if 'status'in OOO0OO00OOO000OO0 :#line:298
                if OOO0OO00OOO000OO0 ['status']==200 :#line:299
                    return OOO0OO00OOO000OO0 ['data']['rows'][4 ]['price']#line:300
        except Exception as O00OOO00OO000OO00 :#line:301
            print (O00OOO00OO000OO00 )#line:302
    def market_sale (OO0OO0OOO0O0OO0O0 ,O00O0OO00000OO0OO ):#line:305
        try :#line:306
            OOO000000OOOOO00O =timi_new ()#line:307
            OOOOOO0OO00OO0OO0 =f'type=crop__{OOO000000OOOOO00O}'#line:308
            O000OOO00O000O000 ={'source':'scsc','authorization':OO0OO0OOO0O0OO0O0 .token ,'timestamp':str (OOO000000OOOOO00O ),'sign':sign (OOOOOO0OO00OO0OO0 ),'signstring':OOOOOO0OO00OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OO00O0O0000O00O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O000OOO00O000O000 ).json ()#line:320
            if 'status'in O0OO00O0O0000O00O :#line:322
                if O0OO00O0O0000O00O ['status']==200 :#line:323
                    if O0OO00O0O0000O00O ['data']['rows']:#line:324
                        O00O0O0OOO0O0O0O0 =O0OO00O0O0000O00O ['data']['rows'][0 ]['packsackItemId']#line:325
                        O00OOOOOOO0OO000O =O0OO00O0O0000O00O ['data']['rows'][0 ]['quantity']#line:326
                        if float (O00O0OO00000OO0OO )>6 :#line:327
                            OO0OOO00OO0OOO000 =f'_packsackItemId={O00O0O0OOO0O0O0O0}&price={str(O00O0OO00000OO0OO)[:5]}&quantity={O00OOOOOOO0OO000O}_{OOO000000OOOOO00O}'#line:328
                            O0O00O00O0O0OOO0O ={'source':'scsc','authorization':OO0OO0OOO0O0OO0O0 .token ,'timestamp':str (OOO000000OOOOO00O ),'sign':sign (OO0OOO00OO0OOO000 ),'signstring':OO0OOO00OO0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOOO00O000O0OOOO0 ={"packsackItemId":O00O0O0OOO0O0O0O0 ,"price":str (O00O0OO00000OO0OO )[:5 ],"quantity":str (O00OOOOOOO0OO000O )}#line:344
                            O0OOO00O000OOO00O =requests .request ('post',f'{host}/market/sale',headers =O0O00O00O0O0OOO0O ,data =OOOO00O000O0OOOO0 ).json ()#line:345
                            if 'status'in O0OOO00O000OOO00O :#line:347
                                if O0OOO00O000OOO00O ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O00OOOOOOO0OO000O}丨价格:{str(O00O0OO00000OO0OO)[:5]}')#line:349
                                if O0OOO00O000OOO00O ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O0OOO00O000OOO00O["message"]}')#line:351
        except Exception as OOO0OO00O0O000OOO :#line:352
            print (OOO0OO00O0O000OOO )#line:353
    def query_to_sell (O0O0O0O0O0000OOOO ):#line:356
        global count_list #line:357
        try :#line:358
            O00O000O00OOOO0OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OOO00O00OO0O0O00O ={'source':'scsc','authorization':O0O0O0O0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O00OOOO0OO ),'signstring':O00O000O00OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O00000O0O0000OO0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00O00OO0O0O00O ).json ()#line:371
            if 'status'in O00000O0O0000OO0O :#line:373
                if O00000O0O0000OO0O ['status']==200 :#line:374
                    for OO0O000OO0OO0OO0O in O00000O0O0000OO0O ['data']['rows']:#line:375
                        O00O0OO0O00O00OOO =OO0O000OO0OO0OO0O ['materialKey']#line:376
                        O0O00O000O0O0000O =OO0O000OO0OO0OO0O ['quantity']#line:377
                        O0OOO0O0O0O0OOOO0 =OO0O000OO0OO0OO0O ['price']#line:378
                        OOOOO000OO0OOO0OO =OO0O000OO0OO0OO0O ['saleState']#line:379
                        if OOOOO000OO0OOO0OO ==0 :#line:380
                            print (f'【出售订单】:名称:{O00O0OO0O00O00OOO}丨数量:{O0O00O000O0O0000O}丨价格:{O0OOO0O0O0O0OOOO0}')#line:381
                            count_list +=O0O00O000O0O0000O #line:382
                            O0OOOO0O0O0O00OO0 =O0O0O0O0O0000OOOO .the_query ()#line:384
                            if float (O0OOOO0O0O0O00OO0 )!=float (O0OOO0O0O0O0OOOO0 ):#line:385
                                O00OO0000OOOO0000 =OO0O000OO0OO0OO0O ['id']#line:386
        except Exception as OOOOO0OOO0O0OOO00 :#line:391
            print (OOOOO0OOO0O0OOO00 )#line:392
    def cacel_sale (O00O00OOOO000OO0O ,OOO0OO0OO000OOOO0 ):#line:395
        try :#line:396
            OO0O0OOO0OO00OO00 =f'_saleId={OOO0OO0OO000OOOO0}_{timi_new()}'#line:397
            O0OO00OO000OO0000 ={'source':'scsc','authorization':O00O00OOOO000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO0OO00OO00 ),'signstring':OO0O0OOO0OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            OO0O0000OO00OO00O ={"saleId":OOO0OO0OO000OOOO0 }#line:409
            O0OOOO000O0OO00OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OO00OO000OO0000 ,data =OO0O0000OO00OO00O ).json ()#line:410
            if 'status'in O0OOOO000O0OO00OO :#line:412
                if O0OOOO000O0OO00OO ['status']==200 :#line:413
                    print (f'【下架出售】:{O0OOOO000O0OO00OO["data"]}')#line:414
        except Exception as OOO0O0000OO000O00 :#line:415
            print (OOO0O0000OO000O00 )#line:416
    def change_nickname (O000OO0O00O0OOO00 ):#line:419
        try :#line:420
            O00O0000OO00O00O0 =timi_new ()#line:421
            O00OO000000OO000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OOOOO00O00OO0OOOO =requests .request ('post','https://www.qmsjmfb.com/',data =O00OO000000OO000O ).text #line:423
            O0000OOO0O0O0OOOO =re .findall ('<ul><li>(.*?)</li>',OOOOO00O00OO0OOOO )[0 ][:3 ]#line:424
            O0O0O0O0O00O0O0OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0000OOO0O0O0OOOO}').json ()#line:425
            OOOO0OOOO000OO0OO =O0O0O0O0O00O0O0OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            OO0OO0O00O0OOOOOO ={"nickname":OOOO0OOOO000OO0OO }#line:427
            O0OOO0000000000O0 =f'_nickname={OOOO0OOOO000OO0OO}_{O00O0000OO00O00O0}'#line:428
            O0OOOOOO0O00OOOO0 ={'source':'scsc','authorization':O000OO0O00O0OOO00 .token ,'timestamp':O00O0000OO00O00O0 ,'sign':sign (O0OOO0000000000O0 ),'signstring':O0OOO0000000000O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OOO0000O00O0OO0O0 =requests .request ('patch',f'{host}/user/nickname',headers =O0OOOOOO0O00OOOO0 ,data =OO0OO0O00O0OOOOOO ).json ()#line:440
            if 'status'in OOO0000O00O0OO0O0 :#line:442
                if OOO0000O00O0OO0O0 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OOOO0OOOO000OO0OO}丨{OOO0000O00O0OO0O0["message"]}')#line:444
        except Exception as O0OOOOOOOOOOOO00O :#line:445
            print (O0OOOOOOOOOOOO00O )#line:446
    def withdraw (OO0000OO0O0OOO00O ):#line:449
        try :#line:450
            O0OOO000O00OO000O =f'__{timi_new()}'#line:451
            O00O0OOO00O0O000O ={'source':'scsc','authorization':OO0000OO0O0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000O00OO000O ),'signstring':O0OOO000O00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OO0OOO0O0OOOOO0OO =requests .request ('get',f'{host}/assets',headers =O00O0OOO00O0O000O ).json ()#line:463
            if 'status'in OO0OOO0O0OOOOO0OO :#line:465
                if OO0OOO0O0OOOOO0OO ['status']==200 :#line:466
                    OOO0OOOO00O00O0O0 =OO0OOO0O0OOOOO0OO ['data']['cash']#line:467
                    if float (OOO0OOOO00O00O0O0 )>20 :#line:468
                        O0OOO000O00OO000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O00O0OOO00O0O000O ={'authorization':OO0000OO0O0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000O00OO000O ),'signstring':O0OOO000O00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OOO000O0O0OO0O0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        O0OOOOO0O000O00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O0OOO00O0O000O ,data =OOO000O0O0OO0O0OO ).json ()#line:482
                        if 'status'in O0OOOOO0O000O00O0 :#line:484
                            if O0OOOOO0O000O00O0 ['status']==200 :#line:485
                                print (f'【余额提现】:{O0OOOOO0O000O00O0["data"]}')#line:486
                        if 'status'in O0OOOOO0O000O00O0 :#line:487
                            if O0OOOOO0O000O00O0 ['status']==500 :#line:488
                                print (f'【余额提现】:{O0OOOOO0O000O00O0["message"]}')#line:489
        except Exception as OOOOO00O0O0OO0O0O :#line:490
            print (OOOOO00O0O0OO0O0O )#line:491
    def invitenum (OO00OOO0O0000OOOO ):#line:494
        global invited_new #line:495
        try :#line:496
            O0O000O0O00OO00O0 =f'__{timi_new()}'#line:497
            OOO00O0O00OOO000O ={'source':'scsc','authorization':OO00OOO0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O0O00OO00O0 ),'signstring':O0O000O0O00OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            O000O0OOO0000OO00 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO00O0O00OOO000O ).json ()#line:509
            if 'status'in O000O0OOO0000OO00 :#line:511
                if O000O0OOO0000OO00 ['status']==200 :#line:512
                    OOOOOO0000OO000O0 =O000O0OOO0000OO00 ['data']['invited_count']#line:513
                    OO00OOOOOOOO0OO0O =O000O0OOO0000OO00 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OOOOOO0000OO000O0}丨间邀好友:{OO00OOOOOOOO0OO0O}')#line:515
                    if OOOOOO0000OO000O0 <2 :#line:516
                        OO000OOOO000OOO0O =f'__{timi_new()}'#line:517
                        OO000O00O00O0O00O ={'source':'scsc','authorization':OO00OOO0O0000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO000OOO0O ),'signstring':OO000OOOO000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OO000OOOO0OO00O0O =requests .request ('get',f'{host}/user',headers =OO000O00O00O0O00O ).json ()#line:529
                        if 'status'in OO000OOOO0OO00O0O :#line:531
                            if OO000OOOO0OO00O0O ['status']==200 :#line:532
                                invited_new .append (OO000OOOO0OO00O0O ['data']['inner_id'])#line:533
        except Exception as O0O0O0O000O000OO0 :#line:534
            print (O0O0O0O000O000OO0 )#line:535
    def game_map (O0O000OO00O0OOOO0 ):#line:538
        try :#line:539
            O0000OOO0OOOOO0O0 =f'__{timi_new()}'#line:540
            OOO0OO0OOO0000OOO ={'source':'scsc','authorization':O0O000OO00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OOOOO0O0 ),'signstring':O0000OOO0OOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O0OO0O00000O000O0 =requests .request ('get',f'{host}/game/map',headers =OOO0OO0OOO0000OOO ).json ()#line:552
            if 'status'in O0OO0O00000O000O0 :#line:554
                if O0OO0O00000O000O0 ['status']==200 :#line:555
                    for O0000O0OOO0O0O00O in O0OO0O00000O000O0 ['data']['list'][0 ]['crops']:#line:556
                        O00O0OOO00O000O00 =O0000O0OOO0O0O00O ['level']#line:558
                        if O00O0OOO00O000O00 ==41 :#line:559
                            OO0O0OO0OOOOOOOO0 =O0000O0OOO0O0O00O ['crop_name']#line:560
                            O00OO00O000O0O000 =O0000O0OOO0O0O00O ['count']#line:561
                            if O00OO00O000O0O000 >0 :#line:562
                                print (f'【农业资产】:{OO0O0OO0OOOOOOOO0}丨数量:{O00OO00O000O0O000}')#line:563
                                O0O0O000OOOOOOO0O =O0O000OO00O0OOOO0 .the_query ()#line:564
                                O0O000OO00O0OOOO0 .market_sale (O0O0O000OOOOOOO0O )#line:565
        except Exception as O0000000000O0OOOO :#line:566
            print (O0000000000O0OOOO )#line:567
    def give_gold (O0O000O000OO0OO0O ):#line:570
        try :#line:571
            OOOOOO0O00OO00OOO =f'__{timi_new()}'#line:572
            O0000OO00OOO00000 ={'source':'scsc','authorization':O0O000O000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O00OO00OOO ),'signstring':OOOOOO0O00OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOOO00O0OOO0OOO0O =requests .request ('get',f'{host}/user',headers =O0000OO00OOO00000 ).json ()#line:584
            if 'status'in OOOO00O0OOO0OOO0O :#line:585
                if OOOO00O0OOO0OOO0O ['status']==200 :#line:586
                    if float (O0O000O000OO0OO0O .doneeNo )!=0 :#line:587
                        OO00OOOOOO0000O0O =OOOO00O0OOO0OOO0O ['data']['assets']['gold']#line:588
                        if float (OO00OOOOOO0000O0O )>float (O0O000O000OO0OO0O .innerId ):#line:589
                            O00O0O00O00OOOO0O =int (float (OO00OOOOOO0000O0O )/1.1 )#line:590
                            OOOOOO0O00OO00OOO =f'_doneeNo={O0O000O000OO0OO0O.doneeNo}&quantity={O00O0O00O00OOOO0O}_{timi_new()}'#line:591
                            O0000OO00OOO00000 ={'source':'scsc','authorization':O0O000O000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O00OO00OOO ),'signstring':OOOOOO0O00OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O00000O0OOO0OOOOO ={"quantity":O00O0O00O00OOOO0O ,"doneeNo":O0O000O000OO0OO0O .doneeNo }#line:606
                            O0OOO0000OOO00O0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0000OO00OOO00000 ,data =O00000O0OOO0OOOOO ).json ()#line:607
                            if 'status'in O0OOO0000OOO00O0O :#line:609
                                if O0OOO0000OOO00O0O ['status']==200 :#line:610
                                    if O0OOO0000OOO00O0O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{O00O0O00O00OOOO0O}种子给{O0O000O000OO0OO0O.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O00OO00OOO0O00000 :#line:615
            print (O00OO00OOO0O00000 )#line:616
    def invitation (OOO0O0OOOO0OOO0O0 ):#line:618
        try :#line:619
            _O0OOOOOO0O0O00O00 =float (bundled_def ())/4 #line:620
            O0OO0O00O0O0OOO0O =f'_innerId={int(_O0OOOOOO0O0O00O00)}_{timi_new()}'#line:622
            O0O00OOO00OOOOOOO ={'source':'scsc','authorization':OOO0O0OOOO0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00O0O0OOO0O ),'signstring':O0OO0O00O0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            OO0000OO0OOO0O0O0 ={"innerId":int (_O0OOOOOO0O0O00O00 )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00OOO00OOOOOOO ,data =OO0000OO0OOO0O0O0 )#line:635
        except Exception as OO00OO0000000000O :#line:636
            print (OO00OO0000000000O )#line:637
    def winning_rewards (O00000O0O000OOO00 ):#line:640
        try :#line:641
            OO000OOOOO0OOO00O =f'__{timi_new()}'#line:642
            O0OOOOO00O0OO0OOO ={'source':'scsc','authorization':O00000O0O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOO0OOO00O ),'signstring':OO000OOOOO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            O0000OO0O0O0OO000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOOO00O0OO0OOO ).json ()#line:654
            if 'status'in O0000OO0O0O0OO000 :#line:656
                if O0000OO0O0O0OO000 ['status']==200 :#line:657
                    if O0000OO0O0O0OO000 ['data']['amount']:#line:658
                        OO00O00OO0OOOOOOO =O0000OO0O0O0OO000 ['data']['amount']['gold']#line:659
                        return OO00O00OO0OOOOOOO #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOOOO0OOO000O0000 :#line:663
            print (OOOOO0OOO000O0000 )#line:664
    def certification (O0OO0O000OOOO0OO0 ):#line:667
        try :#line:668
            O000OOOOO0O000O0O =f'__{timi_new()}'#line:669
            OO00000OOO0O00000 ={'source':'scsc','authorization':O0OO0O000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0O000O0O ),'signstring':O000OOOOO0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O00OO0O00OOO00O0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00000OOO0O00000 ).json ()#line:681
            if 'status'in O00OO0O00OOO00O0O :#line:683
                if O00OO0O00OOO00O0O ['status']==200 :#line:684
                    if O00OO0O00OOO00O0O ['data']['result']:#line:685
                        O00OOO0O0O00OOO0O =O00OO0O00OOO00O0O ['data']['nick_name']#line:686
                        return O00OOO0O0O00OOO0O #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as OO000000OO000OOO0 :#line:690
            print (OO000000OO000OOO0 )#line:691
    def crops_illustrated (OO0O0OOO00OOOOO00 ):#line:694
        try :#line:695
            OO0OO000O0OO0OOOO =f'__{timi_new()}'#line:696
            OO00000O00OOO00O0 ={'source':'scsc','authorization':OO0O0OOO00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0OO0OOOO ),'signstring':OO0OO000O0OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O0OO0O0O00O0OOOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00000O00OOO00O0 ).json ()#line:708
            if 'status'in O0OO0O0O00O0OOOO0 :#line:710
                if O0OO0O0O00O0OOOO0 ['status']==200 :#line:711
                    OO00O00OO0OO00000 =O0OO0O0O00O0OOOO0 ['data'][0 ]['crops']#line:712
                    for O0O0O00O0000OOOO0 in OO00O00OO0OO00000 :#line:713
                        if O0O0O00O0000OOOO0 ['ill_clover_award']:#line:714
                            if float (O0O0O00O0000OOOO0 ['ill_clover_award'])>1 :#line:715
                                if O0O0O00O0000OOOO0 ['is_finish']:#line:716
                                    if not O0O0O00O0000OOOO0 ['is_getit']:#line:717
                                        if OO0O0OOO00OOOOO00 .certification ()!='未实名':#line:718
                                            OO0OO000O0OO0OOOO =f'_award_level={O0O0O00O0000OOOO0["level"]}_{timi_new()}'#line:719
                                            OO00000O00OOO00O0 ={'source':'scsc','authorization':OO0O0OOO00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0OO0OOOO ),'signstring':OO0OO000O0OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0OO000O0O000OO0O ={"award_level":O0O0O00O0000OOOO0 ['level']}#line:731
                                            OOO00O00OOOOOOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00000O00OOO00O0 ,json =O0OO000O0O000OO0O ).json ()#line:733
                                            if 'status'in OOO00O00OOOOOOO0O :#line:734
                                                if OOO00O00OOOOOOO0O ['status']==200 :#line:735
                                                    O0OOO0OO0OOO0O00O =OOO00O00OOOOOOO0O ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O0O0O00O0000OOOO0["crop_name"]}成就丨奖励{O0OOO0OO0OOO0O00O}☘️')#line:738
                                                if OOO00O00OOOOOOO0O ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OOO00O00OOOOOOO0O["message"]}')#line:740
        except Exception as O0OO0O00000OOOOO0 :#line:741
            print (O0OO0O00000OOOOO0 )#line:742
    def watched_ad (O000OO0O0O0O000O0 ):#line:745
        try :#line:746
            OO0000O00O0OOO0O0 =f'__{timi_new()}'#line:747
            OO000O00000O00O00 ={'source':'scsc','authorization':O000OO0O0O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O0OOO0O0 ),'signstring':OO0000O00O0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OOO000O0OO00O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO000O00000O00O00 ).json ()#line:759
            if 'status'in OOO000O0OO00O0OOO :#line:761
                if OOO000O0OO00O0OOO ['status']==200 :#line:762
                    if 'offlineInfo'in OOO000O0OO00O0OOO ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OO000O000OO0OOO00 =OOO000O0OO00O0OOO ['data']['offlineInfo']['off_minute']#line:765
                        O0OO00O0OO0OO000O =float (OOO000O0OO00O0OOO ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO000O00000O00O00 ).json ()#line:768
                        time .sleep (2 )#line:769
                        OO0O0000000O0O000 =requests .request ('get',f'{host}/game/getAllData',headers =OO000O00000O00O00 ).json ()#line:770
                        if 'status'in OO0O0000000O0O000 :#line:772
                            if OO0O0000000O0O000 ['status']==200 :#line:773
                                O0O0O00OOOO0O0000 =float (OO0O0000000O0O000 ['data']['silver'])/1000000000000 #line:774
                                OOOO000OO00000O0O =str (O0O0O00OOOO0O0000 -O0OO00O0OO0OO000O )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OO000O000OO0OOO00}分钟奖励🌱数量:{OOOO000OO00000O0O}t粒')#line:776
        except Exception as OO00O0O000O00OO00 :#line:777
            print (OO00O0O000O00OO00 )#line:778
    def user_ad (O000OOOO00O0000OO ):#line:781
        try :#line:782
            OO0OO0000O00O0OOO =f'__{timi_new()}'#line:783
            O0OO0000OOOO00OOO ={'source':'scsc','authorization':O000OOOO00O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000O00O0OOO ),'signstring':OO0OO0000O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O00OO00OO000OO000 =requests .request ('get',f'{host}/user/ad',headers =O0OO0000OOOO00OOO ).json ()#line:795
            if 'status'in O00OO00OO000OO000 :#line:797
                if O00OO00OO000OO000 ['status']==200 :#line:798
                    O0O0O0000O00OOO00 =O00OO00OO000OO000 ['data']['max_time']#line:799
                    OO0000OOO00000O00 =O00OO00OO000OO000 ['data']['watch_time']#line:800
                    OO0O0OOOO0OOOOOO0 =O00OO00OO000OO000 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{OO0O0OOOO0OOOOOO0 + O0O0O0000O00OOO00 - OO0000OOO00000O00}次丨好友提供:{OO0O0OOOO0OOOOOO0}次')#line:802
                    if OO0O0OOOO0OOOOOO0 +O0O0O0000O00OOO00 -OO0000OOO00000O00 >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OO0O000O00O0O0000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO0000OOOO00OOO ).json ()#line:805
                        if 'status'in OO0O000O00O0O0000 :#line:807
                            if OO0O000O00O0O0000 ['status']==200 :#line:808
                                OOOOOO0O0O0O00O00 =float (OO0O000O00O0O0000 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OOOOOO0O0O0O00O00)}t粒')#line:810
                                return True #line:811
                            if OO0O000O00O0O0000 ['status']==500 :#line:812
                                OO0OOO00OO000000O =OO0O000O00O0O0000 ['message']#line:813
                                print (f'【获取种子】:{OO0OOO00OO000000O}')#line:814
                                return False #line:815
        except Exception as O00O0OOO0O000000O :#line:816
            print (O00O0OOO0O000000O )#line:817
    def synthetic (O0O000O0OOOOOO0OO ):#line:820
        global id ,g #line:821
        try :#line:822
            OO0OOO0OO00O00O0O =O0O000O0OOOOOO0OO .level_new ()#line:823
            O00000O0OO00O00OO =random .randint (9 ,11 )#line:824
            O00O000O00OO0O000 =f'_site=8&targetSite={O00000O0OO00O00OO}_{timi_new()}'#line:825
            O0OOO00O0O000OO0O ={'source':'scsc','authorization':O0O000O0OOOOOO0OO .token ,'timestamp':timi_new (),'sign':sign (O00O000O00OO0O000 ),'signstring':O00O000O00OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OOO0O00O0O0O000O0 ={"site":int (8 ),"targetSite":int (O00000O0OO00O00OO )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00O0O000OO0O ,json =OOO0O00O0O0O000O0 )#line:838
            while True :#line:839
                OO0OO00000O0OO0O0 =f'__{timi_new()}'#line:840
                OOOO00OO0O0OOOO00 ={'source':'scsc','authorization':O0O000O0OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000O0OO0O0 ),'signstring':OO0OO00000O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O00OO000000O0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OO0O0OOOO00 ).json ()#line:852
                if 'status'in O00OO000000O0O0O0 :#line:854
                    if O00OO000000O0O0O0 ['status']==200 :#line:855
                        OOO0OO0O00OO00OO0 =O00OO000000O0O0O0 ['data']['cropList']#line:856
                        OOOO0000OO000O0O0 =O00OO000000O0O0O0 ['data']['gameCoreDataDBid']#line:857
                        O00O0O0000OOOO00O =float (O00OO000000O0O0O0 ['data']['silver'])/1000000000000 #line:858
                        OOOOO000OO000000O =0 #line:863
                        for O00OOOOO0O0O00OOO in OOO0OO0O00OO00OO0 :#line:864
                            if not O00OOOOO0O0O00OOO :#line:865
                                O00O0OO0O00OOO00O =f'_crop_id={OOOO0000OO000O0O0}&site={OOOOO000OO000000O}_{O0O000O0OOOOOO0OO.time}'#line:866
                                O0O00OOOO0OO0O0OO ={'source':'scsc','authorization':O0O000O0OOOOOO0OO .token ,'timestamp':O0O000O0OOOOOO0OO .time ,'sign':sign (O00O0OO0O00OOO00O ),'signstring':O00O0OO0O00OOO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                O0O00OO0O00O000O0 ={"site":OOOOO000OO000000O ,"crop_id":OOOO0000OO000O0O0 }#line:877
                                OOOO00OO000O0000O =requests .request ('post',f'{host}/game/crops/buy',headers =O0O00OOOO0OO0O0OO ,data =O0O00OO0O00O000O0 ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOOO00OO000O0000O :#line:881
                                    if OOOO00OO000O0000O ['status']==200 :#line:882
                                        if OOOO00OO000O0000O ['message']=='种子数量不足':#line:883
                                            OO0OOO0OO00O00O0O =O0O000O0OOOOOO0OO .level_new ()#line:884
                                            print (f'【种植合成】:{OOOO00OO000O0000O["message"]}')#line:885
                                            if not O0O000O0OOOOOO0OO .user_ad ():#line:886
                                                return False #line:887
                                    if OOOO00OO000O0000O ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOOO00OO000O0000O["message"]}')#line:889
                                        return False #line:890
                            OOOOO000OO000000O +=1 #line:891
                        O000O0OOO0O00O00O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OO0O0OOOO00 ).json ()#line:892
                        OO0000O0O0O0OOO0O =O000O0OOO0O00O00O ['data']['cropList']#line:893
                        OO0OO000OO000OOO0 =False #line:894
                        for O00OOOOO0O0O00OOO in range (12 ):#line:895
                            id =OO0000O0O0O0OOO0O [O00OOOOO0O0O00OOO ]['level']#line:896
                            if float (OO0OOO0OO00O00O0O )-float (id )>9 :#line:897
                                OO0O0O0OO00O0OOO0 =f'_site={O00OOOOO0O0O00OOO}_{timi_new()}'#line:898
                                O00OO0O0OO0OOO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000O0OOOOOO0OO .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0OO00O0OOO0 ),'signstring':OO0O0O0OO00O0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                OOO00O0OO0OO00000 ={"site":O00OOOOO0O0O00OOO }#line:910
                                OOO000000O0O0O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO0O0OO0OOO0OO ,data =OOO00O0OO0OO00000 ).json ()#line:912
                                if 'status'in OOO000000O0O0O00O :#line:913
                                    if OOO000000O0O0O00O ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OOOO000OOO000O0O0 in range (11 ):#line:917
                                    OO00O0OO0O0O0OO0O =OOOO000OOO000O0O0 +1 #line:918
                                    g =OO0000O0O0O0OOO0O [OO00O0OO0O0O0OO0O ]['level']#line:919
                                    if id ==g :#line:920
                                        O00O0000OO0OO0O0O =OOOO000OOO000O0O0 +2 #line:921
                                        if O00O0000OO0OO0O0O !=O00OOOOO0O0O00OOO +1 :#line:922
                                            OOO0OOO000O0O0000 =O00OOOOO0O0O00OOO +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O00O000O00OO0O000 =f'_site={OOO0OOO000O0O0000 - 1}&targetSite={O00O0000OO0OO0O0O - 1}_{timi_new()}'#line:926
                                            O0OOO00O0O000OO0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000O0OOOOOO0OO .token ,'timestamp':timi_new (),'sign':sign (O00O000O00OO0O000 ),'signstring':O00O000O00OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            OO0O0O0O000O0OOOO ={"site":int (OOO0OOO000O0O0000 -1 ),"targetSite":int (O00O0000OO0OO0O0O -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO00O0O000OO0O ,json =OO0O0O0O000O0OOOO )#line:945
                                            OO0OO000OO000OOO0 =True #line:947
                                    if OO0OO000OO000OOO0 :#line:948
                                        break #line:949
                                if OO0OO000OO000OOO0 :#line:950
                                    break #line:951
        except :#line:952
            O0O000O0OOOOOO0OO .synthetic ()#line:953
    def level_new (O0000OOOOO00O0OOO ):#line:956
        try :#line:957
            O000O000OOOOO0O00 =f'__{timi_new()}'#line:958
            O00OOOO0OO00O0O0O ={'source':'scsc','authorization':O0000OOOOO00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OOOOO0O00 ),'signstring':O000O000OOOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            OO000O0OOO000O000 =requests .request ('get',f'{host}/user',headers =O00OOOO0OO00O0O0O ).json ()#line:970
            if 'status'in OO000O0OOO000O000 :#line:971
                if OO000O0OOO000O000 ['status']==200 :#line:972
                    return float (OO000O0OOO000O000 ['data']['level'])#line:973
        except Exception as OOOO00OO0O0000OOO :#line:974
            print (OOOO00OO0O0000OOO )#line:975
    def propsraffle (OO0OO0O0O0OO0O0OO ):#line:978
        try :#line:979
            while True :#line:980
                O0O0O0O0O0OOO0000 =f'__{timi_new()}'#line:981
                OOOOO00OOOOO00O00 ={'source':'scsc','authorization':OO0OO0O0O0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O0OOO0000 ),'signstring':O0O0O0O0O0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OO0OOOOO000OOO0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOO00OOOOO00O00 ).json ()#line:993
                if 'status'in OO0OOOOO000OOO0O0 :#line:995
                    if OO0OOOOO000OOO0O0 ['status']==200 :#line:996
                        OOO000OOO00OO0O0O =OO0OOOOO000OOO0O0 ['data']['rows']#line:997
                        O0O00000O0OOOOOO0 =OO0OOOOO000OOO0O0 ['data']['vstate']#line:998
                        if OOO000OOO00OO0O0O ==5 or OOO000OOO00OO0O0O ==6 or OOO000OOO00OO0O0O ==7 :#line:999
                            O0OOO0O0000O0OOO0 =OO0OOOOO000OOO0O0 ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O0OOO0O0000O0OOO0}')#line:1001
                        if OOO000OOO00OO0O0O ==1 or OOO000OOO00OO0O0O ==2 or OOO000OOO00OO0O0O ==3 :#line:1002
                            O0OOO00O0O0O0O0O0 =OO0OOOOO000OOO0O0 ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO00O0O0O0O0O0}')#line:1004
                        if OOO000OOO00OO0O0O ==4 or OOO000OOO00OO0O0O ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OOO000OOO00OO0O0O =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OO00O0O0000OO0 :#line:1046
            print (OO0OO00O0O0000OO0 )#line:1047
    def friends_invitation (O00O0000OOO00OO00 ):#line:1050
        try :#line:1051
            O000OO0OO00OO000O =f'__{timi_new()}'#line:1052
            O0O0O0OOOOOO0OOOO ={'source':'scsc','authorization':O00O0000OOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OO00OO000O ),'signstring':O000OO0OO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            OO0O00OO0OOO000O0 =requests .request ('get',f'{host}/friends',headers =O0O0O0OOOOOO0OOOO ).json ()#line:1064
            if 'status'in OO0O00OO0OOO000O0 :#line:1065
                if OO0O00OO0OOO000O0 ['status']==200 :#line:1066
                    OOOO000O0O0000O00 =OO0O00OO0OOO000O0 ['data']['myInviteter']#line:1067
                    if OOOO000O0O0000O00 :#line:1068
                        O000000O0OO000000 =OOOO000O0O0000O00 ['user']['nickname']#line:1069
                        OOO000000O0O00O0O =O00O0000OOO00OO00 .certification ()#line:1070
                        if OOO000000O0O00O0O =='未实名':#line:1071
                            weishim .append (O00O0000OOO00OO00 .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O000000O0OO000000}丨实名:{OOO000000O0O00O0O}')#line:1073
        except Exception as O0OO0O0O0000O0000 :#line:1077
            print (O0OO0O0O0000O0000 )#line:1078
    def add_clover (O00OOOOO00O00O00O ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O0OO0O0O0OOOO0O0O =f'__{timi_new()}'#line:1084
            O0O0OOO0O0O0OO000 ={'source':'scsc','authorization':O00OOOOO00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0OOOO0O0O ),'signstring':O0OO0O0O0OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            O0000OO0O000000O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0OOO0O0O0OO000 ).json ()#line:1096
            if 'status'in O0000OO0O000000O0 :#line:1098
                if O0000OO0O000000O0 ['status']==200 :#line:1099
                    O0000O0000OO0O000 =O0000OO0O000000O0 ['data']['clover']#line:1100
                    OO0000OOOO0OOO000 =O0000OO0O000000O0 ['data']['used_clover']#line:1101
                    OOO000O00OOOOO0OO =float (O0000O0000OO0O000 )-float (OO0000OOOO0OOO000 )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0000OOOO0OOO000}')#line:1103
                    if O00OOOOO00O00O00O .certification ()!='未实名':#line:1104
                        if OOO000O00OOOOO0OO >1 :#line:1105
                            O0OO0O0O0OOOO0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO000O00OOOOO0OO)}_{timi_new()}'#line:1106
                            OOOO0O00OOO0O0O00 ={'source':'scsc','authorization':O00OOOOO00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0OOOO0O0O ),'signstring':O0OO0O0O0OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OOOO00O0OOO0O0000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO000O00OOOOO0OO )}#line:1118
                            O00OO00OOOO0OOOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0O00OOO0O0O00 ,data =OOOO00O0OOO0O0000 ).json ()#line:1119
                            if 'status'in O00OO00OOOO0OOOOO :#line:1121
                                if O00OO00OOOO0OOOOO ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O00OO00OOOO0OOOOO["data"]["isSuccess"]}丨数量:{OOO000O00OOOOO0OO}')#line:1123
                                if O00OO00OOOO0OOOOO ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O00OO00OOOO0OOOOO["message"]}')#line:1125
            O0O0OOOO0000O000O =requests .request ('get',f'{host}/lottery',headers =O0O0OOO0O0O0OO000 ).json ()#line:1126
            O0000O000OOOO00OO =O00OOOOO00O00O00O .winning_rewards ()#line:1128
            if 'status'in O0O0OOOO0000O000O :#line:1129
                if O0O0OOOO0000O000O ['status']==200 :#line:1130
                    O0OO0OOO0OOO000OO =O0O0OOOO0000O000O ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (O0OO0OOO0OOO000OO )#line:1132
                    O0O0OOO00O00OOOO0 =O0O0OOOO0000O000O ['data'][1 ]['value']#line:1133
                    OOO000OO00O00O000 =O0O0OOOO0000O000O ['data'][0 ]['join_number']#line:1134
                    O00O0O0OO0000OOOO =int (float (O0O0OOOO0000O000O ['data'][0 ]['totalValue']))#line:1135
                    OOO00O0O00O00O0OO =float (O0O0OOO00O00OOOO0 /O00O0O0OO0000OOOO )*10000 #line:1136
                    OOO0OO000000OO00O =O00O0O0OO0000OOOO /OOO000OO00O00O000 #line:1137
                    print (f'【参与抽奖】:预计每天中{str(O0OO0OOO0OOO000OO)[:6]}颗金种子丨好友收益:{str(O0000O000OOOO00OO)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OOO00O0O00O00O0OO)[:6]}颗金种子丨☘️人均:{str(OOO0OO000000OO00O)[:7]}️')#line:1139
        except Exception as O00OO0O0O0OO0OO00 :#line:1140
            print (O00OO0O0O0OO0OO00 )#line:1141
    def energy (OO0OOO00000OO00O0 ):#line:1144
        try :#line:1145
            while True :#line:1146
                OOOO000O0OO0O0000 =f'__{timi_new()}'#line:1147
                O000OO0O00OO0O0OO ={'source':'scsc','authorization':OO0OOO00000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0OO0O0000 ),'signstring':OOOO000O0OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                O000OO0OOOO00O000 =requests .request ('get',f'{host}/energy/general',headers =O000OO0O00OO0O0OO ).json ()#line:1159
                if 'status'in O000OO0OOOO00O000 :#line:1161
                    if O000OO0OOOO00O000 ['status']==200 :#line:1162
                        O00OOO0OOO00000O0 =O000OO0OOOO00O000 ['data']['ordinary_water']#line:1163
                        OOOO0O0O00O0OOO00 =O000OO0OOOO00O000 ['data']['ordinary_fertilizer']#line:1164
                        O0O000O000OOO00OO =O000OO0OOOO00O000 ['data']['videoStatus']#line:1165
                        OO00OO0000OOO000O =O000OO0OOOO00O000 ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(OOOO0O0O00O0OOO00).split(".")[0]}丨水滴:{str(O00OOO0OOO00000O0).split(".")[0]}')#line:1168
                        if float (OOOO0O0O00O0OOO00 )<96 :#line:1169
                            if O0O000O000OOO00OO :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OO0O0O0O0OO0O0O00 =99 -float (OOOO0O0O00O0OOO00 )#line:1172
                                O0000OOO0OO0O000O ={"fertilizer":str (OO0O0O0O0OO0O0O00 ).split ('.')[0 ]}#line:1173
                                O00O00OO00OOOOO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000OO0O00OO0O0OO ).json ()#line:1175
                                if 'status'in O00O00OO00OOOOO0O :#line:1177
                                    if O00O00OO00OOOOO0O ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00OO00OOOOO0O["message"]}')#line:1179
                                    if O00O00OO00OOOOO0O ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00OO00OOOOO0O["message"]}')#line:1181
                                        break #line:1182
                                if float (OOOO0O0O00O0OOO00 )<78 :#line:1184
                                    OO0O0O0O0OO0O0O00 =80 -float (OOOO0O0O00O0OOO00 )#line:1185
                                    O0O0OO0O0O000OO0O =f'_fertilizer={int(OO0O0O0O0OO0O0O00)}_{timi_new()}'#line:1186
                                    OOO0O0OO0O0O00000 ={'source':'scsc','authorization':OO0OOO00000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0O000OO0O ),'signstring':O0O0OO0O0O000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    O00000O0OO00O0OOO ={"fertilizer":int (OO0O0O0O0OO0O0O00 )}#line:1198
                                    OO0000OO0OOO0O0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0O0OO0O0O00000 ,data =O00000O0OO00O0OOO ).json ()#line:1200
                                    if 'status'in OO0000OO0OOO0O0OO :#line:1202
                                        if OO0000OO0OOO0O0OO ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OO0000OO0OOO0O0OO["message"]}丨数量:{int(OO0O0O0O0OO0O0O00)}')#line:1204
                                        if OO0000OO0OOO0O0OO ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OO0000OO0OOO0O0OO["message"]}丨数量:{int(OO0O0O0O0OO0O0O00)}')#line:1206
                                            O0O0000O00O0OOOO0 =OO0000OO0OOO0O0OO ["message"].split ('-')[1 ]#line:1207
                                            O000OOOOO000000O0 =f'__{timi_new()}'#line:1208
                                            O0O0O0OOO000O0OOO ={'source':'scsc','authorization':OO0OOO00000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO000000O0 ),'signstring':O000OOOOO000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OOO0OO0OOO00OO0OO =requests .request ('get',f'{host}/user',headers =O0O0O0OOO000O0OOO ).json ()#line:1220
                                            if 'status'in OOO0OO0OOO00OO0OO :#line:1221
                                                if OOO0OO0OOO00OO0OO ['status']==200 :#line:1222
                                                    OOOOOO0O0OO0O0O00 =OOO0OO0OOO00OO0OO ['data']['inner_id']#line:1223
                                                    if give_gold (OOOOOO0O0OO0O0O00 ,float (O0O0000O00O0OOOO0 )+1 ):#line:1224
                                                        OO0OOO00000OO00O0 .energy ()#line:1225
                        if float (O00OOO0OOO00000O0 )<880 :#line:1226
                            if OO00OO0000OOO000O :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                OOO0000O0000OO000 =999 -float (O00OOO0OOO00000O0 )#line:1229
                                O00O0OO0O0000OO00 ={"water":str (OOO0000O0000OO000 ).split ('.')[0 ]}#line:1230
                                O0O00OOO00O00OO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000OO0O00OO0O0OO ).json ()#line:1232
                                if 'status'in O0O00OOO00O00OO0O :#line:1234
                                    if O0O00OOO00O00OO0O ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{O0O00OOO00O00OO0O["message"]}')#line:1236
                                    if O0O00OOO00O00OO0O ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{O0O00OOO00O00OO0O["message"]}')#line:1238
                                        break #line:1239
                                if float (O00OOO0OOO00000O0 )<780 :#line:1240
                                    OOO0000O0000OO000 =800 -float (O00OOO0OOO00000O0 )#line:1241
                                    OOO0000O0OO000000 =f'_water={int(OOO0000O0000OO000)}_{timi_new()}'#line:1242
                                    OOO00OO0O0OOOO0O0 ={'source':'scsc','authorization':OO0OOO00000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O0OO000000 ),'signstring':OOO0000O0OO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    OOOOO00OOO0O00000 ={"water":int (OOO0000O0000OO000 )}#line:1254
                                    O00OOO0OO0O0OO000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00OO0O0OOOO0O0 ,data =OOOOO00OOO0O00000 ).json ()#line:1256
                                    if 'status'in O00OOO0OO0O0OO000 :#line:1258
                                        if O00OOO0OO0O0OO000 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O00OOO0OO0O0OO000["message"]}丨数量:{int(OOO0000O0000OO000)}')#line:1260
                                        if O00OOO0OO0O0OO000 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O00OOO0OO0O0OO000["message"]}丨数量:{int(OOO0000O0000OO000)}')#line:1262
                                            O0O0000O00O0OOOO0 =O00OOO0OO0O0OO000 ["message"].split ('-')[1 ]#line:1263
                                            O000OOOOO000000O0 =f'__{timi_new()}'#line:1264
                                            O0O0O0OOO000O0OOO ={'source':'scsc','authorization':OO0OOO00000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO000000O0 ),'signstring':O000OOOOO000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OOO0OO0OOO00OO0OO =requests .request ('get',f'{host}/user',headers =O0O0O0OOO000O0OOO ).json ()#line:1276
                                            if 'status'in OOO0OO0OOO00OO0OO :#line:1277
                                                if OOO0OO0OOO00OO0OO ['status']==200 :#line:1278
                                                    OOOOOO0O0OO0O0O00 =OOO0OO0OOO00OO0OO ['data']['inner_id']#line:1279
                                                    if give_gold (OOOOOO0O0OO0O0O00 ,float (O0O0000O00O0OOOO0 )+1 ):#line:1280
                                                        OO0OOO00000OO00O0 .energy ()#line:1281
                        break #line:1282
        except Exception as OOOO000OO0000000O :#line:1283
            print (OOOO000OO0000000O )#line:1284
def bundled_def ():#line:1287
    O000OO0OO00OO0O00 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return O000OO0OO00OO0O00 [random .randint (0 ,len (O000OO0OO00OO0O00 )-1 )]#line:1289
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
        OOO0O00OOOOO00O00 =gitee_edition ()#line:1328
        if version_of_the_validation ()<OOO0O00OOOOO00O00 ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O00OOOOO00O00["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{OOO0O00OOOOO00O00["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0O00OOOOO00O00["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {OOO0O00OOOOO00O00["CityEarth"]["content"]}')#line:1334
    except Exception as OO000O00OO0O00O0O :#line:1335
        print (OO000O00OO0O00O0O )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
