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
@ 版本  4.6
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
        OO000O0O0O00OO000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO000O0O0O00OO000)}个账号==========")#line:17
        for O00O0OOO0OOO0OOO0 in OO000O0O0O00OO000 :#line:18
            OO0OO0000000O000O =[]#line:19
            print (f"------------正在执行第{OO000O0O0O00OO000.index(O00O0OOO0OOO0OOO0) + 1}个账号------------")#line:20
            OO00OOO0O00OOO00O =CityEarth (O00O0OOO0OOO0OOO0 ,OO0OO0000000O000O ,OO000O0O0O00OO000 .index (O00O0OOO0OOO0OOO0 ))#line:21
            def O00O00OOOO0OOO000 ():#line:23
                if OO00OOO0O00OOO00O .base_info ():#line:25
                    OO00OOO0O00OOO00O .sealing ()#line:27
                    OO00OOO0O00OOO00O .invitenum ()#line:29
                    OO00OOO0O00OOO00O .query_to_sell ()#line:31
                    OO00OOO0O00OOO00O .friends_invitation ()#line:35
                    OO00OOO0O00OOO00O .energy ()#line:37
                    OO00OOO0O00OOO00O .add_clover ()#line:39
                    OO00OOO0O00OOO00O .propsraffle ()#line:41
                    OO00OOO0O00OOO00O .synthetic ()#line:43
                    OO00OOO0O00OOO00O .crops_illustrated ()#line:45
                    OO00OOO0O00OOO00O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO00OOO0O00OOO00O .give_gold ()#line:50
            O00OOO000O00O00O0 =threading .Thread (target =O00O00OOOO0OOO000 )#line:52
            O00OOO000O00O00O0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO000OOOO0OO00OO0 =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO000OOOO0OO00OO0 +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0OO0OOOO00O00000 in invited_new :#line:62
            print (O0OO0OOOO00O00000 )#line:63
        print ('开始打印未实名的token')#line:64
        for OO00O0000OOOOO0OO in weishim :#line:65
            print (OO00O0000OOOOO0OO )#line:66
    except Exception as O00O00000OO0OO0O0 :#line:67
        print (O00O00000OO0OO0O0 )#line:68
def give_gold (O000OOOOO0000O0O0 ,O000OO0O00OOO00OO ):#line:72
    try :#line:73
        OO00OOOO0OO0OOOO0 =f'_doneeNo={O000OOOOO0000O0O0}&quantity={int(O000OO0O00OOO00OO)}_{timi_new()}'#line:74
        O0OO0O0O00000OO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0OO0OOOO0 ),'signstring':OO00OOOO0OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO000O00OO00OO0OO ={"quantity":int (O000OO0O00OOO00OO ),"doneeNo":O000OOOOO0000O0O0 }#line:89
        O00O0OO0OO0O00OOO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO0O0O00000OO00 ,data =OO000O00OO00OO0OO ).json ()#line:90
        if 'status'in O00O0OO0OO0O00OOO :#line:92
            if O00O0OO0OO0O00OOO ['status']==200 :#line:93
                if O00O0OO0OO0O00OOO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O000OO0O00OOO00OO)}种子给{O000OOOOO0000O0O0}成功')#line:95
                    return True #line:96
            if O00O0OO0OO0O00OOO ['status']==401 :#line:97
                print (f'【赠送种子】:{O00O0OO0OO0O00OOO["message"]}')#line:98
                return False #line:99
            if O00O0OO0OO0O00OOO ['status']==500 :#line:100
                print (f'【赠送种子】:{O00O0OO0OO0O00OOO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O00OOOO00OOOO00OO :#line:104
        print (O00OOOO00OOOO00OO )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO0O00O0O000O0O00 ):#line:115
    OO0000O00OO000000 =hashlib .md5 (OO0O00O0O000O0O00 .encode ()).hexdigest ()#line:116
    O0O0OO0O0000000O0 =sc1 ()#line:117
    O00O0OOOOOO0OOO00 =sc2 ()#line:118
    O00OOO0O000OOOO00 =sc3 ()#line:119
    O0OO00OOOOOOO0OO0 =O0O0OO0O0000000O0 +OO0000O00OO000000 +O00O0OOOOOO0OOO00 +O00OOO0O000OOOO00 #line:120
    OO0OOO0O0OOOO0O00 =hashlib .md5 (O0OO00OOOOOOO0OO0 .encode ()).hexdigest ()#line:121
    return OO0OOO0O0OOOO0O00 #line:122
def format_msg ():#line:125
    O0O00OOOOO000OOO0 =""#line:126
    for OOOOOO00O0O000OO0 in msg_list :#line:127
        O0O00OOOOO000OOO0 +=str (OOOOOO00O0O000OO0 )+"\r\n"#line:128
    return O0O00OOOOO000OOO0 #line:129
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
def get_json_data (O000OOO0O0O0O0OOO ,OO0OO0OOO0O00000O ,O0OOO000O0OOOOO0O ,O00OO0OOO0O0OOOO0 ):#line:153
    with open (O000OOO0O0O0O0OOO ,'rb')as O0000OOO00OOOO000 :#line:154
        O0O0OOO0OO00OO0OO =json .load (O0000OOO00OOOO000 )#line:155
        O0O0OOO0OO00OO0OO ['data'][OO0OO0OOO0O00000O ][O0OOO000O0OOOOO0O ]=O00OO0OOO0O0OOOO0 #line:156
        OO0OO0O000000OOOO =O0O0OOO0OO00OO0OO #line:157
    O0000OOO00OOOO000 .close ()#line:158
    return OO0OO0O000000OOOO #line:159
