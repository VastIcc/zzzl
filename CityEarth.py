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
        OOOOOO0O0OO00O0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOOOOO0O0OO00O0O0)}个账号==========")#line:17
        for OO00O0000OO0O0OOO in OOOOOO0O0OO00O0O0 :#line:18
            O0O00000OO0000O00 =[]#line:19
            print (f"------------正在执行第{OOOOOO0O0OO00O0O0.index(OO00O0000OO0O0OOO) + 1}个账号------------")#line:20
            OOO0OOOO0OOO0OO0O =CityEarth (OO00O0000OO0O0OOO ,O0O00000OO0000O00 ,OOOOOO0O0OO00O0O0 .index (OO00O0000OO0O0OOO ))#line:21
            def OOO0OOO000OO00O00 ():#line:23
                if OOO0OOOO0OOO0OO0O .base_info ():#line:25
                    OOO0OOOO0OOO0OO0O .sealing ()#line:27
                    OOO0OOOO0OOO0OO0O .invitenum ()#line:29
                    OOO0OOOO0OOO0OO0O .query_to_sell ()#line:31
                    OOO0OOOO0OOO0OO0O .friends_invitation ()#line:35
                    OOO0OOOO0OOO0OO0O .energy ()#line:37
                    OOO0OOOO0OOO0OO0O .add_clover ()#line:39
                    OOO0OOOO0OOO0OO0O .propsraffle ()#line:41
                    OOO0OOOO0OOO0OO0O .synthetic ()#line:43
                    OOO0OOOO0OOO0OO0O .crops_illustrated ()#line:45
                    OOO0OOOO0OOO0OO0O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO0OOOO0OOO0OO0O .give_gold ()#line:50
            O000000O000OO0OO0 =threading .Thread (target =OOO0OOO000OO00O00 )#line:52
            O000000O000OO0OO0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OOOOO0OO0000O0000 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOOO0OO0000O0000 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O00O0OO0OO0O00O0O in invited_new :#line:62
            print (O00O0OO0OO0O00O0O )#line:63
        print ('开始打印未实名的token')#line:64
        for OOOOOOO00OOOO00OO in weishim :#line:65
            print (OOOOOOO00OOOO00OO )#line:66
    except Exception as OOO0OO0000O000000 :#line:67
        print (OOO0OO0000O000000 )#line:68
