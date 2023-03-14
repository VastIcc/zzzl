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
        OOOO00O000000O0OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OOOO00O000000O0OO)}个账号==========")#line:16
        for OO0OO0O0O0O00000O in OOOO00O000000O0OO :#line:17
            O000OO0OOO00O0000 =[]#line:18
            print (f"------------正在执行第{OOOO00O000000O0OO.index(OO0OO0O0O0O00000O) + 1}个账号------------")#line:19
            OOO00OO0O0OOO0O0O =CityEarth (OO0OO0O0O0O00000O ,O000OO0OOO00O0000 ,OOOO00O000000O0OO .index (OO0OO0O0O0O00000O ))#line:20
            def O000OO0OO0O00OOOO ():#line:22
                if OOO00OO0O0OOO0O0O .base_info ():#line:24
                    OOO00OO0O0OOO0O0O .sealing ()#line:26
                    OOO00OO0O0OOO0O0O .invitenum ()#line:28
                    OOO00OO0O0OOO0O0O .query_to_sell ()#line:30
                    OOO00OO0O0OOO0O0O .game_map ()#line:32
                    OOO00OO0O0OOO0O0O .friends_invitation ()#line:34
                    OOO00OO0O0OOO0O0O .energy ()#line:36
                    OOO00OO0O0OOO0O0O .add_clover ()#line:38
                    OOO00OO0O0OOO0O0O .propsraffle ()#line:40
                    OOO00OO0O0OOO0O0O .synthetic ()#line:42
                    OOO00OO0O0OOO0O0O .crops_illustrated ()#line:44
                    OOO00OO0O0OOO0O0O .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        OOO00OO0O0OOO0O0O .give_gold ()#line:49
            O0000OOOO0OOO0O00 =threading .Thread (target =O000OO0OO0O00OOOO )#line:51
            O0000OOOO0OOO0O00 .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理推送通知------------")#line:54
        time .sleep (0.5 )#line:55
        OOO00OOO0OO00OO0O =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOO00OOO0OO00OO0O +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for OOOOOOO00O00O0000 in invited_new :#line:60
            print (OOOOOOO00O00O0000 )#line:61
        print ('开始打印未实名的token')#line:62
        for OO00O00OOOOO0O0O0 in weishim :#line:63
            print (OO00O00OOOOO0O0O0 )#line:64
    except Exception as OOOO000OOO00O0000 :#line:65
        print (OOOO000OOO00O0000 )#line:66
