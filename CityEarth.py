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
version ='3.1.41955435111'#line:1
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
        O0OOO0OOOO00OOOOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OOO0OOOO00OOOOO)}个账号==========")#line:17
        for O0OO00000O0OOOOOO in O0OOO0OOOO00OOOOO :#line:18
            O0OO0000O000OOO00 =[]#line:19
            print (f"------------正在执行第{O0OOO0OOOO00OOOOO.index(O0OO00000O0OOOOOO) + 1}个账号------------")#line:20
            OO0O0OOO0O000O00O =CityEarth (O0OO00000O0OOOOOO ,O0OO0000O000OOO00 ,O0OOO0OOOO00OOOOO .index (O0OO00000O0OOOOOO ))#line:21
            def OOOO000O000OOOOO0 ():#line:23
                if OO0O0OOO0O000O00O .base_info ():#line:25
                    OO0O0OOO0O000O00O .sealing ()#line:27
                    OO0O0OOO0O000O00O .invitenum ()#line:29
                    OO0O0OOO0O000O00O .query_to_sell ()#line:31
                    OO0O0OOO0O000O00O .friends_invitation ()#line:35
                    OO0O0OOO0O000O00O .energy ()#line:37
                    OO0O0OOO0O000O00O .add_clover ()#line:39
                    OO0O0OOO0O000O00O .propsraffle ()#line:41
                    OO0O0OOO0O000O00O .synthetic ()#line:43
                    OO0O0OOO0O000O00O .crops_illustrated ()#line:45
                    OO0O0OOO0O000O00O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0O0OOO0O000O00O .give_gold ()#line:50
            O000O0O00O0OOOO00 =threading .Thread (target =OOOO000O000OOOOO0 )#line:52
            O000O0O00O0OOOO00 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0O00O0OOO00O0OO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O00O0OOO00O0OO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O00OO0O0OO0O000O0 in invited_new :#line:62
            print (O00OO0O0OO0O000O0 )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0000OOOO00OO0O0 in weishim :#line:65
            print (OO0000OOOO00OO0O0 )#line:66
    except Exception as OO0000O0O0O00OO00 :#line:67
        print (OO0000O0O0O00OO00 )#line:68
