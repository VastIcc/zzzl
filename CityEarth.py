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
@ 版本  3.8
"""
##################################配置区##################################
time_xx = random.randint(15, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
eeeeee = False  # 打印没有俩个二级好友的ID
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
        O00OO00OO00O000OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O00OO00OO00O000OO)}个账号==========")#line:16
        for O00OO0O0O0OOOO00O in O00OO00OO00O000OO :#line:17
            OO0O0OOO000O00000 =[]#line:18
            print (f"------------正在执行第{O00OO00OO00O000OO.index(O00OO0O0O0OOOO00O) + 1}个账号------------")#line:19
            OOO0O000O0O0O000O =CityEarth (O00OO0O0O0OOOO00O ,OO0O0OOO000O00000 ,O00OO00OO00O000OO .index (O00OO0O0O0OOOO00O ))#line:20
            def OOOO0O00OO0O00000 ():#line:22
                if OOO0O000O0O0O000O .base_info ():#line:24
                    OOO0O000O0O0O000O .sealing ()#line:26
                    OOO0O000O0O0O000O .invitenum ()#line:28
                    OOO0O000O0O0O000O .query_to_sell ()#line:30
                    OOO0O000O0O0O000O .game_map ()#line:32
                    OOO0O000O0O0O000O .friends_invitation ()#line:34
                    OOO0O000O0O0O000O .energy ()#line:36
                    OOO0O000O0O0O000O .add_clover ()#line:38
                    OOO0O000O0O0O000O .propsraffle ()#line:40
                    OOO0O000O0O0O000O .synthetic ()#line:42
                    OOO0O000O0O0O000O .crops_illustrated ()#line:44
                    OOO0O000O0O0O000O .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        OOO0O000O0O0O000O .give_gold ()#line:49
            O000000OOOO00O0O0 =threading .Thread (target =OOOO0O00OO0O00000 )#line:51
            O000000OOOO00O0O0 .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理推送通知------------")#line:54
        time .sleep (0.5 )#line:55
        OOO0O000OOO0O0OOO =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0O000OOO0O0OOO +' ')#line:57
        if eeeeee :#line:58
            time .sleep (100 )#line:59
            print ('开始打印好友数量不足2的ID')#line:60
            for O000O0O0O0000O00O in invited_new :#line:61
                print (O000O0O0O0000O00O )#line:62
            print ('开始打印未实名的token')#line:63
            for OOOOO0O0OO00O00OO in weishim :#line:64
                print (OOOOO0O0OO00O00OO )#line:65
    except Exception as O00000000000OO0OO :#line:66
        print (O00000000000OO0OO )#line:67
def give_gold (OO00OO0OOOO0O00OO ,O00OOO00O0O00OO00 ):#line:71
    try :#line:72
        OO0OO0O00O00OOOOO =f'_doneeNo={OO00OO0OOOO0O00OO}&quantity={int(O00OOO00O0O00OO00)}_{timi_new()}'#line:73
        OOO0O0O00000OOO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00O00OOOOO ),'signstring':OO0OO0O00O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:84
        OO00OO0OOOOOOOO0O ={"quantity":int (O00OOO00O0O00OO00 ),"doneeNo":OO00OO0OOOO0O00OO }#line:88
        OOOO0OOO000000OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O0O00000OOO00 ,data =OO00OO0OOOOOOOO0O ).json ()#line:89
        if 'status'in OOOO0OOO000000OO0 :#line:91
            if OOOO0OOO000000OO0 ['status']==200 :#line:92
                if OOOO0OOO000000OO0 ['data']:#line:93
                    print (f'【赠送种子】:赠送{int(O00OOO00O0O00OO00)}种子给{OO00OO0OOOO0O00OO}成功')#line:94
                    return True #line:95
            if OOOO0OOO000000OO0 ['status']==401 :#line:96
                print (f'【赠送种子】:{OOOO0OOO000000OO0["message"]}')#line:97
                return False #line:98
            if OOOO0OOO000000OO0 ['status']==500 :#line:99
                print (f'【赠送种子】:{OOOO0OOO000000OO0["message"]}')#line:100
                return False #line:101
        return False #line:102
    except Exception as OOO00O0OO00O0OO0O :#line:103
        print (OOO00O0OO00O0OO0O )#line:104
def kvkv ():#line:107
    return '/vastzzzl/vastzzzl/raw/master'#line:108
def sign (O0OO0O0O0O00O0OOO ):#line:111
    OOO0OO0O00OO00O00 =hashlib .md5 (O0OO0O0O0O00O0OOO .encode ()).hexdigest ()#line:112
    O0O00O00O0O0O00OO =sc1 ()#line:113
    OO00OO0O0O00OOO0O =sc2 ()#line:114
    O0OOO0O00O0OOOOO0 =sc3 ()#line:115
    OOOO00OOO00O0OOO0 =O0O00O00O0O0O00OO +OOO0OO0O00OO00O00 +OO00OO0O0O00OOO0O +O0OOO0O00O0OOOOO0 #line:116
    O0OO0000O000O0O0O =hashlib .md5 (OOOO00OOO00O0OOO0 .encode ()).hexdigest ()#line:117
    return O0OO0000O000O0O0O #line:118
def format_msg ():#line:121
    O0O00OO0OO0OO0OO0 =""#line:122
    for OO0OOOOO0OO0O00O0 in msg_list :#line:123
        O0O00OO0OO0OO0OO0 +=str (OO0OOOOO0OO0O00O0 )+"\r\n"#line:124
    return O0O00OO0OO0OO0OO0 #line:125
def sc1 ():#line:128
    return "scsc%^&*"#line:129
def O000OO0O00OO00O00 ():#line:132
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:133
        pass #line:134
    else :#line:135
        exit (1 )#line:136
def timi_new ():#line:139
    return str (int (time .time ()*1000 ))#line:140
json_path ="CityEarth_data.json"#line:143
json_path1 ="CityEarth_data.json"#line:144
dict ={}#line:145
def get_json_data (OO0OOOO0000OO0OO0 ,O0OO0OOOOOOOOO0O0 ,OOO000O00000O0O0O ,O0O0000000O000000 ):#line:148
    with open (OO0OOOO0000OO0OO0 ,'rb')as O0O0O000O00OO0OO0 :#line:149
        O00OO00O0OO0O0OO0 =json .load (O0O0O000O00OO0OO0 )#line:150
        O00OO00O0OO0O0OO0 ['data'][O0OO0OOOOOOOOO0O0 ][OOO000O00000O0O0O ]=O0O0000000O000000 #line:151
        OOO00O0OO00O00O00 =O00OO00O0OO0O0OO0 #line:152
    O0O0O000O00OO0OO0 .close ()#line:153
    return OOO00O0OO00O00O00 #line:154
def write_json_data (OOOOOOOOOO0OO00O0 ):#line:157
    with open (json_path1 ,'w')as O00O0OOO0O0000OOO :#line:158
        json .dump (OOOOOOOOOO0OO00O0 ,O00O0OOO0O0000OOO )#line:159
    O00O0OOO0O0000OOO .close ()#line:160
    return True #line:161
class CityEarth :#line:164
    def __init__ (OOO000O000O00O0OO ,OO00O00OOO0O00O0O ,OOO0O0O0O0O0O00OO ,OOO0O000OO0O00O0O ):#line:166
        try :#line:167
            OOO000O000O00O0OO .msg =OOO0O0O0O0O0O00OO #line:168
            OOO000O000O00O0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:169
            OOO000O000O00O0OO .token =OO00O00OOO0O00O0O ['authorization']#line:170
            OOO000O000O00O0OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:171
            OOO000O000O00O0OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:172
            OOO000O000O00O0OO .elephant_user =OO00O00OOO0O00O0O ['elephant_user']#line:173
            OOO000O000O00O0OO .elephant_pswd =OO00O00OOO0O00O0O ['elephant_pswd']#line:174
            OOO000O000O00O0OO .elephant_Task_ID =OO00O00OOO0O00O0O ['elephant_Task_ID']#line:175
            OOO000O000O00O0OO .len_new =OOO0O000OO0O00O0O #line:176
        except :#line:177
            print ('变量格式错误')#line:178
    def base_info (O000OO000O0O000O0 ):#line:181
        try :#line:182
            O000OO000O0O000O0 .watched_ad ()#line:184
            OOOOOO0OO0OOO0O00 =f'__{timi_new()}'#line:185
            OOO0OOOO00OOO00O0 ={'source':'scsc','authorization':O000OO000O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OO0OOO0O00 ),'signstring':OOOOOO0OO0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:196
            O00OOO00OO00OOO0O =requests .request ('get',f'{host}/user',headers =OOO0OOOO00OOO00O0 ).json ()#line:197
            if 'status'in O00OOO00OO00OOO0O :#line:199
                if O00OOO00OO00OOO0O ['status']==200 :#line:200
                    OOOOOO00O00O0OOOO =O00OOO00OO00OOO0O ['data']['nickname']#line:201
                    OOOOOOO0O0OOOOOOO =O00OOO00OO00OOO0O ['data']['inner_id']#line:202
                    O000OOO0O00OOOO00 =O00OOO00OO00OOO0O ['data']['assets']['gold']#line:203
                    O0O0OO00O0O0OOO00 =O00OOO00OO00OOO0O ['data']['level']#line:204
                    print (f'【账号信息】:昵称:{OOOOOO00O00O0OOOO[:5]}丨ID:{OOOOOOO0O0OOOOOOO}丨等级:{O0O0OO00O0O0OOO00}丨金种子:{str(O000OOO0O00OOOO00).split(".")[0]}')#line:206
                    if 'wx_'in OOOOOO00O00O0OOOO :#line:207
                        O000OO000O0O000O0 .change_nickname ()#line:208
                if O00OOO00OO00OOO0O ['status']==401 :#line:209
                    print ('【账号信息】:账号失效正在尝试登录')#line:210
                    if O000OO000O0O000O0 .elephant_user =='f':#line:211
                        return False #line:212
                    O0000O00OO000OO0O =Invalid_login .addtask (elephant_user =O000OO000O0O000O0 .elephant_user ,elephant_pswd =O000OO000O0O000O0 .elephant_pswd ,elephant_Task_ID =O000OO000O0O000O0 .elephant_Task_ID )#line:215
                    OO0000OOOO0OO00OO =get_json_data (json_path ,O000OO000O0O000O0 .len_new ,'authorization',O0000O00OO000OO0O )#line:216
                    if write_json_data (OO0000OOOO0OO00OO ):#line:217
                        print ('正在写入账号配置文件')#line:218
                    return False #line:219
                if O00OOO00OO00OOO0O ['status']==500 :#line:220
                    return False #line:221
            return True #line:222
        except Exception as O0OO0OO0O00OOO000 :#line:223
            print (O0OO0OO0O00OOO000 )#line:224
    def sealing (O00OO0OO0OO00O00O ):#line:227
        try :#line:228
            O00000OO0O0000O0O =f'__{timi_new()}'#line:229
            OO0OOO0000OOO00O0 ={'source':'scsc','authorization':O00OO0OO0OO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0O0000O0O ),'signstring':O00000OO0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:240
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOO0000OOO00O0 )#line:241
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOO0000OOO00O0 )#line:242
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOO0000OOO00O0 )#line:243
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOO0000OOO00O0 )#line:244
            requests .request ('get',f'{host}/user',headers =OO0OOO0000OOO00O0 )#line:245
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOO0000OOO00O0 )#line:246
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOO0000OOO00O0 )#line:247
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOO0000OOO00O0 )#line:248
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOO0000OOO00O0 )#line:249
            requests .request ('get',f'{host}/assets',headers =OO0OOO0000OOO00O0 )#line:250
        except Exception as O0OO0OO0O0000O0O0 :#line:251
            print (O0OO0OO0O0000O0O0 )#line:252
    def the_query (OO00OO00O0OO0OOO0 ):#line:255
        try :#line:256
            O0OO00O00O00O00OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:257
            OO0OO00OO0OOO0O0O ={'authorization':OO00OO00O0OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00O00O00OO ),'signstring':O0OO00O00O00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:267
            OO0OO00OO0O0OOOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0OO00OO0OOO0O0O ).json ()#line:269
            if 'status'in OO0OO00OO0O0OOOO0 :#line:271
                if OO0OO00OO0O0OOOO0 ['status']==200 :#line:272
                    OOOOO00O0OO0O0OOO =OO0OO00OO0O0OOOO0 ['data']['rows'][3 ]['price']#line:273
                    OO00OO00O0OO0OOO0 .market_sale (OOOOO00O0OO0O0OOO )#line:274
        except Exception as O0OO00O000OOOO0OO :#line:275
            print (O0OO00O000OOOO0OO )#line:276
    def market_sale (O00000OO0OOO0O0O0 ,OO000O0000OOOOO00 ):#line:279
        try :#line:280
            OOO0O0OO0OO0OOOOO =timi_new ()#line:281
            O0000O00OO0O00OOO =f'type=crop__{OOO0O0OO0OO0OOOOO}'#line:282
            OO00O0O00OO0OO0OO ={'source':'scsc','authorization':O00000OO0OOO0O0O0 .token ,'timestamp':str (OOO0O0OO0OO0OOOOO ),'sign':sign (O0000O00OO0O00OOO ),'signstring':O0000O00OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:293
            OO0O000O0O00OOOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00O0O00OO0OO0OO ).json ()#line:295
            if 'status'in OO0O000O0O00OOOO0 :#line:297
                if OO0O000O0O00OOOO0 ['status']==200 :#line:298
                    if OO0O000O0O00OOOO0 ['data']['rows']:#line:299
                        OOO0OOOO0O00OOO0O =OO0O000O0O00OOOO0 ['data']['rows'][0 ]['packsackItemId']#line:300
                        O0OOOOOOOOOO000O0 =OO0O000O0O00OOOO0 ['data']['rows'][0 ]['quantity']#line:301
                        OO0O000OOO0O0OOO0 =float (OO000O0000OOOOO00 )+float (random .randint (1 ,99 )*0.001 )#line:302
                        OO000OO0O0OO0OO00 =f'_packsackItemId={OOO0OOOO0O00OOO0O}&price={str(OO0O000OOO0O0OOO0)[:7]}&quantity={O0OOOOOOOOOO000O0}_{OOO0O0OO0OO0OOOOO}'#line:303
                        O0O0O0OO00O0OOOO0 ={'source':'scsc','authorization':O00000OO0OOO0O0O0 .token ,'timestamp':str (OOO0O0OO0OO0OOOOO ),'sign':sign (OO000OO0O0OO0OO00 ),'signstring':OO000OO0O0OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:314
                        OO0OO000O0O0OO00O ={"packsackItemId":OOO0OOOO0O00OOO0O ,"price":str (OO0O000OOO0O0OOO0 )[:7 ],"quantity":str (O0OOOOOOOOOO000O0 )}#line:319
                        OOO0OO0O000O0O000 =requests .request ('post',f'{host}/market/sale',headers =O0O0O0OO00O0OOOO0 ,data =OO0OO000O0O0OO00O ).json ()#line:320
                        if 'status'in OOO0OO0O000O0O000 :#line:322
                            if OOO0OO0O000O0O000 ['status']==200 :#line:323
                                print (f'【上架芦荟】:数量:{O0OOOOOOOOOO000O0}丨价格:{str(OO0O000OOO0O0OOO0)[:7]}')#line:324
        except Exception as O00OO00O0OO0OOO00 :#line:325
            print (O00OO00O0OO0OOO00 )#line:326
    def query_to_sell (O0OOO0OOOO00OOOOO ):#line:329
        try :#line:330
            OOO0O0O0OO0O0000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:331
            OO000O0000OO00OOO ={'source':'scsc','authorization':O0OOO0OOOO00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OO0O0000O ),'signstring':OOO0O0O0OO0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:342
            OOO0000O00O00O0OO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO000O0000OO00OOO ).json ()#line:344
            if 'status'in OOO0000O00O00O0OO :#line:346
                if OOO0000O00O00O0OO ['status']==200 :#line:347
                    for O0O00O0OOOOOOO00O in OOO0000O00O00O0OO ['data']['rows']:#line:348
                        O0O00000OOOOOOO0O =O0O00O0OOOOOOO00O ['materialKey']#line:349
                        O0OO000OO0OO00O0O =O0O00O0OOOOOOO00O ['quantity']#line:350
                        OO0O00OOO0O0000O0 =O0O00O0OOOOOOO00O ['price']#line:351
                        O00OO0OO0O0OO00O0 =O0O00O0OOOOOOO00O ['saleState']#line:352
                        if O00OO0OO0O0OO00O0 ==0 :#line:353
                            print (f'【出售订单】:名称:{O0O00000OOOOOOO0O}丨数量:{O0OO000OO0OO00O0O}丨价格:{OO0O00OOO0O0000O0}')#line:354
                            OO0OO0OOO00OO0OO0 =O0O00O0OOOOOOO00O ['id']#line:355
                            O0OOO0OOOO00OOOOO .cacel_sale (OO0OO0OOO00OO0OO0 )#line:356
        except Exception as O0O00000OOOO0O000 :#line:357
            print (O0O00000OOOO0O000 )#line:358
    def cacel_sale (O000000O000OOO0OO ,OOO0OO00OOOOO0OOO ):#line:361
        try :#line:362
            O00O000OOOO0OO0O0 =f'_saleId={OOO0OO00OOOOO0OOO}_{timi_new()}'#line:363
            O00OO00OO0OO00OO0 ={'source':'scsc','authorization':O000000O000OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOO0OO0O0 ),'signstring':O00O000OOOO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:374
            OOO00O00000O000OO ={"saleId":OOO0OO00OOOOO0OOO }#line:377
            O000O0O000000000O =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OO00OO0OO00OO0 ,data =OOO00O00000O000OO ).json ()#line:378
            if 'status'in O000O0O000000000O :#line:380
                if O000O0O000000000O ['status']==200 :#line:381
                    print (f'【下架出售】:{O000O0O000000000O["data"]}')#line:382
        except Exception as OOO00OO0000O0OOO0 :#line:383
            print (OOO00OO0000O0OOO0 )#line:384
    def change_nickname (OOOOO00O00OOO0OOO ):#line:387
        try :#line:388
            O0O0OO00O0000O0O0 =timi_new ()#line:389
            O0O0OO00O0O0O0OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:390
            O0OO0OO00OO000OO0 =requests .request ('post','https://www.qmsjmfb.com/',data =O0O0OO00O0O0O0OOO ).text #line:391
            OOO0OOOO0O0OO00O0 =re .findall ('<ul><li>(.*?)</li>',O0OO0OO00OO000OO0 )[0 ][:3 ]#line:392
            O0000O00OOO000OO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO0OOOO0O0OO00O0}').json ()#line:393
            O0OOO0000000OOOOO =O0000O00OOO000OO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:394
            O0O00O0OO0000O00O ={"nickname":O0OOO0000000OOOOO }#line:395
            O0O0O00OO0O00O0O0 =f'_nickname={O0OOO0000000OOOOO}_{O0O0OO00O0000O0O0}'#line:396
            O00O0000O0OO00O0O ={'source':'scsc','authorization':OOOOO00O00OOO0OOO .token ,'timestamp':O0O0OO00O0000O0O0 ,'sign':sign (O0O0O00OO0O00O0O0 ),'signstring':O0O0O00OO0O00O0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:407
            O0OOOO0OO00O00OOO =requests .request ('patch',f'{host}/user/nickname',headers =O00O0000O0OO00O0O ,data =O0O00O0OO0000O00O ).json ()#line:408
            if 'status'in O0OOOO0OO00O00OOO :#line:410
                if O0OOOO0OO00O00OOO ['status']==200 :#line:411
                    print (f'【修改网名】:网名:{O0OOO0000000OOOOO}丨{O0OOOO0OO00O00OOO["message"]}')#line:412
        except Exception as O0OOO000O0OOO00OO :#line:413
            print (O0OOO000O0OOO00OO )#line:414
    def withdraw (OO00OO0OO0O0OO000 ):#line:417
        try :#line:418
            OOO0O00000O000OO0 =f'__{timi_new()}'#line:419
            OO0OO000O0OO00000 ={'source':'scsc','authorization':OO00OO0OO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00000O000OO0 ),'signstring':OOO0O00000O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:430
            O000OOOOOOO00OOO0 =requests .request ('get',f'{host}/assets',headers =OO0OO000O0OO00000 ).json ()#line:431
            if 'status'in O000OOOOOOO00OOO0 :#line:433
                if O000OOOOOOO00OOO0 ['status']==200 :#line:434
                    OOO0OOO0OO0O0O000 =O000OOOOOOO00OOO0 ['data']['cash']#line:435
                    if float (OOO0OOO0OO0O0O000 )>20 :#line:436
                        OOO0O00000O000OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:437
                        OO0OO000O0OO00000 ={'authorization':OO00OO0OO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00000O000OO0 ),'signstring':OOO0O00000O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
                        OOOO00OOOOOOO00OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:448
                        O0O000O0OOO0O0O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OO000O0OO00000 ,data =OOOO00OOOOOOO00OO ).json ()#line:450
                        if 'status'in O0O000O0OOO0O0O00 :#line:452
                            if O0O000O0OOO0O0O00 ['status']==200 :#line:453
                                print (f'【余额提现】:{O0O000O0OOO0O0O00["data"]}')#line:454
                        if 'status'in O0O000O0OOO0O0O00 :#line:455
                            if O0O000O0OOO0O0O00 ['status']==500 :#line:456
                                print (f'【余额提现】:{O0O000O0OOO0O0O00["message"]}')#line:457
        except Exception as OOO000O00OO00OOOO :#line:458
            print (OOO000O00OO00OOOO )#line:459
    def invitenum (O0O000O000OO00O00 ):#line:462
        global invited_new #line:463
        try :#line:464
            OOO0OOO00000000OO =f'__{timi_new()}'#line:465
            O000O0O000OOO0O0O ={'source':'scsc','authorization':O0O000O000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO00000000OO ),'signstring':OOO0OOO00000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            O0O0OO00000O0OOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O000O0O000OOO0O0O ).json ()#line:477
            if 'status'in O0O0OO00000O0OOO0 :#line:479
                if O0O0OO00000O0OOO0 ['status']==200 :#line:480
                    OO000O0OOOOO000OO =O0O0OO00000O0OOO0 ['data']['invited_count']#line:481
                    O00O0OOOO0O0O0OO0 =O0O0OO00000O0OOO0 ['data']['invited_second_count']#line:482
                    print (f'【我的邀请】:直邀好友:{OO000O0OOOOO000OO}丨间邀好友:{O00O0OOOO0O0O0OO0}')#line:483
                    if OO000O0OOOOO000OO <2 :#line:484
                        O00OO0O0OO00OOO0O =f'__{timi_new()}'#line:485
                        O0O0O00OOO0O0OO00 ={'source':'scsc','authorization':O0O000O000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0OO00OOO0O ),'signstring':O00OO0O0OO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:496
                        OO0O0O0OOOO0000OO =requests .request ('get',f'{host}/user',headers =O0O0O00OOO0O0OO00 ).json ()#line:497
                        if 'status'in OO0O0O0OOOO0000OO :#line:499
                            if OO0O0O0OOOO0000OO ['status']==200 :#line:500
                                invited_new .append (OO0O0O0OOOO0000OO ['data']['inner_id'])#line:501
        except Exception as OO0OO0O000OO000O0 :#line:502
            print (OO0OO0O000OO000O0 )#line:503
    def game_map (O0OOO000OO0000O00 ):#line:506
        try :#line:507
            OO0OO0O00OO0OO000 =f'__{timi_new()}'#line:508
            O0O0OO0OO0OO0O0O0 ={'source':'scsc','authorization':O0OOO000OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00OO0OO000 ),'signstring':OO0OO0O00OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:519
            OO00OO00OOOO000O0 =requests .request ('get',f'{host}/game/map',headers =O0O0OO0OO0OO0O0O0 ).json ()#line:520
            if 'status'in OO00OO00OOOO000O0 :#line:522
                if OO00OO00OOOO000O0 ['status']==200 :#line:523
                    for OO0OO000O00OOO000 in OO00OO00OOOO000O0 ['data']['list'][0 ]['crops']:#line:524
                        OOOOO0O0O0000OOOO =OO0OO000O00OOO000 ['level']#line:526
                        if OOOOO0O0O0000OOOO ==41 :#line:527
                            O00000O00OO00OOO0 =OO0OO000O00OOO000 ['crop_name']#line:528
                            O0O00000OOO000O0O =OO0OO000O00OOO000 ['count']#line:529
                            if O0O00000OOO000O0O >0 :#line:530
                                print (f'【农业资产】:{O00000O00OO00OOO0}丨数量:{O0O00000OOO000O0O}')#line:531
                                O0OOO000OO0000O00 .the_query ()#line:532
        except Exception as OO000OOO0O00OOOO0 :#line:533
            print (OO000OOO0O00OOOO0 )#line:534
    def give_gold (O000OOO00OO000OOO ):#line:537
        try :#line:538
            O00O00O00OOO00OOO =f'__{timi_new()}'#line:539
            OO0OOO000O00O0O0O ={'source':'scsc','authorization':O000OOO00OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00OOO00OOO ),'signstring':O00O00O00OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            OO0O0OO0O00OO0O00 =requests .request ('get',f'{host}/user',headers =OO0OOO000O00O0O0O ).json ()#line:551
            if 'status'in OO0O0OO0O00OO0O00 :#line:552
                if OO0O0OO0O00OO0O00 ['status']==200 :#line:553
                    if float (O000OOO00OO000OOO .doneeNo )!=0 :#line:554
                        OO0O0O0O0000O00OO =OO0O0OO0O00OO0O00 ['data']['assets']['gold']#line:555
                        if float (OO0O0O0O0000O00OO )>float (O000OOO00OO000OOO .innerId ):#line:556
                            O00OO0OOO0O00OOO0 =int (float (OO0O0O0O0000O00OO )/1.1 )#line:557
                            O00O00O00OOO00OOO =f'_doneeNo={O000OOO00OO000OOO.doneeNo}&quantity={O00OO0OOO0O00OOO0}_{timi_new()}'#line:558
                            OO0OOO000O00O0O0O ={'source':'scsc','authorization':O000OOO00OO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00OOO00OOO ),'signstring':O00O00O00OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            OOOOOO0O0O0000000 ={"quantity":O00OO0OOO0O00OOO0 ,"doneeNo":O000OOO00OO000OOO .doneeNo }#line:573
                            OO00O00OOO000O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OOO000O00O0O0O ,data =OOOOOO0O0O0000000 ).json ()#line:574
                            if 'status'in OO00O00OOO000O0O0 :#line:576
                                if OO00O00OOO000O0O0 ['status']==200 :#line:577
                                    if OO00O00OOO000O0O0 ['data']:#line:578
                                        print (f'【赠送种子】:赠送{O00OO0OOO0O00OOO0}种子给{O000OOO00OO000OOO.doneeNo}成功')#line:579
                    else :#line:580
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:581
        except Exception as OO0O000OO00O000OO :#line:582
            print (OO0O000OO00O000OO )#line:583
    def invitation (OO00OO0O00OOO0000 ):#line:585
        try :#line:586
            _OOOO0OO0OO0O00OOO =float (bundled_def ())/4 #line:587
            OOOO0000OO0O00OOO =f'_innerId={int(_OOOO0OO0OO0O00OOO)}_{timi_new()}'#line:588
            O000OOOOO0O00OO00 ={'source':'scsc','authorization':OO00OO0O00OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OO0O00OOO ),'signstring':OOOO0000OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            OOOOOO00000OOO0O0 ={"innerId":int (_OOOO0OO0OO0O00OOO )}#line:600
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000OOOOO0O00OO00 ,data =OOOOOO00000OOO0O0 )#line:601
        except Exception as OO0OO0OO00OO0O00O :#line:602
            print (OO0OO0OO00OO0O00O )#line:603
    def winning_rewards (OOOOOOOO0OOO0O0OO ):#line:606
        try :#line:607
            O0OOO0O00O0OO0OOO =f'__{timi_new()}'#line:608
            O0OOOO00000O00000 ={'source':'scsc','authorization':OOOOOOOO0OOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00O0OO0OOO ),'signstring':O0OOO0O00O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
            O0OO00O000O000OOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOO00000O00000 ).json ()#line:620
            if 'status'in O0OO00O000O000OOO :#line:622
                if O0OO00O000O000OOO ['status']==200 :#line:623
                    if O0OO00O000O000OOO ['data']['amount']:#line:624
                        OOO0O000OOOO0O00O =O0OO00O000O000OOO ['data']['amount']['gold']#line:625
                        return OOO0O000OOOO0O00O #line:626
                    else :#line:627
                        return 0 #line:628
        except Exception as O00O0OOO0000O0O0O :#line:629
            print (O00O0OOO0000O0O0O )#line:630
    def certification (O00O0O0000O000O00 ):#line:633
        try :#line:634
            O0O000O0O0OO0O000 =f'__{timi_new()}'#line:635
            O0O0OOO000000OOOO ={'source':'scsc','authorization':O00O0O0000O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O0O0OO0O000 ),'signstring':O0O000O0O0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:646
            OO0O00OO0000OOOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0OOO000000OOOO ).json ()#line:647
            if 'status'in OO0O00OO0000OOOOO :#line:649
                if OO0O00OO0000OOOOO ['status']==200 :#line:650
                    if OO0O00OO0000OOOOO ['data']['result']:#line:651
                        OOO00000O000O000O =OO0O00OO0000OOOOO ['data']['nick_name']#line:652
                        return OOO00000O000O000O #line:653
                    else :#line:654
                        weishim .append (O00O0O0000O000O00 .token )#line:655
                        return '未实名'#line:656
        except Exception as OOO0O00OO0O0O0O00 :#line:657
            print (OOO0O00OO0O0O0O00 )#line:658
    def crops_illustrated (O00000OOOO00O0O00 ):#line:661
        try :#line:662
            OO00O00OOOOO00OO0 =f'__{timi_new()}'#line:663
            OOO0OOOOO0000000O ={'source':'scsc','authorization':O00000OOOO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOO00OO0 ),'signstring':OO00O00OOOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:674
            OOO0OOO0O0OOO0OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0OOOOO0000000O ).json ()#line:675
            if 'status'in OOO0OOO0O0OOO0OO0 :#line:677
                if OOO0OOO0O0OOO0OO0 ['status']==200 :#line:678
                    OOO0OO0O0OO000OOO =OOO0OOO0O0OOO0OO0 ['data'][0 ]['crops']#line:679
                    for OOOO0O000OOO00000 in OOO0OO0O0OO000OOO :#line:680
                        if OOOO0O000OOO00000 ['ill_clover_award']:#line:681
                            if float (OOOO0O000OOO00000 ['ill_clover_award'])>1 :#line:682
                                if OOOO0O000OOO00000 ['is_finish']:#line:683
                                    if not OOOO0O000OOO00000 ['is_getit']:#line:684
                                        if O00000OOOO00O0O00 .certification ()!='未实名':#line:685
                                            OO00O00OOOOO00OO0 =f'_award_level={OOOO0O000OOO00000["level"]}_{timi_new()}'#line:686
                                            OOO0OOOOO0000000O ={'source':'scsc','authorization':O00000OOOO00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOO00OO0 ),'signstring':OO00O00OOOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:697
                                            OOO0000OOOOOO0O0O ={"award_level":OOOO0O000OOO00000 ['level']}#line:698
                                            O0000O000OOOOO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0OOOOO0000000O ,json =OOO0000OOOOOO0O0O ).json ()#line:700
                                            if 'status'in O0000O000OOOOO000 :#line:701
                                                if O0000O000OOOOO000 ['status']==200 :#line:702
                                                    O000OO0O0O0OO0O0O =O0000O000OOOOO000 ['data']['ill_clover_award']#line:703
                                                    print (f'【图鉴奖励】:领取{OOOO0O000OOO00000["crop_name"]}成就丨奖励{O000OO0O0O0OO0O0O}☘️')#line:705
                                                if O0000O000OOOOO000 ['status']==500 :#line:706
                                                    print (f'【图鉴奖励】:{O0000O000OOOOO000["message"]}')#line:707
        except Exception as OOO00O0O0OO00000O :#line:708
            print (OOO00O0O0OO00000O )#line:709
    def watched_ad (OO0000O000000000O ):#line:712
        try :#line:713
            O0OOO00O0OO000O0O =f'__{timi_new()}'#line:714
            O00O00O0OOO0O0000 ={'source':'scsc','authorization':OO0000O000000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OO000O0O ),'signstring':O0OOO00O0OO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:725
            O0OO0OO0OO0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O00O00O0OOO0O0000 ).json ()#line:726
            if 'status'in O0OO0OO0OO0OOO00O :#line:728
                if O0OO0OO0OO0OOO00O ['status']==200 :#line:729
                    if 'offlineInfo'in O0OO0OO0OO0OOO00O ['data']:#line:730
                        time .sleep (random .randint (1 ,3 ))#line:731
                        O0OOO00000O0O0000 =O0OO0OO0OO0OOO00O ['data']['offlineInfo']['off_minute']#line:732
                        O0OO0OO00OO0OOO0O =float (O0OO0OO0OO0OOO00O ['data']['silver'])/1000000000000 #line:733
                        time .sleep (1 )#line:734
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O00O0OOO0O0000 ).json ()#line:735
                        time .sleep (2 )#line:736
                        OO0OO0000000O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O00O00O0OOO0O0000 ).json ()#line:737
                        if 'status'in OO0OO0000000O0O0O :#line:739
                            if OO0OO0000000O0O0O ['status']==200 :#line:740
                                OOOOOO00O0O00OO00 =float (OO0OO0000000O0O0O ['data']['silver'])/1000000000000 #line:741
                                O000OOOO0OOO0OOO0 =str (OOOOOO00O0O00OO00 -O0OO0OO00OO0OOO0O )[:6 ]#line:742
                                print (f'【离线奖励】:翻倍离线{O0OOO00000O0O0000}分钟奖励🌱数量:{O000OOOO0OOO0OOO0}t粒')#line:743
        except Exception as OOO0000O00OO0OO0O :#line:744
            print (OOO0000O00OO0OO0O )#line:745
    def user_ad (O000000OOOO00O00O ):#line:748
        try :#line:749
            O0O000O000O0OOO00 =f'__{timi_new()}'#line:750
            O00O00O00O0O0OO00 ={'source':'scsc','authorization':O000000OOOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O000O0OOO00 ),'signstring':O0O000O000O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            O0OOO000000000O0O =requests .request ('get',f'{host}/user/ad',headers =O00O00O00O0O0OO00 ).json ()#line:762
            if 'status'in O0OOO000000000O0O :#line:764
                if O0OOO000000000O0O ['status']==200 :#line:765
                    O000O0OO0O000OO00 =O0OOO000000000O0O ['data']['max_time']#line:766
                    O000OO0000O0O00OO =O0OOO000000000O0O ['data']['watch_time']#line:767
                    OO000O00000O0O0OO =O0OOO000000000O0O ['data']['added_time']#line:768
                    print (f'【获取种子】:获取🌱剩余{OO000O00000O0O0OO + O000O0OO0O000OO00 - O000OO0000O0O00OO}次丨好友提供:{OO000O00000O0O0OO}次')#line:769
                    if OO000O00000O0O0OO +O000O0OO0O000OO00 -O000OO0000O0O00OO >0 :#line:770
                        time .sleep (random .randint (16 ,19 ))#line:771
                        O0O0OO00O0OO00O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O00O00O0O0OO00 ).json ()#line:772
                        if 'status'in O0O0OO00O0OO00O0O :#line:774
                            if O0O0OO00O0OO00O0O ['status']==200 :#line:775
                                OOOO000OOOOO0O000 =float (O0O0OO00O0OO00O0O ['data']['silver'])/1000000000000 #line:776
                                print (f'【获取种子】:获得🌱:{int(OOOO000OOOOO0O000)}t粒')#line:777
                                return True #line:778
                            if O0O0OO00O0OO00O0O ['status']==500 :#line:779
                                OOO0OOOO0OOOO000O =O0O0OO00O0OO00O0O ['message']#line:780
                                print (f'【获取种子】:{OOO0OOOO0OOOO000O}')#line:781
                                return False #line:782
        except Exception as O0O00000O0O000000 :#line:783
            print (O0O00000O0O000000 )#line:784
    def synthetic (O0O00O000O0OOOO0O ):#line:787
        global id ,g #line:788
        try :#line:789
            OOO0OO00O00000O00 =O0O00O000O0OOOO0O .level_new ()#line:790
            O000OO0000OO0000O =random .randint (9 ,11 )#line:791
            OOO000000000OO0O0 =f'_site=8&targetSite={O000OO0000OO0000O}_{timi_new()}'#line:792
            OO0O0OOOOO0O0O0OO ={'source':'scsc','authorization':O0O00O000O0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (OOO000000000OO0O0 ),'signstring':OOO000000000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:803
            OO0000O00OO0000OO ={"site":int (8 ),"targetSite":int (O000OO0000OO0000O )}#line:804
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0OOOOO0O0O0OO ,json =OO0000O00OO0000OO )#line:805
            while True :#line:806
                O00O0OOO00OO00OO0 =f'__{timi_new()}'#line:807
                O0O0OOOOOO0O0O0O0 ={'source':'scsc','authorization':O0O00O000O0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO00OO00OO0 ),'signstring':O00O0OOO00OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:818
                OOOO0OOO0OO000O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOOO0O0O0O0 ).json ()#line:819
                if 'status'in OOOO0OOO0OO000O0O :#line:821
                    if OOOO0OOO0OO000O0O ['status']==200 :#line:822
                        O00OO00000OO00O00 =OOOO0OOO0OO000O0O ['data']['cropList']#line:823
                        OOO0OOOOO00O00O00 =OOOO0OOO0OO000O0O ['data']['gameCoreDataDBid']#line:824
                        O0O0000O0000OO000 =float (OOOO0OOO0OO000O0O ['data']['silver'])/1000000000000 #line:825
                        O00O0OO000O0OOOO0 =0 #line:830
                        for O0O0O0O0OOO0OO0OO in O00OO00000OO00O00 :#line:831
                            if not O0O0O0O0OOO0OO0OO :#line:832
                                O0OOOO000OO00OO0O =f'_crop_id={OOO0OOOOO00O00O00}&site={O00O0OO000O0OOOO0}_{O0O00O000O0OOOO0O.time}'#line:833
                                O00O000OOO000O000 ={'source':'scsc','authorization':O0O00O000O0OOOO0O .token ,'timestamp':O0O00O000O0OOOO0O .time ,'sign':sign (O0OOOO000OO00OO0O ),'signstring':O0OOOO000OO00OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
                                O00OOO0O0O00OOOO0 ={"site":O00O0OO000O0OOOO0 ,"crop_id":OOO0OOOOO00O00O00 }#line:844
                                O0O0OOO000OOO0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =O00O000OOO000O000 ,data =O00OOO0O0O00OOOO0 ).json ()#line:845
                                time .sleep (random .randint (1 ,3 )/10 )#line:847
                                if 'status'in O0O0OOO000OOO0OOO :#line:848
                                    if O0O0OOO000OOO0OOO ['status']==200 :#line:849
                                        if O0O0OOO000OOO0OOO ['message']=='种子数量不足':#line:850
                                            OOO0OO00O00000O00 =O0O00O000O0OOOO0O .level_new ()#line:851
                                            print (f'【种植合成】:{O0O0OOO000OOO0OOO["message"]}')#line:852
                                            if not O0O00O000O0OOOO0O .user_ad ():#line:853
                                                return False #line:854
                                    if O0O0OOO000OOO0OOO ['status']==500 :#line:855
                                        print (f'【种植合成】:{O0O0OOO000OOO0OOO["message"]}')#line:856
                                        return False #line:857
                            O00O0OO000O0OOOO0 +=1 #line:858
                        O00O00OOOO0O0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOOO0O0O0O0 ).json ()#line:859
                        O0O0O00000OOOOO0O =O00O00OOOO0O0O00O ['data']['cropList']#line:860
                        O0OO0OOO00OO0OO0O =False #line:861
                        for O0O0O0O0OOO0OO0OO in range (12 ):#line:862
                            id =O0O0O00000OOOOO0O [O0O0O0O0OOO0OO0OO ]['level']#line:863
                            if float (OOO0OO00O00000O00 )-float (id )>9 :#line:864
                                O0O00O000O00O0OOO =f'_site={O0O0O0O0OOO0OO0OO}_{timi_new()}'#line:865
                                O0000000OO0OOOO0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O000O0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0O00O000O00O0OOO ),'signstring':O0O00O000O00O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:876
                                O00O00OOO000OOO00 ={"site":O0O0O0O0OOO0OO0OO }#line:877
                                OO0OOO00O0OOOOOO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0000000OO0OOOO0O ,data =O00O00OOO000OOO00 ).json ()#line:879
                                if 'status'in OO0OOO00O0OOOOOO0 :#line:880
                                    if OO0OOO00O0OOOOOO0 ['status']==200 :#line:881
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:882
                            if id !=0 :#line:883
                                for O0000OO00O00000OO in range (11 ):#line:884
                                    O000OO0OO00OOOOOO =O0000OO00O00000OO +1 #line:885
                                    g =O0O0O00000OOOOO0O [O000OO0OO00OOOOOO ]['level']#line:886
                                    if id ==g :#line:887
                                        O0OO0O0O00000OO0O =O0000OO00O00000OO +2 #line:888
                                        if O0OO0O0O00000OO0O !=O0O0O0O0OOO0OO0OO +1 :#line:889
                                            O0O00O00OOOOO00OO =O0O0O0O0OOO0OO0OO +1 #line:890
                                            time .sleep (random .randint (1 ,3 )/10 )#line:892
                                            OOO000000000OO0O0 =f'_site={O0O00O00OOOOO00OO - 1}&targetSite={O0OO0O0O00000OO0O - 1}_{timi_new()}'#line:893
                                            OO0O0OOOOO0O0O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O000O0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (OOO000000000OO0O0 ),'signstring':OOO000000000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:910
                                            OO000000OO0O0OO00 ={"site":int (O0O00O00OOOOO00OO -1 ),"targetSite":int (O0OO0O0O00000OO0O -1 )}#line:911
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0OOOOO0O0O0OO ,json =OO000000OO0O0OO00 )#line:912
                                            O0OO0OOO00OO0OO0O =True #line:914
                                    if O0OO0OOO00OO0OO0O :#line:915
                                        break #line:916
                                if O0OO0OOO00OO0OO0O :#line:917
                                    break #line:918
        except :#line:919
            O0O00O000O0OOOO0O .synthetic ()#line:920
    def level_new (O000000O00OOO0OO0 ):#line:923
        try :#line:924
            O0O0000O00O00OO00 =f'__{timi_new()}'#line:925
            OOO0O00OO0OO0OO0O ={'source':'scsc','authorization':O000000O00OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O00O00OO00 ),'signstring':O0O0000O00O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:936
            O00O0O0O0O00O000O =requests .request ('get',f'{host}/user',headers =OOO0O00OO0OO0OO0O ).json ()#line:937
            if 'status'in O00O0O0O0O00O000O :#line:938
                if O00O0O0O0O00O000O ['status']==200 :#line:939
                    return float (O00O0O0O0O00O000O ['data']['level'])#line:940
        except Exception as O00OOO0OOOO0O000O :#line:941
            print (O00OOO0OOOO0O000O )#line:942
    def propsraffle (O0O0O0OOO0OO00OOO ):#line:945
        try :#line:946
            while True :#line:947
                OOOOOOOO00O0O0O00 =f'__{timi_new()}'#line:948
                OO00OO0OO0000O00O ={'source':'scsc','authorization':O0O0O0OOO0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO00O0O0O00 ),'signstring':OOOOOOOO00O0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                OOOOO00000OO00OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00OO0OO0000O00O ).json ()#line:960
                if 'status'in OOOOO00000OO00OOO :#line:962
                    if OOOOO00000OO00OOO ['status']==200 :#line:963
                        O0O0O000O0O00O00O =OOOOO00000OO00OOO ['data']['rows']#line:964
                        OOOOOO0OO0000O0OO =OOOOO00000OO00OOO ['data']['vstate']#line:965
                        if O0O0O000O0O00O00O ==5 or O0O0O000O0O00O00O ==6 or O0O0O000O0O00O00O ==7 :#line:966
                            O0O00O0OO0OO000O0 =OOOOO00000OO00OOO ['data']['silver']#line:967
                            print (f'【转盘抽奖】:获得种子:{O0O00O0OO0OO000O0}')#line:968
                        if O0O0O000O0O00O00O ==1 or O0O0O000O0O00O00O ==2 or O0O0O000O0O00O00O ==3 :#line:969
                            OO0O0O000OO00OOO0 =OOOOO00000OO00OOO ['data']['clover']#line:970
                            print (f'【转盘抽奖】:获得三叶草:{OO0O0O000OO00OOO0}')#line:971
                        if O0O0O000O0O00O00O ==4 or O0O0O000O0O00O00O ==8 :#line:972
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:973
                        if O0O0O000O0O00O00O =='抽奖次数已用完':#line:977
                            break #line:1011
                time .sleep (random .randint (8 ,15 )/10 )#line:1012
        except Exception as OOO0O00OOOO00O000 :#line:1013
            print (OOO0O00OOOO00O000 )#line:1014
    def friends_invitation (OO00OOO0O00OOOOO0 ):#line:1017
        try :#line:1018
            OO00O00OO0OOO000O =f'__{timi_new()}'#line:1019
            O0OOO000O000OO0OO ={'source':'scsc','authorization':OO00OOO0O00OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO0OOO000O ),'signstring':OO00O00OO0OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1030
            O0O0O00O000OO0O0O =requests .request ('get',f'{host}/friends',headers =O0OOO000O000OO0OO ).json ()#line:1031
            if 'status'in O0O0O00O000OO0O0O :#line:1032
                if O0O0O00O000OO0O0O ['status']==200 :#line:1033
                    O0OOO0O00OO00OOO0 =O0O0O00O000OO0O0O ['data']['myInviteter']#line:1034
                    if O0OOO0O00OO00OOO0 :#line:1035
                        O0000O0OOOO0O00O0 =O0OOO0O00OO00OOO0 ['user']['nickname']#line:1036
                        O00OO0OO000OO0OOO =OO00OOO0O00OOOOO0 .certification ()#line:1037
                        print (f'【查邀请人】:我的邀请人:{O0000O0OOOO0O00O0}丨实名:{O00OO0OO000OO0OOO}')#line:1038
                    else :#line:1039
                        if OO00OOO0O00OOOOO0 .innerId !='0':#line:1040
                            OO00OOO0O00OOOOO0 .invitation ()#line:1041
        except Exception as OO00OO000OOOO00OO :#line:1042
            print (OO00OO000OOOO00OO )#line:1043
    def add_clover (O0O0O000OO0OOOOO0 ):#line:1046
        global golden_seed #line:1047
        try :#line:1048
            OO0000000O00OO000 =f'__{timi_new()}'#line:1049
            OOOOOO00OO000O000 ={'source':'scsc','authorization':O0O0O000OO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O00OO000 ),'signstring':OO0000000O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1060
            O00O0000O00O0OO0O =requests .request ('get',f'{host}/assets/clovers',headers =OOOOOO00OO000O000 ).json ()#line:1061
            if 'status'in O00O0000O00O0OO0O :#line:1063
                if O00O0000O00O0OO0O ['status']==200 :#line:1064
                    O0000000O0O0O00O0 =O00O0000O00O0OO0O ['data']['clover']#line:1065
                    OOO0O00OO00OO0O0O =O00O0000O00O0OO0O ['data']['used_clover']#line:1066
                    OO0O0O0OO0O0O0O00 =float (O0000000O0O0O00O0 )-float (OOO0O00OO00OO0O0O )#line:1067
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O00OO00OO0O0O}')#line:1068
                    if O0O0O000OO0OOOOO0 .certification ()!='未实名':#line:1069
                        if OO0O0O0OO0O0O0O00 >1 :#line:1070
                            OO0000000O00OO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0O0OO0O0O0O00)}_{timi_new()}'#line:1071
                            O0O0O0O0OO0000OOO ={'source':'scsc','authorization':O0O0O000OO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O00OO000 ),'signstring':OO0000000O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1082
                            OO000O0OO0000O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0O0OO0O0O0O00 )}#line:1083
                            OO000O000OOOOO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0O0O0OO0000OOO ,data =OO000O0OO0000O0O0 ).json ()#line:1084
                            if 'status'in OO000O000OOOOO0O0 :#line:1086
                                if OO000O000OOOOO0O0 ['status']==200 :#line:1087
                                    print (f'【参与抽奖】:添加☘️:{OO000O000OOOOO0O0["data"]}丨数量:{OO0O0O0OO0O0O0O00}')#line:1088
                                if OO000O000OOOOO0O0 ['status']==500 :#line:1089
                                    print (f'【参与抽奖】:添加☘️:{OO000O000OOOOO0O0["message"]}')#line:1090
            OO00O00OOOO0OOOO0 =requests .request ('get',f'{host}/lottery',headers =OOOOOO00OO000O000 ).json ()#line:1091
            OO000O00OOOOOOO00 =O0O0O000OO0OOOOO0 .winning_rewards ()#line:1093
            if 'status'in OO00O00OOOO0OOOO0 :#line:1094
                if OO00O00OOOO0OOOO0 ['status']==200 :#line:1095
                    OO000OOO00O000000 =OO00O00OOOO0OOOO0 ['data'][0 ]['day_get_gold_quantity']#line:1096
                    golden_seed +=float (OO000OOO00O000000 )#line:1097
                    OOOOO0O000O0OOO00 =OO00O00OOOO0OOOO0 ['data'][1 ]['value']#line:1098
                    OO0OO0OO0OOOO00O0 =OO00O00OOOO0OOOO0 ['data'][0 ]['join_number']#line:1099
                    OOOOOO0O00O0000OO =int (float (OO00O00OOOO0OOOO0 ['data'][0 ]['totalValue']))#line:1100
                    O0OOOOOO0000000OO =float (OOOOO0O000O0OOO00 /OOOOOO0O00O0000OO )*10000 #line:1101
                    OO0OO00O00O0O0000 =OOOOOO0O00O0000OO /OO0OO0OO0OOOO00O0 #line:1102
                    print (f'【参与抽奖】:预计每天中{str(OO000OOO00O000000)[:6]}颗金种子丨好友收益:{str(OO000O00OOOOOOO00)[:6]}')#line:1103
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOOOOO0000000OO)[:6]}颗金种子丨☘️人均:{str(OO0OO00O00O0O0000)[:7]}️')#line:1104
        except Exception as O00OO00O0O0OOOOO0 :#line:1105
            print (O00OO00O0O0OOOOO0 )#line:1106
    def energy (O00O0OOO0OO0OO00O ):#line:1109
        try :#line:1110
            while True :#line:1111
                O00O0O0O0O0OOOOO0 =f'__{timi_new()}'#line:1112
                OO000000OOOOO000O ={'source':'scsc','authorization':O00O0OOO0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0O0OOOOO0 ),'signstring':O00O0O0O0O0OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1123
                O0000O0000O0O0OOO =requests .request ('get',f'{host}/energy/general',headers =OO000000OOOOO000O ).json ()#line:1124
                if 'status'in O0000O0000O0O0OOO :#line:1126
                    if O0000O0000O0O0OOO ['status']==200 :#line:1127
                        O0OOOOO000OO00O0O =O0000O0000O0O0OOO ['data']['ordinary_water']#line:1128
                        O0OO0OO000OO000OO =O0000O0000O0O0OOO ['data']['ordinary_fertilizer']#line:1129
                        OO00000O00O0OO0O0 =O0000O0000O0O0OOO ['data']['videoStatus']#line:1130
                        OOOO0OOOO00O0OOO0 =O0000O0000O0O0OOO ['data']['waterVideoKey']#line:1131
                        print (f'【我的营养】:肥料:{str(O0OO0OO000OO000OO).split(".")[0]}丨水滴:{str(O0OOOOO000OO00O0O).split(".")[0]}')#line:1133
                        if float (O0OO0OO000OO000OO )<96 :#line:1134
                            if OO00000O00O0OO0O0 :#line:1135
                                time .sleep (random .randint (160 ,180 )/10 )#line:1136
                                O0000O0O00OOO0O0O =99 -float (O0OO0OO000OO000OO )#line:1137
                                O0OO0O0000OO0000O ={"fertilizer":str (O0000O0O00OOO0O0O ).split ('.')[0 ]}#line:1138
                                O00OOO000OO00OO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO000000OOOOO000O ).json ()#line:1140
                                if 'status'in O00OOO000OO00OO00 :#line:1142
                                    if O00OOO000OO00OO00 ['status']==200 :#line:1143
                                        print (f'【购买肥料】:看广告获取肥料:{O00OOO000OO00OO00["message"]}')#line:1144
                                    if O00OOO000OO00OO00 ['status']==500 :#line:1145
                                        print (f'【购买肥料】:看广告获取肥料:{O00OOO000OO00OO00["message"]}')#line:1146
                                        break #line:1147
                                if float (O0OO0OO000OO000OO )<78 :#line:1149
                                    O0000O0O00OOO0O0O =80 -float (O0OO0OO000OO000OO )#line:1150
                                    O000OO00O0OOOO0O0 =f'_fertilizer={int(O0000O0O00OOO0O0O)}_{timi_new()}'#line:1151
                                    O0000OOOO0O00000O ={'source':'scsc','authorization':O00O0OOO0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00O0OOOO0O0 ),'signstring':O000OO00O0OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                                    OOOO0000O0OO00O00 ={"fertilizer":int (O0000O0O00OOO0O0O )}#line:1163
                                    OO00OO00O0O00OO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0000OOOO0O00000O ,data =OOOO0000O0OO00O00 ).json ()#line:1165
                                    if 'status'in OO00OO00O0O00OO00 :#line:1167
                                        if OO00OO00O0O00OO00 ['status']==200 :#line:1168
                                            print (f'【购买肥料】:购买肥料:{OO00OO00O0O00OO00["message"]}丨数量:{int(O0000O0O00OOO0O0O)}')#line:1169
                                        if OO00OO00O0O00OO00 ['status']==500 :#line:1170
                                            print (f'【购买肥料】:购买肥料:{OO00OO00O0O00OO00["message"]}丨数量:{int(O0000O0O00OOO0O0O)}')#line:1171
                                            O00O00O0OO0O000OO =OO00OO00O0O00OO00 ["message"].split ('-')[1 ]#line:1172
                                            O0OO0OO0OOO0OOO0O =f'__{timi_new()}'#line:1173
                                            O00O00OOOO00OO0O0 ={'source':'scsc','authorization':O00O0OOO0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOO0OOO0O ),'signstring':O0OO0OO0OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1184
                                            O000O00000O0OO00O =requests .request ('get',f'{host}/user',headers =O00O00OOOO00OO0O0 ).json ()#line:1185
                                            if 'status'in O000O00000O0OO00O :#line:1186
                                                if O000O00000O0OO00O ['status']==200 :#line:1187
                                                    O0000O0OO0000O000 =O000O00000O0OO00O ['data']['inner_id']#line:1188
                                                    if give_gold (O0000O0OO0000O000 ,float (O00O00O0OO0O000OO )+1 ):#line:1189
                                                        O00O0OOO0OO0OO00O .energy ()#line:1190
                        if float (O0OOOOO000OO00O0O )<880 :#line:1191
                            if OOOO0OOOO00O0OOO0 :#line:1192
                                time .sleep (random .randint (160 ,180 )/10 )#line:1193
                                O00000O0OOO0O00O0 =999 -float (O0OOOOO000OO00O0O )#line:1194
                                O000O0OO000000O0O ={"water":str (O00000O0OOO0O00O0 ).split ('.')[0 ]}#line:1195
                                O0O00OOO0OOO0OOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO000000OOOOO000O ).json ()#line:1197
                                if 'status'in O0O00OOO0OOO0OOO0 :#line:1199
                                    if O0O00OOO0OOO0OOO0 ['status']==200 :#line:1200
                                        print (f'【购买水滴】:看广告获取水滴:{O0O00OOO0OOO0OOO0["message"]}')#line:1201
                                    if O0O00OOO0OOO0OOO0 ['status']==500 :#line:1202
                                        print (f'【购买水滴】:看广告获取水滴:{O0O00OOO0OOO0OOO0["message"]}')#line:1203
                                        break #line:1204
                                if float (O0OOOOO000OO00O0O )<780 :#line:1205
                                    O00000O0OOO0O00O0 =800 -float (O0OOOOO000OO00O0O )#line:1206
                                    O0O0O0O0000O0OO00 =f'_water={int(O00000O0OOO0O00O0)}_{timi_new()}'#line:1207
                                    OOOOO0O000OOOO000 ={'source':'scsc','authorization':O00O0OOO0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O0000O0OO00 ),'signstring':O0O0O0O0000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1218
                                    O0000O0O0OO0O0OOO ={"water":int (O00000O0OOO0O00O0 )}#line:1219
                                    O000O0O000OO000O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOOO0O000OOOO000 ,data =O0000O0O0OO0O0OOO ).json ()#line:1221
                                    if 'status'in O000O0O000OO000O0 :#line:1223
                                        if O000O0O000OO000O0 ['status']==200 :#line:1224
                                            print (f'【购买水滴】:购买水滴:{O000O0O000OO000O0["message"]}丨数量:{int(O00000O0OOO0O00O0)}')#line:1225
                                        if O000O0O000OO000O0 ['status']==500 :#line:1226
                                            print (f'【购买水滴】:购买水滴:{O000O0O000OO000O0["message"]}丨数量:{int(O00000O0OOO0O00O0)}')#line:1227
                                            O00O00O0OO0O000OO =O000O0O000OO000O0 ["message"].split ('-')[1 ]#line:1228
                                            O0OO0OO0OOO0OOO0O =f'__{timi_new()}'#line:1229
                                            O00O00OOOO00OO0O0 ={'source':'scsc','authorization':O00O0OOO0OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOO0OOO0O ),'signstring':O0OO0OO0OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1240
                                            O000O00000O0OO00O =requests .request ('get',f'{host}/user',headers =O00O00OOOO00OO0O0 ).json ()#line:1241
                                            if 'status'in O000O00000O0OO00O :#line:1242
                                                if O000O00000O0OO00O ['status']==200 :#line:1243
                                                    O0000O0OO0000O000 =O000O00000O0OO00O ['data']['inner_id']#line:1244
                                                    if give_gold (O0000O0OO0000O000 ,float (O00O00O0OO0O000OO )+1 ):#line:1245
                                                        O00O0OOO0OO0OO00O .energy ()#line:1246
                        break #line:1247
        except Exception as O0O0000O0O0O00O00 :#line:1248
            print (O0O0000O0O0O00O00 )#line:1249
def bundled_def ():#line:1252
    O0OOO0OO0O0O0O0O0 =['5570536','7750212','7911652','7911680','7805624']#line:1253
    return O0OOO0OO0O0O0O0O0 [random .randint (0 ,len (O0OOO0OO0O0O0O0O0 )-1 )]#line:1254
def version_of_the_validation ():#line:1258
    return str ((94 -56 )/10 )#line:1259
def sc2 ():#line:1262
    return "19319#$%^&*((*"#line:1263
def OO00OO0OO0OO00OO00o0 ():#line:1266
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1268
def get_ip ():#line:1271
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1273
def gitee_validation ():#line:1276
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1277
def gitee_edition ():#line:1280
    try :#line:1281
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1282
    except :#line:1283
        sys .exit (0 )#line:1284
def O000OO000O0O00OOO00 ():#line:1288
    try :#line:1289
        OO00OOOO00OOOOOO0 =gitee_edition ()#line:1290
        if version_of_the_validation ()<OO00OOOO00OOOOOO0 ['CityEarth']['edition']:#line:1291
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOOO00OOOOOO0["CityEarth"]["edition"]}   ❌')#line:1292
            print (f'更新内容=>>{OO00OOOO00OOOOOO0["CityEarth"]["content"]}')#line:1293
        else :#line:1294
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OOOO00OOOOOO0["CityEarth"]["edition"]}   ✅')#line:1295
            print (f'更新内容=>> {OO00OOOO00OOOOOO0["CityEarth"]["content"]}')#line:1296
    except Exception as OO000O000O0OO0OOO :#line:1297
        print (OO000O000O0OO0OOO )#line:1298
def sc3 ():#line:1301
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1302
if __name__ =='__main__':#line:1305
    start ()#line:1306