def write_json_data (O0OOO0000OO00OOOO ):#line:162
    with open (json_path1 ,'w')as O00OOOO0O0OO00O00 :#line:163
        json .dump (O0OOO0000OO00OOOO ,O00OOOO0O0OO00O00 )#line:164
    O00OOOO0O0OO00O00 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0O0O0OO0OOOOO0OO ,OO00OOOO00O00O0O0 ,O00OO00000O00O00O ,O0O0O0O00OOOOO00O ):#line:171
        try :#line:172
            O0O0O0OO0OOOOO0OO .msg =O00OO00000O00O00O #line:173
            O0O0O0OO0OOOOO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0O0O0OO0OOOOO0OO .token =OO00OOOO00O00O0O0 ['authorization']#line:175
            O0O0O0OO0OOOOO0OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0O0O0OO0OOOOO0OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0O0O0OO0OOOOO0OO .elephant_user =OO00OOOO00O00O0O0 ['elephant_user']#line:178
            O0O0O0OO0OOOOO0OO .elephant_pswd =OO00OOOO00O00O0O0 ['elephant_pswd']#line:179
            O0O0O0OO0OOOOO0OO .elephant_Task_ID =OO00OOOO00O00O0O0 ['elephant_Task_ID']#line:180
            O0O0O0OO0OOOOO0OO .len_new =O0O0O0O00OOOOO00O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O000000OOOOOO0OOO ):#line:186
        try :#line:187
            O000000OOOOOO0OOO .watched_ad ()#line:189
            OOOOO0OO0000OOOO0 =f'__{timi_new()}'#line:190
            OO0OO00OO00OOO00O ={'source':'scsc','authorization':O000000OOOOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0000OOOO0 ),'signstring':OOOOO0OO0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0OO0OO0OO00OO0O0 =requests .request ('get',f'{host}/user',headers =OO0OO00OO00OOO00O ).json ()#line:202
            if 'status'in O0OO0OO0OO00OO0O0 :#line:204
                if O0OO0OO0OO00OO0O0 ['status']==200 :#line:205
                    OOOO0000000O0O000 =O0OO0OO0OO00OO0O0 ['data']['nickname']#line:206
                    O00O0O0OOO000O000 =O0OO0OO0OO00OO0O0 ['data']['inner_id']#line:207
                    OOOOO0OOOO00OOOO0 =O0OO0OO0OO00OO0O0 ['data']['assets']['gold']#line:208
                    OO0OO000000O00OOO =O0OO0OO0OO00OO0O0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OOOO0000000O0O000[:5]}丨ID:{O00O0O0OOO000O000}丨等级:{OO0OO000000O00OOO}丨金种子:{str(OOOOO0OOOO00OOOO0).split(".")[0]}')#line:211
                    if 'wx_'in OOOO0000000O0O000 :#line:212
                        O000000OOOOOO0OOO .change_nickname ()#line:213
                if O0OO0OO0OO00OO0O0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O000000OOOOOO0OOO .elephant_user =='f':#line:216
                        return False #line:217
                    OO00O00000O0O0OOO =Invalid_login .addtask (elephant_user =O000000OOOOOO0OOO .elephant_user ,elephant_pswd =O000000OOOOOO0OOO .elephant_pswd ,elephant_Task_ID =O000000OOOOOO0OOO .elephant_Task_ID )#line:220
                    O000OO0O0O00O0O0O =get_json_data (json_path ,O000000OOOOOO0OOO .len_new ,'authorization',OO00O00000O0O0OOO )#line:221
                    if write_json_data (O000OO0O0O00O0O0O ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0OO0OO0OO00OO0O0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O0O00O00000OOO000 :#line:228
            print (O0O00O00000OOO000 )#line:229
    def sealing (OOOO0O000O000OOO0 ):#line:232
        try :#line:233
            OO000O00O000O00O0 =f'__{timi_new()}'#line:234
            OO0OOOO0OO000O0OO ={'source':'scsc','authorization':OOOO0O000O000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O000O00O0 ),'signstring':OO000O00O000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0OOOO0OO000O0OO )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO0OOOO0OO000O0OO )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0OOOO0OO000O0OO )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0OOOO0OO000O0OO )#line:249
            requests .request ('get',f'{host}/user',headers =OO0OOOO0OO000O0OO )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0OOOO0OO000O0OO )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0OOOO0OO000O0OO )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0OOOO0OO000O0OO )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO0OOOO0OO000O0OO )#line:254
            requests .request ('get',f'{host}/assets',headers =OO0OOOO0OO000O0OO )#line:255
        except Exception as OO0OO000O000O00O0 :#line:256
            print (OO0OO000O000O00O0 )#line:257
    def ddd (O00OOOO0OOOO0O000 ):#line:259
        try :#line:260
            O00OOOO00OO00OO0O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0O0O00000OO0O000 ={'source':'scsc','authorization':O00OOOO0OOOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO00OO00OO0O ),'signstring':O00OOOO00OO00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0O000O000OOOOOO0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O0O00000OO0O000 ).json ()#line:273
            print (O0O000O000OOOOOO0 )#line:274
        except Exception as O000OOOOOO0OOO00O :#line:277
            print (O000OOOOOO0OOO00O )#line:278
    def the_query (OOOO0O0O0O00OOOOO ):#line:283
        try :#line:284
            O0O00O0OOO000OO0O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            OOOO0OO0O0O0OO0O0 ={'authorization':OOOO0O0O0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO000OO0O ),'signstring':O0O00O0OOO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OO000O0OOO0OOO0OO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOOO0OO0O0O0OO0O0 ).json ()#line:296
            if 'status'in OO000O0OOO0OOO0OO :#line:298
                if OO000O0OOO0OOO0OO ['status']==200 :#line:299
                    return OO000O0OOO0OOO0OO ['data']['rows'][4 ]['price']#line:300
        except Exception as OO000O0OOOO0O0OOO :#line:301
            print (OO000O0OOOO0O0OOO )#line:302
    def market_sale (OO0OO00O00OOO0O00 ,O0O00000OOO00OOO0 ):#line:305
        try :#line:306
            OOO00O0OOO0OO00OO =timi_new ()#line:307
            O00O00OO0OOOO0000 =f'type=crop__{OOO00O0OOO0OO00OO}'#line:308
            OOOO0OO0O00O0O0O0 ={'source':'scsc','authorization':OO0OO00O00OOO0O00 .token ,'timestamp':str (OOO00O0OOO0OO00OO ),'sign':sign (O00O00OO0OOOO0000 ),'signstring':O00O00OO0OOOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O0OO0OO0O0000OOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOO0OO0O00O0O0O0 ).json ()#line:320
            if 'status'in O0OO0OO0O0000OOO0 :#line:322
                if O0OO0OO0O0000OOO0 ['status']==200 :#line:323
                    if O0OO0OO0O0000OOO0 ['data']['rows']:#line:324
                        O0O000OO0O00O0O00 =O0OO0OO0O0000OOO0 ['data']['rows'][0 ]['packsackItemId']#line:325
                        O000O00000OO0OOO0 =O0OO0OO0O0000OOO0 ['data']['rows'][0 ]['quantity']#line:326
                        if float (O0O00000OOO00OOO0 )>9 :#line:327
                            OO0000000O00O0O0O =f'_packsackItemId={O0O000OO0O00O0O00}&price={str(O0O00000OOO00OOO0)[:5]}&quantity={O000O00000OO0OOO0}_{OOO00O0OOO0OO00OO}'#line:328
                            OO00O000O0OOO0OOO ={'source':'scsc','authorization':OO0OO00O00OOO0O00 .token ,'timestamp':str (OOO00O0OOO0OO00OO ),'sign':sign (OO0000000O00O0O0O ),'signstring':OO0000000O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            O00OO00OO0O00O000 ={"packsackItemId":O0O000OO0O00O0O00 ,"price":str (O0O00000OOO00OOO0 )[:5 ],"quantity":str (O000O00000OO0OOO0 )}#line:344
                            O0OOOO000OOOOOO0O =requests .request ('post',f'{host}/market/sale',headers =OO00O000O0OOO0OOO ,data =O00OO00OO0O00O000 ).json ()#line:345
                            if 'status'in O0OOOO000OOOOOO0O :#line:347
                                if O0OOOO000OOOOOO0O ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{O000O00000OO0OOO0}丨价格:{str(O0O00000OOO00OOO0)[:5]}')#line:349
        except Exception as OOO0OO0000OOOOO00 :#line:350
            print (OOO0OO0000OOOOO00 )#line:351
    def query_to_sell (O0O0O0OOOO000O000 ):#line:354
        global count_list #line:355
        try :#line:356
            OOOOO000O00O0O00O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:357
            OOOO00000OOOOO000 ={'source':'scsc','authorization':O0O0O0OOOO000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000O00O0O00O ),'signstring':OOOOO000O00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            O0OO0OOOO0OOOO0OO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOOO00000OOOOO000 ).json ()#line:369
            if 'status'in O0OO0OOOO0OOOO0OO :#line:371
                if O0OO0OOOO0OOOO0OO ['status']==200 :#line:372
                    for O00O0O000OO00OOO0 in O0OO0OOOO0OOOO0OO ['data']['rows']:#line:373
                        OO0OO0OOO0O0O0OO0 =O00O0O000OO00OOO0 ['materialKey']#line:374
                        O0OOO00O000OOOO0O =O00O0O000OO00OOO0 ['quantity']#line:375
                        O0OO00OOOOOO00000 =O00O0O000OO00OOO0 ['price']#line:376
                        O0O000000O00OOOO0 =O00O0O000OO00OOO0 ['saleState']#line:377
                        if O0O000000O00OOOO0 ==0 :#line:378
                            print (f'【出售订单】:名称:{OO0OO0OOO0O0O0OO0}丨数量:{O0OOO00O000OOOO0O}丨价格:{O0OO00OOOOOO00000}')#line:379
                            count_list +=O0OOO00O000OOOO0O #line:380
                            O000000OO0O00O00O =O0O0O0OOOO000O000 .the_query ()#line:382
                            if float (O000000OO0O00O00O )!=float (O0OO00OOOOOO00000 ):#line:383
                                O000OO00OO00O0O00 =O00O0O000OO00OOO0 ['id']#line:384
                                if float (datetime .datetime .now ().hour )>8 :#line:385
                                    O0O0O0OOOO000O000 .cacel_sale (O000OO00OO00O0O00 )#line:386
                    O0O0O0OOOO000O000 .game_map ()#line:388
        except Exception as O000OOOOO0OOOO000 :#line:390
            print (O000OOOOO0OOOO000 )#line:391
    def cacel_sale (O0O0000OOOO0O00O0 ,O00O0O00OOOO0O0O0 ):#line:394
        try :#line:395
            O0OOOOO0O0OO0000O =f'_saleId={O00O0O00OOOO0O0O0}_{timi_new()}'#line:396
            O0O0O0OO0000OO00O ={'source':'scsc','authorization':O0O0000OOOO0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0OO0000O ),'signstring':O0OOOOO0O0OO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:407
            O0O0OOOOOOOOOO00O ={"saleId":O00O0O00OOOO0O0O0 }#line:408
            O0OOOO000O0O000O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0O0OO0000OO00O ,data =O0O0OOOOOOOOOO00O ).json ()#line:409
            if 'status'in O0OOOO000O0O000O0 :#line:411
                if O0OOOO000O0O000O0 ['status']==200 :#line:412
                    print (f'【下架出售】:{O0OOOO000O0O000O0["data"]}')#line:413
        except Exception as OO0O000O0OO0O00O0 :#line:414
            print (OO0O000O0OO0O00O0 )#line:415
    def change_nickname (O000O00000O00O00O ):#line:418
        try :#line:419
            OO0OOOO00OO0OOO00 =timi_new ()#line:420
            OOO0OOOO0O0OOO0OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:421
            OOO00OO000O000O0O =requests .request ('post','https://www.qmsjmfb.com/',data =OOO0OOOO0O0OOO0OO ).text #line:422
            OO0OO0O0OO0OOO0OO =re .findall ('<ul><li>(.*?)</li>',OOO00OO000O000O0O )[0 ][:3 ]#line:423
            O0OOOOOO0O0O00O0O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0OO0O0OO0OOO0OO}').json ()#line:424
            OOOOOOOO00OO0000O =O0OOOOOO0O0O00O0O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:425
            O0OOOO00OOO00O00O ={"nickname":OOOOOOOO00OO0000O }#line:426
            OO00O0O0O00OOO0O0 =f'_nickname={OOOOOOOO00OO0000O}_{OO0OOOO00OO0OOO00}'#line:427
            O0OOOOOO00OO00OO0 ={'source':'scsc','authorization':O000O00000O00O00O .token ,'timestamp':OO0OOOO00OO0OOO00 ,'sign':sign (OO00O0O0O00OOO0O0 ),'signstring':OO00O0O0O00OOO0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:438
            OO0O0OOOOO0O0OOO0 =requests .request ('patch',f'{host}/user/nickname',headers =O0OOOOOO00OO00OO0 ,data =O0OOOO00OOO00O00O ).json ()#line:439
            if 'status'in OO0O0OOOOO0O0OOO0 :#line:441
                if OO0O0OOOOO0O0OOO0 ['status']==200 :#line:442
                    print (f'【修改网名】:网名:{OOOOOOOO00OO0000O}丨{OO0O0OOOOO0O0OOO0["message"]}')#line:443
        except Exception as O0000OOO0O00OO0OO :#line:444
            print (O0000OOO0O00OO0OO )#line:445
    def withdraw (OO00OOO0O00O00OOO ):#line:448
        try :#line:449
            O0O0OOO00O000OOOO =f'__{timi_new()}'#line:450
            O0000O00O000OO00O ={'source':'scsc','authorization':OO00OOO0O00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00O000OOOO ),'signstring':O0O0OOO00O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            OOOO000O0OOO0OOOO =requests .request ('get',f'{host}/assets',headers =O0000O00O000OO00O ).json ()#line:462
            if 'status'in OOOO000O0OOO0OOOO :#line:464
                if OOOO000O0OOO0OOOO ['status']==200 :#line:465
                    O0OOO00OO0000OOOO =OOOO000O0OOO0OOOO ['data']['cash']#line:466
                    if float (O0OOO00OO0000OOOO )>20 :#line:467
                        O0O0OOO00O000OOOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:468
                        O0000O00O000OO00O ={'authorization':OO00OOO0O00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO00O000OOOO ),'signstring':O0O0OOO00O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:478
                        O000O00OOOO0O0OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:479
                        O0OOOOOOOO0O00OOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000O00O000OO00O ,data =O000O00OOOO0O0OOO ).json ()#line:481
                        if 'status'in O0OOOOOOOO0O00OOO :#line:483
                            if O0OOOOOOOO0O00OOO ['status']==200 :#line:484
                                print (f'【余额提现】:{O0OOOOOOOO0O00OOO["data"]}')#line:485
                        if 'status'in O0OOOOOOOO0O00OOO :#line:486
                            if O0OOOOOOOO0O00OOO ['status']==500 :#line:487
                                print (f'【余额提现】:{O0OOOOOOOO0O00OOO["message"]}')#line:488
        except Exception as OO00OOOOO000OO000 :#line:489
            print (OO00OOOOO000OO000 )#line:490
    def invitenum (O00O0000O0OOOO0OO ):#line:493
        global invited_new #line:494
        try :#line:495
            O00O00O00000O0000 =f'__{timi_new()}'#line:496
            O0OO0OOO0OOOOOOO0 ={'source':'scsc','authorization':O00O0000O0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00000O0000 ),'signstring':O00O00O00000O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            OOO0OO0OO000OOOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO0OOO0OOOOOOO0 ).json ()#line:508
            if 'status'in OOO0OO0OO000OOOO0 :#line:510
                if OOO0OO0OO000OOOO0 ['status']==200 :#line:511
                    OO00O0OOO00000OOO =OOO0OO0OO000OOOO0 ['data']['invited_count']#line:512
                    OOO0O0OO0OO0000O0 =OOO0OO0OO000OOOO0 ['data']['invited_second_count']#line:513
                    print (f'【我的邀请】:直邀好友:{OO00O0OOO00000OOO}丨间邀好友:{OOO0O0OO0OO0000O0}')#line:514
                    if OO00O0OOO00000OOO <2 :#line:515
                        OOO00O0OO00000O0O =f'__{timi_new()}'#line:516
                        O00OO000O0O00O0OO ={'source':'scsc','authorization':O00O0000O0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO00000O0O ),'signstring':OOO00O0OO00000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:527
                        OOOO0O0O0O000OO0O =requests .request ('get',f'{host}/user',headers =O00OO000O0O00O0OO ).json ()#line:528
                        if 'status'in OOOO0O0O0O000OO0O :#line:530
                            if OOOO0O0O0O000OO0O ['status']==200 :#line:531
                                invited_new .append (OOOO0O0O0O000OO0O ['data']['inner_id'])#line:532
        except Exception as OOOOO0OO0O0000OO0 :#line:533
            print (OOOOO0OO0O0000OO0 )#line:534
    def game_map (O0O0OO000O0000OOO ):#line:537
        try :#line:538
            O00O000OO0000OOO0 =f'__{timi_new()}'#line:539
            OOO0O0OOOO0O0O0OO ={'source':'scsc','authorization':O0O0OO000O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OO0000OOO0 ),'signstring':O00O000OO0000OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            O0O00OOO0O0OOOOO0 =requests .request ('get',f'{host}/game/map',headers =OOO0O0OOOO0O0O0OO ).json ()#line:551
            if 'status'in O0O00OOO0O0OOOOO0 :#line:553
                if O0O00OOO0O0OOOOO0 ['status']==200 :#line:554
                    for O0OOO0OOO00OO00OO in O0O00OOO0O0OOOOO0 ['data']['list'][0 ]['crops']:#line:555
                        OO0OOO000OOOO0O0O =O0OOO0OOO00OO00OO ['level']#line:557
                        if OO0OOO000OOOO0O0O ==41 :#line:558
                            O0O0OOOOO00OO0000 =O0OOO0OOO00OO00OO ['crop_name']#line:559
                            O000OOOOOOOOOO0OO =O0OOO0OOO00OO00OO ['count']#line:560
                            if O000OOOOOOOOOO0OO >0 :#line:561
                                print (f'【农业资产】:{O0O0OOOOO00OO0000}丨数量:{O000OOOOOOOOOO0OO}')#line:562
                                if float (datetime .datetime .now ().hour )>8 :#line:563
                                    OO000O000O0OO0O00 =O0O0OO000O0000OOO .the_query ()#line:564
                                    O0O0OO000O0000OOO .market_sale (OO000O000O0OO0O00 )#line:565
        except Exception as O0000O000OOOO0O00 :#line:566
            print (O0000O000OOOO0O00 )#line:567
    def give_gold (OO0O0OOOOO0OO0OO0 ):#line:570
        try :#line:571
            OOO0OO0000O0OOOOO =f'__{timi_new()}'#line:572
            OOO0OO0O0O0000OO0 ={'source':'scsc','authorization':OO0O0OOOOO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0000O0OOOOO ),'signstring':OOO0OO0000O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOOOOO0OOO0O00O00 =requests .request ('get',f'{host}/user',headers =OOO0OO0O0O0000OO0 ).json ()#line:584
            if 'status'in OOOOOO0OOO0O00O00 :#line:585
                if OOOOOO0OOO0O00O00 ['status']==200 :#line:586
                    if float (OO0O0OOOOO0OO0OO0 .doneeNo )!=0 :#line:587
                        OOOOOO0OO0000OO00 =OOOOOO0OOO0O00O00 ['data']['assets']['gold']#line:588
                        if float (OOOOOO0OO0000OO00 )>float (OO0O0OOOOO0OO0OO0 .innerId ):#line:589
                            OOO00000OOO000OO0 =int (float (OOOOOO0OO0000OO00 )/1.1 )#line:590
                            OOO0OO0000O0OOOOO =f'_doneeNo={OO0O0OOOOO0OO0OO0.doneeNo}&quantity={OOO00000OOO000OO0}_{timi_new()}'#line:591
                            OOO0OO0O0O0000OO0 ={'source':'scsc','authorization':OO0O0OOOOO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0000O0OOOOO ),'signstring':OOO0OO0000O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            OOOO0O0O0OOOOO0OO ={"quantity":OOO00000OOO000OO0 ,"doneeNo":OO0O0OOOOO0OO0OO0 .doneeNo }#line:606
                            O0O00000OOOO0O00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OO0O0O0000OO0 ,data =OOOO0O0O0OOOOO0OO ).json ()#line:607
                            if 'status'in O0O00000OOOO0O00O :#line:609
                                if O0O00000OOOO0O00O ['status']==200 :#line:610
                                    if O0O00000OOOO0O00O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OOO00000OOO000OO0}种子给{OO0O0OOOOO0OO0OO0.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as O000OO0O00O0OO00O :#line:615
            print (O000OO0O00O0OO00O )#line:616
    def invitation (OOO000O00O00O0OO0 ):#line:618
        try :#line:619
            _OO0O0OOOO00OOOOOO =float (bundled_def ())/4 #line:620
            OOO00O0O0O00O0O00 =f'_innerId={int(_OO0O0OOOO00OOOOOO)}_{timi_new()}'#line:621
            O0000O00OO0000OO0 ={'source':'scsc','authorization':OOO000O00O00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O0O00O0O00 ),'signstring':OOO00O0O0O00O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:632
            O000O0O0O0O0OOO00 ={"innerId":int (_OO0O0OOOO00OOOOOO )}#line:633
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0000O00OO0000OO0 ,data =O000O0O0O0O0OOO00 )#line:634
        except Exception as O0O00O0OO0000O000 :#line:635
            print (O0O00O0OO0000O000 )#line:636
    def winning_rewards (OO000OO0OOO0O00OO ):#line:639
        try :#line:640
            OO0OOO000OO0O0OOO =f'__{timi_new()}'#line:641
            OO00O0OO0O00OOO00 ={'source':'scsc','authorization':OO000OO0OOO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000OO0O0OOO ),'signstring':OO0OOO000OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:652
            OOOOOOO00O0O0O0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO00O0OO0O00OOO00 ).json ()#line:653
            if 'status'in OOOOOOO00O0O0O0OO :#line:655
                if OOOOOOO00O0O0O0OO ['status']==200 :#line:656
                    if OOOOOOO00O0O0O0OO ['data']['amount']:#line:657
                        O00000O00O0O0000O =OOOOOOO00O0O0O0OO ['data']['amount']['gold']#line:658
                        return O00000O00O0O0000O #line:659
                    else :#line:660
                        return 0 #line:661
        except Exception as OOOO00O0OOOO00000 :#line:662
            print (OOOO00O0OOOO00000 )#line:663
    def certification (OOO000O0OOO000000 ):#line:666
        try :#line:667
            OO000O00O0O00OO00 =f'__{timi_new()}'#line:668
            O000OOO00O000OOOO ={'source':'scsc','authorization':OOO000O0OOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00O0O00OO00 ),'signstring':OO000O00O0O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O00000O0OO0O0OOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O000OOO00O000OOOO ).json ()#line:680
            if 'status'in O00000O0OO0O0OOOO :#line:682
                if O00000O0OO0O0OOOO ['status']==200 :#line:683
                    if O00000O0OO0O0OOOO ['data']['result']:#line:684
                        O00OOOO00OOOO0OOO =O00000O0OO0O0OOOO ['data']['nick_name']#line:685
                        return O00OOOO00OOOO0OOO #line:686
                    else :#line:687
                        return '未实名'#line:688
        except Exception as O0000000OO0O00OO0 :#line:689
            print (O0000000OO0O00OO0 )#line:690
    def crops_illustrated (O0OO00O0O0OOO000O ):#line:693
        try :#line:694
            OOOO00000000000O0 =f'__{timi_new()}'#line:695
            OO0O000OO0OO00O0O ={'source':'scsc','authorization':O0OO00O0O0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000000000O0 ),'signstring':OOOO00000000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:706
            OO0OOO00O0OOOO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O000OO0OO00O0O ).json ()#line:707
            if 'status'in OO0OOO00O0OOOO0OO :#line:709
                if OO0OOO00O0OOOO0OO ['status']==200 :#line:710
                    O00OO0OO0O000OOOO =OO0OOO00O0OOOO0OO ['data'][0 ]['crops']#line:711
                    for O000000OO0OO0OO00 in O00OO0OO0O000OOOO :#line:712
                        if O000000OO0OO0OO00 ['ill_clover_award']:#line:713
                            if float (O000000OO0OO0OO00 ['ill_clover_award'])>1 :#line:714
                                if O000000OO0OO0OO00 ['is_finish']:#line:715
                                    if not O000000OO0OO0OO00 ['is_getit']:#line:716
                                        if O0OO00O0O0OOO000O .certification ()!='未实名':#line:717
                                            OOOO00000000000O0 =f'_award_level={O000000OO0OO0OO00["level"]}_{timi_new()}'#line:718
                                            OO0O000OO0OO00O0O ={'source':'scsc','authorization':O0OO00O0O0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00000000000O0 ),'signstring':OOOO00000000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:729
                                            OOOO000O00OO000OO ={"award_level":O000000OO0OO0OO00 ['level']}#line:730
                                            OO0O0000O0OO0O000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O000OO0OO00O0O ,json =OOOO000O00OO000OO ).json ()#line:732
                                            if 'status'in OO0O0000O0OO0O000 :#line:733
                                                if OO0O0000O0OO0O000 ['status']==200 :#line:734
                                                    O00O00O00OOOO0OOO =OO0O0000O0OO0O000 ['data']['ill_clover_award']#line:735
                                                    print (f'【图鉴奖励】:领取{O000000OO0OO0OO00["crop_name"]}成就丨奖励{O00O00O00OOOO0OOO}☘️')#line:737
                                                if OO0O0000O0OO0O000 ['status']==500 :#line:738
                                                    print (f'【图鉴奖励】:{OO0O0000O0OO0O000["message"]}')#line:739
        except Exception as O00000OO0O000OO00 :#line:740
            print (O00000OO0O000OO00 )#line:741
    def watched_ad (OOO00OOO000000OO0 ):#line:744
        try :#line:745
            OOOOO00O0OOO0000O =f'__{timi_new()}'#line:746
            O0O000OOO0O0000O0 ={'source':'scsc','authorization':OOO00OOO000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0OOO0000O ),'signstring':OOOOO00O0OOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:757
            OOO0O0OO0O0OOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O000OOO0O0000O0 ).json ()#line:758
            if 'status'in OOO0O0OO0O0OOO0O0 :#line:760
                if OOO0O0OO0O0OOO0O0 ['status']==200 :#line:761
                    if 'offlineInfo'in OOO0O0OO0O0OOO0O0 ['data']:#line:762
                        time .sleep (random .randint (1 ,3 ))#line:763
                        O0000000O0O00O00O =OOO0O0OO0O0OOO0O0 ['data']['offlineInfo']['off_minute']#line:764
                        O00OOOOOOO0OO00O0 =float (OOO0O0OO0O0OOO0O0 ['data']['silver'])/1000000000000 #line:765
                        time .sleep (1 )#line:766
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O000OOO0O0000O0 ).json ()#line:767
                        time .sleep (2 )#line:768
                        OO00OOOOO000O0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O000OOO0O0000O0 ).json ()#line:769
                        if 'status'in OO00OOOOO000O0O00 :#line:771
                            if OO00OOOOO000O0O00 ['status']==200 :#line:772
                                OO00OOOO0OO00O0OO =float (OO00OOOOO000O0O00 ['data']['silver'])/1000000000000 #line:773
                                OO0O0OO0OOOO0000O =str (OO00OOOO0OO00O0OO -O00OOOOOOO0OO00O0 )[:6 ]#line:774
                                print (f'【离线奖励】:翻倍离线{O0000000O0O00O00O}分钟奖励🌱数量:{OO0O0OO0OOOO0000O}t粒')#line:775
        except Exception as O0OOOO00O0OOO0O00 :#line:776
            print (O0OOOO00O0OOO0O00 )#line:777
    def user_ad (O000OOO0000OOOOOO ):#line:780
        try :#line:781
            OOOO000O000O0O0OO =f'__{timi_new()}'#line:782
            O0O0OOOOOO0O0O00O ={'source':'scsc','authorization':O000OOO0000OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O000O0O0OO ),'signstring':OOOO000O000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:793
            O00OOO0000O0OOO00 =requests .request ('get',f'{host}/user/ad',headers =O0O0OOOOOO0O0O00O ).json ()#line:794
            if 'status'in O00OOO0000O0OOO00 :#line:796
                if O00OOO0000O0OOO00 ['status']==200 :#line:797
                    OOO0O0OO00O0O0OOO =O00OOO0000O0OOO00 ['data']['max_time']#line:798
                    O0OO0OO0000000000 =O00OOO0000O0OOO00 ['data']['watch_time']#line:799
                    O0O00O0O0OO000OO0 =O00OOO0000O0OOO00 ['data']['added_time']#line:800
                    print (f'【获取种子】:获取🌱剩余{O0O00O0O0OO000OO0 + OOO0O0OO00O0O0OOO - O0OO0OO0000000000}次丨好友提供:{O0O00O0O0OO000OO0}次')#line:801
                    if O0O00O0O0OO000OO0 +OOO0O0OO00O0O0OOO -O0OO0OO0000000000 >0 :#line:802
                        time .sleep (random .randint (16 ,19 ))#line:803
                        O000O00O0O0O0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOOOOO0O0O00O ).json ()#line:804
                        if 'status'in O000O00O0O0O0OO00 :#line:806
                            if O000O00O0O0O0OO00 ['status']==200 :#line:807
                                O0O0OOO0OOO00O000 =float (O000O00O0O0O0OO00 ['data']['silver'])/1000000000000 #line:808
                                print (f'【获取种子】:获得🌱:{int(O0O0OOO0OOO00O000)}t粒')#line:809
                                return True #line:810
                            if O000O00O0O0O0OO00 ['status']==500 :#line:811
                                OOO00O0O00000O000 =O000O00O0O0O0OO00 ['message']#line:812
                                print (f'【获取种子】:{OOO00O0O00000O000}')#line:813
                                return False #line:814
        except Exception as OOO0OOOO000OOOO0O :#line:815
            print (OOO0OOOO000OOOO0O )#line:816
    def synthetic (O0OO0O0O0O0OOO0OO ):#line:819
        global id ,g #line:820
        try :#line:821
            OO0OO0OO0OO0OO0OO =O0OO0O0O0O0OOO0OO .level_new ()#line:822
            OOO00O00O0OO0O0OO =random .randint (9 ,11 )#line:823
            OOOOO0OO0O00OOOO0 =f'_site=8&targetSite={OOO00O00O0OO0O0OO}_{timi_new()}'#line:824
            OO0000O0O000OO0OO ={'source':'scsc','authorization':O0OO0O0O0O0OOO0OO .token ,'timestamp':timi_new (),'sign':sign (OOOOO0OO0O00OOOO0 ),'signstring':OOOOO0OO0O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:835
            OOOOO00O00OOO00OO ={"site":int (8 ),"targetSite":int (OOO00O00O0OO0O0OO )}#line:836
            requests .request ('post',f'{host}/game/crops/move',headers =OO0000O0O000OO0OO ,json =OOOOO00O00OOO00OO )#line:837
            while True :#line:838
                OO000O0O000000000 =f'__{timi_new()}'#line:839
                O0OO00O0O00OO0000 ={'source':'scsc','authorization':O0OO0O0O0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O000000000 ),'signstring':OO000O0O000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:850
                OOO00OO0OOOO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O0O00OO0000 ).json ()#line:851
                if 'status'in OOO00OO0OOOO0OO00 :#line:853
                    if OOO00OO0OOOO0OO00 ['status']==200 :#line:854
                        O00O0000O0O0OO0OO =OOO00OO0OOOO0OO00 ['data']['cropList']#line:855
                        O0O000000000O0O0O =OOO00OO0OOOO0OO00 ['data']['gameCoreDataDBid']#line:856
                        O0OOO0OO0O00000OO =float (OOO00OO0OOOO0OO00 ['data']['silver'])/1000000000000 #line:857
                        OO0O00O00OO0O00OO =0 #line:862
                        for OO000O00O0O0OOO0O in O00O0000O0O0OO0OO :#line:863
                            if not OO000O00O0O0OOO0O :#line:864
                                O0000000O00O0O00O =f'_crop_id={O0O000000000O0O0O}&site={OO0O00O00OO0O00OO}_{O0OO0O0O0O0OOO0OO.time}'#line:865
                                OOO000OOO0O000O0O ={'source':'scsc','authorization':O0OO0O0O0O0OOO0OO .token ,'timestamp':O0OO0O0O0O0OOO0OO .time ,'sign':sign (O0000000O00O0O00O ),'signstring':O0000000O00O0O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:875
                                O0000OOOO0O0OOOOO ={"site":OO0O00O00OO0O00OO ,"crop_id":O0O000000000O0O0O }#line:876
                                O00000OOO0OO0000O =requests .request ('post',f'{host}/game/crops/buy',headers =OOO000OOO0O000O0O ,data =O0000OOOO0O0OOOOO ).json ()#line:877
                                time .sleep (random .randint (1 ,3 )/10 )#line:879
                                if 'status'in O00000OOO0OO0000O :#line:880
                                    if O00000OOO0OO0000O ['status']==200 :#line:881
                                        if O00000OOO0OO0000O ['message']=='种子数量不足':#line:882
                                            OO0OO0OO0OO0OO0OO =O0OO0O0O0O0OOO0OO .level_new ()#line:883
                                            print (f'【种植合成】:{O00000OOO0OO0000O["message"]}')#line:884
                                            if not O0OO0O0O0O0OOO0OO .user_ad ():#line:885
                                                return False #line:886
                                    if O00000OOO0OO0000O ['status']==500 :#line:887
                                        print (f'【种植合成】:{O00000OOO0OO0000O["message"]}')#line:888
                                        return False #line:889
                            OO0O00O00OO0O00OO +=1 #line:890
                        O000O0O00O0OOOO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O0O00OO0000 ).json ()#line:891
                        OOOOO00OO00OOOOO0 =O000O0O00O0OOOO00 ['data']['cropList']#line:892
                        OO00O0OOOOO00OOOO =False #line:893
                        for OO000O00O0O0OOO0O in range (12 ):#line:894
                            id =OOOOO00OO00OOOOO0 [OO000O00O0O0OOO0O ]['level']#line:895
                            if float (OO0OO0OO0OO0OO0OO )-float (id )>9 :#line:896
                                O0000OOOO0OOOOO0O =f'_site={OO000O00O0O0OOO0O}_{timi_new()}'#line:897
                                O000000OO0OOO0OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO0O0O0O0OOO0OO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOO0OOOOO0O ),'signstring':O0000OOOO0OOOOO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:908
                                O0OOOO0OOOO0O0OOO ={"site":OO000O00O0O0OOO0O }#line:909
                                O0OO00OO0000OO0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000000OO0OOO0OO0 ,data =O0OOOO0OOOO0O0OOO ).json ()#line:911
                                if 'status'in O0OO00OO0000OO0O0 :#line:912
                                    if O0OO00OO0000OO0O0 ['status']==200 :#line:913
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:914
                            if id !=0 :#line:915
                                for O0OOO0OO0O0O0OO00 in range (11 ):#line:916
                                    OO0O0000000OOOO0O =O0OOO0OO0O0O0OO00 +1 #line:917
                                    g =OOOOO00OO00OOOOO0 [OO0O0000000OOOO0O ]['level']#line:918
                                    if id ==g :#line:919
                                        O000O000O00000000 =O0OOO0OO0O0O0OO00 +2 #line:920
                                        if O000O000O00000000 !=OO000O00O0O0OOO0O +1 :#line:921
                                            O000O0OO0OOOO0OO0 =OO000O00O0O0OOO0O +1 #line:922
                                            time .sleep (random .randint (1 ,3 )/10 )#line:924
                                            OOOOO0OO0O00OOOO0 =f'_site={O000O0OO0OOOO0OO0 - 1}&targetSite={O000O000O00000000 - 1}_{timi_new()}'#line:925
                                            OO0000O0O000OO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO0O0O0O0OOO0OO .token ,'timestamp':timi_new (),'sign':sign (OOOOO0OO0O00OOOO0 ),'signstring':OOOOO0OO0O00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:942
                                            OOOO0OOO0O0O0O000 ={"site":int (O000O0OO0OOOO0OO0 -1 ),"targetSite":int (O000O000O00000000 -1 )}#line:943
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0000O0O000OO0OO ,json =OOOO0OOO0O0O0O000 )#line:944
                                            OO00O0OOOOO00OOOO =True #line:946
                                    if OO00O0OOOOO00OOOO :#line:947
                                        break #line:948
                                if OO00O0OOOOO00OOOO :#line:949
                                    break #line:950
        except :#line:951
            O0OO0O0O0O0OOO0OO .synthetic ()#line:952
    def level_new (OO0OOO00O0OO0OO00 ):#line:955
        try :#line:956
            O00O00O000000OO00 =f'__{timi_new()}'#line:957
            O0OO0OO00OOOOO0O0 ={'source':'scsc','authorization':OO0OOO00O0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O000000OO00 ),'signstring':O00O00O000000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:968
            OOOOOOOOO0OO0OOOO =requests .request ('get',f'{host}/user',headers =O0OO0OO00OOOOO0O0 ).json ()#line:969
            if 'status'in OOOOOOOOO0OO0OOOO :#line:970
                if OOOOOOOOO0OO0OOOO ['status']==200 :#line:971
                    return float (OOOOOOOOO0OO0OOOO ['data']['level'])#line:972
        except Exception as OOO0O00OOOO000O0O :#line:973
            print (OOO0O00OOOO000O0O )#line:974
    def propsraffle (OO00OO0O00OOO00OO ):#line:977
        try :#line:978
            while True :#line:979
                OO0OOO0O0OO00O0OO =f'__{timi_new()}'#line:980
                OO0000OOOOO00OOOO ={'source':'scsc','authorization':OO00OO0O00OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0OO00O0OO ),'signstring':OO0OOO0O0OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:991
                O0O0O00O00OOO0O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0000OOOOO00OOOO ).json ()#line:992
                if 'status'in O0O0O00O00OOO0O0O :#line:994
                    if O0O0O00O00OOO0O0O ['status']==200 :#line:995
                        O0OO0000OO000OO0O =O0O0O00O00OOO0O0O ['data']['rows']#line:996
                        O0OOO000O00OO0O0O =O0O0O00O00OOO0O0O ['data']['vstate']#line:997
                        if O0OO0000OO000OO0O ==5 or O0OO0000OO000OO0O ==6 or O0OO0000OO000OO0O ==7 :#line:998
                            O00O0O0000OO00000 =O0O0O00O00OOO0O0O ['data']['silver']#line:999
                            print (f'【转盘抽奖】:获得种子:{O00O0O0000OO00000}')#line:1000
                        if O0OO0000OO000OO0O ==1 or O0OO0000OO000OO0O ==2 or O0OO0000OO000OO0O ==3 :#line:1001
                            OO00OOOOOO000OO00 =O0O0O00O00OOO0O0O ['data']['clover']#line:1002
                            print (f'【转盘抽奖】:获得三叶草:{OO00OOOOOO000OO00}')#line:1003
                        if O0OO0000OO000OO0O ==4 or O0OO0000OO000OO0O ==8 :#line:1004
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1005
                        if O0OO0000OO000OO0O =='抽奖次数已用完':#line:1009
                            break #line:1043
                time .sleep (random .randint (8 ,15 )/10 )#line:1044
        except Exception as OOOO0000O0O0OOOO0 :#line:1045
            print (OOOO0000O0O0OOOO0 )#line:1046
    def friends_invitation (OOOO0000OOO00O00O ):#line:1049
        try :#line:1050
            OO0O0OOO00O0OO0OO =f'__{timi_new()}'#line:1051
            OOO00OOO0OOOO0OOO ={'source':'scsc','authorization':OOOO0000OOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO00O0OO0OO ),'signstring':OO0O0OOO00O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1062
            OO0O0OOOOO000OOOO =requests .request ('get',f'{host}/friends',headers =OOO00OOO0OOOO0OOO ).json ()#line:1063
            if 'status'in OO0O0OOOOO000OOOO :#line:1064
                if OO0O0OOOOO000OOOO ['status']==200 :#line:1065
                    OO00O00OOO00000OO =OO0O0OOOOO000OOOO ['data']['myInviteter']#line:1066
                    if OO00O00OOO00000OO :#line:1067
                        O0O0OO00O0000O00O =OO00O00OOO00000OO ['user']['nickname']#line:1068
                        O0000O00OO0OO0O0O =OOOO0000OOO00O00O .certification ()#line:1069
                        if O0000O00OO0OO0O0O =='未实名':#line:1070
                            weishim .append (OOOO0000OOO00O00O .token )#line:1071
                        print (f'【查邀请人】:我的邀请人:{O0O0OO00O0000O00O}丨实名:{O0000O00OO0OO0O0O}')#line:1072
        except Exception as OOO0000O0OOO0O000 :#line:1076
            print (OOO0000O0OOO0O000 )#line:1077
    def add_clover (O0OOO0O00OO00OOOO ):#line:1080
        global golden_seed #line:1081
        try :#line:1082
            OOO0O0OO000O0O0OO =f'__{timi_new()}'#line:1083
            O0O00OOOOO0000OO0 ={'source':'scsc','authorization':O0OOO0O00OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO000O0O0OO ),'signstring':OOO0O0OO000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1094
            O0OOO0O00O0OO0O0O =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OOOOO0000OO0 ).json ()#line:1095
            if 'status'in O0OOO0O00O0OO0O0O :#line:1097
                if O0OOO0O00O0OO0O0O ['status']==200 :#line:1098
                    OOO0OO00OO000O0O0 =O0OOO0O00O0OO0O0O ['data']['clover']#line:1099
                    O0O00OO0OO0O000O0 =O0OOO0O00O0OO0O0O ['data']['used_clover']#line:1100
                    OO0O0OO0OO00OO0O0 =float (OOO0OO00OO000O0O0 )-float (O0O00OO0OO0O000O0 )#line:1101
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O00OO0OO0O000O0}')#line:1102
                    if O0OOO0O00OO00OOOO .certification ()!='未实名':#line:1103
                        if OO0O0OO0OO00OO0O0 >1 :#line:1104
                            OOO0O0OO000O0O0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0OO0OO00OO0O0)}_{timi_new()}'#line:1105
                            OOO0OOO0O0O0OO0O0 ={'source':'scsc','authorization':O0OOO0O00OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO000O0O0OO ),'signstring':OOO0O0OO000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1116
                            OO0OO00O00000OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0OO0OO00OO0O0 )}#line:1117
                            OO0000OO000000O00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0OOO0O0O0OO0O0 ,data =OO0OO00O00000OOO0 ).json ()#line:1118
                            if 'status'in OO0000OO000000O00 :#line:1120
                                if OO0000OO000000O00 ['status']==200 :#line:1121
                                    print (f'【参与抽奖】:添加☘️:{OO0000OO000000O00["data"]["isSuccess"]}丨数量:{OO0O0OO0OO00OO0O0}')#line:1122
                                if OO0000OO000000O00 ['status']==500 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{OO0000OO000000O00["message"]}')#line:1124
            O0OO00OOOO0OOOOOO =requests .request ('get',f'{host}/lottery',headers =O0O00OOOOO0000OO0 ).json ()#line:1125
            O00O0000OOO0OOO0O =O0OOO0O00OO00OOOO .winning_rewards ()#line:1127
            if 'status'in O0OO00OOOO0OOOOOO :#line:1128
                if O0OO00OOOO0OOOOOO ['status']==200 :#line:1129
                    OO00000OO00OO0O0O =O0OO00OOOO0OOOOOO ['data'][0 ]['day_get_gold_quantity']#line:1130
                    golden_seed +=float (OO00000OO00OO0O0O )#line:1131
                    O0O0000000O000000 =O0OO00OOOO0OOOOOO ['data'][1 ]['value']#line:1132
                    OO0OO0OO0OO0O000O =O0OO00OOOO0OOOOOO ['data'][0 ]['join_number']#line:1133
                    O00O00000000O00OO =int (float (O0OO00OOOO0OOOOOO ['data'][0 ]['totalValue']))#line:1134
                    OOO0O0OOO0OOO0OOO =float (O0O0000000O000000 /O00O00000000O00OO )*10000 #line:1135
                    O000OO000OO0000OO =O00O00000000O00OO /OO0OO0OO0OO0O000O #line:1136
                    print (f'【参与抽奖】:预计每天中{str(OO00000OO00OO0O0O)[:6]}颗金种子丨好友收益:{str(O00O0000OOO0OOO0O)[:6]}')#line:1137
                    print (f'【抽奖统计】:每1万☘️中{str(OOO0O0OOO0OOO0OOO)[:6]}颗金种子丨☘️人均:{str(O000OO000OO0000OO)[:7]}️')#line:1138
        except Exception as OOOOOOOO0000O0000 :#line:1139
            print (OOOOOOOO0000O0000 )#line:1140
    def energy (OO00OOO000O0O00OO ):#line:1143
        try :#line:1144
            while True :#line:1145
                OO00O00O0OOO00OO0 =f'__{timi_new()}'#line:1146
                O00O0OO0O00000OO0 ={'source':'scsc','authorization':OO00OOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O0OOO00OO0 ),'signstring':OO00O00O0OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1157
                O000OOOOOO0OOO0OO =requests .request ('get',f'{host}/energy/general',headers =O00O0OO0O00000OO0 ).json ()#line:1158
                if 'status'in O000OOOOOO0OOO0OO :#line:1160
                    if O000OOOOOO0OOO0OO ['status']==200 :#line:1161
                        OOO0OO00OOOOOOOO0 =O000OOOOOO0OOO0OO ['data']['ordinary_water']#line:1162
                        OOO000O0000O00O00 =O000OOOOOO0OOO0OO ['data']['ordinary_fertilizer']#line:1163
                        O00O00OO000OO00OO =O000OOOOOO0OOO0OO ['data']['videoStatus']#line:1164
                        O0O0OO0O0OO00O000 =O000OOOOOO0OOO0OO ['data']['waterVideoKey']#line:1165
                        print (f'【我的营养】:肥料:{str(OOO000O0000O00O00).split(".")[0]}丨水滴:{str(OOO0OO00OOOOOOOO0).split(".")[0]}')#line:1167
                        if float (OOO000O0000O00O00 )<96 :#line:1168
                            if O00O00OO000OO00OO :#line:1169
                                time .sleep (random .randint (160 ,180 )/10 )#line:1170
                                OOO0O0O00O0000000 =99 -float (OOO000O0000O00O00 )#line:1171
                                O0OO00000OO0O000O ={"fertilizer":str (OOO0O0O00O0000000 ).split ('.')[0 ]}#line:1172
                                OOOOO0OOO0O000OO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00O0OO0O00000OO0 ).json ()#line:1174
                                if 'status'in OOOOO0OOO0O000OO0 :#line:1176
                                    if OOOOO0OOO0O000OO0 ['status']==200 :#line:1177
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0OOO0O000OO0["message"]}')#line:1178
                                    if OOOOO0OOO0O000OO0 ['status']==500 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO0OOO0O000OO0["message"]}')#line:1180
                                        break #line:1181
                                if float (OOO000O0000O00O00 )<78 :#line:1183
                                    OOO0O0O00O0000000 =80 -float (OOO000O0000O00O00 )#line:1184
                                    O0O0O00OOO000000O =f'_fertilizer={int(OOO0O0O00O0000000)}_{timi_new()}'#line:1185
                                    OOO0O0O0000OOOO0O ={'source':'scsc','authorization':OO00OOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOO000000O ),'signstring':O0O0O00OOO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1196
                                    OOOOOOOOOOO000OOO ={"fertilizer":int (OOO0O0O00O0000000 )}#line:1197
                                    O000OO0O0O0O0OO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0O0O0000OOOO0O ,data =OOOOOOOOOOO000OOO ).json ()#line:1199
                                    if 'status'in O000OO0O0O0O0OO00 :#line:1201
                                        if O000OO0O0O0O0OO00 ['status']==200 :#line:1202
                                            print (f'【购买肥料】:购买肥料:{O000OO0O0O0O0OO00["message"]}丨数量:{int(OOO0O0O00O0000000)}')#line:1203
                                        if O000OO0O0O0O0OO00 ['status']==500 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{O000OO0O0O0O0OO00["message"]}丨数量:{int(OOO0O0O00O0000000)}')#line:1205
                                            O0OOO0OOO0000O00O =O000OO0O0O0O0OO00 ["message"].split ('-')[1 ]#line:1206
                                            O00OOOOOO0000OOOO =f'__{timi_new()}'#line:1207
                                            O000OO0OOOO00000O ={'source':'scsc','authorization':OO00OOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO0000OOOO ),'signstring':O00OOOOOO0000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1218
                                            OO0OO0OOOO0000O00 =requests .request ('get',f'{host}/user',headers =O000OO0OOOO00000O ).json ()#line:1219
                                            if 'status'in OO0OO0OOOO0000O00 :#line:1220
                                                if OO0OO0OOOO0000O00 ['status']==200 :#line:1221
                                                    O0000000O0O0O0OOO =OO0OO0OOOO0000O00 ['data']['inner_id']#line:1222
                                                    if give_gold (O0000000O0O0O0OOO ,float (O0OOO0OOO0000O00O )+1 ):#line:1223
                                                        OO00OOO000O0O00OO .energy ()#line:1224
                        if float (OOO0OO00OOOOOOOO0 )<880 :#line:1225
                            if O0O0OO0O0OO00O000 :#line:1226
                                time .sleep (random .randint (160 ,180 )/10 )#line:1227
                                OOOOOOO00000OO00O =999 -float (OOO0OO00OOOOOOOO0 )#line:1228
                                OO0O000OO0O0O0OOO ={"water":str (OOOOOOO00000OO00O ).split ('.')[0 ]}#line:1229
                                OOO00O0OO00OOOO0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00O0OO0O00000OO0 ).json ()#line:1231
                                if 'status'in OOO00O0OO00OOOO0O :#line:1233
                                    if OOO00O0OO00OOOO0O ['status']==200 :#line:1234
                                        print (f'【购买水滴】:看广告获取水滴:{OOO00O0OO00OOOO0O["message"]}')#line:1235
                                    if OOO00O0OO00OOOO0O ['status']==500 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OOO00O0OO00OOOO0O["message"]}')#line:1237
                                        break #line:1238
                                if float (OOO0OO00OOOOOOOO0 )<780 :#line:1239
                                    OOOOOOO00000OO00O =800 -float (OOO0OO00OOOOOOOO0 )#line:1240
                                    O00O0OOO0OOOO00O0 =f'_water={int(OOOOOOO00000OO00O)}_{timi_new()}'#line:1241
                                    O0O0O0O0OO00OO000 ={'source':'scsc','authorization':OO00OOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOO0OOOO00O0 ),'signstring':O00O0OOO0OOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1252
                                    O0OO0O0O00O00OO00 ={"water":int (OOOOOOO00000OO00O )}#line:1253
                                    O0000OOOOO0OO0000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O0O0O0OO00OO000 ,data =O0OO0O0O00O00OO00 ).json ()#line:1255
                                    if 'status'in O0000OOOOO0OO0000 :#line:1257
                                        if O0000OOOOO0OO0000 ['status']==200 :#line:1258
                                            print (f'【购买水滴】:购买水滴:{O0000OOOOO0OO0000["message"]}丨数量:{int(OOOOOOO00000OO00O)}')#line:1259
                                        if O0000OOOOO0OO0000 ['status']==500 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O0000OOOOO0OO0000["message"]}丨数量:{int(OOOOOOO00000OO00O)}')#line:1261
                                            O0OOO0OOO0000O00O =O0000OOOOO0OO0000 ["message"].split ('-')[1 ]#line:1262
                                            O00OOOOOO0000OOOO =f'__{timi_new()}'#line:1263
                                            O000OO0OOOO00000O ={'source':'scsc','authorization':OO00OOO000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO0000OOOO ),'signstring':O00OOOOOO0000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1274
                                            OO0OO0OOOO0000O00 =requests .request ('get',f'{host}/user',headers =O000OO0OOOO00000O ).json ()#line:1275
                                            if 'status'in OO0OO0OOOO0000O00 :#line:1276
                                                if OO0OO0OOOO0000O00 ['status']==200 :#line:1277
                                                    O0000000O0O0O0OOO =OO0OO0OOOO0000O00 ['data']['inner_id']#line:1278
                                                    if give_gold (O0000000O0O0O0OOO ,float (O0OOO0OOO0000O00O )+1 ):#line:1279
                                                        OO00OOO000O0O00OO .energy ()#line:1280
                        break #line:1281
        except Exception as O0000O0000OO00000 :#line:1282
            print (O0000O0000OO00000 )#line:1283
