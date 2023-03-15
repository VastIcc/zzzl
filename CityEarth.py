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
        OO0OOO00O0O00OO00 =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OO0OOO00O0O00OO00)}个账号==========")#line:16
        for O0OOO0OO0O00OOOOO in OO0OOO00O0O00OO00 :#line:17
            O0OOOOO00OO0OOO00 =[]#line:18
            print (f"------------正在执行第{OO0OOO00O0O00OO00.index(O0OOO0OO0O00OOOOO) + 1}个账号------------")#line:19
            OO00OO000OOOOO0OO =CityEarth (O0OOO0OO0O00OOOOO ,O0OOOOO00OO0OOO00 ,OO0OOO00O0O00OO00 .index (O0OOO0OO0O00OOOOO ))#line:20
            def O000000O0OOO0OO00 ():#line:22
                if OO00OO000OOOOO0OO .base_info ():#line:24
                    OO00OO000OOOOO0OO .sealing ()#line:26
                    OO00OO000OOOOO0OO .invitenum ()#line:28
                    OO00OO000OOOOO0OO .query_to_sell ()#line:30
                    OO00OO000OOOOO0OO .game_map ()#line:32
                    OO00OO000OOOOO0OO .friends_invitation ()#line:34
                    OO00OO000OOOOO0OO .energy ()#line:36
                    OO00OO000OOOOO0OO .add_clover ()#line:38
                    OO00OO000OOOOO0OO .propsraffle ()#line:40
                    OO00OO000OOOOO0OO .synthetic ()#line:42
                    OO00OO000OOOOO0OO .crops_illustrated ()#line:44
                    OO00OO000OOOOO0OO .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        OO00OO000OOOOO0OO .give_gold ()#line:49
            OO0O0OOOO0OO0OOOO =threading .Thread (target =O000000O0OOO0OO00 )#line:51
            OO0O0OOOO0OO0OOOO .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理数据------------")#line:54
        time .sleep (0.5 )#line:55
        OO00O00O0O000OOOO =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO00O00O0O000OOOO +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for O00O0OOOO00OOO00O in invited_new :#line:60
            print (O00O0OOOO00OOO00O )#line:61
        print ('开始打印未实名的token')#line:62
        for OO00OO00O00O000OO in weishim :#line:63
            print (OO00OO00O00O000OO )#line:64
    except Exception as OOOO0000000000000 :#line:65
        print (OOOO0000000000000 )#line:66
