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
        OOO0OO0O00OO0O0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOO0OO0O00OO0O0O0)}个账号==========")#line:17
        for OOO0O0O0000O0O0O0 in OOO0OO0O00OO0O0O0 :#line:18
            O0000OO0000OOO0OO =[]#line:19
            print (f"------------正在执行第{OOO0OO0O00OO0O0O0.index(OOO0O0O0000O0O0O0) + 1}个账号------------")#line:20
            O00O0OO0O00OOO0O0 =CityEarth (OOO0O0O0000O0O0O0 ,O0000OO0000OOO0OO ,OOO0OO0O00OO0O0O0 .index (OOO0O0O0000O0O0O0 ))#line:21
            def OO0000000OO0O000O ():#line:23
                if O00O0OO0O00OOO0O0 .base_info ():#line:25
                    O00O0OO0O00OOO0O0 .sealing ()#line:27
                    O00O0OO0O00OOO0O0 .invitenum ()#line:29
                    O00O0OO0O00OOO0O0 .query_to_sell ()#line:31
                    O00O0OO0O00OOO0O0 .friends_invitation ()#line:35
                    O00O0OO0O00OOO0O0 .energy ()#line:37
                    O00O0OO0O00OOO0O0 .add_clover ()#line:39
                    O00O0OO0O00OOO0O0 .propsraffle ()#line:41
                    O00O0OO0O00OOO0O0 .synthetic ()#line:43
                    O00O0OO0O00OOO0O0 .crops_illustrated ()#line:45
                    O00O0OO0O00OOO0O0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O00O0OO0O00OOO0O0 .give_gold ()#line:50
            O0OO0OO0OOOOO0O0O =threading .Thread (target =OO0000000OO0O000O )#line:52
            O0OO0OO0OOOOO0O0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O000OO00OO00O0000 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000OO00OO00O0000 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO00000OOOOO0OOO in invited_new :#line:62
            print (OOO00000OOOOO0OOO )#line:63
        print ('开始打印未实名的token')#line:64
        for OOOOOO0OOO00OOOO0 in weishim :#line:65
            print (OOOOOO0OOO00OOOO0 )#line:66
    except Exception as O0OOOOOO0OO0OOOOO :#line:67
        print (O0OOOOOO0OO0OOOOO )#line:68