def bundled_def ():#line:1286
    O00OOOO0OO000OO0O =['5570536','7750212','7911652','7911680','7805624']#line:1287
    return O00OOOO0OO000OO0O [random .randint (0 ,len (O00OOOO0OO000OO0O )-1 )]#line:1288
def version_of_the_validation ():#line:1292
    return str ((102 -56 )/10 )#line:1293
def ubbbf ():#line:1295
    print ('卡密验证通过   ✅')#line:1296
def sc2 ():#line:1299
    return "19319#$%^&*((*"#line:1300
def OO00OO0OO0OO00OO00o0 ():#line:1303
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1305
def get_ip ():#line:1308
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1310
def gitee_validation ():#line:1313
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1314
def gitee_edition ():#line:1317
    try :#line:1318
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1319
    except :#line:1320
        sys .exit (0 )#line:1321
def O000OO000O0O00OOO00 ():#line:1325
    try :#line:1326
        O0OOOO0O00OO0OOOO =gitee_edition ()#line:1327
        if version_of_the_validation ()<O0OOOO0O00OO0OOOO ['CityEarth']['edition']:#line:1328
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0O00OO0OOOO["CityEarth"]["edition"]}   ❌')#line:1329
            print (f'更新内容=>>{O0OOOO0O00OO0OOOO["CityEarth"]["content"]}')#line:1330
        else :#line:1331
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOO0O00OO0OOOO["CityEarth"]["edition"]}   ✅')#line:1332
            print (f'更新内容=>> {O0OOOO0O00OO0OOOO["CityEarth"]["content"]}')#line:1333
    except Exception as O0OO000OO00OOO00O :#line:1334
        print (O0OO000OO00OOO00O )#line:1335
def sc3 ():#line:1338
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1339
if __name__ =='__main__':#line:1342
    start ()#line:1343
