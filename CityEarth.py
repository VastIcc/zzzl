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
@ 版本  3.7
"""
##################################配置区##################################
time_xx = random.randint(15, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
eeeeee = False                    # 打印没有俩个二级好友的ID
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
msg_list =[]#line:5
invited_new =[]#line:6
def start ():#line:7
    try :#line:8
        O000OO000O0O00OOO00 ()#line:9
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:10
        O000OO0O00OO00O00 ()#line:11
        O0O000O0OO0O0O0O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O0O000O0OO0O0O0O0)}个账号==========")#line:13
        for O0OOOO0000OO00O00 in O0O000O0OO0O0O0O0 :#line:14
            OOO0O000OOOOOO00O =[]#line:15
            print (f"------------正在执行第{O0O000O0OO0O0O0O0.index(O0OOOO0000OO00O00) + 1}个账号------------")#line:16
            OO0O00O00OO0OOOOO =CityEarth (O0OOOO0000OO00O00 ,OOO0O000OOOOOO00O ,O0O000O0OO0O0O0O0 .index (O0OOOO0000OO00O00 ))#line:17
            def OOOO0O00OOOO0OOO0 ():#line:19
                if OO0O00O00OO0OOOOO .base_info ():#line:21
                    OO0O00O00OO0OOOOO .sealing ()#line:23
                    OO0O00O00OO0OOOOO .invitenum ()#line:25
                    OO0O00O00OO0OOOOO .query_to_sell ()#line:27
                    OO0O00O00OO0OOOOO .game_map ()#line:29
                    OO0O00O00OO0OOOOO .friends_invitation ()#line:31
                    OO0O00O00OO0OOOOO .energy ()#line:33
                    OO0O00O00OO0OOOOO .add_clover ()#line:35
                    OO0O00O00OO0OOOOO .propsraffle ()#line:37
                    OO0O00O00OO0OOOOO .synthetic ()#line:39
                    OO0O00O00OO0OOOOO .crops_illustrated ()#line:41
                    OO0O00O00OO0OOOOO .withdraw ()#line:43
                    if float (datetime .datetime .now ().hour )>8 :#line:44
                        OO0O00O00OO0OOOOO .give_gold ()#line:46
            OOO000OO000OOO0O0 =threading .Thread (target =OOOO0O00OOOO0OOO0 )#line:47
            OOO000OO000OOO0O0 .start ()#line:48
            time .sleep (time_xx )#line:49
        print (f"------------正在处理推送通知------------")#line:50
        time .sleep (0.5 )#line:51
        O000O000O0000OO00 =format_msg ()#line:52
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O000O0000OO00 +' ')#line:53
        if eeeeee :#line:54
            time .sleep (100 )#line:55
            print ('开始打印好友数量不足2的ID')#line:56
            print (invited_new )#line:57
    except Exception as O0OO00O0O00OO00OO :#line:58
        print (O0OO00O0O00OO00OO )#line:59
def give_gold (OO00OO00OOOO0OO00 ,OOO0OO0000O00OOO0 ):#line:62
        try :#line:63
            OO00O0O0OOO0O0O0O =f'_doneeNo={OO00OO00OOOO0OO00}&quantity={int(OOO0OO0000O00OOO0)}_{timi_new()}'#line:64
            O0OOOOO0O0O0O0000 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OO00O0O0OOO0O0O0O ),'signstring':OO00O0O0OOO0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:75
            O00OOOOO000O0O000 ={"quantity":int (OOO0OO0000O00OOO0 ),"doneeNo":OO00OO00OOOO0OO00 }#line:79
            OOOOOOOOOO0O0O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0OOOOO0O0O0O0000 ,data =O00OOOOO000O0O000 ).json ()#line:80
            if 'status'in OOOOOOOOOO0O0O0OO :#line:82
                if OOOOOOOOOO0O0O0OO ['status']==200 :#line:83
                    if OOOOOOOOOO0O0O0OO ['data']:#line:84
                        print (f'【赠送种子】:赠送{int(OOO0OO0000O00OOO0)}种子给{OO00OO00OOOO0OO00}成功')#line:85
                        return True #line:86
                if OOOOOOOOOO0O0O0OO ['status']==401 :#line:87
                    print (f'【赠送种子】:{OOOOOOOOOO0O0O0OO["message"]}')#line:88
                    return False #line:89
                if OOOOOOOOOO0O0O0OO ['status']==500 :#line:90
                    print (f'【赠送种子】:{OOOOOOOOOO0O0O0OO["message"]}')#line:91
                    return False #line:92
            return False #line:93
        except Exception as O0O0O000O00O000OO :#line:94
            print (O0O0O000O00O000OO )#line:95
def kvkv ():#line:96
    return '/vastzzzl/vastzzzl/raw/master'#line:97
def sign (O0000O0O0O00000O0 ):#line:100
    OOO0OOOO00O00OOO0 =hashlib .md5 (O0000O0O0O00000O0 .encode ()).hexdigest ()#line:101
    OO0000OO000O000O0 =sc1 ()#line:102
    OOOO000000O00OO00 =sc2 ()#line:103
    OOOO000O0O0OOO0O0 =sc3 ()#line:104
    O0OO00OOOOOO0O0O0 =OO0000OO000O000O0 +OOO0OOOO00O00OOO0 +OOOO000000O00OO00 +OOOO000O0O0OOO0O0 #line:105
    OOOO0O0O0OO0O00O0 =hashlib .md5 (O0OO00OOOOOO0O0O0 .encode ()).hexdigest ()#line:106
    return OOOO0O0O0OO0O00O0 #line:107
def format_msg ():#line:111
    O00O0OO00OO0OOO00 =""#line:112
    for OOOO000O00000OOOO in msg_list :#line:113
        O00O0OO00OO0OOO00 +=str (OOOO000O00000OOOO )+"\r\n"#line:114
    return O00O0OO00OO0OOO00 #line:115
def sc1 ():#line:117
    return "scsc%^&*"#line:118
def O000OO0O00OO00O00 ():#line:120
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:121
        pass #line:122
    else :#line:123
        exit (1 )#line:124
def timi_new ():#line:126
    return str (int (time .time ()*1000 ))#line:127
json_path ="CityEarth_data.json"#line:130
json_path1 ="CityEarth_data.json"#line:131
dict ={}#line:132
def get_json_data (O0OO0O0OO0OO0000O ,OOOOO00OO00OO00OO ,OOO0000OO0O0OO0O0 ,O0O000O0O00O00000 ):#line:134
    with open (O0OO0O0OO0OO0000O ,'rb')as OO0O0000OO0000000 :#line:136
        OOO0O000O0OOOOO0O =json .load (OO0O0000OO0000000 )#line:137
        OOO0O000O0OOOOO0O ['data'][OOOOO00OO00OO00OO ][OOO0000OO0O0OO0O0 ]=O0O000O0O00O00000 #line:138
        OO00O000O0O0OOO0O =OOO0O000O0OOOOO0O #line:139
    OO0O0000OO0000000 .close ()#line:140
    return OO00O000O0O0OOO0O #line:141
def write_json_data (OOO00O00O0000OOO0 ):#line:143
    with open (json_path1 ,'w')as OOOO0OOOOO000OOOO :#line:144
        json .dump (OOO00O00O0000OOO0 ,OOOO0OOOOO000OOOO )#line:145
    OOOO0OOOOO000OOOO .close ()#line:146
    return True #line:147
class CityEarth :#line:149
    def __init__ (OO0OO00OO0OO0O000 ,O00O0000O0O0OO00O ,OO0000OOO0000O00O ,O0O000O0O00O0O000 ):#line:151
        try :#line:152
            OO0OO00OO0OO0O000 .msg =OO0000OOO0000O00O #line:153
            OO0OO00OO0OO0O000 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:154
            OO0OO00OO0OO0O000 .token =O00O0000O0O0OO00O ['authorization']#line:155
            OO0OO00OO0OO0O000 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:156
            OO0OO00OO0OO0O000 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:157
            OO0OO00OO0OO0O000 .elephant_user =O00O0000O0O0OO00O ['elephant_user']#line:158
            OO0OO00OO0OO0O000 .elephant_pswd =O00O0000O0O0OO00O ['elephant_pswd']#line:159
            OO0OO00OO0OO0O000 .elephant_Task_ID =O00O0000O0O0OO00O ['elephant_Task_ID']#line:160
            OO0OO00OO0OO0O000 .len_new =O0O000O0O00O0O000 #line:161
        except :#line:162
            print ('变量格式错误')#line:163
    def base_info (O0O0O0000OO00OO0O ):#line:166
        try :#line:167
            O0O0O0000OO00OO0O .watched_ad ()#line:169
            O00O00O0OO00OOO0O =f'__{timi_new()}'#line:170
            OO00O0OOO000O0000 ={'source':'scsc','authorization':O0O0O0000OO00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO00OOO0O ),'signstring':O00O00O0OO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:181
            O0OO000OO0O0O000O =requests .request ('get',f'{host}/user',headers =OO00O0OOO000O0000 ).json ()#line:182
            if 'status'in O0OO000OO0O0O000O :#line:184
                if O0OO000OO0O0O000O ['status']==200 :#line:185
                    O0O000OO00000OO00 =O0OO000OO0O0O000O ['data']['nickname']#line:186
                    OOOO00O0000O0OOO0 =O0OO000OO0O0O000O ['data']['inner_id']#line:187
                    OOOO0OOOO0O0O0O00 =O0OO000OO0O0O000O ['data']['assets']['gold']#line:188
                    O00O0O00000O00000 =O0OO000OO0O0O000O ['data']['level']#line:189
                    print (f'【账号信息】:昵称:{O0O000OO00000OO00[:5]}丨ID:{OOOO00O0000O0OOO0}丨等级:{O00O0O00000O00000}丨金种子:{str(OOOO0OOOO0O0O0O00).split(".")[0]}')#line:190
                    if 'wx_'in O0O000OO00000OO00 :#line:191
                        O0O0O0000OO00OO0O .change_nickname ()#line:192
                if O0OO000OO0O0O000O ['status']==401 :#line:193
                    print ('【账号信息】:账号失效正在尝试登录')#line:194
                    if O0O0O0000OO00OO0O .elephant_user =='f':#line:195
                        return False #line:196
                    OOO0O0O0O000O000O =Invalid_login .addtask (elephant_user =O0O0O0000OO00OO0O .elephant_user ,elephant_pswd =O0O0O0000OO00OO0O .elephant_pswd ,elephant_Task_ID =O0O0O0000OO00OO0O .elephant_Task_ID )#line:197
                    OOO00OOOOOO000O00 =get_json_data (json_path ,O0O0O0000OO00OO0O .len_new ,'authorization',OOO0O0O0O000O000O )#line:198
                    if write_json_data (OOO00OOOOOO000O00 ):#line:199
                        print ('正在写入账号配置文件')#line:200
                    return False #line:201
                if O0OO000OO0O0O000O ['status']==500 :#line:202
                    return False #line:203
            return True #line:204
        except Exception as OO00000OOOO00O000 :#line:205
            print (OO00000OOOO00O000 )#line:206
    def sealing (OOO0O00OO00OOOO00 ):#line:209
        try :#line:210
            OO0OO0O0OO0OO0O0O =f'__{timi_new()}'#line:211
            O0O0O000OO00OOOO0 ={'source':'scsc','authorization':OOO0O00OO00OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO0OO0O0O ),'signstring':OO0OO0O0OO0OO0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0O000OO00OOOO0 )#line:223
            requests .request ('get',f'{host}/packsack/list',headers =O0O0O000OO00OOOO0 )#line:224
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0O000OO00OOOO0 )#line:225
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0O000OO00OOOO0 )#line:226
            requests .request ('get',f'{host}/user',headers =O0O0O000OO00OOOO0 )#line:227
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0O000OO00OOOO0 )#line:228
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0O000OO00OOOO0 )#line:229
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0O000OO00OOOO0 )#line:230
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0O000OO00OOOO0 )#line:231
            requests .request ('get',f'{host}/assets',headers =O0O0O000OO00OOOO0 )#line:232
        except Exception as O00OO0O00000O0OO0 :#line:233
            print (O00OO0O00000O0OO0 )#line:234
    def the_query (O0O0O000OOO00O0OO ):#line:237
        try :#line:238
            O00O0OO0OO00O0O0O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:239
            OO00000OO00OOO0O0 ={'authorization':O0O0O000OOO00O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO0OO00O0O0O ),'signstring':O00O0OO0OO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            OO0000O0OO0000OO0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO00000OO00OOO0O0 ).json ()#line:250
            if 'status'in OO0000O0OO0000OO0 :#line:252
                if OO0000O0OO0000OO0 ['status']==200 :#line:253
                    O00O00O0OOOO00O00 =OO0000O0OO0000OO0 ['data']['rows'][3 ]['price']#line:254
                    O0O0O000OOO00O0OO .market_sale (O00O00O0OOOO00O00 )#line:255
        except Exception as OO0O0O0O0000OOO00 :#line:256
            print (OO0O0O0O0000OOO00 )#line:257
    def market_sale (OOO000OOO0OOO0OOO ,O00O00O00OOO00O0O ):#line:260
        try :#line:261
            O0O0O0OOOO0O000OO =timi_new ()#line:262
            O00O0OO0O0O0OOO00 =f'type=crop__{O0O0O0OOOO0O000OO}'#line:263
            OOOO00OO0O0O0O0OO ={'source':'scsc','authorization':OOO000OOO0OOO0OOO .token ,'timestamp':str (O0O0O0OOOO0O000OO ),'sign':sign (O00O0OO0O0O0OOO00 ),'signstring':O00O0OO0O0O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            O0O0O0O00O0O0O00O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOO00OO0O0O0O0OO ).json ()#line:275
            if 'status'in O0O0O0O00O0O0O00O :#line:277
                if O0O0O0O00O0O0O00O ['status']==200 :#line:278
                    if O0O0O0O00O0O0O00O ['data']['rows']:#line:279
                        O000O0OO00OOO0OO0 =O0O0O0O00O0O0O00O ['data']['rows'][0 ]['packsackItemId']#line:280
                        OOO0O0OOOOO000OO0 =O0O0O0O00O0O0O00O ['data']['rows'][0 ]['quantity']#line:281
                        OOOO0OOO0O000OO0O =float (O00O00O00OOO00O0O )+0.001 #line:282
                        OOO0000OOO00O0OOO =f'_packsackItemId={O000O0OO00OOO0OO0}&price={str(OOOO0OOO0O000OO0O)[:6]}&quantity={OOO0O0OOOOO000OO0}_{O0O0O0OOOO0O000OO}'#line:283
                        O0O0O00OO0000OO0O ={'source':'scsc','authorization':OOO000OOO0OOO0OOO .token ,'timestamp':str (O0O0O0OOOO0O000OO ),'sign':sign (OOO0000OOO00O0OOO ),'signstring':OOO0000OOO00O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
                        OO0O0O0OOOOOOOO0O ={"packsackItemId":O000O0OO00OOO0OO0 ,"price":str (OOOO0OOO0O000OO0O )[:6 ],"quantity":str (OOO0O0OOOOO000OO0 )}#line:299
                        OOOO0O0O00O000OO0 =requests .request ('post',f'{host}/market/sale',headers =O0O0O00OO0000OO0O ,data =OO0O0O0OOOOOOOO0O ).json ()#line:300
                        if 'status'in OOOO0O0O00O000OO0 :#line:302
                            if OOOO0O0O00O000OO0 ['status']==200 :#line:303
                                print (f'【上架芦荟】:数量:{OOO0O0OOOOO000OO0}丨价格:{str(OOOO0OOO0O000OO0O)[:6]}')#line:304
        except Exception as OOOO0OO0OO0O0OOOO :#line:305
            print (OOOO0OO0OO0O0OOOO )#line:306
    def query_to_sell (O0OOO00O0O000O0OO ):#line:309
        try :#line:310
            O000OO000O00O0O0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:311
            OO0OO0O00OO0OO0O0 ={'source':'scsc','authorization':O0OOO00O0O000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000OO000O00O0O0O ),'signstring':O000OO000O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:322
            O000000000OOO0O00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0OO0O00OO0OO0O0 ).json ()#line:324
            if 'status'in O000000000OOO0O00 :#line:326
                if O000000000OOO0O00 ['status']==200 :#line:327
                    for O0O0O0OOO0O000O00 in O000000000OOO0O00 ['data']['rows']:#line:328
                        O0OO000OOOO0O00O0 =O0O0O0OOO0O000O00 ['materialKey']#line:329
                        OOOO0O0OOO0000OO0 =O0O0O0OOO0O000O00 ['quantity']#line:330
                        OO0OOO0O0OOO00O00 =O0O0O0OOO0O000O00 ['price']#line:331
                        O0O0O00O0OOO000OO =O0O0O0OOO0O000O00 ['saleState']#line:332
                        if O0O0O00O0OOO000OO ==0 :#line:333
                            print (f'【出售订单】:名称:{O0OO000OOOO0O00O0}丨数量:{OOOO0O0OOO0000OO0}丨价格:{OO0OOO0O0OOO00O00}')#line:334
                            OOOO0OO000O0OO000 =O0O0O0OOO0O000O00 ['id']#line:335
                            O0OOO00O0O000O0OO .cacel_sale (OOOO0OO000O0OO000 )#line:336
        except Exception as O000OOO0O00OOOO00 :#line:337
            print (O000OOO0O00OOOO00 )#line:338
    def cacel_sale (OOO00O000OOO0OO00 ,OOO0OO0OOO00OOO00 ):#line:342
        try :#line:343
            OO00OO0O00OO0O000 =f'_saleId={OOO0OO0OOO00OOO00}_{timi_new()}'#line:344
            OO0OOO0000O00O0OO ={'source':'scsc','authorization':OOO00O000OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OO0O00OO0O000 ),'signstring':OO00OO0O00OO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:355
            O0O00O00O0OO0OO00 ={"saleId":OOO0OO0OOO00OOO00 }#line:358
            OOOO000O0O0O000OO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO0OOO0000O00O0OO ,data =O0O00O00O0OO0OO00 ).json ()#line:359
            if 'status'in OOOO000O0O0O000OO :#line:361
                if OOOO000O0O0O000OO ['status']==200 :#line:362
                    print (f'【下架出售】:{OOOO000O0O0O000OO["data"]}')#line:363
        except Exception as O0OOO00OO0O0OO0O0 :#line:364
            print (O0OOO00OO0O0OO0O0 )#line:365
    def change_nickname (OO00OO0OOOOO0O00O ):#line:372
        try :#line:373
            OOO0OOOO0OOO0O00O =timi_new ()#line:374
            OOO0OO0O000OOOO00 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:375
            O0OO0OO000OO00000 =requests .request ('post','https://www.qmsjmfb.com/',data =OOO0OO0O000OOOO00 ).text #line:376
            OOOO0OOOO0OO0OO0O =re .findall ('<ul><li>(.*?)</li>',O0OO0OO000OO00000 )[0 ][:3 ]#line:377
            O000O0O000O00OOO0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOOO0OOOO0OO0OO0O}').json ()#line:378
            OO0O0OOO0OOO000O0 =O000O0O000O00OOO0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:379
            OO0O0000O0O00O0O0 ={"nickname":OO0O0OOO0OOO000O0 }#line:380
            OO00OO00OOO000O0O =f'_nickname={OO0O0OOO0OOO000O0}_{OOO0OOOO0OOO0O00O}'#line:381
            OO0OO0O0OO0OOOOOO ={'source':'scsc','authorization':OO00OO0OOOOO0O00O .token ,'timestamp':OOO0OOOO0OOO0O00O ,'sign':sign (OO00OO00OOO000O0O ),'signstring':OO00OO00OOO000O0O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:392
            OOOOOOO0OO0OOOO00 =requests .request ('patch',f'{host}/user/nickname',headers =OO0OO0O0OO0OOOOOO ,data =OO0O0000O0O00O0O0 ).json ()#line:393
            if 'status'in OOOOOOO0OO0OOOO00 :#line:395
                if OOOOOOO0OO0OOOO00 ['status']==200 :#line:396
                    print (f'【修改网名】:网名:{OO0O0OOO0OOO000O0}丨{OOOOOOO0OO0OOOO00["message"]}')#line:397
        except Exception as OO0O0O0OO0000OO00 :#line:398
            print (OO0O0O0OO0000OO00 )#line:399
    def withdraw (O0OOO000OOOO0OO00 ):#line:404
        try :#line:405
            OO0OOO000OO0O0OOO =f'__{timi_new()}'#line:406
            O0O0OO0OO00OOOOOO ={'source':'scsc','authorization':O0OOO000OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000OO0O0OOO ),'signstring':OO0OOO000OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            O00000O0O0O000OO0 =requests .request ('get',f'{host}/assets',headers =O0O0OO0OO00OOOOOO ).json ()#line:418
            if 'status'in O00000O0O0O000OO0 :#line:420
                if O00000O0O0O000OO0 ['status']==200 :#line:421
                    O00OO0O0OO000OO0O =O00000O0O0O000OO0 ['data']['cash']#line:422
                    if float (O00OO0O0OO000OO0O )>20 :#line:423
                        OO0OOO000OO0O0OOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:424
                        O0O0OO0OO00OOOOOO ={'authorization':O0OOO000OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO000OO0O0OOO ),'signstring':OO0OOO000OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:434
                        O0OO00OO0OOOO00O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:435
                        O00O0OOOO0O0000O0 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0O0OO0OO00OOOOOO ,data =O0OO00OO0OOOO00O0 ).json ()#line:436
                        if 'status'in O00O0OOOO0O0000O0 :#line:438
                            if O00O0OOOO0O0000O0 ['status']==200 :#line:439
                                print (f'【余额提现】:{O00O0OOOO0O0000O0["data"]}')#line:440
                        if 'status'in O00O0OOOO0O0000O0 :#line:441
                            if O00O0OOOO0O0000O0 ['status']==500 :#line:442
                                print (f'【余额提现】:{O00O0OOOO0O0000O0["message"]}')#line:443
        except Exception as OO00000O0OOO0OOO0 :#line:444
            print (OO00000O0OOO0OOO0 )#line:445
    def invitenum (OO0O00OO00000O0OO ):#line:449
        global invited_new #line:450
        try :#line:451
            O00O0O000O0O00000 =f'__{timi_new()}'#line:452
            O00O00O0OO0OO0O0O ={'source':'scsc','authorization':OO0O00OO00000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000O0O00000 ),'signstring':O00O0O000O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O00OO00O0OOOOO0OO =requests .request ('get',f'{host}/invite/invitenum',headers =O00O00O0OO0OO0O0O ).json ()#line:464
            if 'status'in O00OO00O0OOOOO0OO :#line:466
                if O00OO00O0OOOOO0OO ['status']==200 :#line:467
                    OOOOOOO00000OOOOO =O00OO00O0OOOOO0OO ['data']['invited_count']#line:468
                    O000OOO0O0O00OOO0 =O00OO00O0OOOOO0OO ['data']['invited_second_count']#line:469
                    print (f'【我的邀请】:直邀好友:{OOOOOOO00000OOOOO}丨间邀好友:{O000OOO0O0O00OOO0}')#line:470
                    if OOOOOOO00000OOOOO <2 :#line:471
                        O00OO0OO0000O0OOO =f'__{timi_new()}'#line:472
                        O0O0OO00OOO0O0OO0 ={'source':'scsc','authorization':OO0O00OO00000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OO0000O0OOO ),'signstring':O00OO0OO0000O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        O0O000O0O0OOOOOOO =requests .request ('get',f'{host}/user',headers =O0O0OO00OOO0O0OO0 ).json ()#line:484
                        if 'status'in O0O000O0O0OOOOOOO :#line:486
                            if O0O000O0O0OOOOOOO ['status']==200 :#line:487
                                invited_new .append (O0O000O0O0OOOOOOO ['data']['inner_id'])#line:488
        except Exception as OOOO00O00O00O0O0O :#line:489
            print (OOOO00O00O00O0O0O )#line:490
    def game_map (OOOO0000OOOO0O0O0 ):#line:494
        try :#line:495
            O00OO0OOOOOO00O00 =f'__{timi_new()}'#line:496
            O0000O00OOOOO00O0 ={'source':'scsc','authorization':OOOO0000OOOO0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO0OOOOOO00O00 ),'signstring':O00OO0OOOOOO00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            O0000OOOO0OO000OO =requests .request ('get',f'{host}/game/map',headers =O0000O00OOOOO00O0 ).json ()#line:508
            if 'status'in O0000OOOO0OO000OO :#line:510
                if O0000OOOO0OO000OO ['status']==200 :#line:511
                    for O0O0O00OO0O0OOOO0 in O0000OOOO0OO000OO ['data']['list'][0 ]['crops']:#line:512
                        O00OOOO00O00O0O00 =O0O0O00OO0O0OOOO0 ['level']#line:514
                        if O00OOOO00O00O0O00 ==41 :#line:515
                            O0O00000OO00000O0 =O0O0O00OO0O0OOOO0 ['crop_name']#line:516
                            O000OO0O0OO00O0OO =O0O0O00OO0O0OOOO0 ['count']#line:517
                            if O000OO0O0OO00O0OO >0 :#line:518
                                print (f'【农业资产】:{O0O00000OO00000O0}丨数量:{O000OO0O0OO00O0OO}')#line:519
                                OOOO0000OOOO0O0O0 .the_query ()#line:520
        except Exception as OO0O00OO0O00OO000 :#line:521
            print (OO0O00OO0O00OO000 )#line:522
    def give_gold (O000O0O0OOO00O0O0 ):#line:525
        try :#line:526
            OOOOOO0000O0OOOOO =f'__{timi_new()}'#line:527
            O00000OOOO0O0O0OO ={'source':'scsc','authorization':O000O0O0OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000O0OOOOO ),'signstring':OOOOOO0000O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            OOO0OO0000OOOO0OO =requests .request ('get',f'{host}/user',headers =O00000OOOO0O0O0OO ).json ()#line:539
            if 'status'in OOO0OO0000OOOO0OO :#line:540
                if OOO0OO0000OOOO0OO ['status']==200 :#line:541
                    if float (O000O0O0OOO00O0O0 .doneeNo )!=0 :#line:542
                        O00OOOOOO0OOOOOOO =OOO0OO0000OOOO0OO ['data']['assets']['gold']#line:543
                        if float (O00OOOOOO0OOOOOOO )>float (O000O0O0OOO00O0O0 .innerId ):#line:544
                            OOO00OOO0O0OOO000 =int (float (O00OOOOOO0OOOOOOO )/1.1 )#line:545
                            OOOOOO0000O0OOOOO =f'_doneeNo={O000O0O0OOO00O0O0.doneeNo}&quantity={OOO00OOO0O0OOO000}_{timi_new()}'#line:546
                            O00000OOOO0O0O0OO ={'source':'scsc','authorization':O000O0O0OOO00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO0000O0OOOOO ),'signstring':OOOOOO0000O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
                            O00O0OO0OOO000OOO ={"quantity":OOO00OOO0O0OOO000 ,"doneeNo":O000O0O0OOO00O0O0 .doneeNo }#line:561
                            OOO0OO00OO0O0O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O00000OOOO0O0O0OO ,data =O00O0OO0OOO000OOO ).json ()#line:562
                            if 'status'in OOO0OO00OO0O0O0OO :#line:564
                                if OOO0OO00OO0O0O0OO ['status']==200 :#line:565
                                    if OOO0OO00OO0O0O0OO ['data']:#line:566
                                        print (f'【赠送种子】:赠送{OOO00OOO0O0OOO000}种子给{O000O0O0OOO00O0O0.doneeNo}成功')#line:567
                    else :#line:568
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:569
        except Exception as O0OO0OOOO0000OOO0 :#line:570
            print (O0OO0OOOO0000OOO0 )#line:571
    def invitation (O00OOO00O0OOO00OO ):#line:573
        try :#line:574
            _OO000O000000O00O0 =float (bundled_def ())/4 #line:575
            O0O0O00OO0OOO0OOO =f'_innerId={int(_OO000O000000O00O0)}_{timi_new()}'#line:576
            OO0OO0O0OO000O0OO ={'source':'scsc','authorization':O00OOO00O0OOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O00OO0OOO0OOO ),'signstring':O0O0O00OO0OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            OO00OO0OOO0OO0O0O ={"innerId":int (_OO000O000000O00O0 )}#line:588
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OO0O0OO000O0OO ,data =OO00OO0OOO0OO0O0O )#line:589
        except Exception as O0OOOOOO0OOOOOO0O :#line:590
            print (O0OOOOOO0OOOOOO0O )#line:591
    def winning_rewards (OOOO0OO0OO00OOOO0 ):#line:594
        try :#line:595
            OOO000O0O00OOO000 =f'__{timi_new()}'#line:596
            OO0O00OO0O0OOO00O ={'source':'scsc','authorization':OOOO0OO0OO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O00OOO000 ),'signstring':OOO000O0O00OOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
            O0O0OOO00000OO0OO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0O00OO0O0OOO00O ).json ()#line:608
            if 'status'in O0O0OOO00000OO0OO :#line:610
                if O0O0OOO00000OO0OO ['status']==200 :#line:611
                    if O0O0OOO00000OO0OO ['data']['amount']:#line:612
                        OO0O000O0000OO0O0 =O0O0OOO00000OO0OO ['data']['amount']['gold']#line:613
                        return OO0O000O0000OO0O0 #line:614
                    else :#line:615
                        return 0 #line:616
        except Exception as O0O00O00O0OOOOO00 :#line:617
            print (O0O00O00O0OOOOO00 )#line:618
    def certification (O00OOOOOOOOO0OO00 ):#line:621
        try :#line:622
            O0O0OOOOOOOO0O0OO =f'__{timi_new()}'#line:623
            OOO0000000OOOOO00 ={'source':'scsc','authorization':O00OOOOOOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOOOOOOO0O0OO ),'signstring':O0O0OOOOOOOO0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            O000OOO0O0O0O00O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0000000OOOOO00 ).json ()#line:635
            if 'status'in O000OOO0O0O0O00O0 :#line:637
                if O000OOO0O0O0O00O0 ['status']==200 :#line:638
                    if O000OOO0O0O0O00O0 ['data']['result']:#line:639
                        O0000O00OOOO0O0O0 =O000OOO0O0O0O00O0 ['data']['nick_name']#line:640
                        return O0000O00OOOO0O0O0 #line:641
                    else :#line:642
                        return '未实名'#line:643
        except Exception as O0OO000000O0OOOO0 :#line:644
            print (O0OO000000O0OOOO0 )#line:645
    def crops_illustrated (OO0O0O0O0OO0O0OOO ):#line:648
        try :#line:649
            O0O0O000O00O0000O =f'__{timi_new()}'#line:650
            O000OO0O00O000000 ={'source':'scsc','authorization':OO0O0O0O0OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00O0000O ),'signstring':O0O0O000O00O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:661
            OOO0O00000O0OO0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O000OO0O00O000000 ).json ()#line:662
            if 'status'in OOO0O00000O0OO0O0 :#line:664
                if OOO0O00000O0OO0O0 ['status']==200 :#line:665
                    OO00000O0OO00OOOO =OOO0O00000O0OO0O0 ['data'][0 ]['crops']#line:666
                    for OO000OO0OOO00OO00 in OO00000O0OO00OOOO :#line:667
                        if OO000OO0OOO00OO00 ['ill_clover_award']:#line:668
                            if float (OO000OO0OOO00OO00 ['ill_clover_award'])>1 :#line:669
                                if OO000OO0OOO00OO00 ['is_finish']:#line:670
                                    if not OO000OO0OOO00OO00 ['is_getit']:#line:671
                                        if OO0O0O0O0OO0O0OOO .certification ()!='未实名':#line:672
                                            O0O0O000O00O0000O =f'_award_level={OO000OO0OOO00OO00["level"]}_{timi_new()}'#line:673
                                            O000OO0O00O000000 ={'source':'scsc','authorization':OO0O0O0O0OO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O000O00O0000O ),'signstring':O0O0O000O00O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
                                            OOOO0OO000OO0O000 ={"award_level":OO000OO0OOO00OO00 ['level']}#line:685
                                            OOOOOOO0OO0O0000O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O000OO0O00O000000 ,json =OOOO0OO000OO0O000 ).json ()#line:687
                                            if 'status'in OOOOOOO0OO0O0000O :#line:688
                                                if OOOOOOO0OO0O0000O ['status']==200 :#line:689
                                                    OOOO0000000OOOOOO =OOOOOOO0OO0O0000O ['data']['ill_clover_award']#line:690
                                                    print (f'【图鉴奖励】:领取{OO000OO0OOO00OO00["crop_name"]}成就丨奖励{OOOO0000000OOOOOO}☘️')#line:692
                                                if OOOOOOO0OO0O0000O ['status']==500 :#line:693
                                                    print (f'【图鉴奖励】:{OOOOOOO0OO0O0000O["message"]}')#line:694
        except Exception as OO00O0O0OOOO00O00 :#line:695
            print (OO00O0O0OOOO00O00 )#line:696
    def watched_ad (OOO0OOO0OOO000O00 ):#line:699
        try :#line:700
            O0OOO0O0OOO0OOO0O =f'__{timi_new()}'#line:701
            O0OO0000O0O0OOOOO ={'source':'scsc','authorization':OOO0OOO0OOO000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0OOO0OOO0O ),'signstring':O0OOO0O0OOO0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:712
            OOOOOOOO0O0O0O0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0000O0O0OOOOO ).json ()#line:713
            if 'status'in OOOOOOOO0O0O0O0OO :#line:715
                if OOOOOOOO0O0O0O0OO ['status']==200 :#line:716
                    if 'offlineInfo'in OOOOOOOO0O0O0O0OO ['data']:#line:717
                        time .sleep (random .randint (1 ,3 ))#line:718
                        O00O0000O0OO00O0O =OOOOOOOO0O0O0O0OO ['data']['offlineInfo']['off_minute']#line:719
                        O000O0OOOOOO0O00O =float (OOOOOOOO0O0O0O0OO ['data']['silver'])/1000000000000 #line:720
                        time .sleep (1 )#line:721
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OO0000O0O0OOOOO ).json ()#line:722
                        time .sleep (2 )#line:723
                        O00OO0O00OO0OO000 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0000O0O0OOOOO ).json ()#line:724
                        if 'status'in O00OO0O00OO0OO000 :#line:726
                            if O00OO0O00OO0OO000 ['status']==200 :#line:727
                                O0O00O00O0OOO0O00 =float (O00OO0O00OO0OO000 ['data']['silver'])/1000000000000 #line:728
                                OO00O00OO0O00000O =str (O0O00O00O0OOO0O00 -O000O0OOOOOO0O00O )[:6 ]#line:729
                                print (f'【离线奖励】:翻倍离线{O00O0000O0OO00O0O}分钟奖励🌱数量:{OO00O00OO0O00000O}t粒')#line:730
        except Exception as OO0000OOOOOOO0OO0 :#line:731
            print (OO0000OOOOOOO0OO0 )#line:732
    def user_ad (O0OO0O0OO0OOO000O ):#line:735
        try :#line:736
            O0O0000OOO000OOOO =f'__{timi_new()}'#line:737
            O0OOOO0OOO00OOO00 ={'source':'scsc','authorization':O0OO0O0OO0OOO000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OOO000OOOO ),'signstring':O0O0000OOO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:748
            OO000000O00O0OOO0 =requests .request ('get',f'{host}/user/ad',headers =O0OOOO0OOO00OOO00 ).json ()#line:749
            if 'status'in OO000000O00O0OOO0 :#line:751
                if OO000000O00O0OOO0 ['status']==200 :#line:752
                    O000O0O000OOOO0OO =OO000000O00O0OOO0 ['data']['max_time']#line:753
                    O0O00O0O00O0O0O0O =OO000000O00O0OOO0 ['data']['watch_time']#line:754
                    O00O0000OO00OOOOO =OO000000O00O0OOO0 ['data']['added_time']#line:755
                    print (f'【获取种子】:获取🌱剩余{O00O0000OO00OOOOO + O000O0O000OOOO0OO - O0O00O0O00O0O0O0O}次丨好友提供:{O00O0000OO00OOOOO}次')#line:756
                    if O00O0000OO00OOOOO +O000O0O000OOOO0OO -O0O00O0O00O0O0O0O >0 :#line:757
                        time .sleep (random .randint (16 ,19 ))#line:758
                        OO000O00O0O00OOOO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOOO0OOO00OOO00 ).json ()#line:759
                        if 'status'in OO000O00O0O00OOOO :#line:761
                            if OO000O00O0O00OOOO ['status']==200 :#line:762
                                O0OOOO00OOOO0OO00 =float (OO000O00O0O00OOOO ['data']['silver'])/1000000000000 #line:763
                                print (f'【获取种子】:获得🌱:{int(O0OOOO00OOOO0OO00)}t粒')#line:764
                                return True #line:765
                            if OO000O00O0O00OOOO ['status']==500 :#line:766
                                O0O00O00000O0O0O0 =OO000O00O0O00OOOO ['message']#line:767
                                print (f'【获取种子】:{O0O00O00000O0O0O0}')#line:768
                                return False #line:769
        except Exception as O0OOOO00000OO00O0 :#line:770
            print (O0OOOO00000OO00O0 )#line:771
    def synthetic (OOOO0O000OOOOO000 ):#line:774
        global id ,g #line:775
        try :#line:776
            O0O0OO000OOOO0OO0 =OOOO0O000OOOOO000 .level_new ()#line:777
            OOO0000OOOO0O000O =random .randint (9 ,11 )#line:778
            OOOO0O0OOO0O00O0O =f'_site=8&targetSite={OOO0000OOOO0O000O}_{timi_new()}'#line:779
            OO0O00OO0O00OOOOO ={'source':'scsc','authorization':OOOO0O000OOOOO000 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O0OOO0O00O0O ),'signstring':OOOO0O0OOO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:790
            O0000OOOO00OOO0O0 ={"site":int (8 ),"targetSite":int (OOO0000OOOO0O000O )}#line:791
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OO0O00OOOOO ,json =O0000OOOO00OOO0O0 )#line:792
            while True :#line:793
                OOO000O000OO0O00O =f'__{timi_new()}'#line:794
                O0O00O0000O0O0OO0 ={'source':'scsc','authorization':OOOO0O000OOOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O000OO0O00O ),'signstring':OOO000O000OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:805
                O0OOOO000O00000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0000O0O0OO0 ).json ()#line:806
                if 'status'in O0OOOO000O00000O0 :#line:808
                    if O0OOOO000O00000O0 ['status']==200 :#line:809
                        O00O00000OOOO0O00 =O0OOOO000O00000O0 ['data']['cropList']#line:810
                        O00OO0OOO000O0000 =O0OOOO000O00000O0 ['data']['gameCoreDataDBid']#line:811
                        O0OOOOOOO00O00O0O =float (O0OOOO000O00000O0 ['data']['silver'])/1000000000000 #line:812
                        O0O00000O000OO0O0 =0 #line:817
                        for OOOO0OO000OOO00O0 in O00O00000OOOO0O00 :#line:818
                            if not OOOO0OO000OOO00O0 :#line:819
                                O0OOOOO00O0OO00O0 =f'_crop_id={O00OO0OOO000O0000}&site={O0O00000O000OO0O0}_{OOOO0O000OOOOO000.time}'#line:820
                                OOOOOO0OO0O0OO000 ={'source':'scsc','authorization':OOOO0O000OOOOO000 .token ,'timestamp':OOOO0O000OOOOO000 .time ,'sign':sign (O0OOOOO00O0OO00O0 ),'signstring':O0OOOOO00O0OO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:830
                                O00000O00O000000O ={"site":O0O00000O000OO0O0 ,"crop_id":O00OO0OOO000O0000 }#line:831
                                O0O0O0OOOO0OOOO00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOOOO0OO0O0OO000 ,data =O00000O00O000000O ).json ()#line:832
                                time .sleep (random .randint (1 ,3 )/10 )#line:834
                                if 'status'in O0O0O0OOOO0OOOO00 :#line:835
                                    if O0O0O0OOOO0OOOO00 ['status']==200 :#line:836
                                        if O0O0O0OOOO0OOOO00 ['message']=='种子数量不足':#line:837
                                            O0O0OO000OOOO0OO0 =OOOO0O000OOOOO000 .level_new ()#line:838
                                            print (f'【种植合成】:{O0O0O0OOOO0OOOO00["message"]}')#line:839
                                            if not OOOO0O000OOOOO000 .user_ad ():#line:840
                                                return False #line:841
                                    if O0O0O0OOOO0OOOO00 ['status']==500 :#line:842
                                        print (f'【种植合成】:{O0O0O0OOOO0OOOO00["message"]}')#line:843
                                        return False #line:844
                            O0O00000O000OO0O0 +=1 #line:845
                        OO0O00O000O0O0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0O00O0000O0O0OO0 ).json ()#line:846
                        O0OO0OOO0000OOO0O =OO0O00O000O0O0O0O ['data']['cropList']#line:847
                        OOOO0OOOO00OO00OO =False #line:848
                        for OOOO0OO000OOO00O0 in range (12 ):#line:849
                            id =O0OO0OOO0000OOO0O [OOOO0OO000OOO00O0 ]['level']#line:850
                            if float (O0O0OO000OOOO0OO0 )-float (id )>9 :#line:851
                                O0OO00O0O0OOO0OOO =f'_site={OOOO0OO000OOO00O0}_{timi_new()}'#line:852
                                OO0OOO0000O0O0O0O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO0O000OOOOO000 .token ,'timestamp':timi_new (),'sign':sign (O0OO00O0O0OOO0OOO ),'signstring':O0OO00O0O0OOO0OOO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:863
                                OOO00OO0O0000O0OO ={"site":OOOO0OO000OOO00O0 }#line:864
                                O0OOOOOOO00O00O00 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0OOO0000O0O0O0O ,data =OOO00OO0O0000O0OO ).json ()#line:866
                                if 'status'in O0OOOOOOO00O00O00 :#line:867
                                    if O0OOOOOOO00O00O00 ['status']==200 :#line:868
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:869
                            if id !=0 :#line:870
                                for O0O000OOO0000OO0O in range (11 ):#line:871
                                    O0O0OO00O00OOO0OO =O0O000OOO0000OO0O +1 #line:872
                                    g =O0OO0OOO0000OOO0O [O0O0OO00O00OOO0OO ]['level']#line:873
                                    if id ==g :#line:874
                                        OOO0OO00OO0O0O00O =O0O000OOO0000OO0O +2 #line:875
                                        if OOO0OO00OO0O0O00O !=OOOO0OO000OOO00O0 +1 :#line:876
                                            OOOO00000OO00O0O0 =OOOO0OO000OOO00O0 +1 #line:877
                                            time .sleep (random .randint (1 ,3 )/10 )#line:879
                                            OOOO0O0OOO0O00O0O =f'_site={OOOO00000OO00O0O0 - 1}&targetSite={OOO0OO00OO0O0O00O - 1}_{timi_new()}'#line:880
                                            OO0O00OO0O00OOOOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOOO0O000OOOOO000 .token ,'timestamp':timi_new (),'sign':sign (OOOO0O0OOO0O00O0O ),'signstring':OOOO0O0OOO0O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:897
                                            O0O00OO0OOOO000OO ={"site":int (OOOO00000OO00O0O0 -1 ),"targetSite":int (OOO0OO00OO0O0O00O -1 )}#line:898
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OO0O00OOOOO ,json =O0O00OO0OOOO000OO )#line:899
                                            OOOO0OOOO00OO00OO =True #line:901
                                    if OOOO0OOOO00OO00OO :#line:902
                                        break #line:903
                                if OOOO0OOOO00OO00OO :#line:904
                                    break #line:905
        except :#line:906
            OOOO0O000OOOOO000 .synthetic ()#line:907
    def level_new (O00OO0O000O0OO0OO ):#line:910
        try :#line:911
            O0O00O0O000OOOO00 =f'__{timi_new()}'#line:912
            OOOOOOOOO0000O0OO ={'source':'scsc','authorization':O00OO0O000O0OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0O000OOOO00 ),'signstring':O0O00O0O000OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:923
            OOOOOOO00O00OO0O0 =requests .request ('get',f'{host}/user',headers =OOOOOOOOO0000O0OO ).json ()#line:924
            if 'status'in OOOOOOO00O00OO0O0 :#line:925
                if OOOOOOO00O00OO0O0 ['status']==200 :#line:926
                    return float (OOOOOOO00O00OO0O0 ['data']['level'])#line:927
        except Exception as O00OOOO000O00000O :#line:928
            print (O00OOOO000O00000O )#line:929
    def propsraffle (O0OO0OO0000O0O000 ):#line:932
        try :#line:933
            while True :#line:934
                O0O0OO0O0OOOO000O =f'__{timi_new()}'#line:935
                OOO00OO00OOO0OO0O ={'source':'scsc','authorization':O0OO0OO0000O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0O0OOOO000O ),'signstring':O0O0OO0O0OOOO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:946
                OO00OOOOOO0000O0O =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO00OO00OOO0OO0O ).json ()#line:947
                if 'status'in OO00OOOOOO0000O0O :#line:949
                    if OO00OOOOOO0000O0O ['status']==200 :#line:950
                        OOOOO000O000O0OOO =OO00OOOOOO0000O0O ['data']['rows']#line:951
                        OO0OO0OO000O0OO0O =OO00OOOOOO0000O0O ['data']['vstate']#line:952
                        if OOOOO000O000O0OOO ==5 or OOOOO000O000O0OOO ==6 or OOOOO000O000O0OOO ==7 :#line:953
                            OO000O0OOO0O0OOO0 =OO00OOOOOO0000O0O ['data']['silver']#line:954
                            print (f'【转盘抽奖】:获得种子:{OO000O0OOO0O0OOO0}')#line:955
                        if OOOOO000O000O0OOO ==1 or OOOOO000O000O0OOO ==2 or OOOOO000O000O0OOO ==3 :#line:956
                            OO0OOOOOOOO00OOOO =OO00OOOOOO0000O0O ['data']['clover']#line:957
                            print (f'【转盘抽奖】:获得三叶草:{OO0OOOOOOOO00OOOO}')#line:958
                        if OOOOO000O000O0OOO ==4 or OOOOO000O000O0OOO ==8 :#line:959
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:960
                        if OOOOO000O000O0OOO =='抽奖次数已用完':#line:964
                            break #line:998
                time .sleep (random .randint (8 ,15 )/10 )#line:999
        except Exception as OOO0OO0O00OOOOO0O :#line:1000
            print (OOO0OO0O00OOOOO0O )#line:1001
    def friends_invitation (OO0OO0OO00OO0000O ):#line:1004
        try :#line:1005
            OO0OO0O0OO0O0OOOO =f'__{timi_new()}'#line:1006
            O000OOOOOO0OOO00O ={'source':'scsc','authorization':OO0OO0OO00OO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO0O0OOOO ),'signstring':OO0OO0O0OO0O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1017
            O0O0OO00OOO0O00OO =requests .request ('get',f'{host}/friends',headers =O000OOOOOO0OOO00O ).json ()#line:1018
            if 'status'in O0O0OO00OOO0O00OO :#line:1019
                if O0O0OO00OOO0O00OO ['status']==200 :#line:1020
                    OO0OO00O00O00O0OO =O0O0OO00OOO0O00OO ['data']['myInviteter']#line:1021
                    if OO0OO00O00O00O0OO :#line:1022
                        O0OO0O00O00O0O0OO =OO0OO00O00O00O0OO ['user']['nickname']#line:1023
                        O00O0O0O0O0OOO0O0 =OO0OO0OO00OO0000O .certification ()#line:1024
                        print (f'【查邀请人】:我的邀请人:{O0OO0O00O00O0O0OO}丨实名:{O00O0O0O0O0OOO0O0}')#line:1025
                    else :#line:1026
                        if OO0OO0OO00OO0000O .innerId !='0':#line:1027
                            OO0OO0OO00OO0000O .invitation ()#line:1028
        except Exception as OOOOO0OO00O00OO0O :#line:1029
            print (OOOOO0OO00O00OO0O )#line:1030
    def add_clover (O0O0OO00O000OOO0O ):#line:1033
        global golden_seed #line:1034
        try :#line:1035
            O0OOO00O0O0OO0OOO =f'__{timi_new()}'#line:1036
            O00O0O00OOOO0OO0O ={'source':'scsc','authorization':O0O0OO00O000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0OO0OOO ),'signstring':O0OOO00O0O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1047
            OOO000OO000O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O00O0O00OOOO0OO0O ).json ()#line:1048
            if 'status'in OOO000OO000O0O0O0 :#line:1050
                if OOO000OO000O0O0O0 ['status']==200 :#line:1051
                    O000OO0OO00OO0OO0 =OOO000OO000O0O0O0 ['data']['clover']#line:1052
                    OOOOO0OO0O0000000 =OOO000OO000O0O0O0 ['data']['used_clover']#line:1053
                    OO00OOOO00O00OOO0 =float (O000OO0OO00OO0OO0 )-float (OOOOO0OO0O0000000 )#line:1054
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOOO0OO0O0000000}')#line:1055
                    if O0O0OO00O000OOO0O .certification ()!='未实名':#line:1056
                        if OO00OOOO00O00OOO0 >1 :#line:1057
                            O0OOO00O0O0OO0OOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OO00OOOO00O00OOO0)}_{timi_new()}'#line:1058
                            OOOOO00OOO0OO00O0 ={'source':'scsc','authorization':O0O0OO00O000OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00O0O0OO0OOO ),'signstring':O0OOO00O0O0OO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1069
                            O00OOOO000O0OOO00 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OO00OOOO00O00OOO0 )}#line:1070
                            O0O0OOO0OOO0OO0OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOOOO00OOO0OO00O0 ,data =O00OOOO000O0OOO00 ).json ()#line:1071
                            if 'status'in O0O0OOO0OOO0OO0OO :#line:1073
                                if O0O0OOO0OOO0OO0OO ['status']==200 :#line:1074
                                    print (f'【参与抽奖】:添加☘️:{O0O0OOO0OOO0OO0OO["data"]}丨数量:{OO00OOOO00O00OOO0}')#line:1075
                                if O0O0OOO0OOO0OO0OO ['status']==500 :#line:1076
                                    print (f'【参与抽奖】:添加☘️:{O0O0OOO0OOO0OO0OO["message"]}')#line:1077
            O0OO00O0OOOO00OOO =requests .request ('get',f'{host}/lottery',headers =O00O0O00OOOO0OO0O ).json ()#line:1078
            OO0OOOO000O00O0O0 =O0O0OO00O000OOO0O .winning_rewards ()#line:1080
            if 'status'in O0OO00O0OOOO00OOO :#line:1081
                if O0OO00O0OOOO00OOO ['status']==200 :#line:1082
                    O0O0OO0O0OOOO0000 =O0OO00O0OOOO00OOO ['data'][0 ]['day_get_gold_quantity']#line:1083
                    golden_seed +=float (O0O0OO0O0OOOO0000 )#line:1084
                    OOO00O00OOOOO0OOO =O0OO00O0OOOO00OOO ['data'][1 ]['value']#line:1085
                    OOO00O00OOO00O0O0 =O0OO00O0OOOO00OOO ['data'][0 ]['join_number']#line:1086
                    OOO0O0O0OOOO0OO0O =int (float (O0OO00O0OOOO00OOO ['data'][0 ]['totalValue']))#line:1087
                    OOOO0O0O00O0OO000 =float (OOO00O00OOOOO0OOO /OOO0O0O0OOOO0OO0O )*10000 #line:1088
                    OO00O00O000OO0OOO =OOO0O0O0OOOO0OO0O /OOO00O00OOO00O0O0 #line:1089
                    print (f'【参与抽奖】:预计每天中{str(O0O0OO0O0OOOO0000)[:6]}颗金种子丨好友收益:{str(OO0OOOO000O00O0O0)[:6]}')#line:1090
                    print (f'【抽奖统计】:每1万☘️中{str(OOOO0O0O00O0OO000)[:6]}颗金种子丨☘️人均:{str(OO00O00O000OO0OOO)[:7]}️')#line:1091
        except Exception as O00OO00000OOO000O :#line:1092
            print (O00OO00000OOO000O )#line:1093
    def energy (O0O0OOO00O000O00O ):#line:1097
        try :#line:1098
            while True :#line:1099
                O00O0000O0OO0OOO0 =f'__{timi_new()}'#line:1100
                O0OO0000OO00OOO0O ={'source':'scsc','authorization':O0O0OOO00O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0000O0OO0OOO0 ),'signstring':O00O0000O0OO0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1111
                O0O0OO0000OOOO0O0 =requests .request ('get',f'{host}/energy/general',headers =O0OO0000OO00OOO0O ).json ()#line:1112
                if 'status'in O0O0OO0000OOOO0O0 :#line:1114
                    if O0O0OO0000OOOO0O0 ['status']==200 :#line:1115
                        O00OO00OO0OOOOO00 =O0O0OO0000OOOO0O0 ['data']['ordinary_water']#line:1116
                        OO000000OO0O00OOO =O0O0OO0000OOOO0O0 ['data']['ordinary_fertilizer']#line:1117
                        OO000OOO000OO000O =O0O0OO0000OOOO0O0 ['data']['videoStatus']#line:1118
                        OOOOOOOOOO0OO00O0 =O0O0OO0000OOOO0O0 ['data']['waterVideoKey']#line:1119
                        print (f'【我的营养】:肥料:{str(OO000000OO0O00OOO).split(".")[0]}丨水滴:{str(O00OO00OO0OOOOO00).split(".")[0]}')#line:1120
                        if float (OO000000OO0O00OOO )<96 :#line:1121
                            if OO000OOO000OO000O :#line:1122
                                time .sleep (random .randint (160 ,180 )/10 )#line:1123
                                OOO0OO0OOOOO0O00O =99 -float (OO000000OO0O00OOO )#line:1124
                                O00OOO0OOOO0OOO0O ={"fertilizer":str (OOO0OO0OOOOO0O00O ).split ('.')[0 ]}#line:1125
                                OOOOOOOO000OO000O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0OO0000OO00OOO0O ).json ()#line:1126
                                if 'status'in OOOOOOOO000OO000O :#line:1128
                                    if OOOOOOOO000OO000O ['status']==200 :#line:1129
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOOOOO000OO000O["message"]}')#line:1130
                                    if OOOOOOOO000OO000O ['status']==500 :#line:1131
                                        print (f'【购买肥料】:看广告获取肥料:{OOOOOOOO000OO000O["message"]}')#line:1132
                                        break #line:1133
                                if float (OO000000OO0O00OOO )<78 :#line:1135
                                    OOO0OO0OOOOO0O00O =80 -float (OO000000OO0O00OOO )#line:1136
                                    OOOOOO00O00O000O0 =f'_fertilizer={int(OOO0OO0OOOOO0O00O)}_{timi_new()}'#line:1137
                                    O0O0OOO000O0OOO0O ={'source':'scsc','authorization':O0O0OOO00O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOO00O00O000O0 ),'signstring':OOOOOO00O00O000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1148
                                    O00OO00O0OO00OOO0 ={"fertilizer":int (OOO0OO0OOOOO0O00O )}#line:1149
                                    OOOO0000OO0OOO0OO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0O0OOO000O0OOO0O ,data =O00OO00O0OO00OOO0 ).json ()#line:1151
                                    if 'status'in OOOO0000OO0OOO0OO :#line:1153
                                        if OOOO0000OO0OOO0OO ['status']==200 :#line:1154
                                            print (f'【购买肥料】:购买肥料:{OOOO0000OO0OOO0OO["message"]}丨数量:{int(OOO0OO0OOOOO0O00O)}')#line:1155
                                        if OOOO0000OO0OOO0OO ['status']==500 :#line:1156
                                            print (f'【购买肥料】:购买肥料:{OOOO0000OO0OOO0OO["message"]}丨数量:{int(OOO0OO0OOOOO0O00O)}')#line:1157
                                            O000000O0000OO00O =OOOO0000OO0OOO0OO ["message"].split ('-')[1 ]#line:1158
                                            O0OOOO0OO0OOO0000 =f'__{timi_new()}'#line:1159
                                            O0OO00OO0O0OOOO00 ={'source':'scsc','authorization':O0O0OOO00O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OO0OOO0000 ),'signstring':O0OOOO0OO0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1170
                                            O0OO00O00OOO00000 =requests .request ('get',f'{host}/user',headers =O0OO00OO0O0OOOO00 ).json ()#line:1171
                                            if 'status'in O0OO00O00OOO00000 :#line:1172
                                                if O0OO00O00OOO00000 ['status']==200 :#line:1173
                                                    OOOOO00000O0O0000 =O0OO00O00OOO00000 ['data']['inner_id']#line:1174
                                                    if give_gold (OOOOO00000O0O0000 ,float (O000000O0000OO00O )+1 ):#line:1175
                                                        O0O0OOO00O000O00O .energy ()#line:1176
                        if float (O00OO00OO0OOOOO00 )<880 :#line:1177
                            if OOOOOOOOOO0OO00O0 :#line:1178
                                time .sleep (random .randint (160 ,180 )/10 )#line:1179
                                OOOO00O00000O00OO =999 -float (O00OO00OO0OOOOO00 )#line:1180
                                OO0OOOO0O000O00O0 ={"water":str (OOOO00O00000O00OO ).split ('.')[0 ]}#line:1181
                                O00O00000O00OO0OO =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0OO0000OO00OOO0O ).json ()#line:1182
                                if 'status'in O00O00000O00OO0OO :#line:1184
                                    if O00O00000O00OO0OO ['status']==200 :#line:1185
                                        print (f'【购买水滴】:看广告获取水滴:{O00O00000O00OO0OO["message"]}')#line:1186
                                    if O00O00000O00OO0OO ['status']==500 :#line:1187
                                        print (f'【购买水滴】:看广告获取水滴:{O00O00000O00OO0OO["message"]}')#line:1188
                                        break #line:1189
                                if float (O00OO00OO0OOOOO00 )<780 :#line:1190
                                    OOOO00O00000O00OO =800 -float (O00OO00OO0OOOOO00 )#line:1191
                                    OO000OOOOOOOO0OO0 =f'_water={int(OOOO00O00000O00OO)}_{timi_new()}'#line:1192
                                    O000OOO0OO000OOOO ={'source':'scsc','authorization':O0O0OOO00O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOOOOOO0OO0 ),'signstring':OO000OOOOOOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1203
                                    O00000OO00O000OO0 ={"water":int (OOOO00O00000O00OO )}#line:1204
                                    OOO0O0000OOO00OOO =requests .request ('post',f'{host}/energy/general/buy/water',headers =O000OOO0OO000OOOO ,data =O00000OO00O000OO0 ).json ()#line:1206
                                    if 'status'in OOO0O0000OOO00OOO :#line:1208
                                        if OOO0O0000OOO00OOO ['status']==200 :#line:1209
                                            print (f'【购买水滴】:购买水滴:{OOO0O0000OOO00OOO["message"]}丨数量:{int(OOOO00O00000O00OO)}')#line:1210
                                        if OOO0O0000OOO00OOO ['status']==500 :#line:1211
                                            print (f'【购买水滴】:购买水滴:{OOO0O0000OOO00OOO["message"]}丨数量:{int(OOOO00O00000O00OO)}')#line:1212
                                            O000000O0000OO00O =OOO0O0000OOO00OOO ["message"].split ('-')[1 ]#line:1213
                                            O0OOOO0OO0OOO0000 =f'__{timi_new()}'#line:1214
                                            O0OO00OO0O0OOOO00 ={'source':'scsc','authorization':O0O0OOO00O000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0OO0OOO0000 ),'signstring':O0OOOO0OO0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1225
                                            O0OO00O00OOO00000 =requests .request ('get',f'{host}/user',headers =O0OO00OO0O0OOOO00 ).json ()#line:1226
                                            if 'status'in O0OO00O00OOO00000 :#line:1227
                                                if O0OO00O00OOO00000 ['status']==200 :#line:1228
                                                    OOOOO00000O0O0000 =O0OO00O00OOO00000 ['data']['inner_id']#line:1229
                                                    if give_gold (OOOOO00000O0O0000 ,float (O000000O0000OO00O )+1 ):#line:1230
                                                        O0O0OOO00O000O00O .energy ()#line:1231
                        break #line:1232
        except Exception as OO0OO00OO0OO00OO0 :#line:1233
            print (OO0OO00OO0OO00OO0 )#line:1234
def bundled_def ():#line:1236
    O0OOO0O0O0000000O =['5570536','7750212','7911652','7911680','7805624']#line:1237
    return O0OOO0O0O0000000O [random .randint (0 ,len (O0OOO0O0O0000000O )-1 )]#line:1238
def version_of_the_validation ():#line:1242
    return str ((93 -56 )/10 )#line:1243
def sc2 ():#line:1245
    return "19319#$%^&*((*"#line:1246
def OO00OO0OO0OO00OO00o0 ():#line:1248
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1249
def get_ip ():#line:1251
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1252
def gitee_validation ():#line:1254
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1255
def gitee_edition ():#line:1257
    try :#line:1258
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1259
    except :#line:1260
        sys .exit (0 )#line:1261
def O000OO000O0O00OOO00 ():#line:1266
    try :#line:1267
        O0OOOOOO0O000OOOO =gitee_edition ()#line:1268
        if version_of_the_validation ()<O0OOOOOO0O000OOOO ['CityEarth']['edition']:#line:1269
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOOO0O000OOOO["CityEarth"]["edition"]}   ❌')#line:1270
            print (f'更新内容=>>{O0OOOOOO0O000OOOO["CityEarth"]["content"]}   🎉')#line:1271
        else :#line:1272
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOOOOO0O000OOOO["CityEarth"]["edition"]}   ✅')#line:1273
            print (f'更新内容=>> {O0OOOOOO0O000OOOO["CityEarth"]["content"]}   🎉')#line:1274
    except Exception as OO000OOO0OO0OOOO0 :#line:1275
        print (OO000OOO0OO0OOOO0 )#line:1276
def sc3 ():#line:1278
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1279
if __name__ =='__main__':#line:1283
    start ()#line:1284
