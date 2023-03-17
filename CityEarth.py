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
        OO000OOOO0OOOO00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OO000OOOO0OOOO00O)}个账号==========")#line:16
        for O000OO0OO00000000 in OO000OOOO0OOOO00O :#line:17
            OOOOO0O0O0O0O00O0 =[]#line:18
            print (f"------------正在执行第{OO000OOOO0OOOO00O.index(O000OO0OO00000000) + 1}个账号------------")#line:19
            OOO0000O00000OO00 =CityEarth (O000OO0OO00000000 ,OOOOO0O0O0O0O00O0 ,OO000OOOO0OOOO00O .index (O000OO0OO00000000 ))#line:20
            def OO0O000OO000OOO00 ():#line:22
                if OOO0000O00000OO00 .base_info ():#line:24
                    OOO0000O00000OO00 .sealing ()#line:26
                    OOO0000O00000OO00 .invitenum ()#line:28
                    OOO0000O00000OO00 .query_to_sell ()#line:30
                    OOO0000O00000OO00 .game_map ()#line:32
                    OOO0000O00000OO00 .friends_invitation ()#line:36
                    OOO0000O00000OO00 .energy ()#line:38
                    OOO0000O00000OO00 .add_clover ()#line:40
                    OOO0000O00000OO00 .propsraffle ()#line:42
                    OOO0000O00000OO00 .synthetic ()#line:44
                    OOO0000O00000OO00 .crops_illustrated ()#line:46
                    OOO0000O00000OO00 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OOO0000O00000OO00 .give_gold ()#line:51
            OO000OO000OO000O0 =threading .Thread (target =OO0O000OO000OOO00 )#line:53
            OO000OO000OO000O0 .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        O00OOOOO0OO00000O =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OOOOO0OO00000O +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO000O00OOO0OOOO in invited_new :#line:62
            print (OOO000O00OOO0OOOO )#line:63
        print ('开始打印未实名的token')#line:64
        for OOO0OOO0000OO0OOO in weishim :#line:65
            print (OOO0OOO0000OO0OOO )#line:66
    except Exception as OO0O0OOOO0000O0OO :#line:67
        print (OO0O0OOOO0000O0OO )#line:68
