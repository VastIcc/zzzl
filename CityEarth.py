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
        O00OOOO0OO000O0OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O00OOOO0OO000O0OO)}个账号==========")#line:13
        for OOO0OOOOOOOOOOO00 in O00OOOO0OO000O0OO :#line:14
            OOO00O0O00000000O =[]#line:15
            print (f"------------正在执行第{O00OOOO0OO000O0OO.index(OOO0OOOOOOOOOOO00) + 1}个账号------------")#line:16
            O0OO000000O0000O0 =CityEarth (OOO0OOOOOOOOOOO00 ,OOO00O0O00000000O ,O00OOOO0OO000O0OO .index (OOO0OOOOOOOOOOO00 ))#line:17
            def O000O0OOOOOOOO0OO ():#line:19
                if O0OO000000O0000O0 .base_info ():#line:21
                    O0OO000000O0000O0 .sealing ()#line:23
                    O0OO000000O0000O0 .invitenum ()#line:25
                    O0OO000000O0000O0 .game_map ()#line:27
                    O0OO000000O0000O0 .friends_invitation ()#line:29
                    O0OO000000O0000O0 .energy ()#line:31
                    O0OO000000O0000O0 .add_clover ()#line:33
                    O0OO000000O0000O0 .propsraffle ()#line:35
                    O0OO000000O0000O0 .synthetic ()#line:37
                    O0OO000000O0000O0 .crops_illustrated ()#line:39
                    O0OO000000O0000O0 .give_gold ()#line:41
                    O0OO000000O0000O0 .withdraw ()#line:43
            OOO00OOOOOO0000O0 =threading .Thread (target =O000O0OOOOOOOO0OO )#line:45
            OOO00OOOOOO0000O0 .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        OOO0000O000O00OOO =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO0000O000O00OOO +' ')#line:51
    except Exception as OO0OO0OOOO0OO0000 :#line:52
        print (OO0OO0OOOO0OO0000 )#line:53
