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
@ 版本  4.5
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
count_list =0 #line:5
price_new =0 #line:6
msg_list =[]#line:7
invited_new =[]#line:8
weishim =[]#line:9
def start ():#line:12
    try :#line:13
        O000OO000O0O00OOO00 ()#line:14
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:15
        O000OO0O00OO00O00 ()#line:16
        OOO00O00O00OO0OO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:17
        print (f"==========共找到{len(OOO00O00O00OO0OO0)}个账号==========")#line:18
        for OO00O0O0OOO00OOOO in OOO00O00O00OO0OO0 :#line:19
            OO0OO00OOOOOO0OO0 =[]#line:20
            print (f"------------正在执行第{OOO00O00O00OO0OO0.index(OO00O0O0OOO00OOOO) + 1}个账号------------")#line:21
            OOO000O0OOO0OOOOO =CityEarth (OO00O0O0OOO00OOOO ,OO0OO00OOOOOO0OO0 ,OOO00O00O00OO0OO0 .index (OO00O0O0OOO00OOOO ))#line:22
            def O0OO00O0O00OOO0O0 ():#line:24
                if OOO000O0OOO0OOOOO .base_info ():#line:26
                    OOO000O0OOO0OOOOO .sealing ()#line:28
                    OOO000O0OOO0OOOOO .invitenum ()#line:30
                    OOO000O0OOO0OOOOO .query_to_sell ()#line:32
                    OOO000O0OOO0OOOOO .friends_invitation ()#line:36
                    OOO000O0OOO0OOOOO .energy ()#line:38
                    OOO000O0OOO0OOOOO .add_clover ()#line:40
                    OOO000O0OOO0OOOOO .propsraffle ()#line:42
                    OOO000O0OOO0OOOOO .synthetic ()#line:44
                    OOO000O0OOO0OOOOO .crops_illustrated ()#line:46
                    OOO000O0OOO0OOOOO .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OOO000O0OOO0OOOOO .give_gold ()#line:51
            O0O000O0OO000000O =threading .Thread (target =O0OO00O0O00OOO0O0 )#line:53
            O0O000O0OO000000O .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        O0000OO0OOO0OOOOO =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0000OO0OOO0OOOOO +' ')#line:59
        time .sleep (15 )#line:60
        print (f'所有未出售的芦荟:{count_list}颗')#line:61
        print ('开始打印好友数量不足2的ID')#line:62
        for OO00O00O00000OO0O in invited_new :#line:63
            print (OO00O00O00000OO0O )#line:64
        print ('开始打印未实名的token')#line:65
        for O000O0O000O000OO0 in weishim :#line:66
            print (O000O0O000O000OO0 )#line:67
    except Exception as O0OO000OO00OO000O :#line:68
        print (O0OO000OO00OO000O )#line:69
def give_gold (OOOOO00O00O0OO0OO ,O0OO0O0O000OO0000 ):#line:73
    try :#line:74
        O0000O0OO0000OO0O =f'_doneeNo={OOOOO00O00O0OO0OO}&quantity={int(O0OO0O0O000OO0000)}_{timi_new()}'#line:75
        OO000O0OOO0000OO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000O0OO0000OO0O ),'signstring':O0000O0OO0000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:86
        O0OO0OOO0O0000O0O ={"quantity":int (O0OO0O0O000OO0000 ),"doneeNo":OOOOO00O00O0OO0OO }#line:90
        OO00OOOO00O0OOOOO =requests .request ('post',f'{host}/finance/give-gold',headers =OO000O0OOO0000OO0 ,data =O0OO0OOO0O0000O0O ).json ()#line:91
        if 'status'in OO00OOOO00O0OOOOO :#line:93
            if OO00OOOO00O0OOOOO ['status']==200 :#line:94
                if OO00OOOO00O0OOOOO ['data']:#line:95
                    print (f'【赠送种子】:赠送{int(O0OO0O0O000OO0000)}种子给{OOOOO00O00O0OO0OO}成功')#line:96
                    return True #line:97
            if OO00OOOO00O0OOOOO ['status']==401 :#line:98
                print (f'【赠送种子】:{OO00OOOO00O0OOOOO["message"]}')#line:99
                return False #line:100
            if OO00OOOO00O0OOOOO ['status']==500 :#line:101
                print (f'【赠送种子】:{OO00OOOO00O0OOOOO["message"]}')#line:102
                return False #line:103
        return False #line:104
    except Exception as OO0O0000O00O0OOOO :#line:105
        print (OO0O0000O00O0OOOO )#line:106
def kvkv ():#line:109
    return '/vastzzzl/vastzzzl/raw/master'#line:110
def oyoy ():#line:112
    return '卡密未激活   ❌'#line:113
def sign (O0000OOO0OOOOO000 ):#line:116
    OO0O0O000OOOOO0O0 =hashlib .md5 (O0000OOO0OOOOO000 .encode ()).hexdigest ()#line:117
    OOO00OOO0OO0000O0 =sc1 ()#line:118
    OOOOOO000OO0O000O =sc2 ()#line:119
    O000O0OO0O000000O =sc3 ()#line:120
    OO00OO00O0OO00OOO =OOO00OOO0OO0000O0 +OO0O0O000OOOOO0O0 +OOOOOO000OO0O000O +O000O0OO0O000000O #line:121
    O0O0OOOO000000OO0 =hashlib .md5 (OO00OO00O0OO00OOO .encode ()).hexdigest ()#line:122
    return O0O0OOOO000000OO0 #line:123
def format_msg ():#line:126
    O00O0OO00OO0000O0 =""#line:127
    for OO00OO00000O0OOOO in msg_list :#line:128
        O00O0OO00OO0000O0 +=str (OO00OO00000O0OOOO )+"\r\n"#line:129
    return O00O0OO00OO0000O0 #line:130
def sc1 ():#line:133
    return "scsc%^&*"#line:134
def O000OO0O00OO00O00 ():#line:137
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:138
        ubbbf ()#line:139
    else :#line:140
        print (oyoy ())#line:141
        exit (1 )#line:142
def timi_new ():#line:145
    return str (int (time .time ()*1000 ))#line:146
json_path ="CityEarth_data.json"#line:149
json_path1 ="CityEarth_data.json"#line:150
dict ={}#line:151
def get_json_data (O0000OO00O0O00OOO ,OO0O0OO0OOO0OO00O ,OO00O0OO0O0OOO00O ,OOOO0OO0O0OO0OOO0 ):#line:154
    with open (O0000OO00O0O00OOO ,'rb')as O0OO00O00000000O0 :#line:155
        OOO0OO000OO00000O =json .load (O0OO00O00000000O0 )#line:156
        OOO0OO000OO00000O ['data'][OO0O0OO0OOO0OO00O ][OO00O0OO0O0OOO00O ]=OOOO0OO0O0OO0OOO0 #line:157
        OO00OOOOOOOO00000 =OOO0OO000OO00000O #line:158
    O0OO00O00000000O0 .close ()#line:159
    return OO00OOOOOOOO00000 #line:160
def write_json_data (O0OOO00O0000O000O ):#line:163
    with open (json_path1 ,'w')as OOOO0OO000O00OOO0 :#line:164
        json .dump (O0OOO00O0000O000O ,OOOO0OO000O00OOO0 )#line:165
    OOOO0OO000O00OOO0 .close ()#line:166
    return True #line:167
