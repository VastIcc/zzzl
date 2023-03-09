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
        update_the_validation ()#line:9
        print (f'你的卡密是：{gethostname_new()}')#line:10
        asdfgh ()#line:11
        O00OO0O00O0OO0OO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O00OO0O00O0OO0OO0)}个账号==========")#line:13
        for O0O0O0O0000O00O00 in O00OO0O00O0OO0OO0 :#line:14
            O000O0OO000O00O0O =[]#line:15
            print (f"------------正在执行第{O00OO0O00O0OO0OO0.index(O0O0O0O0000O00O00) + 1}个账号------------")#line:16
            OOO0OOOOOO0OOO0O0 =CityEarth (O0O0O0O0000O00O00 ,O000O0OO000O00O0O ,O00OO0O00O0OO0OO0 .index (O0O0O0O0000O00O00 ))#line:17
            def OOOOO0O00O0O0000O ():#line:19
                if OOO0OOOOOO0OOO0O0 .base_info ():#line:21
                    OOO0OOOOOO0OOO0O0 .sealing ()#line:23
                    OOO0OOOOOO0OOO0O0 .invitenum ()#line:25
                    OOO0OOOOOO0OOO0O0 .game_map ()#line:27
                    OOO0OOOOOO0OOO0O0 .friends_invitation ()#line:29
                    OOO0OOOOOO0OOO0O0 .energy ()#line:31
                    OOO0OOOOOO0OOO0O0 .add_clover ()#line:33
                    OOO0OOOOOO0OOO0O0 .propsraffle ()#line:35
                    OOO0OOOOOO0OOO0O0 .synthetic ()#line:37
                    OOO0OOOOOO0OOO0O0 .crops_illustrated ()#line:39
                    OOO0OOOOOO0OOO0O0 .give_gold ()#line:41
                    OOO0OOOOOO0OOO0O0 .withdraw ()#line:43
            O0O0O00OO0OO00O0O =threading .Thread (target =OOOOO0O00O0O0000O )#line:45
            O0O0O00OO0OO00O0O .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        OOO00O0OOO00OOO00 =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO00O0OOO00OOO00 +' ')#line:51
    except Exception as OOO00OOOO0OOOO0O0 :#line:52
        print (OOO00OOOO0OOOO0O0 )#line:53