def give_gold (OO0OO0O00000OO0O0 ,OO000O0OO0OO0O00O ):#line:70
    try :#line:71
        OOOOOO000O00O0OO0 =f'_doneeNo={OO0OO0O00000OO0O0}&quantity={int(OO000O0OO0OO0O00O)}_{timi_new()}'#line:72
        OOO0000OO000O000O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOOOO000O00O0OO0 ),'signstring':OOOOOO000O00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOO00O00O0O0OOOO0 ={"quantity":int (OO000O0OO0OO0O00O ),"doneeNo":OO0OO0O00000OO0O0 }#line:87
        O000O00O0000O00OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0000OO000O000O ,data =OOO00O00O0O0OOOO0 ).json ()#line:88
        if 'status'in O000O00O0000O00OO :#line:90
            if O000O00O0000O00OO ['status']==200 :#line:91
                if O000O00O0000O00OO ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OO000O0OO0OO0O00O)}种子给{OO0OO0O00000OO0O0}成功')#line:93
                    return True #line:94
            if O000O00O0000O00OO ['status']==401 :#line:95
                print (f'【赠送种子】:{O000O00O0000O00OO["message"]}')#line:96
                return False #line:97
            if O000O00O0000O00OO ['status']==500 :#line:98
                print (f'【赠送种子】:{O000O00O0000O00OO["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as O0O0O00O0O00000O0 :#line:102
        print (O0O0O00O0O00000O0 )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def sign (OOOOO00O0O000O00O ):#line:110
    O000OOOO00O000O00 =hashlib .md5 (OOOOO00O0O000O00O .encode ()).hexdigest ()#line:111
    O000OOO0O0O0OOOO0 =sc1 ()#line:112
    O0OOO0O0O00000O0O =sc2 ()#line:113
    O00O0O0OO0OO0OO0O =sc3 ()#line:114
    OOO0O0OOOO0OOO000 =O000OOO0O0O0OOOO0 +O000OOOO00O000O00 +O0OOO0O0O00000O0O +O00O0O0OO0OO0OO0O #line:115
    OO00O00000000O0OO =hashlib .md5 (OOO0O0OOOO0OOO000 .encode ()).hexdigest ()#line:116
    return OO00O00000000O0OO #line:117
def format_msg ():#line:120
    OO0OO0OOO0OO00O00 =""#line:121
    for O00000OO0000OO0O0 in msg_list :#line:122
        OO0OO0OOO0OO00O00 +=str (O00000OO0000OO0O0 )+"\r\n"#line:123
    return OO0OO0OOO0OO00O00 #line:124
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
def get_json_data (O0O000OOO00OOO00O ,OO00O00O00OOOOO00 ,OOO0OO000O0OOOOOO ,O000O00OO000OOO0O ):#line:147
    with open (O0O000OOO00OOO00O ,'rb')as OO000OO00O0000OOO :#line:148
        OOOOO0OO00O00OOO0 =json .load (OO000OO00O0000OOO )#line:149
        OOOOO0OO00O00OOO0 ['data'][OO00O00O00OOOOO00 ][OOO0OO000O0OOOOOO ]=O000O00OO000OOO0O #line:150
        O00O0000000O00O00 =OOOOO0OO00O00OOO0 #line:151
    OO000OO00O0000OOO .close ()#line:152
    return O00O0000000O00O00 #line:153
def write_json_data (OOOOO00000OO000O0 ):#line:156
    with open (json_path1 ,'w')as O0OOOOO00OOOO0O0O :#line:157
        json .dump (OOOOO00000OO000O0 ,O0OOOOO00OOOO0O0O )#line:158
    O0OOOOO00OOOO0O0O .close ()#line:159
    return True #line:160
class CityEarth :#line:163
    def __init__ (OOO00O0OO000O000O ,O0O0O00O0O0O00O00 ,O0O0000O0O0OOOO00 ,OOOOOO0O0OO0O0O00 ):#line:165
        try :#line:166
            OOO00O0OO000O000O .msg =O0O0000O0O0OOOO00 #line:167
            OOO00O0OO000O000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:168
            OOO00O0OO000O000O .token =O0O0O00O0O0O00O00 ['authorization']#line:169
            OOO00O0OO000O000O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:170
            OOO00O0OO000O000O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:171
            OOO00O0OO000O000O .elephant_user =O0O0O00O0O0O00O00 ['elephant_user']#line:172
            OOO00O0OO000O000O .elephant_pswd =O0O0O00O0O0O00O00 ['elephant_pswd']#line:173
            OOO00O0OO000O000O .elephant_Task_ID =O0O0O00O0O0O00O00 ['elephant_Task_ID']#line:174
            OOO00O0OO000O000O .len_new =OOOOOO0O0OO0O0O00 #line:175
        except :#line:176
            print ('变量格式错误')#line:177
    def base_info (OO000OOO00O0OOO00 ):#line:180
        try :#line:181
            OO000OOO00O0OOO00 .watched_ad ()#line:183
            OOOO0OOOOOO0O0000 =f'__{timi_new()}'#line:184
            OO0OO0O00O000OOOO ={'source':'scsc','authorization':OO000OOO00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOOOOO0O0000 ),'signstring':OOOO0OOOOOO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
            O00O0O0OO0O0O0O0O =requests .request ('get',f'{host}/user',headers =OO0OO0O00O000OOOO ).json ()#line:196
            if 'status'in O00O0O0OO0O0O0O0O :#line:198
                if O00O0O0OO0O0O0O0O ['status']==200 :#line:199
                    OO0O00O0OOO000000 =O00O0O0OO0O0O0O0O ['data']['nickname']#line:200
                    OO0O000O0O000OO00 =O00O0O0OO0O0O0O0O ['data']['inner_id']#line:201
                    O0O0O000OOOOOOO0O =O00O0O0OO0O0O0O0O ['data']['assets']['gold']#line:202
                    OOO0O0O000O0000OO =O00O0O0OO0O0O0O0O ['data']['level']#line:203
                    print (f'【账号信息】:昵称:{OO0O00O0OOO000000[:5]}丨ID:{OO0O000O0O000OO00}丨等级:{OOO0O0O000O0000OO}丨金种子:{str(O0O0O000OOOOOOO0O).split(".")[0]}')#line:205
                    if 'wx_'in OO0O00O0OOO000000 :#line:206
                        OO000OOO00O0OOO00 .change_nickname ()#line:207
                if O00O0O0OO0O0O0O0O ['status']==401 :#line:208
                    print ('【账号信息】:账号失效正在尝试登录')#line:209
                    if OO000OOO00O0OOO00 .elephant_user =='f':#line:210
                        return False #line:211
                    O00O000OO000O0O00 =Invalid_login .addtask (elephant_user =OO000OOO00O0OOO00 .elephant_user ,elephant_pswd =OO000OOO00O0OOO00 .elephant_pswd ,elephant_Task_ID =OO000OOO00O0OOO00 .elephant_Task_ID )#line:214
                    O00OO0O000O00O00O =get_json_data (json_path ,OO000OOO00O0OOO00 .len_new ,'authorization',O00O000OO000O0O00 )#line:215
                    if write_json_data (O00OO0O000O00O00O ):#line:216
                        print ('正在写入账号配置文件')#line:217
                    return False #line:218
                if O00O0O0OO0O0O0O0O ['status']==500 :#line:219
                    return False #line:220
            return True #line:221
        except Exception as O0OO0O0O0O000O00O :#line:222
            print (O0OO0O0O0O000O00O )#line:223
    def sealing (O0OOO0O0O0O0OO00O ):#line:226
        try :#line:227
            O0O0OOOO0OO0O0O00 =f'__{timi_new()}'#line:228
            OOO0000OO000OO0OO ={'source':'scsc','authorization':O0OOO0O0O0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOO0OO0O0O00 ),'signstring':O0O0OOOO0OO0O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO0000OO000OO0OO )#line:240
            requests .request ('get',f'{host}/packsack/list',headers =OOO0000OO000OO0OO )#line:241
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO0000OO000OO0OO )#line:242
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO0000OO000OO0OO )#line:243
            requests .request ('get',f'{host}/user',headers =OOO0000OO000OO0OO )#line:244
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO0000OO000OO0OO )#line:245
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO0000OO000OO0OO )#line:246
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO0000OO000OO0OO )#line:247
            requests .request ('get',f'{host}/game/getAllData',headers =OOO0000OO000OO0OO )#line:248
            requests .request ('get',f'{host}/assets',headers =OOO0000OO000OO0OO )#line:249
        except Exception as O00OOOO000OOO0O00 :#line:250
            print (O00OOOO000OOO0O00 )#line:251
    def the_query (O000O000OOO0OOOO0 ):#line:254
        try :#line:255
            OOOOOOO0OOO0OO00O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:256
            O00OO0OOOO0OO0O00 ={'authorization':O000O000OOO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0OOO0OO00O ),'signstring':OOOOOOO0OOO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            O00O00OOO00OO0O00 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O00OO0OOOO0OO0O00 ).json ()#line:268
            if 'status'in O00O00OOO00OO0O00 :#line:270
                if O00O00OOO00OO0O00 ['status']==200 :#line:271
                    OOOO0OO000OO0OO00 =O00O00OOO00OO0O00 ['data']['rows'][3 ]['price']#line:272
                    O000O000OOO0OOOO0 .market_sale (OOOO0OO000OO0OO00 )#line:273
        except Exception as OO00O00OO00OO00OO :#line:274
            print (OO00O00OO00OO00OO )#line:275
    def market_sale (OOOO0OOOOO00O0O00 ,OO0O000000OOOOO0O ):#line:278
        try :#line:279
            O0OO0OOO0OOO00OO0 =timi_new ()#line:280
            OOOO000OO0O0OOO0O =f'type=crop__{O0OO0OOO0OOO00OO0}'#line:281
            O00OO0O00O0O0O0OO ={'source':'scsc','authorization':OOOO0OOOOO00O0O00 .token ,'timestamp':str (O0OO0OOO0OOO00OO0 ),'sign':sign (OOOO000OO0O0OOO0O ),'signstring':OOOO000OO0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            OO00O000OO0OO0O00 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00OO0O00O0O0O0OO ).json ()#line:294
            if 'status'in OO00O000OO0OO0O00 :#line:296
                if OO00O000OO0OO0O00 ['status']==200 :#line:297
                    if OO00O000OO0OO0O00 ['data']['rows']:#line:298
                        O00OO00OO0000000O =OO00O000OO0OO0O00 ['data']['rows'][0 ]['packsackItemId']#line:299
                        O0O0O00OOO00OO00O =OO00O000OO0OO0O00 ['data']['rows'][0 ]['quantity']#line:300
                        O0OOO0O0000O0O0OO =float (OO0O000000OOOOO0O )+float (random .randint (1 ,99 )*0.001 )#line:301
                        OO000O00O0O0O00OO =f'_packsackItemId={O00OO00OO0000000O}&price={str(O0OOO0O0000O0O0OO)[:7]}&quantity={O0O0O00OOO00OO00O}_{O0OO0OOO0OOO00OO0}'#line:302
                        OOO00000O0OOO00O0 ={'source':'scsc','authorization':OOOO0OOOOO00O0O00 .token ,'timestamp':str (O0OO0OOO0OOO00OO0 ),'sign':sign (OO000O00O0O0O00OO ),'signstring':OO000O00O0O0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                        O0O0OOO0O0OO0OOOO ={"packsackItemId":O00OO00OO0000000O ,"price":str (O0OOO0O0000O0O0OO )[:7 ],"quantity":str (O0O0O00OOO00OO00O )}#line:318
                        OO00O0OO0OOO00OOO =requests .request ('post',f'{host}/market/sale',headers =OOO00000O0OOO00O0 ,data =O0O0OOO0O0OO0OOOO ).json ()#line:319
                        if 'status'in OO00O0OO0OOO00OOO :#line:321
                            if OO00O0OO0OOO00OOO ['status']==200 :#line:322
                                print (f'【上架芦荟】:数量:{O0O0O00OOO00OO00O}丨价格:{str(O0OOO0O0000O0O0OO)[:7]}')#line:323
        except Exception as O0OOO0O0OOOOOO00O :#line:324
            print (O0OOO0O0OOOOOO00O )#line:325
    def query_to_sell (OOO0O00OOOO0000OO ):#line:328
        try :#line:329
            OOOO0OOO0O00OO000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:330
            OOO0OOOO0OOO0OO00 ={'source':'scsc','authorization':OOO0O00OOOO0000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0O00OO000 ),'signstring':OOOO0OOO0O00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
            O0OO0OOO00O00OOOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO0OOOO0OOO0OO00 ).json ()#line:343
            if 'status'in O0OO0OOO00O00OOOO :#line:345
                if O0OO0OOO00O00OOOO ['status']==200 :#line:346
                    for OOO0O0O0000OO0O0O in O0OO0OOO00O00OOOO ['data']['rows']:#line:347
                        O0OO00OOOO0OOO000 =OOO0O0O0000OO0O0O ['materialKey']#line:348
                        O0OO000OOO0O0O0OO =OOO0O0O0000OO0O0O ['quantity']#line:349
                        O000O00OOO0O0O000 =OOO0O0O0000OO0O0O ['price']#line:350
                        O0O0O0O0OOO00OOO0 =OOO0O0O0000OO0O0O ['saleState']#line:351
                        if O0O0O0O0OOO00OOO0 ==0 :#line:352
                            print (f'【出售订单】:名称:{O0OO00OOOO0OOO000}丨数量:{O0OO000OOO0O0O0OO}丨价格:{O000O00OOO0O0O000}')#line:353
                            OO00OOOOOOO00OOO0 =OOO0O0O0000OO0O0O ['id']#line:354
                            if float (datetime .datetime .now ().hour )>8 :#line:355
                                OOO0O00OOOO0000OO .cacel_sale (OO00OOOOOOO00OOO0 )#line:356
        except Exception as O0000OOO0O00O0OOO :#line:357
            print (O0000OOO0O00O0OOO )#line:358
    def cacel_sale (O0O0000O0O0OO0000 ,O0O0000O0O000OOO0 ):#line:361
        try :#line:362
            O0OOO00O00OO0OO00 =f'_saleId={O0O0000O0O000OOO0}_{timi_new()}'#line:363
            O0O00O000OOO00O0O ={'source':'scsc','authorization':O0O0000O0O0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O00OO0OO00 ),'signstring':O0OOO00O00OO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:374
            OO000OOOO00OO0OOO ={"saleId":O0O0000O0O000OOO0 }#line:377
            O0O00O00OO0OO0O00 =requests .request ('post',f'{host}/market/cacel-sale',headers =O0O00O000OOO00O0O ,data =OO000OOOO00OO0OOO ).json ()#line:378
            if 'status'in O0O00O00OO0OO0O00 :#line:380
                if O0O00O00OO0OO0O00 ['status']==200 :#line:381
                    print (f'【下架出售】:{O0O00O00OO0OO0O00["data"]}')#line:382
        except Exception as O00O00O0OOO000O00 :#line:383
            print (O00O00O0OOO000O00 )#line:384
    def change_nickname (OOO0OO000O0O00OOO ):#line:387
        try :#line:388
            O00OO00OOOOOO0000 =timi_new ()#line:389
            O0O00O00O00OO0000 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:390
            OO0O0OOOO0000O00O =requests .request ('post','https://www.qmsjmfb.com/',data =O0O00O00O00OO0000 ).text #line:391
            OO0O00O0000O0O0O0 =re .findall ('<ul><li>(.*?)</li>',OO0O0OOOO0000O00O )[0 ][:3 ]#line:392
            O000O000O00OOO0O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O00O0000O0O0O0}').json ()#line:393
            O000O0O0OOO0000O0 =O000O000O00OOO0O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:394
            OOOOO0OOO0O00O0OO ={"nickname":O000O0O0OOO0000O0 }#line:395
            OOO00OOOOOO0O0O00 =f'_nickname={O000O0O0OOO0000O0}_{O00OO00OOOOOO0000}'#line:396
            O0OOO0O00OOOOOO0O ={'source':'scsc','authorization':OOO0OO000O0O00OOO .token ,'timestamp':O00OO00OOOOOO0000 ,'sign':sign (OOO00OOOOOO0O0O00 ),'signstring':OOO00OOOOOO0O0O00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:407
            OOOO0OO0O0OOOOO00 =requests .request ('patch',f'{host}/user/nickname',headers =O0OOO0O00OOOOOO0O ,data =OOOOO0OOO0O00O0OO ).json ()#line:408
            if 'status'in OOOO0OO0O0OOOOO00 :#line:410
                if OOOO0OO0O0OOOOO00 ['status']==200 :#line:411
                    print (f'【修改网名】:网名:{O000O0O0OOO0000O0}丨{OOOO0OO0O0OOOOO00["message"]}')#line:412
        except Exception as O00000000000O00O0 :#line:413
            print (O00000000000O00O0 )#line:414
    def withdraw (OO0O0O0O000OOO00O ):#line:417
        try :#line:418
            O0OO0000O000OOOO0 =f'__{timi_new()}'#line:419
            O0OO0OO0O0O0O00O0 ={'source':'scsc','authorization':OO0O0O0O000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O000OOOO0 ),'signstring':O0OO0000O000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:430
            OOO0O0000O0O00O00 =requests .request ('get',f'{host}/assets',headers =O0OO0OO0O0O0O00O0 ).json ()#line:431
            if 'status'in OOO0O0000O0O00O00 :#line:433
                if OOO0O0000O0O00O00 ['status']==200 :#line:434
                    OO000OO00000O0O00 =OOO0O0000O0O00O00 ['data']['cash']#line:435
                    if float (OO000OO00000O0O00 )>20 :#line:436
                        O0OO0000O000OOOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:437
                        O0OO0OO0O0O0O00O0 ={'authorization':OO0O0O0O000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0000O000OOOO0 ),'signstring':O0OO0000O000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
                        OOOO0O0O0O0O000OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:448
                        OOO0OO0O0OO00O00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0OO0OO0O0O0O00O0 ,data =OOOO0O0O0O0O000OO ).json ()#line:450
                        if 'status'in OOO0OO0O0OO00O00O :#line:452
                            if OOO0OO0O0OO00O00O ['status']==200 :#line:453
                                print (f'【余额提现】:{OOO0OO0O0OO00O00O["data"]}')#line:454
                        if 'status'in OOO0OO0O0OO00O00O :#line:455
                            if OOO0OO0O0OO00O00O ['status']==500 :#line:456
                                print (f'【余额提现】:{OOO0OO0O0OO00O00O["message"]}')#line:457
        except Exception as OO0O0OO0OO0OOO000 :#line:458
            print (OO0O0OO0OO0OOO000 )#line:459
    def invitenum (OO0O0OOO0OOO0000O ):#line:462
        global invited_new #line:463
        try :#line:464
            OOO0O0O00O0OO0OO0 =f'__{timi_new()}'#line:465
            O000000OOO0OO0OO0 ={'source':'scsc','authorization':OO0O0OOO0OOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00O0OO0OO0 ),'signstring':OOO0O0O00O0OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            O00O0000OOOOOOO0O =requests .request ('get',f'{host}/invite/invitenum',headers =O000000OOO0OO0OO0 ).json ()#line:477
            if 'status'in O00O0000OOOOOOO0O :#line:479
                if O00O0000OOOOOOO0O ['status']==200 :#line:480
                    O0OOOOOOO00O0O00O =O00O0000OOOOOOO0O ['data']['invited_count']#line:481
                    O0000000OOO00O00O =O00O0000OOOOOOO0O ['data']['invited_second_count']#line:482
                    print (f'【我的邀请】:直邀好友:{O0OOOOOOO00O0O00O}丨间邀好友:{O0000000OOO00O00O}')#line:483
                    if O0OOOOOOO00O0O00O <2 :#line:484
                        OO0OO000000O0OO0O =f'__{timi_new()}'#line:485
                        O0000O0O0O00000O0 ={'source':'scsc','authorization':OO0O0OOO0OOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000000O0OO0O ),'signstring':OO0OO000000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:496
                        OOOOO0OO0OO000O00 =requests .request ('get',f'{host}/user',headers =O0000O0O0O00000O0 ).json ()#line:497
                        if 'status'in OOOOO0OO0OO000O00 :#line:499
                            if OOOOO0OO0OO000O00 ['status']==200 :#line:500
                                invited_new .append (OOOOO0OO0OO000O00 ['data']['inner_id'])#line:501
        except Exception as OO0OOOOO0000OOOOO :#line:502
            print (OO0OOOOO0000OOOOO )#line:503
    def game_map (O0O0O0O0000O0OOO0 ):#line:506
        try :#line:507
            O0OOOOOO0O00OOO00 =f'__{timi_new()}'#line:508
            OO000OO0000O0O0OO ={'source':'scsc','authorization':O0O0O0O0000O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOOO0O00OOO00 ),'signstring':O0OOOOOO0O00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:519
            OO000O0O0O0000O00 =requests .request ('get',f'{host}/game/map',headers =OO000OO0000O0O0OO ).json ()#line:520
            if 'status'in OO000O0O0O0000O00 :#line:522
                if OO000O0O0O0000O00 ['status']==200 :#line:523
                    for O0OO000OO0O0O0OOO in OO000O0O0O0000O00 ['data']['list'][0 ]['crops']:#line:524
                        O0O0O0OOO00OOOOO0 =O0OO000OO0O0O0OOO ['level']#line:526
                        if O0O0O0OOO00OOOOO0 ==41 :#line:527
                            OO0OOO00OO00O00O0 =O0OO000OO0O0O0OOO ['crop_name']#line:528
                            OO0O0O00OOO0OO0OO =O0OO000OO0O0O0OOO ['count']#line:529
                            if OO0O0O00OOO0OO0OO >0 :#line:530
                                print (f'【农业资产】:{OO0OOO00OO00O00O0}丨数量:{OO0O0O00OOO0OO0OO}')#line:531
                                if float (datetime .datetime .now ().hour )>8 :#line:532
                                    O0O0O0O0000O0OOO0 .the_query ()#line:533
        except Exception as OOOOOOO0OO00000O0 :#line:534
            print (OOOOOOO0OO00000O0 )#line:535
    def give_gold (OO0000O00OOOOOOOO ):#line:538
        try :#line:539
            OOO0OOOOOOO000OO0 =f'__{timi_new()}'#line:540
            OOO0OOOO0O00O0000 ={'source':'scsc','authorization':OO0000O00OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOOO000OO0 ),'signstring':OOO0OOOOOOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OOOOOO0OO0O0O0O0O =requests .request ('get',f'{host}/user',headers =OOO0OOOO0O00O0000 ).json ()#line:552
            if 'status'in OOOOOO0OO0O0O0O0O :#line:553
                if OOOOOO0OO0O0O0O0O ['status']==200 :#line:554
                    if float (OO0000O00OOOOOOOO .doneeNo )!=0 :#line:555
                        OOO0000O00OO00OO0 =OOOOOO0OO0O0O0O0O ['data']['assets']['gold']#line:556
                        if float (OOO0000O00OO00OO0 )>float (OO0000O00OOOOOOOO .innerId ):#line:557
                            O00000O0OO0OO000O =int (float (OOO0000O00OO00OO0 )/1.1 )#line:558
                            OOO0OOOOOOO000OO0 =f'_doneeNo={OO0000O00OOOOOOOO.doneeNo}&quantity={O00000O0OO0OO000O}_{timi_new()}'#line:559
                            OOO0OOOO0O00O0000 ={'source':'scsc','authorization':OO0000O00OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOOOOOO000OO0 ),'signstring':OOO0OOOOOOO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:570
                            OOOO0OOOOO0O000O0 ={"quantity":O00000O0OO0OO000O ,"doneeNo":OO0000O00OOOOOOOO .doneeNo }#line:574
                            OO0O00O0O00O0O00O =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0OOOO0O00O0000 ,data =OOOO0OOOOO0O000O0 ).json ()#line:575
                            if 'status'in OO0O00O0O00O0O00O :#line:577
                                if OO0O00O0O00O0O00O ['status']==200 :#line:578
                                    if OO0O00O0O00O0O00O ['data']:#line:579
                                        print (f'【赠送种子】:赠送{O00000O0OO0OO000O}种子给{OO0000O00OOOOOOOO.doneeNo}成功')#line:580
                    else :#line:581
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:582
        except Exception as OOO0OOO00O0O0000O :#line:583
            print (OOO0OOO00O0O0000O )#line:584
    def invitation (OOO00OOOO000OOOOO ):#line:586
        try :#line:587
            _O0O000OOO0O0OO0OO =float (bundled_def ())/4 #line:588
            O00OOOOO0000OOO00 =f'_innerId={int(_O0O000OOO0O0OO0OO)}_{timi_new()}'#line:589
            OOO0OOO0OOOOOOOOO ={'source':'scsc','authorization':OOO00OOOO000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOO0000OOO00 ),'signstring':O00OOOOO0000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            OOOO0OO0000O0OOOO ={"innerId":int (_O0O000OOO0O0OO0OO )}#line:601
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0OOO0OOOOOOOOO ,data =OOOO0OO0000O0OOOO )#line:602
        except Exception as O0O0OOO0000O0O000 :#line:603
            print (O0O0OOO0000O0O000 )#line:604
    def winning_rewards (OOOO00OOOOOO0O000 ):#line:607
        try :#line:608
            OOO00O00OO00OO000 =f'__{timi_new()}'#line:609
            O00OO00O0O0OOO0OO ={'source':'scsc','authorization':OOOO00OOOOOO0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00OO00OO000 ),'signstring':OOO00O00OO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
            O00O0O000OOO0O00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO00O0O0OOO0OO ).json ()#line:621
            if 'status'in O00O0O000OOO0O00O :#line:623
                if O00O0O000OOO0O00O ['status']==200 :#line:624
                    if O00O0O000OOO0O00O ['data']['amount']:#line:625
                        O0OOO0OOO0O0O000O =O00O0O000OOO0O00O ['data']['amount']['gold']#line:626
                        return O0OOO0OOO0O0O000O #line:627
                    else :#line:628
                        return 0 #line:629
        except Exception as O0OO000O0OO0O0O00 :#line:630
            print (O0OO000O0OO0O0O00 )#line:631
    def certification (OO000OOO00O00O0OO ):#line:634
        try :#line:635
            O0OOOO0O00OOOO000 =f'__{timi_new()}'#line:636
            OOOOO0OO0OOO0OOO0 ={'source':'scsc','authorization':OO000OOO00O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O00OOOO000 ),'signstring':O0OOOO0O00OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:647
            O0OOO00OOO000000O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOOOO0OO0OOO0OOO0 ).json ()#line:648
            if 'status'in O0OOO00OOO000000O :#line:650
                if O0OOO00OOO000000O ['status']==200 :#line:651
                    if O0OOO00OOO000000O ['data']['result']:#line:652
                        OO0O0OOOO0OOO00OO =O0OOO00OOO000000O ['data']['nick_name']#line:653
                        return OO0O0OOOO0OOO00OO #line:654
                    else :#line:655
                        weishim .append (OO000OOO00O00O0OO .token )#line:656
                        return '未实名'#line:657
        except Exception as OOO0000000OOOOOO0 :#line:658
            print (OOO0000000OOOOOO0 )#line:659
    def crops_illustrated (OO0OOO000OO0O00OO ):#line:662
        try :#line:663
            OOO0OO0OOO000000O =f'__{timi_new()}'#line:664
            O00OO0OOOOO0OO0OO ={'source':'scsc','authorization':OO0OOO000OO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO000000O ),'signstring':OOO0OO0OOO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:675
            O00O0OOOOOOO0OO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00OO0OOOOO0OO0OO ).json ()#line:676
            if 'status'in O00O0OOOOOOO0OO00 :#line:678
                if O00O0OOOOOOO0OO00 ['status']==200 :#line:679
                    O0O0O0OO0O0OO0OOO =O00O0OOOOOOO0OO00 ['data'][0 ]['crops']#line:680
                    for OOO0OOOOOOO0O00O0 in O0O0O0OO0O0OO0OOO :#line:681
                        if OOO0OOOOOOO0O00O0 ['ill_clover_award']:#line:682
                            if float (OOO0OOOOOOO0O00O0 ['ill_clover_award'])>1 :#line:683
                                if OOO0OOOOOOO0O00O0 ['is_finish']:#line:684
                                    if not OOO0OOOOOOO0O00O0 ['is_getit']:#line:685
                                        if OO0OOO000OO0O00OO .certification ()!='未实名':#line:686
                                            OOO0OO0OOO000000O =f'_award_level={OOO0OOOOOOO0O00O0["level"]}_{timi_new()}'#line:687
                                            O00OO0OOOOO0OO0OO ={'source':'scsc','authorization':OO0OOO000OO0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO000000O ),'signstring':OOO0OO0OOO000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:698
                                            OO000O000O00O0O0O ={"award_level":OOO0OOOOOOO0O00O0 ['level']}#line:699
                                            OO0OOO0000000O0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00OO0OOOOO0OO0OO ,json =OO000O000O00O0O0O ).json ()#line:701
                                            if 'status'in OO0OOO0000000O0OO :#line:702
                                                if OO0OOO0000000O0OO ['status']==200 :#line:703
                                                    O0OO0000O0OO00OOO =OO0OOO0000000O0OO ['data']['ill_clover_award']#line:704
                                                    print (f'【图鉴奖励】:领取{OOO0OOOOOOO0O00O0["crop_name"]}成就丨奖励{O0OO0000O0OO00OOO}☘️')#line:706
                                                if OO0OOO0000000O0OO ['status']==500 :#line:707
                                                    print (f'【图鉴奖励】:{OO0OOO0000000O0OO["message"]}')#line:708
        except Exception as OOOOOOO000O00000O :#line:709
            print (OOOOOOO000O00000O )#line:710
    def watched_ad (O00O0O0OO000OO00O ):#line:713
        try :#line:714
            O0OO0OOOOOO0O0000 =f'__{timi_new()}'#line:715
            O000000O00O00OOO0 ={'source':'scsc','authorization':O00O0O0OO000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOOOO0O0000 ),'signstring':O0OO0OOOOOO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:726
            O00O0OO0000OO000O =requests .request ('get',f'{host}/game/getAllData',headers =O000000O00O00OOO0 ).json ()#line:727
            if 'status'in O00O0OO0000OO000O :#line:729
                if O00O0OO0000OO000O ['status']==200 :#line:730
                    if 'offlineInfo'in O00O0OO0000OO000O ['data']:#line:731
                        time .sleep (random .randint (1 ,3 ))#line:732
                        O0OOOO0OO0OOOO000 =O00O0OO0000OO000O ['data']['offlineInfo']['off_minute']#line:733
                        O0O0OOOO00OO00000 =float (O00O0OO0000OO000O ['data']['silver'])/1000000000000 #line:734
                        time .sleep (1 )#line:735
                        requests .request ('post',f'{host}/game/watched-ad',headers =O000000O00O00OOO0 ).json ()#line:736
                        time .sleep (2 )#line:737
                        OO00O000O000OO000 =requests .request ('get',f'{host}/game/getAllData',headers =O000000O00O00OOO0 ).json ()#line:738
                        if 'status'in OO00O000O000OO000 :#line:740
                            if OO00O000O000OO000 ['status']==200 :#line:741
                                O00OOO0OO0O0OO0O0 =float (OO00O000O000OO000 ['data']['silver'])/1000000000000 #line:742
                                OOOOO00O00OOOOO00 =str (O00OOO0OO0O0OO0O0 -O0O0OOOO00OO00000 )[:6 ]#line:743
                                print (f'【离线奖励】:翻倍离线{O0OOOO0OO0OOOO000}分钟奖励🌱数量:{OOOOO00O00OOOOO00}t粒')#line:744
        except Exception as O0000O0O0000OO0O0 :#line:745
            print (O0000O0O0000OO0O0 )#line:746
    def user_ad (OOOO00OOO0O0O000O ):#line:749
        try :#line:750
            O00O0O00000O00OO0 =f'__{timi_new()}'#line:751
            O0O0OOO0000O00OOO ={'source':'scsc','authorization':OOOO00OOO0O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O00000O00OO0 ),'signstring':O00O0O00000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:762
            O0OO000O00O000OO0 =requests .request ('get',f'{host}/user/ad',headers =O0O0OOO0000O00OOO ).json ()#line:763
            if 'status'in O0OO000O00O000OO0 :#line:765
                if O0OO000O00O000OO0 ['status']==200 :#line:766
                    OOOO0OO00OOOO0O0O =O0OO000O00O000OO0 ['data']['max_time']#line:767
                    OO0O0OO0OO0O0OO0O =O0OO000O00O000OO0 ['data']['watch_time']#line:768
                    O0OOOOOOOOO0O00OO =O0OO000O00O000OO0 ['data']['added_time']#line:769
                    print (f'【获取种子】:获取🌱剩余{O0OOOOOOOOO0O00OO + OOOO0OO00OOOO0O0O - OO0O0OO0OO0O0OO0O}次丨好友提供:{O0OOOOOOOOO0O00OO}次')#line:770
                    if O0OOOOOOOOO0O00OO +OOOO0OO00OOOO0O0O -OO0O0OO0OO0O0OO0O >0 :#line:771
                        time .sleep (random .randint (16 ,19 ))#line:772
                        O0O0O000O00000O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0O0OOO0000O00OOO ).json ()#line:773
                        if 'status'in O0O0O000O00000O00 :#line:775
                            if O0O0O000O00000O00 ['status']==200 :#line:776
                                O0OO000O00000OO00 =float (O0O0O000O00000O00 ['data']['silver'])/1000000000000 #line:777
                                print (f'【获取种子】:获得🌱:{int(O0OO000O00000OO00)}t粒')#line:778
                                return True #line:779
                            if O0O0O000O00000O00 ['status']==500 :#line:780
                                OOOO0OO00OOO000O0 =O0O0O000O00000O00 ['message']#line:781
                                print (f'【获取种子】:{OOOO0OO00OOO000O0}')#line:782
                                return False #line:783
        except Exception as O00OOO000OO00O00O :#line:784
            print (O00OOO000OO00O00O )#line:785
    def synthetic (O0O00O0OOOOOO00O0 ):#line:788
        global id ,g #line:789
        try :#line:790
            OOO00000O000OOOOO =O0O00O0OOOOOO00O0 .level_new ()#line:791
            O000OO0OO00000000 =random .randint (9 ,11 )#line:792
            OO00O0O00OOO0OOO0 =f'_site=8&targetSite={O000OO0OO00000000}_{timi_new()}'#line:793
            OO00O0OOOOOO000O0 ={'source':'scsc','authorization':O0O00O0OOOOOO00O0 .token ,'timestamp':timi_new (),'sign':sign (OO00O0O00OOO0OOO0 ),'signstring':OO00O0O00OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:804
            O0O00O00O000O000O ={"site":int (8 ),"targetSite":int (O000OO0OO00000000 )}#line:805
            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OOOOOO000O0 ,json =O0O00O00O000O000O )#line:806
            while True :#line:807
                OOOO00OOO00O0O00O =f'__{timi_new()}'#line:808
                OO00O0OO0OO0O0O00 ={'source':'scsc','authorization':O0O00O0OOOOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OOO00O0O00O ),'signstring':OOOO00OOO00O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:819
                OOO00O000OO0O000O =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO0OO0O0O00 ).json ()#line:820
                if 'status'in OOO00O000OO0O000O :#line:822
                    if OOO00O000OO0O000O ['status']==200 :#line:823
                        O0OO0O0O00O0O0OO0 =OOO00O000OO0O000O ['data']['cropList']#line:824
                        O0O00OOOOO000OO0O =OOO00O000OO0O000O ['data']['gameCoreDataDBid']#line:825
                        OOOOOO0O0OO00O00O =float (OOO00O000OO0O000O ['data']['silver'])/1000000000000 #line:826
                        O0OOO00OOO000OO0O =0 #line:831
                        for O0000OOOOOOOOOO0O in O0OO0O0O00O0O0OO0 :#line:832
                            if not O0000OOOOOOOOOO0O :#line:833
                                OO00000O0O000O0O0 =f'_crop_id={O0O00OOOOO000OO0O}&site={O0OOO00OOO000OO0O}_{O0O00O0OOOOOO00O0.time}'#line:834
                                OOO0OOO0O0OOO0OO0 ={'source':'scsc','authorization':O0O00O0OOOOOO00O0 .token ,'timestamp':O0O00O0OOOOOO00O0 .time ,'sign':sign (OO00000O0O000O0O0 ),'signstring':OO00000O0O000O0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:844
                                OOO00O00OO000000O ={"site":O0OOO00OOO000OO0O ,"crop_id":O0O00OOOOO000OO0O }#line:845
                                O00O0OO0000O0O000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO0OOO0O0OOO0OO0 ,data =OOO00O00OO000000O ).json ()#line:846
                                time .sleep (random .randint (1 ,3 )/10 )#line:848
                                if 'status'in O00O0OO0000O0O000 :#line:849
                                    if O00O0OO0000O0O000 ['status']==200 :#line:850
                                        if O00O0OO0000O0O000 ['message']=='种子数量不足':#line:851
                                            OOO00000O000OOOOO =O0O00O0OOOOOO00O0 .level_new ()#line:852
                                            print (f'【种植合成】:{O00O0OO0000O0O000["message"]}')#line:853
                                            if not O0O00O0OOOOOO00O0 .user_ad ():#line:854
                                                return False #line:855
                                    if O00O0OO0000O0O000 ['status']==500 :#line:856
                                        print (f'【种植合成】:{O00O0OO0000O0O000["message"]}')#line:857
                                        return False #line:858
                            O0OOO00OOO000OO0O +=1 #line:859
                        O00OOO0O0OOO000OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00O0OO0OO0O0O00 ).json ()#line:860
                        O00000O0O00O0O00O =O00OOO0O0OOO000OO ['data']['cropList']#line:861
                        OOOO0OOOOOO0OO0OO =False #line:862
                        for O0000OOOOOOOOOO0O in range (12 ):#line:863
                            id =O00000O0O00O0O00O [O0000OOOOOOOOOO0O ]['level']#line:864
                            if float (OOO00000O000OOOOO )-float (id )>9 :#line:865
                                O0OO0OO0O00OO0OOO =f'_site={O0000OOOOOOOOOO0O}_{timi_new()}'#line:866
                                OOOO0O000000O00O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OOOOOO00O0 .token ,'timestamp':timi_new (),'sign':sign (O0OO0OO0O00OO0OOO ),'signstring':O0OO0OO0O00OO0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:877
                                OO0OOO00O000OO00O ={"site":O0000OOOOOOOOOO0O }#line:878
                                OOOO00OO0OOOOO00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO0O000000O00O0 ,data =OO0OOO00O000OO00O ).json ()#line:880
                                if 'status'in OOOO00OO0OOOOO00O :#line:881
                                    if OOOO00OO0OOOOO00O ['status']==200 :#line:882
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:883
                            if id !=0 :#line:884
                                for OOO000OOO0O00OO00 in range (11 ):#line:885
                                    O0O0OOO0000O0OOOO =OOO000OOO0O00OO00 +1 #line:886
                                    g =O00000O0O00O0O00O [O0O0OOO0000O0OOOO ]['level']#line:887
                                    if id ==g :#line:888
                                        O0OO0O00OOOO00O00 =OOO000OOO0O00OO00 +2 #line:889
                                        if O0OO0O00OOOO00O00 !=O0000OOOOOOOOOO0O +1 :#line:890
                                            OOO0OOO00O00O0O00 =O0000OOOOOOOOOO0O +1 #line:891
                                            time .sleep (random .randint (1 ,3 )/10 )#line:893
                                            OO00O0O00OOO0OOO0 =f'_site={OOO0OOO00O00O0O00 - 1}&targetSite={O0OO0O00OOOO00O00 - 1}_{timi_new()}'#line:894
                                            OO00O0OOOOOO000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0O00O0OOOOOO00O0 .token ,'timestamp':timi_new (),'sign':sign (OO00O0O00OOO0OOO0 ),'signstring':OO00O0O00OOO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:911
                                            O0O0OO0OOO00OOOOO ={"site":int (OOO0OOO00O00O0O00 -1 ),"targetSite":int (O0OO0O00OOOO00O00 -1 )}#line:912
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OOOOOO000O0 ,json =O0O0OO0OOO00OOOOO )#line:913
                                            OOOO0OOOOOO0OO0OO =True #line:915
                                    if OOOO0OOOOOO0OO0OO :#line:916
                                        break #line:917
                                if OOOO0OOOOOO0OO0OO :#line:918
                                    break #line:919
        except :#line:920
            O0O00O0OOOOOO00O0 .synthetic ()#line:921
    def level_new (O0OOOOO000OO00O00 ):#line:924
        try :#line:925
            OOO00OOO0000O00O0 =f'__{timi_new()}'#line:926
            OOO00O0OOOO0O00OO ={'source':'scsc','authorization':O0OOOOO000OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOO0000O00O0 ),'signstring':OOO00OOO0000O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:937
            O00O0OO000O0O00OO =requests .request ('get',f'{host}/user',headers =OOO00O0OOOO0O00OO ).json ()#line:938
            if 'status'in O00O0OO000O0O00OO :#line:939
                if O00O0OO000O0O00OO ['status']==200 :#line:940
                    return float (O00O0OO000O0O00OO ['data']['level'])#line:941
        except Exception as OOO0000OOOOO000O0 :#line:942
            print (OOO0000OOOOO000O0 )#line:943
    def propsraffle (O000OO000O0OO00O0 ):#line:946
        try :#line:947
            while True :#line:948
                O00OOO00O0000OO0O =f'__{timi_new()}'#line:949
                OOO00O00O0OO0000O ={'source':'scsc','authorization':O000OO000O0OO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00O0000OO0O ),'signstring':O00OOO00O0000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:960
                O00OO000OOO0OO000 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00O00O0OO0000O ).json ()#line:961
                if 'status'in O00OO000OOO0OO000 :#line:963
                    if O00OO000OOO0OO000 ['status']==200 :#line:964
                        OO0OO000O000OOO0O =O00OO000OOO0OO000 ['data']['rows']#line:965
                        O0OOO000OOO0O00OO =O00OO000OOO0OO000 ['data']['vstate']#line:966
                        if OO0OO000O000OOO0O ==5 or OO0OO000O000OOO0O ==6 or OO0OO000O000OOO0O ==7 :#line:967
                            OO0OOOOOOO0O000OO =O00OO000OOO0OO000 ['data']['silver']#line:968
                            print (f'【转盘抽奖】:获得种子:{OO0OOOOOOO0O000OO}')#line:969
                        if OO0OO000O000OOO0O ==1 or OO0OO000O000OOO0O ==2 or OO0OO000O000OOO0O ==3 :#line:970
                            O0OO0O0O000O00OO0 =O00OO000OOO0OO000 ['data']['clover']#line:971
                            print (f'【转盘抽奖】:获得三叶草:{O0OO0O0O000O00OO0}')#line:972
                        if OO0OO000O000OOO0O ==4 or OO0OO000O000OOO0O ==8 :#line:973
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:974
                        if OO0OO000O000OOO0O =='抽奖次数已用完':#line:978
                            break #line:1012
                time .sleep (random .randint (8 ,15 )/10 )#line:1013
        except Exception as O0O0O00OO0O00O0O0 :#line:1014
            print (O0O0O00OO0O00O0O0 )#line:1015
    def friends_invitation (O000O00O0OO0OOOO0 ):#line:1018
        try :#line:1019
            O0OOOO000OO00O00O =f'__{timi_new()}'#line:1020
            OO00OOOO00O000O0O ={'source':'scsc','authorization':O000O00O0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO000OO00O00O ),'signstring':O0OOOO000OO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1031
            OO0OOOOOO0OOO0OOO =requests .request ('get',f'{host}/friends',headers =OO00OOOO00O000O0O ).json ()#line:1032
            if 'status'in OO0OOOOOO0OOO0OOO :#line:1033
                if OO0OOOOOO0OOO0OOO ['status']==200 :#line:1034
                    OOO0OOO00O00OO0O0 =OO0OOOOOO0OOO0OOO ['data']['myInviteter']#line:1035
                    if OOO0OOO00O00OO0O0 :#line:1036
                        OO0O0O00000OOOO00 =OOO0OOO00O00OO0O0 ['user']['nickname']#line:1037
                        OO0OOO00O0OO0000O =O000O00O0OO0OOOO0 .certification ()#line:1038
                        print (f'【查邀请人】:我的邀请人:{OO0O0O00000OOOO00}丨实名:{OO0OOO00O0OO0000O}')#line:1039
                    else :#line:1040
                        if O000O00O0OO0OOOO0 .innerId !='0':#line:1041
                            O000O00O0OO0OOOO0 .invitation ()#line:1042
        except Exception as O0O00O0O000OOOOOO :#line:1043
            print (O0O00O0O000OOOOOO )#line:1044
    def add_clover (O0OOOOOOOO00O00OO ):#line:1047
        global golden_seed #line:1048
        try :#line:1049
            O00000O0OO0OOO00O =f'__{timi_new()}'#line:1050
            O0OO000O0OO0000O0 ={'source':'scsc','authorization':O0OOOOOOOO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO0OOO00O ),'signstring':O00000O0OO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1061
            O00O0O0O0000O00OO =requests .request ('get',f'{host}/assets/clovers',headers =O0OO000O0OO0000O0 ).json ()#line:1062
            if 'status'in O00O0O0O0000O00OO :#line:1064
                if O00O0O0O0000O00OO ['status']==200 :#line:1065
                    O0O00000OO00000OO =O00O0O0O0000O00OO ['data']['clover']#line:1066
                    O0OO0OOOO0O000O0O =O00O0O0O0000O00OO ['data']['used_clover']#line:1067
                    O00000O0O0OOO0O0O =float (O0O00000OO00000OO )-float (O0OO0OOOO0O000O0O )#line:1068
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OO0OOOO0O000O0O}')#line:1069
                    if O0OOOOOOOO00O00OO .certification ()!='未实名':#line:1070
                        if O00000O0O0OOO0O0O >1 :#line:1071
                            O00000O0OO0OOO00O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000O0O0OOO0O0O)}_{timi_new()}'#line:1072
                            OOO0000000O0O0000 ={'source':'scsc','authorization':O0OOOOOOOO00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO0OOO00O ),'signstring':O00000O0OO0OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1083
                            O00OO0OOOO0O0O0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000O0O0OOO0O0O )}#line:1084
                            O00OOOO0OOOO0OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO0000000O0O0000 ,data =O00OO0OOOO0O0O0OO ).json ()#line:1085
                            if 'status'in O00OOOO0OOOO0OOOO :#line:1087
                                if O00OOOO0OOOO0OOOO ['status']==200 :#line:1088
                                    print (f'【参与抽奖】:添加☘️:{O00OOOO0OOOO0OOOO["data"]}丨数量:{O00000O0O0OOO0O0O}')#line:1089
                                if O00OOOO0OOOO0OOOO ['status']==500 :#line:1090
                                    print (f'【参与抽奖】:添加☘️:{O00OOOO0OOOO0OOOO["message"]}')#line:1091
            O0OOO0O000OO00OO0 =requests .request ('get',f'{host}/lottery',headers =O0OO000O0OO0000O0 ).json ()#line:1092
            OO000O00OO0O00O0O =O0OOOOOOOO00O00OO .winning_rewards ()#line:1094
            if 'status'in O0OOO0O000OO00OO0 :#line:1095
                if O0OOO0O000OO00OO0 ['status']==200 :#line:1096
                    O00OO000OOO0O00O0 =O0OOO0O000OO00OO0 ['data'][0 ]['day_get_gold_quantity']#line:1097
                    golden_seed +=float (O00OO000OOO0O00O0 )#line:1098
                    OO000OO0OOOO0O000 =O0OOO0O000OO00OO0 ['data'][1 ]['value']#line:1099
                    OO00OOOO0O0O0OOO0 =O0OOO0O000OO00OO0 ['data'][0 ]['join_number']#line:1100
                    OO0OOOO0O000000OO =int (float (O0OOO0O000OO00OO0 ['data'][0 ]['totalValue']))#line:1101
                    OO000OOOO0OOOO0OO =float (OO000OO0OOOO0O000 /OO0OOOO0O000000OO )*10000 #line:1102
                    O0000O0OOO00O0OOO =OO0OOOO0O000000OO /OO00OOOO0O0O0OOO0 #line:1103
                    print (f'【参与抽奖】:预计每天中{str(O00OO000OOO0O00O0)[:6]}颗金种子丨好友收益:{str(OO000O00OO0O00O0O)[:6]}')#line:1104
                    print (f'【抽奖统计】:每1万☘️中{str(OO000OOOO0OOOO0OO)[:6]}颗金种子丨☘️人均:{str(O0000O0OOO00O0OOO)[:7]}️')#line:1105
        except Exception as OO0000OOO000O00OO :#line:1106
            print (OO0000OOO000O00OO )#line:1107
    def energy (OO0OOO0OO0OOOO000 ):#line:1110
        try :#line:1111
            while True :#line:1112
                OO0OOOO000OO0O00O =f'__{timi_new()}'#line:1113
                OO0O0OO0OO00OO00O ={'source':'scsc','authorization':OO0OOO0OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO000OO0O00O ),'signstring':OO0OOOO000OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1124
                O0OO000OO000OO000 =requests .request ('get',f'{host}/energy/general',headers =OO0O0OO0OO00OO00O ).json ()#line:1125
                if 'status'in O0OO000OO000OO000 :#line:1127
                    if O0OO000OO000OO000 ['status']==200 :#line:1128
                        OO0OO0OO00O0OO0O0 =O0OO000OO000OO000 ['data']['ordinary_water']#line:1129
                        O00O000O00O0OO0OO =O0OO000OO000OO000 ['data']['ordinary_fertilizer']#line:1130
                        OOOOOOOOOOO0OOOOO =O0OO000OO000OO000 ['data']['videoStatus']#line:1131
                        OOO00OO0O0OO00OOO =O0OO000OO000OO000 ['data']['waterVideoKey']#line:1132
                        print (f'【我的营养】:肥料:{str(O00O000O00O0OO0OO).split(".")[0]}丨水滴:{str(OO0OO0OO00O0OO0O0).split(".")[0]}')#line:1134
                        if float (O00O000O00O0OO0OO )<96 :#line:1135
                            if OOOOOOOOOOO0OOOOO :#line:1136
                                time .sleep (random .randint (160 ,180 )/10 )#line:1137
                                O0OO0O0OOO00000OO =99 -float (O00O000O00O0OO0OO )#line:1138
                                O0OO0OOO0000O0O0O ={"fertilizer":str (O0OO0O0OOO00000OO ).split ('.')[0 ]}#line:1139
                                O00O0000O00000000 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO0O0OO0OO00OO00O ).json ()#line:1141
                                if 'status'in O00O0000O00000000 :#line:1143
                                    if O00O0000O00000000 ['status']==200 :#line:1144
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0000O00000000["message"]}')#line:1145
                                    if O00O0000O00000000 ['status']==500 :#line:1146
                                        print (f'【购买肥料】:看广告获取肥料:{O00O0000O00000000["message"]}')#line:1147
                                        break #line:1148
                                if float (O00O000O00O0OO0OO )<78 :#line:1150
                                    O0OO0O0OOO00000OO =80 -float (O00O000O00O0OO0OO )#line:1151
                                    O0O0O0000OOO000OO =f'_fertilizer={int(O0OO0O0OOO00000OO)}_{timi_new()}'#line:1152
                                    OO0OOOOOO0OOO0O00 ={'source':'scsc','authorization':OO0OOO0OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0000OOO000OO ),'signstring':O0O0O0000OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1163
                                    OOO0OOOOOO00O000O ={"fertilizer":int (O0OO0O0OOO00000OO )}#line:1164
                                    OOO000000000O00OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0OOOOOO0OOO0O00 ,data =OOO0OOOOOO00O000O ).json ()#line:1166
                                    if 'status'in OOO000000000O00OO :#line:1168
                                        if OOO000000000O00OO ['status']==200 :#line:1169
                                            print (f'【购买肥料】:购买肥料:{OOO000000000O00OO["message"]}丨数量:{int(O0OO0O0OOO00000OO)}')#line:1170
                                        if OOO000000000O00OO ['status']==500 :#line:1171
                                            print (f'【购买肥料】:购买肥料:{OOO000000000O00OO["message"]}丨数量:{int(O0OO0O0OOO00000OO)}')#line:1172
                                            O00000OOOO00OOOOO =OOO000000000O00OO ["message"].split ('-')[1 ]#line:1173
                                            O0O0O0O00O0OOOO0O =f'__{timi_new()}'#line:1174
                                            OOOO00OOO0O00O00O ={'source':'scsc','authorization':OO0OOO0OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0OOOO0O ),'signstring':O0O0O0O00O0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1185
                                            OO00OO0OOO00O0O00 =requests .request ('get',f'{host}/user',headers =OOOO00OOO0O00O00O ).json ()#line:1186
                                            if 'status'in OO00OO0OOO00O0O00 :#line:1187
                                                if OO00OO0OOO00O0O00 ['status']==200 :#line:1188
                                                    OO00000OOO000O0O0 =OO00OO0OOO00O0O00 ['data']['inner_id']#line:1189
                                                    if give_gold (OO00000OOO000O0O0 ,float (O00000OOOO00OOOOO )+1 ):#line:1190
                                                        OO0OOO0OO0OOOO000 .energy ()#line:1191
                        if float (OO0OO0OO00O0OO0O0 )<880 :#line:1192
                            if OOO00OO0O0OO00OOO :#line:1193
                                time .sleep (random .randint (160 ,180 )/10 )#line:1194
                                OO000000000O0OOOO =999 -float (OO0OO0OO00O0OO0O0 )#line:1195
                                O00O0OOOO0000OOOO ={"water":str (OO000000000O0OOOO ).split ('.')[0 ]}#line:1196
                                OO0OO0O0000000O00 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO0O0OO0OO00OO00O ).json ()#line:1198
                                if 'status'in OO0OO0O0000000O00 :#line:1200
                                    if OO0OO0O0000000O00 ['status']==200 :#line:1201
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO0O0000000O00["message"]}')#line:1202
                                    if OO0OO0O0000000O00 ['status']==500 :#line:1203
                                        print (f'【购买水滴】:看广告获取水滴:{OO0OO0O0000000O00["message"]}')#line:1204
                                        break #line:1205
                                if float (OO0OO0OO00O0OO0O0 )<780 :#line:1206
                                    OO000000000O0OOOO =800 -float (OO0OO0OO00O0OO0O0 )#line:1207
                                    OOOO00OO000O0OO00 =f'_water={int(OO000000000O0OOOO)}_{timi_new()}'#line:1208
                                    O0OOO0O000O0OOO0O ={'source':'scsc','authorization':OO0OOO0OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00OO000O0OO00 ),'signstring':OOOO00OO000O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1219
                                    O000OOOO0O0000OO0 ={"water":int (OO000000000O0OOOO )}#line:1220
                                    O0OO0OOOO0O0OO0OO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OOO0O000O0OOO0O ,data =O000OOOO0O0000OO0 ).json ()#line:1222
                                    if 'status'in O0OO0OOOO0O0OO0OO :#line:1224
                                        if O0OO0OOOO0O0OO0OO ['status']==200 :#line:1225
                                            print (f'【购买水滴】:购买水滴:{O0OO0OOOO0O0OO0OO["message"]}丨数量:{int(OO000000000O0OOOO)}')#line:1226
                                        if O0OO0OOOO0O0OO0OO ['status']==500 :#line:1227
                                            print (f'【购买水滴】:购买水滴:{O0OO0OOOO0O0OO0OO["message"]}丨数量:{int(OO000000000O0OOOO)}')#line:1228
                                            O00000OOOO00OOOOO =O0OO0OOOO0O0OO0OO ["message"].split ('-')[1 ]#line:1229
                                            O0O0O0O00O0OOOO0O =f'__{timi_new()}'#line:1230
                                            OOOO00OOO0O00O00O ={'source':'scsc','authorization':OO0OOO0OO0OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00O0OOOO0O ),'signstring':O0O0O0O00O0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1241
                                            OO00OO0OOO00O0O00 =requests .request ('get',f'{host}/user',headers =OOOO00OOO0O00O00O ).json ()#line:1242
                                            if 'status'in OO00OO0OOO00O0O00 :#line:1243
                                                if OO00OO0OOO00O0O00 ['status']==200 :#line:1244
                                                    OO00000OOO000O0O0 =OO00OO0OOO00O0O00 ['data']['inner_id']#line:1245
                                                    if give_gold (OO00000OOO000O0O0 ,float (O00000OOOO00OOOOO )+1 ):#line:1246
                                                        OO0OOO0OO0OOOO000 .energy ()#line:1247
                        break #line:1248
        except Exception as O00O0000O00000OOO :#line:1249
            print (O00O0000O00000OOO )#line:1250
