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
@ 版本  4.3
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
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
        O0OOOOOO0O0000O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O0OOOOOO0O0000O0O)}个账号==========")#line:16
        for O00000OOOO000OO0O in O0OOOOOO0O0000O0O :#line:17
            OO00OOOO000OOOO00 =[]#line:18
            print (f"------------正在执行第{O0OOOOOO0O0000O0O.index(O00000OOOO000OO0O) + 1}个账号------------")#line:19
            O0000O0000O00O000 =CityEarth (O00000OOOO000OO0O ,OO00OOOO000OOOO00 ,O0OOOOOO0O0000O0O .index (O00000OOOO000OO0O ))#line:20
            def OOO0O0O0O00O0O0OO ():#line:22
                if O0000O0000O00O000 .base_info ():#line:24
                    O0000O0000O00O000 .sealing ()#line:26
                    O0000O0000O00O000 .invitenum ()#line:28
                    O0000O0000O00O000 .query_to_sell ()#line:30
                    O0000O0000O00O000 .game_map ()#line:32
                    O0000O0000O00O000 .friends_invitation ()#line:36
                    O0000O0000O00O000 .energy ()#line:38
                    O0000O0000O00O000 .add_clover ()#line:40
                    O0000O0000O00O000 .propsraffle ()#line:42
                    O0000O0000O00O000 .synthetic ()#line:44
                    O0000O0000O00O000 .crops_illustrated ()#line:46
                    O0000O0000O00O000 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        O0000O0000O00O000 .give_gold ()#line:51
            OOOO00000O0000OO0 =threading .Thread (target =OOO0O0O0O00O0O0OO )#line:53
            OOOO00000O0000OO0 .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        OOO0O0O0O0O00OO0O =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0O0O0O0O00OO0O +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO0O0000O00000000 in invited_new :#line:62
            print (OO0O0000O00000000 )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0OO0OOO00O00O0O in weishim :#line:65
            print (OO0OO0OOO00O00O0O )#line:66
    except Exception as OO00OOO00O0OO00O0 :#line:67
        print (OO00OOO00O0OO00O0 )#line:68
