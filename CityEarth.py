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
@ 版本  4.2
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
invited_new =[]#line:6
weishim =[]#line:7
def start ():#line:10
    try :#line:11
        O000OO000O0O00OOO00 ()#line:12
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:13
        O000OO0O00OO00O00 ()#line:14
        O0O00O0O0000O0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O0O00O0O0000O0OOO)}个账号==========")#line:16
        for OO00OO0OO0OOOOOO0 in O0O00O0O0000O0OOO :#line:17
            O0OOO0OOO0OOO0000 =[]#line:18
            print (f"------------正在执行第{O0O00O0O0000O0OOO.index(OO00OO0OO0OOOOOO0) + 1}个账号------------")#line:19
            OO00OO0O00000OOOO =CityEarth (OO00OO0OO0OOOOOO0 ,O0OOO0OOO0OOO0000 ,O0O00O0O0000O0OOO .index (OO00OO0OO0OOOOOO0 ))#line:20
            def O0OO000O00O00OOOO ():#line:22
                if OO00OO0O00000OOOO .base_info ():#line:24
                    OO00OO0O00000OOOO .sealing ()#line:26
                    OO00OO0O00000OOOO .invitenum ()#line:28
                    OO00OO0O00000OOOO .query_to_sell ()#line:30
                    OO00OO0O00000OOOO .game_map ()#line:32
                    OO00OO0O00000OOOO .friends_invitation ()#line:36
                    OO00OO0O00000OOOO .energy ()#line:38
                    OO00OO0O00000OOOO .add_clover ()#line:40
                    OO00OO0O00000OOOO .propsraffle ()#line:42
                    OO00OO0O00000OOOO .synthetic ()#line:44
                    OO00OO0O00000OOOO .crops_illustrated ()#line:46
                    OO00OO0O00000OOOO .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OO00OO0O00000OOOO .give_gold ()#line:51
            OO000O0OO0OO000O0 =threading .Thread (target =O0OO000O00O00OOOO )#line:53
            OO000O0OO0OO000O0 .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        O00O0OOOOO0OO0O0O =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O0OOOOO0OO0O0O +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO0000OOOO00OOO0 in invited_new :#line:62
            print (OOO0000OOOO00OOO0 )#line:63
        print ('开始打印未实名的token')#line:64
        for OOO000O0O0OOO00OO in weishim :#line:65
            print (OOO000O0O0OOO00OO )#line:66
    except Exception as OOOOO0O0OOO00O0OO :#line:67
        print (OOOOO0O0OOO00O0OO )#line:68
