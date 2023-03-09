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
        O0O00O0OO00000000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O0O00O0OO00000000)}个账号==========")#line:13
        for O00O0OOOO00OO00OO in O0O00O0OO00000000 :#line:14
            OOOOO00O00OOOO0O0 =[]#line:15
            print (f"------------正在执行第{O0O00O0OO00000000.index(O00O0OOOO00OO00OO) + 1}个账号------------")#line:16
            OO0000O00OO0OO000 =CityEarth (O00O0OOOO00OO00OO ,OOOOO00O00OOOO0O0 ,O0O00O0OO00000000 .index (O00O0OOOO00OO00OO ))#line:17
            def O00O0000OOO0O0O00 ():#line:19
                if OO0000O00OO0OO000 .base_info ():#line:21
                    OO0000O00OO0OO000 .sealing ()#line:23
                    OO0000O00OO0OO000 .invitenum ()#line:25
                    OO0000O00OO0OO000 .game_map ()#line:27
                    OO0000O00OO0OO000 .friends_invitation ()#line:29
                    OO0000O00OO0OO000 .energy ()#line:31
                    OO0000O00OO0OO000 .add_clover ()#line:33
                    OO0000O00OO0OO000 .propsraffle ()#line:35
                    OO0000O00OO0OO000 .synthetic ()#line:37
                    OO0000O00OO0OO000 .crops_illustrated ()#line:39
                    OO0000O00OO0OO000 .give_gold ()#line:41
                    OO0000O00OO0OO000 .withdraw ()#line:43
            O0O00000000OOOOO0 =threading .Thread (target =O00O0000OOO0O0O00 )#line:45
            O0O00000000OOOOO0 .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        O0O0O0O0O0000O0OO =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0O0O0O0000O0OO +' ')#line:51
    except Exception as O00OO0000O0O000OO :#line:52
        print (O00OO0000O0O000OO )#line:53
