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
        O0OO0O000O000OOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OO0O000O000OOO0)}个账号==========")#line:17
        for OOO0OO00O00O00OO0 in O0OO0O000O000OOO0 :#line:18
            OOO0000000OOOOOOO =[]#line:19
            print (f"------------正在执行第{O0OO0O000O000OOO0.index(OOO0OO00O00O00OO0) + 1}个账号------------")#line:20
            O0O0OOO000OO00OOO =CityEarth (OOO0OO00O00O00OO0 ,OOO0000000OOOOOOO ,O0OO0O000O000OOO0 .index (OOO0OO00O00O00OO0 ))#line:21
            def OOO00OO000OOO0O00 ():#line:23
                if O0O0OOO000OO00OOO .base_info ():#line:25
                    O0O0OOO000OO00OOO .sealing ()#line:27
                    O0O0OOO000OO00OOO .invitenum ()#line:29
                    O0O0OOO000OO00OOO .query_to_sell ()#line:31
                    O0O0OOO000OO00OOO .friends_invitation ()#line:35
                    O0O0OOO000OO00OOO .energy ()#line:37
                    O0O0OOO000OO00OOO .add_clover ()#line:39
                    O0O0OOO000OO00OOO .propsraffle ()#line:41
                    O0O0OOO000OO00OOO .synthetic ()#line:43
                    O0O0OOO000OO00OOO .crops_illustrated ()#line:45
                    O0O0OOO000OO00OOO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0O0OOO000OO00OOO .give_gold ()#line:50
            OO000000O0OOOOO0O =threading .Thread (target =OOO00OO000OOO0O00 )#line:52
            OO000000O0OOOOO0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO000O0OOOOOOO0O0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO000O0OOOOOOO0O0 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O0OO00OO00OOO00 in invited_new :#line:62
            print (O0O0OO00OO00OOO00 )#line:63
        print ('开始打印未实名的token')#line:64
        for O000O0O0OOOO00O00 in weishim :#line:65
            print (O000O0O0OOOO00O00 )#line:66
    except Exception as OOO0OOOOO0000OOO0 :#line:67
        print (OOO0OOOOO0000OOO0 )#line:68
