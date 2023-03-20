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
@ 版本  4.8
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
        O000O0O00OO000O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O000O0O00OO000O0O)}个账号==========")#line:17
        for OOOO0O0OOOO00OOO0 in O000O0O00OO000O0O :#line:18
            OO0O000OO0O000OOO =[]#line:19
            print (f"------------正在执行第{O000O0O00OO000O0O.index(OOOO0O0OOOO00OOO0) + 1}个账号------------")#line:20
            OOO0OOOO000O0OOOO =CityEarth (OOOO0O0OOOO00OOO0 ,OO0O000OO0O000OOO ,O000O0O00OO000O0O .index (OOOO0O0OOOO00OOO0 ))#line:21
            def O0OO00O0O0O00O0O0 ():#line:23
                if OOO0OOOO000O0OOOO .base_info ():#line:25
                    OOO0OOOO000O0OOOO .sealing ()#line:27
                    OOO0OOOO000O0OOOO .invitenum ()#line:29
                    OOO0OOOO000O0OOOO .query_to_sell ()#line:31
                    OOO0OOOO000O0OOOO .friends_invitation ()#line:35
                    OOO0OOOO000O0OOOO .energy ()#line:37
                    OOO0OOOO000O0OOOO .add_clover ()#line:39
                    OOO0OOOO000O0OOOO .propsraffle ()#line:41
                    OOO0OOOO000O0OOOO .synthetic ()#line:43
                    OOO0OOOO000O0OOOO .crops_illustrated ()#line:45
                    OOO0OOOO000O0OOOO .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO0OOOO000O0OOOO .give_gold ()#line:50
            OO0000OOO0O0O0O0O =threading .Thread (target =O0OO00O0O0O00O0O0 )#line:52
            OO0000OOO0O0O0O0O .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0O0O00O00O000OO0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0O00O00O000OO0 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OOOO0O000O00O0000 in invited_new :#line:62
            print (OOOO0O000O00O0000 )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0OO00000OO00000 in weishim :#line:65
            print (OO0OO00000OO00000 )#line:66
    except Exception as O0O0000OOO0OO0000 :#line:67
        print (O0O0000OOO0OO0000 )#line:68