def give_gold (OO00OOO0O0000O0OO ,O0000OO000OO00000 ):#line:56
        try :#line:57
            OOO00O0000000OO0O =f'_doneeNo={OO00OOO0O0000O0OO}&quantity={int(O0000OO000OO00000)}_{timi_new()}'#line:58
            OOO0OOO00OO0O00OO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOO00O0000000OO0O ),'signstring':OOO00O0000000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            O000O00OOOOOO0O00 ={"quantity":int (O0000OO000OO00000 ),"doneeNo":OO00OOO0O0000O0OO }#line:73
            OOOO0O0OO00OO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOO00OO0O00OO ,data =O000O00OOOOOO0O00 ).json ()#line:74
            if 'status'in OOOO0O0OO00OO0000 :#line:76
                if OOOO0O0OO00OO0000 ['status']==200 :#line:77
                    if OOOO0O0OO00OO0000 ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(O0000OO000OO00000)}种子给{OO00OOO0O0000O0OO}成功')#line:79
                        return True #line:80
                if OOOO0O0OO00OO0000 ['status']==401 :#line:81
                    print (f'【赠送种子】:{OOOO0O0OO00OO0000["message"]}')#line:82
                    return False #line:83
                if OOOO0O0OO00OO0000 ['status']==500 :#line:84
                    print (f'【赠送种子】:{OOOO0O0OO00OO0000["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as OOO0000OO00O0O0O0 :#line:88
            print (OOO0000OO00O0O0O0 )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (O0O000O00OO0O00OO ):#line:94
    OOOOO0O00O000000O =hashlib .md5 (O0O000O00OO0O00OO .encode ()).hexdigest ()#line:95
    OO0O00O0O0OO0OO00 =sc1 ()#line:96
    OOOOO00O000O0O000 =sc2 ()#line:97
    O000OO0O000O00000 =sc3 ()#line:98
    O0OO00O0O00O00OO0 =OO0O00O0O0OO0OO00 +OOOOO0O00O000000O +OOOOO00O000O0O000 +O000OO0O000O00000 #line:99
    O0000OO0OO0OO0OO0 =hashlib .md5 (O0OO00O0O00O00OO0 .encode ()).hexdigest ()#line:100
    return O0000OO0OO0OO0OO0 #line:101
def format_msg ():#line:105
    O0O0OOOO000OO0O0O =""#line:106
    for O0OO0OO0O0O00OOOO in msg_list :#line:107
        O0O0OOOO000OO0O0O +=str (O0OO0OO0O0O00OOOO )+"\r\n"#line:108
    return O0O0OOOO000OO0O0O #line:109
def sc1 ():#line:111
    return "scsc%^&*"#line:112
def asdfgh ():#line:114
    if gethostname_new ()in gitee_validation ()['validation']:#line:115
        pass #line:116
    else :#line:117
        exit (1 )#line:118
def timi_new ():#line:120
    return str (int (time .time ()*1000 ))#line:121
json_path ="CityEarth_data.json"#line:124
json_path1 ="CityEarth_data.json"#line:125
dict ={}#line:126
def get_json_data (O000O0OO0O0O0OO00 ,OO0OOO0O00000OOO0 ,OO000O00OOO00O00O ,OO0O00OOOO000O0OO ):#line:128
    with open (O000O0OO0O0O0OO00 ,'rb')as O0O0OOOOOOO0OO0O0 :#line:130
        OO0000OO000OO0000 =json .load (O0O0OOOOOOO0OO0O0 )#line:131
        OO0000OO000OO0000 ['data'][OO0OOO0O00000OOO0 ][OO000O00OOO00O00O ]=OO0O00OOOO000O0OO #line:132
        OO0O0OOOOO000O00O =OO0000OO000OO0000 #line:133
    O0O0OOOOOOO0OO0O0 .close ()#line:134
    return OO0O0OOOOO000O00O #line:135
def write_json_data (O0OO0O0OO0O000OO0 ):#line:137
    with open (json_path1 ,'w')as O000000OOOOO000OO :#line:138
        json .dump (O0OO0O0OO0O000OO0 ,O000000OOOOO000OO )#line:139
    O000000OOOOO000OO .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (OO0OOO00OO000OO00 ,O000O000OOO0OO0OO ,OOOOO0O00O000O00O ,O00OO0OOOO0O0O00O ):#line:145
        try :#line:146
            OO0OOO00OO000OO00 .msg =OOOOO0O00O000O00O #line:147
            OO0OOO00OO000OO00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            OO0OOO00OO000OO00 .token =O000O000OOO0OO0OO ['authorization']#line:149
            OO0OOO00OO000OO00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            OO0OOO00OO000OO00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            OO0OOO00OO000OO00 .elephant_user =O000O000OOO0OO0OO ['elephant_user']#line:152
            OO0OOO00OO000OO00 .elephant_pswd =O000O000OOO0OO0OO ['elephant_pswd']#line:153
            OO0OOO00OO000OO00 .elephant_Task_ID =O000O000OOO0OO0OO ['elephant_Task_ID']#line:154
            OO0OOO00OO000OO00 .len_new =O00OO0OOOO0O0O00O #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (O0OOO00O0OOOOO00O ):#line:160
        try :#line:161
            O0OOO00O0OOOOO00O .watched_ad ()#line:163
            OO000OO00000OO00O =f'__{timi_new()}'#line:164
            OO00000O0OO000000 ={'source':'scsc','authorization':O0OOO00O0OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00000OO00O ),'signstring':OO000OO00000OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            OOOOOO0O0OOO0O0O0 =requests .request ('get',f'{host}/user',headers =OO00000O0OO000000 ).json ()#line:176
            if 'status'in OOOOOO0O0OOO0O0O0 :#line:178
                if OOOOOO0O0OOO0O0O0 ['status']==200 :#line:179
                    O0OO0OOOO0O0000OO =OOOOOO0O0OOO0O0O0 ['data']['nickname']#line:180
                    OO0OO0O00OOOOO00O =OOOOOO0O0OOO0O0O0 ['data']['inner_id']#line:181
                    OOOOO0000O000000O =OOOOOO0O0OOO0O0O0 ['data']['assets']['gold']#line:182
                    OOOOOOO00OO0OOO0O =OOOOOO0O0OOO0O0O0 ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{O0OO0OOOO0O0000OO[:5]}丨ID:{OO0OO0O00OOOOO00O}丨等级:{OOOOOOO00OO0OOO0O}丨金种子:{str(OOOOO0000O000000O).split(".")[0]}')#line:184
                if OOOOOO0O0OOO0O0O0 ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if O0OOO00O0OOOOO00O .elephant_user =='f':#line:187
                        return False #line:188
                    OOO0OOO00OOOO0OO0 =Invalid_login .addtask (elephant_user =O0OOO00O0OOOOO00O .elephant_user ,elephant_pswd =O0OOO00O0OOOOO00O .elephant_pswd ,elephant_Task_ID =O0OOO00O0OOOOO00O .elephant_Task_ID )#line:189
                    OOO000O00OO00O0OO =get_json_data (json_path ,O0OOO00O0OOOOO00O .len_new ,'authorization',OOO0OOO00OOOO0OO0 )#line:190
                    if write_json_data (OOO000O00OO00O0OO ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if OOOOOO0O0OOO0O0O0 ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as OOO000OO00OOOO00O :#line:197
            print (OOO000OO00OOOO00O )#line:198
    def sealing (OOOOOOO0O0OO0OO0O ):#line:201
        try :#line:202
            OO0000000OO0O00OO =f'__{timi_new()}'#line:203
            O0OOO0OO0O0O00OO0 ={'source':'scsc','authorization':OOOOOOO0O0OO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000000OO0O00OO ),'signstring':OO0000000OO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OOO0OO0O0O00OO0 )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =O0OOO0OO0O0O00OO0 )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OOO0OO0O0O00OO0 )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OOO0OO0O0O00OO0 )#line:218
            requests .request ('get',f'{host}/user',headers =O0OOO0OO0O0O00OO0 )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OOO0OO0O0O00OO0 )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OOO0OO0O0O00OO0 )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OOO0OO0O0O00OO0 )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =O0OOO0OO0O0O00OO0 )#line:223
            requests .request ('get',f'{host}/assets',headers =O0OOO0OO0O0O00OO0 )#line:224
        except Exception as OO000OO0O0O0000OO :#line:225
            print (OO000OO0O0O0000OO )#line:226
    def withdraw (O0OOO0OO00OO0OOOO ):#line:230
        O0000O00OO0OO000O =f'__{timi_new()}'#line:231
        O0O0OO0O000000OO0 ={'source':'scsc','authorization':O0OOO0OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0OO000O ),'signstring':O0000O00OO0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        OOO0OO0O0OO00O00O =requests .request ('get',f'{host}/assets',headers =O0O0OO0O000000OO0 ).json ()#line:243
        if 'status'in OOO0OO0O0OO00O00O :#line:245
            if OOO0OO0O0OO00O00O ['status']==200 :#line:246
                OOOOOO0OO00O000O0 =OOO0OO0O0OO00O00O ['data']['cash']#line:247
                if float (OOOOOO0OO00O000O0 )>20 :#line:248
                    O0000O00OO0OO000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    O0O0OO0O000000OO0 ={'authorization':O0OOO0OO00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0OO000O ),'signstring':O0000O00OO0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    O000OO0O0OO0O0OOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    OOO0OO00OOOOO00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO0O000000OO0 ,data =O000OO0O0OO0O0OOO ).json ()#line:262
                    print (OOO0OO00OOOOO00O0 )#line:263
    def invitenum (O0O0OO00OO0O0OO00 ):#line:266
        OOO0OOOOO0O0OOO0O =f'__{timi_new()}'#line:267
        O0000O0OO0O0O00O0 ={'source':'scsc','authorization':O0O0OO00OO0O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O0OOO0O ),'signstring':OOO0OOOOO0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        OOOOOO000O00O00OO =requests .request ('get',f'{host}/invite/invitenum',headers =O0000O0OO0O0O00O0 ).json ()#line:279
        if 'status'in OOOOOO000O00O00OO :#line:281
            if OOOOOO000O00O00OO ['status']==200 :#line:282
                OOO00O00O0O000000 =OOOOOO000O00O00OO ['data']['invited_count']#line:283
                OO0O00000OOOO0000 =OOOOOO000O00O00OO ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{OOO00O00O0O000000}丨间邀好友:{OO0O00000OOOO0000}')#line:285
    def game_map (OOO0O00O00O0OO0O0 ):#line:288
        try :#line:289
            O00O00O0O0000O0O0 =f'__{timi_new()}'#line:290
            OOO0O0OO00O00OO00 ={'source':'scsc','authorization':OOO0O00O00O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000O0O0 ),'signstring':O00O00O0O0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0OOOO00O00OOOOOO =requests .request ('get',f'{host}/game/map',headers =OOO0O0OO00O00OO00 ).json ()#line:302
            if 'status'in O0OOOO00O00OOOOOO :#line:304
                if O0OOOO00O00OOOOOO ['status']==200 :#line:305
                    for OO0OO0OO00000OOOO in O0OOOO00O00OOOOOO ['data']['list'][0 ]['crops']:#line:306
                        O0OO000O000OOOO0O =OO0OO0OO00000OOOO ['level']#line:308
                        if O0OO000O000OOOO0O ==41 :#line:309
                            OO000O0OOOO0O000O =OO0OO0OO00000OOOO ['crop_name']#line:310
                            O000O0O000OO00O0O =OO0OO0OO00000OOOO ['count']#line:311
                            if O000O0O000OO00O0O >0 :#line:312
                                print (f'【农业资产】:{OO000O0OOOO0O000O}丨数量:{O000O0O000OO00O0O}')#line:313
        except Exception as OOOO00OO0O0O0OO0O :#line:314
            print (OOOO00OO0O0O0OO0O )#line:315
    def give_gold (OOO0O00O0O0OOO000 ):#line:318
        try :#line:319
            OO00O0O0OOO000000 =f'__{timi_new()}'#line:320
            O0OO0OO0000OOOO0O ={'source':'scsc','authorization':OOO0O00O0O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OOO000000 ),'signstring':OO00O0O0OOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            OO0OO0000OOOO00OO =requests .request ('get',f'{host}/user',headers =O0OO0OO0000OOOO0O ).json ()#line:332
            if 'status'in OO0OO0000OOOO00OO :#line:333
                if OO0OO0000OOOO00OO ['status']==200 :#line:334
                    if float (OOO0O00O0O0OOO000 .doneeNo )!=0 :#line:335
                        O00O0O00OOOO0O0O0 =OO0OO0000OOOO00OO ['data']['assets']['gold']#line:336
                        if float (O00O0O00OOOO0O0O0 )>float (OOO0O00O0O0OOO000 .innerId ):#line:337
                            OOOO000000OO0O0O0 =int (float (O00O0O00OOOO0O0O0 )/1.1 )#line:338
                            OO00O0O0OOO000000 =f'_doneeNo={OOO0O00O0O0OOO000.doneeNo}&quantity={OOOO000000OO0O0O0}_{timi_new()}'#line:339
                            O0OO0OO0000OOOO0O ={'source':'scsc','authorization':OOO0O00O0O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OOO000000 ),'signstring':OO00O0O0OOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O00OO0O000O00O0OO ={"quantity":OOOO000000OO0O0O0 ,"doneeNo":OOO0O00O0O0OOO000 .doneeNo }#line:354
                            O00O00OO000OO0OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OO0OO0000OOOO0O ,data =O00OO0O000O00O0OO ).json ()#line:355
                            if 'status'in O00O00OO000OO0OO0 :#line:357
                                if O00O00OO000OO0OO0 ['status']==200 :#line:358
                                    if O00O00OO000OO0OO0 ['data']:#line:359
                                        print (f'【赠送种子】:赠送{OOOO000000OO0O0O0}种子给{OOO0O00O0O0OOO000.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OO00OO00O00OOOO0O :#line:363
            print (OO00OO00O00OOOO0O )#line:364
    def invitation (OO0OOO000OO00OO00 ):#line:366
        try :#line:367
            _O0000O0O00O00OO00 =float (bundled_def ())/4 #line:368
            O0OO0O000O00OO0OO =f'_innerId={int(_O0000O0O00O00OO00)}_{timi_new()}'#line:369
            OO0OOOOO00O000OOO ={'source':'scsc','authorization':OO0OOO000OO00OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O000O00OO0OO ),'signstring':O0OO0O000O00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            OOOOOOO0OO00O00O0 ={"innerId":int (_O0000O0O00O00OO00 )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOOOO00O000OOO ,data =OOOOOOO0OO00O00O0 )#line:382
        except Exception as OO00OO00OOO0O00OO :#line:383
            print (OO00OO00OOO0O00OO )#line:384
    def winning_rewards (OO00O0OO0O0OO00O0 ):#line:387
        try :#line:388
            O0OO0OOO00O00OOO0 =f'__{timi_new()}'#line:389
            O0OO00OO000O0OO00 ={'source':'scsc','authorization':OO00O0OO0O0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO00O00OOO0 ),'signstring':O0OO0OOO00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            OO0O00O0O0OOOOOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO00OO000O0OO00 ).json ()#line:401
            if 'status'in OO0O00O0O0OOOOOO0 :#line:403
                if OO0O00O0O0OOOOOO0 ['status']==200 :#line:404
                    if OO0O00O0O0OOOOOO0 ['data']['amount']:#line:405
                        OO00OO00OOO00000O =OO0O00O0O0OOOOOO0 ['data']['amount']['gold']#line:406
                        return OO00OO00OOO00000O #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as O000O0OOO0O0OOOOO :#line:410
            print (O000O0OOO0O0OOOOO )#line:411
    def certification (O00OOOOO0O0OO0O0O ):#line:414
        try :#line:415
            O00OOO0000O0000OO =f'__{timi_new()}'#line:416
            O0OO000OO00O0OOO0 ={'source':'scsc','authorization':O00OOOOO0O0OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0000O0000OO ),'signstring':O00OOO0000O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            OO00O00O00OOO0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO000OO00O0OOO0 ).json ()#line:428
            if 'status'in OO00O00O00OOO0O00 :#line:430
                if OO00O00O00OOO0O00 ['status']==200 :#line:431
                    if OO00O00O00OOO0O00 ['data']['result']:#line:432
                        OOOO0O0O0O0O0O0O0 =OO00O00O00OOO0O00 ['data']['nick_name']#line:433
                        return OOOO0O0O0O0O0O0O0 #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as O0000OOOO00O0OO0O :#line:437
            print (O0000OOOO00O0OO0O )#line:438
    def crops_illustrated (OO0OOO000O0000000 ):#line:441
        try :#line:442
            O0O0OO0000OOOO0OO =f'__{timi_new()}'#line:443
            OOO000OOOO0O00000 ={'source':'scsc','authorization':OO0OOO000O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0000OOOO0OO ),'signstring':O0O0OO0000OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            OOO0O00O000O0O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO000OOOO0O00000 ).json ()#line:455
            if 'status'in OOO0O00O000O0O0O0 :#line:457
                if OOO0O00O000O0O0O0 ['status']==200 :#line:458
                    OOOO00O0OO000OOOO =OOO0O00O000O0O0O0 ['data'][0 ]['crops']#line:459
                    for O0O0O0000OOOOOOO0 in OOOO00O0OO000OOOO :#line:460
                        if O0O0O0000OOOOOOO0 ['ill_clover_award']:#line:461
                            if float (O0O0O0000OOOOOOO0 ['ill_clover_award'])>1 :#line:462
                                if O0O0O0000OOOOOOO0 ['is_finish']:#line:463
                                    if not O0O0O0000OOOOOOO0 ['is_getit']:#line:464
                                        if OO0OOO000O0000000 .certification ()!='未实名':#line:465
                                            O0O0OO0000OOOO0OO =f'_award_level={O0O0O0000OOOOOOO0["level"]}_{timi_new()}'#line:466
                                            OOO000OOOO0O00000 ={'source':'scsc','authorization':OO0OOO000O0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0000OOOO0OO ),'signstring':O0O0OO0000OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            O0OOO00OO00O0O0O0 ={"award_level":O0O0O0000OOOOOOO0 ['level']}#line:478
                                            OO0O00OO0O0OO0O00 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO000OOOO0O00000 ,json =O0OOO00OO00O0O0O0 ).json ()#line:480
                                            if 'status'in OO0O00OO0O0OO0O00 :#line:481
                                                if OO0O00OO0O0OO0O00 ['status']==200 :#line:482
                                                    O0OO00O0O000OOOOO =OO0O00OO0O0OO0O00 ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{O0O0O0000OOOOOOO0["crop_name"]}成就丨奖励{O0OO00O0O000OOOOO}☘️')#line:485
                                                if OO0O00OO0O0OO0O00 ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{OO0O00OO0O0OO0O00["message"]}')#line:487
        except Exception as O0OOOOOO0OO000O00 :#line:488
            print (O0OOOOOO0OO000O00 )#line:489
    def watched_ad (OO0OO0O0OOOO0O00O ):#line:492
        try :#line:493
            OO000OO00000O00OO =f'__{timi_new()}'#line:494
            OOO000OO0OO000O00 ={'source':'scsc','authorization':OO0OO0O0OOOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00000O00OO ),'signstring':OO000OO00000O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            O0O0O0000O00OO00O =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0OO000O00 ).json ()#line:506
            if 'status'in O0O0O0000O00OO00O :#line:508
                if O0O0O0000O00OO00O ['status']==200 :#line:509
                    if 'offlineInfo'in O0O0O0000O00OO00O ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        O0OO00OOOO00OOOOO =O0O0O0000O00OO00O ['data']['offlineInfo']['off_minute']#line:512
                        OO0O00OOO00O0OO00 =float (O0O0O0000O00OO00O ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO000OO0OO000O00 ).json ()#line:515
                        time .sleep (2 )#line:516
                        OO0O0O0O00O0OO000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO000OO0OO000O00 ).json ()#line:517
                        if 'status'in OO0O0O0O00O0OO000 :#line:519
                            if OO0O0O0O00O0OO000 ['status']==200 :#line:520
                                O00O0OO00O00O0OOO =float (OO0O0O0O00O0OO000 ['data']['silver'])/1000000000000 #line:521
                                O0OOOOO0O00OOO000 =str (O00O0OO00O00O0OOO -OO0O00OOO00O0OO00 )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{O0OO00OOOO00OOOOO}分钟奖励🌱数量:{O0OOOOO0O00OOO000}t粒')#line:523
        except Exception as OO0OO0000O000O000 :#line:524
            print (OO0OO0000O000O000 )#line:525
    def user_ad (O00OO0O00000O00OO ):#line:528
        try :#line:529
            O0O0OOOO00OO00OOO =f'__{timi_new()}'#line:530
            OOOOO0OO00OO0000O ={'source':'scsc','authorization':O00OO0O00000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO00OO00OOO ),'signstring':O0O0OOOO00OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            OO000OOOO0000OO00 =requests .request ('get',f'{host}/user/ad',headers =OOOOO0OO00OO0000O ).json ()#line:542
            if 'status'in OO000OOOO0000OO00 :#line:544
                if OO000OOOO0000OO00 ['status']==200 :#line:545
                    O00O0000O0O000OO0 =OO000OOOO0000OO00 ['data']['max_time']#line:546
                    OOO0O000OO00OOO00 =OO000OOOO0000OO00 ['data']['watch_time']#line:547
                    OO0O00OOOO00OOO00 =OO000OOOO0000OO00 ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{OO0O00OOOO00OOO00 + O00O0000O0O000OO0 - OOO0O000OO00OOO00}次丨好友提供:{OO0O00OOOO00OOO00}次')#line:549
                    if OO0O00OOOO00OOO00 +O00O0000O0O000OO0 -OOO0O000OO00OOO00 >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        OO0OOO0OO00O0O00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOOOO0OO00OO0000O ).json ()#line:552
                        if 'status'in OO0OOO0OO00O0O00O :#line:554
                            if OO0OOO0OO00O0O00O ['status']==200 :#line:555
                                OO00O000O00O0O0OO =float (OO0OOO0OO00O0O00O ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(OO00O000O00O0O0OO)}t粒')#line:557
                                return True #line:558
                            if OO0OOO0OO00O0O00O ['status']==500 :#line:559
                                OOO0O000OO00000OO =OO0OOO0OO00O0O00O ['message']#line:560
                                print (f'【获取种子】:{OOO0O000OO00000OO}')#line:561
                                return False #line:562
        except Exception as OOO0000OO00000O00 :#line:563
            print (OOO0000OO00000O00 )#line:564
    def synthetic (O0OO00OO00OOO0OO0 ):#line:567
        global id ,g #line:568
        try :#line:569
            O0O0OOO0O00OOO00O =O0OO00OO00OOO0OO0 .level_new ()#line:570
            OOO00O0OOO000O000 =random .randint (9 ,11 )#line:571
            O000OO0O0O0OO0OO0 =f'_site=8&targetSite={OOO00O0OOO000O000}_{timi_new()}'#line:572
            O000O000OOO0000OO ={'source':'scsc','authorization':O0OO00OO00OOO0OO0 .token ,'timestamp':timi_new (),'sign':sign (O000OO0O0O0OO0OO0 ),'signstring':O000OO0O0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            OOOO0O0O0OO0O0OO0 ={"site":int (8 ),"targetSite":int (OOO00O0OOO000O000 )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =O000O000OOO0000OO ,json =OOOO0O0O0OO0O0OO0 )#line:585
            while True :#line:586
                O0O0O00O00OOO0OO0 =f'__{timi_new()}'#line:587
                OOOO0OO0O00O0O0OO ={'source':'scsc','authorization':O0OO00OO00OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O00OOO0OO0 ),'signstring':O0O0O00O00OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                O0O000O00O000O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OO0O00O0O0OO ).json ()#line:599
                if 'status'in O0O000O00O000O0OO :#line:601
                    if O0O000O00O000O0OO ['status']==200 :#line:602
                        OO0O00OO0OOO00O00 =O0O000O00O000O0OO ['data']['cropList']#line:603
                        O000O0000O00O0000 =O0O000O00O000O0OO ['data']['gameCoreDataDBid']#line:604
                        OOO00000O0000000O =float (O0O000O00O000O0OO ['data']['silver'])/1000000000000 #line:605
                        O0OO0O0000OOOOOO0 =0 #line:610
                        for OOOOOOO0000OO0OO0 in OO0O00OO0OOO00O00 :#line:611
                            if not OOOOOOO0000OO0OO0 :#line:612
                                OO0O0O0OO00OOOO00 =f'_crop_id={O000O0000O00O0000}&site={O0OO0O0000OOOOOO0}_{O0OO00OO00OOO0OO0.time}'#line:613
                                OOOOOOOOO0OOOOOOO ={'source':'scsc','authorization':O0OO00OO00OOO0OO0 .token ,'timestamp':O0OO00OO00OOO0OO0 .time ,'sign':sign (OO0O0O0OO00OOOO00 ),'signstring':OO0O0O0OO00OOOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                OO0O00000O000OO0O ={"site":O0OO0O0000OOOOOO0 ,"crop_id":O000O0000O00O0000 }#line:624
                                OO0OOOO00OO00OO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOOOOO0OOOOOOO ,data =OO0O00000O000OO0O ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in OO0OOOO00OO00OO00 :#line:628
                                    if OO0OOOO00OO00OO00 ['status']==200 :#line:629
                                        if OO0OOOO00OO00OO00 ['message']=='种子数量不足':#line:630
                                            O0O0OOO0O00OOO00O =O0OO00OO00OOO0OO0 .level_new ()#line:631
                                            print (f'【种植合成】:{OO0OOOO00OO00OO00["message"]}')#line:632
                                            if not O0OO00OO00OOO0OO0 .user_ad ():#line:633
                                                return False #line:634
                                    if OO0OOOO00OO00OO00 ['status']==500 :#line:635
                                        print (f'【种植合成】:{OO0OOOO00OO00OO00["message"]}')#line:636
                                        return False #line:637
                            O0OO0O0000OOOOOO0 +=1 #line:638
                        O00000OOO0O000OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OO0O00O0O0OO ).json ()#line:639
                        OO0OO00000O0O00O0 =O00000OOO0O000OOO ['data']['cropList']#line:640
                        OO0O0OOOO0O000O00 =False #line:641
                        for OOOOOOO0000OO0OO0 in range (12 ):#line:642
                            id =OO0OO00000O0O00O0 [OOOOOOO0000OO0OO0 ]['level']#line:643
                            if float (O0O0OOO0O00OOO00O )-float (id )>9 :#line:644
                                O00OOO0000O0OO000 =f'_site={OOOOOOO0000OO0OO0}_{timi_new()}'#line:645
                                O000O00000OOOO0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO00OO00OOO0OO0 .token ,'timestamp':timi_new (),'sign':sign (O00OOO0000O0OO000 ),'signstring':O00OOO0000O0OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O0000O0OO00OOO0O0 ={"site":OOOOOOO0000OO0OO0 }#line:657
                                OO0O0O0000OOO0O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O00000OOOO0OO ,data =O0000O0OO00OOO0O0 ).json ()#line:659
                                if 'status'in OO0O0O0000OOO0O0O :#line:660
                                    if OO0O0O0000OOO0O0O ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for O00O00OO0000OO00O in range (11 ):#line:664
                                    OO0O00O000OOOOOOO =O00O00OO0000OO00O +1 #line:665
                                    g =OO0OO00000O0O00O0 [OO0O00O000OOOOOOO ]['level']#line:666
                                    if id ==g :#line:667
                                        O00O0O00OO0O0OO0O =O00O00OO0000OO00O +2 #line:668
                                        if O00O0O00OO0O0OO0O !=OOOOOOO0000OO0OO0 +1 :#line:669
                                            O000O0OOOO00O00O0 =OOOOOOO0000OO0OO0 +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            O000OO0O0O0OO0OO0 =f'_site={O000O0OOOO00O00O0 - 1}&targetSite={O00O0O00OO0O0OO0O - 1}_{timi_new()}'#line:673
                                            O000O000OOO0000OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OO00OO00OOO0OO0 .token ,'timestamp':timi_new (),'sign':sign (O000OO0O0O0OO0OO0 ),'signstring':O000OO0O0O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            OO0O0O0O0O000OO0O ={"site":int (O000O0OOOO00O00O0 -1 ),"targetSite":int (O00O0O00OO0O0OO0O -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =O000O000OOO0000OO ,json =OO0O0O0O0O000OO0O )#line:692
                                            OO0O0OOOO0O000O00 =True #line:694
                                    if OO0O0OOOO0O000O00 :#line:695
                                        break #line:696
                                if OO0O0OOOO0O000O00 :#line:697
                                    break #line:698
        except :#line:699
            O0OO00OO00OOO0OO0 .synthetic ()#line:700
    def level_new (O00OO0OOO0O0000O0 ):#line:703
        try :#line:704
            O0OO0OOO0OOO0O000 =f'__{timi_new()}'#line:705
            OO0O0O0O00O000OOO ={'source':'scsc','authorization':O00OO0OOO0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOO0OOO0O000 ),'signstring':O0OO0OOO0OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OOOO000O00000OOO0 =requests .request ('get',f'{host}/user',headers =OO0O0O0O00O000OOO ).json ()#line:717
            if 'status'in OOOO000O00000OOO0 :#line:718
                if OOOO000O00000OOO0 ['status']==200 :#line:719
                    return float (OOOO000O00000OOO0 ['data']['level'])#line:720
        except Exception as O0O00OOO00OOO0000 :#line:721
            print (O0O00OOO00OOO0000 )#line:722
    def propsraffle (O0O000O0000000OO0 ):#line:725
        try :#line:726
            while True :#line:727
                O000O0O0OO00OO0O0 =f'__{timi_new()}'#line:728
                O0OO0OO0OOO000O00 ={'source':'scsc','authorization':O0O000O0000000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O0OO00OO0O0 ),'signstring':O000O0O0OO00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                OO0000O0O00OO00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO0OO0OOO000O00 ).json ()#line:740
                if 'status'in OO0000O0O00OO00O0 :#line:742
                    if OO0000O0O00OO00O0 ['status']==200 :#line:743
                        OO00O0000O0O00OO0 =OO0000O0O00OO00O0 ['data']['rows']#line:744
                        OO000O0O0O0000O0O =OO0000O0O00OO00O0 ['data']['vstate']#line:745
                        if OO00O0000O0O00OO0 ==5 or OO00O0000O0O00OO0 ==6 or OO00O0000O0O00OO0 ==7 :#line:746
                            OO00OO000O0O0OO00 =OO0000O0O00OO00O0 ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{OO00OO000O0O0OO00}')#line:748
                        if OO00O0000O0O00OO0 ==1 or OO00O0000O0O00OO0 ==2 or OO00O0000O0O00OO0 ==3 :#line:749
                            O00000OOOOOO0OOO0 =OO0000O0O00OO00O0 ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{O00000OOOOOO0OOO0}')#line:751
                        if OO00O0000O0O00OO0 ==4 or OO00O0000O0O00OO0 ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if OO00O0000O0O00OO0 =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as OO0000O000OO00O0O :#line:793
            print (OO0000O000OO00O0O )#line:794
    def friends_invitation (OOOOO000O000000O0 ):#line:797
        try :#line:798
            O0000O00OO0OOO0OO =f'__{timi_new()}'#line:799
            OO00000000OO0O0OO ={'source':'scsc','authorization':OOOOO000O000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OO0OOO0OO ),'signstring':O0000O00OO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            OOO000OO0O0O0O0OO =requests .request ('get',f'{host}/friends',headers =OO00000000OO0O0OO ).json ()#line:811
            if 'status'in OOO000OO0O0O0O0OO :#line:812
                if OOO000OO0O0O0O0OO ['status']==200 :#line:813
                    OOO00OO00OOOOOOO0 =OOO000OO0O0O0O0OO ['data']['myInviteter']#line:814
                    if OOO00OO00OOOOOOO0 :#line:815
                        OO0OO0OOOOOO0O0OO =OOO00OO00OOOOOOO0 ['user']['nickname']#line:816
                        O000OOOO00O00OO00 =OOOOO000O000000O0 .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{OO0OO0OOOOOO0O0OO}丨实名:{O000OOOO00O00OO00}')#line:818
                    else :#line:819
                        if OOOOO000O000000O0 .innerId !='0':#line:820
                            OOOOO000O000000O0 .invitation ()#line:821
        except Exception as OOOOO0O0OOOOOO00O :#line:822
            print (OOOOO0O0OOOOOO00O )#line:823
    def add_clover (O00OOOOOO00O0O000 ):#line:826
        global golden_seed #line:827
        try :#line:828
            O00O0OO00OOO0O0O0 =f'__{timi_new()}'#line:829
            O0O0OOO0O0OOOOOOO ={'source':'scsc','authorization':O00OOOOOO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00OOO0O0O0 ),'signstring':O00O0OO00OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            OO00OO0O0OOO0O0OO =requests .request ('get',f'{host}/assets/clovers',headers =O0O0OOO0O0OOOOOOO ).json ()#line:841
            if 'status'in OO00OO0O0OOO0O0OO :#line:843
                if OO00OO0O0OOO0O0OO ['status']==200 :#line:844
                    OO0OO0OOO0OO0OO0O =OO00OO0O0OOO0O0OO ['data']['clover']#line:845
                    O0O0O0OO0O0O0O000 =OO00OO0O0OOO0O0OO ['data']['used_clover']#line:846
                    OO0OO0OO0O00O0OOO =float (OO0OO0OOO0OO0OO0O )-float (O0O0O0OO0O0O0O000 )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O0OO0O0O0O000}')#line:848
                    if O00OOOOOO00O0O000 .certification ()!='未实名':#line:849
                        if OO0OO0OO0O00O0OOO >1 :#line:850
                            O00O0OO00OOO0O0O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO0OO0O00O0OOO)}_{timi_new()}'#line:851
                            O000OOOO00O0O0O00 ={'source':'scsc','authorization':O00OOOOOO00O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00OOO0O0O0 ),'signstring':O00O0OO00OOO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            O0OO00O000OO0OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO0OO0O00O0OOO )}#line:863
                            OOO00OO00OO000OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O000OOOO00O0O0O00 ,data =O0OO00O000OO0OO00 ).json ()#line:864
                            if 'status'in OOO00OO00OO000OO0 :#line:866
                                if OOO00OO00OO000OO0 ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{OOO00OO00OO000OO0["data"]}丨数量:{OO0OO0OO0O00O0OOO}')#line:868
                                if OOO00OO00OO000OO0 ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{OOO00OO00OO000OO0["message"]}')#line:870
            O00OO00O000OO0000 =requests .request ('get',f'{host}/lottery',headers =O0O0OOO0O0OOOOOOO ).json ()#line:871
            OO00OO0O0O000O0O0 =O00OOOOOO00O0O000 .winning_rewards ()#line:873
            if 'status'in O00OO00O000OO0000 :#line:874
                if O00OO00O000OO0000 ['status']==200 :#line:875
                    OO0O0OOOOO00OOO00 =O00OO00O000OO0000 ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (OO0O0OOOOO00OOO00 )#line:877
                    O0O0O0000O00O0000 =O00OO00O000OO0000 ['data'][1 ]['value']#line:878
                    O0O0OOO00O00000OO =O00OO00O000OO0000 ['data'][0 ]['join_number']#line:879
                    OOO00OO0000OOO00O =int (float (O00OO00O000OO0000 ['data'][0 ]['totalValue']))#line:880
                    OOOO0OO00OO000O00 =float (O0O0O0000O00O0000 /OOO00OO0000OOO00O )*10000 #line:881
                    OOO000000O0O0000O =OOO00OO0000OOO00O /O0O0OOO00O00000OO #line:882
                    print (f'【参与抽奖】:预计每天中{str(OO0O0OOOOO00OOO00)[:6]}颗金种子丨好友收益:{str(OO00OO0O0O000O0O0)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(OOOO0OO00OO000O00)[:6]}颗金种子丨☘️人均:{str(OOO000000O0O0000O)[:7]}️')#line:884
        except Exception as OO0O0OOO0O000OOOO :#line:885
            print (OO0O0OOO0O000OOOO )#line:886
    def energy (O00000OOO0000O0OO ):#line:890
        try :#line:891
            while True :#line:892
                O0OOO0000OOOO00OO =f'__{timi_new()}'#line:893
                OOO00000000O0O000 ={'source':'scsc','authorization':O00000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0000OOOO00OO ),'signstring':O0OOO0000OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                OO000O00O0O000000 =requests .request ('get',f'{host}/energy/general',headers =OOO00000000O0O000 ).json ()#line:905
                if 'status'in OO000O00O0O000000 :#line:907
                    if OO000O00O0O000000 ['status']==200 :#line:908
                        O0O00OOO0000O0OOO =OO000O00O0O000000 ['data']['ordinary_water']#line:909
                        OO0O000O0000OOO00 =OO000O00O0O000000 ['data']['ordinary_fertilizer']#line:910
                        O0O0O0OOO0OO00000 =OO000O00O0O000000 ['data']['videoStatus']#line:911
                        OOO0O0O0O0O0O000O =OO000O00O0O000000 ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(OO0O000O0000OOO00).split(".")[0]}丨水滴:{str(O0O00OOO0000O0OOO).split(".")[0]}')#line:913
                        if float (OO0O000O0000OOO00 )<96 :#line:914
                            if O0O0O0OOO0OO00000 :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                OOOO0000OOOO0000O =99 -float (OO0O000O0000OOO00 )#line:917
                                OO00O0000O0O0O0O0 ={"fertilizer":str (OOOO0000OOOO0000O ).split ('.')[0 ]}#line:918
                                O0O00000OOOOOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00000000O0O000 ).json ()#line:919
                                if 'status'in O0O00000OOOOOOOO0 :#line:921
                                    if O0O00000OOOOOOOO0 ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00000OOOOOOOO0["message"]}')#line:923
                                    if O0O00000OOOOOOOO0 ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00000OOOOOOOO0["message"]}')#line:925
                                        break #line:926
                                if float (OO0O000O0000OOO00 )<78 :#line:928
                                    OOOO0000OOOO0000O =80 -float (OO0O000O0000OOO00 )#line:929
                                    OO0OO00O000O0OOOO =f'_fertilizer={int(OOOO0000OOOO0000O)}_{timi_new()}'#line:930
                                    OO00O0OO0O0O000OO ={'source':'scsc','authorization':O00000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00O000O0OOOO ),'signstring':OO0OO00O000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    OO0O0000OOO00O00O ={"fertilizer":int (OOOO0000OOOO0000O )}#line:942
                                    O00OO0OO0000O0OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00O0OO0O0O000OO ,data =OO0O0000OOO00O00O ).json ()#line:944
                                    if 'status'in O00OO0OO0000O0OO0 :#line:946
                                        if O00OO0OO0000O0OO0 ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{O00OO0OO0000O0OO0["message"]}丨数量:{int(OOOO0000OOOO0000O)}')#line:948
                                        if O00OO0OO0000O0OO0 ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{O00OO0OO0000O0OO0["message"]}丨数量:{int(OOOO0000OOOO0000O)}')#line:950
                                            OOO0O00OOO00OO000 =O00OO0OO0000O0OO0 ["message"].split ('-')[1 ]#line:951
                                            OOOOOOO0OO00O00OO =f'__{timi_new()}'#line:952
                                            OOO0OOO0OO000000O ={'source':'scsc','authorization':O00000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OO00O00OO ),'signstring':OOOOOOO0OO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            O0OO0OO00O0O0O0O0 =requests .request ('get',f'{host}/user',headers =OOO0OOO0OO000000O ).json ()#line:964
                                            if 'status'in O0OO0OO00O0O0O0O0 :#line:965
                                                if O0OO0OO00O0O0O0O0 ['status']==200 :#line:966
                                                    O0OO0OOOOO0OOO0OO =O0OO0OO00O0O0O0O0 ['data']['inner_id']#line:967
                                                    if give_gold (O0OO0OOOOO0OOO0OO ,float (OOO0O00OOO00OO000 )+1 ):#line:968
                                                        O00000OOO0000O0OO .energy ()#line:969
                        if float (O0O00OOO0000O0OOO )<880 :#line:970
                            if OOO0O0O0O0O0O000O :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                OOO0OO0O0OOO00OOO =999 -float (O0O00OOO0000O0OOO )#line:973
                                OO00O00OOO000O0O0 ={"water":str (OOO0OO0O0OOO00OOO ).split ('.')[0 ]}#line:974
                                OO0OOOOOO00O00O0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00000000O0O000 ).json ()#line:975
                                if 'status'in OO0OOOOOO00O00O0O :#line:977
                                    if OO0OOOOOO00O00O0O ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOOOO00O00O0O["message"]}')#line:979
                                    if OO0OOOOOO00O00O0O ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OOOOOO00O00O0O["message"]}')#line:981
                                        break #line:982
                                if float (O0O00OOO0000O0OOO )<780 :#line:983
                                    OOO0OO0O0OOO00OOO =800 -float (O0O00OOO0000O0OOO )#line:984
                                    OOO00O0O00O0OOO0O =f'_water={int(OOO0OO0O0OOO00OOO)}_{timi_new()}'#line:985
                                    O000OOO00000O000O ={'source':'scsc','authorization':O00000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O00O0OOO0O ),'signstring':OOO00O0O00O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    O0000OOO0000O0O00 ={"water":int (OOO0OO0O0OOO00OOO )}#line:997
                                    OOO0O0OO0OO00000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000OOO00000O000O ,data =O0000OOO0000O0O00 ).json ()#line:999
                                    if 'status'in OOO0O0OO0OO00000O :#line:1001
                                        if OOO0O0OO0OO00000O ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{OOO0O0OO0OO00000O["message"]}丨数量:{int(OOO0OO0O0OOO00OOO)}')#line:1003
                                        if OOO0O0OO0OO00000O ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{OOO0O0OO0OO00000O["message"]}丨数量:{int(OOO0OO0O0OOO00OOO)}')#line:1005
                                            OOO0O00OOO00OO000 =OOO0O0OO0OO00000O ["message"].split ('-')[1 ]#line:1006
                                            OOOOOOO0OO00O00OO =f'__{timi_new()}'#line:1007
                                            OOO0OOO0OO000000O ={'source':'scsc','authorization':O00000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OO00O00OO ),'signstring':OOOOOOO0OO00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            O0OO0OO00O0O0O0O0 =requests .request ('get',f'{host}/user',headers =OOO0OOO0OO000000O ).json ()#line:1019
                                            if 'status'in O0OO0OO00O0O0O0O0 :#line:1020
                                                if O0OO0OO00O0O0O0O0 ['status']==200 :#line:1021
                                                    O0OO0OOOOO0OOO0OO =O0OO0OO00O0O0O0O0 ['data']['inner_id']#line:1022
                                                    if give_gold (O0OO0OOOOO0OOO0OO ,float (OOO0O00OOO00OO000 )+1 ):#line:1023
                                                        O00000OOO0000O0OO .energy ()#line:1024
                        break #line:1025
        except Exception as O0O00O000000OOOO0 :#line:1027
            print (O0O00O000000OOOO0 )#line:1028