def give_gold (O00OOOOO00O0O0OO0 ,O00O0000000O00O0O ):#line:56
        try :#line:57
            OO0O0O00000OOO0O0 =f'_doneeNo={O00OOOOO00O0O0OO0}&quantity={int(O00O0000000O00O0O)}_{timi_new()}'#line:58
            OOOOO000OOOOO0OOO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O0O00000OOO0O0 ),'signstring':OO0O0O00000OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            O00O000O00O00OO00 ={"quantity":int (O00O0000000O00O0O ),"doneeNo":O00OOOOO00O0O0OO0 }#line:73
            O00OOOOOOOO00OOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO000OOOOO0OOO ,data =O00O000O00O00OO00 ).json ()#line:74
            if 'status'in O00OOOOOOOO00OOO0 :#line:76
                if O00OOOOOOOO00OOO0 ['status']==200 :#line:77
                    if O00OOOOOOOO00OOO0 ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(O00O0000000O00O0O)}种子给{O00OOOOO00O0O0OO0}成功')#line:79
                        return True #line:80
                if O00OOOOOOOO00OOO0 ['status']==401 :#line:81
                    print (f'【赠送种子】:{O00OOOOOOOO00OOO0["message"]}')#line:82
                    return False #line:83
                if O00OOOOOOOO00OOO0 ['status']==500 :#line:84
                    print (f'【赠送种子】:{O00OOOOOOOO00OOO0["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as O0000000O0O0O00O0 :#line:88
            print (O0000000O0O0O00O0 )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (OOOO00OO0OOOOO000 ):#line:94
    OO00O00O00O00OO00 =hashlib .md5 (OOOO00OO0OOOOO000 .encode ()).hexdigest ()#line:95
    OOOO0O0OOOOO00000 =sc1 ()#line:96
    O0OO0OO000O000OOO =sc2 ()#line:97
    OO000O00OO0000O00 =sc3 ()#line:98
    OO0000O000O000OO0 =OOOO0O0OOOOO00000 +OO00O00O00O00OO00 +O0OO0OO000O000OOO +OO000O00OO0000O00 #line:99
    O0OO00O0000O0OO00 =hashlib .md5 (OO0000O000O000OO0 .encode ()).hexdigest ()#line:100
    return O0OO00O0000O0OO00 #line:101
def format_msg ():#line:105
    O000O000O000O00O0 =""#line:106
    for O0O00OOO0OO0OOO0O in msg_list :#line:107
        O000O000O000O00O0 +=str (O0O00OOO0OO0OOO0O )+"\r\n"#line:108
    return O000O000O000O00O0 #line:109
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
def get_json_data (O0O0OOO0O0O00OO00 ,O0OO00O00O00OOO00 ,OOOOOO0O00OOOOO0O ,OOO000OOOO0O0O00O ):#line:128
    with open (O0O0OOO0O0O00OO00 ,'rb')as O0OOO00OO0000OOO0 :#line:130
        O00OOOOO00O0OO000 =json .load (O0OOO00OO0000OOO0 )#line:131
        O00OOOOO00O0OO000 ['data'][O0OO00O00O00OOO00 ][OOOOOO0O00OOOOO0O ]=OOO000OOOO0O0O00O #line:132
        OO0OOO000000O000O =O00OOOOO00O0OO000 #line:133
    O0OOO00OO0000OOO0 .close ()#line:134
    return OO0OOO000000O000O #line:135
def write_json_data (OOOOOO00OO00OO0O0 ):#line:137
    with open (json_path1 ,'w')as OO0OO00OO00OOOO0O :#line:138
        json .dump (OOOOOO00OO00OO0O0 ,OO0OO00OO00OOOO0O )#line:139
    OO0OO00OO00OOOO0O .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (OOOO00OOOOOOO00OO ,OOO000O00O0OO000O ,O00O000000OOO0OOO ,O0000OO00OOOO0OOO ):#line:145
        try :#line:146
            OOOO00OOOOOOO00OO .msg =O00O000000OOO0OOO #line:147
            OOOO00OOOOOOO00OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            OOOO00OOOOOOO00OO .token =OOO000O00O0OO000O ['authorization']#line:149
            OOOO00OOOOOOO00OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            OOOO00OOOOOOO00OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            OOOO00OOOOOOO00OO .elephant_user =OOO000O00O0OO000O ['elephant_user']#line:152
            OOOO00OOOOOOO00OO .elephant_pswd =OOO000O00O0OO000O ['elephant_pswd']#line:153
            OOOO00OOOOOOO00OO .elephant_Task_ID =OOO000O00O0OO000O ['elephant_Task_ID']#line:154
            OOOO00OOOOOOO00OO .len_new =O0000OO00OOOO0OOO #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (O0000OOOO00000OOO ):#line:160
        try :#line:161
            O0000OOOO00000OOO .watched_ad ()#line:163
            OOOOO00OO0O0OO00O =f'__{timi_new()}'#line:164
            OOOO0O000OO0O0000 ={'source':'scsc','authorization':O0000OOOO00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OO0O0OO00O ),'signstring':OOOOO00OO0O0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            OO0O000O0000O0OO0 =requests .request ('get',f'{host}/user',headers =OOOO0O000OO0O0000 ).json ()#line:176
            if 'status'in OO0O000O0000O0OO0 :#line:178
                if OO0O000O0000O0OO0 ['status']==200 :#line:179
                    OO0000O000OO0O00O =OO0O000O0000O0OO0 ['data']['nickname']#line:180
                    OOOOO0OOOO0O0O000 =OO0O000O0000O0OO0 ['data']['inner_id']#line:181
                    O0OOO00000O00OOO0 =OO0O000O0000O0OO0 ['data']['assets']['gold']#line:182
                    OOO00OO00OOO0OOO0 =OO0O000O0000O0OO0 ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{OO0000O000OO0O00O[:5]}丨ID:{OOOOO0OOOO0O0O000}丨等级:{OOO00OO00OOO0OOO0}丨金种子:{str(O0OOO00000O00OOO0).split(".")[0]}')#line:184
                if OO0O000O0000O0OO0 ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if O0000OOOO00000OOO .elephant_user =='f':#line:187
                        return False #line:188
                    OO0OOOOOO000O0OOO =Invalid_login .addtask (elephant_user =O0000OOOO00000OOO .elephant_user ,elephant_pswd =O0000OOOO00000OOO .elephant_pswd ,elephant_Task_ID =O0000OOOO00000OOO .elephant_Task_ID )#line:189
                    O0OO0O0O00000OO00 =get_json_data (json_path ,O0000OOOO00000OOO .len_new ,'authorization',OO0OOOOOO000O0OOO )#line:190
                    if write_json_data (O0OO0O0O00000OO00 ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if OO0O000O0000O0OO0 ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as O00O0000OOO00OO00 :#line:197
            print (O00O0000OOO00OO00 )#line:198
    def sealing (O00O00O0O00O0OOOO ):#line:201
        try :#line:202
            OO00OOOO0000OOOO0 =f'__{timi_new()}'#line:203
            OOOOOOOO00OOO00O0 ={'source':'scsc','authorization':O00O00O0O00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOO0000OOOO0 ),'signstring':OO00OOOO0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOOOOOOO00OOO00O0 )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =OOOOOOOO00OOO00O0 )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOOOOOOO00OOO00O0 )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOOOOOOO00OOO00O0 )#line:218
            requests .request ('get',f'{host}/user',headers =OOOOOOOO00OOO00O0 )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOOOOOOO00OOO00O0 )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOOOOOOO00OOO00O0 )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =OOOOOOOO00OOO00O0 )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =OOOOOOOO00OOO00O0 )#line:223
            requests .request ('get',f'{host}/assets',headers =OOOOOOOO00OOO00O0 )#line:224
        except Exception as OOOO0O00O000O00OO :#line:225
            print (OOOO0O00O000O00OO )#line:226
    def withdraw (O0000O00O000O0000 ):#line:230
        OO000O0OO00O000O0 =f'__{timi_new()}'#line:231
        O0O0O0OOO0OO00000 ={'source':'scsc','authorization':O0000O00O000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OO00O000O0 ),'signstring':OO000O0OO00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        OOOOOO0OOO000OO00 =requests .request ('get',f'{host}/assets',headers =O0O0O0OOO0OO00000 ).json ()#line:243
        if 'status'in OOOOOO0OOO000OO00 :#line:245
            if OOOOOO0OOO000OO00 ['status']==200 :#line:246
                O0OOOO0OOO0O0O0O0 =OOOOOO0OOO000OO00 ['data']['cash']#line:247
                if float (O0OOOO0OOO0O0O0O0 )>20 :#line:248
                    OO000O0OO00O000O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    O0O0O0OOO0OO00000 ={'authorization':O0000O00O000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OO00O000O0 ),'signstring':OO000O0OO00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    O0000OO00O000OO0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    OOO00OOOOOOO0O0O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0O0OOO0OO00000 ,data =O0000OO00O000OO0O ).json ()#line:262
                    print (OOO00OOOOOOO0O0O0 )#line:263
    def invitenum (O000OO00O0O0O0OOO ):#line:266
        O0O00O0O00O0O0000 =f'__{timi_new()}'#line:267
        OOOOO0O0O000OOO00 ={'source':'scsc','authorization':O000OO00O0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O00O0O0000 ),'signstring':O0O00O0O00O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        O0OO0000O00000O0O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO0O0O000OOO00 ).json ()#line:279
        if 'status'in O0OO0000O00000O0O :#line:281
            if O0OO0000O00000O0O ['status']==200 :#line:282
                OO00O00OO00O000O0 =O0OO0000O00000O0O ['data']['invited_count']#line:283
                O000O0O000OOO0000 =O0OO0000O00000O0O ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{OO00O00OO00O000O0}丨间邀好友:{O000O0O000OOO0000}')#line:285
    def game_map (O0000O00OO0O00O00 ):#line:288
        try :#line:289
            O00000OO0OOOOO0OO =f'__{timi_new()}'#line:290
            OOOO0OOO00OO0O000 ={'source':'scsc','authorization':O0000O00OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0OOOOO0OO ),'signstring':O00000OO0OOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0OOOOOO00O00OOOO =requests .request ('get',f'{host}/game/map',headers =OOOO0OOO00OO0O000 ).json ()#line:302
            if 'status'in O0OOOOOO00O00OOOO :#line:304
                if O0OOOOOO00O00OOOO ['status']==200 :#line:305
                    for O00O00OOO0OOOO0O0 in O0OOOOOO00O00OOOO ['data']['list'][0 ]['crops']:#line:306
                        OO0OO0O0O0O000O00 =O00O00OOO0OOOO0O0 ['level']#line:308
                        if OO0OO0O0O0O000O00 ==41 :#line:309
                            O00000O00O00OOO00 =O00O00OOO0OOOO0O0 ['crop_name']#line:310
                            OO00O00OO0O00000O =O00O00OOO0OOOO0O0 ['count']#line:311
                            if OO00O00OO0O00000O >0 :#line:312
                                print (f'【农业资产】:{O00000O00O00OOO00}丨数量:{OO00O00OO0O00000O}')#line:313
        except Exception as O00OO000OO00OO0OO :#line:314
            print (O00OO000OO00OO0OO )#line:315
    def give_gold (O0O0O00O00000O0O0 ):#line:318
        try :#line:319
            O0OOO0OOOO00OOO00 =f'__{timi_new()}'#line:320
            O0O00OOOO0OOO0OOO ={'source':'scsc','authorization':O0O0O00O00000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOOO00OOO00 ),'signstring':O0OOO0OOOO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            OO0O00000OO0O0O00 =requests .request ('get',f'{host}/user',headers =O0O00OOOO0OOO0OOO ).json ()#line:332
            if 'status'in OO0O00000OO0O0O00 :#line:333
                if OO0O00000OO0O0O00 ['status']==200 :#line:334
                    if float (O0O0O00O00000O0O0 .doneeNo )!=0 :#line:335
                        O00OO0O00OOOOO0O0 =OO0O00000OO0O0O00 ['data']['assets']['gold']#line:336
                        if float (O00OO0O00OOOOO0O0 )>float (O0O0O00O00000O0O0 .innerId ):#line:337
                            OOO000OOOOO0O00OO =int (float (O00OO0O00OOOOO0O0 )/1.1 )#line:338
                            O0OOO0OOOO00OOO00 =f'_doneeNo={O0O0O00O00000O0O0.doneeNo}&quantity={OOO000OOOOO0O00OO}_{timi_new()}'#line:339
                            O0O00OOOO0OOO0OOO ={'source':'scsc','authorization':O0O0O00O00000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOOO00OOO00 ),'signstring':O0OOO0OOOO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O000OOOO00O0O00OO ={"quantity":OOO000OOOOO0O00OO ,"doneeNo":O0O0O00O00000O0O0 .doneeNo }#line:354
                            OOO0000000O000O00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OOOO0OOO0OOO ,data =O000OOOO00O0O00OO ).json ()#line:355
                            if 'status'in OOO0000000O000O00 :#line:357
                                if OOO0000000O000O00 ['status']==200 :#line:358
                                    if OOO0000000O000O00 ['data']:#line:359
                                        print (f'【赠送种子】:赠送{OOO000OOOOO0O00OO}种子给{O0O0O00O00000O0O0.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OOO0O000000000O00 :#line:363
            print (OOO0O000000000O00 )#line:364
    def invitation (OOO00O0000O00O000 ):#line:366
        try :#line:367
            _OOO00OO0O0O000OOO =float (bundled_def ())/4 #line:368
            OO0O0O0OO0O0O0OO0 =f'_innerId={int(_OOO00OO0O0O000OOO)}_{timi_new()}'#line:369
            O00000O0000OOO000 ={'source':'scsc','authorization':OOO00O0000O00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OO0O0O0OO0 ),'signstring':OO0O0O0OO0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            O00OO0OO00OO00OO0 ={"innerId":int (_OOO00OO0O0O000OOO )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00000O0000OOO000 ,data =O00OO0OO00OO00OO0 )#line:382
        except Exception as O0OOOO0O0O00OO000 :#line:383
            print (O0OOOO0O0O00OO000 )#line:384
    def winning_rewards (OO0OO0000OOOOO00O ):#line:387
        try :#line:388
            OOOO0000OO000OOOO =f'__{timi_new()}'#line:389
            OOO0O0000OO000OOO ={'source':'scsc','authorization':OO0OO0000OOOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000OO000OOOO ),'signstring':OOOO0000OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            O0OOO0O0O000O000O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0O0000OO000OOO ).json ()#line:401
            if 'status'in O0OOO0O0O000O000O :#line:403
                if O0OOO0O0O000O000O ['status']==200 :#line:404
                    if O0OOO0O0O000O000O ['data']['amount']:#line:405
                        O0OOO000OOOO0OO0O =O0OOO0O0O000O000O ['data']['amount']['gold']#line:406
                        return O0OOO000OOOO0OO0O #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as OOOOO00OOOOO00O00 :#line:410
            print (OOOOO00OOOOO00O00 )#line:411
    def certification (O000OO0000O000O00 ):#line:414
        try :#line:415
            OOOO0O0O0O00OOO00 =f'__{timi_new()}'#line:416
            O0O0OO0OO00OOO0OO ={'source':'scsc','authorization':O000OO0000O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O0O00OOO00 ),'signstring':OOOO0O0O0O00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            O0OO000O00O0OOOO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O0OO0OO00OOO0OO ).json ()#line:428
            if 'status'in O0OO000O00O0OOOO0 :#line:430
                if O0OO000O00O0OOOO0 ['status']==200 :#line:431
                    if O0OO000O00O0OOOO0 ['data']['result']:#line:432
                        OO00O0O00000000OO =O0OO000O00O0OOOO0 ['data']['nick_name']#line:433
                        return OO00O0O00000000OO #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as OOO0O0O0OOO00O00O :#line:437
            print (OOO0O0O0OOO00O00O )#line:438
    def crops_illustrated (OO0OO00O0O00OO0O0 ):#line:441
        try :#line:442
            OOOO0OOOO0O0OOO00 =f'__{timi_new()}'#line:443
            OO0O0OOO0OO000O0O ={'source':'scsc','authorization':OO0OO00O0O00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0O0OOO00 ),'signstring':OOOO0OOOO0O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            O0O0O000O0O000O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0OOO0OO000O0O ).json ()#line:455
            if 'status'in O0O0O000O0O000O00 :#line:457
                if O0O0O000O0O000O00 ['status']==200 :#line:458
                    O0OOOO00OOOO000O0 =O0O0O000O0O000O00 ['data'][0 ]['crops']#line:459
                    for OOO000OO0O0OO0000 in O0OOOO00OOOO000O0 :#line:460
                        if OOO000OO0O0OO0000 ['ill_clover_award']:#line:461
                            if float (OOO000OO0O0OO0000 ['ill_clover_award'])>1 :#line:462
                                if OOO000OO0O0OO0000 ['is_finish']:#line:463
                                    if not OOO000OO0O0OO0000 ['is_getit']:#line:464
                                        if OO0OO00O0O00OO0O0 .certification ()!='未实名':#line:465
                                            OOOO0OOOO0O0OOO00 =f'_award_level={OOO000OO0O0OO0000["level"]}_{timi_new()}'#line:466
                                            OO0O0OOO0OO000O0O ={'source':'scsc','authorization':OO0OO00O0O00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0O0OOO00 ),'signstring':OOOO0OOOO0O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            OO000OOO00O000000 ={"award_level":OOO000OO0O0OO0000 ['level']}#line:478
                                            OO000O000OOO00000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0OOO0OO000O0O ,json =OO000OOO00O000000 ).json ()#line:480
                                            if 'status'in OO000O000OOO00000 :#line:481
                                                if OO000O000OOO00000 ['status']==200 :#line:482
                                                    O0000OOOOOOOOOOOO =OO000O000OOO00000 ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{OOO000OO0O0OO0000["crop_name"]}成就丨奖励{O0000OOOOOOOOOOOO}☘️')#line:485
                                                if OO000O000OOO00000 ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{OO000O000OOO00000["message"]}')#line:487
        except Exception as O000O000OO0O0O00O :#line:488
            print (O000O000OO0O0O00O )#line:489
    def watched_ad (O00O00OO000O00OO0 ):#line:492
        try :#line:493
            O0O00OOOO0O0OO00O =f'__{timi_new()}'#line:494
            O0O00O0O000OOO00O ={'source':'scsc','authorization':O00O00OO000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO0O0OO00O ),'signstring':O0O00OOOO0O0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            OOOOOOOO0OO0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0O000OOO00O ).json ()#line:506
            if 'status'in OOOOOOOO0OO0O0000 :#line:508
                if OOOOOOOO0OO0O0000 ['status']==200 :#line:509
                    if 'offlineInfo'in OOOOOOOO0OO0O0000 ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        O0O00OOO0OOO0OO00 =OOOOOOOO0OO0O0000 ['data']['offlineInfo']['off_minute']#line:512
                        O000OO0O000O000OO =float (OOOOOOOO0OO0O0000 ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O00O0O000OOO00O ).json ()#line:515
                        time .sleep (2 )#line:516
                        O0OO0OO00000OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0O000OOO00O ).json ()#line:517
                        if 'status'in O0OO0OO00000OOO0O :#line:519
                            if O0OO0OO00000OOO0O ['status']==200 :#line:520
                                O0O0000OOO0O0OO00 =float (O0OO0OO00000OOO0O ['data']['silver'])/1000000000000 #line:521
                                O0O0OO0000OO00O00 =str (O0O0000OOO0O0OO00 -O000OO0O000O000OO )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{O0O00OOO0OOO0OO00}分钟奖励🌱数量:{O0O0OO0000OO00O00}t粒')#line:523
        except Exception as O000OOO0OOOO00O00 :#line:524
            print (O000OOO0OOOO00O00 )#line:525
    def user_ad (O00000OO0OO0O0O00 ):#line:528
        try :#line:529
            O0000OOOOO0OOOO0O =f'__{timi_new()}'#line:530
            OO0000000O00000OO ={'source':'scsc','authorization':O00000OO0OO0O0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOOO0OOOO0O ),'signstring':O0000OOOOO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            O0O00OOOOO0OOOOOO =requests .request ('get',f'{host}/user/ad',headers =OO0000000O00000OO ).json ()#line:542
            if 'status'in O0O00OOOOO0OOOOOO :#line:544
                if O0O00OOOOO0OOOOOO ['status']==200 :#line:545
                    OOOOO0O00OOOO0000 =O0O00OOOOO0OOOOOO ['data']['max_time']#line:546
                    O0O000000OOO0OO00 =O0O00OOOOO0OOOOOO ['data']['watch_time']#line:547
                    O0OOO00O000000OOO =O0O00OOOOO0OOOOOO ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{O0OOO00O000000OOO + OOOOO0O00OOOO0000 - O0O000000OOO0OO00}次丨好友提供:{O0OOO00O000000OOO}次')#line:549
                    if O0OOO00O000000OOO +OOOOO0O00OOOO0000 -O0O000000OOO0OO00 >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        OO00O00OO00000OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0000000O00000OO ).json ()#line:552
                        if 'status'in OO00O00OO00000OOO :#line:554
                            if OO00O00OO00000OOO ['status']==200 :#line:555
                                O00O0OO00000O0000 =float (OO00O00OO00000OOO ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(O00O0OO00000O0000)}t粒')#line:557
                                return True #line:558
                            if OO00O00OO00000OOO ['status']==500 :#line:559
                                O0O0000O00OO0O0OO =OO00O00OO00000OOO ['message']#line:560
                                print (f'【获取种子】:{O0O0000O00OO0O0OO}')#line:561
                                return False #line:562
        except Exception as OOOO00O00OOO0O0O0 :#line:563
            print (OOOO00O00OOO0O0O0 )#line:564
    def synthetic (O00OO00O0OO00OOOO ):#line:567
        global id ,g #line:568
        try :#line:569
            O000OOOOOOOO000OO =O00OO00O0OO00OOOO .level_new ()#line:570
            O0OO000O0O0O00OOO =random .randint (9 ,11 )#line:571
            O0000OOOOO00OO000 =f'_site=8&targetSite={O0OO000O0O0O00OOO}_{timi_new()}'#line:572
            OOO00000OOOO0O00O ={'source':'scsc','authorization':O00OO00O0OO00OOOO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOOO00OO000 ),'signstring':O0000OOOOO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            O000OOOO00OOO0O0O ={"site":int (8 ),"targetSite":int (O0OO000O0O0O00OOO )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000OOOO0O00O ,json =O000OOOO00OOO0O0O )#line:585
            while True :#line:586
                O0OOO00000OOO0000 =f'__{timi_new()}'#line:587
                OO00O0OOO0000O00O ={'source':'scsc','authorization':O00OO00O0OO00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00000OOO0000 ),'signstring':O0OOO00000OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                OOOO000OOOOOOOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OOO0000O00O ).json ()#line:599
                if 'status'in OOOO000OOOOOOOO0O :#line:601
                    if OOOO000OOOOOOOO0O ['status']==200 :#line:602
                        OOOOO00O000O0O0OO =OOOO000OOOOOOOO0O ['data']['cropList']#line:603
                        O0OO0O0O0OOO00O0O =OOOO000OOOOOOOO0O ['data']['gameCoreDataDBid']#line:604
                        OO00O000OOO0O0OO0 =float (OOOO000OOOOOOOO0O ['data']['silver'])/1000000000000 #line:605
                        O0OOO0OO0OO0O00O0 =0 #line:610
                        for OO0OO0O000OO0O000 in OOOOO00O000O0O0OO :#line:611
                            if not OO0OO0O000OO0O000 :#line:612
                                O0000O00OOO00O0OO =f'_crop_id={O0OO0O0O0OOO00O0O}&site={O0OOO0OO0OO0O00O0}_{O00OO00O0OO00OOOO.time}'#line:613
                                OO0O000O0OOO0OOO0 ={'source':'scsc','authorization':O00OO00O0OO00OOOO .token ,'timestamp':O00OO00O0OO00OOOO .time ,'sign':sign (O0000O00OOO00O0OO ),'signstring':O0000O00OOO00O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                O000O0OO0O000OOO0 ={"site":O0OOO0OO0OO0O00O0 ,"crop_id":O0OO0O0O0OOO00O0O }#line:624
                                O0O0O0000OOOO0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0O000O0OOO0OOO0 ,data =O000O0OO0O000OOO0 ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in O0O0O0000OOOO0O00 :#line:628
                                    if O0O0O0000OOOO0O00 ['status']==200 :#line:629
                                        if O0O0O0000OOOO0O00 ['message']=='种子数量不足':#line:630
                                            O000OOOOOOOO000OO =O00OO00O0OO00OOOO .level_new ()#line:631
                                            print (f'【种植合成】:{O0O0O0000OOOO0O00["message"]}')#line:632
                                            if not O00OO00O0OO00OOOO .user_ad ():#line:633
                                                return False #line:634
                                    if O0O0O0000OOOO0O00 ['status']==500 :#line:635
                                        print (f'【种植合成】:{O0O0O0000OOOO0O00["message"]}')#line:636
                                        return False #line:637
                            O0OOO0OO0OO0O00O0 +=1 #line:638
                        O000O00O0O0000O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OOO0000O00O ).json ()#line:639
                        O0O00OOO0OO0O00OO =O000O00O0O0000O0O ['data']['cropList']#line:640
                        O00OO0OOO0OO0O0O0 =False #line:641
                        for OO0OO0O000OO0O000 in range (12 ):#line:642
                            id =O0O00OOO0OO0O00OO [OO0OO0O000OO0O000 ]['level']#line:643
                            if float (O000OOOOOOOO000OO )-float (id )>9 :#line:644
                                OOO0O0OOOOOO0OO00 =f'_site={OO0OO0O000OO0O000}_{timi_new()}'#line:645
                                O00OO0O0OOOO0OOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OO00O0OO00OOOO .token ,'timestamp':timi_new (),'sign':sign (OOO0O0OOOOOO0OO00 ),'signstring':OOO0O0OOOOOO0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O00O0OOO0O0O0OO00 ={"site":OO0OO0O000OO0O000 }#line:657
                                O00OOO0O000OOOOO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO0O0OOOO0OOOO ,data =O00O0OOO0O0O0OO00 ).json ()#line:659
                                if 'status'in O00OOO0O000OOOOO0 :#line:660
                                    if O00OOO0O000OOOOO0 ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for O0000OO0000OO0O0O in range (11 ):#line:664
                                    OO00OO0OOOOOOO000 =O0000OO0000OO0O0O +1 #line:665
                                    g =O0O00OOO0OO0O00OO [OO00OO0OOOOOOO000 ]['level']#line:666
                                    if id ==g :#line:667
                                        O0O0O00OO0OOOOOOO =O0000OO0000OO0O0O +2 #line:668
                                        if O0O0O00OO0OOOOOOO !=OO0OO0O000OO0O000 +1 :#line:669
                                            OO0OO00O000000O00 =OO0OO0O000OO0O000 +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            O0000OOOOO00OO000 =f'_site={OO0OO00O000000O00 - 1}&targetSite={O0O0O00OO0OOOOOOO - 1}_{timi_new()}'#line:673
                                            OOO00000OOOO0O00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00OO00O0OO00OOOO .token ,'timestamp':timi_new (),'sign':sign (O0000OOOOO00OO000 ),'signstring':O0000OOOOO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            O000O0000O0OOO0OO ={"site":int (OO0OO00O000000O00 -1 ),"targetSite":int (O0O0O00OO0OOOOOOO -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO00000OOOO0O00O ,json =O000O0000O0OOO0OO )#line:692
                                            O00OO0OOO0OO0O0O0 =True #line:694
                                    if O00OO0OOO0OO0O0O0 :#line:695
                                        break #line:696
                                if O00OO0OOO0OO0O0O0 :#line:697
                                    break #line:698
        except :#line:699
            O00OO00O0OO00OOOO .synthetic ()#line:700
    def level_new (OOOO000OOOO0O0OOO ):#line:703
        try :#line:704
            O00O000OO00OOOOO0 =f'__{timi_new()}'#line:705
            O0OO00OOO00OOO00O ={'source':'scsc','authorization':OOOO000OOOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OO00OOOOO0 ),'signstring':O00O000OO00OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            O0OO00OO0O000O0O0 =requests .request ('get',f'{host}/user',headers =O0OO00OOO00OOO00O ).json ()#line:717
            if 'status'in O0OO00OO0O000O0O0 :#line:718
                if O0OO00OO0O000O0O0 ['status']==200 :#line:719
                    return float (O0OO00OO0O000O0O0 ['data']['level'])#line:720
        except Exception as O0OOOOOOOOOO0O0OO :#line:721
            print (O0OOOOOOOOOO0O0OO )#line:722
    def propsraffle (OOO00O00000O0O00O ):#line:725
        try :#line:726
            while True :#line:727
                O000000O000OO0O0O =f'__{timi_new()}'#line:728
                OO0O0OOO000000O00 ={'source':'scsc','authorization':OOO00O00000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O000OO0O0O ),'signstring':O000000O000OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                OO0O00O0OOO00OO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0O0OOO000000O00 ).json ()#line:740
                if 'status'in OO0O00O0OOO00OO00 :#line:742
                    if OO0O00O0OOO00OO00 ['status']==200 :#line:743
                        O00OOO00OOOO0O0OO =OO0O00O0OOO00OO00 ['data']['rows']#line:744
                        OOO000000OOO000O0 =OO0O00O0OOO00OO00 ['data']['vstate']#line:745
                        if O00OOO00OOOO0O0OO ==5 or O00OOO00OOOO0O0OO ==6 or O00OOO00OOOO0O0OO ==7 :#line:746
                            OO0000O0O0O0O0000 =OO0O00O0OOO00OO00 ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{OO0000O0O0O0O0000}')#line:748
                        if O00OOO00OOOO0O0OO ==1 or O00OOO00OOOO0O0OO ==2 or O00OOO00OOOO0O0OO ==3 :#line:749
                            O00000O0O00O000OO =OO0O00O0OOO00OO00 ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{O00000O0O00O000OO}')#line:751
                        if O00OOO00OOOO0O0OO ==4 or O00OOO00OOOO0O0OO ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if O00OOO00OOOO0O0OO =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as OO000O0O00O000000 :#line:793
            print (OO000O0O00O000000 )#line:794
    def friends_invitation (OOOOOOOOOO0OO0000 ):#line:797
        try :#line:798
            O000000OO0OOOOO00 =f'__{timi_new()}'#line:799
            O0OOO000OO0OO00O0 ={'source':'scsc','authorization':OOOOOOOOOO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OO0OOOOO00 ),'signstring':O000000OO0OOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            OO0O00OO00O0OOOOO =requests .request ('get',f'{host}/friends',headers =O0OOO000OO0OO00O0 ).json ()#line:811
            if 'status'in OO0O00OO00O0OOOOO :#line:812
                if OO0O00OO00O0OOOOO ['status']==200 :#line:813
                    O0OO0000OOO0O0000 =OO0O00OO00O0OOOOO ['data']['myInviteter']#line:814
                    if O0OO0000OOO0O0000 :#line:815
                        O0O0O00O00000OOO0 =O0OO0000OOO0O0000 ['user']['nickname']#line:816
                        OOO00OOO0O0O00OOO =OOOOOOOOOO0OO0000 .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{O0O0O00O00000OOO0}丨实名:{OOO00OOO0O0O00OOO}')#line:818
                    else :#line:819
                        if OOOOOOOOOO0OO0000 .innerId !='0':#line:820
                            OOOOOOOOOO0OO0000 .invitation ()#line:821
        except Exception as O0000OO0OO0OOOOOO :#line:822
            print (O0000OO0OO0OOOOOO )#line:823
    def add_clover (O00000O0O00000000 ):#line:826
        global golden_seed #line:827
        try :#line:828
            O0OOO000OO00OOOOO =f'__{timi_new()}'#line:829
            OOO0O0000OOO0O00O ={'source':'scsc','authorization':O00000O0O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000OO00OOOOO ),'signstring':O0OOO000OO00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            OOOO000O00000OO0O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0O0000OOO0O00O ).json ()#line:841
            if 'status'in OOOO000O00000OO0O :#line:843
                if OOOO000O00000OO0O ['status']==200 :#line:844
                    O000OO0OO0000OOO0 =OOOO000O00000OO0O ['data']['clover']#line:845
                    OO00O00000OOOOOO0 =OOOO000O00000OO0O ['data']['used_clover']#line:846
                    O0000OO0000O0OOO0 =float (O000OO0OO0000OOO0 )-float (OO00O00000OOOOOO0 )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO00O00000OOOOOO0}')#line:848
                    if O00000O0O00000000 .certification ()!='未实名':#line:849
                        if O0000OO0000O0OOO0 >1 :#line:850
                            O0OOO000OO00OOOOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0000OO0000O0OOO0)}_{timi_new()}'#line:851
                            OOO0O0O0O0OOO00O0 ={'source':'scsc','authorization':O00000O0O00000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO000OO00OOOOO ),'signstring':O0OOO000OO00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            OO0OO0O00O0O00OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0000OO0000O0OOO0 )}#line:863
                            OOO0O0O0OOOO000O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0O0O0O0OOO00O0 ,data =OO0OO0O00O0O00OO0 ).json ()#line:864
                            if 'status'in OOO0O0O0OOOO000O0 :#line:866
                                if OOO0O0O0OOOO000O0 ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{OOO0O0O0OOOO000O0["data"]}丨数量:{O0000OO0000O0OOO0}')#line:868
                                if OOO0O0O0OOOO000O0 ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{OOO0O0O0OOOO000O0["message"]}')#line:870
            O0O0O00000OOO0000 =requests .request ('get',f'{host}/lottery',headers =OOO0O0000OOO0O00O ).json ()#line:871
            O000OOOOO00OO00OO =O00000O0O00000000 .winning_rewards ()#line:873
            if 'status'in O0O0O00000OOO0000 :#line:874
                if O0O0O00000OOO0000 ['status']==200 :#line:875
                    O000000OOOO0OO00O =O0O0O00000OOO0000 ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (O000000OOOO0OO00O )#line:877
                    OOO00OOO0O0OO0O0O =O0O0O00000OOO0000 ['data'][1 ]['value']#line:878
                    OO0O0O0OO00O0OOOO =O0O0O00000OOO0000 ['data'][0 ]['join_number']#line:879
                    OOOO00O0O0OOO000O =int (float (O0O0O00000OOO0000 ['data'][0 ]['totalValue']))#line:880
                    OO0O0000O0OO0O0O0 =float (OOO00OOO0O0OO0O0O /OOOO00O0O0OOO000O )*10000 #line:881
                    OO0000O0O000OOO0O =OOOO00O0O0OOO000O /OO0O0O0OO00O0OOOO #line:882
                    print (f'【参与抽奖】:预计每天中{str(O000000OOOO0OO00O)[:6]}颗金种子丨好友收益:{str(O000OOOOO00OO00OO)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(OO0O0000O0OO0O0O0)[:6]}颗金种子丨☘️人均:{str(OO0000O0O000OOO0O)[:7]}️')#line:884
        except Exception as O00OOOOO0OO0OOO0O :#line:885
            print (O00OOOOO0OO0OOO0O )#line:886
    def energy (OOO0O00O00OOOOO0O ):#line:890
        try :#line:891
            while True :#line:892
                OO0OOO00O0O000OOO =f'__{timi_new()}'#line:893
                O0OOO0O0OOO000O0O ={'source':'scsc','authorization':OOO0O00O00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO00O0O000OOO ),'signstring':OO0OOO00O0O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                O0O0OOOOOO0OO0O0O =requests .request ('get',f'{host}/energy/general',headers =O0OOO0O0OOO000O0O ).json ()#line:905
                if 'status'in O0O0OOOOOO0OO0O0O :#line:907
                    if O0O0OOOOOO0OO0O0O ['status']==200 :#line:908
                        OO0000OOO00O0OOO0 =O0O0OOOOOO0OO0O0O ['data']['ordinary_water']#line:909
                        O000O0O000000000O =O0O0OOOOOO0OO0O0O ['data']['ordinary_fertilizer']#line:910
                        OOOO0O0O00000000O =O0O0OOOOOO0OO0O0O ['data']['videoStatus']#line:911
                        OO0O0OOO0O0O00OO0 =O0O0OOOOOO0OO0O0O ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(O000O0O000000000O).split(".")[0]}丨水滴:{str(OO0000OOO00O0OOO0).split(".")[0]}')#line:913
                        if float (O000O0O000000000O )<96 :#line:914
                            if OOOO0O0O00000000O :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                O000O00O0OOO0OOO0 =99 -float (O000O0O000000000O )#line:917
                                OO000000O0OOO000O ={"fertilizer":str (O000O00O0OOO0OOO0 ).split ('.')[0 ]}#line:918
                                O000OOO00O00O00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OOO0O0OOO000O0O ).json ()#line:919
                                if 'status'in O000OOO00O00O00O0 :#line:921
                                    if O000OOO00O00O00O0 ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO00O00O00O0["message"]}')#line:923
                                    if O000OOO00O00O00O0 ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO00O00O00O0["message"]}')#line:925
                                        break #line:926
                                if float (O000O0O000000000O )<78 :#line:928
                                    O000O00O0OOO0OOO0 =80 -float (O000O0O000000000O )#line:929
                                    O0O0OO00O00OOOO0O =f'_fertilizer={int(O000O00O0OOO0OOO0)}_{timi_new()}'#line:930
                                    O000O00000OOO0000 ={'source':'scsc','authorization':OOO0O00O00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00OOOO0O ),'signstring':O0O0OO00O00OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    O000OOOO0OOO0OOO0 ={"fertilizer":int (O000O00O0OOO0OOO0 )}#line:942
                                    OO00OOO0OO000000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000O00000OOO0000 ,data =O000OOOO0OOO0OOO0 ).json ()#line:944
                                    if 'status'in OO00OOO0OO000000O :#line:946
                                        if OO00OOO0OO000000O ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{OO00OOO0OO000000O["message"]}丨数量:{int(O000O00O0OOO0OOO0)}')#line:948
                                        if OO00OOO0OO000000O ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{OO00OOO0OO000000O["message"]}丨数量:{int(O000O00O0OOO0OOO0)}')#line:950
                                            O0O0O0O000O0O00O0 =OO00OOO0OO000000O ["message"].split ('-')[1 ]#line:951
                                            OO00OO00O0OO0OO0O =f'__{timi_new()}'#line:952
                                            O000000O000OOOOO0 ={'source':'scsc','authorization':OOO0O00O00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O0OO0OO0O ),'signstring':OO00OO00O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            O0O00O0OOO00OO000 =requests .request ('get',f'{host}/user',headers =O000000O000OOOOO0 ).json ()#line:964
                                            if 'status'in O0O00O0OOO00OO000 :#line:965
                                                if O0O00O0OOO00OO000 ['status']==200 :#line:966
                                                    O0O0O00O0OOOO0OOO =O0O00O0OOO00OO000 ['data']['inner_id']#line:967
                                                    if give_gold (O0O0O00O0OOOO0OOO ,float (O0O0O0O000O0O00O0 )+1 ):#line:968
                                                        OOO0O00O00OOOOO0O .energy ()#line:969
                        if float (OO0000OOO00O0OOO0 )<880 :#line:970
                            if OO0O0OOO0O0O00OO0 :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                O000O0OO000OO0000 =999 -float (OO0000OOO00O0OOO0 )#line:973
                                O00O0OO0O00O0000O ={"water":str (O000O0OO000OO0000 ).split ('.')[0 ]}#line:974
                                OO00000OOO00O00O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OOO0O0OOO000O0O ).json ()#line:975
                                if 'status'in OO00000OOO00O00O0 :#line:977
                                    if OO00000OOO00O00O0 ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OO00000OOO00O00O0["message"]}')#line:979
                                    if OO00000OOO00O00O0 ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OO00000OOO00O00O0["message"]}')#line:981
                                        break #line:982
                                if float (OO0000OOO00O0OOO0 )<780 :#line:983
                                    O000O0OO000OO0000 =800 -float (OO0000OOO00O0OOO0 )#line:984
                                    OO00000O0O0OOO00O =f'_water={int(O000O0OO000OO0000)}_{timi_new()}'#line:985
                                    O0000O0O00O0O0OOO ={'source':'scsc','authorization':OOO0O00O00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0O0OOO00O ),'signstring':OO00000O0O0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    O00O0O0OO00OOOOO0 ={"water":int (O000O0OO000OO0000 )}#line:997
                                    O0000000000O00OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0000O0O00O0O0OOO ,data =O00O0O0OO00OOOOO0 ).json ()#line:999
                                    if 'status'in O0000000000O00OOO :#line:1001
                                        if O0000000000O00OOO ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{O0000000000O00OOO["message"]}丨数量:{int(O000O0OO000OO0000)}')#line:1003
                                        if O0000000000O00OOO ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{O0000000000O00OOO["message"]}丨数量:{int(O000O0OO000OO0000)}')#line:1005
                                            O0O0O0O000O0O00O0 =O0000000000O00OOO ["message"].split ('-')[1 ]#line:1006
                                            OO00OO00O0OO0OO0O =f'__{timi_new()}'#line:1007
                                            O000000O000OOOOO0 ={'source':'scsc','authorization':OOO0O00O00OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO00O0OO0OO0O ),'signstring':OO00OO00O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            O0O00O0OOO00OO000 =requests .request ('get',f'{host}/user',headers =O000000O000OOOOO0 ).json ()#line:1019
                                            if 'status'in O0O00O0OOO00OO000 :#line:1020
                                                if O0O00O0OOO00OO000 ['status']==200 :#line:1021
                                                    O0O0O00O0OOOO0OOO =O0O00O0OOO00OO000 ['data']['inner_id']#line:1022
                                                    if give_gold (O0O0O00O0OOOO0OOO ,float (O0O0O0O000O0O00O0 )+1 ):#line:1023
                                                        OOO0O00O00OOOOO0O .energy ()#line:1024
                        break #line:1025
        except Exception as OO0O00O00O0O0OOO0 :#line:1027
            print (OO0O00O00O0O0OOO0 )#line:1028