def give_gold (O000OOO0OO0O00O00 ,O000O0O0O0O0OOOO0 ):#line:72
    try :#line:73
        OO00O0O0000O00O0O =f'_doneeNo={O000OOO0OO0O00O00}&quantity={int(O000O0O0O0O0OOOO0)}_{timi_new()}'#line:74
        OOOOO0OOO0000OOO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO00O0O0000O00O0O ),'signstring':OO00O0O0000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        O0O00OOOOO00OO0OO ={"quantity":int (O000O0O0O0O0OOOO0 ),"doneeNo":O000OOO0OO0O00O00 }#line:89
        OO0OO0OO0OO000O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO0OOO0000OOO0 ,data =O0O00OOOOO00OO0OO ).json ()#line:90
        if 'status'in OO0OO0OO0OO000O00 :#line:92
            if OO0OO0OO0OO000O00 ['status']==200 :#line:93
                if OO0OO0OO0OO000O00 ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O000O0O0O0O0OOOO0)}种子给{O000OOO0OO0O00O00}成功')#line:95
                    return True #line:96
            if OO0OO0OO0OO000O00 ['status']==401 :#line:97
                print (f'【赠送种子】:{OO0OO0OO0OO000O00["message"]}')#line:98
                return False #line:99
            if OO0OO0OO0OO000O00 ['status']==500 :#line:100
                print (f'【赠送种子】:{OO0OO0OO0OO000O00["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OO000OOOOO00OO000 :#line:104
        print (OO000OOOOO00OO000 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0OOO0000O0000OOO ):#line:115
    OOO000OO0O0OO000O =hashlib .md5 (O0OOO0000O0000OOO .encode ()).hexdigest ()#line:116
    OOO00O0O0OO0O00O0 =sc1 ()#line:117
    OO0O000OOOOO0OOO0 =sc2 ()#line:118
    OO000O0O000O0O000 =sc3 ()#line:119
    O0OO00O0O0O0OOO00 =OOO00O0O0OO0O00O0 +OOO000OO0O0OO000O +OO0O000OOOOO0OOO0 +OO000O0O000O0O000 #line:120
    O00OO000OO0O000O0 =hashlib .md5 (O0OO00O0O0O0OOO00 .encode ()).hexdigest ()#line:121
    return O00OO000OO0O000O0 #line:122
def format_msg ():#line:125
    O00OOO0O0OO0OO0O0 =""#line:126
    for OOOOO00O000OO0OO0 in msg_list :#line:127
        O00OOO0O0OO0OO0O0 +=str (OOOOO00O000OO0OO0 )+"\r\n"#line:128
    return O00OOO0O0OO0OO0O0 #line:129
def sc1 ():#line:132
    return "scsc%^&*"#line:133
def O000OO0O00OO00O00 ():#line:136
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:137
        ubbbf ()#line:138
    else :#line:139
        oyoy ()#line:140
        exit (1 )#line:141
def timi_new ():#line:144
    return str (int (time .time ()*1000 ))#line:145
json_path ="CityEarth_data.json"#line:148
json_path1 ="CityEarth_data.json"#line:149
dict ={}#line:150
def get_json_data (OOO00O0OOOO0OOO0O ,OOOO0OOOOOO0OOOO0 ,OO000OOOOOOOOOOO0 ,O0O00O0OOOO0OOO0O ):#line:153
    with open (OOO00O0OOOO0OOO0O ,'rb')as O0OOO00OO0O0OOO0O :#line:154
        O0000OO0OOOOO0OOO =json .load (O0OOO00OO0O0OOO0O )#line:155
        O0000OO0OOOOO0OOO ['data'][OOOO0OOOOOO0OOOO0 ][OO000OOOOOOOOOOO0 ]=O0O00O0OOOO0OOO0O #line:156
        OO00O00O000O0O0O0 =O0000OO0OOOOO0OOO #line:157
    O0OOO00OO0O0OOO0O .close ()#line:158
    return OO00O00O000O0O0O0 #line:159
def write_json_data (OOOOOO0O0O0OOO000 ):#line:162
    with open (json_path1 ,'w')as OOO0OOOOO0OOOOOO0 :#line:163
        json .dump (OOOOOO0O0O0OOO000 ,OOO0OOOOO0OOOOOO0 )#line:164
    OOO0OOOOO0OOOOOO0 .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O00OO00000OO0000O ,O0O0OO0OOO00OOOOO ,O0O0O00OO000OO000 ,O0OO0000000000O00 ):#line:171
        try :#line:172
            O00OO00000OO0000O .msg =O0O0O00OO000OO000 #line:173
            O00OO00000OO0000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O00OO00000OO0000O .token =O0O0OO0OOO00OOOOO ['authorization']#line:175
            O00OO00000OO0000O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O00OO00000OO0000O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O00OO00000OO0000O .elephant_user =O0O0OO0OOO00OOOOO ['elephant_user']#line:178
            O00OO00000OO0000O .elephant_pswd =O0O0OO0OOO00OOOOO ['elephant_pswd']#line:179
            O00OO00000OO0000O .elephant_Task_ID =O0O0OO0OOO00OOOOO ['elephant_Task_ID']#line:180
            O00OO00000OO0000O .len_new =O0OO0000000000O00 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (O0O0O000O0OOO0000 ):#line:186
        try :#line:187
            O0O0O000O0OOO0000 .watched_ad ()#line:189
            O00O000O000O00OOO =f'__{timi_new()}'#line:190
            O0OOOO0OO0OO00O0O ={'source':'scsc','authorization':O0O0O000O0OOO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O000O00OOO ),'signstring':O00O000O000O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            OOO000OOO00O00O00 =requests .request ('get',f'{host}/user',headers =O0OOOO0OO0OO00O0O ).json ()#line:202
            if 'status'in OOO000OOO00O00O00 :#line:204
                if OOO000OOO00O00O00 ['status']==200 :#line:205
                    O000O0O0OOO00O00O =OOO000OOO00O00O00 ['data']['nickname']#line:206
                    OO0O0O000OOO0O00O =OOO000OOO00O00O00 ['data']['inner_id']#line:207
                    O0OOO00O0000OOO0O =OOO000OOO00O00O00 ['data']['assets']['gold']#line:208
                    O000OOOOO0OOOOO0O =OOO000OOO00O00O00 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O000O0O0OOO00O00O[:5]}丨ID:{OO0O0O000OOO0O00O}丨等级:{O000OOOOO0OOOOO0O}丨金种子:{str(O0OOO00O0000OOO0O).split(".")[0]}')#line:211
                    if 'wx_'in O000O0O0OOO00O00O :#line:212
                        O0O0O000O0OOO0000 .change_nickname ()#line:213
                if OOO000OOO00O00O00 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if O0O0O000O0OOO0000 .elephant_user =='f':#line:216
                        return False #line:217
                    O000OO0OOO0O0OOOO =Invalid_login .addtask (elephant_user =O0O0O000O0OOO0000 .elephant_user ,elephant_pswd =O0O0O000O0OOO0000 .elephant_pswd ,elephant_Task_ID =O0O0O000O0OOO0000 .elephant_Task_ID )#line:220
                    O00O0OO000OOO0O00 =get_json_data (json_path ,O0O0O000O0OOO0000 .len_new ,'authorization',O000OO0OOO0O0OOOO )#line:221
                    if write_json_data (O00O0OO000OOO0O00 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if OOO000OOO00O00O00 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as OOO00OO00OOO0OO00 :#line:228
            print (OOO00OO00OOO0OO00 )#line:229
    def sealing (OO000O0O0OO0000OO ):#line:232
        try :#line:233
            OOO0OO0OO00O0OOOO =f'__{timi_new()}'#line:234
            O00OOOOOO00O0OO0O ={'source':'scsc','authorization':OO000O0O0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O0OOOO ),'signstring':OOO0OO0OO00O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOOOO00O0OO0O )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOOOO00O0OO0O )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOOOO00O0OO0O )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOOOO00O0OO0O )#line:249
            requests .request ('get',f'{host}/user',headers =O00OOOOOO00O0OO0O )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOOOO00O0OO0O )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOOOO00O0OO0O )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOOOO00O0OO0O )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOOO00O0OO0O )#line:254
            requests .request ('get',f'{host}/assets',headers =O00OOOOOO00O0OO0O )#line:255
        except Exception as OO00OO00OO0000OO0 :#line:256
            print (OO00OO00OO0000OO0 )#line:257
    def ddd (OOOO0OOO0O00OOOO0 ):#line:259
        try :#line:260
            O00OO00OO0O0OOO0O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O00000O0OOOO0O00O ={'source':'scsc','authorization':OOOO0OOO0O00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OO0O0OOO0O ),'signstring':O00OO00OO0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO000000OO0000O00 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O00000O0OOOO0O00O ).json ()#line:273
            print (OO000000OO0000O00 )#line:274
        except Exception as OOOO00OOO00OO00OO :#line:279
            print (OOOO00OOO00OO00OO )#line:280
    def the_query (OOO0OOO0000O000O0 ):#line:290
        try :#line:291
            OO0O0000O0OO0O00O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            O0OOOOOOOOO0O0O0O ={'authorization':OOO0OOO0000O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0OO0O00O ),'signstring':OO0O0000O0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            O00OOO0OO00OO0O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOOOOOOOO0O0O0O ).json ()#line:304
            if 'status'in O00OOO0OO00OO0O0O :#line:306
                if O00OOO0OO00OO0O0O ['status']==200 :#line:307
                    O0OOOOO0O0O0OO00O =O00OOO0OO00OO0O0O ['data']['rows'][4 ]['price']#line:308
                    OOO0OOO0000O000O0 .market_sale (O0OOOOO0O0O0OO00O )#line:309
        except Exception as OOO0O0O0O0OO000OO :#line:310
            print (OOO0O0O0O0OO000OO )#line:311
    def market_sale (O0O0O0OOOOO0O00OO ,O0O0O00OOO000OOOO ):#line:314
        try :#line:315
            O000O0O00O0O00O0O =timi_new ()#line:316
            O0OOOOO0O000OO0OO =f'type=crop__{O000O0O00O0O00O0O}'#line:317
            O000O0OO0O0000O00 ={'source':'scsc','authorization':O0O0O0OOOOO0O00OO .token ,'timestamp':str (O000O0O00O0O00O0O ),'sign':sign (O0OOOOO0O000OO0OO ),'signstring':O0OOOOO0O000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O0000OO0O0O0OOOOO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O000O0OO0O0000O00 ).json ()#line:330
            if 'status'in O0000OO0O0O0OOOOO :#line:332
                if O0000OO0O0O0OOOOO ['status']==200 :#line:333
                    if O0000OO0O0O0OOOOO ['data']['rows']:#line:334
                        OOOOO0OO000O00000 =O0000OO0O0O0OOOOO ['data']['rows'][0 ]['packsackItemId']#line:335
                        O00OOO00OOO000OOO =O0000OO0O0O0OOOOO ['data']['rows'][0 ]['quantity']#line:336
                        O0OOO0O000O0OO00O =float (O0O0O00OOO000OOOO )-0.001 #line:337
                        if O0OOO0O000O0OO00O >9 :#line:338
                            O0000OO0O000OOO0O =f'_packsackItemId={OOOOO0OO000O00000}&price={str(O0O0O00OOO000OOOO)[:5]}&quantity={O00OOO00OOO000OOO}_{O000O0O00O0O00O0O}'#line:339
                            O00OOO00OOO000O0O ={'source':'scsc','authorization':O0O0O0OOOOO0O00OO .token ,'timestamp':str (O000O0O00O0O00O0O ),'sign':sign (O0000OO0O000OOO0O ),'signstring':O0000OO0O000OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O00OOOO0O0OO0OO0O ={"packsackItemId":OOOOO0OO000O00000 ,"price":str (O0O0O00OOO000OOOO )[:5 ],"quantity":str (O00OOO00OOO000OOO )}#line:355
                            OO0OOO0O00O0000OO =requests .request ('post',f'{host}/market/sale',headers =O00OOO00OOO000O0O ,data =O00OOOO0O0OO0OO0O ).json ()#line:356
                            if 'status'in OO0OOO0O00O0000OO :#line:358
                                if OO0OOO0O00O0000OO ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{O00OOO00OOO000OOO}丨价格:{str(O0O0O00OOO000OOOO)[:5]}')#line:360
        except Exception as O0OOOOOO0O000O00O :#line:361
            print (O0OOOOOO0O000O00O )#line:362
    def query_to_sell (OO000000OOO0000OO ):#line:365
        try :#line:366
            OOOO000000OO0OOO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            OO0O0OO000OOOOO00 ={'source':'scsc','authorization':OO000000OOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000000OO0OOO0 ),'signstring':OOOO000000OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            OO000O0O00O000OO0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0O0OO000OOOOO00 ).json ()#line:380
            if 'status'in OO000O0O00O000OO0 :#line:382
                if OO000O0O00O000OO0 ['status']==200 :#line:383
                    for O00OO000O0000OO0O in OO000O0O00O000OO0 ['data']['rows']:#line:384
                        OOOO00O0O0000OO0O =O00OO000O0000OO0O ['materialKey']#line:385
                        O000OOOO0O0O00OO0 =O00OO000O0000OO0O ['quantity']#line:386
                        OOOOO00O0O0O00O00 =O00OO000O0000OO0O ['price']#line:387
                        OO0OOOOO0OO000OOO =O00OO000O0000OO0O ['saleState']#line:388
                        if OO0OOOOO0OO000OOO ==0 :#line:389
                            print (f'【出售订单】:名称:{OOOO00O0O0000OO0O}丨数量:{O000OOOO0O0O00OO0}丨价格:{OOOOO00O0O0O00O00}')#line:390
                            O00OO00O0O0OO00O0 =O00OO000O0000OO0O ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                OO000000OOO0000OO .cacel_sale (O00OO00O0O0OO00O0 )#line:393
        except Exception as O0OOO0OO0OO00000O :#line:394
            print (O0OOO0OO0OO00000O )#line:395
    def cacel_sale (O0OO00OOOOO00OOOO ,O0OOO0O0O00O00OOO ):#line:398
        try :#line:399
            O0O000O00000OO0O0 =f'_saleId={O0OOO0O0O00O00OOO}_{timi_new()}'#line:400
            O0O0OOOOOO0O0O0OO ={'source':'scsc','authorization':O0OO00OOOOO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O00000OO0O0 ),'signstring':O0O000O00000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O0000O0OO0O0OOOO0 ={"saleId":O0OOO0O0O00O00OOO }#line:414
            OOOOOOO0O000OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O0OOOOOO0O0O0OO ,data =O0000O0OO0O0OOOO0 ).json ()#line:415
            if 'status'in OOOOOOO0O000OOOOO :#line:417
                if OOOOOOO0O000OOOOO ['status']==200 :#line:418
                    print (f'【下架出售】:{OOOOOOO0O000OOOOO["data"]}')#line:419
        except Exception as OO0000OOOO0O0O0OO :#line:420
            print (OO0000OOOO0O0O0OO )#line:421
    def change_nickname (O000OO0000OO0O0OO ):#line:424
        try :#line:425
            OO0000O0O000O000O =timi_new ()#line:426
            O0O0O0OO0OOOO0OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OO00OO00OOOOOO0OO =requests .request ('post','https://www.qmsjmfb.com/',data =O0O0O0OO0OOOO0OOO ).text #line:428
            OOO0OOO0O0OOOO00O =re .findall ('<ul><li>(.*?)</li>',OO00OO00OOOOOO0OO )[0 ][:3 ]#line:429
            OO00O0OO000O0O0OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO0OOO0O0OOOO00O}').json ()#line:430
            O000000O0O0OOOOO0 =OO00O0OO000O0O0OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            OO000O0O0OO000000 ={"nickname":O000000O0O0OOOOO0 }#line:432
            O0000OOO0O000O0O0 =f'_nickname={O000000O0O0OOOOO0}_{OO0000O0O000O000O}'#line:433
            O0000OOOOOOO0OO0O ={'source':'scsc','authorization':O000OO0000OO0O0OO .token ,'timestamp':OO0000O0O000O000O ,'sign':sign (O0000OOO0O000O0O0 ),'signstring':O0000OOO0O000O0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            OO00OO000O0OO0000 =requests .request ('patch',f'{host}/user/nickname',headers =O0000OOOOOOO0OO0O ,data =OO000O0O0OO000000 ).json ()#line:445
            if 'status'in OO00OO000O0OO0000 :#line:447
                if OO00OO000O0OO0000 ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{O000000O0O0OOOOO0}丨{OO00OO000O0OO0000["message"]}')#line:449
        except Exception as O0O0O0OOOO0O000O0 :#line:450
            print (O0O0O0OOOO0O000O0 )#line:451
    def withdraw (O00OO0O0OOOOO0O0O ):#line:454
        try :#line:455
            O0OOOO0OOOOO0000O =f'__{timi_new()}'#line:456
            O00OO0O00OO00O0OO ={'source':'scsc','authorization':O00OO0O0OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOOOO0000O ),'signstring':O0OOOO0OOOOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            OO00OO000OOOO0OOO =requests .request ('get',f'{host}/assets',headers =O00OO0O00OO00O0OO ).json ()#line:468
            if 'status'in OO00OO000OOOO0OOO :#line:470
                if OO00OO000OOOO0OOO ['status']==200 :#line:471
                    OO0OO00O0OO000O00 =OO00OO000OOOO0OOO ['data']['cash']#line:472
                    if float (OO0OO00O0OO000O00 )>20 :#line:473
                        O0OOOO0OOOOO0000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O00OO0O00OO00O0OO ={'authorization':O00OO0O0OOOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OOOOO0000O ),'signstring':O0OOOO0OOOOO0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OOOOOO00OO0OOO0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OO0O000OOOO00000O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OO0O00OO00O0OO ,data =OOOOOO00OO0OOO0O0 ).json ()#line:487
                        if 'status'in OO0O000OOOO00000O :#line:489
                            if OO0O000OOOO00000O ['status']==200 :#line:490
                                print (f'【余额提现】:{OO0O000OOOO00000O["data"]}')#line:491
                        if 'status'in OO0O000OOOO00000O :#line:492
                            if OO0O000OOOO00000O ['status']==500 :#line:493
                                print (f'【余额提现】:{OO0O000OOOO00000O["message"]}')#line:494
        except Exception as OO00OOO0OOOOOO0OO :#line:495
            print (OO00OOO0OOOOOO0OO )#line:496
    def invitenum (OO0O000OOOOO00000 ):#line:499
        global invited_new #line:500
        try :#line:501
            OOO00O00OOOO00OO0 =f'__{timi_new()}'#line:502
            OO0O0O0OO00O00OOO ={'source':'scsc','authorization':OO0O000OOOOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OOOO00OO0 ),'signstring':OOO00O00OOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            OOO0000OOOOOO00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0O0O0OO00O00OOO ).json ()#line:514
            if 'status'in OOO0000OOOOOO00O0 :#line:516
                if OOO0000OOOOOO00O0 ['status']==200 :#line:517
                    O00OO0OO00O0O0OOO =OOO0000OOOOOO00O0 ['data']['invited_count']#line:518
                    O0OO00OO0OO000O0O =OOO0000OOOOOO00O0 ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{O00OO0OO00O0O0OOO}丨间邀好友:{O0OO00OO0OO000O0O}')#line:520
                    if O00OO0OO00O0O0OOO <2 :#line:521
                        OO0OOO0OOOOO0OO00 =f'__{timi_new()}'#line:522
                        O0O000OOO0O0O0O0O ={'source':'scsc','authorization':OO0O000OOOOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0OOOOO0OO00 ),'signstring':OO0OOO0OOOOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        OO000OO0O0OOOO00O =requests .request ('get',f'{host}/user',headers =O0O000OOO0O0O0O0O ).json ()#line:534
                        if 'status'in OO000OO0O0OOOO00O :#line:536
                            if OO000OO0O0OOOO00O ['status']==200 :#line:537
                                invited_new .append (OO000OO0O0OOOO00O ['data']['inner_id'])#line:538
        except Exception as O00OO0OO00000OO00 :#line:539
            print (O00OO0OO00000OO00 )#line:540
    def game_map (OO0OO0000OOOOOOOO ):#line:543
        try :#line:544
            OO00000OOOOOOO00O =f'__{timi_new()}'#line:545
            OOO00OOOOOOOOO0O0 ={'source':'scsc','authorization':OO0OO0000OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOOOOOO00O ),'signstring':OO00000OOOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O000O00O0OOOOOO00 =requests .request ('get',f'{host}/game/map',headers =OOO00OOOOOOOOO0O0 ).json ()#line:557
            if 'status'in O000O00O0OOOOOO00 :#line:559
                if O000O00O0OOOOOO00 ['status']==200 :#line:560
                    for OOOOO0OOOO00OO000 in O000O00O0OOOOOO00 ['data']['list'][0 ]['crops']:#line:561
                        OO0O00OO00O0O0O00 =OOOOO0OOOO00OO000 ['level']#line:563
                        if OO0O00OO00O0O0O00 ==41 :#line:564
                            O00O0O00OO0OOOO00 =OOOOO0OOOO00OO000 ['crop_name']#line:565
                            OOOOO0O0O0O00000O =OOOOO0OOOO00OO000 ['count']#line:566
                            if OOOOO0O0O0O00000O >0 :#line:567
                                print (f'【农业资产】:{O00O0O00OO0OOOO00}丨数量:{OOOOO0O0O0O00000O}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    OO0OO0000OOOOOOOO .the_query ()#line:570
        except Exception as O000O000000OO00O0 :#line:571
            print (O000O000000OO00O0 )#line:572
    def give_gold (O0000OOOOO0OO0O0O ):#line:575
        try :#line:576
            OOOO0OO00OOO00OOO =f'__{timi_new()}'#line:577
            OO0000000O0OOOO0O ={'source':'scsc','authorization':O0000OOOOO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00OOO00OOO ),'signstring':OOOO0OO00OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            O0OOOOOO0O0O0OO0O =requests .request ('get',f'{host}/user',headers =OO0000000O0OOOO0O ).json ()#line:589
            if 'status'in O0OOOOOO0O0O0OO0O :#line:590
                if O0OOOOOO0O0O0OO0O ['status']==200 :#line:591
                    if float (O0000OOOOO0OO0O0O .doneeNo )!=0 :#line:592
                        OOO000OOO0000000O =O0OOOOOO0O0O0OO0O ['data']['assets']['gold']#line:593
                        if float (OOO000OOO0000000O )>float (O0000OOOOO0OO0O0O .innerId ):#line:594
                            O0OOOOOO00OO000O0 =int (float (OOO000OOO0000000O )/1.1 )#line:595
                            OOOO0OO00OOO00OOO =f'_doneeNo={O0000OOOOO0OO0O0O.doneeNo}&quantity={O0OOOOOO00OO000O0}_{timi_new()}'#line:596
                            OO0000000O0OOOO0O ={'source':'scsc','authorization':O0000OOOOO0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OO00OOO00OOO ),'signstring':OOOO0OO00OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            OOO0O0OOO00OOO00O ={"quantity":O0OOOOOO00OO000O0 ,"doneeNo":O0000OOOOO0OO0O0O .doneeNo }#line:611
                            OO0OO0000000OO00O =requests .request ('post',f'{host}/finance/give-gold',headers =OO0000000O0OOOO0O ,data =OOO0O0OOO00OOO00O ).json ()#line:612
                            if 'status'in OO0OO0000000OO00O :#line:614
                                if OO0OO0000000OO00O ['status']==200 :#line:615
                                    if OO0OO0000000OO00O ['data']:#line:616
                                        print (f'【赠送种子】:赠送{O0OOOOOO00OO000O0}种子给{O0000OOOOO0OO0O0O.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as OOOOOO000O00OOOOO :#line:620
            print (OOOOOO000O00OOOOO )#line:621
    def invitation (O0000OOO0OOOOO000 ):#line:623
        try :#line:624
            _O00O0OOO000OOOO0O =float (bundled_def ())/4 #line:625
            O0O00OOO00O000000 =f'_innerId={int(_O00O0OOO000OOOO0O)}_{timi_new()}'#line:626
            O0OOOOO00OO0O00OO ={'source':'scsc','authorization':O0000OOO0OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00O000000 ),'signstring':O0O00OOO00O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            O00OO00O0OO0OO00O ={"innerId":int (_O00O0OOO000OOOO0O )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOOOO00OO0O00OO ,data =O00OO00O0OO0OO00O )#line:639
        except Exception as O00000000O0O00O00 :#line:640
            print (O00000000O0O00O00 )#line:641
    def winning_rewards (O0O0O0OOO000O0O00 ):#line:644
        try :#line:645
            O000000OOO000O000 =f'__{timi_new()}'#line:646
            OO0O0OOO0O00OOO0O ={'source':'scsc','authorization':O0O0O0OOO000O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OOO000O000 ),'signstring':O000000OOO000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            O0OOO00OO0OO00O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O0OOO0O00OOO0O ).json ()#line:658
            if 'status'in O0OOO00OO0OO00O00 :#line:660
                if O0OOO00OO0OO00O00 ['status']==200 :#line:661
                    if O0OOO00OO0OO00O00 ['data']['amount']:#line:662
                        OO00O00OO0OO00000 =O0OOO00OO0OO00O00 ['data']['amount']['gold']#line:663
                        return OO00O00OO0OO00000 #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as OO0O00O00OO00O00O :#line:667
            print (OO0O00O00OO00O00O )#line:668
    def certification (OO000OO0OO0O00O0O ):#line:671
        try :#line:672
            OO00OO0O000OOOO0O =f'__{timi_new()}'#line:673
            OO0000O000O00OOOO ={'source':'scsc','authorization':OO000OO0OO0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O000OOOO0O ),'signstring':OO00OO0O000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            O0OO000O0O0O000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0000O000O00OOOO ).json ()#line:685
            if 'status'in O0OO000O0O0O000O0 :#line:687
                if O0OO000O0O0O000O0 ['status']==200 :#line:688
                    if O0OO000O0O0O000O0 ['data']['result']:#line:689
                        O000O0OOOOOOO00O0 =O0OO000O0O0O000O0 ['data']['nick_name']#line:690
                        return O000O0OOOOOOO00O0 #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as O0000O00O000OOO00 :#line:694
            print (O0000O00O000OOO00 )#line:695
    def crops_illustrated (O000000OOOOOOO0O0 ):#line:698
        try :#line:699
            O00OOOOOO00OOOO00 =f'__{timi_new()}'#line:700
            O00OO0O0O0OO0O000 ={'source':'scsc','authorization':O000000OOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO00OOOO00 ),'signstring':O00OOOOOO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            O0O00OO0000O000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OO0O0O0OO0O000 ).json ()#line:712
            if 'status'in O0O00OO0000O000O0 :#line:714
                if O0O00OO0000O000O0 ['status']==200 :#line:715
                    O0OO000O0O0O00OO0 =O0O00OO0000O000O0 ['data'][0 ]['crops']#line:716
                    for O0O0OO0OOOO00O0O0 in O0OO000O0O0O00OO0 :#line:717
                        if O0O0OO0OOOO00O0O0 ['ill_clover_award']:#line:718
                            if float (O0O0OO0OOOO00O0O0 ['ill_clover_award'])>1 :#line:719
                                if O0O0OO0OOOO00O0O0 ['is_finish']:#line:720
                                    if not O0O0OO0OOOO00O0O0 ['is_getit']:#line:721
                                        if O000000OOOOOOO0O0 .certification ()!='未实名':#line:722
                                            O00OOOOOO00OOOO00 =f'_award_level={O0O0OO0OOOO00O0O0["level"]}_{timi_new()}'#line:723
                                            O00OO0O0O0OO0O000 ={'source':'scsc','authorization':O000000OOOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOO00OOOO00 ),'signstring':O00OOOOOO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            O0OO0OO0O00O0O00O ={"award_level":O0O0OO0OOOO00O0O0 ['level']}#line:735
                                            OO0OOOO0OOO0000O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OO0O0O0OO0O000 ,json =O0OO0OO0O00O0O00O ).json ()#line:737
                                            if 'status'in OO0OOOO0OOO0000O0 :#line:738
                                                if OO0OOOO0OOO0000O0 ['status']==200 :#line:739
                                                    OO00O00O0O000OOOO =OO0OOOO0OOO0000O0 ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{O0O0OO0OOOO00O0O0["crop_name"]}成就丨奖励{OO00O00O0O000OOOO}☘️')#line:742
                                                if OO0OOOO0OOO0000O0 ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{OO0OOOO0OOO0000O0["message"]}')#line:744
        except Exception as O0OO000O00O00OOO0 :#line:745
            print (O0OO000O00O00OOO0 )#line:746
    def watched_ad (O0O0000O00OOOOOOO ):#line:749
        try :#line:750
            OO0O0OOOOO0000O00 =f'__{timi_new()}'#line:751
            O000OO00000000O00 ={'source':'scsc','authorization':O0O0000O00OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOO0000O00 ),'signstring':OO0O0OOOOO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            O0OO00OOOOO0O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO00000000O00 ).json ()#line:763
            if 'status'in O0OO00OOOOO0O0OO0 :#line:765
                if O0OO00OOOOO0O0OO0 ['status']==200 :#line:766
                    if 'offlineInfo'in O0OO00OOOOO0O0OO0 ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        O0O0000000O0O000O =O0OO00OOOOO0O0OO0 ['data']['offlineInfo']['off_minute']#line:769
                        OO000OOO0OO000OO0 =float (O0OO00OOOOO0O0OO0 ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000OO00000000O00 ).json ()#line:772
                        time .sleep (2 )#line:773
                        O0OOO00OOO00O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O000OO00000000O00 ).json ()#line:774
                        if 'status'in O0OOO00OOO00O0OO0 :#line:776
                            if O0OOO00OOO00O0OO0 ['status']==200 :#line:777
                                O0OOOO00OO0OOO0OO =float (O0OOO00OOO00O0OO0 ['data']['silver'])/1000000000000 #line:778
                                OO000O00OOO0O0OO0 =str (O0OOOO00OO0OOO0OO -OO000OOO0OO000OO0 )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{O0O0000000O0O000O}分钟奖励🌱数量:{OO000O00OOO0O0OO0}t粒')#line:780
        except Exception as OO0000OO0O0OOOO0O :#line:781
            print (OO0000OO0O0OOOO0O )#line:782
    def user_ad (OOOO0OO00O00000O0 ):#line:785
        try :#line:786
            OO00OOOOOO0OO0O00 =f'__{timi_new()}'#line:787
            O0OOOOO0O00OOO000 ={'source':'scsc','authorization':OOOO0OO00O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO0OO0O00 ),'signstring':OO00OOOOOO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            O000O0O00000O0OO0 =requests .request ('get',f'{host}/user/ad',headers =O0OOOOO0O00OOO000 ).json ()#line:799
            if 'status'in O000O0O00000O0OO0 :#line:801
                if O000O0O00000O0OO0 ['status']==200 :#line:802
                    O0OO00O000O00000O =O000O0O00000O0OO0 ['data']['max_time']#line:803
                    O00O0O00OO0O00OO0 =O000O0O00000O0OO0 ['data']['watch_time']#line:804
                    OOOOO00000O00OOOO =O000O0O00000O0OO0 ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{OOOOO00000O00OOOO + O0OO00O000O00000O - O00O0O00OO0O00OO0}次丨好友提供:{OOOOO00000O00OOOO}次')#line:806
                    if OOOOO00000O00OOOO +O0OO00O000O00000O -O00O0O00OO0O00OO0 >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        O0OOO0O000000OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOOOO0O00OOO000 ).json ()#line:809
                        if 'status'in O0OOO0O000000OO00 :#line:811
                            if O0OOO0O000000OO00 ['status']==200 :#line:812
                                O00O00OOO0O000000 =float (O0OOO0O000000OO00 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(O00O00OOO0O000000)}t粒')#line:814
                                return True #line:815
                            if O0OOO0O000000OO00 ['status']==500 :#line:816
                                OOO00OO0O0O0OO000 =O0OOO0O000000OO00 ['message']#line:817
                                print (f'【获取种子】:{OOO00OO0O0O0OO000}')#line:818
                                return False #line:819
        except Exception as O0O00OOO00O0O0000 :#line:820
            print (O0O00OOO00O0O0000 )#line:821
    def synthetic (OO0OO0OO0OO0000OO ):#line:824
        global id ,g #line:825
        try :#line:826
            O0OO0O000O000000O =OO0OO0OO0OO0000OO .level_new ()#line:827
            OOOOO00000O00OOO0 =random .randint (9 ,11 )#line:828
            OOO000OOOO00OOO0O =f'_site=8&targetSite={OOOOO00000O00OOO0}_{timi_new()}'#line:829
            O00OOOOO00O0O0000 ={'source':'scsc','authorization':OO0OO0OO0OO0000OO .token ,'timestamp':timi_new (),'sign':sign (OOO000OOOO00OOO0O ),'signstring':OOO000OOOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            OO00OOOOOOOO00O0O ={"site":int (8 ),"targetSite":int (OOOOO00000O00OOO0 )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOOO00O0O0000 ,json =OO00OOOOOOOO00O0O )#line:842
            while True :#line:843
                O00O0OOOOO0O0O00O =f'__{timi_new()}'#line:844
                OOOOOO00OO000OOOO ={'source':'scsc','authorization':OO0OO0OO0OO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOO0O0O00O ),'signstring':O00O0OOOOO0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                OO00O0O0O00000O0O =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO00OO000OOOO ).json ()#line:856
                if 'status'in OO00O0O0O00000O0O :#line:858
                    if OO00O0O0O00000O0O ['status']==200 :#line:859
                        O0O0O00OO00O000OO =OO00O0O0O00000O0O ['data']['cropList']#line:860
                        OOOOOO0000O0000OO =OO00O0O0O00000O0O ['data']['gameCoreDataDBid']#line:861
                        O0O000OOOOO0000O0 =float (OO00O0O0O00000O0O ['data']['silver'])/1000000000000 #line:862
                        OOO0OOOOOOOO000OO =0 #line:867
                        for OOO00OOO00OOOOOOO in O0O0O00OO00O000OO :#line:868
                            if not OOO00OOO00OOOOOOO :#line:869
                                O000O000OO000OOOO =f'_crop_id={OOOOOO0000O0000OO}&site={OOO0OOOOOOOO000OO}_{OO0OO0OO0OO0000OO.time}'#line:870
                                OOO0O00O00OOOO000 ={'source':'scsc','authorization':OO0OO0OO0OO0000OO .token ,'timestamp':OO0OO0OO0OO0000OO .time ,'sign':sign (O000O000OO000OOOO ),'signstring':O000O000OO000OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                OO0O0O0O000O0O00O ={"site":OOO0OOOOOOOO000OO ,"crop_id":OOOOOO0000O0000OO }#line:881
                                O00OO0000O0OO000O =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0O00O00OOOO000 ,data =OO0O0O0O000O0O00O ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in O00OO0000O0OO000O :#line:885
                                    if O00OO0000O0OO000O ['status']==200 :#line:886
                                        if O00OO0000O0OO000O ['message']=='种子数量不足':#line:887
                                            O0OO0O000O000000O =OO0OO0OO0OO0000OO .level_new ()#line:888
                                            print (f'【种植合成】:{O00OO0000O0OO000O["message"]}')#line:889
                                            if not OO0OO0OO0OO0000OO .user_ad ():#line:890
                                                return False #line:891
                                    if O00OO0000O0OO000O ['status']==500 :#line:892
                                        print (f'【种植合成】:{O00OO0000O0OO000O["message"]}')#line:893
                                        return False #line:894
                            OOO0OOOOOOOO000OO +=1 #line:895
                        OOO000O00O00O00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO00OO000OOOO ).json ()#line:896
                        OOOO0OO0000000000 =OOO000O00O00O00OO ['data']['cropList']#line:897
                        OOOO0O000O0OOOOOO =False #line:898
                        for OOO00OOO00OOOOOOO in range (12 ):#line:899
                            id =OOOO0OO0000000000 [OOO00OOO00OOOOOOO ]['level']#line:900
                            if float (O0OO0O000O000000O )-float (id )>9 :#line:901
                                OO00O0O0OO00O0O0O =f'_site={OOO00OOO00OOOOOOO}_{timi_new()}'#line:902
                                O0OO0O000OOOOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OO0OO0OO0000OO .token ,'timestamp':timi_new (),'sign':sign (OO00O0O0OO00O0O0O ),'signstring':OO00O0O0OO00O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                O0000OOOOO0OO0O00 ={"site":OOO00OOO00OOOOOOO }#line:914
                                OOO00OO000000O0O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO0O000OOOOOOO0 ,data =O0000OOOOO0OO0O00 ).json ()#line:916
                                if 'status'in OOO00OO000000O0O0 :#line:917
                                    if OOO00OO000000O0O0 ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O0OOOOO000O0O0OO0 in range (11 ):#line:921
                                    O000O00000OO0OOO0 =O0OOOOO000O0O0OO0 +1 #line:922
                                    g =OOOO0OO0000000000 [O000O00000OO0OOO0 ]['level']#line:923
                                    if id ==g :#line:924
                                        O0OO0OO0OOO000000 =O0OOOOO000O0O0OO0 +2 #line:925
                                        if O0OO0OO0OOO000000 !=OOO00OOO00OOOOOOO +1 :#line:926
                                            O0O0OOOOO0O0000OO =OOO00OOO00OOOOOOO +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            OOO000OOOO00OOO0O =f'_site={O0O0OOOOO0O0000OO - 1}&targetSite={O0OO0OO0OOO000000 - 1}_{timi_new()}'#line:930
                                            O00OOOOO00O0O0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OO0OO0OO0000OO .token ,'timestamp':timi_new (),'sign':sign (OOO000OOOO00OOO0O ),'signstring':OOO000OOOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            OO00OOOO0O0O0O0OO ={"site":int (O0O0OOOOO0O0000OO -1 ),"targetSite":int (O0OO0OO0OOO000000 -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OOOOO00O0O0000 ,json =OO00OOOO0O0O0O0OO )#line:949
                                            OOOO0O000O0OOOOOO =True #line:951
                                    if OOOO0O000O0OOOOOO :#line:952
                                        break #line:953
                                if OOOO0O000O0OOOOOO :#line:954
                                    break #line:955
        except :#line:956
            OO0OO0OO0OO0000OO .synthetic ()#line:957
    def level_new (OOOO0O000OOOOO0OO ):#line:960
        try :#line:961
            O00OO0O0O0O0000OO =f'__{timi_new()}'#line:962
            OO00OO00OOO0OO0OO ={'source':'scsc','authorization':OOOO0O000OOOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O0O0000OO ),'signstring':O00OO0O0O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            OOOO00O000O00OOOO =requests .request ('get',f'{host}/user',headers =OO00OO00OOO0OO0OO ).json ()#line:974
            if 'status'in OOOO00O000O00OOOO :#line:975
                if OOOO00O000O00OOOO ['status']==200 :#line:976
                    return float (OOOO00O000O00OOOO ['data']['level'])#line:977
        except Exception as O0O0O0OO0OOO00OO0 :#line:978
            print (O0O0O0OO0OOO00OO0 )#line:979
    def propsraffle (O00OOO0O000OOOOO0 ):#line:982
        try :#line:983
            while True :#line:984
                OOO0O0O0OOO0O0O00 =f'__{timi_new()}'#line:985
                O00000OO00OO0O0OO ={'source':'scsc','authorization':O00OOO0O000OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOO0O0O00 ),'signstring':OOO0O0O0OOO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                OOO0O0OOO0O0O00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00000OO00OO0O0OO ).json ()#line:997
                if 'status'in OOO0O0OOO0O0O00O0 :#line:999
                    if OOO0O0OOO0O0O00O0 ['status']==200 :#line:1000
                        O0OOO00OOO000OO0O =OOO0O0OOO0O0O00O0 ['data']['rows']#line:1001
                        O00OOOOO000O0O000 =OOO0O0OOO0O0O00O0 ['data']['vstate']#line:1002
                        if O0OOO00OOO000OO0O ==5 or O0OOO00OOO000OO0O ==6 or O0OOO00OOO000OO0O ==7 :#line:1003
                            OO0OO00O00OO00OO0 =OOO0O0OOO0O0O00O0 ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{OO0OO00O00OO00OO0}')#line:1005
                        if O0OOO00OOO000OO0O ==1 or O0OOO00OOO000OO0O ==2 or O0OOO00OOO000OO0O ==3 :#line:1006
                            OOOOO0OO0OO0O0O00 =OOO0O0OOO0O0O00O0 ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0OO0OO0O0O00}')#line:1008
                        if O0OOO00OOO000OO0O ==4 or O0OOO00OOO000OO0O ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if O0OOO00OOO000OO0O =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as O00000OO00OO0O00O :#line:1050
            print (O00000OO00OO0O00O )#line:1051
    def friends_invitation (OO00O0O0O0000000O ):#line:1054
        try :#line:1055
            O00000O0OO00OOOO0 =f'__{timi_new()}'#line:1056
            OO00OO00OO0O00O00 ={'source':'scsc','authorization':OO00O0O0O0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO00OOOO0 ),'signstring':O00000O0OO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            OOO00OO000O0OO0OO =requests .request ('get',f'{host}/friends',headers =OO00OO00OO0O00O00 ).json ()#line:1068
            if 'status'in OOO00OO000O0OO0OO :#line:1069
                if OOO00OO000O0OO0OO ['status']==200 :#line:1070
                    OOOOO0000O0000OOO =OOO00OO000O0OO0OO ['data']['myInviteter']#line:1071
                    if OOOOO0000O0000OOO :#line:1072
                        OO000O0O0OOO0O0OO =OOOOO0000O0000OOO ['user']['nickname']#line:1073
                        OOO0000OOOO0000OO =OO00O0O0O0000000O .certification ()#line:1074
                        if OOO0000OOOO0000OO =='未实名':#line:1075
                            weishim .append (OO00O0O0O0000000O .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{OO000O0O0OOO0O0OO}丨实名:{OOO0000OOOO0000OO}')#line:1077
                    else :#line:1078
                        if OO00O0O0O0000000O .innerId !='0':#line:1079
                            OO00O0O0O0000000O .invitation ()#line:1080
        except Exception as O0O0O00000OOO00OO :#line:1081
            print (O0O0O00000OOO00OO )#line:1082
    def add_clover (O0000OOOO0OOOOOOO ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            OOOO0OOOOO0OO0OOO =f'__{timi_new()}'#line:1088
            O0O00OOOO000O0O00 ={'source':'scsc','authorization':O0000OOOO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO0OO0OOO ),'signstring':OOOO0OOOOO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O0O000O000O000OO0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O00OOOO000O0O00 ).json ()#line:1100
            if 'status'in O0O000O000O000OO0 :#line:1102
                if O0O000O000O000OO0 ['status']==200 :#line:1103
                    OOO0OO00O0O00O00O =O0O000O000O000OO0 ['data']['clover']#line:1104
                    OOO0OO0000OOOOOOO =O0O000O000O000OO0 ['data']['used_clover']#line:1105
                    OO00OO00OO00O00O0 =float (OOO0OO00O0O00O00O )-float (OOO0OO0000OOOOOOO )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0OO0000OOOOOOO}')#line:1107
                    if O0000OOOO0OOOOOOO .certification ()!='未实名':#line:1108
                        if OO00OO00OO00O00O0 >1 :#line:1109
                            OOOO0OOOOO0OO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00OO00OO00O00O0)}_{timi_new()}'#line:1110
                            OOOO0O00O00O0OO00 ={'source':'scsc','authorization':O0000OOOO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOO0OO0OOO ),'signstring':OOOO0OOOOO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            O0OO000OO00OO0OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00OO00OO00O00O0 )}#line:1122
                            O0OO0OO00OO0OO000 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0O00O00O0OO00 ,data =O0OO000OO00OO0OOO ).json ()#line:1123
                            if 'status'in O0OO0OO00OO0OO000 :#line:1125
                                if O0OO0OO00OO0OO000 ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO00OO0OO000["data"]["isSuccess"]}丨数量:{OO00OO00OO00O00O0}')#line:1127
                                if O0OO0OO00OO0OO000 ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO00OO0OO000["message"]}')#line:1129
            OO000O0O00000O00O =requests .request ('get',f'{host}/lottery',headers =O0O00OOOO000O0O00 ).json ()#line:1130
            O00O0O0O0OO000000 =O0000OOOO0OOOOOOO .winning_rewards ()#line:1132
            if 'status'in OO000O0O00000O00O :#line:1133
                if OO000O0O00000O00O ['status']==200 :#line:1134
                    OO00000O0OOOOO000 =OO000O0O00000O00O ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (OO00000O0OOOOO000 )#line:1136
                    OO0O0OO00OOOOOO00 =OO000O0O00000O00O ['data'][1 ]['value']#line:1137
                    OO0O00O00000OOO0O =OO000O0O00000O00O ['data'][0 ]['join_number']#line:1138
                    O000000OO000O000O =int (float (OO000O0O00000O00O ['data'][0 ]['totalValue']))#line:1139
                    O000OOO0000O00OOO =float (OO0O0OO00OOOOOO00 /O000000OO000O000O )*10000 #line:1140
                    OOO000O0000OOO000 =O000000OO000O000O /OO0O00O00000OOO0O #line:1141
                    print (f'【参与抽奖】:预计每天中{str(OO00000O0OOOOO000)[:6]}颗金种子丨好友收益:{str(O00O0O0O0OO000000)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O000OOO0000O00OOO)[:6]}颗金种子丨☘️人均:{str(OOO000O0000OOO000)[:7]}️')#line:1143
        except Exception as OOOO0O0O00O000000 :#line:1144
            print (OOOO0O0O00O000000 )#line:1145
    def energy (OO00O000000O00O0O ):#line:1148
        try :#line:1149
            while True :#line:1150
                O00OO0000000O00O0 =f'__{timi_new()}'#line:1151
                OOOOO0O000000O00O ={'source':'scsc','authorization':OO00O000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0000000O00O0 ),'signstring':O00OO0000000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                O0O0OOO000OO0OO0O =requests .request ('get',f'{host}/energy/general',headers =OOOOO0O000000O00O ).json ()#line:1163
                if 'status'in O0O0OOO000OO0OO0O :#line:1165
                    if O0O0OOO000OO0OO0O ['status']==200 :#line:1166
                        OO00000OO00O0O00O =O0O0OOO000OO0OO0O ['data']['ordinary_water']#line:1167
                        O0000O00O000000O0 =O0O0OOO000OO0OO0O ['data']['ordinary_fertilizer']#line:1168
                        OOOO0OO0OO0O00OO0 =O0O0OOO000OO0OO0O ['data']['videoStatus']#line:1169
                        OO0O00OO0OO0OO00O =O0O0OOO000OO0OO0O ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(O0000O00O000000O0).split(".")[0]}丨水滴:{str(OO00000OO00O0O00O).split(".")[0]}')#line:1172
                        if float (O0000O00O000000O0 )<96 :#line:1173
                            if OOOO0OO0OO0O00OO0 :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                OO0O0O00OOOO0OO0O =99 -float (O0000O00O000000O0 )#line:1176
                                O00OO00OO0O00000O ={"fertilizer":str (OO0O0O00OOOO0OO0O ).split ('.')[0 ]}#line:1177
                                O000O0OO0OOO000O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOOO0O000000O00O ).json ()#line:1179
                                if 'status'in O000O0OO0OOO000O0 :#line:1181
                                    if O000O0OO0OOO000O0 ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0OO0OOO000O0["message"]}')#line:1183
                                    if O000O0OO0OOO000O0 ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{O000O0OO0OOO000O0["message"]}')#line:1185
                                        break #line:1186
                                if float (O0000O00O000000O0 )<78 :#line:1188
                                    OO0O0O00OOOO0OO0O =80 -float (O0000O00O000000O0 )#line:1189
                                    OOOOOOO000000OO0O =f'_fertilizer={int(OO0O0O00OOOO0OO0O)}_{timi_new()}'#line:1190
                                    O0O00000O0O000OOO ={'source':'scsc','authorization':OO00O000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000000OO0O ),'signstring':OOOOOOO000000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    OOOOO0O00OO00OO00 ={"fertilizer":int (OO0O0O00OOOO0OO0O )}#line:1202
                                    O000OO00O00OOOOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O00000O0O000OOO ,data =OOOOO0O00OO00OO00 ).json ()#line:1204
                                    if 'status'in O000OO00O00OOOOO0 :#line:1206
                                        if O000OO00O00OOOOO0 ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O000OO00O00OOOOO0["message"]}丨数量:{int(OO0O0O00OOOO0OO0O)}')#line:1208
                                        if O000OO00O00OOOOO0 ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{O000OO00O00OOOOO0["message"]}丨数量:{int(OO0O0O00OOOO0OO0O)}')#line:1210
                                            OO0O0O0OO00O000OO =O000OO00O00OOOOO0 ["message"].split ('-')[1 ]#line:1211
                                            OOOOO00O0O0000O0O =f'__{timi_new()}'#line:1212
                                            OOOOOO00OO0O0O000 ={'source':'scsc','authorization':OO00O000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0O0000O0O ),'signstring':OOOOO00O0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            O0OO0000OOOOOO000 =requests .request ('get',f'{host}/user',headers =OOOOOO00OO0O0O000 ).json ()#line:1224
                                            if 'status'in O0OO0000OOOOOO000 :#line:1225
                                                if O0OO0000OOOOOO000 ['status']==200 :#line:1226
                                                    OO0OOO0O0O000O0OO =O0OO0000OOOOOO000 ['data']['inner_id']#line:1227
                                                    if give_gold (OO0OOO0O0O000O0OO ,float (OO0O0O0OO00O000OO )+1 ):#line:1228
                                                        OO00O000000O00O0O .energy ()#line:1229
                        if float (OO00000OO00O0O00O )<880 :#line:1230
                            if OO0O00OO0OO0OO00O :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                O00000O0O00O0000O =999 -float (OO00000OO00O0O00O )#line:1233
                                OO00O0O00000OO0O0 ={"water":str (O00000O0O00O0000O ).split ('.')[0 ]}#line:1234
                                OOO0OOO0OO000O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOOO0O000000O00O ).json ()#line:1236
                                if 'status'in OOO0OOO0OO000O0OO :#line:1238
                                    if OOO0OOO0OO000O0OO ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOO0OO000O0OO["message"]}')#line:1240
                                    if OOO0OOO0OO000O0OO ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOO0OO000O0OO["message"]}')#line:1242
                                        break #line:1243
                                if float (OO00000OO00O0O00O )<780 :#line:1244
                                    O00000O0O00O0000O =800 -float (OO00000OO00O0O00O )#line:1245
                                    O0OO00O0OO0O0OOOO =f'_water={int(O00000O0O00O0000O)}_{timi_new()}'#line:1246
                                    O0000O00O0O000000 ={'source':'scsc','authorization':OO00O000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0OO0O0OOOO ),'signstring':O0OO00O0OO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    OOOO0OOO00O000OOO ={"water":int (O00000O0O00O0000O )}#line:1258
                                    O0O000O0O00O0OO00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0000O00O0O000000 ,data =OOOO0OOO00O000OOO ).json ()#line:1260
                                    if 'status'in O0O000O0O00O0OO00 :#line:1262
                                        if O0O000O0O00O0OO00 ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{O0O000O0O00O0OO00["message"]}丨数量:{int(O00000O0O00O0000O)}')#line:1264
                                        if O0O000O0O00O0OO00 ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{O0O000O0O00O0OO00["message"]}丨数量:{int(O00000O0O00O0000O)}')#line:1266
                                            OO0O0O0OO00O000OO =O0O000O0O00O0OO00 ["message"].split ('-')[1 ]#line:1267
                                            OOOOO00O0O0000O0O =f'__{timi_new()}'#line:1268
                                            OOOOOO00OO0O0O000 ={'source':'scsc','authorization':OO00O000000O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0O0000O0O ),'signstring':OOOOO00O0O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            O0OO0000OOOOOO000 =requests .request ('get',f'{host}/user',headers =OOOOOO00OO0O0O000 ).json ()#line:1280
                                            if 'status'in O0OO0000OOOOOO000 :#line:1281
                                                if O0OO0000OOOOOO000 ['status']==200 :#line:1282
                                                    OO0OOO0O0O000O0OO =O0OO0000OOOOOO000 ['data']['inner_id']#line:1283
                                                    if give_gold (OO0OOO0O0O000O0OO ,float (OO0O0O0OO00O000OO )+1 ):#line:1284
                                                        OO00O000000O00O0O .energy ()#line:1285
                        break #line:1286
        except Exception as O00OO0O0O00000O00 :#line:1287
            print (O00OO0O0O00000O00 )#line:1288
