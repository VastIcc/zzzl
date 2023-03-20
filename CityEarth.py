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
time_xx = random.randint(8, 15)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
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
        O0OOO0OOO0O00O0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0OOO0OOO0O00O0O0)}个账号==========")#line:17
        for O00OO00O0O0OO0000 in O0OOO0OOO0O00O0O0 :#line:18
            OO0OOO0OOO0OOOO00 =[]#line:19
            print (f"------------正在执行第{O0OOO0OOO0O00O0O0.index(O00OO00O0O0OO0000) + 1}个账号------------")#line:20
            O0O00OOO0OOOO00O0 =CityEarth (O00OO00O0O0OO0000 ,OO0OOO0OOO0OOOO00 ,O0OOO0OOO0O00O0O0 .index (O00OO00O0O0OO0000 ))#line:21
            def OOO0OOOO00OO000OO ():#line:23
                if O0O00OOO0OOOO00O0 .base_info ():#line:25
                    O0O00OOO0OOOO00O0 .sealing ()#line:27
                    O0O00OOO0OOOO00O0 .invitenum ()#line:29
                    O0O00OOO0OOOO00O0 .query_to_sell ()#line:31
                    O0O00OOO0OOOO00O0 .friends_invitation ()#line:35
                    O0O00OOO0OOOO00O0 .energy ()#line:37
                    O0O00OOO0OOOO00O0 .add_clover ()#line:39
                    O0O00OOO0OOOO00O0 .propsraffle ()#line:41
                    O0O00OOO0OOOO00O0 .synthetic ()#line:43
                    O0O00OOO0OOOO00O0 .crops_illustrated ()#line:45
                    O0O00OOO0OOOO00O0 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        O0O00OOO0OOOO00O0 .give_gold ()#line:50
            OOOOO00O000O0OO00 =threading .Thread (target =OOO0OOOO00OO000OO )#line:52
            OOOOO00O000O0OO00 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O00OO0O00OO00OOOO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OO0O00OO00OOOO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O00000OO0O0OO0O in invited_new :#line:62
            print (O0O00000OO0O0OO0O )#line:63
        print ('开始打印未实名的token')#line:64
        for O0OOOO00O0OOOOO0O in weishim :#line:65
            print (O0OOOO00O0OOOOO0O )#line:66
    except Exception as OO0OO0O000O0O0O00 :#line:67
        print (OO0OO0O000O0O0O00 )#line:68
