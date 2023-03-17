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
        OO00O00OO0O0O0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OO00O00OO0O0O0OOO)}个账号==========")#line:16
        for OO0OO0OO0O00OOOOO in OO00O00OO0O0O0OOO :#line:17
            OO0OO00OO000OO00O =[]#line:18
            print (f"------------正在执行第{OO00O00OO0O0O0OOO.index(OO0OO0OO0O00OOOOO) + 1}个账号------------")#line:19
            OOOOOO0O00OOO0O00 =CityEarth (OO0OO0OO0O00OOOOO ,OO0OO00OO000OO00O ,OO00O00OO0O0O0OOO .index (OO0OO0OO0O00OOOOO ))#line:20
            def O00O0OOOO0O0OOOOO ():#line:22
                if OOOOOO0O00OOO0O00 .base_info ():#line:24
                    OOOOOO0O00OOO0O00 .sealing ()#line:26
                    OOOOOO0O00OOO0O00 .invitenum ()#line:28
                    OOOOOO0O00OOO0O00 .query_to_sell ()#line:30
                    OOOOOO0O00OOO0O00 .game_map ()#line:32
                    OOOOOO0O00OOO0O00 .friends_invitation ()#line:36
                    OOOOOO0O00OOO0O00 .energy ()#line:38
                    OOOOOO0O00OOO0O00 .add_clover ()#line:40
                    OOOOOO0O00OOO0O00 .propsraffle ()#line:42
                    OOOOOO0O00OOO0O00 .synthetic ()#line:44
                    OOOOOO0O00OOO0O00 .crops_illustrated ()#line:46
                    OOOOOO0O00OOO0O00 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OOOOOO0O00OOO0O00 .give_gold ()#line:51
            OOO0OOO000O00000O =threading .Thread (target =O00O0OOOO0O0OOOOO )#line:53
            OOO0OOO000O00000O .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        OOO00OO0O000OO00O =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO00OO0O000OO00O +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O0O0O00OO0OO00O in invited_new :#line:62
            print (O0O0O0O00OO0OO00O )#line:63
        print ('开始打印未实名的token')#line:64
        for O0OOO00O00OO000OO in weishim :#line:65
            print (O0OOO00O00OO000OO )#line:66
    except Exception as OOO0OO0O000O0OO0O :#line:67
        print (OOO0OO0O000O0OO0O )#line:68
def give_gold (OOOO0O0OO0000O0O0 ,O00O0000OOO00OOO0 ):#line:72
    try :#line:73
        OOO00O0OO00O0OO00 =f'_doneeNo={OOOO0O0OO0000O0O0}&quantity={int(O00O0000OOO00OOO0)}_{timi_new()}'#line:74
        OOO0000000O0000OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO00O0OO00 ),'signstring':OOO00O0OO00O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O000OOOOO0O0O0O0O ={"quantity":int (O00O0000OOO00OOO0 ),"doneeNo":OOOO0O0OO0000O0O0 }#line:89
        OO0O00O00OOO0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000000O0000OO ,data =O000OOOOO0O0O0O0O ).json ()#line:90
        if 'status'in OO0O00O00OOO0O000 :#line:92
            if OO0O00O00OOO0O000 ['status']==200 :#line:93
                if OO0O00O00OOO0O000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00O0000OOO00OOO0)}种子给{OOOO0O0OO0000O0O0}成功')#line:95
                    return True #line:96
            if OO0O00O00OOO0O000 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0O00O00OOO0O000["message"]}')#line:98
                return False #line:99
            if OO0O00O00OOO0O000 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0O00O00OOO0O000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00O0O0O0O00O0OOO :#line:104
        print (O00O0O0O0O00O0OOO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0O0O0O00OOO0O00 ):#line:115
    O000OOOOOOOOO0OO0 =hashlib .md5 (OO0O0O0O00OOO0O00 .encode ()).hexdigest ()#line:116
    O00OO000OOOO000OO =sc1 ()#line:117
    OO0OOOOO0OOOO0000 =sc2 ()#line:118
    O00OO0O0000OOOO0O =sc3 ()#line:119
    OOOO000OO0000OOO0 =O00OO000OOOO000OO +O000OOOOOOOOO0OO0 +OO0OOOOO0OOOO0000 +O00OO0O0000OOOO0O #line:120
    O0O00OOOOOO0O00OO =hashlib .md5 (OOOO000OO0000OOO0 .encode ()).hexdigest ()#line:121
    return O0O00OOOOOO0O00OO #line:122
def format_msg ():#line:125
    OO00O0OOOO0O0000O =""#line:126
    for OO00O0O00OOO0OO0O in msg_list :#line:127
        OO00O0OOOO0O0000O +=str (OO00O0O00OOO0OO0O )+"\r\n"#line:128
    return OO00O0OOOO0O0000O #line:129
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
def get_json_data (OO0O0OO0OOOOO0000 ,OOOOO0O00OOOO00OO ,O000000O0O0O0O0OO ,OO00OOOOOO00OO0O0 ):#line:153
    with open (OO0O0OO0OOOOO0000 ,'rb')as O0O00OOO0OOO0000O :#line:154
        OO0OOO000O0O0OO0O =json .load (O0O00OOO0OOO0000O )#line:155
        OO0OOO000O0O0OO0O ['data'][OOOOO0O00OOOO00OO ][O000000O0O0O0O0OO ]=OO00OOOOOO00OO0O0 #line:156
        OOO0OOOO00OOOO00O =OO0OOO000O0O0OO0O #line:157
    O0O00OOO0OOO0000O .close ()#line:158
    return OOO0OOOO00OOOO00O #line:159