class CityEarth :#line:170
    def __init__ (OOOO000O00OO0OO00 ,O0OO0O0OOO00O00OO ,O000OO00O0OO0OO00 ,OO0OOOO0OOO0OOOOO ):#line:172
        try :#line:173
            OOOO000O00OO0OO00 .msg =O000OO00O0OO0OO00 #line:174
            OOOO000O00OO0OO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:175
            OOOO000O00OO0OO00 .token =O0OO0O0OOO00O00OO ['authorization']#line:176
            OOOO000O00OO0OO00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:177
            OOOO000O00OO0OO00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:178
            OOOO000O00OO0OO00 .elephant_user =O0OO0O0OOO00O00OO ['elephant_user']#line:179
            OOOO000O00OO0OO00 .elephant_pswd =O0OO0O0OOO00O00OO ['elephant_pswd']#line:180
            OOOO000O00OO0OO00 .elephant_Task_ID =O0OO0O0OOO00O00OO ['elephant_Task_ID']#line:181
            OOOO000O00OO0OO00 .len_new =OO0OOOO0OOO0OOOOO #line:182
        except :#line:183
            print ('变量格式错误')#line:184
    def base_info (OO0OOOO0O0O0O0OO0 ):#line:187
        try :#line:188
            OO0OOOO0O0O0O0OO0 .watched_ad ()#line:190
            O0O000O00OO0O000O =f'__{timi_new()}'#line:191
            OOOO0O000O0O0OOOO ={'source':'scsc','authorization':OO0OOOO0O0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O00OO0O000O ),'signstring':O0O000O00OO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:202
            O0000OO0O0000O0O0 =requests .request ('get',f'{host}/user',headers =OOOO0O000O0O0OOOO ).json ()#line:203
            if 'status'in O0000OO0O0000O0O0 :#line:205
                if O0000OO0O0000O0O0 ['status']==200 :#line:206
                    OOOOOO0O0O00OO0O0 =O0000OO0O0000O0O0 ['data']['nickname']#line:207
                    OOOO00O000OO0OOOO =O0000OO0O0000O0O0 ['data']['inner_id']#line:208
                    O0OOOO0OO0OOO000O =O0000OO0O0000O0O0 ['data']['assets']['gold']#line:209
                    O00OOOOOO0O0OOOO0 =O0000OO0O0000O0O0 ['data']['level']#line:210
                    print (f'【账号信息】:昵称:{OOOOOO0O0O00OO0O0[:5]}丨ID:{OOOO00O000OO0OOOO}丨等级:{O00OOOOOO0O0OOOO0}丨金种子:{str(O0OOOO0OO0OOO000O).split(".")[0]}')#line:212
                    if 'wx_'in OOOOOO0O0O00OO0O0 :#line:213
                        OO0OOOO0O0O0O0OO0 .change_nickname ()#line:214
                if O0000OO0O0000O0O0 ['status']==401 :#line:215
                    print ('【账号信息】:账号失效正在尝试登录')#line:216
                    if OO0OOOO0O0O0O0OO0 .elephant_user =='f':#line:217
                        return False #line:218
                    O00OO0O0OOOO0000O =Invalid_login .addtask (elephant_user =OO0OOOO0O0O0O0OO0 .elephant_user ,elephant_pswd =OO0OOOO0O0O0O0OO0 .elephant_pswd ,elephant_Task_ID =OO0OOOO0O0O0O0OO0 .elephant_Task_ID )#line:221
                    O0O00OOO0O0000O00 =get_json_data (json_path ,OO0OOOO0O0O0O0OO0 .len_new ,'authorization',O00OO0O0OOOO0000O )#line:222
                    if write_json_data (O0O00OOO0O0000O00 ):#line:223
                        print ('正在写入账号配置文件')#line:224
                    return False #line:225
                if O0000OO0O0000O0O0 ['status']==500 :#line:226
                    return False #line:227
            return True #line:228
        except Exception as O0OOOO0O00OOOOOO0 :#line:229
            print (O0OOOO0O00OOOOOO0 )#line:230
    def sealing (OO00O0OO00O0OOO0O ):#line:233
        try :#line:234
            O0O0OO000000O00OO =f'__{timi_new()}'#line:235
            O0O0OOOOOOOOOO000 ={'source':'scsc','authorization':OO00O0OO00O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000000O00OO ),'signstring':O0O0OO000000O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:246
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0OOOOOOOOOO000 )#line:247
            requests .request ('get',f'{host}/packsack/list',headers =O0O0OOOOOOOOOO000 )#line:248
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0OOOOOOOOOO000 )#line:249
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0OOOOOOOOOO000 )#line:250
            requests .request ('get',f'{host}/user',headers =O0O0OOOOOOOOOO000 )#line:251
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0OOOOOOOOOO000 )#line:252
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0OOOOOOOOOO000 )#line:253
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0OOOOOOOOOO000 )#line:254
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOOOOOOOO000 )#line:255
            requests .request ('get',f'{host}/assets',headers =O0O0OOOOOOOOOO000 )#line:256
        except Exception as O00O000O0OOOO00O0 :#line:257
            print (O00O000O0OOOO00O0 )#line:258
    def ddd (O000OO00O000OO000 ):#line:260
        try :#line:261
            O0O00OO00OOOOOO0O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:262
            OOO000OOO00OO0OOO ={'source':'scsc','authorization':O000OO00O000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OOOOOO0O ),'signstring':O0O00OO00OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:273
            O0O0000000O000OOO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO000OOO00OO0OOO ).json ()#line:274
            print (O0O0000000O000OOO )#line:275
        except Exception as O000O00OOO00000O0 :#line:278
            print (O000O00OOO00000O0 )#line:279
    def the_query (O000OOO000OOO0OOO ):#line:284
        global price_new #line:285
        try :#line:286
            O00OOOO00OOOO0OO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:287
            O00000O00O0OO0O0O ={'authorization':O000OOO000OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OOOO0OO0 ),'signstring':O00OOOO00OOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:297
            OO000O0OO000OO0O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00000O00O0OO0O0O ).json ()#line:299
            if 'status'in OO000O0OO000OO0O0 :#line:301
                if OO000O0OO000OO0O0 ['status']==200 :#line:302
                    OOOO0000O0O00OO00 =OO000O0OO000OO0O0 ['data']['rows'][4 ]['price']#line:303
                    price_new =OOOO0000O0O00OO00 #line:304
                    O000OOO000OOO0OOO .market_sale (OOOO0000O0O00OO00 )#line:305
        except Exception as O0OO0O00O0OOOO0OO :#line:306
            print (O0OO0O00O0OOOO0OO )#line:307
    def market_sale (O0O0000O0O0OO000O ,O0O0OOOO00O0OOOOO ):#line:310
        try :#line:311
            O00OO0OO0O00O00O0 =timi_new ()#line:312
            O0OOOOOOOO0OOOOO0 =f'type=crop__{O00OO0OO0O00O00O0}'#line:313
            OOOO00OOOO0O0OO0O ={'source':'scsc','authorization':O0O0000O0O0OO000O .token ,'timestamp':str (O00OO0OO0O00O00O0 ),'sign':sign (O0OOOOOOOO0OOOOO0 ),'signstring':O0OOOOOOOO0OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:324
            OOO0OO0O0OO0O00OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOO00OOOO0O0OO0O ).json ()#line:326
            if 'status'in OOO0OO0O0OO0O00OO :#line:328
                if OOO0OO0O0OO0O00OO ['status']==200 :#line:329
                    if OOO0OO0O0OO0O00OO ['data']['rows']:#line:330
                        O0O0OO0OOO0O0O0O0 =OOO0OO0O0OO0O00OO ['data']['rows'][0 ]['packsackItemId']#line:331
                        O00O0O00OOOOO0OOO =OOO0OO0O0OO0O00OO ['data']['rows'][0 ]['quantity']#line:332
                        OO0OOOO000000O00O =float (O0O0OOOO00O0OOOOO )-0.001 #line:333
                        if OO0OOOO000000O00O >9 :#line:334
                            O0O00000O0O000000 =f'_packsackItemId={O0O0OO0OOO0O0O0O0}&price={str(O0O0OOOO00O0OOOOO)[:5]}&quantity={O00O0O00OOOOO0OOO}_{O00OO0OO0O00O00O0}'#line:335
                            OO00000O000OOOOO0 ={'source':'scsc','authorization':O0O0000O0O0OO000O .token ,'timestamp':str (O00OO0OO0O00O00O0 ),'sign':sign (O0O00000O0O000000 ),'signstring':O0O00000O0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
                            O0O00OOOOOOOO00OO ={"packsackItemId":O0O0OO0OOO0O0O0O0 ,"price":str (O0O0OOOO00O0OOOOO )[:5 ],"quantity":str (O00O0O00OOOOO0OOO )}#line:351
                            O000OOO000000O00O =requests .request ('post',f'{host}/market/sale',headers =OO00000O000OOOOO0 ,data =O0O00OOOOOOOO00OO ).json ()#line:352
                            if 'status'in O000OOO000000O00O :#line:354
                                if O000OOO000000O00O ['status']==200 :#line:355
                                    print (f'【上架芦荟】:数量:{O00O0O00OOOOO0OOO}丨价格:{str(O0O0OOOO00O0OOOOO)[:5]}')#line:356
        except Exception as OO00O0O0O0O0OO000 :#line:357
            print (OO00O0O0O0O0OO000 )#line:358
    def query_to_sell (O00O000O00O000OO0 ):#line:361
        try :#line:362
            O000O0000O00000OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:363
            O000O00OOO0O0O000 ={'source':'scsc','authorization':O00O000O00O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0000O00000OO ),'signstring':O000O0000O00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:374
            OOOO0OOO0O0000OO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O000O00OOO0O0O000 ).json ()#line:375
            if 'status'in OOOO0OOO0O0000OO0 :#line:377
                if OOOO0OOO0O0000OO0 ['status']==200 :#line:378
                    for O0O00OOOO0OO0000O in OOOO0OOO0O0000OO0 ['data']['rows']:#line:379
                        O00O0O0O0O0OOOOOO =O0O00OOOO0OO0000O ['materialKey']#line:380
                        O000OOO0O0OOO0O0O =O0O00OOOO0OO0000O ['quantity']#line:381
                        OO00OOO00000OO0O0 =O0O00OOOO0OO0000O ['price']#line:382
                        O0O0O0OOO00OOOOOO =O0O00OOOO0OO0000O ['saleState']#line:383
                        if O0O0O0OOO00OOOOOO ==0 :#line:384
                            print (f'【出售订单】:名称:{O00O0O0O0O0OOOOOO}丨数量:{O000OOO0O0OOO0O0O}丨价格:{OO00OOO00000OO0O0}')#line:385
                            if float (count_list )!=float (OO00OOO00000OO0O0 ):#line:386
                                O0OO0O00O000000OO =O0O00OOOO0OO0000O ['id']#line:387
                                if float (datetime .datetime .now ().hour )>8 :#line:388
                                    O00O000O00O000OO0 .cacel_sale (O0OO0O00O000000OO )#line:389
                        O00O000O00O000OO0 .game_map ()#line:391
        except Exception as OO0O00O00O0O00O00 :#line:393
            print (OO0O00O00O0O00O00 )#line:394
    def cacel_sale (OOO00OO000OO00O00 ,OO00OO00000OOOO0O ):#line:397
        try :#line:398
            O00OO00OO0OO00O00 =f'_saleId={OO00OO00000OOOO0O}_{timi_new()}'#line:399
            OO0000O0000O0OO00 ={'source':'scsc','authorization':OOO00OO000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OO0OO00O00 ),'signstring':O00OO00OO0OO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:410
            O0OOO0O0O00000OOO ={"saleId":OO00OO00000OOOO0O }#line:411
            OOOOOO0OO0OO0O00O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0000O0000O0OO00 ,data =O0OOO0O0O00000OOO ).json ()#line:412
            if 'status'in OOOOOO0OO0OO0O00O :#line:414
                if OOOOOO0OO0OO0O00O ['status']==200 :#line:415
                    print (f'【下架出售】:{OOOOOO0OO0OO0O00O["data"]}')#line:416
        except Exception as O00O0000O00000000 :#line:417
            print (O00O0000O00000000 )#line:418
    def change_nickname (O0O00O000000OOOOO ):#line:421
        try :#line:422
            O0O00O000000O0O00 =timi_new ()#line:423
            O00OOOO0O00O0000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:424
            OO0OOOO0O0O0O0OOO =requests .request ('post','https://www.qmsjmfb.com/',data =O00OOOO0O00O0000O ).text #line:425
            O00O00000O0O00O00 =re .findall ('<ul><li>(.*?)</li>',OO0OOOO0O0O0O0OOO )[0 ][:3 ]#line:426
            O0O00O0OOOO0O000O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00O00000O0O00O00}').json ()#line:427
            O000O000O0OO000OO =O0O00O0OOOO0O000O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:428
            OO00O000000OO0O00 ={"nickname":O000O000O0OO000OO }#line:429
            O00O0O0OOO00OOOO0 =f'_nickname={O000O000O0OO000OO}_{O0O00O000000O0O00}'#line:430
            O000O0OOO00O00000 ={'source':'scsc','authorization':O0O00O000000OOOOO .token ,'timestamp':O0O00O000000O0O00 ,'sign':sign (O00O0O0OOO00OOOO0 ),'signstring':O00O0O0OOO00OOOO0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:441
            OOO0OO000OO0000OO =requests .request ('patch',f'{host}/user/nickname',headers =O000O0OOO00O00000 ,data =OO00O000000OO0O00 ).json ()#line:442
            if 'status'in OOO0OO000OO0000OO :#line:444
                if OOO0OO000OO0000OO ['status']==200 :#line:445
                    print (f'【修改网名】:网名:{O000O000O0OO000OO}丨{OOO0OO000OO0000OO["message"]}')#line:446
        except Exception as OO00000OOO0OOOOOO :#line:447
            print (OO00000OOO0OOOOOO )#line:448
    def withdraw (OOO0O0O0000000O0O ):#line:451
        try :#line:452
            O0OO0OOOO00O00OO0 =f'__{timi_new()}'#line:453
            O0O0OO00OOOO0O000 ={'source':'scsc','authorization':OOO0O0O0000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOO00O00OO0 ),'signstring':O0OO0OOOO00O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:464
            O000000000O0OO0O0 =requests .request ('get',f'{host}/assets',headers =O0O0OO00OOOO0O000 ).json ()#line:465
            if 'status'in O000000000O0OO0O0 :#line:467
                if O000000000O0OO0O0 ['status']==200 :#line:468
                    OO0OOOO000O0OO0OO =O000000000O0OO0O0 ['data']['cash']#line:469
                    if float (OO0OOOO000O0OO0OO )>20 :#line:470
                        O0OO0OOOO00O00OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:471
                        O0O0OO00OOOO0O000 ={'authorization':OOO0O0O0000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOO00O00OO0 ),'signstring':O0OO0OOOO00O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
                        O000OO000OO0OO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:482
                        OOO0000OO0000O0O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO00OOOO0O000 ,data =O000OO000OO0OO0OO ).json ()#line:484
                        if 'status'in OOO0000OO0000O0O0 :#line:486
                            if OOO0000OO0000O0O0 ['status']==200 :#line:487
                                print (f'【余额提现】:{OOO0000OO0000O0O0["data"]}')#line:488
                        if 'status'in OOO0000OO0000O0O0 :#line:489
                            if OOO0000OO0000O0O0 ['status']==500 :#line:490
                                print (f'【余额提现】:{OOO0000OO0000O0O0["message"]}')#line:491
        except Exception as O00OO0OO00O0O0000 :#line:492
            print (O00OO0OO00O0O0000 )#line:493
    def invitenum (OO0OOOOO0OO000OO0 ):#line:496
        global invited_new #line:497
        try :#line:498
            OO0000OOOO00OO0O0 =f'__{timi_new()}'#line:499
            OO0000O00O00O00O0 ={'source':'scsc','authorization':OO0OOOOO0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO00OO0O0 ),'signstring':OO0000OOOO00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
            O00O00O0OO0O00O0O =requests .request ('get',f'{host}/invite/invitenum',headers =OO0000O00O00O00O0 ).json ()#line:511
            if 'status'in O00O00O0OO0O00O0O :#line:513
                if O00O00O0OO0O00O0O ['status']==200 :#line:514
                    O0O00O00OOOOOOOO0 =O00O00O0OO0O00O0O ['data']['invited_count']#line:515
                    O0OO00O00OO000OOO =O00O00O0OO0O00O0O ['data']['invited_second_count']#line:516
                    print (f'【我的邀请】:直邀好友:{O0O00O00OOOOOOOO0}丨间邀好友:{O0OO00O00OO000OOO}')#line:517
                    if O0O00O00OOOOOOOO0 <2 :#line:518
                        O0OOO00O00OOO00OO =f'__{timi_new()}'#line:519
                        O00OO0O00OO00O00O ={'source':'scsc','authorization':OO0OOOOO0OO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O00OOO00OO ),'signstring':O0OOO00O00OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:530
                        OO00OO0O0OO0OO0OO =requests .request ('get',f'{host}/user',headers =O00OO0O00OO00O00O ).json ()#line:531
                        if 'status'in OO00OO0O0OO0OO0OO :#line:533
                            if OO00OO0O0OO0OO0OO ['status']==200 :#line:534
                                invited_new .append (OO00OO0O0OO0OO0OO ['data']['inner_id'])#line:535
        except Exception as O0O00O0OO00OO0OOO :#line:536
            print (O0O00O0OO00OO0OOO )#line:537
    def game_map (OOOOOO00O0O00O0O0 ):#line:540
        global count_list #line:541
        try :#line:542
            O0OOOO0O00O0OOOO0 =f'__{timi_new()}'#line:543
            OO00000O00O0OOOOO ={'source':'scsc','authorization':OOOOOO00O0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O00O0OOOO0 ),'signstring':O0OOOO0O00O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:554
            OO0OOOO0O0OOOO0O0 =requests .request ('get',f'{host}/game/map',headers =OO00000O00O0OOOOO ).json ()#line:555
            if 'status'in OO0OOOO0O0OOOO0O0 :#line:557
                if OO0OOOO0O0OOOO0O0 ['status']==200 :#line:558
                    for O00000OOO00O0O000 in OO0OOOO0O0OOOO0O0 ['data']['list'][0 ]['crops']:#line:559
                        OOOO00OO0OO0O0000 =O00000OOO00O0O000 ['level']#line:561
                        if OOOO00OO0OO0O0000 ==41 :#line:562
                            OOOOO0000O00OOOO0 =O00000OOO00O0O000 ['crop_name']#line:563
                            OO000O000OO000O0O =O00000OOO00O0O000 ['count']#line:564
                            if OO000O000OO000O0O >0 :#line:565
                                count_list +=OO000O000OO000O0O #line:566
                                print (f'【农业资产】:{OOOOO0000O00OOOO0}丨数量:{OO000O000OO000O0O}')#line:567
                                if float (datetime .datetime .now ().hour )>8 :#line:568
                                    OOOOOO00O0O00O0O0 .the_query ()#line:569
        except Exception as OOOO00O0OOOO00OO0 :#line:570
            print (OOOO00O0OOOO00OO0 )#line:571
    def give_gold (OOOOO0OO0O0O000OO ):#line:574
        try :#line:575
            O0O0OO00OOO0OO0OO =f'__{timi_new()}'#line:576
            O0O00OO00OOO0OOO0 ={'source':'scsc','authorization':OOOOO0OO0O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OOO0OO0OO ),'signstring':O0O0OO00OOO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            OO0OO0O00OOO00O00 =requests .request ('get',f'{host}/user',headers =O0O00OO00OOO0OOO0 ).json ()#line:588
            if 'status'in OO0OO0O00OOO00O00 :#line:589
                if OO0OO0O00OOO00O00 ['status']==200 :#line:590
                    if float (OOOOO0OO0O0O000OO .doneeNo )!=0 :#line:591
                        O00O0O0O000O0O00O =OO0OO0O00OOO00O00 ['data']['assets']['gold']#line:592
                        if float (O00O0O0O000O0O00O )>float (OOOOO0OO0O0O000OO .innerId ):#line:593
                            OOOOOOOOO0OO000OO =int (float (O00O0O0O000O0O00O )/1.1 )#line:594
                            O0O0OO00OOO0OO0OO =f'_doneeNo={OOOOO0OO0O0O000OO.doneeNo}&quantity={OOOOOOOOO0OO000OO}_{timi_new()}'#line:595
                            O0O00OO00OOO0OOO0 ={'source':'scsc','authorization':OOOOO0OO0O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OOO0OO0OO ),'signstring':O0O0OO00OOO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:606
                            O0O000O00000O00O0 ={"quantity":OOOOOOOOO0OO000OO ,"doneeNo":OOOOO0OO0O0O000OO .doneeNo }#line:610
                            O0OO000O00O0OO000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OO00OOO0OOO0 ,data =O0O000O00000O00O0 ).json ()#line:611
                            if 'status'in O0OO000O00O0OO000 :#line:613
                                if O0OO000O00O0OO000 ['status']==200 :#line:614
                                    if O0OO000O00O0OO000 ['data']:#line:615
                                        print (f'【赠送种子】:赠送{OOOOOOOOO0OO000OO}种子给{OOOOO0OO0O0O000OO.doneeNo}成功')#line:616
                    else :#line:617
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:618
        except Exception as O000OOOO0O0OOO00O :#line:619
            print (O000OOOO0O0OOO00O )#line:620
    def invitation (OO0O0O0OO000000O0 ):#line:622
        try :#line:623
            _OO0O0O0OO0O00000O =float (bundled_def ())/4 #line:624
            OOOOOOO0O000O0O0O =f'_innerId={int(_OO0O0O0OO0O00000O)}_{timi_new()}'#line:625
            O0OOOO00O00O00000 ={'source':'scsc','authorization':OO0O0O0OO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O000O0O0O ),'signstring':OOOOOOO0O000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:636
            O00O00O00000OO0O0 ={"innerId":int (_OO0O0O0OO0O00000O )}#line:637
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOOO00O00O00000 ,data =O00O00O00000OO0O0 )#line:638
        except Exception as OOO0O000OOOOOO00O :#line:639
            print (OOO0O000OOOOOO00O )#line:640
    def winning_rewards (OOO0O0000O00OO0O0 ):#line:643
        try :#line:644
            OOOOO000OO0OO000O =f'__{timi_new()}'#line:645
            O00OO0OOOO0O00O0O ={'source':'scsc','authorization':OOO0O0000O00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000OO0OO000O ),'signstring':OOOOO000OO0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
            OO0OOOOOOOO00O00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO0OOOO0O00O0O ).json ()#line:657
            if 'status'in OO0OOOOOOOO00O00O :#line:659
                if OO0OOOOOOOO00O00O ['status']==200 :#line:660
                    if OO0OOOOOOOO00O00O ['data']['amount']:#line:661
                        OO0OO0O0OO0OOO000 =OO0OOOOOOOO00O00O ['data']['amount']['gold']#line:662
                        return OO0OO0O0OO0OOO000 #line:663
                    else :#line:664
                        return 0 #line:665
        except Exception as O0O000000O00OO00O :#line:666
            print (O0O000000O00OO00O )#line:667
    def certification (O000OOOO0OO00O0OO ):#line:670
        try :#line:671
            O00OOOO000OOOOOOO =f'__{timi_new()}'#line:672
            O0OOO0OO0O0OOO000 ={'source':'scsc','authorization':O000OOOO0OO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000OOOOOOO ),'signstring':O00OOOO000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            OO00OO0O0O0O0OOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OOO0OO0O0OOO000 ).json ()#line:684
            if 'status'in OO00OO0O0O0O0OOO0 :#line:686
                if OO00OO0O0O0O0OOO0 ['status']==200 :#line:687
                    if OO00OO0O0O0O0OOO0 ['data']['result']:#line:688
                        O000000O0OO0000O0 =OO00OO0O0O0O0OOO0 ['data']['nick_name']#line:689
                        return O000000O0OO0000O0 #line:690
                    else :#line:691
                        return '未实名'#line:692
        except Exception as O000O0O0OOO00000O :#line:693
            print (O000O0O0OOO00000O )#line:694
    def crops_illustrated (OOOO0O00O0O0000O0 ):#line:697
        try :#line:698
            OOO00O00O0O0O00OO =f'__{timi_new()}'#line:699
            OOO0OO0OO00OOOOOO ={'source':'scsc','authorization':OOOO0O00O0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0O0O00OO ),'signstring':OOO00O00O0O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:710
            OOO0OOOO0OOOO0O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0OO0OO00OOOOOO ).json ()#line:711
            if 'status'in OOO0OOOO0OOOO0O00 :#line:713
                if OOO0OOOO0OOOO0O00 ['status']==200 :#line:714
                    OOOO000O0000OO0O0 =OOO0OOOO0OOOO0O00 ['data'][0 ]['crops']#line:715
                    for OOOOOO0OO0OOO00OO in OOOO000O0000OO0O0 :#line:716
                        if OOOOOO0OO0OOO00OO ['ill_clover_award']:#line:717
                            if float (OOOOOO0OO0OOO00OO ['ill_clover_award'])>1 :#line:718
                                if OOOOOO0OO0OOO00OO ['is_finish']:#line:719
                                    if not OOOOOO0OO0OOO00OO ['is_getit']:#line:720
                                        if OOOO0O00O0O0000O0 .certification ()!='未实名':#line:721
                                            OOO00O00O0O0O00OO =f'_award_level={OOOOOO0OO0OOO00OO["level"]}_{timi_new()}'#line:722
                                            OOO0OO0OO00OOOOOO ={'source':'scsc','authorization':OOOO0O00O0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0O0O00OO ),'signstring':OOO00O00O0O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:733
                                            O0OOO0O000O000OOO ={"award_level":OOOOOO0OO0OOO00OO ['level']}#line:734
                                            O0O0OOO00OOOO0O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0OO0OO00OOOOOO ,json =O0OOO0O000O000OOO ).json ()#line:736
                                            if 'status'in O0O0OOO00OOOO0O0O :#line:737
                                                if O0O0OOO00OOOO0O0O ['status']==200 :#line:738
                                                    OO00OO0OO00O0O0O0 =O0O0OOO00OOOO0O0O ['data']['ill_clover_award']#line:739
                                                    print (f'【图鉴奖励】:领取{OOOOOO0OO0OOO00OO["crop_name"]}成就丨奖励{OO00OO0OO00O0O0O0}☘️')#line:741
                                                if O0O0OOO00OOOO0O0O ['status']==500 :#line:742
                                                    print (f'【图鉴奖励】:{O0O0OOO00OOOO0O0O["message"]}')#line:743
        except Exception as O0O000OOO00OOO0OO :#line:744
            print (O0O000OOO00OOO0OO )#line:745
    def watched_ad (O0OOOO000OO0OO0O0 ):#line:748
        try :#line:749
            O00O00OOOO0O0000O =f'__{timi_new()}'#line:750
            O0OO0O0O000O00000 ={'source':'scsc','authorization':O0OOOO000OO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOOO0O0000O ),'signstring':O00O00OOOO0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            OOOO0OO000O0OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O000O00000 ).json ()#line:762
            if 'status'in OOOO0OO000O0OOOOO :#line:764
                if OOOO0OO000O0OOOOO ['status']==200 :#line:765
                    if 'offlineInfo'in OOOO0OO000O0OOOOO ['data']:#line:766
                        time .sleep (random .randint (1 ,3 ))#line:767
                        O0OO0000O0O0O0000 =OOOO0OO000O0OOOOO ['data']['offlineInfo']['off_minute']#line:768
                        OOO0OO0OO00O0O00O =float (OOOO0OO000O0OOOOO ['data']['silver'])/1000000000000 #line:769
                        time .sleep (1 )#line:770
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OO0O0O000O00000 ).json ()#line:771
                        time .sleep (2 )#line:772
                        OOO00000OO000O0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O000O00000 ).json ()#line:773
                        if 'status'in OOO00000OO000O0O0 :#line:775
                            if OOO00000OO000O0O0 ['status']==200 :#line:776
                                O00OOOOO0O0O000OO =float (OOO00000OO000O0O0 ['data']['silver'])/1000000000000 #line:777
                                O000O0OO000000O0O =str (O00OOOOO0O0O000OO -OOO0OO0OO00O0O00O )[:6 ]#line:778
                                print (f'【离线奖励】:翻倍离线{O0OO0000O0O0O0000}分钟奖励🌱数量:{O000O0OO000000O0O}t粒')#line:779
        except Exception as OO0O00O0O000OO000 :#line:780
            print (OO0O00O0O000OO000 )#line:781
    def user_ad (OO00000OOO0OO0OOO ):#line:784
        try :#line:785
            O000O00OOO0OO0O00 =f'__{timi_new()}'#line:786
            O0O00OO0O0OOOOO0O ={'source':'scsc','authorization':OO00000OOO0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO0OO0O00 ),'signstring':O000O00OOO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:797
            O0O0O0O0O00OOO00O =requests .request ('get',f'{host}/user/ad',headers =O0O00OO0O0OOOOO0O ).json ()#line:798
            if 'status'in O0O0O0O0O00OOO00O :#line:800
                if O0O0O0O0O00OOO00O ['status']==200 :#line:801
                    OOO0O0OO0OOO0OO0O =O0O0O0O0O00OOO00O ['data']['max_time']#line:802
                    OOOOO00OOO000OO00 =O0O0O0O0O00OOO00O ['data']['watch_time']#line:803
                    OO000O00OO00O0O00 =O0O0O0O0O00OOO00O ['data']['added_time']#line:804
                    print (f'【获取种子】:获取🌱剩余{OO000O00OO00O0O00 + OOO0O0OO0OOO0OO0O - OOOOO00OOO000OO00}次丨好友提供:{OO000O00OO00O0O00}次')#line:805
                    if OO000O00OO00O0O00 +OOO0O0OO0OOO0OO0O -OOOOO00OOO000OO00 >0 :#line:806
                        time .sleep (random .randint (16 ,19 ))#line:807
                        OO0OO0OO00OOOO000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O00OO0O0OOOOO0O ).json ()#line:808
                        if 'status'in OO0OO0OO00OOOO000 :#line:810
                            if OO0OO0OO00OOOO000 ['status']==200 :#line:811
                                O00O0OO0OOOO0OOOO =float (OO0OO0OO00OOOO000 ['data']['silver'])/1000000000000 #line:812
                                print (f'【获取种子】:获得🌱:{int(O00O0OO0OOOO0OOOO)}t粒')#line:813
                                return True #line:814
                            if OO0OO0OO00OOOO000 ['status']==500 :#line:815
                                O00O000OO0OOOOO0O =OO0OO0OO00OOOO000 ['message']#line:816
                                print (f'【获取种子】:{O00O000OO0OOOOO0O}')#line:817
                                return False #line:818
        except Exception as O0000OOOO0O000O0O :#line:819
            print (O0000OOOO0O000O0O )#line:820
    def synthetic (O00OO0O0O000O0O00 ):#line:823
        global id ,g #line:824
        try :#line:825
            OO0O00000O0O0O0OO =O00OO0O0O000O0O00 .level_new ()#line:826
            O00O0OOOOO00O0OOO =random .randint (9 ,11 )#line:827
            OO000O00OO0O00O0O =f'_site=8&targetSite={O00O0OOOOO00O0OOO}_{timi_new()}'#line:828
            OOO00000OOOOO0OO0 ={'source':'scsc','authorization':O00OO0O0O000O0O00 .token ,'timestamp':timi_new (),'sign':sign (OO000O00OO0O00O0O ),'signstring':OO000O00OO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:839
            OO000OOOOO000O000 ={"site":int (8 ),"targetSite":int (O00O0OOOOO00O0OOO )}#line:840
            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000OOOOO0OO0 ,json =OO000OOOOO000O000 )#line:841
            while True :#line:842
                OO0OOO0OO0O00O0OO =f'__{timi_new()}'#line:843
                OO000OOO0OOO00OOO ={'source':'scsc','authorization':O00OO0O0O000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OO0O00O0OO ),'signstring':OO0OOO0OO0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                OOO00OOOO00OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO000OOO0OOO00OOO ).json ()#line:855
                if 'status'in OOO00OOOO00OO0O0O :#line:857
                    if OOO00OOOO00OO0O0O ['status']==200 :#line:858
                        OOO0OO0O000OOOO0O =OOO00OOOO00OO0O0O ['data']['cropList']#line:859
                        O0O00OO0OOOO0O0OO =OOO00OOOO00OO0O0O ['data']['gameCoreDataDBid']#line:860
                        OO00O0O0O00OO000O =float (OOO00OOOO00OO0O0O ['data']['silver'])/1000000000000 #line:861
                        OOOO0O00OO0000OO0 =0 #line:866
                        for OOOO000O00OOO0000 in OOO0OO0O000OOOO0O :#line:867
                            if not OOOO000O00OOO0000 :#line:868
                                OO00000O0OOOOO000 =f'_crop_id={O0O00OO0OOOO0O0OO}&site={OOOO0O00OO0000OO0}_{O00OO0O0O000O0O00.time}'#line:869
                                OO00O00000O000OO0 ={'source':'scsc','authorization':O00OO0O0O000O0O00 .token ,'timestamp':O00OO0O0O000O0O00 .time ,'sign':sign (OO00000O0OOOOO000 ),'signstring':OO00000O0OOOOO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:879
                                OOO00O00O0OOOOOOO ={"site":OOOO0O00OO0000OO0 ,"crop_id":O0O00OO0OOOO0O0OO }#line:880
                                O0O00OO0000OOOOO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00O00000O000OO0 ,data =OOO00O00O0OOOOOOO ).json ()#line:881
                                time .sleep (random .randint (1 ,3 )/10 )#line:883
                                if 'status'in O0O00OO0000OOOOO0 :#line:884
                                    if O0O00OO0000OOOOO0 ['status']==200 :#line:885
                                        if O0O00OO0000OOOOO0 ['message']=='种子数量不足':#line:886
                                            OO0O00000O0O0O0OO =O00OO0O0O000O0O00 .level_new ()#line:887
                                            print (f'【种植合成】:{O0O00OO0000OOOOO0["message"]}')#line:888
                                            if not O00OO0O0O000O0O00 .user_ad ():#line:889
                                                return False #line:890
                                    if O0O00OO0000OOOOO0 ['status']==500 :#line:891
                                        print (f'【种植合成】:{O0O00OO0000OOOOO0["message"]}')#line:892
                                        return False #line:893
                            OOOO0O00OO0000OO0 +=1 #line:894
                        OO000O000000O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OO000OOO0OOO00OOO ).json ()#line:895
                        OOOOO000000OO0OOO =OO000O000000O0000 ['data']['cropList']#line:896
                        OO0OO00OOO0O000OO =False #line:897
                        for OOOO000O00OOO0000 in range (12 ):#line:898
                            id =OOOOO000000OO0OOO [OOOO000O00OOO0000 ]['level']#line:899
                            if float (OO0O00000O0O0O0OO )-float (id )>9 :#line:900
                                O0000OOO0000OOOOO =f'_site={OOOO000O00OOO0000}_{timi_new()}'#line:901
                                OO0O0O00O0O0OO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OO0O0O000O0O00 .token ,'timestamp':timi_new (),'sign':sign (O0000OOO0000OOOOO ),'signstring':O0000OOO0000OOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:912
                                O00OO0O00OOOO000O ={"site":OOOO000O00OOO0000 }#line:913
                                O0OOO000OOO0OOOOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O0O00O0O0OO0O0 ,data =O00OO0O00OOOO000O ).json ()#line:915
                                if 'status'in O0OOO000OOO0OOOOO :#line:916
                                    if O0OOO000OOO0OOOOO ['status']==200 :#line:917
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:918
                            if id !=0 :#line:919
                                for O000O0OOO0OO000OO in range (11 ):#line:920
                                    O00O0000O000000O0 =O000O0OOO0OO000OO +1 #line:921
                                    g =OOOOO000000OO0OOO [O00O0000O000000O0 ]['level']#line:922
                                    if id ==g :#line:923
                                        O0O00OO0O00O0OO0O =O000O0OOO0OO000OO +2 #line:924
                                        if O0O00OO0O00O0OO0O !=OOOO000O00OOO0000 +1 :#line:925
                                            OOOO0OOOOOO00O000 =OOOO000O00OOO0000 +1 #line:926
                                            time .sleep (random .randint (1 ,3 )/10 )#line:928
                                            OO000O00OO0O00O0O =f'_site={OOOO0OOOOOO00O000 - 1}&targetSite={O0O00OO0O00O0OO0O - 1}_{timi_new()}'#line:929
                                            OOO00000OOOOO0OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OO0O0O000O0O00 .token ,'timestamp':timi_new (),'sign':sign (OO000O00OO0O00O0O ),'signstring':OO000O00OO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:946
                                            O00OOOO0O00O0O0O0 ={"site":int (OOOO0OOOOOO00O000 -1 ),"targetSite":int (O0O00OO0O00O0OO0O -1 )}#line:947
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000OOOOO0OO0 ,json =O00OOOO0O00O0O0O0 )#line:948
                                            OO0OO00OOO0O000OO =True #line:950
                                    if OO0OO00OOO0O000OO :#line:951
                                        break #line:952
                                if OO0OO00OOO0O000OO :#line:953
                                    break #line:954
        except :#line:955
            O00OO0O0O000O0O00 .synthetic ()#line:956
    def level_new (O000OOO00OO000O00 ):#line:959
        try :#line:960
            OO0O0OO00O00OO00O =f'__{timi_new()}'#line:961
            O0OO000O0OOO0OO00 ={'source':'scsc','authorization':O000OOO00OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO00O00OO00O ),'signstring':OO0O0OO00O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
            O0OO00O0O0O0OOOOO =requests .request ('get',f'{host}/user',headers =O0OO000O0OOO0OO00 ).json ()#line:973
            if 'status'in O0OO00O0O0O0OOOOO :#line:974
                if O0OO00O0O0O0OOOOO ['status']==200 :#line:975
                    return float (O0OO00O0O0O0OOOOO ['data']['level'])#line:976
        except Exception as O0OO00000O000O0O0 :#line:977
            print (O0OO00000O000O0O0 )#line:978
    def propsraffle (OO0000O0OO0O0O000 ):#line:981
        try :#line:982
            while True :#line:983
                O0O0OO0O0000O0O00 =f'__{timi_new()}'#line:984
                O0OOO00O0O0O00000 ={'source':'scsc','authorization':OO0000O0OO0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0000O0O00 ),'signstring':O0O0OO0O0000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:995
                O0O00OOOOOO0000OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOO00O0O0O00000 ).json ()#line:996
                if 'status'in O0O00OOOOOO0000OO :#line:998
                    if O0O00OOOOOO0000OO ['status']==200 :#line:999
                        O0OOO000OO0OOOO00 =O0O00OOOOOO0000OO ['data']['rows']#line:1000
                        OO00O00O0000O0OO0 =O0O00OOOOOO0000OO ['data']['vstate']#line:1001
                        if O0OOO000OO0OOOO00 ==5 or O0OOO000OO0OOOO00 ==6 or O0OOO000OO0OOOO00 ==7 :#line:1002
                            OOO0O0O000OOOO000 =O0O00OOOOOO0000OO ['data']['silver']#line:1003
                            print (f'【转盘抽奖】:获得种子:{OOO0O0O000OOOO000}')#line:1004
                        if O0OOO000OO0OOOO00 ==1 or O0OOO000OO0OOOO00 ==2 or O0OOO000OO0OOOO00 ==3 :#line:1005
                            OOOOO0000OOOOO00O =O0O00OOOOOO0000OO ['data']['clover']#line:1006
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0000OOOOO00O}')#line:1007
                        if O0OOO000OO0OOOO00 ==4 or O0OOO000OO0OOOO00 ==8 :#line:1008
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1009
                        if O0OOO000OO0OOOO00 =='抽奖次数已用完':#line:1013
                            break #line:1047
                time .sleep (random .randint (8 ,15 )/10 )#line:1048
        except Exception as O0O0O00O0O00O0OOO :#line:1049
            print (O0O0O00O0O00O0OOO )#line:1050
    def friends_invitation (O0OO0O0OOOO0OOOOO ):#line:1053
        try :#line:1054
            O0OO000O0O00O00O0 =f'__{timi_new()}'#line:1055
            O0OOOOOOO000OO00O ={'source':'scsc','authorization':O0OO0O0OOOO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O00O00O0 ),'signstring':O0OO000O0O00O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1066
            O00OOO00000O00O00 =requests .request ('get',f'{host}/friends',headers =O0OOOOOOO000OO00O ).json ()#line:1067
            if 'status'in O00OOO00000O00O00 :#line:1068
                if O00OOO00000O00O00 ['status']==200 :#line:1069
                    OO0O0O00O00OO00O0 =O00OOO00000O00O00 ['data']['myInviteter']#line:1070
                    if OO0O0O00O00OO00O0 :#line:1071
                        O0OOO0O00OO0OOOOO =OO0O0O00O00OO00O0 ['user']['nickname']#line:1072
                        O0000OOO0O00O00O0 =O0OO0O0OOOO0OOOOO .certification ()#line:1073
                        if O0000OOO0O00O00O0 =='未实名':#line:1074
                            weishim .append (O0OO0O0OOOO0OOOOO .token )#line:1075
                        print (f'【查邀请人】:我的邀请人:{O0OOO0O00OO0OOOOO}丨实名:{O0000OOO0O00O00O0}')#line:1076
                    else :#line:1077
                        if O0OO0O0OOOO0OOOOO .innerId !='0':#line:1078
                            O0OO0O0OOOO0OOOOO .invitation ()#line:1079
        except Exception as OOO0000O00000000O :#line:1080
            print (OOO0000O00000000O )#line:1081
    def add_clover (OOO0OOO00000OOO0O ):#line:1084
        global golden_seed #line:1085
        try :#line:1086
            OO00O000OO0O0OO0O =f'__{timi_new()}'#line:1087
            OOO00O00OO0OO00O0 ={'source':'scsc','authorization':OOO0OOO00000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO0O0OO0O ),'signstring':OO00O000OO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1098
            OOOO000OO00000000 =requests .request ('get',f'{host}/assets/clovers',headers =OOO00O00OO0OO00O0 ).json ()#line:1099
            if 'status'in OOOO000OO00000000 :#line:1101
                if OOOO000OO00000000 ['status']==200 :#line:1102
                    OOO00000O0OOO000O =OOOO000OO00000000 ['data']['clover']#line:1103
                    O0OOOO0O0O00OOOO0 =OOOO000OO00000000 ['data']['used_clover']#line:1104
                    O0OO000OOOO000OOO =float (OOO00000O0OOO000O )-float (O0OOOO0O0O00OOOO0 )#line:1105
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOOO0O0O00OOOO0}')#line:1106
                    if OOO0OOO00000OOO0O .certification ()!='未实名':#line:1107
                        if O0OO000OOOO000OOO >1 :#line:1108
                            OO00O000OO0O0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OO000OOOO000OOO)}_{timi_new()}'#line:1109
                            OOOOOO00O0O00000O ={'source':'scsc','authorization':OOO0OOO00000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO0O0OO0O ),'signstring':OO00O000OO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1120
                            OO00O0O0O0O0000O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OO000OOOO000OOO )}#line:1121
                            O00O0O000OO0OO000 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOOO00O0O00000O ,data =OO00O0O0O0O0000O0 ).json ()#line:1122
                            if 'status'in O00O0O000OO0OO000 :#line:1124
                                if O00O0O000OO0OO000 ['status']==200 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O00O0O000OO0OO000["data"]["isSuccess"]}丨数量:{O0OO000OOOO000OOO}')#line:1126
                                if O00O0O000OO0OO000 ['status']==500 :#line:1127
                                    print (f'【参与抽奖】:添加☘️:{O00O0O000OO0OO000["message"]}')#line:1128
            O0OOOO0OO00OOO0OO =requests .request ('get',f'{host}/lottery',headers =OOO00O00OO0OO00O0 ).json ()#line:1129
            O0O0OO0OOOOOO000O =OOO0OOO00000OOO0O .winning_rewards ()#line:1131
            if 'status'in O0OOOO0OO00OOO0OO :#line:1132
                if O0OOOO0OO00OOO0OO ['status']==200 :#line:1133
                    O0OOO0O0O00OOO0O0 =O0OOOO0OO00OOO0OO ['data'][0 ]['day_get_gold_quantity']#line:1134
                    golden_seed +=float (O0OOO0O0O00OOO0O0 )#line:1135
                    OOO0OOO000O0O0OOO =O0OOOO0OO00OOO0OO ['data'][1 ]['value']#line:1136
                    OO0000O0OO0OOOOO0 =O0OOOO0OO00OOO0OO ['data'][0 ]['join_number']#line:1137
                    O0O00OOOO00O000O0 =int (float (O0OOOO0OO00OOO0OO ['data'][0 ]['totalValue']))#line:1138
                    OO00OO0000000OOO0 =float (OOO0OOO000O0O0OOO /O0O00OOOO00O000O0 )*10000 #line:1139
                    OO0OO0000O0000OOO =O0O00OOOO00O000O0 /OO0000O0OO0OOOOO0 #line:1140
                    print (f'【参与抽奖】:预计每天中{str(O0OOO0O0O00OOO0O0)[:6]}颗金种子丨好友收益:{str(O0O0OO0OOOOOO000O)[:6]}')#line:1141
                    print (f'【抽奖统计】:每1万☘️中{str(OO00OO0000000OOO0)[:6]}颗金种子丨☘️人均:{str(OO0OO0000O0000OOO)[:7]}️')#line:1142
        except Exception as O0O0O00OO0OOOOOO0 :#line:1143
            print (O0O0O00OO0OOOOOO0 )#line:1144
    def energy (O00OOO0O0O0O0O000 ):#line:1147
        try :#line:1148
            while True :#line:1149
                O00O00O0O0000O000 =f'__{timi_new()}'#line:1150
                OOO000O00OOOOO0OO ={'source':'scsc','authorization':O00OOO0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000O000 ),'signstring':O00O00O0O0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1161
                OO0OOO00O000000OO =requests .request ('get',f'{host}/energy/general',headers =OOO000O00OOOOO0OO ).json ()#line:1162
                if 'status'in OO0OOO00O000000OO :#line:1164
                    if OO0OOO00O000000OO ['status']==200 :#line:1165
                        O0OOO0O0000OO0OO0 =OO0OOO00O000000OO ['data']['ordinary_water']#line:1166
                        OOOOO00OO0O0OOO00 =OO0OOO00O000000OO ['data']['ordinary_fertilizer']#line:1167
                        OO000OO0O0O0000OO =OO0OOO00O000000OO ['data']['videoStatus']#line:1168
                        OO0OO0OO0O0O0O0O0 =OO0OOO00O000000OO ['data']['waterVideoKey']#line:1169
                        print (f'【我的营养】:肥料:{str(OOOOO00OO0O0OOO00).split(".")[0]}丨水滴:{str(O0OOO0O0000OO0OO0).split(".")[0]}')#line:1171
                        if float (OOOOO00OO0O0OOO00 )<96 :#line:1172
                            if OO000OO0O0O0000OO :#line:1173
                                time .sleep (random .randint (160 ,180 )/10 )#line:1174
                                OO00O0O0O00O0OO00 =99 -float (OOOOO00OO0O0OOO00 )#line:1175
                                O0OOO00OO0OOOOO00 ={"fertilizer":str (OO00O0O0O00O0OO00 ).split ('.')[0 ]}#line:1176
                                O00O0000OO0OO00OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO000O00OOOOO0OO ).json ()#line:1178
                                if 'status'in O00O0000OO0OO00OO :#line:1180
                                    if O00O0000OO0OO00OO ['status']==200 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0000OO0OO00OO["message"]}')#line:1182
                                    if O00O0000OO0OO00OO ['status']==500 :#line:1183
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0000OO0OO00OO["message"]}')#line:1184
                                        break #line:1185
                                if float (OOOOO00OO0O0OOO00 )<78 :#line:1187
                                    OO00O0O0O00O0OO00 =80 -float (OOOOO00OO0O0OOO00 )#line:1188
                                    O0000000OOO00O00O =f'_fertilizer={int(OO00O0O0O00O0OO00)}_{timi_new()}'#line:1189
                                    OOO0O00O00OO00O00 ={'source':'scsc','authorization':O00OOO0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000000OOO00O00O ),'signstring':O0000000OOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1200
                                    OOO0OO000000O000O ={"fertilizer":int (OO00O0O0O00O0OO00 )}#line:1201
                                    OO000OO0OO0OOO0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0O00O00OO00O00 ,data =OOO0OO000000O000O ).json ()#line:1203
                                    if 'status'in OO000OO0OO0OOO0OO :#line:1205
                                        if OO000OO0OO0OOO0OO ['status']==200 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OO000OO0OO0OOO0OO["message"]}丨数量:{int(OO00O0O0O00O0OO00)}')#line:1207
                                        if OO000OO0OO0OOO0OO ['status']==500 :#line:1208
                                            print (f'【购买肥料】:购买肥料:{OO000OO0OO0OOO0OO["message"]}丨数量:{int(OO00O0O0O00O0OO00)}')#line:1209
                                            OOOOOOOOOO0O00000 =OO000OO0OO0OOO0OO ["message"].split ('-')[1 ]#line:1210
                                            O0O0OO0O0OOO0O0O0 =f'__{timi_new()}'#line:1211
                                            O000O0O0OOOO000OO ={'source':'scsc','authorization':O00OOO0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOO0O0O0 ),'signstring':O0O0OO0O0OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1222
                                            OOO0OOOOO0OO0OO00 =requests .request ('get',f'{host}/user',headers =O000O0O0OOOO000OO ).json ()#line:1223
                                            if 'status'in OOO0OOOOO0OO0OO00 :#line:1224
                                                if OOO0OOOOO0OO0OO00 ['status']==200 :#line:1225
                                                    O00O000OO0O0O00O0 =OOO0OOOOO0OO0OO00 ['data']['inner_id']#line:1226
                                                    if give_gold (O00O000OO0O0O00O0 ,float (OOOOOOOOOO0O00000 )+1 ):#line:1227
                                                        O00OOO0O0O0O0O000 .energy ()#line:1228
                        if float (O0OOO0O0000OO0OO0 )<880 :#line:1229
                            if OO0OO0OO0O0O0O0O0 :#line:1230
                                time .sleep (random .randint (160 ,180 )/10 )#line:1231
                                OO00OOO0O00OO000O =999 -float (O0OOO0O0000OO0OO0 )#line:1232
                                OO00O000OOO0OO00O ={"water":str (OO00OOO0O00OO000O ).split ('.')[0 ]}#line:1233
                                O0O0OOOO00000O000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO000O00OOOOO0OO ).json ()#line:1235
                                if 'status'in O0O0OOOO00000O000 :#line:1237
                                    if O0O0OOOO00000O000 ['status']==200 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OOOO00000O000["message"]}')#line:1239
                                    if O0O0OOOO00000O000 ['status']==500 :#line:1240
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OOOO00000O000["message"]}')#line:1241
                                        break #line:1242
                                if float (O0OOO0O0000OO0OO0 )<780 :#line:1243
                                    OO00OOO0O00OO000O =800 -float (O0OOO0O0000OO0OO0 )#line:1244
                                    OOOO0OO00OOO00O00 =f'_water={int(OO00OOO0O00OO000O)}_{timi_new()}'#line:1245
                                    OOO00OOOO000OOOOO ={'source':'scsc','authorization':O00OOO0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00OOO00O00 ),'signstring':OOOO0OO00OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1256
                                    O0OO0O0OO000OO000 ={"water":int (OO00OOO0O00OO000O )}#line:1257
                                    O00OOO000OOO0OOO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00OOOO000OOOOO ,data =O0OO0O0OO000OO000 ).json ()#line:1259
                                    if 'status'in O00OOO000OOO0OOO0 :#line:1261
                                        if O00OOO000OOO0OOO0 ['status']==200 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O00OOO000OOO0OOO0["message"]}丨数量:{int(OO00OOO0O00OO000O)}')#line:1263
                                        if O00OOO000OOO0OOO0 ['status']==500 :#line:1264
                                            print (f'【购买水滴】:购买水滴:{O00OOO000OOO0OOO0["message"]}丨数量:{int(OO00OOO0O00OO000O)}')#line:1265
                                            OOOOOOOOOO0O00000 =O00OOO000OOO0OOO0 ["message"].split ('-')[1 ]#line:1266
                                            O0O0OO0O0OOO0O0O0 =f'__{timi_new()}'#line:1267
                                            O000O0O0OOOO000OO ={'source':'scsc','authorization':O00OOO0O0O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOO0O0O0 ),'signstring':O0O0OO0O0OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1278
                                            OOO0OOOOO0OO0OO00 =requests .request ('get',f'{host}/user',headers =O000O0O0OOOO000OO ).json ()#line:1279
                                            if 'status'in OOO0OOOOO0OO0OO00 :#line:1280
                                                if OOO0OOOOO0OO0OO00 ['status']==200 :#line:1281
                                                    O00O000OO0O0O00O0 =OOO0OOOOO0OO0OO00 ['data']['inner_id']#line:1282
                                                    if give_gold (O00O000OO0O0O00O0 ,float (OOOOOOOOOO0O00000 )+1 ):#line:1283
                                                        O00OOO0O0O0O0O000 .energy ()#line:1284
                        break #line:1285
        except Exception as OO00OOO0OOO0O0O0O :#line:1286
            print (OO00OOO0OOO0O0O0O )#line:1287