def give_gold (OO0000000OO0OOO00 ,OO0O0OO0OO0O0000O ):#line:70
    try :#line:71
        OO0OO0O0OOO0OOO00 =f'_doneeNo={OO0000000OO0OOO00}&quantity={int(OO0O0OO0OO0O0000O)}_{timi_new()}'#line:72
        OO000O00OOOO00OOO ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OOO0OOO00 ),'signstring':OO0OO0O0OOO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOOO00OO000000O00 ={"quantity":int (OO0O0OO0OO0O0000O ),"doneeNo":OO0000000OO0OOO00 }#line:87
        OOO0OOOO0O00OO000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO000O00OOOO00OOO ,data =OOOO00OO000000O00 ).json ()#line:88
        if 'status'in OOO0OOOO0O00OO000 :#line:90
            if OOO0OOOO0O00OO000 ['status']==200 :#line:91
                if OOO0OOOO0O00OO000 ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OO0O0OO0OO0O0000O)}种子给{OO0000000OO0OOO00}成功')#line:93
                    return True #line:94
            if OOO0OOOO0O00OO000 ['status']==401 :#line:95
                print (f'【赠送种子】:{OOO0OOOO0O00OO000["message"]}')#line:96
                return False #line:97
            if OOO0OOOO0O00OO000 ['status']==500 :#line:98
                print (f'【赠送种子】:{OOO0OOOO0O00OO000["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as OOOOOOOOO00OO0O0O :#line:102
        print (OOOOOOOOO00OO0O0O )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def sign (O0OO00O0OOO0OO0OO ):#line:110
    OO00OOOOO0OOOOOOO =hashlib .md5 (O0OO00O0OOO0OO0OO .encode ()).hexdigest ()#line:111
    O0O0O0O000O00OO0O =sc1 ()#line:112
    O0OOOOO0OOOOOO0O0 =sc2 ()#line:113
    OOOO000OO000OOOO0 =sc3 ()#line:114
    O0O00OO0OOO000OO0 =O0O0O0O000O00OO0O +OO00OOOOO0OOOOOOO +O0OOOOO0OOOOOO0O0 +OOOO000OO000OOOO0 #line:115
    OO0OOOOO000O0O0O0 =hashlib .md5 (O0O00OO0OOO000OO0 .encode ()).hexdigest ()#line:116
    return OO0OOOOO000O0O0O0 #line:117
def format_msg ():#line:120
    O00OOOO0OOOO00O0O =""#line:121
    for O0O0000OO0OO0OOO0 in msg_list :#line:122
        O00OOOO0OOOO00O0O +=str (O0O0000OO0OO0OOO0 )+"\r\n"#line:123
    return O00OOOO0OOOO00O0O #line:124
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
def get_json_data (O0O00000O0O00OO00 ,OOOO0O00000O000O0 ,O0000OO00OOOO00OO ,O0O000OO0OO0000O0 ):#line:147
    with open (O0O00000O0O00OO00 ,'rb')as OO0O000O00OOO0O0O :#line:148
        O00OOO0OOOOO0000O =json .load (OO0O000O00OOO0O0O )#line:149
        O00OOO0OOOOO0000O ['data'][OOOO0O00000O000O0 ][O0000OO00OOOO00OO ]=O0O000OO0OO0000O0 #line:150
        O0OOO00OO0O00O000 =O00OOO0OOOOO0000O #line:151
    OO0O000O00OOO0O0O .close ()#line:152
    return O0OOO00OO0O00O000 #line:153
def write_json_data (O00OOOOOO00OO0O0O ):#line:156
    with open (json_path1 ,'w')as O0OOO0OOO0O00OOOO :#line:157
        json .dump (O00OOOOOO00OO0O0O ,O0OOO0OOO0O00OOOO )#line:158
    O0OOO0OOO0O00OOOO .close ()#line:159
    return True #line:160
class CityEarth :#line:163
    def __init__ (O0O0O00000O0OOOO0 ,O0O0000O0000000OO ,OO0OOO0OOO000000O ,O00O0000OO00O0O0O ):#line:165
        try :#line:166
            O0O0O00000O0OOOO0 .msg =OO0OOO0OOO000000O #line:167
            O0O0O00000O0OOOO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:168
            O0O0O00000O0OOOO0 .token =O0O0000O0000000OO ['authorization']#line:169
            O0O0O00000O0OOOO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:170
            O0O0O00000O0OOOO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:171
            O0O0O00000O0OOOO0 .elephant_user =O0O0000O0000000OO ['elephant_user']#line:172
            O0O0O00000O0OOOO0 .elephant_pswd =O0O0000O0000000OO ['elephant_pswd']#line:173
            O0O0O00000O0OOOO0 .elephant_Task_ID =O0O0000O0000000OO ['elephant_Task_ID']#line:174
            O0O0O00000O0OOOO0 .len_new =O00O0000OO00O0O0O #line:175
        except :#line:176
            print ('变量格式错误')#line:177
    def base_info (O0000O00OOO00O0O0 ):#line:180
        try :#line:181
            O0000O00OOO00O0O0 .watched_ad ()#line:183
            O00O00O0O0OOOO0OO =f'__{timi_new()}'#line:184
            O0OO00O00OOO000O0 ={'source':'scsc','authorization':O0000O00OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0O0OOOO0OO ),'signstring':O00O00O0O0OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
            OOOO0OO000OOOOO0O =requests .request ('get',f'{host}/user',headers =O0OO00O00OOO000O0 ).json ()#line:196
            if 'status'in OOOO0OO000OOOOO0O :#line:198
                if OOOO0OO000OOOOO0O ['status']==200 :#line:199
                    O0O0O0OO00OOOOO00 =OOOO0OO000OOOOO0O ['data']['nickname']#line:200
                    OO00OO0O0OOOOO00O =OOOO0OO000OOOOO0O ['data']['inner_id']#line:201
                    OO00000OO00O00O00 =OOOO0OO000OOOOO0O ['data']['assets']['gold']#line:202
                    OOO0O0O0000O0O0OO =OOOO0OO000OOOOO0O ['data']['level']#line:203
                    print (f'【账号信息】:昵称:{O0O0O0OO00OOOOO00[:5]}丨ID:{OO00OO0O0OOOOO00O}丨等级:{OOO0O0O0000O0O0OO}丨金种子:{str(OO00000OO00O00O00).split(".")[0]}')#line:205
                    if 'wx_'in O0O0O0OO00OOOOO00 :#line:206
                        O0000O00OOO00O0O0 .change_nickname ()#line:207
                if OOOO0OO000OOOOO0O ['status']==401 :#line:208
                    print ('【账号信息】:账号失效正在尝试登录')#line:209
                    if O0000O00OOO00O0O0 .elephant_user =='f':#line:210
                        return False #line:211
                    OO00OOO00O0OO0OO0 =Invalid_login .addtask (elephant_user =O0000O00OOO00O0O0 .elephant_user ,elephant_pswd =O0000O00OOO00O0O0 .elephant_pswd ,elephant_Task_ID =O0000O00OOO00O0O0 .elephant_Task_ID )#line:214
                    O0OOOO000OOO0OO0O =get_json_data (json_path ,O0000O00OOO00O0O0 .len_new ,'authorization',OO00OOO00O0OO0OO0 )#line:215
                    if write_json_data (O0OOOO000OOO0OO0O ):#line:216
                        print ('正在写入账号配置文件')#line:217
                    return False #line:218
                if OOOO0OO000OOOOO0O ['status']==500 :#line:219
                    return False #line:220
            return True #line:221
        except Exception as O0O0O0O000OOOO0OO :#line:222
            print (O0O0O0O000OOOO0OO )#line:223
    def sealing (OO0OOOOO0O000O0O0 ):#line:226
        try :#line:227
            OO00000OOOOOO00O0 =f'__{timi_new()}'#line:228
            O00OOOO000OOO0O0O ={'source':'scsc','authorization':OO0OOOOO0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OOOOOO00O0 ),'signstring':OO00000OOOOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOO000OOO0O0O )#line:240
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOO000OOO0O0O )#line:241
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOO000OOO0O0O )#line:242
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOO000OOO0O0O )#line:243
            requests .request ('get',f'{host}/user',headers =O00OOOO000OOO0O0O )#line:244
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOO000OOO0O0O )#line:245
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOO000OOO0O0O )#line:246
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOO000OOO0O0O )#line:247
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOO000OOO0O0O )#line:248
            requests .request ('get',f'{host}/assets',headers =O00OOOO000OOO0O0O )#line:249
        except Exception as O0OOOOO0O0OOOOO00 :#line:250
            print (O0OOOOO0O0OOOOO00 )#line:251
    def the_query (O0O000O0O0O0000O0 ):#line:254
        try :#line:255
            O0OOOOO0O0000OOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:256
            OO00000OO0O0O0O00 ={'authorization':O0O000O0O0O0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0000OOOO ),'signstring':O0OOOOO0O0000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            O00000O000OOOO000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00000OO0O0O0O00 ).json ()#line:268
            if 'status'in O00000O000OOOO000 :#line:270
                if O00000O000OOOO000 ['status']==200 :#line:271
                    O0000O000OO000000 =O00000O000OOOO000 ['data']['rows'][3 ]['price']#line:272
                    O0O000O0O0O0000O0 .market_sale (O0000O000OO000000 )#line:273
        except Exception as OO00O0OO0OO00O0O0 :#line:274
            print (OO00O0OO0OO00O0O0 )#line:275
    def market_sale (OOO0OOO00O00OO0OO ,O0OO00O000OO0OO0O ):#line:278
        try :#line:279
            OOO0OO0O0O0O0OOO0 =timi_new ()#line:280
            O0O0OOOOOOO0O00O0 =f'type=crop__{OOO0OO0O0O0O0OOO0}'#line:281
            OO00OO0O0OOO0O0OO ={'source':'scsc','authorization':OOO0OOO00O00OO0OO .token ,'timestamp':str (OOO0OO0O0O0O0OOO0 ),'sign':sign (O0O0OOOOOOO0O00O0 ),'signstring':O0O0OOOOOOO0O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            O000OOOO00O0O000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00OO0O0OOO0O0OO ).json ()#line:294
            if 'status'in O000OOOO00O0O000O :#line:296
                if O000OOOO00O0O000O ['status']==200 :#line:297
                    if O000OOOO00O0O000O ['data']['rows']:#line:298
                        O0OOOOOO0O000OOOO =O000OOOO00O0O000O ['data']['rows'][0 ]['packsackItemId']#line:299
                        OOOO00O0OOO000O0O =O000OOOO00O0O000O ['data']['rows'][0 ]['quantity']#line:300
                        O0000OO00O000OO0O =float (O0OO00O000OO0OO0O )+float (random .randint (1 ,9 )*0.001 )#line:301
                        O0O0OO00OOO0OO0O0 =f'_packsackItemId={O0OOOOOO0O000OOOO}&price={str(O0000OO00O000OO0O)[:7]}&quantity={OOOO00O0OOO000O0O}_{OOO0OO0O0O0O0OOO0}'#line:302
                        O0000OOO0OOO00O00 ={'source':'scsc','authorization':OOO0OOO00O00OO0OO .token ,'timestamp':str (OOO0OO0O0O0O0OOO0 ),'sign':sign (O0O0OO00OOO0OO0O0 ),'signstring':O0O0OO00OOO0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                        O00O0O00O000OO0OO ={"packsackItemId":O0OOOOOO0O000OOOO ,"price":str (O0000OO00O000OO0O )[:7 ],"quantity":str (OOOO00O0OOO000O0O )}#line:318
                        O00OOOO0OO0000O0O =requests .request ('post',f'{host}/market/sale',headers =O0000OOO0OOO00O00 ,data =O00O0O00O000OO0OO ).json ()#line:319
                        if 'status'in O00OOOO0OO0000O0O :#line:321
                            if O00OOOO0OO0000O0O ['status']==200 :#line:322
                                print (f'【上架芦荟】:数量:{OOOO00O0OOO000O0O}丨价格:{str(O0000OO00O000OO0O)[:7]}')#line:323
        except Exception as OO0O0000O000O0O00 :#line:324
            print (OO0O0000O000O0O00 )#line:325
    def query_to_sell (OOO0O000O0O0O000O ):#line:328
        try :#line:329
            OOO0O0O000O00OOO0 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:330
            O0OOOOOOO0OO0O000 ={'source':'scsc','authorization':OOO0O000O0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O000O00OOO0 ),'signstring':OOO0O0O000O00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
            OOOO000O0OO0O0000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OOOOOOO0OO0O000 ).json ()#line:343
            if 'status'in OOOO000O0OO0O0000 :#line:345
                if OOOO000O0OO0O0000 ['status']==200 :#line:346
                    for OO0OO000000O000O0 in OOOO000O0OO0O0000 ['data']['rows']:#line:347
                        OO0O0O00O0OOOOO00 =OO0OO000000O000O0 ['materialKey']#line:348
                        O0OOOOO00OOO000OO =OO0OO000000O000O0 ['quantity']#line:349
                        O0000O0O000O000OO =OO0OO000000O000O0 ['price']#line:350
                        O00OOOO0O0OOOOO0O =OO0OO000000O000O0 ['saleState']#line:351
                        if O00OOOO0O0OOOOO0O ==0 :#line:352
                            print (f'【出售订单】:名称:{OO0O0O00O0OOOOO00}丨数量:{O0OOOOO00OOO000OO}丨价格:{O0000O0O000O000OO}')#line:353
                            O000O00OOOO0O0000 =OO0OO000000O000O0 ['id']#line:354
                            if float (datetime .datetime .now ().hour )>8 :#line:355
                                OOO0O000O0O0O000O .cacel_sale (O000O00OOOO0O0000 )#line:356
        except Exception as O0O00O00000OO0O0O :#line:357
            print (O0O00O00000OO0O0O )#line:358
    def cacel_sale (O00OO00O0000O0O0O ,O0O00O000OOOOOO00 ):#line:361
        try :#line:362
            O00000OO0O0O0OOOO =f'_saleId={O0O00O000OOOOOO00}_{timi_new()}'#line:363
            OO0OO000OO0O0OOOO ={'source':'scsc','authorization':O00OO00O0000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OO0O0O0OOOO ),'signstring':O00000OO0O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:374
            OOO00000O0OOOO00O ={"saleId":O0O00O000OOOOOO00 }#line:377
            OOOO0000OO00O0O0O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OO000OO0O0OOOO ,data =OOO00000O0OOOO00O ).json ()#line:378
            if 'status'in OOOO0000OO00O0O0O :#line:380
                if OOOO0000OO00O0O0O ['status']==200 :#line:381
                    print (f'【下架出售】:{OOOO0000OO00O0O0O["data"]}')#line:382
        except Exception as OO00O00O00OO0000O :#line:383
            print (OO00O00O00OO0000O )#line:384
    def change_nickname (OO0O000000O00OOOO ):#line:387
        try :#line:388
            O0O0O0OOOO000OO0O =timi_new ()#line:389
            O000O0OOOO0000O0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:390
            O0OOO00O0000000OO =requests .request ('post','https://www.qmsjmfb.com/',data =O000O0OOOO0000O0O ).text #line:391
            OOO0O00OOO0O00O0O =re .findall ('<ul><li>(.*?)</li>',O0OOO00O0000000OO )[0 ][:3 ]#line:392
            OO0OO00O0O00000O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO0O00OOO0O00O0O}').json ()#line:393
            OO0OO000O0O0O0OO0 =OO0OO00O0O00000O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:394
            O0O0O000O0000OOO0 ={"nickname":OO0OO000O0O0O0OO0 }#line:395
            OOO00O00OOO0OO0O0 =f'_nickname={OO0OO000O0O0O0OO0}_{O0O0O0OOOO000OO0O}'#line:396
            O0OO0O000OO00OOO0 ={'source':'scsc','authorization':OO0O000000O00OOOO .token ,'timestamp':O0O0O0OOOO000OO0O ,'sign':sign (OOO00O00OOO0OO0O0 ),'signstring':OOO00O00OOO0OO0O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:407
            OOOO00000O0OO0O00 =requests .request ('patch',f'{host}/user/nickname',headers =O0OO0O000OO00OOO0 ,data =O0O0O000O0000OOO0 ).json ()#line:408
            if 'status'in OOOO00000O0OO0O00 :#line:410
                if OOOO00000O0OO0O00 ['status']==200 :#line:411
                    print (f'【修改网名】:网名:{OO0OO000O0O0O0OO0}丨{OOOO00000O0OO0O00["message"]}')#line:412
        except Exception as O0OO000OO0O0O0OO0 :#line:413
            print (O0OO000OO0O0O0OO0 )#line:414
    def withdraw (O00O000OO0O0OO0OO ):#line:417
        try :#line:418
            OOOOO00OOO0000OO0 =f'__{timi_new()}'#line:419
            OOO0OO0000000O0O0 ={'source':'scsc','authorization':O00O000OO0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOO0000OO0 ),'signstring':OOOOO00OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:430
            O0O0O0O000O00O0OO =requests .request ('get',f'{host}/assets',headers =OOO0OO0000000O0O0 ).json ()#line:431
            if 'status'in O0O0O0O000O00O0OO :#line:433
                if O0O0O0O000O00O0OO ['status']==200 :#line:434
                    OO0OOO0OOOO000000 =O0O0O0O000O00O0OO ['data']['cash']#line:435
                    if float (OO0OOO0OOOO000000 )>20 :#line:436
                        OOOOO00OOO0000OO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:437
                        OOO0OO0000000O0O0 ={'authorization':O00O000OO0O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOO0000OO0 ),'signstring':OOOOO00OOO0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
                        OOO0OO000OO0OO0OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:448
                        O000O0O0O00OOOO00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO0OO0000000O0O0 ,data =OOO0OO000OO0OO0OO ).json ()#line:450
                        if 'status'in O000O0O0O00OOOO00 :#line:452
                            if O000O0O0O00OOOO00 ['status']==200 :#line:453
                                print (f'【余额提现】:{O000O0O0O00OOOO00["data"]}')#line:454
                        if 'status'in O000O0O0O00OOOO00 :#line:455
                            if O000O0O0O00OOOO00 ['status']==500 :#line:456
                                print (f'【余额提现】:{O000O0O0O00OOOO00["message"]}')#line:457
        except Exception as O0OOO00OO0O00000O :#line:458
            print (O0OOO00OO0O00000O )#line:459
    def invitenum (OOO000OOOOO000OOO ):#line:462
        global invited_new #line:463
        try :#line:464
            OOOO0OOOO0O00OO0O =f'__{timi_new()}'#line:465
            O0OO000000O0O000O ={'source':'scsc','authorization':OOO000OOOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOO0O00OO0O ),'signstring':OOOO0OOOO0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            O000O00OO0OO0OOO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0OO000000O0O000O ).json ()#line:477
            if 'status'in O000O00OO0OO0OOO0 :#line:479
                if O000O00OO0OO0OOO0 ['status']==200 :#line:480
                    O00OO0OO0OOOO000O =O000O00OO0OO0OOO0 ['data']['invited_count']#line:481
                    OOOO0OOO00O00O000 =O000O00OO0OO0OOO0 ['data']['invited_second_count']#line:482
                    print (f'【我的邀请】:直邀好友:{O00OO0OO0OOOO000O}丨间邀好友:{OOOO0OOO00O00O000}')#line:483
                    if O00OO0OO0OOOO000O <2 :#line:484
                        O00OOOOOOO00O0000 =f'__{timi_new()}'#line:485
                        O0OO0OO0OOO00O0OO ={'source':'scsc','authorization':OOO000OOOOO000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO00O0000 ),'signstring':O00OOOOOOO00O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:496
                        O000OOO0O000OO00O =requests .request ('get',f'{host}/user',headers =O0OO0OO0OOO00O0OO ).json ()#line:497
                        if 'status'in O000OOO0O000OO00O :#line:499
                            if O000OOO0O000OO00O ['status']==200 :#line:500
                                invited_new .append (O000OOO0O000OO00O ['data']['inner_id'])#line:501
        except Exception as O0OOOO000O0O000OO :#line:502
            print (O0OOOO000O0O000OO )#line:503
    def game_map (OOOOO0OO00O0O0OO0 ):#line:506
        try :#line:507
            OOOO000OOOO00OOO0 =f'__{timi_new()}'#line:508
            OO0OOO0O00OO0OOOO ={'source':'scsc','authorization':OOOOO0OO00O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OOOO00OOO0 ),'signstring':OOOO000OOOO00OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:519
            O0O00OOO0000O00OO =requests .request ('get',f'{host}/game/map',headers =OO0OOO0O00OO0OOOO ).json ()#line:520
            if 'status'in O0O00OOO0000O00OO :#line:522
                if O0O00OOO0000O00OO ['status']==200 :#line:523
                    for OOOO0OOOOOO0OO0OO in O0O00OOO0000O00OO ['data']['list'][0 ]['crops']:#line:524
                        O0O0OO0OO0O0000O0 =OOOO0OOOOOO0OO0OO ['level']#line:526
                        if O0O0OO0OO0O0000O0 ==41 :#line:527
                            O000OOOOO0OO0OO0O =OOOO0OOOOOO0OO0OO ['crop_name']#line:528
                            O00O0O00OO00OOO0O =OOOO0OOOOOO0OO0OO ['count']#line:529
                            if O00O0O00OO00OOO0O >0 :#line:530
                                print (f'【农业资产】:{O000OOOOO0OO0OO0O}丨数量:{O00O0O00OO00OOO0O}')#line:531
                                if float (datetime .datetime .now ().hour )>8 :#line:532
                                    OOOOO0OO00O0O0OO0 .the_query ()#line:533
        except Exception as OO0O0OOO00OOOO00O :#line:534
            print (OO0O0OOO00OOOO00O )#line:535
    def give_gold (OOO0O000OOOO0OO00 ):#line:538
        try :#line:539
            O00OOOO0OO0OO0O0O =f'__{timi_new()}'#line:540
            OOO00O000OO000O00 ={'source':'scsc','authorization':OOO0O000OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0OO0OO0O0O ),'signstring':O00OOOO0OO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            O0OOO00OOO00000O0 =requests .request ('get',f'{host}/user',headers =OOO00O000OO000O00 ).json ()#line:552
            if 'status'in O0OOO00OOO00000O0 :#line:553
                if O0OOO00OOO00000O0 ['status']==200 :#line:554
                    if float (OOO0O000OOOO0OO00 .doneeNo )!=0 :#line:555
                        O00000OO0O00OOOO0 =O0OOO00OOO00000O0 ['data']['assets']['gold']#line:556
                        if float (O00000OO0O00OOOO0 )>float (OOO0O000OOOO0OO00 .innerId ):#line:557
                            O00O0O00O000OO0O0 =int (float (O00000OO0O00OOOO0 )/1.1 )#line:558
                            O00OOOO0OO0OO0O0O =f'_doneeNo={OOO0O000OOOO0OO00.doneeNo}&quantity={O00O0O00O000OO0O0}_{timi_new()}'#line:559
                            OOO00O000OO000O00 ={'source':'scsc','authorization':OOO0O000OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0OO0OO0O0O ),'signstring':O00OOOO0OO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:570
                            OO000O000O0OOO000 ={"quantity":O00O0O00O000OO0O0 ,"doneeNo":OOO0O000OOOO0OO00 .doneeNo }#line:574
                            O0OOOO0OOO0OO0OOO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00O000OO000O00 ,data =OO000O000O0OOO000 ).json ()#line:575
                            if 'status'in O0OOOO0OOO0OO0OOO :#line:577
                                if O0OOOO0OOO0OO0OOO ['status']==200 :#line:578
                                    if O0OOOO0OOO0OO0OOO ['data']:#line:579
                                        print (f'【赠送种子】:赠送{O00O0O00O000OO0O0}种子给{OOO0O000OOOO0OO00.doneeNo}成功')#line:580
                    else :#line:581
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:582
        except Exception as OO00OO00OOO00O0O0 :#line:583
            print (OO00OO00OOO00O0O0 )#line:584
    def invitation (O0O000OO0000O0O0O ):#line:586
        try :#line:587
            _O0OO0O000O00O0OO0 =float (bundled_def ())/4 #line:588
            O0000O0OOO0O000OO =f'_innerId={int(_O0OO0O000O00O0OO0)}_{timi_new()}'#line:589
            OOO0OO0000OO0O0OO ={'source':'scsc','authorization':O0O000OO0000O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOO0O000OO ),'signstring':O0000O0OOO0O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOO0O00O0O0O0O000 ={"innerId":int (_O0OO0O000O00O0OO0 )}#line:601
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0OO0000OO0O0OO ,data =OOO0O00O0O0O0O000 )#line:602
        except Exception as OOO000O0OOO0OO0OO :#line:603
            print (OOO000O0OOO0OO0OO )#line:604
    def winning_rewards (OOOO0O00O0O000O0O ):#line:607
        try :#line:608
            O0O00O0000O00O0O0 =f'__{timi_new()}'#line:609
            O0OOOOOOO000OO000 ={'source':'scsc','authorization':OOOO0O00O0O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0000O00O0O0 ),'signstring':O0O00O0000O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
            OO00000O0000OO0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OOOOOOO000OO000 ).json ()#line:621
            if 'status'in OO00000O0000OO0OO :#line:623
                if OO00000O0000OO0OO ['status']==200 :#line:624
                    if OO00000O0000OO0OO ['data']['amount']:#line:625
                        OO0000O00OOO00OO0 =OO00000O0000OO0OO ['data']['amount']['gold']#line:626
                        return OO0000O00OOO00OO0 #line:627
                    else :#line:628
                        return 0 #line:629
        except Exception as O0OO0OO0OO00OO0O0 :#line:630
            print (O0OO0OO0OO00OO0O0 )#line:631
    def certification (O0OOO0O00000O0OOO ):#line:634
        try :#line:635
            OO0000OOO0OOO0O00 =f'__{timi_new()}'#line:636
            OO00O000OOO0O000O ={'source':'scsc','authorization':O0OOO0O00000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOO0OOO0O00 ),'signstring':OO0000OOO0OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:647
            OO000000O0OO0OOOO =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO00O000OOO0O000O ).json ()#line:648
            if 'status'in OO000000O0OO0OOOO :#line:650
                if OO000000O0OO0OOOO ['status']==200 :#line:651
                    if OO000000O0OO0OOOO ['data']['result']:#line:652
                        O0O0OO0O000OO0OOO =OO000000O0OO0OOOO ['data']['nick_name']#line:653
                        return O0O0OO0O000OO0OOO #line:654
                    else :#line:655
                        return '未实名'#line:656
        except Exception as OO00O0OOO0O00O000 :#line:657
            print (OO00O0OOO0O00O000 )#line:658
    def crops_illustrated (O0O0O0OO00OO0O0OO ):#line:661
        try :#line:662
            O0OOO0OOO000OO0OO =f'__{timi_new()}'#line:663
            O0O0O000O000O00OO ={'source':'scsc','authorization':O0O0O0OO00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000OO0OO ),'signstring':O0OOO0OOO000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:674
            OOO0O0O0OOOO0OO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O0O000O000O00OO ).json ()#line:675
            if 'status'in OOO0O0O0OOOO0OO00 :#line:677
                if OOO0O0O0OOOO0OO00 ['status']==200 :#line:678
                    OO0OO000O0OO00000 =OOO0O0O0OOOO0OO00 ['data'][0 ]['crops']#line:679
                    for O0000OOO00OO00OOO in OO0OO000O0OO00000 :#line:680
                        if O0000OOO00OO00OOO ['ill_clover_award']:#line:681
                            if float (O0000OOO00OO00OOO ['ill_clover_award'])>1 :#line:682
                                if O0000OOO00OO00OOO ['is_finish']:#line:683
                                    if not O0000OOO00OO00OOO ['is_getit']:#line:684
                                        if O0O0O0OO00OO0O0OO .certification ()!='未实名':#line:685
                                            O0OOO0OOO000OO0OO =f'_award_level={O0000OOO00OO00OOO["level"]}_{timi_new()}'#line:686
                                            O0O0O000O000O00OO ={'source':'scsc','authorization':O0O0O0OO00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000OO0OO ),'signstring':O0OOO0OOO000OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:697
                                            O0O0OO0O0O00O00O0 ={"award_level":O0000OOO00OO00OOO ['level']}#line:698
                                            O0O0OOO00O0OO0OOO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O0O000O000O00OO ,json =O0O0OO0O0O00O00O0 ).json ()#line:700
                                            if 'status'in O0O0OOO00O0OO0OOO :#line:701
                                                if O0O0OOO00O0OO0OOO ['status']==200 :#line:702
                                                    O000OO000O000OO0O =O0O0OOO00O0OO0OOO ['data']['ill_clover_award']#line:703
                                                    print (f'【图鉴奖励】:领取{O0000OOO00OO00OOO["crop_name"]}成就丨奖励{O000OO000O000OO0O}☘️')#line:705
                                                if O0O0OOO00O0OO0OOO ['status']==500 :#line:706
                                                    print (f'【图鉴奖励】:{O0O0OOO00O0OO0OOO["message"]}')#line:707
        except Exception as OOO0O00OO00O00000 :#line:708
            print (OOO0O00OO00O00000 )#line:709
    def watched_ad (OOO000O0O000O00O0 ):#line:712
        try :#line:713
            OO0OO0O00O0000OOO =f'__{timi_new()}'#line:714
            O0OO00O00O0O00O0O ={'source':'scsc','authorization':OOO000O0O000O00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00O0000OOO ),'signstring':OO0OO0O00O0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:725
            O0OOO00O00O000O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O00O0O00O0O ).json ()#line:726
            if 'status'in O0OOO00O00O000O0O :#line:728
                if O0OOO00O00O000O0O ['status']==200 :#line:729
                    if 'offlineInfo'in O0OOO00O00O000O0O ['data']:#line:730
                        time .sleep (random .randint (1 ,3 ))#line:731
                        O00OO0O0O00OOOO0O =O0OOO00O00O000O0O ['data']['offlineInfo']['off_minute']#line:732
                        OOO0O0OOOOOOO00O0 =float (O0OOO00O00O000O0O ['data']['silver'])/1000000000000 #line:733
                        time .sleep (1 )#line:734
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OO00O00O0O00O0O ).json ()#line:735
                        time .sleep (2 )#line:736
                        O00000OO000OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO00O00O0O00O0O ).json ()#line:737
                        if 'status'in O00000OO000OOO0OO :#line:739
                            if O00000OO000OOO0OO ['status']==200 :#line:740
                                O000O000O0OO00OO0 =float (O00000OO000OOO0OO ['data']['silver'])/1000000000000 #line:741
                                O0O00O0O0O0O0O0OO =str (O000O000O0OO00OO0 -OOO0O0OOOOOOO00O0 )[:6 ]#line:742
                                print (f'【离线奖励】:翻倍离线{O00OO0O0O00OOOO0O}分钟奖励🌱数量:{O0O00O0O0O0O0O0OO}t粒')#line:743
        except Exception as O0O0000O0O00O0O0O :#line:744
            print (O0O0000O0O00O0O0O )#line:745
    def user_ad (O0OOO0OOO0OOOO0OO ):#line:748
        try :#line:749
            OOO0O0OO0OOOO0OOO =f'__{timi_new()}'#line:750
            O0OOO0O0O000OOO0O ={'source':'scsc','authorization':O0OOO0OOO0OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO0OOOO0OOO ),'signstring':OOO0O0OO0OOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            OOOOO00OO000OOOO0 =requests .request ('get',f'{host}/user/ad',headers =O0OOO0O0O000OOO0O ).json ()#line:762
            if 'status'in OOOOO00OO000OOOO0 :#line:764
                if OOOOO00OO000OOOO0 ['status']==200 :#line:765
                    OOOOOOOO00OOO0000 =OOOOO00OO000OOOO0 ['data']['max_time']#line:766
                    O00OOO0OOO0000OO0 =OOOOO00OO000OOOO0 ['data']['watch_time']#line:767
                    O0O00O0OO00O0OO00 =OOOOO00OO000OOOO0 ['data']['added_time']#line:768
                    print (f'【获取种子】:获取🌱剩余{O0O00O0OO00O0OO00 + OOOOOOOO00OOO0000 - O00OOO0OOO0000OO0}次丨好友提供:{O0O00O0OO00O0OO00}次')#line:769
                    if O0O00O0OO00O0OO00 +OOOOOOOO00OOO0000 -O00OOO0OOO0000OO0 >0 :#line:770
                        time .sleep (random .randint (16 ,19 ))#line:771
                        O00O000OO0OOOOOO0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOO0O0O000OOO0O ).json ()#line:772
                        if 'status'in O00O000OO0OOOOOO0 :#line:774
                            if O00O000OO0OOOOOO0 ['status']==200 :#line:775
                                O0O00O0OOO0OOO0O0 =float (O00O000OO0OOOOOO0 ['data']['silver'])/1000000000000 #line:776
                                print (f'【获取种子】:获得🌱:{int(O0O00O0OOO0OOO0O0)}t粒')#line:777
                                return True #line:778
                            if O00O000OO0OOOOOO0 ['status']==500 :#line:779
                                O0OOO0OO0O00OO0O0 =O00O000OO0OOOOOO0 ['message']#line:780
                                print (f'【获取种子】:{O0OOO0OO0O00OO0O0}')#line:781
                                return False #line:782
        except Exception as O0O0OO0O0O000OOOO :#line:783
            print (O0O0OO0O0O000OOOO )#line:784
    def synthetic (O0O00000O0OO0OO00 ):#line:787
        global id ,g #line:788
        try :#line:789
            O0O0O0OO0O0000000 =O0O00000O0OO0OO00 .level_new ()#line:790
            O0OO0OO00O0OO000O =random .randint (9 ,11 )#line:791
            O000OOO0OO0OOO00O =f'_site=8&targetSite={O0OO0OO00O0OO000O}_{timi_new()}'#line:792
            O00OO0O0O000OO000 ={'source':'scsc','authorization':O0O00000O0OO0OO00 .token ,'timestamp':timi_new (),'sign':sign (O000OOO0OO0OOO00O ),'signstring':O000OOO0OO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:803
            OO0OO00OO0O000O00 ={"site":int (8 ),"targetSite":int (O0OO0OO00O0OO000O )}#line:804
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O0O000OO000 ,json =OO0OO00OO0O000O00 )#line:805
            while True :#line:806
                O00O0O00OOOOOO00O =f'__{timi_new()}'#line:807
                OOOO00OO0OO000OO0 ={'source':'scsc','authorization':O0O00000O0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00OOOOOO00O ),'signstring':O00O0O00OOOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:818
                OO0O0O0O0OOO000OO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OO0OO000OO0 ).json ()#line:819
                if 'status'in OO0O0O0O0OOO000OO :#line:821
                    if OO0O0O0O0OOO000OO ['status']==200 :#line:822
                        O0O0O0000O00OO0O0 =OO0O0O0O0OOO000OO ['data']['cropList']#line:823
                        O00O00OO000OOOOO0 =OO0O0O0O0OOO000OO ['data']['gameCoreDataDBid']#line:824
                        OOOO0O00OO0O00O00 =float (OO0O0O0O0OOO000OO ['data']['silver'])/1000000000000 #line:825
                        O0OO0OOO0000O0O00 =0 #line:830
                        for O0OO0O0OO00O00000 in O0O0O0000O00OO0O0 :#line:831
                            if not O0OO0O0OO00O00000 :#line:832
                                OO0O0O00O0O0O0OOO =f'_crop_id={O00O00OO000OOOOO0}&site={O0OO0OOO0000O0O00}_{O0O00000O0OO0OO00.time}'#line:833
                                OOOO00O0O000OOO0O ={'source':'scsc','authorization':O0O00000O0OO0OO00 .token ,'timestamp':O0O00000O0OO0OO00 .time ,'sign':sign (OO0O0O00O0O0O0OOO ),'signstring':OO0O0O00O0O0O0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
                                O0O000000OOOO00OO ={"site":O0OO0OOO0000O0O00 ,"crop_id":O00O00OO000OOOOO0 }#line:844
                                O0OOO0000O00O0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO00O0O000OOO0O ,data =O0O000000OOOO00OO ).json ()#line:845
                                time .sleep (random .randint (1 ,3 )/10 )#line:847
                                if 'status'in O0OOO0000O00O0O00 :#line:848
                                    if O0OOO0000O00O0O00 ['status']==200 :#line:849
                                        if O0OOO0000O00O0O00 ['message']=='种子数量不足':#line:850
                                            O0O0O0OO0O0000000 =O0O00000O0OO0OO00 .level_new ()#line:851
                                            print (f'【种植合成】:{O0OOO0000O00O0O00["message"]}')#line:852
                                            if not O0O00000O0OO0OO00 .user_ad ():#line:853
                                                return False #line:854
                                    if O0OOO0000O00O0O00 ['status']==500 :#line:855
                                        print (f'【种植合成】:{O0OOO0000O00O0O00["message"]}')#line:856
                                        return False #line:857
                            O0OO0OOO0000O0O00 +=1 #line:858
                        O000000O0O0OO0000 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO00OO0OO000OO0 ).json ()#line:859
                        OO00O0OO00O0O0O0O =O000000O0O0OO0000 ['data']['cropList']#line:860
                        OOOOO000O000OOOO0 =False #line:861
                        for O0OO0O0OO00O00000 in range (12 ):#line:862
                            id =OO00O0OO00O0O0O0O [O0OO0O0OO00O00000 ]['level']#line:863
                            if float (O0O0O0OO0O0000000 )-float (id )>9 :#line:864
                                OO00O0OO0000000OO =f'_site={O0OO0O0OO00O00000}_{timi_new()}'#line:865
                                O0OO0O0OOOOOO0OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00000O0OO0OO00 .token ,'timestamp':timi_new (),'sign':sign (OO00O0OO0000000OO ),'signstring':OO00O0OO0000000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:876
                                O00OO0O0OOOOOO0O0 ={"site":O0OO0O0OO00O00000 }#line:877
                                O0000OOOO00000OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O0OO0O0OOOOOO0OO0 ,data =O00OO0O0OOOOOO0O0 ).json ()#line:879
                                if 'status'in O0000OOOO00000OOO :#line:880
                                    if O0000OOOO00000OOO ['status']==200 :#line:881
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:882
                            if id !=0 :#line:883
                                for O0OOOO0OOOOO0O00O in range (11 ):#line:884
                                    OO0OOO0O0O000000O =O0OOOO0OOOOO0O00O +1 #line:885
                                    g =OO00O0OO00O0O0O0O [OO0OOO0O0O000000O ]['level']#line:886
                                    if id ==g :#line:887
                                        O0000OOOO000OO0O0 =O0OOOO0OOOOO0O00O +2 #line:888
                                        if O0000OOOO000OO0O0 !=O0OO0O0OO00O00000 +1 :#line:889
                                            O0O000OOO0OO0OO00 =O0OO0O0OO00O00000 +1 #line:890
                                            time .sleep (random .randint (1 ,3 )/10 )#line:892
                                            O000OOO0OO0OOO00O =f'_site={O0O000OOO0OO0OO00 - 1}&targetSite={O0000OOOO000OO0O0 - 1}_{timi_new()}'#line:893
                                            O00OO0O0O000OO000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00000O0OO0OO00 .token ,'timestamp':timi_new (),'sign':sign (O000OOO0OO0OOO00O ),'signstring':O000OOO0OO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:910
                                            O00O00O0O00O0OOOO ={"site":int (O0O000OOO0OO0OO00 -1 ),"targetSite":int (O0000OOOO000OO0O0 -1 )}#line:911
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0O0O000OO000 ,json =O00O00O0O00O0OOOO )#line:912
                                            OOOOO000O000OOOO0 =True #line:914
                                    if OOOOO000O000OOOO0 :#line:915
                                        break #line:916
                                if OOOOO000O000OOOO0 :#line:917
                                    break #line:918
        except :#line:919
            O0O00000O0OO0OO00 .synthetic ()#line:920
    def level_new (OOO0000OOOO000O0O ):#line:923
        try :#line:924
            OOOOO0O00OO00O00O =f'__{timi_new()}'#line:925
            O000OOOOO00O000O0 ={'source':'scsc','authorization':OOO0000OOOO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO00O00O ),'signstring':OOOOO0O00OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:936
            OOO000OO000O0000O =requests .request ('get',f'{host}/user',headers =O000OOOOO00O000O0 ).json ()#line:937
            if 'status'in OOO000OO000O0000O :#line:938
                if OOO000OO000O0000O ['status']==200 :#line:939
                    return float (OOO000OO000O0000O ['data']['level'])#line:940
        except Exception as OOO0OOOO0OOO0O0O0 :#line:941
            print (OOO0OOOO0OOO0O0O0 )#line:942
    def propsraffle (OOOO000000O00O0OO ):#line:945
        try :#line:946
            while True :#line:947
                O00000O0000OO00OO =f'__{timi_new()}'#line:948
                OOOO000000O00OOO0 ={'source':'scsc','authorization':OOOO000000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0000OO00OO ),'signstring':O00000O0000OO00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                OO0OO0O00O00O0O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOOO000000O00OOO0 ).json ()#line:960
                if 'status'in OO0OO0O00O00O0O0O :#line:962
                    if OO0OO0O00O00O0O0O ['status']==200 :#line:963
                        OO000O00OOOO0OOO0 =OO0OO0O00O00O0O0O ['data']['rows']#line:964
                        O00O0OO00OO0OOOO0 =OO0OO0O00O00O0O0O ['data']['vstate']#line:965
                        if OO000O00OOOO0OOO0 ==5 or OO000O00OOOO0OOO0 ==6 or OO000O00OOOO0OOO0 ==7 :#line:966
                            O0OOO0OO00O00O0OO =OO0OO0O00O00O0O0O ['data']['silver']#line:967
                            print (f'【转盘抽奖】:获得种子:{O0OOO0OO00O00O0OO}')#line:968
                        if OO000O00OOOO0OOO0 ==1 or OO000O00OOOO0OOO0 ==2 or OO000O00OOOO0OOO0 ==3 :#line:969
                            OOOOO0O0OOO0O0OO0 =OO0OO0O00O00O0O0O ['data']['clover']#line:970
                            print (f'【转盘抽奖】:获得三叶草:{OOOOO0O0OOO0O0OO0}')#line:971
                        if OO000O00OOOO0OOO0 ==4 or OO000O00OOOO0OOO0 ==8 :#line:972
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:973
                        if OO000O00OOOO0OOO0 =='抽奖次数已用完':#line:977
                            break #line:1011
                time .sleep (random .randint (8 ,15 )/10 )#line:1012
        except Exception as OO000OO00O000OOO0 :#line:1013
            print (OO000OO00O000OOO0 )#line:1014
    def friends_invitation (OO000O0O00000O00O ):#line:1017
        try :#line:1018
            O00O0O00O0O0000OO =f'__{timi_new()}'#line:1019
            O0O000OO000000OO0 ={'source':'scsc','authorization':OO000O0O00000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00O0O0000OO ),'signstring':O00O0O00O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1030
            OO0OO00OO00O000O0 =requests .request ('get',f'{host}/friends',headers =O0O000OO000000OO0 ).json ()#line:1031
            if 'status'in OO0OO00OO00O000O0 :#line:1032
                if OO0OO00OO00O000O0 ['status']==200 :#line:1033
                    O0OOO0000OO0O00OO =OO0OO00OO00O000O0 ['data']['myInviteter']#line:1034
                    if O0OOO0000OO0O00OO :#line:1035
                        OOO0O00O0O0O0O0OO =O0OOO0000OO0O00OO ['user']['nickname']#line:1036
                        OOOOO00O0OO0OO0OO =OO000O0O00000O00O .certification ()#line:1037
                        if OOOOO00O0OO0OO0OO =='未实名':#line:1038
                            weishim .append (OO000O0O00000O00O .token )#line:1039
                        print (f'【查邀请人】:我的邀请人:{OOO0O00O0O0O0O0OO}丨实名:{OOOOO00O0OO0OO0OO}')#line:1040
                    else :#line:1041
                        if OO000O0O00000O00O .innerId !='0':#line:1042
                            OO000O0O00000O00O .invitation ()#line:1043
        except Exception as OOOO0OOOOO0000OO0 :#line:1044
            print (OOOO0OOOOO0000OO0 )#line:1045
    def add_clover (O0O00OOO0000OOOO0 ):#line:1048
        global golden_seed #line:1049
        try :#line:1050
            OOO0OOO0OO00000O0 =f'__{timi_new()}'#line:1051
            OO00O00O00O000OO0 ={'source':'scsc','authorization':O0O00OOO0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO00000O0 ),'signstring':OOO0OOO0OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1062
            O00000OO000OOOO0O =requests .request ('get',f'{host}/assets/clovers',headers =OO00O00O00O000OO0 ).json ()#line:1063
            if 'status'in O00000OO000OOOO0O :#line:1065
                if O00000OO000OOOO0O ['status']==200 :#line:1066
                    O0O00OO0OO0OOOOOO =O00000OO000OOOO0O ['data']['clover']#line:1067
                    O0O0O00000O000OO0 =O00000OO000OOOO0O ['data']['used_clover']#line:1068
                    O0O00OOOOOOOOOO0O =float (O0O00OO0OO0OOOOOO )-float (O0O0O00000O000OO0 )#line:1069
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O00000O000OO0}')#line:1070
                    if O0O00OOO0000OOOO0 .certification ()!='未实名':#line:1071
                        if O0O00OOOOOOOOOO0O >1 :#line:1072
                            OOO0OOO0OO00000O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0O00OOOOOOOOOO0O)}_{timi_new()}'#line:1073
                            O00O0OOO0O0OO0OO0 ={'source':'scsc','authorization':O0O00OOO0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO00000O0 ),'signstring':OOO0OOO0OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1084
                            O0000000O0000OOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0O00OOOOOOOOOO0O )}#line:1085
                            O00OOOO0000O000O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O00O0OOO0O0OO0OO0 ,data =O0000000O0000OOOO ).json ()#line:1086
                            if 'status'in O00OOOO0000O000O0 :#line:1088
                                if O00OOOO0000O000O0 ['status']==200 :#line:1089
                                    print (f'【参与抽奖】:添加☘️:{O00OOOO0000O000O0["data"]}丨数量:{O0O00OOOOOOOOOO0O}')#line:1090
                                if O00OOOO0000O000O0 ['status']==500 :#line:1091
                                    print (f'【参与抽奖】:添加☘️:{O00OOOO0000O000O0["message"]}')#line:1092
            OO0OO00OOO0O0OO0O =requests .request ('get',f'{host}/lottery',headers =OO00O00O00O000OO0 ).json ()#line:1093
            O0OO00O0OOO00OO0O =O0O00OOO0000OOOO0 .winning_rewards ()#line:1095
            if 'status'in OO0OO00OOO0O0OO0O :#line:1096
                if OO0OO00OOO0O0OO0O ['status']==200 :#line:1097
                    O0O0OO00O00000O0O =OO0OO00OOO0O0OO0O ['data'][0 ]['day_get_gold_quantity']#line:1098
                    golden_seed +=float (O0O0OO00O00000O0O )#line:1099
                    O000OOO0OOO0OOOO0 =OO0OO00OOO0O0OO0O ['data'][1 ]['value']#line:1100
                    O0000000OO00OOO0O =OO0OO00OOO0O0OO0O ['data'][0 ]['join_number']#line:1101
                    OOO00OOO000OO0000 =int (float (OO0OO00OOO0O0OO0O ['data'][0 ]['totalValue']))#line:1102
                    O000O000O00OO0O0O =float (O000OOO0OOO0OOOO0 /OOO00OOO000OO0000 )*10000 #line:1103
                    O00OOOOOOOOOOO0O0 =OOO00OOO000OO0000 /O0000000OO00OOO0O #line:1104
                    print (f'【参与抽奖】:预计每天中{str(O0O0OO00O00000O0O)[:6]}颗金种子丨好友收益:{str(O0OO00O0OOO00OO0O)[:6]}')#line:1105
                    print (f'【抽奖统计】:每1万☘️中{str(O000O000O00OO0O0O)[:6]}颗金种子丨☘️人均:{str(O00OOOOOOOOOOO0O0)[:7]}️')#line:1106
        except Exception as OOOOOO0OO0OO00OO0 :#line:1107
            print (OOOOOO0OO0OO00OO0 )#line:1108
    def energy (O00O000O00OO0O0OO ):#line:1111
        try :#line:1112
            while True :#line:1113
                OOO0O000OOO0OO000 =f'__{timi_new()}'#line:1114
                OOOO000O00OO0OO00 ={'source':'scsc','authorization':O00O000O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000OOO0OO000 ),'signstring':OOO0O000OOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1125
                O0OOOOOOO0OOO0OO0 =requests .request ('get',f'{host}/energy/general',headers =OOOO000O00OO0OO00 ).json ()#line:1126
                if 'status'in O0OOOOOOO0OOO0OO0 :#line:1128
                    if O0OOOOOOO0OOO0OO0 ['status']==200 :#line:1129
                        O000O0OOO0000O0O0 =O0OOOOOOO0OOO0OO0 ['data']['ordinary_water']#line:1130
                        O0O0O0O0OOOOOO000 =O0OOOOOOO0OOO0OO0 ['data']['ordinary_fertilizer']#line:1131
                        O00000O0O0O0O00O0 =O0OOOOOOO0OOO0OO0 ['data']['videoStatus']#line:1132
                        O0O0O0000O0O00O00 =O0OOOOOOO0OOO0OO0 ['data']['waterVideoKey']#line:1133
                        print (f'【我的营养】:肥料:{str(O0O0O0O0OOOOOO000).split(".")[0]}丨水滴:{str(O000O0OOO0000O0O0).split(".")[0]}')#line:1135
                        if float (O0O0O0O0OOOOOO000 )<96 :#line:1136
                            if O00000O0O0O0O00O0 :#line:1137
                                time .sleep (random .randint (160 ,180 )/10 )#line:1138
                                O00O000OOOO00O000 =99 -float (O0O0O0O0OOOOOO000 )#line:1139
                                O0O0000OOOOOO0O0O ={"fertilizer":str (O00O000OOOO00O000 ).split ('.')[0 ]}#line:1140
                                OOOO000O00OOO0000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO000O00OO0OO00 ).json ()#line:1142
                                if 'status'in OOOO000O00OOO0000 :#line:1144
                                    if OOOO000O00OOO0000 ['status']==200 :#line:1145
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO000O00OOO0000["message"]}')#line:1146
                                    if OOOO000O00OOO0000 ['status']==500 :#line:1147
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO000O00OOO0000["message"]}')#line:1148
                                        break #line:1149
                                if float (O0O0O0O0OOOOOO000 )<78 :#line:1151
                                    O00O000OOOO00O000 =80 -float (O0O0O0O0OOOOOO000 )#line:1152
                                    OO00000OO000OOOO0 =f'_fertilizer={int(O00O000OOOO00O000)}_{timi_new()}'#line:1153
                                    OOOO0O000O0OO0O00 ={'source':'scsc','authorization':O00O000O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO000OOOO0 ),'signstring':OO00000OO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1164
                                    O00OO0OO0OO0O0O0O ={"fertilizer":int (O00O000OOOO00O000 )}#line:1165
                                    OO000000O00OO0OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0O000O0OO0O00 ,data =O00OO0OO0OO0O0O0O ).json ()#line:1167
                                    if 'status'in OO000000O00OO0OOO :#line:1169
                                        if OO000000O00OO0OOO ['status']==200 :#line:1170
                                            print (f'【购买肥料】:购买肥料:{OO000000O00OO0OOO["message"]}丨数量:{int(O00O000OOOO00O000)}')#line:1171
                                        if OO000000O00OO0OOO ['status']==500 :#line:1172
                                            print (f'【购买肥料】:购买肥料:{OO000000O00OO0OOO["message"]}丨数量:{int(O00O000OOOO00O000)}')#line:1173
                                            O0O000O00000O0OO0 =OO000000O00OO0OOO ["message"].split ('-')[1 ]#line:1174
                                            O0OO0O0O0O00OO00O =f'__{timi_new()}'#line:1175
                                            O0OOO0OO0O0OO0O0O ={'source':'scsc','authorization':O00O000O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0O00OO00O ),'signstring':O0OO0O0O0O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1186
                                            OOOOOO0OO0OO0O00O =requests .request ('get',f'{host}/user',headers =O0OOO0OO0O0OO0O0O ).json ()#line:1187
                                            if 'status'in OOOOOO0OO0OO0O00O :#line:1188
                                                if OOOOOO0OO0OO0O00O ['status']==200 :#line:1189
                                                    O000OOO000O0000O0 =OOOOOO0OO0OO0O00O ['data']['inner_id']#line:1190
                                                    if give_gold (O000OOO000O0000O0 ,float (O0O000O00000O0OO0 )+1 ):#line:1191
                                                        O00O000O00OO0O0OO .energy ()#line:1192
                        if float (O000O0OOO0000O0O0 )<880 :#line:1193
                            if O0O0O0000O0O00O00 :#line:1194
                                time .sleep (random .randint (160 ,180 )/10 )#line:1195
                                OOO0O0000000OOOOO =999 -float (O000O0OOO0000O0O0 )#line:1196
                                OO0OO000O00OOO0OO ={"water":str (OOO0O0000000OOOOO ).split ('.')[0 ]}#line:1197
                                O000OOOOOO0OO0OOO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO000O00OO0OO00 ).json ()#line:1199
                                if 'status'in O000OOOOOO0OO0OOO :#line:1201
                                    if O000OOOOOO0OO0OOO ['status']==200 :#line:1202
                                        print (f'【购买水滴】:看广告获取水滴:{O000OOOOOO0OO0OOO["message"]}')#line:1203
                                    if O000OOOOOO0OO0OOO ['status']==500 :#line:1204
                                        print (f'【购买水滴】:看广告获取水滴:{O000OOOOOO0OO0OOO["message"]}')#line:1205
                                        break #line:1206
                                if float (O000O0OOO0000O0O0 )<780 :#line:1207
                                    OOO0O0000000OOOOO =800 -float (O000O0OOO0000O0O0 )#line:1208
                                    O000OOOO00OO0OOO0 =f'_water={int(OOO0O0000000OOOOO)}_{timi_new()}'#line:1209
                                    OO00OOOOO00OOO0O0 ={'source':'scsc','authorization':O00O000O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOOO00OO0OOO0 ),'signstring':O000OOOO00OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                    OO0OOOOO0OO000000 ={"water":int (OOO0O0000000OOOOO )}#line:1221
                                    O0OO0O000O0OOOO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO00OOOOO00OOO0O0 ,data =OO0OOOOO0OO000000 ).json ()#line:1223
                                    if 'status'in O0OO0O000O0OOOO0O :#line:1225
                                        if O0OO0O000O0OOOO0O ['status']==200 :#line:1226
                                            print (f'【购买水滴】:购买水滴:{O0OO0O000O0OOOO0O["message"]}丨数量:{int(OOO0O0000000OOOOO)}')#line:1227
                                        if O0OO0O000O0OOOO0O ['status']==500 :#line:1228
                                            print (f'【购买水滴】:购买水滴:{O0OO0O000O0OOOO0O["message"]}丨数量:{int(OOO0O0000000OOOOO)}')#line:1229
                                            O0O000O00000O0OO0 =O0OO0O000O0OOOO0O ["message"].split ('-')[1 ]#line:1230
                                            O0OO0O0O0O00OO00O =f'__{timi_new()}'#line:1231
                                            O0OOO0OO0O0OO0O0O ={'source':'scsc','authorization':O00O000O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O0O0O00OO00O ),'signstring':O0OO0O0O0O00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1242
                                            OOOOOO0OO0OO0O00O =requests .request ('get',f'{host}/user',headers =O0OOO0OO0O0OO0O0O ).json ()#line:1243
                                            if 'status'in OOOOOO0OO0OO0O00O :#line:1244
                                                if OOOOOO0OO0OO0O00O ['status']==200 :#line:1245
                                                    O000OOO000O0000O0 =OOOOOO0OO0OO0O00O ['data']['inner_id']#line:1246
                                                    if give_gold (O000OOO000O0000O0 ,float (O0O000O00000O0OO0 )+1 ):#line:1247
                                                        O00O000O00OO0O0OO .energy ()#line:1248
                        break #line:1249
        except Exception as OOO00O00OO00000OO :#line:1250
            print (OOO00O00OO00000OO )#line:1251
