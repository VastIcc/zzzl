# coding: utf-8
try:
    import threading, re, os, sys, time, hashlib, json, requests, random, socket, uuid
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
@ 版本  3.2
"""
##################################配置区##################################
time_xx = random.randint(15, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419541311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
def start ():#line:7
    try :#line:8
        O000OO000O0O00OOO00 ()#line:9
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:10
        O000OO0O00OO00O00 ()#line:11
        O00OO0O0OOO0O00O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O00OO0O0OOO0O00O0)}个账号==========")#line:13
        for OO00000O0O0O00OO0 in O00OO0O0OOO0O00O0 :#line:14
            O0OO0000O000O00O0 =[]#line:15
            print (f"------------正在执行第{O00OO0O0OOO0O00O0.index(OO00000O0O0O00OO0) + 1}个账号------------")#line:16
            OOOO00O00000OOO0O =CityEarth (OO00000O0O0O00OO0 ,O0OO0000O000O00O0 ,O00OO0O0OOO0O00O0 .index (OO00000O0O0O00OO0 ))#line:17
            def OOOOOO0O000OOOO00 ():#line:19
                if OOOO00O00000OOO0O .base_info ():#line:21
                    OOOO00O00000OOO0O .sealing ()#line:23
                    OOOO00O00000OOO0O .invitenum ()#line:25
                    OOOO00O00000OOO0O .game_map ()#line:27
                    OOOO00O00000OOO0O .friends_invitation ()#line:29
                    OOOO00O00000OOO0O .energy ()#line:31
                    OOOO00O00000OOO0O .add_clover ()#line:33
                    OOOO00O00000OOO0O .propsraffle ()#line:35
                    OOOO00O00000OOO0O .synthetic ()#line:37
                    OOOO00O00000OOO0O .crops_illustrated ()#line:39
                    OOOO00O00000OOO0O .give_gold ()#line:41
                    OOOO00O00000OOO0O .withdraw ()#line:43
            O000O0000000OO00O =threading .Thread (target =OOOOOO0O000OOOO00 )#line:45
            O000O0000000OO00O .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        O0OOO000O0O0OO000 =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OOO000O0O0OO000 +' ')#line:51
    except Exception as OOOOOOO00O000OO0O :#line:52
        print (OOOOOOO00O000OO0O )#line:53
def give_gold (O000O00O00O0000OO ,OOO00O0OOOOO0O00O ):#line:56
        try :#line:57
            OO0O000O0OO000OOO =f'_doneeNo={O000O00O00O0000OO}&quantity={int(OOO00O0OOOOO0O00O)}_{timi_new()}'#line:58
            O0O0O0OO00OO0O000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O000O0OO000OOO ),'signstring':OO0O000O0OO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OOOOO000OO00OO000 ={"quantity":int (OOO00O0OOOOO0O00O ),"doneeNo":O000O00O00O0000OO }#line:73
            O0O0OOOOO000O000O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0OO00OO0O000 ,data =OOOOO000OO00OO000 ).json ()#line:74
            if 'status'in O0O0OOOOO000O000O :#line:76
                if O0O0OOOOO000O000O ['status']==200 :#line:77
                    if O0O0OOOOO000O000O ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(OOO00O0OOOOO0O00O)}种子给{O000O00O00O0000OO}成功')#line:79
                        return True #line:80
                if O0O0OOOOO000O000O ['status']==401 :#line:81
                    print (f'【赠送种子】:{O0O0OOOOO000O000O["message"]}')#line:82
                    return False #line:83
                if O0O0OOOOO000O000O ['status']==500 :#line:84
                    print (f'【赠送种子】:{O0O0OOOOO000O000O["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as OO000OOOOOO0O000O :#line:88
            print (OO000OOOOOO0O000O )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (OOOOOO0OO00OOO000 ):#line:94
    OO00OOOOO0O000O00 =hashlib .md5 (OOOOOO0OO00OOO000 .encode ()).hexdigest ()#line:95
    O0O00OO00OO0O0OOO =sc1 ()#line:96
    O0O00OO0OOOO0000O =sc2 ()#line:97
    OO000000OO0OO0000 =sc3 ()#line:98
    O0O00000OOO0O0O00 =O0O00OO00OO0O0OOO +OO00OOOOO0O000O00 +O0O00OO0OOOO0000O +OO000000OO0OO0000 #line:99
    O0O00OO00OOOO000O =hashlib .md5 (O0O00000OOO0O0O00 .encode ()).hexdigest ()#line:100
    return O0O00OO00OOOO000O #line:101
def format_msg ():#line:105
    O000O000000OOOO0O =""#line:106
    for O00O0O0O00OOO00O0 in msg_list :#line:107
        O000O000000OOOO0O +=str (O00O0O0O00OOO00O0 )+"\r\n"#line:108
    return O000O000000OOOO0O #line:109
def sc1 ():#line:111
    return "scsc%^&*"#line:112
def O000OO0O00OO00O00 ():#line:114
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:115
        pass #line:116
    else :#line:117
        exit (1 )#line:118
def timi_new ():#line:120
    return str (int (time .time ()*1000 ))#line:121
json_path ="CityEarth_data.json"#line:124
json_path1 ="CityEarth_data.json"#line:125
dict ={}#line:126
def get_json_data (OOOOOO0O00OO0000O ,O0000000OO0OOOO00 ,O0O000000OO0OOO0O ,OOOO0O0000O0OO0OO ):#line:128
    with open (OOOOOO0O00OO0000O ,'rb')as O00O0000OO000OOOO :#line:130
        O00OOOOOO0O00O0O0 =json .load (O00O0000OO000OOOO )#line:131
        O00OOOOOO0O00O0O0 ['data'][O0000000OO0OOOO00 ][O0O000000OO0OOO0O ]=OOOO0O0000O0OO0OO #line:132
        OOO00O0OO00O0OOOO =O00OOOOOO0O00O0O0 #line:133
    O00O0000OO000OOOO .close ()#line:134
    return OOO00O0OO00O0OOOO #line:135
def write_json_data (O0OO0O0O0OOOOOOOO ):#line:137
    with open (json_path1 ,'w')as O0OO0O0O00OOO00O0 :#line:138
        json .dump (O0OO0O0O0OOOOOOOO ,O0OO0O0O00OOO00O0 )#line:139
    O0OO0O0O00OOO00O0 .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (O0O000OOO0OOOOO0O ,O0OO00OO0O0OOOOOO ,O0O0O0OO00O0000OO ,O00O000OO00O0000O ):#line:145
        try :#line:146
            O0O000OOO0OOOOO0O .msg =O0O0O0OO00O0000OO #line:147
            O0O000OOO0OOOOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            O0O000OOO0OOOOO0O .token =O0OO00OO0O0OOOOOO ['authorization']#line:149
            O0O000OOO0OOOOO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            O0O000OOO0OOOOO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            O0O000OOO0OOOOO0O .elephant_user =O0OO00OO0O0OOOOOO ['elephant_user']#line:152
            O0O000OOO0OOOOO0O .elephant_pswd =O0OO00OO0O0OOOOOO ['elephant_pswd']#line:153
            O0O000OOO0OOOOO0O .elephant_Task_ID =O0OO00OO0O0OOOOOO ['elephant_Task_ID']#line:154
            O0O000OOO0OOOOO0O .len_new =O00O000OO00O0000O #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (O0O0OO0O0O0O0O0O0 ):#line:160
        try :#line:161
            O0O0OO0O0O0O0O0O0 .watched_ad ()#line:163
            O0OOO0O000O0OO0O0 =f'__{timi_new()}'#line:164
            OO0O0O0000O000000 ={'source':'scsc','authorization':O0O0OO0O0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O000O0OO0O0 ),'signstring':O0OOO0O000O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            O000O0O00OO0OO0OO =requests .request ('get',f'{host}/user',headers =OO0O0O0000O000000 ).json ()#line:176
            if 'status'in O000O0O00OO0OO0OO :#line:178
                if O000O0O00OO0OO0OO ['status']==200 :#line:179
                    OO0000OO00OOOO00O =O000O0O00OO0OO0OO ['data']['nickname']#line:180
                    OO0OO0OO0OOOOO00O =O000O0O00OO0OO0OO ['data']['inner_id']#line:181
                    O0OO0O00O0O0O0OOO =O000O0O00OO0OO0OO ['data']['assets']['gold']#line:182
                    OO0O0OO0000OO000O =O000O0O00OO0OO0OO ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{OO0000OO00OOOO00O[:5]}丨ID:{OO0OO0OO0OOOOO00O}丨等级:{OO0O0OO0000OO000O}丨金种子:{str(O0OO0O00O0O0O0OOO).split(".")[0]}')#line:184
                if O000O0O00OO0OO0OO ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if O0O0OO0O0O0O0O0O0 .elephant_user =='f':#line:187
                        return False #line:188
                    OO0O0000OOO000O00 =Invalid_login .addtask (elephant_user =O0O0OO0O0O0O0O0O0 .elephant_user ,elephant_pswd =O0O0OO0O0O0O0O0O0 .elephant_pswd ,elephant_Task_ID =O0O0OO0O0O0O0O0O0 .elephant_Task_ID )#line:189
                    OOO0O0000000OO00O =get_json_data (json_path ,O0O0OO0O0O0O0O0O0 .len_new ,'authorization',OO0O0000OOO000O00 )#line:190
                    if write_json_data (OOO0O0000000OO00O ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if O000O0O00OO0OO0OO ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as O0O0000O00O00O000 :#line:197
            print (O0O0000O00O00O000 )#line:198
    def sealing (OO000O0O000O0O0O0 ):#line:201
        try :#line:202
            O000000O00O00O00O =f'__{timi_new()}'#line:203
            O00O0OO00O00O0OO0 ={'source':'scsc','authorization':OO000O0O000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O00O00O00O ),'signstring':O000000O00O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O0OO00O00O0OO0 )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =O00O0OO00O00O0OO0 )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O0OO00O00O0OO0 )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O0OO00O00O0OO0 )#line:218
            requests .request ('get',f'{host}/user',headers =O00O0OO00O00O0OO0 )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O0OO00O00O0OO0 )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O0OO00O00O0OO0 )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O0OO00O00O0OO0 )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =O00O0OO00O00O0OO0 )#line:223
            requests .request ('get',f'{host}/assets',headers =O00O0OO00O00O0OO0 )#line:224
        except Exception as OOO0O00O0OO0OOOOO :#line:225
            print (OOO0O00O0OO0OOOOO )#line:226
    def withdraw (O00OOOOOO000000O0 ):#line:230
        OOO0000OOOOOOO0OO =f'__{timi_new()}'#line:231
        OOO0O00O00O00OO00 ={'source':'scsc','authorization':O00OOOOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOOOOOO0OO ),'signstring':OOO0000OOOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        O0OOOO000O0O00O00 =requests .request ('get',f'{host}/assets',headers =OOO0O00O00O00OO00 ).json ()#line:243
        if 'status'in O0OOOO000O0O00O00 :#line:245
            if O0OOOO000O0O00O00 ['status']==200 :#line:246
                OOOOO000OO0OOO0OO =O0OOOO000O0O00O00 ['data']['cash']#line:247
                if float (OOOOO000OO0OOO0OO )>20 :#line:248
                    OOO0000OOOOOOO0OO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    OOO0O00O00O00OO00 ={'authorization':O00OOOOOO000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOOOOOO0OO ),'signstring':OOO0000OOOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    OO000OO00OO0OO00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    O00000OOOOO0000OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0O00O00O00OO00 ,data =OO000OO00OO0OO00O ).json ()#line:262
                    print (O00000OOOOO0000OO )#line:263
    def invitenum (OOO000000000OOO00 ):#line:266
        O00O0O0OO0O000000 =f'__{timi_new()}'#line:267
        O0O000000OO0OOOOO ={'source':'scsc','authorization':OOO000000000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OO0O000000 ),'signstring':O00O0O0OO0O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        OO000OO0O00O0O00O =requests .request ('get',f'{host}/invite/invitenum',headers =O0O000000OO0OOOOO ).json ()#line:279
        if 'status'in OO000OO0O00O0O00O :#line:281
            if OO000OO0O00O0O00O ['status']==200 :#line:282
                O0O0O0O0OO000O0OO =OO000OO0O00O0O00O ['data']['invited_count']#line:283
                O00O0OO0OO00OOO00 =OO000OO0O00O0O00O ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{O0O0O0O0OO000O0OO}丨间邀好友:{O00O0OO0OO00OOO00}')#line:285
    def game_map (OO0OOO0O0O00000O0 ):#line:288
        try :#line:289
            O0O0O0O00OO000O00 =f'__{timi_new()}'#line:290
            OO0OOOOOOOO0OO0O0 ={'source':'scsc','authorization':OO0OOO0O0O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00OO000O00 ),'signstring':O0O0O0O00OO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0O00OOO00O0OO0O0 =requests .request ('get',f'{host}/game/map',headers =OO0OOOOOOOO0OO0O0 ).json ()#line:302
            if 'status'in O0O00OOO00O0OO0O0 :#line:304
                if O0O00OOO00O0OO0O0 ['status']==200 :#line:305
                    for O00O00OO00O000O0O in O0O00OOO00O0OO0O0 ['data']['list'][0 ]['crops']:#line:306
                        O0O00OO000O0O00OO =O00O00OO00O000O0O ['level']#line:308
                        if O0O00OO000O0O00OO ==41 :#line:309
                            OOO00OOOO0OOO000O =O00O00OO00O000O0O ['crop_name']#line:310
                            O0O0O000O0O0OO00O =O00O00OO00O000O0O ['count']#line:311
                            if O0O0O000O0O0OO00O >0 :#line:312
                                print (f'【农业资产】:{OOO00OOOO0OOO000O}丨数量:{O0O0O000O0O0OO00O}')#line:313
        except Exception as O00O0O0O0O0OOO0OO :#line:314
            print (O00O0O0O0O0OOO0OO )#line:315
    def give_gold (OO0O000O00OO0O000 ):#line:318
        try :#line:319
            OO000000OO00OOOO0 =f'__{timi_new()}'#line:320
            OOO000000O0O00000 ={'source':'scsc','authorization':OO0O000O00OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OO00OOOO0 ),'signstring':OO000000OO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            O0O00OOO00O00O00O =requests .request ('get',f'{host}/user',headers =OOO000000O0O00000 ).json ()#line:332
            if 'status'in O0O00OOO00O00O00O :#line:333
                if O0O00OOO00O00O00O ['status']==200 :#line:334
                    if float (OO0O000O00OO0O000 .doneeNo )!=0 :#line:335
                        OO00OO0O0000OOOO0 =O0O00OOO00O00O00O ['data']['assets']['gold']#line:336
                        if float (OO00OO0O0000OOOO0 )>float (OO0O000O00OO0O000 .innerId ):#line:337
                            OOO0O0OO000O000O0 =int (float (OO00OO0O0000OOOO0 )/1.1 )#line:338
                            OO000000OO00OOOO0 =f'_doneeNo={OO0O000O00OO0O000.doneeNo}&quantity={OOO0O0OO000O000O0}_{timi_new()}'#line:339
                            OOO000000O0O00000 ={'source':'scsc','authorization':OO0O000O00OO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OO00OOOO0 ),'signstring':OO000000OO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            OO0OO0O00OO00O0O0 ={"quantity":OOO0O0OO000O000O0 ,"doneeNo":OO0O000O00OO0O000 .doneeNo }#line:354
                            OO0O00000OO00OOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO000000O0O00000 ,data =OO0OO0O00OO00O0O0 ).json ()#line:355
                            if 'status'in OO0O00000OO00OOO0 :#line:357
                                if OO0O00000OO00OOO0 ['status']==200 :#line:358
                                    if OO0O00000OO00OOO0 ['data']:#line:359
                                        print (f'【赠送种子】:赠送{OOO0O0OO000O000O0}种子给{OO0O000O00OO0O000.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OO00OO000O00O000O :#line:363
            print (OO00OO000O00O000O )#line:364
    def invitation (O0OO0O0OO0OOO00O0 ):#line:366
        try :#line:367
            _OOOO00O00OOO00OO0 =float (bundled_def ())/4 #line:368
            O0000O00000O00O00 =f'_innerId={int(_OOOO00O00OOO00OO0)}_{timi_new()}'#line:369
            O00O000OOO0OOOO00 ={'source':'scsc','authorization':O0OO0O0OO0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00000O00O00 ),'signstring':O0000O00000O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            O00OOO000OO0000OO ={"innerId":int (_OOOO00O00OOO00OO0 )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O000OOO0OOOO00 ,data =O00OOO000OO0000OO )#line:382
        except Exception as OOOOO0O00000O0O00 :#line:383
            print (OOOOO0O00000O0O00 )#line:384
    def winning_rewards (OOOO00O0O000O0000 ):#line:387
        try :#line:388
            OOO0O0OO0O00O0O0O =f'__{timi_new()}'#line:389
            O0OO0O0OO0O0O0OOO ={'source':'scsc','authorization':OOOO00O0O000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0O00O0O0O ),'signstring':OOO0O0OO0O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            OO0O00O0OOOOOOOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0O0OO0O0O0OOO ).json ()#line:401
            if 'status'in OO0O00O0OOOOOOOOO :#line:403
                if OO0O00O0OOOOOOOOO ['status']==200 :#line:404
                    if OO0O00O0OOOOOOOOO ['data']['amount']:#line:405
                        O0OO0000OOO0000OO =OO0O00O0OOOOOOOOO ['data']['amount']['gold']#line:406
                        return O0OO0000OOO0000OO #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as OOOO0OO000000OO0O :#line:410
            print (OOOO0OO000000OO0O )#line:411
    def certification (OO000OOO00000OOOO ):#line:414
        try :#line:415
            OO0O0O000OO0O0OO0 =f'__{timi_new()}'#line:416
            OOO000O00OOOO0000 ={'source':'scsc','authorization':OO000OOO00000OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000OO0O0OO0 ),'signstring':OO0O0O000OO0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            O0OOOOOOOOO00000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO000O00OOOO0000 ).json ()#line:428
            if 'status'in O0OOOOOOOOO00000O :#line:430
                if O0OOOOOOOOO00000O ['status']==200 :#line:431
                    if O0OOOOOOOOO00000O ['data']['result']:#line:432
                        O0O0000OOOOOO0O0O =O0OOOOOOOOO00000O ['data']['nick_name']#line:433
                        return O0O0000OOOOOO0O0O #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as O0OO0O0OO00OOO000 :#line:437
            print (O0OO0O0OO00OOO000 )#line:438
    def crops_illustrated (OOO00000O000OO0OO ):#line:441
        try :#line:442
            O0OOO00OOO0O0O000 =f'__{timi_new()}'#line:443
            OO0O00OOOO00000O0 ={'source':'scsc','authorization':OOO00000O000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOO0O0O000 ),'signstring':O0OOO00OOO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            OO00O000OO0O0OO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00OOOO00000O0 ).json ()#line:455
            if 'status'in OO00O000OO0O0OO0O :#line:457
                if OO00O000OO0O0OO0O ['status']==200 :#line:458
                    OO0O0OOO0000O0O00 =OO00O000OO0O0OO0O ['data'][0 ]['crops']#line:459
                    for OOO0O00000O00OO0O in OO0O0OOO0000O0O00 :#line:460
                        if OOO0O00000O00OO0O ['ill_clover_award']:#line:461
                            if float (OOO0O00000O00OO0O ['ill_clover_award'])>1 :#line:462
                                if OOO0O00000O00OO0O ['is_finish']:#line:463
                                    if not OOO0O00000O00OO0O ['is_getit']:#line:464
                                        if OOO00000O000OO0OO .certification ()!='未实名':#line:465
                                            O0OOO00OOO0O0O000 =f'_award_level={OOO0O00000O00OO0O["level"]}_{timi_new()}'#line:466
                                            OO0O00OOOO00000O0 ={'source':'scsc','authorization':OOO00000O000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOO0O0O000 ),'signstring':O0OOO00OOO0O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            O00O000OO00OOO000 ={"award_level":OOO0O00000O00OO0O ['level']}#line:478
                                            OO00OO0OO0OO0OO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00OOOO00000O0 ,json =O00O000OO00OOO000 ).json ()#line:480
                                            if 'status'in OO00OO0OO0OO0OO0O :#line:481
                                                if OO00OO0OO0OO0OO0O ['status']==200 :#line:482
                                                    O000O000OOOO0O00O =OO00OO0OO0OO0OO0O ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{OOO0O00000O00OO0O["crop_name"]}成就丨奖励{O000O000OOOO0O00O}☘️')#line:485
                                                if OO00OO0OO0OO0OO0O ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{OO00OO0OO0OO0OO0O["message"]}')#line:487
        except Exception as OO0000OO00OOOO0OO :#line:488
            print (OO0000OO00OOOO0OO )#line:489
    def watched_ad (O0O0O0O00O0O0OOO0 ):#line:492
        try :#line:493
            O0O00OO0O0OO0O0OO =f'__{timi_new()}'#line:494
            O0O00OOOOOO0O0O0O ={'source':'scsc','authorization':O0O0O0O00O0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O0OO0O0OO ),'signstring':O0O00OO0O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            O00OO000O0000O000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OOOOOO0O0O0O ).json ()#line:506
            if 'status'in O00OO000O0000O000 :#line:508
                if O00OO000O0000O000 ['status']==200 :#line:509
                    if 'offlineInfo'in O00OO000O0000O000 ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        O0OO0O00O0O0O00O0 =O00OO000O0000O000 ['data']['offlineInfo']['off_minute']#line:512
                        O0O000O0OOOOOOOOO =float (O00OO000O0000O000 ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O00OOOOOO0O0O0O ).json ()#line:515
                        time .sleep (2 )#line:516
                        OO0OOOO0000O0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00OOOOOO0O0O0O ).json ()#line:517
                        if 'status'in OO0OOOO0000O0OOO0 :#line:519
                            if OO0OOOO0000O0OOO0 ['status']==200 :#line:520
                                O00O00000OOO00O0O =float (OO0OOOO0000O0OOO0 ['data']['silver'])/1000000000000 #line:521
                                O00O0OO00O00O0000 =str (O00O00000OOO00O0O -O0O000O0OOOOOOOOO )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{O0OO0O00O0O0O00O0}分钟奖励🌱数量:{O00O0OO00O00O0000}t粒')#line:523
        except Exception as OO0O000O0OOO0OO00 :#line:524
            print (OO0O000O0OOO0OO00 )#line:525
    def user_ad (OO000OO0O0OO0OOOO ):#line:528
        try :#line:529
            OOO00000OO00O0OO0 =f'__{timi_new()}'#line:530
            O0OOOOOOO0OO00OOO ={'source':'scsc','authorization':OO000OO0O0OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000OO00O0OO0 ),'signstring':OOO00000OO00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            OOO0OO0000O00OO00 =requests .request ('get',f'{host}/user/ad',headers =O0OOOOOOO0OO00OOO ).json ()#line:542
            if 'status'in OOO0OO0000O00OO00 :#line:544
                if OOO0OO0000O00OO00 ['status']==200 :#line:545
                    OO000O00OOOO00O00 =OOO0OO0000O00OO00 ['data']['max_time']#line:546
                    O0O0OO0O0O00O000O =OOO0OO0000O00OO00 ['data']['watch_time']#line:547
                    O00OO0O0OO0OOOOOO =OOO0OO0000O00OO00 ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{O00OO0O0OO0OOOOOO + OO000O00OOOO00O00 - O0O0OO0O0O00O000O}次丨好友提供:{O00OO0O0OO0OOOOOO}次')#line:549
                    if O00OO0O0OO0OOOOOO +OO000O00OOOO00O00 -O0O0OO0O0O00O000O >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        OOOOO000OO0O00000 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOOOOOO0OO00OOO ).json ()#line:552
                        if 'status'in OOOOO000OO0O00000 :#line:554
                            if OOOOO000OO0O00000 ['status']==200 :#line:555
                                OOO000000O0O0O00O =float (OOOOO000OO0O00000 ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(OOO000000O0O0O00O)}t粒')#line:557
                                return True #line:558
                            if OOOOO000OO0O00000 ['status']==500 :#line:559
                                O00O0OOOOO0OOOO00 =OOOOO000OO0O00000 ['message']#line:560
                                print (f'【获取种子】:{O00O0OOOOO0OOOO00}')#line:561
                                return False #line:562
        except Exception as OOOOOOOO00O000O0O :#line:563
            print (OOOOOOOO00O000O0O )#line:564
    def synthetic (O0O000OOOO0OOO000 ):#line:567
        global id ,g #line:568
        try :#line:569
            O00OO0OO000OOO0OO =O0O000OOOO0OOO000 .level_new ()#line:570
            O0000OOO00OOOO0O0 =random .randint (9 ,11 )#line:571
            O0OO00000OOOOOOOO =f'_site=8&targetSite={O0000OOO00OOOO0O0}_{timi_new()}'#line:572
            O0OOO000O0O0OO0O0 ={'source':'scsc','authorization':O0O000OOOO0OOO000 .token ,'timestamp':timi_new (),'sign':sign (O0OO00000OOOOOOOO ),'signstring':O0OO00000OOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            O0OO0O000O0O0OOO0 ={"site":int (8 ),"targetSite":int (O0000OOO00OOOO0O0 )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO000O0O0OO0O0 ,json =O0OO0O000O0O0OOO0 )#line:585
            while True :#line:586
                OO0O0000OO0OOOO0O =f'__{timi_new()}'#line:587
                O0O0OOOO00O0O0OO0 ={'source':'scsc','authorization':O0O000OOOO0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO0OOOO0O ),'signstring':OO0O0000OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                O0000OO0OO0OO0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOO00O0O0OO0 ).json ()#line:599
                if 'status'in O0000OO0OO0OO0000 :#line:601
                    if O0000OO0OO0OO0000 ['status']==200 :#line:602
                        O000000O00000OOOO =O0000OO0OO0OO0000 ['data']['cropList']#line:603
                        O00OOO0OO0O0OOO00 =O0000OO0OO0OO0000 ['data']['gameCoreDataDBid']#line:604
                        O0O0O0OO000OOOO00 =float (O0000OO0OO0OO0000 ['data']['silver'])/1000000000000 #line:605
                        O000OOO0O0OOOO00O =0 #line:610
                        for OOO0O00O0OO000OO0 in O000000O00000OOOO :#line:611
                            if not OOO0O00O0OO000OO0 :#line:612
                                O00O00O0O0OOO0O0O =f'_crop_id={O00OOO0OO0O0OOO00}&site={O000OOO0O0OOOO00O}_{O0O000OOOO0OOO000.time}'#line:613
                                OO00OOOOOOO0O0OOO ={'source':'scsc','authorization':O0O000OOOO0OOO000 .token ,'timestamp':O0O000OOOO0OOO000 .time ,'sign':sign (O00O00O0O0OOO0O0O ),'signstring':O00O00O0O0OOO0O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                OO0OOOOOO0OOO000O ={"site":O000OOO0O0OOOO00O ,"crop_id":O00OOO0OO0O0OOO00 }#line:624
                                O0O00OO00O000O0O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OOOOOOO0O0OOO ,data =OO0OOOOOO0OOO000O ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in O0O00OO00O000O0O0 :#line:628
                                    if O0O00OO00O000O0O0 ['status']==200 :#line:629
                                        if O0O00OO00O000O0O0 ['message']=='种子数量不足':#line:630
                                            O00OO0OO000OOO0OO =O0O000OOOO0OOO000 .level_new ()#line:631
                                            print (f'【种植合成】:{O0O00OO00O000O0O0["message"]}')#line:632
                                            if not O0O000OOOO0OOO000 .user_ad ():#line:633
                                                return False #line:634
                                    if O0O00OO00O000O0O0 ['status']==500 :#line:635
                                        print (f'【种植合成】:{O0O00OO00O000O0O0["message"]}')#line:636
                                        return False #line:637
                            O000OOO0O0OOOO00O +=1 #line:638
                        O00000000OOOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OOOO00O0O0OO0 ).json ()#line:639
                        OOO00OO0OOOO00O00 =O00000000OOOO0O0O ['data']['cropList']#line:640
                        O0O0O0OOOOO0O0O00 =False #line:641
                        for OOO0O00O0OO000OO0 in range (12 ):#line:642
                            id =OOO00OO0OOOO00O00 [OOO0O00O0OO000OO0 ]['level']#line:643
                            if float (O00OO0OO000OOO0OO )-float (id )>9 :#line:644
                                OOO00O0OOO0O0OOO0 =f'_site={OOO0O00O0OO000OO0}_{timi_new()}'#line:645
                                O00O0000OOOOOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OOOO0OOO000 .token ,'timestamp':timi_new (),'sign':sign (OOO00O0OOO0O0OOO0 ),'signstring':OOO00O0OOO0O0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O0OO00OOOO00OOO00 ={"site":OOO0O00O0OO000OO0 }#line:657
                                O0000OO000OOOO0OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00O0000OOOOOOOO0 ,data =O0OO00OOOO00OOO00 ).json ()#line:659
                                if 'status'in O0000OO000OOOO0OO :#line:660
                                    if O0000OO000OOOO0OO ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for OOOO0OOOO0OOOO0O0 in range (11 ):#line:664
                                    O0OO0OO00O00OO0O0 =OOOO0OOOO0OOOO0O0 +1 #line:665
                                    g =OOO00OO0OOOO00O00 [O0OO0OO00O00OO0O0 ]['level']#line:666
                                    if id ==g :#line:667
                                        O0O0OO00O0OO00O0O =OOOO0OOOO0OOOO0O0 +2 #line:668
                                        if O0O0OO00O0OO00O0O !=OOO0O00O0OO000OO0 +1 :#line:669
                                            O00O0OOO0000000OO =OOO0O00O0OO000OO0 +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            O0OO00000OOOOOOOO =f'_site={O00O0OOO0000000OO - 1}&targetSite={O0O0OO00O0OO00O0O - 1}_{timi_new()}'#line:673
                                            O0OOO000O0O0OO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O000OOOO0OOO000 .token ,'timestamp':timi_new (),'sign':sign (O0OO00000OOOOOOOO ),'signstring':O0OO00000OOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            OOO0OO000O000000O ={"site":int (O00O0OOO0000000OO -1 ),"targetSite":int (O0O0OO00O0OO00O0O -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0OOO000O0O0OO0O0 ,json =OOO0OO000O000000O )#line:692
                                            O0O0O0OOOOO0O0O00 =True #line:694
                                    if O0O0O0OOOOO0O0O00 :#line:695
                                        break #line:696
                                if O0O0O0OOOOO0O0O00 :#line:697
                                    break #line:698
        except :#line:699
            O0O000OOOO0OOO000 .synthetic ()#line:700
    def level_new (OOOOO0O00OO0OOO00 ):#line:703
        try :#line:704
            OO00O00O00OOOO000 =f'__{timi_new()}'#line:705
            O00O0000O00000OOO ={'source':'scsc','authorization':OOOOO0O00OO0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00O00OOOO000 ),'signstring':OO00O00O00OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            O0000O000O00O00OO =requests .request ('get',f'{host}/user',headers =O00O0000O00000OOO ).json ()#line:717
            if 'status'in O0000O000O00O00OO :#line:718
                if O0000O000O00O00OO ['status']==200 :#line:719
                    return float (O0000O000O00O00OO ['data']['level'])#line:720
        except Exception as O0O00OOO0OO00OO0O :#line:721
            print (O0O00OOO0OO00OO0O )#line:722
    def propsraffle (OOO00000OOO0OO0O0 ):#line:725
        try :#line:726
            while True :#line:727
                O0O00O00O00OOO0O0 =f'__{timi_new()}'#line:728
                OOO0000000OOOO000 ={'source':'scsc','authorization':OOO00000OOO0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O00OOO0O0 ),'signstring':O0O00O00O00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                OO00O0OO000OO0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0000000OOOO000 ).json ()#line:740
                if 'status'in OO00O0OO000OO0OO0 :#line:742
                    if OO00O0OO000OO0OO0 ['status']==200 :#line:743
                        OOOOOOOOO000O000O =OO00O0OO000OO0OO0 ['data']['rows']#line:744
                        O0O00O0O000O0O000 =OO00O0OO000OO0OO0 ['data']['vstate']#line:745
                        if OOOOOOOOO000O000O ==5 or OOOOOOOOO000O000O ==6 or OOOOOOOOO000O000O ==7 :#line:746
                            OO0O0O000OOOO0OOO =OO00O0OO000OO0OO0 ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{OO0O0O000OOOO0OOO}')#line:748
                        if OOOOOOOOO000O000O ==1 or OOOOOOOOO000O000O ==2 or OOOOOOOOO000O000O ==3 :#line:749
                            O0O0OO0O00O0000O0 =OO00O0OO000OO0OO0 ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{O0O0OO0O00O0000O0}')#line:751
                        if OOOOOOOOO000O000O ==4 or OOOOOOOOO000O000O ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if OOOOOOOOO000O000O =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as OOO0OOO0OO00OOO00 :#line:793
            print (OOO0OOO0OO00OOO00 )#line:794
    def friends_invitation (O00OOO000O0OOOOOO ):#line:797
        try :#line:798
            O0O0000OO0OO00OO0 =f'__{timi_new()}'#line:799
            O0000O00OO00000OO ={'source':'scsc','authorization':O00OOO000O0OOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OO00OO0 ),'signstring':O0O0000OO0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            O00O00O000O0O0OOO =requests .request ('get',f'{host}/friends',headers =O0000O00OO00000OO ).json ()#line:811
            if 'status'in O00O00O000O0O0OOO :#line:812
                if O00O00O000O0O0OOO ['status']==200 :#line:813
                    OO0000O0OOOO00O00 =O00O00O000O0O0OOO ['data']['myInviteter']#line:814
                    if OO0000O0OOOO00O00 :#line:815
                        OO000000OO0000O00 =OO0000O0OOOO00O00 ['user']['nickname']#line:816
                        O00OOO0OO0O0OO000 =O00OOO000O0OOOOOO .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{OO000000OO0000O00}丨实名:{O00OOO0OO0O0OO000}')#line:818
                    else :#line:819
                        if O00OOO000O0OOOOOO .innerId !='0':#line:820
                            O00OOO000O0OOOOOO .invitation ()#line:821
        except Exception as OOO000OOOO000O0O0 :#line:822
            print (OOO000OOOO000O0O0 )#line:823
    def add_clover (O0OOOO00O0O00OOOO ):#line:826
        global golden_seed #line:827
        try :#line:828
            O00O0O0O00OO0OO0O =f'__{timi_new()}'#line:829
            OO0O0OOO00O000O00 ={'source':'scsc','authorization':O0OOOO00O0O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O00OO0OO0O ),'signstring':O00O0O0O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            O0O000OO0000OO0OO =requests .request ('get',f'{host}/assets/clovers',headers =OO0O0OOO00O000O00 ).json ()#line:841
            if 'status'in O0O000OO0000OO0OO :#line:843
                if O0O000OO0000OO0OO ['status']==200 :#line:844
                    OO0OO000O0O0O00OO =O0O000OO0000OO0OO ['data']['clover']#line:845
                    OO00OO0000O00O0O0 =O0O000OO0000OO0OO ['data']['used_clover']#line:846
                    OO0O0OO0OO00OO0OO =float (OO0OO000O0O0O00OO )-float (OO00OO0000O00O0O0 )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO00OO0000O00O0O0}')#line:848
                    if O0OOOO00O0O00OOOO .certification ()!='未实名':#line:849
                        if OO0O0OO0OO00OO0OO >1 :#line:850
                            O00O0O0O00OO0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0O0OO0OO00OO0OO)}_{timi_new()}'#line:851
                            O0OO0OOO0OO0O0OO0 ={'source':'scsc','authorization':O0OOOO00O0O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O00OO0OO0O ),'signstring':O00O0O0O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            OOOOOOOOOO000OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0O0OO0OO00OO0OO )}#line:863
                            OO0000O000OO0OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0OOO0OO0O0OO0 ,data =OOOOOOOOOO000OOO0 ).json ()#line:864
                            if 'status'in OO0000O000OO0OO00 :#line:866
                                if OO0000O000OO0OO00 ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{OO0000O000OO0OO00["data"]}丨数量:{OO0O0OO0OO00OO0OO}')#line:868
                                if OO0000O000OO0OO00 ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{OO0000O000OO0OO00["message"]}')#line:870
            O00OOO000O0OOO0OO =requests .request ('get',f'{host}/lottery',headers =OO0O0OOO00O000O00 ).json ()#line:871
            OOO0000O0O0OO00OO =O0OOOO00O0O00OOOO .winning_rewards ()#line:873
            if 'status'in O00OOO000O0OOO0OO :#line:874
                if O00OOO000O0OOO0OO ['status']==200 :#line:875
                    O00OOOOO0OOOO00OO =O00OOO000O0OOO0OO ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (O00OOOOO0OOOO00OO )#line:877
                    O0O00OO0O0OO0O00O =O00OOO000O0OOO0OO ['data'][1 ]['value']#line:878
                    O00000O0OO00OO0O0 =O00OOO000O0OOO0OO ['data'][0 ]['join_number']#line:879
                    OOO00OO0O000OO00O =int (float (O00OOO000O0OOO0OO ['data'][0 ]['totalValue']))#line:880
                    O0O0000OO0OOOO0O0 =float (O0O00OO0O0OO0O00O /OOO00OO0O000OO00O )*10000 #line:881
                    OO00000OOO00O00O0 =OOO00OO0O000OO00O /O00000O0OO00OO0O0 #line:882
                    print (f'【参与抽奖】:预计每天中{str(O00OOOOO0OOOO00OO)[:6]}颗金种子丨好友收益:{str(OOO0000O0O0OO00OO)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0000OO0OOOO0O0)[:6]}颗金种子丨☘️人均:{str(OO00000OOO00O00O0)[:7]}️')#line:884
        except Exception as OO0000OOOO0000OOO :#line:885
            print (OO0000OOOO0000OOO )#line:886
    def energy (O00OO00OO00OO0O00 ):#line:890
        try :#line:891
            while True :#line:892
                OO0OO000O0O00000O =f'__{timi_new()}'#line:893
                O0OO0OOOOOOOOOOOO ={'source':'scsc','authorization':O00OO00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000O0O00000O ),'signstring':OO0OO000O0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                O0OOOO0OOOO000O0O =requests .request ('get',f'{host}/energy/general',headers =O0OO0OOOOOOOOOOOO ).json ()#line:905
                if 'status'in O0OOOO0OOOO000O0O :#line:907
                    if O0OOOO0OOOO000O0O ['status']==200 :#line:908
                        OO0000O00OOOOO0O0 =O0OOOO0OOOO000O0O ['data']['ordinary_water']#line:909
                        O0O00OO0OOOO0O0OO =O0OOOO0OOOO000O0O ['data']['ordinary_fertilizer']#line:910
                        OOOO00OO00OO00000 =O0OOOO0OOOO000O0O ['data']['videoStatus']#line:911
                        OOOO00000OO00O00O =O0OOOO0OOOO000O0O ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(O0O00OO0OOOO0O0OO).split(".")[0]}丨水滴:{str(OO0000O00OOOOO0O0).split(".")[0]}')#line:913
                        if float (O0O00OO0OOOO0O0OO )<96 :#line:914
                            if OOOO00OO00OO00000 :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                O00O0OO00O0O0O0O0 =99 -float (O0O00OO0OOOO0O0OO )#line:917
                                O0OOO00O0OOO000O0 ={"fertilizer":str (O00O0OO00O0O0O0O0 ).split ('.')[0 ]}#line:918
                                OO00O00OOOOOOOO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0OOOOOOOOOOOO ).json ()#line:919
                                if 'status'in OO00O00OOOOOOOO00 :#line:921
                                    if OO00O00OOOOOOOO00 ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{OO00O00OOOOOOOO00["message"]}')#line:923
                                    if OO00O00OOOOOOOO00 ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{OO00O00OOOOOOOO00["message"]}')#line:925
                                        break #line:926
                                if float (O0O00OO0OOOO0O0OO )<78 :#line:928
                                    O00O0OO00O0O0O0O0 =80 -float (O0O00OO0OOOO0O0OO )#line:929
                                    OO00OO00O0OOO0OO0 =f'_fertilizer={int(O00O0OO00O0O0O0O0)}_{timi_new()}'#line:930
                                    OOOOO000O0O0OOO00 ={'source':'scsc','authorization':O00OO00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O0OOO0OO0 ),'signstring':OO00OO00O0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    OOO00O0OO0000O0O0 ={"fertilizer":int (O00O0OO00O0O0O0O0 )}#line:942
                                    O0OO00O0000O000OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOOO000O0O0OOO00 ,data =OOO00O0OO0000O0O0 ).json ()#line:944
                                    if 'status'in O0OO00O0000O000OO :#line:946
                                        if O0OO00O0000O000OO ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{O0OO00O0000O000OO["message"]}丨数量:{int(O00O0OO00O0O0O0O0)}')#line:948
                                        if O0OO00O0000O000OO ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{O0OO00O0000O000OO["message"]}丨数量:{int(O00O0OO00O0O0O0O0)}')#line:950
                                            O0OO00O00O0OO0000 =O0OO00O0000O000OO ["message"].split ('-')[1 ]#line:951
                                            OO0O0000OO0000O0O =f'__{timi_new()}'#line:952
                                            OOO0O0OOO0OO0OO0O ={'source':'scsc','authorization':O00OO00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO0000O0O ),'signstring':OO0O0000OO0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            OOOOOOOO000O000O0 =requests .request ('get',f'{host}/user',headers =OOO0O0OOO0OO0OO0O ).json ()#line:964
                                            if 'status'in OOOOOOOO000O000O0 :#line:965
                                                if OOOOOOOO000O000O0 ['status']==200 :#line:966
                                                    O0OOO0000000OOOOO =OOOOOOOO000O000O0 ['data']['inner_id']#line:967
                                                    if give_gold (O0OOO0000000OOOOO ,float (O0OO00O00O0OO0000 )+1 ):#line:968
                                                        O00OO00OO00OO0O00 .energy ()#line:969
                        if float (OO0000O00OOOOO0O0 )<880 :#line:970
                            if OOOO00000OO00O00O :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                OO00OOO000O00O00O =999 -float (OO0000O00OOOOO0O0 )#line:973
                                OO0OOOO0O0O000000 ={"water":str (OO00OOO000O00O00O ).split ('.')[0 ]}#line:974
                                OO0OOO0O0O0OO0OOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0OOOOOOOOOOOO ).json ()#line:975
                                if 'status'in OO0OOO0O0O0OO0OOO :#line:977
                                    if OO0OOO0O0O0OO0OOO ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOO0O0O0OO0OOO["message"]}')#line:979
                                    if OO0OOO0O0O0OO0OOO ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOO0O0O0OO0OOO["message"]}')#line:981
                                        break #line:982
                                if float (OO0000O00OOOOO0O0 )<780 :#line:983
                                    OO00OOO000O00O00O =800 -float (OO0000O00OOOOO0O0 )#line:984
                                    OO0O00OOO0O0000OO =f'_water={int(OO00OOO000O00O00O)}_{timi_new()}'#line:985
                                    OOO00000OO0OOO0O0 ={'source':'scsc','authorization':O00OO00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO0O0000OO ),'signstring':OO0O00OOO0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    O0O0OO000O0OO00O0 ={"water":int (OO00OOO000O00O00O )}#line:997
                                    OOOO00OOO00OO00O0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00000OO0OOO0O0 ,data =O0O0OO000O0OO00O0 ).json ()#line:999
                                    if 'status'in OOOO00OOO00OO00O0 :#line:1001
                                        if OOOO00OOO00OO00O0 ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{OOOO00OOO00OO00O0["message"]}丨数量:{int(OO00OOO000O00O00O)}')#line:1003
                                        if OOOO00OOO00OO00O0 ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{OOOO00OOO00OO00O0["message"]}丨数量:{int(OO00OOO000O00O00O)}')#line:1005
                                            O0OO00O00O0OO0000 =OOOO00OOO00OO00O0 ["message"].split ('-')[1 ]#line:1006
                                            OO0O0000OO0000O0O =f'__{timi_new()}'#line:1007
                                            OOO0O0OOO0OO0OO0O ={'source':'scsc','authorization':O00OO00OO00OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO0000O0O ),'signstring':OO0O0000OO0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            OOOOOOOO000O000O0 =requests .request ('get',f'{host}/user',headers =OOO0O0OOO0OO0OO0O ).json ()#line:1019
                                            if 'status'in OOOOOOOO000O000O0 :#line:1020
                                                if OOOOOOOO000O000O0 ['status']==200 :#line:1021
                                                    O0OOO0000000OOOOO =OOOOOOOO000O000O0 ['data']['inner_id']#line:1022
                                                    if give_gold (O0OOO0000000OOOOO ,float (O0OO00O00O0OO0000 )+1 ):#line:1023
                                                        O00OO00OO00OO0O00 .energy ()#line:1024
                        break #line:1025
        except Exception as OO0OO0O0OO0OO0OO0 :#line:1027
            print (OO0OO0O0OO0OO0OO0 )#line:1028
def bundled_def ():#line:1030
    OOOO0O0OO0000OO0O =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return OOOO0O0OO0000OO0O [random .randint (0 ,len (OOOO0O0OO0000OO0O )-1 )]#line:1032
def version_of_the_validation ():#line:1036
    return str ((88 -56 )/10 )#line:1037
def sc2 ():#line:1039
    return "19319#$%^&*((*"#line:1040
def OO00OO0OO0OO00OO00o0 ():#line:1042
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1043
def get_ip ():#line:1045
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:1046
def gitee_validation ():#line:1048
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1049
def gitee_edition ():#line:1051
    try :#line:1052
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1053
    except :#line:1054
        sys .exit (0 )#line:1055
def O000OO000O0O00OOO00 ():#line:1060
    try :#line:1061
        OOO0OO0O0O000OOO0 =gitee_edition ()#line:1062
        if version_of_the_validation ()<OOO0OO0O0O000OOO0 ['CityEarth']['edition']:#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO0O0O000OOO0["CityEarth"]["edition"]}   ❌')#line:1064
            print (f'更新内容=>>{OOO0OO0O0O000OOO0["CityEarth"]["content"]}   🎉')#line:1065
        else :#line:1066
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO0O0O000OOO0["CityEarth"]["edition"]}   ✅')#line:1067
            print (f'更新内容=>> {OOO0OO0O0O000OOO0["CityEarth"]["content"]}   🎉')#line:1068
    except Exception as OOO0O0OOOO0000O00 :#line:1069
        print (OOO0O0OOOO0000O00 )#line:1070
def sc3 ():#line:1072
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1073
if __name__ =='__main__':#line:1077
    start ()#line:1078
