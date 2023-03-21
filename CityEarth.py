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
@ 版本  4.9
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.4195543511'#line:1
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
        O0000O00OOOO0OOOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0000O00OOOO0OOOO)}个账号==========")#line:17
        for O00O00O0OO00OO0O0 in O0000O00OOOO0OOOO :#line:18
            OOOOO00000O000O0O =[]#line:19
            print (f"------------正在执行第{O0000O00OOOO0OOOO.index(O00O00O0OO00OO0O0) + 1}个账号------------")#line:20
            OOO0O0OO0OO0O0OO0 =CityEarth (O00O00O0OO00OO0O0 ,OOOOO00000O000O0O ,O0000O00OOOO0OOOO .index (O00O00O0OO00OO0O0 ))#line:21
            def OOO0000OO000OO00O ():#line:23
                if OOO0O0OO0OO0O0OO0 .base_info ():#line:25
                    OOO0O0OO0OO0O0OO0 .sealing ()#line:27
                    OOO0O0OO0OO0O0OO0 .invitenum ()#line:29
                    OOO0O0OO0OO0O0OO0 .query_to_sell ()#line:31
                    OOO0O0OO0OO0O0OO0 .friends_invitation ()#line:35
                    OOO0O0OO0OO0O0OO0 .energy ()#line:37
                    OOO0O0OO0OO0O0OO0 .add_clover ()#line:39
                    OOO0O0OO0OO0O0OO0 .propsraffle ()#line:41
                    OOO0O0OO0OO0O0OO0 .synthetic ()#line:43
                    OOO0O0OO0OO0O0OO0 .crops_illustrated ()#line:45
                    OOO0O0OO0OO0O0OO0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO0O0OO0OO0O0OO0 .give_gold ()#line:50
            OO0OOO0000OO0OO00 =threading .Thread (target =OOO0000OO000OO00O )#line:52
            OO0OOO0000OO0OO00 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O00O00OOOOOOOOOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O00OOOOOOOOOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO0OO0OOOO0O000O0 in invited_new :#line:62
            print (OO0OO0OOOO0O000O0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O000O0O0O0O0OOO00 in weishim :#line:65
            print (O000O0O0O0O0OOO00 )#line:66
    except Exception as OOOO0000000OO00O0 :#line:67
        print (OOOO0000000OO00O0 )#line:68
def give_gold (O0O0O0O000OO000OO ,OOO0O0O0O000O0OO0 ):#line:72
    try :#line:73
        OOOOOO0000OOO000O =f'_doneeNo={O0O0O0O000OO000OO}&quantity={int(OOO0O0O0O000O0OO0)}_{timi_new()}'#line:74
        O0O00O0O0OOOO00OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000OOO000O ),'signstring':OOOOOO0000OOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0O0O0O0000O000O0 ={"quantity":int (OOO0O0O0O000O0OO0 ),"doneeNo":O0O0O0O000OO000OO }#line:89
        O0O0O00O0O00O00OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00O0O0OOOO00OO ,data =O0O0O0O0000O000O0 ).json ()#line:90
        if 'status'in O0O0O00O0O00O00OO :#line:92
            if O0O0O00O0O00O00OO ['status']==200 :#line:93
                if O0O0O00O0O00O00OO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO0O0O0O000O0OO0)}种子给{O0O0O0O000OO000OO}成功')#line:95
                    return True #line:96
            if O0O0O00O0O00O00OO ['status']==401 :#line:97
                print (f'【赠送种子】:{O0O0O00O0O00O00OO["message"]}')#line:98
                return False #line:99
            if O0O0O00O0O00O00OO ['status']==500 :#line:100
                print (f'【赠送种子】:{O0O0O00O0O00O00OO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0O000000O0O0O000 :#line:104
        print (O0O000000O0O0O000 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0OOOO0OO0OOO0OO ):#line:115
    O00OOOOO00O000OOO =hashlib .md5 (OO0OOOO0OO0OOO0OO .encode ()).hexdigest ()#line:116
    OOOO000O0O0O0O0OO =sc1 ()#line:117
    OO0OOO000OO00O0OO =sc2 ()#line:118
    OOO000O0000O0O00O =sc3 ()#line:119
    OOOO00O0000OO0000 =OOOO000O0O0O0O0OO +O00OOOOO00O000OOO +OO0OOO000OO00O0OO +OOO000O0000O0O00O #line:120
    O0OO00OO000O0OO0O =hashlib .md5 (OOOO00O0000OO0000 .encode ()).hexdigest ()#line:121
    return O0OO00OO000O0OO0O #line:122
def format_msg ():#line:125
    O00O0OOO0OOOO0OO0 =""#line:126
    for O000OOOOOO00OOO0O in msg_list :#line:127
        O00O0OOO0OOOO0OO0 +=str (O000OOOOOO00OOO0O )+"\r\n"#line:128
    return O00O0OOO0OOOO0OO0 #line:129
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
def get_json_data (OO00OO000000O0OO0 ,OO0OOO0OOOOO0OOO0 ,O00OO0O00000O00O0 ,O0OOO0OO0OOOO000O ):#line:153
    with open (OO00OO000000O0OO0 ,'rb')as O000OO00OO0OOOOO0 :#line:154
        OO0OOOOO00O000000 =json .load (O000OO00OO0OOOOO0 )#line:155
        OO0OOOOO00O000000 ['data'][OO0OOO0OOOOO0OOO0 ][O00OO0O00000O00O0 ]=O0OOO0OO0OOOO000O #line:156
        O0OOO0OO00000000O =OO0OOOOO00O000000 #line:157
    O000OO00OO0OOOOO0 .close ()#line:158
    return O0OOO0OO00000000O #line:159
def write_json_data (OO00O0OOOO0O00OOO ):#line:162
    with open (json_path1 ,'w')as OO0000000O00OO00O :#line:163
        json .dump (OO00O0OOOO0O00OOO ,OO0000000O00OO00O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    OO0000000O00OO00O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0O0O00OO0OO0O0O0 ,O000O00O0OOO0OOOO ,O0OO0000O00OOO0O0 ,OOOO000O0000000O0 ):#line:171
        try :#line:172
            O0O0O00OO0OO0O0O0 .msg =O0OO0000O00OOO0O0 #line:173
            O0O0O00OO0OO0O0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0O0O00OO0OO0O0O0 .token =O000O00O0OOO0OOOO ['authorization']#line:175
            O0O0O00OO0OO0O0O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0O0O00OO0OO0O0O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0O0O00OO0OO0O0O0 .elephant_user =O000O00O0OOO0OOOO ['elephant_user']#line:178
            O0O0O00OO0OO0O0O0 .elephant_pswd =O000O00O0OOO0OOOO ['elephant_pswd']#line:179
            O0O0O00OO0OO0O0O0 .elephant_Task_ID =O000O00O0OOO0OOOO ['elephant_Task_ID']#line:180
            O0O0O00OO0OO0O0O0 .len_new =OOOO000O0000000O0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O0O0OO000O00O0O ):#line:186
        try :#line:187
            O0O0O0OO000O00O0O .watched_ad ()#line:189
            O00O00O000OO00OOO =f'__{timi_new()}'#line:190
            OO0OO00OO00OO0OO0 ={'source':'scsc','authorization':O0O0O0OO000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000OO00OOO ),'signstring':O00O00O000OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00O00O0000O00OOO =requests .request ('get',f'{host}/user',headers =OO0OO00OO00OO0OO0 ).json ()#line:202
            if 'status'in O00O00O0000O00OOO :#line:204
                if O00O00O0000O00OOO ['status']==200 :#line:205
                    OOO00OO0O0000O000 =O00O00O0000O00OOO ['data']['nickname']#line:206
                    O00OOOOO0000OOOOO =O00O00O0000O00OOO ['data']['inner_id']#line:207
                    O00000O0OOO0OO00O =O00O00O0000O00OOO ['data']['assets']['gold']#line:208
                    OOOO0000O0000O0O0 =O00O00O0000O00OOO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOO00OO0O0000O000[:5]}丨ID:{O00OOOOO0000OOOOO}丨等级:{OOOO0000O0000O0O0}丨金种子:{str(O00000O0OOO0OO00O).split(".")[0]}')#line:211
                    if 'wx_'in OOO00OO0O0000O000 :#line:212
                        O0O0O0OO000O00O0O .change_nickname ()#line:213
                if O00O00O0000O00OOO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O0O0OO000O00O0O .elephant_user =='f':#line:216
                        return False #line:217
                    O0O00OO0000OO000O =Invalid_login .addtask (elephant_user =O0O0O0OO000O00O0O .elephant_user ,elephant_pswd =O0O0O0OO000O00O0O .elephant_pswd ,elephant_Task_ID =O0O0O0OO000O00O0O .elephant_Task_ID )#line:220
                    OO0O000000OO00000 =get_json_data (json_path ,O0O0O0OO000O00O0O .len_new ,'authorization',O0O00OO0000OO000O )#line:221
                    if write_json_data (OO0O000000OO00000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00O00O0000O00OOO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO000O000O0000000 :#line:228
            print (OO000O000O0000000 )#line:229
    def sealing (O0O00O00O00OO00O0 ):#line:232
        try :#line:233
            OOO00O0OO00000000 =f'__{timi_new()}'#line:234
            O0O00O00OO0OOO00O ={'source':'scsc','authorization':O0O00O00O00OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO00000000 ),'signstring':OOO00O0OO00000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O00O00OO0OOO00O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0O00O00OO0OOO00O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O00O00OO0OOO00O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O00O00OO0OOO00O )#line:249
            requests .request ('get',f'{host}/user',headers =O0O00O00OO0OOO00O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O00O00OO0OOO00O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O00O00OO0OOO00O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O00O00OO0OOO00O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0O00O00OO0OOO00O )#line:254
            requests .request ('get',f'{host}/assets',headers =O0O00O00OO0OOO00O )#line:255
        except Exception as O0OO00OOOOOOOO000 :#line:256
            print (O0OO00OOOOOOOO000 )#line:257
    def ddd (O0OOO0O000000O0OO ):#line:259
        try :#line:260
            OOO0O00OO00O0O00O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO0OO0OOO0O0OO00O ={'source':'scsc','authorization':O0OOO0O000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO00O0O00O ),'signstring':OOO0O00OO00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O000OOO00000O00OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO0OO0OOO0O0OO00O ).json ()#line:273
            print (O000OOO00000O00OO )#line:274
        except Exception as O00O0OO0000OO0OOO :#line:277
            print (O00O0OO0000OO0OOO )#line:278
    def the_query (O0O0OO00OO000OOOO ):#line:283
        try :#line:284
            O00O0O0OO00O00OOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0OOO00O00O0OOOO0 ={'authorization':O0O0OO00OO000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO00O00OOO ),'signstring':O00O0O0OO00O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO000O0OOO0000000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOO00O00O0OOOO0 ).json ()#line:296
            if 'status'in OO000O0OOO0000000 :#line:298
                if OO000O0OOO0000000 ['status']==200 :#line:299
                    return OO000O0OOO0000000 ['data']['rows'][4 ]['price']#line:300
        except Exception as O0O000000OOOO0OOO :#line:301
            print (O0O000000OOOO0OOO )#line:302
    def market_sale (O00000O0O0O000000 ,O00000O0OOOO00OO0 ):#line:305
        try :#line:306
            O0OOOO000000OO0OO =timi_new ()#line:307
            OO000OOOOO0OO0OO0 =f'type=crop__{O0OOOO000000OO0OO}'#line:308
            OOOO0OO0O00O00OOO ={'source':'scsc','authorization':O00000O0O0O000000 .token ,'timestamp':str (O0OOOO000000OO0OO ),'sign':sign (OO000OOOOO0OO0OO0 ),'signstring':OO000OOOOO0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O00OOO00O00OOO000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOO0OO0O00O00OOO ).json ()#line:320
            if 'status'in O00OOO00O00OOO000 :#line:322
                if O00OOO00O00OOO000 ['status']==200 :#line:323
                    if O00OOO00O00OOO000 ['data']['rows']:#line:324
                        O0OO000OOOOOOOOO0 =O00OOO00O00OOO000 ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOO0O0OO00000OOOO =O00OOO00O00OOO000 ['data']['rows'][0 ]['quantity']#line:326
                        if float (O00000O0OOOO00OO0 )>7 :#line:327
                            O00O0OOOOO00O00OO =f'_packsackItemId={O0OO000OOOOOOOOO0}&price={str(O00000O0OOOO00OO0)[:5]}&quantity={OOO0O0OO00000OOOO}_{O0OOOO000000OO0OO}'#line:328
                            OO0000OO0000OOOOO ={'source':'scsc','authorization':O00000O0O0O000000 .token ,'timestamp':str (O0OOOO000000OO0OO ),'sign':sign (O00O0OOOOO00O00OO ),'signstring':O00O0OOOOO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOO00OOO0OO0OOOOO ={"packsackItemId":O0OO000OOOOOOOOO0 ,"price":str (O00000O0OOOO00OO0 )[:5 ],"quantity":str (OOO0O0OO00000OOOO )}#line:344
                            O000OOO0O00OO0O00 =requests .request ('post',f'{host}/market/sale',headers =OO0000OO0000OOOOO ,data =OOO00OOO0OO0OOOOO ).json ()#line:345
                            if 'status'in O000OOO0O00OO0O00 :#line:347
                                if O000OOO0O00OO0O00 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OOO0O0OO00000OOOO}丨价格:{str(O00000O0OOOO00OO0)[:5]}')#line:349
                                if O000OOO0O00OO0O00 ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O000OOO0O00OO0O00["message"]}')#line:351
        except Exception as OOO0OO0O000000O0O :#line:352
            print (OOO0OO0O000000O0O )#line:353
    def query_to_sell (O0OOO0000OOOOOO00 ):#line:356
        global count_list #line:357
        try :#line:358
            OOOO000OOOO00000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            O0OO00OOOOOO0O00O ={'source':'scsc','authorization':O0OOO0000OOOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOOO00000O ),'signstring':OOOO000OOOO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O0O0OO0OOO00OO0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00OOOOOO0O00O ).json ()#line:371
            if 'status'in O0O0OO0OOO00OO0O0 :#line:373
                if O0O0OO0OOO00OO0O0 ['status']==200 :#line:374
                    for O000O0OO0OO00000O in O0O0OO0OOO00OO0O0 ['data']['rows']:#line:375
                        OO00OO0O0000OOOO0 =O000O0OO0OO00000O ['materialKey']#line:376
                        O000OO00O00OO0O00 =O000O0OO0OO00000O ['quantity']#line:377
                        OOO0O00OOOOO0O0OO =O000O0OO0OO00000O ['price']#line:378
                        OO0OO00OOOOOO000O =O000O0OO0OO00000O ['saleState']#line:379
                        if OO0OO00OOOOOO000O ==0 :#line:380
                            print (f'【出售订单】:名称:{OO00OO0O0000OOOO0}丨数量:{O000OO00O00OO0O00}丨价格:{OOO0O00OOOOO0O0OO}')#line:381
                            count_list +=O000OO00O00OO0O00 #line:382
                            OO000OO0000O000O0 =O0OOO0000OOOOOO00 .the_query ()#line:384
                            if float (OO000OO0000O000O0 )!=float (OOO0O00OOOOO0O0OO ):#line:385
                                OO0000O0O00OO00OO =O000O0OO0OO00000O ['id']#line:386
                                O0OOO0000OOOOOO00 .cacel_sale (OO0000O0O00OO00OO )#line:387
                    O0OOO0000OOOOOO00 .game_map ()#line:389
        except Exception as OOO00OO0OOO00OO0O :#line:391
            print (OOO00OO0OOO00OO0O )#line:392
    def cacel_sale (OO0OOOOO0000OO0O0 ,OO0O0000O000O0000 ):#line:395
        try :#line:396
            OO000O00O0OOO0000 =f'_saleId={OO0O0000O000O0000}_{timi_new()}'#line:397
            OO0OO00O0OO00OOO0 ={'source':'scsc','authorization':OO0OOOOO0000OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0OOO0000 ),'signstring':OO000O00O0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O0OOO0O000000OO00 ={"saleId":OO0O0000O000O0000 }#line:409
            O0OOOOO0OO0O00000 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO00O0OO00OOO0 ,data =O0OOO0O000000OO00 ).json ()#line:410
            if 'status'in O0OOOOO0OO0O00000 :#line:412
                if O0OOOOO0OO0O00000 ['status']==200 :#line:413
                    print (f'【下架出售】:{O0OOOOO0OO0O00000["data"]}')#line:414
        except Exception as O00000O0O0O000OO0 :#line:415
            print (O00000O0O0O000OO0 )#line:416
    def change_nickname (OO0000OO0O00OOOOO ):#line:419
        try :#line:420
            O0OO00OO000O00OOO =timi_new ()#line:421
            OOO0OOO0O0O00OO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O0000O000OOO0OOOO =requests .request ('post','https://www.qmsjmfb.com/',data =OOO0OOO0O0O00OO00 ).text #line:423
            OOO00O0000O0OO0OO =re .findall ('<ul><li>(.*?)</li>',O0000O000OOO0OOOO )[0 ][:3 ]#line:424
            OOO00OOOO0O0O000O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO00O0000O0OO0OO}').json ()#line:425
            O000OOOOOOOO0O00O =OOO00OOOO0O0O000O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            OO0O00O0OO0O00O0O ={"nickname":O000OOOOOOOO0O00O }#line:427
            OOO0OOOO00OOO0OO0 =f'_nickname={O000OOOOOOOO0O00O}_{O0OO00OO000O00OOO}'#line:428
            O00OO00O00O00OO00 ={'source':'scsc','authorization':OO0000OO0O00OOOOO .token ,'timestamp':O0OO00OO000O00OOO ,'sign':sign (OOO0OOOO00OOO0OO0 ),'signstring':OOO0OOOO00OOO0OO0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO00OO0O000O0O000 =requests .request ('patch',f'{host}/user/nickname',headers =O00OO00O00O00OO00 ,data =OO0O00O0OO0O00O0O ).json ()#line:440
            if 'status'in OO00OO0O000O0O000 :#line:442
                if OO00OO0O000O0O000 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O000OOOOOOOO0O00O}丨{OO00OO0O000O0O000["message"]}')#line:444
        except Exception as O00OOO00OOO0O00O0 :#line:445
            print (O00OOO00OOO0O00O0 )#line:446
    def withdraw (OO0OO0OOO00O00O0O ):#line:449
        try :#line:450
            OO0O0O0000O0O0OOO =f'__{timi_new()}'#line:451
            O00OOO000OOOO000O ={'source':'scsc','authorization':OO0OO0OOO00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0000O0O0OOO ),'signstring':OO0O0O0000O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            O0O0OOOO0OO00O0O0 =requests .request ('get',f'{host}/assets',headers =O00OOO000OOOO000O ).json ()#line:463
            if 'status'in O0O0OOOO0OO00O0O0 :#line:465
                if O0O0OOOO0OO00O0O0 ['status']==200 :#line:466
                    OO0OO0OOOO0O00O0O =O0O0OOOO0OO00O0O0 ['data']['cash']#line:467
                    if float (OO0OO0OOOO0O00O0O )>20 :#line:468
                        OO0O0O0000O0O0OOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O00OOO000OOOO000O ={'authorization':OO0OO0OOO00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0000O0O0OOO ),'signstring':OO0O0O0000O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        OO0O0O0O0OO00OOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OOO0O00OO0OOO00OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OOO000OOOO000O ,data =OO0O0O0O0OO00OOOO ).json ()#line:482
                        if 'status'in OOO0O00OO0OOO00OO :#line:484
                            if OOO0O00OO0OOO00OO ['status']==200 :#line:485
                                print (f'【余额提现】:{OOO0O00OO0OOO00OO["data"]}')#line:486
                        if 'status'in OOO0O00OO0OOO00OO :#line:487
                            if OOO0O00OO0OOO00OO ['status']==500 :#line:488
                                print (f'【余额提现】:{OOO0O00OO0OOO00OO["message"]}')#line:489
        except Exception as O0O00OO0OO0O00000 :#line:490
            print (O0O00OO0OO0O00000 )#line:491
    def invitenum (O0O00O00O0OO00000 ):#line:494
        global invited_new #line:495
        try :#line:496
            O0OO00OO00O0000O0 =f'__{timi_new()}'#line:497
            OO0O0OO0O00O0O000 ={'source':'scsc','authorization':O0O00O00O0OO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00O0000O0 ),'signstring':O0OO00OO00O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            O00OO00O0OO0O00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0O0OO0O00O0O000 ).json ()#line:509
            if 'status'in O00OO00O0OO0O00O0 :#line:511
                if O00OO00O0OO0O00O0 ['status']==200 :#line:512
                    O0OOOOO0OO000000O =O00OO00O0OO0O00O0 ['data']['invited_count']#line:513
                    OOOOO000O0O0OO0O0 =O00OO00O0OO0O00O0 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{O0OOOOO0OO000000O}丨间邀好友:{OOOOO000O0O0OO0O0}')#line:515
                    if O0OOOOO0OO000000O <2 :#line:516
                        O0O00OOOO0OO0OO0O =f'__{timi_new()}'#line:517
                        OO00O0000000OO000 ={'source':'scsc','authorization':O0O00O00O0OO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO0OO0OO0O ),'signstring':O0O00OOOO0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OOO00000000OO0O0O =requests .request ('get',f'{host}/user',headers =OO00O0000000OO000 ).json ()#line:529
                        if 'status'in OOO00000000OO0O0O :#line:531
                            if OOO00000000OO0O0O ['status']==200 :#line:532
                                invited_new .append (OOO00000000OO0O0O ['data']['inner_id'])#line:533
        except Exception as O0O00OO00O00OOO0O :#line:534
            print (O0O00OO00O00OOO0O )#line:535
    def game_map (OO00OOOOO00OO0000 ):#line:538
        try :#line:539
            OOO0O0OOOOO000O0O =f'__{timi_new()}'#line:540
            OOO00O0OOO0OOOOOO ={'source':'scsc','authorization':OO00OOOOO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOOOO000O0O ),'signstring':OOO0O0OOOOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OO000OO00OOO0O0O0 =requests .request ('get',f'{host}/game/map',headers =OOO00O0OOO0OOOOOO ).json ()#line:552
            if 'status'in OO000OO00OOO0O0O0 :#line:554
                if OO000OO00OOO0O0O0 ['status']==200 :#line:555
                    for O0O0OO00OO0O000OO in OO000OO00OOO0O0O0 ['data']['list'][0 ]['crops']:#line:556
                        O0O0000OO00O0OOO0 =O0O0OO00OO0O000OO ['level']#line:558
                        if O0O0000OO00O0OOO0 ==41 :#line:559
                            OO0O000OOOO0000O0 =O0O0OO00OO0O000OO ['crop_name']#line:560
                            O00OOO00000OOOO00 =O0O0OO00OO0O000OO ['count']#line:561
                            if O00OOO00000OOOO00 >0 :#line:562
                                print (f'【农业资产】:{OO0O000OOOO0000O0}丨数量:{O00OOO00000OOOO00}')#line:563
                                O0000O0000O000000 =OO00OOOOO00OO0000 .the_query ()#line:564
                                OO00OOOOO00OO0000 .market_sale (O0000O0000O000000 )#line:565
        except Exception as O0OOOO0OOO0O00OO0 :#line:566
            print (O0OOOO0OOO0O00OO0 )#line:567
    def give_gold (O00O0OOOO0O0OO000 ):#line:570
        try :#line:571
            O000OO0000OO0OOOO =f'__{timi_new()}'#line:572
            OOOO0000O0O0O00OO ={'source':'scsc','authorization':O00O0OOOO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0000OO0OOOO ),'signstring':O000OO0000OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OO0O00OOOOOO0OOO0 =requests .request ('get',f'{host}/user',headers =OOOO0000O0O0O00OO ).json ()#line:584
            if 'status'in OO0O00OOOOOO0OOO0 :#line:585
                if OO0O00OOOOOO0OOO0 ['status']==200 :#line:586
                    if float (O00O0OOOO0O0OO000 .doneeNo )!=0 :#line:587
                        OOO000OOOO0OOOO0O =OO0O00OOOOOO0OOO0 ['data']['assets']['gold']#line:588
                        if float (OOO000OOOO0OOOO0O )>float (O00O0OOOO0O0OO000 .innerId ):#line:589
                            OO000O000OOOOOO0O =int (float (OOO000OOOO0OOOO0O )/1.1 )#line:590
                            O000OO0000OO0OOOO =f'_doneeNo={O00O0OOOO0O0OO000.doneeNo}&quantity={OO000O000OOOOOO0O}_{timi_new()}'#line:591
                            OOOO0000O0O0O00OO ={'source':'scsc','authorization':O00O0OOOO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO0000OO0OOOO ),'signstring':O000OO0000OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O0O0OO0OOOOO00O0O ={"quantity":OO000O000OOOOOO0O ,"doneeNo":O00O0OOOO0O0OO000 .doneeNo }#line:606
                            O00O0O0000OOOOO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0000O0O0O00OO ,data =O0O0OO0OOOOO00O0O ).json ()#line:607
                            if 'status'in O00O0O0000OOOOO00 :#line:609
                                if O00O0O0000OOOOO00 ['status']==200 :#line:610
                                    if O00O0O0000OOOOO00 ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OO000O000OOOOOO0O}种子给{O00O0OOOO0O0OO000.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O0OOOO000O0O0000O :#line:615
            print (O0OOOO000O0O0000O )#line:616
    def invitation (OOOOOO0000O0OOOO0 ):#line:618
        try :#line:619
            _OO00OO00OO0000OO0 =float (bundled_def ())/4 #line:620
            O0OO0OO0O00O0O0OO =f'_innerId={int(_OO00OO00OO0000OO0)}_{timi_new()}'#line:622
            O0OOO00OO0O00OOOO ={'source':'scsc','authorization':OOOOOO0000O0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O00O0O0OO ),'signstring':O0OO0OO0O00O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            O0000OO0OOO00O000 ={"innerId":int (_OO00OO00OO0000OO0 )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOO00OO0O00OOOO ,data =O0000OO0OOO00O000 )#line:635
        except Exception as OOO0O0OO0OOOO00OO :#line:636
            print (OOO0O0OO0OOOO00OO )#line:637
    def winning_rewards (OOO0OOOO0O0000OOO ):#line:640
        try :#line:641
            OOO0OO0O0O0000O0O =f'__{timi_new()}'#line:642
            OO00OOO0O00OOOOOO ={'source':'scsc','authorization':OOO0OOOO0O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0O0000O0O ),'signstring':OOO0OO0O0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OO0OO00OOOO0OOOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00OOO0O00OOOOOO ).json ()#line:654
            if 'status'in OO0OO00OOOO0OOOO0 :#line:656
                if OO0OO00OOOO0OOOO0 ['status']==200 :#line:657
                    if OO0OO00OOOO0OOOO0 ['data']['amount']:#line:658
                        OOO000OO0OO00O000 =OO0OO00OOOO0OOOO0 ['data']['amount']['gold']#line:659
                        return OOO000OO0OO00O000 #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as OOOO00O00O00OOO0O :#line:663
            print (OOOO00O00O00OOO0O )#line:664
    def certification (OO0OO0O00O0O0OO0O ):#line:667
        try :#line:668
            O0OOOO0OOOOO0OOO0 =f'__{timi_new()}'#line:669
            O00O0O0OO0OOO0OO0 ={'source':'scsc','authorization':OO0OO0O00O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOOOO0OOO0 ),'signstring':O0OOOO0OOOOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            O0OO00O0O00OOO00O =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O0O0OO0OOO0OO0 ).json ()#line:681
            if 'status'in O0OO00O0O00OOO00O :#line:683
                if O0OO00O0O00OOO00O ['status']==200 :#line:684
                    if O0OO00O0O00OOO00O ['data']['result']:#line:685
                        O0O00OOOOO0O000O0 =O0OO00O0O00OOO00O ['data']['nick_name']#line:686
                        return O0O00OOOOO0O000O0 #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as OO000OOOO0O000O00 :#line:690
            print (OO000OOOO0O000O00 )#line:691
    def crops_illustrated (O00O00OO00O0O000O ):#line:694
        try :#line:695
            OO0O0OO0OO00OOOO0 =f'__{timi_new()}'#line:696
            OOO0OO0O00O0OOOO0 ={'source':'scsc','authorization':O00O00OO00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OO00OOOO0 ),'signstring':OO0O0OO0OO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            O0O0OO00O00O000OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0OO0O00O0OOOO0 ).json ()#line:708
            if 'status'in O0O0OO00O00O000OO :#line:710
                if O0O0OO00O00O000OO ['status']==200 :#line:711
                    OO0000O00O000O000 =O0O0OO00O00O000OO ['data'][0 ]['crops']#line:712
                    for O0O000OOOOOOOO0O0 in OO0000O00O000O000 :#line:713
                        if O0O000OOOOOOOO0O0 ['ill_clover_award']:#line:714
                            if float (O0O000OOOOOOOO0O0 ['ill_clover_award'])>1 :#line:715
                                if O0O000OOOOOOOO0O0 ['is_finish']:#line:716
                                    if not O0O000OOOOOOOO0O0 ['is_getit']:#line:717
                                        if O00O00OO00O0O000O .certification ()!='未实名':#line:718
                                            OO0O0OO0OO00OOOO0 =f'_award_level={O0O000OOOOOOOO0O0["level"]}_{timi_new()}'#line:719
                                            OOO0OO0O00O0OOOO0 ={'source':'scsc','authorization':O00O00OO00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OO00OOOO0 ),'signstring':OO0O0OO0OO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            O0O00OOO00000O0OO ={"award_level":O0O000OOOOOOOO0O0 ['level']}#line:731
                                            OO00000000O0OO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0OO0O00O0OOOO0 ,json =O0O00OOO00000O0OO ).json ()#line:733
                                            if 'status'in OO00000000O0OO0O0 :#line:734
                                                if OO00000000O0OO0O0 ['status']==200 :#line:735
                                                    OO000OOOOOO000000 =OO00000000O0OO0O0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O0O000OOOOOOOO0O0["crop_name"]}成就丨奖励{OO000OOOOOO000000}☘️')#line:738
                                                if OO00000000O0OO0O0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OO00000000O0OO0O0["message"]}')#line:740
        except Exception as OO00O000OOO00O0O0 :#line:741
            print (OO00O000OOO00O0O0 )#line:742
    def watched_ad (OO00000000O000OOO ):#line:745
        try :#line:746
            OOO000OOOO000OO0O =f'__{timi_new()}'#line:747
            OO0O00O0O0O00O00O ={'source':'scsc','authorization':OO00000000O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOO000OO0O ),'signstring':OOO000OOOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OOO00000OO0OO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O0O0O00O00O ).json ()#line:759
            if 'status'in OOO00000OO0OO0O00 :#line:761
                if OOO00000OO0OO0O00 ['status']==200 :#line:762
                    if 'offlineInfo'in OOO00000OO0OO0O00 ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        OO0O0O0OOOO0OOO00 =OOO00000OO0OO0O00 ['data']['offlineInfo']['off_minute']#line:765
                        OO0OOOO0O0000OO00 =float (OOO00000OO0OO0O00 ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O00O0O0O00O00O ).json ()#line:768
                        time .sleep (2 )#line:769
                        OO0OO0O00000O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00O0O0O00O00O ).json ()#line:770
                        if 'status'in OO0OO0O00000O0OOO :#line:772
                            if OO0OO0O00000O0OOO ['status']==200 :#line:773
                                O0OO00OO0OOO0O00O =float (OO0OO0O00000O0OOO ['data']['silver'])/1000000000000 #line:774
                                O000OO0O0OO00OOO0 =str (O0OO00OO0OOO0O00O -OO0OOOO0O0000OO00 )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{OO0O0O0OOOO0OOO00}分钟奖励🌱数量:{O000OO0O0OO00OOO0}t粒')#line:776
        except Exception as OO0O0OOOOOOO0000O :#line:777
            print (OO0O0OOOOOOO0000O )#line:778
    def user_ad (OOO0OO0O0O0O0O0OO ):#line:781
        try :#line:782
            OO0OOO0O0O000O0O0 =f'__{timi_new()}'#line:783
            O0OO000000O0000O0 ={'source':'scsc','authorization':OOO0OO0O0O0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0O000O0O0 ),'signstring':OO0OOO0O0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            O00OO000OOOOOO00O =requests .request ('get',f'{host}/user/ad',headers =O0OO000000O0000O0 ).json ()#line:795
            if 'status'in O00OO000OOOOOO00O :#line:797
                if O00OO000OOOOOO00O ['status']==200 :#line:798
                    OOOOO00000O0O00O0 =O00OO000OOOOOO00O ['data']['max_time']#line:799
                    O0OOO0O0OO0OOO00O =O00OO000OOOOOO00O ['data']['watch_time']#line:800
                    O0O00O00O00OO0OO0 =O00OO000OOOOOO00O ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{O0O00O00O00OO0OO0 + OOOOO00000O0O00O0 - O0OOO0O0OO0OOO00O}次丨好友提供:{O0O00O00O00OO0OO0}次')#line:802
                    if O0O00O00O00OO0OO0 +OOOOO00000O0O00O0 -O0OOO0O0OO0OOO00O >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OOOO000O0OO000O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OO000000O0000O0 ).json ()#line:805
                        if 'status'in OOOO000O0OO000O00 :#line:807
                            if OOOO000O0OO000O00 ['status']==200 :#line:808
                                O000O0O00OOOO0OOO =float (OOOO000O0OO000O00 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(O000O0O00OOOO0OOO)}t粒')#line:810
                                return True #line:811
                            if OOOO000O0OO000O00 ['status']==500 :#line:812
                                OO00OO0OOO00OOO0O =OOOO000O0OO000O00 ['message']#line:813
                                print (f'【获取种子】:{OO00OO0OOO00OOO0O}')#line:814
                                return False #line:815
        except Exception as O0000O00OO0O0O000 :#line:816
            print (O0000O00OO0O0O000 )#line:817
    def synthetic (OOO0O0OO0O000OOOO ):#line:820
        global id ,g #line:821
        try :#line:822
            O0O0O000O00OO0000 =OOO0O0OO0O000OOOO .level_new ()#line:823
            O00000O000O00OO0O =random .randint (9 ,11 )#line:824
            OO0O00OO0OO00OO0O =f'_site=8&targetSite={O00000O000O00OO0O}_{timi_new()}'#line:825
            OO000OOOOOO0O00OO ={'source':'scsc','authorization':OOO0O0OO0O000OOOO .token ,'timestamp':timi_new (),'sign':sign (OO0O00OO0OO00OO0O ),'signstring':OO0O00OO0OO00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            O0O0O0O00OOO000O0 ={"site":int (8 ),"targetSite":int (O00000O000O00OO0O )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO000OOOOOO0O00OO ,json =O0O0O0O00OOO000O0 )#line:838
            while True :#line:839
                O00OOO0000O00000O =f'__{timi_new()}'#line:840
                O0O00O0O00O00O0O0 ={'source':'scsc','authorization':OOO0O0OO0O000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000O00000O ),'signstring':O00OOO0000O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                O0000000O0O0000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0O00O00O0O0 ).json ()#line:852
                if 'status'in O0000000O0O0000O0 :#line:854
                    if O0000000O0O0000O0 ['status']==200 :#line:855
                        OO0OOO00OOO00O0OO =O0000000O0O0000O0 ['data']['cropList']#line:856
                        O00O000OO00OOOO00 =O0000000O0O0000O0 ['data']['gameCoreDataDBid']#line:857
                        O000OO0OOOO00OOO0 =float (O0000000O0O0000O0 ['data']['silver'])/1000000000000 #line:858
                        O00OOOOOOOOOO000O =0 #line:863
                        for O0000O0OO0O00O000 in OO0OOO00OOO00O0OO :#line:864
                            if not O0000O0OO0O00O000 :#line:865
                                OO0OO00O0OOO0OO00 =f'_crop_id={O00O000OO00OOOO00}&site={O00OOOOOOOOOO000O}_{OOO0O0OO0O000OOOO.time}'#line:866
                                OO0OO0OOO00OOO00O ={'source':'scsc','authorization':OOO0O0OO0O000OOOO .token ,'timestamp':OOO0O0OO0O000OOOO .time ,'sign':sign (OO0OO00O0OOO0OO00 ),'signstring':OO0OO00O0OOO0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                O00OO00O0OO0O0OOO ={"site":O00OOOOOOOOOO000O ,"crop_id":O00O000OO00OOOO00 }#line:877
                                OO000OO000OO0O00O =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OO0OOO00OOO00O ,data =O00OO00O0OO0O0OOO ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OO000OO000OO0O00O :#line:881
                                    if OO000OO000OO0O00O ['status']==200 :#line:882
                                        if OO000OO000OO0O00O ['message']=='种子数量不足':#line:883
                                            O0O0O000O00OO0000 =OOO0O0OO0O000OOOO .level_new ()#line:884
                                            print (f'【种植合成】:{OO000OO000OO0O00O["message"]}')#line:885
                                            if not OOO0O0OO0O000OOOO .user_ad ():#line:886
                                                return False #line:887
                                    if OO000OO000OO0O00O ['status']==500 :#line:888
                                        print (f'【种植合成】:{OO000OO000OO0O00O["message"]}')#line:889
                                        return False #line:890
                            O00OOOOOOOOOO000O +=1 #line:891
                        OO0OOOOO0OO0OO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0O00O00O0O0 ).json ()#line:892
                        O00OO00O00O0OOO0O =OO0OOOOO0OO0OO000 ['data']['cropList']#line:893
                        O0O0O00OOO000000O =False #line:894
                        for O0000O0OO0O00O000 in range (12 ):#line:895
                            id =O00OO00O00O0OOO0O [O0000O0OO0O00O000 ]['level']#line:896
                            if float (O0O0O000O00OO0000 )-float (id )>9 :#line:897
                                OO0O0O0O0OO000OOO =f'_site={O0000O0OO0O00O000}_{timi_new()}'#line:898
                                OOO0O0000OOOO0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O0OO0O000OOOO .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0O0OO000OOO ),'signstring':OO0O0O0O0OO000OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O00OO000OOOOO0O0O ={"site":O0000O0OO0O00O000 }#line:910
                                OOO00O000000O00O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0O0000OOOO0O00 ,data =O00OO000OOOOO0O0O ).json ()#line:912
                                if 'status'in OOO00O000000O00O0 :#line:913
                                    if OOO00O000000O00O0 ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for OO0OOO0O00000000O in range (11 ):#line:917
                                    O0000000OO00OOOO0 =OO0OOO0O00000000O +1 #line:918
                                    g =O00OO00O00O0OOO0O [O0000000OO00OOOO0 ]['level']#line:919
                                    if id ==g :#line:920
                                        OO000O00000OOOO00 =OO0OOO0O00000000O +2 #line:921
                                        if OO000O00000OOOO00 !=O0000O0OO0O00O000 +1 :#line:922
                                            OO000O000O000000O =O0000O0OO0O00O000 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            OO0O00OO0OO00OO0O =f'_site={OO000O000O000000O - 1}&targetSite={OO000O00000OOOO00 - 1}_{timi_new()}'#line:926
                                            OO000OOOOOO0O00OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O0OO0O000OOOO .token ,'timestamp':timi_new (),'sign':sign (OO0O00OO0OO00OO0O ),'signstring':OO0O00OO0OO00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            OOOO0O00O00O0OOOO ={"site":int (OO000O000O000000O -1 ),"targetSite":int (OO000O00000OOOO00 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO000OOOOOO0O00OO ,json =OOOO0O00O00O0OOOO )#line:945
                                            O0O0O00OOO000000O =True #line:947
                                    if O0O0O00OOO000000O :#line:948
                                        break #line:949
                                if O0O0O00OOO000000O :#line:950
                                    break #line:951
        except :#line:952
            OOO0O0OO0O000OOOO .synthetic ()#line:953
    def level_new (O0OO0OOO000O0OO00 ):#line:956
        try :#line:957
            OOO0O0O0OOO0OO000 =f'__{timi_new()}'#line:958
            OOOO00OO000OO0O00 ={'source':'scsc','authorization':O0OO0OOO000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOO0OO000 ),'signstring':OOO0O0O0OOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            OOO0O00O00OO0O00O =requests .request ('get',f'{host}/user',headers =OOOO00OO000OO0O00 ).json ()#line:970
            if 'status'in OOO0O00O00OO0O00O :#line:971
                if OOO0O00O00OO0O00O ['status']==200 :#line:972
                    return float (OOO0O00O00OO0O00O ['data']['level'])#line:973
        except Exception as OOO00O00OOO0000O0 :#line:974
            print (OOO00O00OOO0000O0 )#line:975
    def propsraffle (OO0000OOO0O00O0O0 ):#line:978
        try :#line:979
            while True :#line:980
                O0OOOO00OOO00O000 =f'__{timi_new()}'#line:981
                O0000OOOOOO000O0O ={'source':'scsc','authorization':OO0000OOO0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO00OOO00O000 ),'signstring':O0OOOO00OOO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OOOOO0000OOO0O0O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000OOOOOO000O0O ).json ()#line:993
                if 'status'in OOOOO0000OOO0O0O0 :#line:995
                    if OOOOO0000OOO0O0O0 ['status']==200 :#line:996
                        OOO0OO0O00O0O0OO0 =OOOOO0000OOO0O0O0 ['data']['rows']#line:997
                        OOOOOOOO00O0OO0OO =OOOOO0000OOO0O0O0 ['data']['vstate']#line:998
                        if OOO0OO0O00O0O0OO0 ==5 or OOO0OO0O00O0O0OO0 ==6 or OOO0OO0O00O0O0OO0 ==7 :#line:999
                            O00OOO0O0O00OOOOO =OOOOO0000OOO0O0O0 ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{O00OOO0O0O00OOOOO}')#line:1001
                        if OOO0OO0O00O0O0OO0 ==1 or OOO0OO0O00O0O0OO0 ==2 or OOO0OO0O00O0O0OO0 ==3 :#line:1002
                            O00OO0OOOOOO00O0O =OOOOO0000OOO0O0O0 ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{O00OO0OOOOOO00O0O}')#line:1004
                        if OOO0OO0O00O0O0OO0 ==4 or OOO0OO0O00O0O0OO0 ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OOO0OO0O00O0O0OO0 =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OO00O0O00000O0 :#line:1046
            print (OO0OO00O0O00000O0 )#line:1047
    def friends_invitation (O0O00O00OO0OO0OO0 ):#line:1050
        try :#line:1051
            O00OO0O0O0OOO0O00 =f'__{timi_new()}'#line:1052
            OOO00OOO0OO00OOO0 ={'source':'scsc','authorization':O0O00O00OO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0OOO0O00 ),'signstring':O00OO0O0O0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            OO0OO0OOO0O0OOOO0 =requests .request ('get',f'{host}/friends',headers =OOO00OOO0OO00OOO0 ).json ()#line:1064
            if 'status'in OO0OO0OOO0O0OOOO0 :#line:1065
                if OO0OO0OOO0O0OOOO0 ['status']==200 :#line:1066
                    O0OO0OOOOO00O000O =OO0OO0OOO0O0OOOO0 ['data']['myInviteter']#line:1067
                    if O0OO0OOOOO00O000O :#line:1068
                        OOOO00O0O0O0OO00O =O0OO0OOOOO00O000O ['user']['nickname']#line:1069
                        O0OOOO00O00O0O0O0 =O0O00O00OO0OO0OO0 .certification ()#line:1070
                        if O0OOOO00O00O0O0O0 =='未实名':#line:1071
                            weishim .append (O0O00O00OO0OO0OO0 .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{OOOO00O0O0O0OO00O}丨实名:{O0OOOO00O00O0O0O0}')#line:1073
        except Exception as O00OOOO0000OOOOO0 :#line:1077
            print (O00OOOO0000OOOOO0 )#line:1078
    def add_clover (O00O0000OOO0000OO ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            O000O0OO00O000OO0 =f'__{timi_new()}'#line:1084
            OOO0O00OO00OOOOOO ={'source':'scsc','authorization':O00O0000OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO00O000OO0 ),'signstring':O000O0OO00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO00OOOOO00OO000O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0O00OO00OOOOOO ).json ()#line:1096
            if 'status'in OO00OOOOO00OO000O :#line:1098
                if OO00OOOOO00OO000O ['status']==200 :#line:1099
                    OO0O0O0O000OOO000 =OO00OOOOO00OO000O ['data']['clover']#line:1100
                    O0O00OOO0OOOO0OO0 =OO00OOOOO00OO000O ['data']['used_clover']#line:1101
                    O000OOO00OO000O0O =float (OO0O0O0O000OOO000 )-float (O0O00OOO0OOOO0OO0 )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O00OOO0OOOO0OO0}')#line:1103
                    if O00O0000OOO0000OO .certification ()!='未实名':#line:1104
                        if O000OOO00OO000O0O >1 :#line:1105
                            O000O0OO00O000OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000OOO00OO000O0O)}_{timi_new()}'#line:1106
                            O0O00O0OOO000O00O ={'source':'scsc','authorization':O00O0000OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO00O000OO0 ),'signstring':O000O0OO00O000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OOO0OO0OOOO0OOOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000OOO00OO000O0O )}#line:1118
                            O000000OOO00O0O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O00O0OOO000O00O ,data =OOO0OO0OOOO0OOOO0 ).json ()#line:1119
                            if 'status'in O000000OOO00O0O0O :#line:1121
                                if O000000OOO00O0O0O ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O000000OOO00O0O0O["data"]["isSuccess"]}丨数量:{O000OOO00OO000O0O}')#line:1123
                                if O000000OOO00O0O0O ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O000000OOO00O0O0O["message"]}')#line:1125
            OOO00O00O0O000000 =requests .request ('get',f'{host}/lottery',headers =OOO0O00OO00OOOOOO ).json ()#line:1126
            O0O0O000000O00O00 =O00O0000OOO0000OO .winning_rewards ()#line:1128
            if 'status'in OOO00O00O0O000000 :#line:1129
                if OOO00O00O0O000000 ['status']==200 :#line:1130
                    OOO0OO000OOO0O0OO =OOO00O00O0O000000 ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OOO0OO000OOO0O0OO )#line:1132
                    OOOOOO00O0O0O00OO =OOO00O00O0O000000 ['data'][1 ]['value']#line:1133
                    OOO0O000OO0OO0O00 =OOO00O00O0O000000 ['data'][0 ]['join_number']#line:1134
                    O00O0OOOO0OO0OO00 =int (float (OOO00O00O0O000000 ['data'][0 ]['totalValue']))#line:1135
                    O0OO0OOOO00O000OO =float (OOOOOO00O0O0O00OO /O00O0OOOO0OO0OO00 )*10000 #line:1136
                    O00O000OO0OO0O0OO =O00O0OOOO0OO0OO00 /OOO0O000OO0OO0O00 #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OOO0OO000OOO0O0OO)[:6]}颗金种子丨好友收益:{str(O0O0O000000O00O00)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO0OOOO00O000OO)[:6]}颗金种子丨☘️人均:{str(O00O000OO0OO0O0OO)[:7]}️')#line:1139
        except Exception as O0OOOO0000O00O0O0 :#line:1140
            print (O0OOOO0000O00O0O0 )#line:1141
    def energy (O0OO00O00O0000OO0 ):#line:1144
        try :#line:1145
            while True :#line:1146
                OO0O0OOO0OOO0000O =f'__{timi_new()}'#line:1147
                OOOO0000O0O0O0O00 ={'source':'scsc','authorization':O0OO00O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO0OOO0000O ),'signstring':OO0O0OOO0OOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OOO0OOO0O0OO00OOO =requests .request ('get',f'{host}/energy/general',headers =OOOO0000O0O0O0O00 ).json ()#line:1159
                if 'status'in OOO0OOO0O0OO00OOO :#line:1161
                    if OOO0OOO0O0OO00OOO ['status']==200 :#line:1162
                        O00OO00000OO000O0 =OOO0OOO0O0OO00OOO ['data']['ordinary_water']#line:1163
                        O0OOO00O000O0O0O0 =OOO0OOO0O0OO00OOO ['data']['ordinary_fertilizer']#line:1164
                        OO0OO00OOOOOOOO0O =OOO0OOO0O0OO00OOO ['data']['videoStatus']#line:1165
                        OOOOO0OO0OOOOO0OO =OOO0OOO0O0OO00OOO ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O0OOO00O000O0O0O0).split(".")[0]}丨水滴:{str(O00OO00000OO000O0).split(".")[0]}')#line:1168
                        if float (O0OOO00O000O0O0O0 )<96 :#line:1169
                            if OO0OO00OOOOOOOO0O :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                OO0O0O0O00OOOO000 =99 -float (O0OOO00O000O0O0O0 )#line:1172
                                O0O0000O00000O000 ={"fertilizer":str (OO0O0O0O00OOOO000 ).split ('.')[0 ]}#line:1173
                                OO00O000O0OOO0OO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO0000O0O0O0O00 ).json ()#line:1175
                                if 'status'in OO00O000O0OOO0OO0 :#line:1177
                                    if OO00O000O0OOO0OO0 ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{OO00O000O0OOO0OO0["message"]}')#line:1179
                                    if OO00O000O0OOO0OO0 ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OO00O000O0OOO0OO0["message"]}')#line:1181
                                        break #line:1182
                                if float (O0OOO00O000O0O0O0 )<78 :#line:1184
                                    OO0O0O0O00OOOO000 =80 -float (O0OOO00O000O0O0O0 )#line:1185
                                    OO00OO0OOOO0O0OOO =f'_fertilizer={int(OO0O0O0O00OOOO000)}_{timi_new()}'#line:1186
                                    O0000O0OO00O00O0O ={'source':'scsc','authorization':O0OO00O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OOOO0O0OOO ),'signstring':OO00OO0OOOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    OOOO0OO0O00O0OO0O ={"fertilizer":int (OO0O0O0O00OOOO000 )}#line:1198
                                    O000OO00OOO00000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0000O0OO00O00O0O ,data =OOOO0OO0O00O0OO0O ).json ()#line:1200
                                    if 'status'in O000OO00OOO00000O :#line:1202
                                        if O000OO00OOO00000O ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{O000OO00OOO00000O["message"]}丨数量:{int(OO0O0O0O00OOOO000)}')#line:1204
                                        if O000OO00OOO00000O ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{O000OO00OOO00000O["message"]}丨数量:{int(OO0O0O0O00OOOO000)}')#line:1206
                                            O0OOOOOO000O0O0OO =O000OO00OOO00000O ["message"].split ('-')[1 ]#line:1207
                                            OO0OOO000O0OO0OO0 =f'__{timi_new()}'#line:1208
                                            OOOO00OO00O0O000O ={'source':'scsc','authorization':O0OO00O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O0OO0OO0 ),'signstring':OO0OOO000O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OOOO0O00OO00O00O0 =requests .request ('get',f'{host}/user',headers =OOOO00OO00O0O000O ).json ()#line:1220
                                            if 'status'in OOOO0O00OO00O00O0 :#line:1221
                                                if OOOO0O00OO00O00O0 ['status']==200 :#line:1222
                                                    O0OO0OO0O00OO0OO0 =OOOO0O00OO00O00O0 ['data']['inner_id']#line:1223
                                                    if give_gold (O0OO0OO0O00OO0OO0 ,float (O0OOOOOO000O0O0OO )+1 ):#line:1224
                                                        O0OO00O00O0000OO0 .energy ()#line:1225
                        if float (O00OO00000OO000O0 )<880 :#line:1226
                            if OOOOO0OO0OOOOO0OO :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                OOO0OOO000O00O0OO =999 -float (O00OO00000OO000O0 )#line:1229
                                O000O00O0OOO0000O ={"water":str (OOO0OOO000O00O0OO ).split ('.')[0 ]}#line:1230
                                OOOO000OOOOO0O0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO0000O0O0O0O00 ).json ()#line:1232
                                if 'status'in OOOO000OOOOO0O0O0 :#line:1234
                                    if OOOO000OOOOO0O0O0 ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO000OOOOO0O0O0["message"]}')#line:1236
                                    if OOOO000OOOOO0O0O0 ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO000OOOOO0O0O0["message"]}')#line:1238
                                        break #line:1239
                                if float (O00OO00000OO000O0 )<780 :#line:1240
                                    OOO0OOO000O00O0OO =800 -float (O00OO00000OO000O0 )#line:1241
                                    O00OOOO0000000OO0 =f'_water={int(OOO0OOO000O00O0OO)}_{timi_new()}'#line:1242
                                    OO0O0OOOO000OOO0O ={'source':'scsc','authorization':O0OO00O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0000000OO0 ),'signstring':O00OOOO0000000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O0O0O00O0O00O0OO0 ={"water":int (OOO0OOO000O00O0OO )}#line:1254
                                    O000OOO00O00O00O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0O0OOOO000OOO0O ,data =O0O0O00O0O00O0OO0 ).json ()#line:1256
                                    if 'status'in O000OOO00O00O00O0 :#line:1258
                                        if O000OOO00O00O00O0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O000OOO00O00O00O0["message"]}丨数量:{int(OOO0OOO000O00O0OO)}')#line:1260
                                        if O000OOO00O00O00O0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O000OOO00O00O00O0["message"]}丨数量:{int(OOO0OOO000O00O0OO)}')#line:1262
                                            O0OOOOOO000O0O0OO =O000OOO00O00O00O0 ["message"].split ('-')[1 ]#line:1263
                                            OO0OOO000O0OO0OO0 =f'__{timi_new()}'#line:1264
                                            OOOO00OO00O0O000O ={'source':'scsc','authorization':O0OO00O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000O0OO0OO0 ),'signstring':OO0OOO000O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OOOO0O00OO00O00O0 =requests .request ('get',f'{host}/user',headers =OOOO00OO00O0O000O ).json ()#line:1276
                                            if 'status'in OOOO0O00OO00O00O0 :#line:1277
                                                if OOOO0O00OO00O00O0 ['status']==200 :#line:1278
                                                    O0OO0OO0O00OO0OO0 =OOOO0O00OO00O00O0 ['data']['inner_id']#line:1279
                                                    if give_gold (O0OO0OO0O00OO0OO0 ,float (O0OOOOOO000O0O0OO )+1 ):#line:1280
                                                        O0OO00O00O0000OO0 .energy ()#line:1281
                        break #line:1282
        except Exception as O0O0O000OO00OO00O :#line:1283
            print (O0O0O000OO00OO00O )#line:1284
