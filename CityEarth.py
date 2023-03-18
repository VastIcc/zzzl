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
        OO0OOO00O00O0OO0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(OO0OOO00O00O0OO0O)}个账号==========")#line:17
        for O00OO000O0000OOOO in OO0OOO00O00O0OO0O :#line:18
            OO0000O00OOOO00O0 =[]#line:19
            print (f"------------正在执行第{OO0OOO00O00O0OO0O.index(O00OO000O0000OOOO) + 1}个账号------------")#line:20
            OOOO0OOOOO0O0O000 =CityEarth (O00OO000O0000OOOO ,OO0000O00OOOO00O0 ,OO0OOO00O00O0OO0O .index (O00OO000O0000OOOO ))#line:21
            def OO0OOOOOO000O00O0 ():#line:23
                if OOOO0OOOOO0O0O000 .base_info ():#line:25
                    OOOO0OOOOO0O0O000 .sealing ()#line:27
                    OOOO0OOOOO0O0O000 .invitenum ()#line:29
                    OOOO0OOOOO0O0O000 .query_to_sell ()#line:31
                    OOOO0OOOOO0O0O000 .game_map ()#line:33
                    OOOO0OOOOO0O0O000 .friends_invitation ()#line:37
                    OOOO0OOOOO0O0O000 .energy ()#line:39
                    OOOO0OOOOO0O0O000 .add_clover ()#line:41
                    OOOO0OOOOO0O0O000 .propsraffle ()#line:43
                    OOOO0OOOOO0O0O000 .synthetic ()#line:45
                    OOOO0OOOOO0O0O000 .crops_illustrated ()#line:47
                    OOOO0OOOOO0O0O000 .withdraw ()#line:49
                    if float (datetime .datetime .now ().hour )>8 :#line:50
                        OOOO0OOOOO0O0O000 .give_gold ()#line:52
            O0OOOOOOOOOOOO0OO =threading .Thread (target =OO0OOOOOO000O00O0 )#line:54
            O0OOOOOOOOOOOO0OO .start ()#line:55
            time .sleep (time_xx )#line:56
        print (f"------------正在处理数据------------")#line:57
        time .sleep (0.5 )#line:58
        O00O0OOOOO00O0OOO =format_msg ()#line:59
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O0OOOOO00O0OOO +' ')#line:60
        time .sleep (15 )#line:61
        print (f'所有未出售的芦荟:{count_list}颗')#line:62
        print ('开始打印好友数量不足2的ID')#line:63
        for O0O00OO000OOOO0OO in invited_new :#line:64
            print (O0O00OO000OOOO0OO )#line:65
        print ('开始打印未实名的token')#line:66
        for OO00000OOOOOOO0OO in weishim :#line:67
            print (OO00000OOOOOOO0OO )#line:68
    except Exception as O00OOO0OOOO0000OO :#line:69
        print (O00OOO0OOOO0000OO )#line:70
def give_gold (OOOOO0OO000O0OOOO ,OOOOOOOOO0O000OO0 ):#line:74
    try :#line:75
        O0O0OOO0O00O00OO0 =f'_doneeNo={OOOOO0OO000O0OOOO}&quantity={int(OOOOOOOOO0O000OO0)}_{timi_new()}'#line:76
        O000OO000OO0000O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O00O00OO0 ),'signstring':O0O0OOO0O00O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:87
        OOOO0O0O0OOOOO000 ={"quantity":int (OOOOOOOOO0O000OO0 ),"doneeNo":OOOOO0OO000O0OOOO }#line:91
        OO00OOOO00O000OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O000OO000OO0000O0 ,data =OOOO0O0O0OOOOO000 ).json ()#line:92
        if 'status'in OO00OOOO00O000OO0 :#line:94
            if OO00OOOO00O000OO0 ['status']==200 :#line:95
                if OO00OOOO00O000OO0 ['data']:#line:96
                    print (f'【赠送种子】:赠送{int(OOOOOOOOO0O000OO0)}种子给{OOOOO0OO000O0OOOO}成功')#line:97
                    return True #line:98
            if OO00OOOO00O000OO0 ['status']==401 :#line:99
                print (f'【赠送种子】:{OO00OOOO00O000OO0["message"]}')#line:100
                return False #line:101
            if OO00OOOO00O000OO0 ['status']==500 :#line:102
                print (f'【赠送种子】:{OO00OOOO00O000OO0["message"]}')#line:103
                return False #line:104
        return False #line:105
    except Exception as O0O0O00O0OO0OOOOO :#line:106
        print (O0O0O00O0OO0OOOOO )#line:107
def kvkv ():#line:110
    return '/vastzzzl/vastzzzl/raw/master'#line:111
def oyoy ():#line:113
    return '卡密未激活   ❌'#line:114
def sign (OO00O00O0O00000OO ):#line:117
    OO00OOO00O0OOO00O =hashlib .md5 (OO00O00O0O00000OO .encode ()).hexdigest ()#line:118
    O00O00O00O0O0OO00 =sc1 ()#line:119
    OO0OOO0OO0O0O00OO =sc2 ()#line:120
    O0000OO00O000O000 =sc3 ()#line:121
    O0OO0O0OO0O0OOOO0 =O00O00O00O0O0OO00 +OO00OOO00O0OOO00O +OO0OOO0OO0O0O00OO +O0000OO00O000O000 #line:122
    OOO00OO0O0000OO00 =hashlib .md5 (O0OO0O0OO0O0OOOO0 .encode ()).hexdigest ()#line:123
    return OOO00OO0O0000OO00 #line:124
def format_msg ():#line:127
    O0O000O0OOOOO00OO =""#line:128
    for O0O000OO0OO00O0O0 in msg_list :#line:129
        O0O000O0OOOOO00OO +=str (O0O000OO0OO00O0O0 )+"\r\n"#line:130
    return O0O000O0OOOOO00OO #line:131
def sc1 ():#line:134
    return "scsc%^&*"#line:135
def O000OO0O00OO00O00 ():#line:138
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:139
        ubbbf ()#line:140
    else :#line:141
        print (oyoy ())#line:142
        exit (1 )#line:143
def timi_new ():#line:146
    return str (int (time .time ()*1000 ))#line:147
json_path ="CityEarth_data.json"#line:150
json_path1 ="CityEarth_data.json"#line:151
dict ={}#line:152
def get_json_data (OOOOOOOOOOO000O00 ,OOO0O000O0O000O00 ,OO0000OOO0O00000O ,OOO00O0O0O0O00O00 ):#line:155
    with open (OOOOOOOOOOO000O00 ,'rb')as O00OO0OO00O00O000 :#line:156
        O0OOOOOOOO0OO0O0O =json .load (O00OO0OO00O00O000 )#line:157
        O0OOOOOOOO0OO0O0O ['data'][OOO0O000O0O000O00 ][OO0000OOO0O00000O ]=OOO00O0O0O0O00O00 #line:158
        O00O0O0O00O0O0OO0 =O0OOOOOOOO0OO0O0O #line:159
    O00OO0OO00O00O000 .close ()#line:160
    return O00O0O0O00O0O0OO0 #line:161
def write_json_data (O00O00O00O0O0O000 ):#line:164
    with open (json_path1 ,'w')as O0OOO0O0O000OOOO0 :#line:165
        json .dump (O00O00O00O0O0O000 ,O0OOO0O0O000OOOO0 )#line:166
    O0OOO0O0O000OOOO0 .close ()#line:167
    return True #line:168