def give_gold (O000OO0O00OO00OOO ,O00000OO0OO00000O ):#line:72
    try :#line:73
        O0O00OOOOOO00O00O =f'_doneeNo={O000OO0O00OO00OOO}&quantity={int(O00000OO0OO00000O)}_{timi_new()}'#line:74
        OO0OO000OOOO0O00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O00OOOOOO00O00O ),'signstring':O0O00OOOOOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0O0O0OOO0O000000 ={"quantity":int (O00000OO0OO00000O ),"doneeNo":O000OO0O00OO00OOO }#line:89
        O00O0OOOOOOOO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OO000OOOO0O00O ,data =O0O0O0OOO0O000000 ).json ()#line:90
        if 'status'in O00O0OOOOOOOO0O00 :#line:92
            if O00O0OOOOOOOO0O00 ['status']==200 :#line:93
                if O00O0OOOOOOOO0O00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00000OO0OO00000O)}种子给{O000OO0O00OO00OOO}成功')#line:95
                    return True #line:96
            if O00O0OOOOOOOO0O00 ['status']==401 :#line:97
                print (f'【赠送种子】:{O00O0OOOOOOOO0O00["message"]}')#line:98
                return False #line:99
            if O00O0OOOOOOOO0O00 ['status']==500 :#line:100
                print (f'【赠送种子】:{O00O0OOOOOOOO0O00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0O0O00O0OOO0OO00 :#line:104
        print (O0O0O00O0OOO0OO00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OOOOO0O0OO0OO00 ):#line:115
    O0OO0O0OO0OO00000 =hashlib .md5 (O0OOOOO0O0OO0OO00 .encode ()).hexdigest ()#line:116
    OO0000O00O000O000 =sc1 ()#line:117
    OO00O000OO0OOOO0O =sc2 ()#line:118
    O0000OO0OOOO000OO =sc3 ()#line:119
    OO0O0O00OO00O00O0 =OO0000O00O000O000 +O0OO0O0OO0OO00000 +OO00O000OO0OOOO0O +O0000OO0OOOO000OO #line:120
    OOOO00000OOOO00O0 =hashlib .md5 (OO0O0O00OO00O00O0 .encode ()).hexdigest ()#line:121
    return OOOO00000OOOO00O0 #line:122
def format_msg ():#line:125
    OO0OO0OOOOO00O00O =""#line:126
    for O0OO00000OO00000O in msg_list :#line:127
        OO0OO0OOOOO00O00O +=str (O0OO00000OO00000O )+"\r\n"#line:128
    return OO0OO0OOOOO00O00O #line:129
def sc1 ():#line:132
    return "scsc%^&*"#line:133
def O000OO0O00OO00O00 ():#line:136
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:137
        ubbbf ()#line:138
    else :#line:139
        oyoy ()#line:140
        exit (1 )#line:141
def timi_new ():#line:144
    return str (int (time .time ()*1000 ))#line:145
json_path ="CityEarth_data.json"#line:148
json_path1 ="CityEarth_data.json"#line:149
dict ={}#line:150
def get_json_data (O00O000O0OOO000O0 ,OOO000O0OO0OOO000 ,OOO00OOOOO0O0O00O ,O00O00OO000OO000O ):#line:153
    with open (O00O000O0OOO000O0 ,'rb')as OOO0O00OO00OO0O00 :#line:154
        O00OO00O0OOOOO0OO =json .load (OOO0O00OO00OO0O00 )#line:155
        O00OO00O0OOOOO0OO ['data'][OOO000O0OO0OOO000 ][OOO00OOOOO0O0O00O ]=O00O00OO000OO000O #line:156
        O0O0OO00O0000O0O0 =O00OO00O0OOOOO0OO #line:157
    OOO0O00OO00OO0O00 .close ()#line:158
    return O0O0OO00O0000O0O0 #line:159
def write_json_data (O00O0O0OO0OOOO0O0 ):#line:162
    with open (json_path1 ,'w')as OO0O00O0O00OO0000 :#line:163
        json .dump (O00O0O0OO0OOOO0O0 ,OO0O00O0O00OO0000 )#line:164
    OO0O00O0O00OO0000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O000OO0O0O0O00OO0 ,OO0OO0O00O000OO00 ,O0O00000O0OO00O00 ,OOO0O0O000000000O ):#line:171
        try :#line:172
            O000OO0O0O0O00OO0 .msg =O0O00000O0OO00O00 #line:173
            O000OO0O0O0O00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O000OO0O0O0O00OO0 .token =OO0OO0O00O000OO00 ['authorization']#line:175
            O000OO0O0O0O00OO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O000OO0O0O0O00OO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O000OO0O0O0O00OO0 .elephant_user =OO0OO0O00O000OO00 ['elephant_user']#line:178
            O000OO0O0O0O00OO0 .elephant_pswd =OO0OO0O00O000OO00 ['elephant_pswd']#line:179
            O000OO0O0O0O00OO0 .elephant_Task_ID =OO0OO0O00O000OO00 ['elephant_Task_ID']#line:180
            O000OO0O0O0O00OO0 .len_new =OOO0O0O000000000O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOOOOOOOOOO0O0O0 ):#line:186
        try :#line:187
            OOOOOOOOOOOO0O0O0 .watched_ad ()#line:189
            OO0OO000O00O0O00O =f'__{timi_new()}'#line:190
            OOOOOOOOOO0O0OOOO ={'source':'scsc','authorization':OOOOOOOOOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O00O0O00O ),'signstring':OO0OO000O00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00O00OO0OO0OOO0O =requests .request ('get',f'{host}/user',headers =OOOOOOOOOO0O0OOOO ).json ()#line:202
            if 'status'in O00O00OO0OO0OOO0O :#line:204
                if O00O00OO0OO0OOO0O ['status']==200 :#line:205
                    O00O000O000OO0O00 =O00O00OO0OO0OOO0O ['data']['nickname']#line:206
                    O0O000O0000000O0O =O00O00OO0OO0OOO0O ['data']['inner_id']#line:207
                    O0O0O0O00O0OOOO00 =O00O00OO0OO0OOO0O ['data']['assets']['gold']#line:208
                    O00O000O00O0OO000 =O00O00OO0OO0OOO0O ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00O000O000OO0O00[:5]}丨ID:{O0O000O0000000O0O}丨等级:{O00O000O00O0OO000}丨金种子:{str(O0O0O0O00O0OOOO00).split(".")[0]}')#line:211
                    if 'wx_'in O00O000O000OO0O00 :#line:212
                        OOOOOOOOOOOO0O0O0 .change_nickname ()#line:213
                if O00O00OO0OO0OOO0O ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOOOOOOOOOO0O0O0 .elephant_user =='f':#line:216
                        return False #line:217
                    O0OOOOO0O0O0O0000 =Invalid_login .addtask (elephant_user =OOOOOOOOOOOO0O0O0 .elephant_user ,elephant_pswd =OOOOOOOOOOOO0O0O0 .elephant_pswd ,elephant_Task_ID =OOOOOOOOOOOO0O0O0 .elephant_Task_ID )#line:220
                    O0OO000OO000O000O =get_json_data (json_path ,OOOOOOOOOOOO0O0O0 .len_new ,'authorization',O0OOOOO0O0O0O0000 )#line:221
                    if write_json_data (O0OO000OO000O000O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00O00OO0OO0OOO0O ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O000OO00OOO000O00 :#line:228
            print (O000OO00OOO000O00 )#line:229
    def sealing (O0O0O00OOO00OO0OO ):#line:232
        try :#line:233
            O00OO0OOO00OOO0OO =f'__{timi_new()}'#line:234
            O00O00O0O000O00OO ={'source':'scsc','authorization':O0O0O00OOO00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOO00OOO0OO ),'signstring':O00OO0OOO00OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O00O0O000O00OO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O00O00O0O000O00OO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O00O0O000O00OO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O00O0O000O00OO )#line:249
            requests .request ('get',f'{host}/user',headers =O00O00O0O000O00OO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O00O0O000O00OO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O00O0O000O00OO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O00O0O000O00OO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O00O00O0O000O00OO )#line:254
            requests .request ('get',f'{host}/assets',headers =O00O00O0O000O00OO )#line:255
        except Exception as OOOO000OO0O0OO0OO :#line:256
            print (OOOO000OO0O0OO0OO )#line:257
    def ddd (OOOO0OOO0O000O0O0 ):#line:259
        try :#line:260
            O0OOOO0OOO000OOOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO000OOO00OOO00OO ={'source':'scsc','authorization':OOOO0OOO0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOO000OOOO ),'signstring':O0OOOO0OOO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO00OOOOOO0OOOO00 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO000OOO00OOO00OO ).json ()#line:273
            print (OO00OOOOOO0OOOO00 )#line:274
        except Exception as OO0000OO00O000O0O :#line:279
            print (OO0000OO00O000O0O )#line:280
    def the_query (OO0O0OOO00000OO0O ):#line:290
        try :#line:291
            OOOO0O0O00O0000O0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            OO0O0OO000O0O00OO ={'authorization':OO0O0OOO00000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00O0000O0 ),'signstring':OOOO0O0O00O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            OO00O000O00O0OOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0O0OO000O0O00OO ).json ()#line:304
            if 'status'in OO00O000O00O0OOO0 :#line:306
                if OO00O000O00O0OOO0 ['status']==200 :#line:307
                    O00OOO000OOOOO0OO =OO00O000O00O0OOO0 ['data']['rows'][4 ]['price']#line:308
                    OO0O0OOO00000OO0O .market_sale (O00OOO000OOOOO0OO )#line:309
        except Exception as O00OOOOOO0O00OOO0 :#line:310
            print (O00OOOOOO0O00OOO0 )#line:311
    def market_sale (O00O0000OO0OOOOOO ,O00O0O000O00O0OO0 ):#line:314
        try :#line:315
            OOO0OO0OO00O0O0OO =timi_new ()#line:316
            OO00OOOOO0OO00OOO =f'type=crop__{OOO0OO0OO00O0O0OO}'#line:317
            O000O00O0O00OO000 ={'source':'scsc','authorization':O00O0000OO0OOOOOO .token ,'timestamp':str (OOO0OO0OO00O0O0OO ),'sign':sign (OO00OOOOO0OO00OOO ),'signstring':OO00OOOOO0OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            OOOO0OO000OOOO0O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O000O00O0O00OO000 ).json ()#line:330
            if 'status'in OOOO0OO000OOOO0O0 :#line:332
                if OOOO0OO000OOOO0O0 ['status']==200 :#line:333
                    if OOOO0OO000OOOO0O0 ['data']['rows']:#line:334
                        O00OOO0O000000O00 =OOOO0OO000OOOO0O0 ['data']['rows'][0 ]['packsackItemId']#line:335
                        O0OOO00O00000OOOO =OOOO0OO000OOOO0O0 ['data']['rows'][0 ]['quantity']#line:336
                        OOO00OOO000OOO00O =float (O00O0O000O00O0OO0 )-0.001 #line:337
                        if OOO00OOO000OOO00O >10 :#line:338
                            O0000OOO00000OOOO =f'_packsackItemId={O00OOO0O000000O00}&price={str(O00O0O000O00O0OO0)[:6]}&quantity={O0OOO00O00000OOOO}_{OOO0OO0OO00O0O0OO}'#line:339
                            OOO000OOO0OO00OOO ={'source':'scsc','authorization':O00O0000OO0OOOOOO .token ,'timestamp':str (OOO0OO0OO00O0O0OO ),'sign':sign (O0000OOO00000OOOO ),'signstring':O0000OOO00000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O0OOOO0O0OOO00O00 ={"packsackItemId":O00OOO0O000000O00 ,"price":str (O00O0O000O00O0OO0 )[:6 ],"quantity":str (O0OOO00O00000OOOO )}#line:355
                            O000OOOOO00OOO00O =requests .request ('post',f'{host}/market/sale',headers =OOO000OOO0OO00OOO ,data =O0OOOO0O0OOO00O00 ).json ()#line:356
                            if 'status'in O000OOOOO00OOO00O :#line:358
                                if O000OOOOO00OOO00O ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{O0OOO00O00000OOOO}丨价格:{str(O00O0O000O00O0OO0)[:6]}')#line:360
        except Exception as OOOO00O0O0O00OOO0 :#line:361
            print (OOOO00O0O0O00OOO0 )#line:362
    def query_to_sell (O0OO00O00OOO00O00 ):#line:365
        try :#line:366
            O00000O00OOOO0000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            O0000O0OOO0OO0OO0 ={'source':'scsc','authorization':O0OO00O00OOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00OOOO0000 ),'signstring':O00000O00OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            OOOO000O000OO000O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0000O0OOO0OO0OO0 ).json ()#line:380
            if 'status'in OOOO000O000OO000O :#line:382
                if OOOO000O000OO000O ['status']==200 :#line:383
                    for O0OOOO0O0O0OO00OO in OOOO000O000OO000O ['data']['rows']:#line:384
                        OO0O0OO000OO0000O =O0OOOO0O0O0OO00OO ['materialKey']#line:385
                        OOOO00OO0O0OOOO00 =O0OOOO0O0O0OO00OO ['quantity']#line:386
                        OOOO0OO0O0OOO0OO0 =O0OOOO0O0O0OO00OO ['price']#line:387
                        OO0O0000O0OO0OO00 =O0OOOO0O0O0OO00OO ['saleState']#line:388
                        if OO0O0000O0OO0OO00 ==0 :#line:389
                            print (f'【出售订单】:名称:{OO0O0OO000OO0000O}丨数量:{OOOO00OO0O0OOOO00}丨价格:{OOOO0OO0O0OOO0OO0}')#line:390
                            OOO000O0O0OOO0000 =O0OOOO0O0O0OO00OO ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                O0OO00O00OOO00O00 .cacel_sale (OOO000O0O0OOO0000 )#line:393
        except Exception as OOO00O00OO0O00OO0 :#line:394
            print (OOO00O00OO0O00OO0 )#line:395
    def cacel_sale (O00O0000O00O0O00O ,O0O000OO00OOOO00O ):#line:398
        try :#line:399
            OO0OOOOO00OOOOO00 =f'_saleId={O0O000OO00OOOO00O}_{timi_new()}'#line:400
            O0O000000O0OOO00O ={'source':'scsc','authorization':O00O0000O00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00OOOOO00 ),'signstring':OO0OOOOO00OOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O0O00O00OOOOO000O ={"saleId":O0O000OO00OOOO00O }#line:414
            OOO00O00O000O0OO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O000000O0OOO00O ,data =O0O00O00OOOOO000O ).json ()#line:415
            if 'status'in OOO00O00O000O0OO0 :#line:417
                if OOO00O00O000O0OO0 ['status']==200 :#line:418
                    print (f'【下架出售】:{OOO00O00O000O0OO0["data"]}')#line:419
        except Exception as OO00000O0O0O0OO00 :#line:420
            print (OO00000O0O0O0OO00 )#line:421
    def change_nickname (O0000O0O0O0O00000 ):#line:424
        try :#line:425
            OOOO000OOO00OOO0O =timi_new ()#line:426
            OOO00O0OO0O000000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OO0OO0O00O0OO0000 =requests .request ('post','https://www.qmsjmfb.com/',data =OOO00O0OO0O000000 ).text #line:428
            O0O0OOOOOO0000O0O =re .findall ('<ul><li>(.*?)</li>',OO0OO0O00O0OO0000 )[0 ][:3 ]#line:429
            O0O000OOO00OO00OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0OOOOOO0000O0O}').json ()#line:430
            O0O0O00O00O0O000O =O0O000OOO00OO00OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            O0OO000O000OOO0O0 ={"nickname":O0O0O00O00O0O000O }#line:432
            O0000OO00OOO0000O =f'_nickname={O0O0O00O00O0O000O}_{OOOO000OOO00OOO0O}'#line:433
            O00O0000OOO0OOO00 ={'source':'scsc','authorization':O0000O0O0O0O00000 .token ,'timestamp':OOOO000OOO00OOO0O ,'sign':sign (O0000OO00OOO0000O ),'signstring':O0000OO00OOO0000O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O00OO00000OOOOO0O =requests .request ('patch',f'{host}/user/nickname',headers =O00O0000OOO0OOO00 ,data =O0OO000O000OOO0O0 ).json ()#line:445
            if 'status'in O00OO00000OOOOO0O :#line:447
                if O00OO00000OOOOO0O ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O0O0O00O00O0O000O}丨{O00OO00000OOOOO0O["message"]}')#line:449
        except Exception as O0OO0OO0OOO0O00O0 :#line:450
            print (O0OO0OO0OOO0O00O0 )#line:451
    def withdraw (OO0000OOOO00OOOOO ):#line:454
        try :#line:455
            OO00OO0OOO0000OO0 =f'__{timi_new()}'#line:456
            O0O00O00O0000OO0O ={'source':'scsc','authorization':OO0000OOOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OOO0000OO0 ),'signstring':OO00OO0OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O00OOOOOOOO00O0O0 =requests .request ('get',f'{host}/assets',headers =O0O00O00O0000OO0O ).json ()#line:468
            if 'status'in O00OOOOOOOO00O0O0 :#line:470
                if O00OOOOOOOO00O0O0 ['status']==200 :#line:471
                    OOOOOOOOOO00OO000 =O00OOOOOOOO00O0O0 ['data']['cash']#line:472
                    if float (OOOOOOOOOO00OO000 )>20 :#line:473
                        OO00OO0OOO0000OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O0O00O00O0000OO0O ={'authorization':OO0000OOOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OOO0000OO0 ),'signstring':OO00OO0OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        O00O00OOOO00OO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OO0OO00O00000OO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00O00O0000OO0O ,data =O00O00OOOO00OO00O ).json ()#line:487
                        if 'status'in OO0OO00O00000OO0O :#line:489
                            if OO0OO00O00000OO0O ['status']==200 :#line:490
                                print (f'【余额提现】:{OO0OO00O00000OO0O["data"]}')#line:491
                        if 'status'in OO0OO00O00000OO0O :#line:492
                            if OO0OO00O00000OO0O ['status']==500 :#line:493
                                print (f'【余额提现】:{OO0OO00O00000OO0O["message"]}')#line:494
        except Exception as O00O00OOO00O00O0O :#line:495
            print (O00O00OOO00O00O0O )#line:496
    def invitenum (OO0O0O000OO0OO00O ):#line:499
        global invited_new #line:500
        try :#line:501
            OOOO00O00OOO0O0O0 =f'__{timi_new()}'#line:502
            O000OOO00O0000OOO ={'source':'scsc','authorization':OO0O0O000OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OOO0O0O0 ),'signstring':OOOO00O00OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            OO0O00OOOO0O000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =O000OOO00O0000OOO ).json ()#line:514
            if 'status'in OO0O00OOOO0O000O0 :#line:516
                if OO0O00OOOO0O000O0 ['status']==200 :#line:517
                    OOO0000OOOO0000O0 =OO0O00OOOO0O000O0 ['data']['invited_count']#line:518
                    OOO0O0O00OOO00OOO =OO0O00OOOO0O000O0 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OOO0000OOOO0000O0}丨间邀好友:{OOO0O0O00OOO00OOO}')#line:520
                    if OOO0000OOOO0000O0 <2 :#line:521
                        OOO00O00OOOOOO0OO =f'__{timi_new()}'#line:522
                        OO0O0O00O0OOO0O00 ={'source':'scsc','authorization':OO0O0O000OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOOOOO0OO ),'signstring':OOO00O00OOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O0O00000OOOO000OO =requests .request ('get',f'{host}/user',headers =OO0O0O00O0OOO0O00 ).json ()#line:534
                        if 'status'in O0O00000OOOO000OO :#line:536
                            if O0O00000OOOO000OO ['status']==200 :#line:537
                                invited_new .append (O0O00000OOOO000OO ['data']['inner_id'])#line:538
        except Exception as OO0O0O00O0O00OO0O :#line:539
            print (OO0O0O00O0O00OO0O )#line:540
    def game_map (O0O0O0O00OO00OOOO ):#line:543
        try :#line:544
            OOOOOOOO0OOO0OO00 =f'__{timi_new()}'#line:545
            OO00O0OOO0O0O0OO0 ={'source':'scsc','authorization':O0O0O0O00OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO0OOO0OO00 ),'signstring':OOOOOOOO0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O00OOOOOOO000OO00 =requests .request ('get',f'{host}/game/map',headers =OO00O0OOO0O0O0OO0 ).json ()#line:557
            if 'status'in O00OOOOOOO000OO00 :#line:559
                if O00OOOOOOO000OO00 ['status']==200 :#line:560
                    for O00O0O0OO0000OO0O in O00OOOOOOO000OO00 ['data']['list'][0 ]['crops']:#line:561
                        OO0000OOOOOOO00OO =O00O0O0OO0000OO0O ['level']#line:563
                        if OO0000OOOOOOO00OO ==41 :#line:564
                            O0OO000OOO0O0O0OO =O00O0O0OO0000OO0O ['crop_name']#line:565
                            O0OO00OOO0O0O000O =O00O0O0OO0000OO0O ['count']#line:566
                            if O0OO00OOO0O0O000O >0 :#line:567
                                print (f'【农业资产】:{O0OO000OOO0O0O0OO}丨数量:{O0OO00OOO0O0O000O}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    O0O0O0O00OO00OOOO .the_query ()#line:570
        except Exception as O0000OOOOOOOO00O0 :#line:571
            print (O0000OOOOOOOO00O0 )#line:572
    def give_gold (OO0OO00OOOOOOOO00 ):#line:575
        try :#line:576
            O000O0OOOO0O0O0O0 =f'__{timi_new()}'#line:577
            OOO0000O000O0OOOO ={'source':'scsc','authorization':OO0OO00OOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0O0O0O0 ),'signstring':O000O0OOOO0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            O00O00O0OOOOO0O00 =requests .request ('get',f'{host}/user',headers =OOO0000O000O0OOOO ).json ()#line:589
            if 'status'in O00O00O0OOOOO0O00 :#line:590
                if O00O00O0OOOOO0O00 ['status']==200 :#line:591
                    if float (OO0OO00OOOOOOOO00 .doneeNo )!=0 :#line:592
                        O0OOO0000OO0OOOO0 =O00O00O0OOOOO0O00 ['data']['assets']['gold']#line:593
                        if float (O0OOO0000OO0OOOO0 )>float (OO0OO00OOOOOOOO00 .innerId ):#line:594
                            O0000O0OO00O0O0OO =int (float (O0OOO0000OO0OOOO0 )/1.1 )#line:595
                            O000O0OOOO0O0O0O0 =f'_doneeNo={OO0OO00OOOOOOOO00.doneeNo}&quantity={O0000O0OO00O0O0OO}_{timi_new()}'#line:596
                            OOO0000O000O0OOOO ={'source':'scsc','authorization':OO0OO00OOOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOOO0O0O0O0 ),'signstring':O000O0OOOO0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            O0OOO00O0OO00OO0O ={"quantity":O0000O0OO00O0O0OO ,"doneeNo":OO0OO00OOOOOOOO00 .doneeNo }#line:611
                            OO00OO0O0O0O000OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000O000O0OOOO ,data =O0OOO00O0OO00OO0O ).json ()#line:612
                            if 'status'in OO00OO0O0O0O000OO :#line:614
                                if OO00OO0O0O0O000OO ['status']==200 :#line:615
                                    if OO00OO0O0O0O000OO ['data']:#line:616
                                        print (f'【赠送种子】:赠送{O0000O0OO00O0O0OO}种子给{OO0OO00OOOOOOOO00.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as O0O00OO0OO0OO000O :#line:620
            print (O0O00OO0OO0OO000O )#line:621
    def invitation (OOOO000OOOOO0OOOO ):#line:623
        try :#line:624
            _O0O0O00O0OO00O00O =float (bundled_def ())/4 #line:625
            OOO000OO00OOO000O =f'_innerId={int(_O0O0O00O0OO00O00O)}_{timi_new()}'#line:626
            OOO000O0O000O000O ={'source':'scsc','authorization':OOOO000OOOOO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OOO000O ),'signstring':OOO000OO00OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            OOO0O000OOO0OO000 ={"innerId":int (_O0O0O00O0OO00O00O )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO000O0O000O000O ,data =OOO0O000OOO0OO000 )#line:639
        except Exception as O000OOOO0000O00OO :#line:640
            print (O000OOOO0000O00OO )#line:641
    def winning_rewards (OOOOO0O0000000O0O ):#line:644
        try :#line:645
            O0O0O00OOOOO0O0OO =f'__{timi_new()}'#line:646
            O0O00O0O0OO0OOO0O ={'source':'scsc','authorization':OOOOO0O0000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOOO0O0OO ),'signstring':O0O0O00OOOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O000O0OOOO00000O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O00O0O0OO0OOO0O ).json ()#line:658
            if 'status'in O000O0OOOO00000O0 :#line:660
                if O000O0OOOO00000O0 ['status']==200 :#line:661
                    if O000O0OOOO00000O0 ['data']['amount']:#line:662
                        O0O0O0O00O00OOO00 =O000O0OOOO00000O0 ['data']['amount']['gold']#line:663
                        return O0O0O0O00O00OOO00 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as O00O0O0OOO0OOOO00 :#line:667
            print (O00O0O0OOO0OOOO00 )#line:668
    def certification (O00000O00OOOOOO00 ):#line:671
        try :#line:672
            O00O000OOOOO0O0O0 =f'__{timi_new()}'#line:673
            O00OO0O0OOO00OOO0 ={'source':'scsc','authorization':O00000O00OOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOOO0O0O0 ),'signstring':O00O000OOOOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            OOO0OO0O00O0O00OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O0OOO00OOO0 ).json ()#line:685
            if 'status'in OOO0OO0O00O0O00OO :#line:687
                if OOO0OO0O00O0O00OO ['status']==200 :#line:688
                    if OOO0OO0O00O0O00OO ['data']['result']:#line:689
                        OOO0OO00O0O0O0O0O =OOO0OO0O00O0O00OO ['data']['nick_name']#line:690
                        return OOO0OO00O0O0O0O0O #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as OO0OO000O0O000000 :#line:694
            print (OO0OO000O0O000000 )#line:695
    def crops_illustrated (O0O000OOOOOO00OO0 ):#line:698
        try :#line:699
            OOO000000O00OO0O0 =f'__{timi_new()}'#line:700
            O0OOO00000OOOO00O ={'source':'scsc','authorization':O0O000OOOOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000000O00OO0O0 ),'signstring':OOO000000O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OO000OOOO0O0OOOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO00000OOOO00O ).json ()#line:712
            if 'status'in OO000OOOO0O0OOOO0 :#line:714
                if OO000OOOO0O0OOOO0 ['status']==200 :#line:715
                    O0OO0000OO0OOOOO0 =OO000OOOO0O0OOOO0 ['data'][0 ]['crops']#line:716
                    for OO00O0000OOOO0OOO in O0OO0000OO0OOOOO0 :#line:717
                        if OO00O0000OOOO0OOO ['ill_clover_award']:#line:718
                            if float (OO00O0000OOOO0OOO ['ill_clover_award'])>1 :#line:719
                                if OO00O0000OOOO0OOO ['is_finish']:#line:720
                                    if not OO00O0000OOOO0OOO ['is_getit']:#line:721
                                        if O0O000OOOOOO00OO0 .certification ()!='未实名':#line:722
                                            OOO000000O00OO0O0 =f'_award_level={OO00O0000OOOO0OOO["level"]}_{timi_new()}'#line:723
                                            O0OOO00000OOOO00O ={'source':'scsc','authorization':O0O000OOOOOO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000000O00OO0O0 ),'signstring':OOO000000O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            O00O00000000O0OO0 ={"award_level":OO00O0000OOOO0OOO ['level']}#line:735
                                            O00O00O00OO00OO00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO00000OOOO00O ,json =O00O00000000O0OO0 ).json ()#line:737
                                            if 'status'in O00O00O00OO00OO00 :#line:738
                                                if O00O00O00OO00OO00 ['status']==200 :#line:739
                                                    O0O0000OOO00OO00O =O00O00O00OO00OO00 ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{OO00O0000OOOO0OOO["crop_name"]}成就丨奖励{O0O0000OOO00OO00O}☘️')#line:742
                                                if O00O00O00OO00OO00 ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{O00O00O00OO00OO00["message"]}')#line:744
        except Exception as O0OO0OO0OOO0O0O00 :#line:745
            print (O0OO0OO0OOO0O0O00 )#line:746
    def watched_ad (O000OOO000O00000O ):#line:749
        try :#line:750
            OO000000O00000OO0 =f'__{timi_new()}'#line:751
            O00000OO0O00OO0OO ={'source':'scsc','authorization':O000OOO000O00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O00000OO0 ),'signstring':OO000000O00000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            OOOO0O0OO0OOOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O00000OO0O00OO0OO ).json ()#line:763
            if 'status'in OOOO0O0OO0OOOO0OO :#line:765
                if OOOO0O0OO0OOOO0OO ['status']==200 :#line:766
                    if 'offlineInfo'in OOOO0O0OO0OOOO0OO ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        O0O00OO0OOO00OOO0 =OOOO0O0OO0OOOO0OO ['data']['offlineInfo']['off_minute']#line:769
                        O000OO0OO0O0OOOOO =float (OOOO0O0OO0OOOO0OO ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00000OO0O00OO0OO ).json ()#line:772
                        time .sleep (2 )#line:773
                        OOO0O0O0OO0O0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O00000OO0O00OO0OO ).json ()#line:774
                        if 'status'in OOO0O0O0OO0O0OO00 :#line:776
                            if OOO0O0O0OO0O0OO00 ['status']==200 :#line:777
                                O00O0OO0O0O0O0OOO =float (OOO0O0O0OO0O0OO00 ['data']['silver'])/1000000000000 #line:778
                                O0OOO0000O000OO0O =str (O00O0OO0O0O0O0OOO -O000OO0OO0O0OOOOO )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{O0O00OO0OOO00OOO0}分钟奖励🌱数量:{O0OOO0000O000OO0O}t粒')#line:780
        except Exception as OO0O0O0OO00OOO00O :#line:781
            print (OO0O0O0OO00OOO00O )#line:782
    def user_ad (O00OO0OO000O0O00O ):#line:785
        try :#line:786
            OO0O00OOOO0OO0O00 =f'__{timi_new()}'#line:787
            O0OO0O00O00O000O0 ={'source':'scsc','authorization':O00OO0OO000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOO0OO0O00 ),'signstring':OO0O00OOOO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            OO00O0O0OOOOO0O00 =requests .request ('get',f'{host}/user/ad',headers =O0OO0O00O00O000O0 ).json ()#line:799
            if 'status'in OO00O0O0OOOOO0O00 :#line:801
                if OO00O0O0OOOOO0O00 ['status']==200 :#line:802
                    OO0000O0O00OO0O0O =OO00O0O0OOOOO0O00 ['data']['max_time']#line:803
                    OOO00OOOO0O0O0O0O =OO00O0O0OOOOO0O00 ['data']['watch_time']#line:804
                    OOO00O0000OOO000O =OO00O0O0OOOOO0O00 ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{OOO00O0000OOO000O + OO0000O0O00OO0O0O - OOO00OOOO0O0O0O0O}次丨好友提供:{OOO00O0000OOO000O}次')#line:806
                    if OOO00O0000OOO000O +OO0000O0O00OO0O0O -OOO00OOOO0O0O0O0O >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        OO0OO00OOOOO00O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO0O00O00O000O0 ).json ()#line:809
                        if 'status'in OO0OO00OOOOO00O00 :#line:811
                            if OO0OO00OOOOO00O00 ['status']==200 :#line:812
                                OOO00OO0OOOOO0000 =float (OO0OO00OOOOO00O00 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(OOO00OO0OOOOO0000)}t粒')#line:814
                                return True #line:815
                            if OO0OO00OOOOO00O00 ['status']==500 :#line:816
                                OOO00O0OO0OOO0000 =OO0OO00OOOOO00O00 ['message']#line:817
                                print (f'【获取种子】:{OOO00O0OO0OOO0000}')#line:818
                                return False #line:819
        except Exception as O0O0O0OO00O0OO00O :#line:820
            print (O0O0O0OO00O0OO00O )#line:821
    def synthetic (OO0OO0O0O000OO0O0 ):#line:824
        global id ,g #line:825
        try :#line:826
            O0OO00OOOO0OOO0O0 =OO0OO0O0O000OO0O0 .level_new ()#line:827
            OO0OOO0OOO000OO0O =random .randint (9 ,11 )#line:828
            O000O0O00O000OO00 =f'_site=8&targetSite={OO0OOO0OOO000OO0O}_{timi_new()}'#line:829
            O0OO0O00O000O0O00 ={'source':'scsc','authorization':OO0OO0O0O000OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O000O0O00O000OO00 ),'signstring':O000O0O00O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            OO0O00OO0OO0O00OO ={"site":int (8 ),"targetSite":int (OO0OOO0OOO000OO0O )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O0OO0O00O000O0O00 ,json =OO0O00OO0OO0O00OO )#line:842
            while True :#line:843
                O00OOOOO0O0O0O000 =f'__{timi_new()}'#line:844
                O0O0O00OOO0OO0OO0 ={'source':'scsc','authorization':OO0OO0O0O000OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0O0O0O000 ),'signstring':O00OOOOO0O0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                OO00O000O0OOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O00OOO0OO0OO0 ).json ()#line:856
                if 'status'in OO00O000O0OOOO0O0 :#line:858
                    if OO00O000O0OOOO0O0 ['status']==200 :#line:859
                        O000OOOO0OO0O0OOO =OO00O000O0OOOO0O0 ['data']['cropList']#line:860
                        O0O00O0O000OO0000 =OO00O000O0OOOO0O0 ['data']['gameCoreDataDBid']#line:861
                        O0O000O0OO00000OO =float (OO00O000O0OOOO0O0 ['data']['silver'])/1000000000000 #line:862
                        OOOO00OO0O0000O0O =0 #line:867
                        for OO00O00OO0OOOOO00 in O000OOOO0OO0O0OOO :#line:868
                            if not OO00O00OO0OOOOO00 :#line:869
                                OO0OOOO00OO0O0000 =f'_crop_id={O0O00O0O000OO0000}&site={OOOO00OO0O0000O0O}_{OO0OO0O0O000OO0O0.time}'#line:870
                                O0O0O0OO0OOOO000O ={'source':'scsc','authorization':OO0OO0O0O000OO0O0 .token ,'timestamp':OO0OO0O0O000OO0O0 .time ,'sign':sign (OO0OOOO00OO0O0000 ),'signstring':OO0OOOO00OO0O0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                O0O00O000O0OO0000 ={"site":OOOO00OO0O0000O0O ,"crop_id":O0O00O0O000OO0000 }#line:881
                                O0000OO0O0OO00OOO =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0O0OO0OOOO000O ,data =O0O00O000O0OO0000 ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in O0000OO0O0OO00OOO :#line:885
                                    if O0000OO0O0OO00OOO ['status']==200 :#line:886
                                        if O0000OO0O0OO00OOO ['message']=='种子数量不足':#line:887
                                            O0OO00OOOO0OOO0O0 =OO0OO0O0O000OO0O0 .level_new ()#line:888
                                            print (f'【种植合成】:{O0000OO0O0OO00OOO["message"]}')#line:889
                                            if not OO0OO0O0O000OO0O0 .user_ad ():#line:890
                                                return False #line:891
                                    if O0000OO0O0OO00OOO ['status']==500 :#line:892
                                        print (f'【种植合成】:{O0000OO0O0OO00OOO["message"]}')#line:893
                                        return False #line:894
                            OOOO00OO0O0000O0O +=1 #line:895
                        O0OOOOOO00OOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O00OOO0OO0OO0 ).json ()#line:896
                        O00OOOOOOOOOOO00O =O0OOOOOO00OOO0O0O ['data']['cropList']#line:897
                        O000O000O00OO00O0 =False #line:898
                        for OO00O00OO0OOOOO00 in range (12 ):#line:899
                            id =O00OOOOOOOOOOO00O [OO00O00OO0OOOOO00 ]['level']#line:900
                            if float (O0OO00OOOO0OOO0O0 )-float (id )>9 :#line:901
                                O00000OO00O00O00O =f'_site={OO00O00OO0OOOOO00}_{timi_new()}'#line:902
                                O0O0OO000OOOOO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OO0O0O000OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O00000OO00O00O00O ),'signstring':O00000OO00O00O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                OO0O0O0OO00OOOOO0 ={"site":OO00O00OO0OOOOO00 }#line:914
                                O00O0O0O000O0O0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0OO000OOOOO0O0 ,data =OO0O0O0OO00OOOOO0 ).json ()#line:916
                                if 'status'in O00O0O0O000O0O0OO :#line:917
                                    if O00O0O0O000O0O0OO ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O0OO00OOO0O0O0O00 in range (11 ):#line:921
                                    OO0OO0000OO00O00O =O0OO00OOO0O0O0O00 +1 #line:922
                                    g =O00OOOOOOOOOOO00O [OO0OO0000OO00O00O ]['level']#line:923
                                    if id ==g :#line:924
                                        O00OOO0O00OOOOOO0 =O0OO00OOO0O0O0O00 +2 #line:925
                                        if O00OOO0O00OOOOOO0 !=OO00O00OO0OOOOO00 +1 :#line:926
                                            O00O0OOO0O0000000 =OO00O00OO0OOOOO00 +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            O000O0O00O000OO00 =f'_site={O00O0OOO0O0000000 - 1}&targetSite={O00OOO0O00OOOOOO0 - 1}_{timi_new()}'#line:930
                                            O0OO0O00O000O0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OO0O0O000OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O000O0O00O000OO00 ),'signstring':O000O0O00O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O00OOOO00O00OOO0O ={"site":int (O00O0OOO0O0000000 -1 ),"targetSite":int (O00OOO0O00OOOOOO0 -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OO0O00O000O0O00 ,json =O00OOOO00O00OOO0O )#line:949
                                            O000O000O00OO00O0 =True #line:951
                                    if O000O000O00OO00O0 :#line:952
                                        break #line:953
                                if O000O000O00OO00O0 :#line:954
                                    break #line:955
        except :#line:956
            OO0OO0O0O000OO0O0 .synthetic ()#line:957
    def level_new (OOO000O0OOOOO000O ):#line:960
        try :#line:961
            O0O0O0OOO0OO000O0 =f'__{timi_new()}'#line:962
            OO00O00O000OOOO00 ={'source':'scsc','authorization':OOO000O0OOOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOO0OO000O0 ),'signstring':O0O0O0OOO0OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OO0O000O0000O0O00 =requests .request ('get',f'{host}/user',headers =OO00O00O000OOOO00 ).json ()#line:974
            if 'status'in OO0O000O0000O0O00 :#line:975
                if OO0O000O0000O0O00 ['status']==200 :#line:976
                    return float (OO0O000O0000O0O00 ['data']['level'])#line:977
        except Exception as OOO0OO0OO00OOOOO0 :#line:978
            print (OOO0OO0OO00OOOOO0 )#line:979
    def propsraffle (O00O0000O0O00O0O0 ):#line:982
        try :#line:983
            while True :#line:984
                OOOOOO00000OOOOOO =f'__{timi_new()}'#line:985
                OO0OO0O00O0OO0OO0 ={'source':'scsc','authorization':O00O0000O0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00000OOOOOO ),'signstring':OOOOOO00000OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                O0O00O00OOOOO00OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OO0O00O0OO0OO0 ).json ()#line:997
                if 'status'in O0O00O00OOOOO00OO :#line:999
                    if O0O00O00OOOOO00OO ['status']==200 :#line:1000
                        O000OOO00O0OO0O0O =O0O00O00OOOOO00OO ['data']['rows']#line:1001
                        OO0OO0O00000OOO00 =O0O00O00OOOOO00OO ['data']['vstate']#line:1002
                        if O000OOO00O0OO0O0O ==5 or O000OOO00O0OO0O0O ==6 or O000OOO00O0OO0O0O ==7 :#line:1003
                            OOOO00O0O0OOO0000 =O0O00O00OOOOO00OO ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{OOOO00O0O0OOO0000}')#line:1005
                        if O000OOO00O0OO0O0O ==1 or O000OOO00O0OO0O0O ==2 or O000OOO00O0OO0O0O ==3 :#line:1006
                            OOOOO0OOOO00O00O0 =O0O00O00OOOOO00OO ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0OOOO00O00O0}')#line:1008
                        if O000OOO00O0OO0O0O ==4 or O000OOO00O0OO0O0O ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if O000OOO00O0OO0O0O =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as OO00O000O0O000O0O :#line:1050
            print (OO00O000O0O000O0O )#line:1051
    def friends_invitation (OO0O0000OOO0O0O00 ):#line:1054
        try :#line:1055
            O0OOOO0OOO0O000OO =f'__{timi_new()}'#line:1056
            OOO00000O0O00O0OO ={'source':'scsc','authorization':OO0O0000OOO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOO0O000OO ),'signstring':O0OOOO0OOO0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            O0OO000OO00O0O0O0 =requests .request ('get',f'{host}/friends',headers =OOO00000O0O00O0OO ).json ()#line:1068
            if 'status'in O0OO000OO00O0O0O0 :#line:1069
                if O0OO000OO00O0O0O0 ['status']==200 :#line:1070
                    O0O000000O000O000 =O0OO000OO00O0O0O0 ['data']['myInviteter']#line:1071
                    if O0O000000O000O000 :#line:1072
                        O0OO000OOOO000OO0 =O0O000000O000O000 ['user']['nickname']#line:1073
                        O0OO00OOOO00OOO00 =OO0O0000OOO0O0O00 .certification ()#line:1074
                        if O0OO00OOOO00OOO00 =='未实名':#line:1075
                            weishim .append (OO0O0000OOO0O0O00 .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{O0OO000OOOO000OO0}丨实名:{O0OO00OOOO00OOO00}')#line:1077
                    else :#line:1078
                        if OO0O0000OOO0O0O00 .innerId !='0':#line:1079
                            OO0O0000OOO0O0O00 .invitation ()#line:1080
        except Exception as O0000000O000O0OOO :#line:1081
            print (O0000000O000O0OOO )#line:1082
    def add_clover (O0OO0000OOOOO0000 ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            OOO0O0O000O0OOO00 =f'__{timi_new()}'#line:1088
            O000O0O0O00O00OOO ={'source':'scsc','authorization':O0OO0000OOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O0OOO00 ),'signstring':OOO0O0O000O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            OO000OO0OOO0O0000 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O0O00O00OOO ).json ()#line:1100
            if 'status'in OO000OO0OOO0O0000 :#line:1102
                if OO000OO0OOO0O0000 ['status']==200 :#line:1103
                    O0O0OOO0O0OOOO000 =OO000OO0OOO0O0000 ['data']['clover']#line:1104
                    O0OOO000O0000OO0O =OO000OO0OOO0O0000 ['data']['used_clover']#line:1105
                    O00O0OOOOOOO00O0O =float (O0O0OOO0O0OOOO000 )-float (O0OOO000O0000OO0O )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOO000O0000OO0O}')#line:1107
                    if O0OO0000OOOOO0000 .certification ()!='未实名':#line:1108
                        if O00O0OOOOOOO00O0O >1 :#line:1109
                            OOO0O0O000O0OOO00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O0OOOOOOO00O0O)}_{timi_new()}'#line:1110
                            O00OO0OOOO00OO0O0 ={'source':'scsc','authorization':O0OO0000OOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O0OOO00 ),'signstring':OOO0O0O000O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            OO0OO0OO00OO000OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O0OOOOOOO00O0O )}#line:1122
                            O0O0O00O0OO0OO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO0OOOO00OO0O0 ,data =OO0OO0OO00OO000OO ).json ()#line:1123
                            if 'status'in O0O0O00O0OO0OO0OO :#line:1125
                                if O0O0O00O0OO0OO0OO ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O0O0O00O0OO0OO0OO["data"]["isSuccess"]}丨数量:{O00O0OOOOOOO00O0O}')#line:1127
                                if O0O0O00O0OO0OO0OO ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O0O0O00O0OO0OO0OO["message"]}')#line:1129
            OO000OOOO0O0O0OOO =requests .request ('get',f'{host}/lottery',headers =O000O0O0O00O00OOO ).json ()#line:1130
            O0O0OOO0O00OOOO0O =O0OO0000OOOOO0000 .winning_rewards ()#line:1132
            if 'status'in OO000OOOO0O0O0OOO :#line:1133
                if OO000OOOO0O0O0OOO ['status']==200 :#line:1134
                    O0OO00O000000000O =OO000OOOO0O0O0OOO ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (O0OO00O000000000O )#line:1136
                    OOOO0OOO0000O00O0 =OO000OOOO0O0O0OOO ['data'][1 ]['value']#line:1137
                    O0O0OOO00O0O000O0 =OO000OOOO0O0O0OOO ['data'][0 ]['join_number']#line:1138
                    OOOO0O0O0OOO00O00 =int (float (OO000OOOO0O0O0OOO ['data'][0 ]['totalValue']))#line:1139
                    O0OO0O000OO0000O0 =float (OOOO0OOO0000O00O0 /OOOO0O0O0OOO00O00 )*10000 #line:1140
                    O00O0O00O0O0O000O =OOOO0O0O0OOO00O00 /O0O0OOO00O0O000O0 #line:1141
                    print (f'【参与抽奖】:预计每天中{str(O0OO00O000000000O)[:6]}颗金种子丨好友收益:{str(O0O0OOO0O00OOOO0O)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO0O000OO0000O0)[:6]}颗金种子丨☘️人均:{str(O00O0O00O0O0O000O)[:7]}️')#line:1143
        except Exception as OOOOOOO00000O000O :#line:1144
            print (OOOOOOO00000O000O )#line:1145
    def energy (O0O0000O00O0OOOO0 ):#line:1148
        try :#line:1149
            while True :#line:1150
                O0O00O0O0OO0000OO =f'__{timi_new()}'#line:1151
                OOO0000OOOOO00OO0 ={'source':'scsc','authorization':O0O0000O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0OO0000OO ),'signstring':O0O00O0O0OO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                OOO00O00OOOOOO0O0 =requests .request ('get',f'{host}/energy/general',headers =OOO0000OOOOO00OO0 ).json ()#line:1163
                if 'status'in OOO00O00OOOOOO0O0 :#line:1165
                    if OOO00O00OOOOOO0O0 ['status']==200 :#line:1166
                        O0O0OO0O0OO0O0000 =OOO00O00OOOOOO0O0 ['data']['ordinary_water']#line:1167
                        O000OO00OO000OOO0 =OOO00O00OOOOOO0O0 ['data']['ordinary_fertilizer']#line:1168
                        O0O00O00OOOOO0OO0 =OOO00O00OOOOOO0O0 ['data']['videoStatus']#line:1169
                        OO00000OO00O0OO00 =OOO00O00OOOOOO0O0 ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(O000OO00OO000OOO0).split(".")[0]}丨水滴:{str(O0O0OO0O0OO0O0000).split(".")[0]}')#line:1172
                        if float (O000OO00OO000OOO0 )<96 :#line:1173
                            if O0O00O00OOOOO0OO0 :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                OOOO000OO00OOO0O0 =99 -float (O000OO00OO000OOO0 )#line:1176
                                O00OO0OOOOO00O0OO ={"fertilizer":str (OOOO000OO00OOO0O0 ).split ('.')[0 ]}#line:1177
                                OO0OOOOO000O0OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO0000OOOOO00OO0 ).json ()#line:1179
                                if 'status'in OO0OOOOO000O0OO00 :#line:1181
                                    if OO0OOOOO000O0OO00 ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOOO000O0OO00["message"]}')#line:1183
                                    if OO0OOOOO000O0OO00 ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOOO000O0OO00["message"]}')#line:1185
                                        break #line:1186
                                if float (O000OO00OO000OOO0 )<78 :#line:1188
                                    OOOO000OO00OOO0O0 =80 -float (O000OO00OO000OOO0 )#line:1189
                                    O0OO0OOO00OOO0000 =f'_fertilizer={int(OOOO000OO00OOO0O0)}_{timi_new()}'#line:1190
                                    O00OO00OO0OO0OO0O ={'source':'scsc','authorization':O0O0000O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00OOO0000 ),'signstring':O0OO0OOO00OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    O0OO00000O00OO0OO ={"fertilizer":int (OOOO000OO00OOO0O0 )}#line:1202
                                    O0O000OOO0O0OOOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00OO00OO0OO0OO0O ,data =O0OO00000O00OO0OO ).json ()#line:1204
                                    if 'status'in O0O000OOO0O0OOOOO :#line:1206
                                        if O0O000OOO0O0OOOOO ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O0O000OOO0O0OOOOO["message"]}丨数量:{int(OOOO000OO00OOO0O0)}')#line:1208
                                        if O0O000OOO0O0OOOOO ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{O0O000OOO0O0OOOOO["message"]}丨数量:{int(OOOO000OO00OOO0O0)}')#line:1210
                                            OOOO0000000OO0OO0 =O0O000OOO0O0OOOOO ["message"].split ('-')[1 ]#line:1211
                                            OO000OOO0OO0O0O00 =f'__{timi_new()}'#line:1212
                                            O0OO0000OOOO0O0O0 ={'source':'scsc','authorization':O0O0000O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0OO0O0O00 ),'signstring':OO000OOO0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            O0O0O0O0O00O000O0 =requests .request ('get',f'{host}/user',headers =O0OO0000OOOO0O0O0 ).json ()#line:1224
                                            if 'status'in O0O0O0O0O00O000O0 :#line:1225
                                                if O0O0O0O0O00O000O0 ['status']==200 :#line:1226
                                                    OOOO0000OO0O0O0O0 =O0O0O0O0O00O000O0 ['data']['inner_id']#line:1227
                                                    if give_gold (OOOO0000OO0O0O0O0 ,float (OOOO0000000OO0OO0 )+1 ):#line:1228
                                                        O0O0000O00O0OOOO0 .energy ()#line:1229
                        if float (O0O0OO0O0OO0O0000 )<880 :#line:1230
                            if OO00000OO00O0OO00 :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                O0000O0O0O00OOO0O =999 -float (O0O0OO0O0OO0O0000 )#line:1233
                                OOOOOO00O0O0O0O00 ={"water":str (O0000O0O0O00OOO0O ).split ('.')[0 ]}#line:1234
                                OO00000O0O0O0O00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO0000OOOOO00OO0 ).json ()#line:1236
                                if 'status'in OO00000O0O0O0O00O :#line:1238
                                    if OO00000O0O0O0O00O ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OO00000O0O0O0O00O["message"]}')#line:1240
                                    if OO00000O0O0O0O00O ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{OO00000O0O0O0O00O["message"]}')#line:1242
                                        break #line:1243
                                if float (O0O0OO0O0OO0O0000 )<780 :#line:1244
                                    O0000O0O0O00OOO0O =800 -float (O0O0OO0O0OO0O0000 )#line:1245
                                    OO0O0000O0OOOOOO0 =f'_water={int(O0000O0O0O00OOO0O)}_{timi_new()}'#line:1246
                                    OOOO0OO0000O00O0O ={'source':'scsc','authorization':O0O0000O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0OOOOOO0 ),'signstring':OO0O0000O0OOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    O0O00000OOO0000O0 ={"water":int (O0000O0O0O00OOO0O )}#line:1258
                                    O0O0O0000O000OO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0OO0000O00O0O ,data =O0O00000OOO0000O0 ).json ()#line:1260
                                    if 'status'in O0O0O0000O000OO0O :#line:1262
                                        if O0O0O0000O000OO0O ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{O0O0O0000O000OO0O["message"]}丨数量:{int(O0000O0O0O00OOO0O)}')#line:1264
                                        if O0O0O0000O000OO0O ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{O0O0O0000O000OO0O["message"]}丨数量:{int(O0000O0O0O00OOO0O)}')#line:1266
                                            OOOO0000000OO0OO0 =O0O0O0000O000OO0O ["message"].split ('-')[1 ]#line:1267
                                            OO000OOO0OO0O0O00 =f'__{timi_new()}'#line:1268
                                            O0OO0000OOOO0O0O0 ={'source':'scsc','authorization':O0O0000O00O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0OO0O0O00 ),'signstring':OO000OOO0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            O0O0O0O0O00O000O0 =requests .request ('get',f'{host}/user',headers =O0OO0000OOOO0O0O0 ).json ()#line:1280
                                            if 'status'in O0O0O0O0O00O000O0 :#line:1281
                                                if O0O0O0O0O00O000O0 ['status']==200 :#line:1282
                                                    OOOO0000OO0O0O0O0 =O0O0O0O0O00O000O0 ['data']['inner_id']#line:1283
                                                    if give_gold (OOOO0000OO0O0O0O0 ,float (OOOO0000000OO0OO0 )+1 ):#line:1284
                                                        O0O0000O00O0OOOO0 .energy ()#line:1285
                        break #line:1286
        except Exception as O00OO000O00O00000 :#line:1287
            print (O00OO000O00O00000 )#line:1288
