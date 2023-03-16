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
@ 版本  4.1
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
        OO00O0000O0OO000O =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(OO00O0000O0OO000O)}个账号==========")#line:16
        for O0O0OO00000OOO000 in OO00O0000O0OO000O :#line:17
            O00O000OOOO0OOO0O =[]#line:18
            print (f"------------正在执行第{OO00O0000O0OO000O.index(O0O0OO00000OOO000) + 1}个账号------------")#line:19
            O00OO0O0OO00OO000 =CityEarth (O0O0OO00000OOO000 ,O00O000OOOO0OOO0O ,OO00O0000O0OO000O .index (O0O0OO00000OOO000 ))#line:20
            def OO0O0O000O0OO00O0 ():#line:22
                if O00OO0O0OO00OO000 .base_info ():#line:24
                    O00OO0O0OO00OO000 .sealing ()#line:26
                    O00OO0O0OO00OO000 .invitenum ()#line:28
                    O00OO0O0OO00OO000 .query_to_sell ()#line:30
                    O00OO0O0OO00OO000 .game_map ()#line:32
                    O00OO0O0OO00OO000 .friends_invitation ()#line:34
                    O00OO0O0OO00OO000 .energy ()#line:36
                    O00OO0O0OO00OO000 .add_clover ()#line:38
                    O00OO0O0OO00OO000 .propsraffle ()#line:40
                    O00OO0O0OO00OO000 .synthetic ()#line:42
                    O00OO0O0OO00OO000 .crops_illustrated ()#line:44
                    O00OO0O0OO00OO000 .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        O00OO0O0OO00OO000 .give_gold ()#line:49
            O000O00000O0O0OOO =threading .Thread (target =OO0O0O000O0OO00O0 )#line:51
            O000O00000O0O0OOO .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理数据------------")#line:54
        time .sleep (0.5 )#line:55
        O00O0OO00O00O0OOO =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O00O0OO00O00O0OOO +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for OOOO0OO00OO0OOO00 in invited_new :#line:60
            print (OOOO0OO00OO0OOO00 )#line:61
        print ('开始打印未实名的token')#line:62
        for OOO0O0OOO0O0O00O0 in weishim :#line:63
            print (OOO0O0OOO0O0O00O0 )#line:64
    except Exception as OOOO0OOO0OOO0O0OO :#line:65
        print (OOOO0OOO0OOO0O0OO )#line:66