def write_json_data (O0O0O0OOO000OO0O0 ):#line:162
    with open (json_path1 ,'w')as O0O0OO0OOOOO0OOO0 :#line:163
        json .dump (O0O0O0OOO000OO0O0 ,O0O0OO0OOOOO0OOO0 )#line:164
    O0O0OO0OOOOO0OOO0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O000O0O0OOOOO0OOO ,O0O0O000O0OOO0000 ,O0000OOO0OOO0O00O ,O0O0O00OO00OOOOO0 ):#line:171
        try :#line:172
            O000O0O0OOOOO0OOO .msg =O0000OOO0OOO0O00O #line:173
            O000O0O0OOOOO0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O000O0O0OOOOO0OOO .token =O0O0O000O0OOO0000 ['authorization']#line:175
            O000O0O0OOOOO0OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O000O0O0OOOOO0OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O000O0O0OOOOO0OOO .elephant_user =O0O0O000O0OOO0000 ['elephant_user']#line:178
            O000O0O0OOOOO0OOO .elephant_pswd =O0O0O000O0OOO0000 ['elephant_pswd']#line:179
            O000O0O0OOOOO0OOO .elephant_Task_ID =O0O0O000O0OOO0000 ['elephant_Task_ID']#line:180
            O000O0O0OOOOO0OOO .len_new =O0O0O00OO00OOOOO0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOO00O0OOO0O0000O ):#line:186
        try :#line:187
            OOO00O0OOO0O0000O .watched_ad ()#line:189
            OO0OOO0OO0O000000 =f'__{timi_new()}'#line:190
            OOO00O0OO000O0OO0 ={'source':'scsc','authorization':OOO00O0OOO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO0O000000 ),'signstring':OO0OOO0OO0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0O00000OOOOOO0OO =requests .request ('get',f'{host}/user',headers =OOO00O0OO000O0OO0 ).json ()#line:202
            if 'status'in O0O00000OOOOOO0OO :#line:204
                if O0O00000OOOOOO0OO ['status']==200 :#line:205
                    O000O0O000OO00000 =O0O00000OOOOOO0OO ['data']['nickname']#line:206
                    O00OOOO00O00OO00O =O0O00000OOOOOO0OO ['data']['inner_id']#line:207
                    OOO0000O00OO0O0OO =O0O00000OOOOOO0OO ['data']['assets']['gold']#line:208
                    O0OOOOO00OOOOOO00 =O0O00000OOOOOO0OO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O000O0O000OO00000[:5]}丨ID:{O00OOOO00O00OO00O}丨等级:{O0OOOOO00OOOOOO00}丨金种子:{str(OOO0000O00OO0O0OO).split(".")[0]}')#line:211
                    if 'wx_'in O000O0O000OO00000 :#line:212
                        OOO00O0OOO0O0000O .change_nickname ()#line:213
                if O0O00000OOOOOO0OO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOO00O0OOO0O0000O .elephant_user =='f':#line:216
                        return False #line:217
                    O0O00OOO0OOOOO0OO =Invalid_login .addtask (elephant_user =OOO00O0OOO0O0000O .elephant_user ,elephant_pswd =OOO00O0OOO0O0000O .elephant_pswd ,elephant_Task_ID =OOO00O0OOO0O0000O .elephant_Task_ID )#line:220
                    O0000O0OO0OO00O00 =get_json_data (json_path ,OOO00O0OOO0O0000O .len_new ,'authorization',O0O00OOO0OOOOO0OO )#line:221
                    if write_json_data (O0000O0OO0OO00O00 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0O00000OOOOOO0OO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO0OO0O0OO0000O0 :#line:228
            print (OOO0OO0O0OO0000O0 )#line:229
    def sealing (O0000OOO0000O00O0 ):#line:232
        try :#line:233
            O00000O0O00OO0O0O =f'__{timi_new()}'#line:234
            OOO00OO0O0O00O000 ={'source':'scsc','authorization':O0000OOO0000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O00OO0O0O ),'signstring':O00000O0O00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO00OO0O0O00O000 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO00OO0O0O00O000 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO00OO0O0O00O000 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO00OO0O0O00O000 )#line:249
            requests .request ('get',f'{host}/user',headers =OOO00OO0O0O00O000 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO00OO0O0O00O000 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO00OO0O0O00O000 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO00OO0O0O00O000 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO00OO0O0O00O000 )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO00OO0O0O00O000 )#line:255
        except Exception as OO000O0000O0000O0 :#line:256
            print (OO000O0000O0000O0 )#line:257
    def ddd (O000000000O0OOO0O ):#line:259
        try :#line:260
            O00000OOO000OOOO0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0OOOOO0OO0O00000 ={'source':'scsc','authorization':O000000000O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO000OOOO0 ),'signstring':O00000OOO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0OO00OO00OO0000O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OOOOO0OO0O00000 ).json ()#line:273
            print (O0OO00OO00OO0000O )#line:274
        except Exception as OO00O0OOOOO0OOOOO :#line:279
            print (OO00O0OOOOO0OOOOO )#line:280
    def the_query (O0OOO00OO0000OO00 ):#line:290
        try :#line:291
            O0OOO00OO0O0O0000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            OOOOOOOO0O0O0OO0O ={'authorization':O0OOO00OO0000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO0O0O0000 ),'signstring':O0OOO00OO0O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            OOOO0OOOO000000O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOOOOOOO0O0O0OO0O ).json ()#line:304
            if 'status'in OOOO0OOOO000000O0 :#line:306
                if OOOO0OOOO000000O0 ['status']==200 :#line:307
                    OOO0OO0O00O0OOO0O =OOOO0OOOO000000O0 ['data']['rows'][6 ]['price']#line:308
                    O0OOO00OO0000OO00 .market_sale (OOO0OO0O00O0OOO0O )#line:309
        except Exception as OOOOO0OOOOOOOOO0O :#line:310
            print (OOOOO0OOOOOOOOO0O )#line:311
    def market_sale (OO00OOO0O00O000OO ,OO00000OO000OOO0O ):#line:314
        try :#line:315
            OOO0OO00O000O0OOO =timi_new ()#line:316
            OOOO0O0O0O0OO0O00 =f'type=crop__{OOO0OO00O000O0OOO}'#line:317
            OOO000000O0000000 ={'source':'scsc','authorization':OO00OOO0O00O000OO .token ,'timestamp':str (OOO0OO00O000O0OOO ),'sign':sign (OOOO0O0O0O0OO0O00 ),'signstring':OOOO0O0O0O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O0000000OOOOO0OO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOO000000O0000000 ).json ()#line:330
            if 'status'in O0000000OOOOO0OO0 :#line:332
                if O0000000OOOOO0OO0 ['status']==200 :#line:333
                    if O0000000OOOOO0OO0 ['data']['rows']:#line:334
                        OO000000OOO0OOOOO =O0000000OOOOO0OO0 ['data']['rows'][0 ]['packsackItemId']#line:335
                        OOO0OOOOO0OO0OO0O =O0000000OOOOO0OO0 ['data']['rows'][0 ]['quantity']#line:336
                        OO0OO00OOOO0O0000 =float (OO00000OO000OOO0O )-0.001 #line:337
                        if OO0OO00OOOO0O0000 >8 :#line:338
                            O00OOO0O0O0O00000 =f'_packsackItemId={OO000000OOO0OOOOO}&price={str(OO0OO00OOOO0O0000)[:6]}&quantity={OOO0OOOOO0OO0OO0O}_{OOO0OO00O000O0OOO}'#line:339
                            OO00O0O0OOOO0OO0O ={'source':'scsc','authorization':OO00OOO0O00O000OO .token ,'timestamp':str (OOO0OO00O000O0OOO ),'sign':sign (O00OOO0O0O0O00000 ),'signstring':O00OOO0O0O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O0OOOO0OOO0OOOOOO ={"packsackItemId":OO000000OOO0OOOOO ,"price":str (OO0OO00OOOO0O0000 )[:6 ],"quantity":str (OOO0OOOOO0OO0OO0O )}#line:355
                            OO0O000OO00O00000 =requests .request ('post',f'{host}/market/sale',headers =OO00O0O0OOOO0OO0O ,data =O0OOOO0OOO0OOOOOO ).json ()#line:356
                            if 'status'in OO0O000OO00O00000 :#line:358
                                if OO0O000OO00O00000 ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{OOO0OOOOO0OO0OO0O}丨价格:{str(OO0OO00OOOO0O0000)[:6]}')#line:360
        except Exception as O00O00OO00OOOO000 :#line:361
            print (O00O00OO00OOOO000 )#line:362
    def query_to_sell (OO0OOOOO0OO000OO0 ):#line:365
        try :#line:366
            OO0OO00O0O00OO00O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            O0OO00000OOOOO0OO ={'source':'scsc','authorization':OO0OOOOO0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O0O00OO00O ),'signstring':OO0OO00O0O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            O00O00000000O0000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00000OOOOO0OO ).json ()#line:380
            if 'status'in O00O00000000O0000 :#line:382
                if O00O00000000O0000 ['status']==200 :#line:383
                    for OOOOOO0O0O0OOOOO0 in O00O00000000O0000 ['data']['rows']:#line:384
                        OO00000OOO00OO00O =OOOOOO0O0O0OOOOO0 ['materialKey']#line:385
                        O0OOOO00OO00000OO =OOOOOO0O0O0OOOOO0 ['quantity']#line:386
                        OO00OOO00OO0OO0OO =OOOOOO0O0O0OOOOO0 ['price']#line:387
                        OO00O000O0O00OO0O =OOOOOO0O0O0OOOOO0 ['saleState']#line:388
                        if OO00O000O0O00OO0O ==0 :#line:389
                            print (f'【出售订单】:名称:{OO00000OOO00OO00O}丨数量:{O0OOOO00OO00000OO}丨价格:{OO00OOO00OO0OO0OO}')#line:390
                            O000OO00OO0OOO000 =OOOOOO0O0O0OOOOO0 ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                OO0OOOOO0OO000OO0 .cacel_sale (O000OO00OO0OOO000 )#line:393
        except Exception as O0O00OOO0O00OOO0O :#line:394
            print (O0O00OOO0O00OOO0O )#line:395
    def cacel_sale (O00O0O0OO0O0OOO00 ,O0OO0OOOOOOO0OOOO ):#line:398
        try :#line:399
            OO0OOOOOO0OO0OOO0 =f'_saleId={O0OO0OOOOOOO0OOOO}_{timi_new()}'#line:400
            OO0OO000OO000O000 ={'source':'scsc','authorization':O00O0O0OO0O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO0OO0OOO0 ),'signstring':OO0OOOOOO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O00O00O00O00O0OOO ={"saleId":O0OO0OOOOOOO0OOOO }#line:414
            OOOOO0O0O0OOO00OO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO000OO000O000 ,data =O00O00O00O00O0OOO ).json ()#line:415
            if 'status'in OOOOO0O0O0OOO00OO :#line:417
                if OOOOO0O0O0OOO00OO ['status']==200 :#line:418
                    print (f'【下架出售】:{OOOOO0O0O0OOO00OO["data"]}')#line:419
        except Exception as OOOOOOO00O00OOOOO :#line:420
            print (OOOOOOO00O00OOOOO )#line:421
    def change_nickname (O000OO0OOOOO000OO ):#line:424
        try :#line:425
            O0000OOOOO0OO00OO =timi_new ()#line:426
            OO0000O0000O0OO0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            O000OOOOOO0O00OO0 =requests .request ('post','https://www.qmsjmfb.com/',data =OO0000O0000O0OO0O ).text #line:428
            OOO00O0O0OOO0O0O0 =re .findall ('<ul><li>(.*?)</li>',O000OOOOOO0O00OO0 )[0 ][:3 ]#line:429
            OOOO0O000OOO00O0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO00O0O0OOO0O0O0}').json ()#line:430
            OO0O0OO000O00O00O =OOOO0O000OOO00O0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            O00OO0O0000OO000O ={"nickname":OO0O0OO000O00O00O }#line:432
            OO000O00OOO000O0O =f'_nickname={OO0O0OO000O00O00O}_{O0000OOOOO0OO00OO}'#line:433
            O0OOOO000O000OO0O ={'source':'scsc','authorization':O000OO0OOOOO000OO .token ,'timestamp':O0000OOOOO0OO00OO ,'sign':sign (OO000O00OOO000O0O ),'signstring':OO000O00OOO000O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            OO00OO000OOO000OO =requests .request ('patch',f'{host}/user/nickname',headers =O0OOOO000O000OO0O ,data =O00OO0O0000OO000O ).json ()#line:445
            if 'status'in OO00OO000OOO000OO :#line:447
                if OO00OO000OOO000OO ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{OO0O0OO000O00O00O}丨{OO00OO000OOO000OO["message"]}')#line:449
        except Exception as O0OO0O00O00000OOO :#line:450
            print (O0OO0O00O00000OOO )#line:451
    def withdraw (O0000O0000000O0OO ):#line:454
        try :#line:455
            OO00OOO0O00O0OOO0 =f'__{timi_new()}'#line:456
            O0O0OO0OO00O0OOO0 ={'source':'scsc','authorization':O0000O0000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0O00O0OOO0 ),'signstring':OO00OOO0O00O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O00O000000O0OO00O =requests .request ('get',f'{host}/assets',headers =O0O0OO0OO00O0OOO0 ).json ()#line:468
            if 'status'in O00O000000O0OO00O :#line:470
                if O00O000000O0OO00O ['status']==200 :#line:471
                    OOOO0O0O000000O0O =O00O000000O0OO00O ['data']['cash']#line:472
                    if float (OOOO0O0O000000O0O )>20 :#line:473
                        OO00OOO0O00O0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O0O0OO0OO00O0OOO0 ={'authorization':O0000O0000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0O00O0OOO0 ),'signstring':OO00OOO0O00O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OOO0000OOOOOO00O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OO0OO00000O000OO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO0OO00O0OOO0 ,data =OOO0000OOOOOO00O0 ).json ()#line:487
                        if 'status'in OO0OO00000O000OO0 :#line:489
                            if OO0OO00000O000OO0 ['status']==200 :#line:490
                                print (f'【余额提现】:{OO0OO00000O000OO0["data"]}')#line:491
                        if 'status'in OO0OO00000O000OO0 :#line:492
                            if OO0OO00000O000OO0 ['status']==500 :#line:493
                                print (f'【余额提现】:{OO0OO00000O000OO0["message"]}')#line:494
        except Exception as O0O0OO00O0O00OOOO :#line:495
            print (O0O0OO00O0O00OOOO )#line:496
    def invitenum (OOOO0O0O000000O00 ):#line:499
        global invited_new #line:500
        try :#line:501
            O00OO00O000OOOO00 =f'__{timi_new()}'#line:502
            O0OOO0000O00O000O ={'source':'scsc','authorization':OOOO0O0O000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O000OOOO00 ),'signstring':O00OO00O000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O0O0OO0O00000OOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOO0000O00O000O ).json ()#line:514
            if 'status'in O0O0OO0O00000OOOO :#line:516
                if O0O0OO0O00000OOOO ['status']==200 :#line:517
                    OO000O0O00OOOOO00 =O0O0OO0O00000OOOO ['data']['invited_count']#line:518
                    OO000O0OO000O00OO =O0O0OO0O00000OOOO ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OO000O0O00OOOOO00}丨间邀好友:{OO000O0OO000O00OO}')#line:520
                    if OO000O0O00OOOOO00 <2 :#line:521
                        OOOO00OOO0OOO0O0O =f'__{timi_new()}'#line:522
                        O0OO000O00OOOO000 ={'source':'scsc','authorization':OOOO0O0O000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO0OOO0O0O ),'signstring':OOOO00OOO0OOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OOO0O00O0O000O0OO =requests .request ('get',f'{host}/user',headers =O0OO000O00OOOO000 ).json ()#line:534
                        if 'status'in OOO0O00O0O000O0OO :#line:536
                            if OOO0O00O0O000O0OO ['status']==200 :#line:537
                                invited_new .append (OOO0O00O0O000O0OO ['data']['inner_id'])#line:538
        except Exception as O0OO00000000O0OO0 :#line:539
            print (O0OO00000000O0OO0 )#line:540
    def game_map (OO00O00OOO0OO0000 ):#line:543
        try :#line:544
            O00OO000000O0000O =f'__{timi_new()}'#line:545
            O00O00O000OO0O0O0 ={'source':'scsc','authorization':OO00O00OOO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000000O0000O ),'signstring':O00OO000000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O0OO0O0O0OO00OOOO =requests .request ('get',f'{host}/game/map',headers =O00O00O000OO0O0O0 ).json ()#line:557
            if 'status'in O0OO0O0O0OO00OOOO :#line:559
                if O0OO0O0O0OO00OOOO ['status']==200 :#line:560
                    for OO0OOO0OO000OO00O in O0OO0O0O0OO00OOOO ['data']['list'][0 ]['crops']:#line:561
                        O0O0O0O0OOOOO0O00 =OO0OOO0OO000OO00O ['level']#line:563
                        if O0O0O0O0OOOOO0O00 ==41 :#line:564
                            OO000O0O000OOOO0O =OO0OOO0OO000OO00O ['crop_name']#line:565
                            O0O00O0OOO0O000O0 =OO0OOO0OO000OO00O ['count']#line:566
                            if O0O00O0OOO0O000O0 >0 :#line:567
                                print (f'【农业资产】:{OO000O0O000OOOO0O}丨数量:{O0O00O0OOO0O000O0}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    OO00O00OOO0OO0000 .the_query ()#line:570
        except Exception as O00000000000O0OO0 :#line:571
            print (O00000000000O0OO0 )#line:572
    def give_gold (O0O00OO0O0000O00O ):#line:575
        try :#line:576
            O000OOOO00OOOO00O =f'__{timi_new()}'#line:577
            OOOOOO00OO00000O0 ={'source':'scsc','authorization':O0O00OO0O0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00OOOO00O ),'signstring':O000OOOO00OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            OO00OO00OOOOOOO00 =requests .request ('get',f'{host}/user',headers =OOOOOO00OO00000O0 ).json ()#line:589
            if 'status'in OO00OO00OOOOOOO00 :#line:590
                if OO00OO00OOOOOOO00 ['status']==200 :#line:591
                    if float (O0O00OO0O0000O00O .doneeNo )!=0 :#line:592
                        O0OOOO000O000O0OO =OO00OO00OOOOOOO00 ['data']['assets']['gold']#line:593
                        if float (O0OOOO000O000O0OO )>float (O0O00OO0O0000O00O .innerId ):#line:594
                            OO0OO0O00OO0OO0OO =int (float (O0OOOO000O000O0OO )/1.1 )#line:595
                            O000OOOO00OOOO00O =f'_doneeNo={O0O00OO0O0000O00O.doneeNo}&quantity={OO0OO0O00OO0OO0OO}_{timi_new()}'#line:596
                            OOOOOO00OO00000O0 ={'source':'scsc','authorization':O0O00OO0O0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00OOOO00O ),'signstring':O000OOOO00OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            OOOOOOO00O00OOO00 ={"quantity":OO0OO0O00OO0OO0OO ,"doneeNo":O0O00OO0O0000O00O .doneeNo }#line:611
                            OO0OO000000OO0OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOO00OO00000O0 ,data =OOOOOOO00O00OOO00 ).json ()#line:612
                            if 'status'in OO0OO000000OO0OO0 :#line:614
                                if OO0OO000000OO0OO0 ['status']==200 :#line:615
                                    if OO0OO000000OO0OO0 ['data']:#line:616
                                        print (f'【赠送种子】:赠送{OO0OO0O00OO0OO0OO}种子给{O0O00OO0O0000O00O.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as OO0000000O00OOO0O :#line:620
            print (OO0000000O00OOO0O )#line:621
    def invitation (O000O000O0OOOO000 ):#line:623
        try :#line:624
            _O0O000000O0000OO0 =float (bundled_def ())/4 #line:625
            O0OOOO00O00000O00 =f'_innerId={int(_O0O000000O0000OO0)}_{timi_new()}'#line:626
            OOO0O0O0OO00OOO0O ={'source':'scsc','authorization':O000O000O0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00O00000O00 ),'signstring':O0OOOO00O00000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            O00OOOOO000O0000O ={"innerId":int (_O0O000000O0000OO0 )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O0O0OO00OOO0O ,data =O00OOOOO000O0000O )#line:639
        except Exception as O0O00OO0O0OOO000O :#line:640
            print (O0O00OO0O0OOO000O )#line:641
    def winning_rewards (O000OOOOOO0O0OO00 ):#line:644
        try :#line:645
            O0O0O0OO0OOOO0OO0 =f'__{timi_new()}'#line:646
            O000000O00OOO00O0 ={'source':'scsc','authorization':O000OOOOOO0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0OOOO0OO0 ),'signstring':O0O0O0OO0OOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            OO0000O0O0O0OO0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000000O00OOO00O0 ).json ()#line:658
            if 'status'in OO0000O0O0O0OO0O0 :#line:660
                if OO0000O0O0O0OO0O0 ['status']==200 :#line:661
                    if OO0000O0O0O0OO0O0 ['data']['amount']:#line:662
                        O00OOOOOO0OOO0OO0 =OO0000O0O0O0OO0O0 ['data']['amount']['gold']#line:663
                        return O00OOOOOO0OOO0OO0 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as OOOOOO0O0OO00O0OO :#line:667
            print (OOOOOO0O0OO00O0OO )#line:668
    def certification (OO0O000OOOO00O0OO ):#line:671
        try :#line:672
            O0000000O0000000O =f'__{timi_new()}'#line:673
            O0O00O0000O00000O ={'source':'scsc','authorization':OO0O000OOOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000O0000000O ),'signstring':O0000000O0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            O000O0OO00OOO0OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O00O0000O00000O ).json ()#line:685
            if 'status'in O000O0OO00OOO0OOO :#line:687
                if O000O0OO00OOO0OOO ['status']==200 :#line:688
                    if O000O0OO00OOO0OOO ['data']['result']:#line:689
                        O0O0O0OO00O000O0O =O000O0OO00OOO0OOO ['data']['nick_name']#line:690
                        return O0O0O0OO00O000O0O #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as O00OOOOOO00O0O0OO :#line:694
            print (O00OOOOOO00O0O0OO )#line:695
    def crops_illustrated (OOOO00OO0OOO00OOO ):#line:698
        try :#line:699
            O0O0O0OOOO0O00O0O =f'__{timi_new()}'#line:700
            O00O00O0000OO0OO0 ={'source':'scsc','authorization':OOOO00OO0OOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO0O00O0O ),'signstring':O0O0O0OOOO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            O0000000O0O0O000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O00O0000OO0OO0 ).json ()#line:712
            if 'status'in O0000000O0O0O000O :#line:714
                if O0000000O0O0O000O ['status']==200 :#line:715
                    OO000000000000OOO =O0000000O0O0O000O ['data'][0 ]['crops']#line:716
                    for OO0OOO0O00O000O0O in OO000000000000OOO :#line:717
                        if OO0OOO0O00O000O0O ['ill_clover_award']:#line:718
                            if float (OO0OOO0O00O000O0O ['ill_clover_award'])>1 :#line:719
                                if OO0OOO0O00O000O0O ['is_finish']:#line:720
                                    if not OO0OOO0O00O000O0O ['is_getit']:#line:721
                                        if OOOO00OO0OOO00OOO .certification ()!='未实名':#line:722
                                            O0O0O0OOOO0O00O0O =f'_award_level={OO0OOO0O00O000O0O["level"]}_{timi_new()}'#line:723
                                            O00O00O0000OO0OO0 ={'source':'scsc','authorization':OOOO00OO0OOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO0O00O0O ),'signstring':O0O0O0OOOO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            OOOO0O0OO0OOO0O00 ={"award_level":OO0OOO0O00O000O0O ['level']}#line:735
                                            OO0O00OO0O0O0OOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O00O0000OO0OO0 ,json =OOOO0O0OO0OOO0O00 ).json ()#line:737
                                            if 'status'in OO0O00OO0O0O0OOOO :#line:738
                                                if OO0O00OO0O0O0OOOO ['status']==200 :#line:739
                                                    OO0000000OOO0OOOO =OO0O00OO0O0O0OOOO ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{OO0OOO0O00O000O0O["crop_name"]}成就丨奖励{OO0000000OOO0OOOO}☘️')#line:742
                                                if OO0O00OO0O0O0OOOO ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{OO0O00OO0O0O0OOOO["message"]}')#line:744
        except Exception as OO0OOO0O000000O0O :#line:745
            print (OO0OOO0O000000O0O )#line:746
    def watched_ad (OOO00O0O000OO0OO0 ):#line:749
        try :#line:750
            OO0OO0OO000O0OO00 =f'__{timi_new()}'#line:751
            OOOO000O00000O0O0 ={'source':'scsc','authorization':OOO00O0O000OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO000O0OO00 ),'signstring':OO0OO0OO000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            OOOOOO0OO00000000 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O00000O0O0 ).json ()#line:763
            if 'status'in OOOOOO0OO00000000 :#line:765
                if OOOOOO0OO00000000 ['status']==200 :#line:766
                    if 'offlineInfo'in OOOOOO0OO00000000 ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        O0OO0O00OOO0000O0 =OOOOOO0OO00000000 ['data']['offlineInfo']['off_minute']#line:769
                        OO0O0000OOO0OO00O =float (OOOOOO0OO00000000 ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOO000O00000O0O0 ).json ()#line:772
                        time .sleep (2 )#line:773
                        O0O000O0OOOOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O00000O0O0 ).json ()#line:774
                        if 'status'in O0O000O0OOOOO0O0O :#line:776
                            if O0O000O0OOOOO0O0O ['status']==200 :#line:777
                                O000OOO0O0000OOOO =float (O0O000O0OOOOO0O0O ['data']['silver'])/1000000000000 #line:778
                                OOO00O0OOOOOO000O =str (O000OOO0O0000OOOO -OO0O0000OOO0OO00O )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{O0OO0O00OOO0000O0}分钟奖励🌱数量:{OOO00O0OOOOOO000O}t粒')#line:780
        except Exception as OOO0OO0OOO0O00000 :#line:781
            print (OOO0OO0OOO0O00000 )#line:782
    def user_ad (O0O00O0OO0000O00O ):#line:785
        try :#line:786
            OO000OOOO000000O0 =f'__{timi_new()}'#line:787
            O00OOO0O000OO0000 ={'source':'scsc','authorization':O0O00O0OO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO000000O0 ),'signstring':OO000OOOO000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            OOOOO0O00O00OO0OO =requests .request ('get',f'{host}/user/ad',headers =O00OOO0O000OO0000 ).json ()#line:799
            if 'status'in OOOOO0O00O00OO0OO :#line:801
                if OOOOO0O00O00OO0OO ['status']==200 :#line:802
                    OOO0O0000OOO000O0 =OOOOO0O00O00OO0OO ['data']['max_time']#line:803
                    O0000O00OO0OO0000 =OOOOO0O00O00OO0OO ['data']['watch_time']#line:804
                    OOO0OO0OOO00OOOOO =OOOOO0O00O00OO0OO ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{OOO0OO0OOO00OOOOO + OOO0O0000OOO000O0 - O0000O00OO0OO0000}次丨好友提供:{OOO0OO0OOO00OOOOO}次')#line:806
                    if OOO0OO0OOO00OOOOO +OOO0O0000OOO000O0 -O0000O00OO0OO0000 >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        OOOO0OOO000000O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOO0O000OO0000 ).json ()#line:809
                        if 'status'in OOOO0OOO000000O00 :#line:811
                            if OOOO0OOO000000O00 ['status']==200 :#line:812
                                OOOO0O0O0OOO0O0O0 =float (OOOO0OOO000000O00 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(OOOO0O0O0OOO0O0O0)}t粒')#line:814
                                return True #line:815
                            if OOOO0OOO000000O00 ['status']==500 :#line:816
                                O0O0O0OOO00O00O0O =OOOO0OOO000000O00 ['message']#line:817
                                print (f'【获取种子】:{O0O0O0OOO00O00O0O}')#line:818
                                return False #line:819
        except Exception as OOOOO0OOO00O0OO00 :#line:820
            print (OOOOO0OOO00O0OO00 )#line:821
    def synthetic (OO0OOO0O0000OO0OO ):#line:824
        global id ,g #line:825
        try :#line:826
            O0O0O00O00OOOO0OO =OO0OOO0O0000OO0OO .level_new ()#line:827
            OOO00OOO00OO000O0 =random .randint (9 ,11 )#line:828
            OOOO000000O000OOO =f'_site=8&targetSite={OOO00OOO00OO000O0}_{timi_new()}'#line:829
            O0000OO00OO0OOO0O ={'source':'scsc','authorization':OO0OOO0O0000OO0OO .token ,'timestamp':timi_new (),'sign':sign (OOOO000000O000OOO ),'signstring':OOOO000000O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            O000OOOO0O00OOOO0 ={"site":int (8 ),"targetSite":int (OOO00OOO00OO000O0 )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O0000OO00OO0OOO0O ,json =O000OOOO0O00OOOO0 )#line:842
            while True :#line:843
                O0OOO0OO00000OOO0 =f'__{timi_new()}'#line:844
                O0O0OO0O00O0OO0O0 ={'source':'scsc','authorization':OO0OOO0O0000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00000OOO0 ),'signstring':O0OOO0OO00000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                O000O0O0OOO0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0O00O0OO0O0 ).json ()#line:856
                if 'status'in O000O0O0OOO0O0OOO :#line:858
                    if O000O0O0OOO0O0OOO ['status']==200 :#line:859
                        O0OOOO0000OOOO0O0 =O000O0O0OOO0O0OOO ['data']['cropList']#line:860
                        OOO000O0OOOOO00OO =O000O0O0OOO0O0OOO ['data']['gameCoreDataDBid']#line:861
                        O00O000OO0O0O00OO =float (O000O0O0OOO0O0OOO ['data']['silver'])/1000000000000 #line:862
                        OOOOOO0OO0O0O0OOO =0 #line:867
                        for OO0OO0OOO000O000O in O0OOOO0000OOOO0O0 :#line:868
                            if not OO0OO0OOO000O000O :#line:869
                                OO000OOOO000OO00O =f'_crop_id={OOO000O0OOOOO00OO}&site={OOOOOO0OO0O0O0OOO}_{OO0OOO0O0000OO0OO.time}'#line:870
                                O00O0OOOOOOOO0000 ={'source':'scsc','authorization':OO0OOO0O0000OO0OO .token ,'timestamp':OO0OOO0O0000OO0OO .time ,'sign':sign (OO000OOOO000OO00O ),'signstring':OO000OOOO000OO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                O0O00OO0O000OOO0O ={"site":OOOOOO0OO0O0O0OOO ,"crop_id":OOO000O0OOOOO00OO }#line:881
                                O0OOO0O00OOOOOOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =O00O0OOOOOOOO0000 ,data =O0O00OO0O000OOO0O ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in O0OOO0O00OOOOOOO0 :#line:885
                                    if O0OOO0O00OOOOOOO0 ['status']==200 :#line:886
                                        if O0OOO0O00OOOOOOO0 ['message']=='种子数量不足':#line:887
                                            O0O0O00O00OOOO0OO =OO0OOO0O0000OO0OO .level_new ()#line:888
                                            print (f'【种植合成】:{O0OOO0O00OOOOOOO0["message"]}')#line:889
                                            if not OO0OOO0O0000OO0OO .user_ad ():#line:890
                                                return False #line:891
                                    if O0OOO0O00OOOOOOO0 ['status']==500 :#line:892
                                        print (f'【种植合成】:{O0OOO0O00OOOOOOO0["message"]}')#line:893
                                        return False #line:894
                            OOOOOO0OO0O0O0OOO +=1 #line:895
                        O00OO00OOOO0O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0O00O0OO0O0 ).json ()#line:896
                        O0O000O0OOO0OO00O =O00OO00OOOO0O0OO0 ['data']['cropList']#line:897
                        O000O00OOO0OOOOOO =False #line:898
                        for OO0OO0OOO000O000O in range (12 ):#line:899
                            id =O0O000O0OOO0OO00O [OO0OO0OOO000O000O ]['level']#line:900
                            if float (O0O0O00O00OOOO0OO )-float (id )>9 :#line:901
                                O0OO0O00O0O000000 =f'_site={OO0OO0OOO000O000O}_{timi_new()}'#line:902
                                OOO0O00OOO0OO0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO0O0000OO0OO .token ,'timestamp':timi_new (),'sign':sign (O0OO0O00O0O000000 ),'signstring':O0OO0O00O0O000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                OOO00OOO0O000O00O ={"site":OO0OO0OOO000O000O }#line:914
                                O0000OOO00OO00OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O00OOO0OO0000 ,data =OOO00OOO0O000O00O ).json ()#line:916
                                if 'status'in O0000OOO00OO00OOO :#line:917
                                    if O0000OOO00OO00OOO ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O0O00OO000000O0O0 in range (11 ):#line:921
                                    O00O00O0OOO0O0000 =O0O00OO000000O0O0 +1 #line:922
                                    g =O0O000O0OOO0OO00O [O00O00O0OOO0O0000 ]['level']#line:923
                                    if id ==g :#line:924
                                        O00OO0000OOOOO0OO =O0O00OO000000O0O0 +2 #line:925
                                        if O00OO0000OOOOO0OO !=OO0OO0OOO000O000O +1 :#line:926
                                            OO0OO00OOOO0OOOO0 =OO0OO0OOO000O000O +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            OOOO000000O000OOO =f'_site={OO0OO00OOOO0OOOO0 - 1}&targetSite={O00OO0000OOOOO0OO - 1}_{timi_new()}'#line:930
                                            O0000OO00OO0OOO0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO0O0000OO0OO .token ,'timestamp':timi_new (),'sign':sign (OOOO000000O000OOO ),'signstring':OOOO000000O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O000O0000000O0O0O ={"site":int (OO0OO00OOOO0OOOO0 -1 ),"targetSite":int (O00OO0000OOOOO0OO -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0000OO00OO0OOO0O ,json =O000O0000000O0O0O )#line:949
                                            O000O00OOO0OOOOOO =True #line:951
                                    if O000O00OOO0OOOOOO :#line:952
                                        break #line:953
                                if O000O00OOO0OOOOOO :#line:954
                                    break #line:955
        except :#line:956
            OO0OOO0O0000OO0OO .synthetic ()#line:957
    def level_new (O0O00O00O0OOOOOO0 ):#line:960
        try :#line:961
            O0O0O00OOOO0OO0O0 =f'__{timi_new()}'#line:962
            OOOOOO0O0OOO0000O ={'source':'scsc','authorization':O0O00O00O0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO0OO0O0 ),'signstring':O0O0O00OOOO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OO00OO00O00OOOOOO =requests .request ('get',f'{host}/user',headers =OOOOOO0O0OOO0000O ).json ()#line:974
            if 'status'in OO00OO00O00OOOOOO :#line:975
                if OO00OO00O00OOOOOO ['status']==200 :#line:976
                    return float (OO00OO00O00OOOOOO ['data']['level'])#line:977
        except Exception as O0OOOO000O0O0O00O :#line:978
            print (O0OOOO000O0O0O00O )#line:979
    def propsraffle (O0OO000O0OO0OO00O ):#line:982
        try :#line:983
            while True :#line:984
                OO0O0O000OOO0O0OO =f'__{timi_new()}'#line:985
                O0O0OOOO0000OOO00 ={'source':'scsc','authorization':O0OO000O0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000OOO0O0OO ),'signstring':OO0O0O000OOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                O0O000O00O0O00O00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0OOOO0000OOO00 ).json ()#line:997
                if 'status'in O0O000O00O0O00O00 :#line:999
                    if O0O000O00O0O00O00 ['status']==200 :#line:1000
                        O00O00O00OO0OO0O0 =O0O000O00O0O00O00 ['data']['rows']#line:1001
                        OO0OOOOOOOOOO0O00 =O0O000O00O0O00O00 ['data']['vstate']#line:1002
                        if O00O00O00OO0OO0O0 ==5 or O00O00O00OO0OO0O0 ==6 or O00O00O00OO0OO0O0 ==7 :#line:1003
                            O00OO00OOOOO0OOO0 =O0O000O00O0O00O00 ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{O00OO00OOOOO0OOO0}')#line:1005
                        if O00O00O00OO0OO0O0 ==1 or O00O00O00OO0OO0O0 ==2 or O00O00O00OO0OO0O0 ==3 :#line:1006
                            O0OOO00O00000O0OO =O0O000O00O0O00O00 ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO00O00000O0OO}')#line:1008
                        if O00O00O00OO0OO0O0 ==4 or O00O00O00OO0OO0O0 ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if O00O00O00OO0OO0O0 =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as OO00O00O00O0OOOOO :#line:1050
            print (OO00O00O00O0OOOOO )#line:1051
    def friends_invitation (OOOO00OOOOOOOOO0O ):#line:1054
        try :#line:1055
            O0O000O000000O00O =f'__{timi_new()}'#line:1056
            O0O0O00OOO0OO0O0O ={'source':'scsc','authorization':OOOO00OOOOOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O000000O00O ),'signstring':O0O000O000000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            OOO0000OOO00O000O =requests .request ('get',f'{host}/friends',headers =O0O0O00OOO0OO0O0O ).json ()#line:1068
            if 'status'in OOO0000OOO00O000O :#line:1069
                if OOO0000OOO00O000O ['status']==200 :#line:1070
                    O0O0OO00OOO0OO000 =OOO0000OOO00O000O ['data']['myInviteter']#line:1071
                    if O0O0OO00OOO0OO000 :#line:1072
                        OOO00OOOOO0O0OOOO =O0O0OO00OOO0OO000 ['user']['nickname']#line:1073
                        O0OOOO000O00OO0OO =OOOO00OOOOOOOOO0O .certification ()#line:1074
                        if O0OOOO000O00OO0OO =='未实名':#line:1075
                            weishim .append (OOOO00OOOOOOOOO0O .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{OOO00OOOOO0O0OOOO}丨实名:{O0OOOO000O00OO0OO}')#line:1077
                    else :#line:1078
                        if OOOO00OOOOOOOOO0O .innerId !='0':#line:1079
                            OOOO00OOOOOOOOO0O .invitation ()#line:1080
        except Exception as OO00000OOOOOOOOOO :#line:1081
            print (OO00000OOOOOOOOOO )#line:1082
    def add_clover (OO00O0O000000OOO0 ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            O00OOO0OOOOOO0OO0 =f'__{timi_new()}'#line:1088
            O0O00OO0O0OO0O0OO ={'source':'scsc','authorization':OO00O0O000000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOOO0OO0 ),'signstring':O00OOO0OOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O0O0OOOO00O0OO000 =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OO0O0OO0O0OO ).json ()#line:1100
            if 'status'in O0O0OOOO00O0OO000 :#line:1102
                if O0O0OOOO00O0OO000 ['status']==200 :#line:1103
                    O0000OO0OOO00O00O =O0O0OOOO00O0OO000 ['data']['clover']#line:1104
                    O00000O0000OO0OO0 =O0O0OOOO00O0OO000 ['data']['used_clover']#line:1105
                    O0O0O0O0OOO0OOO00 =float (O0000OO0OOO00O00O )-float (O00000O0000OO0OO0 )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00000O0000OO0OO0}')#line:1107
                    if OO00O0O000000OOO0 .certification ()!='未实名':#line:1108
                        if O0O0O0O0OOO0OOO00 >1 :#line:1109
                            O00OOO0OOOOOO0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0O0O0OOO0OOO00)}_{timi_new()}'#line:1110
                            OO000OO0OOOO0O00O ={'source':'scsc','authorization':OO00O0O000000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOOO0OO0 ),'signstring':O00OOO0OOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            O0OOO00OO0OO000OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0O0O0OOO0OOO00 )}#line:1122
                            O0O00000O0000OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO000OO0OOOO0O00O ,data =O0OOO00OO0OO000OO ).json ()#line:1123
                            if 'status'in O0O00000O0000OOOO :#line:1125
                                if O0O00000O0000OOOO ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O0O00000O0000OOOO["data"]["isSuccess"]}丨数量:{O0O0O0O0OOO0OOO00}')#line:1127
                                if O0O00000O0000OOOO ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O0O00000O0000OOOO["message"]}')#line:1129
            O0O0O0O0OO0OOO00O =requests .request ('get',f'{host}/lottery',headers =O0O00OO0O0OO0O0OO ).json ()#line:1130
            O00000OO00OO0OOO0 =OO00O0O000000OOO0 .winning_rewards ()#line:1132
            if 'status'in O0O0O0O0OO0OOO00O :#line:1133
                if O0O0O0O0OO0OOO00O ['status']==200 :#line:1134
                    O0000O0OOO00O0OOO =O0O0O0O0OO0OOO00O ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (O0000O0OOO00O0OOO )#line:1136
                    O0000000O00OO00O0 =O0O0O0O0OO0OOO00O ['data'][1 ]['value']#line:1137
                    O00O0O0O000O00000 =O0O0O0O0OO0OOO00O ['data'][0 ]['join_number']#line:1138
                    O0O00O0OO0O00O000 =int (float (O0O0O0O0OO0OOO00O ['data'][0 ]['totalValue']))#line:1139
                    O0OO0O00OOOOO0O00 =float (O0000000O00OO00O0 /O0O00O0OO0O00O000 )*10000 #line:1140
                    OO000OOO0O0OOOOOO =O0O00O0OO0O00O000 /O00O0O0O000O00000 #line:1141
                    print (f'【参与抽奖】:预计每天中{str(O0000O0OOO00O0OOO)[:6]}颗金种子丨好友收益:{str(O00000OO00OO0OOO0)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO0O00OOOOO0O00)[:6]}颗金种子丨☘️人均:{str(OO000OOO0O0OOOOOO)[:7]}️')#line:1143
        except Exception as OOO0O000OOOO00000 :#line:1144
            print (OOO0O000OOOO00000 )#line:1145
    def energy (O0O00OOO00O00OOOO ):#line:1148
        try :#line:1149
            while True :#line:1150
                O00O00OOOO0O00OOO =f'__{timi_new()}'#line:1151
                O00O00000OO00O000 ={'source':'scsc','authorization':O0O00OOO00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOO0O00OOO ),'signstring':O00O00OOOO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                OO00O00OOO00O0O0O =requests .request ('get',f'{host}/energy/general',headers =O00O00000OO00O000 ).json ()#line:1163
                if 'status'in OO00O00OOO00O0O0O :#line:1165
                    if OO00O00OOO00O0O0O ['status']==200 :#line:1166
                        OO0OOOO00OOO000O0 =OO00O00OOO00O0O0O ['data']['ordinary_water']#line:1167
                        OOOOO0000O00OOOO0 =OO00O00OOO00O0O0O ['data']['ordinary_fertilizer']#line:1168
                        O0OO000O00O0O00OO =OO00O00OOO00O0O0O ['data']['videoStatus']#line:1169
                        OOOO0O0OOOOOOO0OO =OO00O00OOO00O0O0O ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(OOOOO0000O00OOOO0).split(".")[0]}丨水滴:{str(OO0OOOO00OOO000O0).split(".")[0]}')#line:1172
                        if float (OOOOO0000O00OOOO0 )<96 :#line:1173
                            if O0OO000O00O0O00OO :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                OO0O00OOOOO0O0OOO =99 -float (OOOOO0000O00OOOO0 )#line:1176
                                OO0OOOO00OOOO00O0 ={"fertilizer":str (OO0O00OOOOO0O0OOO ).split ('.')[0 ]}#line:1177
                                OOOOO0000OO00OOOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O00000OO00O000 ).json ()#line:1179
                                if 'status'in OOOOO0000OO00OOOO :#line:1181
                                    if OOOOO0000OO00OOOO ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0000OO00OOOO["message"]}')#line:1183
                                    if OOOOO0000OO00OOOO ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0000OO00OOOO["message"]}')#line:1185
                                        break #line:1186
                                if float (OOOOO0000O00OOOO0 )<78 :#line:1188
                                    OO0O00OOOOO0O0OOO =80 -float (OOOOO0000O00OOOO0 )#line:1189
                                    O0O00OO0O0O0OOOOO =f'_fertilizer={int(OO0O00OOOOO0O0OOO)}_{timi_new()}'#line:1190
                                    O0O0OO000OO0O00O0 ={'source':'scsc','authorization':O0O00OOO00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O0O0OOOOO ),'signstring':O0O00OO0O0O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    O00O00OO00OOOO0O0 ={"fertilizer":int (OO0O00OOOOO0O0OOO )}#line:1202
                                    OOO0O0OOOOO00O00O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0OO000OO0O00O0 ,data =O00O00OO00OOOO0O0 ).json ()#line:1204
                                    if 'status'in OOO0O0OOOOO00O00O :#line:1206
                                        if OOO0O0OOOOO00O00O ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{OOO0O0OOOOO00O00O["message"]}丨数量:{int(OO0O00OOOOO0O0OOO)}')#line:1208
                                        if OOO0O0OOOOO00O00O ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{OOO0O0OOOOO00O00O["message"]}丨数量:{int(OO0O00OOOOO0O0OOO)}')#line:1210
                                            OO00OO000O0OOO0O0 =OOO0O0OOOOO00O00O ["message"].split ('-')[1 ]#line:1211
                                            OO0OO0OOO000OO0O0 =f'__{timi_new()}'#line:1212
                                            O0OOO0OOOO0OO0000 ={'source':'scsc','authorization':O0O00OOO00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOO000OO0O0 ),'signstring':OO0OO0OOO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            OOOO00O00O0O0O00O =requests .request ('get',f'{host}/user',headers =O0OOO0OOOO0OO0000 ).json ()#line:1224
                                            if 'status'in OOOO00O00O0O0O00O :#line:1225
                                                if OOOO00O00O0O0O00O ['status']==200 :#line:1226
                                                    O0OO0OO0OO0OO0OO0 =OOOO00O00O0O0O00O ['data']['inner_id']#line:1227
                                                    if give_gold (O0OO0OO0OO0OO0OO0 ,float (OO00OO000O0OOO0O0 )+1 ):#line:1228
                                                        O0O00OOO00O00OOOO .energy ()#line:1229
                        if float (OO0OOOO00OOO000O0 )<880 :#line:1230
                            if OOOO0O0OOOOOOO0OO :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                OO0O0O0O0O00O000O =999 -float (OO0OOOO00OOO000O0 )#line:1233
                                OO0O0OOOOO00OO00O ={"water":str (OO0O0O0O0O00O000O ).split ('.')[0 ]}#line:1234
                                O00000OOOO0OOOOOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O00000OO00O000 ).json ()#line:1236
                                if 'status'in O00000OOOO0OOOOOO :#line:1238
                                    if O00000OOOO0OOOOOO ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{O00000OOOO0OOOOOO["message"]}')#line:1240
                                    if O00000OOOO0OOOOOO ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{O00000OOOO0OOOOOO["message"]}')#line:1242
                                        break #line:1243
                                if float (OO0OOOO00OOO000O0 )<780 :#line:1244
                                    OO0O0O0O0O00O000O =800 -float (OO0OOOO00OOO000O0 )#line:1245
                                    O0OOO0O00OOO0000O =f'_water={int(OO0O0O0O0O00O000O)}_{timi_new()}'#line:1246
                                    O0O0000O00OO0000O ={'source':'scsc','authorization':O0O00OOO00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00OOO0000O ),'signstring':O0OOO0O00OOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    O00OO000O0OO0O00O ={"water":int (OO0O0O0O0O00O000O )}#line:1258
                                    O00O00000O000O00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0000O00OO0000O ,data =O00OO000O0OO0O00O ).json ()#line:1260
                                    if 'status'in O00O00000O000O00O :#line:1262
                                        if O00O00000O000O00O ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{O00O00000O000O00O["message"]}丨数量:{int(OO0O0O0O0O00O000O)}')#line:1264
                                        if O00O00000O000O00O ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{O00O00000O000O00O["message"]}丨数量:{int(OO0O0O0O0O00O000O)}')#line:1266
                                            OO00OO000O0OOO0O0 =O00O00000O000O00O ["message"].split ('-')[1 ]#line:1267
                                            OO0OO0OOO000OO0O0 =f'__{timi_new()}'#line:1268
                                            O0OOO0OOOO0OO0000 ={'source':'scsc','authorization':O0O00OOO00O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOO000OO0O0 ),'signstring':OO0OO0OOO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            OOOO00O00O0O0O00O =requests .request ('get',f'{host}/user',headers =O0OOO0OOOO0OO0000 ).json ()#line:1280
                                            if 'status'in OOOO00O00O0O0O00O :#line:1281
                                                if OOOO00O00O0O0O00O ['status']==200 :#line:1282
                                                    O0OO0OO0OO0OO0OO0 =OOOO00O00O0O0O00O ['data']['inner_id']#line:1283
                                                    if give_gold (O0OO0OO0OO0OO0OO0 ,float (OO00OO000O0OOO0O0 )+1 ):#line:1284
                                                        O0O00OOO00O00OOOO .energy ()#line:1285
                        break #line:1286
        except Exception as O0O00OOOOO00O000O :#line:1287
            print (O0O00OOOOO00O000O )#line:1288
def bundled_def ():#line:1291
    O0OO00000OO0O00OO =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return O0OO00000OO0O00OO [random .randint (0 ,len (O0OO00000OO0O00OO )-1 )]#line:1293
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
        OO00000OO00OO0O0O =gitee_edition ()#line:1332
        if version_of_the_validation ()<OO00000OO00OO0O0O ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000OO00OO0O0O["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{OO00000OO00OO0O0O["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000OO00OO0O0O["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {OO00000OO00OO0O0O["CityEarth"]["content"]}')#line:1338
    except Exception as O0OO00O0OOOO00O00 :#line:1339
        print (O0OO00O0OOOO00O00 )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