def bundled_def ():#line:1030
    O0OOOOOOO0OOO0OO0 =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return O0OOOOOOO0OOO0OO0 [random .randint (0 ,len (O0OOOOOOO0OOO0OO0 )-1 )]#line:1032
def version_of_the_validation ():#line:1036
    return str ((88 -56 )/10 )#line:1037
def sc2 ():#line:1039
    return "19319#$%^&*((*"#line:1040
def OO00OO0OO0OO00OO00o0 ():#line:1042
    return hashlib .md5 ((':'.join (re .findall ('..','%012x'%uuid .getnode ()))+socket .getfqdn (socket .gethostname ())+socket .gethostbyname (socket .getfqdn (socket .gethostname ()))).encode ('utf-8')).hexdigest ().upper ()#line:1043
def gitee_validation ():#line:1045
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1046
def gitee_edition ():#line:1048
    try :#line:1049
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1050
    except :#line:1051
        sys .exit (0 )#line:1052
def O000OO000O0O00OOO00 ():#line:1057
    try :#line:1058
        O00O0OOOOOO00000O =gitee_edition ()#line:1059
        if version_of_the_validation ()<O00O0OOOOOO00000O ['CityEarth']['edition']:#line:1060
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OOOOOO00000O["CityEarth"]["edition"]}   ❌')#line:1061
            print (f'更新内容=>>{O00O0OOOOOO00000O["CityEarth"]["content"]}   🎉')#line:1062
        else :#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0OOOOOO00000O["CityEarth"]["edition"]}   ✅')#line:1064
            print (f'更新内容=>> {O00O0OOOOOO00000O["CityEarth"]["content"]}   🎉')#line:1065
    except Exception as OO00O00O000OO000O :#line:1066
        print (OO00O00O000OO000O )#line:1067
def sc3 ():#line:1069
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1070
if __name__ =='__main__':#line:1074
    start ()#line:1075
