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
        O0000OO0O0OOO0O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O0000OO0O0OOO0O0O)}个账号==========")#line:13
        for O0O0000O0OO0OO000 in O0000OO0O0OOO0O0O :#line:14
            O0O000O0O00O00OOO =[]#line:15
            print (f"------------正在执行第{O0000OO0O0OOO0O0O.index(O0O0000O0OO0OO000) + 1}个账号------------")#line:16
            O00O00000OOO0OO0O =CityEarth (O0O0000O0OO0OO000 ,O0O000O0O00O00OOO ,O0000OO0O0OOO0O0O .index (O0O0000O0OO0OO000 ))#line:17
            def O000O0O0O00O0OOOO ():#line:19
                if O00O00000OOO0OO0O .base_info ():#line:21
                    O00O00000OOO0OO0O .sealing ()#line:23
                    O00O00000OOO0OO0O .invitenum ()#line:25
                    O00O00000OOO0OO0O .game_map ()#line:27
                    O00O00000OOO0OO0O .friends_invitation ()#line:29
                    O00O00000OOO0OO0O .energy ()#line:31
                    O00O00000OOO0OO0O .add_clover ()#line:33
                    O00O00000OOO0OO0O .propsraffle ()#line:35
                    O00O00000OOO0OO0O .synthetic ()#line:37
                    O00O00000OOO0OO0O .crops_illustrated ()#line:39
                    O00O00000OOO0OO0O .give_gold ()#line:41
                    O00O00000OOO0OO0O .withdraw ()#line:43
            O0OOOO000OOOO0OO0 =threading .Thread (target =O000O0O0O00O0OOOO )#line:45
            O0OOOO000OOOO0OO0 .start ()#line:46
            time .sleep (time_xx )#line:47
        print (f"------------正在处理推送通知------------")#line:48
        time .sleep (0.5 )#line:49
        O000O0OOO0OOO000O =format_msg ()#line:50
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O0OOO0OOO000O +' ')#line:51
    except Exception as OOOO0000OO00OOO0O :#line:52
        print (OOOO0000OO00OOO0O )#line:53
def give_gold (O0O0O000OOOOOO000 ,OOO00O0OOOOO0O000 ):#line:56
        try :#line:57
            OO00O00000O00OO00 =f'_doneeNo={O0O0O000OOOOOO000}&quantity={int(OOO00O0OOOOO0O000)}_{timi_new()}'#line:58
            O0OOOOO000OOO0O0O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO00O00000O00OO00 ),'signstring':OO00O00000O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:69
            OOO0000OO00O0OO0O ={"quantity":int (OOO00O0OOOOO0O000 ),"doneeNo":O0O0O000OOOOOO000 }#line:73
            OOOO0000OOOOO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOOOO000OOO0O0O ,data =OOO0000OO00O0OO0O ).json ()#line:74
            if 'status'in OOOO0000OOOOO0O00 :#line:76
                if OOOO0000OOOOO0O00 ['status']==200 :#line:77
                    if OOOO0000OOOOO0O00 ['data']:#line:78
                        print (f'【赠送种子】:赠送{int(OOO00O0OOOOO0O000)}种子给{O0O0O000OOOOOO000}成功')#line:79
                        return True #line:80
                if OOOO0000OOOOO0O00 ['status']==401 :#line:81
                    print (f'【赠送种子】:{OOOO0000OOOOO0O00["message"]}')#line:82
                    return False #line:83
                if OOOO0000OOOOO0O00 ['status']==500 :#line:84
                    print (f'【赠送种子】:{OOOO0000OOOOO0O00["message"]}')#line:85
                    return False #line:86
            return False #line:87
        except Exception as O0OOO0000O0OO00OO :#line:88
            print (O0OOO0000O0OO00OO )#line:89
def kvkv ():#line:90
    return '/vastzzzl/vastzzzl/raw/master'#line:91
def sign (OO0OOO000OO0O00OO ):#line:94
    O00000O0OOOOOO0O0 =hashlib .md5 (OO0OOO000OO0O00OO .encode ()).hexdigest ()#line:95
    O0000O000OO00000O =sc1 ()#line:96
    OO0OO0O0000000000 =sc2 ()#line:97
    O0O000OOO0O00OO0O =sc3 ()#line:98
    OOO0O00000O0O0000 =O0000O000OO00000O +O00000O0OOOOOO0O0 +OO0OO0O0000000000 +O0O000OOO0O00OO0O #line:99
    OO000O0000OO0000O =hashlib .md5 (OOO0O00000O0O0000 .encode ()).hexdigest ()#line:100
    return OO000O0000OO0000O #line:101
def format_msg ():#line:105
    OO0OOO0O0OO00OO0O =""#line:106
    for OO0OOOO0000O00O0O in msg_list :#line:107
        OO0OOO0O0OO00OO0O +=str (OO0OOOO0000O00O0O )+"\r\n"#line:108
    return OO0OOO0O0OO00OO0O #line:109
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
def get_json_data (O0000O0O000O00O00 ,OO00O000000OOOO00 ,O0OOO00OO0O0OOO00 ,O000OO0O0O0000O00 ):#line:128
    with open (O0000O0O000O00O00 ,'rb')as OOO00OO0OOO000O0O :#line:130
        O0OO000OOOOO00OO0 =json .load (OOO00OO0OOO000O0O )#line:131
        O0OO000OOOOO00OO0 ['data'][OO00O000000OOOO00 ][O0OOO00OO0O0OOO00 ]=O000OO0O0O0000O00 #line:132
        O00O0OOOO00O0O000 =O0OO000OOOOO00OO0 #line:133
    OOO00OO0OOO000O0O .close ()#line:134
    return O00O0OOOO00O0O000 #line:135
def write_json_data (OOO00OOO000000OO0 ):#line:137
    with open (json_path1 ,'w')as O0OO00O0O0OO00000 :#line:138
        json .dump (OOO00OOO000000OO0 ,O0OO00O0O0OO00000 )#line:139
    O0OO00O0O0OO00000 .close ()#line:140
    return True #line:141
