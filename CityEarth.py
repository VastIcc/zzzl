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
@ 版本  3.3
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
        O000OOOOOOOOOO000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O000OOOOOOOOOO000)}个账号==========")#line:13
        for OOOO0O00OOO0OO0O0 in O000OOOOOOOOOO000 :#line:14
            OOO00OOO0000O0O00 =[]#line:15
            print (f"------------正在执行第{O000OOOOOOOOOO000.index(OOOO0O00OOO0OO0O0) + 1}个账号------------")#line:16
            OO00OO00OO0OO00OO =CityEarth (OOOO0O00OOO0OO0O0 ,OOO00OOO0000O0O00 ,O000OOOOOOOOOO000 .index (OOOO0O00OOO0OO0O0 ))#line:17
            def O0O0O0O00OO000000 ():#line:19
                if OO00OO00OO0OO00OO .base_info ():#line:21
                    OO00OO00OO0OO00OO .sealing ()#line:23
                    OO00OO00OO0OO00OO .invitenum ()#line:25
                    OO00OO00OO0OO00OO .game_map ()#line:27
                    OO00OO00OO0OO00OO .friends_invitation ()#line:29
                    OO00OO00OO0OO00OO .energy ()#line:31
                    OO00OO00OO0OO00OO .add_clover ()#line:33
                    OO00OO00OO0OO00OO .propsraffle ()#line:35
                    OO00OO00OO0OO00OO .synthetic ()#line:37
                    OO00OO00OO0OO00OO .crops_illustrated ()#line:39
                    OO00OO00OO0OO00OO .give_gold ()#line:41
                    OO00OO00OO0OO00OO .withdraw ()#line:43
            OOO00OOOOOOOOOOO0 =threading .Thread (target =O0O0O0O00OO000000 )#line:45
            OOO00OOOOOOOOOOO0 .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        O000O0O00O0OOOO0O =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O0O00O0OOOO0O +' ')#line:51
    except Exception as OO0O0OO000OO0OO0O :#line:52
        print (OO0O0OO000OO0OO0O )#line:53
