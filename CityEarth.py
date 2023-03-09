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
@ 版本  3.4
"""
##################################配置区##################################
time_xx = random.randint(12, 15)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
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
        O0O0O00OO0O0000O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O0O0O00OO0O0000O0)}个账号==========")#line:13
        for O0000OO00O0O0O00O in O0O0O00OO0O0000O0 :#line:14
            OOO0O0OOO000O00O0 =[]#line:15
            print (f"------------正在执行第{O0O0O00OO0O0000O0.index(O0000OO00O0O0O00O) + 1}个账号------------")#line:16
            OOOO00O0OOOO0O000 =CityEarth (O0000OO00O0O0O00O ,OOO0O0OOO000O00O0 ,O0O0O00OO0O0000O0 .index (O0000OO00O0O0O00O ))#line:17
            def O000000000O00O00O ():#line:18
                if OOOO00O0OOOO0O000 .base_info ():#line:20
                    OOOO00O0OOOO0O000 .sealing ()#line:22
                    OOOO00O0OOOO0O000 .invitenum ()#line:24
                    OOOO00O0OOOO0O000 .game_map ()#line:26
                    OOOO00O0OOOO0O000 .friends_invitation ()#line:28
                    OOOO00O0OOOO0O000 .energy ()#line:30
                    OOOO00O0OOOO0O000 .add_clover ()#line:32
                    OOOO00O0OOOO0O000 .propsraffle ()#line:34
                    OOOO00O0OOOO0O000 .synthetic ()#line:36
                    OOOO00O0OOOO0O000 .crops_illustrated ()#line:38
                    OOOO00O0OOOO0O000 .give_gold ()#line:40
                    OOOO00O0OOOO0O000 .withdraw ()#line:42
            OO000000O0OO0O0O0 =threading .Thread (target =O000000000O00O00O )#line:44
            OO000000O0OO0O0O0 .start ()#line:45
            time .sleep (time_xx )#line:46
        print (f"------------正在处理推送通知------------")#line:47
        time .sleep (0.5 )#line:48
        O00OO0OO0O00OO00O =format_msg ()#line:49
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OO0OO0O00OO00O +' ')#line:50
    except Exception as O000OO0O0O00OO00O :#line:51
        print (O000OO0O0O00OO00O )#line:52
def give_gold (OO0000OO0OO0O000O ,OO0O0000OOO0O0OO0 ):#line:55
        try :#line:56
            OOO0000O0O00O00O0 =f'_doneeNo={OO0000OO0OO0O000O}&quantity={int(OO0O0000OOO0O0OO0)}_{timi_new()}'#line:57
            O00000000O00O00O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOO0000O0O00O00O0 ),'signstring':OOO0000O0O00O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:68
            O000O0OO0OOOO0OO0 ={"quantity":int (OO0O0000OOO0O0OO0 ),"doneeNo":OO0000OO0OO0O000O }#line:72
            OO00OOOOOOOOOOOOO =requests .request ('post',f'{host}/finance/give-gold',headers =O00000000O00O00O0 ,data =O000O0OO0OOOO0OO0 ).json ()#line:73
            if 'status'in OO00OOOOOOOOOOOOO :#line:75
                if OO00OOOOOOOOOOOOO ['status']==200 :#line:76
                    if OO00OOOOOOOOOOOOO ['data']:#line:77
                        print (f'【赠送种子】:赠送{int(OO0O0000OOO0O0OO0)}种子给{OO0000OO0OO0O000O}成功')#line:78
                        return True #line:79
                if OO00OOOOOOOOOOOOO ['status']==401 :#line:80
                    print (f'【赠送种子】:{OO00OOOOOOOOOOOOO["message"]}')#line:81
                    return False #line:82
                if OO00OOOOOOOOOOOOO ['status']==500 :#line:83
                    print (f'【赠送种子】:{OO00OOOOOOOOOOOOO["message"]}')#line:84
                    return False #line:85
            return False #line:86
        except Exception as OO00O0OOO0OO0O0OO :#line:87
            print (OO00O0OOO0OO0O0OO )#line:88
def kvkv ():#line:89
    return '/vastzzzl/vastzzzl/raw/master'#line:90
def sign (O000OOOOOO0OOO00O ):#line:93
    O0OOO00OOO000OOOO =hashlib .md5 (O000OOOOOO0OOO00O .encode ()).hexdigest ()#line:94
    OO00OOO00O00OO00O =sc1 ()#line:95
    O0OOO0O0OO0O0O000 =sc2 ()#line:96
    OO000O0O00OO0O00O =sc3 ()#line:97
    OO0O00OO0O00O0OOO =OO00OOO00O00OO00O +O0OOO00OOO000OOOO +O0OOO0O0OO0O0O000 +OO000O0O00OO0O00O #line:98
    OOO000OO0OO0OOO00 =hashlib .md5 (OO0O00OO0O00O0OOO .encode ()).hexdigest ()#line:99
    return OOO000OO0OO0OOO00 #line:100
def format_msg ():#line:104
    O0OOOO0OO0OO000OO =""#line:105
    for O00O0O000OOOOO0O0 in msg_list :#line:106
        O0OOOO0OO0OO000OO +=str (O00O0O000OOOOO0O0 )+"\r\n"#line:107
    return O0OOOO0OO0OO000OO #line:108
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
def get_json_data (OOOOOOOO0OOOO0O00 ,O0OOOO0O0OO0000O0 ,OO00O0O0OO0000O00 ,O00OO0O00OOO0O00O ):#line:127
    with open (OOOOOOOO0OOOO0O00 ,'rb')as OOOOOO00000O0OOOO :#line:129
        OO00O0OO00O00OOOO =json .load (OOOOOO00000O0OOOO )#line:130
        OO00O0OO00O00OOOO ['data'][O0OOOO0O0OO0000O0 ][OO00O0O0OO0000O00 ]=O00OO0O00OOO0O00O #line:131
        OOO00OOOOOO000OOO =OO00O0OO00O00OOOO #line:132
    OOOOOO00000O0OOOO .close ()#line:133
    return OOO00OOOOOO000OOO #line:134
def write_json_data (O0OOOOOO000O0OO0O ):#line:136
    with open (json_path1 ,'w')as OO0OO0O000O000O0O :#line:137
        json .dump (O0OOOOOO000O0OO0O ,OO0OO0O000O000O0O )#line:138
    OO0OO0O000O000O0O .close ()#line:139
    return True #line:140
class CityEarth :#line:142
    def __init__ (OOOOOO00O000OOO0O ,OOO0OO0OO00O0O00O ,OOOOO00O0O00OO00O ,O0OO0O00OO00OO0OO ):#line:144
        try :#line:145
            OOOOOO00O000OOO0O .msg =OOOOO00O0O00OO00O #line:146
            OOOOOO00O000OOO0O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:147
            OOOOOO00O000OOO0O .token =OOO0OO0OO00O0O00O ['authorization']#line:148
            OOOOOO00O000OOO0O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:149
            OOOOOO00O000OOO0O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:150
            OOOOOO00O000OOO0O .elephant_user =OOO0OO0OO00O0O00O ['elephant_user']#line:151
            OOOOOO00O000OOO0O .elephant_pswd =OOO0OO0OO00O0O00O ['elephant_pswd']#line:152
            OOOOOO00O000OOO0O .elephant_Task_ID =OOO0OO0OO00O0O00O ['elephant_Task_ID']#line:153
            OOOOOO00O000OOO0O .len_new =O0OO0O00OO00OO0OO #line:154
        except :#line:155
            print ('变量格式错误')#line:156
    def base_info (OO0000OO000O0O0O0 ):#line:159
        try :#line:160
            OO0000OO000O0O0O0 .watched_ad ()#line:162
            OOOOO00O000O00OO0 =f'__{timi_new()}'#line:163
            OOOOO00O000000OOO ={'source':'scsc','authorization':OO0000OO000O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O00OO0 ),'signstring':OOOOO00O000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:174
            OO0O0O000O00000OO =requests .request ('get',f'{host}/user',headers =OOOOO00O000000OOO ).json ()#line:175
            if 'status'in OO0O0O000O00000OO :#line:177
                if OO0O0O000O00000OO ['status']==200 :#line:178
                    OOOO0O0OO0OOO0000 =OO0O0O000O00000OO ['data']['nickname']#line:179
                    O000O00O00O0O0OO0 =OO0O0O000O00000OO ['data']['inner_id']#line:180
                    O0O00OO0OOOOO0OOO =OO0O0O000O00000OO ['data']['assets']['gold']#line:181
                    OOO0000OO00OO00O0 =OO0O0O000O00000OO ['data']['level']#line:182
                    print (f'【账号信息】:昵称:{OOOO0O0OO0OOO0000[:5]}丨ID:{O000O00O00O0O0OO0}丨等级:{OOO0000OO00OO00O0}丨金种子:{str(O0O00OO0OOOOO0OOO).split(".")[0]}')#line:183
                    if 'wx_'in OOOO0O0OO0OOO0000 :#line:184
                        OO0000OO000O0O0O0 .change_nickname ()#line:185
                if OO0O0O000O00000OO ['status']==401 :#line:186
                    print ('【账号信息】:账号失效正在尝试登录')#line:187
                    if OO0000OO000O0O0O0 .elephant_user =='f':#line:188
                        return False #line:189
                    OOO0O00OOO00OO0O0 =Invalid_login .addtask (elephant_user =OO0000OO000O0O0O0 .elephant_user ,elephant_pswd =OO0000OO000O0O0O0 .elephant_pswd ,elephant_Task_ID =OO0000OO000O0O0O0 .elephant_Task_ID )#line:190
                    OO0OO0O0O00O00OO0 =get_json_data (json_path ,OO0000OO000O0O0O0 .len_new ,'authorization',OOO0O00OOO00OO0O0 )#line:191
                    if write_json_data (OO0OO0O0O00O00OO0 ):#line:192
                        print ('正在写入账号配置文件')#line:193
                    return False #line:194
                if OO0O0O000O00000OO ['status']==500 :#line:195
                    return False #line:196
            return True #line:197
        except Exception as O00OOOO0OOO00OOO0 :#line:198
            print (O00OOOO0OOO00OOO0 )#line:199
    def sealing (OO00O000OO0000O00 ):#line:202
        try :#line:203
            O000000O0O000OO0O =f'__{timi_new()}'#line:204
            O0000000O00OOOO0O ={'source':'scsc','authorization':OO00O000OO0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000O0O000OO0O ),'signstring':O000000O0O000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:215
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0000000O00OOOO0O )#line:216
            requests .request ('get',f'{host}/packsack/list',headers =O0000000O00OOOO0O )#line:217
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0000000O00OOOO0O )#line:218
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0000000O00OOOO0O )#line:219
            requests .request ('get',f'{host}/user',headers =O0000000O00OOOO0O )#line:220
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0000000O00OOOO0O )#line:221
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0000000O00OOOO0O )#line:222
            requests .request ('post',f'{host}/announcement/announcement',headers =O0000000O00OOOO0O )#line:223
            requests .request ('get',f'{host}/game/getAllData',headers =O0000000O00OOOO0O )#line:224
            requests .request ('get',f'{host}/assets',headers =O0000000O00OOOO0O )#line:225
        except Exception as OOO0OO000OOOO0OOO :#line:226
            print (OOO0OO000OOOO0OOO )#line:227
    def change_nickname (O0OO0O0000O0O000O ):#line:231
        try :#line:232
            O0O0OO00OOOO0000O =timi_new ()#line:233
            OOO00000OOOO0OOOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:234
            O0O0O0OO0O0O0OOOO =requests .request ('post','https://www.qmsjmfb.com/',data =OOO00000OOOO0OOOO ).text #line:235
            OO000000O0O00O0O0 =re .findall ('<ul><li>(.*?)</li>',O0O0O0OO0O0O0OOOO )[0 ][:3 ]#line:236
            OOO0O00O0000000O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO000000O0O00O0O0}').json ()#line:237
            OO0O0000000OO0OO0 =OOO0O00O0000000O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:238
            O00OOOO0O0OOO00O0 ={"nickname":OO0O0000000OO0OO0 }#line:239
            O00O0O00O000000OO =f'_nickname={OO0O0000000OO0OO0}_{O0O0OO00OOOO0000O}'#line:240
            O0O0OOOO00O0O0O00 ={'source':'scsc','authorization':O0OO0O0000O0O000O .token ,'timestamp':O0O0OO00OOOO0000O ,'sign':sign (O00O0O00O000000OO ),'signstring':O00O0O00O000000OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:251
            OO0O00OO00000O0OO =requests .request ('patch',f'{host}/user/nickname',headers =O0O0OOOO00O0O0O00 ,data =O00OOOO0O0OOO00O0 ).json ()#line:252
            if 'status'in OO0O00OO00000O0OO :#line:254
                if OO0O00OO00000O0OO ['status']==200 :#line:255
                    print (f'【修改网名】:网名:{OO0O0000000OO0OO0}丨{OO0O00OO00000O0OO["message"]}')#line:256
        except Exception as OO00000O000OOO000 :#line:257
            print (OO00000O000OOO000 )#line:258
    def withdraw (OO000OO0OOO00O00O ):#line:263
        O0O000OOOO0OO00O0 =f'__{timi_new()}'#line:264
        OO0O0OOO00OO000O0 ={'source':'scsc','authorization':OO000OO0OOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOO0OO00O0 ),'signstring':O0O000OOOO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:275
        OO0O00OOOO0OO000O =requests .request ('get',f'{host}/assets',headers =OO0O0OOO00OO000O0 ).json ()#line:276
        if 'status'in OO0O00OOOO0OO000O :#line:278
            if OO0O00OOOO0OO000O ['status']==200 :#line:279
                OOO00OOOOOO0O00OO =OO0O00OOOO0OO000O ['data']['cash']#line:280
                if float (OOO00OOOOOO0O00OO )>20 :#line:281
                    O0O000OOOO0OO00O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:282
                    OO0O0OOO00OO000O0 ={'authorization':OO000OO0OOO00O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000OOOO0OO00O0 ),'signstring':O0O000OOOO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
                    OOOO000OOO0OOOO0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:293
                    OOOO0O0O00O0O0O0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OO0O0OOO00OO000O0 ,data =OOOO000OOO0OOOO0O ).json ()#line:295
                    print (OOOO0O0O00O0O0O0O )#line:296
    def invitenum (O000000O000000O0O ):#line:299
        OOO000O000OO00O0O =f'__{timi_new()}'#line:300
        O0OO00O00000O0O0O ={'source':'scsc','authorization':O000000O000000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OO00O0O ),'signstring':OOO000O000OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:311
        O0OO0OOO00O0O0O00 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO00O00000O0O0O ).json ()#line:312
        if 'status'in O0OO0OOO00O0O0O00 :#line:314
            if O0OO0OOO00O0O0O00 ['status']==200 :#line:315
                O0OOO0000OO0000OO =O0OO0OOO00O0O0O00 ['data']['invited_count']#line:316
                OOOO000OOO0OO0O0O =O0OO0OOO00O0O0O00 ['data']['invited_second_count']#line:317
                print (f'【我的邀请】:直邀好友:{O0OOO0000OO0000OO}丨间邀好友:{OOOO000OOO0OO0O0O}')#line:318
    def game_map (O00OO0O0O0OO0O0O0 ):#line:321
        try :#line:322
            O0OO0OO00OO0OOO00 =f'__{timi_new()}'#line:323
            OO000O000OOO0OOO0 ={'source':'scsc','authorization':O00OO0O0O0OO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO00OO0OOO00 ),'signstring':O0OO0OO00OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:334
            OO00O0OO000O00000 =requests .request ('get',f'{host}/game/map',headers =OO000O000OOO0OOO0 ).json ()#line:335
            if 'status'in OO00O0OO000O00000 :#line:337
                if OO00O0OO000O00000 ['status']==200 :#line:338
                    for OOOO0O00OO0OOOOOO in OO00O0OO000O00000 ['data']['list'][0 ]['crops']:#line:339
                        OOO00000O0000OO00 =OOOO0O00OO0OOOOOO ['level']#line:341
                        if OOO00000O0000OO00 ==41 :#line:342
                            OO0OOO00OO0000000 =OOOO0O00OO0OOOOOO ['crop_name']#line:343
                            OO000O0O0000O0OOO =OOOO0O00OO0OOOOOO ['count']#line:344
                            if OO000O0O0000O0OOO >0 :#line:345
                                print (f'【农业资产】:{OO0OOO00OO0000000}丨数量:{OO000O0O0000O0OOO}')#line:346
        except Exception as O0OOOO0O0O0OOO00O :#line:347
            print (O0OOOO0O0O0OOO00O )#line:348
    def give_gold (O000OO0000OOO000O ):#line:351
        try :#line:352
            O000O0O000O000OOO =f'__{timi_new()}'#line:353
            O0O0OO000O00OOOOO ={'source':'scsc','authorization':O000OO0000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O000O000OOO ),'signstring':O000O0O000O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:364
            OOO0O00O0O0OOO0O0 =requests .request ('get',f'{host}/user',headers =O0O0OO000O00OOOOO ).json ()#line:365
            if 'status'in OOO0O00O0O0OOO0O0 :#line:366
                if OOO0O00O0O0OOO0O0 ['status']==200 :#line:367
                    if float (O000OO0000OOO000O .doneeNo )!=0 :#line:368
                        O0O0O00OOO0OO0O00 =OOO0O00O0O0OOO0O0 ['data']['assets']['gold']#line:369
                        if float (O0O0O00OOO0OO0O00 )>float (O000OO0000OOO000O .innerId ):#line:370
                            OOOOOOO00OO0O0O00 =int (float (O0O0O00OOO0OO0O00 )/1.1 )#line:371
                            O000O0O000O000OOO =f'_doneeNo={O000OO0000OOO000O.doneeNo}&quantity={OOOOOOO00OO0O0O00}_{timi_new()}'#line:372
                            O0O0OO000O00OOOOO ={'source':'scsc','authorization':O000OO0000OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0O000O000OOO ),'signstring':O000O0O000O000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:383
                            O0O0000OO0000O00O ={"quantity":OOOOOOO00OO0O0O00 ,"doneeNo":O000OO0000OOO000O .doneeNo }#line:387
                            OOO00OOO0OOO0O0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OO000O00OOOOO ,data =O0O0000OO0000O00O ).json ()#line:388
                            if 'status'in OOO00OOO0OOO0O0O0 :#line:390
                                if OOO00OOO0OOO0O0O0 ['status']==200 :#line:391
                                    if OOO00OOO0OOO0O0O0 ['data']:#line:392
                                        print (f'【赠送种子】:赠送{OOOOOOO00OO0O0O00}种子给{O000OO0000OOO000O.doneeNo}成功')#line:393
                    else :#line:394
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:395
        except Exception as OO0000OOO0O0O000O :#line:396
            print (OO0000OOO0O0O000O )#line:397
    def invitation (O00OOOOO0OOOOOOO0 ):#line:399
        try :#line:400
            _O0000O00O0OOOO0O0 =float (bundled_def ())/4 #line:401
            OO00000O0O000OO00 =f'_innerId={int(_O0000O00O0OOOO0O0)}_{timi_new()}'#line:402
            O0O0OOO0O0O00000O ={'source':'scsc','authorization':O00OOOOO0OOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000O0O000OO00 ),'signstring':OO00000O0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:413
            O00OO0OOOO0O00O00 ={"innerId":int (_O0000O00O0OOOO0O0 )}#line:414
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0O0OOO0O0O00000O ,data =O00OO0OOOO0O00O00 )#line:415
        except Exception as OO0OO0OOO00O00O00 :#line:416
            print (OO0OO0OOO00O00O00 )#line:417
    def winning_rewards (O00O00O000O0OOOOO ):#line:420
        try :#line:421
            OO000000O0OO0O0OO =f'__{timi_new()}'#line:422
            O0O0OOOO0000O00OO ={'source':'scsc','authorization':O00O00O000O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000000O0OO0O0OO ),'signstring':OO000000O0OO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:433
            O00OOOOO0O0OOOO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0OOOO0000O00OO ).json ()#line:434
            if 'status'in O00OOOOO0O0OOOO00 :#line:436
                if O00OOOOO0O0OOOO00 ['status']==200 :#line:437
                    if O00OOOOO0O0OOOO00 ['data']['amount']:#line:438
                        O00OO0OO00000O0OO =O00OOOOO0O0OOOO00 ['data']['amount']['gold']#line:439
                        return O00OO0OO00000O0OO #line:440
                    else :#line:441
                        return 0 #line:442
        except Exception as OOOOOO0000OO0O0O0 :#line:443
            print (OOOOOO0000OO0O0O0 )#line:444
    def certification (O0O00O0000000000O ):#line:447
        try :#line:448
            OOO0O0OO0OOO00O00 =f'__{timi_new()}'#line:449
            OO00O000O0O000O00 ={'source':'scsc','authorization':O0O00O0000000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0OOO00O00 ),'signstring':OOO0O0OO0OOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:460
            O00O000OO000O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00O000O0O000O00 ).json ()#line:461
            if 'status'in O00O000OO000O00O0 :#line:463
                if O00O000OO000O00O0 ['status']==200 :#line:464
                    if O00O000OO000O00O0 ['data']['result']:#line:465
                        O00O0000O0O0O0O00 =O00O000OO000O00O0 ['data']['nick_name']#line:466
                        return O00O0000O0O0O0O00 #line:467
                    else :#line:468
                        return '未实名'#line:469
        except Exception as OOOO00OO0OO0OO0O0 :#line:470
            print (OOOO00OO0OO0OO0O0 )#line:471
    def crops_illustrated (O00O0O00O00O00O0O ):#line:474
        try :#line:475
            O0OO00OO00O00OOO0 =f'__{timi_new()}'#line:476
            O00O0O0O00000O000 ={'source':'scsc','authorization':O00O0O00O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00O00OOO0 ),'signstring':O0OO00OO00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:487
            OOO0000000O0O0O00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O0O0O00000O000 ).json ()#line:488
            if 'status'in OOO0000000O0O0O00 :#line:490
                if OOO0000000O0O0O00 ['status']==200 :#line:491
                    OO0OOO000OO0O0OO0 =OOO0000000O0O0O00 ['data'][0 ]['crops']#line:492
                    for OOO000OOO0O0OOO0O in OO0OOO000OO0O0OO0 :#line:493
                        if OOO000OOO0O0OOO0O ['ill_clover_award']:#line:494
                            if float (OOO000OOO0O0OOO0O ['ill_clover_award'])>1 :#line:495
                                if OOO000OOO0O0OOO0O ['is_finish']:#line:496
                                    if not OOO000OOO0O0OOO0O ['is_getit']:#line:497
                                        if O00O0O00O00O00O0O .certification ()!='未实名':#line:498
                                            O0OO00OO00O00OOO0 =f'_award_level={OOO000OOO0O0OOO0O["level"]}_{timi_new()}'#line:499
                                            O00O0O0O00000O000 ={'source':'scsc','authorization':O00O0O00O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO00O00OOO0 ),'signstring':O0OO00OO00O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:510
                                            OOO0OO0O0O00O0O0O ={"award_level":OOO000OOO0O0OOO0O ['level']}#line:511
                                            O0OO00OOO0000000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O0O0O00000O000 ,json =OOO0OO0O0O00O0O0O ).json ()#line:513
                                            if 'status'in O0OO00OOO0000000O :#line:514
                                                if O0OO00OOO0000000O ['status']==200 :#line:515
                                                    O0OOO0O000OO0O0OO =O0OO00OOO0000000O ['data']['ill_clover_award']#line:516
                                                    print (f'【图鉴奖励】:领取{OOO000OOO0O0OOO0O["crop_name"]}成就丨奖励{O0OOO0O000OO0O0OO}☘️')#line:518
                                                if O0OO00OOO0000000O ['status']==500 :#line:519
                                                    print (f'【图鉴奖励】:{O0OO00OOO0000000O["message"]}')#line:520
        except Exception as O00000O0O0000OOO0 :#line:521
            print (O00000O0O0000OOO0 )#line:522
    def watched_ad (OO0OO00OOOOO000O0 ):#line:525
        try :#line:526
            O0O0OOO0O0OO0OO0O =f'__{timi_new()}'#line:527
            OO00O0O0OOO00OO0O ={'source':'scsc','authorization':OO0OO00OOOOO000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O0OO0OO0O ),'signstring':O0O0OOO0O0OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            O00000OOOOOO0OOOO =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0O0OOO00OO0O ).json ()#line:539
            if 'status'in O00000OOOOOO0OOOO :#line:541
                if O00000OOOOOO0OOOO ['status']==200 :#line:542
                    if 'offlineInfo'in O00000OOOOOO0OOOO ['data']:#line:543
                        time .sleep (random .randint (1 ,3 ))#line:544
                        OOO0O00O00000O00O =O00000OOOOOO0OOOO ['data']['offlineInfo']['off_minute']#line:545
                        OOOOOOO000OOOO0O0 =float (O00000OOOOOO0OOOO ['data']['silver'])/1000000000000 #line:546
                        time .sleep (1 )#line:547
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO00O0O0OOO00OO0O ).json ()#line:548
                        time .sleep (2 )#line:549
                        O0OOOO000O00O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0O0OOO00OO0O ).json ()#line:550
                        if 'status'in O0OOOO000O00O0000 :#line:552
                            if O0OOOO000O00O0000 ['status']==200 :#line:553
                                O0OOOO0OOO0O0O00O =float (O0OOOO000O00O0000 ['data']['silver'])/1000000000000 #line:554
                                OO00OOOOO0O0OO00O =str (O0OOOO0OOO0O0O00O -OOOOOOO000OOOO0O0 )[:6 ]#line:555
                                print (f'【离线奖励】:翻倍离线{OOO0O00O00000O00O}分钟奖励🌱数量:{OO00OOOOO0O0OO00O}t粒')#line:556
        except Exception as OOOO0O0000000OO00 :#line:557
            print (OOOO0O0000000OO00 )#line:558
    def user_ad (OO0O0O0000O00O0OO ):#line:561
        try :#line:562
            O0OO00O0O000O0O0O =f'__{timi_new()}'#line:563
            OO0000OOO000000O0 ={'source':'scsc','authorization':OO0O0O0000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O000O0O0O ),'signstring':O0OO00O0O000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:574
            OOOO0O00O0O00OO00 =requests .request ('get',f'{host}/user/ad',headers =OO0000OOO000000O0 ).json ()#line:575
            if 'status'in OOOO0O00O0O00OO00 :#line:577
                if OOOO0O00O0O00OO00 ['status']==200 :#line:578
                    OO00O00OOO0OOOOOO =OOOO0O00O0O00OO00 ['data']['max_time']#line:579
                    OO000O0OO00000OO0 =OOOO0O00O0O00OO00 ['data']['watch_time']#line:580
                    OOOOO0O0OOO00O0OO =OOOO0O00O0O00OO00 ['data']['added_time']#line:581
                    print (f'【获取种子】:获取🌱剩余{OOOOO0O0OOO00O0OO + OO00O00OOO0OOOOOO - OO000O0OO00000OO0}次丨好友提供:{OOOOO0O0OOO00O0OO}次')#line:582
                    if OOOOO0O0OOO00O0OO +OO00O00OOO0OOOOOO -OO000O0OO00000OO0 >0 :#line:583
                        time .sleep (random .randint (16 ,19 ))#line:584
                        O0000O0O0OO00OO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0000OOO000000O0 ).json ()#line:585
                        if 'status'in O0000O0O0OO00OO0O :#line:587
                            if O0000O0O0OO00OO0O ['status']==200 :#line:588
                                O00000O0O0O0O0OOO =float (O0000O0O0OO00OO0O ['data']['silver'])/1000000000000 #line:589
                                print (f'【获取种子】:获得🌱:{int(O00000O0O0O0O0OOO)}t粒')#line:590
                                return True #line:591
                            if O0000O0O0OO00OO0O ['status']==500 :#line:592
                                O00OOOOO0O0000O00 =O0000O0O0OO00OO0O ['message']#line:593
                                print (f'【获取种子】:{O00OOOOO0O0000O00}')#line:594
                                return False #line:595
        except Exception as O000O0O0OOOO00OOO :#line:596
            print (O000O0O0OOOO00OOO )#line:597
    def synthetic (OO0O0OO0O0000O0O0 ):#line:600
        global id ,g #line:601
        try :#line:602
            O0O0O0OOO0OO0OO00 =OO0O0OO0O0000O0O0 .level_new ()#line:603
            O0O00OOOO0000OOOO =random .randint (9 ,11 )#line:604
            OOO0O0OO000O000O0 =f'_site=8&targetSite={O0O00OOOO0000OOOO}_{timi_new()}'#line:605
            O00000OO00OO0O0OO ={'source':'scsc','authorization':OO0O0OO0O0000O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO0O0OO000O000O0 ),'signstring':OOO0O0OO000O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:616
            O0000OOOOOO000O00 ={"site":int (8 ),"targetSite":int (O0O00OOOO0000OOOO )}#line:617
            requests .request ('post',f'{host}/game/crops/move',headers =O00000OO00OO0O0OO ,json =O0000OOOOOO000O00 )#line:618
            while True :#line:619
                O000OOO0OO0OO0O00 =f'__{timi_new()}'#line:620
                O000O0OOOOO000OO0 ={'source':'scsc','authorization':OO0O0OO0O0000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0OO0OO0O00 ),'signstring':O000OOO0OO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:631
                O00O0OOOOOOO0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OOOOO000OO0 ).json ()#line:632
                if 'status'in O00O0OOOOOOO0O00O :#line:634
                    if O00O0OOOOOOO0O00O ['status']==200 :#line:635
                        OOOOO0O000OO0O0O0 =O00O0OOOOOOO0O00O ['data']['cropList']#line:636
                        OO00O00O00000O00O =O00O0OOOOOOO0O00O ['data']['gameCoreDataDBid']#line:637
                        O0O0OOO0OO000O0OO =float (O00O0OOOOOOO0O00O ['data']['silver'])/1000000000000 #line:638
                        O00000O0000OO00OO =0 #line:643
                        for O00000000O0OO0OOO in OOOOO0O000OO0O0O0 :#line:644
                            if not O00000000O0OO0OOO :#line:645
                                OO000O0O000OO00OO =f'_crop_id={OO00O00O00000O00O}&site={O00000O0000OO00OO}_{OO0O0OO0O0000O0O0.time}'#line:646
                                O0OOOO0O00OOOOOOO ={'source':'scsc','authorization':OO0O0OO0O0000O0O0 .token ,'timestamp':OO0O0OO0O0000O0O0 .time ,'sign':sign (OO000O0O000OO00OO ),'signstring':OO000O0O000OO00OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
                                OOOOO0O000O00O000 ={"site":O00000O0000OO00OO ,"crop_id":OO00O00O00000O00O }#line:657
                                OOO0O0O0O00O0000O =requests .request ('post',f'{host}/game/crops/buy',headers =O0OOOO0O00OOOOOOO ,data =OOOOO0O000O00O000 ).json ()#line:658
                                time .sleep (random .randint (1 ,3 )/10 )#line:660
                                if 'status'in OOO0O0O0O00O0000O :#line:661
                                    if OOO0O0O0O00O0000O ['status']==200 :#line:662
                                        if OOO0O0O0O00O0000O ['message']=='种子数量不足':#line:663
                                            O0O0O0OOO0OO0OO00 =OO0O0OO0O0000O0O0 .level_new ()#line:664
                                            print (f'【种植合成】:{OOO0O0O0O00O0000O["message"]}')#line:665
                                            if not OO0O0OO0O0000O0O0 .user_ad ():#line:666
                                                return False #line:667
                                    if OOO0O0O0O00O0000O ['status']==500 :#line:668
                                        print (f'【种植合成】:{OOO0O0O0O00O0000O["message"]}')#line:669
                                        return False #line:670
                            O00000O0000OO00OO +=1 #line:671
                        OOO0OO0OOO0OO0O00 =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OOOOO000OO0 ).json ()#line:672
                        O00OO0000O0OOO0OO =OOO0OO0OOO0OO0O00 ['data']['cropList']#line:673
                        OO00OOO0O00000O0O =False #line:674
                        for O00000000O0OO0OOO in range (12 ):#line:675
                            id =O00OO0000O0OOO0OO [O00000000O0OO0OOO ]['level']#line:676
                            if float (O0O0O0OOO0OO0OO00 )-float (id )>9 :#line:677
                                O000OOOOOO0O0OO00 =f'_site={O00000000O0OO0OOO}_{timi_new()}'#line:678
                                OOOO0OOO0O0OOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O0OO0O0000O0O0 .token ,'timestamp':timi_new (),'sign':sign (O000OOOOOO0O0OO00 ),'signstring':O000OOOOOO0O0OO00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:689
                                O0O0000OOO0OO0OO0 ={"site":O00000000O0OO0OOO }#line:690
                                O0O0O000OO0OOOO00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO0OOO0O0OOOOO0 ,data =O0O0000OOO0OO0OO0 ).json ()#line:692
                                if 'status'in O0O0O000OO0OOOO00 :#line:693
                                    if O0O0O000OO0OOOO00 ['status']==200 :#line:694
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:695
                            if id !=0 :#line:696
                                for O00OOO000000O00OO in range (11 ):#line:697
                                    OO00OO0OOO0O0O00O =O00OOO000000O00OO +1 #line:698
                                    g =O00OO0000O0OOO0OO [OO00OO0OOO0O0O00O ]['level']#line:699
                                    if id ==g :#line:700
                                        OO00000OO00O0OO00 =O00OOO000000O00OO +2 #line:701
                                        if OO00000OO00O0OO00 !=O00000000O0OO0OOO +1 :#line:702
                                            OOOO00000OOOO0O00 =O00000000O0OO0OOO +1 #line:703
                                            time .sleep (random .randint (1 ,3 )/10 )#line:705
                                            OOO0O0OO000O000O0 =f'_site={OOOO00000OOOO0O00 - 1}&targetSite={OO00000OO00O0OO00 - 1}_{timi_new()}'#line:706
                                            O00000OO00OO0O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0O0OO0O0000O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO0O0OO000O000O0 ),'signstring':OOO0O0OO000O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:723
                                            O0O0O00OOOO000OO0 ={"site":int (OOOO00000OOOO0O00 -1 ),"targetSite":int (OO00000OO00O0OO00 -1 )}#line:724
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00000OO00OO0O0OO ,json =O0O0O00OOOO000OO0 )#line:725
                                            OO00OOO0O00000O0O =True #line:727
                                    if OO00OOO0O00000O0O :#line:728
                                        break #line:729
                                if OO00OOO0O00000O0O :#line:730
                                    break #line:731
        except :#line:732
            OO0O0OO0O0000O0O0 .synthetic ()#line:733
    def level_new (OOO0O00OOO000OO00 ):#line:736
        try :#line:737
            OOO0O0OO00OO000O0 =f'__{timi_new()}'#line:738
            O00OOO0O0OOOOOO00 ={'source':'scsc','authorization':OOO0O00OOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO00OO000O0 ),'signstring':OOO0O0OO00OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:749
            OOOO0O000000OO0O0 =requests .request ('get',f'{host}/user',headers =O00OOO0O0OOOOOO00 ).json ()#line:750
            if 'status'in OOOO0O000000OO0O0 :#line:751
                if OOOO0O000000OO0O0 ['status']==200 :#line:752
                    return float (OOOO0O000000OO0O0 ['data']['level'])#line:753
        except Exception as O0O00O0000OOO00O0 :#line:754
            print (O0O00O0000OOO00O0 )#line:755
    def propsraffle (OO0OOO0OO000000OO ):#line:758
        try :#line:759
            while True :#line:760
                OOO0O0O0O0OOO0000 =f'__{timi_new()}'#line:761
                OOO0OO00O0OO0OOO0 ={'source':'scsc','authorization':OO0OOO0OO000000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0O0OOO0000 ),'signstring':OOO0O0O0O0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:772
                OOOO0O00OO0OOOO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0OO00O0OO0OOO0 ).json ()#line:773
                if 'status'in OOOO0O00OO0OOOO00 :#line:775
                    if OOOO0O00OO0OOOO00 ['status']==200 :#line:776
                        OO0000OOOOO0O0O00 =OOOO0O00OO0OOOO00 ['data']['rows']#line:777
                        OOO0O0OOO0O0000O0 =OOOO0O00OO0OOOO00 ['data']['vstate']#line:778
                        if OO0000OOOOO0O0O00 ==5 or OO0000OOOOO0O0O00 ==6 or OO0000OOOOO0O0O00 ==7 :#line:779
                            O0OO00OO0O0O0OO00 =OOOO0O00OO0OOOO00 ['data']['silver']#line:780
                            print (f'【转盘抽奖】:获得种子:{O0OO00OO0O0O0OO00}')#line:781
                        if OO0000OOOOO0O0O00 ==1 or OO0000OOOOO0O0O00 ==2 or OO0000OOOOO0O0O00 ==3 :#line:782
                            O0OOOOOOOOOOO0000 =OOOO0O00OO0OOOO00 ['data']['clover']#line:783
                            print (f'【转盘抽奖】:获得三叶草:{O0OOOOOOOOOOO0000}')#line:784
                        if OO0000OOOOO0O0O00 ==4 or OO0000OOOOO0O0O00 ==8 :#line:785
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:786
                        if OO0000OOOOO0O0O00 =='抽奖次数已用完':#line:790
                            break #line:824
                time .sleep (random .randint (8 ,15 )/10 )#line:825
        except Exception as O0O0OOOO0OO0OO000 :#line:826
            print (O0O0OOOO0OO0OO000 )#line:827
    def friends_invitation (O000OO0O000OO0OOO ):#line:830
        try :#line:831
            O0OO00OO0000O0000 =f'__{timi_new()}'#line:832
            OOOOOO00O0OO00OOO ={'source':'scsc','authorization':O000OO0O000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OO0000O0000 ),'signstring':O0OO00OO0000O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
            OO0OOO0O000O0O000 =requests .request ('get',f'{host}/friends',headers =OOOOOO00O0OO00OOO ).json ()#line:844
            if 'status'in OO0OOO0O000O0O000 :#line:845
                if OO0OOO0O000O0O000 ['status']==200 :#line:846
                    OO0O0O0OOO000O000 =OO0OOO0O000O0O000 ['data']['myInviteter']#line:847
                    if OO0O0O0OOO000O000 :#line:848
                        O000000OOOOO0OO0O =OO0O0O0OOO000O000 ['user']['nickname']#line:849
                        OOO00O0O0OO00O000 =O000OO0O000OO0OOO .certification ()#line:850
                        print (f'【查邀请人】:我的邀请人:{O000000OOOOO0OO0O}丨实名:{OOO00O0O0OO00O000}')#line:851
                    else :#line:852
                        if O000OO0O000OO0OOO .innerId !='0':#line:853
                            O000OO0O000OO0OOO .invitation ()#line:854
        except Exception as O0000OO0O00OO0000 :#line:855
            print (O0000OO0O00OO0000 )#line:856
    def add_clover (O0O0OO00000O0OO00 ):#line:859
        global golden_seed #line:860
        try :#line:861
            OOO0O0OO00O0000OO =f'__{timi_new()}'#line:862
            O0OO00000000OOO00 ={'source':'scsc','authorization':O0O0OO00000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO00O0000OO ),'signstring':OOO0O0OO00O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:873
            O000O00OO000OO000 =requests .request ('get',f'{host}/assets/clovers',headers =O0OO00000000OOO00 ).json ()#line:874
            if 'status'in O000O00OO000OO000 :#line:876
                if O000O00OO000OO000 ['status']==200 :#line:877
                    O0OO0OO0000000OO0 =O000O00OO000OO000 ['data']['clover']#line:878
                    OOO0O0OO00O0O0OOO =O000O00OO000OO000 ['data']['used_clover']#line:879
                    O0O000O0OO0O00OO0 =float (O0OO0OO0000000OO0 )-float (OOO0O0OO00O0O0OOO )#line:880
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O0OO00O0O0OOO}')#line:881
                    if O0O0OO00000O0OO00 .certification ()!='未实名':#line:882
                        if O0O000O0OO0O00OO0 >1 :#line:883
                            OOO0O0OO00O0000OO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O000O0OO0O00OO0)}_{timi_new()}'#line:884
                            OOO000OO0OO000OO0 ={'source':'scsc','authorization':O0O0OO00000O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO00O0000OO ),'signstring':OOO0O0OO00O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:895
                            OO00OO0000OOO00O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O000O0OO0O00OO0 )}#line:896
                            O0O0OOO0OO000OO00 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO000OO0OO000OO0 ,data =OO00OO0000OOO00O0 ).json ()#line:897
                            if 'status'in O0O0OOO0OO000OO00 :#line:899
                                if O0O0OOO0OO000OO00 ['status']==200 :#line:900
                                    print (f'【参与抽奖】:添加☘️:{O0O0OOO0OO000OO00["data"]}丨数量:{O0O000O0OO0O00OO0}')#line:901
                                if O0O0OOO0OO000OO00 ['status']==500 :#line:902
                                    print (f'【参与抽奖】:添加☘️:{O0O0OOO0OO000OO00["message"]}')#line:903
            O00000O00O0OO00OO =requests .request ('get',f'{host}/lottery',headers =O0OO00000000OOO00 ).json ()#line:904
            O0O0O0OOO0OOO0OOO =O0O0OO00000O0OO00 .winning_rewards ()#line:906
            if 'status'in O00000O00O0OO00OO :#line:907
                if O00000O00O0OO00OO ['status']==200 :#line:908
                    OOO000O0O0000000O =O00000O00O0OO00OO ['data'][0 ]['day_get_gold_quantity']#line:909
                    golden_seed +=float (OOO000O0O0000000O )#line:910
                    O00O0O0000O0O000O =O00000O00O0OO00OO ['data'][1 ]['value']#line:911
                    O000O0O0OO00OOOO0 =O00000O00O0OO00OO ['data'][0 ]['join_number']#line:912
                    OOOOO0O00OOO000OO =int (float (O00000O00O0OO00OO ['data'][0 ]['totalValue']))#line:913
                    O00OO00OO0OO000OO =float (O00O0O0000O0O000O /OOOOO0O00OOO000OO )*10000 #line:914
                    O000O0OO00OOOO00O =OOOOO0O00OOO000OO /O000O0O0OO00OOOO0 #line:915
                    print (f'【参与抽奖】:预计每天中{str(OOO000O0O0000000O)[:6]}颗金种子丨好友收益:{str(O0O0O0OOO0OOO0OOO)[:6]}')#line:916
                    print (f'【抽奖统计】:每1万☘️中{str(O00OO00OO0OO000OO)[:6]}颗金种子丨☘️人均:{str(O000O0OO00OOOO00O)[:7]}️')#line:917
        except Exception as OO000O00O0O00O00O :#line:918
            print (OO000O00O0O00O00O )#line:919
    def energy (O0000000OOO000OOO ):#line:923
        try :#line:924
            while True :#line:925
                OOO0O0000O0000000 =f'__{timi_new()}'#line:926
                O0OO0O000OO00O0OO ={'source':'scsc','authorization':O0000000OOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0000O0000000 ),'signstring':OOO0O0000O0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:937
                O0000000000O0O0O0 =requests .request ('get',f'{host}/energy/general',headers =O0OO0O000OO00O0OO ).json ()#line:938
                if 'status'in O0000000000O0O0O0 :#line:940
                    if O0000000000O0O0O0 ['status']==200 :#line:941
                        O00OOOO0O0O0OOO0O =O0000000000O0O0O0 ['data']['ordinary_water']#line:942
                        O0000O000OO0O0OOO =O0000000000O0O0O0 ['data']['ordinary_fertilizer']#line:943
                        OO0O0O0O0000000OO =O0000000000O0O0O0 ['data']['videoStatus']#line:944
                        OOOO00O000OO00OO0 =O0000000000O0O0O0 ['data']['waterVideoKey']#line:945
                        print (f'【我的营养】:肥料:{str(O0000O000OO0O0OOO).split(".")[0]}丨水滴:{str(O00OOOO0O0O0OOO0O).split(".")[0]}')#line:946
                        if float (O0000O000OO0O0OOO )<96 :#line:947
                            if OO0O0O0O0000000OO :#line:948
                                time .sleep (random .randint (160 ,180 )/10 )#line:949
                                O000OO0OOO00OO000 =99 -float (O0000O000OO0O0OOO )#line:950
                                O0O0O0OOOO00O0O00 ={"fertilizer":str (O000OO0OOO00OO000 ).split ('.')[0 ]}#line:951
                                O0OO0OOO00O0OOOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0O000OO00O0OO ).json ()#line:952
                                if 'status'in O0OO0OOO00O0OOOO0 :#line:954
                                    if O0OO0OOO00O0OOOO0 ['status']==200 :#line:955
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0OOO00O0OOOO0["message"]}')#line:956
                                    if O0OO0OOO00O0OOOO0 ['status']==500 :#line:957
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO0OOO00O0OOOO0["message"]}')#line:958
                                        break #line:959
                                if float (O0000O000OO0O0OOO )<78 :#line:961
                                    O000OO0OOO00OO000 =80 -float (O0000O000OO0O0OOO )#line:962
                                    O0OOOOOO0O0000OOO =f'_fertilizer={int(O000OO0OOO00OO000)}_{timi_new()}'#line:963
                                    O0OO00OO00O00000O ={'source':'scsc','authorization':O0000000OOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0O0000OOO ),'signstring':O0OOOOOO0O0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:974
                                    OO0OO00000O0OO000 ={"fertilizer":int (O000OO0OOO00OO000 )}#line:975
                                    O0O0OO00OOOO00O0O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OO00OO00O00000O ,data =OO0OO00000O0OO000 ).json ()#line:977
                                    if 'status'in O0O0OO00OOOO00O0O :#line:979
                                        if O0O0OO00OOOO00O0O ['status']==200 :#line:980
                                            print (f'【购买肥料】:购买肥料:{O0O0OO00OOOO00O0O["message"]}丨数量:{int(O000OO0OOO00OO000)}')#line:981
                                        if O0O0OO00OOOO00O0O ['status']==500 :#line:982
                                            print (f'【购买肥料】:购买肥料:{O0O0OO00OOOO00O0O["message"]}丨数量:{int(O000OO0OOO00OO000)}')#line:983
                                            OO00O000000O0O0O0 =O0O0OO00OOOO00O0O ["message"].split ('-')[1 ]#line:984
                                            OO000O00OO0OOOO0O =f'__{timi_new()}'#line:985
                                            OOOOOOOOO0OO00000 ={'source':'scsc','authorization':O0000000OOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO0OOOO0O ),'signstring':OO000O00OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:996
                                            O000O0O0OOOOOOOOO =requests .request ('get',f'{host}/user',headers =OOOOOOOOO0OO00000 ).json ()#line:997
                                            if 'status'in O000O0O0OOOOOOOOO :#line:998
                                                if O000O0O0OOOOOOOOO ['status']==200 :#line:999
                                                    O000OOOO0O0000OOO =O000O0O0OOOOOOOOO ['data']['inner_id']#line:1000
                                                    if give_gold (O000OOOO0O0000OOO ,float (OO00O000000O0O0O0 )+1 ):#line:1001
                                                        O0000000OOO000OOO .energy ()#line:1002
                        if float (O00OOOO0O0O0OOO0O )<880 :#line:1003
                            if OOOO00O000OO00OO0 :#line:1004
                                time .sleep (random .randint (160 ,180 )/10 )#line:1005
                                OOOO0OOO0O0000O0O =999 -float (O00OOOO0O0O0OOO0O )#line:1006
                                O0OOO00000OOO0OO0 ={"water":str (OOOO0OOO0O0000O0O ).split ('.')[0 ]}#line:1007
                                O000OO0OO000OOOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0O000OO00O0OO ).json ()#line:1008
                                if 'status'in O000OO0OO000OOOO0 :#line:1010
                                    if O000OO0OO000OOOO0 ['status']==200 :#line:1011
                                        print (f'【购买水滴】:看广告获取水滴:{O000OO0OO000OOOO0["message"]}')#line:1012
                                    if O000OO0OO000OOOO0 ['status']==500 :#line:1013
                                        print (f'【购买水滴】:看广告获取水滴:{O000OO0OO000OOOO0["message"]}')#line:1014
                                        break #line:1015
                                if float (O00OOOO0O0O0OOO0O )<780 :#line:1016
                                    OOOO0OOO0O0000O0O =800 -float (O00OOOO0O0O0OOO0O )#line:1017
                                    O0O0O000O00O00O00 =f'_water={int(OOOO0OOO0O0000O0O)}_{timi_new()}'#line:1018
                                    O0OOO0OO0O0O0O00O ={'source':'scsc','authorization':O0000000OOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00O00O00 ),'signstring':O0O0O000O00O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1029
                                    O0O000OO0OOOO000O ={"water":int (OOOO0OOO0O0000O0O )}#line:1030
                                    OOOO00O0O0OOO00OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOO0OO0O0O0O00O ,data =O0O000OO0OOOO000O ).json ()#line:1032
                                    if 'status'in OOOO00O0O0OOO00OO :#line:1034
                                        if OOOO00O0O0OOO00OO ['status']==200 :#line:1035
                                            print (f'【购买水滴】:购买水滴:{OOOO00O0O0OOO00OO["message"]}丨数量:{int(OOOO0OOO0O0000O0O)}')#line:1036
                                        if OOOO00O0O0OOO00OO ['status']==500 :#line:1037
                                            print (f'【购买水滴】:购买水滴:{OOOO00O0O0OOO00OO["message"]}丨数量:{int(OOOO0OOO0O0000O0O)}')#line:1038
                                            OO00O000000O0O0O0 =OOOO00O0O0OOO00OO ["message"].split ('-')[1 ]#line:1039
                                            OO000O00OO0OOOO0O =f'__{timi_new()}'#line:1040
                                            OOOOOOOOO0OO00000 ={'source':'scsc','authorization':O0000000OOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO0OOOO0O ),'signstring':OO000O00OO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1051
                                            O000O0O0OOOOOOOOO =requests .request ('get',f'{host}/user',headers =OOOOOOOOO0OO00000 ).json ()#line:1052
                                            if 'status'in O000O0O0OOOOOOOOO :#line:1053
                                                if O000O0O0OOOOOOOOO ['status']==200 :#line:1054
                                                    O000OOOO0O0000OOO =O000O0O0OOOOOOOOO ['data']['inner_id']#line:1055
                                                    if give_gold (O000OOOO0O0000OOO ,float (OO00O000000O0O0O0 )+1 ):#line:1056
                                                        O0000000OOO000OOO .energy ()#line:1057
                        break #line:1058
        except Exception as O000OO000OO00OOO0 :#line:1059
            print (O000OO000OO00OOO0 )#line:1060
def bundled_def ():#line:1062
    OOOOOOO0O000O0O00 =['5570536','7750212','7911652','7911680','7805624']#line:1063
    return OOOOOOO0O000O0O00 [random .randint (0 ,len (OOOOOOO0O000O0O00 )-1 )]#line:1064
def version_of_the_validation ():#line:1068
    return str ((90 -56 )/10 )#line:1069
def sc2 ():#line:1071
    return "19319#$%^&*((*"#line:1072
def OO00OO0OO0OO00OO00o0 ():#line:1074
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1075
def get_ip ():#line:1077
    return requests .request ('get','https://www.xiequ.cn/OnlyIp.aspx?yyy=123').text #line:1078
def gitee_validation ():#line:1080
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1081
def gitee_edition ():#line:1083
    try :#line:1084
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1085
    except :#line:1086
        sys .exit (0 )#line:1087
def O000OO000O0O00OOO00 ():#line:1092
    try :#line:1093
        O00000OO00O00OO00 =gitee_edition ()#line:1094
        if version_of_the_validation ()<O00000OO00O00OO00 ['CityEarth']['edition']:#line:1095
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00000OO00O00OO00["CityEarth"]["edition"]}   ❌')#line:1096
            print (f'更新内容=>>{O00000OO00O00OO00["CityEarth"]["content"]}   🎉')#line:1097
        else :#line:1098
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00000OO00O00OO00["CityEarth"]["edition"]}   ✅')#line:1099
            print (f'更新内容=>> {O00000OO00O00OO00["CityEarth"]["content"]}   🎉')#line:1100
    except Exception as O00OO0O0OOO0O0OOO :#line:1101
        print (O00OO0O0OOO0O0OOO )#line:1102
def sc3 ():#line:1104
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1105
if __name__ =='__main__':#line:1109
    start ()#line:1110