def give_gold (OOO000O0000OO0O00 ,O0OO00OOO00O0000O ):#line:72
    try :#line:73
        O00OOOOOOO0OO0O0O =f'_doneeNo={OOO000O0000OO0O00}&quantity={int(O0OO00OOO00O0000O)}_{timi_new()}'#line:74
        O00OOOO0000OO0O00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO0OO0O0O ),'signstring':O00OOOOOOO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OOOO0OO0OO0OO0OO0 ={"quantity":int (O0OO00OOO00O0000O ),"doneeNo":OOO000O0000OO0O00 }#line:89
        OO00O0O0O00000O0O =requests .request ('post',f'{host}/finance/give-gold',headers =O00OOOO0000OO0O00 ,data =OOOO0OO0OO0OO0OO0 ).json ()#line:90
        if 'status'in OO00O0O0O00000O0O :#line:92
            if OO00O0O0O00000O0O ['status']==200 :#line:93
                if OO00O0O0O00000O0O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0OO00OOO00O0000O)}种子给{OOO000O0000OO0O00}成功')#line:95
                    return True #line:96
            if OO00O0O0O00000O0O ['status']==401 :#line:97
                print (f'【赠送种子】:{OO00O0O0O00000O0O["message"]}')#line:98
                return False #line:99
            if OO00O0O0O00000O0O ['status']==500 :#line:100
                print (f'【赠送种子】:{OO00O0O0O00000O0O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0OOOO000O0O00OO0 :#line:104
        print (O0OOOO000O0O00OO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OO0OO000000O0O0 ):#line:115
    OOOO0OO000000O000 =hashlib .md5 (O0OO0OO000000O0O0 .encode ()).hexdigest ()#line:116
    OO000O000O00000OO =sc1 ()#line:117
    OO0OOOOO0OOO0O00O =sc2 ()#line:118
    OOOOO0OO0O0000O0O =sc3 ()#line:119
    OOOO0000O0O00OO00 =OO000O000O00000OO +OOOO0OO000000O000 +OO0OOOOO0OOO0O00O +OOOOO0OO0O0000O0O #line:120
    OO0000O0OO00OO00O =hashlib .md5 (OOOO0000O0O00OO00 .encode ()).hexdigest ()#line:121
    return OO0000O0OO00OO00O #line:122
def format_msg ():#line:125
    OO00000000OO0O00O =""#line:126
    for O00OOOOO0O00O0OOO in msg_list :#line:127
        OO00000000OO0O00O +=str (O00OOOOO0O00O0OOO )+"\r\n"#line:128
    return OO00000000OO0O00O #line:129
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
def get_json_data (OO000OOOO00OO0000 ,OOO00000OOO00OOO0 ,OOOOO0000O0OO0O00 ,OOO00O00000OOO000 ):#line:153
    with open (OO000OOOO00OO0000 ,'rb')as O0O0000O0O0000OO0 :#line:154
        O0O0000O0O0OO0OO0 =json .load (O0O0000O0O0000OO0 )#line:155
        O0O0000O0O0OO0OO0 ['data'][OOO00000OOO00OOO0 ][OOOOO0000O0OO0O00 ]=OOO00O00000OOO000 #line:156
        O0OOOOO0O0O00000O =O0O0000O0O0OO0OO0 #line:157
    O0O0000O0O0000OO0 .close ()#line:158
    return O0OOOOO0O0O00000O #line:159
def write_json_data (OO0OO00OOOOOOO00O ):#line:162
    with open (json_path1 ,'w')as OO00O0O00OO000OOO :#line:163
        json .dump (OO0OO00OOOOOOO00O ,OO00O0O00OO000OOO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OO00O0O00OO000OOO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OOO0OO00OOO0OOO ,O000OO00O0000O0O0 ,O0000000O000OOOO0 ,O0000O0OOOO0OOO0O ):#line:171
        try :#line:172
            O0OOO0OO00OOO0OOO .msg =O0000000O000OOOO0 #line:173
            O0OOO0OO00OOO0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OOO0OO00OOO0OOO .token =O000OO00O0000O0O0 ['authorization']#line:175
            O0OOO0OO00OOO0OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OOO0OO00OOO0OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OOO0OO00OOO0OOO .elephant_user =O000OO00O0000O0O0 ['elephant_user']#line:178
            O0OOO0OO00OOO0OOO .elephant_pswd =O000OO00O0000O0O0 ['elephant_pswd']#line:179
            O0OOO0OO00OOO0OOO .elephant_Task_ID =O000OO00O0000O0O0 ['elephant_Task_ID']#line:180
            O0OOO0OO00OOO0OOO .len_new =O0000O0OOOO0OOO0O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO0OOOO0OO0OO00O0 ):#line:186
        try :#line:187
            OO0OOOO0OO0OO00O0 .watched_ad ()#line:189
            OOO0O0OOOOO00OOO0 =f'__{timi_new()}'#line:190
            O0O0OOO0OO0000O00 ={'source':'scsc','authorization':OO0OOOO0OO0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOOOO00OOO0 ),'signstring':OOO0O0OOOOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00O00OO000OO0O00 =requests .request ('get',f'{host}/user',headers =O0O0OOO0OO0000O00 ).json ()#line:202
            if 'status'in O00O00OO000OO0O00 :#line:204
                if O00O00OO000OO0O00 ['status']==200 :#line:205
                    O0OO00O0OO0000O00 =O00O00OO000OO0O00 ['data']['nickname']#line:206
                    O0OOO0O000O000O00 =O00O00OO000OO0O00 ['data']['inner_id']#line:207
                    O000OO0O0OO0O000O =O00O00OO000OO0O00 ['data']['assets']['gold']#line:208
                    OO000OO0OO000OO0O =O00O00OO000OO0O00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0OO00O0OO0000O00[:5]}丨ID:{O0OOO0O000O000O00}丨等级:{OO000OO0OO000OO0O}丨金种子:{str(O000OO0O0OO0O000O).split(".")[0]}')#line:211
                    if 'wx_'in O0OO00O0OO0000O00 :#line:212
                        OO0OOOO0OO0OO00O0 .change_nickname ()#line:213
                if O00O00OO000OO0O00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO0OOOO0OO0OO00O0 .elephant_user =='f':#line:216
                        return False #line:217
                    OO000OOOO0000O0OO =Invalid_login .addtask (elephant_user =OO0OOOO0OO0OO00O0 .elephant_user ,elephant_pswd =OO0OOOO0OO0OO00O0 .elephant_pswd ,elephant_Task_ID =OO0OOOO0OO0OO00O0 .elephant_Task_ID )#line:220
                    OO0OO0OO0OO000000 =get_json_data (json_path ,OO0OOOO0OO0OO00O0 .len_new ,'authorization',OO000OOOO0000O0OO )#line:221
                    if write_json_data (OO0OO0OO0OO000000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00O00OO000OO0O00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO00OOOOOOO00OOO0 :#line:228
            print (OO00OOOOOOO00OOO0 )#line:229
    def sealing (O0O0OO00OOO000000 ):#line:232
        try :#line:233
            OO0000OOOO0O0O00O =f'__{timi_new()}'#line:234
            OOO000OOO0OO00OO0 ={'source':'scsc','authorization':O0O0OO00OOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO0O0O00O ),'signstring':OO0000OOOO0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000OOO0OO00OO0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO000OOO0OO00OO0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000OOO0OO00OO0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000OOO0OO00OO0 )#line:249
            requests .request ('get',f'{host}/user',headers =OOO000OOO0OO00OO0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000OOO0OO00OO0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000OOO0OO00OO0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000OOO0OO00OO0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO0OO00OO0 )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO000OOO0OO00OO0 )#line:255
        except Exception as O0O0OOO00O000000O :#line:256
            print (O0O0OOO00O000000O )#line:257
    def ddd (OO00O000O0O00O000 ):#line:259
        try :#line:260
            OO0OO000OO0OO0OOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00OOO0OOO0OO00OO ={'source':'scsc','authorization':OO00O000O0O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO0OO0OOO ),'signstring':OO0OO000OO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO00O0OO00000OO00 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00OOO0OOO0OO00OO ).json ()#line:273
            print (OO00O0OO00000OO00 )#line:274
        except Exception as OOO0000OOOO0OOO00 :#line:277
            print (OOO0000OOOO0OOO00 )#line:278
    def the_query (OO00O000O000O0OO0 ):#line:283
        try :#line:284
            OO0O00O0OOOO00OOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO00OOOOO00OOOOO0 ={'authorization':OO00O000O000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OOOO00OOO ),'signstring':OO0O00O0OOOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O00O00000OO0000OO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00OOOOO00OOOOO0 ).json ()#line:296
            if 'status'in O00O00000OO0000OO :#line:298
                if O00O00000OO0000OO ['status']==200 :#line:299
                    return O00O00000OO0000OO ['data']['rows'][4 ]['price']#line:300
        except Exception as OO0O0OO0OO0000000 :#line:301
            print (OO0O0OO0OO0000000 )#line:302
    def market_sale (O0OOO0OO000O00O0O ,OO000O0OOO0O0O0O0 ):#line:305
        try :#line:306
            OO00000O00O0O0OOO =timi_new ()#line:307
            OO00OOO00OO0O0OO0 =f'type=crop__{OO00000O00O0O0OOO}'#line:308
            O0OO0OOOOO0O00O0O ={'source':'scsc','authorization':O0OOO0OO000O00O0O .token ,'timestamp':str (OO00000O00O0O0OOO ),'sign':sign (OO00OOO00OO0O0OO0 ),'signstring':OO00OOO00OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            OO0O0O000OOO00O0O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0OO0OOOOO0O00O0O ).json ()#line:320
            if 'status'in OO0O0O000OOO00O0O :#line:322
                if OO0O0O000OOO00O0O ['status']==200 :#line:323
                    if OO0O0O000OOO00O0O ['data']['rows']:#line:324
                        OOO00OOO0OOO0O00O =OO0O0O000OOO00O0O ['data']['rows'][0 ]['packsackItemId']#line:325
                        OO0O0O0OO00O0OOO0 =OO0O0O000OOO00O0O ['data']['rows'][0 ]['quantity']#line:326
                        if float (OO000O0OOO0O0O0O0 )>8 :#line:327
                            OO0OOOOO0000000OO =f'_packsackItemId={OOO00OOO0OOO0O00O}&price={str(OO000O0OOO0O0O0O0)[:5]}&quantity={OO0O0O0OO00O0OOO0}_{OO00000O00O0O0OOO}'#line:328
                            O0OOO0OOO000OO00O ={'source':'scsc','authorization':O0OOO0OO000O00O0O .token ,'timestamp':str (OO00000O00O0O0OOO ),'sign':sign (OO0OOOOO0000000OO ),'signstring':OO0OOOOO0000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOOOOOO0O0OO000OO ={"packsackItemId":OOO00OOO0OOO0O00O ,"price":str (OO000O0OOO0O0O0O0 )[:5 ],"quantity":str (OO0O0O0OO00O0OOO0 )}#line:344
                            O00OOO0000OOO0OOO =requests .request ('post',f'{host}/market/sale',headers =O0OOO0OOO000OO00O ,data =OOOOOOO0O0OO000OO ).json ()#line:345
                            if 'status'in O00OOO0000OOO0OOO :#line:347
                                if O00OOO0000OOO0OOO ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OO0O0O0OO00O0OOO0}丨价格:{str(OO000O0OOO0O0O0O0)[:5]}')#line:349
                                if O00OOO0000OOO0OOO ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O00OOO0000OOO0OOO["message"]}')#line:351
        except Exception as OO0OO00O0OOOO0OO0 :#line:352
            print (OO0OO00O0OOOO0OO0 )#line:353
    def query_to_sell (O00OO0O00O0OOOO00 ):#line:356
        global count_list #line:357
        try :#line:358
            OO0O00OO000O0O0OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            OO0O000O00OOOO000 ={'source':'scsc','authorization':O00OO0O00O0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO000O0O0OO ),'signstring':OO0O00OO000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            OO00O0OOO0OOOOO0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0O000O00OOOO000 ).json ()#line:371
            if 'status'in OO00O0OOO0OOOOO0O :#line:373
                if OO00O0OOO0OOOOO0O ['status']==200 :#line:374
                    for O00O0OO00O0O0O0OO in OO00O0OOO0OOOOO0O ['data']['rows']:#line:375
                        O0OOOO0O0O0O00OO0 =O00O0OO00O0O0O0OO ['materialKey']#line:376
                        OO00000O00000OOOO =O00O0OO00O0O0O0OO ['quantity']#line:377
                        O0O0OOO000OOOO00O =O00O0OO00O0O0O0OO ['price']#line:378
                        O0OO0000OOOOOOO0O =O00O0OO00O0O0O0OO ['saleState']#line:379
                        if O0OO0000OOOOOOO0O ==0 :#line:380
                            print (f'【出售订单】:名称:{O0OOOO0O0O0O00OO0}丨数量:{OO00000O00000OOOO}丨价格:{O0O0OOO000OOOO00O}')#line:381
                            count_list +=OO00000O00000OOOO #line:382
                            OOO00O000OO000O00 =O00OO0O00O0OOOO00 .the_query ()#line:384
                            if float (OOO00O000OO000O00 )!=float (O0O0OOO000OOOO00O ):#line:385
                                OO0OOO0OOO0OO0OOO =O00O0OO00O0O0O0OO ['id']#line:386
                                O00OO0O00O0OOOO00 .cacel_sale (OO0OOO0OOO0OO0OOO )#line:387
                    O00OO0O00O0OOOO00 .game_map ()#line:389
        except Exception as OOOOO0O000000OOO0 :#line:391
            print (OOOOO0O000000OOO0 )#line:392
    def cacel_sale (O0OOO0OO000O0O0O0 ,O0O000000OOOOO0OO ):#line:395
        try :#line:396
            OO00O0OOOOOOO0000 =f'_saleId={O0O000000OOOOO0OO}_{timi_new()}'#line:397
            OOO00OO0OOO000OO0 ={'source':'scsc','authorization':O0OOO0OO000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OOOOOOO0000 ),'signstring':OO00O0OOOOOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O000O00OO00O0OO00 ={"saleId":O0O000000OOOOO0OO }#line:409
            O0O0O00O0O0OOO000 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO00OO0OOO000OO0 ,data =O000O00OO00O0OO00 ).json ()#line:410
            if 'status'in O0O0O00O0O0OOO000 :#line:412
                if O0O0O00O0O0OOO000 ['status']==200 :#line:413
                    print (f'【下架出售】:{O0O0O00O0O0OOO000["data"]}')#line:414
        except Exception as OOO00O00O000O0O0O :#line:415
            print (OOO00O00O000O0O0O )#line:416
    def change_nickname (OOO0OO0OOO00O0000 ):#line:419
        try :#line:420
            O00000000000O0O00 =timi_new ()#line:421
            OOOO0O0O00OOOO0OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OO00OOOO00OO00OO0 =requests .request ('post','https://www.qmsjmfb.com/',data =OOOO0O0O00OOOO0OO ).text #line:423
            O0O0O0OO00O0OO000 =re .findall ('<ul><li>(.*?)</li>',OO00OOOO00OO00OO0 )[0 ][:3 ]#line:424
            OOO0OO00OOO0O00OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0O0OO00O0OO000}').json ()#line:425
            OO0000O0O0000OO00 =OOO0OO00OOO0O00OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            OOO00000OO00000OO ={"nickname":OO0000O0O0000OO00 }#line:427
            OO00O0OOOO0O0000O =f'_nickname={OO0000O0O0000OO00}_{O00000000000O0O00}'#line:428
            O0O00OOO00OOOO000 ={'source':'scsc','authorization':OOO0OO0OOO00O0000 .token ,'timestamp':O00000000000O0O00 ,'sign':sign (OO00O0OOOO0O0000O ),'signstring':OO00O0OOOO0O0000O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO0OO0OOO0OO0OOOO =requests .request ('patch',f'{host}/user/nickname',headers =O0O00OOO00OOOO000 ,data =OOO00000OO00000OO ).json ()#line:440
            if 'status'in OO0OO0OOO0OO0OOOO :#line:442
                if OO0OO0OOO0OO0OOOO ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OO0000O0O0000OO00}丨{OO0OO0OOO0OO0OOOO["message"]}')#line:444
        except Exception as OO0OO0OO0O0OOOOOO :#line:445
            print (OO0OO0OO0O0OOOOOO )#line:446
    def withdraw (O00O00O000OOO00OO ):#line:449
        try :#line:450
            OOOO0OOOOOO0OO000 =f'__{timi_new()}'#line:451
            O00OO00O00O0000O0 ={'source':'scsc','authorization':O00O00O000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOO0OO000 ),'signstring':OOOO0OOOOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOO0000OO00OO0O0O =requests .request ('get',f'{host}/assets',headers =O00OO00O00O0000O0 ).json ()#line:463
            if 'status'in OOO0000OO00OO0O0O :#line:465
                if OOO0000OO00OO0O0O ['status']==200 :#line:466
                    O0OO00OOOOOO00OOO =OOO0000OO00OO0O0O ['data']['cash']#line:467
                    if float (O0OO00OOOOOO00OOO )>20 :#line:468
                        OOOO0OOOOOO0OO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O00OO00O00O0000O0 ={'authorization':O00O00O000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOO0OO000 ),'signstring':OOOO0OOOOOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O0OOO0OOO000O0O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OO00O0O000O00OO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OO00O00O0000O0 ,data =O0OOO0OOO000O0O0O ).json ()#line:482
                        if 'status'in OO00O0O000O00OO00 :#line:484
                            if OO00O0O000O00OO00 ['status']==200 :#line:485
                                print (f'【余额提现】:{OO00O0O000O00OO00["data"]}')#line:486
                        if 'status'in OO00O0O000O00OO00 :#line:487
                            if OO00O0O000O00OO00 ['status']==500 :#line:488
                                print (f'【余额提现】:{OO00O0O000O00OO00["message"]}')#line:489
        except Exception as OOO0O0OO0000OO00O :#line:490
            print (OOO0O0OO0000OO00O )#line:491
    def invitenum (O00OOO00OOOO00O0O ):#line:494
        global invited_new #line:495
        try :#line:496
            OOOOO0O00OO000OOO =f'__{timi_new()}'#line:497
            O0O0O0OOOO0O000OO ={'source':'scsc','authorization':O00OOO00OOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO000OOO ),'signstring':OOOOO0O00OO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OO00OOOO00O0O0000 =requests .request ('get',f'{host}/invite/invitenum',headers =O0O0O0OOOO0O000OO ).json ()#line:509
            if 'status'in OO00OOOO00O0O0000 :#line:511
                if OO00OOOO00O0O0000 ['status']==200 :#line:512
                    O00O00O0O00000OO0 =OO00OOOO00O0O0000 ['data']['invited_count']#line:513
                    O0O0OOO0O00OO0O0O =OO00OOOO00O0O0000 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{O00O00O0O00000OO0}丨间邀好友:{O0O0OOO0O00OO0O0O}')#line:515
                    if O00O00O0O00000OO0 <2 :#line:516
                        O0OO0OO00O00OOO00 =f'__{timi_new()}'#line:517
                        OOOOOO000O0OO00OO ={'source':'scsc','authorization':O00OOO00OOOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00O00OOO00 ),'signstring':O0OO0OO00O00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OO0O0O000O00000OO =requests .request ('get',f'{host}/user',headers =OOOOOO000O0OO00OO ).json ()#line:529
                        if 'status'in OO0O0O000O00000OO :#line:531
                            if OO0O0O000O00000OO ['status']==200 :#line:532
                                invited_new .append (OO0O0O000O00000OO ['data']['inner_id'])#line:533
        except Exception as O0O0O0O0OOOOO00O0 :#line:534
            print (O0O0O0O0OOOOO00O0 )#line:535
    def game_map (OO0O0O0000OO00O00 ):#line:538
        try :#line:539
            OO00OO0O00O0O0O00 =f'__{timi_new()}'#line:540
            O0OOO000O0000OOOO ={'source':'scsc','authorization':OO0O0O0000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O00O0O0O00 ),'signstring':OO00OO0O00O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O00O00O000OOO00O0 =requests .request ('get',f'{host}/game/map',headers =O0OOO000O0000OOOO ).json ()#line:552
            if 'status'in O00O00O000OOO00O0 :#line:554
                if O00O00O000OOO00O0 ['status']==200 :#line:555
                    for OO0O0OOO0OO00OO0O in O00O00O000OOO00O0 ['data']['list'][0 ]['crops']:#line:556
                        O00O00OOO0O0OO0OO =OO0O0OOO0OO00OO0O ['level']#line:558
                        if O00O00OOO0O0OO0OO ==41 :#line:559
                            O0O0OO00O000O00OO =OO0O0OOO0OO00OO0O ['crop_name']#line:560
                            OOO00OOO0O0OOOO00 =OO0O0OOO0OO00OO0O ['count']#line:561
                            if OOO00OOO0O0OOOO00 >0 :#line:562
                                print (f'【农业资产】:{O0O0OO00O000O00OO}丨数量:{OOO00OOO0O0OOOO00}')#line:563
                                O0OO0OO0O0000O00O =OO0O0O0000OO00O00 .the_query ()#line:564
                                OO0O0O0000OO00O00 .market_sale (O0OO0OO0O0000O00O )#line:565
        except Exception as OOOOO0O0000OOOO0O :#line:566
            print (OOOOO0O0000OOOO0O )#line:567
    def give_gold (OO0O0O0000OOOOO0O ):#line:570
        try :#line:571
            O0O0O0O0O0OO0O00O =f'__{timi_new()}'#line:572
            OO0OOOO0OOO00OO0O ={'source':'scsc','authorization':OO0O0O0000OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O0OO0O00O ),'signstring':O0O0O0O0O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOO00OOOO0O00OO0O =requests .request ('get',f'{host}/user',headers =OO0OOOO0OOO00OO0O ).json ()#line:584
            if 'status'in OOO00OOOO0O00OO0O :#line:585
                if OOO00OOOO0O00OO0O ['status']==200 :#line:586
                    if float (OO0O0O0000OOOOO0O .doneeNo )!=0 :#line:587
                        O0O000000OO00OO0O =OOO00OOOO0O00OO0O ['data']['assets']['gold']#line:588
                        if float (O0O000000OO00OO0O )>float (OO0O0O0000OOOOO0O .innerId ):#line:589
                            O0O00OO000O0OO000 =int (float (O0O000000OO00OO0O )/1.1 )#line:590
                            O0O0O0O0O0OO0O00O =f'_doneeNo={OO0O0O0000OOOOO0O.doneeNo}&quantity={O0O00OO000O0OO000}_{timi_new()}'#line:591
                            OO0OOOO0OOO00OO0O ={'source':'scsc','authorization':OO0O0O0000OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O0OO0O00O ),'signstring':O0O0O0O0O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O000O0OO00OO0O00O ={"quantity":O0O00OO000O0OO000 ,"doneeNo":OO0O0O0000OOOOO0O .doneeNo }#line:606
                            O0OO00OOOO0O0OOOO =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OOOO0OOO00OO0O ,data =O000O0OO00OO0O00O ).json ()#line:607
                            if 'status'in O0OO00OOOO0O0OOOO :#line:609
                                if O0OO00OOOO0O0OOOO ['status']==200 :#line:610
                                    if O0OO00OOOO0O0OOOO ['data']:#line:611
                                        print (f'【赠送种子】:赠送{O0O00OO000O0OO000}种子给{OO0O0O0000OOOOO0O.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OOO0OO0OO00O0OOO0 :#line:615
            print (OOO0OO0OO00O0OOO0 )#line:616
    def invitation (O0OO000000OO0O000 ):#line:618
        try :#line:619
            _OOOO0OOO000OOOOOO =float (bundled_def ())/4 #line:620
            O0O0OOO0OOOO0OOOO =f'_innerId={int(_OOOO0OOO000OOOOOO)}_{timi_new()}'#line:622
            OOOO00OO000OO00O0 ={'source':'scsc','authorization':O0OO000000OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0OOOO0OOOO ),'signstring':O0O0OOO0OOOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            OO00O0OOOO00OO000 ={"innerId":int (_OOOO0OOO000OOOOOO )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00OO000OO00O0 ,data =OO00O0OOOO00OO000 )#line:635
        except Exception as O000OO0O0OO0OOO0O :#line:636
            print (O000OO0O0OO0OOO0O )#line:637
    def winning_rewards (OOO0OO00000O00OO0 ):#line:640
        try :#line:641
            OOOO0000O0OO0OO00 =f'__{timi_new()}'#line:642
            O0OOOO000OO0000O0 ={'source':'scsc','authorization':OOO0OO00000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O0OO0OO00 ),'signstring':OOOO0000O0OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OO0O00O000OOOO000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOO000OO0000O0 ).json ()#line:654
            if 'status'in OO0O00O000OOOO000 :#line:656
                if OO0O00O000OOOO000 ['status']==200 :#line:657
                    if OO0O00O000OOOO000 ['data']['amount']:#line:658
                        O0OO000OOOO000O0O =OO0O00O000OOOO000 ['data']['amount']['gold']#line:659
                        return O0OO000OOOO000O0O #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOOOOO0OOO0000OO0 :#line:663
            print (OOOOOO0OOO0000OO0 )#line:664
    def certification (O0O000OOOOOOOO000 ):#line:667
        try :#line:668
            O0OOOOOO00OOO000O =f'__{timi_new()}'#line:669
            O0O00O0O0000OO00O ={'source':'scsc','authorization':O0O000OOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO00OOO000O ),'signstring':O0OOOOOO00OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            OOO00000OO0OO00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O00O0O0000OO00O ).json ()#line:681
            if 'status'in OOO00000OO0OO00O0 :#line:683
                if OOO00000OO0OO00O0 ['status']==200 :#line:684
                    if OOO00000OO0OO00O0 ['data']['result']:#line:685
                        OO0OO0OOOOOOOOOOO =OOO00000OO0OO00O0 ['data']['nick_name']#line:686
                        return OO0OO0OOOOOOOOOOO #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0OOOO00OOO0O000O :#line:690
            print (O0OOOO00OOO0O000O )#line:691
    def crops_illustrated (O0000O0O000000000 ):#line:694
        try :#line:695
            O0OOOOO0O00OOO0OO =f'__{timi_new()}'#line:696
            OOO00O0000000O0OO ={'source':'scsc','authorization':O0000O0O000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O00OOO0OO ),'signstring':O0OOOOO0O00OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O0000O0000OOOO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO00O0000000O0OO ).json ()#line:708
            if 'status'in O0000O0000OOOO0OO :#line:710
                if O0000O0000OOOO0OO ['status']==200 :#line:711
                    O00OOOO0000OO000O =O0000O0000OOOO0OO ['data'][0 ]['crops']#line:712
                    for OO00O00O00OOOOOOO in O00OOOO0000OO000O :#line:713
                        if OO00O00O00OOOOOOO ['ill_clover_award']:#line:714
                            if float (OO00O00O00OOOOOOO ['ill_clover_award'])>1 :#line:715
                                if OO00O00O00OOOOOOO ['is_finish']:#line:716
                                    if not OO00O00O00OOOOOOO ['is_getit']:#line:717
                                        if O0000O0O000000000 .certification ()!='未实名':#line:718
                                            O0OOOOO0O00OOO0OO =f'_award_level={OO00O00O00OOOOOOO["level"]}_{timi_new()}'#line:719
                                            OOO00O0000000O0OO ={'source':'scsc','authorization':O0000O0O000000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O00OOO0OO ),'signstring':O0OOOOO0O00OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0OO0O00OOO000000 ={"award_level":OO00O00O00OOOOOOO ['level']}#line:731
                                            OOOOO00O0O0000OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO00O0000000O0OO ,json =O0OO0O00OOO000000 ).json ()#line:733
                                            if 'status'in OOOOO00O0O0000OO0 :#line:734
                                                if OOOOO00O0O0000OO0 ['status']==200 :#line:735
                                                    OOO0OO0O00OOOO0OO =OOOOO00O0O0000OO0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{OO00O00O00OOOOOOO["crop_name"]}成就丨奖励{OOO0OO0O00OOOO0OO}☘️')#line:738
                                                if OOOOO00O0O0000OO0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OOOOO00O0O0000OO0["message"]}')#line:740
        except Exception as OOOO0OO00OO00O000 :#line:741
            print (OOOO0OO00OO00O000 )#line:742
    def watched_ad (OO0OOO0OO0OO0O0OO ):#line:745
        try :#line:746
            O0OOO000OOOO0OOOO =f'__{timi_new()}'#line:747
            OOO000OOOO0OO0000 ={'source':'scsc','authorization':OO0OOO0OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000OOOO0OOOO ),'signstring':O0OOO000OOOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            O000000OO0O00000O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOOO0OO0000 ).json ()#line:759
            if 'status'in O000000OO0O00000O :#line:761
                if O000000OO0O00000O ['status']==200 :#line:762
                    if 'offlineInfo'in O000000OO0O00000O ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OO0O00O0O00OOOOO0 =O000000OO0O00000O ['data']['offlineInfo']['off_minute']#line:765
                        O000000O0OOOOO0O0 =float (O000000OO0O00000O ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OOOO0OO0000 ).json ()#line:768
                        time .sleep (2 )#line:769
                        O0O000OO0O00OO000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOOO0OO0000 ).json ()#line:770
                        if 'status'in O0O000OO0O00OO000 :#line:772
                            if O0O000OO0O00OO000 ['status']==200 :#line:773
                                OO0O0O00O00OOOOOO =float (O0O000OO0O00OO000 ['data']['silver'])/1000000000000 #line:774
                                OOOOOO0000OOO0000 =str (OO0O0O00O00OOOOOO -O000000O0OOOOO0O0 )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OO0O00O0O00OOOOO0}分钟奖励🌱数量:{OOOOOO0000OOO0000}t粒')#line:776
        except Exception as O0O000OO0O0OO0O0O :#line:777
            print (O0O000OO0O0OO0O0O )#line:778
    def user_ad (OO0O0OOO00OOOO0OO ):#line:781
        try :#line:782
            O000O0000OOOO0O0O =f'__{timi_new()}'#line:783
            OO000000OOO0OOOO0 ={'source':'scsc','authorization':OO0O0OOO00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000OOOO0O0O ),'signstring':O000O0000OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            OO000O0OO0O0O0O0O =requests .request ('get',f'{host}/user/ad',headers =OO000000OOO0OOOO0 ).json ()#line:795
            if 'status'in OO000O0OO0O0O0O0O :#line:797
                if OO000O0OO0O0O0O0O ['status']==200 :#line:798
                    OOOOO0O0OOOOO0O0O =OO000O0OO0O0O0O0O ['data']['max_time']#line:799
                    OO00O0OOO0OOO0OO0 =OO000O0OO0O0O0O0O ['data']['watch_time']#line:800
                    O0OO0OOOO0O0O0O00 =OO000O0OO0O0O0O0O ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O0OO0OOOO0O0O0O00 + OOOOO0O0OOOOO0O0O - OO00O0OOO0OOO0OO0}次丨好友提供:{O0OO0OOOO0O0O0O00}次')#line:802
                    if O0OO0OOOO0O0O0O00 +OOOOO0O0OOOOO0O0O -OO00O0OOO0OOO0OO0 >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OOOOO00000OOOOOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000000OOO0OOOO0 ).json ()#line:805
                        if 'status'in OOOOO00000OOOOOO0 :#line:807
                            if OOOOO00000OOOOOO0 ['status']==200 :#line:808
                                OOOO00O00O0OOO00O =float (OOOOO00000OOOOOO0 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OOOO00O00O0OOO00O)}t粒')#line:810
                                return True #line:811
                            if OOOOO00000OOOOOO0 ['status']==500 :#line:812
                                OO0OOOO0O0OOOO0OO =OOOOO00000OOOOOO0 ['message']#line:813
                                print (f'【获取种子】:{OO0OOOO0O0OOOO0OO}')#line:814
                                return False #line:815
        except Exception as O0O0O0OO00OO0O00O :#line:816
            print (O0O0O0OO00OO0O00O )#line:817
    def synthetic (OO00OO0OOOOO0OO00 ):#line:820
        global id ,g #line:821
        try :#line:822
            OOOOO0O0OOO00O000 =OO00OO0OOOOO0OO00 .level_new ()#line:823
            OO0O00OO0O00O0O0O =random .randint (9 ,11 )#line:824
            O0000OO0O000OOO00 =f'_site=8&targetSite={OO0O00OO0O00O0O0O}_{timi_new()}'#line:825
            O00OO0O00OOO0O0O0 ={'source':'scsc','authorization':OO00OO0OOOOO0OO00 .token ,'timestamp':timi_new (),'sign':sign (O0000OO0O000OOO00 ),'signstring':O0000OO0O000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OO0O0OO0OO00OO0O0 ={"site":int (8 ),"targetSite":int (OO0O00OO0O00O0O0O )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O00OOO0O0O0 ,json =OO0O0OO0OO00OO0O0 )#line:838
            while True :#line:839
                O00OO0000OOOOO00O =f'__{timi_new()}'#line:840
                OOOOO00O0O00O0OO0 ={'source':'scsc','authorization':OO00OO0OOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000OOOOO00O ),'signstring':O00OO0000OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                OOOO00000O00OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO00O0O00O0OO0 ).json ()#line:852
                if 'status'in OOOO00000O00OOOOO :#line:854
                    if OOOO00000O00OOOOO ['status']==200 :#line:855
                        OOO00O0000O00OO00 =OOOO00000O00OOOOO ['data']['cropList']#line:856
                        OO00O000000O0OO00 =OOOO00000O00OOOOO ['data']['gameCoreDataDBid']#line:857
                        OOOOO00O00O0OOO0O =float (OOOO00000O00OOOOO ['data']['silver'])/1000000000000 #line:858
                        O0O000O0O00OO00OO =0 #line:863
                        for O0OO0000000OO0000 in OOO00O0000O00OO00 :#line:864
                            if not O0OO0000000OO0000 :#line:865
                                OOO0OOOO00000OOO0 =f'_crop_id={OO00O000000O0OO00}&site={O0O000O0O00OO00OO}_{OO00OO0OOOOO0OO00.time}'#line:866
                                OO000000O00O0OOOO ={'source':'scsc','authorization':OO00OO0OOOOO0OO00 .token ,'timestamp':OO00OO0OOOOO0OO00 .time ,'sign':sign (OOO0OOOO00000OOO0 ),'signstring':OOO0OOOO00000OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                OOO00OOO000OOO0O0 ={"site":O0O000O0O00OO00OO ,"crop_id":OO00O000000O0OO00 }#line:877
                                OOO0OO00O000OO00O =requests .request ('post',f'{host}/game/crops/buy',headers =OO000000O00O0OOOO ,data =OOO00OOO000OOO0O0 ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOO0OO00O000OO00O :#line:881
                                    if OOO0OO00O000OO00O ['status']==200 :#line:882
                                        if OOO0OO00O000OO00O ['message']=='种子数量不足':#line:883
                                            OOOOO0O0OOO00O000 =OO00OO0OOOOO0OO00 .level_new ()#line:884
                                            print (f'【种植合成】:{OOO0OO00O000OO00O["message"]}')#line:885
                                            if not OO00OO0OOOOO0OO00 .user_ad ():#line:886
                                                return False #line:887
                                    if OOO0OO00O000OO00O ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOO0OO00O000OO00O["message"]}')#line:889
                                        return False #line:890
                            O0O000O0O00OO00OO +=1 #line:891
                        OOOO0OOO0O00O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO00O0O00O0OO0 ).json ()#line:892
                        O0OO00O0000OO0O0O =OOOO0OOO0O00O0O0O ['data']['cropList']#line:893
                        OO00000000OOO00OO =False #line:894
                        for O0OO0000000OO0000 in range (12 ):#line:895
                            id =O0OO00O0000OO0O0O [O0OO0000000OO0000 ]['level']#line:896
                            if float (OOOOO0O0OOO00O000 )-float (id )>9 :#line:897
                                OOOOOO0OOOO00OO00 =f'_site={O0OO0000000OO0000}_{timi_new()}'#line:898
                                O0OO0OO0O0OOOO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00OO0OOOOO0OO00 .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0OOOO00OO00 ),'signstring':OOOOOO0OOOO00OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                OOOO0OOOO0OO0O00O ={"site":O0OO0000000OO0000 }#line:910
                                OO0000OO000O0OO0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO0OO0O0OOOO0OO ,data =OOOO0OOOO0OO0O00O ).json ()#line:912
                                if 'status'in OO0000OO000O0OO0O :#line:913
                                    if OO0000OO000O0OO0O ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OO00OOO0O0OO0O0OO in range (11 ):#line:917
                                    OO00O0OO000000OO0 =OO00OOO0O0OO0O0OO +1 #line:918
                                    g =O0OO00O0000OO0O0O [OO00O0OO000000OO0 ]['level']#line:919
                                    if id ==g :#line:920
                                        OO00O00O0000O0O0O =OO00OOO0O0OO0O0OO +2 #line:921
                                        if OO00O00O0000O0O0O !=O0OO0000000OO0000 +1 :#line:922
                                            OO00OOO0OOO0OOO0O =O0OO0000000OO0000 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O0000OO0O000OOO00 =f'_site={OO00OOO0OOO0OOO0O - 1}&targetSite={OO00O00O0000O0O0O - 1}_{timi_new()}'#line:926
                                            O00OO0O00OOO0O0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00OO0OOOOO0OO00 .token ,'timestamp':timi_new (),'sign':sign (O0000OO0O000OOO00 ),'signstring':O0000OO0O000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            O0O0OO0O00OO000OO ={"site":int (OO00OOO0OOO0OOO0O -1 ),"targetSite":int (OO00O00O0000O0O0O -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O00OOO0O0O0 ,json =O0O0OO0O00OO000OO )#line:945
                                            OO00000000OOO00OO =True #line:947
                                    if OO00000000OOO00OO :#line:948
                                        break #line:949
                                if OO00000000OOO00OO :#line:950
                                    break #line:951
        except :#line:952
            OO00OO0OOOOO0OO00 .synthetic ()#line:953
    def level_new (O00OO00O0OOOO0OOO ):#line:956
        try :#line:957
            OO0OO0OOOOO0000OO =f'__{timi_new()}'#line:958
            O0O0OO0OO00OO00OO ={'source':'scsc','authorization':O00OO00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOOOO0000OO ),'signstring':OO0OO0OOOOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O0O0O00O0O0O0O0OO =requests .request ('get',f'{host}/user',headers =O0O0OO0OO00OO00OO ).json ()#line:970
            if 'status'in O0O0O00O0O0O0O0OO :#line:971
                if O0O0O00O0O0O0O0OO ['status']==200 :#line:972
                    return float (O0O0O00O0O0O0O0OO ['data']['level'])#line:973
        except Exception as O0O000OOOO0O0O000 :#line:974
            print (O0O000OOOO0O0O000 )#line:975
    def propsraffle (OO00OO00O0000O000 ):#line:978
        try :#line:979
            while True :#line:980
                O0OO00OOO0000O0OO =f'__{timi_new()}'#line:981
                OOOOOO000OOOO0OOO ={'source':'scsc','authorization':OO00OO00O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOO0000O0OO ),'signstring':O0OO00OOO0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                O00O00O00OO0O0OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOOOO000OOOO0OOO ).json ()#line:993
                if 'status'in O00O00O00OO0O0OOO :#line:995
                    if O00O00O00OO0O0OOO ['status']==200 :#line:996
                        O0OO000O00O00000O =O00O00O00OO0O0OOO ['data']['rows']#line:997
                        O0O0OO0OOOO0O000O =O00O00O00OO0O0OOO ['data']['vstate']#line:998
                        if O0OO000O00O00000O ==5 or O0OO000O00O00000O ==6 or O0OO000O00O00000O ==7 :#line:999
                            O0O0OOOOOOOOO0OOO =O00O00O00OO0O0OOO ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O0O0OOOOOOOOO0OOO}')#line:1001
                        if O0OO000O00O00000O ==1 or O0OO000O00O00000O ==2 or O0OO000O00O00000O ==3 :#line:1002
                            OOOOOO00OOOOOOO0O =O00O00O00OO0O0OOO ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{OOOOOO00OOOOOOO0O}')#line:1004
                        if O0OO000O00O00000O ==4 or O0OO000O00O00000O ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if O0OO000O00O00000O =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OOOOO00OOOO00O0OO :#line:1046
            print (OOOOO00OOOO00O0OO )#line:1047
    def friends_invitation (OO00O0OO000O00O0O ):#line:1050
        try :#line:1051
            O0OOO0000OOOOOOOO =f'__{timi_new()}'#line:1052
            OOO0O0OOO0OO000O0 ={'source':'scsc','authorization':OO00O0OO000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOOOOOOO ),'signstring':O0OOO0000OOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O000O0O0O000O0OOO =requests .request ('get',f'{host}/friends',headers =OOO0O0OOO0OO000O0 ).json ()#line:1064
            if 'status'in O000O0O0O000O0OOO :#line:1065
                if O000O0O0O000O0OOO ['status']==200 :#line:1066
                    O0000OOO000OO00OO =O000O0O0O000O0OOO ['data']['myInviteter']#line:1067
                    if O0000OOO000OO00OO :#line:1068
                        OO0OO00OOO0O0O00O =O0000OOO000OO00OO ['user']['nickname']#line:1069
                        OOOOO0O0OO00OOO0O =OO00O0OO000O00O0O .certification ()#line:1070
                        if OOOOO0O0OO00OOO0O =='未实名':#line:1071
                            weishim .append (OO00O0OO000O00O0O .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{OO0OO00OOO0O0O00O}丨实名:{OOOOO0O0OO00OOO0O}')#line:1073
        except Exception as O0OOOO0O000OOO0OO :#line:1077
            print (O0OOOO0O000OOO0OO )#line:1078
    def add_clover (OO00O0OO000000O0O ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O00O000000O0O0000 =f'__{timi_new()}'#line:1084
            O00O0OO0O0OO0000O ={'source':'scsc','authorization':OO00O0OO000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000000O0O0000 ),'signstring':O00O000000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO00OO00OOOO0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0OO0O0OO0000O ).json ()#line:1096
            if 'status'in OO00OO00OOOO0O0O0 :#line:1098
                if OO00OO00OOOO0O0O0 ['status']==200 :#line:1099
                    OO0O00O0O0OO0O000 =OO00OO00OOOO0O0O0 ['data']['clover']#line:1100
                    O00O0OOOOOOO00OOO =OO00OO00OOOO0O0O0 ['data']['used_clover']#line:1101
                    OOO00O0OO0O000000 =float (OO0O00O0O0OO0O000 )-float (O00O0OOOOOOO00OOO )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00O0OOOOOOO00OOO}')#line:1103
                    if OO00O0OO000000O0O .certification ()!='未实名':#line:1104
                        if OOO00O0OO0O000000 >1 :#line:1105
                            O00O000000O0O0000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO00O0OO0O000000)}_{timi_new()}'#line:1106
                            OOO0O0O000O0O0000 ={'source':'scsc','authorization':OO00O0OO000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000000O0O0000 ),'signstring':O00O000000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            O0OO000OO0OOO0OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO00O0OO0O000000 )}#line:1118
                            O0OO0OO0000OO00OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0O0O000O0O0000 ,data =O0OO000OO0OOO0OO0 ).json ()#line:1119
                            if 'status'in O0OO0OO0000OO00OO :#line:1121
                                if O0OO0OO0000OO00OO ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO0000OO00OO["data"]["isSuccess"]}丨数量:{OOO00O0OO0O000000}')#line:1123
                                if O0OO0OO0000OO00OO ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO0000OO00OO["message"]}')#line:1125
            O00O0000000OOOO00 =requests .request ('get',f'{host}/lottery',headers =O00O0OO0O0OO0000O ).json ()#line:1126
            O00O0O000O00O00OO =OO00O0OO000000O0O .winning_rewards ()#line:1128
            if 'status'in O00O0000000OOOO00 :#line:1129
                if O00O0000000OOOO00 ['status']==200 :#line:1130
                    OOO0O0O0000OOO0OO =O00O0000000OOOO00 ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OOO0O0O0000OOO0OO )#line:1132
                    OOO00O0000O0OOOOO =O00O0000000OOOO00 ['data'][1 ]['value']#line:1133
                    OOO00O000OO00OO00 =O00O0000000OOOO00 ['data'][0 ]['join_number']#line:1134
                    OO0OOOO00OO0000OO =int (float (O00O0000000OOOO00 ['data'][0 ]['totalValue']))#line:1135
                    OOOOOOO000OOOOOOO =float (OOO00O0000O0OOOOO /OO0OOOO00OO0000OO )*10000 #line:1136
                    OOO00O00000O00OO0 =OO0OOOO00OO0000OO /OOO00O000OO00OO00 #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OOO0O0O0000OOO0OO)[:6]}颗金种子丨好友收益:{str(O00O0O000O00O00OO)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOOOO000OOOOOOO)[:6]}颗金种子丨☘️人均:{str(OOO00O00000O00OO0)[:7]}️')#line:1139
        except Exception as O000000OO000OOO0O :#line:1140
            print (O000000OO000OOO0O )#line:1141
    def energy (O0O00OOOO00O0OOOO ):#line:1144
        try :#line:1145
            while True :#line:1146
                O00OO0O0O0OO00000 =f'__{timi_new()}'#line:1147
                OO00OOO00000000O0 ={'source':'scsc','authorization':O0O00OOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0OO00000 ),'signstring':O00OO0O0O0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OO000OOOO000O000O =requests .request ('get',f'{host}/energy/general',headers =OO00OOO00000000O0 ).json ()#line:1159
                if 'status'in OO000OOOO000O000O :#line:1161
                    if OO000OOOO000O000O ['status']==200 :#line:1162
                        O00O0O00OOO0O000O =OO000OOOO000O000O ['data']['ordinary_water']#line:1163
                        O0O00O0000OO0OO0O =OO000OOOO000O000O ['data']['ordinary_fertilizer']#line:1164
                        O00OOO0O0OOOO0000 =OO000OOOO000O000O ['data']['videoStatus']#line:1165
                        OO00O00O0000OO0OO =OO000OOOO000O000O ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0O00O0000OO0OO0O).split(".")[0]}丨水滴:{str(O00O0O00OOO0O000O).split(".")[0]}')#line:1168
                        if float (O0O00O0000OO0OO0O )<96 :#line:1169
                            if O00OOO0O0OOOO0000 :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OO0OO0O0OO0OO000O =99 -float (O0O00O0000OO0OO0O )#line:1172
                                O00OOOO0OO0OO00OO ={"fertilizer":str (OO0OO0O0OO0OO000O ).split ('.')[0 ]}#line:1173
                                OO00000O0O000OOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00OOO00000000O0 ).json ()#line:1175
                                if 'status'in OO00000O0O000OOO0 :#line:1177
                                    if OO00000O0O000OOO0 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{OO00000O0O000OOO0["message"]}')#line:1179
                                    if OO00000O0O000OOO0 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OO00000O0O000OOO0["message"]}')#line:1181
                                        break #line:1182
                                if float (O0O00O0000OO0OO0O )<78 :#line:1184
                                    OO0OO0O0OO0OO000O =80 -float (O0O00O0000OO0OO0O )#line:1185
                                    OOO0OOOOO000OOO00 =f'_fertilizer={int(OO0OO0O0OO0OO000O)}_{timi_new()}'#line:1186
                                    OOO0OOO0000000OOO ={'source':'scsc','authorization':O0O00OOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO000OOO00 ),'signstring':OOO0OOOOO000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    OO000000O00000O0O ={"fertilizer":int (OO0OO0O0OO0OO000O )}#line:1198
                                    O0OO000OOO0OO0O00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0OOO0000000OOO ,data =OO000000O00000O0O ).json ()#line:1200
                                    if 'status'in O0OO000OOO0OO0O00 :#line:1202
                                        if O0OO000OOO0OO0O00 ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{O0OO000OOO0OO0O00["message"]}丨数量:{int(OO0OO0O0OO0OO000O)}')#line:1204
                                        if O0OO000OOO0OO0O00 ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{O0OO000OOO0OO0O00["message"]}丨数量:{int(OO0OO0O0OO0OO000O)}')#line:1206
                                            OO00O0OO0000O000O =O0OO000OOO0OO0O00 ["message"].split ('-')[1 ]#line:1207
                                            OO00O00OO0000OO00 =f'__{timi_new()}'#line:1208
                                            OOOO000O0OO0000OO ={'source':'scsc','authorization':O0O00OOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0000OO00 ),'signstring':OO00O00OO0000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            O000OOOOO0O00O0O0 =requests .request ('get',f'{host}/user',headers =OOOO000O0OO0000OO ).json ()#line:1220
                                            if 'status'in O000OOOOO0O00O0O0 :#line:1221
                                                if O000OOOOO0O00O0O0 ['status']==200 :#line:1222
                                                    OOO0OO0OOO00O0OOO =O000OOOOO0O00O0O0 ['data']['inner_id']#line:1223
                                                    if give_gold (OOO0OO0OOO00O0OOO ,float (OO00O0OO0000O000O )+1 ):#line:1224
                                                        O0O00OOOO00O0OOOO .energy ()#line:1225
                        if float (O00O0O00OOO0O000O )<880 :#line:1226
                            if OO00O00O0000OO0OO :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                O00O0O00OOO0O00OO =999 -float (O00O0O00OOO0O000O )#line:1229
                                OOO0OOO000OOOOO00 ={"water":str (O00O0O00OOO0O00OO ).split ('.')[0 ]}#line:1230
                                OO000OO0O0O0O000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00OOO00000000O0 ).json ()#line:1232
                                if 'status'in OO000OO0O0O0O000O :#line:1234
                                    if OO000OO0O0O0O000O ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{OO000OO0O0O0O000O["message"]}')#line:1236
                                    if OO000OO0O0O0O000O ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OO000OO0O0O0O000O["message"]}')#line:1238
                                        break #line:1239
                                if float (O00O0O00OOO0O000O )<780 :#line:1240
                                    O00O0O00OOO0O00OO =800 -float (O00O0O00OOO0O000O )#line:1241
                                    O0OOOO0OO0O00000O =f'_water={int(O00O0O00OOO0O00OO)}_{timi_new()}'#line:1242
                                    O0O0O00O0O0O00000 ={'source':'scsc','authorization':O0O00OOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OO0O00000O ),'signstring':O0OOOO0OO0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    OOOOO00000000O00O ={"water":int (O00O0O00OOO0O00OO )}#line:1254
                                    OO00OO0O0O0O00OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0O00O0O0O00000 ,data =OOOOO00000000O00O ).json ()#line:1256
                                    if 'status'in OO00OO0O0O0O00OO0 :#line:1258
                                        if OO00OO0O0O0O00OO0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{OO00OO0O0O0O00OO0["message"]}丨数量:{int(O00O0O00OOO0O00OO)}')#line:1260
                                        if OO00OO0O0O0O00OO0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{OO00OO0O0O0O00OO0["message"]}丨数量:{int(O00O0O00OOO0O00OO)}')#line:1262
                                            OO00O0OO0000O000O =OO00OO0O0O0O00OO0 ["message"].split ('-')[1 ]#line:1263
                                            OO00O00OO0000OO00 =f'__{timi_new()}'#line:1264
                                            OOOO000O0OO0000OO ={'source':'scsc','authorization':O0O00OOOO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0000OO00 ),'signstring':OO00O00OO0000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            O000OOOOO0O00O0O0 =requests .request ('get',f'{host}/user',headers =OOOO000O0OO0000OO ).json ()#line:1276
                                            if 'status'in O000OOOOO0O00O0O0 :#line:1277
                                                if O000OOOOO0O00O0O0 ['status']==200 :#line:1278
                                                    OOO0OO0OOO00O0OOO =O000OOOOO0O00O0O0 ['data']['inner_id']#line:1279
                                                    if give_gold (OOO0OO0OOO00O0OOO ,float (OO00O0OO0000O000O )+1 ):#line:1280
                                                        O0O00OOOO00O0OOOO .energy ()#line:1281
                        break #line:1282
        except Exception as O0OOO0OOO00O00000 :#line:1283
            print (O0OOO0OOO00O00000 )#line:1284
def bundled_def ():#line:1287
    OOO0000000000OO00 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OOO0000000000OO00 [random .randint (0 ,len (OOO0000000000OO00 )-1 )]#line:1289
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
        O0OO00OO0OOOO0O00 =gitee_edition ()#line:1328
        if version_of_the_validation ()<O0OO00OO0OOOO0O00 ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OO0OOOO0O00["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O0OO00OO0OOOO0O00["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OO0OOOO0O00["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O0OO00OO0OOOO0O00["CityEarth"]["content"]}')#line:1334
    except Exception as OOOO0000O00000O0O :#line:1335
        print (OOOO0000O00000O0O )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