def give_gold (OOO0O000O000O00O0 ,OOOO0000OO000O000 ):#line:72
    try :#line:73
        O000OOOO0O000O0O0 =f'_doneeNo={OOO0O000O000O00O0}&quantity={int(OOOO0000OO000O000)}_{timi_new()}'#line:74
        OO00OOOOO0O0O00OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O000OOOO0O000O0O0 ),'signstring':O000OOOO0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO000000OO00O00OO ={"quantity":int (OOOO0000OO000O000 ),"doneeNo":OOO0O000O000O00O0 }#line:89
        O00O00OO0OO0OO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00OOOOO0O0O00OO ,data =OO000000OO00O00OO ).json ()#line:90
        if 'status'in O00O00OO0OO0OO0OO :#line:92
            if O00O00OO0OO0OO0OO ['status']==200 :#line:93
                if O00O00OO0OO0OO0OO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOOO0000OO000O000)}种子给{OOO0O000O000O00O0}成功')#line:95
                    return True #line:96
            if O00O00OO0OO0OO0OO ['status']==401 :#line:97
                print (f'【赠送种子】:{O00O00OO0OO0OO0OO["message"]}')#line:98
                return False #line:99
            if O00O00OO0OO0OO0OO ['status']==500 :#line:100
                print (f'【赠送种子】:{O00O00OO0OO0OO0OO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO0O00O00O0OO0OO :#line:104
        print (OOO0O00O00O0OO0OO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0000OO0O0OO0OOOO ):#line:115
    OOO0O000O00OOO00O =hashlib .md5 (O0000OO0O0OO0OOOO .encode ()).hexdigest ()#line:116
    OO000O0OO0O000O00 =sc1 ()#line:117
    OO00OO0O0OOO0OOO0 =sc2 ()#line:118
    O000OOO00O0OO0OO0 =sc3 ()#line:119
    O0O0OOOOOO0OO0OOO =OO000O0OO0O000O00 +OOO0O000O00OOO00O +OO00OO0O0OOO0OOO0 +O000OOO00O0OO0OO0 #line:120
    OOO0000OO00OOOOO0 =hashlib .md5 (O0O0OOOOOO0OO0OOO .encode ()).hexdigest ()#line:121
    return OOO0000OO00OOOOO0 #line:122
def format_msg ():#line:125
    OO0000OO00O0O000O =""#line:126
    for O00OOO0000O0OO000 in msg_list :#line:127
        OO0000OO00O0O000O +=str (O00OOO0000O0OO000 )+"\r\n"#line:128
    return OO0000OO00O0O000O #line:129
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
def get_json_data (O00O0O00OO000OO0O ,O0OO0000OOO0OOOOO ,O0OO0O00OOO0OOO0O ,O0OO000OOOOO0OOO0 ):#line:153
    with open (O00O0O00OO000OO0O ,'rb')as OOOO0O0OOO0OO00O0 :#line:154
        O0000O00O0OO0O000 =json .load (OOOO0O0OOO0OO00O0 )#line:155
        O0000O00O0OO0O000 ['data'][O0OO0000OOO0OOOOO ][O0OO0O00OOO0OOO0O ]=O0OO000OOOOO0OOO0 #line:156
        O0O00OO0OOO00OOOO =O0000O00O0OO0O000 #line:157
    OOOO0O0OOO0OO00O0 .close ()#line:158
    return O0O00OO0OOO00OOOO #line:159
def write_json_data (O00O0OO000O00OOOO ):#line:162
    with open (json_path1 ,'w')as O0OO0OO0OO0OOOOO0 :#line:163
        json .dump (O00O0OO000O00OOOO ,O0OO0OO0OO0OOOOO0 )#line:164
    O0OO0OO0OO0OOOOO0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OO0OO0000OOO0O0 ,O00OO000OOOOOO0OO ,OO0OO000OOO000000 ,OO00OO000OO0000OO ):#line:171
        try :#line:172
            O0OO0OO0000OOO0O0 .msg =OO0OO000OOO000000 #line:173
            O0OO0OO0000OOO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OO0OO0000OOO0O0 .token =O00OO000OOOOOO0OO ['authorization']#line:175
            O0OO0OO0000OOO0O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OO0OO0000OOO0O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OO0OO0000OOO0O0 .elephant_user =O00OO000OOOOOO0OO ['elephant_user']#line:178
            O0OO0OO0000OOO0O0 .elephant_pswd =O00OO000OOOOOO0OO ['elephant_pswd']#line:179
            O0OO0OO0000OOO0O0 .elephant_Task_ID =O00OO000OOOOOO0OO ['elephant_Task_ID']#line:180
            O0OO0OO0000OOO0O0 .len_new =OO00OO000OO0000OO #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O00OOO00000O0000O ):#line:186
        try :#line:187
            O00OOO00000O0000O .watched_ad ()#line:189
            O00OO00OOO0O00O0O =f'__{timi_new()}'#line:190
            OOO0O0000OO000OO0 ={'source':'scsc','authorization':O00OOO00000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OOO0O00O0O ),'signstring':O00OO00OOO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOOO0000O00O0O000 =requests .request ('get',f'{host}/user',headers =OOO0O0000OO000OO0 ).json ()#line:202
            if 'status'in OOOO0000O00O0O000 :#line:204
                if OOOO0000O00O0O000 ['status']==200 :#line:205
                    OOOO0OOO00O0OOO00 =OOOO0000O00O0O000 ['data']['nickname']#line:206
                    O0O0OO0O000OOOO00 =OOOO0000O00O0O000 ['data']['inner_id']#line:207
                    O00OOO0O0O0O0OOOO =OOOO0000O00O0O000 ['data']['assets']['gold']#line:208
                    OO00O0O0O00O0O0OO =OOOO0000O00O0O000 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOOO0OOO00O0OOO00[:5]}丨ID:{O0O0OO0O000OOOO00}丨等级:{OO00O0O0O00O0O0OO}丨金种子:{str(O00OOO0O0O0O0OOOO).split(".")[0]}')#line:211
                    if 'wx_'in OOOO0OOO00O0OOO00 :#line:212
                        O00OOO00000O0000O .change_nickname ()#line:213
                if OOOO0000O00O0O000 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O00OOO00000O0000O .elephant_user =='f':#line:216
                        return False #line:217
                    O0O00OOOOOOOO00O0 =Invalid_login .addtask (elephant_user =O00OOO00000O0000O .elephant_user ,elephant_pswd =O00OOO00000O0000O .elephant_pswd ,elephant_Task_ID =O00OOO00000O0000O .elephant_Task_ID )#line:220
                    O0O000OO00O0O0OO0 =get_json_data (json_path ,O00OOO00000O0000O .len_new ,'authorization',O0O00OOOOOOOO00O0 )#line:221
                    if write_json_data (O0O000OO00O0O0OO0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOOO0000O00O0O000 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOOOO0O00OOO0OOOO :#line:228
            print (OOOOO0O00OOO0OOOO )#line:229
    def sealing (OOOOOO0O0OO000OO0 ):#line:232
        try :#line:233
            O0OO0OOO00OO00000 =f'__{timi_new()}'#line:234
            O0OO0OO0OO0O0OOOO ={'source':'scsc','authorization':OOOOOO0O0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00OO00000 ),'signstring':O0OO0OOO00OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0OO0OO0O0OOOO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0OO0OO0O0OOOO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0OO0OO0O0OOOO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0OO0OO0O0OOOO )#line:249
            requests .request ('get',f'{host}/user',headers =O0OO0OO0OO0O0OOOO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0OO0OO0O0OOOO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0OO0OO0O0OOOO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0OO0OO0O0OOOO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO0OO0O0OOOO )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OO0OO0OO0O0OOOO )#line:255
        except Exception as O0O00OO0OOOOO00O0 :#line:256
            print (O0O00OO0OOOOO00O0 )#line:257
    def ddd (OOOO0O0OO000OOO0O ):#line:259
        try :#line:260
            OOO000O00O0O0O00O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OOO0OOO00O0OO0O00 ={'source':'scsc','authorization':OOOO0O0OO000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O00O0O0O00O ),'signstring':OOO000O00O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0O0000OOO000OOOO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO0OOO00O0OO0O00 ).json ()#line:273
            print (O0O0000OOO000OOOO )#line:274
        except Exception as OOO0OOOO0OOO000OO :#line:279
            print (OOO0OOOO0OOO000OO )#line:280
    def the_query (O0O00OO000O00OOO0 ):#line:290
        try :#line:291
            OOOOOO0000O00O000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            OOO0OOOO000OOO000 ={'authorization':O0O00OO000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000O00O000 ),'signstring':OOOOOO0000O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            OO00OO000000O0O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO0OOOO000OOO000 ).json ()#line:304
            if 'status'in OO00OO000000O0O0O :#line:306
                if OO00OO000000O0O0O ['status']==200 :#line:307
                    OOOOOOOO0OOOO0O00 =OO00OO000000O0O0O ['data']['rows'][3 ]['price']#line:308
                    O0O00OO000O00OOO0 .market_sale (OOOOOOOO0OOOO0O00 )#line:309
        except Exception as O0O0000O000000O00 :#line:310
            print (O0O0000O000000O00 )#line:311
    def market_sale (O0000000OOOOOOOOO ,O0O0OOO00OO0OO0O0 ):#line:314
        try :#line:315
            OOOO0OO00OO00O000 =timi_new ()#line:316
            OO0OOO0O0O0O0O00O =f'type=crop__{OOOO0OO00OO00O000}'#line:317
            OO00O0OOOO00OO0OO ={'source':'scsc','authorization':O0000000OOOOOOOOO .token ,'timestamp':str (OOOO0OO00OO00O000 ),'sign':sign (OO0OOO0O0O0O0O00O ),'signstring':OO0OOO0O0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O0O00OOO0OOOOOO00 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00O0OOOO00OO0OO ).json ()#line:330
            if 'status'in O0O00OOO0OOOOOO00 :#line:332
                if O0O00OOO0OOOOOO00 ['status']==200 :#line:333
                    if O0O00OOO0OOOOOO00 ['data']['rows']:#line:334
                        O0OOOO0O0OO00O000 =O0O00OOO0OOOOOO00 ['data']['rows'][0 ]['packsackItemId']#line:335
                        O000O00O0OO00OOO0 =O0O00OOO0OOOOOO00 ['data']['rows'][0 ]['quantity']#line:336
                        O0OOOOO0000000000 =float (O0O0OOO00OO0OO0O0 )-0.00001 #line:337
                        if O0OOOOO0000000000 >8 :#line:338
                            O0O000O00O00OO0O0 =f'_packsackItemId={O0OOOO0O0OO00O000}&price={str(O0OOOOO0000000000)[:9]}&quantity={O000O00O0OO00OOO0}_{OOOO0OO00OO00O000}'#line:339
                            OO0OO0O0OO0OO00OO ={'source':'scsc','authorization':O0000000OOOOOOOOO .token ,'timestamp':str (OOOO0OO00OO00O000 ),'sign':sign (O0O000O00O00OO0O0 ),'signstring':O0O000O00O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O0000OOO0OOO0OOO0 ={"packsackItemId":O0OOOO0O0OO00O000 ,"price":str (O0OOOOO0000000000 )[:9 ],"quantity":str (O000O00O0OO00OOO0 )}#line:355
                            O00O0000000O0OO00 =requests .request ('post',f'{host}/market/sale',headers =OO0OO0O0OO0OO00OO ,data =O0000OOO0OOO0OOO0 ).json ()#line:356
                            if 'status'in O00O0000000O0OO00 :#line:358
                                if O00O0000000O0OO00 ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{O000O00O0OO00OOO0}丨价格:{str(O0OOOOO0000000000)[:9]}')#line:360
        except Exception as OOOOOO00OOOOOO0O0 :#line:361
            print (OOOOOO00OOOOOO0O0 )#line:362
    def query_to_sell (OO00000O00O0OOOOO ):#line:365
        try :#line:366
            O00O0OOO0O00OOO0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            O0O0OO000O0O000O0 ={'source':'scsc','authorization':OO00000O00O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0O00OOO0O ),'signstring':O00O0OOO0O00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            O00O0OOO0OO0O0000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O0OO000O0O000O0 ).json ()#line:380
            if 'status'in O00O0OOO0OO0O0000 :#line:382
                if O00O0OOO0OO0O0000 ['status']==200 :#line:383
                    for O00OOOOO00O0OO0OO in O00O0OOO0OO0O0000 ['data']['rows']:#line:384
                        OOO000O00OO0OOOOO =O00OOOOO00O0OO0OO ['materialKey']#line:385
                        OOOOO000O0OO0O00O =O00OOOOO00O0OO0OO ['quantity']#line:386
                        O00O00OOOO000000O =O00OOOOO00O0OO0OO ['price']#line:387
                        O000OOOO00O0O0OOO =O00OOOOO00O0OO0OO ['saleState']#line:388
                        if O000OOOO00O0O0OOO ==0 :#line:389
                            print (f'【出售订单】:名称:{OOO000O00OO0OOOOO}丨数量:{OOOOO000O0OO0O00O}丨价格:{O00O00OOOO000000O}')#line:390
                            OO00OO00OO00000O0 =O00OOOOO00O0OO0OO ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                OO00000O00O0OOOOO .cacel_sale (OO00OO00OO00000O0 )#line:393
        except Exception as O00OOOO00O0OO000O :#line:394
            print (O00OOOO00O0OO000O )#line:395
    def cacel_sale (OOOO00OO000OOOO00 ,OO0OOO00OO0000O00 ):#line:398
        try :#line:399
            O0OOOOO000OO00OOO =f'_saleId={OO0OOO00OO0000O00}_{timi_new()}'#line:400
            O0OOOO000OO000OO0 ={'source':'scsc','authorization':OOOO00OO000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO000OO00OOO ),'signstring':O0OOOOO000OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O0000O00OO00000OO ={"saleId":OO0OOO00OO0000O00 }#line:414
            OO00O000O0O0OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OOOO000OO000OO0 ,data =O0000O00OO00000OO ).json ()#line:415
            if 'status'in OO00O000O0O0OOOOO :#line:417
                if OO00O000O0O0OOOOO ['status']==200 :#line:418
                    print (f'【下架出售】:{OO00O000O0O0OOOOO["data"]}')#line:419
        except Exception as OO00O0OO0OOOOO0OO :#line:420
            print (OO00O0OO0OOOOO0OO )#line:421
    def change_nickname (O0O000O0000000O00 ):#line:424
        try :#line:425
            OOO0O0OO0O000O00O =timi_new ()#line:426
            OOO000O00OOOOOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOOOO00O000O0O0O0 =requests .request ('post','https://www.qmsjmfb.com/',data =OOO000O00OOOOOO00 ).text #line:428
            OO0O0OOOO0O0OOO00 =re .findall ('<ul><li>(.*?)</li>',OOOOO00O000O0O0O0 )[0 ][:3 ]#line:429
            O0OOO0OO0OOO00O0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0OOOO0O0OOO00}').json ()#line:430
            O000O00O00O000O0O =O0OOO0OO0OOO00O0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            OOOO00O0000O0OOO0 ={"nickname":O000O00O00O000O0O }#line:432
            OOO0O00O0O0000000 =f'_nickname={O000O00O00O000O0O}_{OOO0O0OO0O000O00O}'#line:433
            O0O0OO0OOOOOO00OO ={'source':'scsc','authorization':O0O000O0000000O00 .token ,'timestamp':OOO0O0OO0O000O00O ,'sign':sign (OOO0O00O0O0000000 ),'signstring':OOO0O00O0O0000000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O0OO00O0O0OOO00O0 =requests .request ('patch',f'{host}/user/nickname',headers =O0O0OO0OOOOOO00OO ,data =OOOO00O0000O0OOO0 ).json ()#line:445
            if 'status'in O0OO00O0O0OOO00O0 :#line:447
                if O0OO00O0O0OOO00O0 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O000O00O00O000O0O}丨{O0OO00O0O0OOO00O0["message"]}')#line:449
        except Exception as OO00O0OO0O00000OO :#line:450
            print (OO00O0OO0O00000OO )#line:451
    def withdraw (O000O0O0OO00O000O ):#line:454
        try :#line:455
            OOO00O000OOOOOO0O =f'__{timi_new()}'#line:456
            O00OOOO0000OOOOOO ={'source':'scsc','authorization':O000O0O0OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000OOOOOO0O ),'signstring':OOO00O000OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O0O0OOO00O0O0O000 =requests .request ('get',f'{host}/assets',headers =O00OOOO0000OOOOOO ).json ()#line:468
            if 'status'in O0O0OOO00O0O0O000 :#line:470
                if O0O0OOO00O0O0O000 ['status']==200 :#line:471
                    OOOO0OOOO0OO0OO00 =O0O0OOO00O0O0O000 ['data']['cash']#line:472
                    if float (OOOO0OOOO0OO0OO00 )>20 :#line:473
                        OOO00O000OOOOOO0O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O00OOOO0000OOOOOO ={'authorization':O000O0O0OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000OOOOOO0O ),'signstring':OOO00O000OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        O0OO00OOOOOOOO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        O00OO00O0O00O0OOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OOOO0000OOOOOO ,data =O0OO00OOOOOOOO00O ).json ()#line:487
                        if 'status'in O00OO00O0O00O0OOO :#line:489
                            if O00OO00O0O00O0OOO ['status']==200 :#line:490
                                print (f'【余额提现】:{O00OO00O0O00O0OOO["data"]}')#line:491
                        if 'status'in O00OO00O0O00O0OOO :#line:492
                            if O00OO00O0O00O0OOO ['status']==500 :#line:493
                                print (f'【余额提现】:{O00OO00O0O00O0OOO["message"]}')#line:494
        except Exception as OOOO00OOOOO0O00OO :#line:495
            print (OOOO00OOOOO0O00OO )#line:496
    def invitenum (OO0OOOOOO000O0O0O ):#line:499
        global invited_new #line:500
        try :#line:501
            O0OO0OO00OO0OOO0O =f'__{timi_new()}'#line:502
            OOOOO000O0O00OOO0 ={'source':'scsc','authorization':OO0OOOOOO000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00OO0OOO0O ),'signstring':O0OO0OO00OO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O000O0O0OOOOOO0OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO000O0O00OOO0 ).json ()#line:514
            if 'status'in O000O0O0OOOOOO0OO :#line:516
                if O000O0O0OOOOOO0OO ['status']==200 :#line:517
                    O00OOO0OOO0O0OOOO =O000O0O0OOOOOO0OO ['data']['invited_count']#line:518
                    OOOO0O0O0OO0000OO =O000O0O0OOOOOO0OO ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O00OOO0OOO0O0OOOO}丨间邀好友:{OOOO0O0O0OO0000OO}')#line:520
                    if O00OOO0OOO0O0OOOO <2 :#line:521
                        OO0000O0000O000O0 =f'__{timi_new()}'#line:522
                        O0OO000OOOOOO000O ={'source':'scsc','authorization':OO0OOOOOO000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0000O000O0 ),'signstring':OO0000O0000O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OO00O0OO00OOOOO00 =requests .request ('get',f'{host}/user',headers =O0OO000OOOOOO000O ).json ()#line:534
                        if 'status'in OO00O0OO00OOOOO00 :#line:536
                            if OO00O0OO00OOOOO00 ['status']==200 :#line:537
                                invited_new .append (OO00O0OO00OOOOO00 ['data']['inner_id'])#line:538
        except Exception as O0OO00O000O000O0O :#line:539
            print (O0OO00O000O000O0O )#line:540
    def game_map (OO000O000OO0O0O0O ):#line:543
        try :#line:544
            O0000O00O0OO000OO =f'__{timi_new()}'#line:545
            O0O0OOOO00OOO0000 ={'source':'scsc','authorization':OO000O000OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00O0OO000OO ),'signstring':O0000O00O0OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            OO0O00OO0O000O000 =requests .request ('get',f'{host}/game/map',headers =O0O0OOOO00OOO0000 ).json ()#line:557
            if 'status'in OO0O00OO0O000O000 :#line:559
                if OO0O00OO0O000O000 ['status']==200 :#line:560
                    for OOO0O00O000OOOO00 in OO0O00OO0O000O000 ['data']['list'][0 ]['crops']:#line:561
                        O000O00OOO00000O0 =OOO0O00O000OOOO00 ['level']#line:563
                        if O000O00OOO00000O0 ==41 :#line:564
                            OO0O0O0OOO000O00O =OOO0O00O000OOOO00 ['crop_name']#line:565
                            O0OO00OO00O0O0O00 =OOO0O00O000OOOO00 ['count']#line:566
                            if O0OO00OO00O0O0O00 >0 :#line:567
                                print (f'【农业资产】:{OO0O0O0OOO000O00O}丨数量:{O0OO00OO00O0O0O00}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    OO000O000OO0O0O0O .the_query ()#line:570
        except Exception as O0O00OOOO0O0O00O0 :#line:571
            print (O0O00OOOO0O0O00O0 )#line:572
    def give_gold (OO0O00OOO0OO0OOO0 ):#line:575
        try :#line:576
            OOO00OOO0O00OOOO0 =f'__{timi_new()}'#line:577
            O00000OO0OOO000OO ={'source':'scsc','authorization':OO0O00OOO0OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O00OOOO0 ),'signstring':OOO00OOO0O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            OO00000OOO00OO000 =requests .request ('get',f'{host}/user',headers =O00000OO0OOO000OO ).json ()#line:589
            if 'status'in OO00000OOO00OO000 :#line:590
                if OO00000OOO00OO000 ['status']==200 :#line:591
                    if float (OO0O00OOO0OO0OOO0 .doneeNo )!=0 :#line:592
                        O00OOO0O0OO0OO0O0 =OO00000OOO00OO000 ['data']['assets']['gold']#line:593
                        if float (O00OOO0O0OO0OO0O0 )>float (OO0O00OOO0OO0OOO0 .innerId ):#line:594
                            O00O00OO00O0O000O =int (float (O00OOO0O0OO0OO0O0 )/1.1 )#line:595
                            OOO00OOO0O00OOOO0 =f'_doneeNo={OO0O00OOO0OO0OOO0.doneeNo}&quantity={O00O00OO00O0O000O}_{timi_new()}'#line:596
                            O00000OO0OOO000OO ={'source':'scsc','authorization':OO0O00OOO0OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O00OOOO0 ),'signstring':OOO00OOO0O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            O00OOO00OO0OO0O0O ={"quantity":O00O00OO00O0O000O ,"doneeNo":OO0O00OOO0OO0OOO0 .doneeNo }#line:611
                            O00O0O00OOO0OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O00000OO0OOO000OO ,data =O00OOO00OO0OO0O0O ).json ()#line:612
                            if 'status'in O00O0O00OOO0OOO0O :#line:614
                                if O00O0O00OOO0OOO0O ['status']==200 :#line:615
                                    if O00O0O00OOO0OOO0O ['data']:#line:616
                                        print (f'【赠送种子】:赠送{O00O00OO00O0O000O}种子给{OO0O00OOO0OO0OOO0.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as OO0O00OO0OO0OO00O :#line:620
            print (OO0O00OO0OO0OO00O )#line:621
    def invitation (OO000O00OO0OOOO00 ):#line:623
        try :#line:624
            _OOOO00OOOO00OO0O0 =float (bundled_def ())/4 #line:625
            OOOO000O00O000OO0 =f'_innerId={int(_OOOO00OOOO00OO0O0)}_{timi_new()}'#line:626
            OO00OO00OO0000O00 ={'source':'scsc','authorization':OO000O00OO0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00O000OO0 ),'signstring':OOOO000O00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            OOOO0OOOO0OOO00OO ={"innerId":int (_OOOO00OOOO00OO0O0 )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00OO00OO0000O00 ,data =OOOO0OOOO0OOO00OO )#line:639
        except Exception as OOO000OO0O0O0OOOO :#line:640
            print (OOO000OO0O0O0OOOO )#line:641
    def winning_rewards (OO0OOO0O00O0O000O ):#line:644
        try :#line:645
            O00OO0OOOO0OOO00O =f'__{timi_new()}'#line:646
            OOO0000O000000OO0 ={'source':'scsc','authorization':OO0OOO0O00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOO0OOO00O ),'signstring':O00OO0OOOO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O0OO00000000O0OOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0000O000000OO0 ).json ()#line:658
            if 'status'in O0OO00000000O0OOO :#line:660
                if O0OO00000000O0OOO ['status']==200 :#line:661
                    if O0OO00000000O0OOO ['data']['amount']:#line:662
                        O0OO0O0OOO0O00000 =O0OO00000000O0OOO ['data']['amount']['gold']#line:663
                        return O0OO0O0OOO0O00000 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as O00000O00OOO0O0O0 :#line:667
            print (O00000O00OOO0O0O0 )#line:668
    def certification (OO00O0O000000O0O0 ):#line:671
        try :#line:672
            O0OO00O000OO0000O =f'__{timi_new()}'#line:673
            O00OO0000OO0OOOOO ={'source':'scsc','authorization':OO00O0O000000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000OO0000O ),'signstring':O0OO00O000OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            O000000OO000OOOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0000OO0OOOOO ).json ()#line:685
            if 'status'in O000000OO000OOOO0 :#line:687
                if O000000OO000OOOO0 ['status']==200 :#line:688
                    if O000000OO000OOOO0 ['data']['result']:#line:689
                        OOO000O0OOOOOO00O =O000000OO000OOOO0 ['data']['nick_name']#line:690
                        return OOO000O0OOOOOO00O #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as O0O00O00OO000OOOO :#line:694
            print (O0O00O00OO000OOOO )#line:695
    def crops_illustrated (O000O000OOOOO0OO0 ):#line:698
        try :#line:699
            O0OO00O0OOOOO000O =f'__{timi_new()}'#line:700
            O0OOO00OO00O00000 ={'source':'scsc','authorization':O000O000OOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OOOOO000O ),'signstring':O0OO00O0OOOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOOO00OOOO00OOOO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO00OO00O00000 ).json ()#line:712
            if 'status'in OOOO00OOOO00OOOO0 :#line:714
                if OOOO00OOOO00OOOO0 ['status']==200 :#line:715
                    O0OO0O00OOOOO000O =OOOO00OOOO00OOOO0 ['data'][0 ]['crops']#line:716
                    for OOO000OO000OOO000 in O0OO0O00OOOOO000O :#line:717
                        if OOO000OO000OOO000 ['ill_clover_award']:#line:718
                            if float (OOO000OO000OOO000 ['ill_clover_award'])>1 :#line:719
                                if OOO000OO000OOO000 ['is_finish']:#line:720
                                    if not OOO000OO000OOO000 ['is_getit']:#line:721
                                        if O000O000OOOOO0OO0 .certification ()!='未实名':#line:722
                                            O0OO00O0OOOOO000O =f'_award_level={OOO000OO000OOO000["level"]}_{timi_new()}'#line:723
                                            O0OOO00OO00O00000 ={'source':'scsc','authorization':O000O000OOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OOOOO000O ),'signstring':O0OO00O0OOOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            O0OOO0OOOOOOO0OO0 ={"award_level":OOO000OO000OOO000 ['level']}#line:735
                                            OOOOOO0OO000OOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO00OO00O00000 ,json =O0OOO0OOOOOOO0OO0 ).json ()#line:737
                                            if 'status'in OOOOOO0OO000OOOO0 :#line:738
                                                if OOOOOO0OO000OOOO0 ['status']==200 :#line:739
                                                    OOOOO00OO00OO0OOO =OOOOOO0OO000OOOO0 ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{OOO000OO000OOO000["crop_name"]}成就丨奖励{OOOOO00OO00OO0OOO}☘️')#line:742
                                                if OOOOOO0OO000OOOO0 ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{OOOOOO0OO000OOOO0["message"]}')#line:744
        except Exception as OOOOOOO0O00O0O000 :#line:745
            print (OOOOOOO0O00O0O000 )#line:746
    def watched_ad (O00OO0O0OOOOO0OO0 ):#line:749
        try :#line:750
            O000OO0O0OO000O00 =f'__{timi_new()}'#line:751
            O00O0O0O00O0OO00O ={'source':'scsc','authorization':O00OO0O0OOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0O0OO000O00 ),'signstring':O000OO0O0OO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            OO0O0OOOOO000O000 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O00O0OO00O ).json ()#line:763
            if 'status'in OO0O0OOOOO000O000 :#line:765
                if OO0O0OOOOO000O000 ['status']==200 :#line:766
                    if 'offlineInfo'in OO0O0OOOOO000O000 ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        OOOO0000000000000 =OO0O0OOOOO000O000 ['data']['offlineInfo']['off_minute']#line:769
                        O0O0O0O0O0OO000OO =float (OO0O0OOOOO000O000 ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0O0O00O0OO00O ).json ()#line:772
                        time .sleep (2 )#line:773
                        O000OO0000O0000OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O00O0OO00O ).json ()#line:774
                        if 'status'in O000OO0000O0000OO :#line:776
                            if O000OO0000O0000OO ['status']==200 :#line:777
                                O0O00OOO0OOO0000O =float (O000OO0000O0000OO ['data']['silver'])/1000000000000 #line:778
                                OO00OOO0O00OOOO00 =str (O0O00OOO0OOO0000O -O0O0O0O0O0OO000OO )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{OOOO0000000000000}分钟奖励🌱数量:{OO00OOO0O00OOOO00}t粒')#line:780
        except Exception as O0O0OOOO0OO0OO0O0 :#line:781
            print (O0O0OOOO0OO0OO0O0 )#line:782
    def user_ad (OO00O0OOOO00OOOO0 ):#line:785
        try :#line:786
            O0000O0000O0O0000 =f'__{timi_new()}'#line:787
            OO00O0O0OOO0OOO0O ={'source':'scsc','authorization':OO00O0OOOO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0000O0O0000 ),'signstring':O0000O0000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            OOO0OO0O0O00000O0 =requests .request ('get',f'{host}/user/ad',headers =OO00O0O0OOO0OOO0O ).json ()#line:799
            if 'status'in OOO0OO0O0O00000O0 :#line:801
                if OOO0OO0O0O00000O0 ['status']==200 :#line:802
                    O0O0OOO00O00OOO00 =OOO0OO0O0O00000O0 ['data']['max_time']#line:803
                    O0O00OOOOOO00O000 =OOO0OO0O0O00000O0 ['data']['watch_time']#line:804
                    O0O00O000O00OO000 =OOO0OO0O0O00000O0 ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{O0O00O000O00OO000 + O0O0OOO00O00OOO00 - O0O00OOOOOO00O000}次丨好友提供:{O0O00O000O00OO000}次')#line:806
                    if O0O00O000O00OO000 +O0O0OOO00O00OOO00 -O0O00OOOOOO00O000 >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        O00OO0000000OOOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00O0O0OOO0OOO0O ).json ()#line:809
                        if 'status'in O00OO0000000OOOO0 :#line:811
                            if O00OO0000000OOOO0 ['status']==200 :#line:812
                                O000O0O00000OO0OO =float (O00OO0000000OOOO0 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(O000O0O00000OO0OO)}t粒')#line:814
                                return True #line:815
                            if O00OO0000000OOOO0 ['status']==500 :#line:816
                                O0OO00O0O0OOO0OOO =O00OO0000000OOOO0 ['message']#line:817
                                print (f'【获取种子】:{O0OO00O0O0OOO0OOO}')#line:818
                                return False #line:819
        except Exception as OO000O000O00OO000 :#line:820
            print (OO000O000O00OO000 )#line:821
    def synthetic (O000OOO00OO00000O ):#line:824
        global id ,g #line:825
        try :#line:826
            O0OO0OOO0O000OO00 =O000OOO00OO00000O .level_new ()#line:827
            O0OO00OO000O0OOO0 =random .randint (9 ,11 )#line:828
            OO0OOO0O00OOOO00O =f'_site=8&targetSite={O0OO00OO000O0OOO0}_{timi_new()}'#line:829
            O0O00OO00O0OOOO00 ={'source':'scsc','authorization':O000OOO00OO00000O .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O00OOOO00O ),'signstring':OO0OOO0O00OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            O00OOOO0O0O0OOO0O ={"site":int (8 ),"targetSite":int (O0OO00OO000O0OOO0 )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O0O00OO00O0OOOO00 ,json =O00OOOO0O0O0OOO0O )#line:842
            while True :#line:843
                O00OOOOOOO0OOOOO0 =f'__{timi_new()}'#line:844
                O0OO0000O0O0O0O00 ={'source':'scsc','authorization':O000OOO00OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO0OOOOO0 ),'signstring':O00OOOOOOO0OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                O00O0O0O00OO0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0000O0O0O0O00 ).json ()#line:856
                if 'status'in O00O0O0O00OO0OOO0 :#line:858
                    if O00O0O0O00OO0OOO0 ['status']==200 :#line:859
                        OOO0O0000O0O0O0O0 =O00O0O0O00OO0OOO0 ['data']['cropList']#line:860
                        O00O00O0OO0OO0000 =O00O0O0O00OO0OOO0 ['data']['gameCoreDataDBid']#line:861
                        O00OOOO0O000O00O0 =float (O00O0O0O00OO0OOO0 ['data']['silver'])/1000000000000 #line:862
                        OO0OOOOOOO00OO0O0 =0 #line:867
                        for O00OOOOOO000000O0 in OOO0O0000O0O0O0O0 :#line:868
                            if not O00OOOOOO000000O0 :#line:869
                                O000O00O0O0O0O0O0 =f'_crop_id={O00O00O0OO0OO0000}&site={OO0OOOOOOO00OO0O0}_{O000OOO00OO00000O.time}'#line:870
                                O00OO0000OO000O0O ={'source':'scsc','authorization':O000OOO00OO00000O .token ,'timestamp':O000OOO00OO00000O .time ,'sign':sign (O000O00O0O0O0O0O0 ),'signstring':O000O00O0O0O0O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                OOOOO0OOO00O0O0OO ={"site":OO0OOOOOOO00OO0O0 ,"crop_id":O00O00O0OO0OO0000 }#line:881
                                O0O0OOO000OOOOOOO =requests .request ('post',f'{host}/game/crops/buy',headers =O00OO0000OO000O0O ,data =OOOOO0OOO00O0O0OO ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in O0O0OOO000OOOOOOO :#line:885
                                    if O0O0OOO000OOOOOOO ['status']==200 :#line:886
                                        if O0O0OOO000OOOOOOO ['message']=='种子数量不足':#line:887
                                            O0OO0OOO0O000OO00 =O000OOO00OO00000O .level_new ()#line:888
                                            print (f'【种植合成】:{O0O0OOO000OOOOOOO["message"]}')#line:889
                                            if not O000OOO00OO00000O .user_ad ():#line:890
                                                return False #line:891
                                    if O0O0OOO000OOOOOOO ['status']==500 :#line:892
                                        print (f'【种植合成】:{O0O0OOO000OOOOOOO["message"]}')#line:893
                                        return False #line:894
                            OO0OOOOOOO00OO0O0 +=1 #line:895
                        OO00OOOO0O0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0000O0O0O0O00 ).json ()#line:896
                        OOOO00O0O00OOO000 =OO00OOOO0O0OOO000 ['data']['cropList']#line:897
                        OOOOOO0000OO0OO0O =False #line:898
                        for O00OOOOOO000000O0 in range (12 ):#line:899
                            id =OOOO00O0O00OOO000 [O00OOOOOO000000O0 ]['level']#line:900
                            if float (O0OO0OOO0O000OO00 )-float (id )>9 :#line:901
                                OO00OOO00OOOO00O0 =f'_site={O00OOOOOO000000O0}_{timi_new()}'#line:902
                                OO000OOOO0O000OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOO00OO00000O .token ,'timestamp':timi_new (),'sign':sign (OO00OOO00OOOO00O0 ),'signstring':OO00OOO00OOOO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                OOOOO0OOO0O000OOO ={"site":O00OOOOOO000000O0 }#line:914
                                O00OO000O0OO0O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO000OOOO0O000OO0 ,data =OOOOO0OOO0O000OOO ).json ()#line:916
                                if 'status'in O00OO000O0OO0O00O :#line:917
                                    if O00OO000O0OO0O00O ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O0OOO0O0O0000OOOO in range (11 ):#line:921
                                    OO0OO000000OO0OO0 =O0OOO0O0O0000OOOO +1 #line:922
                                    g =OOOO00O0O00OOO000 [OO0OO000000OO0OO0 ]['level']#line:923
                                    if id ==g :#line:924
                                        OO00OO00O0OO000OO =O0OOO0O0O0000OOOO +2 #line:925
                                        if OO00OO00O0OO000OO !=O00OOOOOO000000O0 +1 :#line:926
                                            O0OOOOOO0O0O000OO =O00OOOOOO000000O0 +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            OO0OOO0O00OOOO00O =f'_site={O0OOOOOO0O0O000OO - 1}&targetSite={OO00OO00O0OO000OO - 1}_{timi_new()}'#line:930
                                            O0O00OO00O0OOOO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOO00OO00000O .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O00OOOO00O ),'signstring':OO0OOO0O00OOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O0000O0000O0OO0OO ={"site":int (O0OOOOOO0O0O000OO -1 ),"targetSite":int (OO00OO00O0OO000OO -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O00OO00O0OOOO00 ,json =O0000O0000O0OO0OO )#line:949
                                            OOOOOO0000OO0OO0O =True #line:951
                                    if OOOOOO0000OO0OO0O :#line:952
                                        break #line:953
                                if OOOOOO0000OO0OO0O :#line:954
                                    break #line:955
        except :#line:956
            O000OOO00OO00000O .synthetic ()#line:957
    def level_new (OOO00000OOOOOOO00 ):#line:960
        try :#line:961
            O0O0O0OOOO0OO00OO =f'__{timi_new()}'#line:962
            O00OO000O000OOO0O ={'source':'scsc','authorization':OOO00000OOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOO0OO00OO ),'signstring':O0O0O0OOOO0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OOOO000O00000OOO0 =requests .request ('get',f'{host}/user',headers =O00OO000O000OOO0O ).json ()#line:974
            if 'status'in OOOO000O00000OOO0 :#line:975
                if OOOO000O00000OOO0 ['status']==200 :#line:976
                    return float (OOOO000O00000OOO0 ['data']['level'])#line:977
        except Exception as O0O0O00OO0OOO00O0 :#line:978
            print (O0O0O00OO0OOO00O0 )#line:979
    def propsraffle (OO00O0OOO0OOO0000 ):#line:982
        try :#line:983
            while True :#line:984
                O0O00OOO00O0O0OO0 =f'__{timi_new()}'#line:985
                O0000000O0OO00OOO ={'source':'scsc','authorization':OO00O0OOO0OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00O0O0OO0 ),'signstring':O0O00OOO00O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                OOO00OO0OO0O0OO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000000O0OO00OOO ).json ()#line:997
                if 'status'in OOO00OO0OO0O0OO0O :#line:999
                    if OOO00OO0OO0O0OO0O ['status']==200 :#line:1000
                        OO0OOOO0O0OOO0O00 =OOO00OO0OO0O0OO0O ['data']['rows']#line:1001
                        OOO0O000OOO000O0O =OOO00OO0OO0O0OO0O ['data']['vstate']#line:1002
                        if OO0OOOO0O0OOO0O00 ==5 or OO0OOOO0O0OOO0O00 ==6 or OO0OOOO0O0OOO0O00 ==7 :#line:1003
                            OOOOOO0OO000000O0 =OOO00OO0OO0O0OO0O ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{OOOOOO0OO000000O0}')#line:1005
                        if OO0OOOO0O0OOO0O00 ==1 or OO0OOOO0O0OOO0O00 ==2 or OO0OOOO0O0OOO0O00 ==3 :#line:1006
                            OO00O00OO00OOO000 =OOO00OO0OO0O0OO0O ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{OO00O00OO00OOO000}')#line:1008
                        if OO0OOOO0O0OOO0O00 ==4 or OO0OOOO0O0OOO0O00 ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if OO0OOOO0O0OOO0O00 =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as OO0OO00OO0OOOOO00 :#line:1050
            print (OO0OO00OO0OOOOO00 )#line:1051
    def friends_invitation (OOOOOOO0O00000OOO ):#line:1054
        try :#line:1055
            OO0O0OOOOOO0O0O0O =f'__{timi_new()}'#line:1056
            OO00O00OO0OOO00OO ={'source':'scsc','authorization':OOOOOOO0O00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOOO0O0O0O ),'signstring':OO0O0OOOOOO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            O0OO0O000O00OO00O =requests .request ('get',f'{host}/friends',headers =OO00O00OO0OOO00OO ).json ()#line:1068
            if 'status'in O0OO0O000O00OO00O :#line:1069
                if O0OO0O000O00OO00O ['status']==200 :#line:1070
                    OOO000O0OO000OO0O =O0OO0O000O00OO00O ['data']['myInviteter']#line:1071
                    if OOO000O0OO000OO0O :#line:1072
                        O0OO0000O00000O00 =OOO000O0OO000OO0O ['user']['nickname']#line:1073
                        OOOOO0000O0OO00O0 =OOOOOOO0O00000OOO .certification ()#line:1074
                        if OOOOO0000O0OO00O0 =='未实名':#line:1075
                            weishim .append (OOOOOOO0O00000OOO .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{O0OO0000O00000O00}丨实名:{OOOOO0000O0OO00O0}')#line:1077
                    else :#line:1078
                        if OOOOOOO0O00000OOO .innerId !='0':#line:1079
                            OOOOOOO0O00000OOO .invitation ()#line:1080
        except Exception as OOO0OO000OOOOOOO0 :#line:1081
            print (OOO0OO000OOOOOOO0 )#line:1082
    def add_clover (OOOOOO00O00OO00O0 ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            OOOOOO0O0000OOOO0 =f'__{timi_new()}'#line:1088
            O00O0OOOO0O0000O0 ={'source':'scsc','authorization':OOOOOO00O00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0000OOOO0 ),'signstring':OOOOOO0O0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O000O0000OOO00O00 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0OOOO0O0000O0 ).json ()#line:1100
            if 'status'in O000O0000OOO00O00 :#line:1102
                if O000O0000OOO00O00 ['status']==200 :#line:1103
                    O0O0O0O0O0OO00O00 =O000O0000OOO00O00 ['data']['clover']#line:1104
                    OOOOO00O0O0OOO000 =O000O0000OOO00O00 ['data']['used_clover']#line:1105
                    OOOO0O00000OOO0O0 =float (O0O0O0O0O0OO00O00 )-float (OOOOO00O0O0OOO000 )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOO00O0O0OOO000}')#line:1107
                    if OOOOOO00O00OO00O0 .certification ()!='未实名':#line:1108
                        if OOOO0O00000OOO0O0 >1 :#line:1109
                            OOOOOO0O0000OOOO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO0O00000OOO0O0)}_{timi_new()}'#line:1110
                            OOO00OO000O00OOO0 ={'source':'scsc','authorization':OOOOOO00O00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O0000OOOO0 ),'signstring':OOOOOO0O0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            OOOOOO0OO000OO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO0O00000OOO0O0 )}#line:1122
                            O00000OO00OO0OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00OO000O00OOO0 ,data =OOOOOO0OO000OO000 ).json ()#line:1123
                            if 'status'in O00000OO00OO0OOOO :#line:1125
                                if O00000OO00OO0OOOO ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O00000OO00OO0OOOO["data"]["isSuccess"]}丨数量:{OOOO0O00000OOO0O0}')#line:1127
                                if O00000OO00OO0OOOO ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O00000OO00OO0OOOO["message"]}')#line:1129
            OOOOOOOOOOO0OO0OO =requests .request ('get',f'{host}/lottery',headers =O00O0OOOO0O0000O0 ).json ()#line:1130
            O00O0OOO0OOO0OOO0 =OOOOOO00O00OO00O0 .winning_rewards ()#line:1132
            if 'status'in OOOOOOOOOOO0OO0OO :#line:1133
                if OOOOOOOOOOO0OO0OO ['status']==200 :#line:1134
                    O0O0OOOO00O000OOO =OOOOOOOOOOO0OO0OO ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (O0O0OOOO00O000OOO )#line:1136
                    OO0O0O0O000O0OOO0 =OOOOOOOOOOO0OO0OO ['data'][1 ]['value']#line:1137
                    OO00O0OO0O00OO00O =OOOOOOOOOOO0OO0OO ['data'][0 ]['join_number']#line:1138
                    O00O00OOOOO0O0O00 =int (float (OOOOOOOOOOO0OO0OO ['data'][0 ]['totalValue']))#line:1139
                    O0O0O0OOO0O0OO000 =float (OO0O0O0O000O0OOO0 /O00O00OOOOO0O0O00 )*10000 #line:1140
                    OOO000OOO00O00O00 =O00O00OOOOO0O0O00 /OO00O0OO0O00OO00O #line:1141
                    print (f'【参与抽奖】:预计每天中{str(O0O0OOOO00O000OOO)[:6]}颗金种子丨好友收益:{str(O00O0OOO0OOO0OOO0)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0O0OOO0O0OO000)[:6]}颗金种子丨☘️人均:{str(OOO000OOO00O00O00)[:7]}️')#line:1143
        except Exception as O00OO00O000O00O0O :#line:1144
            print (O00OO00O000O00O0O )#line:1145
    def energy (OO0O0O00O0000OO0O ):#line:1148
        try :#line:1149
            while True :#line:1150
                OOO0OO0O00OO0O00O =f'__{timi_new()}'#line:1151
                OOOO0OO0O0OOOOOOO ={'source':'scsc','authorization':OO0O0O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O00OO0O00O ),'signstring':OOO0OO0O00OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                O0OO0O0OO0O0OOOOO =requests .request ('get',f'{host}/energy/general',headers =OOOO0OO0O0OOOOOOO ).json ()#line:1163
                if 'status'in O0OO0O0OO0O0OOOOO :#line:1165
                    if O0OO0O0OO0O0OOOOO ['status']==200 :#line:1166
                        OO00OO0000O00OO0O =O0OO0O0OO0O0OOOOO ['data']['ordinary_water']#line:1167
                        OO0O00000OO00O0O0 =O0OO0O0OO0O0OOOOO ['data']['ordinary_fertilizer']#line:1168
                        O0OO0O0O00000O0OO =O0OO0O0OO0O0OOOOO ['data']['videoStatus']#line:1169
                        OOOOO000OOOO000O0 =O0OO0O0OO0O0OOOOO ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(OO0O00000OO00O0O0).split(".")[0]}丨水滴:{str(OO00OO0000O00OO0O).split(".")[0]}')#line:1172
                        if float (OO0O00000OO00O0O0 )<96 :#line:1173
                            if O0OO0O0O00000O0OO :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                O0OO00OO0OOO00O0O =99 -float (OO0O00000OO00O0O0 )#line:1176
                                O00O00OO0O0O0O000 ={"fertilizer":str (O0OO00OO0OOO00O0O ).split ('.')[0 ]}#line:1177
                                O000O0O0OO0OOOO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO0OO0O0OOOOOOO ).json ()#line:1179
                                if 'status'in O000O0O0OO0OOOO0O :#line:1181
                                    if O000O0O0OO0OOOO0O ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O0OO0OOOO0O["message"]}')#line:1183
                                    if O000O0O0OO0OOOO0O ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O0OO0OOOO0O["message"]}')#line:1185
                                        break #line:1186
                                if float (OO0O00000OO00O0O0 )<78 :#line:1188
                                    O0OO00OO0OOO00O0O =80 -float (OO0O00000OO00O0O0 )#line:1189
                                    OO0O0OOOOO0O0OO0O =f'_fertilizer={int(O0OO00OO0OOO00O0O)}_{timi_new()}'#line:1190
                                    O00000O0O0OO0OOO0 ={'source':'scsc','authorization':OO0O0O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOO0O0OO0O ),'signstring':OO0O0OOOOO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    OO000OOO0O000OOO0 ={"fertilizer":int (O0OO00OO0OOO00O0O )}#line:1202
                                    O0O0OO000O0OOOOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00000O0O0OO0OOO0 ,data =OO000OOO0O000OOO0 ).json ()#line:1204
                                    if 'status'in O0O0OO000O0OOOOOO :#line:1206
                                        if O0O0OO000O0OOOOOO ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O0O0OO000O0OOOOOO["message"]}丨数量:{int(O0OO00OO0OOO00O0O)}')#line:1208
                                        if O0O0OO000O0OOOOOO ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{O0O0OO000O0OOOOOO["message"]}丨数量:{int(O0OO00OO0OOO00O0O)}')#line:1210
                                            OO0O0000000OOOOO0 =O0O0OO000O0OOOOOO ["message"].split ('-')[1 ]#line:1211
                                            O000OO0OOO000OO00 =f'__{timi_new()}'#line:1212
                                            O0O000OO00O0O0000 ={'source':'scsc','authorization':OO0O0O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OOO000OO00 ),'signstring':O000OO0OOO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            OO0OOOOOOO0O00OO0 =requests .request ('get',f'{host}/user',headers =O0O000OO00O0O0000 ).json ()#line:1224
                                            if 'status'in OO0OOOOOOO0O00OO0 :#line:1225
                                                if OO0OOOOOOO0O00OO0 ['status']==200 :#line:1226
                                                    OO0O00OOO0O0O0000 =OO0OOOOOOO0O00OO0 ['data']['inner_id']#line:1227
                                                    if give_gold (OO0O00OOO0O0O0000 ,float (OO0O0000000OOOOO0 )+1 ):#line:1228
                                                        OO0O0O00O0000OO0O .energy ()#line:1229
                        if float (OO00OO0000O00OO0O )<880 :#line:1230
                            if OOOOO000OOOO000O0 :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                O0OOOO000O000000O =999 -float (OO00OO0000O00OO0O )#line:1233
                                OO0O0OO0O0O00OOOO ={"water":str (O0OOOO000O000000O ).split ('.')[0 ]}#line:1234
                                OO0000OO00OO0O0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO0OO0O0OOOOOOO ).json ()#line:1236
                                if 'status'in OO0000OO00OO0O0O0 :#line:1238
                                    if OO0000OO00OO0O0O0 ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OO0000OO00OO0O0O0["message"]}')#line:1240
                                    if OO0000OO00OO0O0O0 ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{OO0000OO00OO0O0O0["message"]}')#line:1242
                                        break #line:1243
                                if float (OO00OO0000O00OO0O )<780 :#line:1244
                                    O0OOOO000O000000O =800 -float (OO00OO0000O00OO0O )#line:1245
                                    OO000OOO0O0O00OOO =f'_water={int(O0OOOO000O000000O)}_{timi_new()}'#line:1246
                                    OO0OOOO00O00OO0OO ={'source':'scsc','authorization':OO0O0O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0O0O00OOO ),'signstring':OO000OOO0O0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    O0O00O0OO0OOOOOO0 ={"water":int (O0OOOO000O000000O )}#line:1258
                                    OOO00OO0OOOOOO000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OOOO00O00OO0OO ,data =O0O00O0OO0OOOOOO0 ).json ()#line:1260
                                    if 'status'in OOO00OO0OOOOOO000 :#line:1262
                                        if OOO00OO0OOOOOO000 ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{OOO00OO0OOOOOO000["message"]}丨数量:{int(O0OOOO000O000000O)}')#line:1264
                                        if OOO00OO0OOOOOO000 ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{OOO00OO0OOOOOO000["message"]}丨数量:{int(O0OOOO000O000000O)}')#line:1266
                                            OO0O0000000OOOOO0 =OOO00OO0OOOOOO000 ["message"].split ('-')[1 ]#line:1267
                                            O000OO0OOO000OO00 =f'__{timi_new()}'#line:1268
                                            O0O000OO00O0O0000 ={'source':'scsc','authorization':OO0O0O00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0OOO000OO00 ),'signstring':O000OO0OOO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            OO0OOOOOOO0O00OO0 =requests .request ('get',f'{host}/user',headers =O0O000OO00O0O0000 ).json ()#line:1280
                                            if 'status'in OO0OOOOOOO0O00OO0 :#line:1281
                                                if OO0OOOOOOO0O00OO0 ['status']==200 :#line:1282
                                                    OO0O00OOO0O0O0000 =OO0OOOOOOO0O00OO0 ['data']['inner_id']#line:1283
                                                    if give_gold (OO0O00OOO0O0O0000 ,float (OO0O0000000OOOOO0 )+1 ):#line:1284
                                                        OO0O0O00O0000OO0O .energy ()#line:1285
                        break #line:1286
        except Exception as O0O0O000000OOO00O :#line:1287
            print (O0O0O000000OOO00O )#line:1288
def bundled_def ():#line:1291
    O0O0OO000OOOOOO0O =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return O0O0OO000OOOOOO0O [random .randint (0 ,len (O0O0OO000OOOOOO0O )-1 )]#line:1293
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
        O0OOOOO00O00O00OO =gitee_edition ()#line:1332
        if version_of_the_validation ()<O0OOOOO00O00O00OO ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOO00O00O00OO["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{O0OOOOO00O00O00OO["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOO00O00O00OO["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {O0OOOOO00O00O00OO["CityEarth"]["content"]}')#line:1338
    except Exception as OO0OO0O0O0OOO00OO :#line:1339
        print (OO0OO0O0O0OOO00OO )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
