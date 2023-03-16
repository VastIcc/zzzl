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
@ 版本  4.0
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
        O0000OOOO0OO00O0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:15
        print (f"==========共找到{len(O0000OOOO0OO00O0O)}个账号==========")#line:16
        for O0OO00O0O00O00O00 in O0000OOOO0OO00O0O :#line:17
            O0OOOOOO0O000O0OO =[]#line:18
            print (f"------------正在执行第{O0000OOOO0OO00O0O.index(O0OO00O0O00O00O00) + 1}个账号------------")#line:19
            OOO0O000OOOOOOOO0 =CityEarth (O0OO00O0O00O00O00 ,O0OOOOOO0O000O0OO ,O0000OOOO0OO00O0O .index (O0OO00O0O00O00O00 ))#line:20
            def OO00OOO00O00OO0O0 ():#line:22
                if OOO0O000OOOOOOOO0 .base_info ():#line:24
                    OOO0O000OOOOOOOO0 .sealing ()#line:26
                    OOO0O000OOOOOOOO0 .invitenum ()#line:28
                    OOO0O000OOOOOOOO0 .query_to_sell ()#line:30
                    OOO0O000OOOOOOOO0 .game_map ()#line:32
                    OOO0O000OOOOOOOO0 .friends_invitation ()#line:34
                    OOO0O000OOOOOOOO0 .energy ()#line:36
                    OOO0O000OOOOOOOO0 .add_clover ()#line:38
                    OOO0O000OOOOOOOO0 .propsraffle ()#line:40
                    OOO0O000OOOOOOOO0 .synthetic ()#line:42
                    OOO0O000OOOOOOOO0 .crops_illustrated ()#line:44
                    OOO0O000OOOOOOOO0 .withdraw ()#line:46
                    if float (datetime .datetime .now ().hour )>8 :#line:47
                        OOO0O000OOOOOOOO0 .give_gold ()#line:49
            OO00OO00OOO0OOOOO =threading .Thread (target =OO00OOO00O00OO0O0 )#line:51
            OO00OO00OOO0OOOOO .start ()#line:52
            time .sleep (time_xx )#line:53
        print (f"------------正在处理数据------------")#line:54
        time .sleep (0.5 )#line:55
        O0OOOOO000OO000OO =format_msg ()#line:56
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OOOOO000OO000OO +' ')#line:57
        time .sleep (100 )#line:58
        print ('开始打印好友数量不足2的ID')#line:59
        for OO0000OOOO0O00OO0 in invited_new :#line:60
            print (OO0000OOOO0O00OO0 )#line:61
        print ('开始打印未实名的token')#line:62
        for O0000O00000O0O0O0 in weishim :#line:63
            print (O0000O00000O0O0O0 )#line:64
    except Exception as O0OO0000OO0OOOO0O :#line:65
        print (O0OO0000OO0OOOO0O )#line:66
def give_gold (OO00O0OOOO00000O0 ,OO0O0O000000O0000 ):#line:70
    try :#line:71
        O0OOOOO0O0OO00000 =f'_doneeNo={OO00O0OOOO00000O0}&quantity={int(OO0O0O000000O0000)}_{timi_new()}'#line:72
        OOOOO0OO000O00OO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0OOOOO0O0OO00000 ),'signstring':O0OOOOO0O0OO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:83
        OO00OOO0OOO00000O ={"quantity":int (OO0O0O000000O0000 ),"doneeNo":OO00O0OOOO00000O0 }#line:87
        OOOO00OOO0O0OOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOO0OO000O00OO0 ,data =OO00OOO0OOO00000O ).json ()#line:88
        if 'status'in OOOO00OOO0O0OOO0O :#line:90
            if OOOO00OOO0O0OOO0O ['status']==200 :#line:91
                if OOOO00OOO0O0OOO0O ['data']:#line:92
                    print (f'【赠送种子】:赠送{int(OO0O0O000000O0000)}种子给{OO00O0OOOO00000O0}成功')#line:93
                    return True #line:94
            if OOOO00OOO0O0OOO0O ['status']==401 :#line:95
                print (f'【赠送种子】:{OOOO00OOO0O0OOO0O["message"]}')#line:96
                return False #line:97
            if OOOO00OOO0O0OOO0O ['status']==500 :#line:98
                print (f'【赠送种子】:{OOOO00OOO0O0OOO0O["message"]}')#line:99
                return False #line:100
        return False #line:101
    except Exception as OOO0O000000OO00OO :#line:102
        print (OOO0O000000OO00OO )#line:103
def kvkv ():#line:106
    return '/vastzzzl/vastzzzl/raw/master'#line:107
def oyoy ():#line:109
    return '卡密未激活   ❌'#line:110
def sign (OOOOO0OO0000O0OOO ):#line:113
    OOOOOO00O000OOO00 =hashlib .md5 (OOOOO0OO0000O0OOO .encode ()).hexdigest ()#line:114
    O0OO0OO00OOOO0O0O =sc1 ()#line:115
    OO0OOO000O000O0O0 =sc2 ()#line:116
    O000O00000O000O0O =sc3 ()#line:117
    OOO00OO0OO00O0000 =O0OO0OO00OOOO0O0O +OOOOOO00O000OOO00 +OO0OOO000O000O0O0 +O000O00000O000O0O #line:118
    O0O0O0000O0OOO0OO =hashlib .md5 (OOO00OO0OO00O0000 .encode ()).hexdigest ()#line:119
    return O0O0O0000O0OOO0OO #line:120
def format_msg ():#line:123
    OO00000O00000OO0O =""#line:124
    for O000OO0000OOO0O0O in msg_list :#line:125
        OO00000O00000OO0O +=str (O000OO0000OOO0O0O )+"\r\n"#line:126
    return OO00000O00000OO0O #line:127
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
def get_json_data (O00000OOO0O0OOO00 ,O00OO00OO0OO00OO0 ,OOO0OO0O0OOOO0000 ,O0OO00000OO0O0OO0 ):#line:151
    with open (O00000OOO0O0OOO00 ,'rb')as O000OO0OO0OO000OO :#line:152
        OOO0000OO00O0O00O =json .load (O000OO0OO0OO000OO )#line:153
        OOO0000OO00O0O00O ['data'][O00OO00OO0OO00OO0 ][OOO0OO0O0OOOO0000 ]=O0OO00000OO0O0OO0 #line:154
        O0O0OO0O00O0O0O0O =OOO0000OO00O0O00O #line:155
    O000OO0OO0OO000OO .close ()#line:156
    return O0O0OO0O00O0O0O0O #line:157
def write_json_data (OO0OO000OOO000O0O ):#line:160
    with open (json_path1 ,'w')as O0O0O00O00000OOO0 :#line:161
        json .dump (OO0OO000OOO000O0O ,O0O0O00O00000OOO0 )#line:162
    O0O0O00O00000OOO0 .close ()#line:163
    return True #line:164
