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
        OOOOO0OOO0000OO00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOOOO0OOO0000OO00)}个账号==========")#line:17
        for OO000OO00OOO0O0OO in OOOOO0OOO0000OO00 :#line:18
            OO000000000000OOO =[]#line:19
            print (f"------------正在执行第{OOOOO0OOO0000OO00.index(OO000OO00OOO0O0OO) + 1}个账号------------")#line:20
            OO0O0OOOOOO0O000O =CityEarth (OO000OO00OOO0O0OO ,OO000000000000OOO ,OOOOO0OOO0000OO00 .index (OO000OO00OOO0O0OO ))#line:21
            def OO0OOOO0O0OOOO0O0 ():#line:23
                if OO0O0OOOOOO0O000O .base_info ():#line:25
                    OO0O0OOOOOO0O000O .sealing ()#line:27
                    OO0O0OOOOOO0O000O .invitenum ()#line:29
                    OO0O0OOOOOO0O000O .query_to_sell ()#line:31
                    OO0O0OOOOOO0O000O .friends_invitation ()#line:35
                    OO0O0OOOOOO0O000O .energy ()#line:37
                    OO0O0OOOOOO0O000O .add_clover ()#line:39
                    OO0O0OOOOOO0O000O .propsraffle ()#line:41
                    OO0O0OOOOOO0O000O .synthetic ()#line:43
                    OO0O0OOOOOO0O000O .crops_illustrated ()#line:45
                    OO0O0OOOOOO0O000O .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OO0O0OOOOOO0O000O .give_gold ()#line:50
            O0000O00000O000O0 =threading .Thread (target =OO0OOOO0O0OOOO0O0 )#line:52
            O0000O00000O000O0 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        O0OO000OOO00O00OO =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OO000OOO00O00OO +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0OOOOOOO000OOOOO in invited_new :#line:62
            print (O0OOOOOOO000OOOOO )#line:63
        print ('开始打印未实名的token')#line:64
        for OOOO0OOO0OO00O00O in weishim :#line:65
            print (OOOO0OOO0OO00O00O )#line:66
    except Exception as O0O0O0000OOOO00OO :#line:67
        print (O0O0O0000OOOO00OO )#line:68