def bundled_def ():#line:1253
    OOOO0O0O000OOOOOO =['5570536','7750212','7911652','7911680','7805624']#line:1254
    return OOOO0O0O000OOOOOO [random .randint (0 ,len (OOOO0O0O000OOOOOO )-1 )]#line:1255
def version_of_the_validation ():#line:1259
    return str ((95 -56 )/10 )#line:1260
def sc2 ():#line:1263
    return "19319#$%^&*((*"#line:1264
def OO00OO0OO0OO00OO00o0 ():#line:1267
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1269
def get_ip ():#line:1272
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1274
def gitee_validation ():#line:1277
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1278
def gitee_edition ():#line:1281
    try :#line:1282
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1283
    except :#line:1284
        sys .exit (0 )#line:1285
def O000OO000O0O00OOO00 ():#line:1289
    try :#line:1290
        OOO0OO00OO00OOOO0 =gitee_edition ()#line:1291
        if version_of_the_validation ()<OOO0OO00OO00OOOO0 ['CityEarth']['edition']:#line:1292
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00OO00OOOO0["CityEarth"]["edition"]}   ❌')#line:1293
            print (f'更新内容=>>{OOO0OO00OO00OOOO0["CityEarth"]["content"]}')#line:1294
        else :#line:1295
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO0OO00OO00OOOO0["CityEarth"]["edition"]}   ✅')#line:1296
            print (f'更新内容=>> {OOO0OO00OO00OOOO0["CityEarth"]["content"]}')#line:1297
    except Exception as O00O0OOO0O0O0OO00 :#line:1298
        print (O00O0OOO0O0O0OO00 )#line:1299
def sc3 ():#line:1302
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1303
if __name__ =='__main__':#line:1306
    start ()#line:1307