class CityEarth :#line:143
    def __init__ (O0OOOOOOOOOO00000 ,OOOOOO0O00OO0000O ,OO00OOO0O0OO00OOO ,OO00OO0O00O000O0O ):#line:145
        try :#line:146
            O0OOOOOOOOOO00000 .msg =OO00OOO0O0OO00OOO #line:147
            O0OOOOOOOOOO00000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:148
            O0OOOOOOOOOO00000 .token =OOOOOO0O00OO0000O ['authorization']#line:149
            O0OOOOOOOOOO00000 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:150
            O0OOOOOOOOOO00000 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:151
            O0OOOOOOOOOO00000 .elephant_user =OOOOOO0O00OO0000O ['elephant_user']#line:152
            O0OOOOOOOOOO00000 .elephant_pswd =OOOOOO0O00OO0000O ['elephant_pswd']#line:153
            O0OOOOOOOOOO00000 .elephant_Task_ID =OOOOOO0O00OO0000O ['elephant_Task_ID']#line:154
            O0OOOOOOOOOO00000 .len_new =OO00OO0O00O000O0O #line:155
        except :#line:156
            print ('变量格式错误')#line:157
    def base_info (OO0OO00OO0O0O00O0 ):#line:160
        try :#line:161
            OO0OO00OO0O0O00O0 .watched_ad ()#line:163
            OO0OO0O00O000O00O =f'__{timi_new()}'#line:164
            O000000OOOOO00OOO ={'source':'scsc','authorization':OO0OO00OO0O0O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00O000O00O ),'signstring':OO0OO0O00O000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:175
            O0OOOO0O0OO0O00OO =requests .request ('get',f'{host}/user',headers =O000000OOOOO00OOO ).json ()#line:176
            if 'status'in O0OOOO0O0OO0O00OO :#line:178
                if O0OOOO0O0OO0O00OO ['status']==200 :#line:179
                    O00O00OOOOO0OO00O =O0OOOO0O0OO0O00OO ['data']['nickname']#line:180
                    O0OO00OO0O00OO000 =O0OOOO0O0OO0O00OO ['data']['inner_id']#line:181
                    O0OO00OOOO0OO0000 =O0OOOO0O0OO0O00OO ['data']['assets']['gold']#line:182
                    O00OOO0OOO0O0O000 =O0OOOO0O0OO0O00OO ['data']['level']#line:183
                    print (f'【账号信息】:昵称:{O00O00OOOOO0OO00O[:5]}丨ID:{O0OO00OO0O00OO000}丨等级:{O00OOO0OOO0O0O000}丨金种子:{str(O0OO00OOOO0OO0000).split(".")[0]}')#line:184
                if O0OOOO0O0OO0O00OO ['status']==401 :#line:185
                    print ('【账号信息】:账号失效正在尝试登录')#line:186
                    if OO0OO00OO0O0O00O0 .elephant_user =='f':#line:187
                        return False #line:188
                    OO00OO00000OO0000 =Invalid_login .addtask (elephant_user =OO0OO00OO0O0O00O0 .elephant_user ,elephant_pswd =OO0OO00OO0O0O00O0 .elephant_pswd ,elephant_Task_ID =OO0OO00OO0O0O00O0 .elephant_Task_ID )#line:189
                    O0000OO00O00OO0O0 =get_json_data (json_path ,OO0OO00OO0O0O00O0 .len_new ,'authorization',OO00OO00000OO0000 )#line:190
                    if write_json_data (O0000OO00O00OO0O0 ):#line:191
                        print ('正在写入账号配置文件')#line:192
                    return False #line:193
                if O0OOOO0O0OO0O00OO ['status']==500 :#line:194
                    return False #line:195
            return True #line:196
        except Exception as O0O0000OO00O00OOO :#line:197
            print (O0O0000OO00O00OOO )#line:198
    def sealing (O0OO0O00O00OO0000 ):#line:201
        try :#line:202
            O0000OO000OOOOOOO =f'__{timi_new()}'#line:203
            O0O0OO000OO00O00O ={'source':'scsc','authorization':O0OO0O00O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OO000OOOOOOO ),'signstring':O0000OO000OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:214
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0OO000OO00O00O )#line:215
            requests .request ('get',f'{host}/packsack/list',headers =O0O0OO000OO00O00O )#line:216
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0OO000OO00O00O )#line:217
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0OO000OO00O00O )#line:218
            requests .request ('get',f'{host}/user',headers =O0O0OO000OO00O00O )#line:219
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0OO000OO00O00O )#line:220
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0OO000OO00O00O )#line:221
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0OO000OO00O00O )#line:222
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO000OO00O00O )#line:223
            requests .request ('get',f'{host}/assets',headers =O0O0OO000OO00O00O )#line:224
        except Exception as OOOO00000O0O0O0O0 :#line:225
            print (OOOO00000O0O0O0O0 )#line:226
    def withdraw (O0OOO00O00O000O00 ):#line:230
        O0O0000O0000O0OO0 =f'__{timi_new()}'#line:231
        OOOO0O000OOO00000 ={'source':'scsc','authorization':O0OOO00O00O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0000O0OO0 ),'signstring':O0O0000O0000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:242
        OO000O00O0000OOOO =requests .request ('get',f'{host}/assets',headers =OOOO0O000OOO00000 ).json ()#line:243
        if 'status'in OO000O00O0000OOOO :#line:245
            if OO000O00O0000OOOO ['status']==200 :#line:246
                OO0OO0O00O00OOOO0 =OO000O00O0000OOOO ['data']['cash']#line:247
                if float (OO0OO0O00O00OOOO0 )>20 :#line:248
                    O0O0000O0000O0OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:249
                    OOOO0O000OOO00000 ={'authorization':O0OOO00O00O000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0000O0OO0 ),'signstring':O0O0000O0000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:259
                    OO0O0O000O0O0000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:260
                    OO0OOOOOOOOO0O00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO0O000OOO00000 ,data =OO0O0O000O0O0000O ).json ()#line:262
                    print (OO0OOOOOOOOO0O00O )#line:263
    def invitenum (OO000OO0OOO000OO0 ):#line:266
        OOOOO00O0O000O0OO =f'__{timi_new()}'#line:267
        O0OO00OOOO0OO00O0 ={'source':'scsc','authorization':OO000OO0OOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0O000O0OO ),'signstring':OOOOO00O0O000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:278
        O00O0OO00O0OOO000 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO00OOOO0OO00O0 ).json ()#line:279
        if 'status'in O00O0OO00O0OOO000 :#line:281
            if O00O0OO00O0OOO000 ['status']==200 :#line:282
                O0OOO00OOO00OO00O =O00O0OO00O0OOO000 ['data']['invited_count']#line:283
                OO0OOOOO00O0OOOO0 =O00O0OO00O0OOO000 ['data']['invited_second_count']#line:284
                print (f'【我的邀请】:直邀好友:{O0OOO00OOO00OO00O}丨间邀好友:{OO0OOOOO00O0OOOO0}')#line:285
    def game_map (O0000000O00OO000O ):#line:288
        try :#line:289
            OOO0OO0O0000O00OO =f'__{timi_new()}'#line:290
            OOOOO0O0OOO0O0000 ={'source':'scsc','authorization':O0000000O00OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0000O00OO ),'signstring':OOO0OO0O0000O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:301
            O0OOOO0OOO0O00O00 =requests .request ('get',f'{host}/game/map',headers =OOOOO0O0OOO0O0000 ).json ()#line:302
            if 'status'in O0OOOO0OOO0O00O00 :#line:304
                if O0OOOO0OOO0O00O00 ['status']==200 :#line:305
                    for O0O000O0O00O0OOO0 in O0OOOO0OOO0O00O00 ['data']['list'][0 ]['crops']:#line:306
                        OOOOOOO00OOOO0OO0 =O0O000O0O00O0OOO0 ['level']#line:308
                        if OOOOOOO00OOOO0OO0 ==41 :#line:309
                            O0000O0000O00O0OO =O0O000O0O00O0OOO0 ['crop_name']#line:310
                            OOO0OO0O00O000000 =O0O000O0O00O0OOO0 ['count']#line:311
                            if OOO0OO0O00O000000 >0 :#line:312
                                print (f'【农业资产】:{O0000O0000O00O0OO}丨数量:{OOO0OO0O00O000000}')#line:313
        except Exception as OOOOO0O0O0O00OO0O :#line:314
            print (OOOOO0O0O0O00OO0O )#line:315
    def give_gold (OOOO00O0O00OO0000 ):#line:318
        try :#line:319
            O0O0OO0O00O00OO00 =f'__{timi_new()}'#line:320
            O00O0O0OO00O000O0 ={'source':'scsc','authorization':OOOO00O0O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O00O00OO00 ),'signstring':O0O0OO0O00O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:331
            OOO0O0OOOO0O000OO =requests .request ('get',f'{host}/user',headers =O00O0O0OO00O000O0 ).json ()#line:332
            if 'status'in OOO0O0OOOO0O000OO :#line:333
                if OOO0O0OOOO0O000OO ['status']==200 :#line:334
                    if float (OOOO00O0O00OO0000 .doneeNo )!=0 :#line:335
                        OO0OOO00OO0O0O000 =OOO0O0OOOO0O000OO ['data']['assets']['gold']#line:336
                        if float (OO0OOO00OO0O0O000 )>float (OOOO00O0O00OO0000 .innerId ):#line:337
                            O00O0O00OO000O0OO =int (float (OO0OOO00OO0O0O000 )/1.1 )#line:338
                            O0O0OO0O00O00OO00 =f'_doneeNo={OOOO00O0O00OO0000.doneeNo}&quantity={O00O0O00OO000O0OO}_{timi_new()}'#line:339
                            O00O0O0OO00O000O0 ={'source':'scsc','authorization':OOOO00O0O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O00O00OO00 ),'signstring':O0O0OO0O00O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
                            OOOOO0O000O0000OO ={"quantity":O00O0O00OO000O0OO ,"doneeNo":OOOO00O0O00OO0000 .doneeNo }#line:354
                            O000OOOOO0O0OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0O0OO00O000O0 ,data =OOOOO0O000O0000OO ).json ()#line:355
                            if 'status'in O000OOOOO0O0OOO0O :#line:357
                                if O000OOOOO0O0OOO0O ['status']==200 :#line:358
                                    if O000OOOOO0O0OOO0O ['data']:#line:359
                                        print (f'【赠送种子】:赠送{O00O0O00OO000O0OO}种子给{OOOO00O0O00OO0000.doneeNo}成功')#line:360
                    else :#line:361
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:362
        except Exception as OO0OO000OO0OOO000 :#line:363
            print (OO0OO000OO0OOO000 )#line:364
    def invitation (OO0O0OO000OO0O0O0 ):#line:366
        try :#line:367
            _O000O0O00OOOO00O0 =float (bundled_def ())/4 #line:368
            OO00O000O0OO00OO0 =f'_innerId={int(_O000O0O00OOOO00O0)}_{timi_new()}'#line:369
            O00O0OO0OO0O0OO00 ={'source':'scsc','authorization':OO0O0OO000OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000O0OO00OO0 ),'signstring':OO00O000O0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:380
            OOOOOO0O0O0O0O0OO ={"innerId":int (_O000O0O00OOOO00O0 )}#line:381
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O0OO0OO0O0OO00 ,data =OOOOOO0O0O0O0O0OO )#line:382
        except Exception as OO00OOO000OO0OO0O :#line:383
            print (OO00OOO000OO0OO0O )#line:384
    def winning_rewards (OOOOO00OOOO000O00 ):#line:387
        try :#line:388
            OOO0OOOOO00OO0O0O =f'__{timi_new()}'#line:389
            O000000O00000O0O0 ={'source':'scsc','authorization':OOOOO00OOOO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOO00OO0O0O ),'signstring':OOO0OOOOO00OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:400
            OOOO00000OO0OO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O000000O00000O0O0 ).json ()#line:401
            if 'status'in OOOO00000OO0OO00O :#line:403
                if OOOO00000OO0OO00O ['status']==200 :#line:404
                    if OOOO00000OO0OO00O ['data']['amount']:#line:405
                        O00OO00O00OOO00OO =OOOO00000OO0OO00O ['data']['amount']['gold']#line:406
                        return O00OO00O00OOO00OO #line:407
                    else :#line:408
                        return 0 #line:409
        except Exception as O0OOOO00O00O0O0O0 :#line:410
            print (O0OOOO00O00O0O0O0 )#line:411
    def certification (OO0O0OOO00000OOO0 ):#line:414
        try :#line:415
            O0OO0OO0O00OO0OO0 =f'__{timi_new()}'#line:416
            OOO0OO0OO0OO000OO ={'source':'scsc','authorization':OO0O0OOO00000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0O00OO0OO0 ),'signstring':O0OO0OO0O00OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:427
            OOO00000O0OOO000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0OO0OO0OO000OO ).json ()#line:428
            if 'status'in OOO00000O0OOO000O :#line:430
                if OOO00000O0OOO000O ['status']==200 :#line:431
                    if OOO00000O0OOO000O ['data']['result']:#line:432
                        O000O0OO0OO0O00O0 =OOO00000O0OOO000O ['data']['nick_name']#line:433
                        return O000O0OO0OO0O00O0 #line:434
                    else :#line:435
                        return '未实名'#line:436
        except Exception as O0OO0000OOO00OO00 :#line:437
            print (O0OO0000OOO00OO00 )#line:438
    def crops_illustrated (OOOOOO0000O0OO000 ):#line:441
        try :#line:442
            OO00O0O0000OOOO0O =f'__{timi_new()}'#line:443
            O000OO0O00OOOO00O ={'source':'scsc','authorization':OOOOOO0000O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0000OOOO0O ),'signstring':OO00O0O0000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:454
            O0O0O0OO00O0OO0OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000OO0O00OOOO00O ).json ()#line:455
            if 'status'in O0O0O0OO00O0OO0OO :#line:457
                if O0O0O0OO00O0OO0OO ['status']==200 :#line:458
                    O0OO000OOO0O00O00 =O0O0O0OO00O0OO0OO ['data'][0 ]['crops']#line:459
                    for O00OO00000O0O0O00 in O0OO000OOO0O00O00 :#line:460
                        if O00OO00000O0O0O00 ['ill_clover_award']:#line:461
                            if float (O00OO00000O0O0O00 ['ill_clover_award'])>1 :#line:462
                                if O00OO00000O0O0O00 ['is_finish']:#line:463
                                    if not O00OO00000O0O0O00 ['is_getit']:#line:464
                                        if OOOOOO0000O0OO000 .certification ()!='未实名':#line:465
                                            OO00O0O0000OOOO0O =f'_award_level={O00OO00000O0O0O00["level"]}_{timi_new()}'#line:466
                                            O000OO0O00OOOO00O ={'source':'scsc','authorization':OOOOOO0000O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0000OOOO0O ),'signstring':OO00O0O0000OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:477
                                            O000O0OOO0O0O00O0 ={"award_level":O00OO00000O0O0O00 ['level']}#line:478
                                            O0O000O0O0O0OOO0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000OO0O00OOOO00O ,json =O000O0OOO0O0O00O0 ).json ()#line:480
                                            if 'status'in O0O000O0O0O0OOO0O :#line:481
                                                if O0O000O0O0O0OOO0O ['status']==200 :#line:482
                                                    O0OOO0OO0OOOOOOOO =O0O000O0O0O0OOO0O ['data']['ill_clover_award']#line:483
                                                    print (f'【图鉴奖励】:领取{O00OO00000O0O0O00["crop_name"]}成就丨奖励{O0OOO0OO0OOOOOOOO}☘️')#line:485
                                                if O0O000O0O0O0OOO0O ['status']==500 :#line:486
                                                    print (f'【图鉴奖励】:{O0O000O0O0O0OOO0O["message"]}')#line:487
        except Exception as OO0O0O000OO00O000 :#line:488
            print (OO0O0O000OO00O000 )#line:489
    def watched_ad (OO0O00OOO0OOOOOO0 ):#line:492
        try :#line:493
            O00OOOOO0O0O0OOOO =f'__{timi_new()}'#line:494
            O0OO0OO0O0000O00O ={'source':'scsc','authorization':OO0O00OOO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0O0O0OOOO ),'signstring':O00OOOOO0O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            OO00O00O00O00O000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO0O0000O00O ).json ()#line:506
            if 'status'in OO00O00O00O00O000 :#line:508
                if OO00O00O00O00O000 ['status']==200 :#line:509
                    if 'offlineInfo'in OO00O00O00O00O000 ['data']:#line:510
                        time .sleep (random .randint (3 ,5 ))#line:511
                        OOO000O00OOOOO000 =OO00O00O00O00O000 ['data']['offlineInfo']['off_minute']#line:512
                        O000O0O0OOOOOOOO0 =float (OO00O00O00O00O000 ['data']['silver'])/1000000000000 #line:513
                        time .sleep (1 )#line:514
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OO0OO0O0000O00O ).json ()#line:515
                        time .sleep (2 )#line:516
                        O000OO0OOOOO000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OO0O0000O00O ).json ()#line:517
                        if 'status'in O000OO0OOOOO000O0 :#line:519
                            if O000OO0OOOOO000O0 ['status']==200 :#line:520
                                O00000000000O0OO0 =float (O000OO0OOOOO000O0 ['data']['silver'])/1000000000000 #line:521
                                O00OO00OO00O000OO =str (O00000000000O0OO0 -O000O0O0OOOOOOOO0 )[:6 ]#line:522
                                print (f'【离线奖励】:翻倍离线{OOO000O00OOOOO000}分钟奖励🌱数量:{O00OO00OO00O000OO}t粒')#line:523
        except Exception as O0000000O0OO0000O :#line:524
            print (O0000000O0OO0000O )#line:525
    def user_ad (O000OOO000O00O00O ):#line:528
        try :#line:529
            O0000OOOO00O00O0O =f'__{timi_new()}'#line:530
            OO00000O00O00O0O0 ={'source':'scsc','authorization':O000OOO000O00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO00O00O0O ),'signstring':O0000OOOO00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:541
            O0O00O00OO00OOOOO =requests .request ('get',f'{host}/user/ad',headers =OO00000O00O00O0O0 ).json ()#line:542
            if 'status'in O0O00O00OO00OOOOO :#line:544
                if O0O00O00OO00OOOOO ['status']==200 :#line:545
                    O0OO00OOOOO000O00 =O0O00O00OO00OOOOO ['data']['max_time']#line:546
                    OO000O00OO0OOOO00 =O0O00O00OO00OOOOO ['data']['watch_time']#line:547
                    O0O0OOO0OO0OO000O =O0O00O00OO00OOOOO ['data']['added_time']#line:548
                    print (f'【获取种子】:获取🌱剩余{O0O0OOO0OO0OO000O + O0OO00OOOOO000O00 - OO000O00OO0OOOO00}次丨好友提供:{O0O0OOO0OO0OO000O}次')#line:549
                    if O0O0OOO0OO0OO000O +O0OO00OOOOO000O00 -OO000O00OO0OOOO00 >0 :#line:550
                        time .sleep (random .randint (16 ,19 ))#line:551
                        OO00OO00OO0O0OOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO00000O00O00O0O0 ).json ()#line:552
                        if 'status'in OO00OO00OO0O0OOO0 :#line:554
                            if OO00OO00OO0O0OOO0 ['status']==200 :#line:555
                                O0OOO00O00O00O0O0 =float (OO00OO00OO0O0OOO0 ['data']['silver'])/1000000000000 #line:556
                                print (f'【获取种子】:获得🌱:{int(O0OOO00O00O00O0O0)}t粒')#line:557
                                return True #line:558
                            if OO00OO00OO0O0OOO0 ['status']==500 :#line:559
                                OO0O0OO0O00OO0OOO =OO00OO00OO0O0OOO0 ['message']#line:560
                                print (f'【获取种子】:{OO0O0OO0O00OO0OOO}')#line:561
                                return False #line:562
        except Exception as O00O00O0O0OO0O000 :#line:563
            print (O00O00O0O0OO0O000 )#line:564
    def synthetic (O00O0O00OO0O000OO ):#line:567
        global id ,g #line:568
        try :#line:569
            OO0O0O000O00OO00O =O00O0O00OO0O000OO .level_new ()#line:570
            O0OOOO0OO000000OO =random .randint (9 ,11 )#line:571
            OO0O0000O0OO0OO0O =f'_site=8&targetSite={O0OOOO0OO000000OO}_{timi_new()}'#line:572
            O0O00O0OO0OOOOOO0 ={'source':'scsc','authorization':O00O0O00OO0O000OO .token ,'timestamp':timi_new (),'sign':sign (OO0O0000O0OO0OO0O ),'signstring':OO0O0000O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:583
            OOO0O00OOO0OO00O0 ={"site":int (8 ),"targetSite":int (O0OOOO0OO000000OO )}#line:584
            requests .request ('post',f'{host}/game/crops/move',headers =O0O00O0OO0OOOOOO0 ,json =OOO0O00OOO0OO00O0 )#line:585
            while True :#line:586
                O0000O0O0OO00O0OO =f'__{timi_new()}'#line:587
                OOO0O0OO00O0OOO00 ={'source':'scsc','authorization':O00O0O00OO0O000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0O0OO00O0OO ),'signstring':O0000O0O0OO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
                OO0OOOO0000O00000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O0OO00O0OOO00 ).json ()#line:599
                if 'status'in OO0OOOO0000O00000 :#line:601
                    if OO0OOOO0000O00000 ['status']==200 :#line:602
                        O00OOO0O0O00OO000 =OO0OOOO0000O00000 ['data']['cropList']#line:603
                        O00O0OO0O0OO00000 =OO0OOOO0000O00000 ['data']['gameCoreDataDBid']#line:604
                        OO00OO0OOOO000000 =float (OO0OOOO0000O00000 ['data']['silver'])/1000000000000 #line:605
                        OO00O000O0O00OO00 =0 #line:610
                        for O0OO000OO0000OOO0 in O00OOO0O0O00OO000 :#line:611
                            if not O0OO000OO0000OOO0 :#line:612
                                OO0OO0O0OO0O00OO0 =f'_crop_id={O00O0OO0O0OO00000}&site={OO00O000O0O00OO00}_{O00O0O00OO0O000OO.time}'#line:613
                                O0O0OOOOO0OO0000O ={'source':'scsc','authorization':O00O0O00OO0O000OO .token ,'timestamp':O00O0O00OO0O000OO .time ,'sign':sign (OO0OO0O0OO0O00OO0 ),'signstring':OO0OO0O0OO0O00OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:623
                                O0O0O0OO0OOOO00O0 ={"site":OO00O000O0O00OO00 ,"crop_id":O00O0OO0O0OO00000 }#line:624
                                OOO0000000O000000 =requests .request ('post',f'{host}/game/crops/buy',headers =O0O0OOOOO0OO0000O ,data =O0O0O0OO0OOOO00O0 ).json ()#line:625
                                time .sleep (random .randint (1 ,3 )/10 )#line:627
                                if 'status'in OOO0000000O000000 :#line:628
                                    if OOO0000000O000000 ['status']==200 :#line:629
                                        if OOO0000000O000000 ['message']=='种子数量不足':#line:630
                                            OO0O0O000O00OO00O =O00O0O00OO0O000OO .level_new ()#line:631
                                            print (f'【种植合成】:{OOO0000000O000000["message"]}')#line:632
                                            if not O00O0O00OO0O000OO .user_ad ():#line:633
                                                return False #line:634
                                    if OOO0000000O000000 ['status']==500 :#line:635
                                        print (f'【种植合成】:{OOO0000000O000000["message"]}')#line:636
                                        return False #line:637
                            OO00O000O0O00OO00 +=1 #line:638
                        OO0O00O000OO0O000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O0OO00O0OOO00 ).json ()#line:639
                        OOO0OO0OOOOOO00O0 =OO0O00O000OO0O000 ['data']['cropList']#line:640
                        O0O0000O0OO0OO0OO =False #line:641
                        for O0OO000OO0000OOO0 in range (12 ):#line:642
                            id =OOO0OO0OOOOOO00O0 [O0OO000OO0000OOO0 ]['level']#line:643
                            if float (OO0O0O000O00OO00O )-float (id )>9 :#line:644
                                OO0OO0O0O00O00OOO =f'_site={O0OO000OO0000OOO0}_{timi_new()}'#line:645
                                OOO0OO0O0OOOOO0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O0O00OO0O000OO .token ,'timestamp':timi_new (),'sign':sign (OO0OO0O0O00O00OOO ),'signstring':OO0OO0O0O00O00OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:656
                                O00OO0O0O000O00O0 ={"site":O0OO000OO0000OOO0 }#line:657
                                OO0O0O0OO0OOOOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0OO0O0OOOOO0O0 ,data =O00OO0O0O000O00O0 ).json ()#line:659
                                if 'status'in OO0O0O0OO0OOOOO00 :#line:660
                                    if OO0O0O0OO0OOOOO00 ['status']==200 :#line:661
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:662
                            if id !=0 :#line:663
                                for O0000O00OOO0OOOO0 in range (11 ):#line:664
                                    OOOO00OOOOO00O00O =O0000O00OOO0OOOO0 +1 #line:665
                                    g =OOO0OO0OOOOOO00O0 [OOOO00OOOOO00O00O ]['level']#line:666
                                    if id ==g :#line:667
                                        OOOO0OO0OO0O00O00 =O0000O00OOO0OOOO0 +2 #line:668
                                        if OOOO0OO0OO0O00O00 !=O0OO000OO0000OOO0 +1 :#line:669
                                            O00000O00OOOOOO00 =O0OO000OO0000OOO0 +1 #line:670
                                            time .sleep (random .randint (1 ,3 )/10 )#line:672
                                            OO0O0000O0OO0OO0O =f'_site={O00000O00OOOOOO00 - 1}&targetSite={OOOO0OO0OO0O00O00 - 1}_{timi_new()}'#line:673
                                            O0O00O0OO0OOOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O0O00OO0O000OO .token ,'timestamp':timi_new (),'sign':sign (OO0O0000O0OO0OO0O ),'signstring':OO0O0000O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:690
                                            O0O0OO0000OO0OOO0 ={"site":int (O00000O00OOOOOO00 -1 ),"targetSite":int (OOOO0OO0OO0O00O00 -1 )}#line:691
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0O00O0OO0OOOOOO0 ,json =O0O0OO0000OO0OOO0 )#line:692
                                            O0O0000O0OO0OO0OO =True #line:694
                                    if O0O0000O0OO0OO0OO :#line:695
                                        break #line:696
                                if O0O0000O0OO0OO0OO :#line:697
                                    break #line:698
        except :#line:699
            O00O0O00OO0O000OO .synthetic ()#line:700
    def level_new (O0O0OO00O0O00OO0O ):#line:703
        try :#line:704
            OO0O0O0OOO00OOO0O =f'__{timi_new()}'#line:705
            O0OO0O0O00O000O00 ={'source':'scsc','authorization':O0O0OO00O0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO00OOO0O ),'signstring':OO0O0O0OOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:716
            OOOOOO000O00OO0O0 =requests .request ('get',f'{host}/user',headers =O0OO0O0O00O000O00 ).json ()#line:717
            if 'status'in OOOOOO000O00OO0O0 :#line:718
                if OOOOOO000O00OO0O0 ['status']==200 :#line:719
                    return float (OOOOOO000O00OO0O0 ['data']['level'])#line:720
        except Exception as OO0OOOO0O000OO000 :#line:721
            print (OO0OOOO0O000OO000 )#line:722
    def propsraffle (O0OOOOOO0OO0O0O0O ):#line:725
        try :#line:726
            while True :#line:727
                O0OO000000000000O =f'__{timi_new()}'#line:728
                OO0OOOOO0OO0OOOOO ={'source':'scsc','authorization':O0OOOOOO0OO0O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000000000000O ),'signstring':O0OO000000000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:739
                O0O0000OO0OO0O00O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO0OOOOO0OO0OOOOO ).json ()#line:740
                if 'status'in O0O0000OO0OO0O00O :#line:742
                    if O0O0000OO0OO0O00O ['status']==200 :#line:743
                        OO0OOOO00O00OO00O =O0O0000OO0OO0O00O ['data']['rows']#line:744
                        O00OO000O0O0O000O =O0O0000OO0OO0O00O ['data']['vstate']#line:745
                        if OO0OOOO00O00OO00O ==5 or OO0OOOO00O00OO00O ==6 or OO0OOOO00O00OO00O ==7 :#line:746
                            O0OOOO0OO0O000OO0 =O0O0000OO0OO0O00O ['data']['silver']#line:747
                            print (f'【转盘抽奖】:获得种子:{O0OOOO0OO0O000OO0}')#line:748
                        if OO0OOOO00O00OO00O ==1 or OO0OOOO00O00OO00O ==2 or OO0OOOO00O00OO00O ==3 :#line:749
                            O0OO0OO0OO00O000O =O0O0000OO0OO0O00O ['data']['clover']#line:750
                            print (f'【转盘抽奖】:获得三叶草:{O0OO0OO0OO00O000O}')#line:751
                        if OO0OOOO00O00OO00O ==4 or OO0OOOO00O00OO00O ==8 :#line:752
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:753
                        if OO0OOOO00O00OO00O =='抽奖次数已用完':#line:757
                            break #line:791
                time .sleep (random .randint (8 ,15 )/10 )#line:792
        except Exception as OO0OOO00O0OOO00O0 :#line:793
            print (OO0OOO00O0OOO00O0 )#line:794
    def friends_invitation (OO0O00OOO00OO0000 ):#line:797
        try :#line:798
            OO0OO0O0OO000O000 =f'__{timi_new()}'#line:799
            OO00000O00OOO0O00 ={'source':'scsc','authorization':OO0O00OOO00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO000O000 ),'signstring':OO0OO0O0OO000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:810
            O000O00OO00000OOO =requests .request ('get',f'{host}/friends',headers =OO00000O00OOO0O00 ).json ()#line:811
            if 'status'in O000O00OO00000OOO :#line:812
                if O000O00OO00000OOO ['status']==200 :#line:813
                    OO000O0O0000O00O0 =O000O00OO00000OOO ['data']['myInviteter']#line:814
                    if OO000O0O0000O00O0 :#line:815
                        OO00OO0O00OO000O0 =OO000O0O0000O00O0 ['user']['nickname']#line:816
                        O00O000OO00OOO00O =OO0O00OOO00OO0000 .certification ()#line:817
                        print (f'【查邀请人】:我的邀请人:{OO00OO0O00OO000O0}丨实名:{O00O000OO00OOO00O}')#line:818
                    else :#line:819
                        if OO0O00OOO00OO0000 .innerId !='0':#line:820
                            OO0O00OOO00OO0000 .invitation ()#line:821
        except Exception as O0OO0000000OOO00O :#line:822
            print (O0OO0000000OOO00O )#line:823
    def add_clover (OOOOO0O0O00OOO00O ):#line:826
        global golden_seed #line:827
        try :#line:828
            OOO00OOO0000O0O0O =f'__{timi_new()}'#line:829
            O000OOO00O0O00OOO ={'source':'scsc','authorization':OOOOO0O0O00OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0000O0O0O ),'signstring':OOO00OOO0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:840
            OOO0O00O0OOOO000O =requests .request ('get',f'{host}/assets/clovers',headers =O000OOO00O0O00OOO ).json ()#line:841
            if 'status'in OOO0O00O0OOOO000O :#line:843
                if OOO0O00O0OOOO000O ['status']==200 :#line:844
                    O00O0O0000O000OOO =OOO0O00O0OOOO000O ['data']['clover']#line:845
                    OOO0O000O0OOOOOOO =OOO0O00O0OOOO000O ['data']['used_clover']#line:846
                    O00O0000OO000000O =float (O00O0O0000O000OOO )-float (OOO0O000O0OOOOOOO )#line:847
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O000O0OOOOOOO}')#line:848
                    if OOOOO0O0O00OOO00O .certification ()!='未实名':#line:849
                        if O00O0000OO000000O >1 :#line:850
                            OOO00OOO0000O0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O0000OO000000O)}_{timi_new()}'#line:851
                            OO0OOOO000OOOO0OO ={'source':'scsc','authorization':OOOOO0O0O00OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0000O0O0O ),'signstring':OOO00OOO0000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:862
                            OO0OO0O0O00O0OOO0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O0000OO000000O )}#line:863
                            OOOO0O0OO0000OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOOO000OOOO0OO ,data =OO0OO0O0O00O0OOO0 ).json ()#line:864
                            if 'status'in OOOO0O0OO0000OOOO :#line:866
                                if OOOO0O0OO0000OOOO ['status']==200 :#line:867
                                    print (f'【参与抽奖】:添加☘️:{OOOO0O0OO0000OOOO["data"]}丨数量:{O00O0000OO000000O}')#line:868
                                if OOOO0O0OO0000OOOO ['status']==500 :#line:869
                                    print (f'【参与抽奖】:添加☘️:{OOOO0O0OO0000OOOO["message"]}')#line:870
            OOO00O0OOOOO000OO =requests .request ('get',f'{host}/lottery',headers =O000OOO00O0O00OOO ).json ()#line:871
            OOO0OOOOOOO0O0000 =OOOOO0O0O00OOO00O .winning_rewards ()#line:873
            if 'status'in OOO00O0OOOOO000OO :#line:874
                if OOO00O0OOOOO000OO ['status']==200 :#line:875
                    OOO0OOOOOO0O0O000 =OOO00O0OOOOO000OO ['data'][0 ]['day_get_gold_quantity']#line:876
                    golden_seed +=float (OOO0OOOOOO0O0O000 )#line:877
                    OO0O000OOOOO0O0OO =OOO00O0OOOOO000OO ['data'][1 ]['value']#line:878
                    OO000OOOO0OO0OOOO =OOO00O0OOOOO000OO ['data'][0 ]['join_number']#line:879
                    OO000OOOOOO0000O0 =int (float (OOO00O0OOOOO000OO ['data'][0 ]['totalValue']))#line:880
                    OO00OOO00O0O00O00 =float (OO0O000OOOOO0O0OO /OO000OOOOOO0000O0 )*10000 #line:881
                    OO0O00O0OOOO00O0O =OO000OOOOOO0000O0 /OO000OOOO0OO0OOOO #line:882
                    print (f'【参与抽奖】:预计每天中{str(OOO0OOOOOO0O0O000)[:6]}颗金种子丨好友收益:{str(OOO0OOOOOOO0O0000)[:6]}')#line:883
                    print (f'【抽奖统计】:每1万☘️中{str(OO00OOO00O0O00O00)[:6]}颗金种子丨☘️人均:{str(OO0O00O0OOOO00O0O)[:7]}️')#line:884
        except Exception as OOOOO00OO00O0O00O :#line:885
            print (OOOOO00OO00O0O00O )#line:886
    def energy (O0O0OOO0O0OO0000O ):#line:890
        try :#line:891
            while True :#line:892
                OOOOOOO0OO0OOOO00 =f'__{timi_new()}'#line:893
                O0000O0O0OO0OOO00 ={'source':'scsc','authorization':O0O0OOO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OO0OOOO00 ),'signstring':OOOOOOO0OO0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:904
                OO0OO0OOOO00OOOOO =requests .request ('get',f'{host}/energy/general',headers =O0000O0O0OO0OOO00 ).json ()#line:905
                if 'status'in OO0OO0OOOO00OOOOO :#line:907
                    if OO0OO0OOOO00OOOOO ['status']==200 :#line:908
                        OOOO0OO00000OO0OO =OO0OO0OOOO00OOOOO ['data']['ordinary_water']#line:909
                        OO0000O000O0OO0O0 =OO0OO0OOOO00OOOOO ['data']['ordinary_fertilizer']#line:910
                        OOOOOO00O000000OO =OO0OO0OOOO00OOOOO ['data']['videoStatus']#line:911
                        O000OO0O0OOOO00OO =OO0OO0OOOO00OOOOO ['data']['waterVideoKey']#line:912
                        print (f'【我的营养】:肥料:{str(OO0000O000O0OO0O0).split(".")[0]}丨水滴:{str(OOOO0OO00000OO0OO).split(".")[0]}')#line:913
                        if float (OO0000O000O0OO0O0 )<96 :#line:914
                            if OOOOOO00O000000OO :#line:915
                                time .sleep (random .randint (160 ,180 )/10 )#line:916
                                OOOO00O00OO00OOOO =99 -float (OO0000O000O0OO0O0 )#line:917
                                O0O00000O0O0O00O0 ={"fertilizer":str (OOOO00O00OO00OOOO ).split ('.')[0 ]}#line:918
                                O0O000O00OOOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0000O0O0OO0OOO00 ).json ()#line:919
                                if 'status'in O0O000O00OOOO00O0 :#line:921
                                    if O0O000O00OOOO00O0 ['status']==200 :#line:922
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O00OOOO00O0["message"]}')#line:923
                                    if O0O000O00OOOO00O0 ['status']==500 :#line:924
                                        print (f'【购买肥料】:看广告获取肥料:{O0O000O00OOOO00O0["message"]}')#line:925
                                        break #line:926
                                if float (OO0000O000O0OO0O0 )<78 :#line:928
                                    OOOO00O00OO00OOOO =80 -float (OO0000O000O0OO0O0 )#line:929
                                    OO000O0O0OO00OO00 =f'_fertilizer={int(OOOO00O00OO00OOOO)}_{timi_new()}'#line:930
                                    O000O0O0O0000OO00 ={'source':'scsc','authorization':O0O0OOO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O0OO00OO00 ),'signstring':OO000O0O0OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
                                    OOO000OOO0OOO00O0 ={"fertilizer":int (OOOO00O00OO00OOOO )}#line:942
                                    O0OOOO000OO0O0OO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000O0O0O0000OO00 ,data =OOO000OOO0OOO00O0 ).json ()#line:944
                                    if 'status'in O0OOOO000OO0O0OO0 :#line:946
                                        if O0OOOO000OO0O0OO0 ['status']==200 :#line:947
                                            print (f'【购买肥料】:购买肥料:{O0OOOO000OO0O0OO0["message"]}丨数量:{int(OOOO00O00OO00OOOO)}')#line:948
                                        if O0OOOO000OO0O0OO0 ['status']==500 :#line:949
                                            print (f'【购买肥料】:购买肥料:{O0OOOO000OO0O0OO0["message"]}丨数量:{int(OOOO00O00OO00OOOO)}')#line:950
                                            O0O00OO0O000O000O =O0OOOO000OO0O0OO0 ["message"].split ('-')[1 ]#line:951
                                            O00O0OO0O00OOO0O0 =f'__{timi_new()}'#line:952
                                            O0O0OOOOOO0O0OOOO ={'source':'scsc','authorization':O0O0OOO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0O00OOO0O0 ),'signstring':O00O0OO0O00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                                            OO0000000OOO0O0OO =requests .request ('get',f'{host}/user',headers =O0O0OOOOOO0O0OOOO ).json ()#line:964
                                            if 'status'in OO0000000OOO0O0OO :#line:965
                                                if OO0000000OOO0O0OO ['status']==200 :#line:966
                                                    O000OO00O00O000O0 =OO0000000OOO0O0OO ['data']['inner_id']#line:967
                                                    if give_gold (O000OO00O00O000O0 ,float (O0O00OO0O000O000O )+1 ):#line:968
                                                        O0O0OOO0O0OO0000O .energy ()#line:969
                        if float (OOOO0OO00000OO0OO )<880 :#line:970
                            if O000OO0O0OOOO00OO :#line:971
                                time .sleep (random .randint (160 ,180 )/10 )#line:972
                                O000OOO0OO0OO00O0 =999 -float (OOOO0OO00000OO0OO )#line:973
                                O0000OOO0OO0O0000 ={"water":str (O000OOO0OO0OO00O0 ).split ('.')[0 ]}#line:974
                                OOO00OO000OOO000O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0000O0O0OO0OOO00 ).json ()#line:975
                                if 'status'in OOO00OO000OOO000O :#line:977
                                    if OOO00OO000OOO000O ['status']==200 :#line:978
                                        print (f'【购买水滴】:看广告获取水滴:{OOO00OO000OOO000O["message"]}')#line:979
                                    if OOO00OO000OOO000O ['status']==500 :#line:980
                                        print (f'【购买水滴】:看广告获取水滴:{OOO00OO000OOO000O["message"]}')#line:981
                                        break #line:982
                                if float (OOOO0OO00000OO0OO )<780 :#line:983
                                    O000OOO0OO0OO00O0 =800 -float (OOOO0OO00000OO0OO )#line:984
                                    O0000OOO0OOO0O00O =f'_water={int(O000OOO0OO0OO00O0)}_{timi_new()}'#line:985
                                    OOOO0OOO0OO00OOO0 ={'source':'scsc','authorization':O0O0OOO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0OOO0O00O ),'signstring':O0000OOO0OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                    OOO0OO0000O00O00O ={"water":int (O000OOO0OO0OO00O0 )}#line:997
                                    OOO0OOO0OO00OO0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOOO0OOO0OO00OOO0 ,data =OOO0OO0000O00O00O ).json ()#line:999
                                    if 'status'in OOO0OOO0OO00OO0OO :#line:1001
                                        if OOO0OOO0OO00OO0OO ['status']==200 :#line:1002
                                            print (f'【购买水滴】:购买水滴:{OOO0OOO0OO00OO0OO["message"]}丨数量:{int(O000OOO0OO0OO00O0)}')#line:1003
                                        if OOO0OOO0OO00OO0OO ['status']==500 :#line:1004
                                            print (f'【购买水滴】:购买水滴:{OOO0OOO0OO00OO0OO["message"]}丨数量:{int(O000OOO0OO0OO00O0)}')#line:1005
                                            O0O00OO0O000O000O =OOO0OOO0OO00OO0OO ["message"].split ('-')[1 ]#line:1006
                                            O00O0OO0O00OOO0O0 =f'__{timi_new()}'#line:1007
                                            O0O0OOOOOO0O0OOOO ={'source':'scsc','authorization':O0O0OOO0O0OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0O00OOO0O0 ),'signstring':O00O0OO0O00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1018
                                            OO0000000OOO0O0OO =requests .request ('get',f'{host}/user',headers =O0O0OOOOOO0O0OOOO ).json ()#line:1019
                                            if 'status'in OO0000000OOO0O0OO :#line:1020
                                                if OO0000000OOO0O0OO ['status']==200 :#line:1021
                                                    O000OO00O00O000O0 =OO0000000OOO0O0OO ['data']['inner_id']#line:1022
                                                    if give_gold (O000OO00O00O000O0 ,float (O0O00OO0O000O000O )+1 ):#line:1023
                                                        O0O0OOO0O0OO0000O .energy ()#line:1024
                        break #line:1025
        except Exception as O0OOO0OO0000O0000 :#line:1027
            print (O0OOO0OO0000O0000 )#line:1028
