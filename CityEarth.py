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
@ 版本  4.2
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
        O0O00O0O00O0O0OOO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O0O00O0O00O0O0OOO)}个账号==========")#line:16
        for OOOO0O00O0000OOOO in O0O00O0O00O0O0OOO :#line:17
            OOO0O0OO0OO0O00O0 =[]#line:18
            print (f"------------正在执行第{O0O00O0O00O0O0OOO.index(OOOO0O00O0000OOOO) + 1}个账号------------")#line:19
            OO00OO00O00OO0000 =CityEarth (OOOO0O00O0000OOOO ,OOO0O0OO0OO0O00O0 ,O0O00O0O00O0O0OOO .index (OOOO0O00O0000OOOO ))#line:20
            def O0OOOOOOOOOO0O0OO ():#line:22
                if OO00OO00O00OO0000 .base_info ():#line:24
                    OO00OO00O00OO0000 .sealing ()#line:26
                    OO00OO00O00OO0000 .invitenum ()#line:28
                    OO00OO00O00OO0000 .query_to_sell ()#line:30
                    OO00OO00O00OO0000 .game_map ()#line:32
                    OO00OO00O00OO0000 .friends_invitation ()#line:36
                    OO00OO00O00OO0000 .energy ()#line:38
                    OO00OO00O00OO0000 .add_clover ()#line:40
                    OO00OO00O00OO0000 .propsraffle ()#line:42
                    OO00OO00O00OO0000 .synthetic ()#line:44
                    OO00OO00O00OO0000 .crops_illustrated ()#line:46
                    OO00OO00O00OO0000 .withdraw ()#line:48
                    if float (datetime .datetime .now ().hour )>8 :#line:49
                        OO00OO00O00OO0000 .give_gold ()#line:51
            O0OOOOOO0OO0O0O00 =threading .Thread (target =O0OOOOOOOOOO0O0OO )#line:53
            O0OOOOOO0OO0O0O00 .start ()#line:54
            time .sleep (time_xx )#line:55
        print (f"------------正在处理数据------------")#line:56
        time .sleep (0.5 )#line:57
        OOOO00OO000O0OOO0 =format_msg ()#line:58
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOO00OO000O0OOO0 +' ')#line:59
        time .sleep (100 )#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for O0O0O00O0OO00O00O in invited_new :#line:62
            print (O0O0O00O0OO00O00O )#line:63
        print ('开始打印未实名的token')#line:64
        for OO0OO00O0O0OOOOOO in weishim :#line:65
            print (OO0OO00O0O0OOOOOO )#line:66
    except Exception as O0O000O0O0OO0OOOO :#line:67
        print (O0O000O0O0OO0OOOO )#line:68
def give_gold (O000O0O0O0OOO0O0O ,O00OO0O0OO0000OOO ):#line:72
    try :#line:73
        O00OO0000O0O00000 =f'_doneeNo={O000O0O0O0OOO0O0O}&quantity={int(O00OO0O0OO0000OOO)}_{timi_new()}'#line:74
        OO00OOO0OO0OOOO0O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00OO0000O0O00000 ),'signstring':O00OO0000O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO00OO0OO000000OO ={"quantity":int (O00OO0O0OO0000OOO ),"doneeNo":O000O0O0O0OOO0O0O }#line:89
        OOO0OOOO0OO00O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00OOO0OO0OOOO0O ,data =OO00OO0OO000000OO ).json ()#line:90
        if 'status'in OOO0OOOO0OO00O0OO :#line:92
            if OOO0OOOO0OO00O0OO ['status']==200 :#line:93
                if OOO0OOOO0OO00O0OO ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(O00OO0O0OO0000OOO)}种子给{O000O0O0O0OOO0O0O}成功')#line:95
                    return True #line:96
            if OOO0OOOO0OO00O0OO ['status']==401 :#line:97
                print (f'【赠送种子】:{OOO0OOOO0OO00O0OO["message"]}')#line:98
                return False #line:99
            if OOO0OOOO0OO00O0OO ['status']==500 :#line:100
                print (f'【赠送种子】:{OOO0OOOO0OO00O0OO["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as O0O00O00OO0OOOO00 :#line:104
        print (O0O00O00OO0OOOO00 )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O0O0OO00OOOOO00O0 ):#line:115
    O0000OOO00O0O0000 =hashlib .md5 (O0O0OO00OOOOO00O0 .encode ()).hexdigest ()#line:116
    OOOOOO0OOOO0O0OO0 =sc1 ()#line:117
    OOO0OO0O00OOO00O0 =sc2 ()#line:118
    O00OO00OO0OOOOO0O =sc3 ()#line:119
    OOO0OO0OOOOOO000O =OOOOOO0OOOO0O0OO0 +O0000OOO00O0O0000 +OOO0OO0O00OOO00O0 +O00OO00OO0OOOOO0O #line:120
    OOO0OO0O0OO0OO00O =hashlib .md5 (OOO0OO0OOOOOO000O .encode ()).hexdigest ()#line:121
    return OOO0OO0O0OO0OO00O #line:122
def format_msg ():#line:125
    O00OOOOO000000OO0 =""#line:126
    for O0OOO0O0OOOOO0000 in msg_list :#line:127
        O00OOOOO000000OO0 +=str (O0OOO0O0OOOOO0000 )+"\r\n"#line:128
    return O00OOOOO000000OO0 #line:129
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
def get_json_data (OO0O0OO000O0OO0OO ,OOO00OOOO00O0OO00 ,O0000O0OOO0000OO0 ,OO00OO0000O0O0OOO ):#line:153
    with open (OO0O0OO000O0OO0OO ,'rb')as O0O000OO00000O0O0 :#line:154
        OO0O0000OOOOO0O00 =json .load (O0O000OO00000O0O0 )#line:155
        OO0O0000OOOOO0O00 ['data'][OOO00OOOO00O0OO00 ][O0000O0OOO0000OO0 ]=OO00OO0000O0O0OOO #line:156
        OO000OOO0OO00OOOO =OO0O0000OOOOO0O00 #line:157
    O0O000OO00000O0O0 .close ()#line:158
    return OO000OOO0OO00OOOO #line:159
