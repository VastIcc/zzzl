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
msg_list =[]#line:6
invited_new =[]#line:7
weishim =[]#line:8
def start ():#line:11
    try :#line:12
        O000OO000O0O00OOO00 ()#line:13
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:14
        O000OO0O00OO00O00 ()#line:15
        O00OO0OOOO0OO0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O00OO0OOOO0OO0OOO)}个账号==========")#line:17
        for OOO0O0O00O0OOOO0O in O00OO0OOOO0OO0OOO :#line:18
            O00O0O000O00OOOOO =[]#line:19
            print (f"------------正在执行第{O00OO0OOOO0OO0OOO.index(OOO0O0O00O0OOOO0O) + 1}个账号------------")#line:20
            O0OO0O0OO00OOO0OO =CityEarth (OOO0O0O00O0OOOO0O ,O00O0O000O00OOOOO ,O00OO0OOOO0OO0OOO .index (OOO0O0O00O0OOOO0O ))#line:21
            def O00OO00000OO0O00O ():#line:23
                if O0OO0O0OO00OOO0OO .base_info ():#line:25
                    O0OO0O0OO00OOO0OO .sealing ()#line:27
                    O0OO0O0OO00OOO0OO .invitenum ()#line:29
                    O0OO0O0OO00OOO0OO .query_to_sell ()#line:31
                    O0OO0O0OO00OOO0OO .friends_invitation ()#line:35
                    O0OO0O0OO00OOO0OO .energy ()#line:37
                    O0OO0O0OO00OOO0OO .add_clover ()#line:39
                    O0OO0O0OO00OOO0OO .propsraffle ()#line:41
                    O0OO0O0OO00OOO0OO .synthetic ()#line:43
                    O0OO0O0OO00OOO0OO .crops_illustrated ()#line:45
                    O0OO0O0OO00OOO0OO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0OO0O0OO00OOO0OO .give_gold ()#line:50
            OO0OO00O000OOOO0O =threading .Thread (target =O00OO00000OO0O00O )#line:52
            OO0OO00O000OOOO0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO0000O00O0O0OO00 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0000O00O0O0OO00 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O000OOOO0O0000O0O in invited_new :#line:62
            print (O000OOOO0O0000O0O )#line:63
        print ('开始打印未实名的token')#line:64
        for OOO0O0O0OO0OOO000 in weishim :#line:65
            print (OOO0O0O0OO0OOO000 )#line:66
    except Exception as O00OOOO0OOOO0O0O0 :#line:67
        print (O00OOOO0OOOO0O0O0 )#line:68
def give_gold (OOOO0OO00O0O0O000 ,OO0O000OOOO0O0000 ):#line:72
    try :#line:73
        O00O00000OO00O000 =f'_doneeNo={OOOO0OO00O0O0O000}&quantity={int(OO0O000OOOO0O0000)}_{timi_new()}'#line:74
        OO0000O00OO0O00O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00O00000OO00O000 ),'signstring':O00O00000OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0OO000OO00OO0O00 ={"quantity":int (OO0O000OOOO0O0000 ),"doneeNo":OOOO0OO00O0O0O000 }#line:89
        OO0OO000O00O00000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0000O00OO0O00O0 ,data =O0OO000OO00OO0O00 ).json ()#line:90
        if 'status'in OO0OO000O00O00000 :#line:92
            if OO0OO000O00O00000 ['status']==200 :#line:93
                if OO0OO000O00O00000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OO0O000OOOO0O0000)}种子给{OOOO0OO00O0O0O000}成功')#line:95
                    return True #line:96
            if OO0OO000O00O00000 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0OO000O00O00000["message"]}')#line:98
                return False #line:99
            if OO0OO000O00O00000 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0OO000O00O00000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO0O00O0O00O0O00 :#line:104
        print (OOO0O00O0O00O0O00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OOO00OO00O0O00OO0 ):#line:115
    OO000O0000O00OOO0 =hashlib .md5 (OOO00OO00O0O00OO0 .encode ()).hexdigest ()#line:116
    O000O000O00O0OOOO =sc1 ()#line:117
    OOO00000O000O0OOO =sc2 ()#line:118
    O000OO0000O00OO00 =sc3 ()#line:119
    O000O0O000OOOO0OO =O000O000O00O0OOOO +OO000O0000O00OOO0 +OOO00000O000O0OOO +O000OO0000O00OO00 #line:120
    O000O0OOOO000OOO0 =hashlib .md5 (O000O0O000OOOO0OO .encode ()).hexdigest ()#line:121
    return O000O0OOOO000OOO0 #line:122
def format_msg ():#line:125
    O0O000O00O000O00O =""#line:126
    for O0OOO0OO000O0O00O in msg_list :#line:127
        O0O000O00O000O00O +=str (O0OOO0OO000O0O00O )+"\r\n"#line:128
    return O0O000O00O000O00O #line:129
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
def get_json_data (OOO00O0O000OOO0O0 ,OOOOOO0OOO00OOOO0 ,O000OO0000O0O0000 ,O0O0OO0OO00OOOO00 ):#line:153
    with open (OOO00O0O000OOO0O0 ,'rb')as O00O00000O00000OO :#line:154
        O0OOOOOOOOOO0O0OO =json .load (O00O00000O00000OO )#line:155
        O0OOOOOOOOOO0O0OO ['data'][OOOOOO0OOO00OOOO0 ][O000OO0000O0O0000 ]=O0O0OO0OO00OOOO00 #line:156
        O00OO000O00OOO000 =O0OOOOOOOOOO0O0OO #line:157
    O00O00000O00000OO .close ()#line:158
    return O00OO000O00OOO000 #line:159
