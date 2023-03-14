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
@ 版本  3.8
"""
##################################配置区##################################
time_xx = random.randint(15, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
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
        O00O0O0O0OO0O0OO0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O00O0O0O0OO0O0OO0)}个账号==========")#line:16
        for OO000000000000000 in O00O0O0O0OO0O0OO0 :#line:17
            O00O00OOOOOOO0OOO =[]#line:18
            print (f"------------正在执行第{O00O0O0O0OO0O0OO0.index(OO000000000000000) + 1}个账号------------")#line:19
            O00OOOO00O0000O00 =CityEarth (OO000000000000000 ,O00O00OOOOOOO0OOO ,O00O0O0O0OO0O0OO0 .index (OO000000000000000 ))#line:20
            def O00OOOOO00OO0OOO0 ():#line:22
                if O00OOOO00O0000O00 .base_info ():#line:24
                    O00OOOO00O0000O00 .sealing ()#line:26
                    O00OOOO00O0000O00 .invitenum ()#line:28
                    O00OOOO00O0000O00 .query_to_sell ()#line:30
                    O00OOOO00O0000O00 .game_map ()#line:32
                    O00OOOO00O0000O00 .friends_invitation ()#line:34
                    O00OOOO00O0000O00 .energy ()#line:36
                    O00OOOO00O0000O00 .add_clover ()#line:38
                    O00OOOO00O0000O00 .propsraffle ()#line:40
                    O00OOOO00O0000O00 .synthetic ()#line:42
                    O00OOOO00O0000O00 .crops_illustrated ()#line:44
                    O00OOOO00O0000O00 .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        O00OOOO00O0000O00 .give_gold ()#line:49
            O00O00OO000O00000 =threading .Thread (target =O00OOOOO00OO0OOO0 )#line:51
            O00O00OO000O00000 .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理推送通知------------")#line:54
        time .sleep (0.5 )#line:55
        O0O0OO0O0OO0OO0O0 =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0O0OO0O0OO0OO0O0 +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for O00OO00OO00000OO0 in invited_new :#line:60
            print (O00OO00OO00000OO0 )#line:61
        print ('开始打印未实名的token')#line:62
        for OO0O0O0000000OOOO in weishim :#line:63
            print (OO0O0O0000000OOOO )#line:64
    except Exception as OOO00OO0O00OOOOOO :#line:65
        print (OOO00OO0O00OOOOOO )#line:66
def give_gold (OO0O0OO00000OOOO0 ,OO0000OOOO0OOOOOO ):#line:70
    try :#line:71
        OO0OO0O0OO0OOOOOO =f'_doneeNo={OO0O0OO00000OOOO0}&quantity={int(OO0000OOOO0OOOOOO)}_{timi_new()}'#line:72
        OO00000000O0OO000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO0OOOOOO ),'signstring':OO0OO0O0OO0OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOOO0O0OOO0000OOO ={"quantity":int (OO0000OOOO0OOOOOO ),"doneeNo":OO0O0OO00000OOOO0 }#line:87
        O0OOO0OOO000O0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OO00000000O0OO000 ,data =OOOO0O0OOO0000OOO ).json ()#line:88
        if 'status'in O0OOO0OOO000O0O00 :#line:90
            if O0OOO0OOO000O0O00 ['status']==200 :#line:91
                if O0OOO0OOO000O0O00 ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OO0000OOOO0OOOOOO)}种子给{OO0O0OO00000OOOO0}成功')#line:93
                    return True #line:94
            if O0OOO0OOO000O0O00 ['status']==401 :#line:95
                print (f'【赠送种子】:{O0OOO0OOO000O0O00["message"]}')#line:96
                return False #line:97
            if O0OOO0OOO000O0O00 ['status']==500 :#line:98
                print (f'【赠送种子】:{O0OOO0OOO000O0O00["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as O00O0000O00OOO0OO :#line:102
        print (O00O0000O00OOO0OO )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def sign (O00O0OO00O0OOOO00 ):#line:110
    OOOOOOO0OOOO000O0 =hashlib .md5 (O00O0OO00O0OOOO00 .encode ()).hexdigest ()#line:111
    OOOOOO000OOOO0OO0 =sc1 ()#line:112
    OOO00OO0OOOO0O00O =sc2 ()#line:113
    O0O00O000O0O0OOOO =sc3 ()#line:114
    O0O000O0O0O0O0O00 =OOOOOO000OOOO0OO0 +OOOOOOO0OOOO000O0 +OOO00OO0OOOO0O00O +O0O00O000O0O0OOOO #line:115
    OO0O00OOOOO0OOOO0 =hashlib .md5 (O0O000O0O0O0O0O00 .encode ()).hexdigest ()#line:116
    return OO0O00OOOOO0OOOO0 #line:117
def format_msg ():#line:120
    OO00O00O0O000O00O =""#line:121
    for O00O0O0OO00O0O000 in msg_list :#line:122
        OO00O00O0O000O00O +=str (O00O0O0OO00O0O000 )+"\r\n"#line:123
    return OO00O00O0O000O00O #line:124
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
def get_json_data (OOO0O0O000O0O0OO0 ,OO0000O0000O0O0OO ,OO0000O000O000000 ,OO00OO00O0OOO0O00 ):#line:147
    with open (OOO0O0O000O0O0OO0 ,'rb')as O000O0O0000OOOOO0 :#line:148
        OOOOOO0O00OO0OOO0 =json .load (O000O0O0000OOOOO0 )#line:149
        OOOOOO0O00OO0OOO0 ['data'][OO0000O0000O0O0OO ][OO0000O000O000000 ]=OO00OO00O0OOO0O00 #line:150
        OO0O00000OO0OOO0O =OOOOOO0O00OO0OOO0 #line:151
    O000O0O0000OOOOO0 .close ()#line:152
    return OO0O00000OO0OOO0O #line:153
def write_json_data (OOO0O00O0O0O0OOO0 ):#line:156
    with open (json_path1 ,'w')as O0OOOO0O000000000 :#line:157
        json .dump (OOO0O00O0O0O0OOO0 ,O0OOOO0O000000000 )#line:158
    O0OOOO0O000000000 .close ()#line:159
    return True #line:160
class CityEarth :#line:163
    def __init__ (OOOO0OOOOOOO00OO0 ,OO000O0OOO0OO00O0 ,OOOOO000O0O0O0O00 ,O0OOO00O0000000OO ):#line:165
        try :#line:166
            OOOO0OOOOOOO00OO0 .msg =OOOOO000O0O0O0O00 #line:167
            OOOO0OOOOOOO00OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:168
            OOOO0OOOOOOO00OO0 .token =OO000O0OOO0OO00O0 ['authorization']#line:169
            OOOO0OOOOOOO00OO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:170
            OOOO0OOOOOOO00OO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:171
            OOOO0OOOOOOO00OO0 .elephant_user =OO000O0OOO0OO00O0 ['elephant_user']#line:172
            OOOO0OOOOOOO00OO0 .elephant_pswd =OO000O0OOO0OO00O0 ['elephant_pswd']#line:173
            OOOO0OOOOOOO00OO0 .elephant_Task_ID =OO000O0OOO0OO00O0 ['elephant_Task_ID']#line:174
            OOOO0OOOOOOO00OO0 .len_new =O0OOO00O0000000OO #line:175
        except :#line:176
            print ('变量格式错误')#line:177
    def base_info (O0O00O0O00O00000O ):#line:180
        try :#line:181
            O0O00O0O00O00000O .watched_ad ()#line:183
            O00OO00O00O000000 =f'__{timi_new()}'#line:184
            OO000OOOOOO0O00OO ={'source':'scsc','authorization':O0O00O0O00O00000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O00O000000 ),'signstring':O00OO00O00O000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
            OO0O0OO00OO000O0O =requests .request ('get',f'{host}/user',headers =OO000OOOOOO0O00OO ).json ()#line:196
            if 'status'in OO0O0OO00OO000O0O :#line:198
                if OO0O0OO00OO000O0O ['status']==200 :#line:199
                    O0O0O0O0O0O0O0O00 =OO0O0OO00OO000O0O ['data']['nickname']#line:200
                    O0OO0000OOO0O0O0O =OO0O0OO00OO000O0O ['data']['inner_id']#line:201
                    OOOOO0OO00OO000O0 =OO0O0OO00OO000O0O ['data']['assets']['gold']#line:202
                    OO000OOOO00OO00OO =OO0O0OO00OO000O0O ['data']['level']#line:203
                    print (f'【账号信息】:昵称:{O0O0O0O0O0O0O0O00[:5]}丨ID:{O0OO0000OOO0O0O0O}丨等级:{OO000OOOO00OO00OO}丨金种子:{str(OOOOO0OO00OO000O0).split(".")[0]}')#line:205
                    if 'wx_'in O0O0O0O0O0O0O0O00 :#line:206
                        O0O00O0O00O00000O .change_nickname ()#line:207
                if OO0O0OO00OO000O0O ['status']==401 :#line:208
                    print ('【账号信息】:账号失效正在尝试登录')#line:209
                    if O0O00O0O00O00000O .elephant_user =='f':#line:210
                        return False #line:211
                    O00O000OOOO0OOOOO =Invalid_login .addtask (elephant_user =O0O00O0O00O00000O .elephant_user ,elephant_pswd =O0O00O0O00O00000O .elephant_pswd ,elephant_Task_ID =O0O00O0O00O00000O .elephant_Task_ID )#line:214
                    OO0OO00OOO000000O =get_json_data (json_path ,O0O00O0O00O00000O .len_new ,'authorization',O00O000OOOO0OOOOO )#line:215
                    if write_json_data (OO0OO00OOO000000O ):#line:216
                        print ('正在写入账号配置文件')#line:217
                    return False #line:218
                if OO0O0OO00OO000O0O ['status']==500 :#line:219
                    return False #line:220
            return True #line:221
        except Exception as O0O0OO0O0OOO00O00 :#line:222
            print (O0O0OO0O0OOO00O00 )#line:223
    def sealing (O00O0000O00O00OOO ):#line:226
        try :#line:227
            OO0OO0O00O0O0000O =f'__{timi_new()}'#line:228
            OO0O0000OOO00O00O ={'source':'scsc','authorization':O00O0000O00O00OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O00O0O0000O ),'signstring':OO0OO0O00O0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO0O0000OOO00O00O )#line:240
            requests .request ('get',f'{host}/packsack/list',headers =OO0O0000OOO00O00O )#line:241
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO0O0000OOO00O00O )#line:242
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO0O0000OOO00O00O )#line:243
            requests .request ('get',f'{host}/user',headers =OO0O0000OOO00O00O )#line:244
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO0O0000OOO00O00O )#line:245
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO0O0000OOO00O00O )#line:246
            requests .request ('post',f'{host}/announcement/announcement',headers =OO0O0000OOO00O00O )#line:247
            requests .request ('get',f'{host}/game/getAllData',headers =OO0O0000OOO00O00O )#line:248
            requests .request ('get',f'{host}/assets',headers =OO0O0000OOO00O00O )#line:249
        except Exception as OOOOOOO0OOO0O00OO :#line:250
            print (OOOOOOO0OOO0O00OO )#line:251
    def the_query (O0OO00000O0O00O00 ):#line:254
        try :#line:255
            O00OOO00OO0OOO000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:256
            OO0OOO00OOOOO0OOO ={'authorization':O0OO00000O0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OO0OOO000 ),'signstring':O00OOO00OO0OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            OOOO00O0000O0O00O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0OOO00OOOOO0OOO ).json ()#line:268
            if 'status'in OOOO00O0000O0O00O :#line:270
                if OOOO00O0000O0O00O ['status']==200 :#line:271
                    O00O0OO00OO0OOO0O =OOOO00O0000O0O00O ['data']['rows'][3 ]['price']#line:272
                    O0OO00000O0O00O00 .market_sale (O00O0OO00OO0OOO0O )#line:273
        except Exception as OO0OOOO0O0OO0OOO0 :#line:274
            print (OO0OOOO0O0OO0OOO0 )#line:275
    def market_sale (O0000O00OOO0O0OO0 ,O0000OOO0O0O00OOO ):#line:278
        try :#line:279
            O0O00OO0OOOO00000 =timi_new ()#line:280
            OO00OOOO0OOO00OOO =f'type=crop__{O0O00OO0OOOO00000}'#line:281
            OO00O0O0000O0O0OO ={'source':'scsc','authorization':O0000O00OOO0O0OO0 .token ,'timestamp':str (O0O00OO0OOOO00000 ),'sign':sign (OO00OOOO0OOO00OOO ),'signstring':OO00OOOO0OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            OOOO00O000O0O0000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO00O0O0000O0O0OO ).json ()#line:294
            if 'status'in OOOO00O000O0O0000 :#line:296
                if OOOO00O000O0O0000 ['status']==200 :#line:297
                    if OOOO00O000O0O0000 ['data']['rows']:#line:298
                        OOOO00OOO0000O0OO =OOOO00O000O0O0000 ['data']['rows'][0 ]['packsackItemId']#line:299
                        OO00O0OO0000O0O00 =OOOO00O000O0O0000 ['data']['rows'][0 ]['quantity']#line:300
                        OOO0OO0OO0OO00O0O =float (O0000OOO0O0O00OOO )+float (random .randint (1 ,99 )*0.001 )#line:301
                        OO000000O0OOOOOOO =f'_packsackItemId={OOOO00OOO0000O0OO}&price={str(OOO0OO0OO0OO00O0O)[:7]}&quantity={OO00O0OO0000O0O00}_{O0O00OO0OOOO00000}'#line:302
                        OO0O0000O0000O0OO ={'source':'scsc','authorization':O0000O00OOO0O0OO0 .token ,'timestamp':str (O0O00OO0OOOO00000 ),'sign':sign (OO000000O0OOOOOOO ),'signstring':OO000000O0OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                        OOO0OOO0O0000O00O ={"packsackItemId":OOOO00OOO0000O0OO ,"price":str (OOO0OO0OO0OO00O0O )[:7 ],"quantity":str (OO00O0OO0000O0O00 )}#line:318
                        OO0O00O0OO0OOOO00 =requests .request ('post',f'{host}/market/sale',headers =OO0O0000O0000O0OO ,data =OOO0OOO0O0000O00O ).json ()#line:319
                        if 'status'in OO0O00O0OO0OOOO00 :#line:321
                            if OO0O00O0OO0OOOO00 ['status']==200 :#line:322
                                print (f'【上架芦荟】:数量:{OO00O0OO0000O0O00}丨价格:{str(OOO0OO0OO0OO00O0O)[:7]}')#line:323
        except Exception as O00000OO0O00OO00O :#line:324
            print (O00000OO0O00OO00O )#line:325
    def query_to_sell (O0OO0000OO00O000O ):#line:328
        try :#line:329
            OOOOOOOOO0OO0OO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:330
            OOO0OOO00OO0OOO00 ={'source':'scsc','authorization':O0OO0000OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOO0OO0OO00 ),'signstring':OOOOOOOOO0OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
            OO0OO00O000OOO000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0OOO00OO0OOO00 ).json ()#line:343
            if 'status'in OO0OO00O000OOO000 :#line:345
                if OO0OO00O000OOO000 ['status']==200 :#line:346
                    for OOOOO0O0OOOO0O0OO in OO0OO00O000OOO000 ['data']['rows']:#line:347
                        OOO00O0O0OO00O000 =OOOOO0O0OOOO0O0OO ['materialKey']#line:348
                        OO0O0O0OO00O00O00 =OOOOO0O0OOOO0O0OO ['quantity']#line:349
                        OO0OOO0O000OOO00O =OOOOO0O0OOOO0O0OO ['price']#line:350
                        O0OO00O000O0000OO =OOOOO0O0OOOO0O0OO ['saleState']#line:351
                        if O0OO00O000O0000OO ==0 :#line:352
                            print (f'【出售订单】:名称:{OOO00O0O0OO00O000}丨数量:{OO0O0O0OO00O00O00}丨价格:{OO0OOO0O000OOO00O}')#line:353
                            OO0O00O0O000000OO =OOOOO0O0OOOO0O0OO ['id']#line:354
                            O0OO0000OO00O000O .cacel_sale (OO0O00O0O000000OO )#line:355
        except Exception as OOOO000OO0O0O0000 :#line:356
            print (OOOO000OO0O0O0000 )#line:357
    def cacel_sale (OO000000000OO00O0 ,OO000O0O00OO0OOOO ):#line:360
        try :#line:361
            OOOOO00O0000OOO00 =f'_saleId={OO000O0O00OO0OOOO}_{timi_new()}'#line:362
            O0OOO0O0O000OO0OO ={'source':'scsc','authorization':OO000000000OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00O0000OOO00 ),'signstring':OOOOO00O0000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:373
            O0O00O00O00O0OOOO ={"saleId":OO000O0O00OO0OOOO }#line:376
            OO0O0O00O00O0O0O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0OOO0O0O000OO0OO ,data =O0O00O00O00O0OOOO ).json ()#line:377
            if 'status'in OO0O0O00O00O0O0O0 :#line:379
                if OO0O0O00O00O0O0O0 ['status']==200 :#line:380
                    print (f'【下架出售】:{OO0O0O00O00O0O0O0["data"]}')#line:381
        except Exception as OO0OOOOOO0O00O0OO :#line:382
            print (OO0OOOOOO0O00O0OO )#line:383
    def change_nickname (OOOO00OOO0000OOOO ):#line:386
        try :#line:387
            O00OOOO0OO0OOO0O0 =timi_new ()#line:388
            OO00OO0O0O0OOOO0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:389
            O00000O00OOO00O00 =requests .request ('post','https://www.qmsjmfb.com/',data =OO00OO0O0O0OOOO0O ).text #line:390
            OO0OO000O000O000O =re .findall ('<ul><li>(.*?)</li>',O00000O00OOO00O00 )[0 ][:3 ]#line:391
            O0O0OOO0OOO0OO0OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0OO000O000O000O}').json ()#line:392
            OO0OOO000O0000OO0 =O0O0OOO0OOO0OO0OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:393
            O0O0O0OO00O00O00O ={"nickname":OO0OOO000O0000OO0 }#line:394
            OOOO0O00O0OOO00O0 =f'_nickname={OO0OOO000O0000OO0}_{O00OOOO0OO0OOO0O0}'#line:395
            OO0O0000OO00OO000 ={'source':'scsc','authorization':OOOO00OOO0000OOOO .token ,'timestamp':O00OOOO0OO0OOO0O0 ,'sign':sign (OOOO0O00O0OOO00O0 ),'signstring':OOOO0O00O0OOO00O0 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:406
            OO0000000O0OOOO0O =requests .request ('patch',f'{host}/user/nickname',headers =OO0O0000OO00OO000 ,data =O0O0O0OO00O00O00O ).json ()#line:407
            if 'status'in OO0000000O0OOOO0O :#line:409
                if OO0000000O0OOOO0O ['status']==200 :#line:410
                    print (f'【修改网名】:网名:{OO0OOO000O0000OO0}丨{OO0000000O0OOOO0O["message"]}')#line:411
        except Exception as O00000OOO00O0O00O :#line:412
            print (O00000OOO00O0O00O )#line:413
    def withdraw (OOO00000000OO0OOO ):#line:416
        try :#line:417
            OO0O0OOO000OOOOO0 =f'__{timi_new()}'#line:418
            OOOOOOOOOO00OOOOO ={'source':'scsc','authorization':OOO00000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000OOOOO0 ),'signstring':OO0O0OOO000OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:429
            OO00O000O000O000O =requests .request ('get',f'{host}/assets',headers =OOOOOOOOOO00OOOOO ).json ()#line:430
            if 'status'in OO00O000O000O000O :#line:432
                if OO00O000O000O000O ['status']==200 :#line:433
                    O0OO0O0OOOO0O00OO =OO00O000O000O000O ['data']['cash']#line:434
                    if float (O0OO0O0OOOO0O00OO )>20 :#line:435
                        OO0O0OOO000OOOOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:436
                        OOOOOOOOOO00OOOOO ={'authorization':OOO00000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOO000OOOOO0 ),'signstring':OO0O0OOO000OOOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:446
                        O0OO00OOOO0OO000O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:447
                        O0000OOOOOOO0O0OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOOOOOOOO00OOOOO ,data =O0OO00OOOO0OO000O ).json ()#line:449
                        if 'status'in O0000OOOOOOO0O0OO :#line:451
                            if O0000OOOOOOO0O0OO ['status']==200 :#line:452
                                print (f'【余额提现】:{O0000OOOOOOO0O0OO["data"]}')#line:453
                        if 'status'in O0000OOOOOOO0O0OO :#line:454
                            if O0000OOOOOOO0O0OO ['status']==500 :#line:455
                                print (f'【余额提现】:{O0000OOOOOOO0O0OO["message"]}')#line:456
        except Exception as O0O000OOO0OO0OOO0 :#line:457
            print (O0O000OOO0OO0OOO0 )#line:458
    def invitenum (O0O00O0O0O0OOO0OO ):#line:461
        global invited_new #line:462
        try :#line:463
            OO000OOOOO00OOOOO =f'__{timi_new()}'#line:464
            O0O000000OOOOO000 ={'source':'scsc','authorization':O0O00O0O0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOO00OOOOO ),'signstring':OO000OOOOO00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:475
            OOOOOOO00O0OO0OO0 =requests .request ('get',f'{host}/invite/invitenum',headers =O0O000000OOOOO000 ).json ()#line:476
            if 'status'in OOOOOOO00O0OO0OO0 :#line:478
                if OOOOOOO00O0OO0OO0 ['status']==200 :#line:479
                    OO00OO00OOOOO0O0O =OOOOOOO00O0OO0OO0 ['data']['invited_count']#line:480
                    OO0000O00OO0OOOO0 =OOOOOOO00O0OO0OO0 ['data']['invited_second_count']#line:481
                    print (f'【我的邀请】:直邀好友:{OO00OO00OOOOO0O0O}丨间邀好友:{OO0000O00OO0OOOO0}')#line:482
                    if OO00OO00OOOOO0O0O <2 :#line:483
                        OO0O00O00OO0OO000 =f'__{timi_new()}'#line:484
                        O0O00O0O0O00OOO0O ={'source':'scsc','authorization':O0O00O0O0O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OO0OO000 ),'signstring':OO0O00O00OO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:495
                        OOO0O0O0OOO00O00O =requests .request ('get',f'{host}/user',headers =O0O00O0O0O00OOO0O ).json ()#line:496
                        if 'status'in OOO0O0O0OOO00O00O :#line:498
                            if OOO0O0O0OOO00O00O ['status']==200 :#line:499
                                invited_new .append (OOO0O0O0OOO00O00O ['data']['inner_id'])#line:500
        except Exception as OOO00000OOOO0OOOO :#line:501
            print (OOO00000OOOO0OOOO )#line:502
    def game_map (O000OO0OOO0OO0OOO ):#line:505
        try :#line:506
            O0OOOOOOO0O00O00O =f'__{timi_new()}'#line:507
            OOO00OO0O0O0OOOO0 ={'source':'scsc','authorization':O000OO0OOO0OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOOO0O00O00O ),'signstring':O0OOOOOOO0O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:518
            OO0O000OOOOOOOO0O =requests .request ('get',f'{host}/game/map',headers =OOO00OO0O0O0OOOO0 ).json ()#line:519
            if 'status'in OO0O000OOOOOOOO0O :#line:521
                if OO0O000OOOOOOOO0O ['status']==200 :#line:522
                    for OOOOO0OOO00OOOOOO in OO0O000OOOOOOOO0O ['data']['list'][0 ]['crops']:#line:523
                        O0OO00OO0OO0O000O =OOOOO0OOO00OOOOOO ['level']#line:525
                        if O0OO00OO0OO0O000O ==41 :#line:526
                            O000000O0O00OOOOO =OOOOO0OOO00OOOOOO ['crop_name']#line:527
                            O00O0000OOO0O0OO0 =OOOOO0OOO00OOOOOO ['count']#line:528
                            if O00O0000OOO0O0OO0 >0 :#line:529
                                print (f'【农业资产】:{O000000O0O00OOOOO}丨数量:{O00O0000OOO0O0OO0}')#line:530
                                O000OO0OOO0OO0OOO .the_query ()#line:531
        except Exception as OO000OO0O0OOO000O :#line:532
            print (OO000OO0O0OOO000O )#line:533
    def give_gold (OO0O0O0000OO0O0OO ):#line:536
        try :#line:537
            O0O0O0OO00O00O000 =f'__{timi_new()}'#line:538
            O0000OOO000OOO0OO ={'source':'scsc','authorization':OO0O0O0000OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO00O00O000 ),'signstring':O0O0O0OO00O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:549
            O0OOO0000000000OO =requests .request ('get',f'{host}/user',headers =O0000OOO000OOO0OO ).json ()#line:550
            if 'status'in O0OOO0000000000OO :#line:551
                if O0OOO0000000000OO ['status']==200 :#line:552
                    if float (OO0O0O0000OO0O0OO .doneeNo )!=0 :#line:553
                        O0OO0O0OOO000OO0O =O0OOO0000000000OO ['data']['assets']['gold']#line:554
                        if float (O0OO0O0OOO000OO0O )>float (OO0O0O0000OO0O0OO .innerId ):#line:555
                            O000OOOO000O00OO0 =int (float (O0OO0O0OOO000OO0O )/1.1 )#line:556
                            O0O0O0OO00O00O000 =f'_doneeNo={OO0O0O0000OO0O0OO.doneeNo}&quantity={O000OOOO000O00OO0}_{timi_new()}'#line:557
                            O0000OOO000OOO0OO ={'source':'scsc','authorization':OO0O0O0000OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO00O00O000 ),'signstring':O0O0O0OO00O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:568
                            O00000O0OOOOOOO0O ={"quantity":O000OOOO000O00OO0 ,"doneeNo":OO0O0O0000OO0O0OO .doneeNo }#line:572
                            O0O0OO0O00O000OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0000OOO000OOO0OO ,data =O00000O0OOOOOOO0O ).json ()#line:573
                            if 'status'in O0O0OO0O00O000OO0 :#line:575
                                if O0O0OO0O00O000OO0 ['status']==200 :#line:576
                                    if O0O0OO0O00O000OO0 ['data']:#line:577
                                        print (f'【赠送种子】:赠送{O000OOOO000O00OO0}种子给{OO0O0O0000OO0O0OO.doneeNo}成功')#line:578
                    else :#line:579
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:580
        except Exception as OOO0OO0OOOO000O0O :#line:581
            print (OOO0OO0OOOO000O0O )#line:582
    def invitation (O00O000O0000OOO00 ):#line:584
        try :#line:585
            _OO0OOOOO00OOO0O00 =float (bundled_def ())/4 #line:586
            O00OOOOO000O00O0O =f'_innerId={int(_OO0OOOOO00OOO0O00)}_{timi_new()}'#line:587
            OOOOO00O0OOOO0OOO ={'source':'scsc','authorization':O00O000O0000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO000O00O0O ),'signstring':O00OOOOO000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:598
            OO0OOO0O0O00O0O00 ={"innerId":int (_OO0OOOOO00OOO0O00 )}#line:599
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOOO00O0OOOO0OOO ,data =OO0OOO0O0O00O0O00 )#line:600
        except Exception as OOOOOOOOO0O0OOO00 :#line:601
            print (OOOOOOOOO0O0OOO00 )#line:602
    def winning_rewards (O000O00OOOO00O000 ):#line:605
        try :#line:606
            O0O00O0OO000O000O =f'__{timi_new()}'#line:607
            O0OO0OOOO0O0O00O0 ={'source':'scsc','authorization':O000O00OOOO00O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO000O000O ),'signstring':O0O00O0OO000O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:618
            O000O00OO00O00000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0OO0OOOO0O0O00O0 ).json ()#line:619
            if 'status'in O000O00OO00O00000 :#line:621
                if O000O00OO00O00000 ['status']==200 :#line:622
                    if O000O00OO00O00000 ['data']['amount']:#line:623
                        O0O00OO0OOO00000O =O000O00OO00O00000 ['data']['amount']['gold']#line:624
                        return O0O00OO0OOO00000O #line:625
                    else :#line:626
                        return 0 #line:627
        except Exception as O000O00000OOOO0OO :#line:628
            print (O000O00000OOOO0OO )#line:629
    def certification (O0O0O00OOO0O0OOO0 ):#line:632
        try :#line:633
            OOOOO00OOO00OO0OO =f'__{timi_new()}'#line:634
            O00OO00000OO0O0OO ={'source':'scsc','authorization':O0O0O00OOO0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00OOO00OO0OO ),'signstring':OOOOO00OOO00OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:645
            O00O0OO00O00000OO =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO00000OO0O0OO ).json ()#line:646
            if 'status'in O00O0OO00O00000OO :#line:648
                if O00O0OO00O00000OO ['status']==200 :#line:649
                    if O00O0OO00O00000OO ['data']['result']:#line:650
                        OO0OOOO00OOOO000O =O00O0OO00O00000OO ['data']['nick_name']#line:651
                        return OO0OOOO00OOOO000O #line:652
                    else :#line:653
                        weishim .append (O0O0O00OOO0O0OOO0 .token )#line:654
                        return '未实名'#line:655
        except Exception as O0OOOOOOO0O000OO0 :#line:656
            print (O0OOOOOOO0O000OO0 )#line:657
    def crops_illustrated (O0OOOO0O00OOO0O00 ):#line:660
        try :#line:661
            OOOO00OO0OOOO0O0O =f'__{timi_new()}'#line:662
            OO0O0O000OOOO000O ={'source':'scsc','authorization':O0OOOO0O00OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0OOOO0O0O ),'signstring':OOOO00OO0OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:673
            OOOOOO00O00O0O00O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0O000OOOO000O ).json ()#line:674
            if 'status'in OOOOOO00O00O0O00O :#line:676
                if OOOOOO00O00O0O00O ['status']==200 :#line:677
                    O00OO00O000OOO0O0 =OOOOOO00O00O0O00O ['data'][0 ]['crops']#line:678
                    for O00OOO00O000O0OO0 in O00OO00O000OOO0O0 :#line:679
                        if O00OOO00O000O0OO0 ['ill_clover_award']:#line:680
                            if float (O00OOO00O000O0OO0 ['ill_clover_award'])>1 :#line:681
                                if O00OOO00O000O0OO0 ['is_finish']:#line:682
                                    if not O00OOO00O000O0OO0 ['is_getit']:#line:683
                                        if O0OOOO0O00OOO0O00 .certification ()!='未实名':#line:684
                                            OOOO00OO0OOOO0O0O =f'_award_level={O00OOO00O000O0OO0["level"]}_{timi_new()}'#line:685
                                            OO0O0O000OOOO000O ={'source':'scsc','authorization':O0OOOO0O00OOO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO0OOOO0O0O ),'signstring':OOOO00OO0OOOO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:696
                                            O0OO0O0O00OOO0OO0 ={"award_level":O00OOO00O000O0OO0 ['level']}#line:697
                                            OOO00OO0000OO0O0O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0O000OOOO000O ,json =O0OO0O0O00OOO0OO0 ).json ()#line:699
                                            if 'status'in OOO00OO0000OO0O0O :#line:700
                                                if OOO00OO0000OO0O0O ['status']==200 :#line:701
                                                    O0OOO00O000O0O00O =OOO00OO0000OO0O0O ['data']['ill_clover_award']#line:702
                                                    print (f'【图鉴奖励】:领取{O00OOO00O000O0OO0["crop_name"]}成就丨奖励{O0OOO00O000O0O00O}☘️')#line:704
                                                if OOO00OO0000OO0O0O ['status']==500 :#line:705
                                                    print (f'【图鉴奖励】:{OOO00OO0000OO0O0O["message"]}')#line:706
        except Exception as OOO0OO00O0O00OOOO :#line:707
            print (OOO0OO00O0O00OOOO )#line:708
    def watched_ad (OO0O0OO00OO0OO00O ):#line:711
        try :#line:712
            O00000O00000OOO00 =f'__{timi_new()}'#line:713
            O000O0OO0O0OO0000 ={'source':'scsc','authorization':OO0O0OO00OO0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O00000OOO00 ),'signstring':O00000O00000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:724
            OO0O00O0O000OOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OO0O0OO0000 ).json ()#line:725
            if 'status'in OO0O00O0O000OOOOO :#line:727
                if OO0O00O0O000OOOOO ['status']==200 :#line:728
                    if 'offlineInfo'in OO0O00O0O000OOOOO ['data']:#line:729
                        time .sleep (random .randint (1 ,3 ))#line:730
                        OO0OO00O0O00OOOO0 =OO0O00O0O000OOOOO ['data']['offlineInfo']['off_minute']#line:731
                        OOOOOOOO000O0OOOO =float (OO0O00O0O000OOOOO ['data']['silver'])/1000000000000 #line:732
                        time .sleep (1 )#line:733
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000O0OO0O0OO0000 ).json ()#line:734
                        time .sleep (2 )#line:735
                        OO000O00O0OOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O000O0OO0O0OO0000 ).json ()#line:736
                        if 'status'in OO000O00O0OOOOOOO :#line:738
                            if OO000O00O0OOOOOOO ['status']==200 :#line:739
                                OOOOOO00OO000O000 =float (OO000O00O0OOOOOOO ['data']['silver'])/1000000000000 #line:740
                                O00O0OO000OOOO000 =str (OOOOOO00OO000O000 -OOOOOOOO000O0OOOO )[:6 ]#line:741
                                print (f'【离线奖励】:翻倍离线{OO0OO00O0O00OOOO0}分钟奖励🌱数量:{O00O0OO000OOOO000}t粒')#line:742
        except Exception as OOO000O000O000000 :#line:743
            print (OOO000O000O000000 )#line:744
    def user_ad (O00000OO0O000OO00 ):#line:747
        try :#line:748
            O0O00O00O0OO0OOO0 =f'__{timi_new()}'#line:749
            O000OOO0000OO0OOO ={'source':'scsc','authorization':O00000OO0O000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00O0OO0OOO0 ),'signstring':O0O00O00O0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:760
            OO00OO0O000000OO0 =requests .request ('get',f'{host}/user/ad',headers =O000OOO0000OO0OOO ).json ()#line:761
            if 'status'in OO00OO0O000000OO0 :#line:763
                if OO00OO0O000000OO0 ['status']==200 :#line:764
                    OO00O0O00OO0O0OO0 =OO00OO0O000000OO0 ['data']['max_time']#line:765
                    O00O0O00O0O0000OO =OO00OO0O000000OO0 ['data']['watch_time']#line:766
                    O00OO0OOOOO0000OO =OO00OO0O000000OO0 ['data']['added_time']#line:767
                    print (f'【获取种子】:获取🌱剩余{O00OO0OOOOO0000OO + OO00O0O00OO0O0OO0 - O00O0O00O0O0000OO}次丨好友提供:{O00OO0OOOOO0000OO}次')#line:768
                    if O00OO0OOOOO0000OO +OO00O0O00OO0O0OO0 -O00O0O00O0O0000OO >0 :#line:769
                        time .sleep (random .randint (16 ,19 ))#line:770
                        OO00O0OO0OOOO00O0 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000OOO0000OO0OOO ).json ()#line:771
                        if 'status'in OO00O0OO0OOOO00O0 :#line:773
                            if OO00O0OO0OOOO00O0 ['status']==200 :#line:774
                                OOOOOO000O00O0OO0 =float (OO00O0OO0OOOO00O0 ['data']['silver'])/1000000000000 #line:775
                                print (f'【获取种子】:获得🌱:{int(OOOOOO000O00O0OO0)}t粒')#line:776
                                return True #line:777
                            if OO00O0OO0OOOO00O0 ['status']==500 :#line:778
                                OO0O0000O000O0OOO =OO00O0OO0OOOO00O0 ['message']#line:779
                                print (f'【获取种子】:{OO0O0000O000O0OOO}')#line:780
                                return False #line:781
        except Exception as O00OOOO0OO00OOOO0 :#line:782
            print (O00OOOO0OO00OOOO0 )#line:783
    def synthetic (OOO00OO000O000O0O ):#line:786
        global id ,g #line:787
        try :#line:788
            O0O0000OOOO0O0OOO =OOO00OO000O000O0O .level_new ()#line:789
            OOOO00OO00OOO0OO0 =random .randint (9 ,11 )#line:790
            OO00OO0OOO0O0OOO0 =f'_site=8&targetSite={OOOO00OO00OOO0OO0}_{timi_new()}'#line:791
            OOO000OO00OOO00O0 ={'source':'scsc','authorization':OOO00OO000O000O0O .token ,'timestamp':timi_new (),'sign':sign (OO00OO0OOO0O0OOO0 ),'signstring':OO00OO0OOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:802
            OO00OOOO0O00O0O0O ={"site":int (8 ),"targetSite":int (OOOO00OO00OOO0OO0 )}#line:803
            requests .request ('post',f'{host}/game/crops/move',headers =OOO000OO00OOO00O0 ,json =OO00OOOO0O00O0O0O )#line:804
            while True :#line:805
                O0OOO0OO00OOOOOOO =f'__{timi_new()}'#line:806
                OO00O0OOOOO0O00O0 ={'source':'scsc','authorization':OOO00OO000O000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OO00OOOOOOO ),'signstring':O0OOO0OO00OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:817
                OO0O00O0OO0OOO00O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OOOOO0O00O0 ).json ()#line:818
                if 'status'in OO0O00O0OO0OOO00O :#line:820
                    if OO0O00O0OO0OOO00O ['status']==200 :#line:821
                        O0O0OOO0OO0O0OO0O =OO0O00O0OO0OOO00O ['data']['cropList']#line:822
                        O0OO0000O0O0O0000 =OO0O00O0OO0OOO00O ['data']['gameCoreDataDBid']#line:823
                        OOO000O0OOO00O0O0 =float (OO0O00O0OO0OOO00O ['data']['silver'])/1000000000000 #line:824
                        OO00OOOO00OOOO0OO =0 #line:829
                        for O00OOO0000OOOOOOO in O0O0OOO0OO0O0OO0O :#line:830
                            if not O00OOO0000OOOOOOO :#line:831
                                O000O0OOOO0OOO00O =f'_crop_id={O0OO0000O0O0O0000}&site={OO00OOOO00OOOO0OO}_{OOO00OO000O000O0O.time}'#line:832
                                OO00OO00O0OOO00OO ={'source':'scsc','authorization':OOO00OO000O000O0O .token ,'timestamp':OOO00OO000O000O0O .time ,'sign':sign (O000O0OOOO0OOO00O ),'signstring':O000O0OOOO0OOO00O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:842
                                O00OOO00O0OOOOO0O ={"site":OO00OOOO00OOOO0OO ,"crop_id":O0OO0000O0O0O0000 }#line:843
                                O0O0OO00000O0O0OO =requests .request ('post',f'{host}/game/crops/buy',headers =OO00OO00O0OOO00OO ,data =O00OOO00O0OOOOO0O ).json ()#line:844
                                time .sleep (random .randint (1 ,3 )/10 )#line:846
                                if 'status'in O0O0OO00000O0O0OO :#line:847
                                    if O0O0OO00000O0O0OO ['status']==200 :#line:848
                                        if O0O0OO00000O0O0OO ['message']=='种子数量不足':#line:849
                                            O0O0000OOOO0O0OOO =OOO00OO000O000O0O .level_new ()#line:850
                                            print (f'【种植合成】:{O0O0OO00000O0O0OO["message"]}')#line:851
                                            if not OOO00OO000O000O0O .user_ad ():#line:852
                                                return False #line:853
                                    if O0O0OO00000O0O0OO ['status']==500 :#line:854
                                        print (f'【种植合成】:{O0O0OO00000O0O0OO["message"]}')#line:855
                                        return False #line:856
                            OO00OOOO00OOOO0OO +=1 #line:857
                        OOOO000O0000OOO00 =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OOOOO0O00O0 ).json ()#line:858
                        OO0O0OO00O0000OO0 =OOOO000O0000OOO00 ['data']['cropList']#line:859
                        O000O000O0OOOOO0O =False #line:860
                        for O00OOO0000OOOOOOO in range (12 ):#line:861
                            id =OO0O0OO00O0000OO0 [O00OOO0000OOOOOOO ]['level']#line:862
                            if float (O0O0000OOOO0O0OOO )-float (id )>9 :#line:863
                                OO0OO0O0OO0O0O0OO =f'_site={O00OOO0000OOOOOOO}_{timi_new()}'#line:864
                                O00OO0O0O000O0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00OO000O000O0O .token ,'timestamp':timi_new (),'sign':sign (OO0OO0O0OO0O0O0OO ),'signstring':OO0OO0O0OO0O0O0OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:875
                                O0OOO000O0O00OO00 ={"site":O00OOO0000OOOOOOO }#line:876
                                O00O0O00OO0O0O000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O00OO0O0O000O0000 ,data =O0OOO000O0O00OO00 ).json ()#line:878
                                if 'status'in O00O0O00OO0O0O000 :#line:879
                                    if O00O0O00OO0O0O000 ['status']==200 :#line:880
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:881
                            if id !=0 :#line:882
                                for OO00OOOOOOOOO0O00 in range (11 ):#line:883
                                    OO00OOO000OO0O00O =OO00OOOOOOOOO0O00 +1 #line:884
                                    g =OO0O0OO00O0000OO0 [OO00OOO000OO0O00O ]['level']#line:885
                                    if id ==g :#line:886
                                        O00OOO0O000O0O00O =OO00OOOOOOOOO0O00 +2 #line:887
                                        if O00OOO0O000O0O00O !=O00OOO0000OOOOOOO +1 :#line:888
                                            O0OO00000O0O0O00O =O00OOO0000OOOOOOO +1 #line:889
                                            time .sleep (random .randint (1 ,3 )/10 )#line:891
                                            OO00OO0OOO0O0OOO0 =f'_site={O0OO00000O0O0O00O - 1}&targetSite={O00OOO0O000O0O00O - 1}_{timi_new()}'#line:892
                                            OOO000OO00OOO00O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO00OO000O000O0O .token ,'timestamp':timi_new (),'sign':sign (OO00OO0OOO0O0OOO0 ),'signstring':OO00OO0OOO0O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:909
                                            O000OOOO0000O000O ={"site":int (O0OO00000O0O0O00O -1 ),"targetSite":int (O00OOO0O000O0O00O -1 )}#line:910
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO000OO00OOO00O0 ,json =O000OOOO0000O000O )#line:911
                                            O000O000O0OOOOO0O =True #line:913
                                    if O000O000O0OOOOO0O :#line:914
                                        break #line:915
                                if O000O000O0OOOOO0O :#line:916
                                    break #line:917
        except :#line:918
            OOO00OO000O000O0O .synthetic ()#line:919
    def level_new (OOO000O0O00O00O0O ):#line:922
        try :#line:923
            O0OO0O00OOO000OO0 =f'__{timi_new()}'#line:924
            O0O000O000O0000O0 ={'source':'scsc','authorization':OOO000O0O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0O00OOO000OO0 ),'signstring':O0OO0O00OOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:935
            O000OOOO00OOOOO0O =requests .request ('get',f'{host}/user',headers =O0O000O000O0000O0 ).json ()#line:936
            if 'status'in O000OOOO00OOOOO0O :#line:937
                if O000OOOO00OOOOO0O ['status']==200 :#line:938
                    return float (O000OOOO00OOOOO0O ['data']['level'])#line:939
        except Exception as O00O00OO000O0OOO0 :#line:940
            print (O00O00OO000O0OOO0 )#line:941
    def propsraffle (O000OOOOOOOOO00O0 ):#line:944
        try :#line:945
            while True :#line:946
                OOOOOOOOOO00O000O =f'__{timi_new()}'#line:947
                OO000O0OOO0OOO0O0 ={'source':'scsc','authorization':O000OOOOOOOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOO00O000O ),'signstring':OOOOOOOOOO00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:958
                O0OO0O0O0O00000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO000O0OOO0OOO0O0 ).json ()#line:959
                if 'status'in O0OO0O0O0O00000O0 :#line:961
                    if O0OO0O0O0O00000O0 ['status']==200 :#line:962
                        O0OOOO0OO0OOO0000 =O0OO0O0O0O00000O0 ['data']['rows']#line:963
                        O0OOOOOO000OO0000 =O0OO0O0O0O00000O0 ['data']['vstate']#line:964
                        if O0OOOO0OO0OOO0000 ==5 or O0OOOO0OO0OOO0000 ==6 or O0OOOO0OO0OOO0000 ==7 :#line:965
                            O0000OOO000OO00O0 =O0OO0O0O0O00000O0 ['data']['silver']#line:966
                            print (f'【转盘抽奖】:获得种子:{O0000OOO000OO00O0}')#line:967
                        if O0OOOO0OO0OOO0000 ==1 or O0OOOO0OO0OOO0000 ==2 or O0OOOO0OO0OOO0000 ==3 :#line:968
                            O000OOO000O0O0O00 =O0OO0O0O0O00000O0 ['data']['clover']#line:969
                            print (f'【转盘抽奖】:获得三叶草:{O000OOO000O0O0O00}')#line:970
                        if O0OOOO0OO0OOO0000 ==4 or O0OOOO0OO0OOO0000 ==8 :#line:971
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:972
                        if O0OOOO0OO0OOO0000 =='抽奖次数已用完':#line:976
                            break #line:1010
                time .sleep (random .randint (8 ,15 )/10 )#line:1011
        except Exception as O0OOO000OOOOOO00O :#line:1012
            print (O0OOO000OOOOOO00O )#line:1013
    def friends_invitation (O00O00OOO0OO00OO0 ):#line:1016
        try :#line:1017
            O0OO000O000O0O000 =f'__{timi_new()}'#line:1018
            OOOOO0OOOO0OO0OOO ={'source':'scsc','authorization':O00O00OOO0OO00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O000O0O000 ),'signstring':O0OO000O000O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1029
            OO000OO0O0O0O0O00 =requests .request ('get',f'{host}/friends',headers =OOOOO0OOOO0OO0OOO ).json ()#line:1030
            if 'status'in OO000OO0O0O0O0O00 :#line:1031
                if OO000OO0O0O0O0O00 ['status']==200 :#line:1032
                    O0OOO0OO0000O0OOO =OO000OO0O0O0O0O00 ['data']['myInviteter']#line:1033
                    if O0OOO0OO0000O0OOO :#line:1034
                        OOOO0OO0000OOO000 =O0OOO0OO0000O0OOO ['user']['nickname']#line:1035
                        OO000OOO0O00O0O00 =O00O00OOO0OO00OO0 .certification ()#line:1036
                        print (f'【查邀请人】:我的邀请人:{OOOO0OO0000OOO000}丨实名:{OO000OOO0O00O0O00}')#line:1037
                    else :#line:1038
                        if O00O00OOO0OO00OO0 .innerId !='0':#line:1039
                            O00O00OOO0OO00OO0 .invitation ()#line:1040
        except Exception as O0O0OOOO0O0OOOO00 :#line:1041
            print (O0O0OOOO0O0OOOO00 )#line:1042
    def add_clover (OO0OO0O00O0000OO0 ):#line:1045
        global golden_seed #line:1046
        try :#line:1047
            OOO00OOO0O0OO0OOO =f'__{timi_new()}'#line:1048
            OOO0O0OO0000000OO ={'source':'scsc','authorization':OO0OO0O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O0OO0OOO ),'signstring':OOO00OOO0O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1059
            OO0000000O0O0O00O =requests .request ('get',f'{host}/assets/clovers',headers =OOO0O0OO0000000OO ).json ()#line:1060
            if 'status'in OO0000000O0O0O00O :#line:1062
                if OO0000000O0O0O00O ['status']==200 :#line:1063
                    OO000OO000OO0O00O =OO0000000O0O0O00O ['data']['clover']#line:1064
                    O0OO0OOOOOO00OO0O =OO0000000O0O0O00O ['data']['used_clover']#line:1065
                    OO00OO0OOOOO0O00O =float (OO000OO000OO0O00O )-float (O0OO0OOOOOO00OO0O )#line:1066
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0OOOOOO00OO0O}')#line:1067
                    if OO0OO0O00O0000OO0 .certification ()!='未实名':#line:1068
                        if OO00OO0OOOOO0O00O >1 :#line:1069
                            OOO00OOO0O0OO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00OO0OOOOO0O00O)}_{timi_new()}'#line:1070
                            OOOO00OO00OO0O00O ={'source':'scsc','authorization':OO0OO0O00O0000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0O0OO0OOO ),'signstring':OOO00OOO0O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1081
                            O000O0OO000O00O00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00OO0OOOOO0O00O )}#line:1082
                            O000OO00OO00OO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO00OO00OO0O00O ,data =O000O0OO000O00O00 ).json ()#line:1083
                            if 'status'in O000OO00OO00OO0OO :#line:1085
                                if O000OO00OO00OO0OO ['status']==200 :#line:1086
                                    print (f'【参与抽奖】:添加☘️:{O000OO00OO00OO0OO["data"]}丨数量:{OO00OO0OOOOO0O00O}')#line:1087
                                if O000OO00OO00OO0OO ['status']==500 :#line:1088
                                    print (f'【参与抽奖】:添加☘️:{O000OO00OO00OO0OO["message"]}')#line:1089
            O00O0000O0O0OO000 =requests .request ('get',f'{host}/lottery',headers =OOO0O0OO0000000OO ).json ()#line:1090
            O0OO0O00000O000OO =OO0OO0O00O0000OO0 .winning_rewards ()#line:1092
            if 'status'in O00O0000O0O0OO000 :#line:1093
                if O00O0000O0O0OO000 ['status']==200 :#line:1094
                    O0OOOO00O00O0O000 =O00O0000O0O0OO000 ['data'][0 ]['day_get_gold_quantity']#line:1095
                    golden_seed +=float (O0OOOO00O00O0O000 )#line:1096
                    OOOO0OO0OO00OO0O0 =O00O0000O0O0OO000 ['data'][1 ]['value']#line:1097
                    O0OO00O000OOOOOO0 =O00O0000O0O0OO000 ['data'][0 ]['join_number']#line:1098
                    OOO0OOOO0O0O00OOO =int (float (O00O0000O0O0OO000 ['data'][0 ]['totalValue']))#line:1099
                    OO0O0O0OO00OOO000 =float (OOOO0OO0OO00OO0O0 /OOO0OOOO0O0O00OOO )*10000 #line:1100
                    O0OO000O0O0000OO0 =OOO0OOOO0O0O00OOO /O0OO00O000OOOOOO0 #line:1101
                    print (f'【参与抽奖】:预计每天中{str(O0OOOO00O00O0O000)[:6]}颗金种子丨好友收益:{str(O0OO0O00000O000OO)[:6]}')#line:1102
                    print (f'【抽奖统计】:每1万☘️中{str(OO0O0O0OO00OOO000)[:6]}颗金种子丨☘️人均:{str(O0OO000O0O0000OO0)[:7]}️')#line:1103
        except Exception as O00O000OO0OO00OO0 :#line:1104
            print (O00O000OO0OO00OO0 )#line:1105
    def energy (O00O00OOOO0OOO0OO ):#line:1108
        try :#line:1109
            while True :#line:1110
                O0OOOOO0000OO00O0 =f'__{timi_new()}'#line:1111
                OOOO00O0OO00OOO00 ={'source':'scsc','authorization':O00O00OOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0000OO00O0 ),'signstring':O0OOOOO0000OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1122
                OO00OO0O000O0O00O =requests .request ('get',f'{host}/energy/general',headers =OOOO00O0OO00OOO00 ).json ()#line:1123
                if 'status'in OO00OO0O000O0O00O :#line:1125
                    if OO00OO0O000O0O00O ['status']==200 :#line:1126
                        O0000O00O000O0OOO =OO00OO0O000O0O00O ['data']['ordinary_water']#line:1127
                        O000OOOO0000OO00O =OO00OO0O000O0O00O ['data']['ordinary_fertilizer']#line:1128
                        O00O0OOOOOO00O000 =OO00OO0O000O0O00O ['data']['videoStatus']#line:1129
                        O0O00OO000OOO0O00 =OO00OO0O000O0O00O ['data']['waterVideoKey']#line:1130
                        print (f'【我的营养】:肥料:{str(O000OOOO0000OO00O).split(".")[0]}丨水滴:{str(O0000O00O000O0OOO).split(".")[0]}')#line:1132
                        if float (O000OOOO0000OO00O )<96 :#line:1133
                            if O00O0OOOOOO00O000 :#line:1134
                                time .sleep (random .randint (160 ,180 )/10 )#line:1135
                                O000OO0O00000OOOO =99 -float (O000OOOO0000OO00O )#line:1136
                                OOOOOOO0O0000O00O ={"fertilizer":str (O000OO0O00000OOOO ).split ('.')[0 ]}#line:1137
                                O0O00OOOO00O000O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOOO00O0OO00OOO00 ).json ()#line:1139
                                if 'status'in O0O00OOOO00O000O0 :#line:1141
                                    if O0O00OOOO00O000O0 ['status']==200 :#line:1142
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00OOOO00O000O0["message"]}')#line:1143
                                    if O0O00OOOO00O000O0 ['status']==500 :#line:1144
                                        print (f'【购买肥料】:看广告获取肥料:{O0O00OOOO00O000O0["message"]}')#line:1145
                                        break #line:1146
                                if float (O000OOOO0000OO00O )<78 :#line:1148
                                    O000OO0O00000OOOO =80 -float (O000OOOO0000OO00O )#line:1149
                                    OOOOOO0O000O0O0OO =f'_fertilizer={int(O000OO0O00000OOOO)}_{timi_new()}'#line:1150
                                    O00OO000O000OOOOO ={'source':'scsc','authorization':O00O00OOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0O000O0O0OO ),'signstring':OOOOOO0O000O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1161
                                    O0OO0000O0000OO00 ={"fertilizer":int (O000OO0O00000OOOO )}#line:1162
                                    OOO0O0O00000OO000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00OO000O000OOOOO ,data =O0OO0000O0000OO00 ).json ()#line:1164
                                    if 'status'in OOO0O0O00000OO000 :#line:1166
                                        if OOO0O0O00000OO000 ['status']==200 :#line:1167
                                            print (f'【购买肥料】:购买肥料:{OOO0O0O00000OO000["message"]}丨数量:{int(O000OO0O00000OOOO)}')#line:1168
                                        if OOO0O0O00000OO000 ['status']==500 :#line:1169
                                            print (f'【购买肥料】:购买肥料:{OOO0O0O00000OO000["message"]}丨数量:{int(O000OO0O00000OOOO)}')#line:1170
                                            O00O0OO0OOOOOOO00 =OOO0O0O00000OO000 ["message"].split ('-')[1 ]#line:1171
                                            OO0OO0OO00OO00O0O =f'__{timi_new()}'#line:1172
                                            OOOOO0O00OO0O0O0O ={'source':'scsc','authorization':O00O00OOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00OO00O0O ),'signstring':OO0OO0OO00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1183
                                            O00OOO0O00O00OO0O =requests .request ('get',f'{host}/user',headers =OOOOO0O00OO0O0O0O ).json ()#line:1184
                                            if 'status'in O00OOO0O00O00OO0O :#line:1185
                                                if O00OOO0O00O00OO0O ['status']==200 :#line:1186
                                                    OO00OO0O0O00OOOOO =O00OOO0O00O00OO0O ['data']['inner_id']#line:1187
                                                    if give_gold (OO00OO0O0O00OOOOO ,float (O00O0OO0OOOOOOO00 )+1 ):#line:1188
                                                        O00O00OOOO0OOO0OO .energy ()#line:1189
                        if float (O0000O00O000O0OOO )<880 :#line:1190
                            if O0O00OO000OOO0O00 :#line:1191
                                time .sleep (random .randint (160 ,180 )/10 )#line:1192
                                O0000O0O0O0OOO00O =999 -float (O0000O00O000O0OOO )#line:1193
                                OOOO00O0O000O000O ={"water":str (O0000O0O0O0OOO00O ).split ('.')[0 ]}#line:1194
                                OO0000OOOO0OOO0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOOO00O0OO00OOO00 ).json ()#line:1196
                                if 'status'in OO0000OOOO0OOO0O0 :#line:1198
                                    if OO0000OOOO0OOO0O0 ['status']==200 :#line:1199
                                        print (f'【购买水滴】:看广告获取水滴:{OO0000OOOO0OOO0O0["message"]}')#line:1200
                                    if OO0000OOOO0OOO0O0 ['status']==500 :#line:1201
                                        print (f'【购买水滴】:看广告获取水滴:{OO0000OOOO0OOO0O0["message"]}')#line:1202
                                        break #line:1203
                                if float (O0000O00O000O0OOO )<780 :#line:1204
                                    O0000O0O0O0OOO00O =800 -float (O0000O00O000O0OOO )#line:1205
                                    O0OO0000O000O0OO0 =f'_water={int(O0000O0O0O0OOO00O)}_{timi_new()}'#line:1206
                                    OO00OOO00O0OO00O0 ={'source':'scsc','authorization':O00O00OOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O000O0OO0 ),'signstring':O0OO0000O000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1217
                                    OOO0O000O0O00O0OO ={"water":int (O0000O0O0O0OOO00O )}#line:1218
                                    O0OO0O0O00O00OOOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO00OOO00O0OO00O0 ,data =OOO0O000O0O00O0OO ).json ()#line:1220
                                    if 'status'in O0OO0O0O00O00OOOO :#line:1222
                                        if O0OO0O0O00O00OOOO ['status']==200 :#line:1223
                                            print (f'【购买水滴】:购买水滴:{O0OO0O0O00O00OOOO["message"]}丨数量:{int(O0000O0O0O0OOO00O)}')#line:1224
                                        if O0OO0O0O00O00OOOO ['status']==500 :#line:1225
                                            print (f'【购买水滴】:购买水滴:{O0OO0O0O00O00OOOO["message"]}丨数量:{int(O0000O0O0O0OOO00O)}')#line:1226
                                            O00O0OO0OOOOOOO00 =O0OO0O0O00O00OOOO ["message"].split ('-')[1 ]#line:1227
                                            OO0OO0OO00OO00O0O =f'__{timi_new()}'#line:1228
                                            OOOOO0O00OO0O0O0O ={'source':'scsc','authorization':O00O00OOOO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO00OO00O0O ),'signstring':OO0OO0OO00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1239
                                            O00OOO0O00O00OO0O =requests .request ('get',f'{host}/user',headers =OOOOO0O00OO0O0O0O ).json ()#line:1240
                                            if 'status'in O00OOO0O00O00OO0O :#line:1241
                                                if O00OOO0O00O00OO0O ['status']==200 :#line:1242
                                                    OO00OO0O0O00OOOOO =O00OOO0O00O00OO0O ['data']['inner_id']#line:1243
                                                    if give_gold (OO00OO0O0O00OOOOO ,float (O00O0OO0OOOOOOO00 )+1 ):#line:1244
                                                        O00O00OOOO0OOO0OO .energy ()#line:1245
                        break #line:1246
        except Exception as OO0OOO00O00000O0O :#line:1247
            print (OO0OOO00O00000O0O )#line:1248
def bundled_def ():#line:1251
    OO00O00O00000OO00 =['5570536','7750212','7911652','7911680','7805624']#line:1252
    return OO00O00O00000OO00 [random .randint (0 ,len (OO00O00O00000OO00 )-1 )]#line:1253
def version_of_the_validation ():#line:1257
    return str ((94 -56 )/10 )#line:1258
def sc2 ():#line:1261
    return "19319#$%^&*((*"#line:1262
def OO00OO0OO0OO00OO00o0 ():#line:1265
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1267
def get_ip ():#line:1270
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1272
def gitee_validation ():#line:1275
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1276
def gitee_edition ():#line:1279
    try :#line:1280
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1281
    except :#line:1282
        sys .exit (0 )#line:1283
def O000OO000O0O00OOO00 ():#line:1287
    try :#line:1288
        O00O0O00O0OOOOO0O =gitee_edition ()#line:1289
        if version_of_the_validation ()<O00O0O00O0OOOOO0O ['CityEarth']['edition']:#line:1290
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O00O0OOOOO0O["CityEarth"]["edition"]}   ❌')#line:1291
            print (f'更新内容=>>{O00O0O00O0OOOOO0O["CityEarth"]["content"]}')#line:1292
        else :#line:1293
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O00O0OOOOO0O["CityEarth"]["edition"]}   ✅')#line:1294
            print (f'更新内容=>> {O00O0O00O0OOOOO0O["CityEarth"]["content"]}')#line:1295
    except Exception as O0000O0OO0O0O0000 :#line:1296
        print (O0000O0OO0O0O0000 )#line:1297
def sc3 ():#line:1300
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1301
if __name__ =='__main__':#line:1304
    start ()#line:1305