def bundled_def ():#line:1030
    OO0O00OO0O00O000O =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return OO0O00OO0O00O000O [random .randint (0 ,len (OO0O00OO0O00O000O )-1 )]#line:1032
def version_of_the_validation ():#line:1036
    return str ((88 -56 )/10 )#line:1037
def sc2 ():#line:1039
    return "19319#$%^&*((*"#line:1040
def gethostname_new ():#line:1042
    return hashlib .md5 ((socket .gethostbyname (socket .getfqdn (socket .gethostname ()))+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1043
def gitee_validation ():#line:1045
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1046
def gitee_edition ():#line:1048
    try :#line:1049
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1050
    except :#line:1051
        sys .exit (0 )#line:1052
def update_the_validation ():#line:1057
    try :#line:1058
        O000OO0OOOOOO0O0O =gitee_edition ()#line:1059
        if version_of_the_validation ()<O000OO0OOOOOO0O0O ['CityEarth']['edition']:#line:1060
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OO0OOOOOO0O0O["CityEarth"]["edition"]}   ❌')#line:1061
            print (f'更新内容=>>{O000OO0OOOOOO0O0O["CityEarth"]["content"]}   🎉')#line:1062
        else :#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OO0OOOOOO0O0O["CityEarth"]["edition"]}   ✅')#line:1064
            print (f'更新内容=>> {O000OO0OOOOOO0O0O["CityEarth"]["content"]}   🎉')#line:1065
    except Exception as OO00O0O000OO0O000 :#line:1066
        print (OO00O0O000OO0O000 )#line:1067
def sc3 ():#line:1069
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1070
if __name__ =='__main__':#line:1074
    start ()#line:1075
