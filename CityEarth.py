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
        OO0000OOO0OO0OOO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO0000OOO0OO0OOO0)}个账号==========")#line:17
        for OOO00OOO0O0OOO00O in OO0000OOO0OO0OOO0 :#line:18
            OOOOOO00OO0O0O0OO =[]#line:19
            print (f"------------正在执行第{OO0000OOO0OO0OOO0.index(OOO00OOO0O0OOO00O) + 1}个账号------------")#line:20
            O0OOO0O0OO00O0000 =CityEarth (OOO00OOO0O0OOO00O ,OOOOOO00OO0O0O0OO ,OO0000OOO0OO0OOO0 .index (OOO00OOO0O0OOO00O ))#line:21
            def OO0O00O00OO0O0OOO ():#line:23
                if O0OOO0O0OO00O0000 .base_info ():#line:25
                    O0OOO0O0OO00O0000 .sealing ()#line:27
                    O0OOO0O0OO00O0000 .invitenum ()#line:29
                    O0OOO0O0OO00O0000 .query_to_sell ()#line:31
                    O0OOO0O0OO00O0000 .friends_invitation ()#line:35
                    O0OOO0O0OO00O0000 .energy ()#line:37
                    O0OOO0O0OO00O0000 .add_clover ()#line:39
                    O0OOO0O0OO00O0000 .propsraffle ()#line:41
                    O0OOO0O0OO00O0000 .synthetic ()#line:43
                    O0OOO0O0OO00O0000 .crops_illustrated ()#line:45
                    O0OOO0O0OO00O0000 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0OOO0O0OO00O0000 .give_gold ()#line:50
            O0OOOO0O000000OO0 =threading .Thread (target =OO0O00O00OO0O0OOO )#line:52
            O0OOOO0O000000OO0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0000O0O0O0O0000O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0000O0O0O0O0000O +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O00OOOO00O0000O0O in invited_new :#line:62
            print (O00OOOO00O0000O0O )#line:63
        print ('开始打印未实名的token')#line:64
        for OOO0OOOO0O0O00O0O in weishim :#line:65
            print (OOO0OOOO0O0O00O0O )#line:66
    except Exception as O00O0O0OO0O00OOOO :#line:67
        print (O00O0O0OO0O00OOOO )#line:68
def give_gold (OO00OOOOOO0000O00 ,O0O0OOO000OO0O000 ):#line:72
    try :#line:73
        O0O0OO0OO00OO0000 =f'_doneeNo={OO00OOOOOO0000O00}&quantity={int(O0O0OOO000OO0O000)}_{timi_new()}'#line:74
        O0O0O0OOO00OO000O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OO00OO0000 ),'signstring':O0O0OO0OO00OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO0OOO0OO000O0OO0 ={"quantity":int (O0O0OOO000OO0O000 ),"doneeNo":OO00OOOOOO0000O00 }#line:89
        OOO00000OOOOOO00O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0OOO00OO000O ,data =OO0OOO0OO000O0OO0 ).json ()#line:90
        if 'status'in OOO00000OOOOOO00O :#line:92
            if OOO00000OOOOOO00O ['status']==200 :#line:93
                if OOO00000OOOOOO00O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O0O0OOO000OO0O000)}种子给{OO00OOOOOO0000O00}成功')#line:95
                    return True #line:96
            if OOO00000OOOOOO00O ['status']==401 :#line:97
                print (f'【赠送种子】:{OOO00000OOOOOO00O["message"]}')#line:98
                return False #line:99
            if OOO00000OOOOOO00O ['status']==500 :#line:100
                print (f'【赠送种子】:{OOO00000OOOOOO00O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO0O00OOOOO0OO0O :#line:104
        print (OOO0O00OOOOO0OO0O )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O00000OOOOOO0000O ):#line:115
    OO0O0O00000O0O000 =hashlib .md5 (O00000OOOOOO0000O .encode ()).hexdigest ()#line:116
    OOO000OO00O0000OO =sc1 ()#line:117
    O0000O00000000000 =sc2 ()#line:118
    O0OO0O0OOO0000O00 =sc3 ()#line:119
    O00O00O0OOO0O0000 =OOO000OO00O0000OO +OO0O0O00000O0O000 +O0000O00000000000 +O0OO0O0OOO0000O00 #line:120
    O0OOOOOO0OO0000O0 =hashlib .md5 (O00O00O0OOO0O0000 .encode ()).hexdigest ()#line:121
    return O0OOOOOO0OO0000O0 #line:122
def format_msg ():#line:125
    OO000O0OOO0OO0OO0 =""#line:126
    for OOO00O0O0000000OO in msg_list :#line:127
        OO000O0OOO0OO0OO0 +=str (OOO00O0O0000000OO )+"\r\n"#line:128
    return OO000O0OOO0OO0OO0 #line:129
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
def get_json_data (OOOO0000OOO000OOO ,OOO00O0O00O0000OO ,OO00O0OOOOOOOO00O ,O000OO0000OOOOO00 ):#line:153
    with open (OOOO0000OOO000OOO ,'rb')as OO0OOOO0O000OOOOO :#line:154
        OOOOO0OO000O0O0O0 =json .load (OO0OOOO0O000OOOOO )#line:155
        OOOOO0OO000O0O0O0 ['data'][OOO00O0O00O0000OO ][OO00O0OOOOOOOO00O ]=O000OO0000OOOOO00 #line:156
        OOO0O00OOO000O00O =OOOOO0OO000O0O0O0 #line:157
    OO0OOOO0O000OOOOO .close ()#line:158
    return OOO0O00OOO000O00O #line:159
