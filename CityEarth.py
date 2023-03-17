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
@ 版本  4.4
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
        OOOO00O0OOOO0OO00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OOOO00O0OOOO0OO00)}个账号==========")#line:17
        for O0O000O0OO000O000 in OOOO00O0OOOO0OO00 :#line:18
            OO0O000000O00OOO0 =[]#line:19
            print (f"------------正在执行第{OOOO00O0OOOO0OO00.index(O0O000O0OO000O000) + 1}个账号------------")#line:20
            OOOOOO00OOOO0OOOO =CityEarth (O0O000O0OO000O000 ,OO0O000000O00OOO0 ,OOOO00O0OOOO0OO00 .index (O0O000O0OO000O000 ))#line:21
            def OO000OO0OOO00OOOO ():#line:23
                if OOOOOO00OOOO0OOOO .base_info ():#line:25
                    OOOOOO00OOOO0OOOO .sealing ()#line:27
                    OOOOOO00OOOO0OOOO .invitenum ()#line:29
                    OOOOOO00OOOO0OOOO .query_to_sell ()#line:31
                    OOOOOO00OOOO0OOOO .game_map ()#line:33
                    OOOOOO00OOOO0OOOO .friends_invitation ()#line:37
                    OOOOOO00OOOO0OOOO .energy ()#line:39
                    OOOOOO00OOOO0OOOO .add_clover ()#line:41
                    OOOOOO00OOOO0OOOO .propsraffle ()#line:43
                    OOOOOO00OOOO0OOOO .synthetic ()#line:45
                    OOOOOO00OOOO0OOOO .crops_illustrated ()#line:47
                    OOOOOO00OOOO0OOOO .withdraw ()#line:49
                    if float (datetime .datetime .now ().hour )>8 :#line:50
                        OOOOOO00OOOO0OOOO .give_gold ()#line:52
            OO0000O000O0OOO00 =threading .Thread (target =OO000OO0OOO00OOOO )#line:54
            OO0000O000O0OOO00 .start ()#line:55
            time .sleep (time_xx )#line:56
        print (f"------------正在处理数据------------")#line:57
        time .sleep (0.5 )#line:58
        O0O00O0O00O000000 =format_msg ()#line:59
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O00O0O00O000000 +' ')#line:60
        time .sleep (15 )#line:61
        print (f'所有未出售的芦荟:{count_list}颗')#line:62
        print ('开始打印好友数量不足2的ID')#line:63
        for O000O000O0OOO0O00 in invited_new :#line:64
            print (O000O000O0OOO0O00 )#line:65
        print ('开始打印未实名的token')#line:66
        for O0O00OO00000OOO0O in weishim :#line:67
            print (O0O00OO00000OOO0O )#line:68
    except Exception as OOO00O0O0OOOOO0O0 :#line:69
        print (OOO00O0O0OOOOO0O0 )#line:70
def give_gold (OO0O000O0OO00000O ,O0O000OOO0OOOO0O0 ):#line:74
    try :#line:75
        O0O000000O000O0OO =f'_doneeNo={OO0O000O0OO00000O}&quantity={int(O0O000OOO0OOOO0O0)}_{timi_new()}'#line:76
        OO0OO00O0000OOO00 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O000000O000O0OO ),'signstring':O0O000000O000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:87
        O0000O0O0OO0000OO ={"quantity":int (O0O000OOO0OOOO0O0 ),"doneeNo":OO0O000O0OO00000O }#line:91
        OOO0O00000OO00O0O =requests .request ('post',f'{host}/finance/give-gold',headers =OO0OO00O0000OOO00 ,data =O0000O0O0OO0000OO ).json ()#line:92
        if 'status'in OOO0O00000OO00O0O :#line:94
            if OOO0O00000OO00O0O ['status']==200 :#line:95
                if OOO0O00000OO00O0O ['data']:#line:96
                    print (f'【赠送种子】:赠送{int(O0O000OOO0OOOO0O0)}种子给{OO0O000O0OO00000O}成功')#line:97
                    return True #line:98
            if OOO0O00000OO00O0O ['status']==401 :#line:99
                print (f'【赠送种子】:{OOO0O00000OO00O0O["message"]}')#line:100
                return False #line:101
            if OOO0O00000OO00O0O ['status']==500 :#line:102
                print (f'【赠送种子】:{OOO0O00000OO00O0O["message"]}')#line:103
                return False #line:104
        return False #line:105
    except Exception as OOO0000000O0O0OO0 :#line:106
        print (OOO0000000O0O0OO0 )#line:107
def kvkv ():#line:110
    return '/vastzzzl/vastzzzl/raw/master'#line:111
def oyoy ():#line:113
    return '卡密未激活   ❌'#line:114
def sign (OO0OOOOOO0O0OOOOO ):#line:117
    O0OOO0O0000O00O0O =hashlib .md5 (OO0OOOOOO0O0OOOOO .encode ()).hexdigest ()#line:118
    OO000O0000000O00O =sc1 ()#line:119
    O000000O0OOOO00OO =sc2 ()#line:120
    OO0O0O0OO000O00OO =sc3 ()#line:121
    OO0000O000OO00O00 =OO000O0000000O00O +O0OOO0O0000O00O0O +O000000O0OOOO00OO +OO0O0O0OO000O00OO #line:122
    OOOO0O000O0O0O0O0 =hashlib .md5 (OO0000O000OO00O00 .encode ()).hexdigest ()#line:123
    return OOOO0O000O0O0O0O0 #line:124
def format_msg ():#line:127
    OO0OOO00000OO0O0O =""#line:128
    for O0O0000O000O00000 in msg_list :#line:129
        OO0OOO00000OO0O0O +=str (O0O0000O000O00000 )+"\r\n"#line:130
    return OO0OOO00000OO0O0O #line:131
def sc1 ():#line:134
    return "scsc%^&*"#line:135
def O000OO0O00OO00O00 ():#line:138
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:139
        ubbbf ()#line:140
    else :#line:141
        oyoy ()#line:142
        exit (1 )#line:143
def timi_new ():#line:146
    return str (int (time .time ()*1000 ))#line:147
json_path ="CityEarth_data.json"#line:150
json_path1 ="CityEarth_data.json"#line:151
dict ={}#line:152
def get_json_data (OOO0OO00OOO00O000 ,OO00O0O000O00O00O ,OO0000O0000OO0O00 ,O00O00O0OO0OO0OO0 ):#line:155
    with open (OOO0OO00OOO00O000 ,'rb')as OO00000OO00O000OO :#line:156
        OO00OOO000OOOOOO0 =json .load (OO00000OO00O000OO )#line:157
        OO00OOO000OOOOOO0 ['data'][OO00O0O000O00O00O ][OO0000O0000OO0O00 ]=O00O00O0OO0OO0OO0 #line:158
        OOOOOO00OO00O0O0O =OO00OOO000OOOOOO0 #line:159
    OO00000OO00O000OO .close ()#line:160
    return OOOOOO00OO00O0O0O #line:161
def write_json_data (O0O00O0000000O00O ):#line:164
    with open (json_path1 ,'w')as O0O000000000OO000 :#line:165
        json .dump (O0O00O0000000O00O ,O0O000000000OO000 )#line:166
    O0O000000000OO000 .close ()#line:167
    return True #line:168
