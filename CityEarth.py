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
        OO0OOOOO000O000O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OO0OOOOO000O000O0)}个账号==========")#line:16
        for OOOO00O0OOOO0OO00 in OO0OOOOO000O000O0 :#line:17
            O00OOOOO00O0O000O =[]#line:18
            print (f"------------正在执行第{OO0OOOOO000O000O0.index(OOOO00O0OOOO0OO00) + 1}个账号------------")#line:19
            OOO0OO0OO0O0OOO00 =CityEarth (OOOO00O0OOOO0OO00 ,O00OOOOO00O0O000O ,OO0OOOOO000O000O0 .index (OOOO00O0OOOO0OO00 ))#line:20
            def OO0OOOO00000OO0O0 ():#line:22
                if OOO0OO0OO0O0OOO00 .base_info ():#line:24
                    OOO0OO0OO0O0OOO00 .sealing ()#line:26
                    OOO0OO0OO0O0OOO00 .invitenum ()#line:28
                    OOO0OO0OO0O0OOO00 .query_to_sell ()#line:30
                    OOO0OO0OO0O0OOO00 .game_map ()#line:32
                    OOO0OO0OO0O0OOO00 .friends_invitation ()#line:34
                    OOO0OO0OO0O0OOO00 .energy ()#line:36
                    OOO0OO0OO0O0OOO00 .add_clover ()#line:38
                    OOO0OO0OO0O0OOO00 .propsraffle ()#line:40
                    OOO0OO0OO0O0OOO00 .synthetic ()#line:42
                    OOO0OO0OO0O0OOO00 .crops_illustrated ()#line:44
                    OOO0OO0OO0O0OOO00 .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        OOO0OO0OO0O0OOO00 .give_gold ()#line:49
            O000OOOOO00O00O0O =threading .Thread (target =OO0OOOO00000OO0O0 )#line:51
            O000OOOOO00O00O0O .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理推送通知------------")#line:54
        time .sleep (0.5 )#line:55
        O00OOOO000OOOO000 =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00OOOO000OOOO000 +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for O0OO0O000OO0O0O0O in invited_new :#line:60
            print (O0OO0O000OO0O0O0O )#line:61
        print ('开始打印未实名的token')#line:62
        for O0O00O00OOOOOO000 in weishim :#line:63
            print (O0O00O00OOOOOO000 )#line:64
    except Exception as OO0O000O0O00OO0O0 :#line:65
        print (OO0O000O0O00OO0O0 )#line:66