def give_gold (O00O0O00O00OOO0OO ,O000OOOOOOOO000O0 ):#line:72
    try :#line:73
        OOO0O0000O0O0O0O0 =f'_doneeNo={O00O0O00O00OOO0OO}&quantity={int(O000OOOOOOOO000O0)}_{timi_new()}'#line:74
        O0OO00OO00O0OOOOO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOO0O0000O0O0O0O0 ),'signstring':OOO0O0000O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O00OO0O0OO0O0OO00 ={"quantity":int (O000OOOOOOOO000O0 ),"doneeNo":O00O0O00O00OOO0OO }#line:89
        O00O0OO00O0OO00OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO00OO00O0OOOOO ,data =O00OO0O0OO0O0OO00 ).json ()#line:90
        if 'status'in O00O0OO00O0OO00OO :#line:92
            if O00O0OO00O0OO00OO ['status']==200 :#line:93
                if O00O0OO00O0OO00OO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O000OOOOOOOO000O0)}种子给{O00O0O00O00OOO0OO}成功')#line:95
                    return True #line:96
            if O00O0OO00O0OO00OO ['status']==401 :#line:97
                print (f'【赠送种子】:{O00O0OO00O0OO00OO["message"]}')#line:98
                return False #line:99
            if O00O0OO00O0OO00OO ['status']==500 :#line:100
                print (f'【赠送种子】:{O00O0OO00O0OO00OO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0OOO000O0O0OO000 :#line:104
        print (O0OOO000O0O0OO000 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OOO0OO00OO000O0 ):#line:115
    O00O0O0O000OOOOO0 =hashlib .md5 (O0OOO0OO00OO000O0 .encode ()).hexdigest ()#line:116
    OO00O000OO0OOOOOO =sc1 ()#line:117
    OO00O000O00O00OOO =sc2 ()#line:118
    O0OOO00O00O0OOO0O =sc3 ()#line:119
    O00000OO00O00OO00 =OO00O000OO0OOOOOO +O00O0O0O000OOOOO0 +OO00O000O00O00OOO +O0OOO00O00O0OOO0O #line:120
    OOOOOO0O00OOOOO00 =hashlib .md5 (O00000OO00O00OO00 .encode ()).hexdigest ()#line:121
    return OOOOOO0O00OOOOO00 #line:122
def format_msg ():#line:125
    OOO0O0OO0O0O0OO0O =""#line:126
    for O0OOO0O0OOOOOOOO0 in msg_list :#line:127
        OOO0O0OO0O0O0OO0O +=str (O0OOO0O0OOOOOOOO0 )+"\r\n"#line:128
    return OOO0O0OO0O0O0OO0O #line:129
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
def get_json_data (OOOO00OOOO0O00000 ,O00000O0OOO00O00O ,O00OOOO0OOO000O0O ,OO0000OOO0O0OO0OO ):#line:153
    with open (OOOO00OOOO0O00000 ,'rb')as OOO00OOO00O00O00O :#line:154
        O00O0OOOO0000OOOO =json .load (OOO00OOO00O00O00O )#line:155
        O00O0OOOO0000OOOO ['data'][O00000O0OOO00O00O ][O00OOOO0OOO000O0O ]=OO0000OOO0O0OO0OO #line:156
        OOO0O0OO0OO0OO0O0 =O00O0OOOO0000OOOO #line:157
    OOO00OOO00O00O00O .close ()#line:158
    return OOO0O0OO0OO0OO0O0 #line:159
def write_json_data (OOO00OOO0OO00OO0O ):#line:162
    with open (json_path1 ,'w')as O0OOOOO0OO0OOO0O0 :#line:163
        json .dump (OOO00OOO0OO00OO0O ,O0OOOOO0OO0OOO0O0 ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O0OOOOO0OO0OOO0O0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO0000OOO00OOOOOO ,OOO00OOOOOO000O00 ,OOO0O0OOOO00OO0OO ,O0O0OOO0OO0000OO0 ):#line:171
        try :#line:172
            OO0000OOO00OOOOOO .msg =OOO0O0OOOO00OO0OO #line:173
            OO0000OOO00OOOOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO0000OOO00OOOOOO .token =OOO00OOOOOO000O00 ['authorization']#line:175
            OO0000OOO00OOOOOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO0000OOO00OOOOOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO0000OOO00OOOOOO .elephant_user =OOO00OOOOOO000O00 ['elephant_user']#line:178
            OO0000OOO00OOOOOO .elephant_pswd =OOO00OOOOOO000O00 ['elephant_pswd']#line:179
            OO0000OOO00OOOOOO .elephant_Task_ID =OOO00OOOOOO000O00 ['elephant_Task_ID']#line:180
            OO0000OOO00OOOOOO .len_new =O0O0OOO0OO0000OO0 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO00O0OO0OOO0O0OO ):#line:186
        try :#line:187
            OO00O0OO0OOO0O0OO .watched_ad ()#line:189
            OOOO000OO0000OO00 =f'__{timi_new()}'#line:190
            OOOOOOO00OO000O00 ={'source':'scsc','authorization':OO00O0OO0OOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OO0000OO00 ),'signstring':OOOO000OO0000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0OOO00OO000O0OOO =requests .request ('get',f'{host}/user',headers =OOOOOOO00OO000O00 ).json ()#line:202
            if 'status'in O0OOO00OO000O0OOO :#line:204
                if O0OOO00OO000O0OOO ['status']==200 :#line:205
                    OOO0O0O0OO0O0000O =O0OOO00OO000O0OOO ['data']['nickname']#line:206
                    O000OOOOOO00OOO00 =O0OOO00OO000O0OOO ['data']['inner_id']#line:207
                    O0OOOOO0OO0O00OO0 =O0OOO00OO000O0OOO ['data']['assets']['gold']#line:208
                    O0OOO0O0OO0OOO00O =O0OOO00OO000O0OOO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOO0O0O0OO0O0000O[:5]}丨ID:{O000OOOOOO00OOO00}丨等级:{O0OOO0O0OO0OOO00O}丨金种子:{str(O0OOOOO0OO0O00OO0).split(".")[0]}')#line:211
                    if 'wx_'in OOO0O0O0OO0O0000O :#line:212
                        OO00O0OO0OOO0O0OO .change_nickname ()#line:213
                if O0OOO00OO000O0OOO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO00O0OO0OOO0O0OO .elephant_user =='f':#line:216
                        return False #line:217
                    O00O0000OO0000O0O =Invalid_login .addtask (elephant_user =OO00O0OO0OOO0O0OO .elephant_user ,elephant_pswd =OO00O0OO0OOO0O0OO .elephant_pswd ,elephant_Task_ID =OO00O0OO0OOO0O0OO .elephant_Task_ID )#line:220
                    OO00O00O0000O00O0 =get_json_data (json_path ,OO00O0OO0OOO0O0OO .len_new ,'authorization',O00O0000OO0000O0O )#line:221
                    if write_json_data (OO00O00O0000O00O0 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0OOO00OO000O0OOO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O000O00O0OO0OOOOO :#line:228
            print (O000O00O0OO0OOOOO )#line:229
    def sealing (OOO0O00OO0OO0OOOO ):#line:232
        try :#line:233
            OOO00OOO000OO0OO0 =f'__{timi_new()}'#line:234
            OO0O0OOOO0OO000O0 ={'source':'scsc','authorization':OOO0O00OO0OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO000OO0OO0 ),'signstring':OOO00OOO000OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O0OOOO0OO000O0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO0O0OOOO0OO000O0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O0OOOO0OO000O0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O0OOOO0OO000O0 )#line:249
            requests .request ('get',f'{host}/user',headers =OO0O0OOOO0OO000O0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O0OOOO0OO000O0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O0OOOO0OO000O0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O0OOOO0OO000O0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O0OOOO0OO000O0 )#line:254
            requests .request ('get',f'{host}/assets',headers =OO0O0OOOO0OO000O0 )#line:255
        except Exception as O0OOOO0OO00OOO000 :#line:256
            print (O0OOOO0OO00OOO000 )#line:257
    def ddd (O0O0O00O0O00O0O00 ):#line:259
        try :#line:260
            O000OOOO0OO00O000 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OOO00O0O0OO0OO0OO ={'source':'scsc','authorization':O0O0O00O0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO0OO00O000 ),'signstring':O000OOOO0OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO0OO0O0O000000O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO00O0O0OO0OO0OO ).json ()#line:273
            print (OOO0OO0O0O000000O )#line:274
        except Exception as O00O0O0O0O0O0O00O :#line:277
            print (O00O0O0O0O0O0O00O )#line:278
    def the_query (O000O00OOOO0O000O ):#line:283
        try :#line:284
            OOOO0OOOO0O0OOOO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OO00OO00OOOO00OO0 ={'authorization':O000O00OOOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0O0OOOO0 ),'signstring':OOOO0OOOO0O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO0O0OOO0O00OOO00 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00OO00OOOO00OO0 ).json ()#line:296
            if 'status'in OO0O0OOO0O00OOO00 :#line:298
                if OO0O0OOO0O00OOO00 ['status']==200 :#line:299
                    return OO0O0OOO0O00OOO00 ['data']['rows'][4 ]['price']#line:300
        except Exception as OO0OOO0OOO0O00OO0 :#line:301
            print (OO0OOO0OOO0O00OO0 )#line:302
    def market_sale (OOOO000000O0OOO0O ,O0O0OOOOOO00O0000 ):#line:305
        try :#line:306
            O0OO00OO0OOOOO00O =timi_new ()#line:307
            OOO0O0O00OO00OO00 =f'type=crop__{O0OO00OO0OOOOO00O}'#line:308
            O00OO000O0OO000OO ={'source':'scsc','authorization':OOOO000000O0OOO0O .token ,'timestamp':str (O0OO00OO0OOOOO00O ),'sign':sign (OOO0O0O00OO00OO00 ),'signstring':OOO0O0O00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0O00O000OOOOO0O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00OO000O0OO000OO ).json ()#line:320
            if 'status'in O0O00O000OOOOO0O0 :#line:322
                if O0O00O000OOOOO0O0 ['status']==200 :#line:323
                    if O0O00O000OOOOO0O0 ['data']['rows']:#line:324
                        O0O0OO0000OOO00OO =O0O00O000OOOOO0O0 ['data']['rows'][0 ]['packsackItemId']#line:325
                        O0O00OO0OO0000OO0 =O0O00O000OOOOO0O0 ['data']['rows'][0 ]['quantity']#line:326
                        O0OO0O0OOO000OOO0 =float (O0O0OOOOOO00O0000 )-float (random .randint (1 ,9 )*0.001 )#line:327
                        if float (O0O0OOOOOO00O0000 )>6 :#line:328
                            OO0OO0O0O0O00OO0O =f'_packsackItemId={O0O0OO0000OOO00OO}&price={str(O0OO0O0OOO000OOO0)[:5]}&quantity={O0O00OO0OO0000OO0}_{O0OO00OO0OOOOO00O}'#line:329
                            OO0OO0000O00O00O0 ={'source':'scsc','authorization':OOOO000000O0OOO0O .token ,'timestamp':str (O0OO00OO0OOOOO00O ),'sign':sign (OO0OO0O0O0O00OO0O ),'signstring':OO0OO0O0O0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
                            O0OO0OO00OOO0000O ={"packsackItemId":O0O0OO0000OOO00OO ,"price":str (O0OO0O0OOO000OOO0 )[:5 ],"quantity":str (O0O00OO0OO0000OO0 )}#line:345
                            O00O0O00O0O000000 =requests .request ('post',f'{host}/market/sale',headers =OO0OO0000O00O00O0 ,data =O0OO0OO00OOO0000O ).json ()#line:346
                            if 'status'in O00O0O00O0O000000 :#line:348
                                if O00O0O00O0O000000 ['status']==200 :#line:349
                                    print (f'【上架芦荟】:数量:{O0O00OO0OO0000OO0}丨价格:{str(O0OO0O0OOO000OOO0)[:5]}')#line:350
                                if O00O0O00O0O000000 ['status']==500 :#line:351
                                    print (f'【上架芦荟】:{O00O0O00O0O000000["message"]}')#line:352
        except Exception as OOOO0O000OO0OOOOO :#line:353
            print (OOOO0O000OO0OOOOO )#line:354
    def query_to_sell (OO0OOO0O000O0OO0O ):#line:357
        global count_list #line:358
        try :#line:359
            O0OO0OO0OO00000O0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:360
            OO0O0OOOO0O00OO0O ={'source':'scsc','authorization':OO0OOO0O000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OO00000O0 ),'signstring':O0OO0OO0OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:371
            OO0O00O0OO000OO0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0O0OOOO0O00OO0O ).json ()#line:372
            if 'status'in OO0O00O0OO000OO0O :#line:374
                if OO0O00O0OO000OO0O ['status']==200 :#line:375
                    for O00O00OOOO0O0O0O0 in OO0O00O0OO000OO0O ['data']['rows']:#line:376
                        O0O0OO0OO00OOO0OO =O00O00OOOO0O0O0O0 ['materialKey']#line:377
                        OO000000OOO00OOOO =O00O00OOOO0O0O0O0 ['quantity']#line:378
                        O0OO000O00OOO0O00 =O00O00OOOO0O0O0O0 ['price']#line:379
                        O00000OOOOO0OO000 =O00O00OOOO0O0O0O0 ['saleState']#line:380
                        if O00000OOOOO0OO000 ==0 :#line:381
                            print (f'【出售订单】:名称:{O0O0OO0OO00OOO0OO}丨数量:{OO000000OOO00OOOO}丨价格:{O0OO000O00OOO0O00}')#line:382
                            count_list +=OO000000OOO00OOOO #line:383
                            OO00OO0O0OOO0O0O0 =OO0OOO0O000O0OO0O .the_query ()#line:385
                            if float (OO00OO0O0OOO0O0O0 )!=float (O0OO000O00OOO0O00 ):#line:386
                                OOOOO000OO0000OOO =O00O00OOOO0O0O0O0 ['id']#line:387
                                OO0OOO0O000O0OO0O .cacel_sale (OOOOO000OO0000OOO )#line:388
                    OO0OOO0O000O0OO0O .game_map ()#line:390
        except Exception as O0O0OOOO0OOOO00O0 :#line:392
            print (O0O0OOOO0OOOO00O0 )#line:393
    def cacel_sale (OO0OOOOOO0O00OO0O ,O00000OOOO0000OO0 ):#line:396
        try :#line:397
            O0OOOO0OOO0OO0000 =f'_saleId={O00000OOOO0000OO0}_{timi_new()}'#line:398
            OOO0OO0O0OOOO00O0 ={'source':'scsc','authorization':OO0OOOOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOO0OO0000 ),'signstring':O0OOOO0OOO0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            OOO00OOO0OO00O00O ={"saleId":O00000OOOO0000OO0 }#line:410
            O000OO00OOO0OOO00 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO0OO0O0OOOO00O0 ,data =OOO00OOO0OO00O00O ).json ()#line:411
            if 'status'in O000OO00OOO0OOO00 :#line:413
                if O000OO00OOO0OOO00 ['status']==200 :#line:414
                    print (f'【下架出售】:{O000OO00OOO0OOO00["data"]}')#line:415
        except Exception as OOO0O00O0O0O0OOO0 :#line:416
            print (OOO0O00O0O0O0OOO0 )#line:417
    def change_nickname (O0000000OO0O0O000 ):#line:420
        try :#line:421
            OOOO00OOOOOO0O000 =timi_new ()#line:422
            O00O0O00O0OO0OO0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:423
            O0OOO0OOOO0OO000O =requests .request ('post','https://www.qmsjmfb.com/',data =O00O0O00O0OO0OO0O ).text #line:424
            O00O0OOO00OOO0000 =re .findall ('<ul><li>(.*?)</li>',O0OOO0OOOO0OO000O )[0 ][:3 ]#line:425
            O0O00O0O0O0000OOO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00O0OOO00OOO0000}').json ()#line:426
            OO0O00000OOOOOOOO =O0O00O0O0O0000OOO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:427
            O00OOOO00000OO000 ={"nickname":OO0O00000OOOOOOOO }#line:428
            O00OO0O0O0O0O000O =f'_nickname={OO0O00000OOOOOOOO}_{OOOO00OOOOOO0O000}'#line:429
            O0O000000000O000O ={'source':'scsc','authorization':O0000000OO0O0O000 .token ,'timestamp':OOOO00OOOOOO0O000 ,'sign':sign (O00OO0O0O0O0O000O ),'signstring':O00OO0O0O0O0O000O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:440
            O0000O00O00OOOO00 =requests .request ('patch',f'{host}/user/nickname',headers =O0O000000000O000O ,data =O00OOOO00000OO000 ).json ()#line:441
            if 'status'in O0000O00O00OOOO00 :#line:443
                if O0000O00O00OOOO00 ['status']==200 :#line:444
                    print (f'【修改网名】:网名:{OO0O00000OOOOOOOO}丨{O0000O00O00OOOO00["message"]}')#line:445
        except Exception as O00OO0OOO00O0O0OO :#line:446
            print (O00OO0OOO00O0O0OO )#line:447
    def withdraw (OOO0000OO0O0OO000 ):#line:450
        try :#line:451
            O0O000000OO0000O0 =f'__{timi_new()}'#line:452
            OOO0OO0OO0OO0OO00 ={'source':'scsc','authorization':OOO0000OO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000OO0000O0 ),'signstring':O0O000000OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O0O0OO00O000O0O0O =requests .request ('get',f'{host}/assets',headers =OOO0OO0OO0OO0OO00 ).json ()#line:464
            if 'status'in O0O0OO00O000O0O0O :#line:466
                if O0O0OO00O000O0O0O ['status']==200 :#line:467
                    O0OO0OO0O0O00O000 =O0O0OO00O000O0O0O ['data']['cash']#line:468
                    if float (O0OO0OO0O0O00O000 )>20 :#line:469
                        O0O000000OO0000O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:470
                        OOO0OO0OO0OO0OO00 ={'authorization':OOO0000OO0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000OO0000O0 ),'signstring':O0O000000OO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
                        OO0O00OOOO0000000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:481
                        O0OO0O00O000O0OO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0OO0OO0OO0OO00 ,data =OO0O00OOOO0000000 ).json ()#line:483
                        if 'status'in O0OO0O00O000O0OO0 :#line:485
                            if O0OO0O00O000O0OO0 ['status']==200 :#line:486
                                print (f'【余额提现】:{O0OO0O00O000O0OO0["data"]}')#line:487
                        if 'status'in O0OO0O00O000O0OO0 :#line:488
                            if O0OO0O00O000O0OO0 ['status']==500 :#line:489
                                print (f'【余额提现】:{O0OO0O00O000O0OO0["message"]}')#line:490
        except Exception as O0OO0OOO0000O0OOO :#line:491
            print (O0OO0OOO0000O0OOO )#line:492
    def invitenum (OOOO0OOO0OO000O00 ):#line:495
        global invited_new #line:496
        try :#line:497
            O0O0O0000O00000O0 =f'__{timi_new()}'#line:498
            OOOO0OOO0OO0OO00O ={'source':'scsc','authorization':OOOO0OOO0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000O00000O0 ),'signstring':O0O0O0000O00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:509
            O00OO000OOOO0O00O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0OOO0OO0OO00O ).json ()#line:510
            if 'status'in O00OO000OOOO0O00O :#line:512
                if O00OO000OOOO0O00O ['status']==200 :#line:513
                    O0O00OO0O00000000 =O00OO000OOOO0O00O ['data']['invited_count']#line:514
                    OO0O000OO0O000OO0 =O00OO000OOOO0O00O ['data']['invited_second_count']#line:515
                    print (f'【我的邀请】:直邀好友:{O0O00OO0O00000000}丨间邀好友:{OO0O000OO0O000OO0}')#line:516
                    if O0O00OO0O00000000 <2 :#line:517
                        O00O0OOOO0O00O0OO =f'__{timi_new()}'#line:518
                        O00000O0O00O0OO00 ={'source':'scsc','authorization':OOOO0OOO0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOO0O00O0OO ),'signstring':O00O0OOOO0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                        OOO00OOO0OOOOO0O0 =requests .request ('get',f'{host}/user',headers =O00000O0O00O0OO00 ).json ()#line:530
                        if 'status'in OOO00OOO0OOOOO0O0 :#line:532
                            if OOO00OOO0OOOOO0O0 ['status']==200 :#line:533
                                invited_new .append (OOO00OOO0OOOOO0O0 ['data']['inner_id'])#line:534
        except Exception as O0O00OOOOO0OOO00O :#line:535
            print (O0O00OOOOO0OOO00O )#line:536
    def game_map (OO00O000OOOO00OOO ):#line:539
        try :#line:540
            O0OO0OO0OOOOOOO00 =f'__{timi_new()}'#line:541
            O00000O0OO000OO00 ={'source':'scsc','authorization':OO00O000OOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OOOOOOO00 ),'signstring':O0OO0OO0OOOOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            OOOO0O0OOO000000O =requests .request ('get',f'{host}/game/map',headers =O00000O0OO000OO00 ).json ()#line:553
            if 'status'in OOOO0O0OOO000000O :#line:555
                if OOOO0O0OOO000000O ['status']==200 :#line:556
                    for OOOO0OO00OO00OOO0 in OOOO0O0OOO000000O ['data']['list'][0 ]['crops']:#line:557
                        OO000OOO00O000O00 =OOOO0OO00OO00OOO0 ['level']#line:559
                        if OO000OOO00O000O00 ==41 :#line:560
                            O000O00O0O00O0OOO =OOOO0OO00OO00OOO0 ['crop_name']#line:561
                            OOOOOOO000O00OO0O =OOOO0OO00OO00OOO0 ['count']#line:562
                            if OOOOOOO000O00OO0O >0 :#line:563
                                print (f'【农业资产】:{O000O00O0O00O0OOO}丨数量:{OOOOOOO000O00OO0O}')#line:564
                                O000OOO000000OOO0 =OO00O000OOOO00OOO .the_query ()#line:565
                                OO00O000OOOO00OOO .market_sale (O000OOO000000OOO0 )#line:566
        except Exception as O00000OOO0OO00OO0 :#line:567
            print (O00000OOO0OO00OO0 )#line:568
    def give_gold (OO0000O0O0O0O000O ):#line:571
        try :#line:572
            OO0OOOOO0O0000O0O =f'__{timi_new()}'#line:573
            OO000O0O000OOOO00 ={'source':'scsc','authorization':OO0000O0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0O0000O0O ),'signstring':OO0OOOOO0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
            OOO000OOOO0O0O00O =requests .request ('get',f'{host}/user',headers =OO000O0O000OOOO00 ).json ()#line:585
            if 'status'in OOO000OOOO0O0O00O :#line:586
                if OOO000OOOO0O0O00O ['status']==200 :#line:587
                    if float (OO0000O0O0O0O000O .doneeNo )!=0 :#line:588
                        O0O0OO0O00OO0000O =OOO000OOOO0O0O00O ['data']['assets']['gold']#line:589
                        if float (O0O0OO0O00OO0000O )>float (OO0000O0O0O0O000O .innerId ):#line:590
                            OO0O0OO000OO00O0O =int (float (O0O0OO0O00OO0000O )/1.1 )#line:591
                            OO0OOOOO0O0000O0O =f'_doneeNo={OO0000O0O0O0O000O.doneeNo}&quantity={OO0O0OO000OO00O0O}_{timi_new()}'#line:592
                            OO000O0O000OOOO00 ={'source':'scsc','authorization':OO0000O0O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0O0000O0O ),'signstring':OO0OOOOO0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:603
                            OOO0O00O00000O00O ={"quantity":OO0O0OO000OO00O0O ,"doneeNo":OO0000O0O0O0O000O .doneeNo }#line:607
                            O000000O00OO0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO000O0O000OOOO00 ,data =OOO0O00O00000O00O ).json ()#line:608
                            if 'status'in O000000O00OO0O000 :#line:610
                                if O000000O00OO0O000 ['status']==200 :#line:611
                                    if O000000O00OO0O000 ['data']:#line:612
                                        print (f'【赠送种子】:赠送{OO0O0OO000OO00O0O}种子给{OO0000O0O0O0O000O.doneeNo}成功')#line:613
                    else :#line:614
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:615
        except Exception as O0OOO00O0O00OO0OO :#line:616
            print (O0OOO00O0O00OO0OO )#line:617
    def invitation (OO0O0O000OO00OOOO ):#line:619
        try :#line:620
            _OO0O0O0000OOOOO0O =float (bundled_def ())/4 #line:621
            OO0O00O00OO00O000 =f'_innerId={int(_OO0O0O0000OOOOO0O)}_{timi_new()}'#line:623
            O0O0OOOO0OO0O0000 ={'source':'scsc','authorization':OO0O0O000OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OO00O000 ),'signstring':OO0O00O00OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OOOOO0OO000OO0O0O ={"innerId":int (_OO0O0O0000OOOOO0O )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OOOO0OO0O0000 ,data =OOOOO0OO000OO0O0O )#line:636
        except Exception as O0O00OOOOO00OO00O :#line:637
            print (O0O00OOOOO00OO00O )#line:638
    def winning_rewards (OO0OO00O0OO00000O ):#line:641
        try :#line:642
            OO000O0OOO0OOO0O0 =f'__{timi_new()}'#line:643
            OO00O00000000000O ={'source':'scsc','authorization':OO0OO00O0OO00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OOO0OOO0O0 ),'signstring':OO000O0OOO0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            OOOOOOO00OO0O0OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00O00000000000O ).json ()#line:655
            if 'status'in OOOOOOO00OO0O0OO0 :#line:657
                if OOOOOOO00OO0O0OO0 ['status']==200 :#line:658
                    if OOOOOOO00OO0O0OO0 ['data']['amount']:#line:659
                        OOO0OOOO00OO000O0 =OOOOOOO00OO0O0OO0 ['data']['amount']['gold']#line:660
                        return OOO0OOOO00OO000O0 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as O0OO00OO00OOOOO00 :#line:664
            print (O0OO00OO00OOOOO00 )#line:665
    def certification (O0OOOOOOOOOOO0OOO ):#line:668
        try :#line:669
            O0O0O000OOOO0000O =f'__{timi_new()}'#line:670
            OOO00O000O0O00OOO ={'source':'scsc','authorization':O0OOOOOOOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000OOOO0000O ),'signstring':O0O0O000OOOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            OO000OOO000OO0OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO00O000O0O00OOO ).json ()#line:682
            if 'status'in OO000OOO000OO0OOO :#line:684
                if OO000OOO000OO0OOO ['status']==200 :#line:685
                    if OO000OOO000OO0OOO ['data']['result']:#line:686
                        O0OO0O0OOO0000O00 =OO000OOO000OO0OOO ['data']['nick_name']#line:687
                        return O0OO0O0OOO0000O00 #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as O0OOO0OO000000O00 :#line:691
            print (O0OOO0OO000000O00 )#line:692
    def crops_illustrated (OO00OOO00O0O000OO ):#line:695
        try :#line:696
            OO0O000000O00O000 =f'__{timi_new()}'#line:697
            OO0O00OO0O0O00O0O ={'source':'scsc','authorization':OO00OOO00O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000000O00O000 ),'signstring':OO0O000000O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            O0000O0O00OO00OO0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00OO0O0O00O0O ).json ()#line:709
            if 'status'in O0000O0O00OO00OO0 :#line:711
                if O0000O0O00OO00OO0 ['status']==200 :#line:712
                    OOOOOOO0O0OO000O0 =O0000O0O00OO00OO0 ['data'][0 ]['crops']#line:713
                    for OO0OOOO00OO0O00O0 in OOOOOOO0O0OO000O0 :#line:714
                        if OO0OOOO00OO0O00O0 ['ill_clover_award']:#line:715
                            if float (OO0OOOO00OO0O00O0 ['ill_clover_award'])>1 :#line:716
                                if OO0OOOO00OO0O00O0 ['is_finish']:#line:717
                                    if not OO0OOOO00OO0O00O0 ['is_getit']:#line:718
                                        if OO00OOO00O0O000OO .certification ()!='未实名':#line:719
                                            OO0O000000O00O000 =f'_award_level={OO0OOOO00OO0O00O0["level"]}_{timi_new()}'#line:720
                                            OO0O00OO0O0O00O0O ={'source':'scsc','authorization':OO00OOO00O0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000000O00O000 ),'signstring':OO0O000000O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            OO00OOOOOOO000000 ={"award_level":OO0OOOO00OO0O00O0 ['level']}#line:732
                                            OOO000OO00OOOOOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00OO0O0O00O0O ,json =OO00OOOOOOO000000 ).json ()#line:734
                                            if 'status'in OOO000OO00OOOOOOO :#line:735
                                                if OOO000OO00OOOOOOO ['status']==200 :#line:736
                                                    OO00O000O0OO0000O =OOO000OO00OOOOOOO ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{OO0OOOO00OO0O00O0["crop_name"]}成就丨奖励{OO00O000O0OO0000O}☘️')#line:739
                                                if OOO000OO00OOOOOOO ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{OOO000OO00OOOOOOO["message"]}')#line:741
        except Exception as OO00OO00OOOO00O00 :#line:742
            print (OO00OO00OOOO00O00 )#line:743
    def watched_ad (OO00000O0000OOOO0 ):#line:746
        try :#line:747
            O000OOO00O00000O0 =f'__{timi_new()}'#line:748
            OO0OO00O0O0OO0000 ={'source':'scsc','authorization':OO00000O0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00O00000O0 ),'signstring':O000OOO00O00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            O00OOOO0000O00O00 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO00O0O0OO0000 ).json ()#line:760
            if 'status'in O00OOOO0000O00O00 :#line:762
                if O00OOOO0000O00O00 ['status']==200 :#line:763
                    if 'offlineInfo'in O00OOOO0000O00O00 ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        OO0000OO0OO0OOOO0 =O00OOOO0000O00O00 ['data']['offlineInfo']['off_minute']#line:766
                        OO000OOOO0OO000O0 =float (O00OOOO0000O00O00 ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OO00O0O0OO0000 ).json ()#line:769
                        time .sleep (2 )#line:770
                        OOO0O0OO0OO00OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO00O0O0OO0000 ).json ()#line:771
                        if 'status'in OOO0O0OO0OO00OOOO :#line:773
                            if OOO0O0OO0OO00OOOO ['status']==200 :#line:774
                                OO000000OO000OO0O =float (OOO0O0OO0OO00OOOO ['data']['silver'])/1000000000000 #line:775
                                O0OO0O0O0000O000O =str (OO000000OO000OO0O -OO000OOOO0OO000O0 )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{OO0000OO0OO0OOOO0}分钟奖励🌱数量:{O0OO0O0O0000O000O}t粒')#line:777
        except Exception as O000OO00O0OOO0000 :#line:778
            print (O000OO00O0OOO0000 )#line:779
    def user_ad (O000OOO00O0OO00OO ):#line:782
        try :#line:783
            O0O00O00O000OOO0O =f'__{timi_new()}'#line:784
            O00O0O0OOO0O0OOOO ={'source':'scsc','authorization':O000OOO00O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O000OOO0O ),'signstring':O0O00O00O000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            OOOO0OO0OO0OO0OOO =requests .request ('get',f'{host}/user/ad',headers =O00O0O0OOO0O0OOOO ).json ()#line:796
            if 'status'in OOOO0OO0OO0OO0OOO :#line:798
                if OOOO0OO0OO0OO0OOO ['status']==200 :#line:799
                    O0O0OOO00O0000O0O =OOOO0OO0OO0OO0OOO ['data']['max_time']#line:800
                    OO0O0O0OO0OO0O0O0 =OOOO0OO0OO0OO0OOO ['data']['watch_time']#line:801
                    OO000O0000000OO00 =OOOO0OO0OO0OO0OOO ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{OO000O0000000OO00 + O0O0OOO00O0000O0O - OO0O0O0OO0OO0O0O0}次丨好友提供:{OO000O0000000OO00}次')#line:803
                    if OO000O0000000OO00 +O0O0OOO00O0000O0O -OO0O0O0OO0OO0O0O0 >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        O0OOO000OOOO0OOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O0O0OOO0O0OOOO ).json ()#line:806
                        if 'status'in O0OOO000OOOO0OOO0 :#line:808
                            if O0OOO000OOOO0OOO0 ['status']==200 :#line:809
                                OOOO0O0O00O0O000O =float (O0OOO000OOOO0OOO0 ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(OOOO0O0O00O0O000O)}t粒')#line:811
                                return True #line:812
                            if O0OOO000OOOO0OOO0 ['status']==500 :#line:813
                                OO0OOO0O000O0O000 =O0OOO000OOOO0OOO0 ['message']#line:814
                                print (f'【获取种子】:{OO0OOO0O000O0O000}')#line:815
                                return False #line:816
        except Exception as O00OO00000OO00O0O :#line:817
            print (O00OO00000OO00O0O )#line:818
    def synthetic (O0O00O0OOOO0O00O0 ):#line:821
        global id ,g #line:822
        try :#line:823
            OO0OOOOO0O0OO000O =O0O00O0OOOO0O00O0 .level_new ()#line:824
            OOO00OOO000O00OOO =random .randint (9 ,11 )#line:825
            OOOO000000O0O0000 =f'_site=8&targetSite={OOO00OOO000O00OOO}_{timi_new()}'#line:826
            OO0OO000OO0OO0OOO ={'source':'scsc','authorization':O0O00O0OOOO0O00O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO000000O0O0000 ),'signstring':OOOO000000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            O000O0OO00O000O0O ={"site":int (8 ),"targetSite":int (OOO00OOO000O00OOO )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000OO0OO0OOO ,json =O000O0OO00O000O0O )#line:839
            while True :#line:840
                OO0OOOO00OOOO0O0O =f'__{timi_new()}'#line:841
                O0000O000O0O0000O ={'source':'scsc','authorization':O0O00O0OOOO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO00OOOO0O0O ),'signstring':OO0OOOO00OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                OOOOOO0OOOOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O000O0O0000O ).json ()#line:853
                if 'status'in OOOOOO0OOOOOOO0O0 :#line:855
                    if OOOOOO0OOOOOOO0O0 ['status']==200 :#line:856
                        OO00000OO00O0OOO0 =OOOOOO0OOOOOOO0O0 ['data']['cropList']#line:857
                        O0OO000O00O0O0OO0 =OOOOOO0OOOOOOO0O0 ['data']['gameCoreDataDBid']#line:858
                        O0O00OO0O0OOOO0OO =float (OOOOOO0OOOOOOO0O0 ['data']['silver'])/1000000000000 #line:859
                        O00OO0O00O0OOO0O0 =0 #line:864
                        for O0O0O0000OO00O00O in OO00000OO00O0OOO0 :#line:865
                            if not O0O0O0000OO00O00O :#line:866
                                OOOO0OO000OOOOOO0 =f'_crop_id={O0OO000O00O0O0OO0}&site={O00OO0O00O0OOO0O0}_{O0O00O0OOOO0O00O0.time}'#line:867
                                O00OOOOO00O00O00O ={'source':'scsc','authorization':O0O00O0OOOO0O00O0 .token ,'timestamp':O0O00O0OOOO0O00O0 .time ,'sign':sign (OOOO0OO000OOOOOO0 ),'signstring':OOOO0OO000OOOOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                OO00O0O0OO0OO0000 ={"site":O00OO0O00O0OOO0O0 ,"crop_id":O0OO000O00O0O0OO0 }#line:878
                                O0000O00OO0O0OO0O =requests .request ('post',f'{host}/game/crops/buy',headers =O00OOOOO00O00O00O ,data =OO00O0O0OO0OO0000 ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in O0000O00OO0O0OO0O :#line:882
                                    if O0000O00OO0O0OO0O ['status']==200 :#line:883
                                        if O0000O00OO0O0OO0O ['message']=='种子数量不足':#line:884
                                            OO0OOOOO0O0OO000O =O0O00O0OOOO0O00O0 .level_new ()#line:885
                                            print (f'【种植合成】:{O0000O00OO0O0OO0O["message"]}')#line:886
                                            if not O0O00O0OOOO0O00O0 .user_ad ():#line:887
                                                return False #line:888
                                    if O0000O00OO0O0OO0O ['status']==500 :#line:889
                                        print (f'【种植合成】:{O0000O00OO0O0OO0O["message"]}')#line:890
                                        return False #line:891
                            O00OO0O00O0OOO0O0 +=1 #line:892
                        OOOO0000OO0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =O0000O000O0O0000O ).json ()#line:893
                        O00OO00OOOO0O0000 =OOOO0000OO0OOO00O ['data']['cropList']#line:894
                        OOO0O00OOOOOOO0OO =False #line:895
                        for O0O0O0000OO00O00O in range (12 ):#line:896
                            id =O00OO00OOOO0O0000 [O0O0O0000OO00O00O ]['level']#line:897
                            if float (OO0OOOOO0O0OO000O )-float (id )>9 :#line:898
                                O00OOO0OOO000O0O0 =f'_site={O0O0O0000OO00O00O}_{timi_new()}'#line:899
                                OO00O0OOO00O0O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OOOO0O00O0 .token ,'timestamp':timi_new (),'sign':sign (O00OOO0OOO000O0O0 ),'signstring':O00OOO0OOO000O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                OOO000O00000O00OO ={"site":O0O0O0000OO00O00O }#line:911
                                O0O0O000O0OOOO0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00O0OOO00O0O0OO ,data =OOO000O00000O00OO ).json ()#line:913
                                if 'status'in O0O0O000O0OOOO0O0 :#line:914
                                    if O0O0O000O0OOOO0O0 ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O00OOOOOOO0O0000O in range (11 ):#line:918
                                    O0OOOO0OOOOO000O0 =O00OOOOOOO0O0000O +1 #line:919
                                    g =O00OO00OOOO0O0000 [O0OOOO0OOOOO000O0 ]['level']#line:920
                                    if id ==g :#line:921
                                        O0O00O00000OO0000 =O00OOOOOOO0O0000O +2 #line:922
                                        if O0O00O00000OO0000 !=O0O0O0000OO00O00O +1 :#line:923
                                            OOOO0OOOOO0OO0OOO =O0O0O0000OO00O00O +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            OOOO000000O0O0000 =f'_site={OOOO0OOOOO0OO0OOO - 1}&targetSite={O0O00O00000OO0000 - 1}_{timi_new()}'#line:927
                                            OO0OO000OO0OO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OOOO0O00O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO000000O0O0000 ),'signstring':OOOO000000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            OOOOO0O0OOOOO0OO0 ={"site":int (OOOO0OOOOO0OO0OOO -1 ),"targetSite":int (O0O00O00000OO0000 -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OO000OO0OO0OOO ,json =OOOOO0O0OOOOO0OO0 )#line:946
                                            OOO0O00OOOOOOO0OO =True #line:948
                                    if OOO0O00OOOOOOO0OO :#line:949
                                        break #line:950
                                if OOO0O00OOOOOOO0OO :#line:951
                                    break #line:952
        except :#line:953
            O0O00O0OOOO0O00O0 .synthetic ()#line:954
    def level_new (OO0O0OOOO00O0O00O ):#line:957
        try :#line:958
            OOOO000OO0O0OOO0O =f'__{timi_new()}'#line:959
            OOOOOO000O0O00000 ={'source':'scsc','authorization':OO0O0OOOO00O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OO0O0OOO0O ),'signstring':OOOO000OO0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            O0O000O000O00O00O =requests .request ('get',f'{host}/user',headers =OOOOOO000O0O00000 ).json ()#line:971
            if 'status'in O0O000O000O00O00O :#line:972
                if O0O000O000O00O00O ['status']==200 :#line:973
                    return float (O0O000O000O00O00O ['data']['level'])#line:974
        except Exception as O0000O0O0O0O0000O :#line:975
            print (O0000O0O0O0O0000O )#line:976
    def propsraffle (OO00O0OO000OOOO00 ):#line:979
        try :#line:980
            while True :#line:981
                O00O000OOOO0OOO0O =f'__{timi_new()}'#line:982
                OO0OO00O00OO0OOOO ={'source':'scsc','authorization':OO00O0OO000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOO0OOO0O ),'signstring':O00O000OOOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                O00OO00O0O0O000OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OO00O00OO0OOOO ).json ()#line:994
                if 'status'in O00OO00O0O0O000OO :#line:996
                    if O00OO00O0O0O000OO ['status']==200 :#line:997
                        O0000OO0000O00O0O =O00OO00O0O0O000OO ['data']['rows']#line:998
                        OOO00OO0000000000 =O00OO00O0O0O000OO ['data']['vstate']#line:999
                        if O0000OO0000O00O0O ==5 or O0000OO0000O00O0O ==6 or O0000OO0000O00O0O ==7 :#line:1000
                            OO0OOOOO00000OOO0 =O00OO00O0O0O000OO ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{OO0OOOOO00000OOO0}')#line:1002
                        if O0000OO0000O00O0O ==1 or O0000OO0000O00O0O ==2 or O0000OO0000O00O0O ==3 :#line:1003
                            O0OO0OOO0OOO000OO =O00OO00O0O0O000OO ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O0OO0OOO0OOO000OO}')#line:1005
                        if O0000OO0000O00O0O ==4 or O0000OO0000O00O0O ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if O0000OO0000O00O0O =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as OO0OO00OOOOOOOO00 :#line:1047
            print (OO0OO00OOOOOOOO00 )#line:1048
    def friends_invitation (O0OO0O0000O00O0O0 ):#line:1051
        try :#line:1052
            OOOO0OO0O0O0000OO =f'__{timi_new()}'#line:1053
            OOO0OO0O00O0OOO00 ={'source':'scsc','authorization':O0OO0O0000O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0O0O0000OO ),'signstring':OOOO0OO0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            OO000O0O0O0O000O0 =requests .request ('get',f'{host}/friends',headers =OOO0OO0O00O0OOO00 ).json ()#line:1065
            if 'status'in OO000O0O0O0O000O0 :#line:1066
                if OO000O0O0O0O000O0 ['status']==200 :#line:1067
                    O0000O0O0O00O0000 =OO000O0O0O0O000O0 ['data']['myInviteter']#line:1068
                    if O0000O0O0O00O0000 :#line:1069
                        OOOOO0OO0000O00OO =O0000O0O0O00O0000 ['user']['nickname']#line:1070
                        O0O00O000O00OOOOO =O0OO0O0000O00O0O0 .certification ()#line:1071
                        if O0O00O000O00OOOOO =='未实名':#line:1072
                            weishim .append (O0OO0O0000O00O0O0 .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{OOOOO0OO0000O00OO}丨实名:{O0O00O000O00OOOOO}')#line:1074
        except Exception as OO0O0O0O00O0OO0O0 :#line:1078
            print (OO0O0O0O00O0OO0O0 )#line:1079
    def add_clover (OOO0OO000000OO00O ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            OOOOO0O00OOOOO00O =f'__{timi_new()}'#line:1085
            O0O000OOOOO000O00 ={'source':'scsc','authorization':OOO0OO000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OOOOO00O ),'signstring':OOOOO0O00OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OOOOO0O00O0O0OO0O =requests .request ('get',f'{host}/assets/clovers',headers =O0O000OOOOO000O00 ).json ()#line:1097
            if 'status'in OOOOO0O00O0O0OO0O :#line:1099
                if OOOOO0O00O0O0OO0O ['status']==200 :#line:1100
                    O00OOOOOO0000OOO0 =OOOOO0O00O0O0OO0O ['data']['clover']#line:1101
                    O0OO0OOO000OOOOOO =OOOOO0O00O0O0OO0O ['data']['used_clover']#line:1102
                    O000000O0OO00OO00 =float (O00OOOOOO0000OOO0 )-float (O0OO0OOO000OOOOOO )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0OOO000OOOOOO}')#line:1104
                    if OOO0OO000000OO00O .certification ()!='未实名':#line:1105
                        if O000000O0OO00OO00 >1 :#line:1106
                            OOOOO0O00OOOOO00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000000O0OO00OO00)}_{timi_new()}'#line:1107
                            O0OOO0OOOO00OOOOO ={'source':'scsc','authorization':OOO0OO000000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OOOOO00O ),'signstring':OOOOO0O00OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            O0OO00O000O00OO0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000000O0OO00OO00 )}#line:1119
                            O0O0O00OO0O0000OO =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OOO0OOOO00OOOOO ,data =O0OO00O000O00OO0O ).json ()#line:1120
                            if 'status'in O0O0O00OO0O0000OO :#line:1122
                                if O0O0O00OO0O0000OO ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O0O0O00OO0O0000OO["data"]["isSuccess"]}丨数量:{O000000O0OO00OO00}')#line:1124
                                if O0O0O00OO0O0000OO ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O0O0O00OO0O0000OO["message"]}')#line:1126
            O0O00O0O0O0OO0OO0 =requests .request ('get',f'{host}/lottery',headers =O0O000OOOOO000O00 ).json ()#line:1127
            O0000OOOO000O0OO0 =OOO0OO000000OO00O .winning_rewards ()#line:1129
            if 'status'in O0O00O0O0O0OO0OO0 :#line:1130
                if O0O00O0O0O0OO0OO0 ['status']==200 :#line:1131
                    O000O00OO00OO0OO0 =O0O00O0O0O0OO0OO0 ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (O000O00OO00OO0OO0 )#line:1133
                    O000000000O0OOOOO =O0O00O0O0O0OO0OO0 ['data'][1 ]['value']#line:1134
                    O0OOOO00OO0000000 =O0O00O0O0O0OO0OO0 ['data'][0 ]['join_number']#line:1135
                    O00000OO0OOO0OO00 =int (float (O0O00O0O0O0OO0OO0 ['data'][0 ]['totalValue']))#line:1136
                    O00OO0O0O0O0OO0O0 =float (O000000000O0OOOOO /O00000OO0OOO0OO00 )*10000 #line:1137
                    O0OOOO0O000OOO00O =O00000OO0OOO0OO00 /O0OOOO00OO0000000 #line:1138
                    print (f'【参与抽奖】:预计每天中{str(O000O00OO00OO0OO0)[:6]}颗金种子丨好友收益:{str(O0000OOOO000O0OO0)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O00OO0O0O0O0OO0O0)[:6]}颗金种子丨☘️人均:{str(O0OOOO0O000OOO00O)[:7]}️')#line:1140
        except Exception as O00OO0O00OOO000O0 :#line:1141
            print (O00OO0O00OOO000O0 )#line:1142
    def energy (OOO00O0O000000OO0 ):#line:1145
        try :#line:1146
            while True :#line:1147
                OO0OO000O0OO0OO0O =f'__{timi_new()}'#line:1148
                OO0O0OO0O0000O0OO ={'source':'scsc','authorization':OOO00O0O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0OO0OO0O ),'signstring':OO0OO000O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                OOO0OO0OO0OOOO0OO =requests .request ('get',f'{host}/energy/general',headers =OO0O0OO0O0000O0OO ).json ()#line:1160
                if 'status'in OOO0OO0OO0OOOO0OO :#line:1162
                    if OOO0OO0OO0OOOO0OO ['status']==200 :#line:1163
                        OO00OOOO0000000OO =OOO0OO0OO0OOOO0OO ['data']['ordinary_water']#line:1164
                        OOOO0OO0000O0OO0O =OOO0OO0OO0OOOO0OO ['data']['ordinary_fertilizer']#line:1165
                        O0OOOO0O000OOOOOO =OOO0OO0OO0OOOO0OO ['data']['videoStatus']#line:1166
                        O0000O00OO0000O00 =OOO0OO0OO0OOOO0OO ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(OOOO0OO0000O0OO0O).split(".")[0]}丨水滴:{str(OO00OOOO0000000OO).split(".")[0]}')#line:1169
                        if float (OOOO0OO0000O0OO0O )<96 :#line:1170
                            if O0OOOO0O000OOOOOO :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OOOOO0O00OO00O00O =99 -float (OOOO0OO0000O0OO0O )#line:1173
                                O00OOO0O00O0O0O0O ={"fertilizer":str (OOOOO0O00OO00O00O ).split ('.')[0 ]}#line:1174
                                O0OO000OOO0OOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0O0OO0O0000O0OO ).json ()#line:1176
                                if 'status'in O0OO000OOO0OOOOO0 :#line:1178
                                    if O0OO000OOO0OOOOO0 ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO000OOO0OOOOO0["message"]}')#line:1180
                                    if O0OO000OOO0OOOOO0 ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO000OOO0OOOOO0["message"]}')#line:1182
                                        break #line:1183
                                if float (OOOO0OO0000O0OO0O )<78 :#line:1185
                                    OOOOO0O00OO00O00O =80 -float (OOOO0OO0000O0OO0O )#line:1186
                                    OOOO0OOO00000OOOO =f'_fertilizer={int(OOOOO0O00OO00O00O)}_{timi_new()}'#line:1187
                                    O0000OO0OO0000O00 ={'source':'scsc','authorization':OOO00O0O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00000OOOO ),'signstring':OOOO0OOO00000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    O0000O0O0O000OO0O ={"fertilizer":int (OOOOO0O00OO00O00O )}#line:1199
                                    OOO000000OO00O0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0000OO0OO0000O00 ,data =O0000O0O0O000OO0O ).json ()#line:1201
                                    if 'status'in OOO000000OO00O0OO :#line:1203
                                        if OOO000000OO00O0OO ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OOO000000OO00O0OO["message"]}丨数量:{int(OOOOO0O00OO00O00O)}')#line:1205
                                        if OOO000000OO00O0OO ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OOO000000OO00O0OO["message"]}丨数量:{int(OOOOO0O00OO00O00O)}')#line:1207
                                            O0O0O0OOOOOO0O0OO =OOO000000OO00O0OO ["message"].split ('-')[1 ]#line:1208
                                            O0O0OOO00O00OO000 =f'__{timi_new()}'#line:1209
                                            OOOOO00OOO00O00O0 ={'source':'scsc','authorization':OOO00O0O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00O00OO000 ),'signstring':O0O0OOO00O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            OO00OO00O00O00O00 =requests .request ('get',f'{host}/user',headers =OOOOO00OOO00O00O0 ).json ()#line:1221
                                            if 'status'in OO00OO00O00O00O00 :#line:1222
                                                if OO00OO00O00O00O00 ['status']==200 :#line:1223
                                                    O000OOOO00O000OOO =OO00OO00O00O00O00 ['data']['inner_id']#line:1224
                                                    if give_gold (O000OOOO00O000OOO ,float (O0O0O0OOOOOO0O0OO )+1 ):#line:1225
                                                        OOO00O0O000000OO0 .energy ()#line:1226
                        if float (OO00OOOO0000000OO )<880 :#line:1227
                            if O0000O00OO0000O00 :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O00O00OOO0O0OO000 =999 -float (OO00OOOO0000000OO )#line:1230
                                O00O0OO0OO0OOO000 ={"water":str (O00O00OOO0O0OO000 ).split ('.')[0 ]}#line:1231
                                O0O0O0O0OO0O000OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0O0OO0O0000O0OO ).json ()#line:1233
                                if 'status'in O0O0O0O0OO0O000OO :#line:1235
                                    if O0O0O0O0OO0O000OO ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O0O0OO0O000OO["message"]}')#line:1237
                                    if O0O0O0O0OO0O000OO ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0O0O0OO0O000OO["message"]}')#line:1239
                                        break #line:1240
                                if float (OO00OOOO0000000OO )<780 :#line:1241
                                    O00O00OOO0O0OO000 =800 -float (OO00OOOO0000000OO )#line:1242
                                    OO0O000OOO00O00O0 =f'_water={int(O00O00OOO0O0OO000)}_{timi_new()}'#line:1243
                                    OOOOO0OO00O0O0000 ={'source':'scsc','authorization':OOO00O0O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000OOO00O00O0 ),'signstring':OO0O000OOO00O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    OOOOO0OO0O00O0000 ={"water":int (O00O00OOO0O0OO000 )}#line:1255
                                    O00000O0O00OOOOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOOO0OO00O0O0000 ,data =OOOOO0OO0O00O0000 ).json ()#line:1257
                                    if 'status'in O00000O0O00OOOOOO :#line:1259
                                        if O00000O0O00OOOOOO ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O00000O0O00OOOOOO["message"]}丨数量:{int(O00O00OOO0O0OO000)}')#line:1261
                                        if O00000O0O00OOOOOO ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O00000O0O00OOOOOO["message"]}丨数量:{int(O00O00OOO0O0OO000)}')#line:1263
                                            O0O0O0OOOOOO0O0OO =O00000O0O00OOOOOO ["message"].split ('-')[1 ]#line:1264
                                            O0O0OOO00O00OO000 =f'__{timi_new()}'#line:1265
                                            OOOOO00OOO00O00O0 ={'source':'scsc','authorization':OOO00O0O000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00O00OO000 ),'signstring':O0O0OOO00O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            OO00OO00O00O00O00 =requests .request ('get',f'{host}/user',headers =OOOOO00OOO00O00O0 ).json ()#line:1277
                                            if 'status'in OO00OO00O00O00O00 :#line:1278
                                                if OO00OO00O00O00O00 ['status']==200 :#line:1279
                                                    O000OOOO00O000OOO =OO00OO00O00O00O00 ['data']['inner_id']#line:1280
                                                    if give_gold (O000OOOO00O000OOO ,float (O0O0O0OOOOOO0O0OO )+1 ):#line:1281
                                                        OOO00O0O000000OO0 .energy ()#line:1282
                        break #line:1283
        except Exception as OOO00O0O00OOO000O :#line:1284
            print (OOO00O0O00OOO000O )#line:1285