def give_gold (OO0OO0O0O000O0OO0 ,OOO000O0OOOO00O0O ):#line:72
    try :#line:73
        OO0000O00OOOO00OO =f'_doneeNo={OO0OO0O0O000O0OO0}&quantity={int(OOO000O0OOOO00O0O)}_{timi_new()}'#line:74
        O00OO00O0OO0OOO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0000O00OOOO00OO ),'signstring':OO0000O00OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO0O0OOO00O0O00O0 ={"quantity":int (OOO000O0OOOO00O0O ),"doneeNo":OO0OO0O0O000O0OO0 }#line:89
        O000O00O00OO00000 =requests .request ('post',f'{host}/finance/give-gold',headers =O00OO00O0OO0OOO00 ,data =OO0O0OOO00O0O00O0 ).json ()#line:90
        if 'status'in O000O00O00OO00000 :#line:92
            if O000O00O00OO00000 ['status']==200 :#line:93
                if O000O00O00OO00000 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OOO000O0OOOO00O0O)}种子给{OO0OO0O0O000O0OO0}成功')#line:95
                    return True #line:96
            if O000O00O00OO00000 ['status']==401 :#line:97
                print (f'【赠送种子】:{O000O00O00OO00000["message"]}')#line:98
                return False #line:99
            if O000O00O00OO00000 ['status']==500 :#line:100
                print (f'【赠送种子】:{O000O00O00OO00000["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00OOO0OOOOO0O000 :#line:104
        print (O00OOO0OOOOO0O000 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OOOOOO0O00O0O00O0 ):#line:115
    OO0O00000O0O00O00 =hashlib .md5 (OOOOOO0O00O0O00O0 .encode ()).hexdigest ()#line:116
    OOOO0O00OO00OOO0O =sc1 ()#line:117
    O0O0OO0O00OO00000 =sc2 ()#line:118
    O0O0O0OOO00O0O000 =sc3 ()#line:119
    OO0O0O000O0O00OO0 =OOOO0O00OO00OOO0O +OO0O00000O0O00O00 +O0O0OO0O00OO00000 +O0O0O0OOO00O0O000 #line:120
    O00OO00O00O00O000 =hashlib .md5 (OO0O0O000O0O00OO0 .encode ()).hexdigest ()#line:121
    return O00OO00O00O00O000 #line:122
def format_msg ():#line:125
    O00OOOOO0O0OOO00O =""#line:126
    for OOO0O0OOOOOO0O0OO in msg_list :#line:127
        O00OOOOO0O0OOO00O +=str (OOO0O0OOOOOO0O0OO )+"\r\n"#line:128
    return O00OOOOO0O0OOO00O #line:129
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
def get_json_data (OOOOOO000000O00OO ,O0000OOO00O0OOO00 ,O0O0O0OOO0OOOO000 ,OOOOOO000OOO0O0O0 ):#line:153
    with open (OOOOOO000000O00OO ,'rb')as OOO0000O0OOOO0OOO :#line:154
        O0O0OO0O0OO00O00O =json .load (OOO0000O0OOOO0OOO )#line:155
        O0O0OO0O0OO00O00O ['data'][O0000OOO00O0OOO00 ][O0O0O0OOO0OOOO000 ]=OOOOOO000OOO0O0O0 #line:156
        O0OOO0O00O0000000 =O0O0OO0O0OO00O00O #line:157
    OOO0000O0OOOO0OOO .close ()#line:158
    return O0OOO0O00O0000000 #line:159
def write_json_data (O0OO00OOOOO00000O ):#line:162
    with open (json_path1 ,'w')as O0000OO00OO00OOOO :#line:163
        json .dump (O0OO00OOOOO00000O ,O0000OO00OO00OOOO ,indent =2 ,sort_keys =True ,ensure_ascii =False )#line:164
    O0000OO00OO00OOOO .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OOO00000OOO00O00O ,OOO0O0OOO0O00OOO0 ,O0000O000O0OOOO0O ,OO0O0O0O00OO0000O ):#line:171
        try :#line:172
            OOO00000OOO00O00O .msg =O0000O000O0OOOO0O #line:173
            OOO00000OOO00O00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OOO00000OOO00O00O .token =OOO0O0OOO0O00OOO0 ['authorization']#line:175
            OOO00000OOO00O00O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OOO00000OOO00O00O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OOO00000OOO00O00O .elephant_user =OOO0O0OOO0O00OOO0 ['elephant_user']#line:178
            OOO00000OOO00O00O .elephant_pswd =OOO0O0OOO0O00OOO0 ['elephant_pswd']#line:179
            OOO00000OOO00O00O .elephant_Task_ID =OOO0O0OOO0O00OOO0 ['elephant_Task_ID']#line:180
            OOO00000OOO00O00O .len_new =OO0O0O0O00OO0000O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0OO0OO000O0O0O00 ):#line:186
        try :#line:187
            O0OO0OO000O0O0O00 .watched_ad ()#line:189
            OO000O0O00000O000 =f'__{timi_new()}'#line:190
            O00OO0OOO0O00O0OO ={'source':'scsc','authorization':O0OO0OO000O0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O00000O000 ),'signstring':OO000O0O00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0OO00O0O0O0OOOOO =requests .request ('get',f'{host}/user',headers =O00OO0OOO0O00O0OO ).json ()#line:202
            if 'status'in O0OO00O0O0O0OOOOO :#line:204
                if O0OO00O0O0O0OOOOO ['status']==200 :#line:205
                    O00O0O000OO00O0O0 =O0OO00O0O0O0OOOOO ['data']['nickname']#line:206
                    O00OOOOOO0OOOO000 =O0OO00O0O0O0OOOOO ['data']['inner_id']#line:207
                    OO00OO00O0000000O =O0OO00O0O0O0OOOOO ['data']['assets']['gold']#line:208
                    OOOOOOOOO0000000O =O0OO00O0O0O0OOOOO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00O0O000OO00O0O0[:5]}丨ID:{O00OOOOOO0OOOO000}丨等级:{OOOOOOOOO0000000O}丨金种子:{str(OO00OO00O0000000O).split(".")[0]}')#line:211
                    if 'wx_'in O00O0O000OO00O0O0 :#line:212
                        O0OO0OO000O0O0O00 .change_nickname ()#line:213
                if O0OO00O0O0O0OOOOO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0OO0OO000O0O0O00 .elephant_user =='f':#line:216
                        return False #line:217
                    OO0OOO00O0000O00O =Invalid_login .addtask (elephant_user =O0OO0OO000O0O0O00 .elephant_user ,elephant_pswd =O0OO0OO000O0O0O00 .elephant_pswd ,elephant_Task_ID =O0OO0OO000O0O0O00 .elephant_Task_ID )#line:220
                    OOOO000O0O0OOO00O =get_json_data (json_path ,O0OO0OO000O0O0O00 .len_new ,'authorization',OO0OOO00O0000O00O )#line:221
                    if write_json_data (OOOO000O0O0OOO00O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0OO00O0O0O0OOOOO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOOO0O0OO0O0O0O00 :#line:228
            print (OOOO0O0OO0O0O0O00 )#line:229
    def sealing (O0O00OO0O0OO0000O ):#line:232
        try :#line:233
            OOO00OO0O000OOO0O =f'__{timi_new()}'#line:234
            OO0000OOO0OOOOO0O ={'source':'scsc','authorization':O0O00OO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO0O000OOO0O ),'signstring':OOO00OO0O000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0000OOO0OOOOO0O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO0000OOO0OOOOO0O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0000OOO0OOOOO0O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0000OOO0OOOOO0O )#line:249
            requests .request ('get',f'{host}/user',headers =OO0000OOO0OOOOO0O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0000OOO0OOOOO0O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0000OOO0OOOOO0O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0000OOO0OOOOO0O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO0000OOO0OOOOO0O )#line:254
            requests .request ('get',f'{host}/assets',headers =OO0000OOO0OOOOO0O )#line:255
        except Exception as OOO0O00OO00000OO0 :#line:256
            print (OOO0O00OO00000OO0 )#line:257
    def ddd (O00000OOOO0O0O00O ):#line:259
        try :#line:260
            O00OO000OO000O0OO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            OO000O000OOO00O0O ={'source':'scsc','authorization':O00000OOOO0O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OO000O0OO ),'signstring':O00OO000OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0O0O000OOO0000OO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OO000O000OOO00O0O ).json ()#line:273
            print (O0O0O000OOO0000OO )#line:274
        except Exception as O000O0OO00O00O0OO :#line:277
            print (O000O0OO00O00O0OO )#line:278
    def the_query (O0OOOOO00O000OOO0 ):#line:283
        try :#line:284
            OO0OOOOOO00O000OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O000OO0O0000OO0O0 ={'authorization':O0OOOOO00O000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO00O000OO ),'signstring':OO0OOOOOO00O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O0000OOOO00OOOO00 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O000OO0O0000OO0O0 ).json ()#line:296
            if 'status'in O0000OOOO00OOOO00 :#line:298
                if O0000OOOO00OOOO00 ['status']==200 :#line:299
                    return O0000OOOO00OOOO00 ['data']['rows'][4 ]['price']#line:300
        except Exception as O00OO000OOOOO000O :#line:301
            print (O00OO000OOOOO000O )#line:302
    def market_sale (O0OO0O00000O000OO ,O0OO00000O00O00O0 ):#line:305
        try :#line:306
            O0O0O00O000O00000 =timi_new ()#line:307
            OO0OOO0OO0O0O00OO =f'type=crop__{O0O0O00O000O00000}'#line:308
            O0O0O0OO0000000O0 ={'source':'scsc','authorization':O0OO0O00000O000OO .token ,'timestamp':str (O0O0O00O000O00000 ),'sign':sign (OO0OOO0OO0O0O00OO ),'signstring':OO0OOO0OO0O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O00O0O00O00O00O00 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O0OO0000000O0 ).json ()#line:320
            if 'status'in O00O0O00O00O00O00 :#line:322
                if O00O0O00O00O00O00 ['status']==200 :#line:323
                    if O00O0O00O00O00O00 ['data']['rows']:#line:324
                        O0O0OO000O00O000O =O00O0O00O00O00O00 ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOO0O0O0OOO0O0O00 =O00O0O00O00O00O00 ['data']['rows'][0 ]['quantity']#line:326
                        O0OOO000O0OO0O0O0 =float (O0OO00000O00O00O0 )-float (random .randint (1 ,9 )*0.001 )#line:327
                        if float (O0OO00000O00O00O0 )>6 :#line:328
                            OOO0O00O0OO0OO0O0 =f'_packsackItemId={O0O0OO000O00O000O}&price={str(O0OOO000O0OO0O0O0)[:5]}&quantity={OOO0O0O0OOO0O0O00}_{O0O0O00O000O00000}'#line:329
                            OOOO0000OO0O00OO0 ={'source':'scsc','authorization':O0OO0O00000O000OO .token ,'timestamp':str (O0O0O00O000O00000 ),'sign':sign (OOO0O00O0OO0OO0O0 ),'signstring':OOO0O00O0OO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:340
                            O0O00O0O0OOO000O0 ={"packsackItemId":O0O0OO000O00O000O ,"price":str (O0OOO000O0OO0O0O0 )[:5 ],"quantity":str (OOO0O0O0OOO0O0O00 )}#line:345
                            O0OO0O0OO0O0O000O =requests .request ('post',f'{host}/market/sale',headers =OOOO0000OO0O00OO0 ,data =O0O00O0O0OOO000O0 ).json ()#line:346
                            if 'status'in O0OO0O0OO0O0O000O :#line:348
                                if O0OO0O0OO0O0O000O ['status']==200 :#line:349
                                    print (f'【上架芦荟】:数量:{OOO0O0O0OOO0O0O00}丨价格:{str(O0OOO000O0OO0O0O0)[:5]}')#line:350
                                if O0OO0O0OO0O0O000O ['status']==500 :#line:351
                                    print (f'【上架芦荟】:{O0OO0O0OO0O0O000O["message"]}')#line:352
        except Exception as OO00O0OO0O00OOO00 :#line:353
            print (OO00O0OO0O00OOO00 )#line:354
    def query_to_sell (OO0OO00O0O00OOO00 ):#line:357
        global count_list #line:358
        try :#line:359
            O0OOO0OOO00000OOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:360
            OOO00OOOO00000OO0 ={'source':'scsc','authorization':OO0OO00O0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO00000OOO ),'signstring':O0OOO0OOO00000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:371
            OO00OO000OO0OO0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00OOOO00000OO0 ).json ()#line:372
            if 'status'in OO00OO000OO0OO0O0 :#line:374
                if OO00OO000OO0OO0O0 ['status']==200 :#line:375
                    for OO0O00O0O00OO00OO in OO00OO000OO0OO0O0 ['data']['rows']:#line:376
                        O0O0000O0000O0OO0 =OO0O00O0O00OO00OO ['materialKey']#line:377
                        OO0O00000O0OO0O0O =OO0O00O0O00OO00OO ['quantity']#line:378
                        O0000O0O00O0O0OO0 =OO0O00O0O00OO00OO ['price']#line:379
                        O00OO0O00O0O00000 =OO0O00O0O00OO00OO ['saleState']#line:380
                        if O00OO0O00O0O00000 ==0 :#line:381
                            print (f'【出售订单】:名称:{O0O0000O0000O0OO0}丨数量:{OO0O00000O0OO0O0O}丨价格:{O0000O0O00O0O0OO0}')#line:382
                            count_list +=OO0O00000O0OO0O0O #line:383
                            OOO0OO00O0OOOO0OO =OO0OO00O0O00OOO00 .the_query ()#line:385
                            if float (OOO0OO00O0OOOO0OO )!=float (O0000O0O00O0O0OO0 ):#line:386
                                O0O0O0O00O0O0OO00 =OO0O00O0O00OO00OO ['id']#line:387
                                OO0OO00O0O00OOO00 .cacel_sale (O0O0O0O00O0O0OO00 )#line:388
                    OO0OO00O0O00OOO00 .game_map ()#line:390
        except Exception as O000OOO0OOO000O00 :#line:392
            print (O000OOO0OOO000O00 )#line:393
    def cacel_sale (OO0OO00OOOOOOO0O0 ,OO0O0O00O0OOO0O00 ):#line:396
        try :#line:397
            O0OO00OOOOO00O000 =f'_saleId={OO0O0O00O0OOO0O00}_{timi_new()}'#line:398
            O0O00O00OOOOOOO0O ={'source':'scsc','authorization':OO0OO00OOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOOOO00O000 ),'signstring':O0OO00OOOOO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:409
            OOO00O0OOO0OO0OO0 ={"saleId":OO0O0O00O0OOO0O00 }#line:410
            OOOO0O0OO0OOOO0O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O00O00OOOOOOO0O ,data =OOO00O0OOO0OO0OO0 ).json ()#line:411
            if 'status'in OOOO0O0OO0OOOO0O0 :#line:413
                if OOOO0O0OO0OOOO0O0 ['status']==200 :#line:414
                    print (f'【下架出售】:{OOOO0O0OO0OOOO0O0["data"]}')#line:415
        except Exception as O0OO00000OOO0O00O :#line:416
            print (O0OO00000OOO0O00O )#line:417
    def change_nickname (OOO0OOO000OOO0O00 ):#line:420
        try :#line:421
            OO0OOO00OOO00O0OO =timi_new ()#line:422
            O0O000O00000O000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:423
            OOOO0O00OO0O0OOOO =requests .request ('post','https://www.qmsjmfb.com/',data =O0O000O00000O000O ).text #line:424
            OOO00OOO00000OOO0 =re .findall ('<ul><li>(.*?)</li>',OOOO0O00OO0O0OOOO )[0 ][:3 ]#line:425
            OO00O0O00O00OOO0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO00OOO00000OOO0}').json ()#line:426
            O00OO0OOOOO0OOO00 =OO00O0O00O00OOO0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[1 :6 ]#line:427
            OOO0000O0000OO00O ={"nickname":O00OO0OOOOO0OOO00 }#line:428
            OO0000O0OOO00O0OO =f'_nickname={O00OO0OOOOO0OOO00}_{OO0OOO00OOO00O0OO}'#line:429
            O00OOO0000000O00O ={'source':'scsc','authorization':OOO0OOO000OOO0O00 .token ,'timestamp':OO0OOO00OOO00O0OO ,'sign':sign (OO0000O0OOO00O0OO ),'signstring':OO0000O0OOO00O0OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:440
            OO00O000O00O00O0O =requests .request ('patch',f'{host}/user/nickname',headers =O00OOO0000000O00O ,data =OOO0000O0000OO00O ).json ()#line:441
            if 'status'in OO00O000O00O00O0O :#line:443
                if OO00O000O00O00O0O ['status']==200 :#line:444
                    print (f'【修改网名】:网名:{O00OO0OOOOO0OOO00}丨{OO00O000O00O00O0O["message"]}')#line:445
        except Exception as OOOO000OO000OO0O0 :#line:446
            print (OOOO000OO000OO0O0 )#line:447
    def withdraw (OOO0O0000OO000000 ):#line:450
        try :#line:451
            OO00OOO00000000OO =f'__{timi_new()}'#line:452
            OO0O0O0OO000O000O ={'source':'scsc','authorization':OOO0O0000OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00000000OO ),'signstring':OO00OOO00000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O0OOOO0O0O0OOO0OO =requests .request ('get',f'{host}/assets',headers =OO0O0O0OO000O000O ).json ()#line:464
            if 'status'in O0OOOO0O0O0OOO0OO :#line:466
                if O0OOOO0O0O0OOO0OO ['status']==200 :#line:467
                    OO0O00OOOO0OO0OOO =O0OOOO0O0O0OOO0OO ['data']['cash']#line:468
                    if float (OO0O00OOOO0OO0OOO )>20 :#line:469
                        OO00OOO00000000OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:470
                        OO0O0O0OO000O000O ={'authorization':OOO0O0000OO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00000000OO ),'signstring':OO00OOO00000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
                        O00OOO0000OO0O000 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:481
                        O000OOOOOO0OO00OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0O0O0OO000O000O ,data =O00OOO0000OO0O000 ).json ()#line:483
                        if 'status'in O000OOOOOO0OO00OO :#line:485
                            if O000OOOOOO0OO00OO ['status']==200 :#line:486
                                print (f'【余额提现】:{O000OOOOOO0OO00OO["data"]}')#line:487
                        if 'status'in O000OOOOOO0OO00OO :#line:488
                            if O000OOOOOO0OO00OO ['status']==500 :#line:489
                                print (f'【余额提现】:{O000OOOOOO0OO00OO["message"]}')#line:490
        except Exception as O0OOOOOOOO000OO0O :#line:491
            print (O0OOOOOOOO000OO0O )#line:492
    def invitenum (O0O0000OO00OO00OO ):#line:495
        global invited_new #line:496
        try :#line:497
            O0OO0OOO00000OO00 =f'__{timi_new()}'#line:498
            O00000O0O0OOOO0OO ={'source':'scsc','authorization':O0O0000OO00OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00000OO00 ),'signstring':O0OO0OOO00000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:509
            O0000O0OO0O00OOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O00000O0O0OOOO0OO ).json ()#line:510
            if 'status'in O0000O0OO0O00OOO0 :#line:512
                if O0000O0OO0O00OOO0 ['status']==200 :#line:513
                    O000OOO0O000OO00O =O0000O0OO0O00OOO0 ['data']['invited_count']#line:514
                    OOO00000000OOO0OO =O0000O0OO0O00OOO0 ['data']['invited_second_count']#line:515
                    print (f'【我的邀请】:直邀好友:{O000OOO0O000OO00O}丨间邀好友:{OOO00000000OOO0OO}')#line:516
                    if O000OOO0O000OO00O <2 :#line:517
                        OO00OO0OO0OO0O0OO =f'__{timi_new()}'#line:518
                        O0O00OO0OO00O0OOO ={'source':'scsc','authorization':O0O0000OO00OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OO0O0OO ),'signstring':OO00OO0OO0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:529
                        O00OOO00OO00O0O00 =requests .request ('get',f'{host}/user',headers =O0O00OO0OO00O0OOO ).json ()#line:530
                        if 'status'in O00OOO00OO00O0O00 :#line:532
                            if O00OOO00OO00O0O00 ['status']==200 :#line:533
                                invited_new .append (O00OOO00OO00O0O00 ['data']['inner_id'])#line:534
        except Exception as OOOO0O0O0OOOOO0OO :#line:535
            print (OOOO0O0O0OOOOO0OO )#line:536
    def game_map (O00000OOO000OOOOO ):#line:539
        try :#line:540
            O000OO000O000O00O =f'__{timi_new()}'#line:541
            O00OO00OO000O00O0 ={'source':'scsc','authorization':O00000OOO000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O000O00O ),'signstring':O000OO000O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            O0000OOO00000OOOO =requests .request ('get',f'{host}/game/map',headers =O00OO00OO000O00O0 ).json ()#line:553
            if 'status'in O0000OOO00000OOOO :#line:555
                if O0000OOO00000OOOO ['status']==200 :#line:556
                    for OO00O0OO00O000000 in O0000OOO00000OOOO ['data']['list'][0 ]['crops']:#line:557
                        OO00O0OO0OO00O0OO =OO00O0OO00O000000 ['level']#line:559
                        if OO00O0OO0OO00O0OO ==41 :#line:560
                            OO0O0OOO0OO0O0OOO =OO00O0OO00O000000 ['crop_name']#line:561
                            O0O00O000O00OOO00 =OO00O0OO00O000000 ['count']#line:562
                            if O0O00O000O00OOO00 >0 :#line:563
                                print (f'【农业资产】:{OO0O0OOO0OO0O0OOO}丨数量:{O0O00O000O00OOO00}')#line:564
                                O00OO00O0O0OO0OO0 =O00000OOO000OOOOO .the_query ()#line:565
                                O00000OOO000OOOOO .market_sale (O00OO00O0O0OO0OO0 )#line:566
        except Exception as OO00O0O0OOO00OOO0 :#line:567
            print (OO00O0O0OOO00OOO0 )#line:568
    def give_gold (O00O0OOO00000O00O ):#line:571
        try :#line:572
            OO000OO0OOO00OOO0 =f'__{timi_new()}'#line:573
            O00O0OOOO0O0O00O0 ={'source':'scsc','authorization':O00O0OOO00000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OOO00OOO0 ),'signstring':OO000OO0OOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:584
            O00000OOO00OOOO0O =requests .request ('get',f'{host}/user',headers =O00O0OOOO0O0O00O0 ).json ()#line:585
            if 'status'in O00000OOO00OOOO0O :#line:586
                if O00000OOO00OOOO0O ['status']==200 :#line:587
                    if float (O00O0OOO00000O00O .doneeNo )!=0 :#line:588
                        OOO00OOO000O0O00O =O00000OOO00OOOO0O ['data']['assets']['gold']#line:589
                        if float (OOO00OOO000O0O00O )>float (O00O0OOO00000O00O .innerId ):#line:590
                            OOO00000O0O00O000 =int (float (OOO00OOO000O0O00O )/1.1 )#line:591
                            OO000OO0OOO00OOO0 =f'_doneeNo={O00O0OOO00000O00O.doneeNo}&quantity={OOO00000O0O00O000}_{timi_new()}'#line:592
                            O00O0OOOO0O0O00O0 ={'source':'scsc','authorization':O00O0OOO00000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0OOO00OOO0 ),'signstring':OO000OO0OOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:603
                            OOO0OO0O000OO000O ={"quantity":OOO00000O0O00O000 ,"doneeNo":O00O0OOO00000O00O .doneeNo }#line:607
                            OOOOOO0000OO0O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0OOOO0O0O00O0 ,data =OOO0OO0O000OO000O ).json ()#line:608
                            if 'status'in OOOOOO0000OO0O0O0 :#line:610
                                if OOOOOO0000OO0O0O0 ['status']==200 :#line:611
                                    if OOOOOO0000OO0O0O0 ['data']:#line:612
                                        print (f'【赠送种子】:赠送{OOO00000O0O00O000}种子给{O00O0OOO00000O00O.doneeNo}成功')#line:613
                    else :#line:614
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:615
        except Exception as O00O0000O000O00OO :#line:616
            print (O00O0000O000O00OO )#line:617
    def invitation (O0000OO0O0O00OO0O ):#line:619
        try :#line:620
            _O00OO00OOOOO000OO =float (bundled_def ())/4 #line:621
            O00OO000000O0O00O =f'_innerId={int(_O00OO00OOOOO000OO)}_{timi_new()}'#line:623
            OO000OOOO0O0O0O00 ={'source':'scsc','authorization':O0000OO0O0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000000O0O00O ),'signstring':O00OO000000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OO000OO0O0OOO00O0 ={"innerId":int (_O00OO00OOOOO000OO )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO000OOOO0O0O0O00 ,data =OO000OO0O0OOO00O0 )#line:636
        except Exception as OOOO00OOO00OOO0O0 :#line:637
            print (OOOO00OOO00OOO0O0 )#line:638
    def winning_rewards (O0OO00OO0O0OOO0OO ):#line:641
        try :#line:642
            OO0OO000000O0OOO0 =f'__{timi_new()}'#line:643
            O0000O0O00OOO0000 ={'source':'scsc','authorization':O0OO00OO0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000000O0OOO0 ),'signstring':OO0OO000000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            O0O00000OO0O00000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O0O00OOO0000 ).json ()#line:655
            if 'status'in O0O00000OO0O00000 :#line:657
                if O0O00000OO0O00000 ['status']==200 :#line:658
                    if O0O00000OO0O00000 ['data']['amount']:#line:659
                        O00O000O000O00OO0 =O0O00000OO0O00000 ['data']['amount']['gold']#line:660
                        return O00O000O000O00OO0 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as O0OOOOO00OOOOOOO0 :#line:664
            print (O0OOOOO00OOOOOOO0 )#line:665
    def certification (OO000O0O0O00OO00O ):#line:668
        try :#line:669
            O00O00OO0O00O0O0O =f'__{timi_new()}'#line:670
            O0000O000O00OO0OO ={'source':'scsc','authorization':OO000O0O0O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO0O00O0O0O ),'signstring':O00O00OO0O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            OOO000O00O0O00OOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000O000O00OO0OO ).json ()#line:682
            if 'status'in OOO000O00O0O00OOO :#line:684
                if OOO000O00O0O00OOO ['status']==200 :#line:685
                    if OOO000O00O0O00OOO ['data']['result']:#line:686
                        OOO0000OOOO0O00OO =OOO000O00O0O00OOO ['data']['nick_name']#line:687
                        return OOO0000OOOO0O00OO #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as OOOOO0OO000OO0000 :#line:691
            print (OOOOO0OO000OO0000 )#line:692
    def crops_illustrated (OO0OOO0O000O0O0OO ):#line:695
        try :#line:696
            OO00OO0OO0OO0O00O =f'__{timi_new()}'#line:697
            O00O0OO00OOOOOO0O ={'source':'scsc','authorization':OO0OOO0O000O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OO0O00O ),'signstring':OO00OO0OO0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            OOOO0OO00O00OO000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0OO00OOOOOO0O ).json ()#line:709
            if 'status'in OOOO0OO00O00OO000 :#line:711
                if OOOO0OO00O00OO000 ['status']==200 :#line:712
                    O0OO0000000O0OOOO =OOOO0OO00O00OO000 ['data'][0 ]['crops']#line:713
                    for OOOOO0O0OO000O0OO in O0OO0000000O0OOOO :#line:714
                        if OOOOO0O0OO000O0OO ['ill_clover_award']:#line:715
                            if float (OOOOO0O0OO000O0OO ['ill_clover_award'])>1 :#line:716
                                if OOOOO0O0OO000O0OO ['is_finish']:#line:717
                                    if not OOOOO0O0OO000O0OO ['is_getit']:#line:718
                                        if OO0OOO0O000O0O0OO .certification ()!='未实名':#line:719
                                            OO00OO0OO0OO0O00O =f'_award_level={OOOOO0O0OO000O0OO["level"]}_{timi_new()}'#line:720
                                            O00O0OO00OOOOOO0O ={'source':'scsc','authorization':OO0OOO0O000O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0OO0OO0O00O ),'signstring':OO00OO0OO0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            OOOOOO00000000000 ={"award_level":OOOOO0O0OO000O0OO ['level']}#line:732
                                            O00O0OOO0OO000000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0OO00OOOOOO0O ,json =OOOOOO00000000000 ).json ()#line:734
                                            if 'status'in O00O0OOO0OO000000 :#line:735
                                                if O00O0OOO0OO000000 ['status']==200 :#line:736
                                                    OO0O00000OO00OO0O =O00O0OOO0OO000000 ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{OOOOO0O0OO000O0OO["crop_name"]}成就丨奖励{OO0O00000OO00OO0O}☘️')#line:739
                                                if O00O0OOO0OO000000 ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{O00O0OOO0OO000000["message"]}')#line:741
        except Exception as OO0O0000OOO0O00OO :#line:742
            print (OO0O0000OOO0O00OO )#line:743
    def watched_ad (O00O0000OOOOO0OOO ):#line:746
        try :#line:747
            OOO0000OOO0OO0OOO =f'__{timi_new()}'#line:748
            O0000O00O00O000O0 ={'source':'scsc','authorization':O00O0000OOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOO0OO0OOO ),'signstring':OOO0000OOO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            O0OO00OOOO0OOO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O00O00O000O0 ).json ()#line:760
            if 'status'in O0OO00OOOO0OOO000 :#line:762
                if O0OO00OOOO0OOO000 ['status']==200 :#line:763
                    if 'offlineInfo'in O0OO00OOOO0OOO000 ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        O0OO00000OOOO0O00 =O0OO00OOOO0OOO000 ['data']['offlineInfo']['off_minute']#line:766
                        OO00OOOO0000OOOO0 =float (O0OO00OOOO0OOO000 ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0000O00O00O000O0 ).json ()#line:769
                        time .sleep (2 )#line:770
                        O0000O000000OOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O00O00O000O0 ).json ()#line:771
                        if 'status'in O0000O000000OOO00 :#line:773
                            if O0000O000000OOO00 ['status']==200 :#line:774
                                O0000O0O000OOO0OO =float (O0000O000000OOO00 ['data']['silver'])/1000000000000 #line:775
                                O0OO0O0OOO0OO0OOO =str (O0000O0O000OOO0OO -OO00OOOO0000OOOO0 )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{O0OO00000OOOO0O00}分钟奖励🌱数量:{O0OO0O0OOO0OO0OOO}t粒')#line:777
        except Exception as O00OO0OO0OOOO000O :#line:778
            print (O00OO0OO0OOOO000O )#line:779
    def user_ad (OOOO0OOOOOO00OOO0 ):#line:782
        try :#line:783
            OO000OO0000O0O0OO =f'__{timi_new()}'#line:784
            OO00OOO0O00O0O00O ={'source':'scsc','authorization':OOOO0OOOOOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0000O0O0OO ),'signstring':OO000OO0000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            O0O00OOOO00O00O0O =requests .request ('get',f'{host}/user/ad',headers =OO00OOO0O00O0O00O ).json ()#line:796
            if 'status'in O0O00OOOO00O00O0O :#line:798
                if O0O00OOOO00O00O0O ['status']==200 :#line:799
                    OO00O000000O0OOO0 =O0O00OOOO00O00O0O ['data']['max_time']#line:800
                    O000O00O0000O00OO =O0O00OOOO00O00O0O ['data']['watch_time']#line:801
                    O000OO0OOO0O0O0OO =O0O00OOOO00O00O0O ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{O000OO0OOO0O0O0OO + OO00O000000O0OOO0 - O000O00O0000O00OO}次丨好友提供:{O000OO0OOO0O0O0OO}次')#line:803
                    if O000OO0OOO0O0O0OO +OO00O000000O0OOO0 -O000O00O0000O00OO >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        O00O0O0O0OOOOO00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OOO0O00O0O00O ).json ()#line:806
                        if 'status'in O00O0O0O0OOOOO00O :#line:808
                            if O00O0O0O0OOOOO00O ['status']==200 :#line:809
                                O0000O0O0O0OO0OOO =float (O00O0O0O0OOOOO00O ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(O0000O0O0O0OO0OOO)}t粒')#line:811
                                return True #line:812
                            if O00O0O0O0OOOOO00O ['status']==500 :#line:813
                                O0OO000O0O0OO00O0 =O00O0O0O0OOOOO00O ['message']#line:814
                                print (f'【获取种子】:{O0OO000O0O0OO00O0}')#line:815
                                return False #line:816
        except Exception as OO000000000O000O0 :#line:817
            print (OO000000000O000O0 )#line:818
    def synthetic (OOOO000O0O0OO00OO ):#line:821
        global id ,g #line:822
        try :#line:823
            OO0O0O0OOO000OOOO =OOOO000O0O0OO00OO .level_new ()#line:824
            O0OOOO0OO0O000O0O =random .randint (9 ,11 )#line:825
            OO0OOO00OOO000O00 =f'_site=8&targetSite={O0OOOO0OO0O000O0O}_{timi_new()}'#line:826
            O0OO00O0000OOOO00 ={'source':'scsc','authorization':OOOO000O0O0OO00OO .token ,'timestamp':timi_new (),'sign':sign (OO0OOO00OOO000O00 ),'signstring':OO0OOO00OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            O000O00O0OOOO0OO0 ={"site":int (8 ),"targetSite":int (O0OOOO0OO0O000O0O )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00O0000OOOO00 ,json =O000O00O0OOOO0OO0 )#line:839
            while True :#line:840
                O0O00OOO0OO0OOOO0 =f'__{timi_new()}'#line:841
                O0OO00OOOO0O00O0O ={'source':'scsc','authorization':OOOO000O0O0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO0OO0OOOO0 ),'signstring':O0O00OOO0OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                OO00O00O0O00OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00OOOO0O00O0O ).json ()#line:853
                if 'status'in OO00O00O0O00OO0OO :#line:855
                    if OO00O00O0O00OO0OO ['status']==200 :#line:856
                        OOO0OO00O000O00OO =OO00O00O0O00OO0OO ['data']['cropList']#line:857
                        O00OOOO0OO000OOOO =OO00O00O0O00OO0OO ['data']['gameCoreDataDBid']#line:858
                        OO0OOO000O0O0O0O0 =float (OO00O00O0O00OO0OO ['data']['silver'])/1000000000000 #line:859
                        O0O00O0OOO0000O00 =0 #line:864
                        for OOOO0OO0O0O00O00O in OOO0OO00O000O00OO :#line:865
                            if not OOOO0OO0O0O00O00O :#line:866
                                O000OO0OO0OOO0OOO =f'_crop_id={O00OOOO0OO000OOOO}&site={O0O00O0OOO0000O00}_{OOOO000O0O0OO00OO.time}'#line:867
                                OO0OO0000O0OO0OO0 ={'source':'scsc','authorization':OOOO000O0O0OO00OO .token ,'timestamp':OOOO000O0O0OO00OO .time ,'sign':sign (O000OO0OO0OOO0OOO ),'signstring':O000OO0OO0OOO0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                OOO00000O00O0O0O0 ={"site":O0O00O0OOO0000O00 ,"crop_id":O00OOOO0OO000OOOO }#line:878
                                O0O00OO00O0000OO0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0OO0000O0OO0OO0 ,data =OOO00000O00O0O0O0 ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in O0O00OO00O0000OO0 :#line:882
                                    if O0O00OO00O0000OO0 ['status']==200 :#line:883
                                        if O0O00OO00O0000OO0 ['message']=='种子数量不足':#line:884
                                            OO0O0O0OOO000OOOO =OOOO000O0O0OO00OO .level_new ()#line:885
                                            print (f'【种植合成】:{O0O00OO00O0000OO0["message"]}')#line:886
                                            if not OOOO000O0O0OO00OO .user_ad ():#line:887
                                                return False #line:888
                                    if O0O00OO00O0000OO0 ['status']==500 :#line:889
                                        print (f'【种植合成】:{O0O00OO00O0000OO0["message"]}')#line:890
                                        return False #line:891
                            O0O00O0OOO0000O00 +=1 #line:892
                        O00OOO00OOOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00OOOO0O00O0O ).json ()#line:893
                        OOOOO0OOOOOOOOOO0 =O00OOO00OOOOOO0O0 ['data']['cropList']#line:894
                        OO00OOOO00O00O0O0 =False #line:895
                        for OOOO0OO0O0O00O00O in range (12 ):#line:896
                            id =OOOOO0OOOOOOOOOO0 [OOOO0OO0O0O00O00O ]['level']#line:897
                            if float (OO0O0O0OOO000OOOO )-float (id )>9 :#line:898
                                OO0O0O0O0OO0OO0OO =f'_site={OOOO0OO0O0O00O00O}_{timi_new()}'#line:899
                                OO00O000000OO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000O0O0OO00OO .token ,'timestamp':timi_new (),'sign':sign (OO0O0O0O0OO0OO0OO ),'signstring':OO0O0O0O0OO0OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                OOO0OOO0OOOO00OO0 ={"site":OOOO0OO0O0O00O00O }#line:911
                                OO00O0OO0OOO0O0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00O000000OO0OOO ,data =OOO0OOO0OOOO00OO0 ).json ()#line:913
                                if 'status'in OO00O0OO0OOO0O0OO :#line:914
                                    if OO00O0OO0OOO0O0OO ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O0O0000O0OO00OOOO in range (11 ):#line:918
                                    O0000OOO00OO00O0O =O0O0000O0OO00OOOO +1 #line:919
                                    g =OOOOO0OOOOOOOOOO0 [O0000OOO00OO00O0O ]['level']#line:920
                                    if id ==g :#line:921
                                        OOOOOO000O0O0O00O =O0O0000O0OO00OOOO +2 #line:922
                                        if OOOOOO000O0O0O00O !=OOOO0OO0O0O00O00O +1 :#line:923
                                            OO0000OOOO00O0OOO =OOOO0OO0O0O00O00O +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            OO0OOO00OOO000O00 =f'_site={OO0000OOOO00O0OOO - 1}&targetSite={OOOOOO000O0O0O00O - 1}_{timi_new()}'#line:927
                                            O0OO00O0000OOOO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO000O0O0OO00OO .token ,'timestamp':timi_new (),'sign':sign (OO0OOO00OOO000O00 ),'signstring':OO0OOO00OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            OO00OO0O00OOO0O00 ={"site":int (OO0000OOOO00O0OOO -1 ),"targetSite":int (OOOOOO000O0O0O00O -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00O0000OOOO00 ,json =OO00OO0O00OOO0O00 )#line:946
                                            OO00OOOO00O00O0O0 =True #line:948
                                    if OO00OOOO00O00O0O0 :#line:949
                                        break #line:950
                                if OO00OOOO00O00O0O0 :#line:951
                                    break #line:952
        except :#line:953
            OOOO000O0O0OO00OO .synthetic ()#line:954
    def level_new (OO0000O0OOOOOO0O0 ):#line:957
        try :#line:958
            OOOOOOOO000OO00O0 =f'__{timi_new()}'#line:959
            O00OOOO0OO0OO0OOO ={'source':'scsc','authorization':OO0000O0OOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOO000OO00O0 ),'signstring':OOOOOOOO000OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            O00OO0O0OOOOOOO0O =requests .request ('get',f'{host}/user',headers =O00OOOO0OO0OO0OOO ).json ()#line:971
            if 'status'in O00OO0O0OOOOOOO0O :#line:972
                if O00OO0O0OOOOOOO0O ['status']==200 :#line:973
                    return float (O00OO0O0OOOOOOO0O ['data']['level'])#line:974
        except Exception as O0OO0000O0O000O0O :#line:975
            print (O0OO0000O0O000O0O )#line:976
    def propsraffle (OO0000000O00000O0 ):#line:979
        try :#line:980
            while True :#line:981
                O00000O00000O000O =f'__{timi_new()}'#line:982
                O00O000000OO0O000 ={'source':'scsc','authorization':OO0000000O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00000O000O ),'signstring':O00000O00000O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                O000O0O0O0O0O0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00O000000OO0O000 ).json ()#line:994
                if 'status'in O000O0O0O0O0O0OO0 :#line:996
                    if O000O0O0O0O0O0OO0 ['status']==200 :#line:997
                        OO00O00O0OO00OOOO =O000O0O0O0O0O0OO0 ['data']['rows']#line:998
                        O0O000OOO0OO00O0O =O000O0O0O0O0O0OO0 ['data']['vstate']#line:999
                        if OO00O00O0OO00OOOO ==5 or OO00O00O0OO00OOOO ==6 or OO00O00O0OO00OOOO ==7 :#line:1000
                            OOO000OO0O0OOO00O =O000O0O0O0O0O0OO0 ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{OOO000OO0O0OOO00O}')#line:1002
                        if OO00O00O0OO00OOOO ==1 or OO00O00O0OO00OOOO ==2 or OO00O00O0OO00OOOO ==3 :#line:1003
                            O0000000000O00O00 =O000O0O0O0O0O0OO0 ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O0000000000O00O00}')#line:1005
                        if OO00O00O0OO00OOOO ==4 or OO00O00O0OO00OOOO ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if OO00O00O0OO00OOOO =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as OO0OO0000OOO0O0O0 :#line:1047
            print (OO0OO0000OOO0O0O0 )#line:1048
    def friends_invitation (OOOOOOO0OO00O0O0O ):#line:1051
        try :#line:1052
            O000O00OOOO0000O0 =f'__{timi_new()}'#line:1053
            O00O0O0O00O0000OO ={'source':'scsc','authorization':OOOOOOO0OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOOO0000O0 ),'signstring':O000O00OOOO0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            O0O000O00O0OOO00O =requests .request ('get',f'{host}/friends',headers =O00O0O0O00O0000OO ).json ()#line:1065
            if 'status'in O0O000O00O0OOO00O :#line:1066
                if O0O000O00O0OOO00O ['status']==200 :#line:1067
                    O0OO0O000O00O0000 =O0O000O00O0OOO00O ['data']['myInviteter']#line:1068
                    if O0OO0O000O00O0000 :#line:1069
                        OO0OOO0OOO0O00000 =O0OO0O000O00O0000 ['user']['nickname']#line:1070
                        OO00O0OO00OO0OOO0 =OOOOOOO0OO00O0O0O .certification ()#line:1071
                        if OO00O0OO00OO0OOO0 =='未实名':#line:1072
                            weishim .append (OOOOOOO0OO00O0O0O .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{OO0OOO0OOO0O00000}丨实名:{OO00O0OO00OO0OOO0}')#line:1074
        except Exception as OO0O0O00OOO00O00O :#line:1078
            print (OO0O0O00OOO00O00O )#line:1079
    def add_clover (O0OOO0O000O0O00OO ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            O0OO0OO00O0O000OO =f'__{timi_new()}'#line:1085
            OOO0OO0000000O0OO ={'source':'scsc','authorization':O0OOO0O000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00O0O000OO ),'signstring':O0OO0OO00O0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OO00000O000O0000O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0OO0000000O0OO ).json ()#line:1097
            if 'status'in OO00000O000O0000O :#line:1099
                if OO00000O000O0000O ['status']==200 :#line:1100
                    OOO00000O00O0OO00 =OO00000O000O0000O ['data']['clover']#line:1101
                    O0OO0O00OOOO00000 =OO00000O000O0000O ['data']['used_clover']#line:1102
                    OO0O0OO0O0O00O00O =float (OOO00000O00O0OO00 )-float (O0OO0O00OOOO00000 )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0O00OOOO00000}')#line:1104
                    if O0OOO0O000O0O00OO .certification ()!='未实名':#line:1105
                        if OO0O0OO0O0O00O00O >1 :#line:1106
                            O0OO0OO00O0O000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0OO0O0O00O00O)}_{timi_new()}'#line:1107
                            OOO000OO0O00OO00O ={'source':'scsc','authorization':O0OOO0O000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00O0O000OO ),'signstring':O0OO0OO00O0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            OOO00O000O00OO000 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0OO0O0O00O00O )}#line:1119
                            O0OO0OOO0O00O0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO000OO0O00OO00O ,data =OOO00O000O00OO000 ).json ()#line:1120
                            if 'status'in O0OO0OOO0O00O0OOO :#line:1122
                                if O0OO0OOO0O00O0OOO ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OOO0O00O0OOO["data"]["isSuccess"]}丨数量:{OO0O0OO0O0O00O00O}')#line:1124
                                if O0OO0OOO0O00O0OOO ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OOO0O00O0OOO["message"]}')#line:1126
            OOOOO00000000O0O0 =requests .request ('get',f'{host}/lottery',headers =OOO0OO0000000O0OO ).json ()#line:1127
            OOO0OO0000O0O0OO0 =O0OOO0O000O0O00OO .winning_rewards ()#line:1129
            if 'status'in OOOOO00000000O0O0 :#line:1130
                if OOOOO00000000O0O0 ['status']==200 :#line:1131
                    OO0OO0O0000OOOOO0 =OOOOO00000000O0O0 ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (OO0OO0O0000OOOOO0 )#line:1133
                    O0O0O0O0O0OOOO0O0 =OOOOO00000000O0O0 ['data'][1 ]['value']#line:1134
                    O000000OOO00O0000 =OOOOO00000000O0O0 ['data'][0 ]['join_number']#line:1135
                    OO00O0000O0O00000 =int (float (OOOOO00000000O0O0 ['data'][0 ]['totalValue']))#line:1136
                    O0OOO0OOO0OO0O0O0 =float (O0O0O0O0O0OOOO0O0 /OO00O0000O0O00000 )*10000 #line:1137
                    OO0O0O000OO000O00 =OO00O0000O0O00000 /O000000OOO00O0000 #line:1138
                    print (f'【参与抽奖】:预计每天中{str(OO0OO0O0000OOOOO0)[:6]}颗金种子丨好友收益:{str(OOO0OO0000O0O0OO0)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO0OOO0OO0O0O0)[:6]}颗金种子丨☘️人均:{str(OO0O0O000OO000O00)[:7]}️')#line:1140
        except Exception as O00000OO0OO00O00O :#line:1141
            print (O00000OO0OO00O00O )#line:1142
    def energy (O00OOOOO0OOOOO0OO ):#line:1145
        try :#line:1146
            while True :#line:1147
                O00OOO0OOOOOO0OOO =f'__{timi_new()}'#line:1148
                O0O0O0000OOOOOOOO ={'source':'scsc','authorization':O00OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOOOOO0OOO ),'signstring':O00OOO0OOOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                OOO000O0O0OOO000O =requests .request ('get',f'{host}/energy/general',headers =O0O0O0000OOOOOOOO ).json ()#line:1160
                if 'status'in OOO000O0O0OOO000O :#line:1162
                    if OOO000O0O0OOO000O ['status']==200 :#line:1163
                        O0O0000OOO0OO0OOO =OOO000O0O0OOO000O ['data']['ordinary_water']#line:1164
                        O0O0OO0OOOOOO000O =OOO000O0O0OOO000O ['data']['ordinary_fertilizer']#line:1165
                        O000OOO0O0OOO0O0O =OOO000O0O0OOO000O ['data']['videoStatus']#line:1166
                        OO00O0O000OOO0O00 =OOO000O0O0OOO000O ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(O0O0OO0OOOOOO000O).split(".")[0]}丨水滴:{str(O0O0000OOO0OO0OOO).split(".")[0]}')#line:1169
                        if float (O0O0OO0OOOOOO000O )<96 :#line:1170
                            if O000OOO0O0OOO0O0O :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OO00OO0O00O0OOO0O =99 -float (O0O0OO0OOOOOO000O )#line:1173
                                O00O0O0000OO0O000 ={"fertilizer":str (OO00OO0O00O0OOO0O ).split ('.')[0 ]}#line:1174
                                O0O0O00000O00O0OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O0O0000OOOOOOOO ).json ()#line:1176
                                if 'status'in O0O0O00000O00O0OO :#line:1178
                                    if O0O0O00000O00O0OO ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0O00000O00O0OO["message"]}')#line:1180
                                    if O0O0O00000O00O0OO ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{O0O0O00000O00O0OO["message"]}')#line:1182
                                        break #line:1183
                                if float (O0O0OO0OOOOOO000O )<78 :#line:1185
                                    OO00OO0O00O0OOO0O =80 -float (O0O0OO0OOOOOO000O )#line:1186
                                    OOO0OO0O0O0OO00O0 =f'_fertilizer={int(OO00OO0O00O0OOO0O)}_{timi_new()}'#line:1187
                                    O0OO000OOOO0000O0 ={'source':'scsc','authorization':O00OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0O0OO00O0 ),'signstring':OOO0OO0O0O0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    OOO00O0OOO000OO0O ={"fertilizer":int (OO00OO0O00O0OOO0O )}#line:1199
                                    OOO00O0O0OOOO00OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OO000OOOO0000O0 ,data =OOO00O0OOO000OO0O ).json ()#line:1201
                                    if 'status'in OOO00O0O0OOOO00OO :#line:1203
                                        if OOO00O0O0OOOO00OO ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OOO00O0O0OOOO00OO["message"]}丨数量:{int(OO00OO0O00O0OOO0O)}')#line:1205
                                        if OOO00O0O0OOOO00OO ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OOO00O0O0OOOO00OO["message"]}丨数量:{int(OO00OO0O00O0OOO0O)}')#line:1207
                                            OO00OOO0OO0O0OOOO =OOO00O0O0OOOO00OO ["message"].split ('-')[1 ]#line:1208
                                            OOO0OOO0000O000OO =f'__{timi_new()}'#line:1209
                                            O0O0O00OO000OOOO0 ={'source':'scsc','authorization':O00OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0000O000OO ),'signstring':OOO0OOO0000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            O0O000OO00O00OOO0 =requests .request ('get',f'{host}/user',headers =O0O0O00OO000OOOO0 ).json ()#line:1221
                                            if 'status'in O0O000OO00O00OOO0 :#line:1222
                                                if O0O000OO00O00OOO0 ['status']==200 :#line:1223
                                                    OOO0O0OO00O0O0OO0 =O0O000OO00O00OOO0 ['data']['inner_id']#line:1224
                                                    if give_gold (OOO0O0OO00O0O0OO0 ,float (OO00OOO0OO0O0OOOO )+1 ):#line:1225
                                                        O00OOOOO0OOOOO0OO .energy ()#line:1226
                        if float (O0O0000OOO0OO0OOO )<880 :#line:1227
                            if OO00O0O000OOO0O00 :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                OOO000OOO0O00OO00 =999 -float (O0O0000OOO0OO0OOO )#line:1230
                                O0OO0O000OO0000O0 ={"water":str (OOO000OOO0O00OO00 ).split ('.')[0 ]}#line:1231
                                O000OO0OO0OOOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O0O0000OOOOOOOO ).json ()#line:1233
                                if 'status'in O000OO0OO0OOOO0O0 :#line:1235
                                    if O000OO0OO0OOOO0O0 ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{O000OO0OO0OOOO0O0["message"]}')#line:1237
                                    if O000OO0OO0OOOO0O0 ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O000OO0OO0OOOO0O0["message"]}')#line:1239
                                        break #line:1240
                                if float (O0O0000OOO0OO0OOO )<780 :#line:1241
                                    OOO000OOO0O00OO00 =800 -float (O0O0000OOO0OO0OOO )#line:1242
                                    OOO000OO0O0OO00OO =f'_water={int(OOO000OOO0O00OO00)}_{timi_new()}'#line:1243
                                    O000OOO0OOOO0OO00 ={'source':'scsc','authorization':O00OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0O0OO00OO ),'signstring':OOO000OO0O0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    O0O0000000OOOO00O ={"water":int (OOO000OOO0O00OO00 )}#line:1255
                                    O000OO0OOOOOOO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000OOO0OOOO0OO00 ,data =O0O0000000OOOO00O ).json ()#line:1257
                                    if 'status'in O000OO0OOOOOOO00O :#line:1259
                                        if O000OO0OOOOOOO00O ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O000OO0OOOOOOO00O["message"]}丨数量:{int(OOO000OOO0O00OO00)}')#line:1261
                                        if O000OO0OOOOOOO00O ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O000OO0OOOOOOO00O["message"]}丨数量:{int(OOO000OOO0O00OO00)}')#line:1263
                                            OO00OOO0OO0O0OOOO =O000OO0OOOOOOO00O ["message"].split ('-')[1 ]#line:1264
                                            OOO0OOO0000O000OO =f'__{timi_new()}'#line:1265
                                            O0O0O00OO000OOOO0 ={'source':'scsc','authorization':O00OOOOO0OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0000O000OO ),'signstring':OOO0OOO0000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            O0O000OO00O00OOO0 =requests .request ('get',f'{host}/user',headers =O0O0O00OO000OOOO0 ).json ()#line:1277
                                            if 'status'in O0O000OO00O00OOO0 :#line:1278
                                                if O0O000OO00O00OOO0 ['status']==200 :#line:1279
                                                    OOO0O0OO00O0O0OO0 =O0O000OO00O00OOO0 ['data']['inner_id']#line:1280
                                                    if give_gold (OOO0O0OO00O0O0OO0 ,float (OO00OOO0OO0O0OOOO )+1 ):#line:1281
                                                        O00OOOOO0OOOOO0OO .energy ()#line:1282
                        break #line:1283
        except Exception as O00O0O0OO0O000O00 :#line:1284
            print (O00O0O0OO0O000O00 )#line:1285
def bundled_def ():#line:1288
    O00O00000OOO0OO0O =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return O00O00000OOO0OO0O [random .randint (0 ,len (O00O00000OOO0OO0O )-1 )]#line:1290
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
        OO000OOOOOOOO00O0 =gitee_edition ()#line:1329
        if version_of_the_validation ()<OO000OOOOOOOO00O0 ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OOOOOOOO00O0["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{OO000OOOOOOOO00O0["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OOOOOOOO00O0["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {OO000OOOOOOOO00O0["CityEarth"]["content"]}')#line:1335
    except Exception as OO0O00OOO00000O00 :#line:1336
        print (OO0O00OOO00000O00 )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