def bundled_def ():#line:1287
    OO0OO0OOOOOO0000O =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OO0OO0OOOOOO0000O [random .randint (0 ,len (OO0OO0OOOOOO0000O )-1 )]#line:1289
def version_of_the_validation ():#line:1293
    return str ((105 -56 )/10 )#line:1294
def ubbbf ():#line:1296
    print ('卡密验证通过   ✅')#line:1297
def sc2 ():#line:1300
    return "19319#$%^&*((*"#line:1301
def OO00OO0OO0OO00OO00o0 ():#line:1304
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1306
def get_ip ():#line:1309
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1311
def gitee_validation ():#line:1314
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1315
def gitee_edition ():#line:1318
    try :#line:1319
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1320
    except :#line:1321
        sys .exit (0 )#line:1322
def O000OO000O0O00OOO00 ():#line:1326
    try :#line:1327
        O0OOO0000OOOO00OO =gitee_edition ()#line:1328
        if version_of_the_validation ()<O0OOO0000OOOO00OO ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO0000OOOO00OO["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O0OOO0000OOOO00OO["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO0000OOOO00OO["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O0OOO0000OOOO00OO["CityEarth"]["content"]}')#line:1334
    except Exception as OOO0OO0OOO00OOOOO :#line:1335
        print (OOO0OO0OOO00OOOOO )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