def give_gold (OO0000OO00OO000O0 ,OOO0O000OOOO00OO0 ):#line:72
    try :#line:73
        OOOOO0OO0OOO00O0O =f'_doneeNo={OO0000OO00OO000O0}&quantity={int(OOO0O000OOOO00OO0)}_{timi_new()}'#line:74
        O000O0OOOO00OO000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0OOO00O0O ),'signstring':OOOOO0OO0OOO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOOOO0OO0O00O0O0O ={"quantity":int (OOO0O000OOOO00OO0 ),"doneeNo":OO0000OO00OO000O0 }#line:89
        O0OO00OOOO000O000 =requests .request ('post',f'{host}/finance/give-gold',headers =O000O0OOOO00OO000 ,data =OOOOO0OO0O00O0O0O ).json ()#line:90
        if 'status'in O0OO00OOOO000O000 :#line:92
            if O0OO00OOOO000O000 ['status']==200 :#line:93
                if O0OO00OOOO000O000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO0O000OOOO00OO0)}种子给{OO0000OO00OO000O0}成功')#line:95
                    return True #line:96
            if O0OO00OOOO000O000 ['status']==401 :#line:97
                print (f'【赠送种子】:{O0OO00OOOO000O000["message"]}')#line:98
                return False #line:99
            if O0OO00OOOO000O000 ['status']==500 :#line:100
                print (f'【赠送种子】:{O0OO00OOOO000O000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0O0OOO0O0OO0OOO0 :#line:104
        print (O0O0OOO0O0OO0OOO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O00OO0O0OOO0OO0O0 ):#line:115
    O00000O0OO0O000O0 =hashlib .md5 (O00OO0O0OOO0OO0O0 .encode ()).hexdigest ()#line:116
    OOO0OOO0000OO0OO0 =sc1 ()#line:117
    OO0O0OO00O0OOOO00 =sc2 ()#line:118
    OO0O0OOOO000O00O0 =sc3 ()#line:119
    OO000OOO0OOO00O0O =OOO0OOO0000OO0OO0 +O00000O0OO0O000O0 +OO0O0OO00O0OOOO00 +OO0O0OOOO000O00O0 #line:120
    OOOO000OOOO0O0OOO =hashlib .md5 (OO000OOO0OOO00O0O .encode ()).hexdigest ()#line:121
    return OOOO000OOOO0O0OOO #line:122
def format_msg ():#line:125
    OOO000O00OO0OOOO0 =""#line:126
    for OOOOOO0O0OO00OO0O in msg_list :#line:127
        OOO000O00OO0OOOO0 +=str (OOOOOO0O0OO00OO0O )+"\r\n"#line:128
    return OOO000O00OO0OOOO0 #line:129
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
def get_json_data (OOOOO0OOOO0O00OO0 ,O0000O0OOOO00OO0O ,O00OOO0OOO0O0OOOO ,OOO00O000OOO0OOOO ):#line:153
    with open (OOOOO0OOOO0O00OO0 ,'rb')as O000000OOO00O0O00 :#line:154
        O0000000O0OO0OO00 =json .load (O000000OOO00O0O00 )#line:155
        O0000000O0OO0OO00 ['data'][O0000O0OOOO00OO0O ][O00OOO0OOO0O0OOOO ]=OOO00O000OOO0OOOO #line:156
        O0000OOO00O00O0OO =O0000000O0OO0OO00 #line:157
    O000000OOO00O0O00 .close ()#line:158
    return O0000OOO00O00O0OO #line:159
def write_json_data (O000000OOOO0000OO ):#line:162
    with open (json_path1 ,'w')as OOO0O00000O0O0000 :#line:163
        json .dump (O000000OOOO0000OO ,OOO0O00000O0O0000 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OOO0O00000O0O0000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OO000O00000OOO0 ,O000O0OO0OOO00O0O ,O00O0O0OO00OOO000 ,OOO000OO0OOOOOO0O ):#line:171
        try :#line:172
            O0OO000O00000OOO0 .msg =O00O0O0OO00OOO000 #line:173
            O0OO000O00000OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OO000O00000OOO0 .token =O000O0OO0OOO00O0O ['authorization']#line:175
            O0OO000O00000OOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OO000O00000OOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OO000O00000OOO0 .elephant_user =O000O0OO0OOO00O0O ['elephant_user']#line:178
            O0OO000O00000OOO0 .elephant_pswd =O000O0OO0OOO00O0O ['elephant_pswd']#line:179
            O0OO000O00000OOO0 .elephant_Task_ID =O000O0OO0OOO00O0O ['elephant_Task_ID']#line:180
            O0OO000O00000OOO0 .len_new =OOO000OO0OOOOOO0O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O00O0000OO0O0O0 ):#line:186
        try :#line:187
            O0O00O0000OO0O0O0 .watched_ad ()#line:189
            OOOOOO0O0O000OO00 =f'__{timi_new()}'#line:190
            O0O0O00O0OOO00O00 ={'source':'scsc','authorization':O0O00O0000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0O000OO00 ),'signstring':OOOOOO0O0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOO0000O0O000000 =requests .request ('get',f'{host}/user',headers =O0O0O00O0OOO00O00 ).json ()#line:202
            if 'status'in OOOO0000O0O000000 :#line:204
                if OOOO0000O0O000000 ['status']==200 :#line:205
                    O0000OOO0OOO0000O =OOOO0000O0O000000 ['data']['nickname']#line:206
                    O0OO000OO00000OOO =OOOO0000O0O000000 ['data']['inner_id']#line:207
                    O00O000OOOO0O00OO =OOOO0000O0O000000 ['data']['assets']['gold']#line:208
                    O0O00000OO0OOO0OO =OOOO0000O0O000000 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0000OOO0OOO0000O[:5]}丨ID:{O0OO000OO00000OOO}丨等级:{O0O00000OO0OOO0OO}丨金种子:{str(O00O000OOOO0O00OO).split(".")[0]}')#line:211
                    if 'wx_'in O0000OOO0OOO0000O :#line:212
                        O0O00O0000OO0O0O0 .change_nickname ()#line:213
                if OOOO0000O0O000000 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O00O0000OO0O0O0 .elephant_user =='f':#line:216
                        return False #line:217
                    OOOO00OOO0OOO0O0O =Invalid_login .addtask (elephant_user =O0O00O0000OO0O0O0 .elephant_user ,elephant_pswd =O0O00O0000OO0O0O0 .elephant_pswd ,elephant_Task_ID =O0O00O0000OO0O0O0 .elephant_Task_ID )#line:220
                    OO00O0000OO0OO000 =get_json_data (json_path ,O0O00O0000OO0O0O0 .len_new ,'authorization',OOOO00OOO0OOO0O0O )#line:221
                    if write_json_data (OO00O0000OO0OO000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOO0000O0O000000 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O00000OO0O00OOO00 :#line:228
            print (O00000OO0O00OOO00 )#line:229
    def sealing (OOOO0O00OOOO000O0 ):#line:232
        try :#line:233
            OOOO0O0O00OOOO0O0 =f'__{timi_new()}'#line:234
            O00O00OO0000O0OO0 ={'source':'scsc','authorization':OOOO0O00OOOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00OOOO0O0 ),'signstring':OOOO0O0O00OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O00OO0000O0OO0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O00O00OO0000O0OO0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O00OO0000O0OO0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O00OO0000O0OO0 )#line:249
            requests .request ('get',f'{host}/user',headers =O00O00OO0000O0OO0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O00OO0000O0OO0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O00OO0000O0OO0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O00OO0000O0OO0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O00O00OO0000O0OO0 )#line:254
            requests .request ('get',f'{host}/assets',headers =O00O00OO0000O0OO0 )#line:255
        except Exception as O00OO0OO0O0O0OOO0 :#line:256
            print (O00OO0OO0O0O0OOO0 )#line:257
    def ddd (OOO000O00OO0OO000 ):#line:259
        try :#line:260
            O0OOO0OO0000OO0O0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OOO0000O0O0000O00 ={'source':'scsc','authorization':OOO000O00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0000OO0O0 ),'signstring':O0OOO0OO0000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOOO0OO0OO0OO00O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO0000O0O0000O00 ).json ()#line:273
            print (OOOO0OO0OO0OO00O0 )#line:274
        except Exception as OOOOO0OOOOO00OO00 :#line:277
            print (OOOOO0OOOOO00OO00 )#line:278
    def the_query (O0O0OOO0O00O000O0 ):#line:283
        try :#line:284
            O00O00OOOOO00000O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0O0000O00O00OO00 ={'authorization':O0O0OOO0O00O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOOO00000O ),'signstring':O00O00OOOOO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O00OOOOOO0OO00OOO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0O0000O00O00OO00 ).json ()#line:296
            if 'status'in O00OOOOOO0OO00OOO :#line:298
                if O00OOOOOO0OO00OOO ['status']==200 :#line:299
                    return O00OOOOOO0OO00OOO ['data']['rows'][4 ]['price']#line:300
        except Exception as OOO00000O0OOO0OOO :#line:301
            print (OOO00000O0OOO0OOO )#line:302
    def market_sale (OOO0000000OO0O00O ,OOO00OOOO00O0OOOO ):#line:305
        try :#line:306
            O0O0000000000O0O0 =timi_new ()#line:307
            OOOOOOOO0000O0O0O =f'type=crop__{O0O0000000000O0O0}'#line:308
            O0O0O00O00O00O0O0 ={'source':'scsc','authorization':OOO0000000OO0O00O .token ,'timestamp':str (O0O0000000000O0O0 ),'sign':sign (OOOOOOOO0000O0O0O ),'signstring':OOOOOOOO0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O00O0O00O00000OOO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O00O00O00O0O0 ).json ()#line:320
            if 'status'in O00O0O00O00000OOO :#line:322
                if O00O0O00O00000OOO ['status']==200 :#line:323
                    if O00O0O00O00000OOO ['data']['rows']:#line:324
                        OOOO0OO000O00O0O0 =O00O0O00O00000OOO ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0O00000OOOO0000O =O00O0O00O00000OOO ['data']['rows'][0 ]['quantity']#line:326
                        if float (OOO00OOOO00O0OOOO )>6 :#line:327
                            O0OO00OOO000000OO =f'_packsackItemId={OOOO0OO000O00O0O0}&price={str(OOO00OOOO00O0OOOO)[:5]}&quantity={O0O00000OOOO0000O}_{O0O0000000000O0O0}'#line:328
                            OOOO000O00OOOO00O ={'source':'scsc','authorization':OOO0000000OO0O00O .token ,'timestamp':str (O0O0000000000O0O0 ),'sign':sign (O0OO00OOO000000OO ),'signstring':O0OO00OOO000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOOO00OOOOO0O000O ={"packsackItemId":OOOO0OO000O00O0O0 ,"price":str (OOO00OOOO00O0OOOO )[:5 ],"quantity":str (O0O00000OOOO0000O )}#line:344
                            OOO0000O000OOOOO0 =requests .request ('post',f'{host}/market/sale',headers =OOOO000O00OOOO00O ,data =OOOO00OOOOO0O000O ).json ()#line:345
                            if 'status'in OOO0000O000OOOOO0 :#line:347
                                if OOO0000O000OOOOO0 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O0O00000OOOO0000O}丨价格:{str(OOO00OOOO00O0OOOO)[:5]}')#line:349
                                if OOO0000O000OOOOO0 ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{OOO0000O000OOOOO0["message"]}')#line:351
        except Exception as OOOOOOO00OOOOO000 :#line:352
            print (OOOOOOO00OOOOO000 )#line:353
    def query_to_sell (O00OOOOO0O0O0OOO0 ):#line:356
        global count_list #line:357
        try :#line:358
            OO0O00OO0O0O00O00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            O000O0OOOO0OOO00O ={'source':'scsc','authorization':O00OOOOO0O0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO0O0O00O00 ),'signstring':OO0O00OO0O0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O0OOOOO0O0O0000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O000O0OOOO0OOO00O ).json ()#line:371
            if 'status'in O0OOOOO0O0O0000O0 :#line:373
                if O0OOOOO0O0O0000O0 ['status']==200 :#line:374
                    for O0O00OO0000O0O0O0 in O0OOOOO0O0O0000O0 ['data']['rows']:#line:375
                        OO0OO00O0O00OO0O0 =O0O00OO0000O0O0O0 ['materialKey']#line:376
                        OO00OOO0OOOOOOO0O =O0O00OO0000O0O0O0 ['quantity']#line:377
                        OO00OO0O0O00O00O0 =O0O00OO0000O0O0O0 ['price']#line:378
                        O0000O0O00O0O0OO0 =O0O00OO0000O0O0O0 ['saleState']#line:379
                        if O0000O0O00O0O0OO0 ==0 :#line:380
                            print (f'【出售订单】:名称:{OO0OO00O0O00OO0O0}丨数量:{OO00OOO0OOOOOOO0O}丨价格:{OO00OO0O0O00O00O0}')#line:381
                            count_list +=OO00OOO0OOOOOOO0O #line:382
                            O00OO0O00OO00000O =O00OOOOO0O0O0OOO0 .the_query ()#line:384
                            if float (O00OO0O00OO00000O )!=float (OO00OO0O0O00O00O0 ):#line:385
                                OOO0O00O0O0OO00OO =O0O00OO0000O0O0O0 ['id']#line:386
                                O00OOOOO0O0O0OOO0 .cacel_sale (OOO0O00O0O0OO00OO )#line:387
        except Exception as O0OOOO000O0O0OO00 :#line:391
            print (O0OOOO000O0O0OO00 )#line:392
    def cacel_sale (O00000OOO00OOOO0O ,O0OO0O00OOO0000O0 ):#line:395
        try :#line:396
            OO0OO000OOO0000OO =f'_saleId={O0OO0O00OOO0000O0}_{timi_new()}'#line:397
            OOOO00O0O0O0000O0 ={'source':'scsc','authorization':O00000OOO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOO0000OO ),'signstring':OO0OO000OOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O0O00OOO0O00OOOO0 ={"saleId":O0OO0O00OOO0000O0 }#line:409
            O0OOOO000OOO00000 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOO00O0O0O0000O0 ,data =O0O00OOO0O00OOOO0 ).json ()#line:410
            if 'status'in O0OOOO000OOO00000 :#line:412
                if O0OOOO000OOO00000 ['status']==200 :#line:413
                    print (f'【下架出售】:{O0OOOO000OOO00000["data"]}')#line:414
        except Exception as O0O0000OO0OO0O0O0 :#line:415
            print (O0O0000OO0OO0O0O0 )#line:416
    def change_nickname (OOO000000O00000OO ):#line:419
        try :#line:420
            OOOOO0O0OOOOO0OO0 =timi_new ()#line:421
            O00O0OO0O00OOO0OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O0OO0O000OO00O0OO =requests .request ('post','https://www.qmsjmfb.com/',data =O00O0OO0O00OOO0OO ).text #line:423
            OO00O0O0000000OO0 =re .findall ('<ul><li>(.*?)</li>',O0OO0O000OO00O0OO )[0 ][:3 ]#line:424
            OOOO00000O0O0O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO00O0O0000000OO0}').json ()#line:425
            O000O0O00OOO00O0O =OOOO00000O0O0O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            O0000OO0OO0OO00O0 ={"nickname":O000O0O00OOO00O0O }#line:427
            OO0OOO0OOO0OOOO00 =f'_nickname={O000O0O00OOO00O0O}_{OOOOO0O0OOOOO0OO0}'#line:428
            OOOO0O0OOOO000O00 ={'source':'scsc','authorization':OOO000000O00000OO .token ,'timestamp':OOOOO0O0OOOOO0OO0 ,'sign':sign (OO0OOO0OOO0OOOO00 ),'signstring':OO0OOO0OOO0OOOO00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            O0OOOOO00O000OO00 =requests .request ('patch',f'{host}/user/nickname',headers =OOOO0O0OOOO000O00 ,data =O0000OO0OO0OO00O0 ).json ()#line:440
            if 'status'in O0OOOOO00O000OO00 :#line:442
                if O0OOOOO00O000OO00 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O000O0O00OOO00O0O}丨{O0OOOOO00O000OO00["message"]}')#line:444
        except Exception as OOO000O000OO0O0O0 :#line:445
            print (OOO000O000OO0O0O0 )#line:446
    def withdraw (OO0OO0OOOOOOOO0O0 ):#line:449
        try :#line:450
            O00OO0000OO00O0OO =f'__{timi_new()}'#line:451
            O0O00O00OO000O000 ={'source':'scsc','authorization':OO0OO0OOOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000OO00O0OO ),'signstring':O00OO0000OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            O00000O0O0O000OOO =requests .request ('get',f'{host}/assets',headers =O0O00O00OO000O000 ).json ()#line:463
            if 'status'in O00000O0O0O000OOO :#line:465
                if O00000O0O0O000OOO ['status']==200 :#line:466
                    OO0000OO00O0O00OO =O00000O0O0O000OOO ['data']['cash']#line:467
                    if float (OO0000OO00O0O00OO )>20 :#line:468
                        O00OO0000OO00O0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O0O00O00OO000O000 ={'authorization':OO0OO0OOOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000OO00O0OO ),'signstring':O00OO0000OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OOO0O0O00000OO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OO0O0OOOO000OOOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00O00OO000O000 ,data =OOO0O0O00000OO0O0 ).json ()#line:482
                        if 'status'in OO0O0OOOO000OOOO0 :#line:484
                            if OO0O0OOOO000OOOO0 ['status']==200 :#line:485
                                print (f'【余额提现】:{OO0O0OOOO000OOOO0["data"]}')#line:486
                        if 'status'in OO0O0OOOO000OOOO0 :#line:487
                            if OO0O0OOOO000OOOO0 ['status']==500 :#line:488
                                print (f'【余额提现】:{OO0O0OOOO000OOOO0["message"]}')#line:489
        except Exception as O00O000O00O0O00O0 :#line:490
            print (O00O000O00O0O00O0 )#line:491
    def invitenum (O0OOO0O00OO000000 ):#line:494
        global invited_new #line:495
        try :#line:496
            O0OO00O0O0O000O0O =f'__{timi_new()}'#line:497
            O00OO00OO0OO0OO0O ={'source':'scsc','authorization':O0OOO0O00OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0O000O0O ),'signstring':O0OO00O0O0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OO0OOOOOOO00OOOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00OO00OO0OO0OO0O ).json ()#line:509
            if 'status'in OO0OOOOOOO00OOOO0 :#line:511
                if OO0OOOOOOO00OOOO0 ['status']==200 :#line:512
                    OO0OOOOOO0000O00O =OO0OOOOOOO00OOOO0 ['data']['invited_count']#line:513
                    O0OOOO0O0OOOO00OO =OO0OOOOOOO00OOOO0 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OO0OOOOOO0000O00O}丨间邀好友:{O0OOOO0O0OOOO00OO}')#line:515
                    if OO0OOOOOO0000O00O <2 :#line:516
                        O000O0O000O00OO0O =f'__{timi_new()}'#line:517
                        OO0O00OO00O0O000O ={'source':'scsc','authorization':O0OOO0O00OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O000O00OO0O ),'signstring':O000O0O000O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        O00000000OO00OO00 =requests .request ('get',f'{host}/user',headers =OO0O00OO00O0O000O ).json ()#line:529
                        if 'status'in O00000000OO00OO00 :#line:531
                            if O00000000OO00OO00 ['status']==200 :#line:532
                                invited_new .append (O00000000OO00OO00 ['data']['inner_id'])#line:533
        except Exception as O0O0OOOO00OOOO000 :#line:534
            print (O0O0OOOO00OOOO000 )#line:535
    def game_map (OO0OO00000O0OOO0O ):#line:538
        try :#line:539
            OO0O000O000OO0OO0 =f'__{timi_new()}'#line:540
            OOO0OOO00000O0000 ={'source':'scsc','authorization':OO0OO00000O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O000OO0OO0 ),'signstring':OO0O000O000OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O00O00OOO00OO000O =requests .request ('get',f'{host}/game/map',headers =OOO0OOO00000O0000 ).json ()#line:552
            if 'status'in O00O00OOO00OO000O :#line:554
                if O00O00OOO00OO000O ['status']==200 :#line:555
                    for OOOOOOOOO00OOOOO0 in O00O00OOO00OO000O ['data']['list'][0 ]['crops']:#line:556
                        OO0O0O0OOO0000O0O =OOOOOOOOO00OOOOO0 ['level']#line:558
                        if OO0O0O0OOO0000O0O ==41 :#line:559
                            OO000OO0OO0O0OO0O =OOOOOOOOO00OOOOO0 ['crop_name']#line:560
                            OO000000OOOOO0OO0 =OOOOOOOOO00OOOOO0 ['count']#line:561
                            if OO000000OOOOO0OO0 >0 :#line:562
                                print (f'【农业资产】:{OO000OO0OO0O0OO0O}丨数量:{OO000000OOOOO0OO0}')#line:563
                                OO00OO0O0OOO0O000 =OO0OO00000O0OOO0O .the_query ()#line:564
                                OO0OO00000O0OOO0O .market_sale (OO00OO0O0OOO0O000 )#line:565
        except Exception as O0OOOO0OO00OO0OO0 :#line:566
            print (O0OOOO0OO00OO0OO0 )#line:567
    def give_gold (O00O0OOO0000O00O0 ):#line:570
        try :#line:571
            OO0O00OOO0OO00O00 =f'__{timi_new()}'#line:572
            OOO0O0000O00O0O0O ={'source':'scsc','authorization':O00O0OOO0000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0OO00O00 ),'signstring':OO0O00OOO0OO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            O0O0OOO00000OO0OO =requests .request ('get',f'{host}/user',headers =OOO0O0000O00O0O0O ).json ()#line:584
            if 'status'in O0O0OOO00000OO0OO :#line:585
                if O0O0OOO00000OO0OO ['status']==200 :#line:586
                    if float (O00O0OOO0000O00O0 .doneeNo )!=0 :#line:587
                        OOOOOOOO000OOO0O0 =O0O0OOO00000OO0OO ['data']['assets']['gold']#line:588
                        if float (OOOOOOOO000OOO0O0 )>float (O00O0OOO0000O00O0 .innerId ):#line:589
                            O0O00OO0O0O0000OO =int (float (OOOOOOOO000OOO0O0 )/1.1 )#line:590
                            OO0O00OOO0OO00O00 =f'_doneeNo={O00O0OOO0000O00O0.doneeNo}&quantity={O0O00OO0O0O0000OO}_{timi_new()}'#line:591
                            OOO0O0000O00O0O0O ={'source':'scsc','authorization':O00O0OOO0000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0OO00O00 ),'signstring':OO0O00OOO0OO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O000OO0OO0OOOOO00 ={"quantity":O0O00OO0O0O0000OO ,"doneeNo":O00O0OOO0000O00O0 .doneeNo }#line:606
                            O00000OO00000O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O0000O00O0O0O ,data =O000OO0OO0OOOOO00 ).json ()#line:607
                            if 'status'in O00000OO00000O000 :#line:609
                                if O00000OO00000O000 ['status']==200 :#line:610
                                    if O00000OO00000O000 ['data']:#line:611
                                        print (f'【赠送种子】:赠送{O0O00OO0O0O0000OO}种子给{O00O0OOO0000O00O0.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O000000O0OOOOO000 :#line:615
            print (O000000O0OOOOO000 )#line:616
    def invitation (O0O000OOO00OO0O00 ):#line:618
        try :#line:619
            _OOOO0OOO000O0O0OO =float (bundled_def ())/4 #line:620
            O000OOOO00000OO00 =f'_innerId={int(_OOOO0OOO000O0O0OO)}_{timi_new()}'#line:622
            O00OO0O00O00O0OO0 ={'source':'scsc','authorization':O0O000OOO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00000OO00 ),'signstring':O000OOOO00000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            O0OOO0000O00O000O ={"innerId":int (_OOOO0OOO000O0O0OO )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00OO0O00O00O0OO0 ,data =O0OOO0000O00O000O )#line:635
        except Exception as O0O00OOO00OOOOO00 :#line:636
            print (O0O00OOO00OOOOO00 )#line:637
    def winning_rewards (OO0O000OOO000O000 ):#line:640
        try :#line:641
            OO000O000OOO000OO =f'__{timi_new()}'#line:642
            O00O0O0OO0O0O000O ={'source':'scsc','authorization':OO0O000OOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000OOO000OO ),'signstring':OO000O000OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            O0OO0O0OOO00OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O0O0OO0O0O000O ).json ()#line:654
            if 'status'in O0OO0O0OOO00OOO0O :#line:656
                if O0OO0O0OOO00OOO0O ['status']==200 :#line:657
                    if O0OO0O0OOO00OOO0O ['data']['amount']:#line:658
                        OO0OO0O0OOO00O00O =O0OO0O0OOO00OOO0O ['data']['amount']['gold']#line:659
                        return OO0OO0O0OOO00O00O #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOOOOOOOO0O0O0OOO :#line:663
            print (OOOOOOOOO0O0O0OOO )#line:664
    def certification (O00O000O000OO0OOO ):#line:667
        try :#line:668
            O00OO00OOO00OOOO0 =f'__{timi_new()}'#line:669
            OOOOO000000OOO0O0 ={'source':'scsc','authorization':O00O000O000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OOO00OOOO0 ),'signstring':O00OO00OOO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O0O0OO00000O0000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOO000000OOO0O0 ).json ()#line:681
            if 'status'in O0O0OO00000O0000O :#line:683
                if O0O0OO00000O0000O ['status']==200 :#line:684
                    if O0O0OO00000O0000O ['data']['result']:#line:685
                        OO0O000OOOO0OO00O =O0O0OO00000O0000O ['data']['nick_name']#line:686
                        return OO0O000OOOO0OO00O #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as OOOOO00OOOO0O00OO :#line:690
            print (OOOOO00OOOO0O00OO )#line:691
    def crops_illustrated (OO00O00O0O0O000OO ):#line:694
        try :#line:695
            O0O0000OOO00OO0OO =f'__{timi_new()}'#line:696
            OOO0O0OOOO0000OOO ={'source':'scsc','authorization':OO00O00O0O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOO00OO0OO ),'signstring':O0O0000OOO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O00OO0O0O0O00OOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O0OOOO0000OOO ).json ()#line:708
            if 'status'in O00OO0O0O0O00OOOO :#line:710
                if O00OO0O0O0O00OOOO ['status']==200 :#line:711
                    OOO0O000OOO00O00O =O00OO0O0O0O00OOOO ['data'][0 ]['crops']#line:712
                    for OOOOOO0O0000000O0 in OOO0O000OOO00O00O :#line:713
                        if OOOOOO0O0000000O0 ['ill_clover_award']:#line:714
                            if float (OOOOOO0O0000000O0 ['ill_clover_award'])>1 :#line:715
                                if OOOOOO0O0000000O0 ['is_finish']:#line:716
                                    if not OOOOOO0O0000000O0 ['is_getit']:#line:717
                                        if OO00O00O0O0O000OO .certification ()!='未实名':#line:718
                                            O0O0000OOO00OO0OO =f'_award_level={OOOOOO0O0000000O0["level"]}_{timi_new()}'#line:719
                                            OOO0O0OOOO0000OOO ={'source':'scsc','authorization':OO00O00O0O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOO00OO0OO ),'signstring':O0O0000OOO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0OOOO000OO0OO000 ={"award_level":OOOOOO0O0000000O0 ['level']}#line:731
                                            O00OO00000O0OO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O0OOOO0000OOO ,json =O0OOOO000OO0OO000 ).json ()#line:733
                                            if 'status'in O00OO00000O0OO0O0 :#line:734
                                                if O00OO00000O0OO0O0 ['status']==200 :#line:735
                                                    OOO0O00000O00O0OO =O00OO00000O0OO0O0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{OOOOOO0O0000000O0["crop_name"]}成就丨奖励{OOO0O00000O00O0OO}☘️')#line:738
                                                if O00OO00000O0OO0O0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{O00OO00000O0OO0O0["message"]}')#line:740
        except Exception as OOO000OOOO0O00OOO :#line:741
            print (OOO000OOOO0O00OOO )#line:742
    def watched_ad (O0O0O0OO0O000OOO0 ):#line:745
        try :#line:746
            OO00O0O0OO000O00O =f'__{timi_new()}'#line:747
            OOOOO0OO0000OOOO0 ={'source':'scsc','authorization':O0O0O0OO0O000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OO000O00O ),'signstring':OO00O0O0OO000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            O0OO0O0O0OO0O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OO0000OOOO0 ).json ()#line:759
            if 'status'in O0OO0O0O0OO0O0O0O :#line:761
                if O0OO0O0O0OO0O0O0O ['status']==200 :#line:762
                    if 'offlineInfo'in O0OO0O0O0OO0O0O0O ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        O0O00O000000O0O0O =O0OO0O0O0OO0O0O0O ['data']['offlineInfo']['off_minute']#line:765
                        O0OOO00O0O0O0O0O0 =float (O0OO0O0O0OO0O0O0O ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOOO0OO0000OOOO0 ).json ()#line:768
                        time .sleep (2 )#line:769
                        OOOOO0OO000000O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0OO0000OOOO0 ).json ()#line:770
                        if 'status'in OOOOO0OO000000O00 :#line:772
                            if OOOOO0OO000000O00 ['status']==200 :#line:773
                                OO00O0OOO0O0OOOO0 =float (OOOOO0OO000000O00 ['data']['silver'])/1000000000000 #line:774
                                OO00OOO0O00OO0OO0 =str (OO00O0OOO0O0OOOO0 -O0OOO00O0O0O0O0O0 )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{O0O00O000000O0O0O}分钟奖励🌱数量:{OO00OOO0O00OO0OO0}t粒')#line:776
        except Exception as O0OOOO00000O0OOOO :#line:777
            print (O0OOOO00000O0OOOO )#line:778
    def user_ad (OO00OOOOO000000O0 ):#line:781
        try :#line:782
            O0OOOOOO0OOO0OO00 =f'__{timi_new()}'#line:783
            OO00OOO000OO0OO00 ={'source':'scsc','authorization':OO00OOOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0OOO0OO00 ),'signstring':O0OOOOOO0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O00OOO0OO00OOO0OO =requests .request ('get',f'{host}/user/ad',headers =OO00OOO000OO0OO00 ).json ()#line:795
            if 'status'in O00OOO0OO00OOO0OO :#line:797
                if O00OOO0OO00OOO0OO ['status']==200 :#line:798
                    OOOOO00O0O0000OOO =O00OOO0OO00OOO0OO ['data']['max_time']#line:799
                    O0000OOOO00OOO0OO =O00OOO0OO00OOO0OO ['data']['watch_time']#line:800
                    O00O00O00OO00O000 =O00OOO0OO00OOO0OO ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O00O00O00OO00O000 + OOOOO00O0O0000OOO - O0000OOOO00OOO0OO}次丨好友提供:{O00O00O00OO00O000}次')#line:802
                    if O00O00O00OO00O000 +OOOOO00O0O0000OOO -O0000OOOO00OOO0OO >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        O00OO00OO0O0O0O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OOO000OO0OO00 ).json ()#line:805
                        if 'status'in O00OO00OO0O0O0O00 :#line:807
                            if O00OO00OO0O0O0O00 ['status']==200 :#line:808
                                O000OOOO0OO0O0000 =float (O00OO00OO0O0O0O00 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(O000OOOO0OO0O0000)}t粒')#line:810
                                return True #line:811
                            if O00OO00OO0O0O0O00 ['status']==500 :#line:812
                                OOO0O0O00000000O0 =O00OO00OO0O0O0O00 ['message']#line:813
                                print (f'【获取种子】:{OOO0O0O00000000O0}')#line:814
                                return False #line:815
        except Exception as O00O0O0OO0O000000 :#line:816
            print (O00O0O0OO0O000000 )#line:817
    def synthetic (OOOOOOOO00OOOO0O0 ):#line:820
        global id ,g #line:821
        try :#line:822
            OO0000O00O0OO0OOO =OOOOOOOO00OOOO0O0 .level_new ()#line:823
            O000O00O00OOO00OO =random .randint (9 ,11 )#line:824
            O0OOOO0O00O0O00O0 =f'_site=8&targetSite={O000O00O00OOO00OO}_{timi_new()}'#line:825
            OO00O0OO000O000OO ={'source':'scsc','authorization':OOOOOOOO00OOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O00O0O00O0 ),'signstring':O0OOOO0O00O0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OO0O0OO0OOOOOO00O ={"site":int (8 ),"targetSite":int (O000O00O00OOO00OO )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OO000O000OO ,json =OO0O0OO0OOOOOO00O )#line:838
            while True :#line:839
                OO00O00OOOOO00OOO =f'__{timi_new()}'#line:840
                OOO00000O00OO0O0O ={'source':'scsc','authorization':OOOOOOOO00OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOO00OOO ),'signstring':OO00O00OOOOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O00OOOOOOO00O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000O00OO0O0O ).json ()#line:852
                if 'status'in O00OOOOOOO00O0000 :#line:854
                    if O00OOOOOOO00O0000 ['status']==200 :#line:855
                        OO0000OOO00O0O0O0 =O00OOOOOOO00O0000 ['data']['cropList']#line:856
                        O00O0O0O00O0OOO00 =O00OOOOOOO00O0000 ['data']['gameCoreDataDBid']#line:857
                        OOO00O0O00000OO0O =float (O00OOOOOOO00O0000 ['data']['silver'])/1000000000000 #line:858
                        OOOO000O0O00O0OO0 =0 #line:863
                        for OO0O000OO0OO0O0OO in OO0000OOO00O0O0O0 :#line:864
                            if not OO0O000OO0OO0O0OO :#line:865
                                O00O00OOOOO00OOOO =f'_crop_id={O00O0O0O00O0OOO00}&site={OOOO000O0O00O0OO0}_{OOOOOOOO00OOOO0O0.time}'#line:866
                                OOOO00OO00000OO00 ={'source':'scsc','authorization':OOOOOOOO00OOOO0O0 .token ,'timestamp':OOOOOOOO00OOOO0O0 .time ,'sign':sign (O00O00OOOOO00OOOO ),'signstring':O00O00OOOOO00OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                OO0O00O00OOOOOO0O ={"site":OOOO000O0O00O0OO0 ,"crop_id":O00O0O0O00O0OOO00 }#line:877
                                OO00OOO0000OOO000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO00OO00000OO00 ,data =OO0O00O00OOOOOO0O ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OO00OOO0000OOO000 :#line:881
                                    if OO00OOO0000OOO000 ['status']==200 :#line:882
                                        if OO00OOO0000OOO000 ['message']=='种子数量不足':#line:883
                                            OO0000O00O0OO0OOO =OOOOOOOO00OOOO0O0 .level_new ()#line:884
                                            print (f'【种植合成】:{OO00OOO0000OOO000["message"]}')#line:885
                                            if not OOOOOOOO00OOOO0O0 .user_ad ():#line:886
                                                return False #line:887
                                    if OO00OOO0000OOO000 ['status']==500 :#line:888
                                        print (f'【种植合成】:{OO00OOO0000OOO000["message"]}')#line:889
                                        return False #line:890
                            OOOO000O0O00O0OO0 +=1 #line:891
                        OO00OO0O0OOOOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000O00OO0O0O ).json ()#line:892
                        O0O0OO00OO0OOO0O0 =OO00OO0O0OOOOO00O ['data']['cropList']#line:893
                        OO0O0OO00OO00O0O0 =False #line:894
                        for OO0O000OO0OO0O0OO in range (12 ):#line:895
                            id =O0O0OO00OO0OOO0O0 [OO0O000OO0OO0O0OO ]['level']#line:896
                            if float (OO0000O00O0OO0OOO )-float (id )>9 :#line:897
                                O00O0OO0000O0O000 =f'_site={OO0O000OO0OO0O0OO}_{timi_new()}'#line:898
                                OOOOO0OO0O0OOO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOOOO00OOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (O00O0OO0000O0O000 ),'signstring':O00O0OO0000O0O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O0OOOOO0OO000O0O0 ={"site":OO0O000OO0OO0O0OO }#line:910
                                OOO0O000OOO00000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOO0OO0O0OOO0OO ,data =O0OOOOO0OO000O0O0 ).json ()#line:912
                                if 'status'in OOO0O000OOO00000O :#line:913
                                    if OOO0O000OOO00000O ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OO0OO0O00O0OO00OO in range (11 ):#line:917
                                    OO0OOOOOOOO00O0OO =OO0OO0O00O0OO00OO +1 #line:918
                                    g =O0O0OO00OO0OOO0O0 [OO0OOOOOOOO00O0OO ]['level']#line:919
                                    if id ==g :#line:920
                                        OOOOOOO0OOO000000 =OO0OO0O00O0OO00OO +2 #line:921
                                        if OOOOOOO0OOO000000 !=OO0O000OO0OO0O0OO +1 :#line:922
                                            OO0OO0O0O000OO0OO =OO0O000OO0OO0O0OO +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O0OOOO0O00O0O00O0 =f'_site={OO0OO0O0O000OO0OO - 1}&targetSite={OOOOOOO0OOO000000 - 1}_{timi_new()}'#line:926
                                            OO00O0OO000O000OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOOOOOO00OOOO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O00O0O00O0 ),'signstring':O0OOOO0O00O0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            OO00OO00OOO000O00 ={"site":int (OO0OO0O0O000OO0OO -1 ),"targetSite":int (OOOOOOO0OOO000000 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OO000O000OO ,json =OO00OO00OOO000O00 )#line:945
                                            OO0O0OO00OO00O0O0 =True #line:947
                                    if OO0O0OO00OO00O0O0 :#line:948
                                        break #line:949
                                if OO0O0OO00OO00O0O0 :#line:950
                                    break #line:951
        except :#line:952
            OOOOOOOO00OOOO0O0 .synthetic ()#line:953
    def level_new (OO000OO0OOO0O0OO0 ):#line:956
        try :#line:957
            OOO0O000O000O0O00 =f'__{timi_new()}'#line:958
            O000O0O0O0O00OOO0 ={'source':'scsc','authorization':OO000OO0OOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O000O0O00 ),'signstring':OOO0O000O000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O00OO00O00OO00O0O =requests .request ('get',f'{host}/user',headers =O000O0O0O0O00OOO0 ).json ()#line:970
            if 'status'in O00OO00O00OO00O0O :#line:971
                if O00OO00O00OO00O0O ['status']==200 :#line:972
                    return float (O00OO00O00OO00O0O ['data']['level'])#line:973
        except Exception as OO0000O0O0O0OOOOO :#line:974
            print (OO0000O0O0O0OOOOO )#line:975
    def propsraffle (OO0OOO0OO0OOOOOOO ):#line:978
        try :#line:979
            while True :#line:980
                O0O0O0O0000O0O00O =f'__{timi_new()}'#line:981
                O00000OOOO0O0OOOO ={'source':'scsc','authorization':OO0OOO0OO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0000O0O00O ),'signstring':O0O0O0O0000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OO0OOO00OOOOOOOOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00000OOOO0O0OOOO ).json ()#line:993
                if 'status'in OO0OOO00OOOOOOOOO :#line:995
                    if OO0OOO00OOOOOOOOO ['status']==200 :#line:996
                        O0OO0OO0O0OOOO0O0 =OO0OOO00OOOOOOOOO ['data']['rows']#line:997
                        O0O00000O0000O00O =OO0OOO00OOOOOOOOO ['data']['vstate']#line:998
                        if O0OO0OO0O0OOOO0O0 ==5 or O0OO0OO0O0OOOO0O0 ==6 or O0OO0OO0O0OOOO0O0 ==7 :#line:999
                            O00O0000O0OO0O0O0 =OO0OOO00OOOOOOOOO ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O00O0000O0OO0O0O0}')#line:1001
                        if O0OO0OO0O0OOOO0O0 ==1 or O0OO0OO0O0OOOO0O0 ==2 or O0OO0OO0O0OOOO0O0 ==3 :#line:1002
                            OOOOOOOO000O00O00 =OO0OOO00OOOOOOOOO ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{OOOOOOOO000O00O00}')#line:1004
                        if O0OO0OO0O0OOOO0O0 ==4 or O0OO0OO0O0OOOO0O0 ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if O0OO0OO0O0OOOO0O0 =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OOOOOO0O000OOOOOO :#line:1046
            print (OOOOOO0O000OOOOOO )#line:1047
    def friends_invitation (O00OOOO0OO0O000OO ):#line:1050
        try :#line:1051
            OO000OOO000OOO0O0 =f'__{timi_new()}'#line:1052
            O00OO000OOOO00O0O ={'source':'scsc','authorization':O00OOOO0OO0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO000OOO0O0 ),'signstring':OO000OOO000OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O0OOOOOOO0000O0O0 =requests .request ('get',f'{host}/friends',headers =O00OO000OOOO00O0O ).json ()#line:1064
            if 'status'in O0OOOOOOO0000O0O0 :#line:1065
                if O0OOOOOOO0000O0O0 ['status']==200 :#line:1066
                    OO00O0O0O00OOO000 =O0OOOOOOO0000O0O0 ['data']['myInviteter']#line:1067
                    if OO00O0O0O00OOO000 :#line:1068
                        OO0O0OOO0OOO0OO0O =OO00O0O0O00OOO000 ['user']['nickname']#line:1069
                        O0000O00O0OO0O0O0 =O00OOOO0OO0O000OO .certification ()#line:1070
                        if O0000O00O0OO0O0O0 =='未实名':#line:1071
                            weishim .append (O00OOOO0OO0O000OO .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{OO0O0OOO0OOO0OO0O}丨实名:{O0000O00O0OO0O0O0}')#line:1073
        except Exception as OO0OO0O0OO000OOO0 :#line:1077
            print (OO0OO0O0OO000OOO0 )#line:1078
    def add_clover (O00O0OOOO0O00OO0O ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            OO000OO0OOOO0OO0O =f'__{timi_new()}'#line:1084
            O000O0O00OOO00O00 ={'source':'scsc','authorization':O00O0OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OOOO0OO0O ),'signstring':OO000OO0OOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO0OO0O0O00O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O00OOO00O00 ).json ()#line:1096
            if 'status'in OO0OO0O0O00O0O0O0 :#line:1098
                if OO0OO0O0O00O0O0O0 ['status']==200 :#line:1099
                    OO0O000O000OOO00O =OO0OO0O0O00O0O0O0 ['data']['clover']#line:1100
                    OOO0O0O000OO000OO =OO0OO0O0O00O0O0O0 ['data']['used_clover']#line:1101
                    O0OO0O00O0O0O0O00 =float (OO0O000O000OOO00O )-float (OOO0O0O000OO000OO )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O0O000OO000OO}')#line:1103
                    if O00O0OOOO0O00OO0O .certification ()!='未实名':#line:1104
                        if O0OO0O00O0O0O0O00 >1 :#line:1105
                            OO000OO0OOOO0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO0O00O0O0O0O00)}_{timi_new()}'#line:1106
                            OO0OOO0OO0O0OOO0O ={'source':'scsc','authorization':O00O0OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OOOO0OO0O ),'signstring':OO000OO0OOOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OO000O0000O000O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO0O00O0O0O0O00 )}#line:1118
                            O000000OOOOO00OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0OO0O0OOO0O ,data =OO000O0000O000O0O ).json ()#line:1119
                            if 'status'in O000000OOOOO00OOO :#line:1121
                                if O000000OOOOO00OOO ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O000000OOOOO00OOO["data"]["isSuccess"]}丨数量:{O0OO0O00O0O0O0O00}')#line:1123
                                if O000000OOOOO00OOO ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O000000OOOOO00OOO["message"]}')#line:1125
            OOO0O0OO0O0OOO000 =requests .request ('get',f'{host}/lottery',headers =O000O0O00OOO00O00 ).json ()#line:1126
            O0OO0O0OOOO00O0O0 =O00O0OOOO0O00OO0O .winning_rewards ()#line:1128
            if 'status'in OOO0O0OO0O0OOO000 :#line:1129
                if OOO0O0OO0O0OOO000 ['status']==200 :#line:1130
                    OOO00OO0000000000 =OOO0O0OO0O0OOO000 ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OOO00OO0000000000 )#line:1132
                    O0O00OO000O00000O =OOO0O0OO0O0OOO000 ['data'][1 ]['value']#line:1133
                    O0OOO0000O000OO0O =OOO0O0OO0O0OOO000 ['data'][0 ]['join_number']#line:1134
                    O00000000O0O0OO0O =int (float (OOO0O0OO0O0OOO000 ['data'][0 ]['totalValue']))#line:1135
                    OO00OOOO0000OO0O0 =float (O0O00OO000O00000O /O00000000O0O0OO0O )*10000 #line:1136
                    O0O0OOOO00O0O000O =O00000000O0O0OO0O /O0OOO0000O000OO0O #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OOO00OO0000000000)[:6]}颗金种子丨好友收益:{str(O0OO0O0OOOO00O0O0)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OO00OOOO0000OO0O0)[:6]}颗金种子丨☘️人均:{str(O0O0OOOO00O0O000O)[:7]}️')#line:1139
        except Exception as OOOO0OOO00OOOOOOO :#line:1140
            print (OOOO0OOO00OOOOOOO )#line:1141
    def energy (OO00O00O00OO0O00O ):#line:1144
        try :#line:1145
            while True :#line:1146
                OOO00O0O0OO0000O0 =f'__{timi_new()}'#line:1147
                OO0OOO0OOOO0000O0 ={'source':'scsc','authorization':OO00O00O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O0OO0000O0 ),'signstring':OOO00O0O0OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                O000O0OO0OO00O0OO =requests .request ('get',f'{host}/energy/general',headers =OO0OOO0OOOO0000O0 ).json ()#line:1159
                if 'status'in O000O0OO0OO00O0OO :#line:1161
                    if O000O0OO0OO00O0OO ['status']==200 :#line:1162
                        O00000OO00OO0O000 =O000O0OO0OO00O0OO ['data']['ordinary_water']#line:1163
                        O0O0OO0OOOO0OO000 =O000O0OO0OO00O0OO ['data']['ordinary_fertilizer']#line:1164
                        OOO0OOOOO0O000OO0 =O000O0OO0OO00O0OO ['data']['videoStatus']#line:1165
                        OOO0OO00O00OO0O00 =O000O0OO0OO00O0OO ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0O0OO0OOOO0OO000).split(".")[0]}丨水滴:{str(O00000OO00OO0O000).split(".")[0]}')#line:1168
                        if float (O0O0OO0OOOO0OO000 )<96 :#line:1169
                            if OOO0OOOOO0O000OO0 :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OO0O000OOOO00O0O0 =99 -float (O0O0OO0OOOO0OO000 )#line:1172
                                O0O0O0OO0O0OO0O00 ={"fertilizer":str (OO0O000OOOO00O0O0 ).split ('.')[0 ]}#line:1173
                                O0O0O00OO0OO0O00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOO0OOOO0000O0 ).json ()#line:1175
                                if 'status'in O0O0O00OO0OO0O00O :#line:1177
                                    if O0O0O00OO0OO0O00O ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0O00OO0OO0O00O["message"]}')#line:1179
                                    if O0O0O00OO0OO0O00O ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0O00OO0OO0O00O["message"]}')#line:1181
                                        break #line:1182
                                if float (O0O0OO0OOOO0OO000 )<78 :#line:1184
                                    OO0O000OOOO00O0O0 =80 -float (O0O0OO0OOOO0OO000 )#line:1185
                                    OOO0OOOO0O0O0O00O =f'_fertilizer={int(OO0O000OOOO00O0O0)}_{timi_new()}'#line:1186
                                    OO0O0O0OOOOOOO000 ={'source':'scsc','authorization':OO00O00O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0O0O0O00O ),'signstring':OOO0OOOO0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    OOO0O0OO00OOOOO00 ={"fertilizer":int (OO0O000OOOO00O0O0 )}#line:1198
                                    OOO0OOO0OOOOO0OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O0O0OOOOOOO000 ,data =OOO0O0OO00OOOOO00 ).json ()#line:1200
                                    if 'status'in OOO0OOO0OOOOO0OO0 :#line:1202
                                        if OOO0OOO0OOOOO0OO0 ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OOO0OOO0OOOOO0OO0["message"]}丨数量:{int(OO0O000OOOO00O0O0)}')#line:1204
                                        if OOO0OOO0OOOOO0OO0 ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OOO0OOO0OOOOO0OO0["message"]}丨数量:{int(OO0O000OOOO00O0O0)}')#line:1206
                                            O0OO000OO0OO00OOO =OOO0OOO0OOOOO0OO0 ["message"].split ('-')[1 ]#line:1207
                                            O0OOOO00OO0O00OOO =f'__{timi_new()}'#line:1208
                                            OO0000OOOO0OO0000 ={'source':'scsc','authorization':OO00O00O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OO0O00OOO ),'signstring':O0OOOO00OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OO0000OO00O0O0000 =requests .request ('get',f'{host}/user',headers =OO0000OOOO0OO0000 ).json ()#line:1220
                                            if 'status'in OO0000OO00O0O0000 :#line:1221
                                                if OO0000OO00O0O0000 ['status']==200 :#line:1222
                                                    O0000O000O0O00000 =OO0000OO00O0O0000 ['data']['inner_id']#line:1223
                                                    if give_gold (O0000O000O0O00000 ,float (O0OO000OO0OO00OOO )+1 ):#line:1224
                                                        OO00O00O00OO0O00O .energy ()#line:1225
                        if float (O00000OO00OO0O000 )<880 :#line:1226
                            if OOO0OO00O00OO0O00 :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                OO0O00OO00O00O0OO =999 -float (O00000OO00OO0O000 )#line:1229
                                OOOO0OOO00O0OOOO0 ={"water":str (OO0O00OO00O00O0OO ).split ('.')[0 ]}#line:1230
                                O00O000OO00OO0000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOO0OOOO0000O0 ).json ()#line:1232
                                if 'status'in O00O000OO00OO0000 :#line:1234
                                    if O00O000OO00OO0000 ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{O00O000OO00OO0000["message"]}')#line:1236
                                    if O00O000OO00OO0000 ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{O00O000OO00OO0000["message"]}')#line:1238
                                        break #line:1239
                                if float (O00000OO00OO0O000 )<780 :#line:1240
                                    OO0O00OO00O00O0OO =800 -float (O00000OO00OO0O000 )#line:1241
                                    OOOO0OO0000OOO00O =f'_water={int(OO0O00OO00O00O0OO)}_{timi_new()}'#line:1242
                                    OO0000000000O00O0 ={'source':'scsc','authorization':OO00O00O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0000OOO00O ),'signstring':OOOO0OO0000OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O00O0OOOOO0O00O00 ={"water":int (OO0O00OO00O00O0OO )}#line:1254
                                    O000OO0O00O0000O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0000000000O00O0 ,data =O00O0OOOOO0O00O00 ).json ()#line:1256
                                    if 'status'in O000OO0O00O0000O0 :#line:1258
                                        if O000OO0O00O0000O0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O000OO0O00O0000O0["message"]}丨数量:{int(OO0O00OO00O00O0OO)}')#line:1260
                                        if O000OO0O00O0000O0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O000OO0O00O0000O0["message"]}丨数量:{int(OO0O00OO00O00O0OO)}')#line:1262
                                            O0OO000OO0OO00OOO =O000OO0O00O0000O0 ["message"].split ('-')[1 ]#line:1263
                                            O0OOOO00OO0O00OOO =f'__{timi_new()}'#line:1264
                                            OO0000OOOO0OO0000 ={'source':'scsc','authorization':OO00O00O00OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OO0O00OOO ),'signstring':O0OOOO00OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OO0000OO00O0O0000 =requests .request ('get',f'{host}/user',headers =OO0000OOOO0OO0000 ).json ()#line:1276
                                            if 'status'in OO0000OO00O0O0000 :#line:1277
                                                if OO0000OO00O0O0000 ['status']==200 :#line:1278
                                                    O0000O000O0O00000 =OO0000OO00O0O0000 ['data']['inner_id']#line:1279
                                                    if give_gold (O0000O000O0O00000 ,float (O0OO000OO0OO00OOO )+1 ):#line:1280
                                                        OO00O00O00OO0O00O .energy ()#line:1281
                        break #line:1282
        except Exception as OO0O0OOO000OO0O00 :#line:1283
            print (OO0O0OOO000OO0O00 )#line:1284
def bundled_def ():#line:1287
    O000OOOO0O0O0OOO0 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return O000OOOO0O0O0OOO0 [random .randint (0 ,len (O000OOOO0O0O0OOO0 )-1 )]#line:1289
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
        O00000000OO0000O0 =gitee_edition ()#line:1328
        if version_of_the_validation ()<O00000000OO0000O0 ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00000000OO0000O0["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O00000000OO0000O0["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00000000OO0000O0["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O00000000OO0000O0["CityEarth"]["content"]}')#line:1334
    except Exception as OOO0OOO00O0000000 :#line:1335
        print (OOO0OOO00O0000000 )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
