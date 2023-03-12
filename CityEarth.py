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
@ 版本  3.5
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
        OOOO00OO00O0OO000 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(OOOO00OO00O0OO000)}个账号==========")#line:13
        for O000O000OO0O0O0O0 in OOOO00OO00O0OO000 :#line:14
            O00OOO0O00OO0O00O =[]#line:15
            print (f"------------正在执行第{OOOO00OO00O0OO000.index(O000O000OO0O0O0O0) + 1}个账号------------")#line:16
            O0OOOOO000OOOOO0O =CityEarth (O000O000OO0O0O0O0 ,O00OOO0O00OO0O00O ,OOOO00OO00O0OO000 .index (O000O000OO0O0O0O0 ))#line:17
            def OOOOO0O00OO000OOO ():#line:18
                if O0OOOOO000OOOOO0O .base_info ():#line:20
                    O0OOOOO000OOOOO0O .sealing ()#line:22
                    O0OOOOO000OOOOO0O .invitenum ()#line:24
                    O0OOOOO000OOOOO0O .game_map ()#line:26
                    O0OOOOO000OOOOO0O .friends_invitation ()#line:28
                    O0OOOOO000OOOOO0O .energy ()#line:30
                    O0OOOOO000OOOOO0O .add_clover ()#line:32
                    O0OOOOO000OOOOO0O .propsraffle ()#line:34
                    O0OOOOO000OOOOO0O .synthetic ()#line:36
                    O0OOOOO000OOOOO0O .crops_illustrated ()#line:38
                    O0OOOOO000OOOOO0O .give_gold ()#line:40
                    O0OOOOO000OOOOO0O .withdraw ()#line:42
            O0O0000000O00000O =threading .Thread (target =OOOOO0O00OO000OOO )#line:44
            O0O0000000O00000O .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------正在处理推送通知------------")#line:47
        time .sleep (0.5 )#line:48
        OO00O0OO000OO0O00 =format_msg ()#line:49
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO00O0OO000OO0O00 +' ')#line:50
    except Exception as OOO0OO0000OO0OO0O :#line:51
        print (OOO0OO0000OO0OO0O )#line:52
def give_gold (OOOO0OOOO00O00O00 ,O0O0OOO0OOOOO0O0O ):#line:55
        try :#line:56
            O0000OO00O000OOOO =f'_doneeNo={OOOO0OOOO00O00O00}&quantity={int(O0O0OOO0OOOOO0O0O)}_{timi_new()}'#line:57
            OO00000OOOOOO0O0O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000OO00O000OOOO ),'signstring':O0000OO00O000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:68
            O0O0OOO0O0000O0OO ={"quantity":int (O0O0OOO0OOOOO0O0O ),"doneeNo":OOOO0OOOO00O00O00 }#line:72
            OOOOO000OO00000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OO00000OOOOOO0O0O ,data =O0O0OOO0O0000O0OO ).json ()#line:73
            if 'status'in OOOOO000OO00000O0 :#line:75
                if OOOOO000OO00000O0 ['status']==200 :#line:76
                    if OOOOO000OO00000O0 ['data']:#line:77
                        print (f'【赠送种子】:赠送{int(O0O0OOO0OOOOO0O0O)}种子给{OOOO0OOOO00O00O00}成功')#line:78
                        return True #line:79
                if OOOOO000OO00000O0 ['status']==401 :#line:80
                    print (f'【赠送种子】:{OOOOO000OO00000O0["message"]}')#line:81
                    return False #line:82
                if OOOOO000OO00000O0 ['status']==500 :#line:83
                    print (f'【赠送种子】:{OOOOO000OO00000O0["message"]}')#line:84
                    return False #line:85
            return False #line:86
        except Exception as OOO00OO0OO0O0O000 :#line:87
            print (OOO00OO0OO0O0O000 )#line:88
def kvkv ():#line:89
    return '/vastzzzl/vastzzzl/raw/master'#line:90
def sign (O00O0O000O0OOO00O ):#line:93
    OOOO0OOO0OO00O00O =hashlib .md5 (O00O0O000O0OOO00O .encode ()).hexdigest ()#line:94
    O0OOO0OO00000000O =sc1 ()#line:95
    O0000OO0O00000000 =sc2 ()#line:96
    OO0O000O0OOOO0O00 =sc3 ()#line:97
    OO0OO00OO0OO0OOO0 =O0OOO0OO00000000O +OOOO0OOO0OO00O00O +O0000OO0O00000000 +OO0O000O0OOOO0O00 #line:98
    OO000OOO0OOO0O0O0 =hashlib .md5 (OO0OO00OO0OO0OOO0 .encode ()).hexdigest ()#line:99
    return OO000OOO0OOO0O0O0 #line:100
def format_msg ():#line:104
    OO0OO0OO00000O00O =""#line:105
    for OO0O000O000O00OO0 in msg_list :#line:106
        OO0OO0OO00000O00O +=str (OO0O000O000O00OO0 )+"\r\n"#line:107
    return OO0OO0OO00000O00O #line:108
def sc1 ():#line:110
    return "scsc%^&*"#line:111
def O000OO0O00OO00O00 ():#line:113
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:114
        pass #line:115
    else :#line:116
        exit (1 )#line:117
def timi_new ():#line:119
    return str (int (time .time ()*1000 ))#line:120
json_path ="CityEarth_data.json"#line:123
json_path1 ="CityEarth_data.json"#line:124
dict ={}#line:125
def get_json_data (O0000O0000OOOO00O ,OO00OOOO0O00OOO00 ,OOO0O000O0O0O00O0 ,OO0OOOO0OO00O0OOO ):#line:127
    with open (O0000O0000OOOO00O ,'rb')as OO0O00O00OO0OO0OO :#line:129
        OO00000OO0OO0OOO0 =json .load (OO0O00O00OO0OO0OO )#line:130
        OO00000OO0OO0OOO0 ['data'][OO00OOOO0O00OOO00 ][OOO0O000O0O0O00O0 ]=OO0OOOO0OO00O0OOO #line:131
        OO00O0O00OO0OO000 =OO00000OO0OO0OOO0 #line:132
    OO0O00O00OO0OO0OO .close ()#line:133
    return OO00O0O00OO0OO000 #line:134
def write_json_data (OO000OOO000O0OOOO ):#line:136
    with open (json_path1 ,'w')as O0O0OOOOOOO0O000O :#line:137
        json .dump (OO000OOO000O0OOOO ,O0O0OOOOOOO0O000O )#line:138
    O0O0OOOOOOO0O000O .close ()#line:139
    return True #line:140
