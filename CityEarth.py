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
        OOOOO0OO00O00OOOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OOOOO0OO00O00OOOO)}个账号==========")#line:16
        for O000000000O0000OO in OOOOO0OO00O00OOOO :#line:17
            O0OOO000O0O0OO0OO =[]#line:18
            print (f"------------正在执行第{OOOOO0OO00O00OOOO.index(O000000000O0000OO) + 1}个账号------------")#line:19
            OOO0OOOO0O0OOOO00 =CityEarth (O000000000O0000OO ,O0OOO000O0O0OO0OO ,OOOOO0OO00O00OOOO .index (O000000000O0000OO ))#line:20
            def OO0000O00OO000O0O ():#line:22
                if OOO0OOOO0O0OOOO00 .base_info ():#line:24
                    OOO0OOOO0O0OOOO00 .sealing ()#line:26
                    OOO0OOOO0O0OOOO00 .invitenum ()#line:28
                    OOO0OOOO0O0OOOO00 .query_to_sell ()#line:30
                    OOO0OOOO0O0OOOO00 .game_map ()#line:32
                    OOO0OOOO0O0OOOO00 .friends_invitation ()#line:36
                    OOO0OOOO0O0OOOO00 .energy ()#line:38
                    OOO0OOOO0O0OOOO00 .add_clover ()#line:40
                    OOO0OOOO0O0OOOO00 .propsraffle ()#line:42
                    OOO0OOOO0O0OOOO00 .synthetic ()#line:44
                    OOO0OOOO0O0OOOO00 .crops_illustrated ()#line:46
                    OOO0OOOO0O0OOOO00 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OOO0OOOO0O0OOOO00 .give_gold ()#line:51
            O0000000O00OO000O =threading .Thread (target =OO0000O00OO000O0O )#line:53
            O0000000O00OO000O .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        OOO0OOOOOO00OOOO0 =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0OOOOOO00OOOO0 +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO0OOO0OO0OOOOO0 in invited_new :#line:62
            print (OOO0OOO0OO0OOOOO0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O0O00OOOOOO00OO0O in weishim :#line:65
            print (O0O00OOOOOO00OO0O )#line:66
    except Exception as OO00OOOOOOO0OO0OO :#line:67
        print (OO00OOOOOOO0OO0OO )#line:68
def give_gold (OOO0OOO000O00O0OO ,OOO0O0OO00O0OO000 ):#line:72
    try :#line:73
        O00OOOOO0OOO00000 =f'_doneeNo={OOO0OOO000O00O0OO}&quantity={int(OOO0O0OO00O0OO000)}_{timi_new()}'#line:74
        O00O0000O0000OO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0OOO00000 ),'signstring':O00OOOOO0OOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO00OO0OOO0OOOOOO ={"quantity":int (OOO0O0OO00O0OO000 ),"doneeNo":OOO0OOO000O00O0OO }#line:89
        O0OO0O0O00OO000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0000O0000OO00 ,data =OO00OO0OOO0OOOOOO ).json ()#line:90
        if 'status'in O0OO0O0O00OO000O0 :#line:92
            if O0OO0O0O00OO000O0 ['status']==200 :#line:93
                if O0OO0O0O00OO000O0 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO0O0OO00O0OO000)}种子给{OOO0OOO000O00O0OO}成功')#line:95
                    return True #line:96
            if O0OO0O0O00OO000O0 ['status']==401 :#line:97
                print (f'【赠送种子】:{O0OO0O0O00OO000O0["message"]}')#line:98
                return False #line:99
            if O0OO0O0O00OO000O0 ['status']==500 :#line:100
                print (f'【赠送种子】:{O0OO0O0O00OO000O0["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0000OO0O00OO000O :#line:104
        print (O0000OO0O00OO000O )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OOO00O00O0O00OOOO ):#line:115
    OO0000000O0O0OO0O =hashlib .md5 (OOO00O00O0O00OOOO .encode ()).hexdigest ()#line:116
    O0OO0O0000000OOO0 =sc1 ()#line:117
    OO0OO00OO0O0OO0OO =sc2 ()#line:118
    OOOO0O0OOOOOOO0O0 =sc3 ()#line:119
    OOOO0OO0000OO0O0O =O0OO0O0000000OOO0 +OO0000000O0O0OO0O +OO0OO00OO0O0OO0OO +OOOO0O0OOOOOOO0O0 #line:120
    OOO0O0O00O0OO0000 =hashlib .md5 (OOOO0OO0000OO0O0O .encode ()).hexdigest ()#line:121
    return OOO0O0O00O0OO0000 #line:122
def format_msg ():#line:125
    O0OO0O00O0O0O0000 =""#line:126
    for OOOOO000000OO00OO in msg_list :#line:127
        O0OO0O00O0O0O0000 +=str (OOOOO000000OO00OO )+"\r\n"#line:128
    return O0OO0O00O0O0O0000 #line:129
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
def get_json_data (OO00OOO000000OOO0 ,O000O000O0O00O00O ,OO0O00O00O0OOOOOO ,OO0O0O0O000OO0O0O ):#line:153
    with open (OO00OOO000000OOO0 ,'rb')as O000O0O0000000O0O :#line:154
        O0OO000OO00OOO0OO =json .load (O000O0O0000000O0O )#line:155
        O0OO000OO00OOO0OO ['data'][O000O000O0O00O00O ][OO0O00O00O0OOOOOO ]=OO0O0O0O000OO0O0O #line:156
        OO0000O0O0O0OO0OO =O0OO000OO00OOO0OO #line:157
    O000O0O0000000O0O .close ()#line:158
    return OO0000O0O0O0OO0OO #line:159