def give_gold (O00OO00O0OO00OO0O ,OOOO0O00O0O0O0OOO ):#line:70
    try :#line:71
        OO0O000OOOO0OOOOO =f'_doneeNo={O00OO00O0OO00OO0O}&quantity={int(OOOO0O00O0O0O0OOO)}_{timi_new()}'#line:72
        O00OO0O000O0O0OO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO0O000OOOO0OOOOO ),'signstring':OO0O000OOOO0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OOOO000OOO00OOO00 ={"quantity":int (OOOO0O00O0O0O0OOO ),"doneeNo":O00OO00O0OO00OO0O }#line:87
        O00O0OOOO00O0O00O =requests .request ('post',f'{host}/finance/give-gold',headers =O00OO0O000O0O0OO0 ,data =OOOO000OOO00OOO00 ).json ()#line:88
        if 'status'in O00O0OOOO00O0O00O :#line:90
            if O00O0OOOO00O0O00O ['status']==200 :#line:91
                if O00O0OOOO00O0O00O ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OOOO0O00O0O0O0OOO)}种子给{O00OO00O0OO00OO0O}成功')#line:93
                    return True #line:94
            if O00O0OOOO00O0O00O ['status']==401 :#line:95
                print (f'【赠送种子】:{O00O0OOOO00O0O00O["message"]}')#line:96
                return False #line:97
            if O00O0OOOO00O0O00O ['status']==500 :#line:98
                print (f'【赠送种子】:{O00O0OOOO00O0O00O["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as OOOOO00OO0000O0OO :#line:102
        print (OOOOO00OO0000O0OO )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def sign (OO000O00000O0O0OO ):#line:110
    O0OOOO00O0O0O00OO =hashlib .md5 (OO000O00000O0O0OO .encode ()).hexdigest ()#line:111
    O0000OOOOOOO0OO00 =sc1 ()#line:112
    O0O0OO0000O0OO0OO =sc2 ()#line:113
    O0OO0OO0OO0OO00O0 =sc3 ()#line:114
    O00O0OOO0OOOOOOO0 =O0000OOOOOOO0OO00 +O0OOOO00O0O0O00OO +O0O0OO0000O0OO0OO +O0OO0OO0OO0OO00O0 #line:115
    O0OO0OO0OO0000000 =hashlib .md5 (O00O0OOO0OOOOOOO0 .encode ()).hexdigest ()#line:116
    return O0OO0OO0OO0000000 #line:117
def format_msg ():#line:120
    O0O0O0O0OOO00000O =""#line:121
    for O000O00O0O00O0OOO in msg_list :#line:122
        O0O0O0O0OOO00000O +=str (O000O00O0O00O0OOO )+"\r\n"#line:123
    return O0O0O0O0OOO00000O #line:124
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
def get_json_data (O0O0O0O0O000O0OOO ,OOO0OOOOOO0000O00 ,O00O0OOOO0000OO0O ,OOOO00O00O000OOO0 ):#line:147
    with open (O0O0O0O0O000O0OOO ,'rb')as OOO0O0O0O00O00OOO :#line:148
        O0O0000OO0O0O000O =json .load (OOO0O0O0O00O00OOO )#line:149
        O0O0000OO0O0O000O ['data'][OOO0OOOOOO0000O00 ][O00O0OOOO0000OO0O ]=OOOO00O00O000OOO0 #line:150
        OOO0000OO00000O0O =O0O0000OO0O0O000O #line:151
    OOO0O0O0O00O00OOO .close ()#line:152
    return OOO0000OO00000O0O #line:153
def write_json_data (O0OO0OOO000000000 ):#line:156
    with open (json_path1 ,'w')as O00000O0OO0O0000O :#line:157
        json .dump (O0OO0OOO000000000 ,O00000O0OO0O0000O )#line:158
    O00000O0OO0O0000O .close ()#line:159
    return True #line:160
class CityEarth :#line:163
    def __init__ (O0O00O0OO0O0O0OOO ,OOO0O00O0O00OO00O ,O00OOO0OOO0OO0O00 ,O0O0O00000O0OOOO0 ):#line:165
        try :#line:166
            O0O00O0OO0O0O0OOO .msg =O00OOO0OOO0OO0O00 #line:167
            O0O00O0OO0O0O0OOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:168
            O0O00O0OO0O0O0OOO .token =OOO0O00O0O00OO00O ['authorization']#line:169
            O0O00O0OO0O0O0OOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:170
            O0O00O0OO0O0O0OOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:171
            O0O00O0OO0O0O0OOO .elephant_user =OOO0O00O0O00OO00O ['elephant_user']#line:172
            O0O00O0OO0O0O0OOO .elephant_pswd =OOO0O00O0O00OO00O ['elephant_pswd']#line:173
            O0O00O0OO0O0O0OOO .elephant_Task_ID =OOO0O00O0O00OO00O ['elephant_Task_ID']#line:174
            O0O00O0OO0O0O0OOO .len_new =O0O0O00000O0OOOO0 #line:175
        except :#line:176
            print ('变量格式错误')#line:177
    def base_info (O0OO00OO00OO0OOO0 ):#line:180
        try :#line:181
            O0OO00OO00OO0OOO0 .watched_ad ()#line:183
            OOO00O00O0OO0O0O0 =f'__{timi_new()}'#line:184
            OO000OOOOO000OOO0 ={'source':'scsc','authorization':O0OO00OO00OO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O00O0OO0O0O0 ),'signstring':OOO00O00O0OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:195
            OOO0O000O0O0O0OOO =requests .request ('get',f'{host}/user',headers =OO000OOOOO000OOO0 ).json ()#line:196
            if 'status'in OOO0O000O0O0O0OOO :#line:198
                if OOO0O000O0O0O0OOO ['status']==200 :#line:199
                    OOOO0O0O0O00O000O =OOO0O000O0O0O0OOO ['data']['nickname']#line:200
                    OO0OOO0OOO0O00000 =OOO0O000O0O0O0OOO ['data']['inner_id']#line:201
                    OO000OO00O0000000 =OOO0O000O0O0O0OOO ['data']['assets']['gold']#line:202
                    O0O0OO0OO000000O0 =OOO0O000O0O0O0OOO ['data']['level']#line:203
                    print (f'【账号信息】:昵称:{OOOO0O0O0O00O000O[:5]}丨ID:{OO0OOO0OOO0O00000}丨等级:{O0O0OO0OO000000O0}丨金种子:{str(OO000OO00O0000000).split(".")[0]}')#line:205
                    if 'wx_'in OOOO0O0O0O00O000O :#line:206
                        O0OO00OO00OO0OOO0 .change_nickname ()#line:207
                if OOO0O000O0O0O0OOO ['status']==401 :#line:208
                    print ('【账号信息】:账号失效正在尝试登录')#line:209
                    if O0OO00OO00OO0OOO0 .elephant_user =='f':#line:210
                        return False #line:211
                    OO00O0O00OOO00O00 =Invalid_login .addtask (elephant_user =O0OO00OO00OO0OOO0 .elephant_user ,elephant_pswd =O0OO00OO00OO0OOO0 .elephant_pswd ,elephant_Task_ID =O0OO00OO00OO0OOO0 .elephant_Task_ID )#line:214
                    OOO0O00OOO00O0OOO =get_json_data (json_path ,O0OO00OO00OO0OOO0 .len_new ,'authorization',OO00O0O00OOO00O00 )#line:215
                    if write_json_data (OOO0O00OOO00O0OOO ):#line:216
                        print ('正在写入账号配置文件')#line:217
                    return False #line:218
                if OOO0O000O0O0O0OOO ['status']==500 :#line:219
                    return False #line:220
            return True #line:221
        except Exception as OOO00O0OOOOO0OO00 :#line:222
            print (OOO00O0OOOOO0OO00 )#line:223
    def sealing (O00OO00O000OO0O0O ):#line:226
        try :#line:227
            O0O000000O00O00OO =f'__{timi_new()}'#line:228
            O00OOOOO0O0O00O00 ={'source':'scsc','authorization':O00OO00O000OO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000000O00O00OO ),'signstring':O0O000000O00O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:239
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OOOOO0O0O00O00 )#line:240
            requests .request ('get',f'{host}/packsack/list',headers =O00OOOOO0O0O00O00 )#line:241
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OOOOO0O0O00O00 )#line:242
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OOOOO0O0O00O00 )#line:243
            requests .request ('get',f'{host}/user',headers =O00OOOOO0O0O00O00 )#line:244
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OOOOO0O0O00O00 )#line:245
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OOOOO0O0O00O00 )#line:246
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OOOOO0O0O00O00 )#line:247
            requests .request ('get',f'{host}/game/getAllData',headers =O00OOOOO0O0O00O00 )#line:248
            requests .request ('get',f'{host}/assets',headers =O00OOOOO0O0O00O00 )#line:249
        except Exception as OO0O0000OOOO00O00 :#line:250
            print (OO0O0000OOOO00O00 )#line:251
    def the_query (OO00O0O0OO0O00O00 ):#line:254
        try :#line:255
            OOOOO00000OO0OO0O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:256
            O0OOOOO0OOO00OOOO ={'authorization':OO00O0O0OO0O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00000OO0OO0O ),'signstring':OOOOO00000OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:266
            OOOO00OO0O0000000 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OOOOO0OOO00OOOO ).json ()#line:268
            if 'status'in OOOO00OO0O0000000 :#line:270
                if OOOO00OO0O0000000 ['status']==200 :#line:271
                    OOOO00OOOO00O00O0 =OOOO00OO0O0000000 ['data']['rows'][3 ]['price']#line:272
                    OO00O0O0OO0O00O00 .market_sale (OOOO00OOOO00O00O0 )#line:273
        except Exception as OOOO0OO00O0OOO00O :#line:274
            print (OOOO0OO00O0OOO00O )#line:275
    def market_sale (OO0OO0O00000OOOOO ,OO0OOOO000000O000 ):#line:278
        try :#line:279
            OO00O00O0O0O0OO0O =timi_new ()#line:280
            OO000OO00O0O000O0 =f'type=crop__{OO00O00O0O0O0OO0O}'#line:281
            O0O0O00OO0OOOOO0O ={'source':'scsc','authorization':OO0OO0O00000OOOOO .token ,'timestamp':str (OO00O00O0O0O0OO0O ),'sign':sign (OO000OO00O0O000O0 ),'signstring':OO000OO00O0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
            O0O0O00OO0000O0O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O00OO0OOOOO0O ).json ()#line:294
            if 'status'in O0O0O00OO0000O0O0 :#line:296
                if O0O0O00OO0000O0O0 ['status']==200 :#line:297
                    if O0O0O00OO0000O0O0 ['data']['rows']:#line:298
                        OOOOO0O0O00O0OO00 =O0O0O00OO0000O0O0 ['data']['rows'][0 ]['packsackItemId']#line:299
                        O0O0O00O0OOOO0O0O =O0O0O00OO0000O0O0 ['data']['rows'][0 ]['quantity']#line:300
                        OO00O0OOOO0O00OOO =float (OO0OOOO000000O000 )+float (random .randint (1 ,99 )*0.001 )#line:301
                        OOOO0000OOOO00OO0 =f'_packsackItemId={OOOOO0O0O00O0OO00}&price={str(OO00O0OOOO0O00OOO)[:7]}&quantity={O0O0O00O0OOOO0O0O}_{OO00O00O0O0O0OO0O}'#line:302
                        O0O000O00OOOO00O0 ={'source':'scsc','authorization':OO0OO0O00000OOOOO .token ,'timestamp':str (OO00O00O0O0O0OO0O ),'sign':sign (OOOO0000OOOO00OO0 ),'signstring':OOOO0000OOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:313
                        O00OOOO0OO0O0OOO0 ={"packsackItemId":OOOOO0O0O00O0OO00 ,"price":str (OO00O0OOOO0O00OOO )[:7 ],"quantity":str (O0O0O00O0OOOO0O0O )}#line:318
                        O00O000OO000O0OO0 =requests .request ('post',f'{host}/market/sale',headers =O0O000O00OOOO00O0 ,data =O00OOOO0OO0O0OOO0 ).json ()#line:319
                        if 'status'in O00O000OO000O0OO0 :#line:321
                            if O00O000OO000O0OO0 ['status']==200 :#line:322
                                print (f'【上架芦荟】:数量:{O0O0O00O0OOOO0O0O}丨价格:{str(OO00O0OOOO0O00OOO)[:7]}')#line:323
        except Exception as O00OO00OOOO0O0OO0 :#line:324
            print (O00OO00OOOO0O0OO0 )#line:325
    def query_to_sell (O0OOOOOO0OOO0OO00 ):#line:328
        try :#line:329
            O0O0000OO00OOOO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:330
            O0OO0O0O00OOO0OOO ={'source':'scsc','authorization':O0OOOOOO0OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO00OOOO00 ),'signstring':O0O0000OO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:341
            OOOOO0OOO0000O000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO0O0O00OOO0OOO ).json ()#line:343
            if 'status'in OOOOO0OOO0000O000 :#line:345
                if OOOOO0OOO0000O000 ['status']==200 :#line:346
                    for O0000O0OOOOO00OO0 in OOOOO0OOO0000O000 ['data']['rows']:#line:347
                        O000OO0O0O0000O0O =O0000O0OOOOO00OO0 ['materialKey']#line:348
                        O000O00OOOOOO00O0 =O0000O0OOOOO00OO0 ['quantity']#line:349
                        O00000O0000OO00O0 =O0000O0OOOOO00OO0 ['price']#line:350
                        OOO0OO0OO00000OO0 =O0000O0OOOOO00OO0 ['saleState']#line:351
                        if OOO0OO0OO00000OO0 ==0 :#line:352
                            print (f'【出售订单】:名称:{O000OO0O0O0000O0O}丨数量:{O000O00OOOOOO00O0}丨价格:{O00000O0000OO00O0}')#line:353
                            OO00000O0000O00O0 =O0000O0OOOOO00OO0 ['id']#line:354
                            if float (datetime .datetime .now ().hour )>8 :#line:355
                                O0OOOOOO0OOO0OO00 .cacel_sale (OO00000O0000O00O0 )#line:356
        except Exception as OOOO0OO0O0O00OOO0 :#line:357
            print (OOOO0OO0O0O00OOO0 )#line:358
    def cacel_sale (O000O0O00O00O00OO ,O000OOOOOO0OOO0O0 ):#line:361
        try :#line:362
            OOOO000O0O00O00O0 =f'_saleId={O000OOOOOO0OOO0O0}_{timi_new()}'#line:363
            O0000O0O0O00O00OO ={'source':'scsc','authorization':O000O0O00O00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0O00O00O0 ),'signstring':OOOO000O0O00O00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:374
            O0OO0OO0OOO0O0OOO ={"saleId":O000OOOOOO0OOO0O0 }#line:377
            O000OO0O0O000000O =requests .request ('post',f'{host}/market/cacel-sale',headers =O0000O0O0O00O00OO ,data =O0OO0OO0OOO0O0OOO ).json ()#line:378
            if 'status'in O000OO0O0O000000O :#line:380
                if O000OO0O0O000000O ['status']==200 :#line:381
                    print (f'【下架出售】:{O000OO0O0O000000O["data"]}')#line:382
        except Exception as OOOOOOOO00OOO0OOO :#line:383
            print (OOOOOOOO00OOO0OOO )#line:384
    def change_nickname (OO00O00O00OOO00O0 ):#line:387
        try :#line:388
            O0OO0OOO00O0OO0O0 =timi_new ()#line:389
            O0OO0000OO00OOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:390
            OOO00OO0O00O00O0O =requests .request ('post','https://www.qmsjmfb.com/',data =O0OO0000OO00OOO00 ).text #line:391
            O0O00OO0O000000OO =re .findall ('<ul><li>(.*?)</li>',OOO00OO0O00O00O0O )[0 ][:3 ]#line:392
            O0OO000O0O00O0OO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O00OO0O000000OO}').json ()#line:393
            O00OOOO00000O0OO0 =O0OO000O0O00O0OO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:394
            OO0OO00OOOOOO00O0 ={"nickname":O00OOOO00000O0OO0 }#line:395
            OOO00O000OOOOO0OO =f'_nickname={O00OOOO00000O0OO0}_{O0OO0OOO00O0OO0O0}'#line:396
            O000OOO0O0OOOO0OO ={'source':'scsc','authorization':OO00O00O00OOO00O0 .token ,'timestamp':O0OO0OOO00O0OO0O0 ,'sign':sign (OOO00O000OOOOO0OO ),'signstring':OOO00O000OOOOO0OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:407
            O000OO0OOO000000O =requests .request ('patch',f'{host}/user/nickname',headers =O000OOO0O0OOOO0OO ,data =OO0OO00OOOOOO00O0 ).json ()#line:408
            if 'status'in O000OO0OOO000000O :#line:410
                if O000OO0OOO000000O ['status']==200 :#line:411
                    print (f'【修改网名】:网名:{O00OOOO00000O0OO0}丨{O000OO0OOO000000O["message"]}')#line:412
        except Exception as O0000OOO0000OOOOO :#line:413
            print (O0000OOO0000OOOOO )#line:414
    def withdraw (O00O0O00OO000O0O0 ):#line:417
        try :#line:418
            OO000O0O000OOO000 =f'__{timi_new()}'#line:419
            O0O0OO00O0OOO0OO0 ={'source':'scsc','authorization':O00O0O00OO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O000OOO000 ),'signstring':OO000O0O000OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:430
            O0OOOOO0OO0000O00 =requests .request ('get',f'{host}/assets',headers =O0O0OO00O0OOO0OO0 ).json ()#line:431
            if 'status'in O0OOOOO0OO0000O00 :#line:433
                if O0OOOOO0OO0000O00 ['status']==200 :#line:434
                    O0O0O0O0OOO0O0O00 =O0OOOOO0OO0000O00 ['data']['cash']#line:435
                    if float (O0O0O0O0OOO0O0O00 )>20 :#line:436
                        OO000O0O000OOO000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:437
                        O0O0OO00O0OOO0OO0 ={'authorization':O00O0O00OO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O000OOO000 ),'signstring':OO000O0O000OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
                        O0O00OO0OO0O000OO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:448
                        O0O0O0O0000OOO00O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO00O0OOO0OO0 ,data =O0O00OO0OO0O000OO ).json ()#line:450
                        if 'status'in O0O0O0O0000OOO00O :#line:452
                            if O0O0O0O0000OOO00O ['status']==200 :#line:453
                                print (f'【余额提现】:{O0O0O0O0000OOO00O["data"]}')#line:454
                        if 'status'in O0O0O0O0000OOO00O :#line:455
                            if O0O0O0O0000OOO00O ['status']==500 :#line:456
                                print (f'【余额提现】:{O0O0O0O0000OOO00O["message"]}')#line:457
        except Exception as OO0000OOO0O0OOOOO :#line:458
            print (OO0000OOO0O0OOOOO )#line:459
    def invitenum (OOO0000OO0000O0OO ):#line:462
        global invited_new #line:463
        try :#line:464
            OO0O00OOOOO0O0O0O =f'__{timi_new()}'#line:465
            O0OOOOO000OO0OO0O ={'source':'scsc','authorization':OOO0000OO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOOOO0O0O0O ),'signstring':OO0O00OOOOO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:476
            OO00O0000O00O000O =requests .request ('get',f'{host}/invite/invitenum',headers =O0OOOOO000OO0OO0O ).json ()#line:477
            if 'status'in OO00O0000O00O000O :#line:479
                if OO00O0000O00O000O ['status']==200 :#line:480
                    OO0OOOOO0O0000000 =OO00O0000O00O000O ['data']['invited_count']#line:481
                    OOOOO0OO00OOO00O0 =OO00O0000O00O000O ['data']['invited_second_count']#line:482
                    print (f'【我的邀请】:直邀好友:{OO0OOOOO0O0000000}丨间邀好友:{OOOOO0OO00OOO00O0}')#line:483
                    if OO0OOOOO0O0000000 <2 :#line:484
                        OOOOO0OO0000OO000 =f'__{timi_new()}'#line:485
                        OO0O00000000OO00O ={'source':'scsc','authorization':OOO0000OO0000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OO0000OO000 ),'signstring':OOOOO0OO0000OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:496
                        OO0O0OO0O0O00O0OO =requests .request ('get',f'{host}/user',headers =OO0O00000000OO00O ).json ()#line:497
                        if 'status'in OO0O0OO0O0O00O0OO :#line:499
                            if OO0O0OO0O0O00O0OO ['status']==200 :#line:500
                                invited_new .append (OO0O0OO0O0O00O0OO ['data']['inner_id'])#line:501
        except Exception as OOO0O000O0OOO00OO :#line:502
            print (OOO0O000O0OOO00OO )#line:503
    def game_map (OOOOOO0O000O0O00O ):#line:506
        try :#line:507
            OOOOO00000000000O =f'__{timi_new()}'#line:508
            O0O0O0O000OO00OOO ={'source':'scsc','authorization':OOOOOO0O000O0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO00000000000O ),'signstring':OOOOO00000000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:519
            O0000000O000OOO00 =requests .request ('get',f'{host}/game/map',headers =O0O0O0O000OO00OOO ).json ()#line:520
            if 'status'in O0000000O000OOO00 :#line:522
                if O0000000O000OOO00 ['status']==200 :#line:523
                    for O00O0000OO0OOO00O in O0000000O000OOO00 ['data']['list'][0 ]['crops']:#line:524
                        OO0000OOOOOOO0000 =O00O0000OO0OOO00O ['level']#line:526
                        if OO0000OOOOOOO0000 ==41 :#line:527
                            OOOOOOO00O0O0O000 =O00O0000OO0OOO00O ['crop_name']#line:528
                            OOOOOO0OO0O0O0000 =O00O0000OO0OOO00O ['count']#line:529
                            if OOOOOO0OO0O0O0000 >0 :#line:530
                                print (f'【农业资产】:{OOOOOOO00O0O0O000}丨数量:{OOOOOO0OO0O0O0000}')#line:531
                                if float (datetime .datetime .now ().hour )>8 :#line:532
                                    OOOOOO0O000O0O00O .the_query ()#line:533
        except Exception as O00OO0O0O0OOO0O00 :#line:534
            print (O00OO0O0O0OOO0O00 )#line:535
    def give_gold (OOOO0OOOO000O00OO ):#line:538
        try :#line:539
            OOO0O0O00OO00OO00 =f'__{timi_new()}'#line:540
            O0O0O0O0OO00O00O0 ={'source':'scsc','authorization':OOOO0OOOO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00OO00OO00 ),'signstring':OOO0O0O00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:551
            OOO0OO0OO0000O00O =requests .request ('get',f'{host}/user',headers =O0O0O0O0OO00O00O0 ).json ()#line:552
            if 'status'in OOO0OO0OO0000O00O :#line:553
                if OOO0OO0OO0000O00O ['status']==200 :#line:554
                    if float (OOOO0OOOO000O00OO .doneeNo )!=0 :#line:555
                        O00OOO0OO0O00O00O =OOO0OO0OO0000O00O ['data']['assets']['gold']#line:556
                        if float (O00OOO0OO0O00O00O )>float (OOOO0OOOO000O00OO .innerId ):#line:557
                            OOO0OOOO0OOO0OO00 =int (float (O00OOO0OO0O00O00O )/1.1 )#line:558
                            OOO0O0O00OO00OO00 =f'_doneeNo={OOOO0OOOO000O00OO.doneeNo}&quantity={OOO0OOOO0OOO0OO00}_{timi_new()}'#line:559
                            O0O0O0O0OO00O00O0 ={'source':'scsc','authorization':OOOO0OOOO000O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00OO00OO00 ),'signstring':OOO0O0O00OO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:570
                            OO0O0OOO000OO0OO0 ={"quantity":OOO0OOOO0OOO0OO00 ,"doneeNo":OOOO0OOOO000O00OO .doneeNo }#line:574
                            O0OOOOO00OO0O00O0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O0O0OO00O00O0 ,data =OO0O0OOO000OO0OO0 ).json ()#line:575
                            if 'status'in O0OOOOO00OO0O00O0 :#line:577
                                if O0OOOOO00OO0O00O0 ['status']==200 :#line:578
                                    if O0OOOOO00OO0O00O0 ['data']:#line:579
                                        print (f'【赠送种子】:赠送{OOO0OOOO0OOO0OO00}种子给{OOOO0OOOO000O00OO.doneeNo}成功')#line:580
                    else :#line:581
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:582
        except Exception as O0OO0O000O00O0OOO :#line:583
            print (O0OO0O000O00O0OOO )#line:584
    def invitation (O0OO000OOO0OO0000 ):#line:586
        try :#line:587
            _O00O0O0OO0O00O00O =float (bundled_def ())/4 #line:588
            OO0O0OO00O0000000 =f'_innerId={int(_O00O0O0OO0O00O00O)}_{timi_new()}'#line:589
            O000OO0000OOO000O ={'source':'scsc','authorization':O0OO000OOO0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO00O0000000 ),'signstring':OO0O0OO00O0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:600
            O0O00OOOO0OO0OOO0 ={"innerId":int (_O00O0O0OO0O00O00O )}#line:601
            requests .request ('post',f'{host}/friends/my-invitation',headers =O000OO0000OOO000O ,data =O0O00OOOO0OO0OOO0 )#line:602
        except Exception as O0O0OOOOO00000OO0 :#line:603
            print (O0O0OOOOO00000OO0 )#line:604
    def winning_rewards (O0O00OO0OO0OO00OO ):#line:607
        try :#line:608
            O0OOO0O00OOO0OO00 =f'__{timi_new()}'#line:609
            O0O000OOOO0OO0000 ={'source':'scsc','authorization':O0O00OO0OO0OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O00OOO0OO00 ),'signstring':O0OOO0O00OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:620
            OOO00O00O0OOOO000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0O000OOOO0OO0000 ).json ()#line:621
            if 'status'in OOO00O00O0OOOO000 :#line:623
                if OOO00O00O0OOOO000 ['status']==200 :#line:624
                    if OOO00O00O0OOOO000 ['data']['amount']:#line:625
                        OO0O0O0O0O00OO00O =OOO00O00O0OOOO000 ['data']['amount']['gold']#line:626
                        return OO0O0O0O0O00OO00O #line:627
                    else :#line:628
                        return 0 #line:629
        except Exception as O000OOOO0O00O0O0O :#line:630
            print (O000OOOO0O00O0O0O )#line:631
    def certification (O00O0O0O00O0OOO00 ):#line:634
        try :#line:635
            O00O00000O0OO0O00 =f'__{timi_new()}'#line:636
            OOO00OOOOOO0OO0OO ={'source':'scsc','authorization':O00O0O0O00O0OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000O0OO0O00 ),'signstring':O00O00000O0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:647
            OO0O00O0000OOOO00 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO00OOOOOO0OO0OO ).json ()#line:648
            if 'status'in OO0O00O0000OOOO00 :#line:650
                if OO0O00O0000OOOO00 ['status']==200 :#line:651
                    if OO0O00O0000OOOO00 ['data']['result']:#line:652
                        O0O0O0000OOO000O0 =OO0O00O0000OOOO00 ['data']['nick_name']#line:653
                        return O0O0O0000OOO000O0 #line:654
                    else :#line:655
                        return '未实名'#line:656
        except Exception as O000OO00OOOOOOOOO :#line:657
            print (O000OO00OOOOOOOOO )#line:658
    def crops_illustrated (OO000OO000OOOO0O0 ):#line:661
        try :#line:662
            O0OO000OO0OOO0OO0 =f'__{timi_new()}'#line:663
            O0OO0OO0O0O00OO0O ={'source':'scsc','authorization':OO000OO000OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OO0OOO0OO0 ),'signstring':O0OO000OO0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:674
            OO0000O000O0OOO00 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OO0OO0O0O00OO0O ).json ()#line:675
            if 'status'in OO0000O000O0OOO00 :#line:677
                if OO0000O000O0OOO00 ['status']==200 :#line:678
                    O00OOOO0OO00O000O =OO0000O000O0OOO00 ['data'][0 ]['crops']#line:679
                    for O0O00O00000O00OOO in O00OOOO0OO00O000O :#line:680
                        if O0O00O00000O00OOO ['ill_clover_award']:#line:681
                            if float (O0O00O00000O00OOO ['ill_clover_award'])>1 :#line:682
                                if O0O00O00000O00OOO ['is_finish']:#line:683
                                    if not O0O00O00000O00OOO ['is_getit']:#line:684
                                        if OO000OO000OOOO0O0 .certification ()!='未实名':#line:685
                                            O0OO000OO0OOO0OO0 =f'_award_level={O0O00O00000O00OOO["level"]}_{timi_new()}'#line:686
                                            O0OO0OO0O0O00OO0O ={'source':'scsc','authorization':OO000OO000OOOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OO0OOO0OO0 ),'signstring':O0OO000OO0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:697
                                            O0O0OOOOOOOOOOOO0 ={"award_level":O0O00O00000O00OOO ['level']}#line:698
                                            O0OO00OOOOOOOO0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OO0OO0O0O00OO0O ,json =O0O0OOOOOOOOOOOO0 ).json ()#line:700
                                            if 'status'in O0OO00OOOOOOOO0OO :#line:701
                                                if O0OO00OOOOOOOO0OO ['status']==200 :#line:702
                                                    O0OO0O0O00O000OOO =O0OO00OOOOOOOO0OO ['data']['ill_clover_award']#line:703
                                                    print (f'【图鉴奖励】:领取{O0O00O00000O00OOO["crop_name"]}成就丨奖励{O0OO0O0O00O000OOO}☘️')#line:705
                                                if O0OO00OOOOOOOO0OO ['status']==500 :#line:706
                                                    print (f'【图鉴奖励】:{O0OO00OOOOOOOO0OO["message"]}')#line:707
        except Exception as O0OOO00OO00OOOO00 :#line:708
            print (O0OOO00OO00OOOO00 )#line:709
    def watched_ad (O00O0OOOO0O00OO0O ):#line:712
        try :#line:713
            O0OO00O0O0OOOOOOO =f'__{timi_new()}'#line:714
            O00O0O0O00OO00000 ={'source':'scsc','authorization':O00O0OOOO0O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O0O0OOOOOOO ),'signstring':O0OO00O0O0OOOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:725
            O00O00OOO0000OO0O =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O00OO00000 ).json ()#line:726
            if 'status'in O00O00OOO0000OO0O :#line:728
                if O00O00OOO0000OO0O ['status']==200 :#line:729
                    if 'offlineInfo'in O00O00OOO0000OO0O ['data']:#line:730
                        time .sleep (random .randint (1 ,3 ))#line:731
                        O0000O0O00OOOO00O =O00O00OOO0000OO0O ['data']['offlineInfo']['off_minute']#line:732
                        OO0O00O0O0O0O000O =float (O00O00OOO0000OO0O ['data']['silver'])/1000000000000 #line:733
                        time .sleep (1 )#line:734
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O0O0O00OO00000 ).json ()#line:735
                        time .sleep (2 )#line:736
                        OO0O00O000OO0O00O =requests .request ('get',f'{host}/game/getAllData',headers =O00O0O0O00OO00000 ).json ()#line:737
                        if 'status'in OO0O00O000OO0O00O :#line:739
                            if OO0O00O000OO0O00O ['status']==200 :#line:740
                                OOOOO0O000O00OOO0 =float (OO0O00O000OO0O00O ['data']['silver'])/1000000000000 #line:741
                                OO0OOO0O0O0000O0O =str (OOOOO0O000O00OOO0 -OO0O00O0O0O0O000O )[:6 ]#line:742
                                print (f'【离线奖励】:翻倍离线{O0000O0O00OOOO00O}分钟奖励🌱数量:{OO0OOO0O0O0000O0O}t粒')#line:743
        except Exception as OOO000000O0O00OO0 :#line:744
            print (OOO000000O0O00OO0 )#line:745
    def user_ad (OO00OOOOOOO0O0OO0 ):#line:748
        try :#line:749
            O0O0O00O0OOO0OO00 =f'__{timi_new()}'#line:750
            O000000O00O0O0OOO ={'source':'scsc','authorization':OO00OOOOOOO0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00O0OOO0OO00 ),'signstring':O0O0O00O0OOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            O0000000O00OOO0O0 =requests .request ('get',f'{host}/user/ad',headers =O000000O00O0O0OOO ).json ()#line:762
            if 'status'in O0000000O00OOO0O0 :#line:764
                if O0000000O00OOO0O0 ['status']==200 :#line:765
                    OO0000OO0OO0OOOOO =O0000000O00OOO0O0 ['data']['max_time']#line:766
                    O00OOOOOO0OOOOO0O =O0000000O00OOO0O0 ['data']['watch_time']#line:767
                    OOOOO0O00000O0O0O =O0000000O00OOO0O0 ['data']['added_time']#line:768
                    print (f'【获取种子】:获取🌱剩余{OOOOO0O00000O0O0O + OO0000OO0OO0OOOOO - O00OOOOOO0OOOOO0O}次丨好友提供:{OOOOO0O00000O0O0O}次')#line:769
                    if OOOOO0O00000O0O0O +OO0000OO0OO0OOOOO -O00OOOOOO0OOOOO0O >0 :#line:770
                        time .sleep (random .randint (16 ,19 ))#line:771
                        OO0000O000O000O00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O000000O00O0O0OOO ).json ()#line:772
                        if 'status'in OO0000O000O000O00 :#line:774
                            if OO0000O000O000O00 ['status']==200 :#line:775
                                OOO00O0O0OO0OOO00 =float (OO0000O000O000O00 ['data']['silver'])/1000000000000 #line:776
                                print (f'【获取种子】:获得🌱:{int(OOO00O0O0OO0OOO00)}t粒')#line:777
                                return True #line:778
                            if OO0000O000O000O00 ['status']==500 :#line:779
                                O00O00000OO0000O0 =OO0000O000O000O00 ['message']#line:780
                                print (f'【获取种子】:{O00O00000OO0000O0}')#line:781
                                return False #line:782
        except Exception as O0O0OOOOOOOO0O0OO :#line:783
            print (O0O0OOOOOOOO0O0OO )#line:784
    def synthetic (O0000OO0OO0OOOO0O ):#line:787
        global id ,g #line:788
        try :#line:789
            O0000O0O0OOO0OO00 =O0000OO0OO0OOOO0O .level_new ()#line:790
            OO0OO00000000OO00 =random .randint (9 ,11 )#line:791
            O0O0OOOOO000OOOO0 =f'_site=8&targetSite={OO0OO00000000OO00}_{timi_new()}'#line:792
            OOO0O000O00OO0000 ={'source':'scsc','authorization':O0000OO0OO0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0O0OOOOO000OOOO0 ),'signstring':O0O0OOOOO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:803
            O00O000OO00O0OO0O ={"site":int (8 ),"targetSite":int (OO0OO00000000OO00 )}#line:804
            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000O00OO0000 ,json =O00O000OO00O0OO0O )#line:805
            while True :#line:806
                OOO0O0O0000OO0OO0 =f'__{timi_new()}'#line:807
                OOO0000O00O00OOO0 ={'source':'scsc','authorization':O0000OO0OO0OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0000OO0OO0 ),'signstring':OOO0O0O0000OO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:818
                OO0O00000O0O00OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOO0000O00O00OOO0 ).json ()#line:819
                if 'status'in OO0O00000O0O00OOO :#line:821
                    if OO0O00000O0O00OOO ['status']==200 :#line:822
                        O00000OOOOO0O0OOO =OO0O00000O0O00OOO ['data']['cropList']#line:823
                        OOO00000OO0OO0000 =OO0O00000O0O00OOO ['data']['gameCoreDataDBid']#line:824
                        OO0OOO00O0OO0OO00 =float (OO0O00000O0O00OOO ['data']['silver'])/1000000000000 #line:825
                        OOO0O0O0OO0OO0OO0 =0 #line:830
                        for OO000OO0OOOOO0000 in O00000OOOOO0O0OOO :#line:831
                            if not OO000OO0OOOOO0000 :#line:832
                                O000O0000O000OOOO =f'_crop_id={OOO00000OO0OO0000}&site={OOO0O0O0OO0OO0OO0}_{O0000OO0OO0OOOO0O.time}'#line:833
                                OO0000OOO0OOO0OOO ={'source':'scsc','authorization':O0000OO0OO0OOOO0O .token ,'timestamp':O0000OO0OO0OOOO0O .time ,'sign':sign (O000O0000O000OOOO ),'signstring':O000O0000O000OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:843
                                OO0O0OOOO00O00O0O ={"site":OOO0O0O0OO0OO0OO0 ,"crop_id":OOO00000OO0OO0000 }#line:844
                                O000O0OO000O000O0 =requests .request ('post',f'{host}/game/crops/buy',headers =OO0000OOO0OOO0OOO ,data =OO0O0OOOO00O00O0O ).json ()#line:845
                                time .sleep (random .randint (1 ,3 )/10 )#line:847
                                if 'status'in O000O0OO000O000O0 :#line:848
                                    if O000O0OO000O000O0 ['status']==200 :#line:849
                                        if O000O0OO000O000O0 ['message']=='种子数量不足':#line:850
                                            O0000O0O0OOO0OO00 =O0000OO0OO0OOOO0O .level_new ()#line:851
                                            print (f'【种植合成】:{O000O0OO000O000O0["message"]}')#line:852
                                            if not O0000OO0OO0OOOO0O .user_ad ():#line:853
                                                return False #line:854
                                    if O000O0OO000O000O0 ['status']==500 :#line:855
                                        print (f'【种植合成】:{O000O0OO000O000O0["message"]}')#line:856
                                        return False #line:857
                            OOO0O0O0OO0OO0OO0 +=1 #line:858
                        OOOOO0O0O0O0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOO0000O00O00OOO0 ).json ()#line:859
                        O0000OOO0O0000OO0 =OOOOO0O0O0O0O00O0 ['data']['cropList']#line:860
                        OOO0OOO0000OOOOOO =False #line:861
                        for OO000OO0OOOOO0000 in range (12 ):#line:862
                            id =O0000OOO0O0000OO0 [OO000OO0OOOOO0000 ]['level']#line:863
                            if float (O0000O0O0OOO0OO00 )-float (id )>9 :#line:864
                                OO00OOOOOOOO0O000 =f'_site={OO000OO0OOOOO0000}_{timi_new()}'#line:865
                                OO0O00OO0O000O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000OO0OO0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (OO00OOOOOOOO0O000 ),'signstring':OO00OOOOOOOO0O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:876
                                OO0OO0OOO0O0000O0 ={"site":OO000OO0OOOOO0000 }#line:877
                                O0O00OO0OO00O0O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O00OO0O000O0OO ,data =OO0OO0OOO0O0000O0 ).json ()#line:879
                                if 'status'in O0O00OO0OO00O0O00 :#line:880
                                    if O0O00OO0OO00O0O00 ['status']==200 :#line:881
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:882
                            if id !=0 :#line:883
                                for O000000000OO0O0OO in range (11 ):#line:884
                                    O0OO0O0OOOO0OOO00 =O000000000OO0O0OO +1 #line:885
                                    g =O0000OOO0O0000OO0 [O0OO0O0OOOO0OOO00 ]['level']#line:886
                                    if id ==g :#line:887
                                        OOOOOOO0000OO00O0 =O000000000OO0O0OO +2 #line:888
                                        if OOOOOOO0000OO00O0 !=OO000OO0OOOOO0000 +1 :#line:889
                                            O0OOOOOO0O0OOOOO0 =OO000OO0OOOOO0000 +1 #line:890
                                            time .sleep (random .randint (1 ,3 )/10 )#line:892
                                            O0O0OOOOO000OOOO0 =f'_site={O0OOOOOO0O0OOOOO0 - 1}&targetSite={OOOOOOO0000OO00O0 - 1}_{timi_new()}'#line:893
                                            OOO0O000O00OO0000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0000OO0OO0OOOO0O .token ,'timestamp':timi_new (),'sign':sign (O0O0OOOOO000OOOO0 ),'signstring':O0O0OOOOO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:910
                                            OOO000OO000O0000O ={"site":int (O0OOOOOO0O0OOOOO0 -1 ),"targetSite":int (OOOOOOO0000OO00O0 -1 )}#line:911
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOO0O000O00OO0000 ,json =OOO000OO000O0000O )#line:912
                                            OOO0OOO0000OOOOOO =True #line:914
                                    if OOO0OOO0000OOOOOO :#line:915
                                        break #line:916
                                if OOO0OOO0000OOOOOO :#line:917
                                    break #line:918
        except :#line:919
            O0000OO0OO0OOOO0O .synthetic ()#line:920
    def level_new (OOO0O0OO00OOOO0OO ):#line:923
        try :#line:924
            OO0OO0OO0000O0OOO =f'__{timi_new()}'#line:925
            OO000OOOO0O0OO0O0 ={'source':'scsc','authorization':OOO0O0OO00OOOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OO0000O0OOO ),'signstring':OO0OO0OO0000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:936
            OOOOO0OOO0O000000 =requests .request ('get',f'{host}/user',headers =OO000OOOO0O0OO0O0 ).json ()#line:937
            if 'status'in OOOOO0OOO0O000000 :#line:938
                if OOOOO0OOO0O000000 ['status']==200 :#line:939
                    return float (OOOOO0OOO0O000000 ['data']['level'])#line:940
        except Exception as OO000O000O000O0OO :#line:941
            print (OO000O000O000O0OO )#line:942
    def propsraffle (OOOOO0OOO00OOOO0O ):#line:945
        try :#line:946
            while True :#line:947
                OO0OO0000OO0O00OO =f'__{timi_new()}'#line:948
                OO000O0OO000OO000 ={'source':'scsc','authorization':OOOOO0OOO00OOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000OO0O00OO ),'signstring':OO0OO0000OO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:959
                O00000000OOO000O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO000O0OO000OO000 ).json ()#line:960
                if 'status'in O00000000OOO000O0 :#line:962
                    if O00000000OOO000O0 ['status']==200 :#line:963
                        O0O0000O0O0OOO00O =O00000000OOO000O0 ['data']['rows']#line:964
                        O000O0OOO00O0OO00 =O00000000OOO000O0 ['data']['vstate']#line:965
                        if O0O0000O0O0OOO00O ==5 or O0O0000O0O0OOO00O ==6 or O0O0000O0O0OOO00O ==7 :#line:966
                            O00OOO0O0O0000O0O =O00000000OOO000O0 ['data']['silver']#line:967
                            print (f'【转盘抽奖】:获得种子:{O00OOO0O0O0000O0O}')#line:968
                        if O0O0000O0O0OOO00O ==1 or O0O0000O0O0OOO00O ==2 or O0O0000O0O0OOO00O ==3 :#line:969
                            O0OOOOOOOOO00O0OO =O00000000OOO000O0 ['data']['clover']#line:970
                            print (f'【转盘抽奖】:获得三叶草:{O0OOOOOOOOO00O0OO}')#line:971
                        if O0O0000O0O0OOO00O ==4 or O0O0000O0O0OOO00O ==8 :#line:972
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:973
                        if O0O0000O0O0OOO00O =='抽奖次数已用完':#line:977
                            break #line:1011
                time .sleep (random .randint (8 ,15 )/10 )#line:1012
        except Exception as OOO0OOO0000O0O00O :#line:1013
            print (OOO0OOO0000O0O00O )#line:1014
    def friends_invitation (OOOOO0OOO0O0O0OOO ):#line:1017
        try :#line:1018
            OOOOOOOOOO0OO0O00 =f'__{timi_new()}'#line:1019
            O0OOOO00O0O0OOOOO ={'source':'scsc','authorization':OOOOO0OOO0O0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOOOOO0OO0O00 ),'signstring':OOOOOOOOOO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1030
            O0OOOOOO0OO000000 =requests .request ('get',f'{host}/friends',headers =O0OOOO00O0O0OOOOO ).json ()#line:1031
            if 'status'in O0OOOOOO0OO000000 :#line:1032
                if O0OOOOOO0OO000000 ['status']==200 :#line:1033
                    OO0OO0O0O0OOOO00O =O0OOOOOO0OO000000 ['data']['myInviteter']#line:1034
                    if OO0OO0O0O0OOOO00O :#line:1035
                        OOO0000O0OOO0000O =OO0OO0O0O0OOOO00O ['user']['nickname']#line:1036
                        O0OO0OOOO0O00OOOO =OOOOO0OOO0O0O0OOO .certification ()#line:1037
                        if O0OO0OOOO0O00OOOO =='未实名':#line:1038
                            weishim .append (OOOOO0OOO0O0O0OOO .token )#line:1039
                        print (f'【查邀请人】:我的邀请人:{OOO0000O0OOO0000O}丨实名:{O0OO0OOOO0O00OOOO}')#line:1040
                    else :#line:1041
                        if OOOOO0OOO0O0O0OOO .innerId !='0':#line:1042
                            OOOOO0OOO0O0O0OOO .invitation ()#line:1043
        except Exception as O0O0O00O0OO0O0O00 :#line:1044
            print (O0O0O00O0OO0O0O00 )#line:1045
    def add_clover (OOOO00O000O0O0000 ):#line:1048
        global golden_seed #line:1049
        try :#line:1050
            OOOO0O0OO00O0OO0O =f'__{timi_new()}'#line:1051
            O0000000OOO0000O0 ={'source':'scsc','authorization':OOOO00O000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OO00O0OO0O ),'signstring':OOOO0O0OO00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1062
            O00000O00OOO00O00 =requests .request ('get',f'{host}/assets/clovers',headers =O0000000OOO0000O0 ).json ()#line:1063
            if 'status'in O00000O00OOO00O00 :#line:1065
                if O00000O00OOO00O00 ['status']==200 :#line:1066
                    O00OO0O0O0OO0O0O0 =O00000O00OOO00O00 ['data']['clover']#line:1067
                    OO0OOO000OO0O000O =O00000O00OOO00O00 ['data']['used_clover']#line:1068
                    O000OO0O0OOO0OO0O =float (O00OO0O0O0OO0O0O0 )-float (OO0OOO000OO0O000O )#line:1069
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OOO000OO0O000O}')#line:1070
                    if OOOO00O000O0O0000 .certification ()!='未实名':#line:1071
                        if O000OO0O0OOO0OO0O >1 :#line:1072
                            OOOO0O0OO00O0OO0O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O000OO0O0OOO0OO0O)}_{timi_new()}'#line:1073
                            OO0O00OO0O0O0OO00 ={'source':'scsc','authorization':OOOO00O000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OO00O0OO0O ),'signstring':OOOO0O0OO00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1084
                            O0OOO00OOO0O0OO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000OO0O0OOO0OO0O )}#line:1085
                            O0OO00000O0O0OOO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0O00OO0O0O0OO00 ,data =O0OOO00OOO0O0OO00 ).json ()#line:1086
                            if 'status'in O0OO00000O0O0OOO0 :#line:1088
                                if O0OO00000O0O0OOO0 ['status']==200 :#line:1089
                                    print (f'【参与抽奖】:添加☘️:{O0OO00000O0O0OOO0["data"]}丨数量:{O000OO0O0OOO0OO0O}')#line:1090
                                if O0OO00000O0O0OOO0 ['status']==500 :#line:1091
                                    print (f'【参与抽奖】:添加☘️:{O0OO00000O0O0OOO0["message"]}')#line:1092
            OO0O00OO0OOOOOO00 =requests .request ('get',f'{host}/lottery',headers =O0000000OOO0000O0 ).json ()#line:1093
            OO00OO0OO0OOO0OOO =OOOO00O000O0O0000 .winning_rewards ()#line:1095
            if 'status'in OO0O00OO0OOOOOO00 :#line:1096
                if OO0O00OO0OOOOOO00 ['status']==200 :#line:1097
                    OOO0OOOO00O0O0O00 =OO0O00OO0OOOOOO00 ['data'][0 ]['day_get_gold_quantity']#line:1098
                    golden_seed +=float (OOO0OOOO00O0O0O00 )#line:1099
                    OOOOO00OOOOO00000 =OO0O00OO0OOOOOO00 ['data'][1 ]['value']#line:1100
                    OOO00O0O0OO0O0000 =OO0O00OO0OOOOOO00 ['data'][0 ]['join_number']#line:1101
                    OOOOOO0O0OOO0OO00 =int (float (OO0O00OO0OOOOOO00 ['data'][0 ]['totalValue']))#line:1102
                    O0O0O0000O00OO00O =float (OOOOO00OOOOO00000 /OOOOOO0O0OOO0OO00 )*10000 #line:1103
                    O0OOO0O00OO000O0O =OOOOOO0O0OOO0OO00 /OOO00O0O0OO0O0000 #line:1104
                    print (f'【参与抽奖】:预计每天中{str(OOO0OOOO00O0O0O00)[:6]}颗金种子丨好友收益:{str(OO00OO0OO0OOO0OOO)[:6]}')#line:1105
                    print (f'【抽奖统计】:每1万☘️中{str(O0O0O0000O00OO00O)[:6]}颗金种子丨☘️人均:{str(O0OOO0O00OO000O0O)[:7]}️')#line:1106
        except Exception as O0OO00OOOO00O00OO :#line:1107
            print (O0OO00OOOO00O00OO )#line:1108
    def energy (O00OO00O0O0000O00 ):#line:1111
        try :#line:1112
            while True :#line:1113
                O0000O0000000O0OO =f'__{timi_new()}'#line:1114
                O0OOO0O00O0000O00 ={'source':'scsc','authorization':O00OO00O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0000000O0OO ),'signstring':O0000O0000000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1125
                O0O0OO0OO00OO000O =requests .request ('get',f'{host}/energy/general',headers =O0OOO0O00O0000O00 ).json ()#line:1126
                if 'status'in O0O0OO0OO00OO000O :#line:1128
                    if O0O0OO0OO00OO000O ['status']==200 :#line:1129
                        O00OO0O0OO0OO0OOO =O0O0OO0OO00OO000O ['data']['ordinary_water']#line:1130
                        O000O0O00O00OO00O =O0O0OO0OO00OO000O ['data']['ordinary_fertilizer']#line:1131
                        OOO0O0OO00O00O0O0 =O0O0OO0OO00OO000O ['data']['videoStatus']#line:1132
                        O0O000OO0O00OOO00 =O0O0OO0OO00OO000O ['data']['waterVideoKey']#line:1133
                        print (f'【我的营养】:肥料:{str(O000O0O00O00OO00O).split(".")[0]}丨水滴:{str(O00OO0O0OO0OO0OOO).split(".")[0]}')#line:1135
                        if float (O000O0O00O00OO00O )<96 :#line:1136
                            if OOO0O0OO00O00O0O0 :#line:1137
                                time .sleep (random .randint (160 ,180 )/10 )#line:1138
                                O00O00O00000OO000 =99 -float (O000O0O00O00OO00O )#line:1139
                                O0O00O00OOOOO00O0 ={"fertilizer":str (O00O00O00000OO000 ).split ('.')[0 ]}#line:1140
                                OO00000O00000OOO0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OOO0O00O0000O00 ).json ()#line:1142
                                if 'status'in OO00000O00000OOO0 :#line:1144
                                    if OO00000O00000OOO0 ['status']==200 :#line:1145
                                        print (f'【购买肥料】:看广告获取肥料:{OO00000O00000OOO0["message"]}')#line:1146
                                    if OO00000O00000OOO0 ['status']==500 :#line:1147
                                        print (f'【购买肥料】:看广告获取肥料:{OO00000O00000OOO0["message"]}')#line:1148
                                        break #line:1149
                                if float (O000O0O00O00OO00O )<78 :#line:1151
                                    O00O00O00000OO000 =80 -float (O000O0O00O00OO00O )#line:1152
                                    OOO00OOOO000OOOO0 =f'_fertilizer={int(O00O00O00000OO000)}_{timi_new()}'#line:1153
                                    OO00OO0OOO000OOO0 ={'source':'scsc','authorization':O00OO00O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OOOO000OOOO0 ),'signstring':OOO00OOOO000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1164
                                    OOOO000O00OO0OO0O ={"fertilizer":int (O00O00O00000OO000 )}#line:1165
                                    O00OO0O0000O0OO00 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO00OO0OOO000OOO0 ,data =OOOO000O00OO0OO0O ).json ()#line:1167
                                    if 'status'in O00OO0O0000O0OO00 :#line:1169
                                        if O00OO0O0000O0OO00 ['status']==200 :#line:1170
                                            print (f'【购买肥料】:购买肥料:{O00OO0O0000O0OO00["message"]}丨数量:{int(O00O00O00000OO000)}')#line:1171
                                        if O00OO0O0000O0OO00 ['status']==500 :#line:1172
                                            print (f'【购买肥料】:购买肥料:{O00OO0O0000O0OO00["message"]}丨数量:{int(O00O00O00000OO000)}')#line:1173
                                            O0O000O00O00O00OO =O00OO0O0000O0OO00 ["message"].split ('-')[1 ]#line:1174
                                            O0O00OOOO0O0O0OO0 =f'__{timi_new()}'#line:1175
                                            OO00OO0O0OOOO00OO ={'source':'scsc','authorization':O00OO00O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO0O0O0OO0 ),'signstring':O0O00OOOO0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1186
                                            OO00O00OOOO00O0OO =requests .request ('get',f'{host}/user',headers =OO00OO0O0OOOO00OO ).json ()#line:1187
                                            if 'status'in OO00O00OOOO00O0OO :#line:1188
                                                if OO00O00OOOO00O0OO ['status']==200 :#line:1189
                                                    OO0000O0OO0OOOO00 =OO00O00OOOO00O0OO ['data']['inner_id']#line:1190
                                                    if give_gold (OO0000O0OO0OOOO00 ,float (O0O000O00O00O00OO )+1 ):#line:1191
                                                        O00OO00O0O0000O00 .energy ()#line:1192
                        if float (O00OO0O0OO0OO0OOO )<880 :#line:1193
                            if O0O000OO0O00OOO00 :#line:1194
                                time .sleep (random .randint (160 ,180 )/10 )#line:1195
                                O0OO000O0OO0O0OOO =999 -float (O00OO0O0OO0OO0OOO )#line:1196
                                OO0O000O0OOO0OOOO ={"water":str (O0OO000O0OO0O0OOO ).split ('.')[0 ]}#line:1197
                                O0O0OO0OO000OO00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OOO0O00O0000O00 ).json ()#line:1199
                                if 'status'in O0O0OO0OO000OO00O :#line:1201
                                    if O0O0OO0OO000OO00O ['status']==200 :#line:1202
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OO0OO000OO00O["message"]}')#line:1203
                                    if O0O0OO0OO000OO00O ['status']==500 :#line:1204
                                        print (f'【购买水滴】:看广告获取水滴:{O0O0OO0OO000OO00O["message"]}')#line:1205
                                        break #line:1206
                                if float (O00OO0O0OO0OO0OOO )<780 :#line:1207
                                    O0OO000O0OO0O0OOO =800 -float (O00OO0O0OO0OO0OOO )#line:1208
                                    OOOO0000000O0O00O =f'_water={int(O0OO000O0OO0O0OOO)}_{timi_new()}'#line:1209
                                    OO00000OOO0OOO000 ={'source':'scsc','authorization':O00OO00O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0000000O0O00O ),'signstring':OOOO0000000O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1220
                                    O0OO00O00OOO0OOO0 ={"water":int (O0OO000O0OO0O0OOO )}#line:1221
                                    O0O00OOOOOOOOOO0O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO00000OOO0OOO000 ,data =O0OO00O00OOO0OOO0 ).json ()#line:1223
                                    if 'status'in O0O00OOOOOOOOOO0O :#line:1225
                                        if O0O00OOOOOOOOOO0O ['status']==200 :#line:1226
                                            print (f'【购买水滴】:购买水滴:{O0O00OOOOOOOOOO0O["message"]}丨数量:{int(O0OO000O0OO0O0OOO)}')#line:1227
                                        if O0O00OOOOOOOOOO0O ['status']==500 :#line:1228
                                            print (f'【购买水滴】:购买水滴:{O0O00OOOOOOOOOO0O["message"]}丨数量:{int(O0OO000O0OO0O0OOO)}')#line:1229
                                            O0O000O00O00O00OO =O0O00OOOOOOOOOO0O ["message"].split ('-')[1 ]#line:1230
                                            O0O00OOOO0O0O0OO0 =f'__{timi_new()}'#line:1231
                                            OO00OO0O0OOOO00OO ={'source':'scsc','authorization':O00OO00O0O0000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOOO0O0O0OO0 ),'signstring':O0O00OOOO0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1242
                                            OO00O00OOOO00O0OO =requests .request ('get',f'{host}/user',headers =OO00OO0O0OOOO00OO ).json ()#line:1243
                                            if 'status'in OO00O00OOOO00O0OO :#line:1244
                                                if OO00O00OOOO00O0OO ['status']==200 :#line:1245
                                                    OO0000O0OO0OOOO00 =OO00O00OOOO00O0OO ['data']['inner_id']#line:1246
                                                    if give_gold (OO0000O0OO0OOOO00 ,float (O0O000O00O00O00OO )+1 ):#line:1247
                                                        O00OO00O0O0000O00 .energy ()#line:1248
                        break #line:1249
        except Exception as O0OO0OOO00000000O :#line:1250
            print (O0OO0OOO00000000O )#line:1251
def bundled_def ():#line:1254
    O0OOO00OO0O0000OO =['5570536','7750212','7911652','7911680','7805624']#line:1255
    return O0OOO00OO0O0000OO [random .randint (0 ,len (O0OOO00OO0O0000OO )-1 )]#line:1256
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
        O0O00O0O0OOO00000 =gitee_edition ()#line:1292
        if version_of_the_validation ()<O0O00O0O0OOO00000 ['CityEarth']['edition']:#line:1293
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00O0O0OOO00000["CityEarth"]["edition"]}   ❌')#line:1294
            print (f'更新内容=>>{O0O00O0O0OOO00000["CityEarth"]["content"]}')#line:1295
        else :#line:1296
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O00O0O0OOO00000["CityEarth"]["edition"]}   ✅')#line:1297
            print (f'更新内容=>> {O0O00O0O0OOO00000["CityEarth"]["content"]}')#line:1298
    except Exception as O000OOOO000OOOOOO :#line:1299
        print (O000OOOO000OOOOOO )#line:1300
def sc3 ():#line:1303
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1304
if __name__ =='__main__':#line:1307
    start ()#line:1308