def write_json_data (OO0OOOOOO0OOO00OO ):#line:162
    with open (json_path1 ,'w')as OOOOO0OO0OO00O00O :#line:163
        json .dump (OO0OOOOOO0OOO00OO ,OOOOO0OO0OO00O00O )#line:164
    OOOOO0OO0OO00O00O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (OOO00OOO0000OO0OO ,OOOOO000O0000O000 ,OOO000OOOOOO00000 ,O00O000O00O0O000O ):#line:171
        try :#line:172
            OOO00OOO0000OO0OO .msg =OOO000OOOOOO00000 #line:173
            OOO00OOO0000OO0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            OOO00OOO0000OO0OO .token =OOOOO000O0000O000 ['authorization']#line:175
            OOO00OOO0000OO0OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            OOO00OOO0000OO0OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            OOO00OOO0000OO0OO .elephant_user =OOOOO000O0000O000 ['elephant_user']#line:178
            OOO00OOO0000OO0OO .elephant_pswd =OOOOO000O0000O000 ['elephant_pswd']#line:179
            OOO00OOO0000OO0OO .elephant_Task_ID =OOOOO000O0000O000 ['elephant_Task_ID']#line:180
            OOO00OOO0000OO0OO .len_new =O00O000O00O0O000O #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OOOOOOOOO00OO000O ):#line:186
        try :#line:187
            OOOOOOOOO00OO000O .watched_ad ()#line:189
            O0OOO000000000O00 =f'__{timi_new()}'#line:190
            OOO0OO0OO00O0OO0O ={'source':'scsc','authorization':OOOOOOOOO00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000000000O00 ),'signstring':O0OOO000000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O000OOO0OOOO00OO0 =requests .request ('get',f'{host}/user',headers =OOO0OO0OO00O0OO0O ).json ()#line:202
            if 'status'in O000OOO0OOOO00OO0 :#line:204
                if O000OOO0OOOO00OO0 ['status']==200 :#line:205
                    OO00O0O0O000000O0 =O000OOO0OOOO00OO0 ['data']['nickname']#line:206
                    O0OO0O0OOOO0OOOOO =O000OOO0OOOO00OO0 ['data']['inner_id']#line:207
                    OO0OO0O00O00OO00O =O000OOO0OOOO00OO0 ['data']['assets']['gold']#line:208
                    O0OOO0OO00000OOO0 =O000OOO0OOOO00OO0 ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{OO00O0O0O000000O0[:5]}丨ID:{O0OO0O0OOOO0OOOOO}丨等级:{O0OOO0OO00000OOO0}丨金种子:{str(OO0OO0O00O00OO00O).split(".")[0]}')#line:211
                    if 'wx_'in OO00O0O0O000000O0 :#line:212
                        OOOOOOOOO00OO000O .change_nickname ()#line:213
                if O000OOO0OOOO00OO0 ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OOOOOOOOO00OO000O .elephant_user =='f':#line:216
                        return False #line:217
                    O0OOO0O0000000O0O =Invalid_login .addtask (elephant_user =OOOOOOOOO00OO000O .elephant_user ,elephant_pswd =OOOOOOOOO00OO000O .elephant_pswd ,elephant_Task_ID =OOOOOOOOO00OO000O .elephant_Task_ID )#line:220
                    O0000O0O0O0O0O000 =get_json_data (json_path ,OOOOOOOOO00OO000O .len_new ,'authorization',O0OOO0O0000000O0O )#line:221
                    if write_json_data (O0000O0O0O0O0O000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O000OOO0OOOO00OO0 ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O0OOOO0OO00OOOO0O :#line:228
            print (O0OOOO0OO00OOOO0O )#line:229
    def sealing (OO0OOO00O0OO00O0O ):#line:232
        try :#line:233
            O0OOOOO0O0000000O =f'__{timi_new()}'#line:234
            O0OOO0OOO0OOOOO00 ={'source':'scsc','authorization':OO0OOO00O0OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0000000O ),'signstring':O0OOOOO0O0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0OOO0OOOOO00 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0OOO0OOOOO00 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0OOO0OOOOO00 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0OOO0OOOOO00 )#line:249
            requests .request ('get',f'{host}/user',headers =O0OOO0OOO0OOOOO00 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0OOO0OOOOO00 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0OOO0OOOOO00 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0OOO0OOOOO00 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OOO0OOOOO00 )#line:254
            requests .request ('get',f'{host}/assets',headers =O0OOO0OOO0OOOOO00 )#line:255
        except Exception as OOOOOO0000OO000O0 :#line:256
            print (OOOOOO0000OO000O0 )#line:257
    def ddd (O0O0OOO0O0000000O ):#line:259
        try :#line:260
            O0O0OOOOOO0O00OO0 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O0OO00O0OO0O0OO0O ={'source':'scsc','authorization':O0O0OOO0O0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOOO0O00OO0 ),'signstring':O0O0OOOOOO0O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OOO000O0OOOOOO0O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0OO00O0OO0O0OO0O ).json ()#line:273
            print (OOO000O0OOOOOO0O0 )#line:274
        except Exception as O0O0OOO00OO00O0OO :#line:279
            print (O0O0OOO00OO00O0OO )#line:280
    def the_query (OO000O0O000OOOO0O ):#line:290
        try :#line:291
            OOOOO00OOOO000OOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:292
            OOO00OO0OO000OOOO ={'authorization':OO000O0O000OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOOO000OOO ),'signstring':OOOOO00OOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:302
            O00OOO00O00OOOOO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO00OO0OO000OOOO ).json ()#line:304
            if 'status'in O00OOO00O00OOOOO0 :#line:306
                if O00OOO00O00OOOOO0 ['status']==200 :#line:307
                    O0OO0OOOO0000OO0O =O00OOO00O00OOOOO0 ['data']['rows'][3 ]['price']#line:308
                    OO000O0O000OOOO0O .market_sale (O0OO0OOOO0000OO0O )#line:309
        except Exception as O0O0OO0000O00O00O :#line:310
            print (O0O0OO0000O00O00O )#line:311
    def market_sale (O0OO000OO000OO00O ,O0O00OO00OOOOOO0O ):#line:314
        try :#line:315
            OOOOO00OOOOOO0OOO =timi_new ()#line:316
            O000OO000O0OO0OO0 =f'type=crop__{OOOOO00OOOOOO0OOO}'#line:317
            O00OOOO0O00OOO0OO ={'source':'scsc','authorization':O0OO000OO000OO00O .token ,'timestamp':str (OOOOO00OOOOOO0OOO ),'sign':sign (O000OO000O0OO0OO0 ),'signstring':O000OO000O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:328
            O00OO0O0OO000OOO0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00OOOO0O00OOO0OO ).json ()#line:330
            if 'status'in O00OO0O0OO000OOO0 :#line:332
                if O00OO0O0OO000OOO0 ['status']==200 :#line:333
                    if O00OO0O0OO000OOO0 ['data']['rows']:#line:334
                        OOOOO00O00O00O000 =O00OO0O0OO000OOO0 ['data']['rows'][0 ]['packsackItemId']#line:335
                        O00OO0OOO00O000OO =O00OO0O0OO000OOO0 ['data']['rows'][0 ]['quantity']#line:336
                        OOO00O0OOOO0OOO0O =float (O0O00OO00OOOOOO0O )-0.001 #line:337
                        if OOO00O0OOOO0OOO0O >8 :#line:338
                            O0OOOO00OOOOOOOO0 =f'_packsackItemId={OOOOO00O00O00O000}&price={str(OOO00O0OOOO0OOO0O)[:6]}&quantity={O00OO0OOO00O000OO}_{OOOOO00OOOOOO0OOO}'#line:339
                            OOO0OO0OOOOO00OO0 ={'source':'scsc','authorization':O0OO000OO000OO00O .token ,'timestamp':str (OOOOO00OOOOOO0OOO ),'sign':sign (O0OOOO00OOOOOOOO0 ),'signstring':O0OOOO00OOOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O0O000O0OO0OOO00O ={"packsackItemId":OOOOO00O00O00O000 ,"price":str (OOO00O0OOOO0OOO0O )[:6 ],"quantity":str (O00OO0OOO00O000OO )}#line:355
                            OOO00O0OOO0000O00 =requests .request ('post',f'{host}/market/sale',headers =OOO0OO0OOOOO00OO0 ,data =O0O000O0OO0OOO00O ).json ()#line:356
                            if 'status'in OOO00O0OOO0000O00 :#line:358
                                if OOO00O0OOO0000O00 ['status']==200 :#line:359
                                    print (f'【上架芦荟】:数量:{O00OO0OOO00O000OO}丨价格:{str(OOO00O0OOOO0OOO0O)[:6]}')#line:360
        except Exception as O000O00OOO0000OOO :#line:361
            print (O000O00OOO0000OOO )#line:362
    def query_to_sell (O0O00O0OOOOOOO00O ):#line:365
        try :#line:366
            O0O00OO00OO00OOO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:367
            OO0000O0000OOO00O ={'source':'scsc','authorization':O0O00O0OOOOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00OO00OOO0 ),'signstring':O0O00OO00OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            OO0O000O000000O0O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0000O0000OOO00O ).json ()#line:380
            if 'status'in OO0O000O000000O0O :#line:382
                if OO0O000O000000O0O ['status']==200 :#line:383
                    for OO00O00O00O0OOO0O in OO0O000O000000O0O ['data']['rows']:#line:384
                        O0OO000O0000OOOOO =OO00O00O00O0OOO0O ['materialKey']#line:385
                        O0OOO00OO0O000OO0 =OO00O00O00O0OOO0O ['quantity']#line:386
                        O0O0O0OOO00O0O000 =OO00O00O00O0OOO0O ['price']#line:387
                        OOOO0O00OOO0OOO00 =OO00O00O00O0OOO0O ['saleState']#line:388
                        if OOOO0O00OOO0OOO00 ==0 :#line:389
                            print (f'【出售订单】:名称:{O0OO000O0000OOOOO}丨数量:{O0OOO00OO0O000OO0}丨价格:{O0O0O0OOO00O0O000}')#line:390
                            OOO00000OOOOOOO0O =OO00O00O00O0OOO0O ['id']#line:391
                            if float (datetime .datetime .now ().hour )>8 :#line:392
                                O0O00O0OOOOOOO00O .cacel_sale (OOO00000OOOOOOO0O )#line:393
        except Exception as OOO0O0O000OOO00OO :#line:394
            print (OOO0O0O000OOO00OO )#line:395
    def cacel_sale (OO0O00OOO0O00OOO0 ,OO0O0OO00OO000O00 ):#line:398
        try :#line:399
            OOOOO0OOOOO0OO00O =f'_saleId={OO0O0OO00OO000O00}_{timi_new()}'#line:400
            O00OOOOO00OOOO0OO ={'source':'scsc','authorization':OO0O00OOO0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOOOO0OO00O ),'signstring':OOOOO0OOOOO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
            O00OOOOOOO00O0O0O ={"saleId":OO0O0OO00OO000O00 }#line:414
            OOO0OOOOO00O0O000 =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OOOOO00OOOO0OO ,data =O00OOOOOOO00O0O0O ).json ()#line:415
            if 'status'in OOO0OOOOO00O0O000 :#line:417
                if OOO0OOOOO00O0O000 ['status']==200 :#line:418
                    print (f'【下架出售】:{OOO0OOOOO00O0O000["data"]}')#line:419
        except Exception as OOO00OOO00OOO00O0 :#line:420
            print (OOO00OOO00OOO00O0 )#line:421
    def change_nickname (OO0OOOO0O00OO0O0O ):#line:424
        try :#line:425
            O000OO00O00OOO0O0 =timi_new ()#line:426
            O0OO0O00O0O000OO0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:427
            OOOO0O00O0O000O0O =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO0O00O0O000OO0 ).text #line:428
            OO0O00O00O00OO0O0 =re .findall ('<ul><li>(.*?)</li>',OOOO0O00O0O000O0O )[0 ][:3 ]#line:429
            O00000OO0O0O00OOO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O00O00O00OO0O0}').json ()#line:430
            OOO00OO000000000O =O00000OO0O0O00OOO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:431
            O0OOO00OOOO0OO000 ={"nickname":OOO00OO000000000O }#line:432
            O0OO0000OO0O00O0O =f'_nickname={OOO00OO000000000O}_{O000OO00O00OOO0O0}'#line:433
            OO000OO000O0000OO ={'source':'scsc','authorization':OO0OOOO0O00OO0O0O .token ,'timestamp':O000OO00O00OOO0O0 ,'sign':sign (O0OO0000OO0O00O0O ),'signstring':O0OO0000OO0O00O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:444
            OOO00O00O00OO00OO =requests .request ('patch',f'{host}/user/nickname',headers =OO000OO000O0000OO ,data =O0OOO00OOOO0OO000 ).json ()#line:445
            if 'status'in OOO00O00O00OO00OO :#line:447
                if OOO00O00O00OO00OO ['status']==200 :#line:448
                    print (f'【修改网名】:网名:{OOO00OO000000000O}丨{OOO00O00O00OO00OO["message"]}')#line:449
        except Exception as O000OOOOO0O0OO0O0 :#line:450
            print (O000OOOOO0O0OO0O0 )#line:451
    def withdraw (OOOOOOOOOO000O0O0 ):#line:454
        try :#line:455
            O0000OOOO0000O00O =f'__{timi_new()}'#line:456
            O0O00O00OO00OOOO0 ={'source':'scsc','authorization':OOOOOOOOOO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0000O00O ),'signstring':O0000OOOO0000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:467
            O0OOO00O000OO0O00 =requests .request ('get',f'{host}/assets',headers =O0O00O00OO00OOOO0 ).json ()#line:468
            if 'status'in O0OOO00O000OO0O00 :#line:470
                if O0OOO00O000OO0O00 ['status']==200 :#line:471
                    O00OOO0O0OO0000OO =O0OOO00O000OO0O00 ['data']['cash']#line:472
                    if float (O00OOO0O0OO0000OO )>20 :#line:473
                        O0000OOOO0000O00O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:474
                        O0O00O00OO00OOOO0 ={'authorization':OOOOOOOOOO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0000O00O ),'signstring':O0000OOOO0000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:484
                        OO0000O00O0OOO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:485
                        OOOO00000OO0O0000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O00O00OO00OOOO0 ,data =OO0000O00O0OOO0OO ).json ()#line:487
                        if 'status'in OOOO00000OO0O0000 :#line:489
                            if OOOO00000OO0O0000 ['status']==200 :#line:490
                                print (f'【余额提现】:{OOOO00000OO0O0000["data"]}')#line:491
                        if 'status'in OOOO00000OO0O0000 :#line:492
                            if OOOO00000OO0O0000 ['status']==500 :#line:493
                                print (f'【余额提现】:{OOOO00000OO0O0000["message"]}')#line:494
        except Exception as O0OO0OOOO000O0OO0 :#line:495
            print (O0OO0OOOO000O0OO0 )#line:496
    def invitenum (OOOOOOO0O0000O000 ):#line:499
        global invited_new #line:500
        try :#line:501
            OO0O000O0000O0OO0 =f'__{timi_new()}'#line:502
            OOOO00O0OO00OOO0O ={'source':'scsc','authorization':OOOOOOO0O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O0000O0OO0 ),'signstring':OO0O000O0000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:513
            OO00OOOOO0000O0OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO00O0OO00OOO0O ).json ()#line:514
            if 'status'in OO00OOOOO0000O0OO :#line:516
                if OO00OOOOO0000O0OO ['status']==200 :#line:517
                    OO0OO0O0OO0O0OO00 =OO00OOOOO0000O0OO ['data']['invited_count']#line:518
                    O0OOO00OO0OOOO00O =OO00OOOOO0000O0OO ['data']['invited_second_count']#line:519
                    print (f'【我的邀请】:直邀好友:{OO0OO0O0OO0O0OO00}丨间邀好友:{O0OOO00OO0OOOO00O}')#line:520
                    if OO0OO0O0OO0O0OO00 <2 :#line:521
                        O00OO000OOOO0O00O =f'__{timi_new()}'#line:522
                        O0OOOO00OOO00O0OO ={'source':'scsc','authorization':OOOOOOO0O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OOOO0O00O ),'signstring':O00OO000OOOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:533
                        O0OOO00O00OOO000O =requests .request ('get',f'{host}/user',headers =O0OOOO00OOO00O0OO ).json ()#line:534
                        if 'status'in O0OOO00O00OOO000O :#line:536
                            if O0OOO00O00OOO000O ['status']==200 :#line:537
                                invited_new .append (O0OOO00O00OOO000O ['data']['inner_id'])#line:538
        except Exception as O0O0OO000OOO0O0O0 :#line:539
            print (O0O0OO000OOO0O0O0 )#line:540
    def game_map (O00O0O000O0OOOO00 ):#line:543
        try :#line:544
            O0O0O00OO0OO0OOO0 =f'__{timi_new()}'#line:545
            O00O0O000000000O0 ={'source':'scsc','authorization':O00O0O000O0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OO0OO0OOO0 ),'signstring':O0O0O00OO0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O0O00O00OOO0O0000 =requests .request ('get',f'{host}/game/map',headers =O00O0O000000000O0 ).json ()#line:557
            if 'status'in O0O00O00OOO0O0000 :#line:559
                if O0O00O00OOO0O0000 ['status']==200 :#line:560
                    for OO000OOO0O00OO0OO in O0O00O00OOO0O0000 ['data']['list'][0 ]['crops']:#line:561
                        OOOO00OO0O0O0O00O =OO000OOO0O00OO0OO ['level']#line:563
                        if OOOO00OO0O0O0O00O ==41 :#line:564
                            OO0O0OOOO0OO00O0O =OO000OOO0O00OO0OO ['crop_name']#line:565
                            O000OO0OOOO0O0OO0 =OO000OOO0O00OO0OO ['count']#line:566
                            if O000OO0OOOO0O0OO0 >0 :#line:567
                                print (f'【农业资产】:{OO0O0OOOO0OO00O0O}丨数量:{O000OO0OOOO0O0OO0}')#line:568
                                if float (datetime .datetime .now ().hour )>8 :#line:569
                                    O00O0O000O0OOOO00 .the_query ()#line:570
        except Exception as O0000OO00OO0OOO00 :#line:571
            print (O0000OO00OO0OOO00 )#line:572
    def give_gold (OOO0000000O00OO00 ):#line:575
        try :#line:576
            OOO00O00O00OOOOO0 =f'__{timi_new()}'#line:577
            OO000O0OOOO0O0OOO ={'source':'scsc','authorization':OOO0000000O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O00OOOOO0 ),'signstring':OOO00O00O00OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:588
            OOOOO0OO00O000000 =requests .request ('get',f'{host}/user',headers =OO000O0OOOO0O0OOO ).json ()#line:589
            if 'status'in OOOOO0OO00O000000 :#line:590
                if OOOOO0OO00O000000 ['status']==200 :#line:591
                    if float (OOO0000000O00OO00 .doneeNo )!=0 :#line:592
                        O0O00O00OOOO00000 =OOOOO0OO00O000000 ['data']['assets']['gold']#line:593
                        if float (O0O00O00OOOO00000 )>float (OOO0000000O00OO00 .innerId ):#line:594
                            O0O000OOO0O00OO0O =int (float (O0O00O00OOOO00000 )/1.1 )#line:595
                            OOO00O00O00OOOOO0 =f'_doneeNo={OOO0000000O00OO00.doneeNo}&quantity={O0O000OOO0O00OO0O}_{timi_new()}'#line:596
                            OO000O0OOOO0O0OOO ={'source':'scsc','authorization':OOO0000000O00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O00OOOOO0 ),'signstring':OOO00O00O00OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
                            O00OOOOOOOO00OOO0 ={"quantity":O0O000OOO0O00OO0O ,"doneeNo":OOO0000000O00OO00 .doneeNo }#line:611
                            O0OOO000OOO00OOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO000O0OOOO0O0OOO ,data =O00OOOOOOOO00OOO0 ).json ()#line:612
                            if 'status'in O0OOO000OOO00OOO0 :#line:614
                                if O0OOO000OOO00OOO0 ['status']==200 :#line:615
                                    if O0OOO000OOO00OOO0 ['data']:#line:616
                                        print (f'【赠送种子】:赠送{O0O000OOO0O00OO0O}种子给{OOO0000000O00OO00.doneeNo}成功')#line:617
                    else :#line:618
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:619
        except Exception as O00OOO0OO0O00O000 :#line:620
            print (O00OOO0OO0O00O000 )#line:621
    def invitation (OOO0O00OOO00OO00O ):#line:623
        try :#line:624
            _O0000OOOOO0OOOOOO =float (bundled_def ())/4 #line:625
            OO0OOO00OO0O00OO0 =f'_innerId={int(_O0000OOOOO0OOOOOO)}_{timi_new()}'#line:626
            OOOO00OO0000O0O00 ={'source':'scsc','authorization':OOO0O00OOO00OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00OO0O00OO0 ),'signstring':OO0OOO00OO0O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:637
            OO0O00O0000O0OO00 ={"innerId":int (_O0000OOOOO0OOOOOO )}#line:638
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00OO0000O0O00 ,data =OO0O00O0000O0OO00 )#line:639
        except Exception as O0OO0OO0OOOOOOOO0 :#line:640
            print (O0OO0OO0OOOOOOOO0 )#line:641
    def winning_rewards (O0OO0O0O0O00000OO ):#line:644
        try :#line:645
            OOOO0O0OOO0O0000O =f'__{timi_new()}'#line:646
            OO0O0OO0O0OO00OOO ={'source':'scsc','authorization':O0OO0O0O0O00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OOO0O0000O ),'signstring':OOOO0O0OOO0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:657
            OO00OOO00O0O00OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O0OO0O0OO00OOO ).json ()#line:658
            if 'status'in OO00OOO00O0O00OO0 :#line:660
                if OO00OOO00O0O00OO0 ['status']==200 :#line:661
                    if OO00OOO00O0O00OO0 ['data']['amount']:#line:662
                        O00OOOOOO00OOO00O =OO00OOO00O0O00OO0 ['data']['amount']['gold']#line:663
                        return O00OOOOOO00OOO00O #line:664
                    else :#line:665
                        return 0 #line:666
        except Exception as O0000O000O00O0O00 :#line:667
            print (O0000O000O00O0O00 )#line:668
    def certification (OOO0O00OO0OOOO0OO ):#line:671
        try :#line:672
            O0OOO0O00OOOOOOO0 =f'__{timi_new()}'#line:673
            O0OOO0O0O00OO0O0O ={'source':'scsc','authorization':OOO0O00OO0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00OOOOOOO0 ),'signstring':O0OOO0O00OOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
            OO0O0O0OO0OOO0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OOO0O0O00OO0O0O ).json ()#line:685
            if 'status'in OO0O0O0OO0OOO0O00 :#line:687
                if OO0O0O0OO0OOO0O00 ['status']==200 :#line:688
                    if OO0O0O0OO0OOO0O00 ['data']['result']:#line:689
                        OO0O0OOO0OO00O0OO =OO0O0O0OO0OOO0O00 ['data']['nick_name']#line:690
                        return OO0O0OOO0OO00O0OO #line:691
                    else :#line:692
                        return '未实名'#line:693
        except Exception as O00OOO0O0O0O0O000 :#line:694
            print (O00OOO0O0O0O0O000 )#line:695
    def crops_illustrated (OO00OOOOOOOO00O00 ):#line:698
        try :#line:699
            OOOO0000OOO0OOO0O =f'__{timi_new()}'#line:700
            O0O000OOO0OOO0OO0 ={'source':'scsc','authorization':OO00OOOOOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OOO0OOO0O ),'signstring':OOOO0000OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OO000OO0000OOO00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O000OOO0OOO0OO0 ).json ()#line:712
            if 'status'in OO000OO0000OOO00O :#line:714
                if OO000OO0000OOO00O ['status']==200 :#line:715
                    O0000OOO0OOO000O0 =OO000OO0000OOO00O ['data'][0 ]['crops']#line:716
                    for OO0O000O0OO000OOO in O0000OOO0OOO000O0 :#line:717
                        if OO0O000O0OO000OOO ['ill_clover_award']:#line:718
                            if float (OO0O000O0OO000OOO ['ill_clover_award'])>1 :#line:719
                                if OO0O000O0OO000OOO ['is_finish']:#line:720
                                    if not OO0O000O0OO000OOO ['is_getit']:#line:721
                                        if OO00OOOOOOOO00O00 .certification ()!='未实名':#line:722
                                            OOOO0000OOO0OOO0O =f'_award_level={OO0O000O0OO000OOO["level"]}_{timi_new()}'#line:723
                                            O0O000OOO0OOO0OO0 ={'source':'scsc','authorization':OO00OOOOOOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OOO0OOO0O ),'signstring':OOOO0000OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:734
                                            OO0O0O00OO0O0O000 ={"award_level":OO0O000O0OO000OOO ['level']}#line:735
                                            OOO00000000OO0O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O000OOO0OOO0OO0 ,json =OO0O0O00OO0O0O000 ).json ()#line:737
                                            if 'status'in OOO00000000OO0O00 :#line:738
                                                if OOO00000000OO0O00 ['status']==200 :#line:739
                                                    O00O00000OO0O0O0O =OOO00000000OO0O00 ['data']['ill_clover_award']#line:740
                                                    print (f'【图鉴奖励】:领取{OO0O000O0OO000OOO["crop_name"]}成就丨奖励{O00O00000OO0O0O0O}☘️')#line:742
                                                if OOO00000000OO0O00 ['status']==500 :#line:743
                                                    print (f'【图鉴奖励】:{OOO00000000OO0O00["message"]}')#line:744
        except Exception as O00OOO0000000O00O :#line:745
            print (O00OOO0000000O00O )#line:746
    def watched_ad (O00O0O00000O0OO0O ):#line:749
        try :#line:750
            OOO0O0O00OO00OO00 =f'__{timi_new()}'#line:751
            OO0O000OOOOO0O0OO ={'source':'scsc','authorization':O00O0O00000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00OO00OO00 ),'signstring':OOO0O0O00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            OOOO000OOOO0O000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000OOOOO0O0OO ).json ()#line:763
            if 'status'in OOOO000OOOO0O000O :#line:765
                if OOOO000OOOO0O000O ['status']==200 :#line:766
                    if 'offlineInfo'in OOOO000OOOO0O000O ['data']:#line:767
                        time .sleep (random .randint (1 ,3 ))#line:768
                        OOOOO0OOOO0OOOO00 =OOOO000OOOO0O000O ['data']['offlineInfo']['off_minute']#line:769
                        OO000OO0O00O0OO00 =float (OOOO000OOOO0O000O ['data']['silver'])/1000000000000 #line:770
                        time .sleep (1 )#line:771
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0O000OOOOO0O0OO ).json ()#line:772
                        time .sleep (2 )#line:773
                        OO0O0OO0O0O000OOO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O000OOOOO0O0OO ).json ()#line:774
                        if 'status'in OO0O0OO0O0O000OOO :#line:776
                            if OO0O0OO0O0O000OOO ['status']==200 :#line:777
                                O0OOO0OO00O00000O =float (OO0O0OO0O0O000OOO ['data']['silver'])/1000000000000 #line:778
                                OOO000O0O0000O000 =str (O0OOO0OO00O00000O -OO000OO0O00O0OO00 )[:6 ]#line:779
                                print (f'【离线奖励】:翻倍离线{OOOOO0OOOO0OOOO00}分钟奖励🌱数量:{OOO000O0O0000O000}t粒')#line:780
        except Exception as OOO0000O0OO0OO00O :#line:781
            print (OOO0000O0OO0OO00O )#line:782
    def user_ad (OO0O000O00O0OOOOO ):#line:785
        try :#line:786
            OO0O000000000O00O =f'__{timi_new()}'#line:787
            OO00OO000O0OOOOO0 ={'source':'scsc','authorization':OO0O000O00O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000000000O00O ),'signstring':OO0O000000000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:798
            OOO0O0OO0OOOOO0OO =requests .request ('get',f'{host}/user/ad',headers =OO00OO000O0OOOOO0 ).json ()#line:799
            if 'status'in OOO0O0OO0OOOOO0OO :#line:801
                if OOO0O0OO0OOOOO0OO ['status']==200 :#line:802
                    O0O000OOO0000OO0O =OOO0O0OO0OOOOO0OO ['data']['max_time']#line:803
                    OO00OOOOOOOO00OOO =OOO0O0OO0OOOOO0OO ['data']['watch_time']#line:804
                    O0O00OOOOOOOOO000 =OOO0O0OO0OOOOO0OO ['data']['added_time']#line:805
                    print (f'【获取种子】:获取🌱剩余{O0O00OOOOOOOOO000 + O0O000OOO0000OO0O - OO00OOOOOOOO00OOO}次丨好友提供:{O0O00OOOOOOOOO000}次')#line:806
                    if O0O00OOOOOOOOO000 +O0O000OOO0000OO0O -OO00OOOOOOOO00OOO >0 :#line:807
                        time .sleep (random .randint (16 ,19 ))#line:808
                        O00000O000OO00000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00OO000O0OOOOO0 ).json ()#line:809
                        if 'status'in O00000O000OO00000 :#line:811
                            if O00000O000OO00000 ['status']==200 :#line:812
                                OOOO0O00O0O0O0000 =float (O00000O000OO00000 ['data']['silver'])/1000000000000 #line:813
                                print (f'【获取种子】:获得🌱:{int(OOOO0O00O0O0O0000)}t粒')#line:814
                                return True #line:815
                            if O00000O000OO00000 ['status']==500 :#line:816
                                O0OOOO00OOOO00OOO =O00000O000OO00000 ['message']#line:817
                                print (f'【获取种子】:{O0OOOO00OOOO00OOO}')#line:818
                                return False #line:819
        except Exception as O00OOO00OO000O00O :#line:820
            print (O00OOO00OO000O00O )#line:821
    def synthetic (OO0OOOO000OO0000O ):#line:824
        global id ,g #line:825
        try :#line:826
            O00O00000O00OO0O0 =OO0OOOO000OO0000O .level_new ()#line:827
            OO0000O00O00OOOO0 =random .randint (9 ,11 )#line:828
            O0O0O00O00OO0OO0O =f'_site=8&targetSite={OO0000O00O00OOOO0}_{timi_new()}'#line:829
            O000000OO0OO00000 ={'source':'scsc','authorization':OO0OOOO000OO0000O .token ,'timestamp':timi_new (),'sign':sign (O0O0O00O00OO0OO0O ),'signstring':O0O0O00O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:840
            O000OOOO0OOOO00O0 ={"site":int (8 ),"targetSite":int (OO0000O00O00OOOO0 )}#line:841
            requests .request ('post',f'{host}/game/crops/move',headers =O000000OO0OO00000 ,json =O000OOOO0OOOO00O0 )#line:842
            while True :#line:843
                O0O00OO000O0OO0O0 =f'__{timi_new()}'#line:844
                OOO00O0000O00OO0O ={'source':'scsc','authorization':OO0OOOO000OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO000O0OO0O0 ),'signstring':O0O00OO000O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:855
                O0000O0000OO0O000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0000O00OO0O ).json ()#line:856
                if 'status'in O0000O0000OO0O000 :#line:858
                    if O0000O0000OO0O000 ['status']==200 :#line:859
                        OO00OOO0O0OOO000O =O0000O0000OO0O000 ['data']['cropList']#line:860
                        OOOO0OOO0O000O0OO =O0000O0000OO0O000 ['data']['gameCoreDataDBid']#line:861
                        OO0OOOO0OO000O0OO =float (O0000O0000OO0O000 ['data']['silver'])/1000000000000 #line:862
                        OOO00OOOO0O0O0O00 =0 #line:867
                        for O0000OO00O000OOOO in OO00OOO0O0OOO000O :#line:868
                            if not O0000OO00O000OOOO :#line:869
                                OOO0OO0O00000OOO0 =f'_crop_id={OOOO0OOO0O000O0OO}&site={OOO00OOOO0O0O0O00}_{OO0OOOO000OO0000O.time}'#line:870
                                OOO0O0O00O0OOOOOO ={'source':'scsc','authorization':OO0OOOO000OO0000O .token ,'timestamp':OO0OOOO000OO0000O .time ,'sign':sign (OOO0OO0O00000OOO0 ),'signstring':OOO0OO0O00000OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:880
                                OOO0000000O000O0O ={"site":OOO00OOOO0O0O0O00 ,"crop_id":OOOO0OOO0O000O0OO }#line:881
                                O000O00OOOO00O000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0O0O00O0OOOOOO ,data =OOO0000000O000O0O ).json ()#line:882
                                time .sleep (random .randint (1 ,3 )/10 )#line:884
                                if 'status'in O000O00OOOO00O000 :#line:885
                                    if O000O00OOOO00O000 ['status']==200 :#line:886
                                        if O000O00OOOO00O000 ['message']=='种子数量不足':#line:887
                                            O00O00000O00OO0O0 =OO0OOOO000OO0000O .level_new ()#line:888
                                            print (f'【种植合成】:{O000O00OOOO00O000["message"]}')#line:889
                                            if not OO0OOOO000OO0000O .user_ad ():#line:890
                                                return False #line:891
                                    if O000O00OOOO00O000 ['status']==500 :#line:892
                                        print (f'【种植合成】:{O000O00OOOO00O000["message"]}')#line:893
                                        return False #line:894
                            OOO00OOOO0O0O0O00 +=1 #line:895
                        OOO00O0O00OOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0000O00OO0O ).json ()#line:896
                        O00O0O0OO0O000000 =OOO00O0O00OOO00OO ['data']['cropList']#line:897
                        OO0O0000OO0000OO0 =False #line:898
                        for O0000OO00O000OOOO in range (12 ):#line:899
                            id =O00O0O0OO0O000000 [O0000OO00O000OOOO ]['level']#line:900
                            if float (O00O00000O00OO0O0 )-float (id )>9 :#line:901
                                OOO0OOOO0000OO0O0 =f'_site={O0000OO00O000OOOO}_{timi_new()}'#line:902
                                OOO000000O00O00OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOOO000OO0000O .token ,'timestamp':timi_new (),'sign':sign (OOO0OOOO0000OO0O0 ),'signstring':OOO0OOOO0000OO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:913
                                OO0O0OO0O00OO00OO ={"site":O0000OO00O000OOOO }#line:914
                                OO00O00O0OO0000O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO000000O00O00OO ,data =OO0O0OO0O00OO00OO ).json ()#line:916
                                if 'status'in OO00O00O0OO0000O0 :#line:917
                                    if OO00O00O0OO0000O0 ['status']==200 :#line:918
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:919
                            if id !=0 :#line:920
                                for O00O0O000OO0O0O00 in range (11 ):#line:921
                                    OOO00OO0O0000000O =O00O0O000OO0O0O00 +1 #line:922
                                    g =O00O0O0OO0O000000 [OOO00OO0O0000000O ]['level']#line:923
                                    if id ==g :#line:924
                                        O000O0OO00O00O00O =O00O0O000OO0O0O00 +2 #line:925
                                        if O000O0OO00O00O00O !=O0000OO00O000OOOO +1 :#line:926
                                            O0000OOOO0OO000OO =O0000OO00O000OOOO +1 #line:927
                                            time .sleep (random .randint (1 ,3 )/10 )#line:929
                                            O0O0O00O00OO0OO0O =f'_site={O0000OOOO0OO000OO - 1}&targetSite={O000O0OO00O00O00O - 1}_{timi_new()}'#line:930
                                            O000000OO0OO00000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0OOOO000OO0000O .token ,'timestamp':timi_new (),'sign':sign (O0O0O00O00OO0OO0O ),'signstring':O0O0O00O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:947
                                            O00OOOOOO00OOOOO0 ={"site":int (O0000OOOO0OO000OO -1 ),"targetSite":int (O000O0OO00O00O00O -1 )}#line:948
                                            requests .request ('post',f'{host}/game/crops/move',headers =O000000OO0OO00000 ,json =O00OOOOOO00OOOOO0 )#line:949
                                            OO0O0000OO0000OO0 =True #line:951
                                    if OO0O0000OO0000OO0 :#line:952
                                        break #line:953
                                if OO0O0000OO0000OO0 :#line:954
                                    break #line:955
        except :#line:956
            OO0OOOO000OO0000O .synthetic ()#line:957
    def level_new (O0O00OO0OOO0000O0 ):#line:960
        try :#line:961
            OOO00000OOOOO000O =f'__{timi_new()}'#line:962
            OOOO0OO0OO0O0O0O0 ={'source':'scsc','authorization':O0O00OO0OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000OOOOO000O ),'signstring':OOO00000OOOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:973
            O000000OOOO000O00 =requests .request ('get',f'{host}/user',headers =OOOO0OO0OO0O0O0O0 ).json ()#line:974
            if 'status'in O000000OOOO000O00 :#line:975
                if O000000OOOO000O00 ['status']==200 :#line:976
                    return float (O000000OOOO000O00 ['data']['level'])#line:977
        except Exception as OO0O0O000OO0O000O :#line:978
            print (OO0O0O000OO0O000O )#line:979
    def propsraffle (O0OOOO0O00000000O ):#line:982
        try :#line:983
            while True :#line:984
                O0000O00000000O00 =f'__{timi_new()}'#line:985
                O0O0O0OO0O0000O0O ={'source':'scsc','authorization':O0OOOO0O00000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00000000O00 ),'signstring':O0000O00000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                O000O0OOOOO0O0O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O0O0OO0O0000O0O ).json ()#line:997
                if 'status'in O000O0OOOOO0O0O0O :#line:999
                    if O000O0OOOOO0O0O0O ['status']==200 :#line:1000
                        O0OOO000OOOOOOO0O =O000O0OOOOO0O0O0O ['data']['rows']#line:1001
                        O0OOO00O000O00OOO =O000O0OOOOO0O0O0O ['data']['vstate']#line:1002
                        if O0OOO000OOOOOOO0O ==5 or O0OOO000OOOOOOO0O ==6 or O0OOO000OOOOOOO0O ==7 :#line:1003
                            OO0000OO00000OOO0 =O000O0OOOOO0O0O0O ['data']['silver']#line:1004
                            print (f'【转盘抽奖】:获得种子:{OO0000OO00000OOO0}')#line:1005
                        if O0OOO000OOOOOOO0O ==1 or O0OOO000OOOOOOO0O ==2 or O0OOO000OOOOOOO0O ==3 :#line:1006
                            O0OO0000O0OO00O00 =O000O0OOOOO0O0O0O ['data']['clover']#line:1007
                            print (f'【转盘抽奖】:获得三叶草:{O0OO0000O0OO00O00}')#line:1008
                        if O0OOO000OOOOOOO0O ==4 or O0OOO000OOOOOOO0O ==8 :#line:1009
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1010
                        if O0OOO000OOOOOOO0O =='抽奖次数已用完':#line:1014
                            break #line:1048
                time .sleep (random .randint (8 ,15 )/10 )#line:1049
        except Exception as O0000O000O0OO0OOO :#line:1050
            print (O0000O000O0OO0OOO )#line:1051
    def friends_invitation (OOO0OO0O0O00OOOOO ):#line:1054
        try :#line:1055
            OO00O000O000OO00O =f'__{timi_new()}'#line:1056
            OO0O00OO0OO0OO0O0 ={'source':'scsc','authorization':OOO0OO0O0O00OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O000OO00O ),'signstring':OO00O000O000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            O0OO0O00O00OO00OO =requests .request ('get',f'{host}/friends',headers =OO0O00OO0OO0OO0O0 ).json ()#line:1068
            if 'status'in O0OO0O00O00OO00OO :#line:1069
                if O0OO0O00O00OO00OO ['status']==200 :#line:1070
                    O00O0OO00O0O000OO =O0OO0O00O00OO00OO ['data']['myInviteter']#line:1071
                    if O00O0OO00O0O000OO :#line:1072
                        O00OO0OOOO00OO000 =O00O0OO00O0O000OO ['user']['nickname']#line:1073
                        OO0OO0O0000OOO0OO =OOO0OO0O0O00OOOOO .certification ()#line:1074
                        if OO0OO0O0000OOO0OO =='未实名':#line:1075
                            weishim .append (OOO0OO0O0O00OOOOO .token )#line:1076
                        print (f'【查邀请人】:我的邀请人:{O00OO0OOOO00OO000}丨实名:{OO0OO0O0000OOO0OO}')#line:1077
                    else :#line:1078
                        if OOO0OO0O0O00OOOOO .innerId !='0':#line:1079
                            OOO0OO0O0O00OOOOO .invitation ()#line:1080
        except Exception as OOO0000OO0O00OO0O :#line:1081
            print (OOO0000OO0O00OO0O )#line:1082
    def add_clover (OOOOO00OOO0O0OOOO ):#line:1085
        global golden_seed #line:1086
        try :#line:1087
            O000OOOOO0O00O0O0 =f'__{timi_new()}'#line:1088
            OOO0OO0OO0O0O00O0 ={'source':'scsc','authorization':OOOOO00OOO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0O00O0O0 ),'signstring':O000OOOOO0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1099
            O0O0O00O0O0O0O0OO =requests .request ('get',f'{host}/assets/clovers',headers =OOO0OO0OO0O0O00O0 ).json ()#line:1100
            if 'status'in O0O0O00O0O0O0O0OO :#line:1102
                if O0O0O00O0O0O0O0OO ['status']==200 :#line:1103
                    O0000OO000O00O000 =O0O0O00O0O0O0O0OO ['data']['clover']#line:1104
                    OOOO0OOO000O000OO =O0O0O00O0O0O0O0OO ['data']['used_clover']#line:1105
                    O0O0OO0O00OO0000O =float (O0000OO000O00O000 )-float (OOOO0OOO000O000OO )#line:1106
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOO0OOO000O000OO}')#line:1107
                    if OOOOO00OOO0O0OOOO .certification ()!='未实名':#line:1108
                        if O0O0OO0O00OO0000O >1 :#line:1109
                            O000OOOOO0O00O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0OO0O00OO0000O)}_{timi_new()}'#line:1110
                            O0O0O0OOOOOO0OOOO ={'source':'scsc','authorization':OOOOO00OOO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOO0O00O0O0 ),'signstring':O000OOOOO0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1121
                            OO00OOO0O0OOO0OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0OO0O00OO0000O )}#line:1122
                            O000OO0O00OO00OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0O0OOOOOO0OOOO ,data =OO00OOO0O0OOO0OO0 ).json ()#line:1123
                            if 'status'in O000OO0O00OO00OO0 :#line:1125
                                if O000OO0O00OO00OO0 ['status']==200 :#line:1126
                                    print (f'【参与抽奖】:添加☘️:{O000OO0O00OO00OO0["data"]["isSuccess"]}丨数量:{O0O0OO0O00OO0000O}')#line:1127
                                if O000OO0O00OO00OO0 ['status']==500 :#line:1128
                                    print (f'【参与抽奖】:添加☘️:{O000OO0O00OO00OO0["message"]}')#line:1129
            O0O0O000000000O00 =requests .request ('get',f'{host}/lottery',headers =OOO0OO0OO0O0O00O0 ).json ()#line:1130
            O0O0O0O0O0OO00000 =OOOOO00OOO0O0OOOO .winning_rewards ()#line:1132
            if 'status'in O0O0O000000000O00 :#line:1133
                if O0O0O000000000O00 ['status']==200 :#line:1134
                    O0OO0O0OOOO0O0O00 =O0O0O000000000O00 ['data'][0 ]['day_get_gold_quantity']#line:1135
                    golden_seed +=float (O0OO0O0OOOO0O0O00 )#line:1136
                    OOOO000OOOOOO0OO0 =O0O0O000000000O00 ['data'][1 ]['value']#line:1137
                    O0OO00O00OOOOOO00 =O0O0O000000000O00 ['data'][0 ]['join_number']#line:1138
                    O000O00O00O00OOOO =int (float (O0O0O000000000O00 ['data'][0 ]['totalValue']))#line:1139
                    O00O0O0O0O0O000O0 =float (OOOO000OOOOOO0OO0 /O000O00O00O00OOOO )*10000 #line:1140
                    O0OO0O0O0OOOO0O00 =O000O00O00O00OOOO /O0OO00O00OOOOOO00 #line:1141
                    print (f'【参与抽奖】:预计每天中{str(O0OO0O0OOOO0O0O00)[:6]}颗金种子丨好友收益:{str(O0O0O0O0O0OO00000)[:6]}')#line:1142
                    print (f'【抽奖统计】:每1万☘️中{str(O00O0O0O0O0O000O0)[:6]}颗金种子丨☘️人均:{str(O0OO0O0O0OOOO0O00)[:7]}️')#line:1143
        except Exception as OOO0O0OO00OOO000O :#line:1144
            print (OOO0O0OO00OOO000O )#line:1145
    def energy (OO0OOOOOOOOOOO000 ):#line:1148
        try :#line:1149
            while True :#line:1150
                OOOOO000000000000 =f'__{timi_new()}'#line:1151
                O00OOOO0O0OOOO00O ={'source':'scsc','authorization':OO0OOOOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000000000000 ),'signstring':OOOOO000000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                OOO0O00O0O00OO00O =requests .request ('get',f'{host}/energy/general',headers =O00OOOO0O0OOOO00O ).json ()#line:1163
                if 'status'in OOO0O00O0O00OO00O :#line:1165
                    if OOO0O00O0O00OO00O ['status']==200 :#line:1166
                        OOOO000O0O000O000 =OOO0O00O0O00OO00O ['data']['ordinary_water']#line:1167
                        O0OOO0000OOOO0O00 =OOO0O00O0O00OO00O ['data']['ordinary_fertilizer']#line:1168
                        OOO00O0O00OO00000 =OOO0O00O0O00OO00O ['data']['videoStatus']#line:1169
                        OO0000000OO000OO0 =OOO0O00O0O00OO00O ['data']['waterVideoKey']#line:1170
                        print (f'【我的营养】:肥料:{str(O0OOO0000OOOO0O00).split(".")[0]}丨水滴:{str(OOOO000O0O000O000).split(".")[0]}')#line:1172
                        if float (O0OOO0000OOOO0O00 )<96 :#line:1173
                            if OOO00O0O00OO00000 :#line:1174
                                time .sleep (random .randint (160 ,180 )/10 )#line:1175
                                O0000OOO00O0OO00O =99 -float (O0OOO0000OOOO0O00 )#line:1176
                                O000OO0000000000O ={"fertilizer":str (O0000OOO00O0OO00O ).split ('.')[0 ]}#line:1177
                                O00O00O00OOO00OOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O00OOOO0O0OOOO00O ).json ()#line:1179
                                if 'status'in O00O00O00OOO00OOO :#line:1181
                                    if O00O00O00OOO00OOO ['status']==200 :#line:1182
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O00OOO00OOO["message"]}')#line:1183
                                    if O00O00O00OOO00OOO ['status']==500 :#line:1184
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O00OOO00OOO["message"]}')#line:1185
                                        break #line:1186
                                if float (O0OOO0000OOOO0O00 )<78 :#line:1188
                                    O0000OOO00O0OO00O =80 -float (O0OOO0000OOOO0O00 )#line:1189
                                    OOO00OOO000000O0O =f'_fertilizer={int(O0000OOO00O0OO00O)}_{timi_new()}'#line:1190
                                    OO0O0O000OO0OOO00 ={'source':'scsc','authorization':OO0OOOOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO000000O0O ),'signstring':OOO00OOO000000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    O00OOO0OO0O0OO000 ={"fertilizer":int (O0000OOO00O0OO00O )}#line:1202
                                    O0OOO0OO0OO0OOO0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O0O000OO0OOO00 ,data =O00OOO0OO0O0OO000 ).json ()#line:1204
                                    if 'status'in O0OOO0OO0OO0OOO0O :#line:1206
                                        if O0OOO0OO0OO0OOO0O ['status']==200 :#line:1207
                                            print (f'【购买肥料】:购买肥料:{O0OOO0OO0OO0OOO0O["message"]}丨数量:{int(O0000OOO00O0OO00O)}')#line:1208
                                        if O0OOO0OO0OO0OOO0O ['status']==500 :#line:1209
                                            print (f'【购买肥料】:购买肥料:{O0OOO0OO0OO0OOO0O["message"]}丨数量:{int(O0000OOO00O0OO00O)}')#line:1210
                                            OO0000000O00OO000 =O0OOO0OO0OO0OOO0O ["message"].split ('-')[1 ]#line:1211
                                            OOOOOO0O00OOOOOOO =f'__{timi_new()}'#line:1212
                                            O0OOO00OOO0O00OOO ={'source':'scsc','authorization':OO0OOOOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O00OOOOOOO ),'signstring':OOOOOO0O00OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            OOO0000OOOOO0OO0O =requests .request ('get',f'{host}/user',headers =O0OOO00OOO0O00OOO ).json ()#line:1224
                                            if 'status'in OOO0000OOOOO0OO0O :#line:1225
                                                if OOO0000OOOOO0OO0O ['status']==200 :#line:1226
                                                    O0OO000OO0000O000 =OOO0000OOOOO0OO0O ['data']['inner_id']#line:1227
                                                    if give_gold (O0OO000OO0000O000 ,float (OO0000000O00OO000 )+1 ):#line:1228
                                                        OO0OOOOOOOOOOO000 .energy ()#line:1229
                        if float (OOOO000O0O000O000 )<880 :#line:1230
                            if OO0000000OO000OO0 :#line:1231
                                time .sleep (random .randint (160 ,180 )/10 )#line:1232
                                O0OO0OO0O0O00O000 =999 -float (OOOO000O0O000O000 )#line:1233
                                O00OO00000O00O00O ={"water":str (O0OO0OO0O0O00O000 ).split ('.')[0 ]}#line:1234
                                OO0O0O0O000OOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O00OOOO0O0OOOO00O ).json ()#line:1236
                                if 'status'in OO0O0O0O000OOOOO0 :#line:1238
                                    if OO0O0O0O000OOOOO0 ['status']==200 :#line:1239
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0O0O000OOOOO0["message"]}')#line:1240
                                    if OO0O0O0O000OOOOO0 ['status']==500 :#line:1241
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0O0O000OOOOO0["message"]}')#line:1242
                                        break #line:1243
                                if float (OOOO000O0O000O000 )<780 :#line:1244
                                    O0OO0OO0O0O00O000 =800 -float (OOOO000O0O000O000 )#line:1245
                                    O00OO0OOOOOOOOOO0 =f'_water={int(O0OO0OO0O0O00O000)}_{timi_new()}'#line:1246
                                    OO000O00OO0OOO00O ={'source':'scsc','authorization':OO0OOOOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOOOOOOOO0 ),'signstring':O00OO0OOOOOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1257
                                    O00OOOOO0O0OOOO00 ={"water":int (O0OO0OO0O0O00O000 )}#line:1258
                                    O00000O0OO00000OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO000O00OO0OOO00O ,data =O00OOOOO0O0OOOO00 ).json ()#line:1260
                                    if 'status'in O00000O0OO00000OO :#line:1262
                                        if O00000O0OO00000OO ['status']==200 :#line:1263
                                            print (f'【购买水滴】:购买水滴:{O00000O0OO00000OO["message"]}丨数量:{int(O0OO0OO0O0O00O000)}')#line:1264
                                        if O00000O0OO00000OO ['status']==500 :#line:1265
                                            print (f'【购买水滴】:购买水滴:{O00000O0OO00000OO["message"]}丨数量:{int(O0OO0OO0O0O00O000)}')#line:1266
                                            OO0000000O00OO000 =O00000O0OO00000OO ["message"].split ('-')[1 ]#line:1267
                                            OOOOOO0O00OOOOOOO =f'__{timi_new()}'#line:1268
                                            O0OOO00OOO0O00OOO ={'source':'scsc','authorization':OO0OOOOOOOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O00OOOOOOO ),'signstring':OOOOOO0O00OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1279
                                            OOO0000OOOOO0OO0O =requests .request ('get',f'{host}/user',headers =O0OOO00OOO0O00OOO ).json ()#line:1280
                                            if 'status'in OOO0000OOOOO0OO0O :#line:1281
                                                if OOO0000OOOOO0OO0O ['status']==200 :#line:1282
                                                    O0OO000OO0000O000 =OOO0000OOOOO0OO0O ['data']['inner_id']#line:1283
                                                    if give_gold (O0OO000OO0000O000 ,float (OO0000000O00OO000 )+1 ):#line:1284
                                                        OO0OOOOOOOOOOO000 .energy ()#line:1285
                        break #line:1286
        except Exception as O0OO0O000OOOOO0OO :#line:1287
            print (O0OO0O000OOOOO0OO )#line:1288
def bundled_def ():#line:1291
    OOO0OO0OOOO0OOOO0 =['5570536','7750212','7911652','7911680','7805624']#line:1292
    return OOO0OO0OOOO0OOOO0 [random .randint (0 ,len (OOO0OO0OOOO0OOOO0 )-1 )]#line:1293
def version_of_the_validation ():#line:1297
    return str ((98 -56 )/10 )#line:1298
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
        O0OO00OOO00000000 =gitee_edition ()#line:1332
        if version_of_the_validation ()<O0OO00OOO00000000 ['CityEarth']['edition']:#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO00000000["CityEarth"]["edition"]}   ❌')#line:1334
            print (f'更新内容=>>{O0OO00OOO00000000["CityEarth"]["content"]}')#line:1335
        else :#line:1336
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00OOO00000000["CityEarth"]["edition"]}   ✅')#line:1337
            print (f'更新内容=>> {O0OO00OOO00000000["CityEarth"]["content"]}')#line:1338
    except Exception as O00O0O00O00O00000 :#line:1339
        print (O00O0O00O00O00000 )#line:1340
def sc3 ():#line:1343
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1344
if __name__ =='__main__':#line:1347
    start ()#line:1348