def give_gold (OO0OO00O00000OO00 ,O000OOO0O0O0000O0 ):#line:72
    try :#line:73
        O0000O0OO0O0000O0 =f'_doneeNo={OO0OO00O00000OO00}&quantity={int(O000OOO0O0O0000O0)}_{timi_new()}'#line:74
        OOO0OOO00000OOO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000O0OO0O0000O0 ),'signstring':O0000O0OO0O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0OO0O0O0OOOOO0O0 ={"quantity":int (O000OOO0O0O0000O0 ),"doneeNo":OO0OO00O00000OO00 }#line:89
        O0OO000O0O0OOOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOO00000OOO00 ,data =O0OO0O0O0OOOOO0O0 ).json ()#line:90
        if 'status'in O0OO000O0O0OOOO0O :#line:92
            if O0OO000O0O0OOOO0O ['status']==200 :#line:93
                if O0OO000O0O0OOOO0O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O000OOO0O0O0000O0)}种子给{OO0OO00O00000OO00}成功')#line:95
                    return True #line:96
            if O0OO000O0O0OOOO0O ['status']==401 :#line:97
                print (f'【赠送种子】:{O0OO000O0O0OOOO0O["message"]}')#line:98
                return False #line:99
            if O0OO000O0O0OOOO0O ['status']==500 :#line:100
                print (f'【赠送种子】:{O0OO000O0O0OOOO0O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0OO000OOO00OOOO0 :#line:104
        print (O0OO000OOO00OOOO0 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (OO00O000O000OOO0O ):#line:115
    O0O0OO0OO0O00OO00 =hashlib .md5 (OO00O000O000OOO0O .encode ()).hexdigest ()#line:116
    OOO0O0OO0O0OO0000 =sc1 ()#line:117
    O0OOO0O0O0OOOOOOO =sc2 ()#line:118
    OOOO0OO000OOO0000 =sc3 ()#line:119
    OO0O0OOO000000OOO =OOO0O0OO0O0OO0000 +O0O0OO0OO0O00OO00 +O0OOO0O0O0OOOOOOO +OOOO0OO000OOO0000 #line:120
    OOOOO0OO000O0OO00 =hashlib .md5 (OO0O0OOO000000OOO .encode ()).hexdigest ()#line:121
    return OOOOO0OO000O0OO00 #line:122
def format_msg ():#line:125
    OOOOOOOOOOOO000OO =""#line:126
    for OOO00O0O00OOOOO0O in msg_list :#line:127
        OOOOOOOOOOOO000OO +=str (OOO00O0O00OOOOO0O )+"\r\n"#line:128
    return OOOOOOOOOOOO000OO #line:129
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
def get_json_data (OOO00O000OOOO0OO0 ,OO000OOO0000OO0O0 ,OO0O00O000O00OO0O ,O0O0O0O00OO00OOO0 ):#line:153
    with open (OOO00O000OOOO0OO0 ,'rb')as O0OO0O00OOOO00000 :#line:154
        O0O0O0OOO000OOO00 =json .load (O0OO0O00OOOO00000 )#line:155
        O0O0O0OOO000OOO00 ['data'][OO000OOO0000OO0O0 ][OO0O00O000O00OO0O ]=O0O0O0O00OO00OOO0 #line:156
        O00000O00OO0OOO0O =O0O0O0OOO000OOO00 #line:157
    O0OO0O00OOOO00000 .close ()#line:158
    return O00000O00OO0OOO0O #line:159
def write_json_data (OO000O000OO00OO0O ):#line:162
    with open (json_path1 ,'w')as OO0OO0OO00OOO0O00 :#line:163
        json .dump (OO000O000OO00OO0O ,OO0OO0OO00OOO0O00 )#line:164
    OO0OO0OO00OOO0O00 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OO000O00O00O00OOO ,OO0OOOO000OOO0OOO ,O00OO0OO000OOOO0O ,OOO0OO0O00OO0OOOO ):#line:171
        try :#line:172
            OO000O00O00O00OOO .msg =O00OO0OO000OOOO0O #line:173
            OO000O00O00O00OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OO000O00O00O00OOO .token =OO0OOOO000OOO0OOO ['authorization']#line:175
            OO000O00O00O00OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OO000O00O00O00OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OO000O00O00O00OOO .elephant_user =OO0OOOO000OOO0OOO ['elephant_user']#line:178
            OO000O00O00O00OOO .elephant_pswd =OO0OOOO000OOO0OOO ['elephant_pswd']#line:179
            OO000O00O00O00OOO .elephant_Task_ID =OO0OOOO000OOO0OOO ['elephant_Task_ID']#line:180
            OO000O00O00O00OOO .len_new =OOO0OO0O00OO0OOOO #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO00O00OO00OOO000 ):#line:186
        try :#line:187
            OO00O00OO00OOO000 .watched_ad ()#line:189
            O00OO0OOOOO000O0O =f'__{timi_new()}'#line:190
            OO0OOOO0OOO00O00O ={'source':'scsc','authorization':OO00O00OO00OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOOO000O0O ),'signstring':O00OO0OOOOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O0000OOO00OOOOO00 =requests .request ('get',f'{host}/user',headers =OO0OOOO0OOO00O00O ).json ()#line:202
            if 'status'in O0000OOO00OOOOO00 :#line:204
                if O0000OOO00OOOOO00 ['status']==200 :#line:205
                    O00000OOO000O0O0O =O0000OOO00OOOOO00 ['data']['nickname']#line:206
                    OO00OOO00OOO0OOO0 =O0000OOO00OOOOO00 ['data']['inner_id']#line:207
                    OO00OOO0000000O00 =O0000OOO00OOOOO00 ['data']['assets']['gold']#line:208
                    OO0OOO0OOO0O00000 =O0000OOO00OOOOO00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00000OOO000O0O0O[:5]}丨ID:{OO00OOO00OOO0OOO0}丨等级:{OO0OOO0OOO0O00000}丨金种子:{str(OO00OOO0000000O00).split(".")[0]}')#line:211
                    if 'wx_'in O00000OOO000O0O0O :#line:212
                        OO00O00OO00OOO000 .change_nickname ()#line:213
                if O0000OOO00OOOOO00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO00O00OO00OOO000 .elephant_user =='f':#line:216
                        return False #line:217
                    O00O0OOO0O00OOO00 =Invalid_login .addtask (elephant_user =OO00O00OO00OOO000 .elephant_user ,elephant_pswd =OO00O00OO00OOO000 .elephant_pswd ,elephant_Task_ID =OO00O00OO00OOO000 .elephant_Task_ID )#line:220
                    OO0O000O000000000 =get_json_data (json_path ,OO00O00OO00OOO000 .len_new ,'authorization',O00O0OOO0O00OOO00 )#line:221
                    if write_json_data (OO0O000O000000000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O0000OOO00OOOOO00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O0O0OOOOOOOO0O00O :#line:228
            print (O0O0OOOOOOOO0O00O )#line:229
    def sealing (O0000O0000O00O0OO ):#line:232
        try :#line:233
            OOO0OOOO0OO0O0O0O =f'__{timi_new()}'#line:234
            OO000O0O0000O0OO0 ={'source':'scsc','authorization':O0000O0000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOO0OO0O0O0O ),'signstring':OOO0OOOO0OO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO000O0O0000O0OO0 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OO000O0O0000O0OO0 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO000O0O0000O0OO0 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO000O0O0000O0OO0 )#line:249
            requests .request ('get',f'{host}/user',headers =OO000O0O0000O0OO0 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO000O0O0000O0OO0 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO000O0O0000O0OO0 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OO000O0O0000O0OO0 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OO000O0O0000O0OO0 )#line:254
            requests .request ('get',f'{host}/assets',headers =OO000O0O0000O0OO0 )#line:255
        except Exception as O00000O00OOOOO000 :#line:256
            print (O00000O00OOOOO000 )#line:257
    def ddd (OOO00O0O00OOO0O00 ):#line:259
        try :#line:260
            OOO0O00OOOO00OOOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00OO00O0OOO0OO00 ={'source':'scsc','authorization':OOO00O0O00OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OOOO00OOOO ),'signstring':OOO0O00OOOO00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            O0OO0OO0000OOOO0O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00OO00O0OOO0OO00 ).json ()#line:273
            print (O0OO0OO0000OOOO0O )#line:274
        except Exception as OOO0000000O00OO0O :#line:277
            print (OOO0000000O00OO0O )#line:278
    def the_query (O0OOO0O000O00000O ):#line:283
        try :#line:284
            OOO00OOOO0OOOOOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O000OO0O0O00000OO ={'authorization':O0OOO0O000O00000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO0OOOOOOO ),'signstring':OOO00OOOO0OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            O00000OO0OOO00O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O000OO0O0O00000OO ).json ()#line:296
            if 'status'in O00000OO0OOO00O0O :#line:298
                if O00000OO0OOO00O0O ['status']==200 :#line:299
                    return O00000OO0OOO00O0O ['data']['rows'][4 ]['price']#line:300
        except Exception as O00O0O0OOO00O00OO :#line:301
            print (O00O0O0OOO00O00OO )#line:302
    def market_sale (OOOO000OOO00O000O ,O0OOOO00O0O00O00O ):#line:305
        try :#line:306
            O0OOO0O0OO0000OOO =timi_new ()#line:307
            O00000O000OOOOO00 =f'type=crop__{O0OOO0O0OO0000OOO}'#line:308
            OO00O00OOO0OOOOOO ={'source':'scsc','authorization':OOOO000OOO00O000O .token ,'timestamp':str (O0OOO0O0OO0000OOO ),'sign':sign (O00000O000OOOOO00 ),'signstring':O00000O000OOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:319
            O000OOO0OOO0OOOOO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00O00OOO0OOOOOO ).json ()#line:320
            if 'status'in O000OOO0OOO0OOOOO :#line:322
                if O000OOO0OOO0OOOOO ['status']==200 :#line:323
                    if O000OOO0OOO0OOOOO ['data']['rows']:#line:324
                        O00OOOO00000000O0 =O000OOO0OOO0OOOOO ['data']['rows'][0 ]['packsackItemId']#line:325
                        OOO0OO0O0O0000OO0 =O000OOO0OOO0OOOOO ['data']['rows'][0 ]['quantity']#line:326
                        if O0OOOO00O0O00O00O >9 :#line:327
                            O0O0O0OOO000OO000 =f'_packsackItemId={O00OOOO00000000O0}&price={str(O0OOOO00O0O00O00O)[:5]}&quantity={OOO0OO0O0O0000OO0}_{O0OOO0O0OO0000OOO}'#line:328
                            O0O000OOOOOOO0OO0 ={'source':'scsc','authorization':OOOO000OOO00O000O .token ,'timestamp':str (O0OOO0O0OO0000OOO ),'sign':sign (O0O0O0OOO000OO000 ),'signstring':O0O0O0OOO000OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:339
                            OOO0000OOOOO0O0OO ={"packsackItemId":O00OOOO00000000O0 ,"price":str (O0OOOO00O0O00O00O )[:5 ],"quantity":str (OOO0OO0O0O0000OO0 )}#line:344
                            OOO0O0O0O0000O000 =requests .request ('post',f'{host}/market/sale',headers =O0O000OOOOOOO0OO0 ,data =OOO0000OOOOO0O0OO ).json ()#line:345
                            if 'status'in OOO0O0O0O0000O000 :#line:347
                                if OOO0O0O0O0000O000 ['status']==200 :#line:348
                                    print (f'【上架芦荟】:数量:{OOO0OO0O0O0000OO0}丨价格:{str(O0OOOO00O0O00O00O)[:5]}')#line:349
        except Exception as OOO0000OOO0O0OOO0 :#line:350
            print (OOO0000OOO0O0OOO0 )#line:351
    def query_to_sell (OOO000OO0O000O000 ):#line:354
        global count_list #line:355
        try :#line:356
            O00O0OOOOO000OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:357
            O000O0OOOO000O0OO ={'source':'scsc','authorization':OOO000OO0O000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOO000OO00 ),'signstring':O00O0OOOOO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:368
            OOOOO00000OO0OOO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O000O0OOOO000O0OO ).json ()#line:369
            if 'status'in OOOOO00000OO0OOO0 :#line:371
                if OOOOO00000OO0OOO0 ['status']==200 :#line:372
                    for O0O00000OO0O0O00O in OOOOO00000OO0OOO0 ['data']['rows']:#line:373
                        OOOO00OO0OO000OO0 =O0O00000OO0O0O00O ['materialKey']#line:374
                        OO000000OO00OOOOO =O0O00000OO0O0O00O ['quantity']#line:375
                        O0O00OO000O00OO00 =O0O00000OO0O0O00O ['price']#line:376
                        O00OO0O0OOO000O00 =O0O00000OO0O0O00O ['saleState']#line:377
                        if O00OO0O0OOO000O00 ==0 :#line:378
                            print (f'【出售订单】:名称:{OOOO00OO0OO000OO0}丨数量:{OO000000OO00OOOOO}丨价格:{O0O00OO000O00OO00}')#line:379
                            count_list +=OO000000OO00OOOOO #line:380
                            OO000OO00O00OOOOO =OOO000OO0O000O000 .the_query ()#line:382
                            if float (OO000OO00O00OOOOO )!=float (O0O00OO000O00OO00 ):#line:383
                                OO00OO0O00OOO0000 =O0O00000OO0O0O00O ['id']#line:384
                                if float (datetime .datetime .now ().hour )>8 :#line:385
                                    OOO000OO0O000O000 .cacel_sale (OO00OO0O00OOO0000 )#line:386
                    OOO000OO0O000O000 .game_map ()#line:388
        except Exception as O0000O0000O0O00OO :#line:390
            print (O0000O0000O0O00OO )#line:391
    def cacel_sale (OO0OO0O0O00O0OO0O ,O00000OOO00OOO0OO ):#line:394
        try :#line:395
            OOO0O00OO00000O00 =f'_saleId={O00000OOO00OOO0OO}_{timi_new()}'#line:396
            O00O0OOOO0OOO0000 ={'source':'scsc','authorization':OO0OO0O0O00O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OO00000O00 ),'signstring':OOO0O00OO00000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:407
            OO0O00O0O0O0OOO00 ={"saleId":O00000OOO00OOO0OO }#line:408
            OO000OOO000O00O0O =requests .request ('post',f'{host}/market/cacel-sale',headers =O00O0OOOO0OOO0000 ,data =OO0O00O0O0O0OOO00 ).json ()#line:409
            if 'status'in OO000OOO000O00O0O :#line:411
                if OO000OOO000O00O0O ['status']==200 :#line:412
                    print (f'【下架出售】:{OO000OOO000O00O0O["data"]}')#line:413
        except Exception as O0OOOOO0000OO00O0 :#line:414
            print (O0OOOOO0000OO00O0 )#line:415
    def change_nickname (OO0000O0O0OOO00OO ):#line:418
        try :#line:419
            OOO000OOO0O00O00O =timi_new ()#line:420
            OOO000O0OOO000O00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:421
            O000OOOOO00OO0O00 =requests .request ('post','https://www.qmsjmfb.com/',data =OOO000O0OOO000O00 ).text #line:422
            OO0O0OOO00OO0OOO0 =re .findall ('<ul><li>(.*?)</li>',O000OOOOO00OO0O00 )[0 ][:3 ]#line:423
            O0000O0O0OO00O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0OOO00OO0OOO0}').json ()#line:424
            O00O0000000OO000O =O0000O0O0OO00O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:425
            OO0O00000000OO0OO ={"nickname":O00O0000000OO000O }#line:426
            O0O000OOO0O000O0O =f'_nickname={O00O0000000OO000O}_{OOO000OOO0O00O00O}'#line:427
            O00OO0OO0OOO0O0OO ={'source':'scsc','authorization':OO0000O0O0OOO00OO .token ,'timestamp':OOO000OOO0O00O00O ,'sign':sign (O0O000OOO0O000O0O ),'signstring':O0O000OOO0O000O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:438
            OOOOO0OO00OOO0O00 =requests .request ('patch',f'{host}/user/nickname',headers =O00OO0OO0OOO0O0OO ,data =OO0O00000000OO0OO ).json ()#line:439
            if 'status'in OOOOO0OO00OOO0O00 :#line:441
                if OOOOO0OO00OOO0O00 ['status']==200 :#line:442
                    print (f'【修改网名】:网名:{O00O0000000OO000O}丨{OOOOO0OO00OOO0O00["message"]}')#line:443
        except Exception as O0OOOOOOOO00O0O0O :#line:444
            print (O0OOOOOOOO00O0O0O )#line:445
    def withdraw (OO0OOOO00O0OO0OOO ):#line:448
        try :#line:449
            OO0O0OO00OO00OO00 =f'__{timi_new()}'#line:450
            OOOO00000OO0O0O00 ={'source':'scsc','authorization':OO0OOOO00O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO00OO00OO00 ),'signstring':OO0O0OO00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            O0O0OOO000OOOOO00 =requests .request ('get',f'{host}/assets',headers =OOOO00000OO0O0O00 ).json ()#line:462
            if 'status'in O0O0OOO000OOOOO00 :#line:464
                if O0O0OOO000OOOOO00 ['status']==200 :#line:465
                    O0OO000OO0O00OOOO =O0O0OOO000OOOOO00 ['data']['cash']#line:466
                    if float (O0OO000OO0O00OOOO )>20 :#line:467
                        OO0O0OO00OO00OO00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:468
                        OOOO00000OO0O0O00 ={'authorization':OO0OOOO00O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO00OO00OO00 ),'signstring':OO0O0OO00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:478
                        OOOOO0OO0OO0000O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:479
                        OO0OO0O0OO00000O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO00000OO0O0O00 ,data =OOOOO0OO0OO0000O0 ).json ()#line:481
                        if 'status'in OO0OO0O0OO00000O0 :#line:483
                            if OO0OO0O0OO00000O0 ['status']==200 :#line:484
                                print (f'【余额提现】:{OO0OO0O0OO00000O0["data"]}')#line:485
                        if 'status'in OO0OO0O0OO00000O0 :#line:486
                            if OO0OO0O0OO00000O0 ['status']==500 :#line:487
                                print (f'【余额提现】:{OO0OO0O0OO00000O0["message"]}')#line:488
        except Exception as OOOO0O000O000OOOO :#line:489
            print (OOOO0O000O000OOOO )#line:490
    def invitenum (O0OOOO0O00O0O00O0 ):#line:493
        global invited_new #line:494
        try :#line:495
            O00O0OO000OOOOOOO =f'__{timi_new()}'#line:496
            OOOOO000000O0OO0O ={'source':'scsc','authorization':O0OOOO0O00O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO000OOOOOOO ),'signstring':O00O0OO000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            O00O00OOO00OOO00O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO000000O0OO0O ).json ()#line:508
            if 'status'in O00O00OOO00OOO00O :#line:510
                if O00O00OOO00OOO00O ['status']==200 :#line:511
                    O00OO00O0000OOO00 =O00O00OOO00OOO00O ['data']['invited_count']#line:512
                    O00O0O00OO000O000 =O00O00OOO00OOO00O ['data']['invited_second_count']#line:513
                    print (f'【我的邀请】:直邀好友:{O00OO00O0000OOO00}丨间邀好友:{O00O0O00OO000O000}')#line:514
                    if O00OO00O0000OOO00 <2 :#line:515
                        O0O00O0OO000000OO =f'__{timi_new()}'#line:516
                        O00O00O00O0OOOOO0 ={'source':'scsc','authorization':O0OOOO0O00O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO000000OO ),'signstring':O0O00O0OO000000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:527
                        O00OO0O000000000O =requests .request ('get',f'{host}/user',headers =O00O00O00O0OOOOO0 ).json ()#line:528
                        if 'status'in O00OO0O000000000O :#line:530
                            if O00OO0O000000000O ['status']==200 :#line:531
                                invited_new .append (O00OO0O000000000O ['data']['inner_id'])#line:532
        except Exception as OOOO0O000000O000O :#line:533
            print (OOOO0O000000O000O )#line:534
    def game_map (OOO0O0000O00OO00O ):#line:537
        try :#line:538
            OOO0OO0OOOOOO0O00 =f'__{timi_new()}'#line:539
            O0O00OO000OOOO0OO ={'source':'scsc','authorization':OOO0O0000O00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOOOOO0O00 ),'signstring':OOO0OO0OOOOOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            O0O0O0OO0OOO0O000 =requests .request ('get',f'{host}/game/map',headers =O0O00OO000OOOO0OO ).json ()#line:551
            if 'status'in O0O0O0OO0OOO0O000 :#line:553
                if O0O0O0OO0OOO0O000 ['status']==200 :#line:554
                    for O0O00OO0OOO0OOO0O in O0O0O0OO0OOO0O000 ['data']['list'][0 ]['crops']:#line:555
                        OO0OO00O0OOO00O00 =O0O00OO0OOO0OOO0O ['level']#line:557
                        if OO0OO00O0OOO00O00 ==41 :#line:558
                            O000OOO00000OOO0O =O0O00OO0OOO0OOO0O ['crop_name']#line:559
                            OOOOO0OO0OOOO0000 =O0O00OO0OOO0OOO0O ['count']#line:560
                            if OOOOO0OO0OOOO0000 >0 :#line:561
                                print (f'【农业资产】:{O000OOO00000OOO0O}丨数量:{OOOOO0OO0OOOO0000}')#line:562
                                if float (datetime .datetime .now ().hour )>8 :#line:563
                                    O0O0O00OO0O000OO0 =OOO0O0000O00OO00O .the_query ()#line:564
                                    OOO0O0000O00OO00O .market_sale (O0O0O00OO0O000OO0 )#line:565
        except Exception as O0OOOOO0000OO00OO :#line:566
            print (O0OOOOO0000OO00OO )#line:567
    def give_gold (O0000000000O00OO0 ):#line:570
        try :#line:571
            OOO0O0O0OOOO0O0OO =f'__{timi_new()}'#line:572
            OOOO0OOO0000OOO00 ={'source':'scsc','authorization':O0000000000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOOO0O0OO ),'signstring':OOO0O0O0OOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:583
            OOOO0000OOOOOOOO0 =requests .request ('get',f'{host}/user',headers =OOOO0OOO0000OOO00 ).json ()#line:584
            if 'status'in OOOO0000OOOOOOOO0 :#line:585
                if OOOO0000OOOOOOOO0 ['status']==200 :#line:586
                    if float (O0000000000O00OO0 .doneeNo )!=0 :#line:587
                        OO000000O0OO0OO00 =OOOO0000OOOOOOOO0 ['data']['assets']['gold']#line:588
                        if float (OO000000O0OO0OO00 )>float (O0000000000O00OO0 .innerId ):#line:589
                            OOO00OOO0O00OOO0O =int (float (OO000000O0OO0OO00 )/1.1 )#line:590
                            OOO0O0O0OOOO0O0OO =f'_doneeNo={O0000000000O00OO0.doneeNo}&quantity={OOO00OOO0O00OOO0O}_{timi_new()}'#line:591
                            OOOO0OOO0000OOO00 ={'source':'scsc','authorization':O0000000000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOOO0O0OO ),'signstring':OOO0O0O0OOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:602
                            O00O0000OO0OOO000 ={"quantity":OOO00OOO0O00OOO0O ,"doneeNo":O0000000000O00OO0 .doneeNo }#line:606
                            O00O0OO0000O00O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0OOO0000OOO00 ,data =O00O0000OO0OOO000 ).json ()#line:607
                            if 'status'in O00O0OO0000O00O0O :#line:609
                                if O00O0OO0000O00O0O ['status']==200 :#line:610
                                    if O00O0OO0000O00O0O ['data']:#line:611
                                        print (f'【赠送种子】:赠送{OOO00OOO0O00OOO0O}种子给{O0000000000O00OO0.doneeNo}成功')#line:612
                    else :#line:613
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:614
        except Exception as OOOO0O00OOOOO00OO :#line:615
            print (OOOO0O00OOOOO00OO )#line:616
    def invitation (OOOO00OO0000OOO0O ):#line:618
        try :#line:619
            _O0O000O0OO0O0OO0O =float (bundled_def ())/4 #line:620
            O0OOO00O0OO00OOO0 =f'_innerId={int(_O0O000O0OO0O0OO0O)}_{timi_new()}'#line:621
            OOOO0OO0OOOOO0O00 ={'source':'scsc','authorization':OOOO00OO0000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0OO00OOO0 ),'signstring':O0OOO00O0OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:632
            O0OOO0OOO0O00OO00 ={"innerId":int (_O0O000O0OO0O0OO0O )}#line:633
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO0OO0OOOOO0O00 ,data =O0OOO0OOO0O00OO00 )#line:634
        except Exception as O00O0O00O00000OO0 :#line:635
            print (O00O0O00O00000OO0 )#line:636
    def winning_rewards (OOOOO0OOOO0O000OO ):#line:639
        try :#line:640
            O0000O0OOOO000O0O =f'__{timi_new()}'#line:641
            OO000O0O0OOOO0OO0 ={'source':'scsc','authorization':OOOOO0OOOO0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOOO000O0O ),'signstring':O0000O0OOOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:652
            O0O000O000O00OOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO000O0O0OOOO0OO0 ).json ()#line:653
            if 'status'in O0O000O000O00OOO0 :#line:655
                if O0O000O000O00OOO0 ['status']==200 :#line:656
                    if O0O000O000O00OOO0 ['data']['amount']:#line:657
                        O0O0O0OOO00OOO0OO =O0O000O000O00OOO0 ['data']['amount']['gold']#line:658
                        return O0O0O0OOO00OOO0OO #line:659
                    else :#line:660
                        return 0 #line:661
        except Exception as O000000O00OOOO000 :#line:662
            print (O000000O00OOOO000 )#line:663
    def certification (O00O00OOOOOO0O0O0 ):#line:666
        try :#line:667
            O0OOO000OOO0O0O00 =f'__{timi_new()}'#line:668
            OOOO00O0O00000O00 ={'source':'scsc','authorization':O00O00OOOOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000OOO0O0O00 ),'signstring':O0OOO000OOO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            OOOOOO0OO00O0OO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOO00O0O00000O00 ).json ()#line:680
            if 'status'in OOOOOO0OO00O0OO00 :#line:682
                if OOOOOO0OO00O0OO00 ['status']==200 :#line:683
                    if OOOOOO0OO00O0OO00 ['data']['result']:#line:684
                        OOO00OO0O0O0OO0O0 =OOOOOO0OO00O0OO00 ['data']['nick_name']#line:685
                        return OOO00OO0O0O0OO0O0 #line:686
                    else :#line:687
                        return '未实名'#line:688
        except Exception as OOO0OO0O0O0O000O0 :#line:689
            print (OOO0OO0O0O0O000O0 )#line:690
    def crops_illustrated (O000O0OO000O0OOOO ):#line:693
        try :#line:694
            O00OO000000O0O000 =f'__{timi_new()}'#line:695
            OOO0O00OO0OO0OO00 ={'source':'scsc','authorization':O000O0OO000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000000O0O000 ),'signstring':O00OO000000O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:706
            OOOOO00OO0O000000 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0O00OO0OO0OO00 ).json ()#line:707
            if 'status'in OOOOO00OO0O000000 :#line:709
                if OOOOO00OO0O000000 ['status']==200 :#line:710
                    OO00OOOO00OOO000O =OOOOO00OO0O000000 ['data'][0 ]['crops']#line:711
                    for O000OO00O00OO0000 in OO00OOOO00OOO000O :#line:712
                        if O000OO00O00OO0000 ['ill_clover_award']:#line:713
                            if float (O000OO00O00OO0000 ['ill_clover_award'])>1 :#line:714
                                if O000OO00O00OO0000 ['is_finish']:#line:715
                                    if not O000OO00O00OO0000 ['is_getit']:#line:716
                                        if O000O0OO000O0OOOO .certification ()!='未实名':#line:717
                                            O00OO000000O0O000 =f'_award_level={O000OO00O00OO0000["level"]}_{timi_new()}'#line:718
                                            OOO0O00OO0OO0OO00 ={'source':'scsc','authorization':O000O0OO000O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000000O0O000 ),'signstring':O00OO000000O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:729
                                            O00O00O0OOO00O0O0 ={"award_level":O000OO00O00OO0000 ['level']}#line:730
                                            O00OO0000OOO000OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0O00OO0OO0OO00 ,json =O00O00O0OOO00O0O0 ).json ()#line:732
                                            if 'status'in O00OO0000OOO000OO :#line:733
                                                if O00OO0000OOO000OO ['status']==200 :#line:734
                                                    O0O000OO0OO0O00OO =O00OO0000OOO000OO ['data']['ill_clover_award']#line:735
                                                    print (f'【图鉴奖励】:领取{O000OO00O00OO0000["crop_name"]}成就丨奖励{O0O000OO0OO0O00OO}☘️')#line:737
                                                if O00OO0000OOO000OO ['status']==500 :#line:738
                                                    print (f'【图鉴奖励】:{O00OO0000OOO000OO["message"]}')#line:739
        except Exception as O00OO00000O0O0000 :#line:740
            print (O00OO00000O0O0000 )#line:741
    def watched_ad (O00000OOO0OO00OO0 ):#line:744
        try :#line:745
            OO000OOO0O0O0O00O =f'__{timi_new()}'#line:746
            O0O00OO0OOO000000 ={'source':'scsc','authorization':O00000OOO0OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO0O0O0O00O ),'signstring':OO000OOO0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:757
            O0000O0O0OO00O000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO0OOO000000 ).json ()#line:758
            if 'status'in O0000O0O0OO00O000 :#line:760
                if O0000O0O0OO00O000 ['status']==200 :#line:761
                    if 'offlineInfo'in O0000O0O0OO00O000 ['data']:#line:762
                        time .sleep (random .randint (1 ,3 ))#line:763
                        O0O00O0O0OO00000O =O0000O0O0OO00O000 ['data']['offlineInfo']['off_minute']#line:764
                        O0000OOOOO0OOOOOO =float (O0000O0O0OO00O000 ['data']['silver'])/1000000000000 #line:765
                        time .sleep (1 )#line:766
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O00OO0OOO000000 ).json ()#line:767
                        time .sleep (2 )#line:768
                        OOO0000O00OOO00O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OO0OOO000000 ).json ()#line:769
                        if 'status'in OOO0000O00OOO00O0 :#line:771
                            if OOO0000O00OOO00O0 ['status']==200 :#line:772
                                OO0OOOO0O0O0O0O0O =float (OOO0000O00OOO00O0 ['data']['silver'])/1000000000000 #line:773
                                OO00OO000OO00000O =str (OO0OOOO0O0O0O0O0O -O0000OOOOO0OOOOOO )[:6 ]#line:774
                                print (f'【离线奖励】:翻倍离线{O0O00O0O0OO00000O}分钟奖励🌱数量:{OO00OO000OO00000O}t粒')#line:775
        except Exception as O00O00O0O00OO0OOO :#line:776
            print (O00O00O0O00OO0OOO )#line:777
    def user_ad (O0OO00OO0OO000O00 ):#line:780
        try :#line:781
            O0OO000OO00000OOO =f'__{timi_new()}'#line:782
            OOOOOO000OO000O00 ={'source':'scsc','authorization':O0OO00OO0OO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OO00000OOO ),'signstring':O0OO000OO00000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:793
            O00O00O000O0O000O =requests .request ('get',f'{host}/user/ad',headers =OOOOOO000OO000O00 ).json ()#line:794
            if 'status'in O00O00O000O0O000O :#line:796
                if O00O00O000O0O000O ['status']==200 :#line:797
                    OOO0O0O0000O0OO00 =O00O00O000O0O000O ['data']['max_time']#line:798
                    OO0O000000O0000OO =O00O00O000O0O000O ['data']['watch_time']#line:799
                    O0O00OO0O0O000O00 =O00O00O000O0O000O ['data']['added_time']#line:800
                    print (f'【获取种子】:获取🌱剩余{O0O00OO0O0O000O00 + OOO0O0O0000O0OO00 - OO0O000000O0000OO}次丨好友提供:{O0O00OO0O0O000O00}次')#line:801
                    if O0O00OO0O0O000O00 +OOO0O0O0000O0OO00 -OO0O000000O0000OO >0 :#line:802
                        time .sleep (random .randint (16 ,19 ))#line:803
                        O0000O000OOOO00OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOOOO000OO000O00 ).json ()#line:804
                        if 'status'in O0000O000OOOO00OO :#line:806
                            if O0000O000OOOO00OO ['status']==200 :#line:807
                                OO00OOO00000OO0O0 =float (O0000O000OOOO00OO ['data']['silver'])/1000000000000 #line:808
                                print (f'【获取种子】:获得🌱:{int(OO00OOO00000OO0O0)}t粒')#line:809
                                return True #line:810
                            if O0000O000OOOO00OO ['status']==500 :#line:811
                                OO0O0O0O00OOOO0OO =O0000O000OOOO00OO ['message']#line:812
                                print (f'【获取种子】:{OO0O0O0O00OOOO0OO}')#line:813
                                return False #line:814
        except Exception as O0O0OO0OOOOO0O00O :#line:815
            print (O0O0OO0OOOOO0O00O )#line:816
    def synthetic (OO0OOO0OO00OO00OO ):#line:819
        global id ,g #line:820
        try :#line:821
            OO00O00OO0OO00O0O =OO0OOO0OO00OO00OO .level_new ()#line:822
            O000OO0OO0O00OO00 =random .randint (9 ,11 )#line:823
            OOOOOO0O0O0OOOO00 =f'_site=8&targetSite={O000OO0OO0O00OO00}_{timi_new()}'#line:824
            OO0OOOO0OO0000O0O ={'source':'scsc','authorization':OO0OOO0OO00OO00OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0O0O0OOOO00 ),'signstring':OOOOOO0O0O0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:835
            O0OO0OO00OO00OOO0 ={"site":int (8 ),"targetSite":int (O000OO0OO0O00OO00 )}#line:836
            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOOO0OO0000O0O ,json =O0OO0OO00OO00OOO0 )#line:837
            while True :#line:838
                OOOO0OO0OO00O0OO0 =f'__{timi_new()}'#line:839
                OOOOO00O00OO00OO0 ={'source':'scsc','authorization':OO0OOO0OO00OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO0OO00O0OO0 ),'signstring':OOOO0OO0OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:850
                OOO000O0O0O00000O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO00O00OO00OO0 ).json ()#line:851
                if 'status'in OOO000O0O0O00000O :#line:853
                    if OOO000O0O0O00000O ['status']==200 :#line:854
                        OOO00OO00OOO00OOO =OOO000O0O0O00000O ['data']['cropList']#line:855
                        O00O0OO00OOOO0OO0 =OOO000O0O0O00000O ['data']['gameCoreDataDBid']#line:856
                        OOO00OO0O00OO0000 =float (OOO000O0O0O00000O ['data']['silver'])/1000000000000 #line:857
                        O0OOO0OOOOOO0OOO0 =0 #line:862
                        for O00O00OOO0O0O0000 in OOO00OO00OOO00OOO :#line:863
                            if not O00O00OOO0O0O0000 :#line:864
                                OO0O0OOOO0OO0O00O =f'_crop_id={O00O0OO00OOOO0OO0}&site={O0OOO0OOOOOO0OOO0}_{OO0OOO0OO00OO00OO.time}'#line:865
                                O00O000000O000OO0 ={'source':'scsc','authorization':OO0OOO0OO00OO00OO .token ,'timestamp':OO0OOO0OO00OO00OO .time ,'sign':sign (OO0O0OOOO0OO0O00O ),'signstring':OO0O0OOOO0OO0O00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:875
                                O0OOO00O000OO0OO0 ={"site":O0OOO0OOOOOO0OOO0 ,"crop_id":O00O0OO00OOOO0OO0 }#line:876
                                OO000OO0OOOO00O00 =requests .request ('post',f'{host}/game/crops/buy',headers =O00O000000O000OO0 ,data =O0OOO00O000OO0OO0 ).json ()#line:877
                                time .sleep (random .randint (1 ,3 )/10 )#line:879
                                if 'status'in OO000OO0OOOO00O00 :#line:880
                                    if OO000OO0OOOO00O00 ['status']==200 :#line:881
                                        if OO000OO0OOOO00O00 ['message']=='种子数量不足':#line:882
                                            OO00O00OO0OO00O0O =OO0OOO0OO00OO00OO .level_new ()#line:883
                                            print (f'【种植合成】:{OO000OO0OOOO00O00["message"]}')#line:884
                                            if not OO0OOO0OO00OO00OO .user_ad ():#line:885
                                                return False #line:886
                                    if OO000OO0OOOO00O00 ['status']==500 :#line:887
                                        print (f'【种植合成】:{OO000OO0OOOO00O00["message"]}')#line:888
                                        return False #line:889
                            O0OOO0OOOOOO0OOO0 +=1 #line:890
                        O00O00O0O0O0OOOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOO00O00OO00OO0 ).json ()#line:891
                        OOO0000O0O0O00OOO =O00O00O0O0O0OOOO0 ['data']['cropList']#line:892
                        O0O0OOOO00O0O00OO =False #line:893
                        for O00O00OOO0O0O0000 in range (12 ):#line:894
                            id =OOO0000O0O0O00OOO [O00O00OOO0O0O0000 ]['level']#line:895
                            if float (OO00O00OO0OO00O0O )-float (id )>9 :#line:896
                                OO0OO0O0O0OO0OO00 =f'_site={O00O00OOO0O0O0000}_{timi_new()}'#line:897
                                O00O000000OOOOO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO0OO00OO00OO .token ,'timestamp':timi_new (),'sign':sign (OO0OO0O0O0OO0OO00 ),'signstring':OO0OO0O0O0OO0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:908
                                O0O0OO00OO00OO000 ={"site":O00O00OOO0O0O0000 }#line:909
                                O00OOO00O0OO00OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O000000OOOOO00 ,data =O0O0OO00OO00OO000 ).json ()#line:911
                                if 'status'in O00OOO00O0OO00OOO :#line:912
                                    if O00OOO00O0OO00OOO ['status']==200 :#line:913
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:914
                            if id !=0 :#line:915
                                for OOO00O00OOO0OOO00 in range (11 ):#line:916
                                    O0OO00O000OO00OO0 =OOO00O00OOO0OOO00 +1 #line:917
                                    g =OOO0000O0O0O00OOO [O0OO00O000OO00OO0 ]['level']#line:918
                                    if id ==g :#line:919
                                        O0OOO0OOOO00O0O0O =OOO00O00OOO0OOO00 +2 #line:920
                                        if O0OOO0OOOO00O0O0O !=O00O00OOO0O0O0000 +1 :#line:921
                                            OOO000OOO0OOO0OOO =O00O00OOO0O0O0000 +1 #line:922
                                            time .sleep (random .randint (1 ,3 )/10 )#line:924
                                            OOOOOO0O0O0OOOO00 =f'_site={OOO000OOO0OOO0OOO - 1}&targetSite={O0OOO0OOOO00O0O0O - 1}_{timi_new()}'#line:925
                                            OO0OOOO0OO0000O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOO0OO00OO00OO .token ,'timestamp':timi_new (),'sign':sign (OOOOOO0O0O0OOOO00 ),'signstring':OOOOOO0O0O0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:942
                                            O00OOO0O00O0O00O0 ={"site":int (OOO000OOO0OOO0OOO -1 ),"targetSite":int (O0OOO0OOOO00O0O0O -1 )}#line:943
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0OOOO0OO0000O0O ,json =O00OOO0O00O0O00O0 )#line:944
                                            O0O0OOOO00O0O00OO =True #line:946
                                    if O0O0OOOO00O0O00OO :#line:947
                                        break #line:948
                                if O0O0OOOO00O0O00OO :#line:949
                                    break #line:950
        except :#line:951
            OO0OOO0OO00OO00OO .synthetic ()#line:952
    def level_new (O0OOOO00O00O0OOOO ):#line:955
        try :#line:956
            OO00000O0OO000O0O =f'__{timi_new()}'#line:957
            O0O0O0OO0O0O00OO0 ={'source':'scsc','authorization':O0OOOO00O00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0OO000O0O ),'signstring':OO00000O0OO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:968
            O0O0OO0O0000OOOO0 =requests .request ('get',f'{host}/user',headers =O0O0O0OO0O0O00OO0 ).json ()#line:969
            if 'status'in O0O0OO0O0000OOOO0 :#line:970
                if O0O0OO0O0000OOOO0 ['status']==200 :#line:971
                    return float (O0O0OO0O0000OOOO0 ['data']['level'])#line:972
        except Exception as OOO0O0OOOOOO00OO0 :#line:973
            print (OOO0O0OOOOOO00OO0 )#line:974
    def propsraffle (OOO00OOO0O00O0O00 ):#line:977
        try :#line:978
            while True :#line:979
                O0000OO0O00O0000O =f'__{timi_new()}'#line:980
                OOO00OOO0OO0000OO ={'source':'scsc','authorization':OOO00OOO0O00O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0O00O0000O ),'signstring':O0000OO0O00O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:991
                O0000O0OO00OO00OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00OOO0OO0000OO ).json ()#line:992
                if 'status'in O0000O0OO00OO00OO :#line:994
                    if O0000O0OO00OO00OO ['status']==200 :#line:995
                        O00O00OOOO000O0OO =O0000O0OO00OO00OO ['data']['rows']#line:996
                        OOOOO0O000OO0O00O =O0000O0OO00OO00OO ['data']['vstate']#line:997
                        if O00O00OOOO000O0OO ==5 or O00O00OOOO000O0OO ==6 or O00O00OOOO000O0OO ==7 :#line:998
                            O000000OO0OOO0000 =O0000O0OO00OO00OO ['data']['silver']#line:999
                            print (f'【转盘抽奖】:获得种子:{O000000OO0OOO0000}')#line:1000
                        if O00O00OOOO000O0OO ==1 or O00O00OOOO000O0OO ==2 or O00O00OOOO000O0OO ==3 :#line:1001
                            OOO0OO00O0O00O000 =O0000O0OO00OO00OO ['data']['clover']#line:1002
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OO00O0O00O000}')#line:1003
                        if O00O00OOOO000O0OO ==4 or O00O00OOOO000O0OO ==8 :#line:1004
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1005
                        if O00O00OOOO000O0OO =='抽奖次数已用完':#line:1009
                            break #line:1043
                time .sleep (random .randint (8 ,15 )/10 )#line:1044
        except Exception as O0O0O0O000OO0OO00 :#line:1045
            print (O0O0O0O000OO0OO00 )#line:1046
    def friends_invitation (OOOOO0O0OO00OOO0O ):#line:1049
        try :#line:1050
            OO00OOOOOO0OOO0OO =f'__{timi_new()}'#line:1051
            OO0000O000000O0O0 ={'source':'scsc','authorization':OOOOO0O0OO00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO0OOO0OO ),'signstring':OO00OOOOOO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1062
            O0OOOOOOO000O000O =requests .request ('get',f'{host}/friends',headers =OO0000O000000O0O0 ).json ()#line:1063
            if 'status'in O0OOOOOOO000O000O :#line:1064
                if O0OOOOOOO000O000O ['status']==200 :#line:1065
                    O0O000000O0O00OOO =O0OOOOOOO000O000O ['data']['myInviteter']#line:1066
                    if O0O000000O0O00OOO :#line:1067
                        OO00O0O0O00O0OOOO =O0O000000O0O00OOO ['user']['nickname']#line:1068
                        O000O0OO0O00OOOO0 =OOOOO0O0OO00OOO0O .certification ()#line:1069
                        if O000O0OO0O00OOOO0 =='未实名':#line:1070
                            weishim .append (OOOOO0O0OO00OOO0O .token )#line:1071
                        print (f'【查邀请人】:我的邀请人:{OO00O0O0O00O0OOOO}丨实名:{O000O0OO0O00OOOO0}')#line:1072
        except Exception as OOO0O000O0OOOOOOO :#line:1076
            print (OOO0O000O0OOOOOOO )#line:1077
    def add_clover (O00OO00OOOOOO0000 ):#line:1080
        global golden_seed #line:1081
        try :#line:1082
            O0OO0OO0000000O00 =f'__{timi_new()}'#line:1083
            OOOOO00OO000OO0OO ={'source':'scsc','authorization':O00OO00OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0000000O00 ),'signstring':O0OO0OO0000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1094
            OO000O0O00O00OO00 =requests .request ('get',f'{host}/assets/clovers',headers =OOOOO00OO000OO0OO ).json ()#line:1095
            if 'status'in OO000O0O00O00OO00 :#line:1097
                if OO000O0O00O00OO00 ['status']==200 :#line:1098
                    OO0O0OOO00O0OOO0O =OO000O0O00O00OO00 ['data']['clover']#line:1099
                    OOO00OOOOO0O00000 =OO000O0O00O00OO00 ['data']['used_clover']#line:1100
                    OO0OOO000OO0OOO0O =float (OO0O0OOO00O0OOO0O )-float (OOO00OOOOO0O00000 )#line:1101
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO00OOOOO0O00000}')#line:1102
                    if O00OO00OOOOOO0000 .certification ()!='未实名':#line:1103
                        if OO0OOO000OO0OOO0O >1 :#line:1104
                            O0OO0OO0000000O00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OOO000OO0OOO0O)}_{timi_new()}'#line:1105
                            O00OO00OO00O0000O ={'source':'scsc','authorization':O00OO00OOOOOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0000000O00 ),'signstring':O0OO0OO0000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1116
                            OO0OO0O0OO00OO00O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OOO000OO0OOO0O )}#line:1117
                            O0OOO00O0000OOOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO00OO00O0000O ,data =OO0OO0O0OO00OO00O ).json ()#line:1118
                            if 'status'in O0OOO00O0000OOOO0 :#line:1120
                                if O0OOO00O0000OOOO0 ['status']==200 :#line:1121
                                    print (f'【参与抽奖】:添加☘️:{O0OOO00O0000OOOO0["data"]["isSuccess"]}丨数量:{OO0OOO000OO0OOO0O}')#line:1122
                                if O0OOO00O0000OOOO0 ['status']==500 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O0OOO00O0000OOOO0["message"]}')#line:1124
            OOO0OO00OO00OOO0O =requests .request ('get',f'{host}/lottery',headers =OOOOO00OO000OO0OO ).json ()#line:1125
            OOOOO0O00O0000O00 =O00OO00OOOOOO0000 .winning_rewards ()#line:1127
            if 'status'in OOO0OO00OO00OOO0O :#line:1128
                if OOO0OO00OO00OOO0O ['status']==200 :#line:1129
                    O000OOOOO00O00O0O =OOO0OO00OO00OOO0O ['data'][0 ]['day_get_gold_quantity']#line:1130
                    golden_seed +=float (O000OOOOO00O00O0O )#line:1131
                    OO000O00OOOOO0OOO =OOO0OO00OO00OOO0O ['data'][1 ]['value']#line:1132
                    OO00000OO0OO0O0OO =OOO0OO00OO00OOO0O ['data'][0 ]['join_number']#line:1133
                    OO0OOOO00O000O000 =int (float (OOO0OO00OO00OOO0O ['data'][0 ]['totalValue']))#line:1134
                    O0OO00O0O0O0O0OOO =float (OO000O00OOOOO0OOO /OO0OOOO00O000O000 )*10000 #line:1135
                    O00OOOO0O0OOO0O0O =OO0OOOO00O000O000 /OO00000OO0OO0O0OO #line:1136
                    print (f'【参与抽奖】:预计每天中{str(O000OOOOO00O00O0O)[:6]}颗金种子丨好友收益:{str(OOOOO0O00O0000O00)[:6]}')#line:1137
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO00O0O0O0O0OOO)[:6]}颗金种子丨☘️人均:{str(O00OOOO0O0OOO0O0O)[:7]}️')#line:1138
        except Exception as OOOOOO00O0000O0O0 :#line:1139
            print (OOOOOO00O0000O0O0 )#line:1140
    def energy (O0OO0000O0OO0O0O0 ):#line:1143
        try :#line:1144
            while True :#line:1145
                O0O000OOOO00O0O0O =f'__{timi_new()}'#line:1146
                O00000O0O0O0OO00O ={'source':'scsc','authorization':O0OO0000O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOO00O0O0O ),'signstring':O0O000OOOO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1157
                O0O0O00OOOO0OOO00 =requests .request ('get',f'{host}/energy/general',headers =O00000O0O0O0OO00O ).json ()#line:1158
                if 'status'in O0O0O00OOOO0OOO00 :#line:1160
                    if O0O0O00OOOO0OOO00 ['status']==200 :#line:1161
                        O000OOO0000OOOOOO =O0O0O00OOOO0OOO00 ['data']['ordinary_water']#line:1162
                        O00O00000000OO0O0 =O0O0O00OOOO0OOO00 ['data']['ordinary_fertilizer']#line:1163
                        OOO0OOOO0O00O0OOO =O0O0O00OOOO0OOO00 ['data']['videoStatus']#line:1164
                        O0O0OO000000OO00O =O0O0O00OOOO0OOO00 ['data']['waterVideoKey']#line:1165
                        print (f'【我的营养】:肥料:{str(O00O00000000OO0O0).split(".")[0]}丨水滴:{str(O000OOO0000OOOOOO).split(".")[0]}')#line:1167
                        if float (O00O00000000OO0O0 )<96 :#line:1168
                            if OOO0OOOO0O00O0OOO :#line:1169
                                time .sleep (random .randint (160 ,180 )/10 )#line:1170
                                O0O0O0O0O00O00O00 =99 -float (O00O00000000OO0O0 )#line:1171
                                O000OO0O0O0OOOO0O ={"fertilizer":str (O0O0O0O0O00O00O00 ).split ('.')[0 ]}#line:1172
                                OOOO0O000O0O0OO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00000O0O0O0OO00O ).json ()#line:1174
                                if 'status'in OOOO0O000O0O0OO0O :#line:1176
                                    if OOOO0O000O0O0OO0O ['status']==200 :#line:1177
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO0O000O0O0OO0O["message"]}')#line:1178
                                    if OOOO0O000O0O0OO0O ['status']==500 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO0O000O0O0OO0O["message"]}')#line:1180
                                        break #line:1181
                                if float (O00O00000000OO0O0 )<78 :#line:1183
                                    O0O0O0O0O00O00O00 =80 -float (O00O00000000OO0O0 )#line:1184
                                    OO0OO0O0O0O000000 =f'_fertilizer={int(O0O0O0O0O00O00O00)}_{timi_new()}'#line:1185
                                    OOO0000000O000OO0 ={'source':'scsc','authorization':O0OO0000O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O0O000000 ),'signstring':OO0OO0O0O0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1196
                                    OO0000000O00O000O ={"fertilizer":int (O0O0O0O0O00O00O00 )}#line:1197
                                    O000OO0O00O0OOOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOO0000000O000OO0 ,data =OO0000000O00O000O ).json ()#line:1199
                                    if 'status'in O000OO0O00O0OOOOO :#line:1201
                                        if O000OO0O00O0OOOOO ['status']==200 :#line:1202
                                            print (f'【购买肥料】:购买肥料:{O000OO0O00O0OOOOO["message"]}丨数量:{int(O0O0O0O0O00O00O00)}')#line:1203
                                        if O000OO0O00O0OOOOO ['status']==500 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{O000OO0O00O0OOOOO["message"]}丨数量:{int(O0O0O0O0O00O00O00)}')#line:1205
                                            OOOO0000OO00OOOOO =O000OO0O00O0OOOOO ["message"].split ('-')[1 ]#line:1206
                                            O0O00O00OOOO0OOO0 =f'__{timi_new()}'#line:1207
                                            OO00O0OOOOOOO00O0 ={'source':'scsc','authorization':O0OO0000O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OOOO0OOO0 ),'signstring':O0O00O00OOOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1218
                                            OO00OOOOO00000OO0 =requests .request ('get',f'{host}/user',headers =OO00O0OOOOOOO00O0 ).json ()#line:1219
                                            if 'status'in OO00OOOOO00000OO0 :#line:1220
                                                if OO00OOOOO00000OO0 ['status']==200 :#line:1221
                                                    OO0OOO0O0O0O0OOOO =OO00OOOOO00000OO0 ['data']['inner_id']#line:1222
                                                    if give_gold (OO0OOO0O0O0O0OOOO ,float (OOOO0000OO00OOOOO )+1 ):#line:1223
                                                        O0OO0000O0OO0O0O0 .energy ()#line:1224
                        if float (O000OOO0000OOOOOO )<880 :#line:1225
                            if O0O0OO000000OO00O :#line:1226
                                time .sleep (random .randint (160 ,180 )/10 )#line:1227
                                O000O00O0O000OO00 =999 -float (O000OOO0000OOOOOO )#line:1228
                                O0OOO00O0OO0O0O0O ={"water":str (O000O00O0O000OO00 ).split ('.')[0 ]}#line:1229
                                OOO0O00OOO0O0O00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00000O0O0O0OO00O ).json ()#line:1231
                                if 'status'in OOO0O00OOO0O0O00O :#line:1233
                                    if OOO0O00OOO0O0O00O ['status']==200 :#line:1234
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0O00OOO0O0O00O["message"]}')#line:1235
                                    if OOO0O00OOO0O0O00O ['status']==500 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0O00OOO0O0O00O["message"]}')#line:1237
                                        break #line:1238
                                if float (O000OOO0000OOOOOO )<780 :#line:1239
                                    O000O00O0O000OO00 =800 -float (O000OOO0000OOOOOO )#line:1240
                                    O0000O0000O000OOO =f'_water={int(O000O00O0O000OO00)}_{timi_new()}'#line:1241
                                    O00O0O00000OOO0OO ={'source':'scsc','authorization':O0OO0000O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0000O000OOO ),'signstring':O0000O0000O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1252
                                    OOO0O0000OOO00OOO ={"water":int (O000O00O0O000OO00 )}#line:1253
                                    OO00O000000OOO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00O0O00000OOO0OO ,data =OOO0O0000OOO00OOO ).json ()#line:1255
                                    if 'status'in OO00O000000OOO00O :#line:1257
                                        if OO00O000000OOO00O ['status']==200 :#line:1258
                                            print (f'【购买水滴】:购买水滴:{OO00O000000OOO00O["message"]}丨数量:{int(O000O00O0O000OO00)}')#line:1259
                                        if OO00O000000OOO00O ['status']==500 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{OO00O000000OOO00O["message"]}丨数量:{int(O000O00O0O000OO00)}')#line:1261
                                            OOOO0000OO00OOOOO =OO00O000000OOO00O ["message"].split ('-')[1 ]#line:1262
                                            O0O00O00OOOO0OOO0 =f'__{timi_new()}'#line:1263
                                            OO00O0OOOOOOO00O0 ={'source':'scsc','authorization':O0OO0000O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OOOO0OOO0 ),'signstring':O0O00O00OOOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1274
                                            OO00OOOOO00000OO0 =requests .request ('get',f'{host}/user',headers =OO00O0OOOOOOO00O0 ).json ()#line:1275
                                            if 'status'in OO00OOOOO00000OO0 :#line:1276
                                                if OO00OOOOO00000OO0 ['status']==200 :#line:1277
                                                    OO0OOO0O0O0O0OOOO =OO00OOOOO00000OO0 ['data']['inner_id']#line:1278
                                                    if give_gold (OO0OOO0O0O0O0OOOO ,float (OOOO0000OO00OOOOO )+1 ):#line:1279
                                                        O0OO0000O0OO0O0O0 .energy ()#line:1280
                        break #line:1281
        except Exception as OOOOO0O00OOO0OO00 :#line:1282
            print (OOOOO0O00OOO0OO00 )#line:1283
def bundled_def ():#line:1286
    OO0000OOO0OO0OOO0 =['5570536','7750212','7911652','7911680','7805624']#line:1287
    return OO0000OOO0OO0OOO0 [random .randint (0 ,len (OO0000OOO0OO0OOO0 )-1 )]#line:1288
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
        O0OO0OOOOO0OO00O0 =gitee_edition ()#line:1327
        if version_of_the_validation ()<O0OO0OOOOO0OO00O0 ['CityEarth']['edition']:#line:1328
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0OOOOO0OO00O0["CityEarth"]["edition"]}   ❌')#line:1329
            print (f'更新内容=>>{O0OO0OOOOO0OO00O0["CityEarth"]["content"]}')#line:1330
        else :#line:1331
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0OOOOO0OO00O0["CityEarth"]["edition"]}   ✅')#line:1332
            print (f'更新内容=>> {O0OO0OOOOO0OO00O0["CityEarth"]["content"]}')#line:1333
    except Exception as OO0OO00O0O0O0OO0O :#line:1334
        print (OO0OO00O0O0O0OO0O )#line:1335
def sc3 ():#line:1338
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1339
if __name__ =='__main__':#line:1342
    start ()#line:1343