class CityEarth :#line:171
    def __init__ (O00OOOO00O0O0OO0O ,OOO00O00O0O0OOO00 ,O000O0OOOOOO0O0OO ,O00OOO0O000O0OO00 ):#line:173
        try :#line:174
            O00OOOO00O0O0OO0O .msg =O000O0OOOOOO0O0OO #line:175
            O00OOOO00O0O0OO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:176
            O00OOOO00O0O0OO0O .token =OOO00O00O0O0OOO00 ['authorization']#line:177
            O00OOOO00O0O0OO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:178
            O00OOOO00O0O0OO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:179
            O00OOOO00O0O0OO0O .elephant_user =OOO00O00O0O0OOO00 ['elephant_user']#line:180
            O00OOOO00O0O0OO0O .elephant_pswd =OOO00O00O0O0OOO00 ['elephant_pswd']#line:181
            O00OOOO00O0O0OO0O .elephant_Task_ID =OOO00O00O0O0OOO00 ['elephant_Task_ID']#line:182
            O00OOOO00O0O0OO0O .len_new =O00OOO0O000O0OO00 #line:183
        except :#line:184
            print ('变量格式错误')#line:185
    def base_info (OOO0OOOOO000OOO0O ):#line:188
        try :#line:189
            OOO0OOOOO000OOO0O .watched_ad ()#line:191
            OO0O0O0OOO0O0OOO0 =f'__{timi_new()}'#line:192
            OOOOO0O00000000OO ={'source':'scsc','authorization':OOO0OOOOO000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO0O0OOO0 ),'signstring':OO0O0O0OOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:203
            O000O0O00OOOOO00O =requests .request ('get',f'{host}/user',headers =OOOOO0O00000000OO ).json ()#line:204
            if 'status'in O000O0O00OOOOO00O :#line:206
                if O000O0O00OOOOO00O ['status']==200 :#line:207
                    O0000OO00OO00OOOO =O000O0O00OOOOO00O ['data']['nickname']#line:208
                    OO0O0O0OOOO0OO00O =O000O0O00OOOOO00O ['data']['inner_id']#line:209
                    OO000O0OO00O0O0O0 =O000O0O00OOOOO00O ['data']['assets']['gold']#line:210
                    O0O00OOO0OOOOOOOO =O000O0O00OOOOO00O ['data']['level']#line:211
                    print (f'【账号信息】:昵称:{O0000OO00OO00OOOO[:5]}丨ID:{OO0O0O0OOOO0OO00O}丨等级:{O0O00OOO0OOOOOOOO}丨金种子:{str(OO000O0OO00O0O0O0).split(".")[0]}')#line:213
                    if 'wx_'in O0000OO00OO00OOOO :#line:214
                        OOO0OOOOO000OOO0O .change_nickname ()#line:215
                if O000O0O00OOOOO00O ['status']==401 :#line:216
                    print ('【账号信息】:账号失效正在尝试登录')#line:217
                    if OOO0OOOOO000OOO0O .elephant_user =='f':#line:218
                        return False #line:219
                    O000O00OOO000O0OO =Invalid_login .addtask (elephant_user =OOO0OOOOO000OOO0O .elephant_user ,elephant_pswd =OOO0OOOOO000OOO0O .elephant_pswd ,elephant_Task_ID =OOO0OOOOO000OOO0O .elephant_Task_ID )#line:222
                    O0OO0O0O0OOOO0O0O =get_json_data (json_path ,OOO0OOOOO000OOO0O .len_new ,'authorization',O000O00OOO000O0OO )#line:223
                    if write_json_data (O0OO0O0O0OOOO0O0O ):#line:224
                        print ('正在写入账号配置文件')#line:225
                    return False #line:226
                if O000O0O00OOOOO00O ['status']==500 :#line:227
                    return False #line:228
            return True #line:229
        except Exception as O000OOOOOO0OO00O0 :#line:230
            print (O000OOOOOO0OO00O0 )#line:231
    def sealing (O0O00O0O0O0O00OOO ):#line:234
        try :#line:235
            O0OOO0000OOO000OO =f'__{timi_new()}'#line:236
            OO00O0OO0OO000OO0 ={'source':'scsc','authorization':O0O00O0O0O0O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOO000OO ),'signstring':O0OOO0000OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:247
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O0OO0OO000OO0 )#line:248
            requests .request ('get',f'{host}/packsack/list',headers =OO00O0OO0OO000OO0 )#line:249
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O0OO0OO000OO0 )#line:250
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O0OO0OO000OO0 )#line:251
            requests .request ('get',f'{host}/user',headers =OO00O0OO0OO000OO0 )#line:252
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O0OO0OO000OO0 )#line:253
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O0OO0OO000OO0 )#line:254
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O0OO0OO000OO0 )#line:255
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO0OO000OO0 )#line:256
            requests .request ('get',f'{host}/assets',headers =OO00O0OO0OO000OO0 )#line:257
        except Exception as O0O0O0O0O00O0O000 :#line:258
            print (O0O0O0O0O00O0O000 )#line:259
    def ddd (O0O00OOOO0OO000O0 ):#line:261
        try :#line:262
            O0O000OOO0O0O0OOO =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:263
            OOO00OOOO00000000 ={'source':'scsc','authorization':O0O00OOOO0OO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOO0O0O0OOO ),'signstring':O0O000OOO0O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            O0O0OOO0OO0O0OO0O =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =OOO00OOOO00000000 ).json ()#line:275
            print (O0O0OOO0OO0O0OO0O )#line:276
        except Exception as OO0OOOO00O00OO0OO :#line:279
            print (OO0OOOO00O00OO0OO )#line:280
    def the_query (O0O000OO0O00O00OO ):#line:285
        try :#line:286
            O0O0O00OO0O00O0OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:287
            O0O00O0OOO0O00O00 ={'authorization':O0O000OO0O00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OO0O00O0OO ),'signstring':O0O0O00OO0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:297
            OO00OOOOOOO00O0OO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0O00O0OOO0O00O00 ).json ()#line:299
            if 'status'in OO00OOOOOOO00O0OO :#line:301
                if OO00OOOOOOO00O0OO ['status']==200 :#line:302
                    O0O0000000O00000O =OO00OOOOOOO00O0OO ['data']['rows'][4 ]['price']#line:303
                    O0O000OO0O00O00OO .market_sale (O0O0000000O00000O )#line:304
        except Exception as O0OOO0OOOOOOO0000 :#line:305
            print (O0OOO0OOOOOOO0000 )#line:306
    def market_sale (O0O0O0OOOOOO0O000 ,OOOO00000OO00OO00 ):#line:309
        try :#line:310
            O000OO00O00OOOO00 =timi_new ()#line:311
            O0O0O00OOO0OO00OO =f'type=crop__{O000OO00O00OOOO00}'#line:312
            OOOO0OO0O000O0O00 ={'source':'scsc','authorization':O0O0O0OOOOOO0O000 .token ,'timestamp':str (O000OO00O00OOOO00 ),'sign':sign (O0O0O00OOO0OO00OO ),'signstring':O0O0O00OOO0OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OOOO000O0000O0OOO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOO0OO0O000O0O00 ).json ()#line:325
            if 'status'in OOOO000O0000O0OOO :#line:327
                if OOOO000O0000O0OOO ['status']==200 :#line:328
                    if OOOO000O0000O0OOO ['data']['rows']:#line:329
                        O00OO000O0O00O0OO =OOOO000O0000O0OOO ['data']['rows'][0 ]['packsackItemId']#line:330
                        OO00O0OOOO0O00O00 =OOOO000O0000O0OOO ['data']['rows'][0 ]['quantity']#line:331
                        O00O00OO00OO0O000 =float (OOOO00000OO00OO00 )-0.001 #line:332
                        if O00O00OO00OO0O000 >9 :#line:333
                            O000OOOOO00OO0O0O =f'_packsackItemId={O00OO000O0O00O0OO}&price={str(OOOO00000OO00OO00)[:5]}&quantity={OO00O0OOOO0O00O00}_{O000OO00O00OOOO00}'#line:334
                            OOOO0OO0OO000OOOO ={'source':'scsc','authorization':O0O0O0OOOOOO0O000 .token ,'timestamp':str (O000OO00O00OOOO00 ),'sign':sign (O000OOOOO00OO0O0O ),'signstring':O000OOOOO00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:345
                            O0000OO0OO000O0O0 ={"packsackItemId":O00OO000O0O00O0OO ,"price":str (OOOO00000OO00OO00 )[:5 ],"quantity":str (OO00O0OOOO0O00O00 )}#line:350
                            O0O00000O0O00O0OO =requests .request ('post',f'{host}/market/sale',headers =OOOO0OO0OO000OOOO ,data =O0000OO0OO000O0O0 ).json ()#line:351
                            if 'status'in O0O00000O0O00O0OO :#line:353
                                if O0O00000O0O00O0OO ['status']==200 :#line:354
                                    print (f'【上架芦荟】:数量:{OO00O0OOOO0O00O00}丨价格:{str(OOOO00000OO00OO00)[:5]}')#line:355
        except Exception as O0OO0O0O0O000O000 :#line:356
            print (O0OO0O0O0O000O000 )#line:357
    def query_to_sell (OOO00O0OO0OO00OOO ):#line:360
        try :#line:361
            OO0000000O0O0OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:362
            OO0O0O0O00O0000OO ={'source':'scsc','authorization':OOO00O0OO0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000O0O0OO00 ),'signstring':OO0000000O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:373
            O0OOOOO00OO0000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0O0O0O00O0000OO ).json ()#line:375
            if 'status'in O0OOOOO00OO0000O0 :#line:377
                if O0OOOOO00OO0000O0 ['status']==200 :#line:378
                    for O0000OO0OO0O0O0O0 in O0OOOOO00OO0000O0 ['data']['rows']:#line:379
                        OOOOO0OOOO00000O0 =O0000OO0OO0O0O0O0 ['materialKey']#line:380
                        OO00OO00O00O00000 =O0000OO0OO0O0O0O0 ['quantity']#line:381
                        O00OO000000OOOOOO =O0000OO0OO0O0O0O0 ['price']#line:382
                        O0O00000OO0OO0OOO =O0000OO0OO0O0O0O0 ['saleState']#line:383
                        if O0O00000OO0OO0OOO ==0 :#line:384
                            print (f'【出售订单】:名称:{OOOOO0OOOO00000O0}丨数量:{OO00OO00O00O00000}丨价格:{O00OO000000OOOOOO}')#line:385
                            OOOO0OOOO00OO00OO =O0000OO0OO0O0O0O0 ['id']#line:386
                            if float (datetime .datetime .now ().hour )>8 :#line:387
                                OOO00O0OO0OO00OOO .cacel_sale (OOOO0OOOO00OO00OO )#line:388
        except Exception as OO0OOOO0O000O00O0 :#line:389
            print (OO0OOOO0O000O00O0 )#line:390
    def cacel_sale (OOO00OOOOOOOOOOOO ,O0OOOO000O0OOOOO0 ):#line:393
        try :#line:394
            O00O00O0O000OOOOO =f'_saleId={O0OOOO000O0OOOOO0}_{timi_new()}'#line:395
            O00O00OOO0O0OO00O ={'source':'scsc','authorization':OOO00OOOOOOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O000OOOOO ),'signstring':O00O00O0O000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:406
            O0O00OO00OO000OO0 ={"saleId":O0OOOO000O0OOOOO0 }#line:409
            OO0O00O00O00OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00O00OOO0O0OO00O ,data =O0O00OO00OO000OO0 ).json ()#line:410
            if 'status'in OO0O00O00O00OOOOO :#line:412
                if OO0O00O00O00OOOOO ['status']==200 :#line:413
                    print (f'【下架出售】:{OO0O00O00O00OOOOO["data"]}')#line:414
        except Exception as O0000OOOOOO00O0O0 :#line:415
            print (O0000OOOOOO00O0O0 )#line:416
    def change_nickname (O00O000O000OOO000 ):#line:419
        try :#line:420
            OO0O0OO0O0OO0OOO0 =timi_new ()#line:421
            O00O0OO0000OOO000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            OO0O0000O0O0O0OOO =requests .request ('post','https://www.qmsjmfb.com/',data =O00O0OO0000OOO000 ).text #line:423
            OO00OOOO000O00O0O =re .findall ('<ul><li>(.*?)</li>',OO0O0000O0O0O0OOO )[0 ][:3 ]#line:424
            OOOO00OO0000O00O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO00OOOO000O00O0O}').json ()#line:425
            OO0O0O0OO00O0O0OO =OOOO00OO0000O00O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:426
            O0000O00OO0OO0000 ={"nickname":OO0O0O0OO00O0O0OO }#line:427
            O000O000OOOO00OOO =f'_nickname={OO0O0O0OO00O0O0OO}_{OO0O0OO0O0OO0OOO0}'#line:428
            O00O0OOOO0000O0O0 ={'source':'scsc','authorization':O00O000O000OOO000 .token ,'timestamp':OO0O0OO0O0OO0OOO0 ,'sign':sign (O000O000OOOO00OOO ),'signstring':O000O000OOOO00OOO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO00O0000OO000OOO =requests .request ('patch',f'{host}/user/nickname',headers =O00O0OOOO0000O0O0 ,data =O0000O00OO0OO0000 ).json ()#line:440
            if 'status'in OO00O0000OO000OOO :#line:442
                if OO00O0000OO000OOO ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{OO0O0O0OO00O0O0OO}丨{OO00O0000OO000OOO["message"]}')#line:444
        except Exception as O0000OO00000OOOOO :#line:445
            print (O0000OO00000OOOOO )#line:446
    def withdraw (O0OOO00000000000O ):#line:449
        try :#line:450
            O0O0OOOO0O0OOO000 =f'__{timi_new()}'#line:451
            OOO000OO00O000OO0 ={'source':'scsc','authorization':O0OOO00000000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0O0OOO000 ),'signstring':O0O0OOOO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOOOO0OOOOO0OO000 =requests .request ('get',f'{host}/assets',headers =OOO000OO00O000OO0 ).json ()#line:463
            if 'status'in OOOOO0OOOOO0OO000 :#line:465
                if OOOOO0OOOOO0OO000 ['status']==200 :#line:466
                    O0O0O0O0OO00O00OO =OOOOO0OOOOO0OO000 ['data']['cash']#line:467
                    if float (O0O0O0O0OO00O00OO )>20 :#line:468
                        O0O0OOOO0O0OOO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        OOO000OO00O000OO0 ={'authorization':O0OOO00000000000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0O0OOO000 ),'signstring':O0O0OOOO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O0O00OOOO000OO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        O0O0O0O00OO00OOO0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO000OO00O000OO0 ,data =O0O00OOOO000OO00O ).json ()#line:482
                        if 'status'in O0O0O0O00OO00OOO0 :#line:484
                            if O0O0O0O00OO00OOO0 ['status']==200 :#line:485
                                print (f'【余额提现】:{O0O0O0O00OO00OOO0["data"]}')#line:486
                        if 'status'in O0O0O0O00OO00OOO0 :#line:487
                            if O0O0O0O00OO00OOO0 ['status']==500 :#line:488
                                print (f'【余额提现】:{O0O0O0O00OO00OOO0["message"]}')#line:489
        except Exception as O0OOOOOOO00OO00OO :#line:490
            print (O0OOOOOOO00OO00OO )#line:491
    def invitenum (O00000OOO00O0O000 ):#line:494
        global invited_new #line:495
        try :#line:496
            O0O0OO0O0OOOO00OO =f'__{timi_new()}'#line:497
            O0OO000O0OOO000O0 ={'source':'scsc','authorization':O00000OOO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOOO00OO ),'signstring':O0O0OO0O0OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            OO0000OOO000OOOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO000O0OOO000O0 ).json ()#line:509
            if 'status'in OO0000OOO000OOOOO :#line:511
                if OO0000OOO000OOOOO ['status']==200 :#line:512
                    OOOO0000O00O00000 =OO0000OOO000OOOOO ['data']['invited_count']#line:513
                    OO0OOOO0OO0O00OO0 =OO0000OOO000OOOOO ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{OOOO0000O00O00000}丨间邀好友:{OO0OOOO0OO0O00OO0}')#line:515
                    if OOOO0000O00O00000 <2 :#line:516
                        OOOO00O0O0000O00O =f'__{timi_new()}'#line:517
                        O0000OO000O00OO00 ={'source':'scsc','authorization':O00000OOO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O0000O00O ),'signstring':OOOO00O0O0000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        O0OOO0O000O0O0OO0 =requests .request ('get',f'{host}/user',headers =O0000OO000O00OO00 ).json ()#line:529
                        if 'status'in O0OOO0O000O0O0OO0 :#line:531
                            if O0OOO0O000O0O0OO0 ['status']==200 :#line:532
                                invited_new .append (O0OOO0O000O0O0OO0 ['data']['inner_id'])#line:533
        except Exception as O0O000O0O0OOO0OOO :#line:534
            print (O0O000O0O0OOO0OOO )#line:535
    def game_map (OOO000OOOOOO00OOO ):#line:538
        global count_list #line:539
        try :#line:540
            OO0000O00OOO00O00 =f'__{timi_new()}'#line:541
            OOOOOO0OO0O0O0OOO ={'source':'scsc','authorization':OOO000OOOOOO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00OOO00O00 ),'signstring':OO0000O00OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            OO0O000O00O0O0OOO =requests .request ('get',f'{host}/game/map',headers =OOOOOO0OO0O0O0OOO ).json ()#line:553
            if 'status'in OO0O000O00O0O0OOO :#line:555
                if OO0O000O00O0O0OOO ['status']==200 :#line:556
                    for OO000OOO00000O0OO in OO0O000O00O0O0OOO ['data']['list'][0 ]['crops']:#line:557
                        OOO00OO0OOO000O00 =OO000OOO00000O0OO ['level']#line:559
                        if OOO00OO0OOO000O00 ==41 :#line:560
                            OO0OO00OOO00OOO0O =OO000OOO00000O0OO ['crop_name']#line:561
                            O00O0O0OOOOOO0O00 =OO000OOO00000O0OO ['count']#line:562
                            if O00O0O0OOOOOO0O00 >0 :#line:563
                                count_list +=O00O0O0OOOOOO0O00 #line:564
                                print (f'【农业资产】:{OO0OO00OOO00OOO0O}丨数量:{O00O0O0OOOOOO0O00}')#line:565
                                if float (datetime .datetime .now ().hour )>8 :#line:566
                                    OOO000OOOOOO00OOO .the_query ()#line:567
        except Exception as OOO0O00O0O0O0O0OO :#line:568
            print (OOO0O00O0O0O0O0OO )#line:569
    def give_gold (O0O0OO00OO0O00OO0 ):#line:572
        try :#line:573
            O0O0O000O0OO0O0OO =f'__{timi_new()}'#line:574
            OO0O0OOO0O0O00O00 ={'source':'scsc','authorization':O0O0OO00OO0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O0OO0O0OO ),'signstring':O0O0O000O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:585
            OO00000OO0O000O0O =requests .request ('get',f'{host}/user',headers =OO0O0OOO0O0O00O00 ).json ()#line:586
            if 'status'in OO00000OO0O000O0O :#line:587
                if OO00000OO0O000O0O ['status']==200 :#line:588
                    if float (O0O0OO00OO0O00OO0 .doneeNo )!=0 :#line:589
                        OO0OO0OOO0OOO0O0O =OO00000OO0O000O0O ['data']['assets']['gold']#line:590
                        if float (OO0OO0OOO0OOO0O0O )>float (O0O0OO00OO0O00OO0 .innerId ):#line:591
                            O00OO0000OOOOOO00 =int (float (OO0OO0OOO0OOO0O0O )/1.1 )#line:592
                            O0O0O000O0OO0O0OO =f'_doneeNo={O0O0OO00OO0O00OO0.doneeNo}&quantity={O00OO0000OOOOOO00}_{timi_new()}'#line:593
                            OO0O0OOO0O0O00O00 ={'source':'scsc','authorization':O0O0OO00OO0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O0OO0O0OO ),'signstring':O0O0O000O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:604
                            O000O00OO000O0OOO ={"quantity":O00OO0000OOOOOO00 ,"doneeNo":O0O0OO00OO0O00OO0 .doneeNo }#line:608
                            O0OO0OO00OOO0000O =requests .request ('post',f'{host}/finance/give-gold',headers =OO0O0OOO0O0O00O00 ,data =O000O00OO000O0OOO ).json ()#line:609
                            if 'status'in O0OO0OO00OOO0000O :#line:611
                                if O0OO0OO00OOO0000O ['status']==200 :#line:612
                                    if O0OO0OO00OOO0000O ['data']:#line:613
                                        print (f'【赠送种子】:赠送{O00OO0000OOOOOO00}种子给{O0O0OO00OO0O00OO0.doneeNo}成功')#line:614
                    else :#line:615
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:616
        except Exception as OO0000000OOOOO0O0 :#line:617
            print (OO0000000OOOOO0O0 )#line:618
    def invitation (OOOO0O0O0OO0O0OOO ):#line:620
        try :#line:621
            _OO00O000OOOOOO0OO =float (bundled_def ())/4 #line:622
            O0OOOOOOO0O0O00OO =f'_innerId={int(_OO00O000OOOOOO0OO)}_{timi_new()}'#line:623
            O0O0OO0000OO0000O ={'source':'scsc','authorization':OOOO0O0O0OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0O0O00OO ),'signstring':O0OOOOOOO0O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OOOO00O0000O0OO00 ={"innerId":int (_OO00O000OOOOOO0OO )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OO0000OO0000O ,data =OOOO00O0000O0OO00 )#line:636
        except Exception as OOO00O0O0000O000O :#line:637
            print (OOO00O0O0000O000O )#line:638
    def winning_rewards (O000OO000O0O00O0O ):#line:641
        try :#line:642
            OO0OO000OO00OO0OO =f'__{timi_new()}'#line:643
            O0O0OOOOO00OO0000 ={'source':'scsc','authorization':O000OO000O0O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO00OO0OO ),'signstring':OO0OO000OO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            OOO0OOOOOOO00O0O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0OOOOO00OO0000 ).json ()#line:655
            if 'status'in OOO0OOOOOOO00O0O0 :#line:657
                if OOO0OOOOOOO00O0O0 ['status']==200 :#line:658
                    if OOO0OOOOOOO00O0O0 ['data']['amount']:#line:659
                        O0O00OO00O0O00OO0 =OOO0OOOOOOO00O0O0 ['data']['amount']['gold']#line:660
                        return O0O00OO00O0O00OO0 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as OOOOOOO0000000O0O :#line:664
            print (OOOOOOO0000000O0O )#line:665
    def certification (OO00O00OOOO000000 ):#line:668
        try :#line:669
            O0O0OO000OO0O000O =f'__{timi_new()}'#line:670
            O00OO0O0O0OOOO0OO ={'source':'scsc','authorization':OO00O00OOOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO000OO0O000O ),'signstring':O0O0OO000OO0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            O0O0OOOO0OO000000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O0O0OOOO0OO ).json ()#line:682
            if 'status'in O0O0OOOO0OO000000 :#line:684
                if O0O0OOOO0OO000000 ['status']==200 :#line:685
                    if O0O0OOOO0OO000000 ['data']['result']:#line:686
                        O0O0OO00O00O0OO0O =O0O0OOOO0OO000000 ['data']['nick_name']#line:687
                        return O0O0OO00O00O0OO0O #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as O0OOOOOOO0OO00O00 :#line:691
            print (O0OOOOOOO0OO00O00 )#line:692
    def crops_illustrated (OO00O00OOO0O0000O ):#line:695
        try :#line:696
            OOOO0OOO0OO0OOO00 =f'__{timi_new()}'#line:697
            O0O00OO0OOO0O0OOO ={'source':'scsc','authorization':OO00O00OOO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0OO0OOO00 ),'signstring':OOOO0OOO0OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            O0OOO0OO00O0OOOOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00OO0OOO0O0OOO ).json ()#line:709
            if 'status'in O0OOO0OO00O0OOOOO :#line:711
                if O0OOO0OO00O0OOOOO ['status']==200 :#line:712
                    O00OO00O00OO00000 =O0OOO0OO00O0OOOOO ['data'][0 ]['crops']#line:713
                    for OOOOO0O0000000000 in O00OO00O00OO00000 :#line:714
                        if OOOOO0O0000000000 ['ill_clover_award']:#line:715
                            if float (OOOOO0O0000000000 ['ill_clover_award'])>1 :#line:716
                                if OOOOO0O0000000000 ['is_finish']:#line:717
                                    if not OOOOO0O0000000000 ['is_getit']:#line:718
                                        if OO00O00OOO0O0000O .certification ()!='未实名':#line:719
                                            OOOO0OOO0OO0OOO00 =f'_award_level={OOOOO0O0000000000["level"]}_{timi_new()}'#line:720
                                            O0O00OO0OOO0O0OOO ={'source':'scsc','authorization':OO00O00OOO0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0OO0OOO00 ),'signstring':OOOO0OOO0OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            O0O0O00O0OOOO0OO0 ={"award_level":OOOOO0O0000000000 ['level']}#line:732
                                            O00O0000OO00OOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00OO0OOO0O0OOO ,json =O0O0O00O0OOOO0OO0 ).json ()#line:734
                                            if 'status'in O00O0000OO00OOOO0 :#line:735
                                                if O00O0000OO00OOOO0 ['status']==200 :#line:736
                                                    O0OOOO0O00O00O000 =O00O0000OO00OOOO0 ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{OOOOO0O0000000000["crop_name"]}成就丨奖励{O0OOOO0O00O00O000}☘️')#line:739
                                                if O00O0000OO00OOOO0 ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{O00O0000OO00OOOO0["message"]}')#line:741
        except Exception as O00O0000000OOOOOO :#line:742
            print (O00O0000000OOOOOO )#line:743
    def watched_ad (O00OO0O0OO0O0OOOO ):#line:746
        try :#line:747
            OOOO00OO000OOOO0O =f'__{timi_new()}'#line:748
            O00OO0O00O0OOO0OO ={'source':'scsc','authorization':O00OO0O0OO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO000OOOO0O ),'signstring':OOOO00OO000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            OO0OO00O0O0OO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O00OO0O00O0OOO0OO ).json ()#line:760
            if 'status'in OO0OO00O0O0OO0O0O :#line:762
                if OO0OO00O0O0OO0O0O ['status']==200 :#line:763
                    if 'offlineInfo'in OO0OO00O0O0OO0O0O ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        OO0O000OOOOO0O0O0 =OO0OO00O0O0OO0O0O ['data']['offlineInfo']['off_minute']#line:766
                        OOOO00OO00O00OOO0 =float (OO0OO00O0O0OO0O0O ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00OO0O00O0OOO0OO ).json ()#line:769
                        time .sleep (2 )#line:770
                        OO0OO00OOOOO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O00OO0O00O0OOO0OO ).json ()#line:771
                        if 'status'in OO0OO00OOOOO0OO00 :#line:773
                            if OO0OO00OOOOO0OO00 ['status']==200 :#line:774
                                OO0OOO0O0O00OOO0O =float (OO0OO00OOOOO0OO00 ['data']['silver'])/1000000000000 #line:775
                                OOOO0OOO0OOO0OOO0 =str (OO0OOO0O0O00OOO0O -OOOO00OO00O00OOO0 )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{OO0O000OOOOO0O0O0}分钟奖励🌱数量:{OOOO0OOO0OOO0OOO0}t粒')#line:777
        except Exception as OO00OOOO0000OO0OO :#line:778
            print (OO00OOOO0000OO0OO )#line:779
    def user_ad (O0OOOO0OOO0OOOOO0 ):#line:782
        try :#line:783
            OOO0O00OOOO000OOO =f'__{timi_new()}'#line:784
            OOO0OOOOO0OO0O0O0 ={'source':'scsc','authorization':O0OOOO0OOO0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00OOOO000OOO ),'signstring':OOO0O00OOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            OO0O00O0O0OOOO0O0 =requests .request ('get',f'{host}/user/ad',headers =OOO0OOOOO0OO0O0O0 ).json ()#line:796
            if 'status'in OO0O00O0O0OOOO0O0 :#line:798
                if OO0O00O0O0OOOO0O0 ['status']==200 :#line:799
                    OO00OO0O0O0OOOO00 =OO0O00O0O0OOOO0O0 ['data']['max_time']#line:800
                    OO0OO0OO0O000O00O =OO0O00O0O0OOOO0O0 ['data']['watch_time']#line:801
                    OOOO0OOO00OO00OO0 =OO0O00O0O0OOOO0O0 ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{OOOO0OOO00OO00OO0 + OO00OO0O0O0OOOO00 - OO0OO0OO0O000O00O}次丨好友提供:{OOOO0OOO00OO00OO0}次')#line:803
                    if OOOO0OOO00OO00OO0 +OO00OO0O0O0OOOO00 -OO0OO0OO0O000O00O >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        OO00OOO000OO00000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0OOOOO0OO0O0O0 ).json ()#line:806
                        if 'status'in OO00OOO000OO00000 :#line:808
                            if OO00OOO000OO00000 ['status']==200 :#line:809
                                OOOO00O00OO00OO0O =float (OO00OOO000OO00000 ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(OOOO00O00OO00OO0O)}t粒')#line:811
                                return True #line:812
                            if OO00OOO000OO00000 ['status']==500 :#line:813
                                O0OOOOO00OO00000O =OO00OOO000OO00000 ['message']#line:814
                                print (f'【获取种子】:{O0OOOOO00OO00000O}')#line:815
                                return False #line:816
        except Exception as OOO00OO000OO000OO :#line:817
            print (OOO00OO000OO000OO )#line:818
    def synthetic (O0OO000O000OO0OOO ):#line:821
        global id ,g #line:822
        try :#line:823
            O00OO000O0O0OO00O =O0OO000O000OO0OOO .level_new ()#line:824
            O0O0OO000OOOO0OOO =random .randint (9 ,11 )#line:825
            O00000OO0O0O0O0O0 =f'_site=8&targetSite={O0O0OO000OOOO0OOO}_{timi_new()}'#line:826
            O0OO00O000OO0OOO0 ={'source':'scsc','authorization':O0OO000O000OO0OOO .token ,'timestamp':timi_new (),'sign':sign (O00000OO0O0O0O0O0 ),'signstring':O00000OO0O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            O000OOO0OO0O0OO0O ={"site":int (8 ),"targetSite":int (O0O0OO000OOOO0OOO )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00O000OO0OOO0 ,json =O000OOO0OO0O0OO0O )#line:839
            while True :#line:840
                OO0O0O0O000OO0OO0 =f'__{timi_new()}'#line:841
                O0OOO0O0OOO000OOO ={'source':'scsc','authorization':O0OO000O000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O000OO0OO0 ),'signstring':OO0O0O0O000OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                O0OOOO00O0OO0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0O0OOO000OOO ).json ()#line:853
                if 'status'in O0OOOO00O0OO0O0OO :#line:855
                    if O0OOOO00O0OO0O0OO ['status']==200 :#line:856
                        OO0OO0000O00O00OO =O0OOOO00O0OO0O0OO ['data']['cropList']#line:857
                        O00O0O0OO0000000O =O0OOOO00O0OO0O0OO ['data']['gameCoreDataDBid']#line:858
                        O0O00OO0000O000O0 =float (O0OOOO00O0OO0O0OO ['data']['silver'])/1000000000000 #line:859
                        OO0O000000O00O00O =0 #line:864
                        for OO0O0O0O0OOO00000 in OO0OO0000O00O00OO :#line:865
                            if not OO0O0O0O0OOO00000 :#line:866
                                O0O000OOOO00O0O0O =f'_crop_id={O00O0O0OO0000000O}&site={OO0O000000O00O00O}_{O0OO000O000OO0OOO.time}'#line:867
                                OO0O000OO000OOOO0 ={'source':'scsc','authorization':O0OO000O000OO0OOO .token ,'timestamp':O0OO000O000OO0OOO .time ,'sign':sign (O0O000OOOO00O0O0O ),'signstring':O0O000OOOO00O0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                O000O000OOOO00O0O ={"site":OO0O000000O00O00O ,"crop_id":O00O0O0OO0000000O }#line:878
                                OO000O0O0O0000O0O =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O000OO000OOOO0 ,data =O000O000OOOO00O0O ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in OO000O0O0O0000O0O :#line:882
                                    if OO000O0O0O0000O0O ['status']==200 :#line:883
                                        if OO000O0O0O0000O0O ['message']=='种子数量不足':#line:884
                                            O00OO000O0O0OO00O =O0OO000O000OO0OOO .level_new ()#line:885
                                            print (f'【种植合成】:{OO000O0O0O0000O0O["message"]}')#line:886
                                            if not O0OO000O000OO0OOO .user_ad ():#line:887
                                                return False #line:888
                                    if OO000O0O0O0000O0O ['status']==500 :#line:889
                                        print (f'【种植合成】:{OO000O0O0O0000O0O["message"]}')#line:890
                                        return False #line:891
                            OO0O000000O00O00O +=1 #line:892
                        OO000OO0OO000O00O =requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0O0OOO000OOO ).json ()#line:893
                        O0OOO0O0OO000O0O0 =OO000OO0OO000O00O ['data']['cropList']#line:894
                        OOOO00000OOOOO0O0 =False #line:895
                        for OO0O0O0O0OOO00000 in range (12 ):#line:896
                            id =O0OOO0O0OO000O0O0 [OO0O0O0O0OOO00000 ]['level']#line:897
                            if float (O00OO000O0O0OO00O )-float (id )>9 :#line:898
                                O0OOO00O0O0O0O0O0 =f'_site={OO0O0O0O0OOO00000}_{timi_new()}'#line:899
                                O0OO00000O0O0OOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO000O000OO0OOO .token ,'timestamp':timi_new (),'sign':sign (O0OOO00O0O0O0O0O0 ),'signstring':O0OOO00O0O0O0O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                OO0OOOO0OOO00O00O ={"site":OO0O0O0O0OOO00000 }#line:911
                                O00OO00OOO00O00OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO00000O0O0OOO0 ,data =OO0OOOO0OOO00O00O ).json ()#line:913
                                if 'status'in O00OO00OOO00O00OO :#line:914
                                    if O00OO00OOO00O00OO ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for O0OOOO0O0O000000O in range (11 ):#line:918
                                    O00000OOOOO00O00O =O0OOOO0O0O000000O +1 #line:919
                                    g =O0OOO0O0OO000O0O0 [O00000OOOOO00O00O ]['level']#line:920
                                    if id ==g :#line:921
                                        O00OO00O0OO0O0000 =O0OOOO0O0O000000O +2 #line:922
                                        if O00OO00O0OO0O0000 !=OO0O0O0O0OOO00000 +1 :#line:923
                                            O00OOOOO00OO00OOO =OO0O0O0O0OOO00000 +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            O00000OO0O0O0O0O0 =f'_site={O00OOOOO00OO00OOO - 1}&targetSite={O00OO00O0OO0O0000 - 1}_{timi_new()}'#line:927
                                            O0OO00O000OO0OOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO000O000OO0OOO .token ,'timestamp':timi_new (),'sign':sign (O00000OO0O0O0O0O0 ),'signstring':O00000OO0O0O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            OOOO0O0O0O0OOOO0O ={"site":int (O00OOOOO00OO00OOO -1 ),"targetSite":int (O00OO00O0OO0O0000 -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OO00O000OO0OOO0 ,json =OOOO0O0O0O0OOOO0O )#line:946
                                            OOOO00000OOOOO0O0 =True #line:948
                                    if OOOO00000OOOOO0O0 :#line:949
                                        break #line:950
                                if OOOO00000OOOOO0O0 :#line:951
                                    break #line:952
        except :#line:953
            O0OO000O000OO0OOO .synthetic ()#line:954
    def level_new (OO0O0OO000000OOO0 ):#line:957
        try :#line:958
            OOOO000OOOOO00O0O =f'__{timi_new()}'#line:959
            O0OO0000O00O0OO0O ={'source':'scsc','authorization':OO0O0OO000000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOOOO00O0O ),'signstring':OOOO000OOOOO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            OOOO00O0OO0OO00OO =requests .request ('get',f'{host}/user',headers =O0OO0000O00O0OO0O ).json ()#line:971
            if 'status'in OOOO00O0OO0OO00OO :#line:972
                if OOOO00O0OO0OO00OO ['status']==200 :#line:973
                    return float (OOOO00O0OO0OO00OO ['data']['level'])#line:974
        except Exception as O00O0O000O0O00OOO :#line:975
            print (O00O0O000O0O00OOO )#line:976
    def propsraffle (OOO0000OO0O0000O0 ):#line:979
        try :#line:980
            while True :#line:981
                O00O0O0OO00O00OO0 =f'__{timi_new()}'#line:982
                O0O00O00O00O0O0OO ={'source':'scsc','authorization':OOO0000OO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO00O00OO0 ),'signstring':O00O0O0OO00O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                OO0O0OOOO0OOOO0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00O00O00O0O0OO ).json ()#line:994
                if 'status'in OO0O0OOOO0OOOO0OO :#line:996
                    if OO0O0OOOO0OOOO0OO ['status']==200 :#line:997
                        OOOOO00O0OO00OO00 =OO0O0OOOO0OOOO0OO ['data']['rows']#line:998
                        O00OOOO0OOOOO0OO0 =OO0O0OOOO0OOOO0OO ['data']['vstate']#line:999
                        if OOOOO00O0OO00OO00 ==5 or OOOOO00O0OO00OO00 ==6 or OOOOO00O0OO00OO00 ==7 :#line:1000
                            O0O0OOOO0O000OO00 =OO0O0OOOO0OOOO0OO ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{O0O0OOOO0O000OO00}')#line:1002
                        if OOOOO00O0OO00OO00 ==1 or OOOOO00O0OO00OO00 ==2 or OOOOO00O0OO00OO00 ==3 :#line:1003
                            OOOO0O000OO00OOO0 =OO0O0OOOO0OOOO0OO ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{OOOO0O000OO00OOO0}')#line:1005
                        if OOOOO00O0OO00OO00 ==4 or OOOOO00O0OO00OO00 ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if OOOOO00O0OO00OO00 =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as OO00O000O0000O00O :#line:1047
            print (OO00O000O0000O00O )#line:1048
    def friends_invitation (OO00000OO0OO0OO00 ):#line:1051
        try :#line:1052
            O0OOOO0O0OOO0OOO0 =f'__{timi_new()}'#line:1053
            O0O00OOOOOO0OOOOO ={'source':'scsc','authorization':OO00000OO0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O0OOO0OOO0 ),'signstring':O0OOOO0O0OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            OOO000000OO000O0O =requests .request ('get',f'{host}/friends',headers =O0O00OOOOOO0OOOOO ).json ()#line:1065
            if 'status'in OOO000000OO000O0O :#line:1066
                if OOO000000OO000O0O ['status']==200 :#line:1067
                    O0OOOOOOO00O0O00O =OOO000000OO000O0O ['data']['myInviteter']#line:1068
                    if O0OOOOOOO00O0O00O :#line:1069
                        OO0O0OO00OO00OOOO =O0OOOOOOO00O0O00O ['user']['nickname']#line:1070
                        OOOO00OOO00OO0000 =OO00000OO0OO0OO00 .certification ()#line:1071
                        if OOOO00OOO00OO0000 =='未实名':#line:1072
                            weishim .append (OO00000OO0OO0OO00 .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{OO0O0OO00OO00OOOO}丨实名:{OOOO00OOO00OO0000}')#line:1074
                    else :#line:1075
                        if OO00000OO0OO0OO00 .innerId !='0':#line:1076
                            OO00000OO0OO0OO00 .invitation ()#line:1077
        except Exception as OOOO00O00OO0OO0OO :#line:1078
            print (OOOO00O00OO0OO0OO )#line:1079
    def add_clover (O000O0OO0O00OOO00 ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            OO0000OOOOOOOO0OO =f'__{timi_new()}'#line:1085
            OO000OOOOO00OO0O0 ={'source':'scsc','authorization':O000O0OO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOOOOOO0OO ),'signstring':OO0000OOOOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OOOOO0O0O00O0OO0O =requests .request ('get',f'{host}/assets/clovers',headers =OO000OOOOO00OO0O0 ).json ()#line:1097
            if 'status'in OOOOO0O0O00O0OO0O :#line:1099
                if OOOOO0O0O00O0OO0O ['status']==200 :#line:1100
                    O00O000000O0OOO00 =OOOOO0O0O00O0OO0O ['data']['clover']#line:1101
                    OO0OOO0O00OO000OO =OOOOO0O0O00O0OO0O ['data']['used_clover']#line:1102
                    O00O00O00O00O0OO0 =float (O00O000000O0OOO00 )-float (OO0OOO0O00OO000OO )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OOO0O00OO000OO}')#line:1104
                    if O000O0OO0O00OOO00 .certification ()!='未实名':#line:1105
                        if O00O00O00O00O0OO0 >1 :#line:1106
                            OO0000OOOOOOOO0OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O00O00O00O0OO0)}_{timi_new()}'#line:1107
                            OO0OO00OO00O0O000 ={'source':'scsc','authorization':O000O0OO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOOOOOO0OO ),'signstring':OO0000OOOOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            OO00OOO00O0O00OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O00O00O00O0OO0 )}#line:1119
                            OO00O0OO00OOO0O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OO00OO00O0O000 ,data =OO00OOO00O0O00OO0 ).json ()#line:1120
                            if 'status'in OO00O0OO00OOO0O0O :#line:1122
                                if OO00O0OO00OOO0O0O ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{OO00O0OO00OOO0O0O["data"]["isSuccess"]}丨数量:{O00O00O00O00O0OO0}')#line:1124
                                if OO00O0OO00OOO0O0O ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{OO00O0OO00OOO0O0O["message"]}')#line:1126
            OOO000O00O0O0OO0O =requests .request ('get',f'{host}/lottery',headers =OO000OOOOO00OO0O0 ).json ()#line:1127
            OOOOO0O000O0OO0O0 =O000O0OO0O00OOO00 .winning_rewards ()#line:1129
            if 'status'in OOO000O00O0O0OO0O :#line:1130
                if OOO000O00O0O0OO0O ['status']==200 :#line:1131
                    O00OO0OO0OO00OO00 =OOO000O00O0O0OO0O ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (O00OO0OO0OO00OO00 )#line:1133
                    OO0OOOOO00OO0O000 =OOO000O00O0O0OO0O ['data'][1 ]['value']#line:1134
                    O00OOO0O00OO0OO00 =OOO000O00O0O0OO0O ['data'][0 ]['join_number']#line:1135
                    O0OOOO0OO0O0OOOOO =int (float (OOO000O00O0O0OO0O ['data'][0 ]['totalValue']))#line:1136
                    O0OO0O000O0O00O0O =float (OO0OOOOO00OO0O000 /O0OOOO0OO0O0OOOOO )*10000 #line:1137
                    O00OO0OO00O0O00O0 =O0OOOO0OO0O0OOOOO /O00OOO0O00OO0OO00 #line:1138
                    print (f'【参与抽奖】:预计每天中{str(O00OO0OO0OO00OO00)[:6]}颗金种子丨好友收益:{str(OOOOO0O000O0OO0O0)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O0OO0O000O0O00O0O)[:6]}颗金种子丨☘️人均:{str(O00OO0OO00O0O00O0)[:7]}️')#line:1140
        except Exception as OOOO000O0OO00O0OO :#line:1141
            print (OOOO000O0OO00O0OO )#line:1142
    def energy (OOO0O0O00O0O00O00 ):#line:1145
        try :#line:1146
            while True :#line:1147
                O0O0000O0O00O000O =f'__{timi_new()}'#line:1148
                O0OO0OO00000OO0O0 ={'source':'scsc','authorization':OOO0O0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0O00O000O ),'signstring':O0O0000O0O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                O0O000000O0OOO00O =requests .request ('get',f'{host}/energy/general',headers =O0OO0OO00000OO0O0 ).json ()#line:1160
                if 'status'in O0O000000O0OOO00O :#line:1162
                    if O0O000000O0OOO00O ['status']==200 :#line:1163
                        OO0OOOOOO0OO000OO =O0O000000O0OOO00O ['data']['ordinary_water']#line:1164
                        OOOO000O0O00O0O00 =O0O000000O0OOO00O ['data']['ordinary_fertilizer']#line:1165
                        OOO00O0OO00O000OO =O0O000000O0OOO00O ['data']['videoStatus']#line:1166
                        OO000O00OO0OO000O =O0O000000O0OOO00O ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(OOOO000O0O00O0O00).split(".")[0]}丨水滴:{str(OO0OOOOOO0OO000OO).split(".")[0]}')#line:1169
                        if float (OOOO000O0O00O0O00 )<96 :#line:1170
                            if OOO00O0OO00O000OO :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                OOO0OO0O0O00OO00O =99 -float (OOOO000O0O00O0O00 )#line:1173
                                OOO0000OOOOOO0O0O ={"fertilizer":str (OOO0OO0O0O00OO00O ).split ('.')[0 ]}#line:1174
                                OO00OO0OO00O0O000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0OO00000OO0O0 ).json ()#line:1176
                                if 'status'in OO00OO0OO00O0O000 :#line:1178
                                    if OO00OO0OO00O0O000 ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{OO00OO0OO00O0O000["message"]}')#line:1180
                                    if OO00OO0OO00O0O000 ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{OO00OO0OO00O0O000["message"]}')#line:1182
                                        break #line:1183
                                if float (OOOO000O0O00O0O00 )<78 :#line:1185
                                    OOO0OO0O0O00OO00O =80 -float (OOOO000O0O00O0O00 )#line:1186
                                    O0OOO00OOOO0OOOO0 =f'_fertilizer={int(OOO0OO0O0O00OO00O)}_{timi_new()}'#line:1187
                                    O0OOOOO0O0O0O0O0O ={'source':'scsc','authorization':OOO0O0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOO0OOOO0 ),'signstring':O0OOO00OOOO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    O0OO0O0OOOO0000O0 ={"fertilizer":int (OOO0OO0O0O00OO00O )}#line:1199
                                    O00O0000O000000O0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOOOO0O0O0O0O0O ,data =O0OO0O0OOOO0000O0 ).json ()#line:1201
                                    if 'status'in O00O0000O000000O0 :#line:1203
                                        if O00O0000O000000O0 ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{O00O0000O000000O0["message"]}丨数量:{int(OOO0OO0O0O00OO00O)}')#line:1205
                                        if O00O0000O000000O0 ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{O00O0000O000000O0["message"]}丨数量:{int(OOO0OO0O0O00OO00O)}')#line:1207
                                            O0000OO0OO000OOOO =O00O0000O000000O0 ["message"].split ('-')[1 ]#line:1208
                                            OO00OOO0OOO0O0OOO =f'__{timi_new()}'#line:1209
                                            OO0O0O000OOO00OO0 ={'source':'scsc','authorization':OOO0O0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOO0O0OOO ),'signstring':OO00OOO0OOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            O0OO0OO00O00O0OOO =requests .request ('get',f'{host}/user',headers =OO0O0O000OOO00OO0 ).json ()#line:1221
                                            if 'status'in O0OO0OO00O00O0OOO :#line:1222
                                                if O0OO0OO00O00O0OOO ['status']==200 :#line:1223
                                                    O0OO000OO0OO0000O =O0OO0OO00O00O0OOO ['data']['inner_id']#line:1224
                                                    if give_gold (O0OO000OO0OO0000O ,float (O0000OO0OO000OOOO )+1 ):#line:1225
                                                        OOO0O0O00O0O00O00 .energy ()#line:1226
                        if float (OO0OOOOOO0OO000OO )<880 :#line:1227
                            if OO000O00OO0OO000O :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O0O0O00OO0O0000OO =999 -float (OO0OOOOOO0OO000OO )#line:1230
                                OO0OOOOO0OO0O00O0 ={"water":str (O0O0O00OO0O0000OO ).split ('.')[0 ]}#line:1231
                                OOOO0O00OO00000O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0OO00000OO0O0 ).json ()#line:1233
                                if 'status'in OOOO0O00OO00000O0 :#line:1235
                                    if OOOO0O00OO00000O0 ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O00OO00000O0["message"]}')#line:1237
                                    if OOOO0O00OO00000O0 ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O00OO00000O0["message"]}')#line:1239
                                        break #line:1240
                                if float (OO0OOOOOO0OO000OO )<780 :#line:1241
                                    O0O0O00OO0O0000OO =800 -float (OO0OOOOOO0OO000OO )#line:1242
                                    OOOO00O0O00OOO0OO =f'_water={int(O0O0O00OO0O0000OO)}_{timi_new()}'#line:1243
                                    OO000O00OO0O000OO ={'source':'scsc','authorization':OOO0O0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0O00OOO0OO ),'signstring':OOOO00O0O00OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    O00OO0OO0OOO0OOO0 ={"water":int (O0O0O00OO0O0000OO )}#line:1255
                                    O00OO00O00O00O000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO000O00OO0O000OO ,data =O00OO0OO0OOO0OOO0 ).json ()#line:1257
                                    if 'status'in O00OO00O00O00O000 :#line:1259
                                        if O00OO00O00O00O000 ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O00OO00O00O00O000["message"]}丨数量:{int(O0O0O00OO0O0000OO)}')#line:1261
                                        if O00OO00O00O00O000 ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O00OO00O00O00O000["message"]}丨数量:{int(O0O0O00OO0O0000OO)}')#line:1263
                                            O0000OO0OO000OOOO =O00OO00O00O00O000 ["message"].split ('-')[1 ]#line:1264
                                            OO00OOO0OOO0O0OOO =f'__{timi_new()}'#line:1265
                                            OO0O0O000OOO00OO0 ={'source':'scsc','authorization':OOO0O0O00O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO0OOO0O0OOO ),'signstring':OO00OOO0OOO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            O0OO0OO00O00O0OOO =requests .request ('get',f'{host}/user',headers =OO0O0O000OOO00OO0 ).json ()#line:1277
                                            if 'status'in O0OO0OO00O00O0OOO :#line:1278
                                                if O0OO0OO00O00O0OOO ['status']==200 :#line:1279
                                                    O0OO000OO0OO0000O =O0OO0OO00O00O0OOO ['data']['inner_id']#line:1280
                                                    if give_gold (O0OO000OO0OO0000O ,float (O0000OO0OO000OOOO )+1 ):#line:1281
                                                        OOO0O0O00O0O00O00 .energy ()#line:1282
                        break #line:1283
        except Exception as OO0000O0000OOO0O0 :#line:1284
            print (OO0000O0000OOO0O0 )#line:1285
def bundled_def ():#line:1288
    O0O000O000OOO0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return O0O000O000OOO0OO0 [random .randint (0 ,len (O0O000O000OOO0OO0 )-1 )]#line:1290
def version_of_the_validation ():#line:1294
    return str ((100 -56 )/10 )#line:1295
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
        OOO00000000O00O0O =gitee_edition ()#line:1329
        if version_of_the_validation ()<OOO00000000O00O0O ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00000000O00O0O["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{OOO00000000O00O0O["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO00000000O00O0O["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {OOO00000000O00O0O["CityEarth"]["content"]}')#line:1335
    except Exception as O000OO000OO0O0OOO :#line:1336
        print (O000OO000OO0O0OOO )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