class CityEarth :#line:171
    def __init__ (O0O0OO0OOOO0000O0 ,O0O0O00O000OOO0O0 ,O0OOO000O00000000 ,O000O0OO000000O00 ):#line:173
        try :#line:174
            O0O0OO0OOOO0000O0 .msg =O0OOO000O00000000 #line:175
            O0O0OO0OOOO0000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:176
            O0O0OO0OOOO0000O0 .token =O0O0O00O000OOO0O0 ['authorization']#line:177
            O0O0OO0OOOO0000O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:178
            O0O0OO0OOOO0000O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:179
            O0O0OO0OOOO0000O0 .elephant_user =O0O0O00O000OOO0O0 ['elephant_user']#line:180
            O0O0OO0OOOO0000O0 .elephant_pswd =O0O0O00O000OOO0O0 ['elephant_pswd']#line:181
            O0O0OO0OOOO0000O0 .elephant_Task_ID =O0O0O00O000OOO0O0 ['elephant_Task_ID']#line:182
            O0O0OO0OOOO0000O0 .len_new =O000O0OO000000O00 #line:183
        except :#line:184
            print ('变量格式错误')#line:185
    def base_info (O00OOO00O0000OOO0 ):#line:188
        try :#line:189
            O00OOO00O0000OOO0 .watched_ad ()#line:191
            O0OO0O0O00OO0OOOO =f'__{timi_new()}'#line:192
            OOO00OOOOOO0OO00O ={'source':'scsc','authorization':O00OOO00O0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O00OO0OOOO ),'signstring':O0OO0O0O00OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:203
            OO00OOO0OO00O00O0 =requests .request ('get',f'{host}/user',headers =OOO00OOOOOO0OO00O ).json ()#line:204
            if 'status'in OO00OOO0OO00O00O0 :#line:206
                if OO00OOO0OO00O00O0 ['status']==200 :#line:207
                    OOOO0OOOO0O00OO00 =OO00OOO0OO00O00O0 ['data']['nickname']#line:208
                    O00000OO00O0O0O00 =OO00OOO0OO00O00O0 ['data']['inner_id']#line:209
                    O0O0O0OOO0O0O00OO =OO00OOO0OO00O00O0 ['data']['assets']['gold']#line:210
                    OOOOOOOO0O0O0O000 =OO00OOO0OO00O00O0 ['data']['level']#line:211
                    print (f'【账号信息】:昵称:{OOOO0OOOO0O00OO00[:5]}丨ID:{O00000OO00O0O0O00}丨等级:{OOOOOOOO0O0O0O000}丨金种子:{str(O0O0O0OOO0O0O00OO).split(".")[0]}')#line:213
                    if 'wx_'in OOOO0OOOO0O00OO00 :#line:214
                        O00OOO00O0000OOO0 .change_nickname ()#line:215
                if OO00OOO0OO00O00O0 ['status']==401 :#line:216
                    print ('【账号信息】:账号失效正在尝试登录')#line:217
                    if O00OOO00O0000OOO0 .elephant_user =='f':#line:218
                        return False #line:219
                    OO0O0O00O0OO0O000 =Invalid_login .addtask (elephant_user =O00OOO00O0000OOO0 .elephant_user ,elephant_pswd =O00OOO00O0000OOO0 .elephant_pswd ,elephant_Task_ID =O00OOO00O0000OOO0 .elephant_Task_ID )#line:222
                    OO0000000OOO000OO =get_json_data (json_path ,O00OOO00O0000OOO0 .len_new ,'authorization',OO0O0O00O0OO0O000 )#line:223
                    if write_json_data (OO0000000OOO000OO ):#line:224
                        print ('正在写入账号配置文件')#line:225
                    return False #line:226
                if OO00OOO0OO00O00O0 ['status']==500 :#line:227
                    return False #line:228
            return True #line:229
        except Exception as OOO0O00O00OOOO00O :#line:230
            print (OOO0O00O00OOOO00O )#line:231
    def sealing (O0OO000OO0OO00OOO ):#line:234
        try :#line:235
            O000OOOOOOOOOO0O0 =f'__{timi_new()}'#line:236
            O0O00O0O0OOO0O0OO ={'source':'scsc','authorization':O0OO000OO0OO00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOOOOOOOO0O0 ),'signstring':O000OOOOOOOOOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:247
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O00O0O0OOO0O0OO )#line:248
            requests .request ('get',f'{host}/packsack/list',headers =O0O00O0O0OOO0O0OO )#line:249
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O00O0O0OOO0O0OO )#line:250
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O00O0O0OOO0O0OO )#line:251
            requests .request ('get',f'{host}/user',headers =O0O00O0O0OOO0O0OO )#line:252
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O00O0O0OOO0O0OO )#line:253
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O00O0O0OOO0O0OO )#line:254
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O00O0O0OOO0O0OO )#line:255
            requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0O0OOO0O0OO )#line:256
            requests .request ('get',f'{host}/assets',headers =O0O00O0O0OOO0O0OO )#line:257
        except Exception as O0000O00OO000OO00 :#line:258
            print (O0000O00OO000OO00 )#line:259
    def ddd (OOOOOO0OO0OOOOOOO ):#line:261
        try :#line:262
            O0OOO00000000000O =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:263
            O0O0OO0O0O0OO0O0O ={'source':'scsc','authorization':OOOOOO0OO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00000000000O ),'signstring':O0OOO00000000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            OOO000O00000O0OOO =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O0O0OO0O0O0OO0O0O ).json ()#line:275
            print (OOO000O00000O0OOO )#line:276
        except Exception as OOO00OOOO00O000OO :#line:279
            print (OOO00OOOO00O000OO )#line:280
    def the_query (OOOO000000O000OOO ):#line:285
        try :#line:286
            OOO000O000OO000OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:287
            OOO0OOO0O0000OOOO ={'authorization':OOOO000000O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OO000OO ),'signstring':OOO000O000OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:297
            O0O0O00O0O0OO0000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO0OOO0O0000OOOO ).json ()#line:299
            if 'status'in O0O0O00O0O0OO0000 :#line:301
                if O0O0O00O0O0OO0000 ['status']==200 :#line:302
                    OOO000O00O0000OOO =O0O0O00O0O0OO0000 ['data']['rows'][4 ]['price']#line:303
                    OOOO000000O000OOO .market_sale (OOO000O00O0000OOO )#line:304
        except Exception as OOOOOOOOO0OO000O0 :#line:305
            print (OOOOOOOOO0OO000O0 )#line:306
    def market_sale (O0OOO0OOO00OOOOO0 ,OO0O000OOO0O0OO00 ):#line:309
        try :#line:310
            O0OOOO0O0O0OOOOOO =timi_new ()#line:311
            OOOOO00O0O000O0O0 =f'type=crop__{O0OOOO0O0O0OOOOOO}'#line:312
            OO0O0OO0OOO0O0O0O ={'source':'scsc','authorization':O0OOO0OOO00OOOOO0 .token ,'timestamp':str (O0OOOO0O0O0OOOOOO ),'sign':sign (OOOOO00O0O000O0O0 ),'signstring':OOOOO00O0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:323
            OO00O0OO00O0OO0O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O0OO0OOO0O0O0O ).json ()#line:325
            if 'status'in OO00O0OO00O0OO0O0 :#line:327
                if OO00O0OO00O0OO0O0 ['status']==200 :#line:328
                    if OO00O0OO00O0OO0O0 ['data']['rows']:#line:329
                        OO00O00000OOO00O0 =OO00O0OO00O0OO0O0 ['data']['rows'][0 ]['packsackItemId']#line:330
                        OOO00O0OOO00O0000 =OO00O0OO00O0OO0O0 ['data']['rows'][0 ]['quantity']#line:331
                        OO000O00OOOOO00O0 =float (OO0O000OOO0O0OO00 )-0.001 #line:332
                        if OO000O00OOOOO00O0 >9 :#line:333
                            O00O00000OOOOO0OO =f'_packsackItemId={OO00O00000OOO00O0}&price={str(OO0O000OOO0O0OO00)[:5]}&quantity={OOO00O0OOO00O0000}_{O0OOOO0O0O0OOOOOO}'#line:334
                            OO0O0OOOO0O0OOOO0 ={'source':'scsc','authorization':O0OOO0OOO00OOOOO0 .token ,'timestamp':str (O0OOOO0O0O0OOOOOO ),'sign':sign (O00O00000OOOOO0OO ),'signstring':O00O00000OOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:345
                            O00OO0OO000O0000O ={"packsackItemId":OO00O00000OOO00O0 ,"price":str (OO0O000OOO0O0OO00 )[:5 ],"quantity":str (OOO00O0OOO00O0000 )}#line:350
                            O000O00OOO0O0OOO0 =requests .request ('post',f'{host}/market/sale',headers =OO0O0OOOO0O0OOOO0 ,data =O00OO0OO000O0000O ).json ()#line:351
                            if 'status'in O000O00OOO0O0OOO0 :#line:353
                                if O000O00OOO0O0OOO0 ['status']==200 :#line:354
                                    print (f'【上架芦荟】:数量:{OOO00O0OOO00O0000}丨价格:{str(OO0O000OOO0O0OO00)[:5]}')#line:355
        except Exception as O0O000O0O000O0000 :#line:356
            print (O0O000O0O000O0000 )#line:357
    def query_to_sell (O0OOO000000O00OO0 ):#line:360
        try :#line:361
            OOO0OOO000O0O000O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:362
            O0OO00000OOO0OOOO ={'source':'scsc','authorization':O0OOO000000O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO000O0O000O ),'signstring':OOO0OOO000O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:373
            OO0O00O0OO0OO000O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00000OOO0OOOO ).json ()#line:375
            if 'status'in OO0O00O0OO0OO000O :#line:377
                if OO0O00O0OO0OO000O ['status']==200 :#line:378
                    for O000OO0000O00OO0O in OO0O00O0OO0OO000O ['data']['rows']:#line:379
                        O000O00O0O00O00OO =O000OO0000O00OO0O ['materialKey']#line:380
                        OO00OOOO00O00OOO0 =O000OO0000O00OO0O ['quantity']#line:381
                        OO0OOO0O000O000O0 =O000OO0000O00OO0O ['price']#line:382
                        O00OO00OO00O0OOO0 =O000OO0000O00OO0O ['saleState']#line:383
                        if O00OO00OO00O0OOO0 ==0 :#line:384
                            print (f'【出售订单】:名称:{O000O00O0O00O00OO}丨数量:{OO00OOOO00O00OOO0}丨价格:{OO0OOO0O000O000O0}')#line:385
                            OOO0OO00O00OO00O0 =O000OO0000O00OO0O ['id']#line:386
                            if float (datetime .datetime .now ().hour )>8 :#line:387
                                O0OOO000000O00OO0 .cacel_sale (OOO0OO00O00OO00O0 )#line:388
        except Exception as OOO0O00O000000OO0 :#line:389
            print (OOO0O00O000000OO0 )#line:390
    def cacel_sale (OOO00O00000OO0OOO ,O0OOOOO0O0OOO0O00 ):#line:393
        try :#line:394
            O0O00OO0OOO00O00O =f'_saleId={O0OOOOO0O0OOO0O00}_{timi_new()}'#line:395
            OOOO0O0OO00O000O0 ={'source':'scsc','authorization':OOO00O00000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0OOO00O00O ),'signstring':O0O00OO0OOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:406
            O00000OO0OO0O0O00 ={"saleId":O0OOOOO0O0OOO0O00 }#line:409
            O0OOOO00OOO00OOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OOOO0O0OO00O000O0 ,data =O00000OO0OO0O0O00 ).json ()#line:410
            if 'status'in O0OOOO00OOO00OOOO :#line:412
                if O0OOOO00OOO00OOOO ['status']==200 :#line:413
                    print (f'【下架出售】:{O0OOOO00OOO00OOOO["data"]}')#line:414
        except Exception as OOOO00OO000OOO0O0 :#line:415
            print (OOOO00OO000OOO0O0 )#line:416
    def change_nickname (O000O0OO00O0O0O0O ):#line:419
        try :#line:420
            OOO00O0OO000O0O00 =timi_new ()#line:421
            O0OO00OOOO00O000O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:422
            O0OO0000OO0OO0OO0 =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO00OOOO00O000O ).text #line:423
            OO0O0OO0OO00O0O0O =re .findall ('<ul><li>(.*?)</li>',O0OO0000OO0OO0OO0 )[0 ][:3 ]#line:424
            O00OO0O00O0O00000 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0OO0OO00O0O0O}').json ()#line:425
            O0O0O0O0OO00OO0O0 =O00OO0O00O0O00000 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:426
            OOO000000O00OOOO0 ={"nickname":O0O0O0O0OO00OO0O0 }#line:427
            O0000000O0OOOO000 =f'_nickname={O0O0O0O0OO00OO0O0}_{OOO00O0OO000O0O00}'#line:428
            OOO0O000O0OO0OO00 ={'source':'scsc','authorization':O000O0OO00O0O0O0O .token ,'timestamp':OOO00O0OO000O0O00 ,'sign':sign (O0000000O0OOOO000 ),'signstring':O0000000O0OOOO000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:439
            OO0000000OO0OO0O0 =requests .request ('patch',f'{host}/user/nickname',headers =OOO0O000O0OO0OO00 ,data =OOO000000O00OOOO0 ).json ()#line:440
            if 'status'in OO0000000OO0OO0O0 :#line:442
                if OO0000000OO0OO0O0 ['status']==200 :#line:443
                    print (f'【修改网名】:网名:{O0O0O0O0OO00OO0O0}丨{OO0000000OO0OO0O0["message"]}')#line:444
        except Exception as O0OO0O00O0000OO0O :#line:445
            print (O0OO0O00O0000OO0O )#line:446
    def withdraw (OOO000OOO00000OOO ):#line:449
        try :#line:450
            O0O0O0OOO0OOO0O00 =f'__{timi_new()}'#line:451
            O00OO0OO0OO000OO0 ={'source':'scsc','authorization':OOO000OOO00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOO0OOO0O00 ),'signstring':O0O0O0OOO0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:462
            OOO0O000000O0OOOO =requests .request ('get',f'{host}/assets',headers =O00OO0OO0OO000OO0 ).json ()#line:463
            if 'status'in OOO0O000000O0OOOO :#line:465
                if OOO0O000000O0OOOO ['status']==200 :#line:466
                    OO0OOOO00O0OO0O00 =OOO0O000000O0OOOO ['data']['cash']#line:467
                    if float (OO0OOOO00O0OO0O00 )>20 :#line:468
                        O0O0O0OOO0OOO0O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:469
                        O00OO0OO0OO000OO0 ={'authorization':OOO000OOO00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOO0OOO0O00 ),'signstring':O0O0O0OOO0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:479
                        O0O0O0O0OO0O000O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:480
                        OOO0O0OO00O00O0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OO0OO0OO000OO0 ,data =O0O0O0O0OO0O000O0 ).json ()#line:482
                        if 'status'in OOO0O0OO00O00O0OO :#line:484
                            if OOO0O0OO00O00O0OO ['status']==200 :#line:485
                                print (f'【余额提现】:{OOO0O0OO00O00O0OO["data"]}')#line:486
                        if 'status'in OOO0O0OO00O00O0OO :#line:487
                            if OOO0O0OO00O00O0OO ['status']==500 :#line:488
                                print (f'【余额提现】:{OOO0O0OO00O00O0OO["message"]}')#line:489
        except Exception as OO0O000OOO0O0O000 :#line:490
            print (OO0O000OOO0O0O000 )#line:491
    def invitenum (OO0O00OOO00O0000O ):#line:494
        global invited_new #line:495
        try :#line:496
            OOOOO00O000O0O0OO =f'__{timi_new()}'#line:497
            O00OO000O000000OO ={'source':'scsc','authorization':OO0O00OOO00O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000O0O0OO ),'signstring':OOOOO00O000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:508
            O0OO0O0000OO0OO0O =requests .request ('get',f'{host}/invite/invitenum',headers =O00OO000O000000OO ).json ()#line:509
            if 'status'in O0OO0O0000OO0OO0O :#line:511
                if O0OO0O0000OO0OO0O ['status']==200 :#line:512
                    O0OOOOOOO00OOO000 =O0OO0O0000OO0OO0O ['data']['invited_count']#line:513
                    O0O00O00000OOOO00 =O0OO0O0000OO0OO0O ['data']['invited_second_count']#line:514
                    print (f'【我的邀请】:直邀好友:{O0OOOOOOO00OOO000}丨间邀好友:{O0O00O00000OOOO00}')#line:515
                    if O0OOOOOOO00OOO000 <2 :#line:516
                        O00O0O00OO0O0OO0O =f'__{timi_new()}'#line:517
                        O00OOO0OO000000OO ={'source':'scsc','authorization':OO0O00OOO00O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00OO0O0OO0O ),'signstring':O00O0O00OO0O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:528
                        OOOOOOO0000OO0O0O =requests .request ('get',f'{host}/user',headers =O00OOO0OO000000OO ).json ()#line:529
                        if 'status'in OOOOOOO0000OO0O0O :#line:531
                            if OOOOOOO0000OO0O0O ['status']==200 :#line:532
                                invited_new .append (OOOOOOO0000OO0O0O ['data']['inner_id'])#line:533
        except Exception as OO00000OO0OO0OOO0 :#line:534
            print (OO00000OO0OO0OOO0 )#line:535
    def game_map (OO0OOOOO000O0OO0O ):#line:538
        global count_list #line:539
        try :#line:540
            O000O0OOO0O0OO000 =f'__{timi_new()}'#line:541
            OO0O0O0O00OO00OO0 ={'source':'scsc','authorization':OO0OOOOO000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OOO0O0OO000 ),'signstring':O000O0OOO0O0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:552
            O00O0OO00O00O0O0O =requests .request ('get',f'{host}/game/map',headers =OO0O0O0O00OO00OO0 ).json ()#line:553
            if 'status'in O00O0OO00O00O0O0O :#line:555
                if O00O0OO00O00O0O0O ['status']==200 :#line:556
                    for O000O00000OO0OOO0 in O00O0OO00O00O0O0O ['data']['list'][0 ]['crops']:#line:557
                        OOOO00000OO00OOO0 =O000O00000OO0OOO0 ['level']#line:559
                        if OOOO00000OO00OOO0 ==41 :#line:560
                            OOOO000OO00O0OOOO =O000O00000OO0OOO0 ['crop_name']#line:561
                            OO00O00OO000O00O0 =O000O00000OO0OOO0 ['count']#line:562
                            if OO00O00OO000O00O0 >0 :#line:563
                                count_list +=OO00O00OO000O00O0 #line:564
                                print (f'【农业资产】:{OOOO000OO00O0OOOO}丨数量:{OO00O00OO000O00O0}')#line:565
                                if float (datetime .datetime .now ().hour )>8 :#line:566
                                    OO0OOOOO000O0OO0O .the_query ()#line:567
        except Exception as O000OOOO0OOOOO0OO :#line:568
            print (O000OOOO0OOOOO0OO )#line:569
    def give_gold (O0O0O00OO0OO0O0OO ):#line:572
        try :#line:573
            OO0O0O0OOO0O0OOO0 =f'__{timi_new()}'#line:574
            O0O0OOO0O000000OO ={'source':'scsc','authorization':O0O0O00OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO0O0OOO0 ),'signstring':OO0O0O0OOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:585
            OOOO0O0O0OO00O0O0 =requests .request ('get',f'{host}/user',headers =O0O0OOO0O000000OO ).json ()#line:586
            if 'status'in OOOO0O0O0OO00O0O0 :#line:587
                if OOOO0O0O0OO00O0O0 ['status']==200 :#line:588
                    if float (O0O0O00OO0OO0O0OO .doneeNo )!=0 :#line:589
                        OO0OO0O0OOOOO0000 =OOOO0O0O0OO00O0O0 ['data']['assets']['gold']#line:590
                        if float (OO0OO0O0OOOOO0000 )>float (O0O0O00OO0OO0O0OO .innerId ):#line:591
                            O00O0O0OOO0OO0OO0 =int (float (OO0OO0O0OOOOO0000 )/1.1 )#line:592
                            OO0O0O0OOO0O0OOO0 =f'_doneeNo={O0O0O00OO0OO0O0OO.doneeNo}&quantity={O00O0O0OOO0OO0OO0}_{timi_new()}'#line:593
                            O0O0OOO0O000000OO ={'source':'scsc','authorization':O0O0O00OO0OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO0O0OOO0 ),'signstring':OO0O0O0OOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:604
                            OOO0OOOO0O0000000 ={"quantity":O00O0O0OOO0OO0OO0 ,"doneeNo":O0O0O00OO0OO0O0OO .doneeNo }#line:608
                            O0O000O00OOOOOOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0OOO0O000000OO ,data =OOO0OOOO0O0000000 ).json ()#line:609
                            if 'status'in O0O000O00OOOOOOO0 :#line:611
                                if O0O000O00OOOOOOO0 ['status']==200 :#line:612
                                    if O0O000O00OOOOOOO0 ['data']:#line:613
                                        print (f'【赠送种子】:赠送{O00O0O0OOO0OO0OO0}种子给{O0O0O00OO0OO0O0OO.doneeNo}成功')#line:614
                    else :#line:615
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:616
        except Exception as O0OO00O00O0O0000O :#line:617
            print (O0OO00O00O0O0000O )#line:618
    def invitation (O0000O00OOOOOO000 ):#line:620
        try :#line:621
            _O00O000O00000OO0O =float (bundled_def ())/4 #line:622
            O0O0OOOO00OOOO000 =f'_innerId={int(_O00O000O00000OO0O)}_{timi_new()}'#line:623
            O0OOO0000OOOO00O0 ={'source':'scsc','authorization':O0000O00OOOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO00OOOO000 ),'signstring':O0O0OOOO00OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            O00OO0OO00O0000O0 ={"innerId":int (_O00O000O00000OO0O )}#line:635
            requests .request ('post',f'{host}/friends/my-invitation',headers =O0OOO0000OOOO00O0 ,data =O00OO0OO00O0000O0 )#line:636
        except Exception as O0O0OO0OO00OOOO0O :#line:637
            print (O0O0OO0OO00OOOO0O )#line:638
    def winning_rewards (O00OO0O000O0OO00O ):#line:641
        try :#line:642
            OOOOO00O000OO0OO0 =f'__{timi_new()}'#line:643
            O00O0000000O000O0 ={'source':'scsc','authorization':O00OO0O000O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O000OO0OO0 ),'signstring':OOOOO00O000OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:654
            O0O0O0O00O0OO0OO0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00O0000000O000O0 ).json ()#line:655
            if 'status'in O0O0O0O00O0OO0OO0 :#line:657
                if O0O0O0O00O0OO0OO0 ['status']==200 :#line:658
                    if O0O0O0O00O0OO0OO0 ['data']['amount']:#line:659
                        OO0OOOO0OO000OO00 =O0O0O0O00O0OO0OO0 ['data']['amount']['gold']#line:660
                        return OO0OOOO0OO000OO00 #line:661
                    else :#line:662
                        return 0 #line:663
        except Exception as OOO0OOOO000OO000O :#line:664
            print (OOO0OOOO000OO000O )#line:665
    def certification (O0O0O000OOOOOO0O0 ):#line:668
        try :#line:669
            OO00OOOOOO00O000O =f'__{timi_new()}'#line:670
            OOOOOO00O00O00OOO ={'source':'scsc','authorization':O0O0O000OOOOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOOOOO00O000O ),'signstring':OO00OOOOOO00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:681
            OOOO0O000000O0O00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOOO00O00O00OOO ).json ()#line:682
            if 'status'in OOOO0O000000O0O00 :#line:684
                if OOOO0O000000O0O00 ['status']==200 :#line:685
                    if OOOO0O000000O0O00 ['data']['result']:#line:686
                        O0OOO0OO00O0OOOO0 =OOOO0O000000O0O00 ['data']['nick_name']#line:687
                        return O0OOO0OO00O0OOOO0 #line:688
                    else :#line:689
                        return '未实名'#line:690
        except Exception as O00000O000000OOOO :#line:691
            print (O00000O000000OOOO )#line:692
    def crops_illustrated (OO0OO0OO0000O000O ):#line:695
        try :#line:696
            OOO0OO0O000OO00OO =f'__{timi_new()}'#line:697
            OO0000OOOO0000O00 ={'source':'scsc','authorization':OO0OO0OO0000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O000OO00OO ),'signstring':OOO0OO0O000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:708
            OO0O0O000OOOOO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0000OOOO0000O00 ).json ()#line:709
            if 'status'in OO0O0O000OOOOO0O0 :#line:711
                if OO0O0O000OOOOO0O0 ['status']==200 :#line:712
                    O0000OO00O0O0O000 =OO0O0O000OOOOO0O0 ['data'][0 ]['crops']#line:713
                    for O000000OOOOOOOO0O in O0000OO00O0O0O000 :#line:714
                        if O000000OOOOOOOO0O ['ill_clover_award']:#line:715
                            if float (O000000OOOOOOOO0O ['ill_clover_award'])>1 :#line:716
                                if O000000OOOOOOOO0O ['is_finish']:#line:717
                                    if not O000000OOOOOOOO0O ['is_getit']:#line:718
                                        if OO0OO0OO0000O000O .certification ()!='未实名':#line:719
                                            OOO0OO0O000OO00OO =f'_award_level={O000000OOOOOOOO0O["level"]}_{timi_new()}'#line:720
                                            OO0000OOOO0000O00 ={'source':'scsc','authorization':OO0OO0OO0000O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O000OO00OO ),'signstring':OOO0OO0O000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:731
                                            OO0O0O0OOOOO0000O ={"award_level":O000000OOOOOOOO0O ['level']}#line:732
                                            OOOOO0OOOOOOO00O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0000OOOO0000O00 ,json =OO0O0O0OOOOO0000O ).json ()#line:734
                                            if 'status'in OOOOO0OOOOOOO00O0 :#line:735
                                                if OOOOO0OOOOOOO00O0 ['status']==200 :#line:736
                                                    OOO0OOO00O0OO000O =OOOOO0OOOOOOO00O0 ['data']['ill_clover_award']#line:737
                                                    print (f'【图鉴奖励】:领取{O000000OOOOOOOO0O["crop_name"]}成就丨奖励{OOO0OOO00O0OO000O}☘️')#line:739
                                                if OOOOO0OOOOOOO00O0 ['status']==500 :#line:740
                                                    print (f'【图鉴奖励】:{OOOOO0OOOOOOO00O0["message"]}')#line:741
        except Exception as O00O000OO0O000OOO :#line:742
            print (O00O000OO0O000OOO )#line:743
    def watched_ad (OO0OOOO0O0O000OO0 ):#line:746
        try :#line:747
            O0O00O0O0OOO0O00O =f'__{timi_new()}'#line:748
            OOO0OO00OOO000O0O ={'source':'scsc','authorization':OO0OOOO0O0O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O0OOO0O00O ),'signstring':O0O00O0O0OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:759
            O000OO000OO0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO00OOO000O0O ).json ()#line:760
            if 'status'in O000OO000OO0O0000 :#line:762
                if O000OO000OO0O0000 ['status']==200 :#line:763
                    if 'offlineInfo'in O000OO000OO0O0000 ['data']:#line:764
                        time .sleep (random .randint (1 ,3 ))#line:765
                        O0O0O0000O00OO0O0 =O000OO000OO0O0000 ['data']['offlineInfo']['off_minute']#line:766
                        O0000O0OOOOOO000O =float (O000OO000OO0O0000 ['data']['silver'])/1000000000000 #line:767
                        time .sleep (1 )#line:768
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOO0OO00OOO000O0O ).json ()#line:769
                        time .sleep (2 )#line:770
                        O0OOO0O00OOO0OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0OO00OOO000O0O ).json ()#line:771
                        if 'status'in O0OOO0O00OOO0OOO0 :#line:773
                            if O0OOO0O00OOO0OOO0 ['status']==200 :#line:774
                                O000O000OOOO0OO0O =float (O0OOO0O00OOO0OOO0 ['data']['silver'])/1000000000000 #line:775
                                O00000OO00000O0O0 =str (O000O000OOOO0OO0O -O0000O0OOOOOO000O )[:6 ]#line:776
                                print (f'【离线奖励】:翻倍离线{O0O0O0000O00OO0O0}分钟奖励🌱数量:{O00000OO00000O0O0}t粒')#line:777
        except Exception as O00O0OOO000OO000O :#line:778
            print (O00O0OOO000OO000O )#line:779
    def user_ad (OOO0OO0OO00000OOO ):#line:782
        try :#line:783
            O0O0OO00O00000OO0 =f'__{timi_new()}'#line:784
            OOO00O0000O00O00O ={'source':'scsc','authorization':OOO0OO0OO00000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00000OO0 ),'signstring':O0O0OO00O00000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:795
            O0OO00O0OOO0O000O =requests .request ('get',f'{host}/user/ad',headers =OOO00O0000O00O00O ).json ()#line:796
            if 'status'in O0OO00O0OOO0O000O :#line:798
                if O0OO00O0OOO0O000O ['status']==200 :#line:799
                    OOO0OOO0O0OO000O0 =O0OO00O0OOO0O000O ['data']['max_time']#line:800
                    OO0OOOOO0000OO0O0 =O0OO00O0OOO0O000O ['data']['watch_time']#line:801
                    OOO0O0000OO0O00OO =O0OO00O0OOO0O000O ['data']['added_time']#line:802
                    print (f'【获取种子】:获取🌱剩余{OOO0O0000OO0O00OO + OOO0OOO0O0OO000O0 - OO0OOOOO0000OO0O0}次丨好友提供:{OOO0O0000OO0O00OO}次')#line:803
                    if OOO0O0000OO0O00OO +OOO0OOO0O0OO000O0 -OO0OOOOO0000OO0O0 >0 :#line:804
                        time .sleep (random .randint (16 ,19 ))#line:805
                        O00O0OOO0OO000O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O0000O00O00O ).json ()#line:806
                        if 'status'in O00O0OOO0OO000O0O :#line:808
                            if O00O0OOO0OO000O0O ['status']==200 :#line:809
                                OO00O0000O00OOO0O =float (O00O0OOO0OO000O0O ['data']['silver'])/1000000000000 #line:810
                                print (f'【获取种子】:获得🌱:{int(OO00O0000O00OOO0O)}t粒')#line:811
                                return True #line:812
                            if O00O0OOO0OO000O0O ['status']==500 :#line:813
                                O00OO0OOOOO00O00O =O00O0OOO0OO000O0O ['message']#line:814
                                print (f'【获取种子】:{O00OO0OOOOO00O00O}')#line:815
                                return False #line:816
        except Exception as O0O0O0OOOO0O0OOOO :#line:817
            print (O0O0O0OOOO0O0OOOO )#line:818
    def synthetic (OOOO0O0OOOO000OO0 ):#line:821
        global id ,g #line:822
        try :#line:823
            O0OO000O00O0O00OO =OOOO0O0OOOO000OO0 .level_new ()#line:824
            OO0O00OO0OO00OOO0 =random .randint (9 ,11 )#line:825
            O00O0OO0OOO0OO000 =f'_site=8&targetSite={OO0O00OO0OO00OOO0}_{timi_new()}'#line:826
            O0000O0O0O00O000O ={'source':'scsc','authorization':OOOO0O0OOOO000OO0 .token ,'timestamp':timi_new (),'sign':sign (O00O0OO0OOO0OO000 ),'signstring':O00O0OO0OOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:837
            O0OOOOO00OOOO0000 ={"site":int (8 ),"targetSite":int (OO0O00OO0OO00OOO0 )}#line:838
            requests .request ('post',f'{host}/game/crops/move',headers =O0000O0O0O00O000O ,json =O0OOOOO00OOOO0000 )#line:839
            while True :#line:840
                O00OOO0O0O0OO0O00 =f'__{timi_new()}'#line:841
                OOO0O00OO000O0OOO ={'source':'scsc','authorization':OOOO0O0OOOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O0O0OO0O00 ),'signstring':O00OOO0O0O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:852
                OOOO000OOOO00000O =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00OO000O0OOO ).json ()#line:853
                if 'status'in OOOO000OOOO00000O :#line:855
                    if OOOO000OOOO00000O ['status']==200 :#line:856
                        O000O000OO0O00OO0 =OOOO000OOOO00000O ['data']['cropList']#line:857
                        O00O0O0O0O00OO00O =OOOO000OOOO00000O ['data']['gameCoreDataDBid']#line:858
                        OO0OO00O0OOOO00O0 =float (OOOO000OOOO00000O ['data']['silver'])/1000000000000 #line:859
                        OO0O0OO0000000000 =0 #line:864
                        for OO0OO0O00O0OO0O00 in O000O000OO0O00OO0 :#line:865
                            if not OO0OO0O00O0OO0O00 :#line:866
                                OOOOOO00OO000O000 =f'_crop_id={O00O0O0O0O00OO00O}&site={OO0O0OO0000000000}_{OOOO0O0OOOO000OO0.time}'#line:867
                                OOOO00O0O0O0OOO00 ={'source':'scsc','authorization':OOOO0O0OOOO000OO0 .token ,'timestamp':OOOO0O0OOOO000OO0 .time ,'sign':sign (OOOOOO00OO000O000 ),'signstring':OOOOOO00OO000O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:877
                                O0O00O0O0OO0O00OO ={"site":OO0O0OO0000000000 ,"crop_id":O00O0O0O0O00OO00O }#line:878
                                O00O0OOOOO00OO000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO00O0O0O0OOO00 ,data =O0O00O0O0OO0O00OO ).json ()#line:879
                                time .sleep (random .randint (1 ,3 )/10 )#line:881
                                if 'status'in O00O0OOOOO00OO000 :#line:882
                                    if O00O0OOOOO00OO000 ['status']==200 :#line:883
                                        if O00O0OOOOO00OO000 ['message']=='种子数量不足':#line:884
                                            O0OO000O00O0O00OO =OOOO0O0OOOO000OO0 .level_new ()#line:885
                                            print (f'【种植合成】:{O00O0OOOOO00OO000["message"]}')#line:886
                                            if not OOOO0O0OOOO000OO0 .user_ad ():#line:887
                                                return False #line:888
                                    if O00O0OOOOO00OO000 ['status']==500 :#line:889
                                        print (f'【种植合成】:{O00O0OOOOO00OO000["message"]}')#line:890
                                        return False #line:891
                            OO0O0OO0000000000 +=1 #line:892
                        OO0OOO0O000000OO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0O00OO000O0OOO ).json ()#line:893
                        OOOO00000OO0000OO =OO0OOO0O000000OO0 ['data']['cropList']#line:894
                        OOO0000O0O0OOO00O =False #line:895
                        for OO0OO0O00O0OO0O00 in range (12 ):#line:896
                            id =OOOO00000OO0000OO [OO0OO0O00O0OO0O00 ]['level']#line:897
                            if float (O0OO000O00O0O00OO )-float (id )>9 :#line:898
                                OO00O0O000O0OO000 =f'_site={OO0OO0O00O0OO0O00}_{timi_new()}'#line:899
                                OO0000O000O0OOOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO0O0OOOO000OO0 .token ,'timestamp':timi_new (),'sign':sign (OO00O0O000O0OO000 ),'signstring':OO00O0O000O0OO000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:910
                                O0OOOOO00OO00O00O ={"site":OO0OO0O00O0OO0O00 }#line:911
                                O0O0O00OOO0O00O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0000O000O0OOOOO ,data =O0OOOOO00OO00O00O ).json ()#line:913
                                if 'status'in O0O0O00OOO0O00O0O :#line:914
                                    if O0O0O00OOO0O00O0O ['status']==200 :#line:915
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:916
                            if id !=0 :#line:917
                                for OO0OO00O000O000O0 in range (11 ):#line:918
                                    O0OO0O000OOOO0OOO =OO0OO00O000O000O0 +1 #line:919
                                    g =OOOO00000OO0000OO [O0OO0O000OOOO0OOO ]['level']#line:920
                                    if id ==g :#line:921
                                        O00OOOOO0O00O0OOO =OO0OO00O000O000O0 +2 #line:922
                                        if O00OOOOO0O00O0OOO !=OO0OO0O00O0OO0O00 +1 :#line:923
                                            OO0OO0OO0OOOOOOOO =OO0OO0O00O0OO0O00 +1 #line:924
                                            time .sleep (random .randint (1 ,3 )/10 )#line:926
                                            O00O0OO0OOO0OO000 =f'_site={OO0OO0OO0OOOOOOOO - 1}&targetSite={O00OOOOO0O00O0OOO - 1}_{timi_new()}'#line:927
                                            O0000O0O0O00O000O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO0O0OOOO000OO0 .token ,'timestamp':timi_new (),'sign':sign (O00O0OO0OOO0OO000 ),'signstring':O00O0OO0OOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:944
                                            OOOO0O000000OOO00 ={"site":int (OO0OO0OO0OOOOOOOO -1 ),"targetSite":int (O00OOOOO0O00O0OOO -1 )}#line:945
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0000O0O0O00O000O ,json =OOOO0O000000OOO00 )#line:946
                                            OOO0000O0O0OOO00O =True #line:948
                                    if OOO0000O0O0OOO00O :#line:949
                                        break #line:950
                                if OOO0000O0O0OOO00O :#line:951
                                    break #line:952
        except :#line:953
            OOOO0O0OOOO000OO0 .synthetic ()#line:954
    def level_new (OOOOO000O000O0OOO ):#line:957
        try :#line:958
            OO000O00OO0O00000 =f'__{timi_new()}'#line:959
            O00O0O00OOOO0OOOO ={'source':'scsc','authorization':OOOOO000O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00OO0O00000 ),'signstring':OO000O00OO0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:970
            OOO0O0O00O00OOOO0 =requests .request ('get',f'{host}/user',headers =O00O0O00OOOO0OOOO ).json ()#line:971
            if 'status'in OOO0O0O00O00OOOO0 :#line:972
                if OOO0O0O00O00OOOO0 ['status']==200 :#line:973
                    return float (OOO0O0O00O00OOOO0 ['data']['level'])#line:974
        except Exception as O000O0O00OOO0000O :#line:975
            print (O000O0O00OOO0000O )#line:976
    def propsraffle (OO0O00OO0000000O0 ):#line:979
        try :#line:980
            while True :#line:981
                O0OO0OO0OO0000O00 =f'__{timi_new()}'#line:982
                O000O0O0OOOO0O00O ={'source':'scsc','authorization':OO0O00OO0000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OO0OO0000O00 ),'signstring':O0OO0OO0OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:993
                O0000O0O0O00000OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000O0O0OOOO0O00O ).json ()#line:994
                if 'status'in O0000O0O0O00000OO :#line:996
                    if O0000O0O0O00000OO ['status']==200 :#line:997
                        O00O00OO000O00OOO =O0000O0O0O00000OO ['data']['rows']#line:998
                        O0OO0000OO00O0OOO =O0000O0O0O00000OO ['data']['vstate']#line:999
                        if O00O00OO000O00OOO ==5 or O00O00OO000O00OOO ==6 or O00O00OO000O00OOO ==7 :#line:1000
                            O00O00O00O0O0OOOO =O0000O0O0O00000OO ['data']['silver']#line:1001
                            print (f'【转盘抽奖】:获得种子:{O00O00O00O0O0OOOO}')#line:1002
                        if O00O00OO000O00OOO ==1 or O00O00OO000O00OOO ==2 or O00O00OO000O00OOO ==3 :#line:1003
                            O000OOO00OOO0OO0O =O0000O0O0O00000OO ['data']['clover']#line:1004
                            print (f'【转盘抽奖】:获得三叶草:{O000OOO00OOO0OO0O}')#line:1005
                        if O00O00OO000O00OOO ==4 or O00O00OO000O00OOO ==8 :#line:1006
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1007
                        if O00O00OO000O00OOO =='抽奖次数已用完':#line:1011
                            break #line:1045
                time .sleep (random .randint (8 ,15 )/10 )#line:1046
        except Exception as O0OO00O00O0OOOO0O :#line:1047
            print (O0OO00O00O0OOOO0O )#line:1048
    def friends_invitation (OO00O00000OOOO0OO ):#line:1051
        try :#line:1052
            O000OO00OO000OOOO =f'__{timi_new()}'#line:1053
            O0OOO0000OOOOOOO0 ={'source':'scsc','authorization':OO00O00000OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OO000OOOO ),'signstring':O000OO00OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1064
            O0OOOO000OOO00O0O =requests .request ('get',f'{host}/friends',headers =O0OOO0000OOOOOOO0 ).json ()#line:1065
            if 'status'in O0OOOO000OOO00O0O :#line:1066
                if O0OOOO000OOO00O0O ['status']==200 :#line:1067
                    OOOO000OO00OO0OOO =O0OOOO000OOO00O0O ['data']['myInviteter']#line:1068
                    if OOOO000OO00OO0OOO :#line:1069
                        O0O0OOOOOOOOOOOOO =OOOO000OO00OO0OOO ['user']['nickname']#line:1070
                        OO0O00O00OO0OOO0O =OO00O00000OOOO0OO .certification ()#line:1071
                        if OO0O00O00OO0OOO0O =='未实名':#line:1072
                            weishim .append (OO00O00000OOOO0OO .token )#line:1073
                        print (f'【查邀请人】:我的邀请人:{O0O0OOOOOOOOOOOOO}丨实名:{OO0O00O00OO0OOO0O}')#line:1074
                    else :#line:1075
                        if OO00O00000OOOO0OO .innerId !='0':#line:1076
                            OO00O00000OOOO0OO .invitation ()#line:1077
        except Exception as OOOOOOO0O000OO0OO :#line:1078
            print (OOOOOOO0O000OO0OO )#line:1079
    def add_clover (O0O0O00O00OO0OOOO ):#line:1082
        global golden_seed #line:1083
        try :#line:1084
            O0O0OO0O0OO0O0O0O =f'__{timi_new()}'#line:1085
            OOO0OO00O00000O0O ={'source':'scsc','authorization':O0O0O00O00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OO0O0O0O ),'signstring':O0O0OO0O0OO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1096
            OOOOOO00000OO0O0O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0OO00O00000O0O ).json ()#line:1097
            if 'status'in OOOOOO00000OO0O0O :#line:1099
                if OOOOOO00000OO0O0O ['status']==200 :#line:1100
                    OOO0000OOO0000000 =OOOOOO00000OO0O0O ['data']['clover']#line:1101
                    OOO0O00000OO0000O =OOOOOO00000OO0O0O ['data']['used_clover']#line:1102
                    OOOO000000OOOO000 =float (OOO0000OOO0000000 )-float (OOO0O00000OO0000O )#line:1103
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0O00000OO0000O}')#line:1104
                    if O0O0O00O00OO0OOOO .certification ()!='未实名':#line:1105
                        if OOOO000000OOOO000 >1 :#line:1106
                            O0O0OO0O0OO0O0O0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOO000000OOOO000)}_{timi_new()}'#line:1107
                            O00O0OOO0OOOOOOOO ={'source':'scsc','authorization':O0O0O00O00OO0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OO0O0O0O ),'signstring':O0O0OO0O0OO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1118
                            OO0O000OOOOOO0O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOO000000OOOO000 )}#line:1119
                            O0OO0O00000OOO00O =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O0OOO0OOOOOOOO ,data =OO0O000OOOOOO0O00 ).json ()#line:1120
                            if 'status'in O0OO0O00000OOO00O :#line:1122
                                if O0OO0O00000OOO00O ['status']==200 :#line:1123
                                    print (f'【参与抽奖】:添加☘️:{O0OO0O00000OOO00O["data"]["isSuccess"]}丨数量:{OOOO000000OOOO000}')#line:1124
                                if O0OO0O00000OOO00O ['status']==500 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{O0OO0O00000OOO00O["message"]}')#line:1126
            OOOO0OO00OOOOOOO0 =requests .request ('get',f'{host}/lottery',headers =OOO0OO00O00000O0O ).json ()#line:1127
            O0O00000O00000OOO =O0O0O00O00OO0OOOO .winning_rewards ()#line:1129
            if 'status'in OOOO0OO00OOOOOOO0 :#line:1130
                if OOOO0OO00OOOOOOO0 ['status']==200 :#line:1131
                    O0O00O0O00OOOO000 =OOOO0OO00OOOOOOO0 ['data'][0 ]['day_get_gold_quantity']#line:1132
                    golden_seed +=float (O0O00O0O00OOOO000 )#line:1133
                    OOOO0O000O0OO0OOO =OOOO0OO00OOOOOOO0 ['data'][1 ]['value']#line:1134
                    O00O0OO0O000000OO =OOOO0OO00OOOOOOO0 ['data'][0 ]['join_number']#line:1135
                    OOO0OOO0O0000OO00 =int (float (OOOO0OO00OOOOOOO0 ['data'][0 ]['totalValue']))#line:1136
                    O0O00000OO0O0OO0O =float (OOOO0O000O0OO0OOO /OOO0OOO0O0000OO00 )*10000 #line:1137
                    O00OO0OO0O0O000OO =OOO0OOO0O0000OO00 /O00O0OO0O000000OO #line:1138
                    print (f'【参与抽奖】:预计每天中{str(O0O00O0O00OOOO000)[:6]}颗金种子丨好友收益:{str(O0O00000O00000OOO)[:6]}')#line:1139
                    print (f'【抽奖统计】:每1万☘️中{str(O0O00000OO0O0OO0O)[:6]}颗金种子丨☘️人均:{str(O00OO0OO0O0O000OO)[:7]}️')#line:1140
        except Exception as O0OOO00O00000OOO0 :#line:1141
            print (O0OOO00O00000OOO0 )#line:1142
    def energy (OOO00OOO000OOO0O0 ):#line:1145
        try :#line:1146
            while True :#line:1147
                O00000O0000O0000O =f'__{timi_new()}'#line:1148
                OO0OOOOO00O0O0OO0 ={'source':'scsc','authorization':OOO00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0000O0000O ),'signstring':O00000O0000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1159
                OOOO00OO0OO00OO0O =requests .request ('get',f'{host}/energy/general',headers =OO0OOOOO00O0O0OO0 ).json ()#line:1160
                if 'status'in OOOO00OO0OO00OO0O :#line:1162
                    if OOOO00OO0OO00OO0O ['status']==200 :#line:1163
                        OOOO0O0000O0O00O0 =OOOO00OO0OO00OO0O ['data']['ordinary_water']#line:1164
                        O00OO000OOO00O0O0 =OOOO00OO0OO00OO0O ['data']['ordinary_fertilizer']#line:1165
                        O00OO0OOO000000O0 =OOOO00OO0OO00OO0O ['data']['videoStatus']#line:1166
                        O00OOO00O0O0OOO00 =OOOO00OO0OO00OO0O ['data']['waterVideoKey']#line:1167
                        print (f'【我的营养】:肥料:{str(O00OO000OOO00O0O0).split(".")[0]}丨水滴:{str(OOOO0O0000O0O00O0).split(".")[0]}')#line:1169
                        if float (O00OO000OOO00O0O0 )<96 :#line:1170
                            if O00OO0OOO000000O0 :#line:1171
                                time .sleep (random .randint (160 ,180 )/10 )#line:1172
                                O0O0OOOO00OOOO0OO =99 -float (O00OO000OOO00O0O0 )#line:1173
                                O00OOO0O000OOOOO0 ={"fertilizer":str (O0O0OOOO00OOOO0OO ).split ('.')[0 ]}#line:1174
                                OOOO00OO0O0O0000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0OOOOO00O0O0OO0 ).json ()#line:1176
                                if 'status'in OOOO00OO0O0O0000O :#line:1178
                                    if OOOO00OO0O0O0000O ['status']==200 :#line:1179
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO00OO0O0O0000O["message"]}')#line:1180
                                    if OOOO00OO0O0O0000O ['status']==500 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO00OO0O0O0000O["message"]}')#line:1182
                                        break #line:1183
                                if float (O00OO000OOO00O0O0 )<78 :#line:1185
                                    O0O0OOOO00OOOO0OO =80 -float (O00OO000OOO00O0O0 )#line:1186
                                    O0O0O000O00OO0OO0 =f'_fertilizer={int(O0O0OOOO00OOOO0OO)}_{timi_new()}'#line:1187
                                    O00O00O0OOOO0OOO0 ={'source':'scsc','authorization':OOO00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00OO0OO0 ),'signstring':O0O0O000O00OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1198
                                    O000OOO000000O0O0 ={"fertilizer":int (O0O0OOOO00OOOO0OO )}#line:1199
                                    OOO0OO0OOOOO0OO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00O00O0OOOO0OOO0 ,data =O000OOO000000O0O0 ).json ()#line:1201
                                    if 'status'in OOO0OO0OOOOO0OO00 :#line:1203
                                        if OOO0OO0OOOOO0OO00 ['status']==200 :#line:1204
                                            print (f'【购买肥料】:购买肥料:{OOO0OO0OOOOO0OO00["message"]}丨数量:{int(O0O0OOOO00OOOO0OO)}')#line:1205
                                        if OOO0OO0OOOOO0OO00 ['status']==500 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OOO0OO0OOOOO0OO00["message"]}丨数量:{int(O0O0OOOO00OOOO0OO)}')#line:1207
                                            O0O0OOOOO0O00OOO0 =OOO0OO0OOOOO0OO00 ["message"].split ('-')[1 ]#line:1208
                                            O0OO0O0O00OO0OO0O =f'__{timi_new()}'#line:1209
                                            OO0O00OO000O00O00 ={'source':'scsc','authorization':OOO00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O00OO0OO0O ),'signstring':O0OO0O0O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                            O0OOOO0O000OOOO00 =requests .request ('get',f'{host}/user',headers =OO0O00OO000O00O00 ).json ()#line:1221
                                            if 'status'in O0OOOO0O000OOOO00 :#line:1222
                                                if O0OOOO0O000OOOO00 ['status']==200 :#line:1223
                                                    OOO00OOO00O0OO0OO =O0OOOO0O000OOOO00 ['data']['inner_id']#line:1224
                                                    if give_gold (OOO00OOO00O0OO0OO ,float (O0O0OOOOO0O00OOO0 )+1 ):#line:1225
                                                        OOO00OOO000OOO0O0 .energy ()#line:1226
                        if float (OOOO0O0000O0O00O0 )<880 :#line:1227
                            if O00OOO00O0O0OOO00 :#line:1228
                                time .sleep (random .randint (160 ,180 )/10 )#line:1229
                                O000OOO00000OOOOO =999 -float (OOOO0O0000O0O00O0 )#line:1230
                                O00OOO00O000O0O00 ={"water":str (O000OOO00000OOOOO ).split ('.')[0 ]}#line:1231
                                OO0OO0O000O00OOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0OOOOO00O0O0OO0 ).json ()#line:1233
                                if 'status'in OO0OO0O000O00OOO0 :#line:1235
                                    if OO0OO0O000O00OOO0 ['status']==200 :#line:1236
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO0O000O00OOO0["message"]}')#line:1237
                                    if OO0OO0O000O00OOO0 ['status']==500 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO0O000O00OOO0["message"]}')#line:1239
                                        break #line:1240
                                if float (OOOO0O0000O0O00O0 )<780 :#line:1241
                                    O000OOO00000OOOOO =800 -float (OOOO0O0000O0O00O0 )#line:1242
                                    OOOO0O00O0O0OO00O =f'_water={int(O000OOO00000OOOOO)}_{timi_new()}'#line:1243
                                    O000O0OOOOO000O0O ={'source':'scsc','authorization':OOO00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O00O0O0OO00O ),'signstring':OOOO0O00O0O0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1254
                                    OO000O0OO0O0OOO0O ={"water":int (O000OOO00000OOOOO )}#line:1255
                                    O0OOOO0O0O0O000OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000O0OOOOO000O0O ,data =OO000O0OO0O0OOO0O ).json ()#line:1257
                                    if 'status'in O0OOOO0O0O0O000OO :#line:1259
                                        if O0OOOO0O0O0O000OO ['status']==200 :#line:1260
                                            print (f'【购买水滴】:购买水滴:{O0OOOO0O0O0O000OO["message"]}丨数量:{int(O000OOO00000OOOOO)}')#line:1261
                                        if O0OOOO0O0O0O000OO ['status']==500 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O0OOOO0O0O0O000OO["message"]}丨数量:{int(O000OOO00000OOOOO)}')#line:1263
                                            O0O0OOOOO0O00OOO0 =O0OOOO0O0O0O000OO ["message"].split ('-')[1 ]#line:1264
                                            O0OO0O0O00OO0OO0O =f'__{timi_new()}'#line:1265
                                            OO0O00OO000O00O00 ={'source':'scsc','authorization':OOO00OOO000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O00OO0OO0O ),'signstring':O0OO0O0O00OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1276
                                            O0OOOO0O000OOOO00 =requests .request ('get',f'{host}/user',headers =OO0O00OO000O00O00 ).json ()#line:1277
                                            if 'status'in O0OOOO0O000OOOO00 :#line:1278
                                                if O0OOOO0O000OOOO00 ['status']==200 :#line:1279
                                                    OOO00OOO00O0OO0OO =O0OOOO0O000OOOO00 ['data']['inner_id']#line:1280
                                                    if give_gold (OOO00OOO00O0OO0OO ,float (O0O0OOOOO0O00OOO0 )+1 ):#line:1281
                                                        OOO00OOO000OOO0O0 .energy ()#line:1282
                        break #line:1283
        except Exception as OOOO00OO0OO0OOOO0 :#line:1284
            print (OOOO00OO0OO0OOOO0 )#line:1285
def bundled_def ():#line:1288
    OOOOO0O0OOO0OOO0O =['5570536','7750212','7911652','7911680','7805624']#line:1289
    return OOOOO0O0OOO0OOO0O [random .randint (0 ,len (OOOOO0O0OOO0OOO0O )-1 )]#line:1290
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
        O000OOOO0OOOOO0O0 =gitee_edition ()#line:1329
        if version_of_the_validation ()<O000OOOO0OOOOO0O0 ['CityEarth']['edition']:#line:1330
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOOO0OOOOO0O0["CityEarth"]["edition"]}   ❌')#line:1331
            print (f'更新内容=>>{O000OOOO0OOOOO0O0["CityEarth"]["content"]}')#line:1332
        else :#line:1333
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000OOOO0OOOOO0O0["CityEarth"]["edition"]}   ✅')#line:1334
            print (f'更新内容=>> {O000OOOO0OOOOO0O0["CityEarth"]["content"]}')#line:1335
    except Exception as O0OOO0O0OO0OOOO0O :#line:1336
        print (O0OOO0O0OO0OOOO0O )#line:1337
def sc3 ():#line:1340
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1341
if __name__ =='__main__':#line:1344
    start ()#line:1345
