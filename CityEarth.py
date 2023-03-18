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
        OO0000OO000O00000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO0000OO000O00000)}个账号==========")#line:17
        for OOO000O000O0O00OO in OO0000OO000O00000 :#line:18
            OOOOOO00O0O0O000O =[]#line:19
            print (f"------------正在执行第{OO0000OO000O00000.index(OOO000O000O0O00OO) + 1}个账号------------")#line:20
            O00OO0O00O00000O0 =CityEarth (OOO000O000O0O00OO ,OOOOOO00O0O0O000O ,OO0000OO000O00000 .index (OOO000O000O0O00OO ))#line:21
            def OO0O0OOO000O0O00O ():#line:23
                if O00OO0O00O00000O0 .base_info ():#line:25
                    O00OO0O00O00000O0 .sealing ()#line:27
                    O00OO0O00O00000O0 .invitenum ()#line:29
                    O00OO0O00O00000O0 .query_to_sell ()#line:31
                    O00OO0O00O00000O0 .friends_invitation ()#line:35
                    O00OO0O00O00000O0 .energy ()#line:37
                    O00OO0O00O00000O0 .add_clover ()#line:39
                    O00OO0O00O00000O0 .propsraffle ()#line:41
                    O00OO0O00O00000O0 .synthetic ()#line:43
                    O00OO0O00O00000O0 .crops_illustrated ()#line:45
                    O00OO0O00O00000O0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O00OO0O00O00000O0 .give_gold ()#line:50
            O00OOOO0OO00OOOO0 =threading .Thread (target =OO0O0OOO000O0O00O )#line:52
            O00OOOO0OO00OOOO0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O00O00O0O0OO0O0O0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O00O0O0OO0O0O0 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOO00O00OO0OO0OO0 in invited_new :#line:62
            print (OOO00O00OO0OO0OO0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O00OOOO0OO0O000OO in weishim :#line:65
            print (O00OOOO0OO0O000OO )#line:66
    except Exception as OOO0O0O0O0OOO000O :#line:67
        print (OOO0O0O0O0OOO000O )#line:68
def give_gold (OOOO0OO0OOO0000O0 ,O0OOOO0OO0O0OOOOO ):#line:72
    try :#line:73
        OOOO00O00OO000O0O =f'_doneeNo={OOOO0OO0OOO0000O0}&quantity={int(O0OOOO0OO0O0OOOOO)}_{timi_new()}'#line:74
        OOOOOOO00O0000O00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO000O0O ),'signstring':OOOO00O00OO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O00O000O0O0O0O00O ={"quantity":int (O0OOOO0OO0O0OOOOO ),"doneeNo":OOOO0OO0OOO0000O0 }#line:89
        OOO0O0O0OOOOOOO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOOO00O0000O00 ,data =O00O000O0O0O0O00O ).json ()#line:90
        if 'status'in OOO0O0O0OOOOOOO00 :#line:92
            if OOO0O0O0OOOOOOO00 ['status']==200 :#line:93
                if OOO0O0O0OOOOOOO00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0OOOO0OO0O0OOOOO)}种子给{OOOO0OO0OOO0000O0}成功')#line:95
                    return True #line:96
            if OOO0O0O0OOOOOOO00 ['status']==401 :#line:97
                print (f'【赠送种子】:{OOO0O0O0OOOOOOO00["message"]}')#line:98
                return False #line:99
            if OOO0O0O0OOOOOOO00 ['status']==500 :#line:100
                print (f'【赠送种子】:{OOO0O0O0OOOOOOO00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0OOO0000OOO0OOOO :#line:104
        print (O0OOO0000OOO0OOOO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO00O0O0OO00OO0OO ):#line:115
    OOOOO0000O00OOOOO =hashlib .md5 (OO00O0O0OO00OO0OO .encode ()).hexdigest ()#line:116
    OO00OOOOO0O00OO0O =sc1 ()#line:117
    O0OO0O00000OO00OO =sc2 ()#line:118
    OOOOOOO000000O000 =sc3 ()#line:119
    O0OOOOO0OOOO00O00 =OO00OOOOO0O00OO0O +OOOOO0000O00OOOOO +O0OO0O00000OO00OO +OOOOOOO000000O000 #line:120
    O0O00OOOOO00OOOO0 =hashlib .md5 (O0OOOOO0OOOO00O00 .encode ()).hexdigest ()#line:121
    return O0O00OOOOO00OOOO0 #line:122
def format_msg ():#line:125
    O0OO0000O00O00000 =""#line:126
    for OO0O000O0O000O000 in msg_list :#line:127
        O0OO0000O00O00000 +=str (OO0O000O0O000O000 )+"\r\n"#line:128
    return O0OO0000O00O00000 #line:129
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
def get_json_data (OOOO0O0O0O00OO00O ,OO00O0O0O00O000OO ,OO0OO000000OOOOO0 ,OO00OOO00O0OO0000 ):#line:153
    with open (OOOO0O0O0O00OO00O ,'rb')as OOO0OO00OO0OO0OO0 :#line:154
        OO0000OOOOO0O00OO =json .load (OOO0OO00OO0OO0OO0 )#line:155
        OO0000OOOOO0O00OO ['data'][OO00O0O0O00O000OO ][OO0OO000000OOOOO0 ]=OO00OOO00O0OO0000 #line:156
        O000OOO0O0OOOOOO0 =OO0000OOOOO0O00OO #line:157
    OOO0OO00OO0OO0OO0 .close ()#line:158
    return O000OOO0O0OOOOOO0 #line:159
def write_json_data (O0OO0OO00OO0OO0O0 ):#line:162
    with open (json_path1 ,'w')as O0OOO0OOO0OOO0000 :#line:163
        json .dump (O0OO0OO00OO0OO0O0 ,O0OOO0OOO0OOO0000 )#line:164
    O0OOO0OOO0OOO0000 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OO000O0O00O0OOO ,OO000O0OOOO0000O0 ,O000O0O000000O000 ,O0OOO000O000000OO ):#line:171
        try :#line:172
            O0OO000O0O00O0OOO .msg =O000O0O000000O000 #line:173
            O0OO000O0O00O0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OO000O0O00O0OOO .token =OO000O0OOOO0000O0 ['authorization']#line:175
            O0OO000O0O00O0OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OO000O0O00O0OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OO000O0O00O0OOO .elephant_user =OO000O0OOOO0000O0 ['elephant_user']#line:178
            O0OO000O0O00O0OOO .elephant_pswd =OO000O0OOOO0000O0 ['elephant_pswd']#line:179
            O0OO000O0O00O0OOO .elephant_Task_ID =OO000O0OOOO0000O0 ['elephant_Task_ID']#line:180
            O0OO000O0O00O0OOO .len_new =O0OOO000O000000OO #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOOOO0O00O00O00O ):#line:186
        try :#line:187
            OOOOOO0O00O00O00O .watched_ad ()#line:189
            O0OO0OO0O000OOO0O =f'__{timi_new()}'#line:190
            O00O0O0OO0O000O0O ={'source':'scsc','authorization':OOOOOO0O00O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O000OOO0O ),'signstring':O0OO0OO0O000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O000O0000OO00OO00 =requests .request ('get',f'{host}/user',headers =O00O0O0OO0O000O0O ).json ()#line:202
            if 'status'in O000O0000OO00OO00 :#line:204
                if O000O0000OO00OO00 ['status']==200 :#line:205
                    O00OO0O00OOO0O000 =O000O0000OO00OO00 ['data']['nickname']#line:206
                    OO0OOOOO00O00OOO0 =O000O0000OO00OO00 ['data']['inner_id']#line:207
                    O0O00O0OO00OO0OO0 =O000O0000OO00OO00 ['data']['assets']['gold']#line:208
                    OOOOO0O00000OOOO0 =O000O0000OO00OO00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00OO0O00OOO0O000[:5]}丨ID:{OO0OOOOO00O00OOO0}丨等级:{OOOOO0O00000OOOO0}丨金种子:{str(O0O00O0OO00OO0OO0).split(".")[0]}')#line:211
                    if 'wx_'in O00OO0O00OOO0O000 :#line:212
                        OOOOOO0O00O00O00O .change_nickname ()#line:213
                if O000O0000OO00OO00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOOOO0O00O00O00O .elephant_user =='f':#line:216
                        return False #line:217
                    OO00O0OO0O0OOO0O0 =Invalid_login .addtask (elephant_user =OOOOOO0O00O00O00O .elephant_user ,elephant_pswd =OOOOOO0O00O00O00O .elephant_pswd ,elephant_Task_ID =OOOOOO0O00O00O00O .elephant_Task_ID )#line:220
                    O0O000O00OO0O0000 =get_json_data (json_path ,OOOOOO0O00O00O00O .len_new ,'authorization',OO00O0OO0O0OOO0O0 )#line:221
                    if write_json_data (O0O000O00OO0O0000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O000O0000OO00OO00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O00OO00OOOO00O0OO :#line:228
            print (O00OO00OOOO00O0OO )#line:229
    def sealing (OOOOOO000O0O0OO0O ):#line:232
        try :#line:233
            O0OO000O0O0O0O00O =f'__{timi_new()}'#line:234
            O0OOO0000000000O0 ={'source':'scsc','authorization':OOOOOO000O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O0O0O0O00O ),'signstring':O0OO000O0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0000000000O0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0000000000O0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0000000000O0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0000000000O0 )#line:249
            requests .request ('get',f'{host}/user',headers =O0OOO0000000000O0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0000000000O0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0000000000O0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0000000000O0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0000000000O0 )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OOO0000000000O0 )#line:255
        except Exception as O0O0O0OOOOOO00O00 :#line:256
            print (O0O0O0OOOOOO00O00 )#line:257
    def ddd (O00OO000O0OO0O000 ):#line:259
        try :#line:260
            OO00O0O0000O00O0O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO000OOO0OO0O00OO ={'source':'scsc','authorization':O00OO000O0OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0000O00O0O ),'signstring':OO00O0O0000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOOO00OO000000OO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO000OOO0OO0O00OO ).json ()#line:273
            print (OOOO00OO000000OO0 )#line:274
        except Exception as OO0OOOO000000OOO0 :#line:277
            print (OO0OOOO000000OOO0 )#line:278
    def the_query (O00OOO0O0O0O00OO0 ):#line:283
        try :#line:284
            OOOOOO0000O0000OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0OOOOOOO0O0O0000 ={'authorization':O00OOO0O0O0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000O0000OO ),'signstring':OOOOOO0000O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOO0O0OOO0OO00000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOOOOOO0O0O0000 ).json ()#line:297
            if 'status'in OOO0O0OOO0OO00000 :#line:299
                if OOO0O0OOO0OO00000 ['status']==200 :#line:300
                    OO00000O00O000O00 =OOO0O0OOO0OO00000 ['data']['rows'][4 ]['price']#line:301
                    return OO00000O00O000O00 #line:302
        except Exception as OO0O0000OOOOO00O0 :#line:303
            print (OO0O0000OOOOO00O0 )#line:304
    def market_sale (OOOO00OO0000O0OO0 ,OO000OO0OOO0OOOOO ):#line:307
        try :#line:308
            O0OO00O000O00OO00 =timi_new ()#line:309
            O0O0OOO0OOOOO0000 =f'type=crop__{O0OO00O000O00OO00}'#line:310
            O0O000000OOOO00O0 ={'source':'scsc','authorization':OOOO00OO0000O0OO0 .token ,'timestamp':str (O0OO00O000O00OO00 ),'sign':sign (O0O0OOO0OOOOO0000 ),'signstring':O0O0OOO0OOOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:321
            OOO0OOO000O0OOOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O000000OOOO00O0 ).json ()#line:323
            if 'status'in OOO0OOO000O0OOOO0 :#line:325
                if OOO0OOO000O0OOOO0 ['status']==200 :#line:326
                    if OOO0OOO000O0OOOO0 ['data']['rows']:#line:327
                        OO0000OO00O0OOO00 =OOO0OOO000O0OOOO0 ['data']['rows'][0 ]['packsackItemId']#line:328
                        OOO0O0OO00OO00O00 =OOO0OOO000O0OOOO0 ['data']['rows'][0 ]['quantity']#line:329
                        OOO0O0O0O000OOOOO =float (OO000OO0OOO0OOOOO )-0.001 #line:330
                        if OOO0O0O0O000OOOOO >9 :#line:331
                            OOO000O00O0OO0OOO =f'_packsackItemId={OO0000OO00O0OOO00}&price={str(OO000OO0OOO0OOOOO)[:5]}&quantity={OOO0O0OO00OO00O00}_{O0OO00O000O00OO00}'#line:332
                            O00OO0OO000O00OO0 ={'source':'scsc','authorization':OOOO00OO0000O0OO0 .token ,'timestamp':str (O0OO00O000O00OO00 ),'sign':sign (OOO000O00O0OO0OOO ),'signstring':OOO000O00O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
                            O000O0O0O0OO00000 ={"packsackItemId":OO0000OO00O0OOO00 ,"price":str (OO000OO0OOO0OOOOO )[:5 ],"quantity":str (OOO0O0OO00OO00O00 )}#line:348
                            O0OO000OOOO00OO00 =requests .request ('post',f'{host}/market/sale',headers =O00OO0OO000O00OO0 ,data =O000O0O0O0OO00000 ).json ()#line:349
                            if 'status'in O0OO000OOOO00OO00 :#line:351
                                if O0OO000OOOO00OO00 ['status']==200 :#line:352
                                    print (f'【上架芦荟】:数量:{OOO0O0OO00OO00O00}丨价格:{str(OO000OO0OOO0OOOOO)[:5]}')#line:353
        except Exception as OOOOOOO0O0000000O :#line:354
            print (OOOOOOO0O0000000O )#line:355
    def query_to_sell (OO00O000000OOOOOO ):#line:358
        global count_list #line:359
        try :#line:360
            O00000OOO00OO00O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:361
            OOO00OO00OOOO00OO ={'source':'scsc','authorization':OO00O000000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO00OO00O0 ),'signstring':O00000OOO00OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:372
            O000OOO00O00OOO00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00OO00OOOO00OO ).json ()#line:373
            if 'status'in O000OOO00O00OOO00 :#line:375
                if O000OOO00O00OOO00 ['status']==200 :#line:376
                    for OO00O00OO0OOO0OO0 in O000OOO00O00OOO00 ['data']['rows']:#line:377
                        O00OOOO00OOOOO0O0 =OO00O00OO0OOO0OO0 ['materialKey']#line:378
                        OOO0O000O0O0000OO =OO00O00OO0OOO0OO0 ['quantity']#line:379
                        OO0OOO0O00OOOOOO0 =OO00O00OO0OOO0OO0 ['price']#line:380
                        O00O0OO0O0OOO0OOO =OO00O00OO0OOO0OO0 ['saleState']#line:381
                        if O00O0OO0O0OOO0OOO ==0 :#line:382
                            print (f'【出售订单】:名称:{O00OOOO00OOOOO0O0}丨数量:{OOO0O000O0O0000OO}丨价格:{OO0OOO0O00OOOOOO0}')#line:383
                            count_list +=OOO0O000O0O0000OO #line:384
                            OO00O00000O000OO0 =OO00O000000OOOOOO .the_query ()#line:386
                            if float (OO00O00000O000OO0 )!=float (OO0OOO0O00OOOOOO0 ):#line:387
                                OOOOO00OO0OOOOOOO =OO00O00OO0OOO0OO0 ['id']#line:388
                                if float (datetime .datetime .now ().hour )>8 :#line:389
                                    OO00O000000OOOOOO .cacel_sale (OOOOO00OO0OOOOOOO )#line:390
                                    OO00O000000OOOOOO .market_sale (OO0OOO0O00OOOOOO0 )#line:391
                            OO00O000000OOOOOO .game_map ()#line:393
        except Exception as OOO00O000OO00OO00 :#line:395
            print (OOO00O000OO00OO00 )#line:396
    def cacel_sale (O00O000OOOOO00O00 ,OOOO0000O0OO00000 ):#line:399
        try :#line:400
            O0O00O00O00O0OOOO =f'_saleId={OOOO0000O0OO00000}_{timi_new()}'#line:401
            OO0OO0OO0OO00OO0O ={'source':'scsc','authorization':O00O000OOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O00O0OOOO ),'signstring':O0O00O00O00O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:412
            O0O0000O0OOO00000 ={"saleId":OOOO0000O0OO00000 }#line:413
            OO0O00O00OO00OOO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO0OO0OO00OO0O ,data =O0O0000O0OOO00000 ).json ()#line:414
            if 'status'in OO0O00O00OO00OOO0 :#line:416
                if OO0O00O00OO00OOO0 ['status']==200 :#line:417
                    print (f'【下架出售】:{OO0O00O00OO00OOO0["data"]}')#line:418
        except Exception as OOO0O0OO00OO00OO0 :#line:419
            print (OOO0O0OO00OO00OO0 )#line:420
    def change_nickname (OO00OO00OO0O0OOO0 ):#line:423
        try :#line:424
            O0O0O00000OOO0O0O =timi_new ()#line:425
            OO0O00OO0O0O0O0OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:426
            O0000OOOOO0000000 =requests .request ('post','https://www.qmsjmfb.com/',data =OO0O00OO0O0O0O0OO ).text #line:427
            O0OOO0000000O0OOO =re .findall ('<ul><li>(.*?)</li>',O0000OOOOO0000000 )[0 ][:3 ]#line:428
            OOOO00OOO000O0O0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0OOO0000000O0OOO}').json ()#line:429
            O00O00O0000OO00O0 =OOOO00OOO000O0O0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:430
            O0O00000O00000O0O ={"nickname":O00O00O0000OO00O0 }#line:431
            O00O00O0000OO0OOO =f'_nickname={O00O00O0000OO00O0}_{O0O0O00000OOO0O0O}'#line:432
            O0000O0OO0O0O0OO0 ={'source':'scsc','authorization':OO00OO00OO0O0OOO0 .token ,'timestamp':O0O0O00000OOO0O0O ,'sign':sign (O00O00O0000OO0OOO ),'signstring':O00O00O0000OO0OOO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:443
            OO0OOO0OO0O0000OO =requests .request ('patch',f'{host}/user/nickname',headers =O0000O0OO0O0O0OO0 ,data =O0O00000O00000O0O ).json ()#line:444
            if 'status'in OO0OOO0OO0O0000OO :#line:446
                if OO0OOO0OO0O0000OO ['status']==200 :#line:447
                    print (f'【修改网名】:网名:{O00O00O0000OO00O0}丨{OO0OOO0OO0O0000OO["message"]}')#line:448
        except Exception as O0OOO0OOOO0000O00 :#line:449
            print (O0OOO0OOOO0000O00 )#line:450
    def withdraw (OO0O00OO0OO0O0O0O ):#line:453
        try :#line:454
            O0O0O0O00O0OOO000 =f'__{timi_new()}'#line:455
            O000OO0O0OOOO0000 ={'source':'scsc','authorization':OO0O00OO0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0OOO000 ),'signstring':O0O0O0O00O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:466
            OOOO00O00OO0O00O0 =requests .request ('get',f'{host}/assets',headers =O000OO0O0OOOO0000 ).json ()#line:467
            if 'status'in OOOO00O00OO0O00O0 :#line:469
                if OOOO00O00OO0O00O0 ['status']==200 :#line:470
                    OOOO0O0000OOOO000 =OOOO00O00OO0O00O0 ['data']['cash']#line:471
                    if float (OOOO0O0000OOOO000 )>20 :#line:472
                        O0O0O0O00O0OOO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:473
                        O000OO0O0OOOO0000 ={'authorization':OO0O00OO0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0OOO000 ),'signstring':O0O0O0O00O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        O000O00OO0O0O0O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:484
                        OO00OO0OOO0O00OOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000OO0O0OOOO0000 ,data =O000O00OO0O0O0O0O ).json ()#line:486
                        if 'status'in OO00OO0OOO0O00OOO :#line:488
                            if OO00OO0OOO0O00OOO ['status']==200 :#line:489
                                print (f'【余额提现】:{OO00OO0OOO0O00OOO["data"]}')#line:490
                        if 'status'in OO00OO0OOO0O00OOO :#line:491
                            if OO00OO0OOO0O00OOO ['status']==500 :#line:492
                                print (f'【余额提现】:{OO00OO0OOO0O00OOO["message"]}')#line:493
        except Exception as O0O00OO0OOO0O0O0O :#line:494
            print (O0O00OO0OOO0O0O0O )#line:495
    def invitenum (O00OO0OO00OO000O0 ):#line:498
        global invited_new #line:499
        try :#line:500
            OO0O0000OO0OOOOOO =f'__{timi_new()}'#line:501
            OOOO0OO00000O00OO ={'source':'scsc','authorization':O00OO0OO00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO0OOOOOO ),'signstring':OO0O0000OO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
            O000000O0O0O000O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0OO00000O00OO ).json ()#line:513
            if 'status'in O000000O0O0O000O0 :#line:515
                if O000000O0O0O000O0 ['status']==200 :#line:516
                    OOOO0OO0000000OO0 =O000000O0O0O000O0 ['data']['invited_count']#line:517
                    OO0OOOOO00O00OO0O =O000000O0O0O000O0 ['data']['invited_second_count']#line:518
                    print (f'【我的邀请】:直邀好友:{OOOO0OO0000000OO0}丨间邀好友:{OO0OOOOO00O00OO0O}')#line:519
                    if OOOO0OO0000000OO0 <2 :#line:520
                        O000OO00OO0O00O00 =f'__{timi_new()}'#line:521
                        O00O00O0O0OOOOOOO ={'source':'scsc','authorization':O00OO0OO00OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OO0O00O00 ),'signstring':O000OO00OO0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:532
                        OO00O0OOO0OO0OOOO =requests .request ('get',f'{host}/user',headers =O00O00O0O0OOOOOOO ).json ()#line:533
                        if 'status'in OO00O0OOO0OO0OOOO :#line:535
                            if OO00O0OOO0OO0OOOO ['status']==200 :#line:536
                                invited_new .append (OO00O0OOO0OO0OOOO ['data']['inner_id'])#line:537
        except Exception as OO000O0OO00OO00OO :#line:538
            print (OO000O0OO00OO00OO )#line:539
    def game_map (OO000OO00000OO00O ):#line:542
        try :#line:543
            OO00OO0OO0OOOOO0O =f'__{timi_new()}'#line:544
            O0O00O00O00OO00O0 ={'source':'scsc','authorization':OO000OO00000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OOOOO0O ),'signstring':OO00OO0OO0OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
            O0O000OOO0OO0O0O0 =requests .request ('get',f'{host}/game/map',headers =O0O00O00O00OO00O0 ).json ()#line:556
            if 'status'in O0O000OOO0OO0O0O0 :#line:558
                if O0O000OOO0OO0O0O0 ['status']==200 :#line:559
                    for OO00O000OO0OO000O in O0O000OOO0OO0O0O0 ['data']['list'][0 ]['crops']:#line:560
                        OO00000OOOO00O00O =OO00O000OO0OO000O ['level']#line:562
                        if OO00000OOOO00O00O ==41 :#line:563
                            O0O0OOOO0OO0OO0O0 =OO00O000OO0OO000O ['crop_name']#line:564
                            OO00OO00O0O000OO0 =OO00O000OO0OO000O ['count']#line:565
                            if OO00OO00O0O000OO0 >0 :#line:566
                                print (f'【农业资产】:{O0O0OOOO0OO0OO0O0}丨数量:{OO00OO00O0O000OO0}')#line:567
                                if float (datetime .datetime .now ().hour )>8 :#line:568
                                    OO000OO00000OO00O .the_query ()#line:569
        except Exception as O0O00O0000OOOOOOO :#line:570
            print (O0O00O0000OOOOOOO )#line:571
    def give_gold (OO00OO00O00O0O000 ):#line:574
        try :#line:575
            OOOOOO0OOO0OO0O0O =f'__{timi_new()}'#line:576
            O0OOO00OO0O0OOOO0 ={'source':'scsc','authorization':OO00OO00O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOO0OO0O0O ),'signstring':OOOOOO0OOO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            O00OOOOO0O0O0O00O =requests .request ('get',f'{host}/user',headers =O0OOO00OO0O0OOOO0 ).json ()#line:588
            if 'status'in O00OOOOO0O0O0O00O :#line:589
                if O00OOOOO0O0O0O00O ['status']==200 :#line:590
                    if float (OO00OO00O00O0O000 .doneeNo )!=0 :#line:591
                        OOO0OOO00O0O0000O =O00OOOOO0O0O0O00O ['data']['assets']['gold']#line:592
                        if float (OOO0OOO00O0O0000O )>float (OO00OO00O00O0O000 .innerId ):#line:593
                            O00OOOOO000OOO0OO =int (float (OOO0OOO00O0O0000O )/1.1 )#line:594
                            OOOOOO0OOO0OO0O0O =f'_doneeNo={OO00OO00O00O0O000.doneeNo}&quantity={O00OOOOO000OOO0OO}_{timi_new()}'#line:595
                            O0OOO00OO0O0OOOO0 ={'source':'scsc','authorization':OO00OO00O00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOO0OO0O0O ),'signstring':OOOOOO0OOO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:606
                            O00OOO0OO00OO00OO ={"quantity":O00OOOOO000OOO0OO ,"doneeNo":OO00OO00O00O0O000 .doneeNo }#line:610
                            O00000O0OOO000OOO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO00OO0O0OOOO0 ,data =O00OOO0OO00OO00OO ).json ()#line:611
                            if 'status'in O00000O0OOO000OOO :#line:613
                                if O00000O0OOO000OOO ['status']==200 :#line:614
                                    if O00000O0OOO000OOO ['data']:#line:615
                                        print (f'【赠送种子】:赠送{O00OOOOO000OOO0OO}种子给{OO00OO00O00O0O000.doneeNo}成功')#line:616
                    else :#line:617
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:618
        except Exception as O00OOO0OO00O0O0O0 :#line:619
            print (O00OOO0OO00O0O0O0 )#line:620
    def invitation (O00000OOO0OOO0O0O ):#line:622
        try :#line:623
            _OO00O0000OOOO0OO0 =float (bundled_def ())/4 #line:624
            O00OOO0000O00000O =f'_innerId={int(_OO00O0000OOOO0OO0)}_{timi_new()}'#line:625
            O0O00O0OO0O0OO000 ={'source':'scsc','authorization':O00000OOO0OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000O00000O ),'signstring':O00OOO0000O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:636
            OOO0000OO00O0OOOO ={"innerId":int (_OO00O0000OOOO0OO0 )}#line:637
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O00O0OO0O0OO000 ,data =OOO0000OO00O0OOOO )#line:638
        except Exception as O0O0OOO0OOO00OOOO :#line:639
            print (O0O0OOO0OOO00OOOO )#line:640
    def winning_rewards (O000O0OO0OOOOO000 ):#line:643
        try :#line:644
            O0OO0O0O0O000OO00 =f'__{timi_new()}'#line:645
            OOOO00O000OO0O00O ={'source':'scsc','authorization':O000O0OO0OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0O000OO00 ),'signstring':O0OO0O0O0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
            OO00000OOOOOO0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOO00O000OO0O00O ).json ()#line:657
            if 'status'in OO00000OOOOOO0000 :#line:659
                if OO00000OOOOOO0000 ['status']==200 :#line:660
                    if OO00000OOOOOO0000 ['data']['amount']:#line:661
                        O00O0000OO00O0000 =OO00000OOOOOO0000 ['data']['amount']['gold']#line:662
                        return O00O0000OO00O0000 #line:663
                    else :#line:664
                        return 0 #line:665
        except Exception as OO0O0OO0OOO00OOO0 :#line:666
            print (OO0O0OO0OOO00OOO0 )#line:667
    def certification (OO000OO0000O000OO ):#line:670
        try :#line:671
            OO00O0O0O0000O000 =f'__{timi_new()}'#line:672
            O0OO0OOOOO00O0000 ={'source':'scsc','authorization':OO000OO0000O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0O0000O000 ),'signstring':OO00O0O0O0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            O00OO0OOO00O000OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0OOOOO00O0000 ).json ()#line:684
            if 'status'in O00OO0OOO00O000OO :#line:686
                if O00OO0OOO00O000OO ['status']==200 :#line:687
                    if O00OO0OOO00O000OO ['data']['result']:#line:688
                        OO00OOO0OOO00O0OO =O00OO0OOO00O000OO ['data']['nick_name']#line:689
                        return OO00OOO0OOO00O0OO #line:690
                    else :#line:691
                        return '未实名'#line:692
        except Exception as OOOOO0O00O00OOO0O :#line:693
            print (OOOOO0O00O00OOO0O )#line:694
    def crops_illustrated (OO00OOOO0O00000O0 ):#line:697
        try :#line:698
            OOOO0O0OOO0OOO0O0 =f'__{timi_new()}'#line:699
            OO0O000000OOOOO0O ={'source':'scsc','authorization':OO00OOOO0O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOO0OOO0O0 ),'signstring':OOOO0O0OOO0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:710
            OOO0000O00O0000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O000000OOOOO0O ).json ()#line:711
            if 'status'in OOO0000O00O0000O0 :#line:713
                if OOO0000O00O0000O0 ['status']==200 :#line:714
                    O0O00000000O0OOO0 =OOO0000O00O0000O0 ['data'][0 ]['crops']#line:715
                    for O0O000O0OOO0O0O00 in O0O00000000O0OOO0 :#line:716
                        if O0O000O0OOO0O0O00 ['ill_clover_award']:#line:717
                            if float (O0O000O0OOO0O0O00 ['ill_clover_award'])>1 :#line:718
                                if O0O000O0OOO0O0O00 ['is_finish']:#line:719
                                    if not O0O000O0OOO0O0O00 ['is_getit']:#line:720
                                        if OO00OOOO0O00000O0 .certification ()!='未实名':#line:721
                                            OOOO0O0OOO0OOO0O0 =f'_award_level={O0O000O0OOO0O0O00["level"]}_{timi_new()}'#line:722
                                            OO0O000000OOOOO0O ={'source':'scsc','authorization':OO00OOOO0O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOO0OOO0O0 ),'signstring':OOOO0O0OOO0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:733
                                            OO0000OOOO00O0OO0 ={"award_level":O0O000O0OOO0O0O00 ['level']}#line:734
                                            O0O0OO0OO0OO0O0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O000000OOOOO0O ,json =OO0000OOOO00O0OO0 ).json ()#line:736
                                            if 'status'in O0O0OO0OO0OO0O0OO :#line:737
                                                if O0O0OO0OO0OO0O0OO ['status']==200 :#line:738
                                                    O0000O00OO0OOO0O0 =O0O0OO0OO0OO0O0OO ['data']['ill_clover_award']#line:739
                                                    print (f'【图鉴奖励】:领取{O0O000O0OOO0O0O00["crop_name"]}成就丨奖励{O0000O00OO0OOO0O0}☘️')#line:741
                                                if O0O0OO0OO0OO0O0OO ['status']==500 :#line:742
                                                    print (f'【图鉴奖励】:{O0O0OO0OO0OO0O0OO["message"]}')#line:743
        except Exception as O0OOOOOO00O0O0OO0 :#line:744
            print (O0OOOOOO00O0O0OO0 )#line:745
    def watched_ad (O0000OO0O000O00OO ):#line:748
        try :#line:749
            OO000O0O000OOOO0O =f'__{timi_new()}'#line:750
            OOOOO0O0OOOO00OOO ={'source':'scsc','authorization':O0000OO0O000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O000OOOO0O ),'signstring':OO000O0O000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            OOOOOO0O0OO0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0O0OOOO00OOO ).json ()#line:762
            if 'status'in OOOOOO0O0OO0O00O0 :#line:764
                if OOOOOO0O0OO0O00O0 ['status']==200 :#line:765
                    if 'offlineInfo'in OOOOOO0O0OO0O00O0 ['data']:#line:766
                        time .sleep (random .randint (1 ,3 ))#line:767
                        OO0OO000O00O0OOOO =OOOOOO0O0OO0O00O0 ['data']['offlineInfo']['off_minute']#line:768
                        OO0OOOO0OOO000OOO =float (OOOOOO0O0OO0O00O0 ['data']['silver'])/1000000000000 #line:769
                        time .sleep (1 )#line:770
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOOO0O0OOOO00OOO ).json ()#line:771
                        time .sleep (2 )#line:772
                        OOOO00O00OO0OO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO0O0OOOO00OOO ).json ()#line:773
                        if 'status'in OOOO00O00OO0OO0O0 :#line:775
                            if OOOO00O00OO0OO0O0 ['status']==200 :#line:776
                                OO000OO0O0O0O0OO0 =float (OOOO00O00OO0OO0O0 ['data']['silver'])/1000000000000 #line:777
                                OO00OOOO0OO000OOO =str (OO000OO0O0O0O0OO0 -OO0OOOO0OOO000OOO )[:6 ]#line:778
                                print (f'【离线奖励】:翻倍离线{OO0OO000O00O0OOOO}分钟奖励🌱数量:{OO00OOOO0OO000OOO}t粒')#line:779
        except Exception as O0OOOOO0O00OOO00O :#line:780
            print (O0OOOOO0O00OOO00O )#line:781
    def user_ad (OOO000000000OO00O ):#line:784
        try :#line:785
            OO0OO0OO00O00000O =f'__{timi_new()}'#line:786
            O00OOOOO0O000O00O ={'source':'scsc','authorization':OOO000000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00O00000O ),'signstring':OO0OO0OO00O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:797
            OOO000OOOO0OOOO00 =requests .request ('get',f'{host}/user/ad',headers =O00OOOOO0O000O00O ).json ()#line:798
            if 'status'in OOO000OOOO0OOOO00 :#line:800
                if OOO000OOOO0OOOO00 ['status']==200 :#line:801
                    OOO0OOO0OOO0O000O =OOO000OOOO0OOOO00 ['data']['max_time']#line:802
                    OO0O0O00O00OO0O0O =OOO000OOOO0OOOO00 ['data']['watch_time']#line:803
                    O0OOO0OO00O0O00O0 =OOO000OOOO0OOOO00 ['data']['added_time']#line:804
                    print (f'【获取种子】:获取🌱剩余{O0OOO0OO00O0O00O0 + OOO0OOO0OOO0O000O - OO0O0O00O00OO0O0O}次丨好友提供:{O0OOO0OO00O0O00O0}次')#line:805
                    if O0OOO0OO00O0O00O0 +OOO0OOO0OOO0O000O -OO0O0O00O00OO0O0O >0 :#line:806
                        time .sleep (random .randint (16 ,19 ))#line:807
                        O00O0O0O00O0OO000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOOOO0O000O00O ).json ()#line:808
                        if 'status'in O00O0O0O00O0OO000 :#line:810
                            if O00O0O0O00O0OO000 ['status']==200 :#line:811
                                OO0O0000O00O0OO00 =float (O00O0O0O00O0OO000 ['data']['silver'])/1000000000000 #line:812
                                print (f'【获取种子】:获得🌱:{int(OO0O0000O00O0OO00)}t粒')#line:813
                                return True #line:814
                            if O00O0O0O00O0OO000 ['status']==500 :#line:815
                                OO00OO0OOOOOOO0O0 =O00O0O0O00O0OO000 ['message']#line:816
                                print (f'【获取种子】:{OO00OO0OOOOOOO0O0}')#line:817
                                return False #line:818
        except Exception as OO0O00O0OOOO000OO :#line:819
            print (OO0O00O0OOOO000OO )#line:820
    def synthetic (O000OO0OOO00O0OO0 ):#line:823
        global id ,g #line:824
        try :#line:825
            OO0O000O0OOO000OO =O000OO0OOO00O0OO0 .level_new ()#line:826
            OO0OOO00O0O00O0O0 =random .randint (9 ,11 )#line:827
            OO000O00OO00O00OO =f'_site=8&targetSite={OO0OOO00O0O00O0O0}_{timi_new()}'#line:828
            OOO000O00O0O0OO00 ={'source':'scsc','authorization':O000OO0OOO00O0OO0 .token ,'timestamp':timi_new (),'sign':sign (OO000O00OO00O00OO ),'signstring':OO000O00OO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:839
            O0O000000OOOOO0O0 ={"site":int (8 ),"targetSite":int (OO0OOO00O0O00O0O0 )}#line:840
            requests .request ('post',f'{host}/game/crops/move',headers =OOO000O00O0O0OO00 ,json =O0O000000OOOOO0O0 )#line:841
            while True :#line:842
                OO00O0OO00O0O00OO =f'__{timi_new()}'#line:843
                OOO00000OOO00000O ={'source':'scsc','authorization':O000OO0OOO00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO00O0O00OO ),'signstring':OO00O0OO00O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                OOO00OO0O0O000000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000OOO00000O ).json ()#line:855
                if 'status'in OOO00OO0O0O000000 :#line:857
                    if OOO00OO0O0O000000 ['status']==200 :#line:858
                        OOO00OOO0O0OOO0OO =OOO00OO0O0O000000 ['data']['cropList']#line:859
                        O0OOO0O00OO0O00O0 =OOO00OO0O0O000000 ['data']['gameCoreDataDBid']#line:860
                        O00OO0OO000OO00OO =float (OOO00OO0O0O000000 ['data']['silver'])/1000000000000 #line:861
                        OOOO0O0O0OO000OO0 =0 #line:866
                        for O0OOOO0OO0OO0O0O0 in OOO00OOO0O0OOO0OO :#line:867
                            if not O0OOOO0OO0OO0O0O0 :#line:868
                                O0O0OO0OOOO0OOOO0 =f'_crop_id={O0OOO0O00OO0O00O0}&site={OOOO0O0O0OO000OO0}_{O000OO0OOO00O0OO0.time}'#line:869
                                O00000O00OO0OO0OO ={'source':'scsc','authorization':O000OO0OOO00O0OO0 .token ,'timestamp':O000OO0OOO00O0OO0 .time ,'sign':sign (O0O0OO0OOOO0OOOO0 ),'signstring':O0O0OO0OOOO0OOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:879
                                OOOO00OO00O0O00OO ={"site":OOOO0O0O0OO000OO0 ,"crop_id":O0OOO0O00OO0O00O0 }#line:880
                                OO000O00000O000O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O00000O00OO0OO0OO ,data =OOOO00OO00O0O00OO ).json ()#line:881
                                time .sleep (random .randint (1 ,3 )/10 )#line:883
                                if 'status'in OO000O00000O000O0 :#line:884
                                    if OO000O00000O000O0 ['status']==200 :#line:885
                                        if OO000O00000O000O0 ['message']=='种子数量不足':#line:886
                                            OO0O000O0OOO000OO =O000OO0OOO00O0OO0 .level_new ()#line:887
                                            print (f'【种植合成】:{OO000O00000O000O0["message"]}')#line:888
                                            if not O000OO0OOO00O0OO0 .user_ad ():#line:889
                                                return False #line:890
                                    if OO000O00000O000O0 ['status']==500 :#line:891
                                        print (f'【种植合成】:{OO000O00000O000O0["message"]}')#line:892
                                        return False #line:893
                            OOOO0O0O0OO000OO0 +=1 #line:894
                        O0OO0O000O00O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOO00000OOO00000O ).json ()#line:895
                        OOO0OOO0O00OOO00O =O0OO0O000O00O0OOO ['data']['cropList']#line:896
                        O00OO0OOO00OOO0OO =False #line:897
                        for O0OOOO0OO0OO0O0O0 in range (12 ):#line:898
                            id =OOO0OOO0O00OOO00O [O0OOOO0OO0OO0O0O0 ]['level']#line:899
                            if float (OO0O000O0OOO000OO )-float (id )>9 :#line:900
                                OO00O0OOOOOO000O0 =f'_site={O0OOOO0OO0OO0O0O0}_{timi_new()}'#line:901
                                OOO0O000O0O0OO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OO0OOO00O0OO0 .token ,'timestamp':timi_new (),'sign':sign (OO00O0OOOOOO000O0 ),'signstring':OO00O0OOOOOO000O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:912
                                OOOOO000OOO0O0O00 ={"site":O0OOOO0OO0OO0O0O0 }#line:913
                                OOOOO0OOO000O000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O000O0O0OO0OO ,data =OOOOO000OOO0O0O00 ).json ()#line:915
                                if 'status'in OOOOO0OOO000O000O :#line:916
                                    if OOOOO0OOO000O000O ['status']==200 :#line:917
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:918
                            if id !=0 :#line:919
                                for OO0000O0OOO0OOOOO in range (11 ):#line:920
                                    OOO0000OOO00O0OO0 =OO0000O0OOO0OOOOO +1 #line:921
                                    g =OOO0OOO0O00OOO00O [OOO0000OOO00O0OO0 ]['level']#line:922
                                    if id ==g :#line:923
                                        O000OO000O00O0000 =OO0000O0OOO0OOOOO +2 #line:924
                                        if O000OO000O00O0000 !=O0OOOO0OO0OO0O0O0 +1 :#line:925
                                            O0O00OO000000OO00 =O0OOOO0OO0OO0O0O0 +1 #line:926
                                            time .sleep (random .randint (1 ,3 )/10 )#line:928
                                            OO000O00OO00O00OO =f'_site={O0O00OO000000OO00 - 1}&targetSite={O000OO000O00O0000 - 1}_{timi_new()}'#line:929
                                            OOO000O00O0O0OO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OO0OOO00O0OO0 .token ,'timestamp':timi_new (),'sign':sign (OO000O00OO00O00OO ),'signstring':OO000O00OO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:946
                                            O000O0OO000000O00 ={"site":int (O0O00OO000000OO00 -1 ),"targetSite":int (O000OO000O00O0000 -1 )}#line:947
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO000O00O0O0OO00 ,json =O000O0OO000000O00 )#line:948
                                            O00OO0OOO00OOO0OO =True #line:950
                                    if O00OO0OOO00OOO0OO :#line:951
                                        break #line:952
                                if O00OO0OOO00OOO0OO :#line:953
                                    break #line:954
        except :#line:955
            O000OO0OOO00O0OO0 .synthetic ()#line:956
    def level_new (OOO0O00OOOO000OOO ):#line:959
        try :#line:960
            O0OO00O000000OO0O =f'__{timi_new()}'#line:961
            O0O00OOOO0OOOO000 ={'source':'scsc','authorization':OOO0O00OOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000000OO0O ),'signstring':O0OO00O000000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
            O0O0O00OO0OO0OO00 =requests .request ('get',f'{host}/user',headers =O0O00OOOO0OOOO000 ).json ()#line:973
            if 'status'in O0O0O00OO0OO0OO00 :#line:974
                if O0O0O00OO0OO0OO00 ['status']==200 :#line:975
                    return float (O0O0O00OO0OO0OO00 ['data']['level'])#line:976
        except Exception as O000O00OOO00OOOO0 :#line:977
            print (O000O00OOO00OOOO0 )#line:978
    def propsraffle (OO0000OO000000OO0 ):#line:981
        try :#line:982
            while True :#line:983
                OO0O00OO00OO0OO0O =f'__{timi_new()}'#line:984
                OO00O00000OOOO000 ={'source':'scsc','authorization':OO0000OO000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OO00OO0OO0O ),'signstring':OO0O00OO00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:995
                O000O0O0OO0O0O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O00000OOOO000 ).json ()#line:996
                if 'status'in O000O0O0OO0O0O00O :#line:998
                    if O000O0O0OO0O0O00O ['status']==200 :#line:999
                        O00000O00O00O0000 =O000O0O0OO0O0O00O ['data']['rows']#line:1000
                        OOO0OO000OO0OO000 =O000O0O0OO0O0O00O ['data']['vstate']#line:1001
                        if O00000O00O00O0000 ==5 or O00000O00O00O0000 ==6 or O00000O00O00O0000 ==7 :#line:1002
                            OO0OO0OO00O0O00O0 =O000O0O0OO0O0O00O ['data']['silver']#line:1003
                            print (f'【转盘抽奖】:获得种子:{OO0OO0OO00O0O00O0}')#line:1004
                        if O00000O00O00O0000 ==1 or O00000O00O00O0000 ==2 or O00000O00O00O0000 ==3 :#line:1005
                            O0O0O00OO0OOOOO00 =O000O0O0OO0O0O00O ['data']['clover']#line:1006
                            print (f'【转盘抽奖】:获得三叶草:{O0O0O00OO0OOOOO00}')#line:1007
                        if O00000O00O00O0000 ==4 or O00000O00O00O0000 ==8 :#line:1008
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1009
                        if O00000O00O00O0000 =='抽奖次数已用完':#line:1013
                            break #line:1047
                time .sleep (random .randint (8 ,15 )/10 )#line:1048
        except Exception as O0O0OO000000OO0O0 :#line:1049
            print (O0O0OO000000OO0O0 )#line:1050
    def friends_invitation (O00OOOO0O0O00OO00 ):#line:1053
        try :#line:1054
            OO0O0000O0O000OOO =f'__{timi_new()}'#line:1055
            O0O00OOO0O0OOO000 ={'source':'scsc','authorization':O00OOOO0O0O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0O000OOO ),'signstring':OO0O0000O0O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1066
            OOOOOO0OOOO0O0000 =requests .request ('get',f'{host}/friends',headers =O0O00OOO0O0OOO000 ).json ()#line:1067
            if 'status'in OOOOOO0OOOO0O0000 :#line:1068
                if OOOOOO0OOOO0O0000 ['status']==200 :#line:1069
                    O0OOOOOOOO0O000OO =OOOOOO0OOOO0O0000 ['data']['myInviteter']#line:1070
                    if O0OOOOOOOO0O000OO :#line:1071
                        O00O00O00O00OOO0O =O0OOOOOOOO0O000OO ['user']['nickname']#line:1072
                        O000O0OOO0OO000O0 =O00OOOO0O0O00OO00 .certification ()#line:1073
                        if O000O0OOO0OO000O0 =='未实名':#line:1074
                            weishim .append (O00OOOO0O0O00OO00 .token )#line:1075
                        print (f'【查邀请人】:我的邀请人:{O00O00O00O00OOO0O}丨实名:{O000O0OOO0OO000O0}')#line:1076
        except Exception as OO00O0OO00O0000O0 :#line:1080
            print (OO00O0OO00O0000O0 )#line:1081
    def add_clover (O00O00O0000O00O0O ):#line:1084
        global golden_seed #line:1085
        try :#line:1086
            O0OOOOOOO0O000000 =f'__{timi_new()}'#line:1087
            O00OO0O0OO0000000 ={'source':'scsc','authorization':O00O00O0000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0O000000 ),'signstring':O0OOOOOOO0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1098
            OO0O0OO0OO0OOO0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00OO0O0OO0000000 ).json ()#line:1099
            if 'status'in OO0O0OO0OO0OOO0O0 :#line:1101
                if OO0O0OO0OO0OOO0O0 ['status']==200 :#line:1102
                    O000O0OOO00O00O00 =OO0O0OO0OO0OOO0O0 ['data']['clover']#line:1103
                    OO000000O000O0O0O =OO0O0OO0OO0OOO0O0 ['data']['used_clover']#line:1104
                    O0OOO0000O0O00OOO =float (O000O0OOO00O00O00 )-float (OO000000O000O0O0O )#line:1105
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO000000O000O0O0O}')#line:1106
                    if O00O00O0000O00O0O .certification ()!='未实名':#line:1107
                        if O0OOO0000O0O00OOO >1 :#line:1108
                            O0OOOOOOO0O000000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO0000O0O00OOO)}_{timi_new()}'#line:1109
                            O000OO0OO0000000O ={'source':'scsc','authorization':O00O00O0000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0O000000 ),'signstring':O0OOOOOOO0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1120
                            O0O0O0O00O0OO0O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO0000O0O00OOO )}#line:1121
                            O0O0000000OOOOO0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O000OO0OO0000000O ,data =O0O0O0O00O0OO0O0O ).json ()#line:1122
                            if 'status'in O0O0000000OOOOO0O :#line:1124
                                if O0O0000000OOOOO0O ['status']==200 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O0O0000000OOOOO0O["data"]["isSuccess"]}丨数量:{O0OOO0000O0O00OOO}')#line:1126
                                if O0O0000000OOOOO0O ['status']==500 :#line:1127
                                    print (f'【参与抽奖】:添加☘️:{O0O0000000OOOOO0O["message"]}')#line:1128
            OOO000O000OO0OO0O =requests .request ('get',f'{host}/lottery',headers =O00OO0O0OO0000000 ).json ()#line:1129
            OO0OO000OOO0O0OO0 =O00O00O0000O00O0O .winning_rewards ()#line:1131
            if 'status'in OOO000O000OO0OO0O :#line:1132
                if OOO000O000OO0OO0O ['status']==200 :#line:1133
                    OOOOO00O0O0OO0OO0 =OOO000O000OO0OO0O ['data'][0 ]['day_get_gold_quantity']#line:1134
                    golden_seed +=float (OOOOO00O0O0OO0OO0 )#line:1135
                    O0O0O0000OOO00O00 =OOO000O000OO0OO0O ['data'][1 ]['value']#line:1136
                    O0000O0000O0O000O =OOO000O000OO0OO0O ['data'][0 ]['join_number']#line:1137
                    O0O0OOOOO00O0OO00 =int (float (OOO000O000OO0OO0O ['data'][0 ]['totalValue']))#line:1138
                    OO00O0O00O0OO000O =float (O0O0O0000OOO00O00 /O0O0OOOOO00O0OO00 )*10000 #line:1139
                    OO0O0O0O0O00O00O0 =O0O0OOOOO00O0OO00 /O0000O0000O0O000O #line:1140
                    print (f'【参与抽奖】:预计每天中{str(OOOOO00O0O0OO0OO0)[:6]}颗金种子丨好友收益:{str(OO0OO000OOO0O0OO0)[:6]}')#line:1141
                    print (f'【抽奖统计】:每1万☘️中{str(OO00O0O00O0OO000O)[:6]}颗金种子丨☘️人均:{str(OO0O0O0O0O00O00O0)[:7]}️')#line:1142
        except Exception as OO0OOO0O0OOO000OO :#line:1143
            print (OO0OOO0O0OOO000OO )#line:1144
    def energy (O00O0O0OO00OOOO0O ):#line:1147
        try :#line:1148
            while True :#line:1149
                O00OOOOOOOOO0OO00 =f'__{timi_new()}'#line:1150
                O0O0OOOOOOOO00O00 ={'source':'scsc','authorization':O00O0O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOOOO0OO00 ),'signstring':O00OOOOOOOOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1161
                O0OOO00OO0O00000O =requests .request ('get',f'{host}/energy/general',headers =O0O0OOOOOOOO00O00 ).json ()#line:1162
                if 'status'in O0OOO00OO0O00000O :#line:1164
                    if O0OOO00OO0O00000O ['status']==200 :#line:1165
                        O00O0OO00O0O0OOOO =O0OOO00OO0O00000O ['data']['ordinary_water']#line:1166
                        OOOOO0000000OOO0O =O0OOO00OO0O00000O ['data']['ordinary_fertilizer']#line:1167
                        OOOO00O0000OO000O =O0OOO00OO0O00000O ['data']['videoStatus']#line:1168
                        O0O0O0OOO0OOOO000 =O0OOO00OO0O00000O ['data']['waterVideoKey']#line:1169
                        print (f'【我的营养】:肥料:{str(OOOOO0000000OOO0O).split(".")[0]}丨水滴:{str(O00O0OO00O0O0OOOO).split(".")[0]}')#line:1171
                        if float (OOOOO0000000OOO0O )<96 :#line:1172
                            if OOOO00O0000OO000O :#line:1173
                                time .sleep (random .randint (160 ,180 )/10 )#line:1174
                                O000OO00OO0O0O0OO =99 -float (OOOOO0000000OOO0O )#line:1175
                                OO0O0OOO0OO0O00OO ={"fertilizer":str (O000OO00OO0O0O0OO ).split ('.')[0 ]}#line:1176
                                O0O00000000O00OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0OOOOOOOO00O00 ).json ()#line:1178
                                if 'status'in O0O00000000O00OOO :#line:1180
                                    if O0O00000000O00OOO ['status']==200 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00000000O00OOO["message"]}')#line:1182
                                    if O0O00000000O00OOO ['status']==500 :#line:1183
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00000000O00OOO["message"]}')#line:1184
                                        break #line:1185
                                if float (OOOOO0000000OOO0O )<78 :#line:1187
                                    O000OO00OO0O0O0OO =80 -float (OOOOO0000000OOO0O )#line:1188
                                    OOOOOO0OOOO000OOO =f'_fertilizer={int(O000OO00OO0O0O0OO)}_{timi_new()}'#line:1189
                                    O0O0O0O0O000000OO ={'source':'scsc','authorization':O00O0O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOOO000OOO ),'signstring':OOOOOO0OOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1200
                                    OOO00O0000O0O0O00 ={"fertilizer":int (O000OO00OO0O0O0OO )}#line:1201
                                    OO0O0OOOO00O0OOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0O0O0O000000OO ,data =OOO00O0000O0O0O00 ).json ()#line:1203
                                    if 'status'in OO0O0OOOO00O0OOOO :#line:1205
                                        if OO0O0OOOO00O0OOOO ['status']==200 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OO0O0OOOO00O0OOOO["message"]}丨数量:{int(O000OO00OO0O0O0OO)}')#line:1207
                                        if OO0O0OOOO00O0OOOO ['status']==500 :#line:1208
                                            print (f'【购买肥料】:购买肥料:{OO0O0OOOO00O0OOOO["message"]}丨数量:{int(O000OO00OO0O0O0OO)}')#line:1209
                                            O0OOO00OOOOO0O000 =OO0O0OOOO00O0OOOO ["message"].split ('-')[1 ]#line:1210
                                            O0O00OO00OOOOO0O0 =f'__{timi_new()}'#line:1211
                                            OO00OOOOOOOOOO0O0 ={'source':'scsc','authorization':O00O0O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OOOOO0O0 ),'signstring':O0O00OO00OOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1222
                                            O0OO0OOO0O0OOO00O =requests .request ('get',f'{host}/user',headers =OO00OOOOOOOOOO0O0 ).json ()#line:1223
                                            if 'status'in O0OO0OOO0O0OOO00O :#line:1224
                                                if O0OO0OOO0O0OOO00O ['status']==200 :#line:1225
                                                    OOOO0000O0OOOOOOO =O0OO0OOO0O0OOO00O ['data']['inner_id']#line:1226
                                                    if give_gold (OOOO0000O0OOOOOOO ,float (O0OOO00OOOOO0O000 )+1 ):#line:1227
                                                        O00O0O0OO00OOOO0O .energy ()#line:1228
                        if float (O00O0OO00O0O0OOOO )<880 :#line:1229
                            if O0O0O0OOO0OOOO000 :#line:1230
                                time .sleep (random .randint (160 ,180 )/10 )#line:1231
                                O0OOOOOO0O0000O0O =999 -float (O00O0OO00O0O0OOOO )#line:1232
                                OO000O0OOOO00O000 ={"water":str (O0OOOOOO0O0000O0O ).split ('.')[0 ]}#line:1233
                                OO0OOOO000O0O000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0OOOOOOOO00O00 ).json ()#line:1235
                                if 'status'in OO0OOOO000O0O000O :#line:1237
                                    if OO0OOOO000O0O000O ['status']==200 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOO000O0O000O["message"]}')#line:1239
                                    if OO0OOOO000O0O000O ['status']==500 :#line:1240
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOO000O0O000O["message"]}')#line:1241
                                        break #line:1242
                                if float (O00O0OO00O0O0OOOO )<780 :#line:1243
                                    O0OOOOOO0O0000O0O =800 -float (O00O0OO00O0O0OOOO )#line:1244
                                    O00OOO00OOOO0O0O0 =f'_water={int(O0OOOOOO0O0000O0O)}_{timi_new()}'#line:1245
                                    O00O0O0O00OOOO00O ={'source':'scsc','authorization':O00O0O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OOOO0O0O0 ),'signstring':O00OOO00OOOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1256
                                    OOOOO0OOOO0OOOOOO ={"water":int (O0OOOOOO0O0000O0O )}#line:1257
                                    O0OOOO000000O00OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00O0O0O00OOOO00O ,data =OOOOO0OOOO0OOOOOO ).json ()#line:1259
                                    if 'status'in O0OOOO000000O00OO :#line:1261
                                        if O0OOOO000000O00OO ['status']==200 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O0OOOO000000O00OO["message"]}丨数量:{int(O0OOOOOO0O0000O0O)}')#line:1263
                                        if O0OOOO000000O00OO ['status']==500 :#line:1264
                                            print (f'【购买水滴】:购买水滴:{O0OOOO000000O00OO["message"]}丨数量:{int(O0OOOOOO0O0000O0O)}')#line:1265
                                            O0OOO00OOOOO0O000 =O0OOOO000000O00OO ["message"].split ('-')[1 ]#line:1266
                                            O0O00OO00OOOOO0O0 =f'__{timi_new()}'#line:1267
                                            OO00OOOOOOOOOO0O0 ={'source':'scsc','authorization':O00O0O0OO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OOOOO0O0 ),'signstring':O0O00OO00OOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1278
                                            O0OO0OOO0O0OOO00O =requests .request ('get',f'{host}/user',headers =OO00OOOOOOOOOO0O0 ).json ()#line:1279
                                            if 'status'in O0OO0OOO0O0OOO00O :#line:1280
                                                if O0OO0OOO0O0OOO00O ['status']==200 :#line:1281
                                                    OOOO0000O0OOOOOOO =O0OO0OOO0O0OOO00O ['data']['inner_id']#line:1282
                                                    if give_gold (OOOO0000O0OOOOOOO ,float (O0OOO00OOOOO0O000 )+1 ):#line:1283
                                                        O00O0O0OO00OOOO0O .energy ()#line:1284
                        break #line:1285
        except Exception as OOO0O00O0O00OOO00 :#line:1286
            print (OOO0O00O0O00OOO00 )#line:1287
def bundled_def ():#line:1290
    O0O0O0OOOOO0O00O0 =['5570536','7750212','7911652','7911680','7805624']#line:1291
    return O0O0O0OOOOO0O00O0 [random .randint (0 ,len (O0O0O0OOOOO0O00O0 )-1 )]#line:1292
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
        OOO0OO0OOOO00000O =gitee_edition ()#line:1331
        if version_of_the_validation ()<OOO0OO0OOOO00000O ['CityEarth']['edition']:#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO0OOOO00000O["CityEarth"]["edition"]}   ❌')#line:1333
            print (f'更新内容=>>{OOO0OO0OOOO00000O["CityEarth"]["content"]}')#line:1334
        else :#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO0OOOO00000O["CityEarth"]["edition"]}   ✅')#line:1336
            print (f'更新内容=>> {OOO0OO0OOOO00000O["CityEarth"]["content"]}')#line:1337
    except Exception as OO0O00OOO0O000000 :#line:1338
        print (OO0O00OOO0O000000 )#line:1339
def sc3 ():#line:1342
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1343
if __name__ =='__main__':#line:1346
    start ()#line:1347