def bundled_def ():#line:1030
    OOO0OO0000OOO00O0 =['5570536','7750212','7911652','7911680','7805624']#line:1031
    return OOO0OO0000OOO00O0 [random .randint (0 ,len (OOO0OO0000OOO00O0 )-1 )]#line:1032
def version_of_the_validation ():#line:1036
    return str ((88 -56 )/10 )#line:1037
def sc2 ():#line:1039
    return "19319#$%^&*((*"#line:1040
def OO00OO0OO0OO00OO00o0 ():#line:1042
    return hashlib .md5 ((socket .gethostbyname (socket .getfqdn (socket .gethostname ()))+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1043
def gitee_validation ():#line:1045
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1046
def gitee_edition ():#line:1048
    try :#line:1049
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1050
    except :#line:1051
        sys .exit (0 )#line:1052
def O000OO000O0O00OOO00 ():#line:1057
    try :#line:1058
        OO0O0OOO0000O00O0 =gitee_edition ()#line:1059
        if version_of_the_validation ()<OO0O0OOO0000O00O0 ['CityEarth']['edition']:#line:1060
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0000O00O0["CityEarth"]["edition"]}   ❌')#line:1061
            print (f'更新内容=>>{OO0O0OOO0000O00O0["CityEarth"]["content"]}   🎉')#line:1062
        else :#line:1063
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0000O00O0["CityEarth"]["edition"]}   ✅')#line:1064
            print (f'更新内容=>> {OO0O0OOO0000O00O0["CityEarth"]["content"]}   🎉')#line:1065
    except Exception as O00O0O0OOOOO00O0O :#line:1066
        print (O00O0O0OOOOO00O0O )#line:1067
def sc3 ():#line:1069
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1070
if __name__ =='__main__':#line:1074
    start ()#line:1075