def give_gold (O00O0O0O00O0OO0O0 ,OOO0O00OOO0O0O00O ):#line:70
    try :#line:71
        O0O0000OOO00OOO00 =f'_doneeNo={O00O0O0O00O0OO0O0}&quantity={int(OOO0O00OOO0O0O00O)}_{timi_new()}'#line:72
        OOOOO000000OOO000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0O0000OOO00OOO00 ),'signstring':O0O0000OOO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        O000O0O00000O0OO0 ={"quantity":int (OOO0O00OOO0O0O00O ),"doneeNo":O00O0O0O00O0OO0O0 }#line:87
        O00O000OO00OOO000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO000000OOO000 ,data =O000O0O00000O0OO0 ).json ()#line:88
        if 'status'in O00O000OO00OOO000 :#line:90
            if O00O000OO00OOO000 ['status']==200 :#line:91
                if O00O000OO00OOO000 ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OOO0O00OOO0O0O00O)}种子给{O00O0O0O00O0OO0O0}成功')#line:93
                    return True #line:94
            if O00O000OO00OOO000 ['status']==401 :#line:95
                print (f'【赠送种子】:{O00O000OO00OOO000["message"]}')#line:96
                return False #line:97
            if O00O000OO00OOO000 ['status']==500 :#line:98
                print (f'【赠送种子】:{O00O000OO00OOO000["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as O00OO000O0000OO00 :#line:102
        print (O00OO000O0000OO00 )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def oyoy ():#line:109
    return '卡密未激活   ❌'#line:110
def sign (OOOOO00OO000O00O0 ):#line:113
    OOOOO00OOOOO00O0O =hashlib .md5 (OOOOO00OO000O00O0 .encode ()).hexdigest ()#line:114
    O0O000OOOOO000OO0 =sc1 ()#line:115
    O0OOO000OO0O00000 =sc2 ()#line:116
    O00OO00OOO0O0OO0O =sc3 ()#line:117
    O0O0OOO000OOOO000 =O0O000OOOOO000OO0 +OOOOO00OOOOO00O0O +O0OOO000OO0O00000 +O00OO00OOO0O0OO0O #line:118
    OO000OO000O000O00 =hashlib .md5 (O0O0OOO000OOOO000 .encode ()).hexdigest ()#line:119
    return OO000OO000O000O00 #line:120
def format_msg ():#line:123
    O0OO0O0OOO000OO00 =""#line:124
    for O00OO000OOOO00OO0 in msg_list :#line:125
        O0OO0O0OOO000OO00 +=str (O00OO000OOOO00OO0 )+"\r\n"#line:126
    return O0OO0O0OOO000OO00 #line:127
def sc1 ():#line:130
    return "scsc%^&*"#line:131
def O000OO0O00OO00O00 ():#line:134
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:135
        ubbbf ()#line:136
    else :#line:137
        oyoy ()#line:138
        exit (1 )#line:139
def timi_new ():#line:142
    return str (int (time .time ()*1000 ))#line:143
json_path ="CityEarth_data.json"#line:146
json_path1 ="CityEarth_data.json"#line:147
dict ={}#line:148
def get_json_data (O00OO00OO00O0000O ,OOOO0O0O0O0O00OOO ,O000O000O000000OO ,OOO0O000OOO0OO0O0 ):#line:151
    with open (O00OO00OO00O0000O ,'rb')as O0OOOO00OO00O0OOO :#line:152
        O0OO0O0O000OO0O00 =json .load (O0OOOO00OO00O0OOO )#line:153
        O0OO0O0O000OO0O00 ['data'][OOOO0O0O0O0O00OOO ][O000O000O000000OO ]=OOO0O000OOO0OO0O0 #line:154
        O0O0000000OOOOO0O =O0OO0O0O000OO0O00 #line:155
    O0OOOO00OO00O0OOO .close ()#line:156
    return O0O0000000OOOOO0O #line:157
def write_json_data (O00000O0O00O00OOO ):#line:160
    with open (json_path1 ,'w')as O00O00O00O0O00O00 :#line:161
        json .dump (O00000O0O00O00OOO ,O00O00O00O0O00O00 )#line:162
    O00O00O00O0O00O00 .close ()#line:163
    return True #line:164
class CityEarth :#line:167
    def __init__ (O00O0OO0O000OOOOO ,OOOO0OO0000OO0O00 ,OOO00O000OOO0O0O0 ,O00O00O0000OOO0OO ):#line:169
        try :#line:170
            O00O0OO0O000OOOOO .msg =OOO00O000OOO0O0O0 #line:171
            O00O0OO0O000OOOOO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:172
            O00O0OO0O000OOOOO .token =OOOO0OO0000OO0O00 ['authorization']#line:173
            O00O0OO0O000OOOOO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:174
            O00O0OO0O000OOOOO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:175
            O00O0OO0O000OOOOO .elephant_user =OOOO0OO0000OO0O00 ['elephant_user']#line:176
            O00O0OO0O000OOOOO .elephant_pswd =OOOO0OO0000OO0O00 ['elephant_pswd']#line:177
            O00O0OO0O000OOOOO .elephant_Task_ID =OOOO0OO0000OO0O00 ['elephant_Task_ID']#line:178
            O00O0OO0O000OOOOO .len_new =O00O00O0000OOO0OO #line:179
        except :#line:180
            print ('变量格式错误')#line:181
    def base_info (OOOOO0O00O000O0O0 ):#line:184
        try :#line:185
            OOOOO0O00O000O0O0 .watched_ad ()#line:187
            OO0O00O00OO000OO0 =f'__{timi_new()}'#line:188
            OO00000OO00O00O00 ={'source':'scsc','authorization':OOOOO0O00O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00OO000OO0 ),'signstring':OO0O00O00OO000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
            O0O0O00OO0OO00OOO =requests .request ('get',f'{host}/user',headers =OO00000OO00O00O00 ).json ()#line:200
            if 'status'in O0O0O00OO0OO00OOO :#line:202
                if O0O0O00OO0OO00OOO ['status']==200 :#line:203
                    OOOOOOO0O0O0O00OO =O0O0O00OO0OO00OOO ['data']['nickname']#line:204
                    O0O00000O0OOOO0O0 =O0O0O00OO0OO00OOO ['data']['inner_id']#line:205
                    O0OO0OO0O0O0OO0O0 =O0O0O00OO0OO00OOO ['data']['assets']['gold']#line:206
                    O0O00O00O000O0OOO =O0O0O00OO0OO00OOO ['data']['level']#line:207
                    print (f'【账号信息】:昵称:{OOOOOOO0O0O0O00OO[:5]}丨ID:{O0O00000O0OOOO0O0}丨等级:{O0O00O00O000O0OOO}丨金种子:{str(O0OO0OO0O0O0OO0O0).split(".")[0]}')#line:209
                    if 'wx_'in OOOOOOO0O0O0O00OO :#line:210
                        OOOOO0O00O000O0O0 .change_nickname ()#line:211
                if O0O0O00OO0OO00OOO ['status']==401 :#line:212
                    print ('【账号信息】:账号失效正在尝试登录')#line:213
                    if OOOOO0O00O000O0O0 .elephant_user =='f':#line:214
                        return False #line:215
                    OOO000OO0O0O00OOO =Invalid_login .addtask (elephant_user =OOOOO0O00O000O0O0 .elephant_user ,elephant_pswd =OOOOO0O00O000O0O0 .elephant_pswd ,elephant_Task_ID =OOOOO0O00O000O0O0 .elephant_Task_ID )#line:218
                    OOO0OO00O00O0OO0O =get_json_data (json_path ,OOOOO0O00O000O0O0 .len_new ,'authorization',OOO000OO0O0O00OOO )#line:219
                    if write_json_data (OOO0OO00O00O0OO0O ):#line:220
                        print ('正在写入账号配置文件')#line:221
                    return False #line:222
                if O0O0O00OO0OO00OOO ['status']==500 :#line:223
                    return False #line:224
            return True #line:225
        except Exception as O0OO0OO0O0O0O0OOO :#line:226
            print (O0OO0OO0O0O0O0OOO )#line:227
    def sealing (O0O0000O0O0O0000O ):#line:230
        try :#line:231
            OO00O00OOO000O00O =f'__{timi_new()}'#line:232
            O0OO00000OO00OO0O ={'source':'scsc','authorization':O0O0000O0O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOO000O00O ),'signstring':OO00O00OOO000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:243
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO00000OO00OO0O )#line:244
            requests .request ('get',f'{host}/packsack/list',headers =O0OO00000OO00OO0O )#line:245
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO00000OO00OO0O )#line:246
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO00000OO00OO0O )#line:247
            requests .request ('get',f'{host}/user',headers =O0OO00000OO00OO0O )#line:248
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO00000OO00OO0O )#line:249
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO00000OO00OO0O )#line:250
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO00000OO00OO0O )#line:251
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO00000OO00OO0O )#line:252
            requests .request ('get',f'{host}/assets',headers =O0OO00000OO00OO0O )#line:253
        except Exception as OOO0OO0OO0O00OO0O :#line:254
            print (OOO0OO0OO0O00OO0O )#line:255
    def the_query (O0O00OO0000O0O000 ):#line:258
        try :#line:259
            O0O0O000O0O0000OO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:260
            O0O00OOO00OOO0O00 ={'authorization':O0O00OO0000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O0O0000OO ),'signstring':O0O0O000O0O0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:270
            OOOOOO0O00000OOOO =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0O00OOO00OOO0O00 ).json ()#line:272
            if 'status'in OOOOOO0O00000OOOO :#line:274
                if OOOOOO0O00000OOOO ['status']==200 :#line:275
                    OOO0OOOO00000O000 =OOOOOO0O00000OOOO ['data']['rows'][3 ]['price']#line:276
                    O0O00OO0000O0O000 .market_sale (OOO0OOOO00000O000 )#line:277
        except Exception as OOO0OOOO000O00OOO :#line:278
            print (OOO0OOOO000O00OOO )#line:279
    def market_sale (O0O0OO0OO00O00OO0 ,OO000O00O0OOOO0O0 ):#line:282
        try :#line:283
            O0000OO000O00O0OO =timi_new ()#line:284
            OOO0O0000OOO00OO0 =f'type=crop__{O0000OO000O00O0OO}'#line:285
            O00O000OOOOO00OOO ={'source':'scsc','authorization':O0O0OO0OO00O00OO0 .token ,'timestamp':str (O0000OO000O00O0OO ),'sign':sign (OOO0O0000OOO00OO0 ),'signstring':OOO0O0000OOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:296
            O000OOO00OO000000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O00O000OOOOO00OOO ).json ()#line:298
            if 'status'in O000OOO00OO000000 :#line:300
                if O000OOO00OO000000 ['status']==200 :#line:301
                    if O000OOO00OO000000 ['data']['rows']:#line:302
                        O0OO000000O000OO0 =O000OOO00OO000000 ['data']['rows'][0 ]['packsackItemId']#line:303
                        O0OOO00OOOOOO0000 =O000OOO00OO000000 ['data']['rows'][0 ]['quantity']#line:304
                        OO00000O000OO0O00 =float (OO000O00O0OOOO0O0 )+float (random .randint (1 ,9 )*0.001 )#line:305
                        if OO00000O000OO0O00 >8 :#line:306
                            O0OOOOOOOO000OO00 =f'_packsackItemId={O0OO000000O000OO0}&price={str(OO00000O000OO0O00)[:7]}&quantity={O0OOO00OOOOOO0000}_{O0000OO000O00O0OO}'#line:307
                            O0O00O000OO00OO0O ={'source':'scsc','authorization':O0O0OO0OO00O00OO0 .token ,'timestamp':str (O0000OO000O00O0OO ),'sign':sign (O0OOOOOOOO000OO00 ),'signstring':O0OOOOOOOO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:318
                            OO0O00OOO0O000O00 ={"packsackItemId":O0OO000000O000OO0 ,"price":str (OO00000O000OO0O00 )[:7 ],"quantity":str (O0OOO00OOOOOO0000 )}#line:323
                            OOOO00OOOOOO0O0OO =requests .request ('post',f'{host}/market/sale',headers =O0O00O000OO00OO0O ,data =OO0O00OOO0O000O00 ).json ()#line:324
                            if 'status'in OOOO00OOOOOO0O0OO :#line:326
                                if OOOO00OOOOOO0O0OO ['status']==200 :#line:327
                                    print (f'【上架芦荟】:数量:{O0OOO00OOOOOO0000}丨价格:{str(OO00000O000OO0O00)[:7]}')#line:328
        except Exception as O0OOOO00OOOOOO00O :#line:329
            print (O0OOOO00OOOOOO00O )#line:330
    def query_to_sell (OOOO00O000OOO0OO0 ):#line:333
        try :#line:334
            O00O00000OOO0O000 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:335
            O0000O0OOOO00O0OO ={'source':'scsc','authorization':OOOO00O000OOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000OOO0O000 ),'signstring':O00O00000OOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:346
            OO00O0000O0O000O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0000O0OOOO00O0OO ).json ()#line:348
            if 'status'in OO00O0000O0O000O0 :#line:350
                if OO00O0000O0O000O0 ['status']==200 :#line:351
                    for OO0O0OOO0OOOO00O0 in OO00O0000O0O000O0 ['data']['rows']:#line:352
                        OOOO00000O00O0O00 =OO0O0OOO0OOOO00O0 ['materialKey']#line:353
                        OOO0O00OO000O0OO0 =OO0O0OOO0OOOO00O0 ['quantity']#line:354
                        OOOO0O00O0OOOO000 =OO0O0OOO0OOOO00O0 ['price']#line:355
                        O0O0OO0OO0O0000OO =OO0O0OOO0OOOO00O0 ['saleState']#line:356
                        if O0O0OO0OO0O0000OO ==0 :#line:357
                            print (f'【出售订单】:名称:{OOOO00000O00O0O00}丨数量:{OOO0O00OO000O0OO0}丨价格:{OOOO0O00O0OOOO000}')#line:358
                            OOOO00OOOO0O0O0OO =OO0O0OOO0OOOO00O0 ['id']#line:359
                            if float (datetime .datetime .now ().hour )>8 :#line:360
                                OOOO00O000OOO0OO0 .cacel_sale (OOOO00OOOO0O0O0OO )#line:361
        except Exception as OOO0O0O0O00OO000O :#line:362
            print (OOO0O0O0O00OO000O )#line:363
    def cacel_sale (O00O000O0OOO0OO0O ,OOO0O0OO0000O0O0O ):#line:366
        try :#line:367
            O0O0OO00OOO000O0O =f'_saleId={OOO0O0OO0000O0O0O}_{timi_new()}'#line:368
            OO00O000000O0OO0O ={'source':'scsc','authorization':O00O000O0OOO0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00OOO000O0O ),'signstring':O0O0OO00OOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:379
            OOO0OOOO000000OO0 ={"saleId":OOO0O0OO0000O0O0O }#line:382
            OOOOOOO0OOO00OOO0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OO00O000000O0OO0O ,data =OOO0OOOO000000OO0 ).json ()#line:383
            if 'status'in OOOOOOO0OOO00OOO0 :#line:385
                if OOOOOOO0OOO00OOO0 ['status']==200 :#line:386
                    print (f'【下架出售】:{OOOOOOO0OOO00OOO0["data"]}')#line:387
        except Exception as O0OOOOOOOOO00OO0O :#line:388
            print (O0OOOOOOOOO00OO0O )#line:389
    def change_nickname (O0O0OOOOO00O0000O ):#line:392
        try :#line:393
            OOO0O000O00O00OOO =timi_new ()#line:394
            O000OO000O0000OOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:395
            OOOOO00O0O0O0OOOO =requests .request ('post','https://www.qmsjmfb.com/',data =O000OO000O0000OOO ).text #line:396
            OOO0O00OO0000O0OO =re .findall ('<ul><li>(.*?)</li>',OOOOO00O0O0O0OOOO )[0 ][:3 ]#line:397
            OOO0000OO0OOOOO00 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOO0O00OO0000O0OO}').json ()#line:398
            OOOOOOOOOOOO000O0 =OOO0000OO0OOOOO00 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:399
            OOOO00OO0O0O00000 ={"nickname":OOOOOOOOOOOO000O0 }#line:400
            O00000OO000OOO00O =f'_nickname={OOOOOOOOOOOO000O0}_{OOO0O000O00O00OOO}'#line:401
            OO0000O0O00O0OO0O ={'source':'scsc','authorization':O0O0OOOOO00O0000O .token ,'timestamp':OOO0O000O00O00OOO ,'sign':sign (O00000OO000OOO00O ),'signstring':O00000OO000OOO00O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:412
            O00000O0000OO0O00 =requests .request ('patch',f'{host}/user/nickname',headers =OO0000O0O00O0OO0O ,data =OOOO00OO0O0O00000 ).json ()#line:413
            if 'status'in O00000O0000OO0O00 :#line:415
                if O00000O0000OO0O00 ['status']==200 :#line:416
                    print (f'【修改网名】:网名:{OOOOOOOOOOOO000O0}丨{O00000O0000OO0O00["message"]}')#line:417
        except Exception as OOO0OO000OO0OOOOO :#line:418
            print (OOO0OO000OO0OOOOO )#line:419
    def withdraw (OO0O0OOO000OO0OOO ):#line:422
        try :#line:423
            OO0O00O0000O0OOO0 =f'__{timi_new()}'#line:424
            OOOO00000O0O00O0O ={'source':'scsc','authorization':OO0O0OOO000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0000O0OOO0 ),'signstring':OO0O00O0000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:435
            OOOOOOOOOO0OOOOO0 =requests .request ('get',f'{host}/assets',headers =OOOO00000O0O00O0O ).json ()#line:436
            if 'status'in OOOOOOOOOO0OOOOO0 :#line:438
                if OOOOOOOOOO0OOOOO0 ['status']==200 :#line:439
                    OOOOO00OO00OO0OO0 =OOOOOOOOOO0OOOOO0 ['data']['cash']#line:440
                    if float (OOOOO00OO00OO0OO0 )>20 :#line:441
                        OO0O00O0000O0OOO0 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:442
                        OOOO00000O0O00O0O ={'authorization':OO0O0OOO000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0000O0OOO0 ),'signstring':OO0O00O0000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:452
                        O00O00OO0O0O0O0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:453
                        OO0OOO0O0OOOOOO0O =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOOO00000O0O00O0O ,data =O00O00OO0O0O0O0O0 ).json ()#line:455
                        if 'status'in OO0OOO0O0OOOOOO0O :#line:457
                            if OO0OOO0O0OOOOOO0O ['status']==200 :#line:458
                                print (f'【余额提现】:{OO0OOO0O0OOOOOO0O["data"]}')#line:459
                        if 'status'in OO0OOO0O0OOOOOO0O :#line:460
                            if OO0OOO0O0OOOOOO0O ['status']==500 :#line:461
                                print (f'【余额提现】:{OO0OOO0O0OOOOOO0O["message"]}')#line:462
        except Exception as O00OOO0O000O0OO00 :#line:463
            print (O00OOO0O000O0OO00 )#line:464
    def invitenum (OOO00O0000O00OOO0 ):#line:467
        global invited_new #line:468
        try :#line:469
            O0000OOO00000OO00 =f'__{timi_new()}'#line:470
            OOOOOOOO0OO00O0O0 ={'source':'scsc','authorization':OOO00O0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO00000OO00 ),'signstring':O0000OOO00000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
            OO00O00000000O0OO =requests .request ('get',f'{host}/invite/invitenum',headers =OOOOOOOO0OO00O0O0 ).json ()#line:482
            if 'status'in OO00O00000000O0OO :#line:484
                if OO00O00000000O0OO ['status']==200 :#line:485
                    O00O00OO0OO0OO0O0 =OO00O00000000O0OO ['data']['invited_count']#line:486
                    OOOOOO00OO0OO00OO =OO00O00000000O0OO ['data']['invited_second_count']#line:487
                    print (f'【我的邀请】:直邀好友:{O00O00OO0OO0OO0O0}丨间邀好友:{OOOOOO00OO0OO00OO}')#line:488
                    if O00O00OO0OO0OO0O0 <2 :#line:489
                        OO0O0O000O0000O0O =f'__{timi_new()}'#line:490
                        O0O0O0OO0O0O00O0O ={'source':'scsc','authorization':OOO00O0000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000O0000O0O ),'signstring':OO0O0O000O0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:501
                        O0O0000OOOOOOO0O0 =requests .request ('get',f'{host}/user',headers =O0O0O0OO0O0O00O0O ).json ()#line:502
                        if 'status'in O0O0000OOOOOOO0O0 :#line:504
                            if O0O0000OOOOOOO0O0 ['status']==200 :#line:505
                                invited_new .append (O0O0000OOOOOOO0O0 ['data']['inner_id'])#line:506
        except Exception as OO00000OO0OO0O000 :#line:507
            print (OO00000OO0OO0O000 )#line:508
    def game_map (O00OO0OO0O0000OOO ):#line:511
        try :#line:512
            OO0000OOO0OO00O00 =f'__{timi_new()}'#line:513
            O00O000OO0OOO00O0 ={'source':'scsc','authorization':O00OO0OO0O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOO0OO00O00 ),'signstring':OO0000OOO0OO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:524
            OO0O00OOO0O0OOO00 =requests .request ('get',f'{host}/game/map',headers =O00O000OO0OOO00O0 ).json ()#line:525
            if 'status'in OO0O00OOO0O0OOO00 :#line:527
                if OO0O00OOO0O0OOO00 ['status']==200 :#line:528
                    for O0000O0OOO000O000 in OO0O00OOO0O0OOO00 ['data']['list'][0 ]['crops']:#line:529
                        O0OO00OOO0O0000O0 =O0000O0OOO000O000 ['level']#line:531
                        if O0OO00OOO0O0000O0 ==41 :#line:532
                            O00OO00000O000O0O =O0000O0OOO000O000 ['crop_name']#line:533
                            O00OOOO00OO0O0O00 =O0000O0OOO000O000 ['count']#line:534
                            if O00OOOO00OO0O0O00 >0 :#line:535
                                print (f'【农业资产】:{O00OO00000O000O0O}丨数量:{O00OOOO00OO0O0O00}')#line:536
                                if float (datetime .datetime .now ().hour )>8 :#line:537
                                    O00OO0OO0O0000OOO .the_query ()#line:538
        except Exception as O000O0O0O0O00O0OO :#line:539
            print (O000O0O0O0O00O0OO )#line:540
    def give_gold (O0O0OO0O0OOOO00O0 ):#line:543
        try :#line:544
            OO0O0O000000OOOO0 =f'__{timi_new()}'#line:545
            OO00O00O0O0O0OO0O ={'source':'scsc','authorization':O0O0OO0O0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000000OOOO0 ),'signstring':OO0O0O000000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:556
            O0O00O0OO00OO00O0 =requests .request ('get',f'{host}/user',headers =OO00O00O0O0O0OO0O ).json ()#line:557
            if 'status'in O0O00O0OO00OO00O0 :#line:558
                if O0O00O0OO00OO00O0 ['status']==200 :#line:559
                    if float (O0O0OO0O0OOOO00O0 .doneeNo )!=0 :#line:560
                        O00OOO0O0OOOO0O00 =O0O00O0OO00OO00O0 ['data']['assets']['gold']#line:561
                        if float (O00OOO0O0OOOO0O00 )>float (O0O0OO0O0OOOO00O0 .innerId ):#line:562
                            OOOOO0OO000O0OOOO =int (float (O00OOO0O0OOOO0O00 )/1.1 )#line:563
                            OO0O0O000000OOOO0 =f'_doneeNo={O0O0OO0O0OOOO00O0.doneeNo}&quantity={OOOOO0OO000O0OOOO}_{timi_new()}'#line:564
                            OO00O00O0O0O0OO0O ={'source':'scsc','authorization':O0O0OO0O0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O000000OOOO0 ),'signstring':OO0O0O000000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:575
                            OOO0O000000OO00OO ={"quantity":OOOOO0OO000O0OOOO ,"doneeNo":O0O0OO0O0OOOO00O0 .doneeNo }#line:579
                            OO00OOOO0OOOOO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OO00O00O0O0O0OO0O ,data =OOO0O000000OO00OO ).json ()#line:580
                            if 'status'in OO00OOOO0OOOOO0OO :#line:582
                                if OO00OOOO0OOOOO0OO ['status']==200 :#line:583
                                    if OO00OOOO0OOOOO0OO ['data']:#line:584
                                        print (f'【赠送种子】:赠送{OOOOO0OO000O0OOOO}种子给{O0O0OO0O0OOOO00O0.doneeNo}成功')#line:585
                    else :#line:586
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:587
        except Exception as O00O0O00OOOOO0OO0 :#line:588
            print (O00O0O00OOOOO0OO0 )#line:589
    def invitation (O00O0O0O0000OOOOO ):#line:591
        try :#line:592
            _OOOOO000O000O00O0 =float (bundled_def ())/4 #line:593
            O00000O0O0O0O0OO0 =f'_innerId={int(_OOOOO000O000O00O0)}_{timi_new()}'#line:594
            OOO0O00000O00000O ={'source':'scsc','authorization':O00O0O0O0000OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0O0O0OO0 ),'signstring':O00000O0O0O0O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:605
            O00OOOO0O0O00000O ={"innerId":int (_OOOOO000O000O00O0 )}#line:606
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOO0O00000O00000O ,data =O00OOOO0O0O00000O )#line:607
        except Exception as O0OO00O0OOOOOOOO0 :#line:608
            print (O0OO00O0OOOOOOOO0 )#line:609
    def winning_rewards (OOO00O0O0O0OO000O ):#line:612
        try :#line:613
            O00O00O0OO0000O0O =f'__{timi_new()}'#line:614
            O0000O00O00O00O00 ={'source':'scsc','authorization':OOO00O0O0O0OO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO0000O0O ),'signstring':O00O00O0OO0000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:625
            OOO0O0O000O00O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O00O00O00O00 ).json ()#line:626
            if 'status'in OOO0O0O000O00O000 :#line:628
                if OOO0O0O000O00O000 ['status']==200 :#line:629
                    if OOO0O0O000O00O000 ['data']['amount']:#line:630
                        OOO00O0O000O0O0O0 =OOO0O0O000O00O000 ['data']['amount']['gold']#line:631
                        return OOO00O0O000O0O0O0 #line:632
                    else :#line:633
                        return 0 #line:634
        except Exception as OOO0OOO0OOOOO00O0 :#line:635
            print (OOO0OOO0OOOOO00O0 )#line:636
    def certification (OOO0000OO0O000OO0 ):#line:639
        try :#line:640
            OOO0OOO0OOOO00000 =f'__{timi_new()}'#line:641
            O0OO0OO0O00OOO0OO ={'source':'scsc','authorization':OOO0000OO0O000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOOO00000 ),'signstring':OOO0OOO0OOOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:652
            O0O000OOO0O0OO000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0OO0OO0O00OOO0OO ).json ()#line:653
            if 'status'in O0O000OOO0O0OO000 :#line:655
                if O0O000OOO0O0OO000 ['status']==200 :#line:656
                    if O0O000OOO0O0OO000 ['data']['result']:#line:657
                        OOO0OOO000O0O0O00 =O0O000OOO0O0OO000 ['data']['nick_name']#line:658
                        return OOO0OOO000O0O0O00 #line:659
                    else :#line:660
                        return '未实名'#line:661
        except Exception as O0OOO0OOOOO0OOOO0 :#line:662
            print (O0OOO0OOOOO0OOOO0 )#line:663
    def crops_illustrated (OO000OO0OO0OOO0OO ):#line:666
        try :#line:667
            OO00O0O00OOO000OO =f'__{timi_new()}'#line:668
            OO0O0O0OOO000O000 ={'source':'scsc','authorization':OO000OO0OO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OOO000OO ),'signstring':OO00O0O00OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:679
            O0OOO0000OO0000O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0O0OOO000O000 ).json ()#line:680
            if 'status'in O0OOO0000OO0000O0 :#line:682
                if O0OOO0000OO0000O0 ['status']==200 :#line:683
                    O000O0O00OOO0OOOO =O0OOO0000OO0000O0 ['data'][0 ]['crops']#line:684
                    for O0O000000OOO00O0O in O000O0O00OOO0OOOO :#line:685
                        if O0O000000OOO00O0O ['ill_clover_award']:#line:686
                            if float (O0O000000OOO00O0O ['ill_clover_award'])>1 :#line:687
                                if O0O000000OOO00O0O ['is_finish']:#line:688
                                    if not O0O000000OOO00O0O ['is_getit']:#line:689
                                        if OO000OO0OO0OOO0OO .certification ()!='未实名':#line:690
                                            OO00O0O00OOO000OO =f'_award_level={O0O000000OOO00O0O["level"]}_{timi_new()}'#line:691
                                            OO0O0O0OOO000O000 ={'source':'scsc','authorization':OO000OO0OO0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O00OOO000OO ),'signstring':OO00O0O00OOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:702
                                            OO0OOO0OO0O00OOO0 ={"award_level":O0O000000OOO00O0O ['level']}#line:703
                                            OOO0OOOO0OO0OOOO0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0O0OOO000O000 ,json =OO0OOO0OO0O00OOO0 ).json ()#line:705
                                            if 'status'in OOO0OOOO0OO0OOOO0 :#line:706
                                                if OOO0OOOO0OO0OOOO0 ['status']==200 :#line:707
                                                    O00OO0OO0O0OOO0OO =OOO0OOOO0OO0OOOO0 ['data']['ill_clover_award']#line:708
                                                    print (f'【图鉴奖励】:领取{O0O000000OOO00O0O["crop_name"]}成就丨奖励{O00OO0OO0O0OOO0OO}☘️')#line:710
                                                if OOO0OOOO0OO0OOOO0 ['status']==500 :#line:711
                                                    print (f'【图鉴奖励】:{OOO0OOOO0OO0OOOO0["message"]}')#line:712
        except Exception as O00OOOO00O00OO00O :#line:713
            print (O00OOOO00O00OO00O )#line:714
    def watched_ad (OOO00000000OOO0OO ):#line:717
        try :#line:718
            OOOO00O0000000000 =f'__{timi_new()}'#line:719
            O0O0O00OO0000000O ={'source':'scsc','authorization':OOO00000000OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O0000000000 ),'signstring':OOOO00O0000000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:730
            OOO0000OO0OO00OOO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O00OO0000000O ).json ()#line:731
            if 'status'in OOO0000OO0OO00OOO :#line:733
                if OOO0000OO0OO00OOO ['status']==200 :#line:734
                    if 'offlineInfo'in OOO0000OO0OO00OOO ['data']:#line:735
                        time .sleep (random .randint (1 ,3 ))#line:736
                        OO0O00OOO0OO0O000 =OOO0000OO0OO00OOO ['data']['offlineInfo']['off_minute']#line:737
                        O0O0O00O0OO00O0OO =float (OOO0000OO0OO00OOO ['data']['silver'])/1000000000000 #line:738
                        time .sleep (1 )#line:739
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0O0O00OO0000000O ).json ()#line:740
                        time .sleep (2 )#line:741
                        OO0OO0O0OOO0O00OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0O00OO0000000O ).json ()#line:742
                        if 'status'in OO0OO0O0OOO0O00OO :#line:744
                            if OO0OO0O0OOO0O00OO ['status']==200 :#line:745
                                O0O00OOO0OO0OOO00 =float (OO0OO0O0OOO0O00OO ['data']['silver'])/1000000000000 #line:746
                                OOO00OOOOO00OOOO0 =str (O0O00OOO0OO0OOO00 -O0O0O00O0OO00O0OO )[:6 ]#line:747
                                print (f'【离线奖励】:翻倍离线{OO0O00OOO0OO0O000}分钟奖励🌱数量:{OOO00OOOOO00OOOO0}t粒')#line:748
        except Exception as O00OO00OOO0O000O0 :#line:749
            print (O00OO00OOO0O000O0 )#line:750
    def user_ad (OOO00O000O0O0OOO0 ):#line:753
        try :#line:754
            OO0O00O00O00O0OO0 =f'__{timi_new()}'#line:755
            O0000OOO0O0OO0O0O ={'source':'scsc','authorization':OOO00O000O0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O00O00O0OO0 ),'signstring':OO0O00O00O00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:766
            OO0OO0O00OOOO000O =requests .request ('get',f'{host}/user/ad',headers =O0000OOO0O0OO0O0O ).json ()#line:767
            if 'status'in OO0OO0O00OOOO000O :#line:769
                if OO0OO0O00OOOO000O ['status']==200 :#line:770
                    OO0O0O00O0OO00OOO =OO0OO0O00OOOO000O ['data']['max_time']#line:771
                    OO00OO0O0O000O0O0 =OO0OO0O00OOOO000O ['data']['watch_time']#line:772
                    OOOO000OOO0000OOO =OO0OO0O00OOOO000O ['data']['added_time']#line:773
                    print (f'【获取种子】:获取🌱剩余{OOOO000OOO0000OOO + OO0O0O00O0OO00OOO - OO00OO0O0O000O0O0}次丨好友提供:{OOOO000OOO0000OOO}次')#line:774
                    if OOOO000OOO0000OOO +OO0O0O00O0OO00OOO -OO00OO0O0O000O0O0 >0 :#line:775
                        time .sleep (random .randint (16 ,19 ))#line:776
                        O0OO0OO0O00OO0OOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0000OOO0O0OO0O0O ).json ()#line:777
                        if 'status'in O0OO0OO0O00OO0OOO :#line:779
                            if O0OO0OO0O00OO0OOO ['status']==200 :#line:780
                                OO00O0OO0OOO00O00 =float (O0OO0OO0O00OO0OOO ['data']['silver'])/1000000000000 #line:781
                                print (f'【获取种子】:获得🌱:{int(OO00O0OO0OOO00O00)}t粒')#line:782
                                return True #line:783
                            if O0OO0OO0O00OO0OOO ['status']==500 :#line:784
                                OOO0O000OO0000O00 =O0OO0OO0O00OO0OOO ['message']#line:785
                                print (f'【获取种子】:{OOO0O000OO0000O00}')#line:786
                                return False #line:787
        except Exception as OO0OOO0000O000OOO :#line:788
            print (OO0OOO0000O000OOO )#line:789
    def synthetic (OOO0O0OO000O00000 ):#line:792
        global id ,g #line:793
        try :#line:794
            OOO0OO00000O00OO0 =OOO0O0OO000O00000 .level_new ()#line:795
            O00O0OO00OO0OO000 =random .randint (9 ,11 )#line:796
            O0O0OOO0O0O00O0O0 =f'_site=8&targetSite={O00O0OO00OO0OO000}_{timi_new()}'#line:797
            OO00O0OO00000O0OO ={'source':'scsc','authorization':OOO0O0OO000O00000 .token ,'timestamp':timi_new (),'sign':sign (O0O0OOO0O0O00O0O0 ),'signstring':O0O0OOO0O0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:808
            OO000OOO0O0OOOOOO ={"site":int (8 ),"targetSite":int (O00O0OO00OO0OO000 )}#line:809
            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OO00000O0OO ,json =OO000OOO0O0OOOOOO )#line:810
            while True :#line:811
                O0OO00O00OOOOO0OO =f'__{timi_new()}'#line:812
                OO0O00000OO0OOOO0 ={'source':'scsc','authorization':OOO0O0OO000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00OOOOO0OO ),'signstring':O0OO00O00OOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:823
                O0O0O00O000OOOO0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00000OO0OOOO0 ).json ()#line:824
                if 'status'in O0O0O00O000OOOO0O :#line:826
                    if O0O0O00O000OOOO0O ['status']==200 :#line:827
                        OO00OOO0OO0O0OOO0 =O0O0O00O000OOOO0O ['data']['cropList']#line:828
                        O000O00OO00OOO0OO =O0O0O00O000OOOO0O ['data']['gameCoreDataDBid']#line:829
                        OOOOOOOO0OO0000OO =float (O0O0O00O000OOOO0O ['data']['silver'])/1000000000000 #line:830
                        O00O0O0O0O00O00O0 =0 #line:835
                        for OO0O00O00O00O00O0 in OO00OOO0OO0O0OOO0 :#line:836
                            if not OO0O00O00O00O00O0 :#line:837
                                O0OO000OOO0000000 =f'_crop_id={O000O00OO00OOO0OO}&site={O00O0O0O0O00O00O0}_{OOO0O0OO000O00000.time}'#line:838
                                OO000OOO00O0OOO00 ={'source':'scsc','authorization':OOO0O0OO000O00000 .token ,'timestamp':OOO0O0OO000O00000 .time ,'sign':sign (O0OO000OOO0000000 ),'signstring':O0OO000OOO0000000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:848
                                OOO00O00O0O000OO0 ={"site":O00O0O0O0O00O00O0 ,"crop_id":O000O00OO00OOO0OO }#line:849
                                O0O0O00O0O00O0OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OO000OOO00O0OOO00 ,data =OOO00O00O0O000OO0 ).json ()#line:850
                                time .sleep (random .randint (1 ,3 )/10 )#line:852
                                if 'status'in O0O0O00O0O00O0OOO :#line:853
                                    if O0O0O00O0O00O0OOO ['status']==200 :#line:854
                                        if O0O0O00O0O00O0OOO ['message']=='种子数量不足':#line:855
                                            OOO0OO00000O00OO0 =OOO0O0OO000O00000 .level_new ()#line:856
                                            print (f'【种植合成】:{O0O0O00O0O00O0OOO["message"]}')#line:857
                                            if not OOO0O0OO000O00000 .user_ad ():#line:858
                                                return False #line:859
                                    if O0O0O00O0O00O0OOO ['status']==500 :#line:860
                                        print (f'【种植合成】:{O0O0O00O0O00O0OOO["message"]}')#line:861
                                        return False #line:862
                            O00O0O0O0O00O00O0 +=1 #line:863
                        OO00OO000OO0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =OO0O00000OO0OOOO0 ).json ()#line:864
                        OO0O0OO00OO000000 =OO00OO000OO0O0000 ['data']['cropList']#line:865
                        OOOOO00O00O0O0OOO =False #line:866
                        for OO0O00O00O00O00O0 in range (12 ):#line:867
                            id =OO0O0OO00OO000000 [OO0O00O00O00O00O0 ]['level']#line:868
                            if float (OOO0OO00000O00OO0 )-float (id )>9 :#line:869
                                O0O0O0OO000O00O00 =f'_site={OO0O00O00O00O00O0}_{timi_new()}'#line:870
                                OOO000OO0000O00OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O0OO000O00000 .token ,'timestamp':timi_new (),'sign':sign (O0O0O0OO000O00O00 ),'signstring':O0O0O0OO000O00O00 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:881
                                OOOOO0O0OOOO0O0OO ={"site":OO0O00O00O00O00O0 }#line:882
                                OOO0O00O00OOO0OOO =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO000OO0000O00OO ,data =OOOOO0O0OOOO0O0OO ).json ()#line:884
                                if 'status'in OOO0O00O00OOO0OOO :#line:885
                                    if OOO0O00O00OOO0OOO ['status']==200 :#line:886
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:887
                            if id !=0 :#line:888
                                for OO0000OO0000000O0 in range (11 ):#line:889
                                    O00OO000O0O0OOOOO =OO0000OO0000000O0 +1 #line:890
                                    g =OO0O0OO00OO000000 [O00OO000O0O0OOOOO ]['level']#line:891
                                    if id ==g :#line:892
                                        O0000O000O0O000O0 =OO0000OO0000000O0 +2 #line:893
                                        if O0000O000O0O000O0 !=OO0O00O00O00O00O0 +1 :#line:894
                                            OOO0OO000OO0O00O0 =OO0O00O00O00O00O0 +1 #line:895
                                            time .sleep (random .randint (1 ,3 )/10 )#line:897
                                            O0O0OOO0O0O00O0O0 =f'_site={OOO0OO000OO0O00O0 - 1}&targetSite={O0000O000O0O000O0 - 1}_{timi_new()}'#line:898
                                            OO00O0OO00000O0OO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0O0OO000O00000 .token ,'timestamp':timi_new (),'sign':sign (O0O0OOO0O0O00O0O0 ),'signstring':O0O0OOO0O0O00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:915
                                            O00O0000000OOOOO0 ={"site":int (OOO0OO000OO0O00O0 -1 ),"targetSite":int (O0000O000O0O000O0 -1 )}#line:916
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO00O0OO00000O0OO ,json =O00O0000000OOOOO0 )#line:917
                                            OOOOO00O00O0O0OOO =True #line:919
                                    if OOOOO00O00O0O0OOO :#line:920
                                        break #line:921
                                if OOOOO00O00O0O0OOO :#line:922
                                    break #line:923
        except :#line:924
            OOO0O0OO000O00000 .synthetic ()#line:925
    def level_new (O0O000000OOO00000 ):#line:928
        try :#line:929
            O000OOO0000O0O000 =f'__{timi_new()}'#line:930
            O0OO0OO0O000OOO00 ={'source':'scsc','authorization':O0O000000OOO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0000O0O000 ),'signstring':O000OOO0000O0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:941
            O0OO0O0000O0OOO0O =requests .request ('get',f'{host}/user',headers =O0OO0OO0O000OOO00 ).json ()#line:942
            if 'status'in O0OO0O0000O0OOO0O :#line:943
                if O0OO0O0000O0OOO0O ['status']==200 :#line:944
                    return float (O0OO0O0000O0OOO0O ['data']['level'])#line:945
        except Exception as OO00OOO00OOOOO0OO :#line:946
            print (OO00OOO00OOOOO0OO )#line:947
    def propsraffle (OO0O0O0000OO00000 ):#line:950
        try :#line:951
            while True :#line:952
                O000OOO00OO000O00 =f'__{timi_new()}'#line:953
                O00OO0O00O0OO0OOO ={'source':'scsc','authorization':OO0O0O0000OO00000 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO00OO000O00 ),'signstring':O000OOO00OO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:964
                O0O00OO00000O00O0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O00OO0O00O0OO0OOO ).json ()#line:965
                if 'status'in O0O00OO00000O00O0 :#line:967
                    if O0O00OO00000O00O0 ['status']==200 :#line:968
                        OO00O00OOO0O0O00O =O0O00OO00000O00O0 ['data']['rows']#line:969
                        OOOO000OO0000OOO0 =O0O00OO00000O00O0 ['data']['vstate']#line:970
                        if OO00O00OOO0O0O00O ==5 or OO00O00OOO0O0O00O ==6 or OO00O00OOO0O0O00O ==7 :#line:971
                            OO00O0OOO00OOO000 =O0O00OO00000O00O0 ['data']['silver']#line:972
                            print (f'【转盘抽奖】:获得种子:{OO00O0OOO00OOO000}')#line:973
                        if OO00O00OOO0O0O00O ==1 or OO00O00OOO0O0O00O ==2 or OO00O00OOO0O0O00O ==3 :#line:974
                            O000O0OO0O0O0O000 =O0O00OO00000O00O0 ['data']['clover']#line:975
                            print (f'【转盘抽奖】:获得三叶草:{O000O0OO0O0O0O000}')#line:976
                        if OO00O00OOO0O0O00O ==4 or OO00O00OOO0O0O00O ==8 :#line:977
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:978
                        if OO00O00OOO0O0O00O =='抽奖次数已用完':#line:982
                            break #line:1016
                time .sleep (random .randint (8 ,15 )/10 )#line:1017
        except Exception as OO000O0OO0O0O0OO0 :#line:1018
            print (OO000O0OO0O0O0OO0 )#line:1019
    def friends_invitation (OO0O0OO00OOO0OOO0 ):#line:1022
        try :#line:1023
            OO00O0O0O000OOOO0 =f'__{timi_new()}'#line:1024
            OO0OOOOO000OO0O0O ={'source':'scsc','authorization':OO0O0OO00OOO0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0O0O000OOOO0 ),'signstring':OO00O0O0O000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1035
            O0OOO000OO000OO0O =requests .request ('get',f'{host}/friends',headers =OO0OOOOO000OO0O0O ).json ()#line:1036
            if 'status'in O0OOO000OO000OO0O :#line:1037
                if O0OOO000OO000OO0O ['status']==200 :#line:1038
                    OOOOOO0O0OO0000O0 =O0OOO000OO000OO0O ['data']['myInviteter']#line:1039
                    if OOOOOO0O0OO0000O0 :#line:1040
                        O00O000O00O0O0O00 =OOOOOO0O0OO0000O0 ['user']['nickname']#line:1041
                        OOO00O0O0O000OOO0 =OO0O0OO00OOO0OOO0 .certification ()#line:1042
                        if OOO00O0O0O000OOO0 =='未实名':#line:1043
                            weishim .append (OO0O0OO00OOO0OOO0 .token )#line:1044
                        print (f'【查邀请人】:我的邀请人:{O00O000O00O0O0O00}丨实名:{OOO00O0O0O000OOO0}')#line:1045
                    else :#line:1046
                        if OO0O0OO00OOO0OOO0 .innerId !='0':#line:1047
                            OO0O0OO00OOO0OOO0 .invitation ()#line:1048
        except Exception as O0OO0OOO00O0OO0O0 :#line:1049
            print (O0OO0OOO00O0OO0O0 )#line:1050
    def add_clover (OOOOO0O0O00000OO0 ):#line:1053
        global golden_seed #line:1054
        try :#line:1055
            O000000OOOOOO0OO0 =f'__{timi_new()}'#line:1056
            OOOO0OO0O0000OOO0 ={'source':'scsc','authorization':OOOOO0O0O00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OOOOOO0OO0 ),'signstring':O000000OOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
            OOOO000OO0O0000OO =requests .request ('get',f'{host}/assets/clovers',headers =OOOO0OO0O0000OOO0 ).json ()#line:1068
            if 'status'in OOOO000OO0O0000OO :#line:1070
                if OOOO000OO0O0000OO ['status']==200 :#line:1071
                    OO0O00OOO00OO0O0O =OOOO000OO0O0000OO ['data']['clover']#line:1072
                    OO0OO0OO00000000O =OOOO000OO0O0000OO ['data']['used_clover']#line:1073
                    O00000O00OO0O0O00 =float (OO0O00OOO00OO0O0O )-float (OO0OO0OO00000000O )#line:1074
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO0OO0OO00000000O}')#line:1075
                    if OOOOO0O0O00000OO0 .certification ()!='未实名':#line:1076
                        if O00000O00OO0O0O00 >1 :#line:1077
                            O000000OOOOOO0OO0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00000O00OO0O0O00)}_{timi_new()}'#line:1078
                            OOOO0OO00O000O000 ={'source':'scsc','authorization':OOOOO0O0O00000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000000OOOOOO0OO0 ),'signstring':O000000OOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1089
                            O00OOO000O0OO000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00000O00OO0O0O00 )}#line:1090
                            O00OO0O0O0O0O0OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOO0OO00O000O000 ,data =O00OOO000O0OO000O ).json ()#line:1091
                            if 'status'in O00OO0O0O0O0O0OO0 :#line:1093
                                if O00OO0O0O0O0O0OO0 ['status']==200 :#line:1094
                                    print (f'【参与抽奖】:添加☘️:{O00OO0O0O0O0O0OO0["data"]}丨数量:{O00000O00OO0O0O00}')#line:1095
                                if O00OO0O0O0O0O0OO0 ['status']==500 :#line:1096
                                    print (f'【参与抽奖】:添加☘️:{O00OO0O0O0O0O0OO0["message"]}')#line:1097
            OO0OOO0O0000O000O =requests .request ('get',f'{host}/lottery',headers =OOOO0OO0O0000OOO0 ).json ()#line:1098
            OOO0O000OOOOO0OOO =OOOOO0O0O00000OO0 .winning_rewards ()#line:1100
            if 'status'in OO0OOO0O0000O000O :#line:1101
                if OO0OOO0O0000O000O ['status']==200 :#line:1102
                    OO0O00000OO0O0OO0 =OO0OOO0O0000O000O ['data'][0 ]['day_get_gold_quantity']#line:1103
                    golden_seed +=float (OO0O00000OO0O0OO0 )#line:1104
                    O0O000O00OOOOO0O0 =OO0OOO0O0000O000O ['data'][1 ]['value']#line:1105
                    OO0O00OO000000000 =OO0OOO0O0000O000O ['data'][0 ]['join_number']#line:1106
                    O0O0OOOO000000OO0 =int (float (OO0OOO0O0000O000O ['data'][0 ]['totalValue']))#line:1107
                    OOO00O0O0000O0000 =float (O0O000O00OOOOO0O0 /O0O0OOOO000000OO0 )*10000 #line:1108
                    OOOOO00OO0O0OOO0O =O0O0OOOO000000OO0 /OO0O00OO000000000 #line:1109
                    print (f'【参与抽奖】:预计每天中{str(OO0O00000OO0O0OO0)[:6]}颗金种子丨好友收益:{str(OOO0O000OOOOO0OOO)[:6]}')#line:1110
                    print (f'【抽奖统计】:每1万☘️中{str(OOO00O0O0000O0000)[:6]}颗金种子丨☘️人均:{str(OOOOO00OO0O0OOO0O)[:7]}️')#line:1111
        except Exception as O000O0OOOOO00O0OO :#line:1112
            print (O000O0OOOOO00O0OO )#line:1113
    def energy (OOOOO000000O0000O ):#line:1116
        try :#line:1117
            while True :#line:1118
                OO000O000OO0OO00O =f'__{timi_new()}'#line:1119
                O0O000O000O00O000 ={'source':'scsc','authorization':OOOOO000000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O000OO0OO00O ),'signstring':OO000O000OO0OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1130
                OO0O0OO000000OO0O =requests .request ('get',f'{host}/energy/general',headers =O0O000O000O00O000 ).json ()#line:1131
                if 'status'in OO0O0OO000000OO0O :#line:1133
                    if OO0O0OO000000OO0O ['status']==200 :#line:1134
                        O0000OOO000OO0O0O =OO0O0OO000000OO0O ['data']['ordinary_water']#line:1135
                        OO000O000OOOOOO00 =OO0O0OO000000OO0O ['data']['ordinary_fertilizer']#line:1136
                        OOO000O0OOOO00O0O =OO0O0OO000000OO0O ['data']['videoStatus']#line:1137
                        OOOOOOO0OOO0O0O0O =OO0O0OO000000OO0O ['data']['waterVideoKey']#line:1138
                        print (f'【我的营养】:肥料:{str(OO000O000OOOOOO00).split(".")[0]}丨水滴:{str(O0000OOO000OO0O0O).split(".")[0]}')#line:1140
                        if float (OO000O000OOOOOO00 )<96 :#line:1141
                            if OOO000O0OOOO00O0O :#line:1142
                                time .sleep (random .randint (160 ,180 )/10 )#line:1143
                                O000O0OO00OOOOOOO =99 -float (OO000O000OOOOOO00 )#line:1144
                                OOOOOO0O00OO00000 ={"fertilizer":str (O000O0OO00OOOOOOO ).split ('.')[0 ]}#line:1145
                                OOOO0OOOOOOOOO00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0O000O000O00O000 ).json ()#line:1147
                                if 'status'in OOOO0OOOOOOOOO00O :#line:1149
                                    if OOOO0OOOOOOOOO00O ['status']==200 :#line:1150
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO0OOOOOOOOO00O["message"]}')#line:1151
                                    if OOOO0OOOOOOOOO00O ['status']==500 :#line:1152
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO0OOOOOOOOO00O["message"]}')#line:1153
                                        break #line:1154
                                if float (OO000O000OOOOOO00 )<78 :#line:1156
                                    O000O0OO00OOOOOOO =80 -float (OO000O000OOOOOO00 )#line:1157
                                    OOO0OO0OOO00OOO00 =f'_fertilizer={int(O000O0OO00OOOOOOO)}_{timi_new()}'#line:1158
                                    O000OO0OO000OO0O0 ={'source':'scsc','authorization':OOOOO000000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO00OOO00 ),'signstring':OOO0OO0OOO00OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1169
                                    O0O0O00O0OO0OOO00 ={"fertilizer":int (O000O0OO00OOOOOOO )}#line:1170
                                    O0OOO0000OOO0OOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O000OO0OO000OO0O0 ,data =O0O0O00O0OO0OOO00 ).json ()#line:1172
                                    if 'status'in O0OOO0000OOO0OOOO :#line:1174
                                        if O0OOO0000OOO0OOOO ['status']==200 :#line:1175
                                            print (f'【购买肥料】:购买肥料:{O0OOO0000OOO0OOOO["message"]}丨数量:{int(O000O0OO00OOOOOOO)}')#line:1176
                                        if O0OOO0000OOO0OOOO ['status']==500 :#line:1177
                                            print (f'【购买肥料】:购买肥料:{O0OOO0000OOO0OOOO["message"]}丨数量:{int(O000O0OO00OOOOOOO)}')#line:1178
                                            OOOOO0OO0OOOO0O0O =O0OOO0000OOO0OOOO ["message"].split ('-')[1 ]#line:1179
                                            O0OOOOO00O0000O00 =f'__{timi_new()}'#line:1180
                                            O00O000OOO000O0O0 ={'source':'scsc','authorization':OOOOO000000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00O0000O00 ),'signstring':O0OOOOO00O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1191
                                            O000000OO0O0OOOOO =requests .request ('get',f'{host}/user',headers =O00O000OOO000O0O0 ).json ()#line:1192
                                            if 'status'in O000000OO0O0OOOOO :#line:1193
                                                if O000000OO0O0OOOOO ['status']==200 :#line:1194
                                                    OOOOOOO000O0O0OOO =O000000OO0O0OOOOO ['data']['inner_id']#line:1195
                                                    if give_gold (OOOOOOO000O0O0OOO ,float (OOOOO0OO0OOOO0O0O )+1 ):#line:1196
                                                        OOOOO000000O0000O .energy ()#line:1197
                        if float (O0000OOO000OO0O0O )<880 :#line:1198
                            if OOOOOOO0OOO0O0O0O :#line:1199
                                time .sleep (random .randint (160 ,180 )/10 )#line:1200
                                O000OOO0O0O0000OO =999 -float (O0000OOO000OO0O0O )#line:1201
                                O000O00O0O00O0OO0 ={"water":str (O000OOO0O0O0000OO ).split ('.')[0 ]}#line:1202
                                OOO0000000O00O000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0O000O000O00O000 ).json ()#line:1204
                                if 'status'in OOO0000000O00O000 :#line:1206
                                    if OOO0000000O00O000 ['status']==200 :#line:1207
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0000000O00O000["message"]}')#line:1208
                                    if OOO0000000O00O000 ['status']==500 :#line:1209
                                        print (f'【购买水滴】:看广告获取水滴:{OOO0000000O00O000["message"]}')#line:1210
                                        break #line:1211
                                if float (O0000OOO000OO0O0O )<780 :#line:1212
                                    O000OOO0O0O0000OO =800 -float (O0000OOO000OO0O0O )#line:1213
                                    O0O000O000000O00O =f'_water={int(O000OOO0O0O0000OO)}_{timi_new()}'#line:1214
                                    OO0OOO00O0O000O0O ={'source':'scsc','authorization':OOOOO000000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O000O000000O00O ),'signstring':O0O000O000000O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1225
                                    O0OO00OO0OO00OO00 ={"water":int (O000OOO0O0O0000OO )}#line:1226
                                    O0O0OOO0OO00OO00O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0OOO00O0O000O0O ,data =O0OO00OO0OO00OO00 ).json ()#line:1228
                                    if 'status'in O0O0OOO0OO00OO00O :#line:1230
                                        if O0O0OOO0OO00OO00O ['status']==200 :#line:1231
                                            print (f'【购买水滴】:购买水滴:{O0O0OOO0OO00OO00O["message"]}丨数量:{int(O000OOO0O0O0000OO)}')#line:1232
                                        if O0O0OOO0OO00OO00O ['status']==500 :#line:1233
                                            print (f'【购买水滴】:购买水滴:{O0O0OOO0OO00OO00O["message"]}丨数量:{int(O000OOO0O0O0000OO)}')#line:1234
                                            OOOOO0OO0OOOO0O0O =O0O0OOO0OO00OO00O ["message"].split ('-')[1 ]#line:1235
                                            O0OOOOO00O0000O00 =f'__{timi_new()}'#line:1236
                                            O00O000OOO000O0O0 ={'source':'scsc','authorization':OOOOO000000O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00O0000O00 ),'signstring':O0OOOOO00O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1247
                                            O000000OO0O0OOOOO =requests .request ('get',f'{host}/user',headers =O00O000OOO000O0O0 ).json ()#line:1248
                                            if 'status'in O000000OO0O0OOOOO :#line:1249
                                                if O000000OO0O0OOOOO ['status']==200 :#line:1250
                                                    OOOOOOO000O0O0OOO =O000000OO0O0OOOOO ['data']['inner_id']#line:1251
                                                    if give_gold (OOOOOOO000O0O0OOO ,float (OOOOO0OO0OOOO0O0O )+1 ):#line:1252
                                                        OOOOO000000O0000O .energy ()#line:1253
                        break #line:1254
        except Exception as OO000000000O00O0O :#line:1255
            print (OO000000000O00O0O )#line:1256