def give_gold (OO00OO0OO0OO0O000 ,OOO00OOOOOO0OO0O0 ):#line:56
        try :#line:57
            O00OO0000OO00000O =f'_doneeNo={OO00OO0OO0OO0O000}&quantity={int(OOO00OOOOOO0OO0O0)}_{timi_new()}'#line:58
            OOO0OOO00O00O0000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O00OO0000OO00000O ),'signstring':O00OO0000OO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OOOOOO0OO0OOOO0OO ={"quantity":int (OOO00OOOOOO0OO0O0 ),"doneeNo":OO00OO0OO0OO0O000 }#line:73
            O0OO0OO0OOOO0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOO00O00O0000 ,data =OOOOOO0OO0OOOO0OO ).json ()#line:74
            if 'status'in O0OO0OO0OOOO0O000 :#line:76
                if O0OO0OO0OOOO0O000 ['status']==200 :#line:77
                    if O0OO0OO0OOOO0O000 ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(OOO00OOOOOO0OO0O0)}种子给{OO00OO0OO0OO0O000}成功')#line:79
                        return True #line:80
                if O0OO0OO0OOOO0O000 ['status']==401 :#line:81
                    print (f'【赠送种子】:{O0OO0OO0OOOO0O000["message"]}')#line:82
                    return False #line:83
                if O0OO0OO0OOOO0O000 ['status']==500 :#line:84
                    print (f'【赠送种子】:{O0OO0OO0OOOO0O000["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as O0OO0O0OOOOO00OO0 :#line:88
            print (O0OO0O0OOOOO00OO0 )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (OO00O0OO00O0OOO00 ):#line:94
    O0O0O00O0O0O0OOOO =hashlib .md5 (OO00O0OO00O0OOO00 .encode ()).hexdigest ()#line:95
    OOOOO0OO00O0O000O =sc1 ()#line:96
    O00000OO00OOOOOO0 =sc2 ()#line:97
    O0OO00OO000OOO00O =sc3 ()#line:98
    OOO0000OOO0OOO000 =OOOOO0OO00O0O000O +O0O0O00O0O0O0OOOO +O00000OO00OOOOOO0 +O0OO00OO000OOO00O #line:99
    O0000000OOO00OO00 =hashlib .md5 (OOO0000OOO0OOO000 .encode ()).hexdigest ()#line:100
    return O0000000OOO00OO00 #line:101
def format_msg ():#line:105
    O0OOOOO0O0OOOO0O0 =""#line:106
    for OO0O0OOOO0O0OO0O0 in msg_list :#line:107
        O0OOOOO0O0OOOO0O0 +=str (OO0O0OOOO0O0OO0O0 )+"\r\n"#line:108
    return O0OOOOO0O0OOOO0O0 #line:109
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
def get_json_data (O0OO0O000000O0000 ,O000O00O00O0O00OO ,O00O0O0OOOOOOOOOO ,O0000O00OOO0OO000 ):#line:128
    with open (O0OO0O000000O0000 ,'rb')as OOO000OOOO00OOOOO :#line:130
        OOO00OO0OO0O0O0O0 =json .load (OOO000OOOO00OOOOO )#line:131
        OOO00OO0OO0O0O0O0 ['data'][O000O00O00O0O00OO ][O00O0O0OOOOOOOOOO ]=O0000O00OOO0OO000 #line:132
        O00OO00O000000O0O =OOO00OO0OO0O0O0O0 #line:133
    OOO000OOOO00OOOOO .close ()#line:134
    return O00OO00O000000O0O #line:135
def write_json_data (O0O00OOOOO000O0OO ):#line:137
    with open (json_path1 ,'w')as OO0000O000000OOO0 :#line:138
        json .dump (O0O00OOOOO000O0OO ,OO0000O000000OOO0 )#line:139
    OO0000O000000OOO0 .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (OO0000O000OOO0000 ,OOO0OOO0OOOOOO000 ,O0000O0O00O00OOO0 ,O0OOOO0OO00OOO000 ):#line:145
        try :#line:146
            OO0000O000OOO0000 .msg =O0000O0O00O00OOO0 #line:147
            OO0000O000OOO0000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            OO0000O000OOO0000 .token =OOO0OOO0OOOOOO000 ['authorization']#line:149
            OO0000O000OOO0000 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            OO0000O000OOO0000 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            OO0000O000OOO0000 .elephant_user =OOO0OOO0OOOOOO000 ['elephant_user']#line:152
            OO0000O000OOO0000 .elephant_pswd =OOO0OOO0OOOOOO000 ['elephant_pswd']#line:153
            OO0000O000OOO0000 .elephant_Task_ID =OOO0OOO0OOOOOO000 ['elephant_Task_ID']#line:154
            OO0000O000OOO0000 .len_new =O0OOOO0OO00OOO000 #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (O0O0O00O0O00OOO0O ):#line:160
        try :#line:161
            O0O0O00O0O00OOO0O .watched_ad ()#line:163
            OOO0O0OOOO000000O =f'__{timi_new()}'#line:164
            O00O0OOOO00O0OO00 ={'source':'scsc','authorization':O0O0O00O0O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOOO000000O ),'signstring':OOO0O0OOOO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            OOO0OO00O0000OO00 =requests .request ('get',f'{host}/user',headers =O00O0OOOO00O0OO00 ).json ()#line:176
            if 'status'in OOO0OO00O0000OO00 :#line:178
                if OOO0OO00O0000OO00 ['status']==200 :#line:179
                    OOOOOOOOOO0OO0OO0 =OOO0OO00O0000OO00 ['data']['nickname']#line:180
                    OO0O0000OOOO000O0 =OOO0OO00O0000OO00 ['data']['inner_id']#line:181
                    O00O0000OOO0OO0O0 =OOO0OO00O0000OO00 ['data']['assets']['gold']#line:182
                    O0OOO00OO0000OOOO =OOO0OO00O0000OO00 ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{OOOOOOOOOO0OO0OO0[:5]}丨ID:{OO0O0000OOOO000O0}丨等级:{O0OOO00OO0000OOOO}丨金种子:{str(O00O0000OOO0OO0O0).split(".")[0]}')#line:184
                if OOO0OO00O0000OO00 ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if O0O0O00O0O00OOO0O .elephant_user =='f':#line:187
                        return False #line:188
                    OOO0O0O0O0OOOO00O =Invalid_login .addtask (elephant_user =O0O0O00O0O00OOO0O .elephant_user ,elephant_pswd =O0O0O00O0O00OOO0O .elephant_pswd ,elephant_Task_ID =O0O0O00O0O00OOO0O .elephant_Task_ID )#line:189
                    OOOO0OO00OOO00OO0 =get_json_data (json_path ,O0O0O00O0O00OOO0O .len_new ,'authorization',OOO0O0O0O0OOOO00O )#line:190
                    if write_json_data (OOOO0OO00OOO00OO0 ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if OOO0OO00O0000OO00 ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as O0OO0OO000OO0O0O0 :#line:197
            print (O0OO0OO000OO0O0O0 )#line:198
    def sealing (OOO00OO0OOOOO00OO ):#line:201
        try :#line:202
            O00O000O0000OOOO0 =f'__{timi_new()}'#line:203
            OOO00OO0OOO0OOOO0 ={'source':'scsc','authorization':OOO00OO0OOOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000O0000OOOO0 ),'signstring':O00O000O0000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO00OO0OOO0OOOO0 )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =OOO00OO0OOO0OOOO0 )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO00OO0OOO0OOOO0 )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO00OO0OOO0OOOO0 )#line:218
            requests .request ('get',f'{host}/user',headers =OOO00OO0OOO0OOOO0 )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO00OO0OOO0OOOO0 )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO00OO0OOO0OOOO0 )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO00OO0OOO0OOOO0 )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =OOO00OO0OOO0OOOO0 )#line:223
            requests .request ('get',f'{host}/assets',headers =OOO00OO0OOO0OOOO0 )#line:224
        except Exception as OOO0O0OOO00OOOO00 :#line:225
            print (OOO0O0OOO00OOOO00 )#line:226
    def withdraw (OO000O0OO0OOOOO0O ):#line:230
        OOOOOOO000O0O0000 =f'__{timi_new()}'#line:231
        O0OO0OOO0O00000O0 ={'source':'scsc','authorization':OO000O0OO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000O0O0000 ),'signstring':OOOOOOO000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        OOOOOO00000OOOO0O =requests .request ('get',f'{host}/assets',headers =O0OO0OOO0O00000O0 ).json ()#line:243
        if 'status'in OOOOOO00000OOOO0O :#line:245
            if OOOOOO00000OOOO0O ['status']==200 :#line:246
                OO00000000OOO00O0 =OOOOOO00000OOOO0O ['data']['cash']#line:247
                if float (OO00000000OOO00O0 )>20 :#line:248
                    OOOOOOO000O0O0000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    O0OO0OOO0O00000O0 ={'authorization':OO000O0OO0OOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000O0O0000 ),'signstring':OOOOOOO000O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    O000OOOO000OO00OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    OOO0O0OO00OO00O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OO0OOO0O00000O0 ,data =O000OOOO000OO00OO ).json ()#line:262
                    print (OOO0O0OO00OO00O00 )#line:263
    def invitenum (O000O00O0O000O0O0 ):#line:266
        OO0000OOOO000O0OO =f'__{timi_new()}'#line:267
        OO00O0000O0OO0OO0 ={'source':'scsc','authorization':O000O00O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOO000O0OO ),'signstring':OO0000OOOO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        OOOO0O0O00OO0O0O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO00O0000O0OO0OO0 ).json ()#line:279
        if 'status'in OOOO0O0O00OO0O0O0 :#line:281
            if OOOO0O0O00OO0O0O0 ['status']==200 :#line:282
                O0OOO0000OO0OOOOO =OOOO0O0O00OO0O0O0 ['data']['invited_count']#line:283
                OO00OOOOO00O0O0O0 =OOOO0O0O00OO0O0O0 ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{O0OOO0000OO0OOOOO}丨间邀好友:{OO00OOOOO00O0O0O0}')#line:285
    def game_map (OO0OOO0000000O0OO ):#line:288
        try :#line:289
            OO000O00000OO00OO =f'__{timi_new()}'#line:290
            OO00O00OO0O00O00O ={'source':'scsc','authorization':OO0OOO0000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00000OO00OO ),'signstring':OO000O00000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            OOO0OOO0O0OO0OO0O =requests .request ('get',f'{host}/game/map',headers =OO00O00OO0O00O00O ).json ()#line:302
            if 'status'in OOO0OOO0O0OO0OO0O :#line:304
                if OOO0OOO0O0OO0OO0O ['status']==200 :#line:305
                    for O0O0O00OO0000O0O0 in OOO0OOO0O0OO0OO0O ['data']['list'][0 ]['crops']:#line:306
                        OOO000O0000O000OO =O0O0O00OO0000O0O0 ['level']#line:308
                        if OOO000O0000O000OO ==41 :#line:309
                            OOO0OO0OO0O0O00O0 =O0O0O00OO0000O0O0 ['crop_name']#line:310
                            O00000OO0OOOOOO00 =O0O0O00OO0000O0O0 ['count']#line:311
                            if O00000OO0OOOOOO00 >0 :#line:312
                                print (f'【农业资产】:{OOO0OO0OO0O0O00O0}丨数量:{O00000OO0OOOOOO00}')#line:313
        except Exception as OOOO0OO00OO00OO00 :#line:314
            print (OOOO0OO00OO00OO00 )#line:315
    def give_gold (O0OO00O000OO000OO ):#line:318
        try :#line:319
            O00O00O0O0000OO00 =f'__{timi_new()}'#line:320
            OOO00O0000O000000 ={'source':'scsc','authorization':O0OO00O000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000OO00 ),'signstring':O00O00O0O0000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            O0O0OOO0000O0OOOO =requests .request ('get',f'{host}/user',headers =OOO00O0000O000000 ).json ()#line:332
            if 'status'in O0O0OOO0000O0OOOO :#line:333
                if O0O0OOO0000O0OOOO ['status']==200 :#line:334
                    if float (O0OO00O000OO000OO .doneeNo )!=0 :#line:335
                        OO0O0OOOOOOO0O000 =O0O0OOO0000O0OOOO ['data']['assets']['gold']#line:336
                        if float (OO0O0OOOOOOO0O000 )>float (O0OO00O000OO000OO .innerId ):#line:337
                            OO0OO00O0OOO00O00 =int (float (OO0O0OOOOOOO0O000 )/1.1 )#line:338
                            O00O00O0O0000OO00 =f'_doneeNo={O0OO00O000OO000OO.doneeNo}&quantity={OO0OO00O0OOO00O00}_{timi_new()}'#line:339
                            OOO00O0000O000000 ={'source':'scsc','authorization':O0OO00O000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0000OO00 ),'signstring':O00O00O0O0000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            OOOO0O0000000O000 ={"quantity":OO0OO00O0OOO00O00 ,"doneeNo":O0OO00O000OO000OO .doneeNo }#line:354
                            OO00OOO0OOOOO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00O0000O000000 ,data =OOOO0O0000000O000 ).json ()#line:355
                            if 'status'in OO00OOO0OOOOO0O00 :#line:357
                                if OO00OOO0OOOOO0O00 ['status']==200 :#line:358
                                    if OO00OOO0OOOOO0O00 ['data']:#line:359
                                        print (f'【赠送种子】:赠送{OO0OO00O0OOO00O00}种子给{O0OO00O000OO000OO.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OO0OO0OOOOOO0OO0O :#line:363
            print (OO0OO0OOOOOO0OO0O )#line:364
    def invitation (OOO0OOOO00OOO0O0O ):#line:366
        try :#line:367
            _OO0O0OO00000OO000 =float (bundled_def ())/4 #line:368
            O0OOO0OOOO0000O0O =f'_innerId={int(_OO0O0OO00000OO000)}_{timi_new()}'#line:369
            OOO000O0OO00O0000 ={'source':'scsc','authorization':OOO0OOOO00OOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOOO0000O0O ),'signstring':O0OOO0OOOO0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            OO000OO0OO00O00O0 ={"innerId":int (_OO0O0OO00000OO000 )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO000O0OO00O0000 ,data =OO000OO0OO00O00O0 )#line:382
        except Exception as O0OO000O0O0O0000O :#line:383
            print (O0OO000O0O0O0000O )#line:384
    def winning_rewards (O00O0000O0OO0O00O ):#line:387
        try :#line:388
            O00OOO0O00OOO0OOO =f'__{timi_new()}'#line:389
            O00000O00O0O0O0O0 ={'source':'scsc','authorization':O00O0000O0OO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O00OOO0OOO ),'signstring':O00OOO0O00OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            O0O00OO0O000OOOO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00000O00O0O0O0O0 ).json ()#line:401
            if 'status'in O0O00OO0O000OOOO0 :#line:403
                if O0O00OO0O000OOOO0 ['status']==200 :#line:404
                    if O0O00OO0O000OOOO0 ['data']['amount']:#line:405
                        O0O0OOOO00OOO0OO0 =O0O00OO0O000OOOO0 ['data']['amount']['gold']#line:406
                        return O0O0OOOO00OOO0OO0 #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as OO00O0OO00O000OOO :#line:410
            print (OO00O0OO00O000OOO )#line:411
    def certification (OOO0000O0O0O0OO0O ):#line:414
        try :#line:415
            OOOO000O00O0OOOO0 =f'__{timi_new()}'#line:416
            O00O0O0O0O0OO0000 ={'source':'scsc','authorization':OOO0000O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00O0OOOO0 ),'signstring':OOOO000O00O0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            OOO0OOO0000O00OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00O0O0O0O0OO0000 ).json ()#line:428
            if 'status'in OOO0OOO0000O00OO0 :#line:430
                if OOO0OOO0000O00OO0 ['status']==200 :#line:431
                    if OOO0OOO0000O00OO0 ['data']['result']:#line:432
                        OOO0000O0OOO0000O =OOO0OOO0000O00OO0 ['data']['nick_name']#line:433
                        return OOO0000O0OOO0000O #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as O00O00O00000OO0OO :#line:437
            print (O00O00O00000OO0OO )#line:438
    def crops_illustrated (OO00000OOOO00O00O ):#line:441
        try :#line:442
            OOO0OOOOO0O0O000O =f'__{timi_new()}'#line:443
            O00000O000OO00OOO ={'source':'scsc','authorization':OO00000OOOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O0O000O ),'signstring':OOO0OOOOO0O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            O0O0OOOO0000OO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00000O000OO00OOO ).json ()#line:455
            if 'status'in O0O0OOOO0000OO0O0 :#line:457
                if O0O0OOOO0000OO0O0 ['status']==200 :#line:458
                    OOO00OOOOO000OOO0 =O0O0OOOO0000OO0O0 ['data'][0 ]['crops']#line:459
                    for O0OOOO00O0O000OOO in OOO00OOOOO000OOO0 :#line:460
                        if O0OOOO00O0O000OOO ['ill_clover_award']:#line:461
                            if float (O0OOOO00O0O000OOO ['ill_clover_award'])>1 :#line:462
                                if O0OOOO00O0O000OOO ['is_finish']:#line:463
                                    if not O0OOOO00O0O000OOO ['is_getit']:#line:464
                                        if OO00000OOOO00O00O .certification ()!='未实名':#line:465
                                            OOO0OOOOO0O0O000O =f'_award_level={O0OOOO00O0O000OOO["level"]}_{timi_new()}'#line:466
                                            O00000O000OO00OOO ={'source':'scsc','authorization':OO00000OOOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO0O0O000O ),'signstring':OOO0OOOOO0O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            OO0O0OOO00O00O0O0 ={"award_level":O0OOOO00O0O000OOO ['level']}#line:478
                                            O00OO0OOOOO000OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00000O000OO00OOO ,json =OO0O0OOO00O00O0O0 ).json ()#line:480
                                            if 'status'in O00OO0OOOOO000OOO :#line:481
                                                if O00OO0OOOOO000OOO ['status']==200 :#line:482
                                                    O0O0000O0OO0000O0 =O00OO0OOOOO000OOO ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{O0OOOO00O0O000OOO["crop_name"]}成就丨奖励{O0O0000O0OO0000O0}☘️')#line:485
                                                if O00OO0OOOOO000OOO ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{O00OO0OOOOO000OOO["message"]}')#line:487
        except Exception as OO0OOO0O00O0O0OO0 :#line:488
            print (OO0OOO0O00O0O0OO0 )#line:489
    def watched_ad (O0OOO000OO0000OOO ):#line:492
        try :#line:493
            O0O00OO0O0OO000OO =f'__{timi_new()}'#line:494
            O000O0000OOOOO000 ={'source':'scsc','authorization':O0OOO000OO0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O0OO000OO ),'signstring':O0O00OO0O0OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            OO000OO0000000O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000O0000OOOOO000 ).json ()#line:506
            if 'status'in OO000OO0000000O00 :#line:508
                if OO000OO0000000O00 ['status']==200 :#line:509
                    if 'offlineInfo'in OO000OO0000000O00 ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        O0O00O0O00O0O000O =OO000OO0000000O00 ['data']['offlineInfo']['off_minute']#line:512
                        O0OOOO0O000000O00 =float (OO000OO0000000O00 ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000O0000OOOOO000 ).json ()#line:515
                        time .sleep (2 )#line:516
                        OO0O00O0O0OO00O0O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0000OOOOO000 ).json ()#line:517
                        if 'status'in OO0O00O0O0OO00O0O :#line:519
                            if OO0O00O0O0OO00O0O ['status']==200 :#line:520
                                O00OO0OO00OO0OOOO =float (OO0O00O0O0OO00O0O ['data']['silver'])/1000000000000 #line:521
                                O0O00OO00O0OOOOO0 =str (O00OO0OO00OO0OOOO -O0OOOO0O000000O00 )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{O0O00O0O00O0O000O}分钟奖励🌱数量:{O0O00OO00O0OOOOO0}t粒')#line:523
        except Exception as OOOOO0OO00OO0OO0O :#line:524
            print (OOOOO0OO00OO0OO0O )#line:525
    def user_ad (O00O0OO0OO0OOOO00 ):#line:528
        try :#line:529
            O0OOO0OO0OOO0OO00 =f'__{timi_new()}'#line:530
            OO000O0OO000OO00O ={'source':'scsc','authorization':O00O0OO0OO0OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO0OOO0OO00 ),'signstring':O0OOO0OO0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            O0O00OOOO0O0OOOOO =requests .request ('get',f'{host}/user/ad',headers =OO000O0OO000OO00O ).json ()#line:542
            if 'status'in O0O00OOOO0O0OOOOO :#line:544
                if O0O00OOOO0O0OOOOO ['status']==200 :#line:545
                    OO000O00OOOO0OOOO =O0O00OOOO0O0OOOOO ['data']['max_time']#line:546
                    O00OO0O00OO0OOO0O =O0O00OOOO0O0OOOOO ['data']['watch_time']#line:547
                    OOO000O0O0OOOO0O0 =O0O00OOOO0O0OOOOO ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{OOO000O0O0OOOO0O0 + OO000O00OOOO0OOOO - O00OO0O00OO0OOO0O}次丨好友提供:{OOO000O0O0OOOO0O0}次')#line:549
                    if OOO000O0O0OOOO0O0 +OO000O00OOOO0OOOO -O00OO0O00OO0OOO0O >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        OOOO0OO0000O00O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO000O0OO000OO00O ).json ()#line:552
                        if 'status'in OOOO0OO0000O00O00 :#line:554
                            if OOOO0OO0000O00O00 ['status']==200 :#line:555
                                OO0O000O0O000OOOO =float (OOOO0OO0000O00O00 ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(OO0O000O0O000OOOO)}t粒')#line:557
                                return True #line:558
                            if OOOO0OO0000O00O00 ['status']==500 :#line:559
                                OOO0O000O0O0000O0 =OOOO0OO0000O00O00 ['message']#line:560
                                print (f'【获取种子】:{OOO0O000O0O0000O0}')#line:561
                                return False #line:562
        except Exception as OO00OO0OOO0000OO0 :#line:563
            print (OO00OO0OOO0000OO0 )#line:564
    def synthetic (OO00O0O0OO0O0OO0O ):#line:567
        global id ,g #line:568
        try :#line:569
            O0OO0OO000O00O0OO =OO00O0O0OO0O0OO0O .level_new ()#line:570
            OO00000000O0OO0O0 =random .randint (9 ,11 )#line:571
            OOOOOOOO0O0OO0000 =f'_site=8&targetSite={OO00000000O0OO0O0}_{timi_new()}'#line:572
            O00OO0OOOO00O00OO ={'source':'scsc','authorization':OO00O0O0OO0O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OOOOOOOO0O0OO0000 ),'signstring':OOOOOOOO0O0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            O0O0OO00OOOOO0O00 ={"site":int (8 ),"targetSite":int (OO00000000O0OO0O0 )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0OOOO00O00OO ,json =O0O0OO00OOOOO0O00 )#line:585
            while True :#line:586
                OO000OO0000O0OOO0 =f'__{timi_new()}'#line:587
                O0O0OO0OOO00O0OOO ={'source':'scsc','authorization':OO00O0O0OO0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO0000O0OOO0 ),'signstring':OO000OO0000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                OO0O00OOOO00O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OOO00O0OOO ).json ()#line:599
                if 'status'in OO0O00OOOO00O0OO0 :#line:601
                    if OO0O00OOOO00O0OO0 ['status']==200 :#line:602
                        OO000O0OOO00OO0O0 =OO0O00OOOO00O0OO0 ['data']['cropList']#line:603
                        O0O00O00O00O00O00 =OO0O00OOOO00O0OO0 ['data']['gameCoreDataDBid']#line:604
                        O0OOO00000OO0O000 =float (OO0O00OOOO00O0OO0 ['data']['silver'])/1000000000000 #line:605
                        OOO0O00O0OOOO0OO0 =0 #line:610
                        for O000O0OOOOOOO0O0O in OO000O0OOO00OO0O0 :#line:611
                            if not O000O0OOOOOOO0O0O :#line:612
                                OOOO0O0OO00OOOO00 =f'_crop_id={O0O00O00O00O00O00}&site={OOO0O00O0OOOO0OO0}_{OO00O0O0OO0O0OO0O.time}'#line:613
                                O0OOO00O0O00000OO ={'source':'scsc','authorization':OO00O0O0OO0O0OO0O .token ,'timestamp':OO00O0O0OO0O0OO0O .time ,'sign':sign (OOOO0O0OO00OOOO00 ),'signstring':OOOO0O0OO00OOOO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                O000OO0000O0O0O00 ={"site":OOO0O00O0OOOO0OO0 ,"crop_id":O0O00O00O00O00O00 }#line:624
                                OOO00OO0OOO00O00O =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOO00O0O00000OO ,data =O000OO0000O0O0O00 ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in OOO00OO0OOO00O00O :#line:628
                                    if OOO00OO0OOO00O00O ['status']==200 :#line:629
                                        if OOO00OO0OOO00O00O ['message']=='种子数量不足':#line:630
                                            O0OO0OO000O00O0OO =OO00O0O0OO0O0OO0O .level_new ()#line:631
                                            print (f'【种植合成】:{OOO00OO0OOO00O00O["message"]}')#line:632
                                            if not OO00O0O0OO0O0OO0O .user_ad ():#line:633
                                                return False #line:634
                                    if OOO00OO0OOO00O00O ['status']==500 :#line:635
                                        print (f'【种植合成】:{OOO00OO0OOO00O00O["message"]}')#line:636
                                        return False #line:637
                            OOO0O00O0OOOO0OO0 +=1 #line:638
                        OOO0OO0O00OO0OO00 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OOO00O0OOO ).json ()#line:639
                        O00O0OOOOO00O0O00 =OOO0OO0O00OO0OO00 ['data']['cropList']#line:640
                        OO00OO00OO00OO00O =False #line:641
                        for O000O0OOOOOOO0O0O in range (12 ):#line:642
                            id =O00O0OOOOO00O0O00 [O000O0OOOOOOO0O0O ]['level']#line:643
                            if float (O0OO0OO000O00O0OO )-float (id )>9 :#line:644
                                OO00O00OOOOO0OO0O =f'_site={O000O0OOOOOOO0O0O}_{timi_new()}'#line:645
                                O000O00000OOO0O00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00O0O0OO0O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OO00O00OOOOO0OO0O ),'signstring':OO00O00OOOOO0OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O00O0OO0OOOO0O00O ={"site":O000O0OOOOOOO0O0O }#line:657
                                O0O00O00000O000OO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O00000OOO0O00 ,data =O00O0OO0OOOO0O00O ).json ()#line:659
                                if 'status'in O0O00O00000O000OO :#line:660
                                    if O0O00O00000O000OO ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for OO000O0OO0OO0O00O in range (11 ):#line:664
                                    OOO0O0000000OOO00 =OO000O0OO0OO0O00O +1 #line:665
                                    g =O00O0OOOOO00O0O00 [OOO0O0000000OOO00 ]['level']#line:666
                                    if id ==g :#line:667
                                        O000O0O0O0O00O0O0 =OO000O0OO0OO0O00O +2 #line:668
                                        if O000O0O0O0O00O0O0 !=O000O0OOOOOOO0O0O +1 :#line:669
                                            OOOO0O0O00O00O000 =O000O0OOOOOOO0O0O +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            OOOOOOOO0O0OO0000 =f'_site={OOOO0O0O00O00O000 - 1}&targetSite={O000O0O0O0O00O0O0 - 1}_{timi_new()}'#line:673
                                            O00OO0OOOO00O00OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00O0O0OO0O0OO0O .token ,'timestamp':timi_new (),'sign':sign (OOOOOOOO0O0OO0000 ),'signstring':OOOOOOOO0O0OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            O0000OOOOOOOOO000 ={"site":int (OOOO0O0O00O00O000 -1 ),"targetSite":int (O000O0O0O0O00O0O0 -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0OOOO00O00OO ,json =O0000OOOOOOOOO000 )#line:692
                                            OO00OO00OO00OO00O =True #line:694
                                    if OO00OO00OO00OO00O :#line:695
                                        break #line:696
                                if OO00OO00OO00OO00O :#line:697
                                    break #line:698
        except :#line:699
            OO00O0O0OO0O0OO0O .synthetic ()#line:700
    def level_new (O00OOO0O00O0000OO ):#line:703
        try :#line:704
            OO0OO000OO00OOO0O =f'__{timi_new()}'#line:705
            O0OOO000OOO000O0O ={'source':'scsc','authorization':O00OOO0O00O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO00OOO0O ),'signstring':OO0OO000OO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OO0O0O000OOO0O0O0 =requests .request ('get',f'{host}/user',headers =O0OOO000OOO000O0O ).json ()#line:717
            if 'status'in OO0O0O000OOO0O0O0 :#line:718
                if OO0O0O000OOO0O0O0 ['status']==200 :#line:719
                    return float (OO0O0O000OOO0O0O0 ['data']['level'])#line:720
        except Exception as O00000OO00OOOO00O :#line:721
            print (O00000OO00OOOO00O )#line:722
    def propsraffle (O000O0OO00OOO00OO ):#line:725
        try :#line:726
            while True :#line:727
                OO000O0O0O0O00OOO =f'__{timi_new()}'#line:728
                O00000OO00O0OOO00 ={'source':'scsc','authorization':O000O0OO00OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0O0O00OOO ),'signstring':OO000O0O0O0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                O0000000000OO0OOO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00000OO00O0OOO00 ).json ()#line:740
                if 'status'in O0000000000OO0OOO :#line:742
                    if O0000000000OO0OOO ['status']==200 :#line:743
                        O000OO000OO00O0O0 =O0000000000OO0OOO ['data']['rows']#line:744
                        OO0O0OOOO0000O00O =O0000000000OO0OOO ['data']['vstate']#line:745
                        if O000OO000OO00O0O0 ==5 or O000OO000OO00O0O0 ==6 or O000OO000OO00O0O0 ==7 :#line:746
                            O0OOOOO0O0OO0O0OO =O0000000000OO0OOO ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{O0OOOOO0O0OO0O0OO}')#line:748
                        if O000OO000OO00O0O0 ==1 or O000OO000OO00O0O0 ==2 or O000OO000OO00O0O0 ==3 :#line:749
                            OOOOO0OO0OO00OOO0 =O0000000000OO0OOO ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0OO0OO00OOO0}')#line:751
                        if O000OO000OO00O0O0 ==4 or O000OO000OO00O0O0 ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if O000OO000OO00O0O0 =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as O0O0000O0O00OO0OO :#line:793
            print (O0O0000O0O00OO0OO )#line:794
    def friends_invitation (O0OOOOOO0000O0000 ):#line:797
        try :#line:798
            OOO000OO0OOOO00O0 =f'__{timi_new()}'#line:799
            O00O00OOOO000OOOO ={'source':'scsc','authorization':O0OOOOOO0000O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OO0OOOO00O0 ),'signstring':OOO000OO0OOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            O00O0O0O0OO0OOO00 =requests .request ('get',f'{host}/friends',headers =O00O00OOOO000OOOO ).json ()#line:811
            if 'status'in O00O0O0O0OO0OOO00 :#line:812
                if O00O0O0O0OO0OOO00 ['status']==200 :#line:813
                    OOOOOOO00OOOO0000 =O00O0O0O0OO0OOO00 ['data']['myInviteter']#line:814
                    if OOOOOOO00OOOO0000 :#line:815
                        OO000O000OOO0O000 =OOOOOOO00OOOO0000 ['user']['nickname']#line:816
                        OOOO0OO0000OOOOOO =O0OOOOOO0000O0000 .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{OO000O000OOO0O000}丨实名:{OOOO0OO0000OOOOOO}')#line:818
                    else :#line:819
                        if O0OOOOOO0000O0000 .innerId !='0':#line:820
                            O0OOOOOO0000O0000 .invitation ()#line:821
        except Exception as O00OO000O0OOO00O0 :#line:822
            print (O00OO000O0OOO00O0 )#line:823
    def add_clover (O0O00000O0OOOO00O ):#line:826
        global golden_seed #line:827
        try :#line:828
            OO0OOO0O0000O0O0O =f'__{timi_new()}'#line:829
            OOO000OO0000O00OO ={'source':'scsc','authorization':O0O00000O0OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0000O0O0O ),'signstring':OO0OOO0O0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            OOO0000OO0000O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO000OO0000O00OO ).json ()#line:841
            if 'status'in OOO0000OO0000O0O0 :#line:843
                if OOO0000OO0000O0O0 ['status']==200 :#line:844
                    O0OO000OO0OOOOO00 =OOO0000OO0000O0O0 ['data']['clover']#line:845
                    O0O00000O00O0OOOO =OOO0000OO0000O0O0 ['data']['used_clover']#line:846
                    OO0OO00O0O0OOOO00 =float (O0OO000OO0OOOOO00 )-float (O0O00000O00O0OOOO )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O00000O00O0OOOO}')#line:848
                    if O0O00000O0OOOO00O .certification ()!='未实名':#line:849
                        if OO0OO00O0O0OOOO00 >1 :#line:850
                            OO0OOO0O0000O0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO0OO00O0O0OOOO00)}_{timi_new()}'#line:851
                            O00OO0OO0O0OOO0O0 ={'source':'scsc','authorization':O0O00000O0OOOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O0000O0O0O ),'signstring':OO0OOO0O0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            O0O0OOOOOO0O00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO0OO00O0O0OOOO00 )}#line:863
                            OOO0OOOO000O0O000 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00OO0OO0O0OOO0O0 ,data =O0O0OOOOOO0O00O0O ).json ()#line:864
                            if 'status'in OOO0OOOO000O0O000 :#line:866
                                if OOO0OOOO000O0O000 ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{OOO0OOOO000O0O000["data"]}丨数量:{OO0OO00O0O0OOOO00}')#line:868
                                if OOO0OOOO000O0O000 ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{OOO0OOOO000O0O000["message"]}')#line:870
            OO00O0OOOO00O0OO0 =requests .request ('get',f'{host}/lottery',headers =OOO000OO0000O00OO ).json ()#line:871
            O0OO0O000000O00O0 =O0O00000O0OOOO00O .winning_rewards ()#line:873
            if 'status'in OO00O0OOOO00O0OO0 :#line:874
                if OO00O0OOOO00O0OO0 ['status']==200 :#line:875
                    OOOO00OO0OO0O0OO0 =OO00O0OOOO00O0OO0 ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (OOOO00OO0OO0O0OO0 )#line:877
                    OOOO0O0OOOO0OO00O =OO00O0OOOO00O0OO0 ['data'][1 ]['value']#line:878
                    OOOOO0OOOO000O000 =OO00O0OOOO00O0OO0 ['data'][0 ]['join_number']#line:879
                    OO000000OOOOO0OO0 =int (float (OO00O0OOOO00O0OO0 ['data'][0 ]['totalValue']))#line:880
                    O000OO0OOO0000OO0 =float (OOOO0O0OOOO0OO00O /OO000000OOOOO0OO0 )*10000 #line:881
                    OOOO00OO00O000O00 =OO000000OOOOO0OO0 /OOOOO0OOOO000O000 #line:882
                    print (f'【参与抽奖】:预计每天中{str(OOOO00OO0OO0O0OO0)[:6]}颗金种子丨好友收益:{str(O0OO0O000000O00O0)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(O000OO0OOO0000OO0)[:6]}颗金种子丨☘️人均:{str(OOOO00OO00O000O00)[:7]}️')#line:884
        except Exception as OOO0O0O0O00OO00O0 :#line:885
            print (OOO0O0O0O00OO00O0 )#line:886
    def energy (OOO00O0000OOO00OO ):#line:890
        try :#line:891
            while True :#line:892
                O0O00OO0OO000OOOO =f'__{timi_new()}'#line:893
                OOOO00O00O0O0OOOO ={'source':'scsc','authorization':OOO00O0000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OO000OOOO ),'signstring':O0O00OO0OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                OOOO00O000OO00000 =requests .request ('get',f'{host}/energy/general',headers =OOOO00O00O0O0OOOO ).json ()#line:905
                if 'status'in OOOO00O000OO00000 :#line:907
                    if OOOO00O000OO00000 ['status']==200 :#line:908
                        OOOO0OOO0OOOO0OOO =OOOO00O000OO00000 ['data']['ordinary_water']#line:909
                        OOO0OO000OOO0O0O0 =OOOO00O000OO00000 ['data']['ordinary_fertilizer']#line:910
                        OOOO00OO0000OO0OO =OOOO00O000OO00000 ['data']['videoStatus']#line:911
                        O00O00OOOOO00O00O =OOOO00O000OO00000 ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(OOO0OO000OOO0O0O0).split(".")[0]}丨水滴:{str(OOOO0OOO0OOOO0OOO).split(".")[0]}')#line:913
                        if float (OOO0OO000OOO0O0O0 )<96 :#line:914
                            if OOOO00OO0000OO0OO :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                OO0OO000O000OO000 =99 -float (OOO0OO000OOO0O0O0 )#line:917
                                OOOOO00OO00O0OO00 ={"fertilizer":str (OO0OO000O000OO000 ).split ('.')[0 ]}#line:918
                                O0O000O0O0000000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO00O00O0O0OOOO ).json ()#line:919
                                if 'status'in O0O000O0O0000000O :#line:921
                                    if O0O000O0O0000000O ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O0O0000000O["message"]}')#line:923
                                    if O0O000O0O0000000O ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O0O0000000O["message"]}')#line:925
                                        break #line:926
                                if float (OOO0OO000OOO0O0O0 )<78 :#line:928
                                    OO0OO000O000OO000 =80 -float (OOO0OO000OOO0O0O0 )#line:929
                                    OOOO00OO00OO0O00O =f'_fertilizer={int(OO0OO000O000OO000)}_{timi_new()}'#line:930
                                    OO000O0OOO00OOO0O ={'source':'scsc','authorization':OOO00O0000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00OO0O00O ),'signstring':OOOO00OO00OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    O00O00O0000OOOO0O ={"fertilizer":int (OO0OO000O000OO000 )}#line:942
                                    OO00OOO0000OOOO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO000O0OOO00OOO0O ,data =O00O00O0000OOOO0O ).json ()#line:944
                                    if 'status'in OO00OOO0000OOOO00 :#line:946
                                        if OO00OOO0000OOOO00 ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{OO00OOO0000OOOO00["message"]}丨数量:{int(OO0OO000O000OO000)}')#line:948
                                        if OO00OOO0000OOOO00 ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{OO00OOO0000OOOO00["message"]}丨数量:{int(OO0OO000O000OO000)}')#line:950
                                            OOOO0OO00OOOO00O0 =OO00OOO0000OOOO00 ["message"].split ('-')[1 ]#line:951
                                            O00OO0O00OOOOO00O =f'__{timi_new()}'#line:952
                                            OOO0O0O00O0OO0000 ={'source':'scsc','authorization':OOO00O0000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00OOOOO00O ),'signstring':O00OO0O00OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            OO0O000O0OOO0O0O0 =requests .request ('get',f'{host}/user',headers =OOO0O0O00O0OO0000 ).json ()#line:964
                                            if 'status'in OO0O000O0OOO0O0O0 :#line:965
                                                if OO0O000O0OOO0O0O0 ['status']==200 :#line:966
                                                    O000O0O0O00OOO000 =OO0O000O0OOO0O0O0 ['data']['inner_id']#line:967
                                                    if give_gold (O000O0O0O00OOO000 ,float (OOOO0OO00OOOO00O0 )+1 ):#line:968
                                                        OOO00O0000OOO00OO .energy ()#line:969
                        if float (OOOO0OOO0OOOO0OOO )<880 :#line:970
                            if O00O00OOOOO00O00O :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                OO0OO0O0O00O0000O =999 -float (OOOO0OOO0OOOO0OOO )#line:973
                                OO00OOO0O0O000OO0 ={"water":str (OO0OO0O0O00O0000O ).split ('.')[0 ]}#line:974
                                OOOO0O0000OOO0O0O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO00O00O0O0OOOO ).json ()#line:975
                                if 'status'in OOOO0O0000OOO0O0O :#line:977
                                    if OOOO0O0000OOO0O0O ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O0000OOO0O0O["message"]}')#line:979
                                    if OOOO0O0000OOO0O0O ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OOOO0O0000OOO0O0O["message"]}')#line:981
                                        break #line:982
                                if float (OOOO0OOO0OOOO0OOO )<780 :#line:983
                                    OO0OO0O0O00O0000O =800 -float (OOOO0OOO0OOOO0OOO )#line:984
                                    OOO000OOO00O00000 =f'_water={int(OO0OO0O0O00O0000O)}_{timi_new()}'#line:985
                                    O000O0O0000OO0OO0 ={'source':'scsc','authorization':OOO00O0000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOO00O00000 ),'signstring':OOO000OOO00O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    OOOO00OO0OO00OOO0 ={"water":int (OO0OO0O0O00O0000O )}#line:997
                                    O00000OOOOO0OO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000O0O0000OO0OO0 ,data =OOOO00OO0OO00OOO0 ).json ()#line:999
                                    if 'status'in O00000OOOOO0OO00O :#line:1001
                                        if O00000OOOOO0OO00O ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{O00000OOOOO0OO00O["message"]}丨数量:{int(OO0OO0O0O00O0000O)}')#line:1003
                                        if O00000OOOOO0OO00O ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{O00000OOOOO0OO00O["message"]}丨数量:{int(OO0OO0O0O00O0000O)}')#line:1005
                                            OOOO0OO00OOOO00O0 =O00000OOOOO0OO00O ["message"].split ('-')[1 ]#line:1006
                                            O00OO0O00OOOOO00O =f'__{timi_new()}'#line:1007
                                            OOO0O0O00O0OO0000 ={'source':'scsc','authorization':OOO00O0000OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00OOOOO00O ),'signstring':O00OO0O00OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            OO0O000O0OOO0O0O0 =requests .request ('get',f'{host}/user',headers =OOO0O0O00O0OO0000 ).json ()#line:1019
                                            if 'status'in OO0O000O0OOO0O0O0 :#line:1020
                                                if OO0O000O0OOO0O0O0 ['status']==200 :#line:1021
                                                    O000O0O0O00OOO000 =OO0O000O0OOO0O0O0 ['data']['inner_id']#line:1022
                                                    if give_gold (O000O0O0O00OOO000 ,float (OOOO0OO00OOOO00O0 )+1 ):#line:1023
                                                        OOO00O0000OOO00OO .energy ()#line:1024
                        break #line:1025
        except Exception as O0O0O0OOOOO0O0OO0 :#line:1027
            print (O0O0O0OOOOO0O0OO0 )#line:1028
def bundled_def ():#line:1030
    O00OOO00OO00O00O0 =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return O00OOO00OO00O00O0 [random .randint (0 ,len (O00OOO00OO00O00O0 )-1 )]#line:1032
def version_of_the_validation ():#line:1036
    return str ((89 -56 )/10 )#line:1037
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
        OOOOOO0000OOO000O =gitee_edition ()#line:1062
        if version_of_the_validation ()<OOOOOO0000OOO000O ['CityEarth']['edition']:#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0000OOO000O["CityEarth"]["edition"]}   ❌')#line:1064
            print (f'更新内容=>>{OOOOOO0000OOO000O["CityEarth"]["content"]}   🎉')#line:1065
        else :#line:1066
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOOO0000OOO000O["CityEarth"]["edition"]}   ✅')#line:1067
            print (f'更新内容=>> {OOOOOO0000OOO000O["CityEarth"]["content"]}   🎉')#line:1068
    except Exception as O00O0O0O0000OOO0O :#line:1069
        print (O00O0O0O0000OOO0O )#line:1070
def sc3 ():#line:1072
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1073
if __name__ =='__main__':#line:1077
    start ()#line:1078