class CityEarth :#line:167
    def __init__ (O0000O0OOO0O0O0OO ,OO000O0OOOOO00OOO ,OO00OOO0O0OOO0O0O ,OOOO0O000OO0O0OOO ):#line:169
        try :#line:170
            O0000O0OOO0O0O0OO .msg =OO00OOO0O0OOO0O0O #line:171
            O0000O0OOO0O0O0OO .time =str (time .time ()*1000 ).split ('.')[0 ]#line:172
            O0000O0OOO0O0O0OO .token =OO000O0OOOOO00OOO ['authorization']#line:173
            O0000O0OOO0O0O0OO .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:174
            O0000O0OOO0O0O0OO .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:175
            O0000O0OOO0O0O0OO .elephant_user =OO000O0OOOOO00OOO ['elephant_user']#line:176
            O0000O0OOO0O0O0OO .elephant_pswd =OO000O0OOOOO00OOO ['elephant_pswd']#line:177
            O0000O0OOO0O0O0OO .elephant_Task_ID =OO000O0OOOOO00OOO ['elephant_Task_ID']#line:178
            O0000O0OOO0O0O0OO .len_new =OOOO0O000OO0O0OOO #line:179
        except :#line:180
            print ('变量格式错误')#line:181
    def base_info (OOO0OO00O0OO00O00 ):#line:184
        try :#line:185
            OOO0OO00O0OO00O00 .watched_ad ()#line:187
            OO0000OO00000OO0O =f'__{timi_new()}'#line:188
            O0OO000OOO0000OOO ={'source':'scsc','authorization':OOO0OO00O0OO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OO00000OO0O ),'signstring':OO0000OO00000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:199
            OOO00O0O0OO00OO0O =requests .request ('get',f'{host}/user',headers =O0OO000OOO0000OOO ).json ()#line:200
            if 'status'in OOO00O0O0OO00OO0O :#line:202
                if OOO00O0O0OO00OO0O ['status']==200 :#line:203
                    OO000O0000OO000O0 =OOO00O0O0OO00OO0O ['data']['nickname']#line:204
                    O0O000OOOOOOO0OOO =OOO00O0O0OO00OO0O ['data']['inner_id']#line:205
                    OOOOO0OOOOOO000O0 =OOO00O0O0OO00OO0O ['data']['assets']['gold']#line:206
                    O0O0OO0O000O0O0OO =OOO00O0O0OO00OO0O ['data']['level']#line:207
                    print (f'【账号信息】:昵称:{OO000O0000OO000O0[:5]}丨ID:{O0O000OOOOOOO0OOO}丨等级:{O0O0OO0O000O0O0OO}丨金种子:{str(OOOOO0OOOOOO000O0).split(".")[0]}')#line:209
                    if 'wx_'in OO000O0000OO000O0 :#line:210
                        OOO0OO00O0OO00O00 .change_nickname ()#line:211
                if OOO00O0O0OO00OO0O ['status']==401 :#line:212
                    print ('【账号信息】:账号失效正在尝试登录')#line:213
                    if OOO0OO00O0OO00O00 .elephant_user =='f':#line:214
                        return False #line:215
                    O0O0OOOO0OO00OO0O =Invalid_login .addtask (elephant_user =OOO0OO00O0OO00O00 .elephant_user ,elephant_pswd =OOO0OO00O0OO00O00 .elephant_pswd ,elephant_Task_ID =OOO0OO00O0OO00O00 .elephant_Task_ID )#line:218
                    OO0OO0O00O0OOO000 =get_json_data (json_path ,OOO0OO00O0OO00O00 .len_new ,'authorization',O0O0OOOO0OO00OO0O )#line:219
                    if write_json_data (OO0OO0O00O0OOO000 ):#line:220
                        print ('正在写入账号配置文件')#line:221
                    return False #line:222
                if OOO00O0O0OO00OO0O ['status']==500 :#line:223
                    return False #line:224
            return True #line:225
        except Exception as O00O00O000O0O0OO0 :#line:226
            print (O00O00O000O0O0OO0 )#line:227
    def sealing (O00000OOO000O0OO0 ):#line:230
        try :#line:231
            O000O00OOO0O000O0 =f'__{timi_new()}'#line:232
            O0OO0OOO0O0OOO000 ={'source':'scsc','authorization':O00000OOO000O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00OOO0O000O0 ),'signstring':O000O00OOO0O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:243
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0OO0OOO0O0OOO000 )#line:244
            requests .request ('get',f'{host}/packsack/list',headers =O0OO0OOO0O0OOO000 )#line:245
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0OO0OOO0O0OOO000 )#line:246
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0OO0OOO0O0OOO000 )#line:247
            requests .request ('get',f'{host}/user',headers =O0OO0OOO0O0OOO000 )#line:248
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0OO0OOO0O0OOO000 )#line:249
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0OO0OOO0O0OOO000 )#line:250
            requests .request ('post',f'{host}/announcement/announcement',headers =O0OO0OOO0O0OOO000 )#line:251
            requests .request ('get',f'{host}/game/getAllData',headers =O0OO0OOO0O0OOO000 )#line:252
            requests .request ('get',f'{host}/assets',headers =O0OO0OOO0O0OOO000 )#line:253
        except Exception as OO0OOO00OO000OO0O :#line:254
            print (OO0OOO00OO000OO0O )#line:255
    def the_query (O00O00OO000OO0O00 ):#line:258
        try :#line:259
            O00OO0O000O0000O0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:260
            OOO00OOOO000OO00O ={'authorization':O00O00OO000OO0O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0O000O0000O0 ),'signstring':O00OO0O000O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:270
            OO0000OO0O0OO0O0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO00OOOO000OO00O ).json ()#line:272
            if 'status'in OO0000OO0O0OO0O0O :#line:274
                if OO0000OO0O0OO0O0O ['status']==200 :#line:275
                    OOO000O0OOOO00000 =OO0000OO0O0OO0O0O ['data']['rows'][3 ]['price']#line:276
                    O00O00OO000OO0O00 .market_sale (OOO000O0OOOO00000 )#line:277
        except Exception as O0OO00O0O0OOOOOOO :#line:278
            print (O0OO00O0O0OOOOOOO )#line:279
    def market_sale (OO0OOO000O00O0OOO ,O0OO000OO0OOO0O0O ):#line:282
        try :#line:283
            OO000OO0OOO0OO000 =timi_new ()#line:284
            O0O0O0OO0O00O000O =f'type=crop__{OO000OO0OOO0OO000}'#line:285
            O000OOO00OOOOOO0O ={'source':'scsc','authorization':OO0OOO000O00O0OOO .token ,'timestamp':str (OO000OO0OOO0OO000 ),'sign':sign (O0O0O0OO0O00O000O ),'signstring':O0O0O0OO0O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:296
            OOO00O000OO00000O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O000OOO00OOOOOO0O ).json ()#line:298
            if 'status'in OOO00O000OO00000O :#line:300
                if OOO00O000OO00000O ['status']==200 :#line:301
                    if OOO00O000OO00000O ['data']['rows']:#line:302
                        OO0O0OO0O0O0OOO00 =OOO00O000OO00000O ['data']['rows'][0 ]['packsackItemId']#line:303
                        OOO0O0O0O0O00O0OO =OOO00O000OO00000O ['data']['rows'][0 ]['quantity']#line:304
                        OO0OO0OO00OO0OOO0 =float (O0OO000OO0OOO0O0O )+float (random .randint (1 ,9 )*0.001 )#line:305
                        O00OOO00OO00000O0 =f'_packsackItemId={OO0O0OO0O0O0OOO00}&price={str(OO0OO0OO00OO0OOO0)[:7]}&quantity={OOO0O0O0O0O00O0OO}_{OO000OO0OOO0OO000}'#line:306
                        OOO0O0OO0O0O00OOO ={'source':'scsc','authorization':OO0OOO000O00O0OOO .token ,'timestamp':str (OO000OO0OOO0OO000 ),'sign':sign (O00OOO00OO00000O0 ),'signstring':O00OOO00OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
                        O0000O00OO0O0OOOO ={"packsackItemId":OO0O0OO0O0O0OOO00 ,"price":str (OO0OO0OO00OO0OOO0 )[:7 ],"quantity":str (OOO0O0O0O0O00O0OO )}#line:322
                        O0OO0OOO000O0000O =requests .request ('post',f'{host}/market/sale',headers =OOO0O0OO0O0O00OOO ,data =O0000O00OO0O0OOOO ).json ()#line:323
                        if 'status'in O0OO0OOO000O0000O :#line:325
                            if O0OO0OOO000O0000O ['status']==200 :#line:326
                                print (f'【上架芦荟】:数量:{OOO0O0O0O0O00O0OO}丨价格:{str(OO0OO0OO00OO0OOO0)[:7]}')#line:327
        except Exception as O0OO000000OOOO0OO :#line:328
            print (O0OO000000OOOO0OO )#line:329
    def query_to_sell (O0OO0OO000OO0000O ):#line:332
        try :#line:333
            O00OO00OO00OOOOOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:334
            O0O0O0OO0OO0OOO00 ={'source':'scsc','authorization':O0OO0OO000OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00OO00OOOOOO ),'signstring':O00OO00OO00OOOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:345
            O0OO00OO0000OO000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0O0O0OO0OO0OOO00 ).json ()#line:347
            if 'status'in O0OO00OO0000OO000 :#line:349
                if O0OO00OO0000OO000 ['status']==200 :#line:350
                    for O0O0000OOOO0OO00O in O0OO00OO0000OO000 ['data']['rows']:#line:351
                        O00O0O0OOO000OOOO =O0O0000OOOO0OO00O ['materialKey']#line:352
                        OOOO0OO0OOO00OO0O =O0O0000OOOO0OO00O ['quantity']#line:353
                        OO00OO0O000O0000O =O0O0000OOOO0OO00O ['price']#line:354
                        O00O00OOOOO0OOO00 =O0O0000OOOO0OO00O ['saleState']#line:355
                        if O00O00OOOOO0OOO00 ==0 :#line:356
                            print (f'【出售订单】:名称:{O00O0O0OOO000OOOO}丨数量:{OOOO0OO0OOO00OO0O}丨价格:{OO00OO0O000O0000O}')#line:357
                            OOO0O00OO0OO00O00 =O0O0000OOOO0OO00O ['id']#line:358
                            if float (datetime .datetime .now ().hour )>8 :#line:359
                                O0OO0OO000OO0000O .cacel_sale (OOO0O00OO0OO00O00 )#line:360
        except Exception as O0000O00O00OO0O00 :#line:361
            print (O0000O00O00OO0O00 )#line:362
    def cacel_sale (O0000O0OO00O0OOO0 ,OOOO0OOOOO00OO0OO ):#line:365
        try :#line:366
            O00000O000O0O000O =f'_saleId={OOOO0OOOOO00OO0OO}_{timi_new()}'#line:367
            OO0O000OOO00O0OO0 ={'source':'scsc','authorization':O0000O0OO00O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O000O0O000O ),'signstring':O00000O000O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:378
            O000OO000OO00O00O ={"saleId":OOOO0OOOOO00OO0OO }#line:381
            O0OOOOO0O00000O0O =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0O000OOO00O0OO0 ,data =O000OO000OO00O00O ).json ()#line:382
            if 'status'in O0OOOOO0O00000O0O :#line:384
                if O0OOOOO0O00000O0O ['status']==200 :#line:385
                    print (f'【下架出售】:{O0OOOOO0O00000O0O["data"]}')#line:386
        except Exception as OO0OOOOO00000O0O0 :#line:387
            print (OO0OOOOO00000O0O0 )#line:388
    def change_nickname (O0O0000OOO00O0OOO ):#line:391
        try :#line:392
            O0OO0OOOO0OOOO00O =timi_new ()#line:393
            O000000O0OO0OOO0O ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:394
            OO0O0O0000O0OOO0O =requests .request ('post','https://www.qmsjmfb.com/',data =O000000O0OO0OOO0O ).text #line:395
            O0O0OOO0O0000OO00 =re .findall ('<ul><li>(.*?)</li>',OO0O0O0000O0OOO0O )[0 ][:3 ]#line:396
            O000O000OO00OO0O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O0O0OOO0O0000OO00}').json ()#line:397
            O0OOOO0O00O00000O =O000O000OO00OO0O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:398
            OOOOO0O00OO0O00OO ={"nickname":O0OOOO0O00O00000O }#line:399
            OOO0OOOOO0O000O00 =f'_nickname={O0OOOO0O00O00000O}_{O0OO0OOOO0OOOO00O}'#line:400
            O00O0OOO000O0O0O0 ={'source':'scsc','authorization':O0O0000OOO00O0OOO .token ,'timestamp':O0OO0OOOO0OOOO00O ,'sign':sign (OOO0OOOOO0O000O00 ),'signstring':OOO0OOOOO0O000O00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:411
            OOO0O0OOO000O00O0 =requests .request ('patch',f'{host}/user/nickname',headers =O00O0OOO000O0O0O0 ,data =OOOOO0O00OO0O00OO ).json ()#line:412
            if 'status'in OOO0O0OOO000O00O0 :#line:414
                if OOO0O0OOO000O00O0 ['status']==200 :#line:415
                    print (f'【修改网名】:网名:{O0OOOO0O00O00000O}丨{OOO0O0OOO000O00O0["message"]}')#line:416
        except Exception as OO00OO00OO0O00OO0 :#line:417
            print (OO00OO00OO0O00OO0 )#line:418
    def withdraw (OO00OO0000O0O00OO ):#line:421
        try :#line:422
            OOO0OOO0OOO00OO00 =f'__{timi_new()}'#line:423
            O00O0O000OO00O0O0 ={'source':'scsc','authorization':OO00OO0000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO00OO00 ),'signstring':OOO0OOO0OOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:434
            OO00OO00000O00OOO =requests .request ('get',f'{host}/assets',headers =O00O0O000OO00O0O0 ).json ()#line:435
            if 'status'in OO00OO00000O00OOO :#line:437
                if OO00OO00000O00OOO ['status']==200 :#line:438
                    OOO0OO0000OOO0000 =OO00OO00000O00OOO ['data']['cash']#line:439
                    if float (OOO0OO0000OOO0000 )>20 :#line:440
                        OOO0OOO0OOO00OO00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:441
                        O00O0O000OO00O0O0 ={'authorization':OO00OO0000O0O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OOO00OO00 ),'signstring':OOO0OOO0OOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:451
                        O000000O0OO00OOOO ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:452
                        OO0000000OO0O0O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00O0O000OO00O0O0 ,data =O000000O0OO00OOOO ).json ()#line:454
                        if 'status'in OO0000000OO0O0O00 :#line:456
                            if OO0000000OO0O0O00 ['status']==200 :#line:457
                                print (f'【余额提现】:{OO0000000OO0O0O00["data"]}')#line:458
                        if 'status'in OO0000000OO0O0O00 :#line:459
                            if OO0000000OO0O0O00 ['status']==500 :#line:460
                                print (f'【余额提现】:{OO0000000OO0O0O00["message"]}')#line:461
        except Exception as O000000OOO000O0OO :#line:462
            print (O000000OOO000O0OO )#line:463
    def invitenum (OOOOO00O00OOOOO00 ):#line:466
        global invited_new #line:467
        try :#line:468
            O000OO00OOOOO000O =f'__{timi_new()}'#line:469
            OOOO0000O00O00000 ={'source':'scsc','authorization':OOOOO00O00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO00OOOOO000O ),'signstring':O000OO00OOOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:480
            O0000O0OO0OOOOO0O =requests .request ('get',f'{host}/invite/invitenum',headers =OOOO0000O00O00000 ).json ()#line:481
            if 'status'in O0000O0OO0OOOOO0O :#line:483
                if O0000O0OO0OOOOO0O ['status']==200 :#line:484
                    O0O0OOO0O0000O00O =O0000O0OO0OOOOO0O ['data']['invited_count']#line:485
                    OO000OOO0OOOOO00O =O0000O0OO0OOOOO0O ['data']['invited_second_count']#line:486
                    print (f'【我的邀请】:直邀好友:{O0O0OOO0O0000O00O}丨间邀好友:{OO000OOO0OOOOO00O}')#line:487
                    if O0O0OOO0O0000O00O <2 :#line:488
                        OOO0OO0OO00O00000 =f'__{timi_new()}'#line:489
                        OOOOO0O00OO00OO0O ={'source':'scsc','authorization':OOOOO00O00OOOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OO00O00000 ),'signstring':OOO0OO0OO00O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:500
                        O00OO00000000OO0O =requests .request ('get',f'{host}/user',headers =OOOOO0O00OO00OO0O ).json ()#line:501
                        if 'status'in O00OO00000000OO0O :#line:503
                            if O00OO00000000OO0O ['status']==200 :#line:504
                                invited_new .append (O00OO00000000OO0O ['data']['inner_id'])#line:505
        except Exception as OOOO000O00OO00000 :#line:506
            print (OOOO000O00OO00000 )#line:507
    def game_map (OO00OOOO000O0OO0O ):#line:510
        try :#line:511
            OO00O000OO0000000 =f'__{timi_new()}'#line:512
            O0000O000OO000O00 ={'source':'scsc','authorization':OO00OOOO000O0OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OO0000000 ),'signstring':OO00O000OO0000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:523
            O0O0OO00O0O0O000O =requests .request ('get',f'{host}/game/map',headers =O0000O000OO000O00 ).json ()#line:524
            if 'status'in O0O0OO00O0O0O000O :#line:526
                if O0O0OO00O0O0O000O ['status']==200 :#line:527
                    for O00OOOO00OOO0OOOO in O0O0OO00O0O0O000O ['data']['list'][0 ]['crops']:#line:528
                        O00OOO0000O000OO0 =O00OOOO00OOO0OOOO ['level']#line:530
                        if O00OOO0000O000OO0 ==41 :#line:531
                            OOOOO000OO0O000O0 =O00OOOO00OOO0OOOO ['crop_name']#line:532
                            O00OOOOOO0O0O00O0 =O00OOOO00OOO0OOOO ['count']#line:533
                            if O00OOOOOO0O0O00O0 >0 :#line:534
                                print (f'【农业资产】:{OOOOO000OO0O000O0}丨数量:{O00OOOOOO0O0O00O0}')#line:535
                                if float (datetime .datetime .now ().hour )>8 :#line:536
                                    OO00OOOO000O0OO0O .the_query ()#line:537
        except Exception as OOO00O0O00O000O0O :#line:538
            print (OOO00O0O00O000O0O )#line:539
    def give_gold (OO00OO0000O0OO0O0 ):#line:542
        try :#line:543
            O0O0000000O0000O0 =f'__{timi_new()}'#line:544
            OOOOOOOO00O00OO0O ={'source':'scsc','authorization':OO00OO0000O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000000O0000O0 ),'signstring':O0O0000000O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
            OO0OOOOO000OOO0OO =requests .request ('get',f'{host}/user',headers =OOOOOOOO00O00OO0O ).json ()#line:556
            if 'status'in OO0OOOOO000OOO0OO :#line:557
                if OO0OOOOO000OOO0OO ['status']==200 :#line:558
                    if float (OO00OO0000O0OO0O0 .doneeNo )!=0 :#line:559
                        O0OOOOO00OO0O0OOO =OO0OOOOO000OOO0OO ['data']['assets']['gold']#line:560
                        if float (O0OOOOO00OO0O0OOO )>float (OO00OO0000O0OO0O0 .innerId ):#line:561
                            OO00OOOOOOOO00OO0 =int (float (O0OOOOO00OO0O0OOO )/1.1 )#line:562
                            O0O0000000O0000O0 =f'_doneeNo={OO00OO0000O0OO0O0.doneeNo}&quantity={OO00OOOOOOOO00OO0}_{timi_new()}'#line:563
                            OOOOOOOO00O00OO0O ={'source':'scsc','authorization':OO00OO0000O0OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000000O0000O0 ),'signstring':O0O0000000O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:574
                            O00000O00OO0O000O ={"quantity":OO00OOOOOOOO00OO0 ,"doneeNo":OO00OO0000O0OO0O0 .doneeNo }#line:578
                            OO00O0O0OOOO0O000 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOOOOOO00O00OO0O ,data =O00000O00OO0O000O ).json ()#line:579
                            if 'status'in OO00O0O0OOOO0O000 :#line:581
                                if OO00O0O0OOOO0O000 ['status']==200 :#line:582
                                    if OO00O0O0OOOO0O000 ['data']:#line:583
                                        print (f'【赠送种子】:赠送{OO00OOOOOOOO00OO0}种子给{OO00OO0000O0OO0O0.doneeNo}成功')#line:584
                    else :#line:585
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:586
        except Exception as OOOO0O000O0000O00 :#line:587
            print (OOOO0O000O0000O00 )#line:588
    def invitation (O00OOOO000O00O0OO ):#line:590
        try :#line:591
            _OO0O0O00OO0OOOOO0 =float (bundled_def ())/4 #line:592
            O00OO0OO0O0OOO0OO =f'_innerId={int(_OO0O0O00OO0OOOOO0)}_{timi_new()}'#line:593
            O00O0OO0000OO0O00 ={'source':'scsc','authorization':O00OOOO000O00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0O0OOO0OO ),'signstring':O00OO0OO0O0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:604
            OO0OO0OO0O0O0OO0O ={"innerId":int (_OO0O0O00OO0OOOOO0 )}#line:605
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O0OO0000OO0O00 ,data =OO0OO0OO0O0O0OO0O )#line:606
        except Exception as OOOO0O0O00OO0OOOO :#line:607
            print (OOOO0O0O00OO0OOOO )#line:608
    def winning_rewards (O00O00OO0000000O0 ):#line:611
        try :#line:612
            O0000O0OOO00OO000 =f'__{timi_new()}'#line:613
            OOO00OOO0OOOOO0O0 ={'source':'scsc','authorization':O00O00OO0000000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O0OOO00OO000 ),'signstring':O0000O0OOO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:624
            O0OOO000O000OOO0O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO00OOO0OOOOO0O0 ).json ()#line:625
            if 'status'in O0OOO000O000OOO0O :#line:627
                if O0OOO000O000OOO0O ['status']==200 :#line:628
                    if O0OOO000O000OOO0O ['data']['amount']:#line:629
                        OOOO0OOOOO00O0OOO =O0OOO000O000OOO0O ['data']['amount']['gold']#line:630
                        return OOOO0OOOOO00O0OOO #line:631
                    else :#line:632
                        return 0 #line:633
        except Exception as OOO0OOO0OOO00O00O :#line:634
            print (OOO0OOO0OOO00O00O )#line:635
    def certification (OO0O000OOO000OO00 ):#line:638
        try :#line:639
            OOO0O0O00O00O000O =f'__{timi_new()}'#line:640
            OO0OO00OO00OOOOOO ={'source':'scsc','authorization':OO0O000OOO000OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O00O00O000O ),'signstring':OOO0O0O00O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:651
            O0O00O0O0OO00O0O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OO0OO00OO00OOOOOO ).json ()#line:652
            if 'status'in O0O00O0O0OO00O0O0 :#line:654
                if O0O00O0O0OO00O0O0 ['status']==200 :#line:655
                    if O0O00O0O0OO00O0O0 ['data']['result']:#line:656
                        O00OOOO00OO0O0OO0 =O0O00O0O0OO00O0O0 ['data']['nick_name']#line:657
                        return O00OOOO00OO0O0OO0 #line:658
                    else :#line:659
                        return '未实名'#line:660
        except Exception as OO0OOOO000OO00OO0 :#line:661
            print (OO0OOOO000OO00OO0 )#line:662
    def crops_illustrated (OO0O0OO000OO000OO ):#line:665
        try :#line:666
            OOO0O00O00OO00O0O =f'__{timi_new()}'#line:667
            O00O00OO000OO00O0 ={'source':'scsc','authorization':OO0O0OO000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00OO00O0O ),'signstring':OOO0O00O00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:678
            O000OOOO00OOO000O =requests .request ('get',f'{host}/game/crops/illustrated',headers =O00O00OO000OO00O0 ).json ()#line:679
            if 'status'in O000OOOO00OOO000O :#line:681
                if O000OOOO00OOO000O ['status']==200 :#line:682
                    OOO0OO00OO0O0OOO0 =O000OOOO00OOO000O ['data'][0 ]['crops']#line:683
                    for O00000O00O0OO0O0O in OOO0OO00OO0O0OOO0 :#line:684
                        if O00000O00O0OO0O0O ['ill_clover_award']:#line:685
                            if float (O00000O00O0OO0O0O ['ill_clover_award'])>1 :#line:686
                                if O00000O00O0OO0O0O ['is_finish']:#line:687
                                    if not O00000O00O0OO0O0O ['is_getit']:#line:688
                                        if OO0O0OO000OO000OO .certification ()!='未实名':#line:689
                                            OOO0O00O00OO00O0O =f'_award_level={O00000O00O0OO0O0O["level"]}_{timi_new()}'#line:690
                                            O00O00OO000OO00O0 ={'source':'scsc','authorization':OO0O0OO000OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00OO00O0O ),'signstring':OOO0O00O00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:701
                                            O00O0OOOOOOO00O00 ={"award_level":O00000O00O0OO0O0O ['level']}#line:702
                                            OO00OO00OOO00O0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O00O00OO000OO00O0 ,json =O00O0OOOOOOO00O00 ).json ()#line:704
                                            if 'status'in OO00OO00OOO00O0O0 :#line:705
                                                if OO00OO00OOO00O0O0 ['status']==200 :#line:706
                                                    OO0OO00OO0OO0OOOO =OO00OO00OOO00O0O0 ['data']['ill_clover_award']#line:707
                                                    print (f'【图鉴奖励】:领取{O00000O00O0OO0O0O["crop_name"]}成就丨奖励{OO0OO00OO0OO0OOOO}☘️')#line:709
                                                if OO00OO00OOO00O0O0 ['status']==500 :#line:710
                                                    print (f'【图鉴奖励】:{OO00OO00OOO00O0O0["message"]}')#line:711
        except Exception as O0OOO0OOO0000O00O :#line:712
            print (O0OOO0OOO0000O00O )#line:713
    def watched_ad (OO000OOO000O00O00 ):#line:716
        try :#line:717
            OO0OOO0O000000OO0 =f'__{timi_new()}'#line:718
            OO0OO0O0O000OOO00 ={'source':'scsc','authorization':OO000OOO000O00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0O000000OO0 ),'signstring':OO0OOO0O000000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:729
            OOOOOOO000OOO000O =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0O0O000OOO00 ).json ()#line:730
            if 'status'in OOOOOOO000OOO000O :#line:732
                if OOOOOOO000OOO000O ['status']==200 :#line:733
                    if 'offlineInfo'in OOOOOOO000OOO000O ['data']:#line:734
                        time .sleep (random .randint (1 ,3 ))#line:735
                        O000O00000O0OO00O =OOOOOOO000OOO000O ['data']['offlineInfo']['off_minute']#line:736
                        OO0OO00OOOOOO00OO =float (OOOOOOO000OOO000O ['data']['silver'])/1000000000000 #line:737
                        time .sleep (1 )#line:738
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO0OO0O0O000OOO00 ).json ()#line:739
                        time .sleep (2 )#line:740
                        OO0O00000OO00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OO0OO0O0O000OOO00 ).json ()#line:741
                        if 'status'in OO0O00000OO00OOO0 :#line:743
                            if OO0O00000OO00OOO0 ['status']==200 :#line:744
                                O00O0O00000O00O00 =float (OO0O00000OO00OOO0 ['data']['silver'])/1000000000000 #line:745
                                O00O0OOOOO000OO0O =str (O00O0O00000O00O00 -OO0OO00OOOOOO00OO )[:6 ]#line:746
                                print (f'【离线奖励】:翻倍离线{O000O00000O0OO00O}分钟奖励🌱数量:{O00O0OOOOO000OO0O}t粒')#line:747
        except Exception as O00OO00O0O00OO0OO :#line:748
            print (O00OO00O0O00OO0OO )#line:749
    def user_ad (OO000OO0OOO000000 ):#line:752
        try :#line:753
            OO000O0OOOO00O00O =f'__{timi_new()}'#line:754
            OOO00O0O00O00OO0O ={'source':'scsc','authorization':OO000OO0OOO000000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0OOOO00O00O ),'signstring':OO000O0OOOO00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:765
            O0OO0O0OOOO000OO0 =requests .request ('get',f'{host}/user/ad',headers =OOO00O0O00O00OO0O ).json ()#line:766
            if 'status'in O0OO0O0OOOO000OO0 :#line:768
                if O0OO0O0OOOO000OO0 ['status']==200 :#line:769
                    OO000OOOOO0O00000 =O0OO0O0OOOO000OO0 ['data']['max_time']#line:770
                    O00OOOOO00OO0OOOO =O0OO0O0OOOO000OO0 ['data']['watch_time']#line:771
                    O00OO00O0000OOOOO =O0OO0O0OOOO000OO0 ['data']['added_time']#line:772
                    print (f'【获取种子】:获取🌱剩余{O00OO00O0000OOOOO + OO000OOOOO0O00000 - O00OOOOO00OO0OOOO}次丨好友提供:{O00OO00O0000OOOOO}次')#line:773
                    if O00OO00O0000OOOOO +OO000OOOOO0O00000 -O00OOOOO00OO0OOOO >0 :#line:774
                        time .sleep (random .randint (16 ,19 ))#line:775
                        O0O0O0OO00000000O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O0O00O00OO0O ).json ()#line:776
                        if 'status'in O0O0O0OO00000000O :#line:778
                            if O0O0O0OO00000000O ['status']==200 :#line:779
                                O0OO000OO0000O0OO =float (O0O0O0OO00000000O ['data']['silver'])/1000000000000 #line:780
                                print (f'【获取种子】:获得🌱:{int(O0OO000OO0000O0OO)}t粒')#line:781
                                return True #line:782
                            if O0O0O0OO00000000O ['status']==500 :#line:783
                                OOOO0000O0O0O0OO0 =O0O0O0OO00000000O ['message']#line:784
                                print (f'【获取种子】:{OOOO0000O0O0O0OO0}')#line:785
                                return False #line:786
        except Exception as OO00O0O00O000OO00 :#line:787
            print (OO00O0O00O000OO00 )#line:788
    def synthetic (OO0000OOO0O0OOO0O ):#line:791
        global id ,g #line:792
        try :#line:793
            OOOOOOOO0O0OOO000 =OO0000OOO0O0OOO0O .level_new ()#line:794
            O0O0OOO00OOO0OOO0 =random .randint (9 ,11 )#line:795
            OO0O00000OO0O0000 =f'_site=8&targetSite={O0O0OOO00OOO0OOO0}_{timi_new()}'#line:796
            OOOOO0OO00O00OOO0 ={'source':'scsc','authorization':OO0000OOO0O0OOO0O .token ,'timestamp':timi_new (),'sign':sign (OO0O00000OO0O0000 ),'signstring':OO0O00000OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:807
            O0OO00OO000OO000O ={"site":int (8 ),"targetSite":int (O0O0OOO00OOO0OOO0 )}#line:808
            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0OO00O00OOO0 ,json =O0OO00OO000OO000O )#line:809
            while True :#line:810
                OOOOO0OOO000O0OO0 =f'__{timi_new()}'#line:811
                O0O0OO0OOOOO0000O ={'source':'scsc','authorization':OO0000OOO0O0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0OOO000O0OO0 ),'signstring':OOOOO0OOO000O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:822
                O0O00O0O0OOOO00OO =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OOOOO0000O ).json ()#line:823
                if 'status'in O0O00O0O0OOOO00OO :#line:825
                    if O0O00O0O0OOOO00OO ['status']==200 :#line:826
                        OOO00O00O0OO000OO =O0O00O0O0OOOO00OO ['data']['cropList']#line:827
                        O0OOOOO00O0OOO0OO =O0O00O0O0OOOO00OO ['data']['gameCoreDataDBid']#line:828
                        OOOOO0OO00000O0O0 =float (O0O00O0O0OOOO00OO ['data']['silver'])/1000000000000 #line:829
                        OO0O000O000O0O00O =0 #line:834
                        for O00OOOOOO0O0OOOO0 in OOO00O00O0OO000OO :#line:835
                            if not O00OOOOOO0O0OOOO0 :#line:836
                                O0O0OOOOOOO00OOOO =f'_crop_id={O0OOOOO00O0OOO0OO}&site={OO0O000O000O0O00O}_{OO0000OOO0O0OOO0O.time}'#line:837
                                OOO00OOOO000OO000 ={'source':'scsc','authorization':OO0000OOO0O0OOO0O .token ,'timestamp':OO0000OOO0O0OOO0O .time ,'sign':sign (O0O0OOOOOOO00OOOO ),'signstring':O0O0OOOOOOO00OOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:847
                                O0OO0O0O00O000O00 ={"site":OO0O000O000O0O00O ,"crop_id":O0OOOOO00O0OOO0OO }#line:848
                                O00O000O000OO0000 =requests .request ('post',f'{host}/game/crops/buy',headers =OOO00OOOO000OO000 ,data =O0OO0O0O00O000O00 ).json ()#line:849
                                time .sleep (random .randint (1 ,3 )/10 )#line:851
                                if 'status'in O00O000O000OO0000 :#line:852
                                    if O00O000O000OO0000 ['status']==200 :#line:853
                                        if O00O000O000OO0000 ['message']=='种子数量不足':#line:854
                                            OOOOOOOO0O0OOO000 =OO0000OOO0O0OOO0O .level_new ()#line:855
                                            print (f'【种植合成】:{O00O000O000OO0000["message"]}')#line:856
                                            if not OO0000OOO0O0OOO0O .user_ad ():#line:857
                                                return False #line:858
                                    if O00O000O000OO0000 ['status']==500 :#line:859
                                        print (f'【种植合成】:{O00O000O000OO0000["message"]}')#line:860
                                        return False #line:861
                            OO0O000O000O0O00O +=1 #line:862
                        O000000OOOOO00OO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O0OO0OOOOO0000O ).json ()#line:863
                        O00OO0000OOO0OO00 =O000000OOOOO00OO0 ['data']['cropList']#line:864
                        O0O000OO00OO00O0O =False #line:865
                        for O00OOOOOO0O0OOOO0 in range (12 ):#line:866
                            id =O00OO0000OOO0OO00 [O00OOOOOO0O0OOOO0 ]['level']#line:867
                            if float (OOOOOOOO0O0OOO000 )-float (id )>9 :#line:868
                                O0OO0000OO00OOOOO =f'_site={O00OOOOOO0O0OOOO0}_{timi_new()}'#line:869
                                OOO0OO000O0OOO00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0000OOO0O0OOO0O .token ,'timestamp':timi_new (),'sign':sign (O0OO0000OO00OOOOO ),'signstring':O0OO0000OO00OOOOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:880
                                O0OOOOOOOO000000O ={"site":O00OOOOOO0O0OOOO0 }#line:881
                                OO00O0OO0O00O0O0O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOO0OO000O0OOO00O ,data =O0OOOOOOOO000000O ).json ()#line:883
                                if 'status'in OO00O0OO0O00O0O0O :#line:884
                                    if OO00O0OO0O00O0O0O ['status']==200 :#line:885
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:886
                            if id !=0 :#line:887
                                for O00O00OOO0O000000 in range (11 ):#line:888
                                    OO0OO0OOO0OO0O00O =O00O00OOO0O000000 +1 #line:889
                                    g =O00OO0000OOO0OO00 [OO0OO0OOO0OO0O00O ]['level']#line:890
                                    if id ==g :#line:891
                                        O00O0OO00OOOOOO0O =O00O00OOO0O000000 +2 #line:892
                                        if O00O0OO00OOOOOO0O !=O00OOOOOO0O0OOOO0 +1 :#line:893
                                            OOOOO0OOOO0OO0OO0 =O00OOOOOO0O0OOOO0 +1 #line:894
                                            time .sleep (random .randint (1 ,3 )/10 )#line:896
                                            OO0O00000OO0O0000 =f'_site={OOOOO0OOOO0OO0OO0 - 1}&targetSite={O00O0OO00OOOOOO0O - 1}_{timi_new()}'#line:897
                                            OOOOO0OO00O00OOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO0000OOO0O0OOO0O .token ,'timestamp':timi_new (),'sign':sign (OO0O00000OO0O0000 ),'signstring':OO0O00000OO0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:914
                                            OOOOO0O0O00OO00OO ={"site":int (OOOOO0OOOO0OO0OO0 -1 ),"targetSite":int (O00O0OO00OOOOOO0O -1 )}#line:915
                                            requests .request ('post',f'{host}/game/crops/move',headers =OOOOO0OO00O00OOO0 ,json =OOOOO0O0O00OO00OO )#line:916
                                            O0O000OO00OO00O0O =True #line:918
                                    if O0O000OO00OO00O0O :#line:919
                                        break #line:920
                                if O0O000OO00OO00O0O :#line:921
                                    break #line:922
        except :#line:923
            OO0000OOO0O0OOO0O .synthetic ()#line:924
    def level_new (OO0000OOOO00O000O ):#line:927
        try :#line:928
            O0O0O0OOOOOO00O00 =f'__{timi_new()}'#line:929
            O0O000O00000O00O0 ={'source':'scsc','authorization':OO0000OOOO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OOOOOO00O00 ),'signstring':O0O0O0OOOOOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:940
            OO00OO0O000O0OO00 =requests .request ('get',f'{host}/user',headers =O0O000O00000O00O0 ).json ()#line:941
            if 'status'in OO00OO0O000O0OO00 :#line:942
                if OO00OO0O000O0OO00 ['status']==200 :#line:943
                    return float (OO00OO0O000O0OO00 ['data']['level'])#line:944
        except Exception as O0OO000OO0OO000O0 :#line:945
            print (O0OO000OO0OO000O0 )#line:946
    def propsraffle (OOOOOO00OOO0OO000 ):#line:949
        try :#line:950
            while True :#line:951
                OO0O0O0O0O0O0OOOO =f'__{timi_new()}'#line:952
                OO00O0OO0O000OO0O ={'source':'scsc','authorization':OOOOOO00OOO0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0O0O0OOOO ),'signstring':OO0O0O0O0O0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:963
                OO0O0OOOOO000000O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OO00O0OO0O000OO0O ).json ()#line:964
                if 'status'in OO0O0OOOOO000000O :#line:966
                    if OO0O0OOOOO000000O ['status']==200 :#line:967
                        O00OO0OOOOO0O0O0O =OO0O0OOOOO000000O ['data']['rows']#line:968
                        OOOOO0O0O0OOO0O00 =OO0O0OOOOO000000O ['data']['vstate']#line:969
                        if O00OO0OOOOO0O0O0O ==5 or O00OO0OOOOO0O0O0O ==6 or O00OO0OOOOO0O0O0O ==7 :#line:970
                            O000OOO00OOOOOO00 =OO0O0OOOOO000000O ['data']['silver']#line:971
                            print (f'【转盘抽奖】:获得种子:{O000OOO00OOOOOO00}')#line:972
                        if O00OO0OOOOO0O0O0O ==1 or O00OO0OOOOO0O0O0O ==2 or O00OO0OOOOO0O0O0O ==3 :#line:973
                            O0OO000O00OO000OO =OO0O0OOOOO000000O ['data']['clover']#line:974
                            print (f'【转盘抽奖】:获得三叶草:{O0OO000O00OO000OO}')#line:975
                        if O00OO0OOOOO0O0O0O ==4 or O00OO0OOOOO0O0O0O ==8 :#line:976
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:977
                        if O00OO0OOOOO0O0O0O =='抽奖次数已用完':#line:981
                            break #line:1015
                time .sleep (random .randint (8 ,15 )/10 )#line:1016
        except Exception as OO00O0OO0000000O0 :#line:1017
            print (OO00O0OO0000000O0 )#line:1018
    def friends_invitation (O000OOOOOO0000O0O ):#line:1021
        try :#line:1022
            O00O000OOO0OOO0OO =f'__{timi_new()}'#line:1023
            O00O0O00O0000000O ={'source':'scsc','authorization':O000OOOOOO0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOO0OOO0OO ),'signstring':O00O000OOO0OOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1034
            O00O00O00OO0OOOO0 =requests .request ('get',f'{host}/friends',headers =O00O0O00O0000000O ).json ()#line:1035
            if 'status'in O00O00O00OO0OOOO0 :#line:1036
                if O00O00O00OO0OOOO0 ['status']==200 :#line:1037
                    O00O0O0OOO000O0OO =O00O00O00OO0OOOO0 ['data']['myInviteter']#line:1038
                    if O00O0O0OOO000O0OO :#line:1039
                        O0OO000OO0O0OO00O =O00O0O0OOO000O0OO ['user']['nickname']#line:1040
                        OOO00OO0OO000O0OO =O000OOOOOO0000O0O .certification ()#line:1041
                        if OOO00OO0OO000O0OO =='未实名':#line:1042
                            weishim .append (O000OOOOOO0000O0O .token )#line:1043
                        print (f'【查邀请人】:我的邀请人:{O0OO000OO0O0OO00O}丨实名:{OOO00OO0OO000O0OO}')#line:1044
                    else :#line:1045
                        if O000OOOOOO0000O0O .innerId !='0':#line:1046
                            O000OOOOOO0000O0O .invitation ()#line:1047
        except Exception as O0OOO00O0OO00OOO0 :#line:1048
            print (O0OOO00O0OO00OOO0 )#line:1049
    def add_clover (O0OO0O0000O0O0000 ):#line:1052
        global golden_seed #line:1053
        try :#line:1054
            OO0O0OOOOO0OO00O0 =f'__{timi_new()}'#line:1055
            O0OO00O00O0OOO0OO ={'source':'scsc','authorization':O0OO0O0000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOO0OO00O0 ),'signstring':OO0O0OOOOO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1066
            O0O00OO00OOO000O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0OO00O00O0OOO0OO ).json ()#line:1067
            if 'status'in O0O00OO00OOO000O0 :#line:1069
                if O0O00OO00OOO000O0 ['status']==200 :#line:1070
                    OO000OO0OOOO000OO =O0O00OO00OOO000O0 ['data']['clover']#line:1071
                    O0O0O0O0OOO00O0OO =O0O00OO00OOO000O0 ['data']['used_clover']#line:1072
                    O00OOO0O0OOOO0OOO =float (OO000OO0OOOO000OO )-float (O0O0O0O0OOO00O0OO )#line:1073
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0O0O0O0OOO00O0OO}')#line:1074
                    if O0OO0O0000O0O0000 .certification ()!='未实名':#line:1075
                        if O00OOO0O0OOOO0OOO >1 :#line:1076
                            OO0O0OOOOO0OO00O0 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00OOO0O0OOOO0OOO)}_{timi_new()}'#line:1077
                            O0O0OOOO00000O0OO ={'source':'scsc','authorization':O0OO0O0000O0O0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OOOOO0OO00O0 ),'signstring':OO0O0OOOOO0OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1088
                            O0O0OO0O0O00OO0OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00OOO0O0OOOO0OOO )}#line:1089
                            OOO0000O00O0O0OO0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0O0OOOO00000O0OO ,data =O0O0OO0O0O00OO0OO ).json ()#line:1090
                            if 'status'in OOO0000O00O0O0OO0 :#line:1092
                                if OOO0000O00O0O0OO0 ['status']==200 :#line:1093
                                    print (f'【参与抽奖】:添加☘️:{OOO0000O00O0O0OO0["data"]}丨数量:{O00OOO0O0OOOO0OOO}')#line:1094
                                if OOO0000O00O0O0OO0 ['status']==500 :#line:1095
                                    print (f'【参与抽奖】:添加☘️:{OOO0000O00O0O0OO0["message"]}')#line:1096
            OOO00O000OOOOO0OO =requests .request ('get',f'{host}/lottery',headers =O0OO00O00O0OOO0OO ).json ()#line:1097
            OOOOOO0O000O0O0OO =O0OO0O0000O0O0000 .winning_rewards ()#line:1099
            if 'status'in OOO00O000OOOOO0OO :#line:1100
                if OOO00O000OOOOO0OO ['status']==200 :#line:1101
                    OOO0OO000OOOO00O0 =OOO00O000OOOOO0OO ['data'][0 ]['day_get_gold_quantity']#line:1102
                    golden_seed +=float (OOO0OO000OOOO00O0 )#line:1103
                    O0OOOO0OOO0OOO0OO =OOO00O000OOOOO0OO ['data'][1 ]['value']#line:1104
                    OOOO0O00O0OO0000O =OOO00O000OOOOO0OO ['data'][0 ]['join_number']#line:1105
                    OO00O000O0OOO00OO =int (float (OOO00O000OOOOO0OO ['data'][0 ]['totalValue']))#line:1106
                    OO0O000OO000O0O0O =float (O0OOOO0OOO0OOO0OO /OO00O000O0OOO00OO )*10000 #line:1107
                    O0O0OO00OOO0OO0OO =OO00O000O0OOO00OO /OOOO0O00O0OO0000O #line:1108
                    print (f'【参与抽奖】:预计每天中{str(OOO0OO000OOOO00O0)[:6]}颗金种子丨好友收益:{str(OOOOOO0O000O0O0OO)[:6]}')#line:1109
                    print (f'【抽奖统计】:每1万☘️中{str(OO0O000OO000O0O0O)[:6]}颗金种子丨☘️人均:{str(O0O0OO00OOO0OO0OO)[:7]}️')#line:1110
        except Exception as OOOOO0O000O00OOOO :#line:1111
            print (OOOOO0O000O00OOOO )#line:1112
    def energy (OOOOOO000OOOO0OO0 ):#line:1115
        try :#line:1116
            while True :#line:1117
                OO000O00000O00OO0 =f'__{timi_new()}'#line:1118
                O000O0OO00OOO0000 ={'source':'scsc','authorization':OOOOOO000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O00000O00OO0 ),'signstring':OO000O00000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1129
                O00O00O0OO00O0O0O =requests .request ('get',f'{host}/energy/general',headers =O000O0OO00OOO0000 ).json ()#line:1130
                if 'status'in O00O00O0OO00O0O0O :#line:1132
                    if O00O00O0OO00O0O0O ['status']==200 :#line:1133
                        O0OO0O0O0O00OO0OO =O00O00O0OO00O0O0O ['data']['ordinary_water']#line:1134
                        OO00OOO000OO0OOO0 =O00O00O0OO00O0O0O ['data']['ordinary_fertilizer']#line:1135
                        O00O00O00O00O000O =O00O00O0OO00O0O0O ['data']['videoStatus']#line:1136
                        O0OOOO0O0O0OOOOO0 =O00O00O0OO00O0O0O ['data']['waterVideoKey']#line:1137
                        print (f'【我的营养】:肥料:{str(OO00OOO000OO0OOO0).split(".")[0]}丨水滴:{str(O0OO0O0O0O00OO0OO).split(".")[0]}')#line:1139
                        if float (OO00OOO000OO0OOO0 )<96 :#line:1140
                            if O00O00O00O00O000O :#line:1141
                                time .sleep (random .randint (160 ,180 )/10 )#line:1142
                                OO0O0OO0OOOO0O00O =99 -float (OO00OOO000OO0OOO0 )#line:1143
                                O000O00OO0000OOOO ={"fertilizer":str (OO0O0OO0OOOO0O00O ).split ('.')[0 ]}#line:1144
                                OOOOO00O000O0OO0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O000O0OO00OOO0000 ).json ()#line:1146
                                if 'status'in OOOOO00O000O0OO0O :#line:1148
                                    if OOOOO00O000O0OO0O ['status']==200 :#line:1149
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO00O000O0OO0O["message"]}')#line:1150
                                    if OOOOO00O000O0OO0O ['status']==500 :#line:1151
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOO00O000O0OO0O["message"]}')#line:1152
                                        break #line:1153
                                if float (OO00OOO000OO0OOO0 )<78 :#line:1155
                                    OO0O0OO0OOOO0O00O =80 -float (OO00OOO000OO0OOO0 )#line:1156
                                    OO00O00OOOOO0O00O =f'_fertilizer={int(OO0O0OO0OOOO0O00O)}_{timi_new()}'#line:1157
                                    OO0O000O0O00000OO ={'source':'scsc','authorization':OOOOOO000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOOO0O00O ),'signstring':OO00O00OOOOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1168
                                    OO0O0O0O00O00OO0O ={"fertilizer":int (OO0O0OO0OOOO0O00O )}#line:1169
                                    OO0OO0OO0O0O0O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OO0O000O0O00000OO ,data =OO0O0O0O00O00OO0O ).json ()#line:1171
                                    if 'status'in OO0OO0OO0O0O0O000 :#line:1173
                                        if OO0OO0OO0O0O0O000 ['status']==200 :#line:1174
                                            print (f'【购买肥料】:购买肥料:{OO0OO0OO0O0O0O000["message"]}丨数量:{int(OO0O0OO0OOOO0O00O)}')#line:1175
                                        if OO0OO0OO0O0O0O000 ['status']==500 :#line:1176
                                            print (f'【购买肥料】:购买肥料:{OO0OO0OO0O0O0O000["message"]}丨数量:{int(OO0O0OO0OOOO0O00O)}')#line:1177
                                            O00OO0OO0OOO0O0OO =OO0OO0OO0O0O0O000 ["message"].split ('-')[1 ]#line:1178
                                            O00000O0OO000O0OO =f'__{timi_new()}'#line:1179
                                            O0000OO0000O0O00O ={'source':'scsc','authorization':OOOOOO000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO000O0OO ),'signstring':O00000O0OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1190
                                            O0OO0OOOO00O0O00O =requests .request ('get',f'{host}/user',headers =O0000OO0000O0O00O ).json ()#line:1191
                                            if 'status'in O0OO0OOOO00O0O00O :#line:1192
                                                if O0OO0OOOO00O0O00O ['status']==200 :#line:1193
                                                    O000O00O00000O0OO =O0OO0OOOO00O0O00O ['data']['inner_id']#line:1194
                                                    if give_gold (O000O00O00000O0OO ,float (O00OO0OO0OOO0O0OO )+1 ):#line:1195
                                                        OOOOOO000OOOO0OO0 .energy ()#line:1196
                        if float (O0OO0O0O0O00OO0OO )<880 :#line:1197
                            if O0OOOO0O0O0OOOOO0 :#line:1198
                                time .sleep (random .randint (160 ,180 )/10 )#line:1199
                                O00OO00000O0OO00O =999 -float (O0OO0O0O0O00OO0OO )#line:1200
                                O0O00O0OO000OO0OO ={"water":str (O00OO00000O0OO00O ).split ('.')[0 ]}#line:1201
                                O0000OOO00OO0O0O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O000O0OO00OOO0000 ).json ()#line:1203
                                if 'status'in O0000OOO00OO0O0O0 :#line:1205
                                    if O0000OOO00OO0O0O0 ['status']==200 :#line:1206
                                        print (f'【购买水滴】:看广告获取水滴:{O0000OOO00OO0O0O0["message"]}')#line:1207
                                    if O0000OOO00OO0O0O0 ['status']==500 :#line:1208
                                        print (f'【购买水滴】:看广告获取水滴:{O0000OOO00OO0O0O0["message"]}')#line:1209
                                        break #line:1210
                                if float (O0OO0O0O0O00OO0OO )<780 :#line:1211
                                    O00OO00000O0OO00O =800 -float (O0OO0O0O0O00OO0OO )#line:1212
                                    O00O0O0O0O0000OOO =f'_water={int(O00OO00000O0OO00O)}_{timi_new()}'#line:1213
                                    OOO00OOO00OO0OO0O ={'source':'scsc','authorization':OOOOOO000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0O0O0000OOO ),'signstring':O00O0O0O0O0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1224
                                    O0OOO00OOOOO00000 ={"water":int (O00OO00000O0OO00O )}#line:1225
                                    O0OOOO0OOOOO00000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00OOO00OO0OO0O ,data =O0OOO00OOOOO00000 ).json ()#line:1227
                                    if 'status'in O0OOOO0OOOOO00000 :#line:1229
                                        if O0OOOO0OOOOO00000 ['status']==200 :#line:1230
                                            print (f'【购买水滴】:购买水滴:{O0OOOO0OOOOO00000["message"]}丨数量:{int(O00OO00000O0OO00O)}')#line:1231
                                        if O0OOOO0OOOOO00000 ['status']==500 :#line:1232
                                            print (f'【购买水滴】:购买水滴:{O0OOOO0OOOOO00000["message"]}丨数量:{int(O00OO00000O0OO00O)}')#line:1233
                                            O00OO0OO0OOO0O0OO =O0OOOO0OOOOO00000 ["message"].split ('-')[1 ]#line:1234
                                            O00000O0OO000O0OO =f'__{timi_new()}'#line:1235
                                            O0000OO0000O0O00O ={'source':'scsc','authorization':OOOOOO000OOOO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0OO000O0OO ),'signstring':O00000O0OO000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1246
                                            O0OO0OOOO00O0O00O =requests .request ('get',f'{host}/user',headers =O0000OO0000O0O00O ).json ()#line:1247
                                            if 'status'in O0OO0OOOO00O0O00O :#line:1248
                                                if O0OO0OOOO00O0O00O ['status']==200 :#line:1249
                                                    O000O00O00000O0OO =O0OO0OOOO00O0O00O ['data']['inner_id']#line:1250
                                                    if give_gold (O000O00O00000O0OO ,float (O00OO0OO0OOO0O0OO )+1 ):#line:1251
                                                        OOOOOO000OOOO0OO0 .energy ()#line:1252
                        break #line:1253
        except Exception as OO0OOOOO0O0O0000O :#line:1254
            print (OO0OOOOO0O0O0000O )#line:1255