def write_json_data (OOOOO0000OO0000OO ):#line:162
    with open (json_path1 ,'w')as OO0OO0OO0OO0000OO :#line:163
        json .dump (OOOOO0000OO0000OO ,OO0OO0OO0OO0000OO )#line:164
    OO0OO0OO0OO0000OO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO0O00OOO0O00OOO0 ,O000O000O00O00OOO ,OO000000OOO0000OO ,O0O0O00O000O00OOO ):#line:171
        try :#line:172
            OO0O00OOO0O00OOO0 .msg =OO000000OOO0000OO #line:173
            OO0O00OOO0O00OOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO0O00OOO0O00OOO0 .token =O000O000O00O00OOO ['authorization']#line:175
            OO0O00OOO0O00OOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO0O00OOO0O00OOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO0O00OOO0O00OOO0 .elephant_user =O000O000O00O00OOO ['elephant_user']#line:178
            OO0O00OOO0O00OOO0 .elephant_pswd =O000O000O00O00OOO ['elephant_pswd']#line:179
            OO0O00OOO0O00OOO0 .elephant_Task_ID =O000O000O00O00OOO ['elephant_Task_ID']#line:180
            OO0O00OOO0O00OOO0 .len_new =O0O0O00O000O00OOO #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOO0O0000OOOO0OOO ):#line:186
        try :#line:187
            OOO0O0000OOOO0OOO .watched_ad ()#line:189
            O000000O00O0O00OO =f'__{timi_new()}'#line:190
            O00O000OOOO00OOO0 ={'source':'scsc','authorization':OOO0O0000OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O00O0O00OO ),'signstring':O000000O00O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0000OO0OOO000000 =requests .request ('get',f'{host}/user',headers =O00O000OOOO00OOO0 ).json ()#line:202
            if 'status'in O0000OO0OOO000000 :#line:204
                if O0000OO0OOO000000 ['status']==200 :#line:205
                    OO0O000OO0O0OOO0O =O0000OO0OOO000000 ['data']['nickname']#line:206
                    O0000O000OOOOOOO0 =O0000OO0OOO000000 ['data']['inner_id']#line:207
                    OOO0000O0O0O0000O =O0000OO0OOO000000 ['data']['assets']['gold']#line:208
                    OOO0O00OOOOO0O0OO =O0000OO0OOO000000 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OO0O000OO0O0OOO0O[:5]}丨ID:{O0000O000OOOOOOO0}丨等级:{OOO0O00OOOOO0O0OO}丨金种子:{str(OOO0000O0O0O0000O).split(".")[0]}')#line:211
                    if 'wx_'in OO0O000OO0O0OOO0O :#line:212
                        OOO0O0000OOOO0OOO .change_nickname ()#line:213
                if O0000OO0OOO000000 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOO0O0000OOOO0OOO .elephant_user =='f':#line:216
                        return False #line:217
                    OOO00OO0OO000O000 =Invalid_login .addtask (elephant_user =OOO0O0000OOOO0OOO .elephant_user ,elephant_pswd =OOO0O0000OOOO0OOO .elephant_pswd ,elephant_Task_ID =OOO0O0000OOOO0OOO .elephant_Task_ID )#line:220
                    OOOOOO0000O0OO00O =get_json_data (json_path ,OOO0O0000OOOO0OOO .len_new ,'authorization',OOO00OO0OO000O000 )#line:221
                    if write_json_data (OOOOOO0000O0OO00O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0000OO0OOO000000 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO0O0OO0OO0OOOO00 :#line:228
            print (OO0O0OO0OO0OOOO00 )#line:229
    def sealing (O000OOO000O00O000 ):#line:232
        try :#line:233
            O0O000000OOOO0000 =f'__{timi_new()}'#line:234
            OOO0O00OOOO0000OO ={'source':'scsc','authorization':O000OOO000O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000OOOO0000 ),'signstring':O0O000000OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0O00OOOO0000OO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO0O00OOOO0000OO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0O00OOOO0000OO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0O00OOOO0000OO )#line:249
            requests .request ('get',f'{host}/user',headers =OOO0O00OOOO0000OO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0O00OOOO0000OO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0O00OOOO0000OO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0O00OOOO0000OO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00OOOO0000OO )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO0O00OOOO0000OO )#line:255
        except Exception as O0O0O0OO0O0O00000 :#line:256
            print (O0O0O0OO0O0O00000 )#line:257
    def ddd (OO0OO0OO0O00O0O0O ):#line:259
        try :#line:260
            OO0O00O0O00OO000O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OOO00000OOO0O00O0 ={'source':'scsc','authorization':OO0OO0OO0O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0O00OO000O ),'signstring':OO0O00O0O00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO0O0000O0O00OO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO00000OOO0O00O0 ).json ()#line:273
            print (OOO0O0000O0O00OO0 )#line:274
        except Exception as O0000OO00000OO0OO :#line:277
            print (O0000OO00000OO0OO )#line:278
    def the_query (OOOO000O0O0O0O0O0 ):#line:283
        try :#line:284
            O0O0OOO00OOO00000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O00OOO00O0O0OOO00 ={'authorization':OOOO000O0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00OOO00000 ),'signstring':O0O0OOO00OOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOOO00O00O00OO0O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00OOO00O0O0OOO00 ).json ()#line:297
            if 'status'in OOOO00O00O00OO0O0 :#line:299
                if OOOO00O00O00OO0O0 ['status']==200 :#line:300
                    OO0O00O0OOOO000OO =OOOO00O00O00OO0O0 ['data']['rows'][4 ]['price']#line:301
                    return OO0O00O0OOOO000OO #line:302
        except Exception as O0OOOO00O0OO00000 :#line:303
            print (O0OOOO00O0OO00000 )#line:304
    def market_sale (O00O0OOO0OO00000O ,O00O00OOOOO000OO0 ):#line:307
        try :#line:308
            O0000OO0OO00000OO =timi_new ()#line:309
            O0OOO0O0OO000O00O =f'type=crop__{O0000OO0OO00000OO}'#line:310
            O0O00000O0000O00O ={'source':'scsc','authorization':O00O0OOO0OO00000O .token ,'timestamp':str (O0000OO0OO00000OO ),'sign':sign (O0OOO0O0OO000O00O ),'signstring':O0OOO0O0OO000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:321
            OOO00O00O00OO0000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O00000O0000O00O ).json ()#line:323
            if 'status'in OOO00O00O00OO0000 :#line:325
                if OOO00O00O00OO0000 ['status']==200 :#line:326
                    if OOO00O00O00OO0000 ['data']['rows']:#line:327
                        OOO0OO0OOOO0OOOOO =OOO00O00O00OO0000 ['data']['rows'][0 ]['packsackItemId']#line:328
                        O0O0OO0OO0OOOOOOO =OOO00O00O00OO0000 ['data']['rows'][0 ]['quantity']#line:329
                        O00O0OO0O0OO0O00O =float (O00O00OOOOO000OO0 )-0.001 #line:330
                        if O00O0OO0O0OO0O00O >9 :#line:331
                            OOO00O00OO0OOOO0O =f'_packsackItemId={OOO0OO0OOOO0OOOOO}&price={str(O00O00OOOOO000OO0)[:5]}&quantity={O0O0OO0OO0OOOOOOO}_{O0000OO0OO00000OO}'#line:332
                            O000OOO0OOO0OOOOO ={'source':'scsc','authorization':O00O0OOO0OO00000O .token ,'timestamp':str (O0000OO0OO00000OO ),'sign':sign (OOO00O00OO0OOOO0O ),'signstring':OOO00O00OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
                            OO00OO000000O00OO ={"packsackItemId":OOO0OO0OOOO0OOOOO ,"price":str (O00O00OOOOO000OO0 )[:5 ],"quantity":str (O0O0OO0OO0OOOOOOO )}#line:348
                            O0O0OO0000O00O000 =requests .request ('post',f'{host}/market/sale',headers =O000OOO0OOO0OOOOO ,data =OO00OO000000O00OO ).json ()#line:349
                            if 'status'in O0O0OO0000O00O000 :#line:351
                                if O0O0OO0000O00O000 ['status']==200 :#line:352
                                    print (f'【上架芦荟】:数量:{O0O0OO0OO0OOOOOOO}丨价格:{str(O00O00OOOOO000OO0)[:5]}')#line:353
        except Exception as OO0000O00OOOOOOOO :#line:354
            print (OO0000O00OOOOOOOO )#line:355
    def query_to_sell (O000O0OOOO000OO00 ):#line:358
        global count_list #line:359
        try :#line:360
            O0O0O0OO0O0O0OO0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:361
            O0O00OO0OOOOOO000 ={'source':'scsc','authorization':O000O0OOOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0O0O0OO0O ),'signstring':O0O0O0OO0O0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:372
            O0OOO0O00OO0OO0OO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O00OO0OOOOOO000 ).json ()#line:373
            if 'status'in O0OOO0O00OO0OO0OO :#line:375
                if O0OOO0O00OO0OO0OO ['status']==200 :#line:376
                    for O00O000O0OO000OOO in O0OOO0O00OO0OO0OO ['data']['rows']:#line:377
                        OOOO000OOOOOOO00O =O00O000O0OO000OOO ['materialKey']#line:378
                        O0O00O0OO000O0000 =O00O000O0OO000OOO ['quantity']#line:379
                        O000O00OO00OO000O =O00O000O0OO000OOO ['price']#line:380
                        OOOOOO00OO00O00O0 =O00O000O0OO000OOO ['saleState']#line:381
                        if OOOOOO00OO00O00O0 ==0 :#line:382
                            print (f'【出售订单】:名称:{OOOO000OOOOOOO00O}丨数量:{O0O00O0OO000O0000}丨价格:{O000O00OO00OO000O}')#line:383
                            count_list +=O0O00O0OO000O0000 #line:384
                            O00O00O0OO0O000OO =O000O0OOOO000OO00 .the_query ()#line:386
                            if float (O00O00O0OO0O000OO )!=float (O000O00OO00OO000O ):#line:387
                                O00O0O0O00000OOO0 =O00O000O0OO000OOO ['id']#line:388
                                if float (datetime .datetime .now ().hour )>8 :#line:389
                                    O000O0OOOO000OO00 .cacel_sale (O00O0O0O00000OOO0 )#line:390
                                    O000O0OOOO000OO00 .market_sale (O000O00OO00OO000O )#line:391
                            O000O0OOOO000OO00 .game_map ()#line:393
        except Exception as O0000OO0O0O0O00O0 :#line:395
            print (O0000OO0O0O0O00O0 )#line:396
    def cacel_sale (OO0OOOOO00O000OO0 ,O000OOO000O0OOO00 ):#line:399
        try :#line:400
            O00OOO0OO0O00O0OO =f'_saleId={O000OOO000O0OOO00}_{timi_new()}'#line:401
            O0O0000OO00OO0OOO ={'source':'scsc','authorization':OO0OOOOO00O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OO0O00O0OO ),'signstring':O00OOO0OO0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:412
            OOO0O00000O00OOO0 ={"saleId":O000OOO000O0OOO00 }#line:413
            O0O0OOOOOOO000O0O =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0000OO00OO0OOO ,data =OOO0O00000O00OOO0 ).json ()#line:414
            if 'status'in O0O0OOOOOOO000O0O :#line:416
                if O0O0OOOOOOO000O0O ['status']==200 :#line:417
                    print (f'【下架出售】:{O0O0OOOOOOO000O0O["data"]}')#line:418
        except Exception as O0OO0OO00O0OO0OOO :#line:419
            print (O0OO0OO00O0OO0OOO )#line:420
    def change_nickname (O000O00000OO00O00 ):#line:423
        try :#line:424
            O000OOO0OOO000OOO =timi_new ()#line:425
            OO0O00O0OO00000O0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:426
            O0000OO00O00O00O0 =requests .request ('post','https://www.qmsjmfb.com/',data =OO0O00O0OO00000O0 ).text #line:427
            O00OOOOOOO0000OO0 =re .findall ('<ul><li>(.*?)</li>',O0000OO00O00O00O0 )[0 ][:3 ]#line:428
            O00OO0000OOO0O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00OOOOOOO0000OO0}').json ()#line:429
            O0000OO00OOO0OOO0 =O00OO0000OOO0O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:430
            OO0OOO0O00OO00O0O ={"nickname":O0000OO00OOO0OOO0 }#line:431
            OOO000O00O0O00O0O =f'_nickname={O0000OO00OOO0OOO0}_{O000OOO0OOO000OOO}'#line:432
            OOO000000000O0OO0 ={'source':'scsc','authorization':O000O00000OO00O00 .token ,'timestamp':O000OOO0OOO000OOO ,'sign':sign (OOO000O00O0O00O0O ),'signstring':OOO000O00O0O00O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:443
            OOO0OOO0O0OOO00OO =requests .request ('patch',f'{host}/user/nickname',headers =OOO000000000O0OO0 ,data =OO0OOO0O00OO00O0O ).json ()#line:444
            if 'status'in OOO0OOO0O0OOO00OO :#line:446
                if OOO0OOO0O0OOO00OO ['status']==200 :#line:447
                    print (f'【修改网名】:网名:{O0000OO00OOO0OOO0}丨{OOO0OOO0O0OOO00OO["message"]}')#line:448
        except Exception as O0O0OOOO0O000O00O :#line:449
            print (O0O0OOOO0O000O00O )#line:450
    def withdraw (OO00OOO0OOOOO0OOO ):#line:453
        try :#line:454
            OOOOO00O0O0OO0OO0 =f'__{timi_new()}'#line:455
            OOO00OO00OOO000OO ={'source':'scsc','authorization':OO00OOO0OOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0O0OO0OO0 ),'signstring':OOOOO00O0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:466
            OO0OO0O0OOOOOO0OO =requests .request ('get',f'{host}/assets',headers =OOO00OO00OOO000OO ).json ()#line:467
            if 'status'in OO0OO0O0OOOOOO0OO :#line:469
                if OO0OO0O0OOOOOO0OO ['status']==200 :#line:470
                    O0O0OO0O0000O0000 =OO0OO0O0OOOOOO0OO ['data']['cash']#line:471
                    if float (O0O0OO0O0000O0000 )>20 :#line:472
                        OOOOO00O0O0OO0OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:473
                        OOO00OO00OOO000OO ={'authorization':OO00OOO0OOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0O0OO0OO0 ),'signstring':OOOOO00O0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        O0OOOO00O0OO000OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:484
                        OO0OOOOO0O0O000OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO00OO00OOO000OO ,data =O0OOOO00O0OO000OO ).json ()#line:486
                        if 'status'in OO0OOOOO0O0O000OO :#line:488
                            if OO0OOOOO0O0O000OO ['status']==200 :#line:489
                                print (f'【余额提现】:{OO0OOOOO0O0O000OO["data"]}')#line:490
                        if 'status'in OO0OOOOO0O0O000OO :#line:491
                            if OO0OOOOO0O0O000OO ['status']==500 :#line:492
                                print (f'【余额提现】:{OO0OOOOO0O0O000OO["message"]}')#line:493
        except Exception as OOOOOO0000OO0000O :#line:494
            print (OOOOOO0000OO0000O )#line:495
    def invitenum (OOOOOOO0000O0OO0O ):#line:498
        global invited_new #line:499
        try :#line:500
            OO0OOOO000O0O0OOO =f'__{timi_new()}'#line:501
            OOO0OOO0OO0OO00OO ={'source':'scsc','authorization':OOOOOOO0000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO000O0O0OOO ),'signstring':OO0OOOO000O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
            OO00OO00OOOO0OO00 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0OOO0OO0OO00OO ).json ()#line:513
            if 'status'in OO00OO00OOOO0OO00 :#line:515
                if OO00OO00OOOO0OO00 ['status']==200 :#line:516
                    OOO00OOOO0O00O0OO =OO00OO00OOOO0OO00 ['data']['invited_count']#line:517
                    OOO000OOO0O000OO0 =OO00OO00OOOO0OO00 ['data']['invited_second_count']#line:518
                    print (f'【我的邀请】:直邀好友:{OOO00OOOO0O00O0OO}丨间邀好友:{OOO000OOO0O000OO0}')#line:519
                    if OOO00OOOO0O00O0OO <2 :#line:520
                        OO0OO000000O0O0O0 =f'__{timi_new()}'#line:521
                        O0O0O0O0O0O00OOOO ={'source':'scsc','authorization':OOOOOOO0000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000000O0O0O0 ),'signstring':OO0OO000000O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:532
                        OOO0000O0000O0O00 =requests .request ('get',f'{host}/user',headers =O0O0O0O0O0O00OOOO ).json ()#line:533
                        if 'status'in OOO0000O0000O0O00 :#line:535
                            if OOO0000O0000O0O00 ['status']==200 :#line:536
                                invited_new .append (OOO0000O0000O0O00 ['data']['inner_id'])#line:537
        except Exception as OOOO000OOO0OOO00O :#line:538
            print (OOOO000OOO0OOO00O )#line:539
    def game_map (O0OOO00OOOO00O0OO ):#line:542
        try :#line:543
            O0OO00000OOO0O00O =f'__{timi_new()}'#line:544
            O0OOO000000O0OO0O ={'source':'scsc','authorization':O0OOO00OOOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00000OOO0O00O ),'signstring':O0OO00000OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
            OO0O0OOO0O0O0O0O0 =requests .request ('get',f'{host}/game/map',headers =O0OOO000000O0OO0O ).json ()#line:556
            if 'status'in OO0O0OOO0O0O0O0O0 :#line:558
                if OO0O0OOO0O0O0O0O0 ['status']==200 :#line:559
                    for OO0O0OOOO0000OOOO in OO0O0OOO0O0O0O0O0 ['data']['list'][0 ]['crops']:#line:560
                        O000O000000OO0O0O =OO0O0OOOO0000OOOO ['level']#line:562
                        if O000O000000OO0O0O ==41 :#line:563
                            O000O00OOOOO000O0 =OO0O0OOOO0000OOOO ['crop_name']#line:564
                            O0O0O0O0O0000O0O0 =OO0O0OOOO0000OOOO ['count']#line:565
                            if O0O0O0O0O0000O0O0 >0 :#line:566
                                print (f'【农业资产】:{O000O00OOOOO000O0}丨数量:{O0O0O0O0O0000O0O0}')#line:567
                                if float (datetime .datetime .now ().hour )>8 :#line:568
                                    O0OOO00OOOO00O0OO .the_query ()#line:569
        except Exception as OO0O0O0OOO0OOO00O :#line:570
            print (OO0O0O0OOO0OOO00O )#line:571
    def give_gold (O0O0OO0OOOO0OO0O0 ):#line:574
        try :#line:575
            OOO00OO0O0O00000O =f'__{timi_new()}'#line:576
            OO0O00OOOO0O0O0OO ={'source':'scsc','authorization':O0O0OO0OOOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O0O00000O ),'signstring':OOO00OO0O0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            OO000OOO00O0OO000 =requests .request ('get',f'{host}/user',headers =OO0O00OOOO0O0O0OO ).json ()#line:588
            if 'status'in OO000OOO00O0OO000 :#line:589
                if OO000OOO00O0OO000 ['status']==200 :#line:590
                    if float (O0O0OO0OOOO0OO0O0 .doneeNo )!=0 :#line:591
                        O0O0OOO000OO00O0O =OO000OOO00O0OO000 ['data']['assets']['gold']#line:592
                        if float (O0O0OOO000OO00O0O )>float (O0O0OO0OOOO0OO0O0 .innerId ):#line:593
                            OOOOO00000O0O00OO =int (float (O0O0OOO000OO00O0O )/1.1 )#line:594
                            OOO00OO0O0O00000O =f'_doneeNo={O0O0OO0OOOO0OO0O0.doneeNo}&quantity={OOOOO00000O0O00OO}_{timi_new()}'#line:595
                            OO0O00OOOO0O0O0OO ={'source':'scsc','authorization':O0O0OO0OOOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O0O00000O ),'signstring':OOO00OO0O0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:606
                            O0OOOO00OO000O0O0 ={"quantity":OOOOO00000O0O00OO ,"doneeNo":O0O0OO0OOOO0OO0O0 .doneeNo }#line:610
                            O00OO0OOO000OO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O00OOOO0O0O0OO ,data =O0OOOO00OO000O0O0 ).json ()#line:611
                            if 'status'in O00OO0OOO000OO0O0 :#line:613
                                if O00OO0OOO000OO0O0 ['status']==200 :#line:614
                                    if O00OO0OOO000OO0O0 ['data']:#line:615
                                        print (f'【赠送种子】:赠送{OOOOO00000O0O00OO}种子给{O0O0OO0OOOO0OO0O0.doneeNo}成功')#line:616
                    else :#line:617
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:618
        except Exception as OOO0000000O0O0OOO :#line:619
            print (OOO0000000O0O0OOO )#line:620
    def invitation (OO0OO0O000O0OOO00 ):#line:622
        try :#line:623
            _O00000O0O0O00O000 =float (bundled_def ())/4 #line:624
            O00OOO0OOO000O0O0 =f'_innerId={int(_O00000O0O0O00O000)}_{timi_new()}'#line:625
            OOOOOO00O0O0O0000 ={'source':'scsc','authorization':OO0OO0O000O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOO000O0O0 ),'signstring':O00OOO0OOO000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:636
            O000OOO000O0O000O ={"innerId":int (_O00000O0O0O00O000 )}#line:637
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOOOO00O0O0O0000 ,data =O000OOO000O0O000O )#line:638
        except Exception as O00O0O0O000OOO00O :#line:639
            print (O00O0O0O000OOO00O )#line:640
    def winning_rewards (OO00O0000O0OO0OOO ):#line:643
        try :#line:644
            OOOO0OO00OO0OO0OO =f'__{timi_new()}'#line:645
            O0O0O00OO0O0000OO ={'source':'scsc','authorization':OO00O0000O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00OO0OO0OO ),'signstring':OOOO0OO00OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
            OOO000O0OO0000O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O00OO0O0000OO ).json ()#line:657
            if 'status'in OOO000O0OO0000O00 :#line:659
                if OOO000O0OO0000O00 ['status']==200 :#line:660
                    if OOO000O0OO0000O00 ['data']['amount']:#line:661
                        O00O000O0O0OO00OO =OOO000O0OO0000O00 ['data']['amount']['gold']#line:662
                        return O00O000O0O0OO00OO #line:663
                    else :#line:664
                        return 0 #line:665
        except Exception as O0OOO00OOO00000O0 :#line:666
            print (O0OOO00OOO00000O0 )#line:667
    def certification (O0OO0OO00O0O000OO ):#line:670
        try :#line:671
            OOOO0000O000OO0OO =f'__{timi_new()}'#line:672
            OOO0OOOOOOOO0OO0O ={'source':'scsc','authorization':O0OO0OO00O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000O000OO0OO ),'signstring':OOOO0000O000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            O00000O000OOO0000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0OOOOOOOO0OO0O ).json ()#line:684
            if 'status'in O00000O000OOO0000 :#line:686
                if O00000O000OOO0000 ['status']==200 :#line:687
                    if O00000O000OOO0000 ['data']['result']:#line:688
                        O00O0O0O00O00O0OO =O00000O000OOO0000 ['data']['nick_name']#line:689
                        return O00O0O0O00O00O0OO #line:690
                    else :#line:691
                        return '未实名'#line:692
        except Exception as O0000OO00OO00O0O0 :#line:693
            print (O0000OO00OO00O0O0 )#line:694
    def crops_illustrated (O00OO0000OOOO0OO0 ):#line:697
        try :#line:698
            O00OO000O00OO000O =f'__{timi_new()}'#line:699
            O00O0O0OO00O0000O ={'source':'scsc','authorization':O00OO0000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000O00OO000O ),'signstring':O00OO000O00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:710
            O00O00O0000O00O0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0O0OO00O0000O ).json ()#line:711
            if 'status'in O00O00O0000O00O0O :#line:713
                if O00O00O0000O00O0O ['status']==200 :#line:714
                    OOO0OO000O00OO0O0 =O00O00O0000O00O0O ['data'][0 ]['crops']#line:715
                    for O0O0O00O0OOO0O000 in OOO0OO000O00OO0O0 :#line:716
                        if O0O0O00O0OOO0O000 ['ill_clover_award']:#line:717
                            if float (O0O0O00O0OOO0O000 ['ill_clover_award'])>1 :#line:718
                                if O0O0O00O0OOO0O000 ['is_finish']:#line:719
                                    if not O0O0O00O0OOO0O000 ['is_getit']:#line:720
                                        if O00OO0000OOOO0OO0 .certification ()!='未实名':#line:721
                                            O00OO000O00OO000O =f'_award_level={O0O0O00O0OOO0O000["level"]}_{timi_new()}'#line:722
                                            O00O0O0OO00O0000O ={'source':'scsc','authorization':O00OO0000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000O00OO000O ),'signstring':O00OO000O00OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:733
                                            OO0O0000OOO00000O ={"award_level":O0O0O00O0OOO0O000 ['level']}#line:734
                                            OO0O0OOO00O0OO000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0O0OO00O0000O ,json =OO0O0000OOO00000O ).json ()#line:736
                                            if 'status'in OO0O0OOO00O0OO000 :#line:737
                                                if OO0O0OOO00O0OO000 ['status']==200 :#line:738
                                                    O00OOO000O00OOO0O =OO0O0OOO00O0OO000 ['data']['ill_clover_award']#line:739
                                                    print (f'【图鉴奖励】:领取{O0O0O00O0OOO0O000["crop_name"]}成就丨奖励{O00OOO000O00OOO0O}☘️')#line:741
                                                if OO0O0OOO00O0OO000 ['status']==500 :#line:742
                                                    print (f'【图鉴奖励】:{OO0O0OOO00O0OO000["message"]}')#line:743
        except Exception as OOO0O000OOO00000O :#line:744
            print (OOO0O000OOO00000O )#line:745
    def watched_ad (OOO0OO0O0O00OO000 ):#line:748
        try :#line:749
            OO00OOO0OOOOOOO0O =f'__{timi_new()}'#line:750
            OOO0O00O00OO00OOO ={'source':'scsc','authorization':OOO0OO0O0O00OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOOOOOO0O ),'signstring':OO00OOO0OOOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            O000OOO000O00000O =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00O00OO00OOO ).json ()#line:762
            if 'status'in O000OOO000O00000O :#line:764
                if O000OOO000O00000O ['status']==200 :#line:765
                    if 'offlineInfo'in O000OOO000O00000O ['data']:#line:766
                        time .sleep (random .randint (1 ,3 ))#line:767
                        O00O0000O0OO0OO0O =O000OOO000O00000O ['data']['offlineInfo']['off_minute']#line:768
                        OO0000OO00OOO0OOO =float (O000OOO000O00000O ['data']['silver'])/1000000000000 #line:769
                        time .sleep (1 )#line:770
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO0O00O00OO00OOO ).json ()#line:771
                        time .sleep (2 )#line:772
                        OOO000OOO0OO000O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00O00OO00OOO ).json ()#line:773
                        if 'status'in OOO000OOO0OO000O0 :#line:775
                            if OOO000OOO0OO000O0 ['status']==200 :#line:776
                                OOOO0OOO0O0O000OO =float (OOO000OOO0OO000O0 ['data']['silver'])/1000000000000 #line:777
                                OOOO00OOOO000OO00 =str (OOOO0OOO0O0O000OO -OO0000OO00OOO0OOO )[:6 ]#line:778
                                print (f'【离线奖励】:翻倍离线{O00O0000O0OO0OO0O}分钟奖励🌱数量:{OOOO00OOOO000OO00}t粒')#line:779
        except Exception as OOOOO0O00O0OO0O00 :#line:780
            print (OOOOO0O00O0OO0O00 )#line:781
    def user_ad (OOO00O0OO00O00000 ):#line:784
        try :#line:785
            OOO00OOO0000OO000 =f'__{timi_new()}'#line:786
            OO00O0OO000OO00OO ={'source':'scsc','authorization':OOO00O0OO00O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0000OO000 ),'signstring':OOO00OOO0000OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:797
            O00O000O00O00OOOO =requests .request ('get',f'{host}/user/ad',headers =OO00O0OO000OO00OO ).json ()#line:798
            if 'status'in O00O000O00O00OOOO :#line:800
                if O00O000O00O00OOOO ['status']==200 :#line:801
                    O00O0OO0O0OOO0OO0 =O00O000O00O00OOOO ['data']['max_time']#line:802
                    OO0OOO0OOOOO0OOO0 =O00O000O00O00OOOO ['data']['watch_time']#line:803
                    OOOO0O00OOO0O0000 =O00O000O00O00OOOO ['data']['added_time']#line:804
                    print (f'【获取种子】:获取🌱剩余{OOOO0O00OOO0O0000 + O00O0OO0O0OOO0OO0 - OO0OOO0OOOOO0OOO0}次丨好友提供:{OOOO0O00OOO0O0000}次')#line:805
                    if OOOO0O00OOO0O0000 +O00O0OO0O0OOO0OO0 -OO0OOO0OOOOO0OOO0 >0 :#line:806
                        time .sleep (random .randint (16 ,19 ))#line:807
                        OOO0O000OOO0000O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00O0OO000OO00OO ).json ()#line:808
                        if 'status'in OOO0O000OOO0000O0 :#line:810
                            if OOO0O000OOO0000O0 ['status']==200 :#line:811
                                O00O0O0O0O000000O =float (OOO0O000OOO0000O0 ['data']['silver'])/1000000000000 #line:812
                                print (f'【获取种子】:获得🌱:{int(O00O0O0O0O000000O)}t粒')#line:813
                                return True #line:814
                            if OOO0O000OOO0000O0 ['status']==500 :#line:815
                                O00OOO0000O0OO00O =OOO0O000OOO0000O0 ['message']#line:816
                                print (f'【获取种子】:{O00OOO0000O0OO00O}')#line:817
                                return False #line:818
        except Exception as O00O000O00O0O0000 :#line:819
            print (O00O000O00O0O0000 )#line:820
    def synthetic (O0O00000O000O0O0O ):#line:823
        global id ,g #line:824
        try :#line:825
            O0000000O0OO00OO0 =O0O00000O000O0O0O .level_new ()#line:826
            OOO0OO00O000O0O00 =random .randint (9 ,11 )#line:827
            OO0OOO0O00O000OOO =f'_site=8&targetSite={OOO0OO00O000O0O00}_{timi_new()}'#line:828
            O00O0OOO0O0O00O00 ={'source':'scsc','authorization':O0O00000O000O0O0O .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O00O000OOO ),'signstring':OO0OOO0O00O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:839
            O0000000OO0OO0O00 ={"site":int (8 ),"targetSite":int (OOO0OO00O000O0O00 )}#line:840
            requests .request ('post',f'{host}/game/crops/move',headers =O00O0OOO0O0O00O00 ,json =O0000000OO0OO0O00 )#line:841
            while True :#line:842
                OOOOOOO0O0O000O0O =f'__{timi_new()}'#line:843
                O0O0O0O0OOOO000OO ={'source':'scsc','authorization':O0O00000O000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O0O000O0O ),'signstring':OOOOOOO0O0O000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                OO0O00O000OOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0OOOO000OO ).json ()#line:855
                if 'status'in OO0O00O000OOO0O0O :#line:857
                    if OO0O00O000OOO0O0O ['status']==200 :#line:858
                        O0OO0O0O0O000000O =OO0O00O000OOO0O0O ['data']['cropList']#line:859
                        OO0000O000O0O0OO0 =OO0O00O000OOO0O0O ['data']['gameCoreDataDBid']#line:860
                        OO000OO00OOO0OO0O =float (OO0O00O000OOO0O0O ['data']['silver'])/1000000000000 #line:861
                        O0O00O0O000OOO00O =0 #line:866
                        for OOO0OO0OOO0OOO00O in O0OO0O0O0O000000O :#line:867
                            if not OOO0OO0OOO0OOO00O :#line:868
                                OO00OOOO0000000O0 =f'_crop_id={OO0000O000O0O0OO0}&site={O0O00O0O000OOO00O}_{O0O00000O000O0O0O.time}'#line:869
                                OO0OO0OO00OOOOO00 ={'source':'scsc','authorization':O0O00000O000O0O0O .token ,'timestamp':O0O00000O000O0O0O .time ,'sign':sign (OO00OOOO0000000O0 ),'signstring':OO00OOOO0000000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:879
                                O0OOO00O0O0000OOO ={"site":O0O00O0O000OOO00O ,"crop_id":OO0000O000O0O0OO0 }#line:880
                                O0O0O0000O000OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OO0OO00OOOOO00 ,data =O0OOO00O0O0000OOO ).json ()#line:881
                                time .sleep (random .randint (1 ,3 )/10 )#line:883
                                if 'status'in O0O0O0000O000OO00 :#line:884
                                    if O0O0O0000O000OO00 ['status']==200 :#line:885
                                        if O0O0O0000O000OO00 ['message']=='种子数量不足':#line:886
                                            O0000000O0OO00OO0 =O0O00000O000O0O0O .level_new ()#line:887
                                            print (f'【种植合成】:{O0O0O0000O000OO00["message"]}')#line:888
                                            if not O0O00000O000O0O0O .user_ad ():#line:889
                                                return False #line:890
                                    if O0O0O0000O000OO00 ['status']==500 :#line:891
                                        print (f'【种植合成】:{O0O0O0000O000OO00["message"]}')#line:892
                                        return False #line:893
                            O0O00O0O000OOO00O +=1 #line:894
                        O0O00000O0OOO000O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0O0OOOO000OO ).json ()#line:895
                        OOO0OOOO0OO0OO0O0 =O0O00000O0OOO000O ['data']['cropList']#line:896
                        O0O00O0OO0O0OO00O =False #line:897
                        for OOO0OO0OOO0OOO00O in range (12 ):#line:898
                            id =OOO0OOOO0OO0OO0O0 [OOO0OO0OOO0OOO00O ]['level']#line:899
                            if float (O0000000O0OO00OO0 )-float (id )>9 :#line:900
                                O0000000OOOOO0OO0 =f'_site={OOO0OO0OOO0OOO00O}_{timi_new()}'#line:901
                                OOO0OOOO000O0OO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00000O000O0O0O .token ,'timestamp':timi_new (),'sign':sign (O0000000OOOOO0OO0 ),'signstring':O0000000OOOOO0OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:912
                                OOO00000O00000O00 ={"site":OOO0OO0OOO0OOO00O }#line:913
                                OO0OOO00OOOO00000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0OOOO000O0OO00 ,data =OOO00000O00000O00 ).json ()#line:915
                                if 'status'in OO0OOO00OOOO00000 :#line:916
                                    if OO0OOO00OOOO00000 ['status']==200 :#line:917
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:918
                            if id !=0 :#line:919
                                for O0OO0OOOOO0O00O00 in range (11 ):#line:920
                                    O0O00O0OO0O0O000O =O0OO0OOOOO0O00O00 +1 #line:921
                                    g =OOO0OOOO0OO0OO0O0 [O0O00O0OO0O0O000O ]['level']#line:922
                                    if id ==g :#line:923
                                        OO0OOO00OO000000O =O0OO0OOOOO0O00O00 +2 #line:924
                                        if OO0OOO00OO000000O !=OOO0OO0OOO0OOO00O +1 :#line:925
                                            OOOOOOO000OOO0000 =OOO0OO0OOO0OOO00O +1 #line:926
                                            time .sleep (random .randint (1 ,3 )/10 )#line:928
                                            OO0OOO0O00O000OOO =f'_site={OOOOOOO000OOO0000 - 1}&targetSite={OO0OOO00OO000000O - 1}_{timi_new()}'#line:929
                                            O00O0OOO0O0O00O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00000O000O0O0O .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0O00O000OOO ),'signstring':OO0OOO0O00O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:946
                                            O00O00OO0000O0OO0 ={"site":int (OOOOOOO000OOO0000 -1 ),"targetSite":int (OO0OOO00OO000000O -1 )}#line:947
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00O0OOO0O0O00O00 ,json =O00O00OO0000O0OO0 )#line:948
                                            O0O00O0OO0O0OO00O =True #line:950
                                    if O0O00O0OO0O0OO00O :#line:951
                                        break #line:952
                                if O0O00O0OO0O0OO00O :#line:953
                                    break #line:954
        except :#line:955
            O0O00000O000O0O0O .synthetic ()#line:956
    def level_new (OO00OOOO0000OOO0O ):#line:959
        try :#line:960
            OO0O000O000000O00 =f'__{timi_new()}'#line:961
            OO0OOOO0OOO00OOO0 ={'source':'scsc','authorization':OO00OOOO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O000000O00 ),'signstring':OO0O000O000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
            OO0O00OO0OO00OOOO =requests .request ('get',f'{host}/user',headers =OO0OOOO0OOO00OOO0 ).json ()#line:973
            if 'status'in OO0O00OO0OO00OOOO :#line:974
                if OO0O00OO0OO00OOOO ['status']==200 :#line:975
                    return float (OO0O00OO0OO00OOOO ['data']['level'])#line:976
        except Exception as O000O00OOO00OOOO0 :#line:977
            print (O000O00OOO00OOOO0 )#line:978
    def propsraffle (O00O0OOOOOOO0O0O0 ):#line:981
        try :#line:982
            while True :#line:983
                O0OOO00O000O000O0 =f'__{timi_new()}'#line:984
                OO0OOOOOO00OOOO0O ={'source':'scsc','authorization':O00O0OOOOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O000O000O0 ),'signstring':O0OOO00O000O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:995
                OO000OO0000O00O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OOOOOO00OOOO0O ).json ()#line:996
                if 'status'in OO000OO0000O00O0O :#line:998
                    if OO000OO0000O00O0O ['status']==200 :#line:999
                        OO000O00O00O000OO =OO000OO0000O00O0O ['data']['rows']#line:1000
                        O00000OOOOOO000OO =OO000OO0000O00O0O ['data']['vstate']#line:1001
                        if OO000O00O00O000OO ==5 or OO000O00O00O000OO ==6 or OO000O00O00O000OO ==7 :#line:1002
                            O0OO000O0O0O0O0OO =OO000OO0000O00O0O ['data']['silver']#line:1003
                            print (f'【转盘抽奖】:获得种子:{O0OO000O0O0O0O0OO}')#line:1004
                        if OO000O00O00O000OO ==1 or OO000O00O00O000OO ==2 or OO000O00O00O000OO ==3 :#line:1005
                            O00O0O0O000OO0OO0 =OO000OO0000O00O0O ['data']['clover']#line:1006
                            print (f'【转盘抽奖】:获得三叶草:{O00O0O0O000OO0OO0}')#line:1007
                        if OO000O00O00O000OO ==4 or OO000O00O00O000OO ==8 :#line:1008
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1009
                        if OO000O00O00O000OO =='抽奖次数已用完':#line:1013
                            break #line:1047
                time .sleep (random .randint (8 ,15 )/10 )#line:1048
        except Exception as O00O00OO000OO0000 :#line:1049
            print (O00O00OO000OO0000 )#line:1050
    def friends_invitation (O0OOOO00OOOOO0000 ):#line:1053
        try :#line:1054
            O0OO0OO0O00O0OOOO =f'__{timi_new()}'#line:1055
            OOOO00OOO00OO0O0O ={'source':'scsc','authorization':O0OOOO00OOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O00O0OOOO ),'signstring':O0OO0OO0O00O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1066
            O000OO0000000OOOO =requests .request ('get',f'{host}/friends',headers =OOOO00OOO00OO0O0O ).json ()#line:1067
            if 'status'in O000OO0000000OOOO :#line:1068
                if O000OO0000000OOOO ['status']==200 :#line:1069
                    OOOOOOO0000O0O0O0 =O000OO0000000OOOO ['data']['myInviteter']#line:1070
                    if OOOOOOO0000O0O0O0 :#line:1071
                        O00O00OO00O0O0000 =OOOOOOO0000O0O0O0 ['user']['nickname']#line:1072
                        O0O0O0000OOOO0O00 =O0OOOO00OOOOO0000 .certification ()#line:1073
                        if O0O0O0000OOOO0O00 =='未实名':#line:1074
                            weishim .append (O0OOOO00OOOOO0000 .token )#line:1075
                        print (f'【查邀请人】:我的邀请人:{O00O00OO00O0O0000}丨实名:{O0O0O0000OOOO0O00}')#line:1076
        except Exception as OOO000000OO00000O :#line:1080
            print (OOO000000OO00000O )#line:1081
    def add_clover (OO0O0O0OOOOO00OOO ):#line:1084
        global golden_seed #line:1085
        try :#line:1086
            O000000O000OOO00O =f'__{timi_new()}'#line:1087
            O0O0OO0O0OOOO0OO0 ={'source':'scsc','authorization':OO0O0O0OOOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O000OOO00O ),'signstring':O000000O000OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1098
            O0O0O0O0OOOO0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0OO0O0OOOO0OO0 ).json ()#line:1099
            if 'status'in O0O0O0O0OOOO0O0O0 :#line:1101
                if O0O0O0O0OOOO0O0O0 ['status']==200 :#line:1102
                    OOO0000000O000OOO =O0O0O0O0OOOO0O0O0 ['data']['clover']#line:1103
                    O0OO0OO00000OOOOO =O0O0O0O0OOOO0O0O0 ['data']['used_clover']#line:1104
                    O0000OOOOOOOO0000 =float (OOO0000000O000OOO )-float (O0OO0OO00000OOOOO )#line:1105
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0OO00000OOOOO}')#line:1106
                    if OO0O0O0OOOOO00OOO .certification ()!='未实名':#line:1107
                        if O0000OOOOOOOO0000 >1 :#line:1108
                            O000000O000OOO00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000OOOOOOOO0000)}_{timi_new()}'#line:1109
                            OO00O0O0O0O0O000O ={'source':'scsc','authorization':OO0O0O0OOOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O000OOO00O ),'signstring':O000000O000OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1120
                            OOO000OOO00OO00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000OOOOOOOO0000 )}#line:1121
                            O0O0000O0O000O00O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO00O0O0O0O0O000O ,data =OOO000OOO00OO00OO ).json ()#line:1122
                            if 'status'in O0O0000O0O000O00O :#line:1124
                                if O0O0000O0O000O00O ['status']==200 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O0O0000O0O000O00O["data"]["isSuccess"]}丨数量:{O0000OOOOOOOO0000}')#line:1126
                                if O0O0000O0O000O00O ['status']==500 :#line:1127
                                    print (f'【参与抽奖】:添加☘️:{O0O0000O0O000O00O["message"]}')#line:1128
            O0OO0OO0O000O0OOO =requests .request ('get',f'{host}/lottery',headers =O0O0OO0O0OOOO0OO0 ).json ()#line:1129
            O0O0OO0OO0OOOO000 =OO0O0O0OOOOO00OOO .winning_rewards ()#line:1131
            if 'status'in O0OO0OO0O000O0OOO :#line:1132
                if O0OO0OO0O000O0OOO ['status']==200 :#line:1133
                    O00OO000O0O00OO00 =O0OO0OO0O000O0OOO ['data'][0 ]['day_get_gold_quantity']#line:1134
                    golden_seed +=float (O00OO000O0O00OO00 )#line:1135
                    OO000O0OOOO00O000 =O0OO0OO0O000O0OOO ['data'][1 ]['value']#line:1136
                    OO000O000000O0000 =O0OO0OO0O000O0OOO ['data'][0 ]['join_number']#line:1137
                    O0O0O0O00OOOOO0OO =int (float (O0OO0OO0O000O0OOO ['data'][0 ]['totalValue']))#line:1138
                    OO0O0OO00OOOO0O00 =float (OO000O0OOOO00O000 /O0O0O0O00OOOOO0OO )*10000 #line:1139
                    O00O0OOOOOOO00000 =O0O0O0O00OOOOO0OO /OO000O000000O0000 #line:1140
                    print (f'【参与抽奖】:预计每天中{str(O00OO000O0O00OO00)[:6]}颗金种子丨好友收益:{str(O0O0OO0OO0OOOO000)[:6]}')#line:1141
                    print (f'【抽奖统计】:每1万☘️中{str(OO0O0OO00OOOO0O00)[:6]}颗金种子丨☘️人均:{str(O00O0OOOOOOO00000)[:7]}️')#line:1142
        except Exception as O0OOOO0O000O00000 :#line:1143
            print (O0OOOO0O000O00000 )#line:1144
    def energy (OOOOO0O0O00O0O0O0 ):#line:1147
        try :#line:1148
            while True :#line:1149
                O00OOOOO00O0OO0OO =f'__{timi_new()}'#line:1150
                O000000O0O0O00O00 ={'source':'scsc','authorization':OOOOO0O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO00O0OO0OO ),'signstring':O00OOOOO00O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1161
                OOO000O0OO0OO00OO =requests .request ('get',f'{host}/energy/general',headers =O000000O0O0O00O00 ).json ()#line:1162
                if 'status'in OOO000O0OO0OO00OO :#line:1164
                    if OOO000O0OO0OO00OO ['status']==200 :#line:1165
                        O0O0O0O0OOOOO00OO =OOO000O0OO0OO00OO ['data']['ordinary_water']#line:1166
                        O00O0O00OOO0000O0 =OOO000O0OO0OO00OO ['data']['ordinary_fertilizer']#line:1167
                        OO0OOO00OO0O0O00O =OOO000O0OO0OO00OO ['data']['videoStatus']#line:1168
                        OO0OO0OOOO000O0O0 =OOO000O0OO0OO00OO ['data']['waterVideoKey']#line:1169
                        print (f'【我的营养】:肥料:{str(O00O0O00OOO0000O0).split(".")[0]}丨水滴:{str(O0O0O0O0OOOOO00OO).split(".")[0]}')#line:1171
                        if float (O00O0O00OOO0000O0 )<96 :#line:1172
                            if OO0OOO00OO0O0O00O :#line:1173
                                time .sleep (random .randint (160 ,180 )/10 )#line:1174
                                OO00O000OOOO0O0OO =99 -float (O00O0O00OOO0000O0 )#line:1175
                                OO0OOOO00OOO00OOO ={"fertilizer":str (OO00O000OOOO0O0OO ).split ('.')[0 ]}#line:1176
                                O0OO0O0O00O000O00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000000O0O0O00O00 ).json ()#line:1178
                                if 'status'in O0OO0O0O00O000O00 :#line:1180
                                    if O0OO0O0O00O000O00 ['status']==200 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0O0O00O000O00["message"]}')#line:1182
                                    if O0OO0O0O00O000O00 ['status']==500 :#line:1183
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0O0O00O000O00["message"]}')#line:1184
                                        break #line:1185
                                if float (O00O0O00OOO0000O0 )<78 :#line:1187
                                    OO00O000OOOO0O0OO =80 -float (O00O0O00OOO0000O0 )#line:1188
                                    OO0O0O0OOO0O0OO0O =f'_fertilizer={int(OO00O000OOOO0O0OO)}_{timi_new()}'#line:1189
                                    OOO0OOO0OO00O0O00 ={'source':'scsc','authorization':OOOOO0O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO0O0OO0O ),'signstring':OO0O0O0OOO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1200
                                    OOO0OOOO0O0OO0000 ={"fertilizer":int (OO00O000OOOO0O0OO )}#line:1201
                                    OOOOO00000OO0OO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0OOO0OO00O0O00 ,data =OOO0OOOO0O0OO0000 ).json ()#line:1203
                                    if 'status'in OOOOO00000OO0OO0O :#line:1205
                                        if OOOOO00000OO0OO0O ['status']==200 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OOOOO00000OO0OO0O["message"]}丨数量:{int(OO00O000OOOO0O0OO)}')#line:1207
                                        if OOOOO00000OO0OO0O ['status']==500 :#line:1208
                                            print (f'【购买肥料】:购买肥料:{OOOOO00000OO0OO0O["message"]}丨数量:{int(OO00O000OOOO0O0OO)}')#line:1209
                                            O000OO00OO0OOOOOO =OOOOO00000OO0OO0O ["message"].split ('-')[1 ]#line:1210
                                            OOO000O0O0OOO0OOO =f'__{timi_new()}'#line:1211
                                            O0O00O000O0O0O000 ={'source':'scsc','authorization':OOOOO0O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0OOO0OOO ),'signstring':OOO000O0O0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1222
                                            OOO00O0O00OOO0O00 =requests .request ('get',f'{host}/user',headers =O0O00O000O0O0O000 ).json ()#line:1223
                                            if 'status'in OOO00O0O00OOO0O00 :#line:1224
                                                if OOO00O0O00OOO0O00 ['status']==200 :#line:1225
                                                    OO00OOO0O0O00OOOO =OOO00O0O00OOO0O00 ['data']['inner_id']#line:1226
                                                    if give_gold (OO00OOO0O0O00OOOO ,float (O000OO00OO0OOOOOO )+1 ):#line:1227
                                                        OOOOO0O0O00O0O0O0 .energy ()#line:1228
                        if float (O0O0O0O0OOOOO00OO )<880 :#line:1229
                            if OO0OO0OOOO000O0O0 :#line:1230
                                time .sleep (random .randint (160 ,180 )/10 )#line:1231
                                O0000OO0000O000OO =999 -float (O0O0O0O0OOOOO00OO )#line:1232
                                O00OO0OOO00000O00 ={"water":str (O0000OO0000O000OO ).split ('.')[0 ]}#line:1233
                                O0OO0OOO0OO0000OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000000O0O0O00O00 ).json ()#line:1235
                                if 'status'in O0OO0OOO0OO0000OO :#line:1237
                                    if O0OO0OOO0OO0000OO ['status']==200 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO0OOO0OO0000OO["message"]}')#line:1239
                                    if O0OO0OOO0OO0000OO ['status']==500 :#line:1240
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO0OOO0OO0000OO["message"]}')#line:1241
                                        break #line:1242
                                if float (O0O0O0O0OOOOO00OO )<780 :#line:1243
                                    O0000OO0000O000OO =800 -float (O0O0O0O0OOOOO00OO )#line:1244
                                    O0O00000O0O0000OO =f'_water={int(O0000OO0000O000OO)}_{timi_new()}'#line:1245
                                    O0O0OOOOOOOO0OOO0 ={'source':'scsc','authorization':OOOOO0O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00000O0O0000OO ),'signstring':O0O00000O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1256
                                    OOOO0OO0OO0O0OO00 ={"water":int (O0000OO0000O000OO )}#line:1257
                                    O00000OO0O00OO0O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0OOOOOOOO0OOO0 ,data =OOOO0OO0OO0O0OO00 ).json ()#line:1259
                                    if 'status'in O00000OO0O00OO0O0 :#line:1261
                                        if O00000OO0O00OO0O0 ['status']==200 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O00000OO0O00OO0O0["message"]}丨数量:{int(O0000OO0000O000OO)}')#line:1263
                                        if O00000OO0O00OO0O0 ['status']==500 :#line:1264
                                            print (f'【购买水滴】:购买水滴:{O00000OO0O00OO0O0["message"]}丨数量:{int(O0000OO0000O000OO)}')#line:1265
                                            O000OO00OO0OOOOOO =O00000OO0O00OO0O0 ["message"].split ('-')[1 ]#line:1266
                                            OOO000O0O0OOO0OOO =f'__{timi_new()}'#line:1267
                                            O0O00O000O0O0O000 ={'source':'scsc','authorization':OOOOO0O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0OOO0OOO ),'signstring':OOO000O0O0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1278
                                            OOO00O0O00OOO0O00 =requests .request ('get',f'{host}/user',headers =O0O00O000O0O0O000 ).json ()#line:1279
                                            if 'status'in OOO00O0O00OOO0O00 :#line:1280
                                                if OOO00O0O00OOO0O00 ['status']==200 :#line:1281
                                                    OO00OOO0O0O00OOOO =OOO00O0O00OOO0O00 ['data']['inner_id']#line:1282
                                                    if give_gold (OO00OOO0O0O00OOOO ,float (O000OO00OO0OOOOOO )+1 ):#line:1283
                                                        OOOOO0O0O00O0O0O0 .energy ()#line:1284
                        break #line:1285
        except Exception as OOOOOO0OOO0OO0O0O :#line:1286
            print (OOOOOO0OOO0OO0O0O )#line:1287
def bundled_def ():#line:1290
    OO0O0O0O00OOOOOOO =['5570536','7750212','7911652','7911680','7805624']#line:1291
    return OO0O0O0O00OOOOOOO [random .randint (0 ,len (OO0O0O0O00OOOOOOO )-1 )]#line:1292
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
        OO0OOO0OO000O0O00 =gitee_edition ()#line:1331
        if version_of_the_validation ()<OO0OOO0OO000O0O00 ['CityEarth']['edition']:#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO0OO000O0O00["CityEarth"]["edition"]}   ❌')#line:1333
            print (f'更新内容=>>{OO0OOO0OO000O0O00["CityEarth"]["content"]}')#line:1334
        else :#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0OOO0OO000O0O00["CityEarth"]["edition"]}   ✅')#line:1336
            print (f'更新内容=>> {OO0OOO0OO000O0O00["CityEarth"]["content"]}')#line:1337
    except Exception as OOOO00O00OOO00000 :#line:1338
        print (OOOO00O00OOO00000 )#line:1339
def sc3 ():#line:1342
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1343
if __name__ =='__main__':#line:1346
    start ()#line:1347