def bundled_def ():#line:1259
    O00OO0OO0OOO00000 =['5570536','7750212','7911652','7911680','7805624']#line:1260
    return O00OO0OO0OOO00000 [random .randint (0 ,len (O00OO0OO0OOO00000 )-1 )]#line:1261
def version_of_the_validation ():#line:1265
    return str ((97 -56 )/10 )#line:1266
def ubbbf ():#line:1268
    print ('卡密验证通过   ✅')#line:1269
def sc2 ():#line:1272
    return "19319#$%^&*((*"#line:1273
def OO00OO0OO0OO00OO00o0 ():#line:1276
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1278
def get_ip ():#line:1281
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1283
def gitee_validation ():#line:1286
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1287
def gitee_edition ():#line:1290
    try :#line:1291
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1292
    except :#line:1293
        sys .exit (0 )#line:1294
def O000OO000O0O00OOO00 ():#line:1298
    try :#line:1299
        O0O0OOO0OOO00O0OO =gitee_edition ()#line:1300
        if version_of_the_validation ()<O0O0OOO0OOO00O0OO ['CityEarth']['edition']:#line:1301
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO0OOO00O0OO["CityEarth"]["edition"]}   ❌')#line:1302
            print (f'更新内容=>>{O0O0OOO0OOO00O0OO["CityEarth"]["content"]}')#line:1303
        else :#line:1304
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OOO0OOO00O0OO["CityEarth"]["edition"]}   ✅')#line:1305
            print (f'更新内容=>> {O0O0OOO0OOO00O0OO["CityEarth"]["content"]}')#line:1306
    except Exception as OO0O0OOO000OOOO00 :#line:1307
        print (OO0O0OOO000OOOO00 )#line:1308
def sc3 ():#line:1311
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1312
if __name__ =='__main__':#line:1315
    start ()#line:1316