def give_gold (O0O00O0OO000O00O0 ,O00OOO0OOO0O0000O ):#line:72
    try :#line:73
        O0O00O00OOO0OOO00 =f'_doneeNo={O0O00O0OO000O00O0}&quantity={int(O00OOO0OOO0O0000O)}_{timi_new()}'#line:74
        OOOOO0000O0O0OOOO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O00O00OOO0OOO00 ),'signstring':O0O00O00OOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O000O0O0O00O00OO0 ={"quantity":int (O00OOO0OOO0O0000O ),"doneeNo":O0O00O0OO000O00O0 }#line:89
        OO00O000OO000O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO0000O0O0OOOO ,data =O000O0O0O00O00OO0 ).json ()#line:90
        if 'status'in OO00O000OO000O0O0 :#line:92
            if OO00O000OO000O0O0 ['status']==200 :#line:93
                if OO00O000OO000O0O0 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00OOO0OOO0O0000O)}种子给{O0O00O0OO000O00O0}成功')#line:95
                    return True #line:96
            if OO00O000OO000O0O0 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO00O000OO000O0O0["message"]}')#line:98
                return False #line:99
            if OO00O000OO000O0O0 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO00O000OO000O0O0["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO00O00O0OOO0O00 :#line:104
        print (OOO00O00O0OOO0O00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OOOOOO00O00OOOO ):#line:115
    OOO00OOO0OOO0OOO0 =hashlib .md5 (O0OOOOOO00O00OOOO .encode ()).hexdigest ()#line:116
    OO0O00OO0OO00000O =sc1 ()#line:117
    O00OO0O000000O000 =sc2 ()#line:118
    OO00000O0O0O0O000 =sc3 ()#line:119
    OOOO0OOOO0O000O00 =OO0O00OO0OO00000O +OOO00OOO0OOO0OOO0 +O00OO0O000000O000 +OO00000O0O0O0O000 #line:120
    O00OOO0OOO00O0OO0 =hashlib .md5 (OOOO0OOOO0O000O00 .encode ()).hexdigest ()#line:121
    return O00OOO0OOO00O0OO0 #line:122
def format_msg ():#line:125
    OO0OOO000O0OOOO00 =""#line:126
    for O0000OO0000OO00O0 in msg_list :#line:127
        OO0OOO000O0OOOO00 +=str (O0000OO0000OO00O0 )+"\r\n"#line:128
    return OO0OOO000O0OOOO00 #line:129
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
def get_json_data (O000OOO0OOO00O0O0 ,OO0OO0O00O000OO00 ,OO00O0O0O0O000O00 ,OOO0O000OO0OO0O00 ):#line:153
    with open (O000OOO0OOO00O0O0 ,'rb')as O00O00O0O00O0000O :#line:154
        O000000OO0O0O0OO0 =json .load (O00O00O0O00O0000O )#line:155
        O000000OO0O0O0OO0 ['data'][OO0OO0O00O000OO00 ][OO00O0O0O0O000O00 ]=OOO0O000OO0OO0O00 #line:156
        O00O0000OOOO0O0OO =O000000OO0O0O0OO0 #line:157
    O00O00O0O00O0000O .close ()#line:158
    return O00O0000OOOO0O0OO #line:159
def write_json_data (O000OO000OO00OOOO ):#line:162
    with open (json_path1 ,'w')as O00O0000000O00OO0 :#line:163
        json .dump (O000OO000OO00OOOO ,O00O0000000O00OO0 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O00O0000000O00OO0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OOO0O00000O000000 ,O00000O00OOOO0O00 ,O0OOOOO00OO0O00OO ,O0O0000OOOO000O0O ):#line:171
        try :#line:172
            OOO0O00000O000000 .msg =O0OOOOO00OO0O00OO #line:173
            OOO0O00000O000000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OOO0O00000O000000 .token =O00000O00OOOO0O00 ['authorization']#line:175
            OOO0O00000O000000 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OOO0O00000O000000 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OOO0O00000O000000 .elephant_user =O00000O00OOOO0O00 ['elephant_user']#line:178
            OOO0O00000O000000 .elephant_pswd =O00000O00OOOO0O00 ['elephant_pswd']#line:179
            OOO0O00000O000000 .elephant_Task_ID =O00000O00OOOO0O00 ['elephant_Task_ID']#line:180
            OOO0O00000O000000 .len_new =O0O0000OOOO000O0O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0000OOOOO000000O ):#line:186
        try :#line:187
            O0000OOOOO000000O .watched_ad ()#line:189
            OOO0O0OO00OO0O0OO =f'__{timi_new()}'#line:190
            OO0O0000O0OO000O0 ={'source':'scsc','authorization':O0000OOOOO000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO00OO0O0OO ),'signstring':OOO0O0OO00OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0O0O000O0OO0OO00 =requests .request ('get',f'{host}/user',headers =OO0O0000O0OO000O0 ).json ()#line:202
            if 'status'in O0O0O000O0OO0OO00 :#line:204
                if O0O0O000O0OO0OO00 ['status']==200 :#line:205
                    OOOO00O000O00O00O =O0O0O000O0OO0OO00 ['data']['nickname']#line:206
                    OO000OO0O0OO0000O =O0O0O000O0OO0OO00 ['data']['inner_id']#line:207
                    OOO0OOO00O0OOO0O0 =O0O0O000O0OO0OO00 ['data']['assets']['gold']#line:208
                    OOOOOO00000OO00O0 =O0O0O000O0OO0OO00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOOO00O000O00O00O[:5]}丨ID:{OO000OO0O0OO0000O}丨等级:{OOOOOO00000OO00O0}丨金种子:{str(OOO0OOO00O0OOO0O0).split(".")[0]}')#line:211
                    if 'wx_'in OOOO00O000O00O00O :#line:212
                        O0000OOOOO000000O .change_nickname ()#line:213
                if O0O0O000O0OO0OO00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0000OOOOO000000O .elephant_user =='f':#line:216
                        return False #line:217
                    OO0O0O00OO0O00O0O =Invalid_login .addtask (elephant_user =O0000OOOOO000000O .elephant_user ,elephant_pswd =O0000OOOOO000000O .elephant_pswd ,elephant_Task_ID =O0000OOOOO000000O .elephant_Task_ID )#line:220
                    O000O000O0O00000O =get_json_data (json_path ,O0000OOOOO000000O .len_new ,'authorization',OO0O0O00OO0O00O0O )#line:221
                    if write_json_data (O000O000O0O00000O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0O0O000O0OO0OO00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO0OO0OO0OOOOO0OO :#line:228
            print (OO0OO0OO0OOOOO0OO )#line:229
    def sealing (O0O00OOOOOO00O00O ):#line:232
        try :#line:233
            O0O0O000OOO000000 =f'__{timi_new()}'#line:234
            OOOO00OOOOO0OO0O0 ={'source':'scsc','authorization':O0O00OOOOOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OOO000000 ),'signstring':O0O0O000OOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOO00OOOOO0OO0O0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOOO00OOOOO0OO0O0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOO00OOOOO0OO0O0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOO00OOOOO0OO0O0 )#line:249
            requests .request ('get',f'{host}/user',headers =OOOO00OOOOO0OO0O0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOO00OOOOO0OO0O0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOO00OOOOO0OO0O0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOO00OOOOO0OO0O0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OOOOO0OO0O0 )#line:254
            requests .request ('get',f'{host}/assets',headers =OOOO00OOOOO0OO0O0 )#line:255
        except Exception as OOO00O00O00OOOOO0 :#line:256
            print (OOO00O00O00OOOOO0 )#line:257
    def ddd (O00OOO00O00000OOO ):#line:259
        try :#line:260
            OO0OO00000OOO00OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0O00OO0OOOOO0O00 ={'source':'scsc','authorization':O00OOO00O00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000OOO00OO ),'signstring':OO0OO00000OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O00OO0OO0O0O00O0O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O00OO0OOOOO0O00 ).json ()#line:273
            print (O00OO0OO0O0O00O0O )#line:274
        except Exception as O00OOOO00OOO0OOO0 :#line:277
            print (O00OOOO00OOO0OOO0 )#line:278
    def the_query (O0O0O0O00OO0OO000 ):#line:283
        try :#line:284
            OOO0000OOO00O0O00 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O000O000OO0O000OO ={'authorization':O0O0O0O00OO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOO00O0O00 ),'signstring':OOO0000OOO00O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO000O000OO0000O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O000O000OO0O000OO ).json ()#line:296
            if 'status'in OO000O000OO0000O0 :#line:298
                if OO000O000OO0000O0 ['status']==200 :#line:299
                    return OO000O000OO0000O0 ['data']['rows'][4 ]['price']#line:300
        except Exception as O0OOO0OOOOOO0O000 :#line:301
            print (O0OOO0OOOOOO0O000 )#line:302
    def market_sale (O000O0OOO00O000OO ,OO00OOOOO00O0OO0O ):#line:305
        try :#line:306
            O00OO0000O0O0O0OO =timi_new ()#line:307
            O0OO0000O0OO0OO0O =f'type=crop__{O00OO0000O0O0O0OO}'#line:308
            OOO0O000O0OO0OO0O ={'source':'scsc','authorization':O000O0OOO00O000OO .token ,'timestamp':str (O00OO0000O0O0O0OO ),'sign':sign (O0OO0000O0OO0OO0O ),'signstring':O0OO0000O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OOO0OO00OOOO0OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOO0O000O0OO0OO0O ).json ()#line:320
            if 'status'in O0OOO0OO00OOOO0OO :#line:322
                if O0OOO0OO00OOOO0OO ['status']==200 :#line:323
                    if O0OOO0OO00OOOO0OO ['data']['rows']:#line:324
                        O00OOOO0O0OO00OO0 =O0OOO0OO00OOOO0OO ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0OO0O0OOO000000O =O0OOO0OO00OOOO0OO ['data']['rows'][0 ]['quantity']#line:326
                        if float (OO00OOOOO00O0OO0O )>9 :#line:327
                            O0O0OO00OO00O0O0O =f'_packsackItemId={O00OOOO0O0OO00OO0}&price={str(OO00OOOOO00O0OO0O)[:5]}&quantity={O0OO0O0OOO000000O}_{O00OO0000O0O0O0OO}'#line:328
                            O0O0000O00OOOOO00 ={'source':'scsc','authorization':O000O0OOO00O000OO .token ,'timestamp':str (O00OO0000O0O0O0OO ),'sign':sign (O0O0OO00OO00O0O0O ),'signstring':O0O0OO00OO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OO000000OOOO00000 ={"packsackItemId":O00OOOO0O0OO00OO0 ,"price":str (OO00OOOOO00O0OO0O )[:5 ],"quantity":str (O0OO0O0OOO000000O )}#line:344
                            O00O0000OOOOOO0O0 =requests .request ('post',f'{host}/market/sale',headers =O0O0000O00OOOOO00 ,data =OO000000OOOO00000 ).json ()#line:345
                            if 'status'in O00O0000OOOOOO0O0 :#line:347
                                if O00O0000OOOOOO0O0 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O0OO0O0OOO000000O}丨价格:{str(OO00OOOOO00O0OO0O)[:5]}')#line:349
                                if O00O0000OOOOOO0O0 ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O00O0000OOOOOO0O0["message"]}')#line:351
        except Exception as OOOO0O0OOO00OO0OO :#line:352
            print (OOOO0O0OOO00OO0OO )#line:353
    def query_to_sell (O0OOOOOO0OOO00OOO ):#line:356
        global count_list #line:357
        try :#line:358
            O0O0000OOOO0O000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            O00OO0OO0OOO0O00O ={'source':'scsc','authorization':O0OOOOOO0OOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOOO0O000O ),'signstring':O0O0000OOOO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            OOOO00O0OOOOO00O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OO0OO0OOO0O00O ).json ()#line:371
            if 'status'in OOOO00O0OOOOO00O0 :#line:373
                if OOOO00O0OOOOO00O0 ['status']==200 :#line:374
                    for OOO0000OOOO0OOOOO in OOOO00O0OOOOO00O0 ['data']['rows']:#line:375
                        OO000O000O0OOOOO0 =OOO0000OOOO0OOOOO ['materialKey']#line:376
                        O0OO0O0O000OOOOOO =OOO0000OOOO0OOOOO ['quantity']#line:377
                        OO00OOOOOO0O0OO00 =OOO0000OOOO0OOOOO ['price']#line:378
                        OOO0000O000000O0O =OOO0000OOOO0OOOOO ['saleState']#line:379
                        if OOO0000O000000O0O ==0 :#line:380
                            print (f'【出售订单】:名称:{OO000O000O0OOOOO0}丨数量:{O0OO0O0O000OOOOOO}丨价格:{OO00OOOOOO0O0OO00}')#line:381
                            count_list +=O0OO0O0O000OOOOOO #line:382
                            OOOO00000OOO0O0OO =O0OOOOOO0OOO00OOO .the_query ()#line:384
                            if float (OOOO00000OOO0O0OO )!=float (OO00OOOOOO0O0OO00 ):#line:385
                                OO000OO0O0O0OO0OO =OOO0000OOOO0OOOOO ['id']#line:386
                                if float (datetime .datetime .now ().hour )>8 :#line:387
                                    O0OOOOOO0OOO00OOO .cacel_sale (OO000OO0O0O0OO0OO )#line:388
                    O0OOOOOO0OOO00OOO .game_map ()#line:390
        except Exception as OOO0OOO00O00O00O0 :#line:392
            print (OOO0OOO00O00O00O0 )#line:393
    def cacel_sale (OO0O000OO00000OOO ,OOOO0O00OOO00000O ):#line:396
        try :#line:397
            O0O00OO00O00O0O0O =f'_saleId={OOOO0O00OOO00000O}_{timi_new()}'#line:398
            OOOO0O0OOO000000O ={'source':'scsc','authorization':OO0O000OO00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00O00O0O0O ),'signstring':O0O00OO00O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            OO0OOO00O000O0OO0 ={"saleId":OOOO0O00OOO00000O }#line:410
            OOO0O00OOOO00OOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOO0O0OOO000000O ,data =OO0OOO00O000O0OO0 ).json ()#line:411
            if 'status'in OOO0O00OOOO00OOOO :#line:413
                if OOO0O00OOOO00OOOO ['status']==200 :#line:414
                    print (f'【下架出售】:{OOO0O00OOOO00OOOO["data"]}')#line:415
        except Exception as OO0O0O0O00O000O0O :#line:416
            print (OO0O0O0O00O000O0O )#line:417
    def change_nickname (O000OO0O0O00OOOO0 ):#line:420
        try :#line:421
            O000O00OOO0O00OOO =timi_new ()#line:422
            O0OO00OO00O0OOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:423
            O0OOOOOOOO0000OOO =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO00OO00O0OOO00 ).text #line:424
            OO0OO0OOOO0OO0000 =re .findall ('<ul><li>(.*?)</li>',O0OOOOOOOO0000OOO )[0 ][:3 ]#line:425
            O0OOO00000O0O0000 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0OO0OOOO0OO0000}').json ()#line:426
            O0OOOOO0000O0O0O0 =O0OOO00000O0O0000 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:427
            OO0OOOOO0OO0O0OOO ={"nickname":O0OOOOO0000O0O0O0 }#line:428
            O000OOOO000O0O000 =f'_nickname={O0OOOOO0000O0O0O0}_{O000O00OOO0O00OOO}'#line:429
            OOO00000000OOOO00 ={'source':'scsc','authorization':O000OO0O0O00OOOO0 .token ,'timestamp':O000O00OOO0O00OOO ,'sign':sign (O000OOOO000O0O000 ),'signstring':O000OOOO000O0O000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:440
            OOOO00OO0OOOOO0O0 =requests .request ('patch',f'{host}/user/nickname',headers =OOO00000000OOOO00 ,data =OO0OOOOO0OO0O0OOO ).json ()#line:441
            if 'status'in OOOO00OO0OOOOO0O0 :#line:443
                if OOOO00OO0OOOOO0O0 ['status']==200 :#line:444
                    print (f'【修改网名】:网名:{O0OOOOO0000O0O0O0}丨{OOOO00OO0OOOOO0O0["message"]}')#line:445
        except Exception as O0OOO0O0OOOO000OO :#line:446
            print (O0OOO0O0OOOO000OO )#line:447
    def withdraw (OO00OO0OO0OO0O0OO ):#line:450
        try :#line:451
            OOOO0OO0O00O0OOO0 =f'__{timi_new()}'#line:452
            O0OOOOO00O00O00O0 ={'source':'scsc','authorization':OO00OO0OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O00O0OOO0 ),'signstring':OOOO0OO0O00O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O00O0OOO0OO0OOOOO =requests .request ('get',f'{host}/assets',headers =O0OOOOO00O00O00O0 ).json ()#line:464
            if 'status'in O00O0OOO0OO0OOOOO :#line:466
                if O00O0OOO0OO0OOOOO ['status']==200 :#line:467
                    O0O0O0O0OO0000000 =O00O0OOO0OO0OOOOO ['data']['cash']#line:468
                    if float (O0O0O0O0OO0000000 )>20 :#line:469
                        OOOO0OO0O00O0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:470
                        O0OOOOO00O00O00O0 ={'authorization':OO00OO0OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O00O0OOO0 ),'signstring':OOOO0OO0O00O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
                        OO000OO0O0O0000OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:481
                        O0000OOO0O00O0O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OOOOO00O00O00O0 ,data =OO000OO0O0O0000OO ).json ()#line:483
                        if 'status'in O0000OOO0O00O0O00 :#line:485
                            if O0000OOO0O00O0O00 ['status']==200 :#line:486
                                print (f'【余额提现】:{O0000OOO0O00O0O00["data"]}')#line:487
                        if 'status'in O0000OOO0O00O0O00 :#line:488
                            if O0000OOO0O00O0O00 ['status']==500 :#line:489
                                print (f'【余额提现】:{O0000OOO0O00O0O00["message"]}')#line:490
        except Exception as OO0OO0O000OOO0000 :#line:491
            print (OO0OO0O000OOO0000 )#line:492
    def invitenum (O0OOO00OO00000O00 ):#line:495
        global invited_new #line:496
        try :#line:497
            O000O0OO0O000O0O0 =f'__{timi_new()}'#line:498
            O00O00OO000OOOOO0 ={'source':'scsc','authorization':O0OOO00OO00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O000O0O0 ),'signstring':O000O0OO0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:509
            OO0OOO0O0OOOOOO00 =requests .request ('get',f'{host}/invite/invitenum',headers =O00O00OO000OOOOO0 ).json ()#line:510
            if 'status'in OO0OOO0O0OOOOOO00 :#line:512
                if OO0OOO0O0OOOOOO00 ['status']==200 :#line:513
                    OO0000O0O0O000O00 =OO0OOO0O0OOOOOO00 ['data']['invited_count']#line:514
                    OOO0O000O000O00O0 =OO0OOO0O0OOOOOO00 ['data']['invited_second_count']#line:515
                    print (f'【我的邀请】:直邀好友:{OO0000O0O0O000O00}丨间邀好友:{OOO0O000O000O00O0}')#line:516
                    if OO0000O0O0O000O00 <2 :#line:517
                        OOOO00000OOO0O000 =f'__{timi_new()}'#line:518
                        OO0000OO00OO000OO ={'source':'scsc','authorization':O0OOO00OO00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000OOO0O000 ),'signstring':OOOO00000OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                        OOOO0OO0OO0OO0000 =requests .request ('get',f'{host}/user',headers =OO0000OO00OO000OO ).json ()#line:530
                        if 'status'in OOOO0OO0OO0OO0000 :#line:532
                            if OOOO0OO0OO0OO0000 ['status']==200 :#line:533
                                invited_new .append (OOOO0OO0OO0OO0000 ['data']['inner_id'])#line:534
        except Exception as OO0O0OO0O00OOOOO0 :#line:535
            print (OO0O0OO0O00OOOOO0 )#line:536
    def game_map (OOO00OOOOOOOOO00O ):#line:539
        try :#line:540
            OOOOO00OO0OO0OOO0 =f'__{timi_new()}'#line:541
            OO00O00OO0O0OOOO0 ={'source':'scsc','authorization':OOO00OOOOOOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0OO0OOO0 ),'signstring':OOOOO00OO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            O0OO000OO00O0OOOO =requests .request ('get',f'{host}/game/map',headers =OO00O00OO0O0OOOO0 ).json ()#line:553
            if 'status'in O0OO000OO00O0OOOO :#line:555
                if O0OO000OO00O0OOOO ['status']==200 :#line:556
                    for OO0000OO0O00OO000 in O0OO000OO00O0OOOO ['data']['list'][0 ]['crops']:#line:557
                        OOO0OOO000OOOO00O =OO0000OO0O00OO000 ['level']#line:559
                        if OOO0OOO000OOOO00O ==41 :#line:560
                            OOO000O00OOO00OOO =OO0000OO0O00OO000 ['crop_name']#line:561
                            O0O000OO000OOO0O0 =OO0000OO0O00OO000 ['count']#line:562
                            if O0O000OO000OOO0O0 >0 :#line:563
                                print (f'【农业资产】:{OOO000O00OOO00OOO}丨数量:{O0O000OO000OOO0O0}')#line:564
                                if float (datetime .datetime .now ().hour )>8 :#line:565
                                    OOO000O00O0O0OO0O =OOO00OOOOOOOOO00O .the_query ()#line:566
                                    OOO00OOOOOOOOO00O .market_sale (OOO000O00O0O0OO0O )#line:567
        except Exception as O000000OOO00000OO :#line:568
            print (O000000OOO00000OO )#line:569
    def give_gold (OOOOOO000OO000O00 ):#line:572
        try :#line:573
            OOO0OO0OO00O00OOO =f'__{timi_new()}'#line:574
            O0OO0OOO000000OOO ={'source':'scsc','authorization':OOOOOO000OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O00OOO ),'signstring':OOO0OO0OO00O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:585
            OO0OO000OO00OOO0O =requests .request ('get',f'{host}/user',headers =O0OO0OOO000000OOO ).json ()#line:586
            if 'status'in OO0OO000OO00OOO0O :#line:587
                if OO0OO000OO00OOO0O ['status']==200 :#line:588
                    if float (OOOOOO000OO000O00 .doneeNo )!=0 :#line:589
                        OO00O0O000OO0000O =OO0OO000OO00OOO0O ['data']['assets']['gold']#line:590
                        if float (OO00O0O000OO0000O )>float (OOOOOO000OO000O00 .innerId ):#line:591
                            O0O00O0OOO0O0OOO0 =int (float (OO00O0O000OO0000O )/1.1 )#line:592
                            OOO0OO0OO00O00OOO =f'_doneeNo={OOOOOO000OO000O00.doneeNo}&quantity={O0O00O0OOO0O0OOO0}_{timi_new()}'#line:593
                            O0OO0OOO000000OOO ={'source':'scsc','authorization':OOOOOO000OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O00OOO ),'signstring':OOO0OO0OO00O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:604
                            O00O00OO0O00O00O0 ={"quantity":O0O00O0OOO0O0OOO0 ,"doneeNo":OOOOOO000OO000O00 .doneeNo }#line:608
                            OOOOO0OOOO00OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO0OOO000000OOO ,data =O00O00OO0O00O00O0 ).json ()#line:609
                            if 'status'in OOOOO0OOOO00OO00O :#line:611
                                if OOOOO0OOOO00OO00O ['status']==200 :#line:612
                                    if OOOOO0OOOO00OO00O ['data']:#line:613
                                        print (f'【赠送种子】:赠送{O0O00O0OOO0O0OOO0}种子给{OOOOOO000OO000O00.doneeNo}成功')#line:614
                    else :#line:615
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:616
        except Exception as OO0O0OO00O0O0O0O0 :#line:617
            print (OO0O0OO00O0O0O0O0 )#line:618
    def invitation (OOO0OO00O0000O000 ):#line:620
        try :#line:621
            _OO0OOOOO0O00OOOOO =float (bundled_def ())/4 #line:622
            OO00OO0O0OO00OO00 =f'_innerId={int(_OO0OOOOO0O00OOOOO)}_{timi_new()}'#line:623
            O0O0O00O00O0OO0O0 ={'source':'scsc','authorization':OOO0OO00O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O0OO00OO00 ),'signstring':OO00OO0O0OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OO0O0OOOO000OO00O ={"innerId":int (_OO0OOOOO0O00OOOOO )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0O00O00O0OO0O0 ,data =OO0O0OOOO000OO00O )#line:636
        except Exception as O0O0O000OO0OOO000 :#line:637
            print (O0O0O000OO0OOO000 )#line:638
    def winning_rewards (OO00OO000OO000000 ):#line:641
        try :#line:642
            O0000O0OOOOO0OOO0 =f'__{timi_new()}'#line:643
            OOOO00O0O0O000OOO ={'source':'scsc','authorization':OO00OO000OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOOOO0OOO0 ),'signstring':O0000O0OOOOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            OO000OO0OOO0OOOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO00O0O0O000OOO ).json ()#line:655
            if 'status'in OO000OO0OOO0OOOO0 :#line:657
                if OO000OO0OOO0OOOO0 ['status']==200 :#line:658
                    if OO000OO0OOO0OOOO0 ['data']['amount']:#line:659
                        O0OOOO000OO0O00OO =OO000OO0OOO0OOOO0 ['data']['amount']['gold']#line:660
                        return O0OOOO000OO0O00OO #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as O0OOO0O0OOO0OOOOO :#line:664
            print (O0OOO0O0OOO0OOOOO )#line:665
    def certification (O00000OO0OOO00O0O ):#line:668
        try :#line:669
            O00OO0O0OOOO0OO00 =f'__{timi_new()}'#line:670
            O00OO00OO00O00O00 ={'source':'scsc','authorization':O00000OO0OOO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OOOO0OO00 ),'signstring':O00OO0O0OOOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            O0O000OO000OOOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO00OO00O00O00 ).json ()#line:682
            if 'status'in O0O000OO000OOOO0O :#line:684
                if O0O000OO000OOOO0O ['status']==200 :#line:685
                    if O0O000OO000OOOO0O ['data']['result']:#line:686
                        OOO0OO00O000O0OOO =O0O000OO000OOOO0O ['data']['nick_name']#line:687
                        return OOO0OO00O000O0OOO #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as OO0OOO000O000O00O :#line:691
            print (OO0OOO000O000O00O )#line:692
    def crops_illustrated (OOO00O00OOO00OOOO ):#line:695
        try :#line:696
            O00OOO00OO0O0O000 =f'__{timi_new()}'#line:697
            OOO000O00OO000OO0 ={'source':'scsc','authorization':OOO00O00OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OO0O0O000 ),'signstring':O00OOO00OO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            OO0O00O00000O0O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO000O00OO000OO0 ).json ()#line:709
            if 'status'in OO0O00O00000O0O0O :#line:711
                if OO0O00O00000O0O0O ['status']==200 :#line:712
                    O00OO000OO0O0OOOO =OO0O00O00000O0O0O ['data'][0 ]['crops']#line:713
                    for OOOO0OO000OOO0000 in O00OO000OO0O0OOOO :#line:714
                        if OOOO0OO000OOO0000 ['ill_clover_award']:#line:715
                            if float (OOOO0OO000OOO0000 ['ill_clover_award'])>1 :#line:716
                                if OOOO0OO000OOO0000 ['is_finish']:#line:717
                                    if not OOOO0OO000OOO0000 ['is_getit']:#line:718
                                        if OOO00O00OOO00OOOO .certification ()!='未实名':#line:719
                                            O00OOO00OO0O0O000 =f'_award_level={OOOO0OO000OOO0000["level"]}_{timi_new()}'#line:720
                                            OOO000O00OO000OO0 ={'source':'scsc','authorization':OOO00O00OOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OO0O0O000 ),'signstring':O00OOO00OO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            OOO0OOOOOOO000O0O ={"award_level":OOOO0OO000OOO0000 ['level']}#line:732
                                            OO0O0OO000OO0O0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO000O00OO000OO0 ,json =OOO0OOOOOOO000O0O ).json ()#line:734
                                            if 'status'in OO0O0OO000OO0O0O0 :#line:735
                                                if OO0O0OO000OO0O0O0 ['status']==200 :#line:736
                                                    OO0000OO0OOOOOOO0 =OO0O0OO000OO0O0O0 ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{OOOO0OO000OOO0000["crop_name"]}成就丨奖励{OO0000OO0OOOOOOO0}☘️')#line:739
                                                if OO0O0OO000OO0O0O0 ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{OO0O0OO000OO0O0O0["message"]}')#line:741
        except Exception as OO00O0O0O0OOO0O00 :#line:742
            print (OO00O0O0O0OOO0O00 )#line:743
    def watched_ad (O0OOOO0OOO00O000O ):#line:746
        try :#line:747
            O0O0OO0OOOOOOOOO0 =f'__{timi_new()}'#line:748
            OOO000OOO0000OOO0 ={'source':'scsc','authorization':O0OOOO0OOO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOOOOOOOO0 ),'signstring':O0O0OO0OOOOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            O000OO00OOOO00O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO0000OOO0 ).json ()#line:760
            if 'status'in O000OO00OOOO00O0O :#line:762
                if O000OO00OOOO00O0O ['status']==200 :#line:763
                    if 'offlineInfo'in O000OO00OOOO00O0O ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        O000O000OOOOOO00O =O000OO00OOOO00O0O ['data']['offlineInfo']['off_minute']#line:766
                        OO0O0OOO00O0O0OO0 =float (O000OO00OOOO00O0O ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OOO0000OOO0 ).json ()#line:769
                        time .sleep (2 )#line:770
                        O00000O0O00OO0000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOO0000OOO0 ).json ()#line:771
                        if 'status'in O00000O0O00OO0000 :#line:773
                            if O00000O0O00OO0000 ['status']==200 :#line:774
                                O00OOO0000O0OOOOO =float (O00000O0O00OO0000 ['data']['silver'])/1000000000000 #line:775
                                O0O000O00O0O0O0O0 =str (O00OOO0000O0OOOOO -OO0O0OOO00O0O0OO0 )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{O000O000OOOOOO00O}分钟奖励🌱数量:{O0O000O00O0O0O0O0}t粒')#line:777
        except Exception as O0OO000O0OO00OO00 :#line:778
            print (O0OO000O0OO00OO00 )#line:779
    def user_ad (OO00OO00O0OO0OO00 ):#line:782
        try :#line:783
            O000OO00OOOOOO0OO =f'__{timi_new()}'#line:784
            OO0OOO0OO0O0O0000 ={'source':'scsc','authorization':OO00OO00O0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OOOOOO0OO ),'signstring':O000OO00OOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            OOOOOOO00O00OOOO0 =requests .request ('get',f'{host}/user/ad',headers =OO0OOO0OO0O0O0000 ).json ()#line:796
            if 'status'in OOOOOOO00O00OOOO0 :#line:798
                if OOOOOOO00O00OOOO0 ['status']==200 :#line:799
                    O000OOO0000OO0O00 =OOOOOOO00O00OOOO0 ['data']['max_time']#line:800
                    O0O000OOO0OO0O00O =OOOOOOO00O00OOOO0 ['data']['watch_time']#line:801
                    OO0000OO000000OOO =OOOOOOO00O00OOOO0 ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{OO0000OO000000OOO + O000OOO0000OO0O00 - O0O000OOO0OO0O00O}次丨好友提供:{OO0000OO000000OOO}次')#line:803
                    if OO0000OO000000OOO +O000OOO0000OO0O00 -O0O000OOO0OO0O00O >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        OOOOO0OO0OO000OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0OOO0OO0O0O0000 ).json ()#line:806
                        if 'status'in OOOOO0OO0OO000OOO :#line:808
                            if OOOOO0OO0OO000OOO ['status']==200 :#line:809
                                O00OO0OO0OO0OO000 =float (OOOOO0OO0OO000OOO ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(O00OO0OO0OO0OO000)}t粒')#line:811
                                return True #line:812
                            if OOOOO0OO0OO000OOO ['status']==500 :#line:813
                                OO000O0000000O0OO =OOOOO0OO0OO000OOO ['message']#line:814
                                print (f'【获取种子】:{OO000O0000000O0OO}')#line:815
                                return False #line:816
        except Exception as OOOO0O0000OO00OOO :#line:817
            print (OOOO0O0000OO00OOO )#line:818
    def synthetic (O0O00OO0O00O0O000 ):#line:821
        global id ,g #line:822
        try :#line:823
            OO00OOO00O000000O =O0O00OO0O00O0O000 .level_new ()#line:824
            O0OO0000OO0O0OOO0 =random .randint (9 ,11 )#line:825
            OO0OOO0O0O0OO0O00 =f'_site=8&targetSite={O0OO0000OO0O0OOO0}_{timi_new()}'#line:826
            OOO0O0O0O0O000OO0 ={'source':'scsc','authorization':O0O00OO0O00O0O000 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O0O0OO0O00 ),'signstring':OO0OOO0O0O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            OOOOOOO0000OO0O0O ={"site":int (8 ),"targetSite":int (O0OO0000OO0O0OOO0 )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0O0O0O000OO0 ,json =OOOOOOO0000OO0O0O )#line:839
            while True :#line:840
                O0O0O0O0O00O000O0 =f'__{timi_new()}'#line:841
                O0O0O0OOO00000O0O ={'source':'scsc','authorization':O0O00OO0O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0O00O000O0 ),'signstring':O0O0O0O0O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                O00OO0O000000O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00000O0O ).json ()#line:853
                if 'status'in O00OO0O000000O00O :#line:855
                    if O00OO0O000000O00O ['status']==200 :#line:856
                        O0OOOOO0OOO0OOO0O =O00OO0O000000O00O ['data']['cropList']#line:857
                        O0000OOO00000OOO0 =O00OO0O000000O00O ['data']['gameCoreDataDBid']#line:858
                        OO0000O0OOO0O0OO0 =float (O00OO0O000000O00O ['data']['silver'])/1000000000000 #line:859
                        OOOO00O000O0OOO0O =0 #line:864
                        for O0OOO00O000OO00O0 in O0OOOOO0OOO0OOO0O :#line:865
                            if not O0OOO00O000OO00O0 :#line:866
                                OO0O00000OO0O0O0O =f'_crop_id={O0000OOO00000OOO0}&site={OOOO00O000O0OOO0O}_{O0O00OO0O00O0O000.time}'#line:867
                                OO00OOO00O0O0O00O ={'source':'scsc','authorization':O0O00OO0O00O0O000 .token ,'timestamp':O0O00OO0O00O0O000 .time ,'sign':sign (OO0O00000OO0O0O0O ),'signstring':OO0O00000OO0O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                OOO0OOOO000O00OOO ={"site":OOOO00O000O0OOO0O ,"crop_id":O0000OOO00000OOO0 }#line:878
                                O000O0OO00O000O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OOO00O0O0O00O ,data =OOO0OOOO000O00OOO ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in O000O0OO00O000O00 :#line:882
                                    if O000O0OO00O000O00 ['status']==200 :#line:883
                                        if O000O0OO00O000O00 ['message']=='种子数量不足':#line:884
                                            OO00OOO00O000000O =O0O00OO0O00O0O000 .level_new ()#line:885
                                            print (f'【种植合成】:{O000O0OO00O000O00["message"]}')#line:886
                                            if not O0O00OO0O00O0O000 .user_ad ():#line:887
                                                return False #line:888
                                    if O000O0OO00O000O00 ['status']==500 :#line:889
                                        print (f'【种植合成】:{O000O0OO00O000O00["message"]}')#line:890
                                        return False #line:891
                            OOOO00O000O0OOO0O +=1 #line:892
                        OO0OOO0OOO00000OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00000O0O ).json ()#line:893
                        OOO0O0000OO0000OO =OO0OOO0OOO00000OO ['data']['cropList']#line:894
                        OOO000OOOO0OOOOO0 =False #line:895
                        for O0OOO00O000OO00O0 in range (12 ):#line:896
                            id =OOO0O0000OO0000OO [O0OOO00O000OO00O0 ]['level']#line:897
                            if float (OO00OOO00O000000O )-float (id )>9 :#line:898
                                OOOO0OO0OO000OO00 =f'_site={O0OOO00O000OO00O0}_{timi_new()}'#line:899
                                O0OOOOO0OOOO00OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00OO0O00O0O000 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0OO000OO00 ),'signstring':OOOO0OO0OO000OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                O000OO0O0OO0OOOO0 ={"site":O0OOO00O000OO00O0 }#line:911
                                OO00OO0000OO000O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OOOOO0OOOO00OOO ,data =O000OO0O0OO0OOOO0 ).json ()#line:913
                                if 'status'in OO00OO0000OO000O0 :#line:914
                                    if OO00OO0000OO000O0 ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O0OOOOO00OOO00OOO in range (11 ):#line:918
                                    OO0OO0O000OO000OO =O0OOOOO00OOO00OOO +1 #line:919
                                    g =OOO0O0000OO0000OO [OO0OO0O000OO000OO ]['level']#line:920
                                    if id ==g :#line:921
                                        OOO0OO00000O0O000 =O0OOOOO00OOO00OOO +2 #line:922
                                        if OOO0OO00000O0O000 !=O0OOO00O000OO00O0 +1 :#line:923
                                            OO0O0O00O000OOO0O =O0OOO00O000OO00O0 +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            OO0OOO0O0O0OO0O00 =f'_site={OO0O0O00O000OOO0O - 1}&targetSite={OOO0OO00000O0O000 - 1}_{timi_new()}'#line:927
                                            OOO0O0O0O0O000OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00OO0O00O0O000 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O0O0OO0O00 ),'signstring':OO0OOO0O0O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            O0OOOOOOOO000OOO0 ={"site":int (OO0O0O00O000OOO0O -1 ),"targetSite":int (OOO0OO00000O0O000 -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0O0O0O000OO0 ,json =O0OOOOOOOO000OOO0 )#line:946
                                            OOO000OOOO0OOOOO0 =True #line:948
                                    if OOO000OOOO0OOOOO0 :#line:949
                                        break #line:950
                                if OOO000OOOO0OOOOO0 :#line:951
                                    break #line:952
        except :#line:953
            O0O00OO0O00O0O000 .synthetic ()#line:954
    def level_new (O00OOOOO00O00OO00 ):#line:957
        try :#line:958
            OOO00OO00OO0O00OO =f'__{timi_new()}'#line:959
            O00O00O0OO0O00O0O ={'source':'scsc','authorization':O00OOOOO00O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00OO0O00OO ),'signstring':OOO00OO00OO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            O00O000OO000O00O0 =requests .request ('get',f'{host}/user',headers =O00O00O0OO0O00O0O ).json ()#line:971
            if 'status'in O00O000OO000O00O0 :#line:972
                if O00O000OO000O00O0 ['status']==200 :#line:973
                    return float (O00O000OO000O00O0 ['data']['level'])#line:974
        except Exception as O000000O000O00000 :#line:975
            print (O000000O000O00000 )#line:976
    def propsraffle (OOO0OOO00OO00OO00 ):#line:979
        try :#line:980
            while True :#line:981
                O0OO0OOO0OOO0OO00 =f'__{timi_new()}'#line:982
                O0OO0O0O0000000O0 ={'source':'scsc','authorization':OOO0OOO00OO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO0OOO0OO00 ),'signstring':O0OO0OOO0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                O00O0OO0OOOO00OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0O0O0000000O0 ).json ()#line:994
                if 'status'in O00O0OO0OOOO00OOO :#line:996
                    if O00O0OO0OOOO00OOO ['status']==200 :#line:997
                        OO0OO0OO00O00OO00 =O00O0OO0OOOO00OOO ['data']['rows']#line:998
                        O00OOOO00OOOO0O00 =O00O0OO0OOOO00OOO ['data']['vstate']#line:999
                        if OO0OO0OO00O00OO00 ==5 or OO0OO0OO00O00OO00 ==6 or OO0OO0OO00O00OO00 ==7 :#line:1000
                            O000000OOOO0O0O0O =O00O0OO0OOOO00OOO ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{O000000OOOO0O0O0O}')#line:1002
                        if OO0OO0OO00O00OO00 ==1 or OO0OO0OO00O00OO00 ==2 or OO0OO0OO00O00OO00 ==3 :#line:1003
                            O0O00OOOO0O0OOOOO =O00O0OO0OOOO00OOO ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O0O00OOOO0O0OOOOO}')#line:1005
                        if OO0OO0OO00O00OO00 ==4 or OO0OO0OO00O00OO00 ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if OO0OO0OO00O00OO00 =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as O0O0O0O0O0OO000O0 :#line:1047
            print (O0O0O0O0O0OO000O0 )#line:1048
    def friends_invitation (OOOO0OO0OOOOOO0OO ):#line:1051
        try :#line:1052
            O0O0000OO00000OO0 =f'__{timi_new()}'#line:1053
            O0OO0OOOO0OOO0O0O ={'source':'scsc','authorization':OOOO0OO0OOOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO00000OO0 ),'signstring':O0O0000OO00000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            OOOOOO00O0O0O000O =requests .request ('get',f'{host}/friends',headers =O0OO0OOOO0OOO0O0O ).json ()#line:1065
            if 'status'in OOOOOO00O0O0O000O :#line:1066
                if OOOOOO00O0O0O000O ['status']==200 :#line:1067
                    OOOO00OO00O00OOO0 =OOOOOO00O0O0O000O ['data']['myInviteter']#line:1068
                    if OOOO00OO00O00OOO0 :#line:1069
                        O0O00OO000000O00O =OOOO00OO00O00OOO0 ['user']['nickname']#line:1070
                        O0OOO0O00OOOO000O =OOOO0OO0OOOOOO0OO .certification ()#line:1071
                        if O0OOO0O00OOOO000O =='未实名':#line:1072
                            weishim .append (OOOO0OO0OOOOOO0OO .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{O0O00OO000000O00O}丨实名:{O0OOO0O00OOOO000O}')#line:1074
        except Exception as OOOO000OOO00O0OO0 :#line:1078
            print (OOOO000OOO00O0OO0 )#line:1079
    def add_clover (OOO0O0OOOO00OOOOO ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            O00O000O0OOOO00OO =f'__{timi_new()}'#line:1085
            O0OOOO0OO000OO000 ={'source':'scsc','authorization':OOO0O0OOOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O0OOOO00OO ),'signstring':O00O000O0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            O0O0OO00O0OOOOOOO =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOO0OO000OO000 ).json ()#line:1097
            if 'status'in O0O0OO00O0OOOOOOO :#line:1099
                if O0O0OO00O0OOOOOOO ['status']==200 :#line:1100
                    O0OO0OO00O00OOOOO =O0O0OO00O0OOOOOOO ['data']['clover']#line:1101
                    OO000O00O0OO0OO0O =O0O0OO00O0OOOOOOO ['data']['used_clover']#line:1102
                    O00O0000OOO0OO0OO =float (O0OO0OO00O00OOOOO )-float (OO000O00O0OO0OO0O )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO000O00O0OO0OO0O}')#line:1104
                    if OOO0O0OOOO00OOOOO .certification ()!='未实名':#line:1105
                        if O00O0000OOO0OO0OO >1 :#line:1106
                            O00O000O0OOOO00OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O0000OOO0OO0OO)}_{timi_new()}'#line:1107
                            OO0OO00OOOO0OOO0O ={'source':'scsc','authorization':OOO0O0OOOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O0OOOO00OO ),'signstring':O00O000O0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            OOO000OOOOOO0OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O0000OOO0OO0OO )}#line:1119
                            O00OOOOO0O00OOOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OO00OOOO0OOO0O ,data =OOO000OOOOOO0OO00 ).json ()#line:1120
                            if 'status'in O00OOOOO0O00OOOO0 :#line:1122
                                if O00OOOOO0O00OOOO0 ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O00OOOOO0O00OOOO0["data"]["isSuccess"]}丨数量:{O00O0000OOO0OO0OO}')#line:1124
                                if O00OOOOO0O00OOOO0 ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O00OOOOO0O00OOOO0["message"]}')#line:1126
            OOOO0OO0OOOO0O0OO =requests .request ('get',f'{host}/lottery',headers =O0OOOO0OO000OO000 ).json ()#line:1127
            OOO0OOO0000O00OO0 =OOO0O0OOOO00OOOOO .winning_rewards ()#line:1129
            if 'status'in OOOO0OO0OOOO0O0OO :#line:1130
                if OOOO0OO0OOOO0O0OO ['status']==200 :#line:1131
                    O0O00OOO0O0OO000O =OOOO0OO0OOOO0O0OO ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (O0O00OOO0O0OO000O )#line:1133
                    OO0OO0O00O0000OO0 =OOOO0OO0OOOO0O0OO ['data'][1 ]['value']#line:1134
                    O0OO00O0OOOO0OO0O =OOOO0OO0OOOO0O0OO ['data'][0 ]['join_number']#line:1135
                    O0O0O0O00000O000O =int (float (OOOO0OO0OOOO0O0OO ['data'][0 ]['totalValue']))#line:1136
                    OO0O0OOOOO0OOO000 =float (OO0OO0O00O0000OO0 /O0O0O0O00000O000O )*10000 #line:1137
                    OOO0O00O000OOO00O =O0O0O0O00000O000O /O0OO00O0OOOO0OO0O #line:1138
                    print (f'【参与抽奖】:预计每天中{str(O0O00OOO0O0OO000O)[:6]}颗金种子丨好友收益:{str(OOO0OOO0000O00OO0)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(OO0O0OOOOO0OOO000)[:6]}颗金种子丨☘️人均:{str(OOO0O00O000OOO00O)[:7]}️')#line:1140
        except Exception as OO0OO0O00O00O000O :#line:1141
            print (OO0OO0O00O00O000O )#line:1142
    def energy (OOOOOO0000OO0OO0O ):#line:1145
        try :#line:1146
            while True :#line:1147
                OOOO0OOOO000OOOO0 =f'__{timi_new()}'#line:1148
                OO0OO00OO0OOOO0OO ={'source':'scsc','authorization':OOOOOO0000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO000OOOO0 ),'signstring':OOOO0OOOO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                OOO0O0OOO0O0OO0O0 =requests .request ('get',f'{host}/energy/general',headers =OO0OO00OO0OOOO0OO ).json ()#line:1160
                if 'status'in OOO0O0OOO0O0OO0O0 :#line:1162
                    if OOO0O0OOO0O0OO0O0 ['status']==200 :#line:1163
                        O00000OOOOOOO00OO =OOO0O0OOO0O0OO0O0 ['data']['ordinary_water']#line:1164
                        OO00OOO00O0O0000O =OOO0O0OOO0O0OO0O0 ['data']['ordinary_fertilizer']#line:1165
                        OO000000O0000O0OO =OOO0O0OOO0O0OO0O0 ['data']['videoStatus']#line:1166
                        O00O00O000OO0O00O =OOO0O0OOO0O0OO0O0 ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(OO00OOO00O0O0000O).split(".")[0]}丨水滴:{str(O00000OOOOOOO00OO).split(".")[0]}')#line:1169
                        if float (OO00OOO00O0O0000O )<96 :#line:1170
                            if OO000000O0000O0OO :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OOO0O0OOO0O000000 =99 -float (OO00OOO00O0O0000O )#line:1173
                                O0O00O0000OO00000 ={"fertilizer":str (OOO0O0OOO0O000000 ).split ('.')[0 ]}#line:1174
                                O0O0000O0O000O00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OO00OO0OOOO0OO ).json ()#line:1176
                                if 'status'in O0O0000O0O000O00O :#line:1178
                                    if O0O0000O0O000O00O ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0000O0O000O00O["message"]}')#line:1180
                                    if O0O0000O0O000O00O ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0000O0O000O00O["message"]}')#line:1182
                                        break #line:1183
                                if float (OO00OOO00O0O0000O )<78 :#line:1185
                                    OOO0O0OOO0O000000 =80 -float (OO00OOO00O0O0000O )#line:1186
                                    OOOOO00OOO0000OO0 =f'_fertilizer={int(OOO0O0OOO0O000000)}_{timi_new()}'#line:1187
                                    OOOO0000000OOO00O ={'source':'scsc','authorization':OOOOOO0000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOO0000OO0 ),'signstring':OOOOO00OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    O0OOOO0OO0OOO00OO ={"fertilizer":int (OOO0O0OOO0O000000 )}#line:1199
                                    OO0OO0O00O0OOOOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0000000OOO00O ,data =O0OOOO0OO0OOO00OO ).json ()#line:1201
                                    if 'status'in OO0OO0O00O0OOOOOO :#line:1203
                                        if OO0OO0O00O0OOOOOO ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OO0OO0O00O0OOOOOO["message"]}丨数量:{int(OOO0O0OOO0O000000)}')#line:1205
                                        if OO0OO0O00O0OOOOOO ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OO0OO0O00O0OOOOOO["message"]}丨数量:{int(OOO0O0OOO0O000000)}')#line:1207
                                            O000O0O0OO0OO00O0 =OO0OO0O00O0OOOOOO ["message"].split ('-')[1 ]#line:1208
                                            OOO00O00OOO0OOOOO =f'__{timi_new()}'#line:1209
                                            O0O000000OOOO0O00 ={'source':'scsc','authorization':OOOOOO0000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOO0OOOOO ),'signstring':OOO00O00OOO0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            OO0OOO0O000O0O00O =requests .request ('get',f'{host}/user',headers =O0O000000OOOO0O00 ).json ()#line:1221
                                            if 'status'in OO0OOO0O000O0O00O :#line:1222
                                                if OO0OOO0O000O0O00O ['status']==200 :#line:1223
                                                    OO0000OO0O00O0OO0 =OO0OOO0O000O0O00O ['data']['inner_id']#line:1224
                                                    if give_gold (OO0000OO0O00O0OO0 ,float (O000O0O0OO0OO00O0 )+1 ):#line:1225
                                                        OOOOOO0000OO0OO0O .energy ()#line:1226
                        if float (O00000OOOOOOO00OO )<880 :#line:1227
                            if O00O00O000OO0O00O :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O0OO00O0O0OO00OOO =999 -float (O00000OOOOOOO00OO )#line:1230
                                O0OO00OO0O0OOOO00 ={"water":str (O0OO00O0O0OO00OOO ).split ('.')[0 ]}#line:1231
                                OO0OO000O00OOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OO00OO0OOOO0OO ).json ()#line:1233
                                if 'status'in OO0OO000O00OOO0O0 :#line:1235
                                    if OO0OO000O00OOO0O0 ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO000O00OOO0O0["message"]}')#line:1237
                                    if OO0OO000O00OOO0O0 ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO000O00OOO0O0["message"]}')#line:1239
                                        break #line:1240
                                if float (O00000OOOOOOO00OO )<780 :#line:1241
                                    O0OO00O0O0OO00OOO =800 -float (O00000OOOOOOO00OO )#line:1242
                                    OO000000OOOOOO0O0 =f'_water={int(O0OO00O0O0OO00OOO)}_{timi_new()}'#line:1243
                                    O00OO0OO00000OOOO ={'source':'scsc','authorization':OOOOOO0000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OOOOOO0O0 ),'signstring':OO000000OOOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    O000OOO00000O00OO ={"water":int (O0OO00O0O0OO00OOO )}#line:1255
                                    O00000O0000OO00O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00OO0OO00000OOOO ,data =O000OOO00000O00OO ).json ()#line:1257
                                    if 'status'in O00000O0000OO00O0 :#line:1259
                                        if O00000O0000OO00O0 ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O00000O0000OO00O0["message"]}丨数量:{int(O0OO00O0O0OO00OOO)}')#line:1261
                                        if O00000O0000OO00O0 ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O00000O0000OO00O0["message"]}丨数量:{int(O0OO00O0O0OO00OOO)}')#line:1263
                                            O000O0O0OO0OO00O0 =O00000O0000OO00O0 ["message"].split ('-')[1 ]#line:1264
                                            OOO00O00OOO0OOOOO =f'__{timi_new()}'#line:1265
                                            O0O000000OOOO0O00 ={'source':'scsc','authorization':OOOOOO0000OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOO0OOOOO ),'signstring':OOO00O00OOO0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            OO0OOO0O000O0O00O =requests .request ('get',f'{host}/user',headers =O0O000000OOOO0O00 ).json ()#line:1277
                                            if 'status'in OO0OOO0O000O0O00O :#line:1278
                                                if OO0OOO0O000O0O00O ['status']==200 :#line:1279
                                                    OO0000OO0O00O0OO0 =OO0OOO0O000O0O00O ['data']['inner_id']#line:1280
                                                    if give_gold (OO0000OO0O00O0OO0 ,float (O000O0O0OO0OO00O0 )+1 ):#line:1281
                                                        OOOOOO0000OO0OO0O .energy ()#line:1282
                        break #line:1283
        except Exception as O0O00OOOO0000O00O :#line:1284
            print (O0O00OOOO0000O00O )#line:1285
def bundled_def ():#line:1288
    O0O0OOOO00O0OOOOO =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return O0O0OOOO00O0OOOOO [random .randint (0 ,len (O0O0OOOO00O0OOOOO )-1 )]#line:1290
def version_of_the_validation ():#line:1294
    return str ((103 -56 )/10 )#line:1295
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
        O00OO00OOOOO0O000 =gitee_edition ()#line:1329
        if version_of_the_validation ()<O00OO00OOOOO0O000 ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO00OOOOO0O000["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{O00OO00OOOOO0O000["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO00OOOOO0O000["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {O00OO00OOOOO0O000["CityEarth"]["content"]}')#line:1335
    except Exception as OO00O0OOO0OO0O000 :#line:1336
        print (OO00O0OOO0OO0O000 )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
