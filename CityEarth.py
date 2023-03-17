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
        O0O00000O000OO00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O0O00000O000OO00O)}个账号==========")#line:16
        for OO0OOO00O0O0OOO0O in O0O00000O000OO00O :#line:17
            O0OOO0OOO000OO0O0 =[]#line:18
            print (f"------------正在执行第{O0O00000O000OO00O.index(OO0OOO00O0O0OOO0O) + 1}个账号------------")#line:19
            OOOO0O00OO0000OO0 =CityEarth (OO0OOO00O0O0OOO0O ,O0OOO0OOO000OO0O0 ,O0O00000O000OO00O .index (OO0OOO00O0O0OOO0O ))#line:20
            def O0000O0O000O00000 ():#line:22
                if OOOO0O00OO0000OO0 .base_info ():#line:24
                    OOOO0O00OO0000OO0 .sealing ()#line:26
                    OOOO0O00OO0000OO0 .invitenum ()#line:28
                    OOOO0O00OO0000OO0 .query_to_sell ()#line:30
                    OOOO0O00OO0000OO0 .game_map ()#line:32
                    OOOO0O00OO0000OO0 .ddd ()#line:34
                    OOOO0O00OO0000OO0 .friends_invitation ()#line:36
                    OOOO0O00OO0000OO0 .energy ()#line:38
                    OOOO0O00OO0000OO0 .add_clover ()#line:40
                    OOOO0O00OO0000OO0 .propsraffle ()#line:42
                    OOOO0O00OO0000OO0 .synthetic ()#line:44
                    OOOO0O00OO0000OO0 .crops_illustrated ()#line:46
                    OOOO0O00OO0000OO0 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OOOO0O00OO0000OO0 .give_gold ()#line:51
            O0OOOO0OOOOOOO0O0 =threading .Thread (target =O0000O0O000O00000 )#line:53
            O0OOOO0OOOOOOO0O0 .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        OO0OO0OO0OO0O00OO =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0OO0OO0OO0O00OO +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO0OOOO00O000OO00 in invited_new :#line:62
            print (OO0OOOO00O000OO00 )#line:63
        print ('开始打印未实名的token')#line:64
        for O0000OO00OOO0O0OO in weishim :#line:65
            print (O0000OO00OOO0O0OO )#line:66
    except Exception as OO00000O00O00OOO0 :#line:67
        print (OO00000O00O00OOO0 )#line:68
def give_gold (O00OOO000O000O0OO ,O00000O00O0OO00OO ):#line:72
    try :#line:73
        O00O00000OOO000O0 =f'_doneeNo={O00OOO000O000O0OO}&quantity={int(O00000O00O0OO00OO)}_{timi_new()}'#line:74
        OOO0O00O0OO0O0OO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00O00000OOO000O0 ),'signstring':O00O00000OOO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO0O0OOO0O0OOOO00 ={"quantity":int (O00000O00O0OO00OO ),"doneeNo":O00OOO000O000O0OO }#line:89
        OO0000O0O0O00O00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O00O0OO0O0OO0 ,data =OO0O0OOO0O0OOOO00 ).json ()#line:90
        if 'status'in OO0000O0O0O00O00O :#line:92
            if OO0000O0O0O00O00O ['status']==200 :#line:93
                if OO0000O0O0O00O00O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00000O00O0OO00OO)}种子给{O00OOO000O000O0OO}成功')#line:95
                    return True #line:96
            if OO0000O0O0O00O00O ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0000O0O0O00O00O["message"]}')#line:98
                return False #line:99
            if OO0000O0O0O00O00O ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0000O0O0O00O00O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0000O00O0O0OOO00 :#line:104
        print (O0000O00O0O0OOO00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0OO0O0O000OO0OO ):#line:115
    O00O0O0O000OOO0O0 =hashlib .md5 (OO0OO0O0O000OO0OO .encode ()).hexdigest ()#line:116
    OO00OO00O00O0OOO0 =sc1 ()#line:117
    O00OOOOO0O0OOO0OO =sc2 ()#line:118
    O0OO0OO000OOO000O =sc3 ()#line:119
    O0O00OOO00O0000OO =OO00OO00O00O0OOO0 +O00O0O0O000OOO0O0 +O00OOOOO0O0OOO0OO +O0OO0OO000OOO000O #line:120
    OO0O0O00OOO000000 =hashlib .md5 (O0O00OOO00O0000OO .encode ()).hexdigest ()#line:121
    return OO0O0O00OOO000000 #line:122
def format_msg ():#line:125
    OOO0O00OO0O000000 =""#line:126
    for O00000OOO0OO0OO00 in msg_list :#line:127
        OOO0O00OO0O000000 +=str (O00000OOO0OO0OO00 )+"\r\n"#line:128
    return OOO0O00OO0O000000 #line:129
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
def get_json_data (OO0OOO00000OO000O ,OO0O0OOOOO00O0OO0 ,O0OOOO0O000O0O000 ,OO0000O00O0OO0OOO ):#line:153
    with open (OO0OOO00000OO000O ,'rb')as O0O0O0OO000O000O0 :#line:154
        O0OOOO0OO0O00000O =json .load (O0O0O0OO000O000O0 )#line:155
        O0OOOO0OO0O00000O ['data'][OO0O0OOOOO00O0OO0 ][O0OOOO0O000O0O000 ]=OO0000O00O0OO0OOO #line:156
        OOOO0O000O00O00OO =O0OOOO0OO0O00000O #line:157
    O0O0O0OO000O000O0 .close ()#line:158
    return OOOO0O000O00O00OO #line:159