def bundled_def ():#line:1291
    OOOO0OO0O0OOOOOOO =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return OOOO0OO0O0OOOOOOO [random .randint (0 ,len (OOOO0OO0O0OOOOOOO )-1 )]#line:1293
def version_of_the_validation ():#line:1297
    return str ((99 -56 )/10 )#line:1298
def ubbbf ():#line:1300
    print ('卡密验证通过   ✅')#line:1301
def sc2 ():#line:1304
    return "19319#$%^&*((*"#line:1305
def OO00OO0OO0OO00OO00o0 ():#line:1308
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1310
def get_ip ():#line:1313
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1315
def gitee_validation ():#line:1318
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1319
def gitee_edition ():#line:1322
    try :#line:1323
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1324
    except :#line:1325
        sys .exit (0 )#line:1326
def O000OO000O0O00OOO00 ():#line:1330
    try :#line:1331
        OOO0OOO000000OO0O =gitee_edition ()#line:1332
        if version_of_the_validation ()<OOO0OOO000000OO0O ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOO000000OO0O["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{OOO0OOO000000OO0O["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OOO000000OO0O["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {OOO0OOO000000OO0O["CityEarth"]["content"]}')#line:1338
    except Exception as O0OOO00O0O00O0O0O :#line:1339
        print (O0OOO00O0O00O0O0O )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