def bundled_def ():#line:1254
    OOO0OOO0O0O0OOO0O =['5570536','7750212','7911652','7911680','7805624']#line:1255
    return OOO0OOO0O0O0OOO0O [random .randint (0 ,len (OOO0OOO0O0O0OOO0O )-1 )]#line:1256
def version_of_the_validation ():#line:1260
    return str ((95 -56 )/10 )#line:1261
def sc2 ():#line:1264
    return "19319#$%^&*((*"#line:1265
def OO00OO0OO0OO00OO00o0 ():#line:1268
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1270
def get_ip ():#line:1273
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1275
def gitee_validation ():#line:1278
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1279
def gitee_edition ():#line:1282
    try :#line:1283
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1284
    except :#line:1285
        sys .exit (0 )#line:1286
def O000OO000O0O00OOO00 ():#line:1290
    try :#line:1291
        O0OO0O00000OOOOOO =gitee_edition ()#line:1292
        if version_of_the_validation ()<O0OO0O00000OOOOOO ['CityEarth']['edition']:#line:1293
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0O00000OOOOOO["CityEarth"]["edition"]}   ❌')#line:1294
            print (f'更新内容=>>{O0OO0O00000OOOOOO["CityEarth"]["content"]}')#line:1295
        else :#line:1296
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO0O00000OOOOOO["CityEarth"]["edition"]}   ✅')#line:1297
            print (f'更新内容=>> {O0OO0O00000OOOOOO["CityEarth"]["content"]}')#line:1298
    except Exception as O0OOO0OO00OO0000O :#line:1299
        print (O0OOO0OO00OO0000O )#line:1300
def sc3 ():#line:1303
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1304
if __name__ =='__main__':#line:1307
    start ()#line:1308