class CityEarth :#line:142
    def __init__ (O000O0000OOO0O00O ,O00O0OOOOOOOOO0O0 ,O0OOOOOO0O000OOO0 ,O000O0OO00OOO0O0O ):#line:144
        try :#line:145
            O000O0000OOO0O00O .msg =O0OOOOOO0O000OOO0 #line:146
            O000O0000OOO0O00O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:147
            O000O0000OOO0O00O .token =O00O0OOOOOOOOO0O0 ['authorization']#line:148
            O000O0000OOO0O00O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:149
            O000O0000OOO0O00O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:150
            O000O0000OOO0O00O .elephant_user =O00O0OOOOOOOOO0O0 ['elephant_user']#line:151
            O000O0000OOO0O00O .elephant_pswd =O00O0OOOOOOOOO0O0 ['elephant_pswd']#line:152
            O000O0000OOO0O00O .elephant_Task_ID =O00O0OOOOOOOOO0O0 ['elephant_Task_ID']#line:153
            O000O0000OOO0O00O .len_new =O000O0OO00OOO0O0O #line:154
        except :#line:155
            print ('变量格式错误')#line:156
    def base_info (O0O0O00O000OOO00O ):#line:159
        try :#line:160
            O0O0O00O000OOO00O .watched_ad ()#line:162
            OO0O0OOOO00OOOO00 =f'__{timi_new()}'#line:163
            O0000OO00O000O0OO ={'source':'scsc','authorization':O0O0O00O000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOO00OOOO00 ),'signstring':OO0O0OOOO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:174
            O0OO00OOO000O00O0 =requests .request ('get',f'{host}/user',headers =O0000OO00O000O0OO ).json ()#line:175
            if 'status'in O0OO00OOO000O00O0 :#line:177
                if O0OO00OOO000O00O0 ['status']==200 :#line:178
                    OOOO0O0O0O0OOOO0O =O0OO00OOO000O00O0 ['data']['nickname']#line:179
                    O00OOOO000OO0000O =O0OO00OOO000O00O0 ['data']['inner_id']#line:180
                    OO0OO0000OOO00OO0 =O0OO00OOO000O00O0 ['data']['assets']['gold']#line:181
                    O0O000O00O00000OO =O0OO00OOO000O00O0 ['data']['level']#line:182
                    print (f'【账号信息】:昵称:{OOOO0O0O0O0OOOO0O[:5]}丨ID:{O00OOOO000OO0000O}丨等级:{O0O000O00O00000OO}丨金种子:{str(OO0OO0000OOO00OO0).split(".")[0]}')#line:183
                    if 'wx_'in OOOO0O0O0O0OOOO0O :#line:184
                        O0O0O00O000OOO00O .change_nickname ()#line:185
                if O0OO00OOO000O00O0 ['status']==401 :#line:186
                    print ('【账号信息】:账号失效正在尝试登录')#line:187
                    if O0O0O00O000OOO00O .elephant_user =='f':#line:188
                        return False #line:189
                    O000000O0O000000O =Invalid_login .addtask (elephant_user =O0O0O00O000OOO00O .elephant_user ,elephant_pswd =O0O0O00O000OOO00O .elephant_pswd ,elephant_Task_ID =O0O0O00O000OOO00O .elephant_Task_ID )#line:190
                    O0O0OOO0O000OOOO0 =get_json_data (json_path ,O0O0O00O000OOO00O .len_new ,'authorization',O000000O0O000000O )#line:191
                    if write_json_data (O0O0OOO0O000OOOO0 ):#line:192
                        print ('正在写入账号配置文件')#line:193
                    return False #line:194
                if O0OO00OOO000O00O0 ['status']==500 :#line:195
                    return False #line:196
            return True #line:197
        except Exception as OO0O00OOOO0000000 :#line:198
            print (OO0O00OOOO0000000 )#line:199
    def sealing (O0OO00OO00OOO0OOO ):#line:202
        try :#line:203
            OO00O00OO00OO0O00 =f'__{timi_new()}'#line:204
            OO000O0000O0000OO ={'source':'scsc','authorization':O0OO00OO00OOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OO00OO0O00 ),'signstring':OO00O00OO00OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO000O0000O0000OO )#line:216
            requests .request ('get',f'{host}/packsack/list',headers =OO000O0000O0000OO )#line:217
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO000O0000O0000OO )#line:218
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO000O0000O0000OO )#line:219
            requests .request ('get',f'{host}/user',headers =OO000O0000O0000OO )#line:220
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO000O0000O0000OO )#line:221
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO000O0000O0000OO )#line:222
            requests .request ('post',f'{host}/announcement/announcement',headers =OO000O0000O0000OO )#line:223
            requests .request ('get',f'{host}/game/getAllData',headers =OO000O0000O0000OO )#line:224
            requests .request ('get',f'{host}/assets',headers =OO000O0000O0000OO )#line:225
        except Exception as O0OOO00O0000O00O0 :#line:226
            print (O0OOO00O0000O00O0 )#line:227
    def change_nickname (OOOO000O00OO00OOO ):#line:231
        try :#line:232
            OO00OOOOO00OO00OO =timi_new ()#line:233
            O00000000OO0OOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:234
            OOO0OOO0OO0OOOOO0 =requests .request ('post','https://www.qmsjmfb.com/',data =O00000000OO0OOO00 ).text #line:235
            O0OO00O0OO00O00OO =re .findall ('<ul><li>(.*?)</li>',OOO0OOO0OO0OOOOO0 )[0 ][:3 ]#line:236
            O0OO00O00O00O0OO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0OO00O0OO00O00OO}').json ()#line:237
            O0OOOO0000OO0O0OO =O0OO00O00O00O0OO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:238
            O0OOOOO0O0OOO0O00 ={"nickname":O0OOOO0000OO0O0OO }#line:239
            OO0O0000O0OOOO0O0 =f'_nickname={O0OOOO0000OO0O0OO}_{OO00OOOOO00OO00OO}'#line:240
            O00OOOOOO0O000000 ={'source':'scsc','authorization':OOOO000O00OO00OOO .token ,'timestamp':OO00OOOOO00OO00OO ,'sign':sign (OO0O0000O0OOOO0O0 ),'signstring':OO0O0000O0OOOO0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:251
            O00O00000O0000000 =requests .request ('patch',f'{host}/user/nickname',headers =O00OOOOOO0O000000 ,data =O0OOOOO0O0OOO0O00 ).json ()#line:252
            if 'status'in O00O00000O0000000 :#line:254
                if O00O00000O0000000 ['status']==200 :#line:255
                    print (f'【修改网名】:网名:{O0OOOO0000OO0O0OO}丨{O00O00000O0000000["message"]}')#line:256
        except Exception as O0O00O00O0000OO00 :#line:257
            print (O0O00O00O0000OO00 )#line:258
    def withdraw (OO0O0OOO0OO0O000O ):#line:263
        OO00000OO0000O000 =f'__{timi_new()}'#line:264
        O00O0O000OOO0OO0O ={'source':'scsc','authorization':OO0O0OOO0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0000O000 ),'signstring':OO00000OO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:275
        OOOOO0O000OOOOOOO =requests .request ('get',f'{host}/assets',headers =O00O0O000OOO0OO0O ).json ()#line:276
        if 'status'in OOOOO0O000OOOOOOO :#line:278
            if OOOOO0O000OOOOOOO ['status']==200 :#line:279
                OOOO0O0OOO0O0O0O0 =OOOOO0O000OOOOOOO ['data']['cash']#line:280
                if float (OOOO0O0OOO0O0O0O0 )>20 :#line:281
                    OO00000OO0000O000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:282
                    O00O0O000OOO0OO0O ={'authorization':OO0O0OOO0OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0000O000 ),'signstring':OO00000OO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
                    O0OO00OO0O00OOO00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:293
                    OOO0OO00O000O00O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O0O000OOO0OO0O ,data =O0OO00OO0O00OOO00 ).json ()#line:295
                    print (OOO0OO00O000O00O0 )#line:296
    def invitenum (OOO0OOO0OO0000000 ):#line:299
        O00000O000O0O000O =f'__{timi_new()}'#line:300
        O00O00000OO0O0OOO ={'source':'scsc','authorization':OOO0OOO0OO0000000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O000O0O000O ),'signstring':O00000O000O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:311
        OO00O00000OO00000 =requests .request ('get',f'{host}/invite/invitenum',headers =O00O00000OO0O0OOO ).json ()#line:312
        if 'status'in OO00O00000OO00000 :#line:314
            if OO00O00000OO00000 ['status']==200 :#line:315
                OO0OOO000000OOOOO =OO00O00000OO00000 ['data']['invited_count']#line:316
                OOOO0OO0OOO000000 =OO00O00000OO00000 ['data']['invited_second_count']#line:317
                print (f'【我的邀请】:直邀好友:{OO0OOO000000OOOOO}丨间邀好友:{OOOO0OO0OOO000000}')#line:318
    def game_map (O00OO0OOO000OO0OO ):#line:321
        try :#line:322
            O0O0OO0000O0OO0O0 =f'__{timi_new()}'#line:323
            O000OO0O0O0O0OOOO ={'source':'scsc','authorization':O00OO0OOO000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0000O0OO0O0 ),'signstring':O0O0OO0000O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:334
            OO000OO0OO0O0OO00 =requests .request ('get',f'{host}/game/map',headers =O000OO0O0O0O0OOOO ).json ()#line:335
            if 'status'in OO000OO0OO0O0OO00 :#line:337
                if OO000OO0OO0O0OO00 ['status']==200 :#line:338
                    for O00OO0OOO0O00O00O in OO000OO0OO0O0OO00 ['data']['list'][0 ]['crops']:#line:339
                        OOOOO0OOO000OOOOO =O00OO0OOO0O00O00O ['level']#line:341
                        if OOOOO0OOO000OOOOO ==41 :#line:342
                            O00O0OOO00OO0O0OO =O00OO0OOO0O00O00O ['crop_name']#line:343
                            O0O00OOO0OO0000O0 =O00OO0OOO0O00O00O ['count']#line:344
                            if O0O00OOO0OO0000O0 >0 :#line:345
                                print (f'【农业资产】:{O00O0OOO00OO0O0OO}丨数量:{O0O00OOO0OO0000O0}')#line:346
        except Exception as OO00OO0000000OOOO :#line:347
            print (OO00OO0000000OOOO )#line:348
    def give_gold (OOOO000000OO00O00 ):#line:351
        try :#line:352
            OOOO0O00O0OOO00O0 =f'__{timi_new()}'#line:353
            OOOO00OO00O000O0O ={'source':'scsc','authorization':OOOO000000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0OOO00O0 ),'signstring':OOOO0O00O0OOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:364
            OO00OOOOO0O00O000 =requests .request ('get',f'{host}/user',headers =OOOO00OO00O000O0O ).json ()#line:365
            if 'status'in OO00OOOOO0O00O000 :#line:366
                if OO00OOOOO0O00O000 ['status']==200 :#line:367
                    if float (OOOO000000OO00O00 .doneeNo )!=0 :#line:368
                        OO00OOOO000OO0000 =OO00OOOOO0O00O000 ['data']['assets']['gold']#line:369
                        if float (OO00OOOO000OO0000 )>float (OOOO000000OO00O00 .innerId ):#line:370
                            O000O000O000O0O00 =int (float (OO00OOOO000OO0000 )/1.1 )#line:371
                            OOOO0O00O0OOO00O0 =f'_doneeNo={OOOO000000OO00O00.doneeNo}&quantity={O000O000O000O0O00}_{timi_new()}'#line:372
                            OOOO00OO00O000O0O ={'source':'scsc','authorization':OOOO000000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0OOO00O0 ),'signstring':OOOO0O00O0OOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:383
                            OOO00OOOO00O00O00 ={"quantity":O000O000O000O0O00 ,"doneeNo":OOOO000000OO00O00 .doneeNo }#line:387
                            O0O00OOO0O000OO00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO00OO00O000O0O ,data =OOO00OOOO00O00O00 ).json ()#line:388
                            if 'status'in O0O00OOO0O000OO00 :#line:390
                                if O0O00OOO0O000OO00 ['status']==200 :#line:391
                                    if O0O00OOO0O000OO00 ['data']:#line:392
                                        print (f'【赠送种子】:赠送{O000O000O000O0O00}种子给{OOOO000000OO00O00.doneeNo}成功')#line:393
                    else :#line:394
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:395
        except Exception as O00O000O00O00OOOO :#line:396
            print (O00O000O00O00OOOO )#line:397
    def invitation (O00OOO00000OOO0O0 ):#line:399
        try :#line:400
            _O0O0OOOO000O0OO00 =float (bundled_def ())/4 #line:401
            OO0O000O00OOOO0O0 =f'_innerId={int(_O0O0OOOO000O0OO00)}_{timi_new()}'#line:402
            OO00OO00000O0O00O ={'source':'scsc','authorization':O00OOO00000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O000O00OOOO0O0 ),'signstring':OO0O000O00OOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            OOOOO000OO00O0OOO ={"innerId":int (_O0O0OOOO000O0OO00 )}#line:414
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO00OO00000O0O00O ,data =OOOOO000OO00O0OOO )#line:415
        except Exception as O00000O0O0OO0O00O :#line:416
            print (O00000O0O0OO0O00O )#line:417
    def winning_rewards (O0OO00O0OOO00O0O0 ):#line:420
        try :#line:421
            O0O0000O0OOOOOOOO =f'__{timi_new()}'#line:422
            O0OOOO00O0O0O00OO ={'source':'scsc','authorization':O0OO00O0OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000O0OOOOOOOO ),'signstring':O0O0000O0OOOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:433
            O0OO0OOO00O00O00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOO00O0O0O00OO ).json ()#line:434
            if 'status'in O0OO0OOO00O00O00O :#line:436
                if O0OO0OOO00O00O00O ['status']==200 :#line:437
                    if O0OO0OOO00O00O00O ['data']['amount']:#line:438
                        O0OO0O00O0OO0O0OO =O0OO0OOO00O00O00O ['data']['amount']['gold']#line:439
                        return O0OO0O00O0OO0O0OO #line:440
                    else :#line:441
                        return 0 #line:442
        except Exception as O0OO00OO0000OO0OO :#line:443
            print (O0OO00OO0000OO0OO )#line:444
    def certification (O000O000OOOO0O0OO ):#line:447
        try :#line:448
            OO0O00O0O0OOO00O0 =f'__{timi_new()}'#line:449
            OO0OO0OOO00OO0000 ={'source':'scsc','authorization':O000O000OOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0O0OOO00O0 ),'signstring':OO0O00O0O0OOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:460
            O0OOO0OO0OO0O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OO0OOO00OO0000 ).json ()#line:461
            if 'status'in O0OOO0OO0OO0O00O0 :#line:463
                if O0OOO0OO0OO0O00O0 ['status']==200 :#line:464
                    if O0OOO0OO0OO0O00O0 ['data']['result']:#line:465
                        O000OOOO00OOO00O0 =O0OOO0OO0OO0O00O0 ['data']['nick_name']#line:466
                        return O000OOOO00OOO00O0 #line:467
                    else :#line:468
                        return '未实名'#line:469
        except Exception as O000O0O0O0O0O0O00 :#line:470
            print (O000O0O0O0O0O0O00 )#line:471
    def crops_illustrated (OO0O000O00O00O0O0 ):#line:474
        try :#line:475
            OO0OOOOOO0OO00000 =f'__{timi_new()}'#line:476
            OO0O00O0O000O00O0 ={'source':'scsc','authorization':OO0O000O00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO0OO00000 ),'signstring':OO0OOOOOO0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
            OO0O0000000O00OOO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00O0O000O00O0 ).json ()#line:488
            if 'status'in OO0O0000000O00OOO :#line:490
                if OO0O0000000O00OOO ['status']==200 :#line:491
                    O0000O0OOO0OO000O =OO0O0000000O00OOO ['data'][0 ]['crops']#line:492
                    for OO0O000000O0O0OOO in O0000O0OOO0OO000O :#line:493
                        if OO0O000000O0O0OOO ['ill_clover_award']:#line:494
                            if float (OO0O000000O0O0OOO ['ill_clover_award'])>1 :#line:495
                                if OO0O000000O0O0OOO ['is_finish']:#line:496
                                    if not OO0O000000O0O0OOO ['is_getit']:#line:497
                                        if OO0O000O00O00O0O0 .certification ()!='未实名':#line:498
                                            OO0OOOOOO0OO00000 =f'_award_level={OO0O000000O0O0OOO["level"]}_{timi_new()}'#line:499
                                            OO0O00O0O000O00O0 ={'source':'scsc','authorization':OO0O000O00O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOOO0OO00000 ),'signstring':OO0OOOOOO0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                            OOO000OOO0000OOOO ={"award_level":OO0O000000O0O0OOO ['level']}#line:511
                                            OOO0O00O0OOOOOOOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00O0O000O00O0 ,json =OOO000OOO0000OOOO ).json ()#line:513
                                            if 'status'in OOO0O00O0OOOOOOOO :#line:514
                                                if OOO0O00O0OOOOOOOO ['status']==200 :#line:515
                                                    O0O00O0O000O0OOO0 =OOO0O00O0OOOOOOOO ['data']['ill_clover_award']#line:516
                                                    print (f'【图鉴奖励】:领取{OO0O000000O0O0OOO["crop_name"]}成就丨奖励{O0O00O0O000O0OOO0}☘️')#line:518
                                                if OOO0O00O0OOOOOOOO ['status']==500 :#line:519
                                                    print (f'【图鉴奖励】:{OOO0O00O0OOOOOOOO["message"]}')#line:520
        except Exception as OOOOOO00O0O00OO0O :#line:521
            print (OOOOOO00O0O00OO0O )#line:522
    def watched_ad (O00O0O0O0OO00OOO0 ):#line:525
        try :#line:526
            O0O00O0O00OOOO0OO =f'__{timi_new()}'#line:527
            O000000000OOOO0O0 ={'source':'scsc','authorization':O00O0O0O0OO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O00OOOO0OO ),'signstring':O0O00O0O00OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            O0000OO000O0O0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000000000OOOO0O0 ).json ()#line:539
            if 'status'in O0000OO000O0O0O00 :#line:541
                if O0000OO000O0O0O00 ['status']==200 :#line:542
                    if 'offlineInfo'in O0000OO000O0O0O00 ['data']:#line:543
                        time .sleep (random .randint (1 ,3 ))#line:544
                        OO0O00OO0O0O00OO0 =O0000OO000O0O0O00 ['data']['offlineInfo']['off_minute']#line:545
                        O0OO0O0O000OOOO00 =float (O0000OO000O0O0O00 ['data']['silver'])/1000000000000 #line:546
                        time .sleep (1 )#line:547
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000000000OOOO0O0 ).json ()#line:548
                        time .sleep (2 )#line:549
                        OOO0OO0OOO00OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O000000000OOOO0O0 ).json ()#line:550
                        if 'status'in OOO0OO0OOO00OOO0O :#line:552
                            if OOO0OO0OOO00OOO0O ['status']==200 :#line:553
                                OO0OOO0O00OO00000 =float (OOO0OO0OOO00OOO0O ['data']['silver'])/1000000000000 #line:554
                                OOO0OOO0O0O000O00 =str (OO0OOO0O00OO00000 -O0OO0O0O000OOOO00 )[:6 ]#line:555
                                print (f'【离线奖励】:翻倍离线{OO0O00OO0O0O00OO0}分钟奖励🌱数量:{OOO0OOO0O0O000O00}t粒')#line:556
        except Exception as OOOOOO0OO00O0OO0O :#line:557
            print (OOOOOO0OO00O0OO0O )#line:558
    def user_ad (O0O00O0OOO00OO0O0 ):#line:561
        try :#line:562
            O0OO0000O0000OO0O =f'__{timi_new()}'#line:563
            O00O00OOOOOOOOOOO ={'source':'scsc','authorization':O0O00O0OOO00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O0000OO0O ),'signstring':O0OO0000O0000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:574
            O000OO0O0O00O0O0O =requests .request ('get',f'{host}/user/ad',headers =O00O00OOOOOOOOOOO ).json ()#line:575
            if 'status'in O000OO0O0O00O0O0O :#line:577
                if O000OO0O0O00O0O0O ['status']==200 :#line:578
                    OOO0OO0OO0O0OO00O =O000OO0O0O00O0O0O ['data']['max_time']#line:579
                    O0OO0OOOO000OO0O0 =O000OO0O0O00O0O0O ['data']['watch_time']#line:580
                    O00OOO0OOOO0OOOO0 =O000OO0O0O00O0O0O ['data']['added_time']#line:581
                    print (f'【获取种子】:获取🌱剩余{O00OOO0OOOO0OOOO0 + OOO0OO0OO0O0OO00O - O0OO0OOOO000OO0O0}次丨好友提供:{O00OOO0OOOO0OOOO0}次')#line:582
                    if O00OOO0OOOO0OOOO0 +OOO0OO0OO0O0OO00O -O0OO0OOOO000OO0O0 >0 :#line:583
                        time .sleep (random .randint (16 ,19 ))#line:584
                        O0O00O00O0OO000O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00O00OOOOOOOOOOO ).json ()#line:585
                        if 'status'in O0O00O00O0OO000O0 :#line:587
                            if O0O00O00O0OO000O0 ['status']==200 :#line:588
                                O0O00OO0OOOO0O0OO =float (O0O00O00O0OO000O0 ['data']['silver'])/1000000000000 #line:589
                                print (f'【获取种子】:获得🌱:{int(O0O00OO0OOOO0O0OO)}t粒')#line:590
                                return True #line:591
                            if O0O00O00O0OO000O0 ['status']==500 :#line:592
                                OOO000OO0O0000O00 =O0O00O00O0OO000O0 ['message']#line:593
                                print (f'【获取种子】:{OOO000OO0O0000O00}')#line:594
                                return False #line:595
        except Exception as OOO0O0OOOOOOOO000 :#line:596
            print (OOO0O0OOOOOOOO000 )#line:597
    def synthetic (O00000OO0O0O0O0O0 ):#line:600
        global id ,g #line:601
        try :#line:602
            O0OOOO000OO00OO00 =O00000OO0O0O0O0O0 .level_new ()#line:603
            O0OOO000OO0OOO000 =random .randint (9 ,11 )#line:604
            O00O000OO000OO0O0 =f'_site=8&targetSite={O0OOO000OO0OOO000}_{timi_new()}'#line:605
            OO000OO0O0O0OOOO0 ={'source':'scsc','authorization':O00000OO0O0O0O0O0 .token ,'timestamp':timi_new (),'sign':sign (O00O000OO000OO0O0 ),'signstring':O00O000OO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:616
            OO0000O000OO00OO0 ={"site":int (8 ),"targetSite":int (O0OOO000OO0OOO000 )}#line:617
            requests .request ('post',f'{host}/game/crops/move',headers =OO000OO0O0O0OOOO0 ,json =OO0000O000OO00OO0 )#line:618
            while True :#line:619
                O000O0OO0000OOOOO =f'__{timi_new()}'#line:620
                O0OOOO00O0OO0OO0O ={'source':'scsc','authorization':O00000OO0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0000OOOOO ),'signstring':O000O0OO0000OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:631
                OO000OOOOO0O0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00O0OO0OO0O ).json ()#line:632
                if 'status'in OO000OOOOO0O0OOOO :#line:634
                    if OO000OOOOO0O0OOOO ['status']==200 :#line:635
                        OO0O00O0OO000O00O =OO000OOOOO0O0OOOO ['data']['cropList']#line:636
                        O0OO000000000OO00 =OO000OOOOO0O0OOOO ['data']['gameCoreDataDBid']#line:637
                        O00OO0OOO0000OOO0 =float (OO000OOOOO0O0OOOO ['data']['silver'])/1000000000000 #line:638
                        OO0O0O0O0OO00O0OO =0 #line:643
                        for OOO0OO000OOO00OO0 in OO0O00O0OO000O00O :#line:644
                            if not OOO0OO000OOO00OO0 :#line:645
                                OOO00O00OOO0O00OO =f'_crop_id={O0OO000000000OO00}&site={OO0O0O0O0OO00O0OO}_{O00000OO0O0O0O0O0.time}'#line:646
                                O0000000000O0OO00 ={'source':'scsc','authorization':O00000OO0O0O0O0O0 .token ,'timestamp':O00000OO0O0O0O0O0 .time ,'sign':sign (OOO00O00OOO0O00OO ),'signstring':OOO00O00OOO0O00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
                                O0000OO00O00OOOO0 ={"site":OO0O0O0O0OO00O0OO ,"crop_id":O0OO000000000OO00 }#line:657
                                O00OO0O0OO0O0000O =requests .request ('post',f'{host}/game/crops/buy',headers =O0000000000O0OO00 ,data =O0000OO00O00OOOO0 ).json ()#line:658
                                time .sleep (random .randint (1 ,3 )/10 )#line:660
                                if 'status'in O00OO0O0OO0O0000O :#line:661
                                    if O00OO0O0OO0O0000O ['status']==200 :#line:662
                                        if O00OO0O0OO0O0000O ['message']=='种子数量不足':#line:663
                                            O0OOOO000OO00OO00 =O00000OO0O0O0O0O0 .level_new ()#line:664
                                            print (f'【种植合成】:{O00OO0O0OO0O0000O["message"]}')#line:665
                                            if not O00000OO0O0O0O0O0 .user_ad ():#line:666
                                                return False #line:667
                                    if O00OO0O0OO0O0000O ['status']==500 :#line:668
                                        print (f'【种植合成】:{O00OO0O0OO0O0000O["message"]}')#line:669
                                        return False #line:670
                            OO0O0O0O0OO00O0OO +=1 #line:671
                        OOOOOOO0OO0O000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OOOO00O0OO0OO0O ).json ()#line:672
                        OOOO0O0OO0000O0O0 =OOOOOOO0OO0O000O0 ['data']['cropList']#line:673
                        OO000OOO000000000 =False #line:674
                        for OOO0OO000OOO00OO0 in range (12 ):#line:675
                            id =OOOO0O0OO0000O0O0 [OOO0OO000OOO00OO0 ]['level']#line:676
                            if float (O0OOOO000OO00OO00 )-float (id )>9 :#line:677
                                OO0OOO0OOO00OO0OO =f'_site={OOO0OO000OOO00OO0}_{timi_new()}'#line:678
                                O0O0O0O000OO0OOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00000OO0O0O0O0O0 .token ,'timestamp':timi_new (),'sign':sign (OO0OOO0OOO00OO0OO ),'signstring':OO0OOO0OOO00OO0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:689
                                OOO0OO0OO0O0OOOO0 ={"site":OOO0OO000OOO00OO0 }#line:690
                                OO00OOOOOO00O000O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0O0O000OO0OOOO ,data =OOO0OO0OO0O0OOOO0 ).json ()#line:692
                                if 'status'in OO00OOOOOO00O000O :#line:693
                                    if OO00OOOOOO00O000O ['status']==200 :#line:694
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:695
                            if id !=0 :#line:696
                                for O0OO000OOO0O0000O in range (11 ):#line:697
                                    OO00000O0O0O00OO0 =O0OO000OOO0O0000O +1 #line:698
                                    g =OOOO0O0OO0000O0O0 [OO00000O0O0O00OO0 ]['level']#line:699
                                    if id ==g :#line:700
                                        O00000OO00O000O0O =O0OO000OOO0O0000O +2 #line:701
                                        if O00000OO00O000O0O !=OOO0OO000OOO00OO0 +1 :#line:702
                                            O00OO00O0OO00O0OO =OOO0OO000OOO00OO0 +1 #line:703
                                            time .sleep (random .randint (1 ,3 )/10 )#line:705
                                            O00O000OO000OO0O0 =f'_site={O00OO00O0OO00O0OO - 1}&targetSite={O00000OO00O000O0O - 1}_{timi_new()}'#line:706
                                            OO000OO0O0O0OOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00000OO0O0O0O0O0 .token ,'timestamp':timi_new (),'sign':sign (O00O000OO000OO0O0 ),'signstring':O00O000OO000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:723
                                            O00O000OO0O000000 ={"site":int (O00OO00O0OO00O0OO -1 ),"targetSite":int (O00000OO00O000O0O -1 )}#line:724
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO000OO0O0O0OOOO0 ,json =O00O000OO0O000000 )#line:725
                                            OO000OOO000000000 =True #line:727
                                    if OO000OOO000000000 :#line:728
                                        break #line:729
                                if OO000OOO000000000 :#line:730
                                    break #line:731
        except :#line:732
            O00000OO0O0O0O0O0 .synthetic ()#line:733
    def level_new (OO00O0000O00O0OO0 ):#line:736
        try :#line:737
            OO000O0OOO00OOOO0 =f'__{timi_new()}'#line:738
            O00O00000O0OO0OOO ={'source':'scsc','authorization':OO00O0000O00O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OOO00OOOO0 ),'signstring':OO000O0OOO00OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:749
            OO0OO0O0O00OOOOOO =requests .request ('get',f'{host}/user',headers =O00O00000O0OO0OOO ).json ()#line:750
            if 'status'in OO0OO0O0O00OOOOOO :#line:751
                if OO0OO0O0O00OOOOOO ['status']==200 :#line:752
                    return float (OO0OO0O0O00OOOOOO ['data']['level'])#line:753
        except Exception as OOOOOOO00O0OOOOO0 :#line:754
            print (OOOOOOO00O0OOOOO0 )#line:755
    def propsraffle (O0000OO0O0O0000OO ):#line:758
        try :#line:759
            while True :#line:760
                OOO00000000O00O0O =f'__{timi_new()}'#line:761
                O0O00O0OOO00O0000 ={'source':'scsc','authorization':O0000OO0O0O0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00000000O00O0O ),'signstring':OOO00000000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:772
                O0OOOO00O0000O000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00O0OOO00O0000 ).json ()#line:773
                if 'status'in O0OOOO00O0000O000 :#line:775
                    if O0OOOO00O0000O000 ['status']==200 :#line:776
                        OO0O00OOO000OO0OO =O0OOOO00O0000O000 ['data']['rows']#line:777
                        O0OOOOO0O0000OO0O =O0OOOO00O0000O000 ['data']['vstate']#line:778
                        if OO0O00OOO000OO0OO ==5 or OO0O00OOO000OO0OO ==6 or OO0O00OOO000OO0OO ==7 :#line:779
                            O00000OOO0O00OOOO =O0OOOO00O0000O000 ['data']['silver']#line:780
                            print (f'【转盘抽奖】:获得种子:{O00000OOO0O00OOOO}')#line:781
                        if OO0O00OOO000OO0OO ==1 or OO0O00OOO000OO0OO ==2 or OO0O00OOO000OO0OO ==3 :#line:782
                            O000OO0O00O00O000 =O0OOOO00O0000O000 ['data']['clover']#line:783
                            print (f'【转盘抽奖】:获得三叶草:{O000OO0O00O00O000}')#line:784
                        if OO0O00OOO000OO0OO ==4 or OO0O00OOO000OO0OO ==8 :#line:785
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:786
                        if OO0O00OOO000OO0OO =='抽奖次数已用完':#line:790
                            break #line:824
                time .sleep (random .randint (8 ,15 )/10 )#line:825
        except Exception as OOO0OO00O0O00000O :#line:826
            print (OOO0OO00O0O00000O )#line:827
    def friends_invitation (O000000OOO00OOO00 ):#line:830
        try :#line:831
            O0000O00OOOOO0O0O =f'__{timi_new()}'#line:832
            O0000000OOOO0O000 ={'source':'scsc','authorization':O000000OOO00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00OOOOO0O0O ),'signstring':O0000O00OOOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
            O00OO0OO0OOO000O0 =requests .request ('get',f'{host}/friends',headers =O0000000OOOO0O000 ).json ()#line:844
            if 'status'in O00OO0OO0OOO000O0 :#line:845
                if O00OO0OO0OOO000O0 ['status']==200 :#line:846
                    OOOOOO0O00OO00OOO =O00OO0OO0OOO000O0 ['data']['myInviteter']#line:847
                    if OOOOOO0O00OO00OOO :#line:848
                        OO0O00OO0000OO00O =OOOOOO0O00OO00OOO ['user']['nickname']#line:849
                        O00OOO00O00OO00O0 =O000000OOO00OOO00 .certification ()#line:850
                        print (f'【查邀请人】:我的邀请人:{OO0O00OO0000OO00O}丨实名:{O00OOO00O00OO00O0}')#line:851
                    else :#line:852
                        if O000000OOO00OOO00 .innerId !='0':#line:853
                            O000000OOO00OOO00 .invitation ()#line:854
        except Exception as O00OOOO000O0O0000 :#line:855
            print (O00OOOO000O0O0000 )#line:856
    def add_clover (O00OOOO0000O0O0O0 ):#line:859
        global golden_seed #line:860
        try :#line:861
            OOO0O0OO0O0OOO000 =f'__{timi_new()}'#line:862
            OOOOO0OO0O0O00O00 ={'source':'scsc','authorization':O00OOOO0000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0O0OOO000 ),'signstring':OOO0O0OO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:873
            O0O0000O000O0O0OO =requests .request ('get',f'{host}/assets/clovers',headers =OOOOO0OO0O0O00O00 ).json ()#line:874
            if 'status'in O0O0000O000O0O0OO :#line:876
                if O0O0000O000O0O0OO ['status']==200 :#line:877
                    O0OO0OO00000OOOOO =O0O0000O000O0O0OO ['data']['clover']#line:878
                    O0OOO00000OOO00OO =O0O0000O000O0O0OO ['data']['used_clover']#line:879
                    O0OOO0O0OO0OOO0OO =float (O0OO0OO00000OOOOO )-float (O0OOO00000OOO00OO )#line:880
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOO00000OOO00OO}')#line:881
                    if O00OOOO0000O0O0O0 .certification ()!='未实名':#line:882
                        if O0OOO0O0OO0OOO0OO >1 :#line:883
                            OOO0O0OO0O0OOO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO0O0OO0OOO0OO)}_{timi_new()}'#line:884
                            OO0OOO0O000O00OO0 ={'source':'scsc','authorization':O00OOOO0000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0O0OOO000 ),'signstring':OOO0O0OO0O0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:895
                            O0OOOO0OOO000O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO0O0OO0OOO0OO )}#line:896
                            OOOO00O0OO00O0OOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0OOO0O000O00OO0 ,data =O0OOOO0OOO000O0O0 ).json ()#line:897
                            if 'status'in OOOO00O0OO00O0OOO :#line:899
                                if OOOO00O0OO00O0OOO ['status']==200 :#line:900
                                    print (f'【参与抽奖】:添加☘️:{OOOO00O0OO00O0OOO["data"]}丨数量:{O0OOO0O0OO0OOO0OO}')#line:901
                                if OOOO00O0OO00O0OOO ['status']==500 :#line:902
                                    print (f'【参与抽奖】:添加☘️:{OOOO00O0OO00O0OOO["message"]}')#line:903
            OO0000000OO00000O =requests .request ('get',f'{host}/lottery',headers =OOOOO0OO0O0O00O00 ).json ()#line:904
            O000OO00OO00OOOO0 =O00OOOO0000O0O0O0 .winning_rewards ()#line:906
            if 'status'in OO0000000OO00000O :#line:907
                if OO0000000OO00000O ['status']==200 :#line:908
                    O0O0000OOOOOO0000 =OO0000000OO00000O ['data'][0 ]['day_get_gold_quantity']#line:909
                    golden_seed +=float (O0O0000OOOOOO0000 )#line:910
                    O0O0O00000OO0OOOO =OO0000000OO00000O ['data'][1 ]['value']#line:911
                    OOO0O0O00O0000OOO =OO0000000OO00000O ['data'][0 ]['join_number']#line:912
                    O0O000OOOO0OO00OO =int (float (OO0000000OO00000O ['data'][0 ]['totalValue']))#line:913
                    OOOO00O000OO0OO00 =float (O0O0O00000OO0OOOO /O0O000OOOO0OO00OO )*10000 #line:914
                    O0OOO0O0OOO000O0O =O0O000OOOO0OO00OO /OOO0O0O00O0000OOO #line:915
                    print (f'【参与抽奖】:预计每天中{str(O0O0000OOOOOO0000)[:6]}颗金种子丨好友收益:{str(O000OO00OO00OOOO0)[:6]}')#line:916
                    print (f'【抽奖统计】:每1万☘️中{str(OOOO00O000OO0OO00)[:6]}颗金种子丨☘️人均:{str(O0OOO0O0OOO000O0O)[:7]}️')#line:917
        except Exception as O000OOO00O00OOO0O :#line:918
            print (O000OOO00O00OOO0O )#line:919
    def energy (OO00O00O0OOOO0OOO ):#line:923
        try :#line:924
            while True :#line:925
                OO0OO0OO0OO00OO0O =f'__{timi_new()}'#line:926
                OO0OOOO0OOO0OOO00 ={'source':'scsc','authorization':OO00O00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0OO00OO0O ),'signstring':OO0OO0OO0OO00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:937
                O000OOOO000O0O0OO =requests .request ('get',f'{host}/energy/general',headers =OO0OOOO0OOO0OOO00 ).json ()#line:938
                if 'status'in O000OOOO000O0O0OO :#line:940
                    if O000OOOO000O0O0OO ['status']==200 :#line:941
                        O0OO0OOOOO0OOOO0O =O000OOOO000O0O0OO ['data']['ordinary_water']#line:942
                        O00O0OOO00OO000OO =O000OOOO000O0O0OO ['data']['ordinary_fertilizer']#line:943
                        O0O00000OOO0000O0 =O000OOOO000O0O0OO ['data']['videoStatus']#line:944
                        O0O0OO0O00OOOOOOO =O000OOOO000O0O0OO ['data']['waterVideoKey']#line:945
                        print (f'【我的营养】:肥料:{str(O00O0OOO00OO000OO).split(".")[0]}丨水滴:{str(O0OO0OOOOO0OOOO0O).split(".")[0]}')#line:946
                        if float (O00O0OOO00OO000OO )<96 :#line:947
                            if O0O00000OOO0000O0 :#line:948
                                time .sleep (random .randint (160 ,180 )/10 )#line:949
                                O0O0OO000000OOOO0 =99 -float (O00O0OOO00OO000OO )#line:950
                                OO00000000OOO0O00 ={"fertilizer":str (O0O0OO000000OOOO0 ).split ('.')[0 ]}#line:951
                                OO0OOOO00O0O0O0OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOOO0OOO0OOO00 ).json ()#line:952
                                if 'status'in OO0OOOO00O0O0O0OO :#line:954
                                    if OO0OOOO00O0O0O0OO ['status']==200 :#line:955
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOO00O0O0O0OO["message"]}')#line:956
                                    if OO0OOOO00O0O0O0OO ['status']==500 :#line:957
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOO00O0O0O0OO["message"]}')#line:958
                                        break #line:959
                                if float (O00O0OOO00OO000OO )<78 :#line:961
                                    O0O0OO000000OOOO0 =80 -float (O00O0OOO00OO000OO )#line:962
                                    O0000O000OOO00OO0 =f'_fertilizer={int(O0O0OO000000OOOO0)}_{timi_new()}'#line:963
                                    O000OO0OO0O0OO00O ={'source':'scsc','authorization':OO00O00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O000OOO00OO0 ),'signstring':O0000O000OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:974
                                    OO0O0OOO0O000OO00 ={"fertilizer":int (O0O0OO000000OOOO0 )}#line:975
                                    OOO000O0OO0000OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000OO0OO0O0OO00O ,data =OO0O0OOO0O000OO00 ).json ()#line:977
                                    if 'status'in OOO000O0OO0000OOO :#line:979
                                        if OOO000O0OO0000OOO ['status']==200 :#line:980
                                            print (f'【购买肥料】:购买肥料:{OOO000O0OO0000OOO["message"]}丨数量:{int(O0O0OO000000OOOO0)}')#line:981
                                        if OOO000O0OO0000OOO ['status']==500 :#line:982
                                            print (f'【购买肥料】:购买肥料:{OOO000O0OO0000OOO["message"]}丨数量:{int(O0O0OO000000OOOO0)}')#line:983
                                            O0OOOO0O000O00OO0 =OOO000O0OO0000OOO ["message"].split ('-')[1 ]#line:984
                                            OO000000OO0O00OOO =f'__{timi_new()}'#line:985
                                            O0O00O00O0O0OO0O0 ={'source':'scsc','authorization':OO00O00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OO0O00OOO ),'signstring':OO000000OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                            O00OO000O00O000O0 =requests .request ('get',f'{host}/user',headers =O0O00O00O0O0OO0O0 ).json ()#line:997
                                            if 'status'in O00OO000O00O000O0 :#line:998
                                                if O00OO000O00O000O0 ['status']==200 :#line:999
                                                    OO000O00OO00OO00O =O00OO000O00O000O0 ['data']['inner_id']#line:1000
                                                    if give_gold (OO000O00OO00OO00O ,float (O0OOOO0O000O00OO0 )+1 ):#line:1001
                                                        OO00O00O0OOOO0OOO .energy ()#line:1002
                        if float (O0OO0OOOOO0OOOO0O )<880 :#line:1003
                            if O0O0OO0O00OOOOOOO :#line:1004
                                time .sleep (random .randint (160 ,180 )/10 )#line:1005
                                OO0000OO0O000O000 =999 -float (O0OO0OOOOO0OOOO0O )#line:1006
                                OOOO0OOO0OOOOO000 ={"water":str (OO0000OO0O000O000 ).split ('.')[0 ]}#line:1007
                                O000000O00OOO00O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOOO0OOO0OOO00 ).json ()#line:1008
                                if 'status'in O000000O00OOO00O0 :#line:1010
                                    if O000000O00OOO00O0 ['status']==200 :#line:1011
                                        print (f'【购买水滴】:看广告获取水滴:{O000000O00OOO00O0["message"]}')#line:1012
                                    if O000000O00OOO00O0 ['status']==500 :#line:1013
                                        print (f'【购买水滴】:看广告获取水滴:{O000000O00OOO00O0["message"]}')#line:1014
                                        break #line:1015
                                if float (O0OO0OOOOO0OOOO0O )<780 :#line:1016
                                    OO0000OO0O000O000 =800 -float (O0OO0OOOOO0OOOO0O )#line:1017
                                    OOO0OO00000000O00 =f'_water={int(OO0000OO0O000O000)}_{timi_new()}'#line:1018
                                    O00OOOOO0O0OOO0OO ={'source':'scsc','authorization':OO00O00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00000000O00 ),'signstring':OOO0OO00000000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1029
                                    O00O0O0OO00000O0O ={"water":int (OO0000OO0O000O000 )}#line:1030
                                    OO00OO000OOO00OO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O00OOOOO0O0OOO0OO ,data =O00O0O0OO00000O0O ).json ()#line:1032
                                    if 'status'in OO00OO000OOO00OO0 :#line:1034
                                        if OO00OO000OOO00OO0 ['status']==200 :#line:1035
                                            print (f'【购买水滴】:购买水滴:{OO00OO000OOO00OO0["message"]}丨数量:{int(OO0000OO0O000O000)}')#line:1036
                                        if OO00OO000OOO00OO0 ['status']==500 :#line:1037
                                            print (f'【购买水滴】:购买水滴:{OO00OO000OOO00OO0["message"]}丨数量:{int(OO0000OO0O000O000)}')#line:1038
                                            O0OOOO0O000O00OO0 =OO00OO000OOO00OO0 ["message"].split ('-')[1 ]#line:1039
                                            OO000000OO0O00OOO =f'__{timi_new()}'#line:1040
                                            O0O00O00O0O0OO0O0 ={'source':'scsc','authorization':OO00O00O0OOOO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000OO0O00OOO ),'signstring':OO000000OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1051
                                            O00OO000O00O000O0 =requests .request ('get',f'{host}/user',headers =O0O00O00O0O0OO0O0 ).json ()#line:1052
                                            if 'status'in O00OO000O00O000O0 :#line:1053
                                                if O00OO000O00O000O0 ['status']==200 :#line:1054
                                                    OO000O00OO00OO00O =O00OO000O00O000O0 ['data']['inner_id']#line:1055
                                                    if give_gold (OO000O00OO00OO00O ,float (O0OOOO0O000O00OO0 )+1 ):#line:1056
                                                        OO00O00O0OOOO0OOO .energy ()#line:1057
                        break #line:1058
        except Exception as OO0O0O0O00000O000 :#line:1059
            print (OO0O0O0O00000O000 )#line:1060