def write_json_data (OO00000O00OOO00OO ):#line:162
    with open (json_path1 ,'w')as O0OOO00O00O0O0O0O :#line:163
        json .dump (OO00000O00OOO00OO ,O0OOO00O00O0O0O0O ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O0OOO00O00O0O0O0O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OO0O00000O000OO ,OOOO00O000O0O0OOO ,OOOO00O0OO0OO0O00 ,O0OOOO0O0OOO0OOO0 ):#line:171
        try :#line:172
            O0OO0O00000O000OO .msg =OOOO00O0OO0OO0O00 #line:173
            O0OO0O00000O000OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OO0O00000O000OO .token =OOOO00O000O0O0OOO ['authorization']#line:175
            O0OO0O00000O000OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OO0O00000O000OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OO0O00000O000OO .elephant_user =OOOO00O000O0O0OOO ['elephant_user']#line:178
            O0OO0O00000O000OO .elephant_pswd =OOOO00O000O0O0OOO ['elephant_pswd']#line:179
            O0OO0O00000O000OO .elephant_Task_ID =OOOO00O000O0O0OOO ['elephant_Task_ID']#line:180
            O0OO0O00000O000OO .len_new =O0OOOO0O0OOO0OOO0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO0OOO0OOO000O0OO ):#line:186
        try :#line:187
            OO0OOO0OOO000O0OO .watched_ad ()#line:189
            O0OO0O0OOO0O0O0OO =f'__{timi_new()}'#line:190
            OO0OO0O00OOO0O0O0 ={'source':'scsc','authorization':OO0OOO0OOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOO0O0O0OO ),'signstring':O0OO0O0OOO0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00O0O0OOOOOOOOO0 =requests .request ('get',f'{host}/user',headers =OO0OO0O00OOO0O0O0 ).json ()#line:202
            if 'status'in O00O0O0OOOOOOOOO0 :#line:204
                if O00O0O0OOOOOOOOO0 ['status']==200 :#line:205
                    OO000O00000O0O0OO =O00O0O0OOOOOOOOO0 ['data']['nickname']#line:206
                    OO0OO0000O00OOO00 =O00O0O0OOOOOOOOO0 ['data']['inner_id']#line:207
                    O0O0000O0OO0OO000 =O00O0O0OOOOOOOOO0 ['data']['assets']['gold']#line:208
                    O0O000O0OO00OOO0O =O00O0O0OOOOOOOOO0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OO000O00000O0O0OO[:5]}丨ID:{OO0OO0000O00OOO00}丨等级:{O0O000O0OO00OOO0O}丨金种子:{str(O0O0000O0OO0OO000).split(".")[0]}')#line:211
                    if 'wx_'in OO000O00000O0O0OO :#line:212
                        OO0OOO0OOO000O0OO .change_nickname ()#line:213
                if O00O0O0OOOOOOOOO0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO0OOO0OOO000O0OO .elephant_user =='f':#line:216
                        return False #line:217
                    OOO00OO00OOO000OO =Invalid_login .addtask (elephant_user =OO0OOO0OOO000O0OO .elephant_user ,elephant_pswd =OO0OOO0OOO000O0OO .elephant_pswd ,elephant_Task_ID =OO0OOO0OOO000O0OO .elephant_Task_ID )#line:220
                    OO000OO0OOOOOOOO0 =get_json_data (json_path ,OO0OOO0OOO000O0OO .len_new ,'authorization',OOO00OO00OOO000OO )#line:221
                    if write_json_data (OO000OO0OOOOOOOO0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00O0O0OOOOOOOOO0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OO0O0OO000OOO00OO :#line:228
            print (OO0O0OO000OOO00OO )#line:229
    def sealing (O0000OOOO00OOOOO0 ):#line:232
        try :#line:233
            OO00000O00OOOO0O0 =f'__{timi_new()}'#line:234
            OO000000O00OO000O ={'source':'scsc','authorization':O0000OOOO00OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O00OOOO0O0 ),'signstring':OO00000O00OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO000000O00OO000O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO000000O00OO000O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO000000O00OO000O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO000000O00OO000O )#line:249
            requests .request ('get',f'{host}/user',headers =OO000000O00OO000O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO000000O00OO000O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO000000O00OO000O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO000000O00OO000O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO000000O00OO000O )#line:254
            requests .request ('get',f'{host}/assets',headers =OO000000O00OO000O )#line:255
        except Exception as OOOOOOO0OOOOO0OO0 :#line:256
            print (OOOOOOO0OOOOO0OO0 )#line:257
    def ddd (O0OO0000OOO00O0O0 ):#line:259
        try :#line:260
            OOOOOOO00O00000OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0000O00OOOOO0OO0 ={'source':'scsc','authorization':O0OO0000OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO00O00000OO ),'signstring':OOOOOOO00O00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO0O0OO000OO00O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0000O00OOOOO0OO0 ).json ()#line:273
            print (OOO0O0OO000OO00O0 )#line:274
        except Exception as OO000O0O0OOOO0O00 :#line:277
            print (OO000O0O0OOOO0O00 )#line:278
    def the_query (O0O0O0OO0OOO000O0 ):#line:283
        try :#line:284
            O000OOO0O00OOOOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0OOOO00OOO00O0OO ={'authorization':O0O0O0OO0OOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O00OOOOOO ),'signstring':O000OOO0O00OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O000O0O0O0OO00O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOOO00OOO00O0OO ).json ()#line:296
            if 'status'in O000O0O0O0OO00O0O :#line:298
                if O000O0O0O0OO00O0O ['status']==200 :#line:299
                    return O000O0O0O0OO00O0O ['data']['rows'][4 ]['price']#line:300
        except Exception as OO00O0OOO00000O00 :#line:301
            print (OO00O0OOO00000O00 )#line:302
    def market_sale (OO0OOOO00OO00000O ,OOOO0OOO0O0000O00 ):#line:305
        try :#line:306
            O0O00OO0OOOO00O0O =timi_new ()#line:307
            OO000OO00OOO00OO0 =f'type=crop__{O0O00OO0OOOO00O0O}'#line:308
            O0000O0O0O00O0OOO ={'source':'scsc','authorization':OO0OOOO00OO00000O .token ,'timestamp':str (O0O00OO0OOOO00O0O ),'sign':sign (OO000OO00OOO00OO0 ),'signstring':OO000OO00OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0000OOOO0O00000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0000O0O0O00O0OOO ).json ()#line:320
            if 'status'in O0000OOOO0O00000O :#line:322
                if O0000OOOO0O00000O ['status']==200 :#line:323
                    if O0000OOOO0O00000O ['data']['rows']:#line:324
                        O00OO00OOOOOO000O =O0000OOOO0O00000O ['data']['rows'][0 ]['packsackItemId']#line:325
                        OO000O0OO000O0O00 =O0000OOOO0O00000O ['data']['rows'][0 ]['quantity']#line:326
                        if float (OOOO0OOO0O0000O00 )>8 :#line:327
                            OOO0OOO0000O0000O =f'_packsackItemId={O00OO00OOOOOO000O}&price={str(OOOO0OOO0O0000O00)[:5]}&quantity={OO000O0OO000O0O00}_{O0O00OO0OOOO00O0O}'#line:328
                            O0OOO0OOOOOOOOO0O ={'source':'scsc','authorization':OO0OOOO00OO00000O .token ,'timestamp':str (O0O00OO0OOOO00O0O ),'sign':sign (OOO0OOO0000O0000O ),'signstring':OOO0OOO0000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOO0O000OO0OO0000 ={"packsackItemId":O00OO00OOOOOO000O ,"price":str (OOOO0OOO0O0000O00 )[:5 ],"quantity":str (OO000O0OO000O0O00 )}#line:344
                            O0OOOOO00O00O0OOO =requests .request ('post',f'{host}/market/sale',headers =O0OOO0OOOOOOOOO0O ,data =OOO0O000OO0OO0000 ).json ()#line:345
                            if 'status'in O0OOOOO00O00O0OOO :#line:347
                                if O0OOOOO00O00O0OOO ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OO000O0OO000O0O00}丨价格:{str(OOOO0OOO0O0000O00)[:5]}')#line:349
                                if O0OOOOO00O00O0OOO ['status']==500 :#line:350
                                    print (f'【上架芦荟】:{O0OOOOO00O00O0OOO["message"]}')#line:351
        except Exception as O000000OOOO00O00O :#line:352
            print (O000000OOOO00O00O )#line:353
    def query_to_sell (O000O0OO0O0OO000O ):#line:356
        global count_list #line:357
        try :#line:358
            O0O0O0OO000O00O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:359
            O00OO0O0OO0O0O00O ={'source':'scsc','authorization':O000O0OO0O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO000O00O0O ),'signstring':O0O0O0OO000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:370
            O000O00O0O0000000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OO0O0OO0O0O00O ).json ()#line:371
            if 'status'in O000O00O0O0000000 :#line:373
                if O000O00O0O0000000 ['status']==200 :#line:374
                    for OO00OOOO0OOO00000 in O000O00O0O0000000 ['data']['rows']:#line:375
                        O0O0O00000OO0000O =OO00OOOO0OOO00000 ['materialKey']#line:376
                        OO000OOO0OOO00000 =OO00OOOO0OOO00000 ['quantity']#line:377
                        OO0OO0000OO00O0OO =OO00OOOO0OOO00000 ['price']#line:378
                        OO0O0O0OO0O0OO00O =OO00OOOO0OOO00000 ['saleState']#line:379
                        if OO0O0O0OO0O0OO00O ==0 :#line:380
                            print (f'【出售订单】:名称:{O0O0O00000OO0000O}丨数量:{OO000OOO0OOO00000}丨价格:{OO0OO0000OO00O0OO}')#line:381
                            count_list +=OO000OOO0OOO00000 #line:382
                            O0O0O00O000O00OOO =O000O0OO0O0OO000O .the_query ()#line:384
                            if float (O0O0O00O000O00OOO )!=float (OO0OO0000OO00O0OO ):#line:385
                                OOOOOOOO00OOO0O0O =OO00OOOO0OOO00000 ['id']#line:386
                                O000O0OO0O0OO000O .cacel_sale (OOOOOOOO00OOO0O0O )#line:387
                    O000O0OO0O0OO000O .game_map ()#line:389
        except Exception as O0OO00OO000OOOO00 :#line:391
            print (O0OO00OO000OOOO00 )#line:392
    def cacel_sale (OO000OO0000000O00 ,O0OOOO00O00OO0OOO ):#line:395
        try :#line:396
            O0O00O00000O0OO0O =f'_saleId={O0OOOO00O00OO0OOO}_{timi_new()}'#line:397
            O0O0OO0O0O0OOOO0O ={'source':'scsc','authorization':OO000OO0000000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00000O0OO0O ),'signstring':O0O00O00000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:408
            O0OO000000OO00O00 ={"saleId":O0OOOO00O00OO0OOO }#line:409
            O0000O00000OO0000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0OO0O0O0OOOO0O ,data =O0OO000000OO00O00 ).json ()#line:410
            if 'status'in O0000O00000OO0000 :#line:412
                if O0000O00000OO0000 ['status']==200 :#line:413
                    print (f'【下架出售】:{O0000O00000OO0000["data"]}')#line:414
        except Exception as O0O0000O0O00O0000 :#line:415
            print (O0O0000O0O00O0000 )#line:416
    def change_nickname (O0OO0O0OO00OO0O00 ):#line:419
        try :#line:420
            OO0O00OOOO00OOO00 =timi_new ()#line:421
            O0000O0O00000O0O0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OO0OOO0O000OO00OO =requests .request ('post','https://www.qmsjmfb.com/',data =O0000O0O00000O0O0 ).text #line:423
            OO0O0O00O00OO00OO =re .findall ('<ul><li>(.*?)</li>',OO0OOO0O000OO00OO )[0 ][:3 ]#line:424
            OOO0OOOOOO0000OOO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0O00O00OO00OO}').json ()#line:425
            OOO000OO0OOO00O00 =OOO0OOOOOO0000OOO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:426
            O0O00O000OO0O0O0O ={"nickname":OOO000OO0OOO00O00 }#line:427
            O0OOO0000OOO000O0 =f'_nickname={OOO000OO0OOO00O00}_{OO0O00OOOO00OOO00}'#line:428
            O00OO00OOOO0O0000 ={'source':'scsc','authorization':O0OO0O0OO00OO0O00 .token ,'timestamp':OO0O00OOOO00OOO00 ,'sign':sign (O0OOO0000OOO000O0 ),'signstring':O0OOO0000OOO000O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            O00O0O0000OOO0O00 =requests .request ('patch',f'{host}/user/nickname',headers =O00OO00OOOO0O0000 ,data =O0O00O000OO0O0O0O ).json ()#line:440
            if 'status'in O00O0O0000OOO0O00 :#line:442
                if O00O0O0000OOO0O00 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OOO000OO0OOO00O00}丨{O00O0O0000OOO0O00["message"]}')#line:444
        except Exception as OOOO00000000OO000 :#line:445
            print (OOOO00000000OO000 )#line:446
    def withdraw (OOO0O0O0O0000O00O ):#line:449
        try :#line:450
            OO0OOOOO00O00O0OO =f'__{timi_new()}'#line:451
            OOO0O0OOO0000O00O ={'source':'scsc','authorization':OOO0O0O0O0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00O00O0OO ),'signstring':OO0OOOOO00O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOOOOO000OOO0OO0O =requests .request ('get',f'{host}/assets',headers =OOO0O0OOO0000O00O ).json ()#line:463
            if 'status'in OOOOOO000OOO0OO0O :#line:465
                if OOOOOO000OOO0OO0O ['status']==200 :#line:466
                    OOO000000O000O0OO =OOOOOO000OOO0OO0O ['data']['cash']#line:467
                    if float (OOO000000O000O0OO )>20 :#line:468
                        OO0OOOOO00O00O0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        OOO0O0OOO0000O00O ={'authorization':OOO0O0O0O0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO00O00O0OO ),'signstring':OO0OOOOO00O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O0O0O0O000O0OOO00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OOOO000OO00O0OO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0O0OOO0000O00O ,data =O0O0O0O000O0OOO00 ).json ()#line:482
                        if 'status'in OOOO000OO00O0OO0O :#line:484
                            if OOOO000OO00O0OO0O ['status']==200 :#line:485
                                print (f'【余额提现】:{OOOO000OO00O0OO0O["data"]}')#line:486
                        if 'status'in OOOO000OO00O0OO0O :#line:487
                            if OOOO000OO00O0OO0O ['status']==500 :#line:488
                                print (f'【余额提现】:{OOOO000OO00O0OO0O["message"]}')#line:489
        except Exception as OOOOO000O0OO00OOO :#line:490
            print (OOOOO000O0OO00OOO )#line:491
    def invitenum (OOOOOOO0OO000O0O0 ):#line:494
        global invited_new #line:495
        try :#line:496
            OOO00OO0OOO0000O0 =f'__{timi_new()}'#line:497
            O0OO0OOO00O00000O ={'source':'scsc','authorization':OOOOOOO0OO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0OOO0000O0 ),'signstring':OOO00OO0OOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OO00O0OO000OO0000 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO0OOO00O00000O ).json ()#line:509
            if 'status'in OO00O0OO000OO0000 :#line:511
                if OO00O0OO000OO0000 ['status']==200 :#line:512
                    OO0O0OOOO0000O00O =OO00O0OO000OO0000 ['data']['invited_count']#line:513
                    OOOOOO0OO0OO0OOOO =OO00O0OO000OO0000 ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OO0O0OOOO0000O00O}丨间邀好友:{OOOOOO0OO0OO0OOOO}')#line:515
                    if OO0O0OOOO0000O00O <2 :#line:516
                        OO0OOOOOOO0O0O0OO =f'__{timi_new()}'#line:517
                        OO0O00O0OOOO0O000 ={'source':'scsc','authorization':OOOOOOO0OO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOOO0O0O0OO ),'signstring':OO0OOOOOOO0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OOOO000O00O0OO0O0 =requests .request ('get',f'{host}/user',headers =OO0O00O0OOOO0O000 ).json ()#line:529
                        if 'status'in OOOO000O00O0OO0O0 :#line:531
                            if OOOO000O00O0OO0O0 ['status']==200 :#line:532
                                invited_new .append (OOOO000O00O0OO0O0 ['data']['inner_id'])#line:533
        except Exception as OOO00O00OOOO00OO0 :#line:534
            print (OOO00O00OOOO00OO0 )#line:535
    def game_map (O00OOOOO00OOO0OO0 ):#line:538
        try :#line:539
            OO00O0000000000OO =f'__{timi_new()}'#line:540
            O0O000OOO0000OOOO ={'source':'scsc','authorization':O00OOOOO00OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000000000OO ),'signstring':OO00O0000000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O0OOOOO0OOOO00OO0 =requests .request ('get',f'{host}/game/map',headers =O0O000OOO0000OOOO ).json ()#line:552
            if 'status'in O0OOOOO0OOOO00OO0 :#line:554
                if O0OOOOO0OOOO00OO0 ['status']==200 :#line:555
                    for OOO00O000OO0OOOOO in O0OOOOO0OOOO00OO0 ['data']['list'][0 ]['crops']:#line:556
                        OOOOO0OO00OOOOO00 =OOO00O000OO0OOOOO ['level']#line:558
                        if OOOOO0OO00OOOOO00 ==41 :#line:559
                            O0OO00O0OO0O00OO0 =OOO00O000OO0OOOOO ['crop_name']#line:560
                            O0OO0O000OO0O0O0O =OOO00O000OO0OOOOO ['count']#line:561
                            if O0OO0O000OO0O0O0O >0 :#line:562
                                print (f'【农业资产】:{O0OO00O0OO0O00OO0}丨数量:{O0OO0O000OO0O0O0O}')#line:563
                                O000O0OO00OO0OOO0 =O00OOOOO00OOO0OO0 .the_query ()#line:564
                                O00OOOOO00OOO0OO0 .market_sale (O000O0OO00OO0OOO0 )#line:565
        except Exception as OOO0OOOO00O0O0O00 :#line:566
            print (OOO0OOOO00O0O0O00 )#line:567
    def give_gold (OO00O0O00O0O000O0 ):#line:570
        try :#line:571
            OOO000OO00OOOO000 =f'__{timi_new()}'#line:572
            OOOOOO0O00000000O ={'source':'scsc','authorization':OO00O0O00O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OOOO000 ),'signstring':OOO000OO00OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            O0O00O0O0O00O00OO =requests .request ('get',f'{host}/user',headers =OOOOOO0O00000000O ).json ()#line:584
            if 'status'in O0O00O0O0O00O00OO :#line:585
                if O0O00O0O0O00O00OO ['status']==200 :#line:586
                    if float (OO00O0O00O0O000O0 .doneeNo )!=0 :#line:587
                        OOO0O0OOOOO000OO0 =O0O00O0O0O00O00OO ['data']['assets']['gold']#line:588
                        if float (OOO0O0OOOOO000OO0 )>float (OO00O0O00O0O000O0 .innerId ):#line:589
                            OOOOO00O0OO0OOO00 =int (float (OOO0O0OOOOO000OO0 )/1.1 )#line:590
                            OOO000OO00OOOO000 =f'_doneeNo={OO00O0O00O0O000O0.doneeNo}&quantity={OOOOO00O0OO0OOO00}_{timi_new()}'#line:591
                            OOOOOO0O00000000O ={'source':'scsc','authorization':OO00O0O00O0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO00OOOO000 ),'signstring':OOO000OO00OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OO0OOO00O00O0000O ={"quantity":OOOOO00O0OO0OOO00 ,"doneeNo":OO00O0O00O0O000O0 .doneeNo }#line:606
                            OO0OO0OOO000OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOO0O00000000O ,data =OO0OOO00O00O0000O ).json ()#line:607
                            if 'status'in OO0OO0OOO000OOO0O :#line:609
                                if OO0OO0OOO000OOO0O ['status']==200 :#line:610
                                    if OO0OO0OOO000OOO0O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OOOOO00O0OO0OOO00}种子给{OO00O0O00O0O000O0.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OO0O0OOOOO0000O00 :#line:615
            print (OO0O0OOOOO0000O00 )#line:616
    def invitation (O00O00OOO0O000000 ):#line:618
        try :#line:619
            _O0000O000O0OO0O00 =float (bundled_def ())/4 #line:620
            OO0O0OOO0O0O0O0O0 =f'_innerId={int(_O0000O000O0OO0O00)}_{timi_new()}'#line:622
            O00O000OOO0O00000 ={'source':'scsc','authorization':O00O00OOO0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO0O0O0O0O0 ),'signstring':OO0O0OOO0O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:633
            OOOO0O0O0O0O000O0 ={"innerId":int (_O0000O000O0OO0O00 )}#line:634
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O000OOO0O00000 ,data =OOOO0O0O0O0O000O0 )#line:635
        except Exception as O000OOO0000O00OO0 :#line:636
            print (O000OOO0000O00OO0 )#line:637
    def winning_rewards (O00OOOOO000OO0OO0 ):#line:640
        try :#line:641
            OO0O0000O00OOOOO0 =f'__{timi_new()}'#line:642
            OOOOO0OO0O0000OO0 ={'source':'scsc','authorization':O00OOOOO000OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O00OOOOO0 ),'signstring':OO0O0000O00OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:653
            OOO0OOOOO00OO0000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOOOO0OO0O0000OO0 ).json ()#line:654
            if 'status'in OOO0OOOOO00OO0000 :#line:656
                if OOO0OOOOO00OO0000 ['status']==200 :#line:657
                    if OOO0OOOOO00OO0000 ['data']['amount']:#line:658
                        OO0O0O00O00O00OOO =OOO0OOOOO00OO0000 ['data']['amount']['gold']#line:659
                        return OO0O0O00O00O00OOO #line:660
                    else :#line:661
                        return 0 #line:662
        except Exception as O0O00OOO0OO00O000 :#line:663
            print (O0O00OOO0OO00O000 )#line:664
    def certification (O00OO0000000O000O ):#line:667
        try :#line:668
            O0O0O0000OO00O0O0 =f'__{timi_new()}'#line:669
            O00000O0OO0OO00O0 ={'source':'scsc','authorization':O00OO0000000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OO00O0O0 ),'signstring':O0O0O0000OO00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:680
            OOOO0O0000000OOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00000O0OO0OO00O0 ).json ()#line:681
            if 'status'in OOOO0O0000000OOOO :#line:683
                if OOOO0O0000000OOOO ['status']==200 :#line:684
                    if OOOO0O0000000OOOO ['data']['result']:#line:685
                        OOOOO0O00O000O0O0 =OOOO0O0000000OOOO ['data']['nick_name']#line:686
                        return OOOOO0O00O000O0O0 #line:687
                    else :#line:688
                        return '未实名'#line:689
        except Exception as O0OO0OO00OO0OOO00 :#line:690
            print (O0OO0OO00OO0OOO00 )#line:691
    def crops_illustrated (O000O0O00000OO000 ):#line:694
        try :#line:695
            O0OO0OO0OOO0000OO =f'__{timi_new()}'#line:696
            OO00000OOO000O00O ={'source':'scsc','authorization':O000O0O00000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOO0000OO ),'signstring':O0OO0OO0OOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:707
            OO0OO0OOO0OOO0OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO00000OOO000O00O ).json ()#line:708
            if 'status'in OO0OO0OOO0OOO0OOO :#line:710
                if OO0OO0OOO0OOO0OOO ['status']==200 :#line:711
                    OO00OOO00O0O00O00 =OO0OO0OOO0OOO0OOO ['data'][0 ]['crops']#line:712
                    for O0O000O00OOO00OOO in OO00OOO00O0O00O00 :#line:713
                        if O0O000O00OOO00OOO ['ill_clover_award']:#line:714
                            if float (O0O000O00OOO00OOO ['ill_clover_award'])>1 :#line:715
                                if O0O000O00OOO00OOO ['is_finish']:#line:716
                                    if not O0O000O00OOO00OOO ['is_getit']:#line:717
                                        if O000O0O00000OO000 .certification ()!='未实名':#line:718
                                            O0OO0OO0OOO0000OO =f'_award_level={O0O000O00OOO00OOO["level"]}_{timi_new()}'#line:719
                                            OO00000OOO000O00O ={'source':'scsc','authorization':O000O0O00000OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOO0000OO ),'signstring':O0OO0OO0OOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
                                            OO00O00O0000O00OO ={"award_level":O0O000O00OOO00OOO ['level']}#line:731
                                            OO0OOOOO0O0OO0OO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO00000OOO000O00O ,json =OO00O00O0000O00OO ).json ()#line:733
                                            if 'status'in OO0OOOOO0O0OO0OO0 :#line:734
                                                if OO0OOOOO0O0OO0OO0 ['status']==200 :#line:735
                                                    O0OOO0000O000OO00 =OO0OOOOO0O0OO0OO0 ['data']['ill_clover_award']#line:736
                                                    print (f'【图鉴奖励】:领取{O0O000O00OOO00OOO["crop_name"]}成就丨奖励{O0OOO0000O000OO00}☘️')#line:738
                                                if OO0OOOOO0O0OO0OO0 ['status']==500 :#line:739
                                                    print (f'【图鉴奖励】:{OO0OOOOO0O0OO0OO0["message"]}')#line:740
        except Exception as OO000O0O0O0OOOOO0 :#line:741
            print (OO000O0O0O0OOOOO0 )#line:742
    def watched_ad (OO0O0OO000OO0OOO0 ):#line:745
        try :#line:746
            OO00O0O000O00OOOO =f'__{timi_new()}'#line:747
            OO0OO0000OOO0O0OO ={'source':'scsc','authorization':OO0O0OO000OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O000O00OOOO ),'signstring':OO00O0O000O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:758
            OO00000O0O0OO00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0000OOO0O0OO ).json ()#line:759
            if 'status'in OO00000O0O0OO00O0 :#line:761
                if OO00000O0O0OO00O0 ['status']==200 :#line:762
                    if 'offlineInfo'in OO00000O0O0OO00O0 ['data']:#line:763
                        time .sleep (random .randint (1 ,3 ))#line:764
                        O00OOO0OOO000OOO0 =OO00000O0O0OO00O0 ['data']['offlineInfo']['off_minute']#line:765
                        OO0OO0OO000OO0O0O =float (OO00000O0O0OO00O0 ['data']['silver'])/1000000000000 #line:766
                        time .sleep (1 )#line:767
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OO0000OOO0O0OO ).json ()#line:768
                        time .sleep (2 )#line:769
                        OOO0OOO0OO0O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0000OOO0O0OO ).json ()#line:770
                        if 'status'in OOO0OOO0OO0O0OOOO :#line:772
                            if OOO0OOO0OO0O0OOOO ['status']==200 :#line:773
                                OOO0O00OOO000O0OO =float (OOO0OOO0OO0O0OOOO ['data']['silver'])/1000000000000 #line:774
                                O00OOO0O0OO00OO00 =str (OOO0O00OOO000O0OO -OO0OO0OO000OO0O0O )[:6 ]#line:775
                                print (f'【离线奖励】:翻倍离线{O00OOO0OOO000OOO0}分钟奖励🌱数量:{O00OOO0O0OO00OO00}t粒')#line:776
        except Exception as OO000O000000O00O0 :#line:777
            print (OO000O000000O00O0 )#line:778
    def user_ad (O000000O0000O0000 ):#line:781
        try :#line:782
            OO000O000OO0OO0OO =f'__{timi_new()}'#line:783
            OOO00O0OOO00O000O ={'source':'scsc','authorization':O000000O0000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000OO0OO0OO ),'signstring':OO000O000OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:794
            OO00OO00O0OO000OO =requests .request ('get',f'{host}/user/ad',headers =OOO00O0OOO00O000O ).json ()#line:795
            if 'status'in OO00OO00O0OO000OO :#line:797
                if OO00OO00O0OO000OO ['status']==200 :#line:798
                    OO00OO00OOOOOOO0O =OO00OO00O0OO000OO ['data']['max_time']#line:799
                    OO0O0O00OO0000OOO =OO00OO00O0OO000OO ['data']['watch_time']#line:800
                    OOO00OO0OOOOO0000 =OO00OO00O0OO000OO ['data']['added_time']#line:801
                    print (f'【获取种子】:获取🌱剩余{OOO00OO0OOOOO0000 + OO00OO00OOOOOOO0O - OO0O0O00OO0000OOO}次丨好友提供:{OOO00OO0OOOOO0000}次')#line:802
                    if OOO00OO0OOOOO0000 +OO00OO00OOOOOOO0O -OO0O0O00OO0000OOO >0 :#line:803
                        time .sleep (random .randint (16 ,19 ))#line:804
                        OOOOO000O0OO0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O0OOO00O000O ).json ()#line:805
                        if 'status'in OOOOO000O0OO0OO00 :#line:807
                            if OOOOO000O0OO0OO00 ['status']==200 :#line:808
                                OOOOOOOOOOOO00O0O =float (OOOOO000O0OO0OO00 ['data']['silver'])/1000000000000 #line:809
                                print (f'【获取种子】:获得🌱:{int(OOOOOOOOOOOO00O0O)}t粒')#line:810
                                return True #line:811
                            if OOOOO000O0OO0OO00 ['status']==500 :#line:812
                                O0000OOOOOOOO0OOO =OOOOO000O0OO0OO00 ['message']#line:813
                                print (f'【获取种子】:{O0000OOOOOOOO0OOO}')#line:814
                                return False #line:815
        except Exception as OO0O000OO000OO0OO :#line:816
            print (OO0O000OO000OO0OO )#line:817
    def synthetic (OOO00000OOOO000O0 ):#line:820
        global id ,g #line:821
        try :#line:822
            OOO0O00O0O00OOOOO =OOO00000OOOO000O0 .level_new ()#line:823
            OOOOOO00OOOO0OO0O =random .randint (9 ,11 )#line:824
            O0OOOO0O0O000O0OO =f'_site=8&targetSite={OOOOOO00OOOO0OO0O}_{timi_new()}'#line:825
            OO00O00OO0OOO00OO ={'source':'scsc','authorization':OOO00000OOOO000O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O0O000O0OO ),'signstring':O0OOOO0O0O000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:836
            OO00OO0O0O0O00OO0 ={"site":int (8 ),"targetSite":int (OOOOOO00OOOO0OO0O )}#line:837
            requests .request ('post',f'{host}/game/crops/move',headers =OO00O00OO0OOO00OO ,json =OO00OO0O0O0O00OO0 )#line:838
            while True :#line:839
                O00000OO000O0O00O =f'__{timi_new()}'#line:840
                O0OOO0O0000OOOOO0 ={'source':'scsc','authorization':OOO00000OOOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO000O0O00O ),'signstring':O00000OO000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:851
                OO000O0O0O00OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0O0000OOOOO0 ).json ()#line:852
                if 'status'in OO000O0O0O00OOOO0 :#line:854
                    if OO000O0O0O00OOOO0 ['status']==200 :#line:855
                        O0OO00OOOO0000000 =OO000O0O0O00OOOO0 ['data']['cropList']#line:856
                        O0000OO000O0O0000 =OO000O0O0O00OOOO0 ['data']['gameCoreDataDBid']#line:857
                        OO000OO000O000OOO =float (OO000O0O0O00OOOO0 ['data']['silver'])/1000000000000 #line:858
                        OO00O00OOO0OOOO00 =0 #line:863
                        for OO0O00O00OO0O0O00 in O0OO00OOOO0000000 :#line:864
                            if not OO0O00O00OO0O0O00 :#line:865
                                OO0OOO0O00OO00O00 =f'_crop_id={O0000OO000O0O0000}&site={OO00O00OOO0OOOO00}_{OOO00000OOOO000O0.time}'#line:866
                                O0OOOOO0000OOOOOO ={'source':'scsc','authorization':OOO00000OOOO000O0 .token ,'timestamp':OOO00000OOOO000O0 .time ,'sign':sign (OO0OOO0O00OO00O00 ),'signstring':OO0OOO0O00OO00O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:876
                                O0OOO00OO0O0OOOOO ={"site":OO00O00OOO0OOOO00 ,"crop_id":O0000OO000O0O0000 }#line:877
                                OOOOOO000000O00O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOOOO0000OOOOOO ,data =O0OOO00OO0O0OOOOO ).json ()#line:878
                                time .sleep (random .randint (1 ,3 )/10 )#line:880
                                if 'status'in OOOOOO000000O00O0 :#line:881
                                    if OOOOOO000000O00O0 ['status']==200 :#line:882
                                        if OOOOOO000000O00O0 ['message']=='种子数量不足':#line:883
                                            OOO0O00O0O00OOOOO =OOO00000OOOO000O0 .level_new ()#line:884
                                            print (f'【种植合成】:{OOOOOO000000O00O0["message"]}')#line:885
                                            if not OOO00000OOOO000O0 .user_ad ():#line:886
                                                return False #line:887
                                    if OOOOOO000000O00O0 ['status']==500 :#line:888
                                        print (f'【种植合成】:{OOOOOO000000O00O0["message"]}')#line:889
                                        return False #line:890
                            OO00O00OOO0OOOO00 +=1 #line:891
                        O00000O0O0O0O0OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0O0000OOOOO0 ).json ()#line:892
                        OO0OOOO0O0OOOOO00 =O00000O0O0O0O0OOO ['data']['cropList']#line:893
                        O0OOOOO0O00O0O0OO =False #line:894
                        for OO0O00O00OO0O0O00 in range (12 ):#line:895
                            id =OO0OOOO0O0OOOOO00 [OO0O00O00OO0O0O00 ]['level']#line:896
                            if float (OOO0O00O0O00OOOOO )-float (id )>9 :#line:897
                                O000OO000OO0OOOOO =f'_site={OO0O00O00OO0O0O00}_{timi_new()}'#line:898
                                OO00OOOO0OO0OO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00000OOOO000O0 .token ,'timestamp':timi_new (),'sign':sign (O000OO000OO0OOOOO ),'signstring':O000OO000OO0OOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:909
                                O00000O000O0O00OO ={"site":OO0O00O00OO0O0O00 }#line:910
                                OO0O0O00OO0OO0O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00OOOO0OO0OO0OO ,data =O00000O000O0O00OO ).json ()#line:912
                                if 'status'in OO0O0O00OO0OO0O00 :#line:913
                                    if OO0O0O00OO0OO0O00 ['status']==200 :#line:914
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:915
                            if id !=0 :#line:916
                                for O0O000000OOOO00O0 in range (11 ):#line:917
                                    O00O0O0OO00O0O0OO =O0O000000OOOO00O0 +1 #line:918
                                    g =OO0OOOO0O0OOOOO00 [O00O0O0OO00O0O0OO ]['level']#line:919
                                    if id ==g :#line:920
                                        O0OOO00OOOOOO00O0 =O0O000000OOOO00O0 +2 #line:921
                                        if O0OOO00OOOOOO00O0 !=OO0O00O00OO0O0O00 +1 :#line:922
                                            O0OO000OOO0OOOO00 =OO0O00O00OO0O0O00 +1 #line:923
                                            time .sleep (random .randint (1 ,3 )/10 )#line:925
                                            O0OOOO0O0O000O0OO =f'_site={O0OO000OOO0OOOO00 - 1}&targetSite={O0OOO00OOOOOO00O0 - 1}_{timi_new()}'#line:926
                                            OO00O00OO0OOO00OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00000OOOO000O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOO0O0O000O0OO ),'signstring':O0OOOO0O0O000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:943
                                            OOO00OO0O000OOOOO ={"site":int (O0OO000OOO0OOOO00 -1 ),"targetSite":int (O0OOO00OOOOOO00O0 -1 )}#line:944
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00O00OO0OOO00OO ,json =OOO00OO0O000OOOOO )#line:945
                                            O0OOOOO0O00O0O0OO =True #line:947
                                    if O0OOOOO0O00O0O0OO :#line:948
                                        break #line:949
                                if O0OOOOO0O00O0O0OO :#line:950
                                    break #line:951
        except :#line:952
            OOO00000OOOO000O0 .synthetic ()#line:953
    def level_new (O0O0000000O000OO0 ):#line:956
        try :#line:957
            OO00OO00O0000O000 =f'__{timi_new()}'#line:958
            O00O0OOO0OOO000O0 ={'source':'scsc','authorization':O0O0000000O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O0000O000 ),'signstring':OO00OO00O0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:969
            O00000O0O00O0O00O =requests .request ('get',f'{host}/user',headers =O00O0OOO0OOO000O0 ).json ()#line:970
            if 'status'in O00000O0O00O0O00O :#line:971
                if O00000O0O00O0O00O ['status']==200 :#line:972
                    return float (O00000O0O00O0O00O ['data']['level'])#line:973
        except Exception as O00O00O0O0O0000O0 :#line:974
            print (O00O00O0O0O0000O0 )#line:975
    def propsraffle (OO000OOOO0O00OO0O ):#line:978
        try :#line:979
            while True :#line:980
                O00O0O0OO0O00OOO0 =f'__{timi_new()}'#line:981
                O0OOOOOO0OOO000O0 ={'source':'scsc','authorization':OO000OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO0O00OOO0 ),'signstring':O00O0O0OO0O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:992
                OO0O0OOO0O00O000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OOOOOO0OOO000O0 ).json ()#line:993
                if 'status'in OO0O0OOO0O00O000O :#line:995
                    if OO0O0OOO0O00O000O ['status']==200 :#line:996
                        OO00OOO0OOO000O00 =OO0O0OOO0O00O000O ['data']['rows']#line:997
                        O0OOOOO0O00O00O0O =OO0O0OOO0O00O000O ['data']['vstate']#line:998
                        if OO00OOO0OOO000O00 ==5 or OO00OOO0OOO000O00 ==6 or OO00OOO0OOO000O00 ==7 :#line:999
                            OOOO00OOOOOOO0O0O =OO0O0OOO0O00O000O ['data']['silver']#line:1000
                            print (f'【转盘抽奖】:获得种子:{OOOO00OOOOOOO0O0O}')#line:1001
                        if OO00OOO0OOO000O00 ==1 or OO00OOO0OOO000O00 ==2 or OO00OOO0OOO000O00 ==3 :#line:1002
                            O0OOO0OOO0O000000 =OO0O0OOO0O00O000O ['data']['clover']#line:1003
                            print (f'【转盘抽奖】:获得三叶草:{O0OOO0OOO0O000000}')#line:1004
                        if OO00OOO0OOO000O00 ==4 or OO00OOO0OOO000O00 ==8 :#line:1005
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1006
                        if OO00OOO0OOO000O00 =='抽奖次数已用完':#line:1010
                            break #line:1044
                time .sleep (random .randint (8 ,15 )/10 )#line:1045
        except Exception as OO0OOO0000O0OOO0O :#line:1046
            print (OO0OOO0000O0OOO0O )#line:1047
    def friends_invitation (O0OO00O00OOOO00OO ):#line:1050
        try :#line:1051
            O00O00OO0O000OO00 =f'__{timi_new()}'#line:1052
            OOOOO000OO0O0O0OO ={'source':'scsc','authorization':O0OO00O00OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO0O000OO00 ),'signstring':O00O00OO0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1063
            O0OOO00O0O0OOO0OO =requests .request ('get',f'{host}/friends',headers =OOOOO000OO0O0O0OO ).json ()#line:1064
            if 'status'in O0OOO00O0O0OOO0OO :#line:1065
                if O0OOO00O0O0OOO0OO ['status']==200 :#line:1066
                    OOOO00OOO000OOO0O =O0OOO00O0O0OOO0OO ['data']['myInviteter']#line:1067
                    if OOOO00OOO000OOO0O :#line:1068
                        O00OOOOO0O0000OOO =OOOO00OOO000OOO0O ['user']['nickname']#line:1069
                        OO0OOOO000OO0OO00 =O0OO00O00OOOO00OO .certification ()#line:1070
                        if OO0OOOO000OO0OO00 =='未实名':#line:1071
                            weishim .append (O0OO00O00OOOO00OO .token )#line:1072
                        print (f'【查邀请人】:我的邀请人:{O00OOOOO0O0000OOO}丨实名:{OO0OOOO000OO0OO00}')#line:1073
        except Exception as OOO00OOOO0OO00OO0 :#line:1077
            print (OOO00OOOO0OO00OO0 )#line:1078
    def add_clover (O000000O00OOOO000 ):#line:1081
        global golden_seed #line:1082
        try :#line:1083
            OO0OO00O00OO000OO =f'__{timi_new()}'#line:1084
            O0000O0O00O0OO00O ={'source':'scsc','authorization':O000000O00OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O00OO000OO ),'signstring':OO0OO00O00OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1095
            OO00OO000OO0OO00O =requests .request ('get',f'{host}/assets/clovers',headers =O0000O0O00O0OO00O ).json ()#line:1096
            if 'status'in OO00OO000OO0OO00O :#line:1098
                if OO00OO000OO0OO00O ['status']==200 :#line:1099
                    O00O00OOO000000OO =OO00OO000OO0OO00O ['data']['clover']#line:1100
                    OOOO000O0O0OO0OO0 =OO00OO000OO0OO00O ['data']['used_clover']#line:1101
                    OO0O0O00000O0OOO0 =float (O00O00OOO000000OO )-float (OOOO000O0O0OO0OO0 )#line:1102
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOO000O0O0OO0OO0}')#line:1103
                    if O000000O00OOOO000 .certification ()!='未实名':#line:1104
                        if OO0O0O00000O0OOO0 >1 :#line:1105
                            OO0OO00O00OO000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0O00000O0OOO0)}_{timi_new()}'#line:1106
                            O0O000OOOO0OO0000 ={'source':'scsc','authorization':O000000O00OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O00OO000OO ),'signstring':OO0OO00O00OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1117
                            OO00OOOO0OOO00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0O00000O0OOO0 )}#line:1118
                            O0O00OO00OOOOOO0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O000OOOO0OO0000 ,data =OO00OOOO0OOO00O0O ).json ()#line:1119
                            if 'status'in O0O00OO00OOOOOO0O :#line:1121
                                if O0O00OO00OOOOOO0O ['status']==200 :#line:1122
                                    print (f'【参与抽奖】:添加☘️:{O0O00OO00OOOOOO0O["data"]["isSuccess"]}丨数量:{OO0O0O00000O0OOO0}')#line:1123
                                if O0O00OO00OOOOOO0O ['status']==500 :#line:1124
                                    print (f'【参与抽奖】:添加☘️:{O0O00OO00OOOOOO0O["message"]}')#line:1125
            O0O00O000OO0OO0OO =requests .request ('get',f'{host}/lottery',headers =O0000O0O00O0OO00O ).json ()#line:1126
            O0O0000O00O000O00 =O000000O00OOOO000 .winning_rewards ()#line:1128
            if 'status'in O0O00O000OO0OO0OO :#line:1129
                if O0O00O000OO0OO0OO ['status']==200 :#line:1130
                    OO0OOOO0O00OO0O00 =O0O00O000OO0OO0OO ['data'][0 ]['day_get_gold_quantity']#line:1131
                    golden_seed +=float (OO0OOOO0O00OO0O00 )#line:1132
                    O0OOOO00OOO00OOO0 =O0O00O000OO0OO0OO ['data'][1 ]['value']#line:1133
                    O000O0O000O0O0OO0 =O0O00O000OO0OO0OO ['data'][0 ]['join_number']#line:1134
                    O000OO00O0O0OO0OO =int (float (O0O00O000OO0OO0OO ['data'][0 ]['totalValue']))#line:1135
                    OOOOOOOO0OOO00O00 =float (O0OOOO00OOO00OOO0 /O000OO00O0O0OO0OO )*10000 #line:1136
                    OOOOOO00000000O0O =O000OO00O0O0OO0OO /O000O0O000O0O0OO0 #line:1137
                    print (f'【参与抽奖】:预计每天中{str(OO0OOOO0O00OO0O00)[:6]}颗金种子丨好友收益:{str(O0O0000O00O000O00)[:6]}')#line:1138
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOOOOO0OOO00O00)[:6]}颗金种子丨☘️人均:{str(OOOOOO00000000O0O)[:7]}️')#line:1139
        except Exception as O0OOO0O00OO000O00 :#line:1140
            print (O0OOO0O00OO000O00 )#line:1141
    def energy (O000O0OO0OO0OOO0O ):#line:1144
        try :#line:1145
            while True :#line:1146
                O0OO00O000OO00000 =f'__{timi_new()}'#line:1147
                O00O0OO0OOO000OO0 ={'source':'scsc','authorization':O000O0OO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O000OO00000 ),'signstring':O0OO00O000OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1158
                OO0O0000OO0OO0000 =requests .request ('get',f'{host}/energy/general',headers =O00O0OO0OOO000OO0 ).json ()#line:1159
                if 'status'in OO0O0000OO0OO0000 :#line:1161
                    if OO0O0000OO0OO0000 ['status']==200 :#line:1162
                        O0000OOOOOO0OOOOO =OO0O0000OO0OO0000 ['data']['ordinary_water']#line:1163
                        O00OO00OOOOO00OO0 =OO0O0000OO0OO0000 ['data']['ordinary_fertilizer']#line:1164
                        O00O0OO0OOOO0O0OO =OO0O0000OO0OO0000 ['data']['videoStatus']#line:1165
                        O00000O00OO00000O =OO0O0000OO0OO0000 ['data']['waterVideoKey']#line:1166
                        print (f'【我的营养】:肥料:{str(O00OO00OOOOO00OO0).split(".")[0]}丨水滴:{str(O0000OOOOOO0OOOOO).split(".")[0]}')#line:1168
                        if float (O00OO00OOOOO00OO0 )<96 :#line:1169
                            if O00O0OO0OOOO0O0OO :#line:1170
                                time .sleep (random .randint (160 ,180 )/10 )#line:1171
                                O0O000000000000OO =99 -float (O00OO00OOOOO00OO0 )#line:1172
                                O0O0O0O00O0O00O0O ={"fertilizer":str (O0O000000000000OO ).split ('.')[0 ]}#line:1173
                                OOO0O0OOO0OO0OOOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0OO0OOO000OO0 ).json ()#line:1175
                                if 'status'in OOO0O0OOO0OO0OOOO :#line:1177
                                    if OOO0O0OOO0OO0OOOO ['status']==200 :#line:1178
                                        print (f'【购买肥料】:看广告获取肥料:{OOO0O0OOO0OO0OOOO["message"]}')#line:1179
                                    if OOO0O0OOO0OO0OOOO ['status']==500 :#line:1180
                                        print (f'【购买肥料】:看广告获取肥料:{OOO0O0OOO0OO0OOOO["message"]}')#line:1181
                                        break #line:1182
                                if float (O00OO00OOOOO00OO0 )<78 :#line:1184
                                    O0O000000000000OO =80 -float (O00OO00OOOOO00OO0 )#line:1185
                                    OOOOOO0OOO00OOO00 =f'_fertilizer={int(O0O000000000000OO)}_{timi_new()}'#line:1186
                                    O0O0OOO0O00O000O0 ={'source':'scsc','authorization':O000O0OO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0OOO00OOO00 ),'signstring':OOOOOO0OOO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1197
                                    O0O0OO0OO0O000000 ={"fertilizer":int (O0O000000000000OO )}#line:1198
                                    OOO0OOOOO000000O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0OOO0O00O000O0 ,data =O0O0OO0OO0O000000 ).json ()#line:1200
                                    if 'status'in OOO0OOOOO000000O0 :#line:1202
                                        if OOO0OOOOO000000O0 ['status']==200 :#line:1203
                                            print (f'【购买肥料】:购买肥料:{OOO0OOOOO000000O0["message"]}丨数量:{int(O0O000000000000OO)}')#line:1204
                                        if OOO0OOOOO000000O0 ['status']==500 :#line:1205
                                            print (f'【购买肥料】:购买肥料:{OOO0OOOOO000000O0["message"]}丨数量:{int(O0O000000000000OO)}')#line:1206
                                            O00000O0OOOO0O000 =OOO0OOOOO000000O0 ["message"].split ('-')[1 ]#line:1207
                                            O00OO00O00O00OO0O =f'__{timi_new()}'#line:1208
                                            OOO0O0O0O0OOOO00O ={'source':'scsc','authorization':O000O0OO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O00O00OO0O ),'signstring':O00OO00O00O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                            OOO0OOO0O000O0OOO =requests .request ('get',f'{host}/user',headers =OOO0O0O0O0OOOO00O ).json ()#line:1220
                                            if 'status'in OOO0OOO0O000O0OOO :#line:1221
                                                if OOO0OOO0O000O0OOO ['status']==200 :#line:1222
                                                    O0O000OO0O000O000 =OOO0OOO0O000O0OOO ['data']['inner_id']#line:1223
                                                    if give_gold (O0O000OO0O000O000 ,float (O00000O0OOOO0O000 )+1 ):#line:1224
                                                        O000O0OO0OO0OOO0O .energy ()#line:1225
                        if float (O0000OOOOOO0OOOOO )<880 :#line:1226
                            if O00000O00OO00000O :#line:1227
                                time .sleep (random .randint (160 ,180 )/10 )#line:1228
                                O000OO0OOO0OO0OOO =999 -float (O0000OOOOOO0OOOOO )#line:1229
                                OO0O000O0OO0O00O0 ={"water":str (O000OO0OOO0OO0OOO ).split ('.')[0 ]}#line:1230
                                O00OOOOOO000O0OO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0OO0OOO000OO0 ).json ()#line:1232
                                if 'status'in O00OOOOOO000O0OO0 :#line:1234
                                    if O00OOOOOO000O0OO0 ['status']==200 :#line:1235
                                        print (f'【购买水滴】:看广告获取水滴:{O00OOOOOO000O0OO0["message"]}')#line:1236
                                    if O00OOOOOO000O0OO0 ['status']==500 :#line:1237
                                        print (f'【购买水滴】:看广告获取水滴:{O00OOOOOO000O0OO0["message"]}')#line:1238
                                        break #line:1239
                                if float (O0000OOOOOO0OOOOO )<780 :#line:1240
                                    O000OO0OOO0OO0OOO =800 -float (O0000OOOOOO0OOOOO )#line:1241
                                    O00OOO0OOOO00OOOO =f'_water={int(O000OO0OOO0OO0OOO)}_{timi_new()}'#line:1242
                                    O0O0OOOOOOOOO00OO ={'source':'scsc','authorization':O000O0OO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOO00OOOO ),'signstring':O00OOO0OOOO00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1253
                                    O00O0O000O00O00OO ={"water":int (O000OO0OOO0OO0OOO )}#line:1254
                                    O00OO0OOOOO0000O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0OOOOOOOOO00OO ,data =O00O0O000O00O00OO ).json ()#line:1256
                                    if 'status'in O00OO0OOOOO0000O0 :#line:1258
                                        if O00OO0OOOOO0000O0 ['status']==200 :#line:1259
                                            print (f'【购买水滴】:购买水滴:{O00OO0OOOOO0000O0["message"]}丨数量:{int(O000OO0OOO0OO0OOO)}')#line:1260
                                        if O00OO0OOOOO0000O0 ['status']==500 :#line:1261
                                            print (f'【购买水滴】:购买水滴:{O00OO0OOOOO0000O0["message"]}丨数量:{int(O000OO0OOO0OO0OOO)}')#line:1262
                                            O00000O0OOOO0O000 =O00OO0OOOOO0000O0 ["message"].split ('-')[1 ]#line:1263
                                            O00OO00O00O00OO0O =f'__{timi_new()}'#line:1264
                                            OOO0O0O0O0OOOO00O ={'source':'scsc','authorization':O000O0OO0OO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O00O00OO0O ),'signstring':O00OO00O00O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1275
                                            OOO0OOO0O000O0OOO =requests .request ('get',f'{host}/user',headers =OOO0O0O0O0OOOO00O ).json ()#line:1276
                                            if 'status'in OOO0OOO0O000O0OOO :#line:1277
                                                if OOO0OOO0O000O0OOO ['status']==200 :#line:1278
                                                    O0O000OO0O000O000 =OOO0OOO0O000O0OOO ['data']['inner_id']#line:1279
                                                    if give_gold (O0O000OO0O000O000 ,float (O00000O0OOOO0O000 )+1 ):#line:1280
                                                        O000O0OO0OO0OOO0O .energy ()#line:1281
                        break #line:1282
        except Exception as O0O0000O000000OOO :#line:1283
            print (O0O0000O000000OOO )#line:1284
def bundled_def ():#line:1287
    OO0OO00OO0O00OOO0 =['5570536','7750212','7911652','7911680','7805624']#line:1288
    return OO0OO00OO0O00OOO0 [random .randint (0 ,len (OO0OO00OO0O00OOO0 )-1 )]#line:1289
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
        O000OOO0OOOO00OO0 =gitee_edition ()#line:1328
        if version_of_the_validation ()<O000OOO0OOOO00OO0 ['CityEarth']['edition']:#line:1329
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO0OOOO00OO0["CityEarth"]["edition"]}   ❌')#line:1330
            print (f'更新内容=>>{O000OOO0OOOO00OO0["CityEarth"]["content"]}')#line:1331
        else :#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOO0OOOO00OO0["CityEarth"]["edition"]}   ✅')#line:1333
            print (f'更新内容=>> {O000OOO0OOOO00OO0["CityEarth"]["content"]}')#line:1334
    except Exception as O0O00O0OO0O0000OO :#line:1335
        print (O0O00O0OO0O0000OO )#line:1336
def sc3 ():#line:1339
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1340
if __name__ =='__main__':#line:1343
    start ()#line:1344