def bundled_def ():#line:1258
    O00OOOOOOOO00OOOO =['5570536','7750212','7911652','7911680','7805624']#line:1259
    return O00OOOOOOOO00OOOO [random .randint (0 ,len (O00OOOOOOOO00OOOO )-1 )]#line:1260
def version_of_the_validation ():#line:1264
    return str ((96 -56 )/10 )#line:1265
def ubbbf ():#line:1267
    print ('卡密验证通过   ✅')#line:1268
def sc2 ():#line:1271
    return "19319#$%^&*((*"#line:1272
def OO00OO0OO0OO00OO00o0 ():#line:1275
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1277
def get_ip ():#line:1280
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1282
def gitee_validation ():#line:1285
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1286
def gitee_edition ():#line:1289
    try :#line:1290
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1291
    except :#line:1292
        sys .exit (0 )#line:1293
def O000OO000O0O00OOO00 ():#line:1297
    try :#line:1298
        OO0O0OOO0O00OOOO0 =gitee_edition ()#line:1299
        if version_of_the_validation ()<OO0O0OOO0O00OOOO0 ['CityEarth']['edition']:#line:1300
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0O00OOOO0["CityEarth"]["edition"]}   ❌')#line:1301
            print (f'更新内容=>>{OO0O0OOO0O00OOOO0["CityEarth"]["content"]}')#line:1302
        else :#line:1303
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0OOO0O00OOOO0["CityEarth"]["edition"]}   ✅')#line:1304
            print (f'更新内容=>> {OO0O0OOO0O00OOOO0["CityEarth"]["content"]}')#line:1305
    except Exception as O000OOOO00OO0OOOO :#line:1306
        print (O000OOOO00OO0OOOO )#line:1307
def sc3 ():#line:1310
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1311
if __name__ =='__main__':#line:1314
    start ()#line:1315