def bundled_def ():#line:1291
    O0OO0000O00O0OOOO =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return O0OO0000O00O0OOOO [random .randint (0 ,len (O0OO0000O00O0OOOO )-1 )]#line:1293
def version_of_the_validation ():#line:1297
    return str ((98 -56 )/10 )#line:1298
def ubbbf ():#line:1300
    print ('卡密验证通过   ✅')#line:1301
def sc2 ():#line:1304
    return "19319#$%^&*((*"#line:1305
def OO00OO0OO0OO00OO00o0 ():#line:1308
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1310
def get_ip ():#line:1313
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1315
def gitee_validation ():#line:1318
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1319
def gitee_edition ():#line:1322
    try :#line:1323
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1324
    except :#line:1325
        sys .exit (0 )#line:1326
def O000OO000O0O00OOO00 ():#line:1330
    try :#line:1331
        O00O00OO0000OO0O0 =gitee_edition ()#line:1332
        if version_of_the_validation ()<O00O00OO0000OO0O0 ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OO0000OO0O0["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{O00O00OO0000OO0O0["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00OO0000OO0O0["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {O00O00OO0000OO0O0["CityEarth"]["content"]}')#line:1338
    except Exception as O00O0OO0OO0O0O000 :#line:1339
        print (O00O0OO0OO0O0O000 )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