def give_gold (O000O00O00OO0O0OO ,OOOOOO0O0000OO0OO ):#line:72
    try :#line:73
        OOOO0OO0O000OO00O =f'_doneeNo={O000O00O00OO0O0OO}&quantity={int(OOOOOO0O0000OO0OO)}_{timi_new()}'#line:74
        OO00000OOO000000O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O000OO00O ),'signstring':OOOO0OO0O000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO0O00OO00000OO0O ={"quantity":int (OOOOOO0O0000OO0OO ),"doneeNo":O000O00O00OO0O0OO }#line:89
        OOOOO000O000000OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00000OOO000000O ,data =OO0O00OO00000OO0O ).json ()#line:90
        if 'status'in OOOOO000O000000OO :#line:92
            if OOOOO000O000000OO ['status']==200 :#line:93
                if OOOOO000O000000OO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOOOOO0O0000OO0OO)}种子给{O000O00O00OO0O0OO}成功')#line:95
                    return True #line:96
            if OOOOO000O000000OO ['status']==401 :#line:97
                print (f'【赠送种子】:{OOOOO000O000000OO["message"]}')#line:98
                return False #line:99
            if OOOOO000O000000OO ['status']==500 :#line:100
                print (f'【赠送种子】:{OOOOO000O000000OO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O000000000OOO0OOO :#line:104
        print (O000000000OOO0OOO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0OO0O0OO00O0OO0 ):#line:115
    O00OOO0OO0OOO0O00 =hashlib .md5 (OO0OO0O0OO00O0OO0 .encode ()).hexdigest ()#line:116
    OO0O0000000OOO00O =sc1 ()#line:117
    O0OO0OO0OOO0OO00O =sc2 ()#line:118
    O0OOO0O000OO00OO0 =sc3 ()#line:119
    OO0OO00000O0OO0O0 =OO0O0000000OOO00O +O00OOO0OO0OOO0O00 +O0OO0OO0OOO0OO00O +O0OOO0O000OO00OO0 #line:120
    OOOOO0OO0O0OO00OO =hashlib .md5 (OO0OO00000O0OO0O0 .encode ()).hexdigest ()#line:121
    return OOOOO0OO0O0OO00OO #line:122
def format_msg ():#line:125
    O0OOO0OOOO00000O0 =""#line:126
    for O0O0OO00O0O0O0O00 in msg_list :#line:127
        O0OOO0OOOO00000O0 +=str (O0O0OO00O0O0O0O00 )+"\r\n"#line:128
    return O0OOO0OOOO00000O0 #line:129
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
def get_json_data (O0000O0OOO0OO00OO ,O00O0000O0O0000OO ,OO00OO00O00O0O0OO ,OOOOOO00OOO0OOO00 ):#line:153
    with open (O0000O0OOO0OO00OO ,'rb')as OOOOO00O000O0000O :#line:154
        O000OOOOO0OO0O00O =json .load (OOOOO00O000O0000O )#line:155
        O000OOOOO0OO0O00O ['data'][O00O0000O0O0000OO ][OO00OO00O00O0O0OO ]=OOOOOO00OOO0OOO00 #line:156
        O00O00O0000OOOO00 =O000OOOOO0OO0O00O #line:157
    OOOOO00O000O0000O .close ()#line:158
    return O00O00O0000OOOO00 #line:159
def write_json_data (O0O0OO0OOOOOOOOO0 ):#line:162
    with open (json_path1 ,'w')as OO0O0OOOOO00OO0OO :#line:163
        json .dump (O0O0OO0OOOOOOOOO0 ,OO0O0OOOOO00OO0OO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OO0O0OOOOO00OO0OO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O00O00O00O0OOOOO0 ,O0O0O0O00OOO00O0O ,OOO0OOO0O0O0000O0 ,OOOO0O0OO0O0O0000 ):#line:171
        try :#line:172
            O00O00O00O0OOOOO0 .msg =OOO0OOO0O0O0000O0 #line:173
            O00O00O00O0OOOOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O00O00O00O0OOOOO0 .token =O0O0O0O00OOO00O0O ['authorization']#line:175
            O00O00O00O0OOOOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O00O00O00O0OOOOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O00O00O00O0OOOOO0 .elephant_user =O0O0O0O00OOO00O0O ['elephant_user']#line:178
            O00O00O00O0OOOOO0 .elephant_pswd =O0O0O0O00OOO00O0O ['elephant_pswd']#line:179
            O00O00O00O0OOOOO0 .elephant_Task_ID =O0O0O0O00OOO00O0O ['elephant_Task_ID']#line:180
            O00O00O00O0OOOOO0 .len_new =OOOO0O0OO0O0O0000 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOOOO000O0OO0OO0 ):#line:186
        try :#line:187
            OOOOOO000O0OO0OO0 .watched_ad ()#line:189
            OO0000000OO0000O0 =f'__{timi_new()}'#line:190
            O0O0O0000O00O00O0 ={'source':'scsc','authorization':OOOOOO000O0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000OO0000O0 ),'signstring':OO0000000OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0OO0OO000O00OOO0 =requests .request ('get',f'{host}/user',headers =O0O0O0000O00O00O0 ).json ()#line:202
            if 'status'in O0OO0OO000O00OOO0 :#line:204
                if O0OO0OO000O00OOO0 ['status']==200 :#line:205
                    O00000000000OOOOO =O0OO0OO000O00OOO0 ['data']['nickname']#line:206
                    O0O00O00O0OO00OO0 =O0OO0OO000O00OOO0 ['data']['inner_id']#line:207
                    OO0O0OOO0OOO0OOOO =O0OO0OO000O00OOO0 ['data']['assets']['gold']#line:208
                    OO0OO000OO0OOO0O0 =O0OO0OO000O00OOO0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00000000000OOOOO[:5]}丨ID:{O0O00O00O0OO00OO0}丨等级:{OO0OO000OO0OOO0O0}丨金种子:{str(OO0O0OOO0OOO0OOOO).split(".")[0]}')#line:211
                    if 'wx_'in O00000000000OOOOO :#line:212
                        OOOOOO000O0OO0OO0 .change_nickname ()#line:213
                if O0OO0OO000O00OOO0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOOOO000O0OO0OO0 .elephant_user =='f':#line:216
                        return False #line:217
                    OOO0O0O00O0OOO000 =Invalid_login .addtask (elephant_user =OOOOOO000O0OO0OO0 .elephant_user ,elephant_pswd =OOOOOO000O0OO0OO0 .elephant_pswd ,elephant_Task_ID =OOOOOO000O0OO0OO0 .elephant_Task_ID )#line:220
                    OO00O0O0O0OOOOOOO =get_json_data (json_path ,OOOOOO000O0OO0OO0 .len_new ,'authorization',OOO0O0O00O0OOO000 )#line:221
                    if write_json_data (OO00O0O0O0OOOOOOO ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0OO0OO000O00OOO0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOOO00OO00O00OO0O :#line:228
            print (OOOO00OO00O00OO0O )#line:229
    def sealing (O0O0OO00OO0O0OOO0 ):#line:232
        try :#line:233
            O00OO0O0O0OO00OO0 =f'__{timi_new()}'#line:234
            OOO000O00O00O00O0 ={'source':'scsc','authorization':O0O0OO00OO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0OO00OO0 ),'signstring':O00OO0O0O0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO000O00O00O00O0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO000O00O00O00O0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO000O00O00O00O0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO000O00O00O00O0 )#line:249
            requests .request ('get',f'{host}/user',headers =OOO000O00O00O00O0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO000O00O00O00O0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO000O00O00O00O0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO000O00O00O00O0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO000O00O00O00O0 )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO000O00O00O00O0 )#line:255
        except Exception as OO00O0OOO00O0O0OO :#line:256
            print (OO00O0OOO00O0O0OO )#line:257
    def ddd (O0OOOO0OOOO00OOOO ):#line:259
        try :#line:260
            OOO0OO000OO0O0OO0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00O0O0000OOO0O00 ={'source':'scsc','authorization':O0OOOO0OOOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000OO0O0OO0 ),'signstring':OOO0OO000OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO00O0O000OO0O00 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00O0O0000OOO0O00 ).json ()#line:273
            print (OOO00O0O000OO0O00 )#line:274
        except Exception as O000000O0O0OO00O0 :#line:277
            print (O000000O0O0OO00O0 )#line:278
    def the_query (OO00OO00O0000OO00 ):#line:283
        try :#line:284
            OOOO0OOOO0OOO0OO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0OOO00O0OO000OOO ={'authorization':OO00OO00O0000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0OOO0OO0 ),'signstring':OOOO0OOOO0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO0O0000O00O0O000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOO00O0OO000OOO ).json ()#line:296
            if 'status'in OO0O0000O00O0O000 :#line:298
                if OO0O0000O00O0O000 ['status']==200 :#line:299
                    return OO0O0000O00O0O000 ['data']['rows'][4 ]['price']#line:300
        except Exception as O00OOO00000000OO0 :#line:301
            print (O00OOO00000000OO0 )#line:302
    def market_sale (O00O00OO0OOOOO0OO ,O000OO0OOO0000000 ):#line:305
        try :#line:306
            OO00O000000O00OO0 =timi_new ()#line:307
            OOO0000000OOOO0O0 =f'type=crop__{OO00O000000O00OO0}'#line:308
            O00OOOOO00000O0OO ={'source':'scsc','authorization':O00O00OO0OOOOO0OO .token ,'timestamp':str (OO00O000000O00OO0 ),'sign':sign (OOO0000000OOOO0O0 ),'signstring':OOO0000000OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            OO00OO0OOO0OO0000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00OOOOO00000O0OO ).json ()#line:320
            if 'status'in OO00OO0OOO0OO0000 :#line:322
                if OO00OO0OOO0OO0000 ['status']==200 :#line:323
                    if OO00OO0OOO0OO0000 ['data']['rows']:#line:324
                        O000O0OO0OOO000O0 =OO00OO0OOO0OO0000 ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0O0O0OO00O0O0OO0 =OO00OO0OOO0OO0000 ['data']['rows'][0 ]['quantity']#line:326
                        O00O0OO0O0O0OO000 =O000OO0OOO0000000 #line:327
                        if float (O000OO0OOO0000000 )>5 :#line:328
                            OOOO0000OOO000O00 =f'_packsackItemId={O000O0OO0OOO000O0}&price={str(O00O0OO0O0O0OO000)[:5]}&quantity={O0O0O0OO00O0O0OO0}_{OO00O000000O00OO0}'#line:329
                            O0OOO000000O0O0OO ={'source':'scsc','authorization':O00O00OO0OOOOO0OO .token ,'timestamp':str (OO00O000000O00OO0 ),'sign':sign (OOOO0000OOO000O00 ),'signstring':OOOO0000OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
                            O00OOOO0OOOO0OOO0 ={"packsackItemId":O000O0OO0OOO000O0 ,"price":str (O00O0OO0O0O0OO000 )[:5 ],"quantity":str (O0O0O0OO00O0O0OO0 )}#line:345
                            O000OO00O0OO0O0OO =requests .request ('post',f'{host}/market/sale',headers =O0OOO000000O0O0OO ,data =O00OOOO0OOOO0OOO0 ).json ()#line:346
                            if 'status'in O000OO00O0OO0O0OO :#line:348
                                if O000OO00O0OO0O0OO ['status']==200 :#line:349
                                    print (f'【上架芦荟】:数量:{O0O0O0OO00O0O0OO0}丨价格:{str(O00O0OO0O0O0OO000)[:5]}')#line:350
                                if O000OO00O0OO0O0OO ['status']==500 :#line:351
                                    print (f'【上架芦荟】:{O000OO00O0OO0O0OO["message"]}')#line:352
        except Exception as O0000000O0000O0O0 :#line:353
            print (O0000000O0000O0O0 )#line:354
    def query_to_sell (OO0000O00OO0OO0OO ):#line:357
        global count_list #line:358
        try :#line:359
            OOOOOOO0OOOO000O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:360
            O00OOO000O0O000O0 ={'source':'scsc','authorization':OO0000O00OO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOOO000O0 ),'signstring':OOOOOOO0OOOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:371
            OOO0O0O0000O000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OOO000O0O000O0 ).json ()#line:372
            if 'status'in OOO0O0O0000O000O0 :#line:374
                if OOO0O0O0000O000O0 ['status']==200 :#line:375
                    for OO0O000OOOOOOO0O0 in OOO0O0O0000O000O0 ['data']['rows']:#line:376
                        OOOOOO0OO00000OO0 =OO0O000OOOOOOO0O0 ['materialKey']#line:377
                        O0O0000OOO0000O0O =OO0O000OOOOOOO0O0 ['quantity']#line:378
                        OOOOOOO00OOOOOOOO =OO0O000OOOOOOO0O0 ['price']#line:379
                        OOOOOOO00O0OOO0O0 =OO0O000OOOOOOO0O0 ['saleState']#line:380
                        if OOOOOOO00O0OOO0O0 ==0 :#line:381
                            print (f'【出售订单】:名称:{OOOOOO0OO00000OO0}丨数量:{O0O0000OOO0000O0O}丨价格:{OOOOOOO00OOOOOOOO}')#line:382
                            count_list +=O0O0000OOO0000O0O #line:383
                            OOOOOO0000OOOOOO0 =OO0000O00OO0OO0OO .the_query ()#line:385
                            if float (OOOOOO0000OOOOOO0 )!=float (OOOOOOO00OOOOOOOO ):#line:386
                                OO0000OOOOO00OO0O =OO0O000OOOOOOO0O0 ['id']#line:387
                                OO0000O00OO0OO0OO .cacel_sale (OO0000OOOOO00OO0O )#line:388
                    OO0000O00OO0OO0OO .game_map ()#line:390
        except Exception as OOOO0O0O0O0000O0O :#line:392
            print (OOOO0O0O0O0000O0O )#line:393
    def cacel_sale (OOOOOOOOOOO00O000 ,OOO0OO00O000OO00O ):#line:396
        try :#line:397
            OOO0O0OO00O0OOO0O =f'_saleId={OOO0OO00O000OO00O}_{timi_new()}'#line:398
            O000O0OOO0OOOO00O ={'source':'scsc','authorization':OOOOOOOOOOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO00O0OOO0O ),'signstring':OOO0O0OO00O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            O0OOOO00OOO00OO0O ={"saleId":OOO0OO00O000OO00O }#line:410
            O00000OOO0OOOO000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O000O0OOO0OOOO00O ,data =O0OOOO00OOO00OO0O ).json ()#line:411
            if 'status'in O00000OOO0OOOO000 :#line:413
                if O00000OOO0OOOO000 ['status']==200 :#line:414
                    print (f'【下架出售】:{O00000OOO0OOOO000["data"]}')#line:415
        except Exception as OOO0OO0000OOO0O00 :#line:416
            print (OOO0OO0000OOO0O00 )#line:417
    def change_nickname (O0O0OOOO000OOOOOO ):#line:420
        try :#line:421
            O0OOO0OOO000OO0OO =timi_new ()#line:422
            O00O0O000O000O0OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:423
            O00O00OO0O00O0O0O =requests .request ('post','https://www.qmsjmfb.com/',data =O00O0O000O000O0OO ).text #line:424
            O0OO0O0O00OOOO0OO =re .findall ('<ul><li>(.*?)</li>',O00O00OO0O00O0O0O )[0 ][:3 ]#line:425
            O0OO000OOO000OO0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0OO0O0O00OOOO0OO}').json ()#line:426
            O000000OO0OOO0O0O =O0OO000OOO000OO0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:427
            O0OO0O00O0OOO00O0 ={"nickname":O000000OO0OOO0O0O }#line:428
            O000O0OOOO0OOO000 =f'_nickname={O000000OO0OOO0O0O}_{O0OOO0OOO000OO0OO}'#line:429
            O0000O0O0000OO000 ={'source':'scsc','authorization':O0O0OOOO000OOOOOO .token ,'timestamp':O0OOO0OOO000OO0OO ,'sign':sign (O000O0OOOO0OOO000 ),'signstring':O000O0OOOO0OOO000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:440
            O0000OO00OOOOOO00 =requests .request ('patch',f'{host}/user/nickname',headers =O0000O0O0000OO000 ,data =O0OO0O00O0OOO00O0 ).json ()#line:441
            if 'status'in O0000OO00OOOOOO00 :#line:443
                if O0000OO00OOOOOO00 ['status']==200 :#line:444
                    print (f'【修改网名】:网名:{O000000OO0OOO0O0O}丨{O0000OO00OOOOOO00["message"]}')#line:445
        except Exception as O0O00OO000O0O00O0 :#line:446
            print (O0O00OO000O0O00O0 )#line:447
    def withdraw (OO0O0O00000O0OO00 ):#line:450
        try :#line:451
            O0O00OOOO000O0000 =f'__{timi_new()}'#line:452
            O0O00000OO0OOO000 ={'source':'scsc','authorization':OO0O0O00000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO000O0000 ),'signstring':O0O00OOOO000O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O000OO000OO00O0OO =requests .request ('get',f'{host}/assets',headers =O0O00000OO0OOO000 ).json ()#line:464
            if 'status'in O000OO000OO00O0OO :#line:466
                if O000OO000OO00O0OO ['status']==200 :#line:467
                    OO0OOO00O0O0OOO0O =O000OO000OO00O0OO ['data']['cash']#line:468
                    if float (OO0OOO00O0O0OOO0O )>20 :#line:469
                        O0O00OOOO000O0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:470
                        O0O00000OO0OOO000 ={'authorization':OO0O0O00000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO000O0000 ),'signstring':O0O00OOOO000O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
                        OO000OOOO00O0OOO0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:481
                        OOOOO00OO0OOOOO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00000OO0OOO000 ,data =OO000OOOO00O0OOO0 ).json ()#line:483
                        if 'status'in OOOOO00OO0OOOOO00 :#line:485
                            if OOOOO00OO0OOOOO00 ['status']==200 :#line:486
                                print (f'【余额提现】:{OOOOO00OO0OOOOO00["data"]}')#line:487
                        if 'status'in OOOOO00OO0OOOOO00 :#line:488
                            if OOOOO00OO0OOOOO00 ['status']==500 :#line:489
                                print (f'【余额提现】:{OOOOO00OO0OOOOO00["message"]}')#line:490
        except Exception as O00O0OOO0OO00O00O :#line:491
            print (O00O0OOO0OO00O00O )#line:492
    def invitenum (OO000O0OOO00O00OO ):#line:495
        global invited_new #line:496
        try :#line:497
            O0OO000O0O000000O =f'__{timi_new()}'#line:498
            OOOOOOOOO0OOO0000 ={'source':'scsc','authorization':OO000O0OOO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O000000O ),'signstring':O0OO000O0O000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:509
            O0OO0OO000OO000OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOOOOOO0OOO0000 ).json ()#line:510
            if 'status'in O0OO0OO000OO000OO :#line:512
                if O0OO0OO000OO000OO ['status']==200 :#line:513
                    O0OO00OOO000OO000 =O0OO0OO000OO000OO ['data']['invited_count']#line:514
                    OO00O000OO000OO0O =O0OO0OO000OO000OO ['data']['invited_second_count']#line:515
                    print (f'【我的邀请】:直邀好友:{O0OO00OOO000OO000}丨间邀好友:{OO00O000OO000OO0O}')#line:516
                    if O0OO00OOO000OO000 <2 :#line:517
                        O000O0000OO0O0O0O =f'__{timi_new()}'#line:518
                        OO0O000O000O0O0OO ={'source':'scsc','authorization':OO000O0OOO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000OO0O0O0O ),'signstring':O000O0000OO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                        OO0OO0OO0OO00O0O0 =requests .request ('get',f'{host}/user',headers =OO0O000O000O0O0OO ).json ()#line:530
                        if 'status'in OO0OO0OO0OO00O0O0 :#line:532
                            if OO0OO0OO0OO00O0O0 ['status']==200 :#line:533
                                invited_new .append (OO0OO0OO0OO00O0O0 ['data']['inner_id'])#line:534
        except Exception as O000OO00000O0000O :#line:535
            print (O000OO00000O0000O )#line:536
    def game_map (O0000000O0O000OOO ):#line:539
        try :#line:540
            OOOO0O00O0OO0O0OO =f'__{timi_new()}'#line:541
            O000O0O0OOO0O0O0O ={'source':'scsc','authorization':O0000000O0O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0OO0O0OO ),'signstring':OOOO0O00O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            OO000000O0000OOO0 =requests .request ('get',f'{host}/game/map',headers =O000O0O0OOO0O0O0O ).json ()#line:553
            if 'status'in OO000000O0000OOO0 :#line:555
                if OO000000O0000OOO0 ['status']==200 :#line:556
                    for OO0O0OOO00OOO0O0O in OO000000O0000OOO0 ['data']['list'][0 ]['crops']:#line:557
                        OOO0000OO0O0O0OO0 =OO0O0OOO00OOO0O0O ['level']#line:559
                        if OOO0000OO0O0O0OO0 ==41 :#line:560
                            OO00OOOO000OOOO0O =OO0O0OOO00OOO0O0O ['crop_name']#line:561
                            OOO0O000OOO0O000O =OO0O0OOO00OOO0O0O ['count']#line:562
                            if OOO0O000OOO0O000O >0 :#line:563
                                print (f'【农业资产】:{OO00OOOO000OOOO0O}丨数量:{OOO0O000OOO0O000O}')#line:564
                                O0OO0OO00000O0000 =O0000000O0O000OOO .the_query ()#line:565
                                O0000000O0O000OOO .market_sale (O0OO0OO00000O0000 )#line:566
        except Exception as OOO0O00O000OOO00O :#line:567
            print (OOO0O00O000OOO00O )#line:568
    def give_gold (OO0000O0OO0OOO0OO ):#line:571
        try :#line:572
            O000OO00000OOOO0O =f'__{timi_new()}'#line:573
            OOO0OOOO0OO0OOO00 ={'source':'scsc','authorization':OO0000O0OO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00000OOOO0O ),'signstring':O000OO00000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
            OO0000O00OOOO00O0 =requests .request ('get',f'{host}/user',headers =OOO0OOOO0OO0OOO00 ).json ()#line:585
            if 'status'in OO0000O00OOOO00O0 :#line:586
                if OO0000O00OOOO00O0 ['status']==200 :#line:587
                    if float (OO0000O0OO0OOO0OO .doneeNo )!=0 :#line:588
                        OO0O0000OOO0OO00O =OO0000O00OOOO00O0 ['data']['assets']['gold']#line:589
                        if float (OO0O0000OOO0OO00O )>float (OO0000O0OO0OOO0OO .innerId ):#line:590
                            OOOOO0OO00O00O0OO =int (float (OO0O0000OOO0OO00O )/1.1 )#line:591
                            O000OO00000OOOO0O =f'_doneeNo={OO0000O0OO0OOO0OO.doneeNo}&quantity={OOOOO0OO00O00O0OO}_{timi_new()}'#line:592
                            OOO0OOOO0OO0OOO00 ={'source':'scsc','authorization':OO0000O0OO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00000OOOO0O ),'signstring':O000OO00000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:603
                            OOO0OO0000OOO0OO0 ={"quantity":OOOOO0OO00O00O0OO ,"doneeNo":OO0000O0OO0OOO0OO .doneeNo }#line:607
                            O000O00OOOOO000OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOOO0OO0OOO00 ,data =OOO0OO0000OOO0OO0 ).json ()#line:608
                            if 'status'in O000O00OOOOO000OO :#line:610
                                if O000O00OOOOO000OO ['status']==200 :#line:611
                                    if O000O00OOOOO000OO ['data']:#line:612
                                        print (f'【赠送种子】:赠送{OOOOO0OO00O00O0OO}种子给{OO0000O0OO0OOO0OO.doneeNo}成功')#line:613
                    else :#line:614
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:615
        except Exception as OOOOO00O0O0000OO0 :#line:616
            print (OOOOO00O0O0000OO0 )#line:617
    def invitation (OOOOO000OOO0OO0OO ):#line:619
        try :#line:620
            _O0O0OO0O000O0O0O0 =float (bundled_def ())/4 #line:621
            O00O000O00000O000 =f'_innerId={int(_O0O0OO0O000O0O0O0)}_{timi_new()}'#line:623
            O0OO0OO000OO00OOO ={'source':'scsc','authorization':OOOOO000OOO0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O00000O000 ),'signstring':O00O000O00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OOOO0OO00000O0OO0 ={"innerId":int (_O0O0OO0O000O0O0O0 )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OO0OO000OO00OOO ,data =OOOO0OO00000O0OO0 )#line:636
        except Exception as OOOOO0O0O00OOO000 :#line:637
            print (OOOOO0O0O00OOO000 )#line:638
    def winning_rewards (O000OOO00O0O0OO0O ):#line:641
        try :#line:642
            OO0000OO0OOO0O00O =f'__{timi_new()}'#line:643
            O00O0OOO00000OO00 ={'source':'scsc','authorization':O000OOO00O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO0OOO0O00O ),'signstring':OO0000OO0OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            OO0O0O0000O0OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O0OOO00000OO00 ).json ()#line:655
            if 'status'in OO0O0O0000O0OOO0O :#line:657
                if OO0O0O0000O0OOO0O ['status']==200 :#line:658
                    if OO0O0O0000O0OOO0O ['data']['amount']:#line:659
                        OO0000OOO00OO0000 =OO0O0O0000O0OOO0O ['data']['amount']['gold']#line:660
                        return OO0000OOO00OO0000 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as O00OOO000OOOOO0O0 :#line:664
            print (O00OOO000OOOOO0O0 )#line:665
    def certification (O000OO0000OO00O00 ):#line:668
        try :#line:669
            OOOOOOOO00OO00OO0 =f'__{timi_new()}'#line:670
            O0OO000OO000OOOO0 ={'source':'scsc','authorization':O000OO0000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO00OO00OO0 ),'signstring':OOOOOOOO00OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            O0OO0OO00OOOO00OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO000OO000OOOO0 ).json ()#line:682
            if 'status'in O0OO0OO00OOOO00OO :#line:684
                if O0OO0OO00OOOO00OO ['status']==200 :#line:685
                    if O0OO0OO00OOOO00OO ['data']['result']:#line:686
                        O0O00OOO00O0OOOOO =O0OO0OO00OOOO00OO ['data']['nick_name']#line:687
                        return O0O00OOO00O0OOOOO #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as O0O0OO0OO000000OO :#line:691
            print (O0O0OO0OO000000OO )#line:692
    def crops_illustrated (OO00000O0O0O0OO00 ):#line:695
        try :#line:696
            OO0OO000OOO0000O0 =f'__{timi_new()}'#line:697
            O0000000OO0OOO0OO ={'source':'scsc','authorization':OO00000O0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOO0000O0 ),'signstring':OO0OO000OOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            O0OOO00O000O00OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0000000OO0OOO0OO ).json ()#line:709
            if 'status'in O0OOO00O000O00OO0 :#line:711
                if O0OOO00O000O00OO0 ['status']==200 :#line:712
                    OOO0000000O000O0O =O0OOO00O000O00OO0 ['data'][0 ]['crops']#line:713
                    for OOO000O0OO0O00OOO in OOO0000000O000O0O :#line:714
                        if OOO000O0OO0O00OOO ['ill_clover_award']:#line:715
                            if float (OOO000O0OO0O00OOO ['ill_clover_award'])>1 :#line:716
                                if OOO000O0OO0O00OOO ['is_finish']:#line:717
                                    if not OOO000O0OO0O00OOO ['is_getit']:#line:718
                                        if OO00000O0O0O0OO00 .certification ()!='未实名':#line:719
                                            OO0OO000OOO0000O0 =f'_award_level={OOO000O0OO0O00OOO["level"]}_{timi_new()}'#line:720
                                            O0000000OO0OOO0OO ={'source':'scsc','authorization':OO00000O0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OOO0000O0 ),'signstring':OO0OO000OOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            OOOOOO00OOO000OO0 ={"award_level":OOO000O0OO0O00OOO ['level']}#line:732
                                            O00000O0OO0OOO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0000000OO0OOO0OO ,json =OOOOOO00OOO000OO0 ).json ()#line:734
                                            if 'status'in O00000O0OO0OOO0O0 :#line:735
                                                if O00000O0OO0OOO0O0 ['status']==200 :#line:736
                                                    O000O0OO000OOOO0O =O00000O0OO0OOO0O0 ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{OOO000O0OO0O00OOO["crop_name"]}成就丨奖励{O000O0OO000OOOO0O}☘️')#line:739
                                                if O00000O0OO0OOO0O0 ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{O00000O0OO0OOO0O0["message"]}')#line:741
        except Exception as OO0OOOOOOO00OOO00 :#line:742
            print (OO0OOOOOOO00OOO00 )#line:743
    def watched_ad (OO0OOO0O0OOOO0O0O ):#line:746
        try :#line:747
            O00O00O00O00O0OO0 =f'__{timi_new()}'#line:748
            OOO00O0OO0OOOO00O ={'source':'scsc','authorization':OO0OOO0O0OOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00O00O0OO0 ),'signstring':O00O00O00O00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            OO00O00OOOOOOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0OO0OOOO00O ).json ()#line:760
            if 'status'in OO00O00OOOOOOO0OO :#line:762
                if OO00O00OOOOOOO0OO ['status']==200 :#line:763
                    if 'offlineInfo'in OO00O00OOOOOOO0OO ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        O0O000OO0OOO0OO0O =OO00O00OOOOOOO0OO ['data']['offlineInfo']['off_minute']#line:766
                        OO000O00OO000O000 =float (OO00O00OOOOOOO0OO ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO00O0OO0OOOO00O ).json ()#line:769
                        time .sleep (2 )#line:770
                        O0O00000OO000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0OO0OOOO00O ).json ()#line:771
                        if 'status'in O0O00000OO000OOO0 :#line:773
                            if O0O00000OO000OOO0 ['status']==200 :#line:774
                                O0O0O0OOOO0000O0O =float (O0O00000OO000OOO0 ['data']['silver'])/1000000000000 #line:775
                                O0OO00O0OOO0O0O0O =str (O0O0O0OOOO0000O0O -OO000O00OO000O000 )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{O0O000OO0OOO0OO0O}分钟奖励🌱数量:{O0OO00O0OOO0O0O0O}t粒')#line:777
        except Exception as OO0OO0OOOO000000O :#line:778
            print (OO0OO0OOOO000000O )#line:779
    def user_ad (OOO000O0O00O0OOOO ):#line:782
        try :#line:783
            OOOO0OO00OOOO00OO =f'__{timi_new()}'#line:784
            O000000OOO0OO0OO0 ={'source':'scsc','authorization':OOO000O0O00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00OOOO00OO ),'signstring':OOOO0OO00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            O0O000O00000OOO00 =requests .request ('get',f'{host}/user/ad',headers =O000000OOO0OO0OO0 ).json ()#line:796
            if 'status'in O0O000O00000OOO00 :#line:798
                if O0O000O00000OOO00 ['status']==200 :#line:799
                    OO00OOO0000OOO00O =O0O000O00000OOO00 ['data']['max_time']#line:800
                    O0OOOO000O0OO0O0O =O0O000O00000OOO00 ['data']['watch_time']#line:801
                    O0O00O0000000000O =O0O000O00000OOO00 ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{O0O00O0000000000O + OO00OOO0000OOO00O - O0OOOO000O0OO0O0O}次丨好友提供:{O0O00O0000000000O}次')#line:803
                    if O0O00O0000000000O +OO00OOO0000OOO00O -O0OOOO000O0OO0O0O >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        OOO000OO00O0O00O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000000OOO0OO0OO0 ).json ()#line:806
                        if 'status'in OOO000OO00O0O00O0 :#line:808
                            if OOO000OO00O0O00O0 ['status']==200 :#line:809
                                OOO0OOO000OO00OOO =float (OOO000OO00O0O00O0 ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(OOO0OOO000OO00OOO)}t粒')#line:811
                                return True #line:812
                            if OOO000OO00O0O00O0 ['status']==500 :#line:813
                                OO000OO0O0OO000OO =OOO000OO00O0O00O0 ['message']#line:814
                                print (f'【获取种子】:{OO000OO0O0OO000OO}')#line:815
                                return False #line:816
        except Exception as OOOO0OOOOOO0O000O :#line:817
            print (OOOO0OOOOOO0O000O )#line:818
    def synthetic (O000OOOO00O0O0000 ):#line:821
        global id ,g #line:822
        try :#line:823
            OOO0OOOOOOO00O000 =O000OOOO00O0O0000 .level_new ()#line:824
            OO0OO00OO00OO00O0 =random .randint (9 ,11 )#line:825
            O0OOO000OO0O0OO00 =f'_site=8&targetSite={OO0OO00OO00OO00O0}_{timi_new()}'#line:826
            OO0O00O00O0O00OO0 ={'source':'scsc','authorization':O000OOOO00O0O0000 .token ,'timestamp':timi_new (),'sign':sign (O0OOO000OO0O0OO00 ),'signstring':O0OOO000OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            O000O00OOOOO0O00O ={"site":int (8 ),"targetSite":int (OO0OO00OO00OO00O0 )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00O00O0O00OO0 ,json =O000O00OOOOO0O00O )#line:839
            while True :#line:840
                OO0OOOO0O00O0O0OO =f'__{timi_new()}'#line:841
                O0OO00OOOO0OO0000 ={'source':'scsc','authorization':O000OOOO00O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O00O0O0OO ),'signstring':OO0OOOO0O00O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                OO00OO0O00OOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00OOOO0OO0000 ).json ()#line:853
                if 'status'in OO00OO0O00OOOO0O0 :#line:855
                    if OO00OO0O00OOOO0O0 ['status']==200 :#line:856
                        OO0O0OOO000OO0O00 =OO00OO0O00OOOO0O0 ['data']['cropList']#line:857
                        OOOOOO0OOO000000O =OO00OO0O00OOOO0O0 ['data']['gameCoreDataDBid']#line:858
                        O000OOO0OOOOO00O0 =float (OO00OO0O00OOOO0O0 ['data']['silver'])/1000000000000 #line:859
                        OOO0OOO0OO00O0OOO =0 #line:864
                        for OOOOO0O0OO0000OO0 in OO0O0OOO000OO0O00 :#line:865
                            if not OOOOO0O0OO0000OO0 :#line:866
                                OOO0OOO00O0OO00O0 =f'_crop_id={OOOOOO0OOO000000O}&site={OOO0OOO0OO00O0OOO}_{O000OOOO00O0O0000.time}'#line:867
                                OO0OOO000OOOO0OOO ={'source':'scsc','authorization':O000OOOO00O0O0000 .token ,'timestamp':O000OOOO00O0O0000 .time ,'sign':sign (OOO0OOO00O0OO00O0 ),'signstring':OOO0OOO00O0OO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                OOOO0O0OOO00OOOO0 ={"site":OOO0OOO0OO00O0OOO ,"crop_id":OOOOOO0OOO000000O }#line:878
                                OOOOO0000O00OO0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OOO000OOOO0OOO ,data =OOOO0O0OOO00OOOO0 ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in OOOOO0000O00OO0OO :#line:882
                                    if OOOOO0000O00OO0OO ['status']==200 :#line:883
                                        if OOOOO0000O00OO0OO ['message']=='种子数量不足':#line:884
                                            OOO0OOOOOOO00O000 =O000OOOO00O0O0000 .level_new ()#line:885
                                            print (f'【种植合成】:{OOOOO0000O00OO0OO["message"]}')#line:886
                                            if not O000OOOO00O0O0000 .user_ad ():#line:887
                                                return False #line:888
                                    if OOOOO0000O00OO0OO ['status']==500 :#line:889
                                        print (f'【种植合成】:{OOOOO0000O00OO0OO["message"]}')#line:890
                                        return False #line:891
                            OOO0OOO0OO00O0OOO +=1 #line:892
                        O0OO0000O000O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00OOOO0OO0000 ).json ()#line:893
                        O0OOOO000O000O000 =O0OO0000O000O0OOO ['data']['cropList']#line:894
                        O0O0O000O0O00O000 =False #line:895
                        for OOOOO0O0OO0000OO0 in range (12 ):#line:896
                            id =O0OOOO000O000O000 [OOOOO0O0OO0000OO0 ]['level']#line:897
                            if float (OOO0OOOOOOO00O000 )-float (id )>9 :#line:898
                                O00O00000000O0OOO =f'_site={OOOOO0O0OO0000OO0}_{timi_new()}'#line:899
                                OOOOOOOOOOO0O0O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOOO00O0O0000 .token ,'timestamp':timi_new (),'sign':sign (O00O00000000O0OOO ),'signstring':O00O00000000O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                O0OO00OOOOOOO0OO0 ={"site":OOOOO0O0OO0000OO0 }#line:911
                                OOO00OOOO00O00O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOOOOOOO0O0O0O ,data =O0OO00OOOOOOO0OO0 ).json ()#line:913
                                if 'status'in OOO00OOOO00O00O00 :#line:914
                                    if OOO00OOOO00O00O00 ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O0OOOO0O00OO0OOOO in range (11 ):#line:918
                                    O000OOOO0OO00O000 =O0OOOO0O00OO0OOOO +1 #line:919
                                    g =O0OOOO000O000O000 [O000OOOO0OO00O000 ]['level']#line:920
                                    if id ==g :#line:921
                                        O00O0O0O0O0O00O00 =O0OOOO0O00OO0OOOO +2 #line:922
                                        if O00O0O0O0O0O00O00 !=OOOOO0O0OO0000OO0 +1 :#line:923
                                            O0OOOO000OO0OOO00 =OOOOO0O0OO0000OO0 +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            O0OOO000OO0O0OO00 =f'_site={O0OOOO000OO0OOO00 - 1}&targetSite={O00O0O0O0O0O00O00 - 1}_{timi_new()}'#line:927
                                            OO0O00O00O0O00OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOOO00O0O0000 .token ,'timestamp':timi_new (),'sign':sign (O0OOO000OO0O0OO00 ),'signstring':O0OOO000OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            O00O00O0O0000O00O ={"site":int (O0OOOO000OO0OOO00 -1 ),"targetSite":int (O00O0O0O0O0O00O00 -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00O00O0O00OO0 ,json =O00O00O0O0000O00O )#line:946
                                            O0O0O000O0O00O000 =True #line:948
                                    if O0O0O000O0O00O000 :#line:949
                                        break #line:950
                                if O0O0O000O0O00O000 :#line:951
                                    break #line:952
        except :#line:953
            O000OOOO00O0O0000 .synthetic ()#line:954
    def level_new (O000O00OOO0O0OOOO ):#line:957
        try :#line:958
            O0OOO0OO00OO00OO0 =f'__{timi_new()}'#line:959
            O0O0O0000O0OO0000 ={'source':'scsc','authorization':O000O00OOO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00OO00OO0 ),'signstring':O0OOO0OO00OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            OOO00OO0O00OO0OOO =requests .request ('get',f'{host}/user',headers =O0O0O0000O0OO0000 ).json ()#line:971
            if 'status'in OOO00OO0O00OO0OOO :#line:972
                if OOO00OO0O00OO0OOO ['status']==200 :#line:973
                    return float (OOO00OO0O00OO0OOO ['data']['level'])#line:974
        except Exception as O00O0O0OOO0O000OO :#line:975
            print (O00O0O0OOO0O000OO )#line:976
    def propsraffle (OO00O0O000O000O0O ):#line:979
        try :#line:980
            while True :#line:981
                OOO00OOOO000000O0 =f'__{timi_new()}'#line:982
                O0OO0OO0000O0O0OO ={'source':'scsc','authorization':OO00O0O000O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO000000O0 ),'signstring':OOO00OOOO000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                OO0OOOOO0OOO0O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0OO0000O0O0OO ).json ()#line:994
                if 'status'in OO0OOOOO0OOO0O00O :#line:996
                    if OO0OOOOO0OOO0O00O ['status']==200 :#line:997
                        OO000O0O00O00OOOO =OO0OOOOO0OOO0O00O ['data']['rows']#line:998
                        OOOOO000O0OO000O0 =OO0OOOOO0OOO0O00O ['data']['vstate']#line:999
                        if OO000O0O00O00OOOO ==5 or OO000O0O00O00OOOO ==6 or OO000O0O00O00OOOO ==7 :#line:1000
                            OO0OOOOOO0OOO0OOO =OO0OOOOO0OOO0O00O ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{OO0OOOOOO0OOO0OOO}')#line:1002
                        if OO000O0O00O00OOOO ==1 or OO000O0O00O00OOOO ==2 or OO000O0O00O00OOOO ==3 :#line:1003
                            O0O000O0OOO0000OO =OO0OOOOO0OOO0O00O ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O0O000O0OOO0000OO}')#line:1005
                        if OO000O0O00O00OOOO ==4 or OO000O0O00O00OOOO ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if OO000O0O00O00OOOO =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as OO0000000000OO0OO :#line:1047
            print (OO0000000000OO0OO )#line:1048
    def friends_invitation (O0O000000OO0O0O0O ):#line:1051
        try :#line:1052
            OOOO00000OOO0OO0O =f'__{timi_new()}'#line:1053
            OOOOOO0000OO0OO00 ={'source':'scsc','authorization':O0O000000OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000OOO0OO0O ),'signstring':OOOO00000OOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            OOO00O0OOO0O0OOO0 =requests .request ('get',f'{host}/friends',headers =OOOOOO0000OO0OO00 ).json ()#line:1065
            if 'status'in OOO00O0OOO0O0OOO0 :#line:1066
                if OOO00O0OOO0O0OOO0 ['status']==200 :#line:1067
                    O00O000OO0O0OO000 =OOO00O0OOO0O0OOO0 ['data']['myInviteter']#line:1068
                    if O00O000OO0O0OO000 :#line:1069
                        OOOO000000OOO0OO0 =O00O000OO0O0OO000 ['user']['nickname']#line:1070
                        OOO0O0000OO00OOO0 =O0O000000OO0O0O0O .certification ()#line:1071
                        if OOO0O0000OO00OOO0 =='未实名':#line:1072
                            weishim .append (O0O000000OO0O0O0O .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{OOOO000000OOO0OO0}丨实名:{OOO0O0000OO00OOO0}')#line:1074
        except Exception as OOO0000000OO00OOO :#line:1078
            print (OOO0000000OO00OOO )#line:1079
    def add_clover (O0000OO0OO0000OOO ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            O0O00O0OOO00O0OO0 =f'__{timi_new()}'#line:1085
            OOO000OOOO00OO000 ={'source':'scsc','authorization':O0000OO0OO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO00O0OO0 ),'signstring':O0O00O0OOO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OOOOOOO00O0000O0O =requests .request ('get',f'{host}/assets/clovers',headers =OOO000OOOO00OO000 ).json ()#line:1097
            if 'status'in OOOOOOO00O0000O0O :#line:1099
                if OOOOOOO00O0000O0O ['status']==200 :#line:1100
                    OOO00O00OO0OO0000 =OOOOOOO00O0000O0O ['data']['clover']#line:1101
                    O0OO000000OO0OOO0 =OOOOOOO00O0000O0O ['data']['used_clover']#line:1102
                    O0OOO0000OO00OOO0 =float (OOO00O00OO0OO0000 )-float (O0OO000000OO0OOO0 )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO000000OO0OOO0}')#line:1104
                    if O0000OO0OO0000OOO .certification ()!='未实名':#line:1105
                        if O0OOO0000OO00OOO0 >1 :#line:1106
                            O0O00O0OOO00O0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO0000OO00OOO0)}_{timi_new()}'#line:1107
                            OOO00000OOOOO0000 ={'source':'scsc','authorization':O0000OO0OO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO00O0OO0 ),'signstring':O0O00O0OOO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            OOO0O0OOO0O00O0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO0000OO00OOO0 )}#line:1119
                            O000O0O0OOO0OOOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00000OOOOO0000 ,data =OOO0O0OOO0O00O0OO ).json ()#line:1120
                            if 'status'in O000O0O0OOO0OOOO0 :#line:1122
                                if O000O0O0OOO0OOOO0 ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O000O0O0OOO0OOOO0["data"]["isSuccess"]}丨数量:{O0OOO0000OO00OOO0}')#line:1124
                                if O000O0O0OOO0OOOO0 ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O000O0O0OOO0OOOO0["message"]}')#line:1126
            O00OO0OOO0O0OOOO0 =requests .request ('get',f'{host}/lottery',headers =OOO000OOOO00OO000 ).json ()#line:1127
            O00OOO000O00OO0O0 =O0000OO0OO0000OOO .winning_rewards ()#line:1129
            if 'status'in O00OO0OOO0O0OOOO0 :#line:1130
                if O00OO0OOO0O0OOOO0 ['status']==200 :#line:1131
                    OO0OO0OO0O0O0OOO0 =O00OO0OOO0O0OOOO0 ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (OO0OO0OO0O0O0OOO0 )#line:1133
                    OOO0000OOO0OO0O0O =O00OO0OOO0O0OOOO0 ['data'][1 ]['value']#line:1134
                    OOO00O00O000O0O0O =O00OO0OOO0O0OOOO0 ['data'][0 ]['join_number']#line:1135
                    OOOO0OOOOOO0O00O0 =int (float (O00OO0OOO0O0OOOO0 ['data'][0 ]['totalValue']))#line:1136
                    O0OOO0000OOOO00OO =float (OOO0000OOO0OO0O0O /OOOO0OOOOOO0O00O0 )*10000 #line:1137
                    OO000OOO0O00O0OO0 =OOOO0OOOOOO0O00O0 /OOO00O00O000O0O0O #line:1138
                    print (f'【参与抽奖】:预计每天中{str(OO0OO0OO0O0O0OOO0)[:6]}颗金种子丨好友收益:{str(O00OOO000O00OO0O0)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO0000OOOO00OO)[:6]}颗金种子丨☘️人均:{str(OO000OOO0O00O0OO0)[:7]}️')#line:1140
        except Exception as OO0O0OO00O0O0O00O :#line:1141
            print (OO0O0OO00O0O0O00O )#line:1142
    def energy (O00000000O00000O0 ):#line:1145
        try :#line:1146
            while True :#line:1147
                OOOOO0O0OOO0O000O =f'__{timi_new()}'#line:1148
                O00OOOO0000O00OOO ={'source':'scsc','authorization':O00000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O0OOO0O000O ),'signstring':OOOOO0O0OOO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                OO0OO0000000OO0O0 =requests .request ('get',f'{host}/energy/general',headers =O00OOOO0000O00OOO ).json ()#line:1160
                if 'status'in OO0OO0000000OO0O0 :#line:1162
                    if OO0OO0000000OO0O0 ['status']==200 :#line:1163
                        OO000OOOO0OOO0O00 =OO0OO0000000OO0O0 ['data']['ordinary_water']#line:1164
                        O0OOO000O000OO000 =OO0OO0000000OO0O0 ['data']['ordinary_fertilizer']#line:1165
                        OOOO00O0O0000O00O =OO0OO0000000OO0O0 ['data']['videoStatus']#line:1166
                        OO0O0O0O0O0O0O000 =OO0OO0000000OO0O0 ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(O0OOO000O000OO000).split(".")[0]}丨水滴:{str(OO000OOOO0OOO0O00).split(".")[0]}')#line:1169
                        if float (O0OOO000O000OO000 )<96 :#line:1170
                            if OOOO00O0O0000O00O :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OO000OOOOO0000O00 =99 -float (O0OOO000O000OO000 )#line:1173
                                OO0O0000000O0000O ={"fertilizer":str (OO000OOOOO0000O00 ).split ('.')[0 ]}#line:1174
                                O000OOOOO00000O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OOOO0000O00OOO ).json ()#line:1176
                                if 'status'in O000OOOOO00000O0O :#line:1178
                                    if O000OOOOO00000O0O ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOOOO00000O0O["message"]}')#line:1180
                                    if O000OOOOO00000O0O ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOOOO00000O0O["message"]}')#line:1182
                                        break #line:1183
                                if float (O0OOO000O000OO000 )<78 :#line:1185
                                    OO000OOOOO0000O00 =80 -float (O0OOO000O000OO000 )#line:1186
                                    OOO00O0OO00OO000O =f'_fertilizer={int(OO000OOOOO0000O00)}_{timi_new()}'#line:1187
                                    OOOO0OOO000OOO0O0 ={'source':'scsc','authorization':O00000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO00OO000O ),'signstring':OOO00O0OO00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    OOO00OO0O0O0OO0O0 ={"fertilizer":int (OO000OOOOO0000O00 )}#line:1199
                                    OO0O0O0000O0OOOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0OOO000OOO0O0 ,data =OOO00OO0O0O0OO0O0 ).json ()#line:1201
                                    if 'status'in OO0O0O0000O0OOOO0 :#line:1203
                                        if OO0O0O0000O0OOOO0 ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OO0O0O0000O0OOOO0["message"]}丨数量:{int(OO000OOOOO0000O00)}')#line:1205
                                        if OO0O0O0000O0OOOO0 ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OO0O0O0000O0OOOO0["message"]}丨数量:{int(OO000OOOOO0000O00)}')#line:1207
                                            OO0000O00000OO0O0 =OO0O0O0000O0OOOO0 ["message"].split ('-')[1 ]#line:1208
                                            O00OOOO0000O0OOOO =f'__{timi_new()}'#line:1209
                                            OO00000OOO0OOOO00 ={'source':'scsc','authorization':O00000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0000O0OOOO ),'signstring':O00OOOO0000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            OO0O0000OOOOOO000 =requests .request ('get',f'{host}/user',headers =OO00000OOO0OOOO00 ).json ()#line:1221
                                            if 'status'in OO0O0000OOOOOO000 :#line:1222
                                                if OO0O0000OOOOOO000 ['status']==200 :#line:1223
                                                    O0OOOOO0OOOOO00O0 =OO0O0000OOOOOO000 ['data']['inner_id']#line:1224
                                                    if give_gold (O0OOOOO0OOOOO00O0 ,float (OO0000O00000OO0O0 )+1 ):#line:1225
                                                        O00000000O00000O0 .energy ()#line:1226
                        if float (OO000OOOO0OOO0O00 )<880 :#line:1227
                            if OO0O0O0O0O0O0O000 :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O000OOOOO00OOOOO0 =999 -float (OO000OOOO0OOO0O00 )#line:1230
                                OO0OO0OOO0O0OO000 ={"water":str (O000OOOOO00OOOOO0 ).split ('.')[0 ]}#line:1231
                                OOO0OOOO000O0000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OOOO0000O00OOO ).json ()#line:1233
                                if 'status'in OOO0OOOO000O0000O :#line:1235
                                    if OOO0OOOO000O0000O ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOOO000O0000O["message"]}')#line:1237
                                    if OOO0OOOO000O0000O ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOOO000O0000O["message"]}')#line:1239
                                        break #line:1240
                                if float (OO000OOOO0OOO0O00 )<780 :#line:1241
                                    O000OOOOO00OOOOO0 =800 -float (OO000OOOO0OOO0O00 )#line:1242
                                    O0OO0O00OOO000OOO =f'_water={int(O000OOOOO00OOOOO0)}_{timi_new()}'#line:1243
                                    O00O00000O0O0OO0O ={'source':'scsc','authorization':O00000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00OOO000OOO ),'signstring':O0OO0O00OOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    OO0OO00O0OO0O00O0 ={"water":int (O000OOOOO00OOOOO0 )}#line:1255
                                    OO0O0OO00OOOOO000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00O00000O0O0OO0O ,data =OO0OO00O0OO0O00O0 ).json ()#line:1257
                                    if 'status'in OO0O0OO00OOOOO000 :#line:1259
                                        if OO0O0OO00OOOOO000 ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{OO0O0OO00OOOOO000["message"]}丨数量:{int(O000OOOOO00OOOOO0)}')#line:1261
                                        if OO0O0OO00OOOOO000 ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{OO0O0OO00OOOOO000["message"]}丨数量:{int(O000OOOOO00OOOOO0)}')#line:1263
                                            OO0000O00000OO0O0 =OO0O0OO00OOOOO000 ["message"].split ('-')[1 ]#line:1264
                                            O00OOOO0000O0OOOO =f'__{timi_new()}'#line:1265
                                            OO00000OOO0OOOO00 ={'source':'scsc','authorization':O00000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0000O0OOOO ),'signstring':O00OOOO0000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            OO0O0000OOOOOO000 =requests .request ('get',f'{host}/user',headers =OO00000OOO0OOOO00 ).json ()#line:1277
                                            if 'status'in OO0O0000OOOOOO000 :#line:1278
                                                if OO0O0000OOOOOO000 ['status']==200 :#line:1279
                                                    O0OOOOO0OOOOO00O0 =OO0O0000OOOOOO000 ['data']['inner_id']#line:1280
                                                    if give_gold (O0OOOOO0OOOOO00O0 ,float (OO0000O00000OO0O0 )+1 ):#line:1281
                                                        O00000000O00000O0 .energy ()#line:1282
                        break #line:1283
        except Exception as O0000OOOOOO00OOOO :#line:1284
            print (O0000OOOOOO00OOOO )#line:1285
def bundled_def ():#line:1288
    O000OOOO00OOOO0OO =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return O000OOOO00OOOO0OO [random .randint (0 ,len (O000OOOO00OOOO0OO )-1 )]#line:1290
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
        O0OOO00O0OO0OO0OO =gitee_edition ()#line:1329
        if version_of_the_validation ()<O0OOO00O0OO0OO0OO ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO00O0OO0OO0OO["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{O0OOO00O0OO0OO0OO["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO00O0OO0OO0OO["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {O0OOO00O0OO0OO0OO["CityEarth"]["content"]}')#line:1335
    except Exception as O0O0OO0O0OOOO0OO0 :#line:1336
        print (O0O0OO0O0OOOO0OO0 )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