def write_json_data (OO00OO0O000O0OO00 ):#line:162
    with open (json_path1 ,'w')as OO0O00OOOO000O000 :#line:163
        json .dump (OO00OO0O000O0OO00 ,OO0O00OOOO000O000 )#line:164
    OO0O00OOOO000O000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OOOOOO0OO0OOOOO ,OO0OO0OO0OO0O0O00 ,OOOO00OOO0OOOO0O0 ,O0OOO0OOOO000OO0O ):#line:171
        try :#line:172
            O0OOOOOO0OO0OOOOO .msg =OOOO00OOO0OOOO0O0 #line:173
            O0OOOOOO0OO0OOOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OOOOOO0OO0OOOOO .token =OO0OO0OO0OO0O0O00 ['authorization']#line:175
            O0OOOOOO0OO0OOOOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OOOOOO0OO0OOOOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OOOOOO0OO0OOOOO .elephant_user =OO0OO0OO0OO0O0O00 ['elephant_user']#line:178
            O0OOOOOO0OO0OOOOO .elephant_pswd =OO0OO0OO0OO0O0O00 ['elephant_pswd']#line:179
            O0OOOOOO0OO0OOOOO .elephant_Task_ID =OO0OO0OO0OO0O0O00 ['elephant_Task_ID']#line:180
            O0OOOOOO0OO0OOOOO .len_new =O0OOO0OOOO000OO0O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O00OOO000OO000OO0 ):#line:186
        try :#line:187
            O00OOO000OO000OO0 .watched_ad ()#line:189
            O00000OO00O000OO0 =f'__{timi_new()}'#line:190
            O0OOOOO0O0000OO00 ={'source':'scsc','authorization':O00OOO000OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO00O000OO0 ),'signstring':O00000OO00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00OOOOO00O00OO0O =requests .request ('get',f'{host}/user',headers =O0OOOOO0O0000OO00 ).json ()#line:202
            if 'status'in O00OOOOO00O00OO0O :#line:204
                if O00OOOOO00O00OO0O ['status']==200 :#line:205
                    O000O0O0O00000000 =O00OOOOO00O00OO0O ['data']['nickname']#line:206
                    OOO00OOO0O0O000O0 =O00OOOOO00O00OO0O ['data']['inner_id']#line:207
                    O0O0OOO00O000OO00 =O00OOOOO00O00OO0O ['data']['assets']['gold']#line:208
                    O0OO0OO00000000O0 =O00OOOOO00O00OO0O ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O000O0O0O00000000[:5]}丨ID:{OOO00OOO0O0O000O0}丨等级:{O0OO0OO00000000O0}丨金种子:{str(O0O0OOO00O000OO00).split(".")[0]}')#line:211
                    if 'wx_'in O000O0O0O00000000 :#line:212
                        O00OOO000OO000OO0 .change_nickname ()#line:213
                if O00OOOOO00O00OO0O ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O00OOO000OO000OO0 .elephant_user =='f':#line:216
                        return False #line:217
                    O0O00O00O0000OO0O =Invalid_login .addtask (elephant_user =O00OOO000OO000OO0 .elephant_user ,elephant_pswd =O00OOO000OO000OO0 .elephant_pswd ,elephant_Task_ID =O00OOO000OO000OO0 .elephant_Task_ID )#line:220
                    O00OOOO0O0O000000 =get_json_data (json_path ,O00OOO000OO000OO0 .len_new ,'authorization',O0O00O00O0000OO0O )#line:221
                    if write_json_data (O00OOOO0O0O000000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00OOOOO00O00OO0O ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOOOO0O0O0O0O00OO :#line:228
            print (OOOOO0O0O0O0O00OO )#line:229
    def sealing (O0OOO0OO0O00OO00O ):#line:232
        try :#line:233
            OO00O0OO00OO000O0 =f'__{timi_new()}'#line:234
            O0OOOOOOO000OO000 ={'source':'scsc','authorization':O0OOO0OO0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO00OO000O0 ),'signstring':OO00O0OO00OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOOOOOO000OO000 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OOOOOOO000OO000 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOOOOOO000OO000 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOOOOOO000OO000 )#line:249
            requests .request ('get',f'{host}/user',headers =O0OOOOOOO000OO000 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOOOOOO000OO000 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOOOOOO000OO000 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOOOOOO000OO000 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOOOOOO000OO000 )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OOOOOOO000OO000 )#line:255
        except Exception as O0OOOOOO0O00O0000 :#line:256
            print (O0OOOOOO0O00O0000 )#line:257
    def ddd (O000OO000000O0OOO ):#line:259
        try :#line:260
            OO00OO0O00000O000 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO0OO0O00OOO0O0O0 ={'source':'scsc','authorization':O000OO000000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O00000O000 ),'signstring':OO00OO0O00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O00O0O0000O0000O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OO0O00OOO0O0O0 ).json ()#line:273
            print (O00O0O0000O0000O0 )#line:274
        except Exception as OOO0O0O0O0OO0OOO0 :#line:279
            print (OOO0O0O0O0OO0OOO0 )#line:280
    def the_query (OOO0OO0OOOOOO00OO ):#line:290
        try :#line:291
            OOO00O0OOO00OO0O0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            O00OO0O0O0O00O0O0 ={'authorization':OOO0OO0OOOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOO00OO0O0 ),'signstring':OOO00O0OOO00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            OO0000O0O0OOOO00O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00OO0O0O0O00O0O0 ).json ()#line:304
            if 'status'in OO0000O0O0OOOO00O :#line:306
                if OO0000O0O0OOOO00O ['status']==200 :#line:307
                    O00O00000000OOOO0 =OO0000O0O0OOOO00O ['data']['rows'][3 ]['price']#line:308
                    OOO0OO0OOOOOO00OO .market_sale (O00O00000000OOOO0 )#line:309
        except Exception as O0000O00O0OOOOO0O :#line:310
            print (O0000O00O0OOOOO0O )#line:311
    def market_sale (O0000O0000O0OO0OO ,OOO00O000O0O000OO ):#line:314
        try :#line:315
            O0OOOOOOO0OO000O0 =timi_new ()#line:316
            OO0OOO0O00OO0O000 =f'type=crop__{O0OOOOOOO0OO000O0}'#line:317
            OO00OOOO00O0O0OOO ={'source':'scsc','authorization':O0000O0000O0OO0OO .token ,'timestamp':str (O0OOOOOOO0OO000O0 ),'sign':sign (OO0OOO0O00OO0O000 ),'signstring':OO0OOO0O00OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O0O000OOOOO0000O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00OOOO00O0O0OOO ).json ()#line:330
            if 'status'in O0O000OOOOO0000O0 :#line:332
                if O0O000OOOOO0000O0 ['status']==200 :#line:333
                    if O0O000OOOOO0000O0 ['data']['rows']:#line:334
                        O0OO000O0000O00O0 =O0O000OOOOO0000O0 ['data']['rows'][0 ]['packsackItemId']#line:335
                        O0O0OO000O00O0000 =O0O000OOOOO0000O0 ['data']['rows'][0 ]['quantity']#line:336
                        OOOOOOOO000O0O0O0 =float (OOO00O000O0O000OO )-0.00001 #line:337
                        if OOOOOOOO000O0O0O0 >8 :#line:338
                            O000000OO0000OOO0 =f'_packsackItemId={O0OO000O0000O00O0}&price={str(OOOOOOOO000O0O0O0)[:9]}&quantity={O0O0OO000O00O0000}_{O0OOOOOOO0OO000O0}'#line:339
                            O0O0OOOO00O00O000 ={'source':'scsc','authorization':O0000O0000O0OO0OO .token ,'timestamp':str (O0OOOOOOO0OO000O0 ),'sign':sign (O000000OO0000OOO0 ),'signstring':O000000OO0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            OO0000OOOOO0O00O0 ={"packsackItemId":O0OO000O0000O00O0 ,"price":str (OOOOOOOO000O0O0O0 )[:9 ],"quantity":str (O0O0OO000O00O0000 )}#line:355
                            O00O0OOOOOOOO00OO =requests .request ('post',f'{host}/market/sale',headers =O0O0OOOO00O00O000 ,data =OO0000OOOOO0O00O0 ).json ()#line:356
                            if 'status'in O00O0OOOOOOOO00OO :#line:358
                                if O00O0OOOOOOOO00OO ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{O0O0OO000O00O0000}丨价格:{str(OOOOOOOO000O0O0O0)[:9]}')#line:360
        except Exception as OO000OOO0OOOO000O :#line:361
            print (OO000OOO0OOOO000O )#line:362
    def query_to_sell (OOO0O00O0O00OO0O0 ):#line:365
        try :#line:366
            O00OO0OO00O0O000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            OO0O000000O0OOO0O ={'source':'scsc','authorization':OOO0O00O0O00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO00O0O000O ),'signstring':O00OO0OO00O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            OOOO0O00OO00OO00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0O000000O0OOO0O ).json ()#line:380
            if 'status'in OOOO0O00OO00OO00O :#line:382
                if OOOO0O00OO00OO00O ['status']==200 :#line:383
                    for OO000OO0O00O00O0O in OOOO0O00OO00OO00O ['data']['rows']:#line:384
                        OOO00O0O000OOOOO0 =OO000OO0O00O00O0O ['materialKey']#line:385
                        O0O0OO00O00O00O00 =OO000OO0O00O00O0O ['quantity']#line:386
                        OO00OO00O00O00000 =OO000OO0O00O00O0O ['price']#line:387
                        O0000000O00000OOO =OO000OO0O00O00O0O ['saleState']#line:388
                        if O0000000O00000OOO ==0 :#line:389
                            print (f'【出售订单】:名称:{OOO00O0O000OOOOO0}丨数量:{O0O0OO00O00O00O00}丨价格:{OO00OO00O00O00000}')#line:390
                            OO0O00OO0O0000O00 =OO000OO0O00O00O0O ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                OOO0O00O0O00OO0O0 .cacel_sale (OO0O00OO0O0000O00 )#line:393
        except Exception as O0O00000O0O0000OO :#line:394
            print (O0O00000O0O0000OO )#line:395
    def cacel_sale (O00OOO0O00O00O0O0 ,O00OOO0000000O0O0 ):#line:398
        try :#line:399
            O000000O0O00OOOOO =f'_saleId={O00OOO0000000O0O0}_{timi_new()}'#line:400
            OO000OO0OO0O0O0O0 ={'source':'scsc','authorization':O00OOO0O00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0O00OOOOO ),'signstring':O000000O0O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O0OO0O0O000000O00 ={"saleId":O00OOO0000000O0O0 }#line:414
            O00OOO0OOOOOOOO0O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO000OO0OO0O0O0O0 ,data =O0OO0O0O000000O00 ).json ()#line:415
            if 'status'in O00OOO0OOOOOOOO0O :#line:417
                if O00OOO0OOOOOOOO0O ['status']==200 :#line:418
                    print (f'【下架出售】:{O00OOO0OOOOOOOO0O["data"]}')#line:419
        except Exception as O0O00O000O000O0O0 :#line:420
            print (O0O00O000O000O0O0 )#line:421
    def change_nickname (OOO0OOO0000O00OO0 ):#line:424
        try :#line:425
            OO00OO000O0OOO0OO =timi_new ()#line:426
            O00O00000O00O000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOO0O0O0OOOOO00OO =requests .request ('post','https://www.qmsjmfb.com/',data =O00O00000O00O000O ).text #line:428
            OO0OO000OOO0O00O0 =re .findall ('<ul><li>(.*?)</li>',OOO0O0O0OOOOO00OO )[0 ][:3 ]#line:429
            OOOO0000OOOO0O000 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0OO000OOO0O00O0}').json ()#line:430
            O00O00OO0OO0O0000 =OOOO0000OOOO0O000 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            O0OO0O0OO0O0OOOO0 ={"nickname":O00O00OO0OO0O0000 }#line:432
            O00000OOOOO000000 =f'_nickname={O00O00OO0OO0O0000}_{OO00OO000O0OOO0OO}'#line:433
            O00OOOOO0O00OOO00 ={'source':'scsc','authorization':OOO0OOO0000O00OO0 .token ,'timestamp':OO00OO000O0OOO0OO ,'sign':sign (O00000OOOOO000000 ),'signstring':O00000OOOOO000000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            O000000O00O0OOO00 =requests .request ('patch',f'{host}/user/nickname',headers =O00OOOOO0O00OOO00 ,data =O0OO0O0OO0O0OOOO0 ).json ()#line:445
            if 'status'in O000000O00O0OOO00 :#line:447
                if O000000O00O0OOO00 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O00O00OO0OO0O0000}丨{O000000O00O0OOO00["message"]}')#line:449
        except Exception as O0OO00OOO0000OO00 :#line:450
            print (O0OO00OOO0000OO00 )#line:451
    def withdraw (O00OOO0O0O0O0OO00 ):#line:454
        try :#line:455
            O0O000OOO00OO0O00 =f'__{timi_new()}'#line:456
            OOOOOOO00O0OOOO00 ={'source':'scsc','authorization':O00OOO0O0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO00OO0O00 ),'signstring':O0O000OOO00OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OOO0O0OOO00OOOO0O =requests .request ('get',f'{host}/assets',headers =OOOOOOO00O0OOOO00 ).json ()#line:468
            if 'status'in OOO0O0OOO00OOOO0O :#line:470
                if OOO0O0OOO00OOOO0O ['status']==200 :#line:471
                    O00OO0OOOOO0OOO0O =OOO0O0OOO00OOOO0O ['data']['cash']#line:472
                    if float (O00OO0OOOOO0OOO0O )>20 :#line:473
                        O0O000OOO00OO0O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        OOOOOOO00O0OOOO00 ={'authorization':O00OOO0O0O0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO00OO0O00 ),'signstring':O0O000OOO00OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OOOOO0O00OOOO00OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OO00O0OOOOOO0000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOOOOO00O0OOOO00 ,data =OOOOO0O00OOOO00OO ).json ()#line:487
                        if 'status'in OO00O0OOOOOO0000O :#line:489
                            if OO00O0OOOOOO0000O ['status']==200 :#line:490
                                print (f'【余额提现】:{OO00O0OOOOOO0000O["data"]}')#line:491
                        if 'status'in OO00O0OOOOOO0000O :#line:492
                            if OO00O0OOOOOO0000O ['status']==500 :#line:493
                                print (f'【余额提现】:{OO00O0OOOOOO0000O["message"]}')#line:494
        except Exception as O00O0OOOO0O0OO0OO :#line:495
            print (O00O0OOOO0O0OO0OO )#line:496
    def invitenum (OOO00O0O00OOO000O ):#line:499
        global invited_new #line:500
        try :#line:501
            O00O0OOO0OOO00O00 =f'__{timi_new()}'#line:502
            OOO0O0O0OOO00000O ={'source':'scsc','authorization':OOO00O0O00OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OOO00O00 ),'signstring':O00O0OOO0OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            O0OO00OO0O0000O0O =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0O0O0OOO00000O ).json ()#line:514
            if 'status'in O0OO00OO0O0000O0O :#line:516
                if O0OO00OO0O0000O0O ['status']==200 :#line:517
                    OOO000O0O00OOOOOO =O0OO00OO0O0000O0O ['data']['invited_count']#line:518
                    OOOO00O0000OO0O00 =O0OO00OO0O0000O0O ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OOO000O0O00OOOOOO}丨间邀好友:{OOOO00O0000OO0O00}')#line:520
                    if OOO000O0O00OOOOOO <2 :#line:521
                        O0O0O00O00OO0O000 =f'__{timi_new()}'#line:522
                        OO0OOOOOO0000O0O0 ={'source':'scsc','authorization':OOO00O0O00OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O00OO0O000 ),'signstring':O0O0O00O00OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O0OOOO000OO0OO0OO =requests .request ('get',f'{host}/user',headers =OO0OOOOOO0000O0O0 ).json ()#line:534
                        if 'status'in O0OOOO000OO0OO0OO :#line:536
                            if O0OOOO000OO0OO0OO ['status']==200 :#line:537
                                invited_new .append (O0OOOO000OO0OO0OO ['data']['inner_id'])#line:538
        except Exception as O0OOO0O0OO00O00O0 :#line:539
            print (O0OOO0O0OO00O00O0 )#line:540
    def game_map (OO00O0O0OO0O0OO00 ):#line:543
        try :#line:544
            OOOOO000OOO000000 =f'__{timi_new()}'#line:545
            OO0OO0000OOOOO000 ={'source':'scsc','authorization':OO00O0O0OO0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000OOO000000 ),'signstring':OOOOO000OOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            OOO00O00O00O000O0 =requests .request ('get',f'{host}/game/map',headers =OO0OO0000OOOOO000 ).json ()#line:557
            if 'status'in OOO00O00O00O000O0 :#line:559
                if OOO00O00O00O000O0 ['status']==200 :#line:560
                    for OOO0O000O0O0O00O0 in OOO00O00O00O000O0 ['data']['list'][0 ]['crops']:#line:561
                        OO00OOO00O0O0000O =OOO0O000O0O0O00O0 ['level']#line:563
                        if OO00OOO00O0O0000O ==41 :#line:564
                            OO00OOOOOOO0OOOOO =OOO0O000O0O0O00O0 ['crop_name']#line:565
                            O0O0000OOO0OO00OO =OOO0O000O0O0O00O0 ['count']#line:566
                            if O0O0000OOO0OO00OO >0 :#line:567
                                print (f'【农业资产】:{OO00OOOOOOO0OOOOO}丨数量:{O0O0000OOO0OO00OO}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    OO00O0O0OO0O0OO00 .the_query ()#line:570
        except Exception as O0000OOO00O0OO0O0 :#line:571
            print (O0000OOO00O0OO0O0 )#line:572
    def give_gold (O0OOOOO0OOOO0000O ):#line:575
        try :#line:576
            OO00OO00OOOOO0O00 =f'__{timi_new()}'#line:577
            OOOOOO0O0O0O0OOO0 ={'source':'scsc','authorization':O0OOOOO0OOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OOOOO0O00 ),'signstring':OO00OO00OOOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            O000OOOOO00O00OO0 =requests .request ('get',f'{host}/user',headers =OOOOOO0O0O0O0OOO0 ).json ()#line:589
            if 'status'in O000OOOOO00O00OO0 :#line:590
                if O000OOOOO00O00OO0 ['status']==200 :#line:591
                    if float (O0OOOOO0OOOO0000O .doneeNo )!=0 :#line:592
                        O00OO000OO000O00O =O000OOOOO00O00OO0 ['data']['assets']['gold']#line:593
                        if float (O00OO000OO000O00O )>float (O0OOOOO0OOOO0000O .innerId ):#line:594
                            O0O0OOO0000OOOOOO =int (float (O00OO000OO000O00O )/1.1 )#line:595
                            OO00OO00OOOOO0O00 =f'_doneeNo={O0OOOOO0OOOO0000O.doneeNo}&quantity={O0O0OOO0000OOOOOO}_{timi_new()}'#line:596
                            OOOOOO0O0O0O0OOO0 ={'source':'scsc','authorization':O0OOOOO0OOOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00OOOOO0O00 ),'signstring':OO00OO00OOOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            OOOOOOOO0000000O0 ={"quantity":O0O0OOO0000OOOOOO ,"doneeNo":O0OOOOO0OOOO0000O .doneeNo }#line:611
                            O00OOO0OO0O00O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOO0O0O0O0OOO0 ,data =OOOOOOOO0000000O0 ).json ()#line:612
                            if 'status'in O00OOO0OO0O00O000 :#line:614
                                if O00OOO0OO0O00O000 ['status']==200 :#line:615
                                    if O00OOO0OO0O00O000 ['data']:#line:616
                                        print (f'【赠送种子】:赠送{O0O0OOO0000OOOOOO}种子给{O0OOOOO0OOOO0000O.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as O0O00OO0O000OOOOO :#line:620
            print (O0O00OO0O000OOOOO )#line:621
    def invitation (OO0O00OOO000OOOOO ):#line:623
        try :#line:624
            _OOO0000O00OOOO0OO =float (bundled_def ())/4 #line:625
            OO0O0O0OO000OO000 =f'_innerId={int(_OOO0000O00OOOO0OO)}_{timi_new()}'#line:626
            OO0O00O0OOOO000OO ={'source':'scsc','authorization':OO0O00OOO000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO000OO000 ),'signstring':OO0O0O0OO000OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            OO0O0O00OO00O0OOO ={"innerId":int (_OOO0000O00OOOO0OO )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0O00O0OOOO000OO ,data =OO0O0O00OO00O0OOO )#line:639
        except Exception as O00O000OOOOOO0OOO :#line:640
            print (O00O000OOOOOO0OOO )#line:641
    def winning_rewards (O0OO0OOOO000OO0O0 ):#line:644
        try :#line:645
            OO0000OO0O000OOOO =f'__{timi_new()}'#line:646
            OOOOOO00O0O0OOOO0 ={'source':'scsc','authorization':O0OO0OOOO000OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO0O000OOOO ),'signstring':OO0000OO0O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O0OOOO0OO0O0O0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOOO00O0O0OOOO0 ).json ()#line:658
            if 'status'in O0OOOO0OO0O0O0000 :#line:660
                if O0OOOO0OO0O0O0000 ['status']==200 :#line:661
                    if O0OOOO0OO0O0O0000 ['data']['amount']:#line:662
                        O00OO00O0O00OO000 =O0OOOO0OO0O0O0000 ['data']['amount']['gold']#line:663
                        return O00OO00O0O00OO000 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as OOO0O00O0O00O0O00 :#line:667
            print (OOO0O00O0O00O0O00 )#line:668
    def certification (OOO0OOOOOO0O00OOO ):#line:671
        try :#line:672
            O00OOOOOO000OO0O0 =f'__{timi_new()}'#line:673
            O0OO0O0OOO0O0OOOO ={'source':'scsc','authorization':OOO0OOOOOO0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO000OO0O0 ),'signstring':O00OOOOOO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            OOOO0O0000OOOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0O0OOO0O0OOOO ).json ()#line:685
            if 'status'in OOOO0O0000OOOOO00 :#line:687
                if OOOO0O0000OOOOO00 ['status']==200 :#line:688
                    if OOOO0O0000OOOOO00 ['data']['result']:#line:689
                        OOO0000O0O000OOO0 =OOOO0O0000OOOOO00 ['data']['nick_name']#line:690
                        return OOO0000O0O000OOO0 #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as O00O0OOO0O0O0OOOO :#line:694
            print (O00O0OOO0O0O0OOOO )#line:695
    def crops_illustrated (O0000O0OOOO00O0OO ):#line:698
        try :#line:699
            OOO0O0O0OO00O0O0O =f'__{timi_new()}'#line:700
            O0O0O00O00000O0O0 ={'source':'scsc','authorization':O0000O0OOOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO00O0O0O ),'signstring':OOO0O0O0OO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            O0O00O0OO000O0OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O00O00000O0O0 ).json ()#line:712
            if 'status'in O0O00O0OO000O0OOO :#line:714
                if O0O00O0OO000O0OOO ['status']==200 :#line:715
                    OOOOO0000OOO00000 =O0O00O0OO000O0OOO ['data'][0 ]['crops']#line:716
                    for O0OO0OO00O000000O in OOOOO0000OOO00000 :#line:717
                        if O0OO0OO00O000000O ['ill_clover_award']:#line:718
                            if float (O0OO0OO00O000000O ['ill_clover_award'])>1 :#line:719
                                if O0OO0OO00O000000O ['is_finish']:#line:720
                                    if not O0OO0OO00O000000O ['is_getit']:#line:721
                                        if O0000O0OOOO00O0OO .certification ()!='未实名':#line:722
                                            OOO0O0O0OO00O0O0O =f'_award_level={O0OO0OO00O000000O["level"]}_{timi_new()}'#line:723
                                            O0O0O00O00000O0O0 ={'source':'scsc','authorization':O0000O0OOOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO00O0O0O ),'signstring':OOO0O0O0OO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            O000OO0OO0O0OO000 ={"award_level":O0OO0OO00O000000O ['level']}#line:735
                                            OO0O000O00OOO000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O00O00000O0O0 ,json =O000OO0OO0O0OO000 ).json ()#line:737
                                            if 'status'in OO0O000O00OOO000O :#line:738
                                                if OO0O000O00OOO000O ['status']==200 :#line:739
                                                    O0OO00OO00000OOOO =OO0O000O00OOO000O ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{O0OO0OO00O000000O["crop_name"]}成就丨奖励{O0OO00OO00000OOOO}☘️')#line:742
                                                if OO0O000O00OOO000O ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{OO0O000O00OOO000O["message"]}')#line:744
        except Exception as OOO0O000OOOOO0OO0 :#line:745
            print (OOO0O000OOOOO0OO0 )#line:746
    def watched_ad (O0000000OOOOOOO00 ):#line:749
        try :#line:750
            OOOOO00O000O00O00 =f'__{timi_new()}'#line:751
            OOO000OOOO0OOO0O0 ={'source':'scsc','authorization':O0000000OOOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O00O00 ),'signstring':OOOOO00O000O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            OOOOOO0OOO0OOOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOOO0OOO0O0 ).json ()#line:763
            if 'status'in OOOOOO0OOO0OOOO0O :#line:765
                if OOOOOO0OOO0OOOO0O ['status']==200 :#line:766
                    if 'offlineInfo'in OOOOOO0OOO0OOOO0O ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        OO0OO00OO0O000OOO =OOOOOO0OOO0OOOO0O ['data']['offlineInfo']['off_minute']#line:769
                        OOO000O0000OO00O0 =float (OOOOOO0OOO0OOOO0O ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OOOO0OOO0O0 ).json ()#line:772
                        time .sleep (2 )#line:773
                        O00OO0O0OO000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OOOO0OOO0O0 ).json ()#line:774
                        if 'status'in O00OO0O0OO000OOO0 :#line:776
                            if O00OO0O0OO000OOO0 ['status']==200 :#line:777
                                OOO0O0OOOOO00OO00 =float (O00OO0O0OO000OOO0 ['data']['silver'])/1000000000000 #line:778
                                OO0000000000O00OO =str (OOO0O0OOOOO00OO00 -OOO000O0000OO00O0 )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{OO0OO00OO0O000OOO}分钟奖励🌱数量:{OO0000000000O00OO}t粒')#line:780
        except Exception as O0000O0O0OO0O0OO0 :#line:781
            print (O0000O0O0OO0O0OO0 )#line:782
    def user_ad (O0O0O000000OOO0O0 ):#line:785
        try :#line:786
            O00OOOO0O000000OO =f'__{timi_new()}'#line:787
            O0O0000O0OOO0O0OO ={'source':'scsc','authorization':O0O0O000000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0O000000OO ),'signstring':O00OOOO0O000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            OO0O0O0O0OOO0OO00 =requests .request ('get',f'{host}/user/ad',headers =O0O0000O0OOO0O0OO ).json ()#line:799
            if 'status'in OO0O0O0O0OOO0OO00 :#line:801
                if OO0O0O0O0OOO0OO00 ['status']==200 :#line:802
                    OOOO0O00O00OO0OO0 =OO0O0O0O0OOO0OO00 ['data']['max_time']#line:803
                    OOO00000O0OOOO0O0 =OO0O0O0O0OOO0OO00 ['data']['watch_time']#line:804
                    O0O0OOOOOOOOOOO00 =OO0O0O0O0OOO0OO00 ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{O0O0OOOOOOOOOOO00 + OOOO0O00O00OO0OO0 - OOO00000O0OOOO0O0}次丨好友提供:{O0O0OOOOOOOOOOO00}次')#line:806
                    if O0O0OOOOOOOOOOO00 +OOOO0O00O00OO0OO0 -OOO00000O0OOOO0O0 >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        O0OO00000O0O00OO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0000O0OOO0O0OO ).json ()#line:809
                        if 'status'in O0OO00000O0O00OO0 :#line:811
                            if O0OO00000O0O00OO0 ['status']==200 :#line:812
                                O00O0000OO0OOO00O =float (O0OO00000O0O00OO0 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(O00O0000OO0OOO00O)}t粒')#line:814
                                return True #line:815
                            if O0OO00000O0O00OO0 ['status']==500 :#line:816
                                OOOOOOO00O00O0OO0 =O0OO00000O0O00OO0 ['message']#line:817
                                print (f'【获取种子】:{OOOOOOO00O00O0OO0}')#line:818
                                return False #line:819
        except Exception as OOO0OO00000O0O00O :#line:820
            print (OOO0OO00000O0O00O )#line:821
    def synthetic (OOOO000O00OOOOO00 ):#line:824
        global id ,g #line:825
        try :#line:826
            O0000O00OOO000OO0 =OOOO000O00OOOOO00 .level_new ()#line:827
            O0OO00O0OO00OOOOO =random .randint (9 ,11 )#line:828
            OOOO0OO0OO00O0OO0 =f'_site=8&targetSite={O0OO00O0OO00OOOOO}_{timi_new()}'#line:829
            OOOOO0000O00000O0 ={'source':'scsc','authorization':OOOO000O00OOOOO00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0OO00O0OO0 ),'signstring':OOOO0OO0OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            OOOOO000O0OO0OOOO ={"site":int (8 ),"targetSite":int (O0OO00O0OO00OOOOO )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0000O00000O0 ,json =OOOOO000O0OO0OOOO )#line:842
            while True :#line:843
                O0OO00OO0OOOOOO00 =f'__{timi_new()}'#line:844
                O0OOOO00O0OOO00OO ={'source':'scsc','authorization':OOOO000O00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0OOOOOO00 ),'signstring':O0OO00OO0OOOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                O0000OO00OOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00O0OOO00OO ).json ()#line:856
                if 'status'in O0000OO00OOOOO0O0 :#line:858
                    if O0000OO00OOOOO0O0 ['status']==200 :#line:859
                        O00OOOOO00OOO00OO =O0000OO00OOOOO0O0 ['data']['cropList']#line:860
                        O0O0OOO0O0O0000OO =O0000OO00OOOOO0O0 ['data']['gameCoreDataDBid']#line:861
                        O0O000OO0OOOOO00O =float (O0000OO00OOOOO0O0 ['data']['silver'])/1000000000000 #line:862
                        OO00O0000O0O00O0O =0 #line:867
                        for OO0OOOO0OO0OO0000 in O00OOOOO00OOO00OO :#line:868
                            if not OO0OOOO0OO0OO0000 :#line:869
                                OOOO000O00OOO0000 =f'_crop_id={O0O0OOO0O0O0000OO}&site={OO00O0000O0O00O0O}_{OOOO000O00OOOOO00.time}'#line:870
                                OOOOOO0000000O0O0 ={'source':'scsc','authorization':OOOO000O00OOOOO00 .token ,'timestamp':OOOO000O00OOOOO00 .time ,'sign':sign (OOOO000O00OOO0000 ),'signstring':OOOO000O00OOO0000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                OO0OO0OOOO0O0O0O0 ={"site":OO00O0000O0O00O0O ,"crop_id":O0O0OOO0O0O0000OO }#line:881
                                OOO00O0000000OOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOO0000000O0O0 ,data =OO0OO0OOOO0O0O0O0 ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in OOO00O0000000OOO0 :#line:885
                                    if OOO00O0000000OOO0 ['status']==200 :#line:886
                                        if OOO00O0000000OOO0 ['message']=='种子数量不足':#line:887
                                            O0000O00OOO000OO0 =OOOO000O00OOOOO00 .level_new ()#line:888
                                            print (f'【种植合成】:{OOO00O0000000OOO0["message"]}')#line:889
                                            if not OOOO000O00OOOOO00 .user_ad ():#line:890
                                                return False #line:891
                                    if OOO00O0000000OOO0 ['status']==500 :#line:892
                                        print (f'【种植合成】:{OOO00O0000000OOO0["message"]}')#line:893
                                        return False #line:894
                            OO00O0000O0O00O0O +=1 #line:895
                        OO000OO00O0O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00O0OOO00OO ).json ()#line:896
                        O0O000O00O00OO0OO =OO000OO00O0O0O00O ['data']['cropList']#line:897
                        O00OOO0OOO0000OOO =False #line:898
                        for OO0OOOO0OO0OO0000 in range (12 ):#line:899
                            id =O0O000O00O00OO0OO [OO0OOOO0OO0OO0000 ]['level']#line:900
                            if float (O0000O00OOO000OO0 )-float (id )>9 :#line:901
                                O0O0OOOOO000OO0OO =f'_site={OO0OOOO0OO0OO0000}_{timi_new()}'#line:902
                                O000O0O00O00O0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000O00OOOOO00 .token ,'timestamp':timi_new (),'sign':sign (O0O0OOOOO000OO0OO ),'signstring':O0O0OOOOO000OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                O0000O0OOOOOOO0OO ={"site":OO0OOOO0OO0OO0000 }#line:914
                                OOOOO00O000OO00OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0O00O00O0OOO ,data =O0000O0OOOOOOO0OO ).json ()#line:916
                                if 'status'in OOOOO00O000OO00OO :#line:917
                                    if OOOOO00O000OO00OO ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for OO00O0OOOO000OO00 in range (11 ):#line:921
                                    OOO0OOO0OOO0OOO00 =OO00O0OOOO000OO00 +1 #line:922
                                    g =O0O000O00O00OO0OO [OOO0OOO0OOO0OOO00 ]['level']#line:923
                                    if id ==g :#line:924
                                        O0O0O0OO0O0O0OOOO =OO00O0OOOO000OO00 +2 #line:925
                                        if O0O0O0OO0O0O0OOOO !=OO0OOOO0OO0OO0000 +1 :#line:926
                                            OOOOO00000O000000 =OO0OOOO0OO0OO0000 +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            OOOO0OO0OO00O0OO0 =f'_site={OOOOO00000O000000 - 1}&targetSite={O0O0O0OO0O0O0OOOO - 1}_{timi_new()}'#line:930
                                            OOOOO0000O00000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000O00OOOOO00 .token ,'timestamp':timi_new (),'sign':sign (OOOO0OO0OO00O0OO0 ),'signstring':OOOO0OO0OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O0000O0O000O0OOO0 ={"site":int (OOOOO00000O000000 -1 ),"targetSite":int (O0O0O0OO0O0O0OOOO -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0000O00000O0 ,json =O0000O0O000O0OOO0 )#line:949
                                            O00OOO0OOO0000OOO =True #line:951
                                    if O00OOO0OOO0000OOO :#line:952
                                        break #line:953
                                if O00OOO0OOO0000OOO :#line:954
                                    break #line:955
        except :#line:956
            OOOO000O00OOOOO00 .synthetic ()#line:957
    def level_new (OO0O0O0O0O0OOO00O ):#line:960
        try :#line:961
            O000O00OO0OO00000 =f'__{timi_new()}'#line:962
            OO0O000OO0O0OO0OO ={'source':'scsc','authorization':OO0O0O0O0O0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OO0OO00000 ),'signstring':O000O00OO0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OO0O0O0OO00OOO0O0 =requests .request ('get',f'{host}/user',headers =OO0O000OO0O0OO0OO ).json ()#line:974
            if 'status'in OO0O0O0OO00OOO0O0 :#line:975
                if OO0O0O0OO00OOO0O0 ['status']==200 :#line:976
                    return float (OO0O0O0OO00OOO0O0 ['data']['level'])#line:977
        except Exception as O0000O0000OO0OOO0 :#line:978
            print (O0000O0000OO0OOO0 )#line:979
    def propsraffle (OO0OO0OOOOO0OO00O ):#line:982
        try :#line:983
            while True :#line:984
                O0OO0000O0O00OO0O =f'__{timi_new()}'#line:985
                O000OO0OO0O0OOOO0 ={'source':'scsc','authorization':OO0OO0OOOOO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O0O00OO0O ),'signstring':O0OO0000O0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                OO0OOO00O0O00OO0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000OO0OO0O0OOOO0 ).json ()#line:997
                if 'status'in OO0OOO00O0O00OO0O :#line:999
                    if OO0OOO00O0O00OO0O ['status']==200 :#line:1000
                        O0000O0OOO0O0O0O0 =OO0OOO00O0O00OO0O ['data']['rows']#line:1001
                        OO0O0OO0O0O00O000 =OO0OOO00O0O00OO0O ['data']['vstate']#line:1002
                        if O0000O0OOO0O0O0O0 ==5 or O0000O0OOO0O0O0O0 ==6 or O0000O0OOO0O0O0O0 ==7 :#line:1003
                            O0O0O000000000000 =OO0OOO00O0O00OO0O ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{O0O0O000000000000}')#line:1005
                        if O0000O0OOO0O0O0O0 ==1 or O0000O0OOO0O0O0O0 ==2 or O0000O0OOO0O0O0O0 ==3 :#line:1006
                            O0O0OO0OO0O00OO00 =OO0OOO00O0O00OO0O ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OO0OO0O00OO00}')#line:1008
                        if O0000O0OOO0O0O0O0 ==4 or O0000O0OOO0O0O0O0 ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if O0000O0OOO0O0O0O0 =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as O00OOO0OO0OOO00OO :#line:1050
            print (O00OOO0OO0OOO00OO )#line:1051
    def friends_invitation (O0O00000OO000OO00 ):#line:1054
        try :#line:1055
            OOOOOO0OO0OO0O0OO =f'__{timi_new()}'#line:1056
            OOO0OO00000OO0O0O ={'source':'scsc','authorization':O0O00000OO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0OO0O0OO ),'signstring':OOOOOO0OO0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            O0O0OOOO00OO0000O =requests .request ('get',f'{host}/friends',headers =OOO0OO00000OO0O0O ).json ()#line:1068
            if 'status'in O0O0OOOO00OO0000O :#line:1069
                if O0O0OOOO00OO0000O ['status']==200 :#line:1070
                    O0O000OO0OO0OOO0O =O0O0OOOO00OO0000O ['data']['myInviteter']#line:1071
                    if O0O000OO0OO0OOO0O :#line:1072
                        O000000OO000O00OO =O0O000OO0OO0OOO0O ['user']['nickname']#line:1073
                        OO0OOOOO0OOOOO000 =O0O00000OO000OO00 .certification ()#line:1074
                        if OO0OOOOO0OOOOO000 =='未实名':#line:1075
                            weishim .append (O0O00000OO000OO00 .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{O000000OO000O00OO}丨实名:{OO0OOOOO0OOOOO000}')#line:1077
                    else :#line:1078
                        if O0O00000OO000OO00 .innerId !='0':#line:1079
                            O0O00000OO000OO00 .invitation ()#line:1080
        except Exception as O00O0O0OO0O000000 :#line:1081
            print (O00O0O0OO0O000000 )#line:1082
    def add_clover (O00O00OOOOOOO00OO ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            OOO00000000O0OO0O =f'__{timi_new()}'#line:1088
            O00OO0O0OO00OO0OO ={'source':'scsc','authorization':O00O00OOOOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000000O0OO0O ),'signstring':OOO00000000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O0OO0OOO0O00O00OO =requests .request ('get',f'{host}/assets/clovers',headers =O00OO0O0OO00OO0OO ).json ()#line:1100
            if 'status'in O0OO0OOO0O00O00OO :#line:1102
                if O0OO0OOO0O00O00OO ['status']==200 :#line:1103
                    OO00O0000OO000O00 =O0OO0OOO0O00O00OO ['data']['clover']#line:1104
                    O00O0O0O00O0O0O00 =O0OO0OOO0O00O00OO ['data']['used_clover']#line:1105
                    O0OOO000OOO00OOO0 =float (OO00O0000OO000O00 )-float (O00O0O0O00O0O0O00 )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{O00O0O0O00O0O0O00}')#line:1107
                    if O00O00OOOOOOO00OO .certification ()!='未实名':#line:1108
                        if O0OOO000OOO00OOO0 >1 :#line:1109
                            OOO00000000O0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO000OOO00OOO0)}_{timi_new()}'#line:1110
                            O0000OO00000O0OO0 ={'source':'scsc','authorization':O00O00OOOOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000000O0OO0O ),'signstring':OOO00000000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            O0O0O0O000OOO0OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO000OOO00OOO0 )}#line:1122
                            OOOO0OOOOOO0OO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0000OO00000O0OO0 ,data =O0O0O0O000OOO0OOO ).json ()#line:1123
                            if 'status'in OOOO0OOOOOO0OO00O :#line:1125
                                if OOOO0OOOOOO0OO00O ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OOOOOO0OO00O["data"]["isSuccess"]}丨数量:{O0OOO000OOO00OOO0}')#line:1127
                                if OOOO0OOOOOO0OO00O ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{OOOO0OOOOOO0OO00O["message"]}')#line:1129
            O0O0O0O00O0OOOO00 =requests .request ('get',f'{host}/lottery',headers =O00OO0O0OO00OO0OO ).json ()#line:1130
            OOO00OOOOOO0OOOOO =O00O00OOOOOOO00OO .winning_rewards ()#line:1132
            if 'status'in O0O0O0O00O0OOOO00 :#line:1133
                if O0O0O0O00O0OOOO00 ['status']==200 :#line:1134
                    OOO0O0O00OO0O0000 =O0O0O0O00O0OOOO00 ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (OOO0O0O00OO0O0000 )#line:1136
                    OO0OOOO0O000OO00O =O0O0O0O00O0OOOO00 ['data'][1 ]['value']#line:1137
                    O0O0OO0OOO00O0O00 =O0O0O0O00O0OOOO00 ['data'][0 ]['join_number']#line:1138
                    OO000OO0O0O0000OO =int (float (O0O0O0O00O0OOOO00 ['data'][0 ]['totalValue']))#line:1139
                    O0OOO00OOO0OO00OO =float (OO0OOOO0O000OO00O /OO000OO0O0O0000OO )*10000 #line:1140
                    OO0O000OO0O0O0O0O =OO000OO0O0O0000OO /O0O0OO0OOO00O0O00 #line:1141
                    print (f'【参与抽奖】:预计每天中{str(OOO0O0O00OO0O0000)[:6]}颗金种子丨好友收益:{str(OOO00OOOOOO0OOOOO)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO00OOO0OO00OO)[:6]}颗金种子丨☘️人均:{str(OO0O000OO0O0O0O0O)[:7]}️')#line:1143
        except Exception as OOOO0OO00O00O00O0 :#line:1144
            print (OOOO0OO00O00O00O0 )#line:1145
    def energy (OO0OO0O00O0O0000O ):#line:1148
        try :#line:1149
            while True :#line:1150
                O0OO0000O0O0OOO00 =f'__{timi_new()}'#line:1151
                O00OO0OOO0000O000 ={'source':'scsc','authorization':OO0OO0O00O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O0O0OOO00 ),'signstring':O0OO0000O0O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                O0000OO0OOO00OO00 =requests .request ('get',f'{host}/energy/general',headers =O00OO0OOO0000O000 ).json ()#line:1163
                if 'status'in O0000OO0OOO00OO00 :#line:1165
                    if O0000OO0OOO00OO00 ['status']==200 :#line:1166
                        OO000OO0OOOOO000O =O0000OO0OOO00OO00 ['data']['ordinary_water']#line:1167
                        O0OOOOO0O0000O000 =O0000OO0OOO00OO00 ['data']['ordinary_fertilizer']#line:1168
                        OOO0000O000O00O0O =O0000OO0OOO00OO00 ['data']['videoStatus']#line:1169
                        O0OO0OO00OOOO0OOO =O0000OO0OOO00OO00 ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(O0OOOOO0O0000O000).split(".")[0]}丨水滴:{str(OO000OO0OOOOO000O).split(".")[0]}')#line:1172
                        if float (O0OOOOO0O0000O000 )<96 :#line:1173
                            if OOO0000O000O00O0O :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                O000O00OOOO000000 =99 -float (O0OOOOO0O0000O000 )#line:1176
                                O0O00O0OO0O0O00OO ={"fertilizer":str (O000O00OOOO000000 ).split ('.')[0 ]}#line:1177
                                O000O0O00O000O00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OO0OOO0000O000 ).json ()#line:1179
                                if 'status'in O000O0O00O000O00O :#line:1181
                                    if O000O0O00O000O00O ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O00O000O00O["message"]}')#line:1183
                                    if O000O0O00O000O00O ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0O00O000O00O["message"]}')#line:1185
                                        break #line:1186
                                if float (O0OOOOO0O0000O000 )<78 :#line:1188
                                    O000O00OOOO000000 =80 -float (O0OOOOO0O0000O000 )#line:1189
                                    O0000O000O000000O =f'_fertilizer={int(O000O00OOOO000000)}_{timi_new()}'#line:1190
                                    O0O0O0OO0OO0OO0OO ={'source':'scsc','authorization':OO0OO0O00O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000O000000O ),'signstring':O0000O000O000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    O00O0000O000O0O00 ={"fertilizer":int (O000O00OOOO000000 )}#line:1202
                                    OOO00000OOO0OO0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0O0OO0OO0OO0OO ,data =O00O0000O000O0O00 ).json ()#line:1204
                                    if 'status'in OOO00000OOO0OO0OO :#line:1206
                                        if OOO00000OOO0OO0OO ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{OOO00000OOO0OO0OO["message"]}丨数量:{int(O000O00OOOO000000)}')#line:1208
                                        if OOO00000OOO0OO0OO ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{OOO00000OOO0OO0OO["message"]}丨数量:{int(O000O00OOOO000000)}')#line:1210
                                            O00OOO0O00OO0O000 =OOO00000OOO0OO0OO ["message"].split ('-')[1 ]#line:1211
                                            OOO0O00O00O0OO000 =f'__{timi_new()}'#line:1212
                                            O00OO000OOOOOOOOO ={'source':'scsc','authorization':OO0OO0O00O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00O0OO000 ),'signstring':OOO0O00O00O0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            O0OOOO00000O0O0OO =requests .request ('get',f'{host}/user',headers =O00OO000OOOOOOOOO ).json ()#line:1224
                                            if 'status'in O0OOOO00000O0O0OO :#line:1225
                                                if O0OOOO00000O0O0OO ['status']==200 :#line:1226
                                                    OO0OOO000000O0OOO =O0OOOO00000O0O0OO ['data']['inner_id']#line:1227
                                                    if give_gold (OO0OOO000000O0OOO ,float (O00OOO0O00OO0O000 )+1 ):#line:1228
                                                        OO0OO0O00O0O0000O .energy ()#line:1229
                        if float (OO000OO0OOOOO000O )<880 :#line:1230
                            if O0OO0OO00OOOO0OOO :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                OOO0OOO00O000000O =999 -float (OO000OO0OOOOO000O )#line:1233
                                OO0OO000OO0000O00 ={"water":str (OOO0OOO00O000000O ).split ('.')[0 ]}#line:1234
                                O000000000OO00O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OO0OOO0000O000 ).json ()#line:1236
                                if 'status'in O000000000OO00O00 :#line:1238
                                    if O000000000OO00O00 ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{O000000000OO00O00["message"]}')#line:1240
                                    if O000000000OO00O00 ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{O000000000OO00O00["message"]}')#line:1242
                                        break #line:1243
                                if float (OO000OO0OOOOO000O )<780 :#line:1244
                                    OOO0OOO00O000000O =800 -float (OO000OO0OOOOO000O )#line:1245
                                    O0O0O0000OOO0OOOO =f'_water={int(OOO0OOO00O000000O)}_{timi_new()}'#line:1246
                                    OOO00000000000O0O ={'source':'scsc','authorization':OO0OO0O00O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OOO0OOOO ),'signstring':O0O0O0000OOO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    O00000OO0000OO0O0 ={"water":int (OOO0OOO00O000000O )}#line:1258
                                    O0OOOO00OO0O000OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00000000000O0O ,data =O00000OO0000OO0O0 ).json ()#line:1260
                                    if 'status'in O0OOOO00OO0O000OO :#line:1262
                                        if O0OOOO00OO0O000OO ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{O0OOOO00OO0O000OO["message"]}丨数量:{int(OOO0OOO00O000000O)}')#line:1264
                                        if O0OOOO00OO0O000OO ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{O0OOOO00OO0O000OO["message"]}丨数量:{int(OOO0OOO00O000000O)}')#line:1266
                                            O00OOO0O00OO0O000 =O0OOOO00OO0O000OO ["message"].split ('-')[1 ]#line:1267
                                            OOO0O00O00O0OO000 =f'__{timi_new()}'#line:1268
                                            O00OO000OOOOOOOOO ={'source':'scsc','authorization':OO0OO0O00O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00O0OO000 ),'signstring':OOO0O00O00O0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            O0OOOO00000O0O0OO =requests .request ('get',f'{host}/user',headers =O00OO000OOOOOOOOO ).json ()#line:1280
                                            if 'status'in O0OOOO00000O0O0OO :#line:1281
                                                if O0OOOO00000O0O0OO ['status']==200 :#line:1282
                                                    OO0OOO000000O0OOO =O0OOOO00000O0O0OO ['data']['inner_id']#line:1283
                                                    if give_gold (OO0OOO000000O0OOO ,float (O00OOO0O00OO0O000 )+1 ):#line:1284
                                                        OO0OO0O00O0O0000O .energy ()#line:1285
                        break #line:1286
        except Exception as O000O00000O0O0O0O :#line:1287
            print (O000O00000O0O0O0O )#line:1288
def bundled_def ():#line:1291
    OO00O0OO0OO00O00O =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return OO00O0OO0OO00O00O [random .randint (0 ,len (OO00O0OO0OO00O00O )-1 )]#line:1293
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
        O000O00OO0OO000O0 =gitee_edition ()#line:1332
        if version_of_the_validation ()<O000O00OO0OO000O0 ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00OO0OO000O0["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{O000O00OO0OO000O0["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O00OO0OO000O0["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {O000O00OO0OO000O0["CityEarth"]["content"]}')#line:1338
    except Exception as OOOO0OOOOO00000OO :#line:1339
        print (OOOO0OOOOO00000OO )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