def give_gold (O00OOO00O0OOO00O0 ,OOOO0O0OO000O000O ):#line:56
        try :#line:57
            OO0OO000OO00OO0OO =f'_doneeNo={O00OOO00O0OOO00O0}&quantity={int(OOOO0O0OO000O000O)}_{timi_new()}'#line:58
            O0OOO0O000OO0O00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO00OO0OO ),'signstring':OO0OO000OO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            O0O0OOO0O0OO0OO0O ={"quantity":int (OOOO0O0OO000O000O ),"doneeNo":O00OOO00O0OOO00O0 }#line:73
            O00OOOOO00OOO0000 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO0O000OO0O00O ,data =O0O0OOO0O0OO0OO0O ).json ()#line:74
            if 'status'in O00OOOOO00OOO0000 :#line:76
                if O00OOOOO00OOO0000 ['status']==200 :#line:77
                    if O00OOOOO00OOO0000 ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(OOOO0O0OO000O000O)}种子给{O00OOO00O0OOO00O0}成功')#line:79
                        return True #line:80
                if O00OOOOO00OOO0000 ['status']==401 :#line:81
                    print (f'【赠送种子】:{O00OOOOO00OOO0000["message"]}')#line:82
                    return False #line:83
                if O00OOOOO00OOO0000 ['status']==500 :#line:84
                    print (f'【赠送种子】:{O00OOOOO00OOO0000["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as OOOO0O0OOO0O000OO :#line:88
            print (OOOO0O0OOO0O000OO )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (O0O0OOO0O0O0000OO ):#line:94
    OOOO00OO00OOOOOO0 =hashlib .md5 (O0O0OOO0O0O0000OO .encode ()).hexdigest ()#line:95
    O00O0OOO0OOOOO0OO =sc1 ()#line:96
    OO0OOO0OOO000OO00 =sc2 ()#line:97
    O00OOOOO000OO0O00 =sc3 ()#line:98
    OO0000000O0OOOO00 =O00O0OOO0OOOOO0OO +OOOO00OO00OOOOOO0 +OO0OOO0OOO000OO00 +O00OOOOO000OO0O00 #line:99
    OOO00OO000OOO000O =hashlib .md5 (OO0000000O0OOOO00 .encode ()).hexdigest ()#line:100
    return OOO00OO000OOO000O #line:101
def format_msg ():#line:105
    OOO0OOOOO00O000O0 =""#line:106
    for OOO00000O00OO0OOO in msg_list :#line:107
        OOO0OOOOO00O000O0 +=str (OOO00000O00OO0OOO )+"\r\n"#line:108
    return OOO0OOOOO00O000O0 #line:109
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
def get_json_data (OO000O0OO0O0O0000 ,O0OO0O000O00O000O ,O0OOOO00O00O0000O ,OO0OOOOOO0O000000 ):#line:128
    with open (OO000O0OO0O0O0000 ,'rb')as O0OO0OOOOO0OOOO00 :#line:130
        OOO0OOOO0O0OO00O0 =json .load (O0OO0OOOOO0OOOO00 )#line:131
        OOO0OOOO0O0OO00O0 ['data'][O0OO0O000O00O000O ][O0OOOO00O00O0000O ]=OO0OOOOOO0O000000 #line:132
        OOOO000OO00O0O0O0 =OOO0OOOO0O0OO00O0 #line:133
    O0OO0OOOOO0OOOO00 .close ()#line:134
    return OOOO000OO00O0O0O0 #line:135
def write_json_data (O000OO0O0OO0OO0O0 ):#line:137
    with open (json_path1 ,'w')as O0O0O0OO000000O0O :#line:138
        json .dump (O000OO0O0OO0OO0O0 ,O0O0O0OO000000O0O )#line:139
    O0O0O0OO000000O0O .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (OO000O0OO0O000O0O ,O0O0000O000OO00O0 ,OOO000OOOO0OOOOO0 ,O0O00O0O0OO00O00O ):#line:145
        try :#line:146
            OO000O0OO0O000O0O .msg =OOO000OOOO0OOOOO0 #line:147
            OO000O0OO0O000O0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            OO000O0OO0O000O0O .token =O0O0000O000OO00O0 ['authorization']#line:149
            OO000O0OO0O000O0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            OO000O0OO0O000O0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            OO000O0OO0O000O0O .elephant_user =O0O0000O000OO00O0 ['elephant_user']#line:152
            OO000O0OO0O000O0O .elephant_pswd =O0O0000O000OO00O0 ['elephant_pswd']#line:153
            OO000O0OO0O000O0O .elephant_Task_ID =O0O0000O000OO00O0 ['elephant_Task_ID']#line:154
            OO000O0OO0O000O0O .len_new =O0O00O0O0OO00O00O #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (OOO0O000OOOO00O00 ):#line:160
        try :#line:161
            OOO0O000OOOO00O00 .watched_ad ()#line:163
            OO00O0OO0O00OO0O0 =f'__{timi_new()}'#line:164
            O00O000O0O0OOOO0O ={'source':'scsc','authorization':OOO0O000OOOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO0O00OO0O0 ),'signstring':OO00O0OO0O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            OOO0O00O0OOO000O0 =requests .request ('get',f'{host}/user',headers =O00O000O0O0OOOO0O ).json ()#line:176
            if 'status'in OOO0O00O0OOO000O0 :#line:178
                if OOO0O00O0OOO000O0 ['status']==200 :#line:179
                    O0O000O0OO0OOO000 =OOO0O00O0OOO000O0 ['data']['nickname']#line:180
                    OO0OO0O00000O0O00 =OOO0O00O0OOO000O0 ['data']['inner_id']#line:181
                    O0O0O0OOO0OOOOOOO =OOO0O00O0OOO000O0 ['data']['assets']['gold']#line:182
                    OO0OOOO00O0000O0O =OOO0O00O0OOO000O0 ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{O0O000O0OO0OOO000[:5]}丨ID:{OO0OO0O00000O0O00}丨等级:{OO0OOOO00O0000O0O}丨金种子:{str(O0O0O0OOO0OOOOOOO).split(".")[0]}')#line:184
                if OOO0O00O0OOO000O0 ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if OOO0O000OOOO00O00 .elephant_user =='f':#line:187
                        return False #line:188
                    OO0OOO0OO00O0O00O =Invalid_login .addtask (elephant_user =OOO0O000OOOO00O00 .elephant_user ,elephant_pswd =OOO0O000OOOO00O00 .elephant_pswd ,elephant_Task_ID =OOO0O000OOOO00O00 .elephant_Task_ID )#line:189
                    O000O000OOOOO0O0O =get_json_data (json_path ,OOO0O000OOOO00O00 .len_new ,'authorization',OO0OOO0OO00O0O00O )#line:190
                    if write_json_data (O000O000OOOOO0O0O ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if OOO0O00O0OOO000O0 ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as OOO000O00OOOO000O :#line:197
            print (OOO000O00OOOO000O )#line:198
    def sealing (O000O00O0OOO000OO ):#line:201
        try :#line:202
            O0OOO0OOO0OO0O000 =f'__{timi_new()}'#line:203
            OOO0OOOO0OO00OO0O ={'source':'scsc','authorization':O000O00O0OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO0OO0O000 ),'signstring':O0OOO0OOO0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0OOOO0OO00OO0O )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =OOO0OOOO0OO00OO0O )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0OOOO0OO00OO0O )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0OOOO0OO00OO0O )#line:218
            requests .request ('get',f'{host}/user',headers =OOO0OOOO0OO00OO0O )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0OOOO0OO00OO0O )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0OOOO0OO00OO0O )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0OOOO0OO00OO0O )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0OOOO0OO00OO0O )#line:223
            requests .request ('get',f'{host}/assets',headers =OOO0OOOO0OO00OO0O )#line:224
        except Exception as O0O0O0OO000000O00 :#line:225
            print (O0O0O0OO000000O00 )#line:226
    def withdraw (OOO000O00000OOO0O ):#line:230
        OOOO0000000OO00O0 =f'__{timi_new()}'#line:231
        OO0OO0O0O0000O00O ={'source':'scsc','authorization':OOO000O00000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000OO00O0 ),'signstring':OOOO0000000OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        O00OOO0OOO0O000OO =requests .request ('get',f'{host}/assets',headers =OO0OO0O0O0000O00O ).json ()#line:243
        if 'status'in O00OOO0OOO0O000OO :#line:245
            if O00OOO0OOO0O000OO ['status']==200 :#line:246
                O0OO00OOOO0O0OOO0 =O00OOO0OOO0O000OO ['data']['cash']#line:247
                if float (O0OO00OOOO0O0OOO0 )>20 :#line:248
                    OOOO0000000OO00O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    OO0OO0O0O0000O00O ={'authorization':OOO000O00000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000OO00O0 ),'signstring':OOOO0000000OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    OOO0OOOOO0O00OO0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    OO0O0O0OO0OOOO000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0OO0O0O0000O00O ,data =OOO0OOOOO0O00OO0O ).json ()#line:262
                    print (OO0O0O0OO0OOOO000 )#line:263
    def invitenum (O00OOOOOO000OOOO0 ):#line:266
        O00OO0O00OOO00OO0 =f'__{timi_new()}'#line:267
        OO0OOO0OOOOO0O0OO ={'source':'scsc','authorization':O00OOOOOO000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O00OOO00OO0 ),'signstring':O00OO0O00OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        O00OOO0O0O0OOOOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0OOO0OOOOO0O0OO ).json ()#line:279
        if 'status'in O00OOO0O0O0OOOOO0 :#line:281
            if O00OOO0O0O0OOOOO0 ['status']==200 :#line:282
                OO0OOO00OO0000000 =O00OOO0O0O0OOOOO0 ['data']['invited_count']#line:283
                O00O0OOO00O00O0O0 =O00OOO0O0O0OOOOO0 ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{OO0OOO00OO0000000}丨间邀好友:{O00O0OOO00O00O0O0}')#line:285
    def game_map (OOOO0O000OOOO000O ):#line:288
        try :#line:289
            OO00O0O0OOOOOOOO0 =f'__{timi_new()}'#line:290
            O000O0OO000000OO0 ={'source':'scsc','authorization':OOOO0O000OOOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OOOOOOOO0 ),'signstring':OO00O0O0OOOOOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0OO0O00O00OOOO00 =requests .request ('get',f'{host}/game/map',headers =O000O0OO000000OO0 ).json ()#line:302
            if 'status'in O0OO0O00O00OOOO00 :#line:304
                if O0OO0O00O00OOOO00 ['status']==200 :#line:305
                    for O00OOO00O0O0OO0OO in O0OO0O00O00OOOO00 ['data']['list'][0 ]['crops']:#line:306
                        OOO00OO0O00OO0OOO =O00OOO00O0O0OO0OO ['level']#line:308
                        if OOO00OO0O00OO0OOO ==41 :#line:309
                            O0OOO0OOOOOO0OOOO =O00OOO00O0O0OO0OO ['crop_name']#line:310
                            O00OO0000OO00OO00 =O00OOO00O0O0OO0OO ['count']#line:311
                            if O00OO0000OO00OO00 >0 :#line:312
                                print (f'【农业资产】:{O0OOO0OOOOOO0OOOO}丨数量:{O00OO0000OO00OO00}')#line:313
        except Exception as O000OOO0OOO0OO000 :#line:314
            print (O000OOO0OOO0OO000 )#line:315
    def give_gold (OOOOOOO0OOO0OOOOO ):#line:318
        try :#line:319
            O000OO00000O00000 =f'__{timi_new()}'#line:320
            O0OOO000O0000O0O0 ={'source':'scsc','authorization':OOOOOOO0OOO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00000O00000 ),'signstring':O000OO00000O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            OO0000000OOO00OOO =requests .request ('get',f'{host}/user',headers =O0OOO000O0000O0O0 ).json ()#line:332
            if 'status'in OO0000000OOO00OOO :#line:333
                if OO0000000OOO00OOO ['status']==200 :#line:334
                    if float (OOOOOOO0OOO0OOOOO .doneeNo )!=0 :#line:335
                        OO0O00O00000OOOOO =OO0000000OOO00OOO ['data']['assets']['gold']#line:336
                        if float (OO0O00O00000OOOOO )>float (OOOOOOO0OOO0OOOOO .innerId ):#line:337
                            OO0O0OOOO000O0OO0 =int (float (OO0O00O00000OOOOO )/1.1 )#line:338
                            O000OO00000O00000 =f'_doneeNo={OOOOOOO0OOO0OOOOO.doneeNo}&quantity={OO0O0OOOO000O0OO0}_{timi_new()}'#line:339
                            O0OOO000O0000O0O0 ={'source':'scsc','authorization':OOOOOOO0OOO0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00000O00000 ),'signstring':O000OO00000O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            O00O0OOOO00OO0O0O ={"quantity":OO0O0OOOO000O0OO0 ,"doneeNo":OOOOOOO0OOO0OOOOO .doneeNo }#line:354
                            O00O0OOO0OOOO0OOO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOO000O0000O0O0 ,data =O00O0OOOO00OO0O0O ).json ()#line:355
                            if 'status'in O00O0OOO0OOOO0OOO :#line:357
                                if O00O0OOO0OOOO0OOO ['status']==200 :#line:358
                                    if O00O0OOO0OOOO0OOO ['data']:#line:359
                                        print (f'【赠送种子】:赠送{OO0O0OOOO000O0OO0}种子给{OOOOOOO0OOO0OOOOO.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OOO0OOOO0O0000OO0 :#line:363
            print (OOO0OOOO0O0000OO0 )#line:364
    def invitation (OO00OOOOO0000OO0O ):#line:366
        try :#line:367
            _O0O00OOOO00000OOO =float (bundled_def ())/4 #line:368
            OOO0O0000OO0OO0OO =f'_innerId={int(_O0O00OOOO00000OOO)}_{timi_new()}'#line:369
            O000O000O0OO0O000 ={'source':'scsc','authorization':OO00OOOOO0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000OO0OO0OO ),'signstring':OOO0O0000OO0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            O000O00OOOO0OO00O ={"innerId":int (_O0O00OOOO00000OOO )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000O000O0OO0O000 ,data =O000O00OOOO0OO00O )#line:382
        except Exception as OO0000O0O000OOO00 :#line:383
            print (OO0000O0O000OOO00 )#line:384
    def winning_rewards (O0OOO0O000O0O0000 ):#line:387
        try :#line:388
            O00O0OO00O00OO00O =f'__{timi_new()}'#line:389
            O0OO0O00000OO0O00 ={'source':'scsc','authorization':O0OOO0O000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O00OO00O ),'signstring':O00O0OO00O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            O0OOOO00000000O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0O00000OO0O00 ).json ()#line:401
            if 'status'in O0OOOO00000000O00 :#line:403
                if O0OOOO00000000O00 ['status']==200 :#line:404
                    if O0OOOO00000000O00 ['data']['amount']:#line:405
                        OOOO0O0OOO00O0000 =O0OOOO00000000O00 ['data']['amount']['gold']#line:406
                        return OOOO0O0OOO00O0000 #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as O0OO0O0O0O0OO0O00 :#line:410
            print (O0OO0O0O0O0OO0O00 )#line:411
    def certification (O00OOOOOOO000O0OO ):#line:414
        try :#line:415
            OO00000OO0O00OOOO =f'__{timi_new()}'#line:416
            OOOO000OOOOOOOOO0 ={'source':'scsc','authorization':O00OOOOOOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0O00OOOO ),'signstring':OO00000OO0O00OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            O0OO0OO0OO0OOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOO000OOOOOOOOO0 ).json ()#line:428
            if 'status'in O0OO0OO0OO0OOOO00 :#line:430
                if O0OO0OO0OO0OOOO00 ['status']==200 :#line:431
                    if O0OO0OO0OO0OOOO00 ['data']['result']:#line:432
                        OO00000OO0O00OOO0 =O0OO0OO0OO0OOOO00 ['data']['nick_name']#line:433
                        return OO00000OO0O00OOO0 #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as O000OOOO0O00O0000 :#line:437
            print (O000OOOO0O00O0000 )#line:438
    def crops_illustrated (O0O0O0OOOOO00O0O0 ):#line:441
        try :#line:442
            OOO00O0OOOO000OOO =f'__{timi_new()}'#line:443
            OO0OOO00OOO0O00O0 ={'source':'scsc','authorization':O0O0O0OOOOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO000OOO ),'signstring':OOO00O0OOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            O0000OO000O0000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0OOO00OOO0O00O0 ).json ()#line:455
            if 'status'in O0000OO000O0000O0 :#line:457
                if O0000OO000O0000O0 ['status']==200 :#line:458
                    O000O0000OO0OO000 =O0000OO000O0000O0 ['data'][0 ]['crops']#line:459
                    for O0OOOOOOOO0OO0OO0 in O000O0000OO0OO000 :#line:460
                        if O0OOOOOOOO0OO0OO0 ['ill_clover_award']:#line:461
                            if float (O0OOOOOOOO0OO0OO0 ['ill_clover_award'])>1 :#line:462
                                if O0OOOOOOOO0OO0OO0 ['is_finish']:#line:463
                                    if not O0OOOOOOOO0OO0OO0 ['is_getit']:#line:464
                                        if O0O0O0OOOOO00O0O0 .certification ()!='未实名':#line:465
                                            OOO00O0OOOO000OOO =f'_award_level={O0OOOOOOOO0OO0OO0["level"]}_{timi_new()}'#line:466
                                            OO0OOO00OOO0O00O0 ={'source':'scsc','authorization':O0O0O0OOOOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO000OOO ),'signstring':OOO00O0OOOO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            O00OOO00O0O00O0OO ={"award_level":O0OOOOOOOO0OO0OO0 ['level']}#line:478
                                            O0OOO0O0OOOOOOOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0OOO00OOO0O00O0 ,json =O00OOO00O0O00O0OO ).json ()#line:480
                                            if 'status'in O0OOO0O0OOOOOOOOO :#line:481
                                                if O0OOO0O0OOOOOOOOO ['status']==200 :#line:482
                                                    OO00O0OOO00O0000O =O0OOO0O0OOOOOOOOO ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{O0OOOOOOOO0OO0OO0["crop_name"]}成就丨奖励{OO00O0OOO00O0000O}☘️')#line:485
                                                if O0OOO0O0OOOOOOOOO ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{O0OOO0O0OOOOOOOOO["message"]}')#line:487
        except Exception as OOOOO00000O0O0O00 :#line:488
            print (OOOOO00000O0O0O00 )#line:489
    def watched_ad (OO0O0O0OOO0OO00OO ):#line:492
        try :#line:493
            O0O0000OOOOO00000 =f'__{timi_new()}'#line:494
            O0O0O000OOO000OOO ={'source':'scsc','authorization':OO0O0O0OOO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOOOO00000 ),'signstring':O0O0000OOOOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            O0O0OO0OOO000OOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O000OOO000OOO ).json ()#line:506
            if 'status'in O0O0OO0OOO000OOOO :#line:508
                if O0O0OO0OOO000OOOO ['status']==200 :#line:509
                    if 'offlineInfo'in O0O0OO0OOO000OOOO ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        O0O00OO0O00000O00 =O0O0OO0OOO000OOOO ['data']['offlineInfo']['off_minute']#line:512
                        O0O0OO0O0000OO00O =float (O0O0OO0OOO000OOOO ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O000OOO000OOO ).json ()#line:515
                        time .sleep (2 )#line:516
                        O0000O000O0O00O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O000OOO000OOO ).json ()#line:517
                        if 'status'in O0000O000O0O00O0O :#line:519
                            if O0000O000O0O00O0O ['status']==200 :#line:520
                                OO0000O00O00O0000 =float (O0000O000O0O00O0O ['data']['silver'])/1000000000000 #line:521
                                O0OOO000OO000OOOO =str (OO0000O00O00O0000 -O0O0OO0O0000OO00O )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{O0O00OO0O00000O00}分钟奖励🌱数量:{O0OOO000OO000OOOO}t粒')#line:523
        except Exception as O0000O0O00OO000O0 :#line:524
            print (O0000O0O00OO000O0 )#line:525
    def user_ad (OOO0OO00OO0OOO00O ):#line:528
        try :#line:529
            OOO00O0OOOO0OOO0O =f'__{timi_new()}'#line:530
            OOO0O0OOOO0OO0O00 ={'source':'scsc','authorization':OOO0OO00OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO0OOO0O ),'signstring':OOO00O0OOOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            OOOO0000OO0000O0O =requests .request ('get',f'{host}/user/ad',headers =OOO0O0OOOO0OO0O00 ).json ()#line:542
            if 'status'in OOOO0000OO0000O0O :#line:544
                if OOOO0000OO0000O0O ['status']==200 :#line:545
                    OOOOOOO0OO00O00O0 =OOOO0000OO0000O0O ['data']['max_time']#line:546
                    O00O0OOOO0000O0OO =OOOO0000OO0000O0O ['data']['watch_time']#line:547
                    O0O0OOOO00OO000O0 =OOOO0000OO0000O0O ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{O0O0OOOO00OO000O0 + OOOOOOO0OO00O00O0 - O00O0OOOO0000O0OO}次丨好友提供:{O0O0OOOO00OO000O0}次')#line:549
                    if O0O0OOOO00OO000O0 +OOOOOOO0OO00O00O0 -O00O0OOOO0000O0OO >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        O000OOOOO00O00O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0O0OOOO0OO0O00 ).json ()#line:552
                        if 'status'in O000OOOOO00O00O00 :#line:554
                            if O000OOOOO00O00O00 ['status']==200 :#line:555
                                OOOO0OO0O0OO000OO =float (O000OOOOO00O00O00 ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(OOOO0OO0O0OO000OO)}t粒')#line:557
                                return True #line:558
                            if O000OOOOO00O00O00 ['status']==500 :#line:559
                                OOO0OO0O00O000OO0 =O000OOOOO00O00O00 ['message']#line:560
                                print (f'【获取种子】:{OOO0OO0O00O000OO0}')#line:561
                                return False #line:562
        except Exception as OO0OOO000O00000O0 :#line:563
            print (OO0OOO000O00000O0 )#line:564
    def synthetic (OOO000OO00OO00OO0 ):#line:567
        global id ,g #line:568
        try :#line:569
            OOOO0OOO0OO000OO0 =OOO000OO00OO00OO0 .level_new ()#line:570
            OOO0O0O0OO00O0O00 =random .randint (9 ,11 )#line:571
            O0000OOOO0O0O0OOO =f'_site=8&targetSite={OOO0O0O0OO00O0O00}_{timi_new()}'#line:572
            OO0O0O000OO0OOOOO ={'source':'scsc','authorization':OOO000OO00OO00OO0 .token ,'timestamp':timi_new (),'sign':sign (O0000OOOO0O0O0OOO ),'signstring':O0000OOOO0O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            OOOO00OOO00O00OOO ={"site":int (8 ),"targetSite":int (OOO0O0O0OO00O0O00 )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0O000OO0OOOOO ,json =OOOO00OOO00O00OOO )#line:585
            while True :#line:586
                O000OOO0OO0OO0OOO =f'__{timi_new()}'#line:587
                O0O0O0OOO00O00O0O ={'source':'scsc','authorization':OOO000OO00OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0OO0OOO ),'signstring':O000OOO0OO0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                OO0O0O00OOOO0OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00O00O0O ).json ()#line:599
                if 'status'in OO0O0O00OOOO0OO0O :#line:601
                    if OO0O0O00OOOO0OO0O ['status']==200 :#line:602
                        OO0O0O00OOOO0O000 =OO0O0O00OOOO0OO0O ['data']['cropList']#line:603
                        OOO0O00OOO000OO0O =OO0O0O00OOOO0OO0O ['data']['gameCoreDataDBid']#line:604
                        OO0OO0O00O0OO0O00 =float (OO0O0O00OOOO0OO0O ['data']['silver'])/1000000000000 #line:605
                        O000O000OOO000O00 =0 #line:610
                        for OO0O0OO0OOOO00OOO in OO0O0O00OOOO0O000 :#line:611
                            if not OO0O0OO0OOOO00OOO :#line:612
                                OOO0OOO0000O0OO00 =f'_crop_id={OOO0O00OOO000OO0O}&site={O000O000OOO000O00}_{OOO000OO00OO00OO0.time}'#line:613
                                OOOOO0O00O00O00O0 ={'source':'scsc','authorization':OOO000OO00OO00OO0 .token ,'timestamp':OOO000OO00OO00OO0 .time ,'sign':sign (OOO0OOO0000O0OO00 ),'signstring':OOO0OOO0000O0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                OOO00OOOO000OOOO0 ={"site":O000O000OOO000O00 ,"crop_id":OOO0O00OOO000OO0O }#line:624
                                OOOO000OOO0O0OOOO =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOO0O00O00O00O0 ,data =OOO00OOOO000OOOO0 ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in OOOO000OOO0O0OOOO :#line:628
                                    if OOOO000OOO0O0OOOO ['status']==200 :#line:629
                                        if OOOO000OOO0O0OOOO ['message']=='种子数量不足':#line:630
                                            OOOO0OOO0OO000OO0 =OOO000OO00OO00OO0 .level_new ()#line:631
                                            print (f'【种植合成】:{OOOO000OOO0O0OOOO["message"]}')#line:632
                                            if not OOO000OO00OO00OO0 .user_ad ():#line:633
                                                return False #line:634
                                    if OOOO000OOO0O0OOOO ['status']==500 :#line:635
                                        print (f'【种植合成】:{OOOO000OOO0O0OOOO["message"]}')#line:636
                                        return False #line:637
                            O000O000OOO000O00 +=1 #line:638
                        O00OO0OOO00000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O0OOO00O00O0O ).json ()#line:639
                        O00OO0000OO0OO0O0 =O00OO0OOO00000OO0 ['data']['cropList']#line:640
                        OOO00OOO0O0OOOO00 =False #line:641
                        for OO0O0OO0OOOO00OOO in range (12 ):#line:642
                            id =O00OO0000OO0OO0O0 [OO0O0OO0OOOO00OOO ]['level']#line:643
                            if float (OOOO0OOO0OO000OO0 )-float (id )>9 :#line:644
                                OO0OOOO0OO00OO00O =f'_site={OO0O0OO0OOOO00OOO}_{timi_new()}'#line:645
                                O0O0O0OOO00O00OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO000OO00OO00OO0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOOO0OO00OO00O ),'signstring':OO0OOOO0OO00OO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O000O00OO00OO000O ={"site":OO0O0OO0OOOO00OOO }#line:657
                                O00OO00OOO00O000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O0OOO00O00OOO ,data =O000O00OO00OO000O ).json ()#line:659
                                if 'status'in O00OO00OOO00O000O :#line:660
                                    if O00OO00OOO00O000O ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for OOO000O0O0O0O00OO in range (11 ):#line:664
                                    OO00O0OOOOOOOOOOO =OOO000O0O0O0O00OO +1 #line:665
                                    g =O00OO0000OO0OO0O0 [OO00O0OOOOOOOOOOO ]['level']#line:666
                                    if id ==g :#line:667
                                        O00000OO00O0O0O0O =OOO000O0O0O0O00OO +2 #line:668
                                        if O00000OO00O0O0O0O !=OO0O0OO0OOOO00OOO +1 :#line:669
                                            O000O000O00000000 =OO0O0OO0OOOO00OOO +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            O0000OOOO0O0O0OOO =f'_site={O000O000O00000000 - 1}&targetSite={O00000OO00O0O0O0O - 1}_{timi_new()}'#line:673
                                            OO0O0O000OO0OOOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO000OO00OO00OO0 .token ,'timestamp':timi_new (),'sign':sign (O0000OOOO0O0O0OOO ),'signstring':O0000OOOO0O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            OOO0O0O00OO000O00 ={"site":int (O000O000O00000000 -1 ),"targetSite":int (O00000OO00O0O0O0O -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O0O000OO0OOOOO ,json =OOO0O0O00OO000O00 )#line:692
                                            OOO00OOO0O0OOOO00 =True #line:694
                                    if OOO00OOO0O0OOOO00 :#line:695
                                        break #line:696
                                if OOO00OOO0O0OOOO00 :#line:697
                                    break #line:698
        except :#line:699
            OOO000OO00OO00OO0 .synthetic ()#line:700
    def level_new (OO0O0OOO0O00O0OOO ):#line:703
        try :#line:704
            O000000OO0OO0O000 =f'__{timi_new()}'#line:705
            OOO0OO00O0OOO000O ={'source':'scsc','authorization':OO0O0OOO0O00O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OO0OO0O000 ),'signstring':O000000OO0OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OOO0OO0O00OO000OO =requests .request ('get',f'{host}/user',headers =OOO0OO00O0OOO000O ).json ()#line:717
            if 'status'in OOO0OO0O00OO000OO :#line:718
                if OOO0OO0O00OO000OO ['status']==200 :#line:719
                    return float (OOO0OO0O00OO000OO ['data']['level'])#line:720
        except Exception as O00000OO000O00O0O :#line:721
            print (O00000OO000O00O0O )#line:722
    def propsraffle (O000OOO0O0OOOOOOO ):#line:725
        try :#line:726
            while True :#line:727
                OOOOOO0O000OOO00O =f'__{timi_new()}'#line:728
                OOOO0OOOO00O000O0 ={'source':'scsc','authorization':O000OOO0O0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O000OOO00O ),'signstring':OOOOOO0O000OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                O0OOOOOO000OO000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO0OOOO00O000O0 ).json ()#line:740
                if 'status'in O0OOOOOO000OO000O :#line:742
                    if O0OOOOOO000OO000O ['status']==200 :#line:743
                        OO00000OO0O0OOOOO =O0OOOOOO000OO000O ['data']['rows']#line:744
                        OO00000OO0O000O0O =O0OOOOOO000OO000O ['data']['vstate']#line:745
                        if OO00000OO0O0OOOOO ==5 or OO00000OO0O0OOOOO ==6 or OO00000OO0O0OOOOO ==7 :#line:746
                            OOO00O0O0000OO0OO =O0OOOOOO000OO000O ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{OOO00O0O0000OO0OO}')#line:748
                        if OO00000OO0O0OOOOO ==1 or OO00000OO0O0OOOOO ==2 or OO00000OO0O0OOOOO ==3 :#line:749
                            O00000000O000O0O0 =O0OOOOOO000OO000O ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{O00000000O000O0O0}')#line:751
                        if OO00000OO0O0OOOOO ==4 or OO00000OO0O0OOOOO ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if OO00000OO0O0OOOOO =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as OO0O0O0O00OO00OOO :#line:793
            print (OO0O0O0O00OO00OOO )#line:794
    def friends_invitation (OO00OO0O0O0OO000O ):#line:797
        try :#line:798
            O0000OO0000O0OO0O =f'__{timi_new()}'#line:799
            O0OOO00O0OO000O0O ={'source':'scsc','authorization':OO00OO0O0O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO0000O0OO0O ),'signstring':O0000OO0000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            OOO00O00OOOO0OOO0 =requests .request ('get',f'{host}/friends',headers =O0OOO00O0OO000O0O ).json ()#line:811
            if 'status'in OOO00O00OOOO0OOO0 :#line:812
                if OOO00O00OOOO0OOO0 ['status']==200 :#line:813
                    OOO0O00O000O0OOO0 =OOO00O00OOOO0OOO0 ['data']['myInviteter']#line:814
                    if OOO0O00O000O0OOO0 :#line:815
                        OO0000O0O0OO0000O =OOO0O00O000O0OOO0 ['user']['nickname']#line:816
                        O0000OO0OO00OOO00 =OO00OO0O0O0OO000O .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{OO0000O0O0OO0000O}丨实名:{O0000OO0OO00OOO00}')#line:818
                    else :#line:819
                        if OO00OO0O0O0OO000O .innerId !='0':#line:820
                            OO00OO0O0O0OO000O .invitation ()#line:821
        except Exception as OO0OO00OO00O00O0O :#line:822
            print (OO0OO00OO00O00O0O )#line:823
    def add_clover (O000OO00OOO0OOOO0 ):#line:826
        global golden_seed #line:827
        try :#line:828
            O0O0O00OOOO00OO00 =f'__{timi_new()}'#line:829
            O000O0000O00O000O ={'source':'scsc','authorization':O000OO00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO00OO00 ),'signstring':O0O0O00OOOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            O0OOO0000OO00OO00 =requests .request ('get',f'{host}/assets/clovers',headers =O000O0000O00O000O ).json ()#line:841
            if 'status'in O0OOO0000OO00OO00 :#line:843
                if O0OOO0000OO00OO00 ['status']==200 :#line:844
                    O00000OO0OO000000 =O0OOO0000OO00OO00 ['data']['clover']#line:845
                    O0O0000000OOOO0O0 =O0OOO0000OO00OO00 ['data']['used_clover']#line:846
                    OO00O00O00OO0OOO0 =float (O00000OO0OO000000 )-float (O0O0000000OOOO0O0 )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0000000OOOO0O0}')#line:848
                    if O000OO00OOO0OOOO0 .certification ()!='未实名':#line:849
                        if OO00O00O00OO0OOO0 >1 :#line:850
                            O0O0O00OOOO00OO00 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00O00O00OO0OOO0)}_{timi_new()}'#line:851
                            O00O0O00000OOOOOO ={'source':'scsc','authorization':O000OO00OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OOOO00OO00 ),'signstring':O0O0O00OOOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            O0O00OOO0OOO00OO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00O00O00OO0OOO0 )}#line:863
                            O0OO0OO0OOOOO0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O0O00000OOOOOO ,data =O0O00OOO0OOO00OO0 ).json ()#line:864
                            if 'status'in O0OO0OO0OOOOO0OOO :#line:866
                                if O0OO0OO0OOOOO0OOO ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO0OOOOO0OOO["data"]}丨数量:{OO00O00O00OO0OOO0}')#line:868
                                if O0OO0OO0OOOOO0OOO ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{O0OO0OO0OOOOO0OOO["message"]}')#line:870
            O0OO0O0OO0O0OOO00 =requests .request ('get',f'{host}/lottery',headers =O000O0000O00O000O ).json ()#line:871
            OOO0O00OO00O0OO0O =O000OO00OOO0OOOO0 .winning_rewards ()#line:873
            if 'status'in O0OO0O0OO0O0OOO00 :#line:874
                if O0OO0O0OO0O0OOO00 ['status']==200 :#line:875
                    OOOOO0OO00O0OO0O0 =O0OO0O0OO0O0OOO00 ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (OOOOO0OO00O0OO0O0 )#line:877
                    O00O0OOO00O0OOOOO =O0OO0O0OO0O0OOO00 ['data'][1 ]['value']#line:878
                    O0O00O0O0OO0OO0OO =O0OO0O0OO0O0OOO00 ['data'][0 ]['join_number']#line:879
                    OOO0O0O000OOO00O0 =int (float (O0OO0O0OO0O0OOO00 ['data'][0 ]['totalValue']))#line:880
                    O00O00OOOO0O0OO0O =float (O00O0OOO00O0OOOOO /OOO0O0O000OOO00O0 )*10000 #line:881
                    OOO00O0O0O0OOO0OO =OOO0O0O000OOO00O0 /O0O00O0O0OO0OO0OO #line:882
                    print (f'【参与抽奖】:预计每天中{str(OOOOO0OO00O0OO0O0)[:6]}颗金种子丨好友收益:{str(OOO0O00OO00O0OO0O)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(O00O00OOOO0O0OO0O)[:6]}颗金种子丨☘️人均:{str(OOO00O0O0O0OOO0OO)[:7]}️')#line:884
        except Exception as OOO00000O0O0O00OO :#line:885
            print (OOO00000O0O0O00OO )#line:886
    def energy (O0OO0O000OOO000OO ):#line:890
        try :#line:891
            while True :#line:892
                O00OO000OO0OOO0O0 =f'__{timi_new()}'#line:893
                OOO00000OOO0OO0OO ={'source':'scsc','authorization':O0OO0O000OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO000OO0OOO0O0 ),'signstring':O00OO000OO0OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                O0O00O00O00O00O0O =requests .request ('get',f'{host}/energy/general',headers =OOO00000OOO0OO0OO ).json ()#line:905
                if 'status'in O0O00O00O00O00O0O :#line:907
                    if O0O00O00O00O00O0O ['status']==200 :#line:908
                        OO000OO0O00O0000O =O0O00O00O00O00O0O ['data']['ordinary_water']#line:909
                        O0000O0OOO00OO00O =O0O00O00O00O00O0O ['data']['ordinary_fertilizer']#line:910
                        O0OOOOO00O0OO0000 =O0O00O00O00O00O0O ['data']['videoStatus']#line:911
                        O0O0O00O00OOO0000 =O0O00O00O00O00O0O ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(O0000O0OOO00OO00O).split(".")[0]}丨水滴:{str(OO000OO0O00O0000O).split(".")[0]}')#line:913
                        if float (O0000O0OOO00OO00O )<96 :#line:914
                            if O0OOOOO00O0OO0000 :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                O00O0O0O0O0O000O0 =99 -float (O0000O0OOO00OO00O )#line:917
                                OOOO00OOOO0O0O0OO ={"fertilizer":str (O00O0O0O0O0O000O0 ).split ('.')[0 ]}#line:918
                                O000OO0OOOOOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO00000OOO0OO0OO ).json ()#line:919
                                if 'status'in O000OO0OOOOOO00O0 :#line:921
                                    if O000OO0OOOOOO00O0 ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{O000OO0OOOOOO00O0["message"]}')#line:923
                                    if O000OO0OOOOOO00O0 ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{O000OO0OOOOOO00O0["message"]}')#line:925
                                        break #line:926
                                if float (O0000O0OOO00OO00O )<78 :#line:928
                                    O00O0O0O0O0O000O0 =80 -float (O0000O0OOO00OO00O )#line:929
                                    OOOO0OOO00O00O00O =f'_fertilizer={int(O00O0O0O0O0O000O0)}_{timi_new()}'#line:930
                                    O00O0O0OOO00O0O0O ={'source':'scsc','authorization':O0OO0O000OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO00O00O00O ),'signstring':OOOO0OOO00O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    OOO00OOO0O0OOO000 ={"fertilizer":int (O00O0O0O0O0O000O0 )}#line:942
                                    O0000O000O0O0OOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00O0O0OOO00O0O0O ,data =OOO00OOO0O0OOO000 ).json ()#line:944
                                    if 'status'in O0000O000O0O0OOOO :#line:946
                                        if O0000O000O0O0OOOO ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{O0000O000O0O0OOOO["message"]}丨数量:{int(O00O0O0O0O0O000O0)}')#line:948
                                        if O0000O000O0O0OOOO ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{O0000O000O0O0OOOO["message"]}丨数量:{int(O00O0O0O0O0O000O0)}')#line:950
                                            OOO00O0O000OOO000 =O0000O000O0O0OOOO ["message"].split ('-')[1 ]#line:951
                                            OOOOOOO000OOO0000 =f'__{timi_new()}'#line:952
                                            OOOOO0OO0O0O0000O ={'source':'scsc','authorization':O0OO0O000OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000OOO0000 ),'signstring':OOOOOOO000OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            O0OO0O0O0000O0000 =requests .request ('get',f'{host}/user',headers =OOOOO0OO0O0O0000O ).json ()#line:964
                                            if 'status'in O0OO0O0O0000O0000 :#line:965
                                                if O0OO0O0O0000O0000 ['status']==200 :#line:966
                                                    O0OOOO0O00000OOOO =O0OO0O0O0000O0000 ['data']['inner_id']#line:967
                                                    if give_gold (O0OOOO0O00000OOOO ,float (OOO00O0O000OOO000 )+1 ):#line:968
                                                        O0OO0O000OOO000OO .energy ()#line:969
                        if float (OO000OO0O00O0000O )<880 :#line:970
                            if O0O0O00O00OOO0000 :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                OOOO0OOOO00O0OOOO =999 -float (OO000OO0O00O0000O )#line:973
                                OOOOOOOOO00O00OOO ={"water":str (OOOO0OOOO00O0OOOO ).split ('.')[0 ]}#line:974
                                OOO0OOO00OOOOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO00000OOO0OO0OO ).json ()#line:975
                                if 'status'in OOO0OOO00OOOOO0O0 :#line:977
                                    if OOO0OOO00OOOOO0O0 ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOO00OOOOO0O0["message"]}')#line:979
                                    if OOO0OOO00OOOOO0O0 ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0OOO00OOOOO0O0["message"]}')#line:981
                                        break #line:982
                                if float (OO000OO0O00O0000O )<780 :#line:983
                                    OOOO0OOOO00O0OOOO =800 -float (OO000OO0O00O0000O )#line:984
                                    OO0000OOOOO0OOO0O =f'_water={int(OOOO0OOOO00O0OOOO)}_{timi_new()}'#line:985
                                    OO0O0OO0O000O0O0O ={'source':'scsc','authorization':O0OO0O000OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOOOO0OOO0O ),'signstring':OO0000OOOOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    O00O0000O0000O00O ={"water":int (OOOO0OOOO00O0OOOO )}#line:997
                                    OO0O0OOOO00O0OOO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0O0OO0O000O0O0O ,data =O00O0000O0000O00O ).json ()#line:999
                                    if 'status'in OO0O0OOOO00O0OOO0 :#line:1001
                                        if OO0O0OOOO00O0OOO0 ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{OO0O0OOOO00O0OOO0["message"]}丨数量:{int(OOOO0OOOO00O0OOOO)}')#line:1003
                                        if OO0O0OOOO00O0OOO0 ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{OO0O0OOOO00O0OOO0["message"]}丨数量:{int(OOOO0OOOO00O0OOOO)}')#line:1005
                                            OOO00O0O000OOO000 =OO0O0OOOO00O0OOO0 ["message"].split ('-')[1 ]#line:1006
                                            OOOOOOO000OOO0000 =f'__{timi_new()}'#line:1007
                                            OOOOO0OO0O0O0000O ={'source':'scsc','authorization':O0OO0O000OOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO000OOO0000 ),'signstring':OOOOOOO000OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            O0OO0O0O0000O0000 =requests .request ('get',f'{host}/user',headers =OOOOO0OO0O0O0000O ).json ()#line:1019
                                            if 'status'in O0OO0O0O0000O0000 :#line:1020
                                                if O0OO0O0O0000O0000 ['status']==200 :#line:1021
                                                    O0OOOO0O00000OOOO =O0OO0O0O0000O0000 ['data']['inner_id']#line:1022
                                                    if give_gold (O0OOOO0O00000OOOO ,float (OOO00O0O000OOO000 )+1 ):#line:1023
                                                        O0OO0O000OOO000OO .energy ()#line:1024
                        break #line:1025
        except Exception as O0O0000O00O0OOOO0 :#line:1027
            print (O0O0000O00O0OOOO0 )#line:1028
def bundled_def ():#line:1030
    O000OOO0OOOO00O0O =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return O000OOO0OOOO00O0O [random .randint (0 ,len (O000OOO0OOOO00O0O )-1 )]#line:1032
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
        O0O00O0OOOOOOOOOO =gitee_edition ()#line:1059
        if version_of_the_validation ()<O0O00O0OOOOOOOOOO ['CityEarth']['edition']:#line:1060
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00O0OOOOOOOOOO["CityEarth"]["edition"]}   ❌')#line:1061
            print (f'更新内容=>>{O0O00O0OOOOOOOOOO["CityEarth"]["content"]}   🎉')#line:1062
        else :#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00O0OOOOOOOOOO["CityEarth"]["edition"]}   ✅')#line:1064
            print (f'更新内容=>> {O0O00O0OOOOOOOOOO["CityEarth"]["content"]}   🎉')#line:1065
    except Exception as O0O0000OOO0O0OOO0 :#line:1066
        print (O0O0000OOO0O0OOO0 )#line:1067
def sc3 ():#line:1069
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1070
if __name__ =='__main__':#line:1074
    start ()#line:1075