def bundled_def ():#line:1062
    O0000O0O0O000O0OO =['5570536','7750212','7911652','7911680','7805624']#line:1063
    return O0000O0O0O000O0OO [random .randint (0 ,len (O0000O0O0O000O0OO )-1 )]#line:1064
def version_of_the_validation ():#line:1068
    return str ((91 -56 )/10 )#line:1069
def sc2 ():#line:1071
    return "19319#$%^&*((*"#line:1072
def OO00OO0OO0OO00OO00o0 ():#line:1074
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1075
def get_ip ():#line:1077
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1078
def gitee_validation ():#line:1080
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1081
def gitee_edition ():#line:1083
    try :#line:1084
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1085
    except :#line:1086
        sys .exit (0 )#line:1087
def O000OO000O0O00OOO00 ():#line:1092
    try :#line:1093
        OO00OO00OO0O0OO0O =gitee_edition ()#line:1094
        if version_of_the_validation ()<OO00OO00OO0O0OO0O ['CityEarth']['edition']:#line:1095
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OO00OO0O0OO0O["CityEarth"]["edition"]}   ❌')#line:1096
            print (f'更新内容=>>{OO00OO00OO0O0OO0O["CityEarth"]["content"]}   🎉')#line:1097
        else :#line:1098
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00OO00OO0O0OO0O["CityEarth"]["edition"]}   ✅')#line:1099
            print (f'更新内容=>> {OO00OO00OO0O0OO0O["CityEarth"]["content"]}   🎉')#line:1100
    except Exception as O0OO0OO0OOOO0O0O0 :#line:1101
        print (O0OO0OO0OOOO0O0O0 )#line:1102
def sc3 ():#line:1104
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1105
if __name__ =='__main__':#line:1109
    start ()#line:1110