def bundled_def ():#line:1290
    O0000O00OO000OO0O =['5570536','7750212','7911652','7911680','7805624']#line:1291
    return O0000O00OO000OO0O [random .randint (0 ,len (O0000O00OO000OO0O )-1 )]#line:1292
def version_of_the_validation ():#line:1296
    return str ((101 -56 )/10 )#line:1297
def ubbbf ():#line:1299
    print ('卡密验证通过   ✅')#line:1300
def sc2 ():#line:1303
    return "19319#$%^&*((*"#line:1304
def OO00OO0OO0OO00OO00o0 ():#line:1307
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1309
def get_ip ():#line:1312
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1314
def gitee_validation ():#line:1317
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1318
def gitee_edition ():#line:1321
    try :#line:1322
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1323
    except :#line:1324
        sys .exit (0 )#line:1325
def O000OO000O0O00OOO00 ():#line:1329
    try :#line:1330
        O0OO0OOO0OO0O0OOO =gitee_edition ()#line:1331
        if version_of_the_validation ()<O0OO0OOO0OO0O0OOO ['CityEarth']['edition']:#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0OOO0OO0O0OOO["CityEarth"]["edition"]}   ❌')#line:1333
            print (f'更新内容=>>{O0OO0OOO0OO0O0OOO["CityEarth"]["content"]}')#line:1334
        else :#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0OOO0OO0O0OOO["CityEarth"]["edition"]}   ✅')#line:1336
            print (f'更新内容=>> {O0OO0OOO0OO0O0OOO["CityEarth"]["content"]}')#line:1337
    except Exception as O00O00O0O0OO0O00O :#line:1338
        print (O00O00O0O0OO0O00O )#line:1339
def sc3 ():#line:1342
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1343
if __name__ =='__main__':#line:1346
    start ()#line:1347
