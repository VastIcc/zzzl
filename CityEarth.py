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
@ 版本  3.9
"""
##################################配置区##################################
time_xx = random.randint(12, 15)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
invited_new =[]#line:6
weishim =[]#line:7
def start ():#line:10
    try :#line:11
        O000OO000O0O00OOO00 ()#line:12
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:13
        O000OO0O00OO00O00 ()#line:14
        OOOOOO0O0O0O000OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OOOOOO0O0O0O000OO)}个账号==========")#line:16
        for OO00OO0OOOO0OOO0O in OOOOOO0O0O0O000OO :#line:17
            OOO00OO00000O0OO0 =[]#line:18
            print (f"------------正在执行第{OOOOOO0O0O0O000OO.index(OO00OO0OOOO0OOO0O) + 1}个账号------------")#line:19
            O00O00O00OO0O0O00 =CityEarth (OO00OO0OOOO0OOO0O ,OOO00OO00000O0OO0 ,OOOOOO0O0O0O000OO .index (OO00OO0OOOO0OOO0O ))#line:20
            def O0000O0O00O0O00OO ():#line:22
                if O00O00O00OO0O0O00 .base_info ():#line:24
                    O00O00O00OO0O0O00 .sealing ()#line:26
                    O00O00O00OO0O0O00 .invitenum ()#line:28
                    O00O00O00OO0O0O00 .query_to_sell ()#line:30
                    O00O00O00OO0O0O00 .game_map ()#line:32
                    O00O00O00OO0O0O00 .friends_invitation ()#line:34
                    O00O00O00OO0O0O00 .energy ()#line:36
                    O00O00O00OO0O0O00 .add_clover ()#line:38
                    O00O00O00OO0O0O00 .propsraffle ()#line:40
                    O00O00O00OO0O0O00 .synthetic ()#line:42
                    O00O00O00OO0O0O00 .crops_illustrated ()#line:44
                    O00O00O00OO0O0O00 .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        O00O00O00OO0O0O00 .give_gold ()#line:49
            OOOO000000000O0O0 =threading .Thread (target =O0000O0O00O0O00OO )#line:51
            OOOO000000000O0O0 .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理推送通知------------")#line:54
        time .sleep (0.5 )#line:55
        OOOOO00OO00OO0O00 =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOOO00OO00OO0O00 +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for O0OO00O0000OOO000 in invited_new :#line:60
            print (O0OO00O0000OOO000 )#line:61
        print ('开始打印未实名的token')#line:62
        for OOO0OO00O000O00O0 in weishim :#line:63
            print (OOO0OO00O000O00O0 )#line:64
    except Exception as OO0OOO0000OO0OO0O :#line:65
        print (OO0OOO0000OO0OO0O )#line:66
def give_gold (OOO0O0O00O00O0O00 ,OO00O0O00OOOOO0O0 ):#line:70
    try :#line:71
        OOOO00O00OO00000O =f'_doneeNo={OOO0O0O00O00O0O00}&quantity={int(OO00O0O00OOOOO0O0)}_{timi_new()}'#line:72
        OOOO0000OO0OOO0O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO00O00OO00000O ),'signstring':OOOO00O00OO00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOO0O0OOO00OO000O ={"quantity":int (OO00O0O00OOOOO0O0 ),"doneeNo":OOO0O0O00O00O0O00 }#line:87
        OOO00OO00O0OOOOO0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0000OO0OOO0O0 ,data =OOO0O0OOO00OO000O ).json ()#line:88
        if 'status'in OOO00OO00O0OOOOO0 :#line:90
            if OOO00OO00O0OOOOO0 ['status']==200 :#line:91
                if OOO00OO00O0OOOOO0 ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OO00O0O00OOOOO0O0)}种子给{OOO0O0O00O00O0O00}成功')#line:93
                    return True #line:94
            if OOO00OO00O0OOOOO0 ['status']==401 :#line:95
                print (f'【赠送种子】:{OOO00OO00O0OOOOO0["message"]}')#line:96
                return False #line:97
            if OOO00OO00O0OOOOO0 ['status']==500 :#line:98
                print (f'【赠送种子】:{OOO00OO00O0OOOOO0["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as OOOOO0O000O0O0OO0 :#line:102
        print (OOOOO0O000O0O0OO0 )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def sign (OOOO000000O0000OO ):#line:110
    OOO0O00OOO000O0O0 =hashlib .md5 (OOOO000000O0000OO .encode ()).hexdigest ()#line:111
    O0O0OO00O00O0O00O =sc1 ()#line:112
    OO0OOO0OO0OO00O0O =sc2 ()#line:113
    O0O0OO000OO00O00O =sc3 ()#line:114
    O0000O000OOO0OO00 =O0O0OO00O00O0O00O +OOO0O00OOO000O0O0 +OO0OOO0OO0OO00O0O +O0O0OO000OO00O00O #line:115
    O0O000OOOO0O0OO0O =hashlib .md5 (O0000O000OOO0OO00 .encode ()).hexdigest ()#line:116
    return O0O000OOOO0O0OO0O #line:117
def format_msg ():#line:120
    OOO00O0O0000OO0O0 =""#line:121
    for O0OOO0OO000O0000O in msg_list :#line:122
        OOO00O0O0000OO0O0 +=str (O0OOO0OO000O0000O )+"\r\n"#line:123
    return OOO00O0O0000OO0O0 #line:124
def sc1 ():#line:127
    return "scsc%^&*"#line:128
def O000OO0O00OO00O00 ():#line:131
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:132
        pass #line:133
    else :#line:134
        exit (1 )#line:135
def timi_new ():#line:138
    return str (int (time .time ()*1000 ))#line:139
json_path ="CityEarth_data.json"#line:142
json_path1 ="CityEarth_data.json"#line:143
dict ={}#line:144
def get_json_data (O00O0OOO00O0O0O0O ,OO00O0O0OOO000OO0 ,O0O0OO00O0OOO00OO ,O0OO0OOOOOO0OOOO0 ):#line:147
    with open (O00O0OOO00O0O0O0O ,'rb')as OOO0O00O00OOO0OOO :#line:148
        O00OOO0OO000OO0O0 =json .load (OOO0O00O00OOO0OOO )#line:149
        O00OOO0OO000OO0O0 ['data'][OO00O0O0OOO000OO0 ][O0O0OO00O0OOO00OO ]=O0OO0OOOOOO0OOOO0 #line:150
        O0O0OO0O00OOOOO0O =O00OOO0OO000OO0O0 #line:151
    OOO0O00O00OOO0OOO .close ()#line:152
    return O0O0OO0O00OOOOO0O #line:153
def write_json_data (O00O0O00O0O0OO000 ):#line:156
    with open (json_path1 ,'w')as OOOOO000O0OOOO00O :#line:157
        json .dump (O00O0O00O0O0OO000 ,OOOOO000O0OOOO00O )#line:158
    OOOOO000O0OOOO00O .close ()#line:159
    return True #line:160
class CityEarth :#line:163
    def __init__ (OO0OOOO0OO00OO0O0 ,OOO0OO000O00000O0 ,O00O0000000O0O0OO ,O000OOO00O00OO0OO ):#line:165
        try :#line:166
            OO0OOOO0OO00OO0O0 .msg =O00O0000000O0O0OO #line:167
            OO0OOOO0OO00OO0O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:168
            OO0OOOO0OO00OO0O0 .token =OOO0OO000O00000O0 ['authorization']#line:169
            OO0OOOO0OO00OO0O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:170
            OO0OOOO0OO00OO0O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:171
            OO0OOOO0OO00OO0O0 .elephant_user =OOO0OO000O00000O0 ['elephant_user']#line:172
            OO0OOOO0OO00OO0O0 .elephant_pswd =OOO0OO000O00000O0 ['elephant_pswd']#line:173
            OO0OOOO0OO00OO0O0 .elephant_Task_ID =OOO0OO000O00000O0 ['elephant_Task_ID']#line:174
            OO0OOOO0OO00OO0O0 .len_new =O000OOO00O00OO0OO #line:175
        except :#line:176
            print ('变量格式错误')#line:177
    def base_info (O0000OOOO0OOOOOO0 ):#line:180
        try :#line:181
            O0000OOOO0OOOOOO0 .watched_ad ()#line:183
            OOO000O0O0O0OO0OO =f'__{timi_new()}'#line:184
            O000O0000OO00000O ={'source':'scsc','authorization':O0000OOOO0OOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O0O0OO0OO ),'signstring':OOO000O0O0O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
            O000000O0000OOO00 =requests .request ('get',f'{host}/user',headers =O000O0000OO00000O ).json ()#line:196
            if 'status'in O000000O0000OOO00 :#line:198
                if O000000O0000OOO00 ['status']==200 :#line:199
                    O00OOO00OOO0OOO0O =O000000O0000OOO00 ['data']['nickname']#line:200
                    OO00000000OOOO000 =O000000O0000OOO00 ['data']['inner_id']#line:201
                    O0OO0OO00O0OO0OO0 =O000000O0000OOO00 ['data']['assets']['gold']#line:202
                    O0O0OO000OOOOOO0O =O000000O0000OOO00 ['data']['level']#line:203
                    print (f'【账号信息】:昵称:{O00OOO00OOO0OOO0O[:5]}丨ID:{OO00000000OOOO000}丨等级:{O0O0OO000OOOOOO0O}丨金种子:{str(O0OO0OO00O0OO0OO0).split(".")[0]}')#line:205
                    if 'wx_'in O00OOO00OOO0OOO0O :#line:206
                        O0000OOOO0OOOOOO0 .change_nickname ()#line:207
                if O000000O0000OOO00 ['status']==401 :#line:208
                    print ('【账号信息】:账号失效正在尝试登录')#line:209
                    if O0000OOOO0OOOOOO0 .elephant_user =='f':#line:210
                        return False #line:211
                    O0O0O0O00O0OOO0O0 =Invalid_login .addtask (elephant_user =O0000OOOO0OOOOOO0 .elephant_user ,elephant_pswd =O0000OOOO0OOOOOO0 .elephant_pswd ,elephant_Task_ID =O0000OOOO0OOOOOO0 .elephant_Task_ID )#line:214
                    OO00O0OOO000OOO00 =get_json_data (json_path ,O0000OOOO0OOOOOO0 .len_new ,'authorization',O0O0O0O00O0OOO0O0 )#line:215
                    if write_json_data (OO00O0OOO000OOO00 ):#line:216
                        print ('正在写入账号配置文件')#line:217
                    return False #line:218
                if O000000O0000OOO00 ['status']==500 :#line:219
                    return False #line:220
            return True #line:221
        except Exception as OOO0O0O000OOO000O :#line:222
            print (OOO0O0O000OOO000O )#line:223
    def sealing (OOO0O0O0O0000000O ):#line:226
        try :#line:227
            OO0OO00OOO0OO000O =f'__{timi_new()}'#line:228
            OO00O0O00OO0OOOO0 ={'source':'scsc','authorization':OOO0O0O0O0000000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00OOO0OO000O ),'signstring':OO0OO00OOO0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O0O00OO0OOOO0 )#line:240
            requests .request ('get',f'{host}/packsack/list',headers =OO00O0O00OO0OOOO0 )#line:241
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O0O00OO0OOOO0 )#line:242
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O0O00OO0OOOO0 )#line:243
            requests .request ('get',f'{host}/user',headers =OO00O0O00OO0OOOO0 )#line:244
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O0O00OO0OOOO0 )#line:245
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O0O00OO0OOOO0 )#line:246
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O0O00OO0OOOO0 )#line:247
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O0O00OO0OOOO0 )#line:248
            requests .request ('get',f'{host}/assets',headers =OO00O0O00OO0OOOO0 )#line:249
        except Exception as OO00O0OOO00O00OOO :#line:250
            print (OO00O0OOO00O00OOO )#line:251
    def the_query (OO0O00O0O0000O000 ):#line:254
        try :#line:255
            O0OOO00OO00O0OO00 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:256
            OO00OOOOO0OO0OOO0 ={'authorization':OO0O00O0O0000O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OO00O0OO00 ),'signstring':O0OOO00OO00O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            O0000O0O0O00OO0O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00OOOOO0OO0OOO0 ).json ()#line:268
            if 'status'in O0000O0O0O00OO0O0 :#line:270
                if O0000O0O0O00OO0O0 ['status']==200 :#line:271
                    O00OO0O0OO0O0OOOO =O0000O0O0O00OO0O0 ['data']['rows'][3 ]['price']#line:272
                    OO0O00O0O0000O000 .market_sale (O00OO0O0OO0O0OOOO )#line:273
        except Exception as O0O00OO000O000O00 :#line:274
            print (O0O00OO000O000O00 )#line:275
    def market_sale (OO0O0O00OO0000OO0 ,OO00OOO0OOOO000OO ):#line:278
        try :#line:279
            OO0O00OO00000OO00 =timi_new ()#line:280
            O00O0OOOOO0OOOO0O =f'type=crop__{OO0O00OO00000OO00}'#line:281
            O0O0O0O0OOOOO0OOO ={'source':'scsc','authorization':OO0O0O00OO0000OO0 .token ,'timestamp':str (OO0O00OO00000OO00 ),'sign':sign (O00O0OOOOO0OOOO0O ),'signstring':O00O0OOOOO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            O000O00O00OOOOO00 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O0O0OOOOO0OOO ).json ()#line:294
            if 'status'in O000O00O00OOOOO00 :#line:296
                if O000O00O00OOOOO00 ['status']==200 :#line:297
                    if O000O00O00OOOOO00 ['data']['rows']:#line:298
                        OO0O00OOO00O00O00 =O000O00O00OOOOO00 ['data']['rows'][0 ]['packsackItemId']#line:299
                        O0O0O0OO000O0000O =O000O00O00OOOOO00 ['data']['rows'][0 ]['quantity']#line:300
                        OOOO0O0OOO0O000O0 =float (OO00OOO0OOOO000OO )+float (random .randint (1 ,99 )*0.001 )#line:301
                        O00OO0O000000O0OO =f'_packsackItemId={OO0O00OOO00O00O00}&price={str(OOOO0O0OOO0O000O0)[:7]}&quantity={O0O0O0OO000O0000O}_{OO0O00OO00000OO00}'#line:302
                        O0O0OO000O0O0000O ={'source':'scsc','authorization':OO0O0O00OO0000OO0 .token ,'timestamp':str (OO0O00OO00000OO00 ),'sign':sign (O00OO0O000000O0OO ),'signstring':O00OO0O000000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                        OO0O0O00000OO00O0 ={"packsackItemId":OO0O00OOO00O00O00 ,"price":str (OOOO0O0OOO0O000O0 )[:7 ],"quantity":str (O0O0O0OO000O0000O )}#line:318
                        O0OOO0O0O0OO0000O =requests .request ('post',f'{host}/market/sale',headers =O0O0OO000O0O0000O ,data =OO0O0O00000OO00O0 ).json ()#line:319
                        if 'status'in O0OOO0O0O0OO0000O :#line:321
                            if O0OOO0O0O0OO0000O ['status']==200 :#line:322
                                print (f'【上架芦荟】:数量:{O0O0O0OO000O0000O}丨价格:{str(OOOO0O0OOO0O000O0)[:7]}')#line:323
        except Exception as O000OOOOO0OOO00OO :#line:324
            print (O000OOOOO0OOO00OO )#line:325
    def query_to_sell (OO0000O00000O00O0 ):#line:328
        try :#line:329
            OO0OO0O000OOO0OOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:330
            OOO0OO0O00O0O0OO0 ={'source':'scsc','authorization':OO0000O00000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O000OOO0OOO ),'signstring':OO0OO0O000OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
            O0O00000000O0O00O =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0OO0O00O0O0OO0 ).json ()#line:343
            if 'status'in O0O00000000O0O00O :#line:345
                if O0O00000000O0O00O ['status']==200 :#line:346
                    for O0O0OOOOO000OOO00 in O0O00000000O0O00O ['data']['rows']:#line:347
                        OO00O0O0OOO0O0000 =O0O0OOOOO000OOO00 ['materialKey']#line:348
                        O0OOOOO0OOOO00O00 =O0O0OOOOO000OOO00 ['quantity']#line:349
                        OOOOOOO0O000000OO =O0O0OOOOO000OOO00 ['price']#line:350
                        O00OOO00O0OO0O0OO =O0O0OOOOO000OOO00 ['saleState']#line:351
                        if O00OOO00O0OO0O0OO ==0 :#line:352
                            print (f'【出售订单】:名称:{OO00O0O0OOO0O0000}丨数量:{O0OOOOO0OOOO00O00}丨价格:{OOOOOOO0O000000OO}')#line:353
                            O00OO00OO0O0OOOO0 =O0O0OOOOO000OOO00 ['id']#line:354
                            OO0000O00000O00O0 .cacel_sale (O00OO00OO0O0OOOO0 )#line:355
        except Exception as OO0OO0OOO0O0OO000 :#line:356
            print (OO0OO0OOO0O0OO000 )#line:357
    def cacel_sale (OO00O0O000O00OOOO ,O000O0000O00OO0O0 ):#line:360
        try :#line:361
            O0O0OOO0O0OOO00OO =f'_saleId={O000O0000O00OO0O0}_{timi_new()}'#line:362
            O000OO0OO000OO00O ={'source':'scsc','authorization':OO00O0O000O00OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O0OOO00OO ),'signstring':O0O0OOO0O0OOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:373
            O00OO0O0O0OOO000O ={"saleId":O000O0000O00OO0O0 }#line:376
            OO00OOO0OOOO0O0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O000OO0OO000OO00O ,data =O00OO0O0O0OOO000O ).json ()#line:377
            if 'status'in OO00OOO0OOOO0O0OO :#line:379
                if OO00OOO0OOOO0O0OO ['status']==200 :#line:380
                    print (f'【下架出售】:{OO00OOO0OOOO0O0OO["data"]}')#line:381
        except Exception as OO00000O00O0OOOOO :#line:382
            print (OO00000O00O0OOOOO )#line:383
    def change_nickname (OO0O0OOOOOOOO0000 ):#line:386
        try :#line:387
            OO0OOO0O0OO000000 =timi_new ()#line:388
            OO0OO0O00O0OO0O0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:389
            OOOO000OO0O0OO00O =requests .request ('post','https://www.qmsjmfb.com/',data =OO0OO0O00O0OO0O0O ).text #line:390
            OOOO000O00O0O00OO =re .findall ('<ul><li>(.*?)</li>',OOOO000OO0O0OO00O )[0 ][:3 ]#line:391
            OOO0OOO0OO00O0000 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOOO000O00O0O00OO}').json ()#line:392
            O0OO0OOOOOOOO00OO =OOO0OOO0OO00O0000 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:393
            OOO0OO00OO0OO00O0 ={"nickname":O0OO0OOOOOOOO00OO }#line:394
            OO00O0OOOOO0OOOO0 =f'_nickname={O0OO0OOOOOOOO00OO}_{OO0OOO0O0OO000000}'#line:395
            OOO00OOOO0O000OO0 ={'source':'scsc','authorization':OO0O0OOOOOOOO0000 .token ,'timestamp':OO0OOO0O0OO000000 ,'sign':sign (OO00O0OOOOO0OOOO0 ),'signstring':OO00O0OOOOO0OOOO0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:406
            O0000O0000OOOO00O =requests .request ('patch',f'{host}/user/nickname',headers =OOO00OOOO0O000OO0 ,data =OOO0OO00OO0OO00O0 ).json ()#line:407
            if 'status'in O0000O0000OOOO00O :#line:409
                if O0000O0000OOOO00O ['status']==200 :#line:410
                    print (f'【修改网名】:网名:{O0OO0OOOOOOOO00OO}丨{O0000O0000OOOO00O["message"]}')#line:411
        except Exception as OOOO0000O0OO0OO00 :#line:412
            print (OOOO0000O0OO0OO00 )#line:413
    def withdraw (OO0000OO0000O00O0 ):#line:416
        try :#line:417
            OO0OO0O0O0000O0O0 =f'__{timi_new()}'#line:418
            O00000OOOO00O0OO0 ={'source':'scsc','authorization':OO0000OO0000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O0000O0O0 ),'signstring':OO0OO0O0O0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            O000O00000O0000OO =requests .request ('get',f'{host}/assets',headers =O00000OOOO00O0OO0 ).json ()#line:430
            if 'status'in O000O00000O0000OO :#line:432
                if O000O00000O0000OO ['status']==200 :#line:433
                    O00OO00OOO0OO0O00 =O000O00000O0000OO ['data']['cash']#line:434
                    if float (O00OO00OOO0OO0O00 )>20 :#line:435
                        OO0OO0O0O0000O0O0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:436
                        O00000OOOO00O0OO0 ={'authorization':OO0000OO0000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0O0000O0O0 ),'signstring':OO0OO0O0O0000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:446
                        O0000O0000O0O00OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:447
                        OOO0O0O0O000OOOOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00000OOOO00O0OO0 ,data =O0000O0000O0O00OO ).json ()#line:449
                        if 'status'in OOO0O0O0O000OOOOO :#line:451
                            if OOO0O0O0O000OOOOO ['status']==200 :#line:452
                                print (f'【余额提现】:{OOO0O0O0O000OOOOO["data"]}')#line:453
                        if 'status'in OOO0O0O0O000OOOOO :#line:454
                            if OOO0O0O0O000OOOOO ['status']==500 :#line:455
                                print (f'【余额提现】:{OOO0O0O0O000OOOOO["message"]}')#line:456
        except Exception as OO00O0OOO0OOO0OO0 :#line:457
            print (OO00O0OOO0OOO0OO0 )#line:458
    def invitenum (O0OO0O0O0O0OO0OOO ):#line:461
        global invited_new #line:462
        try :#line:463
            OOOOOO00OOO00O00O =f'__{timi_new()}'#line:464
            OOOOO00OO0000OO00 ={'source':'scsc','authorization':O0OO0O0O0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00OOO00O00O ),'signstring':OOOOOO00OOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:475
            O000O0O0000O0OO0O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOO00OO0000OO00 ).json ()#line:476
            if 'status'in O000O0O0000O0OO0O :#line:478
                if O000O0O0000O0OO0O ['status']==200 :#line:479
                    O00O0O0O000OOO000 =O000O0O0000O0OO0O ['data']['invited_count']#line:480
                    O0000OOO00OO00O00 =O000O0O0000O0OO0O ['data']['invited_second_count']#line:481
                    print (f'【我的邀请】:直邀好友:{O00O0O0O000OOO000}丨间邀好友:{O0000OOO00OO00O00}')#line:482
                    if O00O0O0O000OOO000 <2 :#line:483
                        O0O00OO0O00O0O0O0 =f'__{timi_new()}'#line:484
                        OO00OOOO000OOO000 ={'source':'scsc','authorization':O0OO0O0O0O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO0O00O0O0O0 ),'signstring':O0O00OO0O00O0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:495
                        O0O00O0O00000O000 =requests .request ('get',f'{host}/user',headers =OO00OOOO000OOO000 ).json ()#line:496
                        if 'status'in O0O00O0O00000O000 :#line:498
                            if O0O00O0O00000O000 ['status']==200 :#line:499
                                invited_new .append (O0O00O0O00000O000 ['data']['inner_id'])#line:500
        except Exception as OO0OO00OO00OO0OOO :#line:501
            print (OO0OO00OO00OO0OOO )#line:502
    def game_map (O00OO00OO0O00OOO0 ):#line:505
        try :#line:506
            O0OO0O0OO0OO000OO =f'__{timi_new()}'#line:507
            O0OOOO00OO0000000 ={'source':'scsc','authorization':O00OO00OO0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OO0OO000OO ),'signstring':O0OO0O0OO0OO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:518
            OOO00000000O0OO0O =requests .request ('get',f'{host}/game/map',headers =O0OOOO00OO0000000 ).json ()#line:519
            if 'status'in OOO00000000O0OO0O :#line:521
                if OOO00000000O0OO0O ['status']==200 :#line:522
                    for O00OOO00O0OOO0OO0 in OOO00000000O0OO0O ['data']['list'][0 ]['crops']:#line:523
                        O00OOOO000OO0O00O =O00OOO00O0OOO0OO0 ['level']#line:525
                        if O00OOOO000OO0O00O ==41 :#line:526
                            O0O0O0O0OO00O000O =O00OOO00O0OOO0OO0 ['crop_name']#line:527
                            OO0000OOO00OOO00O =O00OOO00O0OOO0OO0 ['count']#line:528
                            if OO0000OOO00OOO00O >0 :#line:529
                                print (f'【农业资产】:{O0O0O0O0OO00O000O}丨数量:{OO0000OOO00OOO00O}')#line:530
                                if float (datetime .datetime .now ().hour )>8 :#line:531
                                    O00OO00OO0O00OOO0 .the_query ()#line:532
        except Exception as OO00O00O0OO0O000O :#line:533
            print (OO00O00O0OO0O000O )#line:534
    def give_gold (OO0O0O0OOOOOO0OO0 ):#line:537
        try :#line:538
            OOO0O000O0O0O0OOO =f'__{timi_new()}'#line:539
            O0O0O0OOOO0000OO0 ={'source':'scsc','authorization':OO0O0O0OOOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O0O0O0OOO ),'signstring':OOO0O000O0O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            O000O0O0000000000 =requests .request ('get',f'{host}/user',headers =O0O0O0OOOO0000OO0 ).json ()#line:551
            if 'status'in O000O0O0000000000 :#line:552
                if O000O0O0000000000 ['status']==200 :#line:553
                    if float (OO0O0O0OOOOOO0OO0 .doneeNo )!=0 :#line:554
                        O000OO0OO0000OO0O =O000O0O0000000000 ['data']['assets']['gold']#line:555
                        if float (O000OO0OO0000OO0O )>float (OO0O0O0OOOOOO0OO0 .innerId ):#line:556
                            O0OOO0OOO0O0OO00O =int (float (O000OO0OO0000OO0O )/1.1 )#line:557
                            OOO0O000O0O0O0OOO =f'_doneeNo={OO0O0O0OOOOOO0OO0.doneeNo}&quantity={O0OOO0OOO0O0OO00O}_{timi_new()}'#line:558
                            O0O0O0OOOO0000OO0 ={'source':'scsc','authorization':OO0O0O0OOOOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O0O0O0OOO ),'signstring':OOO0O000O0O0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:569
                            OO000OO000OOO0OO0 ={"quantity":O0OOO0OOO0O0OO00O ,"doneeNo":OO0O0O0OOOOOO0OO0 .doneeNo }#line:573
                            O00000OOOOO0OO0O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0OOOO0000OO0 ,data =OO000OO000OOO0OO0 ).json ()#line:574
                            if 'status'in O00000OOOOO0OO0O0 :#line:576
                                if O00000OOOOO0OO0O0 ['status']==200 :#line:577
                                    if O00000OOOOO0OO0O0 ['data']:#line:578
                                        print (f'【赠送种子】:赠送{O0OOO0OOO0O0OO00O}种子给{OO0O0O0OOOOOO0OO0.doneeNo}成功')#line:579
                    else :#line:580
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:581
        except Exception as OO0OOO0O000OOOOOO :#line:582
            print (OO0OOO0O000OOOOOO )#line:583
    def invitation (O0O0OOOO00OOOOOOO ):#line:585
        try :#line:586
            _O0OO0O0000O00O000 =float (bundled_def ())/4 #line:587
            O0OOOOOO0O0O0O00O =f'_innerId={int(_O0OO0O0000O00O000)}_{timi_new()}'#line:588
            OOO0O000O0O00OOO0 ={'source':'scsc','authorization':O0O0OOOO00OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0O0O0O00O ),'signstring':O0OOOOOO0O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:599
            OO0O00O0O0O0O0000 ={"innerId":int (_O0OO0O0000O00O000 )}#line:600
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O000O0O00OOO0 ,data =OO0O00O0O0O0O0000 )#line:601
        except Exception as O000O000O000O00OO :#line:602
            print (O000O000O000O00OO )#line:603
    def winning_rewards (O00000O0OO0OO0OO0 ):#line:606
        try :#line:607
            O00OO0O0O000O0O0O =f'__{timi_new()}'#line:608
            O0O0O0O00O0OOO00O ={'source':'scsc','authorization':O00000O0OO0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O0O000O0O0O ),'signstring':O00OO0O0O000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:619
            O0000000OOO00OO00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O0O0O00O0OOO00O ).json ()#line:620
            if 'status'in O0000000OOO00OO00 :#line:622
                if O0000000OOO00OO00 ['status']==200 :#line:623
                    if O0000000OOO00OO00 ['data']['amount']:#line:624
                        OO0O0O0O0000000OO =O0000000OOO00OO00 ['data']['amount']['gold']#line:625
                        return OO0O0O0O0000000OO #line:626
                    else :#line:627
                        return 0 #line:628
        except Exception as OOOOOO0OOOOOO0O00 :#line:629
            print (OOOOOO0OOOOOO0O00 )#line:630
    def certification (OOO0O0OO00O000OOO ):#line:633
        try :#line:634
            OO00O0O0O00OO0000 =f'__{timi_new()}'#line:635
            OO00OOOOOOO00OOOO ={'source':'scsc','authorization':OOO0O0OO00O000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0O00OO0000 ),'signstring':OO00O0O0O00OO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:646
            OOOO00O000O00O0O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00OOOOOOO00OOOO ).json ()#line:647
            if 'status'in OOOO00O000O00O0O0 :#line:649
                if OOOO00O000O00O0O0 ['status']==200 :#line:650
                    if OOOO00O000O00O0O0 ['data']['result']:#line:651
                        O00OO0OOOOO00O000 =OOOO00O000O00O0O0 ['data']['nick_name']#line:652
                        return O00OO0OOOOO00O000 #line:653
                    else :#line:654
                        weishim .append (OOO0O0OO00O000OOO .token )#line:655
                        return '未实名'#line:656
        except Exception as OOOOO00OOO000OO00 :#line:657
            print (OOOOO00OOO000OO00 )#line:658
    def crops_illustrated (OOO00O000O0OO0OOO ):#line:661
        try :#line:662
            O00O00O00O00O0OOO =f'__{timi_new()}'#line:663
            O0000O0OO00OOOOOO ={'source':'scsc','authorization':OOO00O000O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00O00O0OOO ),'signstring':O00O00O00O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:674
            O000O0OOOOO0OOO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0000O0OO00OOOOOO ).json ()#line:675
            if 'status'in O000O0OOOOO0OOO00 :#line:677
                if O000O0OOOOO0OOO00 ['status']==200 :#line:678
                    O00O0O00000O000O0 =O000O0OOOOO0OOO00 ['data'][0 ]['crops']#line:679
                    for O00OOOOO00O00OO00 in O00O0O00000O000O0 :#line:680
                        if O00OOOOO00O00OO00 ['ill_clover_award']:#line:681
                            if float (O00OOOOO00O00OO00 ['ill_clover_award'])>1 :#line:682
                                if O00OOOOO00O00OO00 ['is_finish']:#line:683
                                    if not O00OOOOO00O00OO00 ['is_getit']:#line:684
                                        if OOO00O000O0OO0OOO .certification ()!='未实名':#line:685
                                            O00O00O00O00O0OOO =f'_award_level={O00OOOOO00O00OO00["level"]}_{timi_new()}'#line:686
                                            O0000O0OO00OOOOOO ={'source':'scsc','authorization':OOO00O000O0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00O00O0OOO ),'signstring':O00O00O00O00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:697
                                            O0O0OO000O0O0O0O0 ={"award_level":O00OOOOO00O00OO00 ['level']}#line:698
                                            O0OO00O0O00OOO00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0000O0OO00OOOOOO ,json =O0O0OO000O0O0O0O0 ).json ()#line:700
                                            if 'status'in O0OO00O0O00OOO00O :#line:701
                                                if O0OO00O0O00OOO00O ['status']==200 :#line:702
                                                    O00OO0O00O0OOOOOO =O0OO00O0O00OOO00O ['data']['ill_clover_award']#line:703
                                                    print (f'【图鉴奖励】:领取{O00OOOOO00O00OO00["crop_name"]}成就丨奖励{O00OO0O00O0OOOOOO}☘️')#line:705
                                                if O0OO00O0O00OOO00O ['status']==500 :#line:706
                                                    print (f'【图鉴奖励】:{O0OO00O0O00OOO00O["message"]}')#line:707
        except Exception as OO000O00OOOO0OOO0 :#line:708
            print (OO000O00OOOO0OOO0 )#line:709
    def watched_ad (OO000O0O0O0OOO00O ):#line:712
        try :#line:713
            OOO000O000OOOOO00 =f'__{timi_new()}'#line:714
            OOOO000O0OOOOOOOO ={'source':'scsc','authorization':OO000O0O0O0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OOOOO00 ),'signstring':OOO000O000OOOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:725
            OOOOOO00000O00000 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OOOOOOOO ).json ()#line:726
            if 'status'in OOOOOO00000O00000 :#line:728
                if OOOOOO00000O00000 ['status']==200 :#line:729
                    if 'offlineInfo'in OOOOOO00000O00000 ['data']:#line:730
                        time .sleep (random .randint (1 ,3 ))#line:731
                        O0OO0O0O0000O00OO =OOOOOO00000O00000 ['data']['offlineInfo']['off_minute']#line:732
                        O0OOO0OO000OOOOO0 =float (OOOOOO00000O00000 ['data']['silver'])/1000000000000 #line:733
                        time .sleep (1 )#line:734
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOO000O0OOOOOOOO ).json ()#line:735
                        time .sleep (2 )#line:736
                        OOO0OO0000000O0OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO000O0OOOOOOOO ).json ()#line:737
                        if 'status'in OOO0OO0000000O0OO :#line:739
                            if OOO0OO0000000O0OO ['status']==200 :#line:740
                                OOOOOOO0O00O0O0OO =float (OOO0OO0000000O0OO ['data']['silver'])/1000000000000 #line:741
                                O00O0O0OOOOOO0O00 =str (OOOOOOO0O00O0O0OO -O0OOO0OO000OOOOO0 )[:6 ]#line:742
                                print (f'【离线奖励】:翻倍离线{O0OO0O0O0000O00OO}分钟奖励🌱数量:{O00O0O0OOOOOO0O00}t粒')#line:743
        except Exception as OO0O0OO00000O00OO :#line:744
            print (OO0O0OO00000O00OO )#line:745
    def user_ad (O0O000OOO0000O0OO ):#line:748
        try :#line:749
            OO00OOO000OOOOO0O =f'__{timi_new()}'#line:750
            OOO0O0OO0000O0OO0 ={'source':'scsc','authorization':O0O000OOO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO000OOOOO0O ),'signstring':OO00OOO000OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            OO00O0OO0O00O0000 =requests .request ('get',f'{host}/user/ad',headers =OOO0O0OO0000O0OO0 ).json ()#line:762
            if 'status'in OO00O0OO0O00O0000 :#line:764
                if OO00O0OO0O00O0000 ['status']==200 :#line:765
                    O00OOO00OO0OO0000 =OO00O0OO0O00O0000 ['data']['max_time']#line:766
                    O00O000000O0000OO =OO00O0OO0O00O0000 ['data']['watch_time']#line:767
                    O0000O0O00000O00O =OO00O0OO0O00O0000 ['data']['added_time']#line:768
                    print (f'【获取种子】:获取🌱剩余{O0000O0O00000O00O + O00OOO00OO0OO0000 - O00O000000O0000OO}次丨好友提供:{O0000O0O00000O00O}次')#line:769
                    if O0000O0O00000O00O +O00OOO00OO0OO0000 -O00O000000O0000OO >0 :#line:770
                        time .sleep (random .randint (16 ,19 ))#line:771
                        O00OO00O0O00OOO0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO0O0OO0000O0OO0 ).json ()#line:772
                        if 'status'in O00OO00O0O00OOO0O :#line:774
                            if O00OO00O0O00OOO0O ['status']==200 :#line:775
                                OO0O0O00OO0000OOO =float (O00OO00O0O00OOO0O ['data']['silver'])/1000000000000 #line:776
                                print (f'【获取种子】:获得🌱:{int(OO0O0O00OO0000OOO)}t粒')#line:777
                                return True #line:778
                            if O00OO00O0O00OOO0O ['status']==500 :#line:779
                                O00O0O00O0000OOOO =O00OO00O0O00OOO0O ['message']#line:780
                                print (f'【获取种子】:{O00O0O00O0000OOOO}')#line:781
                                return False #line:782
        except Exception as O0O0000000OOOOOO0 :#line:783
            print (O0O0000000OOOOOO0 )#line:784
    def synthetic (O0O0OO0OO0O0OO0O0 ):#line:787
        global id ,g #line:788
        try :#line:789
            OO0O0000O0O000OOO =O0O0OO0OO0O0OO0O0 .level_new ()#line:790
            OOO0000OOOOO00OO0 =random .randint (9 ,11 )#line:791
            OOOO00OO0OO0OO000 =f'_site=8&targetSite={OOO0000OOOOO00OO0}_{timi_new()}'#line:792
            OOO0O0OO00OO0O0O0 ={'source':'scsc','authorization':O0O0OO0OO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO00OO0OO0OO000 ),'signstring':OOOO00OO0OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:803
            OOO0OOOO000O0O0O0 ={"site":int (8 ),"targetSite":int (OOO0000OOOOO00OO0 )}#line:804
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0OO00OO0O0O0 ,json =OOO0OOOO000O0O0O0 )#line:805
            while True :#line:806
                OOOO0O0000OO00OO0 =f'__{timi_new()}'#line:807
                O00O0000OOOO00000 ={'source':'scsc','authorization':O0O0OO0OO0O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0000OO00OO0 ),'signstring':OOOO0O0000OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:818
                O0OO0O000O00O0OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O0000OOOO00000 ).json ()#line:819
                if 'status'in O0OO0O000O00O0OO0 :#line:821
                    if O0OO0O000O00O0OO0 ['status']==200 :#line:822
                        OO0000OOO0O0O00O0 =O0OO0O000O00O0OO0 ['data']['cropList']#line:823
                        O0OOOO00OOO00000O =O0OO0O000O00O0OO0 ['data']['gameCoreDataDBid']#line:824
                        O0O0OO000OO00000O =float (O0OO0O000O00O0OO0 ['data']['silver'])/1000000000000 #line:825
                        OOO00000O000OO0O0 =0 #line:830
                        for O0000O000000O0OOO in OO0000OOO0O0O00O0 :#line:831
                            if not O0000O000000O0OOO :#line:832
                                OOO00O00000O0OOO0 =f'_crop_id={O0OOOO00OOO00000O}&site={OOO00000O000OO0O0}_{O0O0OO0OO0O0OO0O0.time}'#line:833
                                OO00000OO0O00OO0O ={'source':'scsc','authorization':O0O0OO0OO0O0OO0O0 .token ,'timestamp':O0O0OO0OO0O0OO0O0 .time ,'sign':sign (OOO00O00000O0OOO0 ),'signstring':OOO00O00000O0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
                                OO0O000OOOO0OOOO0 ={"site":OOO00000O000OO0O0 ,"crop_id":O0OOOO00OOO00000O }#line:844
                                O0000O0O0O0000000 =requests .request ('post',f'{host}/game/crops/buy',headers =OO00000OO0O00OO0O ,data =OO0O000OOOO0OOOO0 ).json ()#line:845
                                time .sleep (random .randint (1 ,3 )/10 )#line:847
                                if 'status'in O0000O0O0O0000000 :#line:848
                                    if O0000O0O0O0000000 ['status']==200 :#line:849
                                        if O0000O0O0O0000000 ['message']=='种子数量不足':#line:850
                                            OO0O0000O0O000OOO =O0O0OO0OO0O0OO0O0 .level_new ()#line:851
                                            print (f'【种植合成】:{O0000O0O0O0000000["message"]}')#line:852
                                            if not O0O0OO0OO0O0OO0O0 .user_ad ():#line:853
                                                return False #line:854
                                    if O0000O0O0O0000000 ['status']==500 :#line:855
                                        print (f'【种植合成】:{O0000O0O0O0000000["message"]}')#line:856
                                        return False #line:857
                            OOO00000O000OO0O0 +=1 #line:858
                        O0OO00OO0OO00O0OO =requests .request ('get',f'{host}/game/getAllData',headers =O00O0000OOOO00000 ).json ()#line:859
                        OOOO000OO0000OO0O =O0OO00OO0OO00O0OO ['data']['cropList']#line:860
                        OOO0OOO000OO0O000 =False #line:861
                        for O0000O000000O0OOO in range (12 ):#line:862
                            id =OOOO000OO0000OO0O [O0000O000000O0OOO ]['level']#line:863
                            if float (OO0O0000O0O000OOO )-float (id )>9 :#line:864
                                O0000O0000OOOOOOO =f'_site={O0000O000000O0OOO}_{timi_new()}'#line:865
                                O0O0OOO000O0O0O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0OO0OO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0000O0000OOOOOOO ),'signstring':O0000O0000OOOOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:876
                                OOOO000OO0OO00O00 ={"site":O0000O000000O0OOO }#line:877
                                OOO0000OO0O00O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0O0OOO000O0O0O0O ,data =OOOO000OO0OO00O00 ).json ()#line:879
                                if 'status'in OOO0000OO0O00O00O :#line:880
                                    if OOO0000OO0O00O00O ['status']==200 :#line:881
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:882
                            if id !=0 :#line:883
                                for O00OO0O0O0OO00OO0 in range (11 ):#line:884
                                    O0OO0OO0O00OOO0OO =O00OO0O0O0OO00OO0 +1 #line:885
                                    g =OOOO000OO0000OO0O [O0OO0OO0O00OOO0OO ]['level']#line:886
                                    if id ==g :#line:887
                                        O00OO0OOOOOO0OO00 =O00OO0O0O0OO00OO0 +2 #line:888
                                        if O00OO0OOOOOO0OO00 !=O0000O000000O0OOO +1 :#line:889
                                            O0O000O0OOOO0O000 =O0000O000000O0OOO +1 #line:890
                                            time .sleep (random .randint (1 ,3 )/10 )#line:892
                                            OOOO00OO0OO0OO000 =f'_site={O0O000O0OOOO0O000 - 1}&targetSite={O00OO0OOOOOO0OO00 - 1}_{timi_new()}'#line:893
                                            OOO0O0OO00OO0O0O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O0OO0OO0O0OO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO00OO0OO0OO000 ),'signstring':OOOO00OO0OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:910
                                            OO0OOOO00000000O0 ={"site":int (O0O000O0OOOO0O000 -1 ),"targetSite":int (O00OO0OOOOOO0OO00 -1 )}#line:911
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O0OO00OO0O0O0 ,json =OO0OOOO00000000O0 )#line:912
                                            OOO0OOO000OO0O000 =True #line:914
                                    if OOO0OOO000OO0O000 :#line:915
                                        break #line:916
                                if OOO0OOO000OO0O000 :#line:917
                                    break #line:918
        except :#line:919
            O0O0OO0OO0O0OO0O0 .synthetic ()#line:920
    def level_new (O0OO0O0O0O0O00000 ):#line:923
        try :#line:924
            OOOOOO000OOOO00OO =f'__{timi_new()}'#line:925
            O0O00OO0O0O00OOOO ={'source':'scsc','authorization':O0OO0O0O0O0O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO000OOOO00OO ),'signstring':OOOOOO000OOOO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:936
            OO00OO0O0O00OO00O =requests .request ('get',f'{host}/user',headers =O0O00OO0O0O00OOOO ).json ()#line:937
            if 'status'in OO00OO0O0O00OO00O :#line:938
                if OO00OO0O0O00OO00O ['status']==200 :#line:939
                    return float (OO00OO0O0O00OO00O ['data']['level'])#line:940
        except Exception as O0OOO000000O0OO0O :#line:941
            print (O0OOO000000O0OO0O )#line:942
    def propsraffle (O0OO0OO0OOOO0O000 ):#line:945
        try :#line:946
            while True :#line:947
                OOOO00O00O0O0OOOO =f'__{timi_new()}'#line:948
                OO00OO0O0O00O0O0O ={'source':'scsc','authorization':O0OO0OO0OOOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O00O0O0OOOO ),'signstring':OOOO00O00O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                O0O0O00OO0O00O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00OO0O0O00O0O0O ).json ()#line:960
                if 'status'in O0O0O00OO0O00O0OO :#line:962
                    if O0O0O00OO0O00O0OO ['status']==200 :#line:963
                        O00O00O0000OO0O00 =O0O0O00OO0O00O0OO ['data']['rows']#line:964
                        O00O000OOOOO0O0O0 =O0O0O00OO0O00O0OO ['data']['vstate']#line:965
                        if O00O00O0000OO0O00 ==5 or O00O00O0000OO0O00 ==6 or O00O00O0000OO0O00 ==7 :#line:966
                            O0OOOOO000O0O00O0 =O0O0O00OO0O00O0OO ['data']['silver']#line:967
                            print (f'【转盘抽奖】:获得种子:{O0OOOOO000O0O00O0}')#line:968
                        if O00O00O0000OO0O00 ==1 or O00O00O0000OO0O00 ==2 or O00O00O0000OO0O00 ==3 :#line:969
                            OO0O0OOO0OOOOO00O =O0O0O00OO0O00O0OO ['data']['clover']#line:970
                            print (f'【转盘抽奖】:获得三叶草:{OO0O0OOO0OOOOO00O}')#line:971
                        if O00O00O0000OO0O00 ==4 or O00O00O0000OO0O00 ==8 :#line:972
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:973
                        if O00O00O0000OO0O00 =='抽奖次数已用完':#line:977
                            break #line:1011
                time .sleep (random .randint (8 ,15 )/10 )#line:1012
        except Exception as OOO000OO00O0OO00O :#line:1013
            print (OOO000OO00O0OO00O )#line:1014
    def friends_invitation (O0O0O0OOO0O000000 ):#line:1017
        try :#line:1018
            OOO0OO0O0000O000O =f'__{timi_new()}'#line:1019
            O0OOO00OOOOOO0000 ={'source':'scsc','authorization':O0O0O0OOO0O000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0000O000O ),'signstring':OOO0OO0O0000O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1030
            OO0OO00000OOO0O0O =requests .request ('get',f'{host}/friends',headers =O0OOO00OOOOOO0000 ).json ()#line:1031
            if 'status'in OO0OO00000OOO0O0O :#line:1032
                if OO0OO00000OOO0O0O ['status']==200 :#line:1033
                    OO000OO0OO0O000OO =OO0OO00000OOO0O0O ['data']['myInviteter']#line:1034
                    if OO000OO0OO0O000OO :#line:1035
                        OO0O0O00OOOOOO0OO =OO000OO0OO0O000OO ['user']['nickname']#line:1036
                        O00O00OO0OO000OO0 =O0O0O0OOO0O000000 .certification ()#line:1037
                        print (f'【查邀请人】:我的邀请人:{OO0O0O00OOOOOO0OO}丨实名:{O00O00OO0OO000OO0}')#line:1038
                    else :#line:1039
                        if O0O0O0OOO0O000000 .innerId !='0':#line:1040
                            O0O0O0OOO0O000000 .invitation ()#line:1041
        except Exception as OO00OOOOO00OOOO0O :#line:1042
            print (OO00OOOOO00OOOO0O )#line:1043
    def add_clover (OO0O000O0OO00O000 ):#line:1046
        global golden_seed #line:1047
        try :#line:1048
            OO0O0O0O000O0000O =f'__{timi_new()}'#line:1049
            O000OOO000O00O0O0 ={'source':'scsc','authorization':OO0O000O0OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O000O0000O ),'signstring':OO0O0O0O000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1060
            O0O0OOO00OO000OOO =requests .request ('get',f'{host}/assets/clovers',headers =O000OOO000O00O0O0 ).json ()#line:1061
            if 'status'in O0O0OOO00OO000OOO :#line:1063
                if O0O0OOO00OO000OOO ['status']==200 :#line:1064
                    O0O0O0O0O00OO00O0 =O0O0OOO00OO000OOO ['data']['clover']#line:1065
                    O000O0O00OOO0OO00 =O0O0OOO00OO000OOO ['data']['used_clover']#line:1066
                    O0O0OOOOOOO00O00O =float (O0O0O0O0O00OO00O0 )-float (O000O0O00OOO0OO00 )#line:1067
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000O0O00OOO0OO00}')#line:1068
                    if OO0O000O0OO00O000 .certification ()!='未实名':#line:1069
                        if O0O0OOOOOOO00O00O >1 :#line:1070
                            OO0O0O0O000O0000O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O0OOOOOOO00O00O)}_{timi_new()}'#line:1071
                            OOO00O0000OO00O0O ={'source':'scsc','authorization':OO0O000O0OO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O000O0000O ),'signstring':OO0O0O0O000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1082
                            OO00O00OOOOO00O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O0OOOOOOO00O00O )}#line:1083
                            O0O0OO00OO0000O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00O0000OO00O0O ,data =OO00O00OOOOO00O0O ).json ()#line:1084
                            if 'status'in O0O0OO00OO0000O0O :#line:1086
                                if O0O0OO00OO0000O0O ['status']==200 :#line:1087
                                    print (f'【参与抽奖】:添加☘️:{O0O0OO00OO0000O0O["data"]}丨数量:{O0O0OOOOOOO00O00O}')#line:1088
                                if O0O0OO00OO0000O0O ['status']==500 :#line:1089
                                    print (f'【参与抽奖】:添加☘️:{O0O0OO00OO0000O0O["message"]}')#line:1090
            OOO0O0O0OOOOOO0O0 =requests .request ('get',f'{host}/lottery',headers =O000OOO000O00O0O0 ).json ()#line:1091
            OO00OO00O0OO00O00 =OO0O000O0OO00O000 .winning_rewards ()#line:1093
            if 'status'in OOO0O0O0OOOOOO0O0 :#line:1094
                if OOO0O0O0OOOOOO0O0 ['status']==200 :#line:1095
                    OOO00OO0O0000OOOO =OOO0O0O0OOOOOO0O0 ['data'][0 ]['day_get_gold_quantity']#line:1096
                    golden_seed +=float (OOO00OO0O0000OOOO )#line:1097
                    OO00OO000OO0O000O =OOO0O0O0OOOOOO0O0 ['data'][1 ]['value']#line:1098
                    O00O0O00OO0000O00 =OOO0O0O0OOOOOO0O0 ['data'][0 ]['join_number']#line:1099
                    O0OO0O0OOO000O0O0 =int (float (OOO0O0O0OOOOOO0O0 ['data'][0 ]['totalValue']))#line:1100
                    OOOOOO00O0OOOOO00 =float (OO00OO000OO0O000O /O0OO0O0OOO000O0O0 )*10000 #line:1101
                    O000O0000000000OO =O0OO0O0OOO000O0O0 /O00O0O00OO0000O00 #line:1102
                    print (f'【参与抽奖】:预计每天中{str(OOO00OO0O0000OOOO)[:6]}颗金种子丨好友收益:{str(OO00OO00O0OO00O00)[:6]}')#line:1103
                    print (f'【抽奖统计】:每1万☘️中{str(OOOOOO00O0OOOOO00)[:6]}颗金种子丨☘️人均:{str(O000O0000000000OO)[:7]}️')#line:1104
        except Exception as OO000O000OOO0OOO0 :#line:1105
            print (OO000O000OOO0OOO0 )#line:1106
    def energy (O00OO00O0O0O0OO0O ):#line:1109
        try :#line:1110
            while True :#line:1111
                O0OO0O0OOO00O000O =f'__{timi_new()}'#line:1112
                O000OO0O0O0O00O0O ={'source':'scsc','authorization':O00OO00O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0OOO00O000O ),'signstring':O0OO0O0OOO00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1123
                OO0O0000O0OO0O00O =requests .request ('get',f'{host}/energy/general',headers =O000OO0O0O0O00O0O ).json ()#line:1124
                if 'status'in OO0O0000O0OO0O00O :#line:1126
                    if OO0O0000O0OO0O00O ['status']==200 :#line:1127
                        OO000OOOOO0OOO0OO =OO0O0000O0OO0O00O ['data']['ordinary_water']#line:1128
                        O0O0O0O0OOOO0O00O =OO0O0000O0OO0O00O ['data']['ordinary_fertilizer']#line:1129
                        OO0OO000OO0O0OO00 =OO0O0000O0OO0O00O ['data']['videoStatus']#line:1130
                        O0OO0OO0000OO0OOO =OO0O0000O0OO0O00O ['data']['waterVideoKey']#line:1131
                        print (f'【我的营养】:肥料:{str(O0O0O0O0OOOO0O00O).split(".")[0]}丨水滴:{str(OO000OOOOO0OOO0OO).split(".")[0]}')#line:1133
                        if float (O0O0O0O0OOOO0O00O )<96 :#line:1134
                            if OO0OO000OO0O0OO00 :#line:1135
                                time .sleep (random .randint (160 ,180 )/10 )#line:1136
                                O0O0000O0000OO0O0 =99 -float (O0O0O0O0OOOO0O00O )#line:1137
                                OO00OO000O00OO00O ={"fertilizer":str (O0O0000O0000OO0O0 ).split ('.')[0 ]}#line:1138
                                O00O00O0O000O00OO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000OO0O0O0O00O0O ).json ()#line:1140
                                if 'status'in O00O00O0O000O00OO :#line:1142
                                    if O00O00O0O000O00OO ['status']==200 :#line:1143
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O0O000O00OO["message"]}')#line:1144
                                    if O00O00O0O000O00OO ['status']==500 :#line:1145
                                        print (f'【购买肥料】:看广告获取肥料:{O00O00O0O000O00OO["message"]}')#line:1146
                                        break #line:1147
                                if float (O0O0O0O0OOOO0O00O )<78 :#line:1149
                                    O0O0000O0000OO0O0 =80 -float (O0O0O0O0OOOO0O00O )#line:1150
                                    O000O00O0OO00OOO0 =f'_fertilizer={int(O0O0000O0000OO0O0)}_{timi_new()}'#line:1151
                                    OO0000O0O00O0O0O0 ={'source':'scsc','authorization':O00OO00O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O0OO00OOO0 ),'signstring':O000O00O0OO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1162
                                    O0O00O0O0O0O00O00 ={"fertilizer":int (O0O0000O0000OO0O0 )}#line:1163
                                    O0OO0O0OOOO0O0000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0000O0O00O0O0O0 ,data =O0O00O0O0O0O00O00 ).json ()#line:1165
                                    if 'status'in O0OO0O0OOOO0O0000 :#line:1167
                                        if O0OO0O0OOOO0O0000 ['status']==200 :#line:1168
                                            print (f'【购买肥料】:购买肥料:{O0OO0O0OOOO0O0000["message"]}丨数量:{int(O0O0000O0000OO0O0)}')#line:1169
                                        if O0OO0O0OOOO0O0000 ['status']==500 :#line:1170
                                            print (f'【购买肥料】:购买肥料:{O0OO0O0OOOO0O0000["message"]}丨数量:{int(O0O0000O0000OO0O0)}')#line:1171
                                            OOOO0O0O00OOO0O0O =O0OO0O0OOOO0O0000 ["message"].split ('-')[1 ]#line:1172
                                            OOOO0O0O00OO00000 =f'__{timi_new()}'#line:1173
                                            OO0O0O00OOO0O00O0 ={'source':'scsc','authorization':O00OO00O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00OO00000 ),'signstring':OOOO0O0O00OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1184
                                            OOO0OO0OO00000000 =requests .request ('get',f'{host}/user',headers =OO0O0O00OOO0O00O0 ).json ()#line:1185
                                            if 'status'in OOO0OO0OO00000000 :#line:1186
                                                if OOO0OO0OO00000000 ['status']==200 :#line:1187
                                                    O00OOO0O00O00OOO0 =OOO0OO0OO00000000 ['data']['inner_id']#line:1188
                                                    if give_gold (O00OOO0O00O00OOO0 ,float (OOOO0O0O00OOO0O0O )+1 ):#line:1189
                                                        O00OO00O0O0O0OO0O .energy ()#line:1190
                        if float (OO000OOOOO0OOO0OO )<880 :#line:1191
                            if O0OO0OO0000OO0OOO :#line:1192
                                time .sleep (random .randint (160 ,180 )/10 )#line:1193
                                OOOOOOO0O0O00000O =999 -float (OO000OOOOO0OOO0OO )#line:1194
                                O0O0000OO0O0O0OOO ={"water":str (OOOOOOO0O0O00000O ).split ('.')[0 ]}#line:1195
                                OO0O0O0OOOOO0O0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000OO0O0O0O00O0O ).json ()#line:1197
                                if 'status'in OO0O0O0OOOOO0O0OO :#line:1199
                                    if OO0O0O0OOOOO0O0OO ['status']==200 :#line:1200
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0O0OOOOO0O0OO["message"]}')#line:1201
                                    if OO0O0O0OOOOO0O0OO ['status']==500 :#line:1202
                                        print (f'【购买水滴】:看广告获取水滴:{OO0O0O0OOOOO0O0OO["message"]}')#line:1203
                                        break #line:1204
                                if float (OO000OOOOO0OOO0OO )<780 :#line:1205
                                    OOOOOOO0O0O00000O =800 -float (OO000OOOOO0OOO0OO )#line:1206
                                    OO000OOO000000000 =f'_water={int(OOOOOOO0O0O00000O)}_{timi_new()}'#line:1207
                                    OO0OO0000000OOOO0 ={'source':'scsc','authorization':O00OO00O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOO000000000 ),'signstring':OO000OOO000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1218
                                    O000O0O00OO000OOO ={"water":int (OOOOOOO0O0O00000O )}#line:1219
                                    OOO0O00000O00OOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OO0000000OOOO0 ,data =O000O0O00OO000OOO ).json ()#line:1221
                                    if 'status'in OOO0O00000O00OOOO :#line:1223
                                        if OOO0O00000O00OOOO ['status']==200 :#line:1224
                                            print (f'【购买水滴】:购买水滴:{OOO0O00000O00OOOO["message"]}丨数量:{int(OOOOOOO0O0O00000O)}')#line:1225
                                        if OOO0O00000O00OOOO ['status']==500 :#line:1226
                                            print (f'【购买水滴】:购买水滴:{OOO0O00000O00OOOO["message"]}丨数量:{int(OOOOOOO0O0O00000O)}')#line:1227
                                            OOOO0O0O00OOO0O0O =OOO0O00000O00OOOO ["message"].split ('-')[1 ]#line:1228
                                            OOOO0O0O00OO00000 =f'__{timi_new()}'#line:1229
                                            OO0O0O00OOO0O00O0 ={'source':'scsc','authorization':O00OO00O0O0O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0O00OO00000 ),'signstring':OOOO0O0O00OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1240
                                            OOO0OO0OO00000000 =requests .request ('get',f'{host}/user',headers =OO0O0O00OOO0O00O0 ).json ()#line:1241
                                            if 'status'in OOO0OO0OO00000000 :#line:1242
                                                if OOO0OO0OO00000000 ['status']==200 :#line:1243
                                                    O00OOO0O00O00OOO0 =OOO0OO0OO00000000 ['data']['inner_id']#line:1244
                                                    if give_gold (O00OOO0O00O00OOO0 ,float (OOOO0O0O00OOO0O0O )+1 ):#line:1245
                                                        O00OO00O0O0O0OO0O .energy ()#line:1246
                        break #line:1247
        except Exception as OO0000OO0OOO00OOO :#line:1248
            print (OO0000OO0OOO00OOO )#line:1249
def bundled_def ():#line:1252
    OO0000O0000O0OO00 =['5570536','7750212','7911652','7911680','7805624']#line:1253
    return OO0000O0000O0OO00 [random .randint (0 ,len (OO0000O0000O0OO00 )-1 )]#line:1254
def version_of_the_validation ():#line:1258
    return str ((95 -56 )/10 )#line:1259
def sc2 ():#line:1262
    return "19319#$%^&*((*"#line:1263
def OO00OO0OO0OO00OO00o0 ():#line:1266
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1268
def get_ip ():#line:1271
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1273
def gitee_validation ():#line:1276
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1277
def gitee_edition ():#line:1280
    try :#line:1281
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1282
    except :#line:1283
        sys .exit (0 )#line:1284
def O000OO000O0O00OOO00 ():#line:1288
    try :#line:1289
        O000O000O0O0OOOO0 =gitee_edition ()#line:1290
        if version_of_the_validation ()<O000O000O0O0OOOO0 ['CityEarth']['edition']:#line:1291
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O000O0O0OOOO0["CityEarth"]["edition"]}   ❌')#line:1292
            print (f'更新内容=>>{O000O000O0O0OOOO0["CityEarth"]["content"]}')#line:1293
        else :#line:1294
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O000O000O0O0OOOO0["CityEarth"]["edition"]}   ✅')#line:1295
            print (f'更新内容=>> {O000O000O0O0OOOO0["CityEarth"]["content"]}')#line:1296
    except Exception as O0000OOO000OO0OOO :#line:1297
        print (O0000OOO000OO0OOO )#line:1298
def sc3 ():#line:1301
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1302
if __name__ =='__main__':#line:1305
    start ()#line:1306