def bundled_def ():#line:1288
    OOOO0O0000OO0O000 =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return OOOO0O0000OO0O000 [random .randint (0 ,len (OOOO0O0000OO0O000 )-1 )]#line:1290
def version_of_the_validation ():#line:1294
    return str ((104 -56 )/10 )#line:1295
def ubbbf ():#line:1297
    print ('卡密验证通过   ✅')#line:1298
def sc2 ():#line:1301
    return "19319#$%^&*((*"#line:1302
def OO00OO0OO0OO00OO00o0 ():#line:1305
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1307
def get_ip ():#line:1310
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1312
def gitee_validation ():#line:1315
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1316
def gitee_edition ():#line:1319
    try :#line:1320
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1321
    except :#line:1322
        sys .exit (0 )#line:1323
def O000OO000O0O00OOO00 ():#line:1327
    try :#line:1328
        OO0000O0O0OO0OO00 =gitee_edition ()#line:1329
        if version_of_the_validation ()<OO0000O0O0OO0OO00 ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000O0O0OO0OO00["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{OO0000O0O0OO0OO00["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000O0O0OO0OO00["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {OO0000O0O0OO0OO00["CityEarth"]["content"]}')#line:1335
    except Exception as OOOOOO0O000O00O00 :#line:1336
        print (OOOOOO0O000O00O00 )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