def write_json_data (O0OOOO000OO0OOOO0 ):#line:162
    with open (json_path1 ,'w')as O0O0O0O00O0O00O0O :#line:163
        json .dump (O0OOOO000OO0OOOO0 ,O0O0O0O00O0O00O0O )#line:164
    O0O0O0O00O0O00O0O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0O0000O000O00O00 ,OOO0OO0OO00O0000O ,OO00OO0OO0O0000O0 ,O0O000OOOOOOO00OO ):#line:171
        try :#line:172
            O0O0000O000O00O00 .msg =OO00OO0OO0O0000O0 #line:173
            O0O0000O000O00O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0O0000O000O00O00 .token =OOO0OO0OO00O0000O ['authorization']#line:175
            O0O0000O000O00O00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0O0000O000O00O00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0O0000O000O00O00 .elephant_user =OOO0OO0OO00O0000O ['elephant_user']#line:178
            O0O0000O000O00O00 .elephant_pswd =OOO0OO0OO00O0000O ['elephant_pswd']#line:179
            O0O0000O000O00O00 .elephant_Task_ID =OOO0OO0OO00O0000O ['elephant_Task_ID']#line:180
            O0O0000O000O00O00 .len_new =O0O000OOOOOOO00OO #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOOO0O0OO00O00O0 ):#line:186
        try :#line:187
            OOOOO0O0OO00O00O0 .watched_ad ()#line:189
            OOOOOOO0OOOO000O0 =f'__{timi_new()}'#line:190
            O0OO00O000O000O00 ={'source':'scsc','authorization':OOOOO0O0OO00O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOOO000O0 ),'signstring':OOOOOOO0OOOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0000O0OOOO00O0O0 =requests .request ('get',f'{host}/user',headers =O0OO00O000O000O00 ).json ()#line:202
            if 'status'in O0000O0OOOO00O0O0 :#line:204
                if O0000O0OOOO00O0O0 ['status']==200 :#line:205
                    O0000O0000OOO0O0O =O0000O0OOOO00O0O0 ['data']['nickname']#line:206
                    O0O00000O0OO00O00 =O0000O0OOOO00O0O0 ['data']['inner_id']#line:207
                    OOO0OOOOO0OOO0O00 =O0000O0OOOO00O0O0 ['data']['assets']['gold']#line:208
                    OOOO0OOOOOOOO0000 =O0000O0OOOO00O0O0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O0000O0000OOO0O0O[:5]}丨ID:{O0O00000O0OO00O00}丨等级:{OOOO0OOOOOOOO0000}丨金种子:{str(OOO0OOOOO0OOO0O00).split(".")[0]}')#line:211
                    if 'wx_'in O0000O0000OOO0O0O :#line:212
                        OOOOO0O0OO00O00O0 .change_nickname ()#line:213
                if O0000O0OOOO00O0O0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOOO0O0OO00O00O0 .elephant_user =='f':#line:216
                        return False #line:217
                    O00OO0O0000000OOO =Invalid_login .addtask (elephant_user =OOOOO0O0OO00O00O0 .elephant_user ,elephant_pswd =OOOOO0O0OO00O00O0 .elephant_pswd ,elephant_Task_ID =OOOOO0O0OO00O00O0 .elephant_Task_ID )#line:220
                    O00O000000O000O0O =get_json_data (json_path ,OOOOO0O0OO00O00O0 .len_new ,'authorization',O00OO0O0000000OOO )#line:221
                    if write_json_data (O00O000000O000O0O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0000O0OOOO00O0O0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO00O00O00O00OOO :#line:228
            print (OOO00O00O00O00OOO )#line:229
    def sealing (OO00O0O0O0O0OO000 ):#line:232
        try :#line:233
            OOO0OOOO0OOOOOOO0 =f'__{timi_new()}'#line:234
            O0O00OO0O0OOOO0OO ={'source':'scsc','authorization':OO00O0O0O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0OOOOOOO0 ),'signstring':OOO0OOOO0OOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O00OO0O0OOOO0OO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0O00OO0O0OOOO0OO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O00OO0O0OOOO0OO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O00OO0O0OOOO0OO )#line:249
            requests .request ('get',f'{host}/user',headers =O0O00OO0O0OOOO0OO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O00OO0O0OOOO0OO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O00OO0O0OOOO0OO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O00OO0O0OOOO0OO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO0O0OOOO0OO )#line:254
            requests .request ('get',f'{host}/assets',headers =O0O00OO0O0OOOO0OO )#line:255
        except Exception as OOOOOO0O0OOO0OO00 :#line:256
            print (OOOOOO0O0OOO0OO00 )#line:257
    def ddd (O0O00OO0O0OO0O0OO ):#line:259
        try :#line:260
            OO0O00O0OOO00OO00 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO000OOOO0000O000 ={'source':'scsc','authorization':O0O00OO0O0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OOO00OO00 ),'signstring':OO0O00O0OOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO000O0O00O0OO00O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO000OOOO0000O000 ).json ()#line:273
            print (OO000O0O00O0OO00O )#line:274
        except Exception as O0000O00OOO00OOO0 :#line:279
            print (O0000O00OOO00OOO0 )#line:280
    def the_query (OO000OOOO00O00OO0 ):#line:290
        try :#line:291
            O00OOO0O00OOOOO00 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            O0000O0O0OOOO0O00 ={'authorization':OO000OOOO00O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O00OOOOO00 ),'signstring':O00OOO0O00OOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            OOOOOO00OO000000O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0000O0O0OOOO0O00 ).json ()#line:304
            if 'status'in OOOOOO00OO000000O :#line:306
                if OOOOOO00OO000000O ['status']==200 :#line:307
                    O00OOOO000000OOOO =OOOOOO00OO000000O ['data']['rows'][4 ]['price']#line:308
                    OO000OOOO00O00OO0 .market_sale (O00OOOO000000OOOO )#line:309
        except Exception as OOOOOO00000OOO000 :#line:310
            print (OOOOOO00000OOO000 )#line:311
    def market_sale (O0OOO000OOOO0O0OO ,OOO00000000OOO00O ):#line:314
        try :#line:315
            OOO000OO0O000OO0O =timi_new ()#line:316
            OO000O000OO0OOO00 =f'type=crop__{OOO000OO0O000OO0O}'#line:317
            O0OO0O00OO00OO0OO ={'source':'scsc','authorization':O0OOO000OOOO0O0OO .token ,'timestamp':str (OOO000OO0O000OO0O ),'sign':sign (OO000O000OO0OOO00 ),'signstring':OO000O000OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O0OO00O00000OOOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0OO0O00OO00OO0OO ).json ()#line:330
            if 'status'in O0OO00O00000OOOO0 :#line:332
                if O0OO00O00000OOOO0 ['status']==200 :#line:333
                    if O0OO00O00000OOOO0 ['data']['rows']:#line:334
                        OO000O0OO0OOOOOOO =O0OO00O00000OOOO0 ['data']['rows'][0 ]['packsackItemId']#line:335
                        OO0O00OOO0OO0OOOO =O0OO00O00000OOOO0 ['data']['rows'][0 ]['quantity']#line:336
                        OO0OOO0O00OOOO0OO =float (OOO00000000OOO00O )-0.001 #line:337
                        if OO0OOO0O00OOOO0OO >8 :#line:338
                            OOOO000O00O0O0O00 =f'_packsackItemId={OO000O0OO0OOOOOOO}&price={str(OOO00000000OOO00O)[:6]}&quantity={OO0O00OOO0OO0OOOO}_{OOO000OO0O000OO0O}'#line:339
                            O0OO0OO0OO00O0OOO ={'source':'scsc','authorization':O0OOO000OOOO0O0OO .token ,'timestamp':str (OOO000OO0O000OO0O ),'sign':sign (OOOO000O00O0O0O00 ),'signstring':OOOO000O00O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            OO000OOO00OOOOOO0 ={"packsackItemId":OO000O0OO0OOOOOOO ,"price":str (OOO00000000OOO00O )[:6 ],"quantity":str (OO0O00OOO0OO0OOOO )}#line:355
                            OOO0OOOOO000O0O00 =requests .request ('post',f'{host}/market/sale',headers =O0OO0OO0OO00O0OOO ,data =OO000OOO00OOOOOO0 ).json ()#line:356
                            if 'status'in OOO0OOOOO000O0O00 :#line:358
                                if OOO0OOOOO000O0O00 ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{OO0O00OOO0OO0OOOO}丨价格:{str(OOO00000000OOO00O)[:6]}')#line:360
        except Exception as OO0OO000OO0OOO0O0 :#line:361
            print (OO0OO000OO0OOO0O0 )#line:362
    def query_to_sell (OOO0OOOO00O0OO00O ):#line:365
        try :#line:366
            O000OO0O000OOOO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            OOOOO0OOOO00OO0O0 ={'source':'scsc','authorization':OOO0OOOO00O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O000OOOO00 ),'signstring':O000OO0O000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            O0O0OO000OO00OOO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOOO0OOOO00OO0O0 ).json ()#line:380
            if 'status'in O0O0OO000OO00OOO0 :#line:382
                if O0O0OO000OO00OOO0 ['status']==200 :#line:383
                    for O00O00O0O000OOOO0 in O0O0OO000OO00OOO0 ['data']['rows']:#line:384
                        OOO0O00OO0O0O0OO0 =O00O00O0O000OOOO0 ['materialKey']#line:385
                        O0O000O00O0OO000O =O00O00O0O000OOOO0 ['quantity']#line:386
                        O00O00O0O0OOOOOOO =O00O00O0O000OOOO0 ['price']#line:387
                        OOO0O0OOOO00O000O =O00O00O0O000OOOO0 ['saleState']#line:388
                        if OOO0O0OOOO00O000O ==0 :#line:389
                            print (f'【出售订单】:名称:{OOO0O00OO0O0O0OO0}丨数量:{O0O000O00O0OO000O}丨价格:{O00O00O0O0OOOOOOO}')#line:390
                            O0O0O0O0000OOOO00 =O00O00O0O000OOOO0 ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                OOO0OOOO00O0OO00O .cacel_sale (O0O0O0O0000OOOO00 )#line:393
        except Exception as OOOO0OO0O0O0OOOO0 :#line:394
            print (OOOO0OO0O0O0OOOO0 )#line:395
    def cacel_sale (O00O0OO000OO0O0OO ,OOOO000O0O00000OO ):#line:398
        try :#line:399
            O00OOOOO0OOO0OOO0 =f'_saleId={OOOO000O0O00000OO}_{timi_new()}'#line:400
            OO0000O0OOOOO00OO ={'source':'scsc','authorization':O00O0OO000OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0OOO0OOO0 ),'signstring':O00OOOOO0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O000OOOO0O0OOOOOO ={"saleId":OOOO000O0O00000OO }#line:414
            O0O00OO000OOO0000 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0000O0OOOOO00OO ,data =O000OOOO0O0OOOOOO ).json ()#line:415
            if 'status'in O0O00OO000OOO0000 :#line:417
                if O0O00OO000OOO0000 ['status']==200 :#line:418
                    print (f'【下架出售】:{O0O00OO000OOO0000["data"]}')#line:419
        except Exception as O00OOOO0O00OOOO00 :#line:420
            print (O00OOOO0O00OOOO00 )#line:421
    def change_nickname (O000OO00O0OO0O0O0 ):#line:424
        try :#line:425
            O0OOO000O0O000000 =timi_new ()#line:426
            O0OO0OO0O000OO000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOO0000O0000OO00O =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO0OO0O000OO000 ).text #line:428
            O0000O0O00O0O00OO =re .findall ('<ul><li>(.*?)</li>',OOO0000O0000OO00O )[0 ][:3 ]#line:429
            O0O0O00O00O0O0O00 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0000O0O00O0O00OO}').json ()#line:430
            O0000OOO000000O00 =O0O0O00O00O0O0O00 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            O00O00000O00000O0 ={"nickname":O0000OOO000000O00 }#line:432
            OOO0OO00OO0000000 =f'_nickname={O0000OOO000000O00}_{O0OOO000O0O000000}'#line:433
            OOOO000000OO0OO0O ={'source':'scsc','authorization':O000OO00O0OO0O0O0 .token ,'timestamp':O0OOO000O0O000000 ,'sign':sign (OOO0OO00OO0000000 ),'signstring':OOO0OO00OO0000000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            OO0OOO0O0O0O00O0O =requests .request ('patch',f'{host}/user/nickname',headers =OOOO000000OO0OO0O ,data =O00O00000O00000O0 ).json ()#line:445
            if 'status'in OO0OOO0O0O0O00O0O :#line:447
                if OO0OOO0O0O0O00O0O ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O0000OOO000000O00}丨{OO0OOO0O0O0O00O0O["message"]}')#line:449
        except Exception as OOOO00O00O000OO00 :#line:450
            print (OOOO00O00O000OO00 )#line:451
    def withdraw (O000O0O00OOOO000O ):#line:454
        try :#line:455
            OOOO00OO00OO0O0O0 =f'__{timi_new()}'#line:456
            OO000O0O0O0O0OO00 ={'source':'scsc','authorization':O000O0O00OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00OO0O0O0 ),'signstring':OOOO00OO00OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OOO0O0OOOO0O00OO0 =requests .request ('get',f'{host}/assets',headers =OO000O0O0O0O0OO00 ).json ()#line:468
            if 'status'in OOO0O0OOOO0O00OO0 :#line:470
                if OOO0O0OOOO0O00OO0 ['status']==200 :#line:471
                    O00OO0O00OO0OOOO0 =OOO0O0OOOO0O00OO0 ['data']['cash']#line:472
                    if float (O00OO0O00OO0OOOO0 )>20 :#line:473
                        OOOO00OO00OO0O0O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        OO000O0O0O0O0OO00 ={'authorization':O000O0O00OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00OO0O0O0 ),'signstring':OOOO00OO00OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        O0O00OO00O0000OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OOO0OOO0O00OO00OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO000O0O0O0O0OO00 ,data =O0O00OO00O0000OOO ).json ()#line:487
                        if 'status'in OOO0OOO0O00OO00OO :#line:489
                            if OOO0OOO0O00OO00OO ['status']==200 :#line:490
                                print (f'【余额提现】:{OOO0OOO0O00OO00OO["data"]}')#line:491
                        if 'status'in OOO0OOO0O00OO00OO :#line:492
                            if OOO0OOO0O00OO00OO ['status']==500 :#line:493
                                print (f'【余额提现】:{OOO0OOO0O00OO00OO["message"]}')#line:494
        except Exception as OO0O0OO0O0O000O00 :#line:495
            print (OO0O0OO0O0O000O00 )#line:496
    def invitenum (O00O0OO0OO00O000O ):#line:499
        global invited_new #line:500
        try :#line:501
            OO000O00000O000O0 =f'__{timi_new()}'#line:502
            OOO000O0OOO00O0OO ={'source':'scsc','authorization':O00O0OO0OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00000O000O0 ),'signstring':OO000O00000O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O00OO0OOOO0OOO00O =requests .request ('get',f'{host}/invite/invitenum',headers =OOO000O0OOO00O0OO ).json ()#line:514
            if 'status'in O00OO0OOOO0OOO00O :#line:516
                if O00OO0OOOO0OOO00O ['status']==200 :#line:517
                    OO00O0O000OOOO0OO =O00OO0OOOO0OOO00O ['data']['invited_count']#line:518
                    OO0O0O0OOOOO0OOOO =O00OO0OOOO0OOO00O ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OO00O0O000OOOO0OO}丨间邀好友:{OO0O0O0OOOOO0OOOO}')#line:520
                    if OO00O0O000OOOO0OO <2 :#line:521
                        OO00OOO00OOOO0OOO =f'__{timi_new()}'#line:522
                        OO00OO00000O0O00O ={'source':'scsc','authorization':O00O0OO0OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00OOOO0OOO ),'signstring':OO00OOO00OOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OO0O0OOOOO000000O =requests .request ('get',f'{host}/user',headers =OO00OO00000O0O00O ).json ()#line:534
                        if 'status'in OO0O0OOOOO000000O :#line:536
                            if OO0O0OOOOO000000O ['status']==200 :#line:537
                                invited_new .append (OO0O0OOOOO000000O ['data']['inner_id'])#line:538
        except Exception as OOOOOOO000OO00000 :#line:539
            print (OOOOOOO000OO00000 )#line:540
    def game_map (O0000O0O00OOO0OO0 ):#line:543
        try :#line:544
            O0OO00OO0OO0000O0 =f'__{timi_new()}'#line:545
            O0OO0OO0OOO00O00O ={'source':'scsc','authorization':O0000O0O00OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0OO0000O0 ),'signstring':O0OO00OO0OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O0OO0OOO00OOOO0OO =requests .request ('get',f'{host}/game/map',headers =O0OO0OO0OOO00O00O ).json ()#line:557
            if 'status'in O0OO0OOO00OOOO0OO :#line:559
                if O0OO0OOO00OOOO0OO ['status']==200 :#line:560
                    for OOO00OO0000OOOOOO in O0OO0OOO00OOOO0OO ['data']['list'][0 ]['crops']:#line:561
                        OO0OO0O00OOO0O00O =OOO00OO0000OOOOOO ['level']#line:563
                        if OO0OO0O00OOO0O00O ==41 :#line:564
                            O00OO000OOO0O0OOO =OOO00OO0000OOOOOO ['crop_name']#line:565
                            O0O0000OO0O0O0000 =OOO00OO0000OOOOOO ['count']#line:566
                            if O0O0000OO0O0O0000 >0 :#line:567
                                print (f'【农业资产】:{O00OO000OOO0O0OOO}丨数量:{O0O0000OO0O0O0000}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    O0000O0O00OOO0OO0 .the_query ()#line:570
        except Exception as O0OO0O0O00000O000 :#line:571
            print (O0OO0O0O00000O000 )#line:572
    def give_gold (OO00OOOOOOO0000O0 ):#line:575
        try :#line:576
            OOO0O00O0OOO0O000 =f'__{timi_new()}'#line:577
            O00O0O0O000O00OO0 ={'source':'scsc','authorization':OO00OOOOOOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O0OOO0O000 ),'signstring':OOO0O00O0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            O00OOOOOOOO00OOOO =requests .request ('get',f'{host}/user',headers =O00O0O0O000O00OO0 ).json ()#line:589
            if 'status'in O00OOOOOOOO00OOOO :#line:590
                if O00OOOOOOOO00OOOO ['status']==200 :#line:591
                    if float (OO00OOOOOOO0000O0 .doneeNo )!=0 :#line:592
                        O00O0O00000O000O0 =O00OOOOOOOO00OOOO ['data']['assets']['gold']#line:593
                        if float (O00O0O00000O000O0 )>float (OO00OOOOOOO0000O0 .innerId ):#line:594
                            OO0OO000000OO000O =int (float (O00O0O00000O000O0 )/1.1 )#line:595
                            OOO0O00O0OOO0O000 =f'_doneeNo={OO00OOOOOOO0000O0.doneeNo}&quantity={OO0OO000000OO000O}_{timi_new()}'#line:596
                            O00O0O0O000O00OO0 ={'source':'scsc','authorization':OO00OOOOOOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O0OOO0O000 ),'signstring':OOO0O00O0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            O0OOOO0O0O0000000 ={"quantity":OO0OO000000OO000O ,"doneeNo":OO00OOOOOOO0000O0 .doneeNo }#line:611
                            OO0000O0OOOOO00O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0O0O000O00OO0 ,data =O0OOOO0O0O0000000 ).json ()#line:612
                            if 'status'in OO0000O0OOOOO00O0 :#line:614
                                if OO0000O0OOOOO00O0 ['status']==200 :#line:615
                                    if OO0000O0OOOOO00O0 ['data']:#line:616
                                        print (f'【赠送种子】:赠送{OO0OO000000OO000O}种子给{OO00OOOOOOO0000O0.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as O0OOOO00000OO0OOO :#line:620
            print (O0OOOO00000OO0OOO )#line:621
    def invitation (O000OOO0OOOOOOOO0 ):#line:623
        try :#line:624
            _O0OO0OO0OOO0OOO00 =float (bundled_def ())/4 #line:625
            O0OOO00O0O0O00000 =f'_innerId={int(_O0OO0OO0OOO0OOO00)}_{timi_new()}'#line:626
            OO00O0O0OO0O0OOOO ={'source':'scsc','authorization':O000OOO0OOOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0O00000 ),'signstring':O0OOO00O0O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            OO000OOOO00O00OOO ={"innerId":int (_O0OO0OO0OOO0OOO00 )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00O0O0OO0O0OOOO ,data =OO000OOOO00O00OOO )#line:639
        except Exception as O0000O0OO00OOO000 :#line:640
            print (O0000O0OO00OOO000 )#line:641
    def winning_rewards (OO0OO00O00OO00O0O ):#line:644
        try :#line:645
            O000O00OOO00O00OO =f'__{timi_new()}'#line:646
            OO000O0O00OOO00OO ={'source':'scsc','authorization':OO0OO00O00OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO00O00OO ),'signstring':O000O00OOO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            OOO000OO0000O0O0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO000O0O00OOO00OO ).json ()#line:658
            if 'status'in OOO000OO0000O0O0O :#line:660
                if OOO000OO0000O0O0O ['status']==200 :#line:661
                    if OOO000OO0000O0O0O ['data']['amount']:#line:662
                        OO0OO0OOO0O00OO00 =OOO000OO0000O0O0O ['data']['amount']['gold']#line:663
                        return OO0OO0OOO0O00OO00 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as OOOOOOOOO0O0OOO0O :#line:667
            print (OOOOOOOOO0O0OOO0O )#line:668
    def certification (O0O0O00O0O00OOO0O ):#line:671
        try :#line:672
            OOO0OOO000O00O00O =f'__{timi_new()}'#line:673
            O0000OOO0OO0O0OOO ={'source':'scsc','authorization':O0O0O00O0O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO000O00O00O ),'signstring':OOO0OOO000O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            OO0000O0OO00O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000OOO0OO0O0OOO ).json ()#line:685
            if 'status'in OO0000O0OO00O00O0 :#line:687
                if OO0000O0OO00O00O0 ['status']==200 :#line:688
                    if OO0000O0OO00O00O0 ['data']['result']:#line:689
                        O00O000000OO0OO00 =OO0000O0OO00O00O0 ['data']['nick_name']#line:690
                        return O00O000000OO0OO00 #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as OOO00OO0OOOOOOO0O :#line:694
            print (OOO00OO0OOOOOOO0O )#line:695
    def crops_illustrated (O00O000OO00O0O000 ):#line:698
        try :#line:699
            O00OOOO00OO0O0O00 =f'__{timi_new()}'#line:700
            O0OOO0O0OOOOO0O00 ={'source':'scsc','authorization':O00O000OO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OO0O0O00 ),'signstring':O00OOOO00OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            O000OOOOO00O00OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO0O0OOOOO0O00 ).json ()#line:712
            if 'status'in O000OOOOO00O00OO0 :#line:714
                if O000OOOOO00O00OO0 ['status']==200 :#line:715
                    OOOO000OO0O0O0000 =O000OOOOO00O00OO0 ['data'][0 ]['crops']#line:716
                    for OOOO0O000OOOO0OOO in OOOO000OO0O0O0000 :#line:717
                        if OOOO0O000OOOO0OOO ['ill_clover_award']:#line:718
                            if float (OOOO0O000OOOO0OOO ['ill_clover_award'])>1 :#line:719
                                if OOOO0O000OOOO0OOO ['is_finish']:#line:720
                                    if not OOOO0O000OOOO0OOO ['is_getit']:#line:721
                                        if O00O000OO00O0O000 .certification ()!='未实名':#line:722
                                            O00OOOO00OO0O0O00 =f'_award_level={OOOO0O000OOOO0OOO["level"]}_{timi_new()}'#line:723
                                            O0OOO0O0OOOOO0O00 ={'source':'scsc','authorization':O00O000OO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OO0O0O00 ),'signstring':O00OOOO00OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            O0O00O0000OO00O0O ={"award_level":OOOO0O000OOOO0OOO ['level']}#line:735
                                            O000000O00OOO000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO0O0OOOOO0O00 ,json =O0O00O0000OO00O0O ).json ()#line:737
                                            if 'status'in O000000O00OOO000O :#line:738
                                                if O000000O00OOO000O ['status']==200 :#line:739
                                                    O00OO00O0OOOO0OOO =O000000O00OOO000O ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{OOOO0O000OOOO0OOO["crop_name"]}成就丨奖励{O00OO00O0OOOO0OOO}☘️')#line:742
                                                if O000000O00OOO000O ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{O000000O00OOO000O["message"]}')#line:744
        except Exception as O0OOO0000000O000O :#line:745
            print (O0OOO0000000O000O )#line:746
    def watched_ad (O00O0OOO000O000O0 ):#line:749
        try :#line:750
            O000O000OOOOOO00O =f'__{timi_new()}'#line:751
            O0O00O0OO0OOO0O0O ={'source':'scsc','authorization':O00O0OOO000O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O000OOOOOO00O ),'signstring':O000O000OOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            O000OO0OOO0OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0OO0OOO0O0O ).json ()#line:763
            if 'status'in O000OO0OOO0OO0O0O :#line:765
                if O000OO0OOO0OO0O0O ['status']==200 :#line:766
                    if 'offlineInfo'in O000OO0OOO0OO0O0O ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        OO0OO0OO000O000OO =O000OO0OOO0OO0O0O ['data']['offlineInfo']['off_minute']#line:769
                        OO00OO0OO00O0000O =float (O000OO0OOO0OO0O0O ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O00O0OO0OOO0O0O ).json ()#line:772
                        time .sleep (2 )#line:773
                        OO000OOOO0OOOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0OO0OOO0O0O ).json ()#line:774
                        if 'status'in OO000OOOO0OOOOO00 :#line:776
                            if OO000OOOO0OOOOO00 ['status']==200 :#line:777
                                O0000OOOO00000O00 =float (OO000OOOO0OOOOO00 ['data']['silver'])/1000000000000 #line:778
                                O000OOO0OO00OOOOO =str (O0000OOOO00000O00 -OO00OO0OO00O0000O )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{OO0OO0OO000O000OO}分钟奖励🌱数量:{O000OOO0OO00OOOOO}t粒')#line:780
        except Exception as O0000OOO00000OO0O :#line:781
            print (O0000OOO00000OO0O )#line:782
    def user_ad (O0O0O0O0000O00OO0 ):#line:785
        try :#line:786
            OOOOOO0000O00O0OO =f'__{timi_new()}'#line:787
            O0O00OOOOOOO0O00O ={'source':'scsc','authorization':O0O0O0O0000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000O00O0OO ),'signstring':OOOOOO0000O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            O000O00OOO000O000 =requests .request ('get',f'{host}/user/ad',headers =O0O00OOOOOOO0O00O ).json ()#line:799
            if 'status'in O000O00OOO000O000 :#line:801
                if O000O00OOO000O000 ['status']==200 :#line:802
                    O0O00O00000000000 =O000O00OOO000O000 ['data']['max_time']#line:803
                    O0O000O00OOO0O0O0 =O000O00OOO000O000 ['data']['watch_time']#line:804
                    OOOO0000OO000O0OO =O000O00OOO000O000 ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{OOOO0000OO000O0OO + O0O00O00000000000 - O0O000O00OOO0O0O0}次丨好友提供:{OOOO0000OO000O0OO}次')#line:806
                    if OOOO0000OO000O0OO +O0O00O00000000000 -O0O000O00OOO0O0O0 >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        O000O0000O0OOO0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00OOOOOOO0O00O ).json ()#line:809
                        if 'status'in O000O0000O0OOO0OO :#line:811
                            if O000O0000O0OOO0OO ['status']==200 :#line:812
                                O00OOO0OOO0O00000 =float (O000O0000O0OOO0OO ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(O00OOO0OOO0O00000)}t粒')#line:814
                                return True #line:815
                            if O000O0000O0OOO0OO ['status']==500 :#line:816
                                OOOOOOO0000OO0O00 =O000O0000O0OOO0OO ['message']#line:817
                                print (f'【获取种子】:{OOOOOOO0000OO0O00}')#line:818
                                return False #line:819
        except Exception as OO00OOO0OO0OOO000 :#line:820
            print (OO00OOO0OO0OOO000 )#line:821
    def synthetic (O00OOOO00O0OO0OO0 ):#line:824
        global id ,g #line:825
        try :#line:826
            O0O00O00OO000OOOO =O00OOOO00O0OO0OO0 .level_new ()#line:827
            OO0O0O000O0OO00O0 =random .randint (9 ,11 )#line:828
            OOOOO000OOOOOO000 =f'_site=8&targetSite={OO0O0O000O0OO00O0}_{timi_new()}'#line:829
            O00O000OOOOOOO0OO ={'source':'scsc','authorization':O00OOOO00O0OO0OO0 .token ,'timestamp':timi_new (),'sign':sign (OOOOO000OOOOOO000 ),'signstring':OOOOO000OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            O0O0OO0OO0OO00O00 ={"site":int (8 ),"targetSite":int (OO0O0O000O0OO00O0 )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O00O000OOOOOOO0OO ,json =O0O0OO0OO0OO00O00 )#line:842
            while True :#line:843
                O0OO00O00O0O000O0 =f'__{timi_new()}'#line:844
                OOOO000O00OOO0OOO ={'source':'scsc','authorization':O00OOOO00O0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00O0O000O0 ),'signstring':O0OO00O00O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                O0OO000OOO0O00O00 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O00OOO0OOO ).json ()#line:856
                if 'status'in O0OO000OOO0O00O00 :#line:858
                    if O0OO000OOO0O00O00 ['status']==200 :#line:859
                        O00O00O000000OOOO =O0OO000OOO0O00O00 ['data']['cropList']#line:860
                        O000OOO0O00OO000O =O0OO000OOO0O00O00 ['data']['gameCoreDataDBid']#line:861
                        OOOO0OOO0O0000OOO =float (O0OO000OOO0O00O00 ['data']['silver'])/1000000000000 #line:862
                        OOOOO0OO000OO00OO =0 #line:867
                        for OOO00OO0O0O00OOO0 in O00O00O000000OOOO :#line:868
                            if not OOO00OO0O0O00OOO0 :#line:869
                                O0O0O00OO00000O00 =f'_crop_id={O000OOO0O00OO000O}&site={OOOOO0OO000OO00OO}_{O00OOOO00O0OO0OO0.time}'#line:870
                                O0OO00OO000OO0O0O ={'source':'scsc','authorization':O00OOOO00O0OO0OO0 .token ,'timestamp':O00OOOO00O0OO0OO0 .time ,'sign':sign (O0O0O00OO00000O00 ),'signstring':O0O0O00OO00000O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                O00OO0O0OO0000O00 ={"site":OOOOO0OO000OO00OO ,"crop_id":O000OOO0O00OO000O }#line:881
                                OOOO000O0OOO0OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0OO00OO000OO0O0O ,data =O00OO0O0OO0000O00 ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in OOOO000O0OOO0OOO0 :#line:885
                                    if OOOO000O0OOO0OOO0 ['status']==200 :#line:886
                                        if OOOO000O0OOO0OOO0 ['message']=='种子数量不足':#line:887
                                            O0O00O00OO000OOOO =O00OOOO00O0OO0OO0 .level_new ()#line:888
                                            print (f'【种植合成】:{OOOO000O0OOO0OOO0["message"]}')#line:889
                                            if not O00OOOO00O0OO0OO0 .user_ad ():#line:890
                                                return False #line:891
                                    if OOOO000O0OOO0OOO0 ['status']==500 :#line:892
                                        print (f'【种植合成】:{OOOO000O0OOO0OOO0["message"]}')#line:893
                                        return False #line:894
                            OOOOO0OO000OO00OO +=1 #line:895
                        O0OOO0000O0000OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O00OOO0OOO ).json ()#line:896
                        OO0O00OO00OOO0O00 =O0OOO0000O0000OOO ['data']['cropList']#line:897
                        OO0O00000000O0000 =False #line:898
                        for OOO00OO0O0O00OOO0 in range (12 ):#line:899
                            id =OO0O00OO00OOO0O00 [OOO00OO0O0O00OOO0 ]['level']#line:900
                            if float (O0O00O00OO000OOOO )-float (id )>9 :#line:901
                                O00O0O000O00O0OOO =f'_site={OOO00OO0O0O00OOO0}_{timi_new()}'#line:902
                                O000O00O0000OO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OOOO00O0OO0OO0 .token ,'timestamp':timi_new (),'sign':sign (O00O0O000O00O0OOO ),'signstring':O00O0O000O00O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                O00O0OO0OOOOOO0O0 ={"site":OOO00OO0O0O00OOO0 }#line:914
                                OOO0OO0OOOOO0O000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O00O0000OO000 ,data =O00O0OO0OOOOOO0O0 ).json ()#line:916
                                if 'status'in OOO0OO0OOOOO0O000 :#line:917
                                    if OOO0OO0OOOOO0O000 ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O0O0O00OO0OOO0OO0 in range (11 ):#line:921
                                    OO000000OOOOO0O0O =O0O0O00OO0OOO0OO0 +1 #line:922
                                    g =OO0O00OO00OOO0O00 [OO000000OOOOO0O0O ]['level']#line:923
                                    if id ==g :#line:924
                                        O0OO00OO0O00OO0O0 =O0O0O00OO0OOO0OO0 +2 #line:925
                                        if O0OO00OO0O00OO0O0 !=OOO00OO0O0O00OOO0 +1 :#line:926
                                            O0000000O00O00OO0 =OOO00OO0O0O00OOO0 +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            OOOOO000OOOOOO000 =f'_site={O0000000O00O00OO0 - 1}&targetSite={O0OO00OO0O00OO0O0 - 1}_{timi_new()}'#line:930
                                            O00O000OOOOOOO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OOOO00O0OO0OO0 .token ,'timestamp':timi_new (),'sign':sign (OOOOO000OOOOOO000 ),'signstring':OOOOO000OOOOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O0OOO0O0000OOO00O ={"site":int (O0000000O00O00OO0 -1 ),"targetSite":int (O0OO00OO0O00OO0O0 -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00O000OOOOOOO0OO ,json =O0OOO0O0000OOO00O )#line:949
                                            OO0O00000000O0000 =True #line:951
                                    if OO0O00000000O0000 :#line:952
                                        break #line:953
                                if OO0O00000000O0000 :#line:954
                                    break #line:955
        except :#line:956
            O00OOOO00O0OO0OO0 .synthetic ()#line:957
    def level_new (O0O0OOO00O0O00OOO ):#line:960
        try :#line:961
            OOOO000000000O000 =f'__{timi_new()}'#line:962
            OOOO00O0OOOOOOO0O ={'source':'scsc','authorization':O0O0OOO00O0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000000000O000 ),'signstring':OOOO000000000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OOO000O000O0O00O0 =requests .request ('get',f'{host}/user',headers =OOOO00O0OOOOOOO0O ).json ()#line:974
            if 'status'in OOO000O000O0O00O0 :#line:975
                if OOO000O000O0O00O0 ['status']==200 :#line:976
                    return float (OOO000O000O0O00O0 ['data']['level'])#line:977
        except Exception as OOOO000OO0O0OOO0O :#line:978
            print (OOOO000OO0O0OOO0O )#line:979
    def propsraffle (OO00OOOO0OOOO00OO ):#line:982
        try :#line:983
            while True :#line:984
                OOO0OO000O00OOOO0 =f'__{timi_new()}'#line:985
                O00OOOO000OO00O0O ={'source':'scsc','authorization':OO00OOOO0OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO000O00OOOO0 ),'signstring':OOO0OO000O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                O00OO0OO0O00OO000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OOOO000OO00O0O ).json ()#line:997
                if 'status'in O00OO0OO0O00OO000 :#line:999
                    if O00OO0OO0O00OO000 ['status']==200 :#line:1000
                        OOO000000O000000O =O00OO0OO0O00OO000 ['data']['rows']#line:1001
                        O00OO00000OOOO000 =O00OO0OO0O00OO000 ['data']['vstate']#line:1002
                        if OOO000000O000000O ==5 or OOO000000O000000O ==6 or OOO000000O000000O ==7 :#line:1003
                            O0O000O0O00OOOOOO =O00OO0OO0O00OO000 ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{O0O000O0O00OOOOOO}')#line:1005
                        if OOO000000O000000O ==1 or OOO000000O000000O ==2 or OOO000000O000000O ==3 :#line:1006
                            O0O00OO00O000000O =O00OO0OO0O00OO000 ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{O0O00OO00O000000O}')#line:1008
                        if OOO000000O000000O ==4 or OOO000000O000000O ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if OOO000000O000000O =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as OOO0OO00OOO0O0O00 :#line:1050
            print (OOO0OO00OOO0O0O00 )#line:1051
    def friends_invitation (OO000O00O0OOOO00O ):#line:1054
        try :#line:1055
            OO00O000OO0000OO0 =f'__{timi_new()}'#line:1056
            OO000O00O000O0OOO ={'source':'scsc','authorization':OO000O00O0OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO0000OO0 ),'signstring':OO00O000OO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            OOOO0O00OO00O0O00 =requests .request ('get',f'{host}/friends',headers =OO000O00O000O0OOO ).json ()#line:1068
            if 'status'in OOOO0O00OO00O0O00 :#line:1069
                if OOOO0O00OO00O0O00 ['status']==200 :#line:1070
                    O0O000OO0000OOO00 =OOOO0O00OO00O0O00 ['data']['myInviteter']#line:1071
                    if O0O000OO0000OOO00 :#line:1072
                        OOO00OOO0000OOO0O =O0O000OO0000OOO00 ['user']['nickname']#line:1073
                        O00O0OOO0OOO0OOO0 =OO000O00O0OOOO00O .certification ()#line:1074
                        if O00O0OOO0OOO0OOO0 =='未实名':#line:1075
                            weishim .append (OO000O00O0OOOO00O .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{OOO00OOO0000OOO0O}丨实名:{O00O0OOO0OOO0OOO0}')#line:1077
                    else :#line:1078
                        if OO000O00O0OOOO00O .innerId !='0':#line:1079
                            OO000O00O0OOOO00O .invitation ()#line:1080
        except Exception as O0OO000000000OOOO :#line:1081
            print (O0OO000000000OOOO )#line:1082
    def add_clover (OO00OOO0O00O00O0O ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            O0OO000OOOO00OOO0 =f'__{timi_new()}'#line:1088
            O00OO00OO00000000 ={'source':'scsc','authorization':OO00OOO0O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOO00OOO0 ),'signstring':O0OO000OOOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O0OOO0O0O000000OO =requests .request ('get',f'{host}/assets/clovers',headers =O00OO00OO00000000 ).json ()#line:1100
            if 'status'in O0OOO0O0O000000OO :#line:1102
                if O0OOO0O0O000000OO ['status']==200 :#line:1103
                    OO0O000O000OO0O00 =O0OOO0O0O000000OO ['data']['clover']#line:1104
                    OOO0OO0O0OO0O00O0 =O0OOO0O0O000000OO ['data']['used_clover']#line:1105
                    OO0O0O0OOO0000000 =float (OO0O000O000OO0O00 )-float (OOO0OO0O0OO0O00O0 )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0OO0O0OO0O00O0}')#line:1107
                    if OO00OOO0O00O00O0O .certification ()!='未实名':#line:1108
                        if OO0O0O0OOO0000000 >1 :#line:1109
                            O0OO000OOOO00OOO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0O0OOO0000000)}_{timi_new()}'#line:1110
                            O00OO00O000OO0000 ={'source':'scsc','authorization':OO00OOO0O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOO00OOO0 ),'signstring':O0OO000OOOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            O0000O0O000OOOOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0O0OOO0000000 )}#line:1122
                            O0O000O0O00OOOO0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO00O000OO0000 ,data =O0000O0O000OOOOO0 ).json ()#line:1123
                            if 'status'in O0O000O0O00OOOO0O :#line:1125
                                if O0O000O0O00OOOO0O ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O0O000O0O00OOOO0O["data"]["isSuccess"]}丨数量:{OO0O0O0OOO0000000}')#line:1127
                                if O0O000O0O00OOOO0O ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O0O000O0O00OOOO0O["message"]}')#line:1129
            O00O0000OOOOOO0OO =requests .request ('get',f'{host}/lottery',headers =O00OO00OO00000000 ).json ()#line:1130
            OOO00000O000OO00O =OO00OOO0O00O00O0O .winning_rewards ()#line:1132
            if 'status'in O00O0000OOOOOO0OO :#line:1133
                if O00O0000OOOOOO0OO ['status']==200 :#line:1134
                    O0OOOO0OO0O0O00OO =O00O0000OOOOOO0OO ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (O0OOOO0OO0O0O00OO )#line:1136
                    O00OOO0OO00000000 =O00O0000OOOOOO0OO ['data'][1 ]['value']#line:1137
                    O000O00O00O000O0O =O00O0000OOOOOO0OO ['data'][0 ]['join_number']#line:1138
                    O00OO0OOO0000OOO0 =int (float (O00O0000OOOOOO0OO ['data'][0 ]['totalValue']))#line:1139
                    OOOO0O0OOOO0O0O00 =float (O00OOO0OO00000000 /O00OO0OOO0000OOO0 )*10000 #line:1140
                    O000O0OOOOOOO0000 =O00OO0OOO0000OOO0 /O000O00O00O000O0O #line:1141
                    print (f'【参与抽奖】:预计每天中{str(O0OOOO0OO0O0O00OO)[:6]}颗金种子丨好友收益:{str(OOO00000O000OO00O)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(OOOO0O0OOOO0O0O00)[:6]}颗金种子丨☘️人均:{str(O000O0OOOOOOO0000)[:7]}️')#line:1143
        except Exception as O0000O0O0OO00000O :#line:1144
            print (O0000O0O0OO00000O )#line:1145
    def energy (OO0000O0OO0O0O0OO ):#line:1148
        try :#line:1149
            while True :#line:1150
                OO00O00OO0O00OOOO =f'__{timi_new()}'#line:1151
                OOOOOO00O000OO00O ={'source':'scsc','authorization':OO0000O0OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0O00OOOO ),'signstring':OO00O00OO0O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                O00OO00OO0O0O000O =requests .request ('get',f'{host}/energy/general',headers =OOOOOO00O000OO00O ).json ()#line:1163
                if 'status'in O00OO00OO0O0O000O :#line:1165
                    if O00OO00OO0O0O000O ['status']==200 :#line:1166
                        OOOOO0O0000OO0OO0 =O00OO00OO0O0O000O ['data']['ordinary_water']#line:1167
                        O0OO000O0OO00000O =O00OO00OO0O0O000O ['data']['ordinary_fertilizer']#line:1168
                        OOOO0O0OOOOO0O0O0 =O00OO00OO0O0O000O ['data']['videoStatus']#line:1169
                        O0OOOO00OOOO0O0OO =O00OO00OO0O0O000O ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(O0OO000O0OO00000O).split(".")[0]}丨水滴:{str(OOOOO0O0000OO0OO0).split(".")[0]}')#line:1172
                        if float (O0OO000O0OO00000O )<96 :#line:1173
                            if OOOO0O0OOOOO0O0O0 :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                OOO00O0OO0O0OOO00 =99 -float (O0OO000O0OO00000O )#line:1176
                                OO0OO0O0000O0OO0O ={"fertilizer":str (OOO00O0OO0O0OOO00 ).split ('.')[0 ]}#line:1177
                                OO000O00O0OOOOO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOOO00O000OO00O ).json ()#line:1179
                                if 'status'in OO000O00O0OOOOO0O :#line:1181
                                    if OO000O00O0OOOOO0O ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O00O0OOOOO0O["message"]}')#line:1183
                                    if OO000O00O0OOOOO0O ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{OO000O00O0OOOOO0O["message"]}')#line:1185
                                        break #line:1186
                                if float (O0OO000O0OO00000O )<78 :#line:1188
                                    OOO00O0OO0O0OOO00 =80 -float (O0OO000O0OO00000O )#line:1189
                                    O0000O00000OO00OO =f'_fertilizer={int(OOO00O0OO0O0OOO00)}_{timi_new()}'#line:1190
                                    OOO0000OOOOOOO0O0 ={'source':'scsc','authorization':OO0000O0OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00000OO00OO ),'signstring':O0000O00000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    O0OOO00OO00O0000O ={"fertilizer":int (OOO00O0OO0O0OOO00 )}#line:1202
                                    O0000O000O0000OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0000OOOOOOO0O0 ,data =O0OOO00OO00O0000O ).json ()#line:1204
                                    if 'status'in O0000O000O0000OOO :#line:1206
                                        if O0000O000O0000OOO ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O0000O000O0000OOO["message"]}丨数量:{int(OOO00O0OO0O0OOO00)}')#line:1208
                                        if O0000O000O0000OOO ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{O0000O000O0000OOO["message"]}丨数量:{int(OOO00O0OO0O0OOO00)}')#line:1210
                                            O0OO000OOOOO00OOO =O0000O000O0000OOO ["message"].split ('-')[1 ]#line:1211
                                            OOOOOO000O000O0O0 =f'__{timi_new()}'#line:1212
                                            OO00OO0O0OO00O0OO ={'source':'scsc','authorization':OO0000O0OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000O000O0O0 ),'signstring':OOOOOO000O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            OOOOOOO00O0OOOO0O =requests .request ('get',f'{host}/user',headers =OO00OO0O0OO00O0OO ).json ()#line:1224
                                            if 'status'in OOOOOOO00O0OOOO0O :#line:1225
                                                if OOOOOOO00O0OOOO0O ['status']==200 :#line:1226
                                                    OO0O0000OOO000OO0 =OOOOOOO00O0OOOO0O ['data']['inner_id']#line:1227
                                                    if give_gold (OO0O0000OOO000OO0 ,float (O0OO000OOOOO00OOO )+1 ):#line:1228
                                                        OO0000O0OO0O0O0OO .energy ()#line:1229
                        if float (OOOOO0O0000OO0OO0 )<880 :#line:1230
                            if O0OOOO00OOOO0O0OO :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                OOO00O0O00OO00000 =999 -float (OOOOO0O0000OO0OO0 )#line:1233
                                O0OOO000O00O00O0O ={"water":str (OOO00O0O00OO00000 ).split ('.')[0 ]}#line:1234
                                OO0O0OOOO0O0OO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOOO00O000OO00O ).json ()#line:1236
                                if 'status'in OO0O0OOOO0O0OO0OO :#line:1238
                                    if OO0O0OOOO0O0OO0OO ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0OOOO0O0OO0OO["message"]}')#line:1240
                                    if OO0O0OOOO0O0OO0OO ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0OOOO0O0OO0OO["message"]}')#line:1242
                                        break #line:1243
                                if float (OOOOO0O0000OO0OO0 )<780 :#line:1244
                                    OOO00O0O00OO00000 =800 -float (OOOOO0O0000OO0OO0 )#line:1245
                                    O000O0O0OOO00000O =f'_water={int(OOO00O0O00OO00000)}_{timi_new()}'#line:1246
                                    OOOO0000OO0000O0O ={'source':'scsc','authorization':OO0000O0OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OOO00000O ),'signstring':O000O0O0OOO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    OOO00O000O000000O ={"water":int (OOO00O0O00OO00000 )}#line:1258
                                    OO0OO00O00O00OO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0000OO0000O0O ,data =OOO00O000O000000O ).json ()#line:1260
                                    if 'status'in OO0OO00O00O00OO0O :#line:1262
                                        if OO0OO00O00O00OO0O ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{OO0OO00O00O00OO0O["message"]}丨数量:{int(OOO00O0O00OO00000)}')#line:1264
                                        if OO0OO00O00O00OO0O ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{OO0OO00O00O00OO0O["message"]}丨数量:{int(OOO00O0O00OO00000)}')#line:1266
                                            O0OO000OOOOO00OOO =OO0OO00O00O00OO0O ["message"].split ('-')[1 ]#line:1267
                                            OOOOOO000O000O0O0 =f'__{timi_new()}'#line:1268
                                            OO00OO0O0OO00O0OO ={'source':'scsc','authorization':OO0000O0OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000O000O0O0 ),'signstring':OOOOOO000O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            OOOOOOO00O0OOOO0O =requests .request ('get',f'{host}/user',headers =OO00OO0O0OO00O0OO ).json ()#line:1280
                                            if 'status'in OOOOOOO00O0OOOO0O :#line:1281
                                                if OOOOOOO00O0OOOO0O ['status']==200 :#line:1282
                                                    OO0O0000OOO000OO0 =OOOOOOO00O0OOOO0O ['data']['inner_id']#line:1283
                                                    if give_gold (OO0O0000OOO000OO0 ,float (O0OO000OOOOO00OOO )+1 ):#line:1284
                                                        OO0000O0OO0O0O0OO .energy ()#line:1285
                        break #line:1286
        except Exception as O0O0O00OO0O00000O :#line:1287
            print (O0O0O00OO0O00000O )#line:1288
def bundled_def ():#line:1291
    OOOOOOOOO000OOOOO =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return OOOOOOOOO000OOOOO [random .randint (0 ,len (OOOOOOOOO000OOOOO )-1 )]#line:1293
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
        OO0OOOO0O0O0OO000 =gitee_edition ()#line:1332
        if version_of_the_validation ()<OO0OOOO0O0O0OO000 ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOOO0O0O0OO000["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{OO0OOOO0O0O0OO000["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOOO0O0O0OO000["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {OO0OOOO0O0O0OO000["CityEarth"]["content"]}')#line:1338
    except Exception as OOOOO00O0O00OOO00 :#line:1339
        print (OOOOO00O0O00OOO00 )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
