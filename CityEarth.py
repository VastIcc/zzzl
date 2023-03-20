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
        O0OOOOOOOO00O00OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OOOOOOOO00O00OO)}个账号==========")#line:17
        for O0O0O0OO0OO000000 in O0OOOOOOOO00O00OO :#line:18
            O0O0OO0000OOO0000 =[]#line:19
            print (f"------------正在执行第{O0OOOOOOOO00O00OO.index(O0O0O0OO0OO000000) + 1}个账号------------")#line:20
            OO000OOOO0000O00O =CityEarth (O0O0O0OO0OO000000 ,O0O0OO0000OOO0000 ,O0OOOOOOOO00O00OO .index (O0O0O0OO0OO000000 ))#line:21
            def OOO00OOO0OO00OO0O ():#line:23
                if OO000OOOO0000O00O .base_info ():#line:25
                    OO000OOOO0000O00O .sealing ()#line:27
                    OO000OOOO0000O00O .invitenum ()#line:29
                    OO000OOOO0000O00O .query_to_sell ()#line:31
                    OO000OOOO0000O00O .friends_invitation ()#line:35
                    OO000OOOO0000O00O .energy ()#line:37
                    OO000OOOO0000O00O .add_clover ()#line:39
                    OO000OOOO0000O00O .propsraffle ()#line:41
                    OO000OOOO0000O00O .synthetic ()#line:43
                    OO000OOOO0000O00O .crops_illustrated ()#line:45
                    OO000OOOO0000O00O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO000OOOO0000O00O .give_gold ()#line:50
            O0000O0OO00O00OO0 =threading .Thread (target =OOO00OOO0OO00OO0O )#line:52
            O0000O0OO00O00OO0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0OO0O000OO0OO00O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OO0O000OO0OO00O +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O000OOO0000000000 in invited_new :#line:62
            print (O000OOO0000000000 )#line:63
        print ('开始打印未实名的token')#line:64
        for OOOO0O00O0O0O00OO in weishim :#line:65
            print (OOOO0O00O0O0O00OO )#line:66
    except Exception as O0OOOOO00O00000O0 :#line:67
        print (O0OOOOO00O00000O0 )#line:68
def give_gold (O0OO0OO000OO0OOOO ,OO0OO0OO000OOO000 ):#line:72
    try :#line:73
        O0000OOOOOOO0O0O0 =f'_doneeNo={O0OO0OO000OO0OOOO}&quantity={int(OO0OO0OO000OOO000)}_{timi_new()}'#line:74
        OOO00OOOOOO0OO0O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000OOOOOOO0O0O0 ),'signstring':O0000OOOOOOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO0OO000O00O0O00O ={"quantity":int (OO0OO0OO000OOO000 ),"doneeNo":O0OO0OO000OO0OOOO }#line:89
        OO0OO000OO000OOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OOOOOO0OO0O0 ,data =OO0OO000O00O0O00O ).json ()#line:90
        if 'status'in OO0OO000OO000OOO0 :#line:92
            if OO0OO000OO000OOO0 ['status']==200 :#line:93
                if OO0OO000OO000OOO0 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OO0OO0OO000OOO000)}种子给{O0OO0OO000OO0OOOO}成功')#line:95
                    return True #line:96
            if OO0OO000OO000OOO0 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0OO000OO000OOO0["message"]}')#line:98
                return False #line:99
            if OO0OO000OO000OOO0 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0OO000OO000OOO0["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00O0OO0O00OOOOOO :#line:104
        print (O00O0OO0O00OOOOOO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OOO000OOO000OOOO0 ):#line:115
    O0O0O0OO000O0O0O0 =hashlib .md5 (OOO000OOO000OOOO0 .encode ()).hexdigest ()#line:116
    OOOOO0O0OO00000O0 =sc1 ()#line:117
    O0O00O0000O000O00 =sc2 ()#line:118
    OOOO0O0OOO0O0OOO0 =sc3 ()#line:119
    OOOOO00000O0O00OO =OOOOO0O0OO00000O0 +O0O0O0OO000O0O0O0 +O0O00O0000O000O00 +OOOO0O0OOO0O0OOO0 #line:120
    OOO0OOO00O0O000O0 =hashlib .md5 (OOOOO00000O0O00OO .encode ()).hexdigest ()#line:121
    return OOO0OOO00O0O000O0 #line:122
def format_msg ():#line:125
    O0O0OOO000O000OOO =""#line:126
    for OO000O0O0O0O0O00O in msg_list :#line:127
        O0O0OOO000O000OOO +=str (OO000O0O0O0O0O00O )+"\r\n"#line:128
    return O0O0OOO000O000OOO #line:129
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
def get_json_data (O0OO000OOO00OO00O ,OO0000O0OO000OOOO ,OO0OO0O0OO00O0OOO ,O00O000OO0OOOO000 ):#line:153
    with open (O0OO000OOO00OO00O ,'rb')as OO0OOOOO000O00O00 :#line:154
        OO00O0O00O0OOOO00 =json .load (OO0OOOOO000O00O00 )#line:155
        OO00O0O00O0OOOO00 ['data'][OO0000O0OO000OOOO ][OO0OO0O0OO00O0OOO ]=O00O000OO0OOOO000 #line:156
        O0OO0OO0OO00OOOO0 =OO00O0O00O0OOOO00 #line:157
    OO0OOOOO000O00O00 .close ()#line:158
    return O0OO0OO0OO00OOOO0 #line:159
def write_json_data (OOO0OOOOOOO0OO0O0 ):#line:162
    with open (json_path1 ,'w')as OOOOO000O00O0OOOO :#line:163
        json .dump (OOO0OOOOOOO0OO0O0 ,OOOOO000O00O0OOOO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OOOOO000O00O0OOOO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO0O0000OO00OOOO0 ,O0O0O0O000O00O0O0 ,OOOOOO0OO0O0O0000 ,OOO00OO0O0O0O00O0 ):#line:171
        try :#line:172
            OO0O0000OO00OOOO0 .msg =OOOOOO0OO0O0O0000 #line:173
            OO0O0000OO00OOOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO0O0000OO00OOOO0 .token =O0O0O0O000O00O0O0 ['authorization']#line:175
            OO0O0000OO00OOOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO0O0000OO00OOOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO0O0000OO00OOOO0 .elephant_user =O0O0O0O000O00O0O0 ['elephant_user']#line:178
            OO0O0000OO00OOOO0 .elephant_pswd =O0O0O0O000O00O0O0 ['elephant_pswd']#line:179
            OO0O0000OO00OOOO0 .elephant_Task_ID =O0O0O0O000O00O0O0 ['elephant_Task_ID']#line:180
            OO0O0000OO00OOOO0 .len_new =OOO00OO0O0O0O00O0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O000O000O00O0OO ):#line:186
        try :#line:187
            O0O000O000O00O0OO .watched_ad ()#line:189
            O0O00OO00OO0OOOO0 =f'__{timi_new()}'#line:190
            O00OOO00OO00O00OO ={'source':'scsc','authorization':O0O000O000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OO0OOOO0 ),'signstring':O0O00OO00OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOOO00O00O0OO0O0 =requests .request ('get',f'{host}/user',headers =O00OOO00OO00O00OO ).json ()#line:202
            if 'status'in OOOOO00O00O0OO0O0 :#line:204
                if OOOOO00O00O0OO0O0 ['status']==200 :#line:205
                    O0OOO0O0OO0O0OOOO =OOOOO00O00O0OO0O0 ['data']['nickname']#line:206
                    O000OOO0OOO000O0O =OOOOO00O00O0OO0O0 ['data']['inner_id']#line:207
                    O0000000OO00OO000 =OOOOO00O00O0OO0O0 ['data']['assets']['gold']#line:208
                    O0O0O0O000OOO0000 =OOOOO00O00O0OO0O0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0OOO0O0OO0O0OOOO[:5]}丨ID:{O000OOO0OOO000O0O}丨等级:{O0O0O0O000OOO0000}丨金种子:{str(O0000000OO00OO000).split(".")[0]}')#line:211
                    if 'wx_'in O0OOO0O0OO0O0OOOO :#line:212
                        O0O000O000O00O0OO .change_nickname ()#line:213
                if OOOOO00O00O0OO0O0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O000O000O00O0OO .elephant_user =='f':#line:216
                        return False #line:217
                    OO000OO00O000000O =Invalid_login .addtask (elephant_user =O0O000O000O00O0OO .elephant_user ,elephant_pswd =O0O000O000O00O0OO .elephant_pswd ,elephant_Task_ID =O0O000O000O00O0OO .elephant_Task_ID )#line:220
                    O0O0O0OO0O0OO0O0O =get_json_data (json_path ,O0O000O000O00O0OO .len_new ,'authorization',OO000OO00O000000O )#line:221
                    if write_json_data (O0O0O0OO0O0OO0O0O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOOO00O00O0OO0O0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO000O0000OOOOO0O :#line:228
            print (OO000O0000OOOOO0O )#line:229
    def sealing (OOOO0O0OO00O0OOOO ):#line:232
        try :#line:233
            OO0OO0O0OO000O000 =f'__{timi_new()}'#line:234
            O0OOO0O0OOO00O0OO ={'source':'scsc','authorization':OOOO0O0OO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO000O000 ),'signstring':OO0OO0O0OO000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0O0OOO00O0OO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0O0OOO00O0OO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0O0OOO00O0OO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0O0OOO00O0OO )#line:249
            requests .request ('get',f'{host}/user',headers =O0OOO0O0OOO00O0OO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0O0OOO00O0OO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0O0OOO00O0OO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0O0OOO00O0OO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0O0OOO00O0OO )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OOO0O0OOO00O0OO )#line:255
        except Exception as O0O0O00O00OOO0000 :#line:256
            print (O0O0O00O00OOO0000 )#line:257
    def ddd (O0OOOO0O00O0OOO00 ):#line:259
        try :#line:260
            O00000OO000OOO0OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00OOOO0O0O00O0OO ={'source':'scsc','authorization':O0OOOO0O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO000OOO0OO ),'signstring':O00000OO000OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0O00OO0000O00OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00OOOO0O0O00O0OO ).json ()#line:273
            print (OO0O00OO0000O00OO )#line:274
        except Exception as OOO0000O0OOO0OOO0 :#line:277
            print (OOO0000O0OOO0OOO0 )#line:278
    def the_query (OO00OOO000000OO00 ):#line:283
        try :#line:284
            O0OOOO00OO0O0OO00 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO0O0O0O00O0OOO00 ={'authorization':OO00OOO000000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OO0O0OO00 ),'signstring':O0OOOO00OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO000OO0O00O0OOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0O0O0O00O0OOO00 ).json ()#line:296
            if 'status'in OO000OO0O00O0OOO0 :#line:298
                if OO000OO0O00O0OOO0 ['status']==200 :#line:299
                    return OO000OO0O00O0OOO0 ['data']['rows'][4 ]['price']#line:300
        except Exception as OO0O0O0OO0OO00O0O :#line:301
            print (OO0O0O0OO0OO00O0O )#line:302
    def market_sale (OO0000O0O00OO0000 ,OO0O0000OOOOO00OO ):#line:305
        try :#line:306
            O00OOO0O0OOO000O0 =timi_new ()#line:307
            O000O0OOO0O000OO0 =f'type=crop__{O00OOO0O0OOO000O0}'#line:308
            OO00000OOOOO00O00 ={'source':'scsc','authorization':OO0000O0O00OO0000 .token ,'timestamp':str (O00OOO0O0OOO000O0 ),'sign':sign (O000O0OOO0O000OO0 ),'signstring':O000O0OOO0O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            OO0000O0O0000OOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00000OOOOO00O00 ).json ()#line:320
            if 'status'in OO0000O0O0000OOO0 :#line:322
                if OO0000O0O0000OOO0 ['status']==200 :#line:323
                    if OO0000O0O0000OOO0 ['data']['rows']:#line:324
                        OOO0O000O0O0O0OO0 =OO0000O0O0000OOO0 ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOOO0000OOO0O0000 =OO0000O0O0000OOO0 ['data']['rows'][0 ]['quantity']#line:326
                        if float (OO0O0000OOOOO00OO )>6 :#line:327
                            O00O0OO0O0O000OO0 =f'_packsackItemId={OOO0O000O0O0O0OO0}&price={str(OO0O0000OOOOO00OO)[:5]}&quantity={OOOO0000OOO0O0000}_{O00OOO0O0OOO000O0}'#line:328
                            OO0OO0OO0OO00O00O ={'source':'scsc','authorization':OO0000O0O00OO0000 .token ,'timestamp':str (O00OOO0O0OOO000O0 ),'sign':sign (O00O0OO0O0O000OO0 ),'signstring':O00O0OO0O0O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            O000O00OOOO0OOO00 ={"packsackItemId":OOO0O000O0O0O0OO0 ,"price":str (OO0O0000OOOOO00OO )[:5 ],"quantity":str (OOOO0000OOO0O0000 )}#line:344
                            OO0O000OO00O000OO =requests .request ('post',f'{host}/market/sale',headers =OO0OO0OO0OO00O00O ,data =O000O00OOOO0OOO00 ).json ()#line:345
                            if 'status'in OO0O000OO00O000OO :#line:347
                                if OO0O000OO00O000OO ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OOOO0000OOO0O0000}丨价格:{str(OO0O0000OOOOO00OO)[:5]}')#line:349
                                if OO0O000OO00O000OO ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{OO0O000OO00O000OO["message"]}')#line:351
        except Exception as OOOOOOOO000O000OO :#line:352
            print (OOOOOOOO000O000OO )#line:353
    def query_to_sell (O0O0OOO000OOO00O0 ):#line:356
        global count_list #line:357
        try :#line:358
            OO00OOOOO0OOOOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            O00OOO00O00OOOO0O ={'source':'scsc','authorization':O0O0OOO000OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOO0OOOOOOO ),'signstring':OO00OOOOO0OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O0O0O00OOOO0OO000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OOO00O00OOOO0O ).json ()#line:371
            if 'status'in O0O0O00OOOO0OO000 :#line:373
                if O0O0O00OOOO0OO000 ['status']==200 :#line:374
                    for O0OO0OO0O00OOOOO0 in O0O0O00OOOO0OO000 ['data']['rows']:#line:375
                        O000OOOO0OO0O0O0O =O0OO0OO0O00OOOOO0 ['materialKey']#line:376
                        O0O0O0O0O0OO00OOO =O0OO0OO0O00OOOOO0 ['quantity']#line:377
                        OOO0OO0OOOOOOOO00 =O0OO0OO0O00OOOOO0 ['price']#line:378
                        OOOOOOO00O0OOOOOO =O0OO0OO0O00OOOOO0 ['saleState']#line:379
                        if OOOOOOO00O0OOOOOO ==0 :#line:380
                            print (f'【出售订单】:名称:{O000OOOO0OO0O0O0O}丨数量:{O0O0O0O0O0OO00OOO}丨价格:{OOO0OO0OOOOOOOO00}')#line:381
                            count_list +=O0O0O0O0O0OO00OOO #line:382
                            O0OOOO000O00OO000 =O0O0OOO000OOO00O0 .the_query ()#line:384
                            if float (O0OOOO000O00OO000 )!=float (OOO0OO0OOOOOOOO00 ):#line:385
                                O0OO0000OO0O0O00O =O0OO0OO0O00OOOOO0 ['id']#line:386
                                O0O0OOO000OOO00O0 .cacel_sale (O0OO0000OO0O0O00O )#line:387
                    O0O0OOO000OOO00O0 .game_map ()#line:389
        except Exception as O0000000O00O0OOOO :#line:391
            print (O0000000O00O0OOOO )#line:392
    def cacel_sale (OO00000OOOO00OO00 ,O000O0O000O00OO00 ):#line:395
        try :#line:396
            O00OO000000000000 =f'_saleId={O000O0O000O00OO00}_{timi_new()}'#line:397
            O0O0O00O00OOO00O0 ={'source':'scsc','authorization':OO00000OOOO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000000000000 ),'signstring':O00OO000000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O00O0O0O0OO0O0000 ={"saleId":O000O0O000O00OO00 }#line:409
            O0O0OO0O00OO0OO00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0O00O00OOO00O0 ,data =O00O0O0O0OO0O0000 ).json ()#line:410
            if 'status'in O0O0OO0O00OO0OO00 :#line:412
                if O0O0OO0O00OO0OO00 ['status']==200 :#line:413
                    print (f'【下架出售】:{O0O0OO0O00OO0OO00["data"]}')#line:414
        except Exception as OOO00O000000OO00O :#line:415
            print (OOO00O000000OO00O )#line:416
    def change_nickname (O00O0OO0000OO0OOO ):#line:419
        try :#line:420
            O0O0000000O0OO0O0 =timi_new ()#line:421
            O000O0O00OO000O00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O0O0OO00O0000OO0O =requests .request ('post','https://www.qmsjmfb.com/',data =O000O0O00OO000O00 ).text #line:423
            O0O0OO0OO0000000O =re .findall ('<ul><li>(.*?)</li>',O0O0OO00O0000OO0O )[0 ][:3 ]#line:424
            O0O0000000O0O000O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0OO0OO0000000O}').json ()#line:425
            O0O00O0O0OOO0OO0O =O0O0000000O0O000O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            O0O0O0O0OOO0O0O0O ={"nickname":O0O00O0O0OOO0OO0O }#line:427
            O0O00O0000000O00O =f'_nickname={O0O00O0O0OOO0OO0O}_{O0O0000000O0OO0O0}'#line:428
            O00O000OOO0000O0O ={'source':'scsc','authorization':O00O0OO0000OO0OOO .token ,'timestamp':O0O0000000O0OO0O0 ,'sign':sign (O0O00O0000000O00O ),'signstring':O0O00O0000000O00O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OOO0000O0OO000000 =requests .request ('patch',f'{host}/user/nickname',headers =O00O000OOO0000O0O ,data =O0O0O0O0OOO0O0O0O ).json ()#line:440
            if 'status'in OOO0000O0OO000000 :#line:442
                if OOO0000O0OO000000 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O0O00O0O0OOO0OO0O}丨{OOO0000O0OO000000["message"]}')#line:444
        except Exception as OO0OO00O00OOO0OOO :#line:445
            print (OO0OO00O00OOO0OOO )#line:446
    def withdraw (OO0O00O0O000OOOO0 ):#line:449
        try :#line:450
            O0O0000O0OOO0OOO0 =f'__{timi_new()}'#line:451
            OO00O0OO0OOOO0000 ={'source':'scsc','authorization':OO0O00O0O000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0OOO0OOO0 ),'signstring':O0O0000O0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            O0O000OOOOO00OOOO =requests .request ('get',f'{host}/assets',headers =OO00O0OO0OOOO0000 ).json ()#line:463
            if 'status'in O0O000OOOOO00OOOO :#line:465
                if O0O000OOOOO00OOOO ['status']==200 :#line:466
                    O0OO000OOOO00O0OO =O0O000OOOOO00OOOO ['data']['cash']#line:467
                    if float (O0OO000OOOO00O0OO )>20 :#line:468
                        O0O0000O0OOO0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        OO00O0OO0OOOO0000 ={'authorization':OO0O00O0O000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0OOO0OOO0 ),'signstring':O0O0000O0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OO0O00OOOOO000OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        O0OOOO0O000O0000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO00O0OO0OOOO0000 ,data =OO0O00OOOOO000OOO ).json ()#line:482
                        if 'status'in O0OOOO0O000O0000O :#line:484
                            if O0OOOO0O000O0000O ['status']==200 :#line:485
                                print (f'【余额提现】:{O0OOOO0O000O0000O["data"]}')#line:486
                        if 'status'in O0OOOO0O000O0000O :#line:487
                            if O0OOOO0O000O0000O ['status']==500 :#line:488
                                print (f'【余额提现】:{O0OOOO0O000O0000O["message"]}')#line:489
        except Exception as OOO0O0OO0OOO0OO00 :#line:490
            print (OOO0O0OO0OOO0OO00 )#line:491
    def invitenum (O0OOOO0OO0O0O0O00 ):#line:494
        global invited_new #line:495
        try :#line:496
            OO0O0O00000O0O000 =f'__{timi_new()}'#line:497
            O0O00OO00000O0OO0 ={'source':'scsc','authorization':O0OOOO0OO0O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O00000O0O000 ),'signstring':OO0O0O00000O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OOO00OO0O0OO0000O =requests .request ('get',f'{host}/invite/invitenum',headers =O0O00OO00000O0OO0 ).json ()#line:509
            if 'status'in OOO00OO0O0OO0000O :#line:511
                if OOO00OO0O0OO0000O ['status']==200 :#line:512
                    OOO0O00O0000OOO00 =OOO00OO0O0OO0000O ['data']['invited_count']#line:513
                    O00O0O0O0OOO0OOOO =OOO00OO0O0OO0000O ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OOO0O00O0000OOO00}丨间邀好友:{O00O0O0O0OOO0OOOO}')#line:515
                    if OOO0O00O0000OOO00 <2 :#line:516
                        OOO0OO000O000OO0O =f'__{timi_new()}'#line:517
                        OO0O0O0O00OO00OO0 ={'source':'scsc','authorization':O0OOOO0OO0O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O000OO0O ),'signstring':OOO0OO000O000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OOOOOO00O00O0OO0O =requests .request ('get',f'{host}/user',headers =OO0O0O0O00OO00OO0 ).json ()#line:529
                        if 'status'in OOOOOO00O00O0OO0O :#line:531
                            if OOOOOO00O00O0OO0O ['status']==200 :#line:532
                                invited_new .append (OOOOOO00O00O0OO0O ['data']['inner_id'])#line:533
        except Exception as O000O00O000OOOO0O :#line:534
            print (O000O00O000OOOO0O )#line:535
    def game_map (O0O0O0OOO0OOOOO00 ):#line:538
        try :#line:539
            O00O00000OO0000OO =f'__{timi_new()}'#line:540
            O0OO000O0O0O00O00 ={'source':'scsc','authorization':O0O0O0OOO0OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OO0000OO ),'signstring':O00O00000OO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OOOO00O00O0O000OO =requests .request ('get',f'{host}/game/map',headers =O0OO000O0O0O00O00 ).json ()#line:552
            if 'status'in OOOO00O00O0O000OO :#line:554
                if OOOO00O00O0O000OO ['status']==200 :#line:555
                    for O0O000O0OOO0O0OO0 in OOOO00O00O0O000OO ['data']['list'][0 ]['crops']:#line:556
                        O0OOOO0O0OOO0O000 =O0O000O0OOO0O0OO0 ['level']#line:558
                        if O0OOOO0O0OOO0O000 ==41 :#line:559
                            O000OOOO0OOO0OO00 =O0O000O0OOO0O0OO0 ['crop_name']#line:560
                            OO00O0O0OOOO0000O =O0O000O0OOO0O0OO0 ['count']#line:561
                            if OO00O0O0OOOO0000O >0 :#line:562
                                print (f'【农业资产】:{O000OOOO0OOO0OO00}丨数量:{OO00O0O0OOOO0000O}')#line:563
                                OOOO0OOO0O00O00OO =O0O0O0OOO0OOOOO00 .the_query ()#line:564
                                O0O0O0OOO0OOOOO00 .market_sale (OOOO0OOO0O00O00OO )#line:565
        except Exception as O000OO0OOO0OO0O00 :#line:566
            print (O000OO0OOO0OO0O00 )#line:567
    def give_gold (O00O00OO00000OO0O ):#line:570
        try :#line:571
            OOO00OO0OOOO000O0 =f'__{timi_new()}'#line:572
            OO00000OO00O0O0O0 ={'source':'scsc','authorization':O00O00OO00000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOOO000O0 ),'signstring':OOO00OO0OOOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OO0O0O0OO0000OOOO =requests .request ('get',f'{host}/user',headers =OO00000OO00O0O0O0 ).json ()#line:584
            if 'status'in OO0O0O0OO0000OOOO :#line:585
                if OO0O0O0OO0000OOOO ['status']==200 :#line:586
                    if float (O00O00OO00000OO0O .doneeNo )!=0 :#line:587
                        O0O000OOOOO00O0O0 =OO0O0O0OO0000OOOO ['data']['assets']['gold']#line:588
                        if float (O0O000OOOOO00O0O0 )>float (O00O00OO00000OO0O .innerId ):#line:589
                            OO0OOOO00O0O00O0O =int (float (O0O000OOOOO00O0O0 )/1.1 )#line:590
                            OOO00OO0OOOO000O0 =f'_doneeNo={O00O00OO00000OO0O.doneeNo}&quantity={OO0OOOO00O0O00O0O}_{timi_new()}'#line:591
                            OO00000OO00O0O0O0 ={'source':'scsc','authorization':O00O00OO00000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOOO000O0 ),'signstring':OOO00OO0OOOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O0000O0000OOOOOOO ={"quantity":OO0OOOO00O0O00O0O ,"doneeNo":O00O00OO00000OO0O .doneeNo }#line:606
                            OOO0O0000OOO0O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00000OO00O0O0O0 ,data =O0000O0000OOOOOOO ).json ()#line:607
                            if 'status'in OOO0O0000OOO0O0OO :#line:609
                                if OOO0O0000OOO0O0OO ['status']==200 :#line:610
                                    if OOO0O0000OOO0O0OO ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OO0OOOO00O0O00O0O}种子给{O00O00OO00000OO0O.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O00OO0OOO0OO000O0 :#line:615
            print (O00OO0OOO0OO000O0 )#line:616
    def invitation (O00OO0O0OOO0O00OO ):#line:618
        try :#line:619
            _O0000O0OOOO00O00O =float (bundled_def ())/4 #line:620
            OO0OO00OOO000OO00 =f'_innerId={int(_O0000O0OOOO00O00O)}_{timi_new()}'#line:622
            OO0OO0000O0O0O000 ={'source':'scsc','authorization':O00OO0O0OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00OOO000OO00 ),'signstring':OO0OO00OOO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            O00O0OOOO0O00O000 ={"innerId":int (_O0000O0OOOO00O00O )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO0000O0O0O000 ,data =O00O0OOOO0O00O000 )#line:635
        except Exception as O0O0OOOO0OOO00000 :#line:636
            print (O0O0OOOO0OOO00000 )#line:637
    def winning_rewards (O0000O00OO0O0O000 ):#line:640
        try :#line:641
            O0O00OO0O00O00000 =f'__{timi_new()}'#line:642
            OOOOOOO0OO00O0000 ={'source':'scsc','authorization':O0000O00OO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O00O00000 ),'signstring':O0O00OO0O00O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            O00OO0O0000OOO000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOOOO0OO00O0000 ).json ()#line:654
            if 'status'in O00OO0O0000OOO000 :#line:656
                if O00OO0O0000OOO000 ['status']==200 :#line:657
                    if O00OO0O0000OOO000 ['data']['amount']:#line:658
                        OO0OO00000O0O0OOO =O00OO0O0000OOO000 ['data']['amount']['gold']#line:659
                        return OO0OO00000O0O0OOO #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOO00O0OO0000OO00 :#line:663
            print (OOO00O0OO0000OO00 )#line:664
    def certification (OOO00OOO00O0OO0OO ):#line:667
        try :#line:668
            O0000000OO0O000OO =f'__{timi_new()}'#line:669
            O000OOOO0OOOO0O0O ={'source':'scsc','authorization':OOO00OOO00O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000OO0O000OO ),'signstring':O0000000OO0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O0OOOO00OO0OOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000OOOO0OOOO0O0O ).json ()#line:681
            if 'status'in O0OOOO00OO0OOOO00 :#line:683
                if O0OOOO00OO0OOOO00 ['status']==200 :#line:684
                    if O0OOOO00OO0OOOO00 ['data']['result']:#line:685
                        O0O00OOOO0O00O0OO =O0OOOO00OO0OOOO00 ['data']['nick_name']#line:686
                        return O0O00OOOO0O00O0OO #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0OOOOOO00000OO00 :#line:690
            print (O0OOOOOO00000OO00 )#line:691
    def crops_illustrated (OO0O000OOOO000OOO ):#line:694
        try :#line:695
            OO00OO000000OOOO0 =f'__{timi_new()}'#line:696
            OO0O0O0O0OO0OOO0O ={'source':'scsc','authorization':OO0O000OOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000000OOOO0 ),'signstring':OO00OO000000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            OOOOO00000O0O0O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0O0O0OO0OOO0O ).json ()#line:708
            if 'status'in OOOOO00000O0O0O00 :#line:710
                if OOOOO00000O0O0O00 ['status']==200 :#line:711
                    OO0OOOO00O00OO0O0 =OOOOO00000O0O0O00 ['data'][0 ]['crops']#line:712
                    for O0O00O0OO00O0OOO0 in OO0OOOO00O00OO0O0 :#line:713
                        if O0O00O0OO00O0OOO0 ['ill_clover_award']:#line:714
                            if float (O0O00O0OO00O0OOO0 ['ill_clover_award'])>1 :#line:715
                                if O0O00O0OO00O0OOO0 ['is_finish']:#line:716
                                    if not O0O00O0OO00O0OOO0 ['is_getit']:#line:717
                                        if OO0O000OOOO000OOO .certification ()!='未实名':#line:718
                                            OO00OO000000OOOO0 =f'_award_level={O0O00O0OO00O0OOO0["level"]}_{timi_new()}'#line:719
                                            OO0O0O0O0OO0OOO0O ={'source':'scsc','authorization':OO0O000OOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO000000OOOO0 ),'signstring':OO00OO000000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            OO0OO0OO0000O0O0O ={"award_level":O0O00O0OO00O0OOO0 ['level']}#line:731
                                            O0000OO0OOO00000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0O0O0OO0OOO0O ,json =OO0OO0OO0000O0O0O ).json ()#line:733
                                            if 'status'in O0000OO0OOO00000O :#line:734
                                                if O0000OO0OOO00000O ['status']==200 :#line:735
                                                    O0O0O0000O0O000O0 =O0000OO0OOO00000O ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O0O00O0OO00O0OOO0["crop_name"]}成就丨奖励{O0O0O0000O0O000O0}☘️')#line:738
                                                if O0000OO0OOO00000O ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{O0000OO0OOO00000O["message"]}')#line:740
        except Exception as OOOO0OOO0O000OOO0 :#line:741
            print (OOOO0OOO0O000OOO0 )#line:742
    def watched_ad (OOO000O00O0OOO0OO ):#line:745
        try :#line:746
            O00OOO0OOOO0O00O0 =f'__{timi_new()}'#line:747
            OOO0000OO0O00O00O ={'source':'scsc','authorization':OOO000O00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOO0O00O0 ),'signstring':O00OOO0OOOO0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OO000OO0OO0OO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0000OO0O00O00O ).json ()#line:759
            if 'status'in OO000OO0OO0OO0O00 :#line:761
                if OO000OO0OO0OO0O00 ['status']==200 :#line:762
                    if 'offlineInfo'in OO000OO0OO0OO0O00 ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OO000OO0000O0000O =OO000OO0OO0OO0O00 ['data']['offlineInfo']['off_minute']#line:765
                        OOO0O0O0O0000O00O =float (OO000OO0OO0OO0O00 ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO0000OO0O00O00O ).json ()#line:768
                        time .sleep (2 )#line:769
                        O0O00OOO00OO00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0000OO0O00O00O ).json ()#line:770
                        if 'status'in O0O00OOO00OO00OO0 :#line:772
                            if O0O00OOO00OO00OO0 ['status']==200 :#line:773
                                OOO0OOO0O000OO0OO =float (O0O00OOO00OO00OO0 ['data']['silver'])/1000000000000 #line:774
                                OOO0O0O0O0OOOO00O =str (OOO0OOO0O000OO0OO -OOO0O0O0O0000O00O )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OO000OO0000O0000O}分钟奖励🌱数量:{OOO0O0O0O0OOOO00O}t粒')#line:776
        except Exception as OOOOO00000O0000O0 :#line:777
            print (OOOOO00000O0000O0 )#line:778
    def user_ad (OO00OOO000O00OO00 ):#line:781
        try :#line:782
            O00O00O000O0OOO0O =f'__{timi_new()}'#line:783
            OO00OO00O0000OO00 ={'source':'scsc','authorization':OO00OOO000O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000O0OOO0O ),'signstring':O00O00O000O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O0OOOOOOO00OO0O00 =requests .request ('get',f'{host}/user/ad',headers =OO00OO00O0000OO00 ).json ()#line:795
            if 'status'in O0OOOOOOO00OO0O00 :#line:797
                if O0OOOOOOO00OO0O00 ['status']==200 :#line:798
                    O00O0O000OO00O0O0 =O0OOOOOOO00OO0O00 ['data']['max_time']#line:799
                    O0OO0O00OOO0000OO =O0OOOOOOO00OO0O00 ['data']['watch_time']#line:800
                    O0OO0O00O0O0O0OO0 =O0OOOOOOO00OO0O00 ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O0OO0O00O0O0O0OO0 + O00O0O000OO00O0O0 - O0OO0O00OOO0000OO}次丨好友提供:{O0OO0O00O0O0O0OO0}次')#line:802
                    if O0OO0O00O0O0O0OO0 +O00O0O000OO00O0O0 -O0OO0O00OOO0000OO >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        O0OO0OO00O00000OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OO00O0000OO00 ).json ()#line:805
                        if 'status'in O0OO0OO00O00000OO :#line:807
                            if O0OO0OO00O00000OO ['status']==200 :#line:808
                                OO0OOO0OO00OO0000 =float (O0OO0OO00O00000OO ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OO0OOO0OO00OO0000)}t粒')#line:810
                                return True #line:811
                            if O0OO0OO00O00000OO ['status']==500 :#line:812
                                OO000O0O0OO00OOOO =O0OO0OO00O00000OO ['message']#line:813
                                print (f'【获取种子】:{OO000O0O0OO00OOOO}')#line:814
                                return False #line:815
        except Exception as OO00O00000OOO0O00 :#line:816
            print (OO00O00000OOO0O00 )#line:817
    def synthetic (O0O0O00OOO000O000 ):#line:820
        global id ,g #line:821
        try :#line:822
            OOOOOO00OO00O0O0O =O0O0O00OOO000O000 .level_new ()#line:823
            O00OO00O00OOO00O0 =random .randint (9 ,11 )#line:824
            O000O000OO0OO00OO =f'_site=8&targetSite={O00OO00O00OOO00O0}_{timi_new()}'#line:825
            OO0O00OOO00OOOOO0 ={'source':'scsc','authorization':O0O0O00OOO000O000 .token ,'timestamp':timi_new (),'sign':sign (O000O000OO0OO00OO ),'signstring':O000O000OO0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            O000000OOO0O0O000 ={"site":int (8 ),"targetSite":int (O00OO00O00OOO00O0 )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OOO00OOOOO0 ,json =O000000OOO0O0O000 )#line:838
            while True :#line:839
                O0OOO0O0OOO0OOO0O =f'__{timi_new()}'#line:840
                O0O0OOOOO00OO000O ={'source':'scsc','authorization':O0O0O00OOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0OOO0OOO0O ),'signstring':O0OOO0O0OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O00OOO0O00OO0O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOO00OO000O ).json ()#line:852
                if 'status'in O00OOO0O00OO0O0O0 :#line:854
                    if O00OOO0O00OO0O0O0 ['status']==200 :#line:855
                        OO0OOOO0OO00O0OOO =O00OOO0O00OO0O0O0 ['data']['cropList']#line:856
                        O0O0OO0OO0O000000 =O00OOO0O00OO0O0O0 ['data']['gameCoreDataDBid']#line:857
                        O00000OOO0O0OOOOO =float (O00OOO0O00OO0O0O0 ['data']['silver'])/1000000000000 #line:858
                        OO00O00O0O0000OOO =0 #line:863
                        for O0OO0OOO0OO0O0000 in OO0OOOO0OO00O0OOO :#line:864
                            if not O0OO0OOO0OO0O0000 :#line:865
                                O000O0O00O00OOOO0 =f'_crop_id={O0O0OO0OO0O000000}&site={OO00O00O0O0000OOO}_{O0O0O00OOO000O000.time}'#line:866
                                O0O0O0000O0O000OO ={'source':'scsc','authorization':O0O0O00OOO000O000 .token ,'timestamp':O0O0O00OOO000O000 .time ,'sign':sign (O000O0O00O00OOOO0 ),'signstring':O000O0O00O00OOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                O0O0O00OOOOOOOOOO ={"site":OO00O00O0O0000OOO ,"crop_id":O0O0OO0OO0O000000 }#line:877
                                OO00O00OOO000O000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0O0000O0O000OO ,data =O0O0O00OOOOOOOOOO ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OO00O00OOO000O000 :#line:881
                                    if OO00O00OOO000O000 ['status']==200 :#line:882
                                        if OO00O00OOO000O000 ['message']=='种子数量不足':#line:883
                                            OOOOOO00OO00O0O0O =O0O0O00OOO000O000 .level_new ()#line:884
                                            print (f'【种植合成】:{OO00O00OOO000O000["message"]}')#line:885
                                            if not O0O0O00OOO000O000 .user_ad ():#line:886
                                                return False #line:887
                                    if OO00O00OOO000O000 ['status']==500 :#line:888
                                        print (f'【种植合成】:{OO00O00OOO000O000["message"]}')#line:889
                                        return False #line:890
                            OO00O00O0O0000OOO +=1 #line:891
                        OOOOO000O00OO0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOO00OO000O ).json ()#line:892
                        O00O000O0O00OOOO0 =OOOOO000O00OO0OO0 ['data']['cropList']#line:893
                        O0O0000O00O0OO000 =False #line:894
                        for O0OO0OOO0OO0O0000 in range (12 ):#line:895
                            id =O00O000O0O00OOOO0 [O0OO0OOO0OO0O0000 ]['level']#line:896
                            if float (OOOOOO00OO00O0O0O )-float (id )>9 :#line:897
                                OO00O00000000OOO0 =f'_site={O0OO0OOO0OO0O0000}_{timi_new()}'#line:898
                                OO0OO0OOOOOO0000O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0O00OOO000O000 .token ,'timestamp':timi_new (),'sign':sign (OO00O00000000OOO0 ),'signstring':OO00O00000000OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O0OO000OOOOOOO0OO ={"site":O0OO0OOO0OO0O0000 }#line:910
                                O0OOO00OOO0O0O0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0OO0OOOOOO0000O ,data =O0OO000OOOOOOO0OO ).json ()#line:912
                                if 'status'in O0OOO00OOO0O0O0OO :#line:913
                                    if O0OOO00OOO0O0O0OO ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OOOO0000OOOO0OOO0 in range (11 ):#line:917
                                    O000OO0O0O0OO000O =OOOO0000OOOO0OOO0 +1 #line:918
                                    g =O00O000O0O00OOOO0 [O000OO0O0O0OO000O ]['level']#line:919
                                    if id ==g :#line:920
                                        OO0OO0OO000000O0O =OOOO0000OOOO0OOO0 +2 #line:921
                                        if OO0OO0OO000000O0O !=O0OO0OOO0OO0O0000 +1 :#line:922
                                            O0OOO00OOO000O000 =O0OO0OOO0OO0O0000 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O000O000OO0OO00OO =f'_site={O0OOO00OOO000O000 - 1}&targetSite={OO0OO0OO000000O0O - 1}_{timi_new()}'#line:926
                                            OO0O00OOO00OOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0O00OOO000O000 .token ,'timestamp':timi_new (),'sign':sign (O000O000OO0OO00OO ),'signstring':O000O000OO0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            OO00O0OOOO00O0O00 ={"site":int (O0OOO00OOO000O000 -1 ),"targetSite":int (OO0OO0OO000000O0O -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OOO00OOOOO0 ,json =OO00O0OOOO00O0O00 )#line:945
                                            O0O0000O00O0OO000 =True #line:947
                                    if O0O0000O00O0OO000 :#line:948
                                        break #line:949
                                if O0O0000O00O0OO000 :#line:950
                                    break #line:951
        except :#line:952
            O0O0O00OOO000O000 .synthetic ()#line:953
    def level_new (OO000000O00OO000O ):#line:956
        try :#line:957
            O00O0O00O0OO00O0O =f'__{timi_new()}'#line:958
            OOOO0OOO0O00OO0OO ={'source':'scsc','authorization':OO000000O00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00O0OO00O0O ),'signstring':O00O0O00O0OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O000OOOOO00OO00O0 =requests .request ('get',f'{host}/user',headers =OOOO0OOO0O00OO0OO ).json ()#line:970
            if 'status'in O000OOOOO00OO00O0 :#line:971
                if O000OOOOO00OO00O0 ['status']==200 :#line:972
                    return float (O000OOOOO00OO00O0 ['data']['level'])#line:973
        except Exception as O0OO00OOOOO0OO00O :#line:974
            print (O0OO00OOOOO0OO00O )#line:975
    def propsraffle (OOO00OOO0OOOO0OO0 ):#line:978
        try :#line:979
            while True :#line:980
                OO00O00OOOOOO0OO0 =f'__{timi_new()}'#line:981
                OOOOOOO0000OOOOO0 ={'source':'scsc','authorization':OOO00OOO0OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOOO0OO0 ),'signstring':OO00O00OOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                O0O0O00OOO00O0000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOOOO0000OOOOO0 ).json ()#line:993
                if 'status'in O0O0O00OOO00O0000 :#line:995
                    if O0O0O00OOO00O0000 ['status']==200 :#line:996
                        OO000O000OO00OOO0 =O0O0O00OOO00O0000 ['data']['rows']#line:997
                        O0000OOO0000OOOO0 =O0O0O00OOO00O0000 ['data']['vstate']#line:998
                        if OO000O000OO00OOO0 ==5 or OO000O000OO00OOO0 ==6 or OO000O000OO00OOO0 ==7 :#line:999
                            O0O000OO0O00O0000 =O0O0O00OOO00O0000 ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O0O000OO0O00O0000}')#line:1001
                        if OO000O000OO00OOO0 ==1 or OO000O000OO00OOO0 ==2 or OO000O000OO00OOO0 ==3 :#line:1002
                            OOO0O0OOO0OO0O0O0 =O0O0O00OOO00O0000 ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{OOO0O0OOO0OO0O0O0}')#line:1004
                        if OO000O000OO00OOO0 ==4 or OO000O000OO00OOO0 ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OO000O000OO00OOO0 =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as O0O0O0O0OO0OO00OO :#line:1046
            print (O0O0O0O0OO0OO00OO )#line:1047
    def friends_invitation (OOO0OO00OOO000O0O ):#line:1050
        try :#line:1051
            O000O0O0OO0OOOOOO =f'__{timi_new()}'#line:1052
            OOO00O0O000OO00OO ={'source':'scsc','authorization':OOO0OO00OOO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OO0OOOOOO ),'signstring':O000O0O0OO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            OO0000OOOOOOOO0OO =requests .request ('get',f'{host}/friends',headers =OOO00O0O000OO00OO ).json ()#line:1064
            if 'status'in OO0000OOOOOOOO0OO :#line:1065
                if OO0000OOOOOOOO0OO ['status']==200 :#line:1066
                    O00OOO0000OOOO0O0 =OO0000OOOOOOOO0OO ['data']['myInviteter']#line:1067
                    if O00OOO0000OOOO0O0 :#line:1068
                        O00O00OOOOO0O0OO0 =O00OOO0000OOOO0O0 ['user']['nickname']#line:1069
                        OOO0OO00OOO000000 =OOO0OO00OOO000O0O .certification ()#line:1070
                        if OOO0OO00OOO000000 =='未实名':#line:1071
                            weishim .append (OOO0OO00OOO000O0O .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O00O00OOOOO0O0OO0}丨实名:{OOO0OO00OOO000000}')#line:1073
        except Exception as O0OO00O00O000O00O :#line:1077
            print (O0OO00O00O000O00O )#line:1078
    def add_clover (O000OOO0OOOO000OO ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O00OOO0O00O0OOO0O =f'__{timi_new()}'#line:1084
            O0O000OOOO00O000O ={'source':'scsc','authorization':O000OOO0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O00O0OOO0O ),'signstring':O00OOO0O00O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            O0OO0O00O000O0OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O000OOOO00O000O ).json ()#line:1096
            if 'status'in O0OO0O00O000O0OO0 :#line:1098
                if O0OO0O00O000O0OO0 ['status']==200 :#line:1099
                    O00O0O0O0O0OO0000 =O0OO0O00O000O0OO0 ['data']['clover']#line:1100
                    OOOO0OOO0O0O0OO0O =O0OO0O00O000O0OO0 ['data']['used_clover']#line:1101
                    O0OO000O0OOOO0OO0 =float (O00O0O0O0O0OO0000 )-float (OOOO0OOO0O0O0OO0O )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOO0OOO0O0O0OO0O}')#line:1103
                    if O000OOO0OOOO000OO .certification ()!='未实名':#line:1104
                        if O0OO000O0OOOO0OO0 >1 :#line:1105
                            O00OOO0O00O0OOO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO000O0OOOO0OO0)}_{timi_new()}'#line:1106
                            O00OOO0000OOO0O0O ={'source':'scsc','authorization':O000OOO0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O00O0OOO0O ),'signstring':O00OOO0O00O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OO0O0O0O000O000O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO000O0OOOO0OO0 )}#line:1118
                            O00O0000O0O000000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OOO0000OOO0O0O ,data =OO0O0O0O000O000O0 ).json ()#line:1119
                            if 'status'in O00O0000O0O000000 :#line:1121
                                if O00O0000O0O000000 ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O00O0000O0O000000["data"]["isSuccess"]}丨数量:{O0OO000O0OOOO0OO0}')#line:1123
                                if O00O0000O0O000000 ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O00O0000O0O000000["message"]}')#line:1125
            O0OO000O0000O0O0O =requests .request ('get',f'{host}/lottery',headers =O0O000OOOO00O000O ).json ()#line:1126
            O000OOO00OO0OO0OO =O000OOO0OOOO000OO .winning_rewards ()#line:1128
            if 'status'in O0OO000O0000O0O0O :#line:1129
                if O0OO000O0000O0O0O ['status']==200 :#line:1130
                    OOOO00000000O0OO0 =O0OO000O0000O0O0O ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OOOO00000000O0OO0 )#line:1132
                    O0000OOO0000O0OOO =O0OO000O0000O0O0O ['data'][1 ]['value']#line:1133
                    O0O0O00OO0O0O0O0O =O0OO000O0000O0O0O ['data'][0 ]['join_number']#line:1134
                    O0O00OO00O0O0OO0O =int (float (O0OO000O0000O0O0O ['data'][0 ]['totalValue']))#line:1135
                    O00O0000O000OO000 =float (O0000OOO0000O0OOO /O0O00OO00O0O0OO0O )*10000 #line:1136
                    O0OOOO000O0O000OO =O0O00OO00O0O0OO0O /O0O0O00OO0O0O0O0O #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OOOO00000000O0OO0)[:6]}颗金种子丨好友收益:{str(O000OOO00OO0OO0OO)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(O00O0000O000OO000)[:6]}颗金种子丨☘️人均:{str(O0OOOO000O0O000OO)[:7]}️')#line:1139
        except Exception as O00O000000OO0O0OO :#line:1140
            print (O00O000000OO0O0OO )#line:1141
    def energy (OOOO00O00O000O0OO ):#line:1144
        try :#line:1145
            while True :#line:1146
                OO00O0O00O00OO00O =f'__{timi_new()}'#line:1147
                O0O00OO000O00O000 ={'source':'scsc','authorization':OOOO00O00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00O00OO00O ),'signstring':OO00O0O00O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OOOOOO00O0O000O0O =requests .request ('get',f'{host}/energy/general',headers =O0O00OO000O00O000 ).json ()#line:1159
                if 'status'in OOOOOO00O0O000O0O :#line:1161
                    if OOOOOO00O0O000O0O ['status']==200 :#line:1162
                        OO0O0O0O00O0OOOOO =OOOOOO00O0O000O0O ['data']['ordinary_water']#line:1163
                        OO0OOOOOOOOOOOO00 =OOOOOO00O0O000O0O ['data']['ordinary_fertilizer']#line:1164
                        O0O000OO00O00OOO0 =OOOOOO00O0O000O0O ['data']['videoStatus']#line:1165
                        OO0O0OOOO0OOOO0OO =OOOOOO00O0O000O0O ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(OO0OOOOOOOOOOOO00).split(".")[0]}丨水滴:{str(OO0O0O0O00O0OOOOO).split(".")[0]}')#line:1168
                        if float (OO0OOOOOOOOOOOO00 )<96 :#line:1169
                            if O0O000OO00O00OOO0 :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                O0O0O00OO0O0OO000 =99 -float (OO0OOOOOOOOOOOO00 )#line:1172
                                OO000OOOO0OO0O00O ={"fertilizer":str (O0O0O00OO0O0OO000 ).split ('.')[0 ]}#line:1173
                                O000OO0OO0000OOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O00OO000O00O000 ).json ()#line:1175
                                if 'status'in O000OO0OO0000OOO0 :#line:1177
                                    if O000OO0OO0000OOO0 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{O000OO0OO0000OOO0["message"]}')#line:1179
                                    if O000OO0OO0000OOO0 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{O000OO0OO0000OOO0["message"]}')#line:1181
                                        break #line:1182
                                if float (OO0OOOOOOOOOOOO00 )<78 :#line:1184
                                    O0O0O00OO0O0OO000 =80 -float (OO0OOOOOOOOOOOO00 )#line:1185
                                    OO0OO0O0OOOOOO0OO =f'_fertilizer={int(O0O0O00OO0O0OO000)}_{timi_new()}'#line:1186
                                    OOOOOO0O0O00O000O ={'source':'scsc','authorization':OOOO00O00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OOOOOO0OO ),'signstring':OO0OO0O0OOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    O0000000O0OO0O0O0 ={"fertilizer":int (O0O0O00OO0O0OO000 )}#line:1198
                                    OO0OO00000O00O00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOOO0O0O00O000O ,data =O0000000O0OO0O0O0 ).json ()#line:1200
                                    if 'status'in OO0OO00000O00O00O :#line:1202
                                        if OO0OO00000O00O00O ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OO0OO00000O00O00O["message"]}丨数量:{int(O0O0O00OO0O0OO000)}')#line:1204
                                        if OO0OO00000O00O00O ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OO0OO00000O00O00O["message"]}丨数量:{int(O0O0O00OO0O0OO000)}')#line:1206
                                            OOO000O0O00O00O0O =OO0OO00000O00O00O ["message"].split ('-')[1 ]#line:1207
                                            O00OO0O00O0OOO0O0 =f'__{timi_new()}'#line:1208
                                            O00O0OO0OOOO0O000 ={'source':'scsc','authorization':OOOO00O00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00O0OOO0O0 ),'signstring':O00OO0O00O0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            O0O00OO00O00O0O0O =requests .request ('get',f'{host}/user',headers =O00O0OO0OOOO0O000 ).json ()#line:1220
                                            if 'status'in O0O00OO00O00O0O0O :#line:1221
                                                if O0O00OO00O00O0O0O ['status']==200 :#line:1222
                                                    O0OO00000OO000OO0 =O0O00OO00O00O0O0O ['data']['inner_id']#line:1223
                                                    if give_gold (O0OO00000OO000OO0 ,float (OOO000O0O00O00O0O )+1 ):#line:1224
                                                        OOOO00O00O000O0OO .energy ()#line:1225
                        if float (OO0O0O0O00O0OOOOO )<880 :#line:1226
                            if OO0O0OOOO0OOOO0OO :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                O0OOO000O0O00OOO0 =999 -float (OO0O0O0O00O0OOOOO )#line:1229
                                OO0OOOO0O0O000000 ={"water":str (O0OOO000O0O00OOO0 ).split ('.')[0 ]}#line:1230
                                O0OOOO000O0OO00OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O00OO000O00O000 ).json ()#line:1232
                                if 'status'in O0OOOO000O0OO00OO :#line:1234
                                    if O0OOOO000O0OO00OO ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOOO000O0OO00OO["message"]}')#line:1236
                                    if O0OOOO000O0OO00OO ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{O0OOOO000O0OO00OO["message"]}')#line:1238
                                        break #line:1239
                                if float (OO0O0O0O00O0OOOOO )<780 :#line:1240
                                    O0OOO000O0O00OOO0 =800 -float (OO0O0O0O00O0OOOOO )#line:1241
                                    O00000OOO0OO0O000 =f'_water={int(O0OOO000O0O00OOO0)}_{timi_new()}'#line:1242
                                    O000O000O0OOO0O00 ={'source':'scsc','authorization':OOOO00O00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO0OO0O000 ),'signstring':O00000OOO0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O0O00000OO0O0O0O0 ={"water":int (O0OOO000O0O00OOO0 )}#line:1254
                                    OO000OO0OOO0O0OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000O000O0OOO0O00 ,data =O0O00000OO0O0O0O0 ).json ()#line:1256
                                    if 'status'in OO000OO0OOO0O0OO0 :#line:1258
                                        if OO000OO0OOO0O0OO0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{OO000OO0OOO0O0OO0["message"]}丨数量:{int(O0OOO000O0O00OOO0)}')#line:1260
                                        if OO000OO0OOO0O0OO0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{OO000OO0OOO0O0OO0["message"]}丨数量:{int(O0OOO000O0O00OOO0)}')#line:1262
                                            OOO000O0O00O00O0O =OO000OO0OOO0O0OO0 ["message"].split ('-')[1 ]#line:1263
                                            O00OO0O00O0OOO0O0 =f'__{timi_new()}'#line:1264
                                            O00O0OO0OOOO0O000 ={'source':'scsc','authorization':OOOO00O00O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00O0OOO0O0 ),'signstring':O00OO0O00O0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            O0O00OO00O00O0O0O =requests .request ('get',f'{host}/user',headers =O00O0OO0OOOO0O000 ).json ()#line:1276
                                            if 'status'in O0O00OO00O00O0O0O :#line:1277
                                                if O0O00OO00O00O0O0O ['status']==200 :#line:1278
                                                    O0OO00000OO000OO0 =O0O00OO00O00O0O0O ['data']['inner_id']#line:1279
                                                    if give_gold (O0OO00000OO000OO0 ,float (OOO000O0O00O00O0O )+1 ):#line:1280
                                                        OOOO00O00O000O0OO .energy ()#line:1281
                        break #line:1282
        except Exception as OO0OOO000OO0OO0OO :#line:1283
            print (OO0OOO000OO0OO0OO )#line:1284
def bundled_def ():#line:1287
    O0OOO0OOO0OO0OO00 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return O0OOO0OOO0OO0OO00 [random .randint (0 ,len (O0OOO0OOO0OO0OO00 )-1 )]#line:1289
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
        OO00OO0OO0O000O0O =gitee_edition ()#line:1328
        if version_of_the_validation ()<OO00OO0OO0O000O0O ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OO0OO0O000O0O["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{OO00OO0OO0O000O0O["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OO0OO0O000O0O["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {OO00OO0OO0O000O0O["CityEarth"]["content"]}')#line:1334
    except Exception as O00000O0O0O000OOO :#line:1335
        print (O00000O0O0O000OOO )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
