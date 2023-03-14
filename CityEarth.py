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
        OO0OO0OO00O0OOO0O =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(OO0OO0OO00O0OOO0O)}个账号==========")#line:13
        for O00O0O00O0OOO0OO0 in OO0OO0OO00O0OOO0O :#line:14
            O00O0O0OOO00OO0O0 =[]#line:15
            print (f"------------正在执行第{OO0OO0OO00O0OOO0O.index(O00O0O00O0OOO0OO0) + 1}个账号------------")#line:16
            OOO0O00OOOOOOOOO0 =CityEarth (O00O0O00O0OOO0OO0 ,O00O0O0OOO00OO0O0 ,OO0OO0OO00O0OOO0O .index (O00O0O00O0OOO0OO0 ))#line:17
            def OO00O0OO0O0OO0OOO ():#line:19
                if OOO0O00OOOOOOOOO0 .base_info ():#line:21
                    OOO0O00OOOOOOOOO0 .sealing ()#line:23
                    OOO0O00OOOOOOOOO0 .invitenum ()#line:25
                    OOO0O00OOOOOOOOO0 .query_to_sell ()#line:27
                    OOO0O00OOOOOOOOO0 .game_map ()#line:29
                    OOO0O00OOOOOOOOO0 .friends_invitation ()#line:31
                    OOO0O00OOOOOOOOO0 .energy ()#line:33
                    OOO0O00OOOOOOOOO0 .add_clover ()#line:35
                    OOO0O00OOOOOOOOO0 .propsraffle ()#line:37
                    OOO0O00OOOOOOOOO0 .synthetic ()#line:39
                    OOO0O00OOOOOOOOO0 .crops_illustrated ()#line:41
                    OOO0O00OOOOOOOOO0 .withdraw ()#line:43
                    if float (datetime .datetime .now ().hour )>8 :#line:44
                        OOO0O00OOOOOOOOO0 .give_gold ()#line:46
            O00OOOO0O0000OO0O =threading .Thread (target =OO00O0OO0O0OO0OOO )#line:47
            O00OOOO0O0000OO0O .start ()#line:48
            time .sleep (time_xx )#line:49
        print (f"------------正在处理推送通知------------")#line:50
        time .sleep (0.5 )#line:51
        O000O00OOOO0OOO0O =format_msg ()#line:52
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O000O00OOOO0OOO0O +' ')#line:53
        if eeeeee :#line:54
            time .sleep (100 )#line:55
            print ('开始打印好友数量不足2的ID')#line:56
            print (invited_new )#line:57
    except Exception as O000000OO00OOO0OO :#line:58
        print (O000000OO00OOO0OO )#line:59
def give_gold (O0O0O0O0O000OO0OO ,O00O0O0OOOO0O0000 ):#line:62
        try :#line:63
            O000OOOO0OOOO00O0 =f'_doneeNo={O0O0O0O0O000OO0OO}&quantity={int(O00O0O0OOOO0O0000)}_{timi_new()}'#line:64
            OOO00OO0O0O0O00O0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O000OOOO0OOOO00O0 ),'signstring':O000OOOO0OOOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:75
            O0O0OO0000O0O0O0O ={"quantity":int (O00O0O0OOOO0O0000 ),"doneeNo":O0O0O0O0O000OO0OO }#line:79
            OO000OOOO0O000OOO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO00OO0O0O0O00O0 ,data =O0O0OO0000O0O0O0O ).json ()#line:80
            if 'status'in OO000OOOO0O000OOO :#line:82
                if OO000OOOO0O000OOO ['status']==200 :#line:83
                    if OO000OOOO0O000OOO ['data']:#line:84
                        print (f'【赠送种子】:赠送{int(O00O0O0OOOO0O0000)}种子给{O0O0O0O0O000OO0OO}成功')#line:85
                        return True #line:86
                if OO000OOOO0O000OOO ['status']==401 :#line:87
                    print (f'【赠送种子】:{OO000OOOO0O000OOO["message"]}')#line:88
                    return False #line:89
                if OO000OOOO0O000OOO ['status']==500 :#line:90
                    print (f'【赠送种子】:{OO000OOOO0O000OOO["message"]}')#line:91
                    return False #line:92
            return False #line:93
        except Exception as O0OOO0O0OO00O0OOO :#line:94
            print (O0OOO0O0OO00O0OOO )#line:95
def kvkv ():#line:96
    return '/vastzzzl/vastzzzl/raw/master'#line:97
def sign (OO0O00OO000OO00O0 ):#line:100
    OO0O0OOOO0O0OO0O0 =hashlib .md5 (OO0O00OO000OO00O0 .encode ()).hexdigest ()#line:101
    O0OOO0O0000OOOO00 =sc1 ()#line:102
    O00000OO0OO0OO0O0 =sc2 ()#line:103
    O0O0000OO00O0OO0O =sc3 ()#line:104
    O000000000OO0OOOO =O0OOO0O0000OOOO00 +OO0O0OOOO0O0OO0O0 +O00000OO0OO0OO0O0 +O0O0000OO00O0OO0O #line:105
    OOOOOOO000O00OO00 =hashlib .md5 (O000000000OO0OOOO .encode ()).hexdigest ()#line:106
    return OOOOOOO000O00OO00 #line:107
def format_msg ():#line:111
    OO0OOOO0OO000000O =""#line:112
    for OO00O0O00O0OO0OO0 in msg_list :#line:113
        OO0OOOO0OO000000O +=str (OO00O0O00O0OO0OO0 )+"\r\n"#line:114
    return OO0OOOO0OO000000O #line:115
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
def get_json_data (O0O0OO0OOOO0OO000 ,O0OOOO000O0OOOO0O ,O0O0OO00OOOO0OOO0 ,OO0OO0O00OOOO00OO ):#line:134
    with open (O0O0OO0OOOO0OO000 ,'rb')as OO0O0O00O00OOOO00 :#line:136
        O0O000O0O00O0O00O =json .load (OO0O0O00O00OOOO00 )#line:137
        O0O000O0O00O0O00O ['data'][O0OOOO000O0OOOO0O ][O0O0OO00OOOO0OOO0 ]=OO0OO0O00OOOO00OO #line:138
        O000O0O000OOO0O0O =O0O000O0O00O0O00O #line:139
    OO0O0O00O00OOOO00 .close ()#line:140
    return O000O0O000OOO0O0O #line:141
def write_json_data (OOOO0OOO00O0OOO0O ):#line:143
    with open (json_path1 ,'w')as OOOOOOOOOOOO00O00 :#line:144
        json .dump (OOOO0OOO00O0OOO0O ,OOOOOOOOOOOO00O00 )#line:145
    OOOOOOOOOOOO00O00 .close ()#line:146
    return True #line:147
class CityEarth :#line:149
    def __init__ (OOO0OO0O000O0000O ,O00O00000OO0000OO ,O0OO0O0OO0OOOO00O ,O000O00OO0OO0O0OO ):#line:151
        try :#line:152
            OOO0OO0O000O0000O .msg =O0OO0O0OO0OOOO00O #line:153
            OOO0OO0O000O0000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:154
            OOO0OO0O000O0000O .token =O00O00000OO0000OO ['authorization']#line:155
            OOO0OO0O000O0000O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:156
            OOO0OO0O000O0000O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:157
            OOO0OO0O000O0000O .elephant_user =O00O00000OO0000OO ['elephant_user']#line:158
            OOO0OO0O000O0000O .elephant_pswd =O00O00000OO0000OO ['elephant_pswd']#line:159
            OOO0OO0O000O0000O .elephant_Task_ID =O00O00000OO0000OO ['elephant_Task_ID']#line:160
            OOO0OO0O000O0000O .len_new =O000O00OO0OO0O0OO #line:161
        except :#line:162
            print ('变量格式错误')#line:163
    def base_info (O000000O000OO00OO ):#line:166
        try :#line:167
            O000000O000OO00OO .watched_ad ()#line:169
            OO0O0000O0O0OOOOO =f'__{timi_new()}'#line:170
            O0O0OOO00OO00O0O0 ={'source':'scsc','authorization':O000000O000OO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000O0O0OOOOO ),'signstring':OO0O0000O0O0OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:181
            O0O0O0O0O0O00O0OO =requests .request ('get',f'{host}/user',headers =O0O0OOO00OO00O0O0 ).json ()#line:182
            if 'status'in O0O0O0O0O0O00O0OO :#line:184
                if O0O0O0O0O0O00O0OO ['status']==200 :#line:185
                    O00OO0OO0OOO0O000 =O0O0O0O0O0O00O0OO ['data']['nickname']#line:186
                    O000OOO00OOO0O00O =O0O0O0O0O0O00O0OO ['data']['inner_id']#line:187
                    O0O0O0O0000OO00OO =O0O0O0O0O0O00O0OO ['data']['assets']['gold']#line:188
                    O000O00OOOOOOOO0O =O0O0O0O0O0O00O0OO ['data']['level']#line:189
                    print (f'【账号信息】:昵称:{O00OO0OO0OOO0O000[:5]}丨ID:{O000OOO00OOO0O00O}丨等级:{O000O00OOOOOOOO0O}丨金种子:{str(O0O0O0O0000OO00OO).split(".")[0]}')#line:190
                    if 'wx_'in O00OO0OO0OOO0O000 :#line:191
                        O000000O000OO00OO .change_nickname ()#line:192
                if O0O0O0O0O0O00O0OO ['status']==401 :#line:193
                    print ('【账号信息】:账号失效正在尝试登录')#line:194
                    if O000000O000OO00OO .elephant_user =='f':#line:195
                        return False #line:196
                    O000OOO0OO0O0O0OO =Invalid_login .addtask (elephant_user =O000000O000OO00OO .elephant_user ,elephant_pswd =O000000O000OO00OO .elephant_pswd ,elephant_Task_ID =O000000O000OO00OO .elephant_Task_ID )#line:197
                    O00O0O0O00O00O00O =get_json_data (json_path ,O000000O000OO00OO .len_new ,'authorization',O000OOO0OO0O0O0OO )#line:198
                    if write_json_data (O00O0O0O00O00O00O ):#line:199
                        print ('正在写入账号配置文件')#line:200
                    return False #line:201
                if O0O0O0O0O0O00O0OO ['status']==500 :#line:202
                    return False #line:203
            return True #line:204
        except Exception as OO0O000OO00OO0000 :#line:205
            print (OO0O000OO00OO0000 )#line:206
    def sealing (O0OO000O0OOO0O00O ):#line:209
        try :#line:210
            OO0000O0O0O0O000O =f'__{timi_new()}'#line:211
            OO00O000O0O00000O ={'source':'scsc','authorization':O0OO000O0OOO0O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O0O0O0O000O ),'signstring':OO0000O0O0O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OO00O000O0O00000O )#line:223
            requests .request ('get',f'{host}/packsack/list',headers =OO00O000O0O00000O )#line:224
            requests .request ('get',f'{host}/friends/invited/ad',headers =OO00O000O0O00000O )#line:225
            requests .request ('get',f'{host}/assets/gold/rank',headers =OO00O000O0O00000O )#line:226
            requests .request ('get',f'{host}/user',headers =OO00O000O0O00000O )#line:227
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OO00O000O0O00000O )#line:228
            requests .request ('get',f'{host}/finance/get-power-list',headers =OO00O000O0O00000O )#line:229
            requests .request ('post',f'{host}/announcement/announcement',headers =OO00O000O0O00000O )#line:230
            requests .request ('get',f'{host}/game/getAllData',headers =OO00O000O0O00000O )#line:231
            requests .request ('get',f'{host}/assets',headers =OO00O000O0O00000O )#line:232
        except Exception as O0000OO00O000OO0O :#line:233
            print (O0000OO00O000OO0O )#line:234
    def the_query (OOOOO0OOOO0O000O0 ):#line:237
        try :#line:238
            OOOO0O0OO0O00O000 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:239
            OOO0OO00O0O0OO00O ={'authorization':OOOOO0OOOO0O000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O0OO0O00O000 ),'signstring':OOOO0O0OO0O00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            O00000OOOO0OO00O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OOO0OO00O0O0OO00O ).json ()#line:250
            if 'status'in O00000OOOO0OO00O0 :#line:252
                if O00000OOOO0OO00O0 ['status']==200 :#line:253
                    OOOO0000O00OO00O0 =O00000OOOO0OO00O0 ['data']['rows'][3 ]['price']#line:254
                    OOOOO0OOOO0O000O0 .market_sale (OOOO0000O00OO00O0 )#line:255
        except Exception as OOO0O0OO000OOO0O0 :#line:256
            print (OOO0O0OO000OOO0O0 )#line:257
    def market_sale (O0000000O0000O00O ,OOO0O0O00OOOO0OO0 ):#line:260
        try :#line:261
            O00O000000000O0OO =timi_new ()#line:262
            OO0O00O000OOOOO0O =f'type=crop__{O00O000000000O0OO}'#line:263
            O0O0000O0OOO0OOOO ={'source':'scsc','authorization':O0000000O0000O00O .token ,'timestamp':str (O00O000000000O0OO ),'sign':sign (OO0O00O000OOOOO0O ),'signstring':OO0O00O000OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            OO0O00OO0000000O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0000O0OOO0OOOO ).json ()#line:275
            if 'status'in OO0O00OO0000000O0 :#line:277
                if OO0O00OO0000000O0 ['status']==200 :#line:278
                    if OO0O00OO0000000O0 ['data']['rows']:#line:279
                        OO00O000OOOO0OO0O =OO0O00OO0000000O0 ['data']['rows'][0 ]['packsackItemId']#line:280
                        O000OO000OO0000O0 =OO0O00OO0000000O0 ['data']['rows'][0 ]['quantity']#line:281
                        OO0O0OO0OOOOOO000 =float (OOO0O0O00OOOO0OO0 )+float (random .randint (1 ,99 )*0.001 )#line:282
                        OO0OO000O000OOO00 =f'_packsackItemId={OO00O000OOOO0OO0O}&price={str(OO0O0OO0OOOOOO000)[:6]}&quantity={O000OO000OO0000O0}_{O00O000000000O0OO}'#line:283
                        O000OO0OO00OO0O00 ={'source':'scsc','authorization':O0000000O0000O00O .token ,'timestamp':str (O00O000000000O0OO ),'sign':sign (OO0OO000O000OOO00 ),'signstring':OO0OO000O000OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
                        OO0O0O00OO0OO0O00 ={"packsackItemId":OO00O000OOOO0OO0O ,"price":str (OO0O0OO0OOOOOO000 )[:6 ],"quantity":str (O000OO000OO0000O0 )}#line:299
                        OO00000OO0OO0O00O =requests .request ('post',f'{host}/market/sale',headers =O000OO0OO00OO0O00 ,data =OO0O0O00OO0OO0O00 ).json ()#line:300
                        if 'status'in OO00000OO0OO0O00O :#line:302
                            if OO00000OO0OO0O00O ['status']==200 :#line:303
                                print (f'【上架芦荟】:数量:{O000OO000OO0000O0}丨价格:{str(OO0O0OO0OOOOOO000)[:6]}')#line:304
        except Exception as OO0O0000O0000O000 :#line:305
            print (OO0O0000O0000O000 )#line:306
    def query_to_sell (OO0OOO0OOO0O0OOOO ):#line:309
        try :#line:310
            O00O0O0OOOOOOO0OO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:311
            O0OO0O00OO0O0000O ={'source':'scsc','authorization':OO0OOO0OOO0O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O0OOOOOOO0OO ),'signstring':O00O0O0OOOOOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:322
            O0OOOO0O0O0OOO000 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO0O00OO0O0000O ).json ()#line:324
            if 'status'in O0OOOO0O0O0OOO000 :#line:326
                if O0OOOO0O0O0OOO000 ['status']==200 :#line:327
                    for OOO000000O0OOOO00 in O0OOOO0O0O0OOO000 ['data']['rows']:#line:328
                        O0O00O00OOOO000OO =OOO000000O0OOOO00 ['materialKey']#line:329
                        O0OO0000OO0O000O0 =OOO000000O0OOOO00 ['quantity']#line:330
                        OOO0O0OOOOO000OOO =OOO000000O0OOOO00 ['price']#line:331
                        OO0OO0OO000000O00 =OOO000000O0OOOO00 ['saleState']#line:332
                        if OO0OO0OO000000O00 ==0 :#line:333
                            print (f'【出售订单】:名称:{O0O00O00OOOO000OO}丨数量:{O0OO0000OO0O000O0}丨价格:{OOO0O0OOOOO000OOO}')#line:334
                            O00OOO0O0O000000O =OOO000000O0OOOO00 ['id']#line:335
                            OO0OOO0OOO0O0OOOO .cacel_sale (O00OOO0O0O000000O )#line:336
        except Exception as OO000O00O0000O00O :#line:337
            print (OO000O00O0000O00O )#line:338
    def cacel_sale (OO000O0000OOOOOOO ,OOOOOO000O0O0OO00 ):#line:342
        try :#line:343
            O00OOOO0O0O00OO00 =f'_saleId={OOOOOO000O0O0OO00}_{timi_new()}'#line:344
            OOO0O00OOOOOOOO00 ={'source':'scsc','authorization':OO000O0000OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO0O0O00OO00 ),'signstring':O00OOOO0O0O00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:355
            O0O0OO0OO0000OOOO ={"saleId":OOOOOO000O0O0OO00 }#line:358
            OOO0OO00O000O00O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO0O00OOOOOOOO00 ,data =O0O0OO0OO0000OOOO ).json ()#line:359
            if 'status'in OOO0OO00O000O00O0 :#line:361
                if OOO0OO00O000O00O0 ['status']==200 :#line:362
                    print (f'【下架出售】:{OOO0OO00O000O00O0["data"]}')#line:363
        except Exception as O0000OO00OOOOO0OO :#line:364
            print (O0000OO00OOOOO0OO )#line:365
    def change_nickname (OOOOO0OOOO00OOOOO ):#line:372
        try :#line:373
            OO0OOOO00OO0O00O0 =timi_new ()#line:374
            O0000000O0O00OOOO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:375
            OOO0OOOOOOOOOOOO0 =requests .request ('post','https://www.qmsjmfb.com/',data =O0000000O0O00OOOO ).text #line:376
            O00O00OOOO0O0OO00 =re .findall ('<ul><li>(.*?)</li>',OOO0OOOOOOOOOOOO0 )[0 ][:3 ]#line:377
            OOOOO0000OOOOO0O0 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={O00O00OOOO0O0OO00}').json ()#line:378
            OOOO00OO000O000O0 =OOOOO0000OOOOO0O0 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:379
            O00OO0000O0OOO0OO ={"nickname":OOOO00OO000O000O0 }#line:380
            O0OOO00O0000000OO =f'_nickname={OOOO00OO000O000O0}_{OO0OOOO00OO0O00O0}'#line:381
            O0O000OOOO00OO000 ={'source':'scsc','authorization':OOOOO0OOOO00OOOOO .token ,'timestamp':OO0OOOO00OO0O00O0 ,'sign':sign (O0OOO00O0000000OO ),'signstring':O0OOO00O0000000OO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:392
            O00OOO0OO000O0OO0 =requests .request ('patch',f'{host}/user/nickname',headers =O0O000OOOO00OO000 ,data =O00OO0000O0OOO0OO ).json ()#line:393
            if 'status'in O00OOO0OO000O0OO0 :#line:395
                if O00OOO0OO000O0OO0 ['status']==200 :#line:396
                    print (f'【修改网名】:网名:{OOOO00OO000O000O0}丨{O00OOO0OO000O0OO0["message"]}')#line:397
        except Exception as OO0OO0OO0OO0O0O0O :#line:398
            print (OO0OO0OO0OO0O0O0O )#line:399
    def withdraw (OO0OOO00O00O0OOO0 ):#line:404
        try :#line:405
            OO00O0000O0O0O00O =f'__{timi_new()}'#line:406
            OOO00OO0O000OO0OO ={'source':'scsc','authorization':OO0OOO00O00O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000O0O0O00O ),'signstring':OO00O0000O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            O00O0OO00000OO0OO =requests .request ('get',f'{host}/assets',headers =OOO00OO0O000OO0OO ).json ()#line:418
            if 'status'in O00O0OO00000OO0OO :#line:420
                if O00O0OO00000OO0OO ['status']==200 :#line:421
                    O0OO0O0O00OO0OO00 =O00O0OO00000OO0OO ['data']['cash']#line:422
                    if float (O0OO0O0O00OO0OO00 )>20 :#line:423
                        OO00O0000O0O0O00O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:424
                        OOO00OO0O000OO0OO ={'authorization':OO0OOO00O00O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0000O0O0O00O ),'signstring':OO00O0000O0O0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:434
                        OOOO00OO0O00O0O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:435
                        OOO0OOOOOO000O000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO00OO0O000OO0OO ,data =OOOO00OO0O00O0O00 ).json ()#line:436
                        if 'status'in OOO0OOOOOO000O000 :#line:438
                            if OOO0OOOOOO000O000 ['status']==200 :#line:439
                                print (f'【余额提现】:{OOO0OOOOOO000O000["data"]}')#line:440
                        if 'status'in OOO0OOOOOO000O000 :#line:441
                            if OOO0OOOOOO000O000 ['status']==500 :#line:442
                                print (f'【余额提现】:{OOO0OOOOOO000O000["message"]}')#line:443
        except Exception as O000O0OOO0O0O000O :#line:444
            print (O000O0OOO0O0O000O )#line:445
    def invitenum (OOO00O00O000O0OOO ):#line:449
        global invited_new #line:450
        try :#line:451
            O0OOO0OOO000O0O0O =f'__{timi_new()}'#line:452
            O00O0000O0OOOOO0O ={'source':'scsc','authorization':OOO00O00O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0OOO000O0O0O ),'signstring':O0OOO0OOO000O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            O00O00000000OOOOO =requests .request ('get',f'{host}/invite/invitenum',headers =O00O0000O0OOOOO0O ).json ()#line:464
            if 'status'in O00O00000000OOOOO :#line:466
                if O00O00000000OOOOO ['status']==200 :#line:467
                    O00OOOO0O0O000000 =O00O00000000OOOOO ['data']['invited_count']#line:468
                    OO000O0000O000OO0 =O00O00000000OOOOO ['data']['invited_second_count']#line:469
                    print (f'【我的邀请】:直邀好友:{O00OOOO0O0O000000}丨间邀好友:{OO000O0000O000OO0}')#line:470
                    if O00OOOO0O0O000000 <2 :#line:471
                        O0O00O0OOO00OOO0O =f'__{timi_new()}'#line:472
                        O0OOO00OO000OOO00 ={'source':'scsc','authorization':OOO00O00O000O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OOO00OOO0O ),'signstring':O0O00O0OOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        OOOO0O000O0OOOOO0 =requests .request ('get',f'{host}/user',headers =O0OOO00OO000OOO00 ).json ()#line:484
                        if 'status'in OOOO0O000O0OOOOO0 :#line:486
                            if OOOO0O000O0OOOOO0 ['status']==200 :#line:487
                                invited_new .append (OOOO0O000O0OOOOO0 ['data']['inner_id'])#line:488
        except Exception as O00O0OOO0OOO0OO00 :#line:489
            print (O00O0OOO0OOO0OO00 )#line:490
    def game_map (OOO0O00O0O0O0O0O0 ):#line:494
        try :#line:495
            O0O0O0O00OO0O00OO =f'__{timi_new()}'#line:496
            OOO0O0O000000O0OO ={'source':'scsc','authorization':OOO0O00O0O0O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0O00OO0O00OO ),'signstring':O0O0O0O00OO0O00OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            OOO00O00OO00OOO0O =requests .request ('get',f'{host}/game/map',headers =OOO0O0O000000O0OO ).json ()#line:508
            if 'status'in OOO00O00OO00OOO0O :#line:510
                if OOO00O00OO00OOO0O ['status']==200 :#line:511
                    for O0OO0O0O00OOO0O00 in OOO00O00OO00OOO0O ['data']['list'][0 ]['crops']:#line:512
                        OO0OOO0000OOO0OO0 =O0OO0O0O00OOO0O00 ['level']#line:514
                        if OO0OOO0000OOO0OO0 ==41 :#line:515
                            OOO000O000OOOO00O =O0OO0O0O00OOO0O00 ['crop_name']#line:516
                            O0O0OO0000O0O0OO0 =O0OO0O0O00OOO0O00 ['count']#line:517
                            if O0O0OO0000O0O0OO0 >0 :#line:518
                                print (f'【农业资产】:{OOO000O000OOOO00O}丨数量:{O0O0OO0000O0O0OO0}')#line:519
                                OOO0O00O0O0O0O0O0 .the_query ()#line:520
        except Exception as OOOO0O0OO00OO00OO :#line:521
            print (OOOO0O0OO00OO00OO )#line:522
    def give_gold (O000OO0OOOO000OO0 ):#line:525
        try :#line:526
            O0O0OO0OOO00O0O0O =f'__{timi_new()}'#line:527
            O00O0OOOOOO00OOOO ={'source':'scsc','authorization':O000OO0OOOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOO00O0O0O ),'signstring':O0O0OO0OOO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            OOO0OO00OOO0O00OO =requests .request ('get',f'{host}/user',headers =O00O0OOOOOO00OOOO ).json ()#line:539
            if 'status'in OOO0OO00OOO0O00OO :#line:540
                if OOO0OO00OOO0O00OO ['status']==200 :#line:541
                    if float (O000OO0OOOO000OO0 .doneeNo )!=0 :#line:542
                        OO00OO0OO00OOOO00 =OOO0OO00OOO0O00OO ['data']['assets']['gold']#line:543
                        if float (OO00OO0OO00OOOO00 )>float (O000OO0OOOO000OO0 .innerId ):#line:544
                            O0000O00O000O0O0O =int (float (OO00OO0OO00OOOO00 )/1.1 )#line:545
                            O0O0OO0OOO00O0O0O =f'_doneeNo={O000OO0OOOO000OO0.doneeNo}&quantity={O0000O00O000O0O0O}_{timi_new()}'#line:546
                            O00O0OOOOOO00OOOO ={'source':'scsc','authorization':O000OO0OOOO000OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO0OOO00O0O0O ),'signstring':O0O0OO0OOO00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
                            O0O0OOO0OO0000OO0 ={"quantity":O0000O00O000O0O0O ,"doneeNo":O000OO0OOOO000OO0 .doneeNo }#line:561
                            OO0OO000OO00OO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O00O0OOOOOO00OOOO ,data =O0O0OOO0OO0000OO0 ).json ()#line:562
                            if 'status'in OO0OO000OO00OO0OO :#line:564
                                if OO0OO000OO00OO0OO ['status']==200 :#line:565
                                    if OO0OO000OO00OO0OO ['data']:#line:566
                                        print (f'【赠送种子】:赠送{O0000O00O000O0O0O}种子给{O000OO0OOOO000OO0.doneeNo}成功')#line:567
                    else :#line:568
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:569
        except Exception as O0O000O0OOO0OO000 :#line:570
            print (O0O000O0OOO0OO000 )#line:571
    def invitation (OOOO0O000O0O0O000 ):#line:573
        try :#line:574
            _O000000OO0OO0O00O =float (bundled_def ())/4 #line:575
            O00OOO00OOO000O0O =f'_innerId={int(_O000000OO0OO0O00O)}_{timi_new()}'#line:576
            O00000OOOO0O000O0 ={'source':'scsc','authorization':OOOO0O000O0O0O000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00OOO000O0O ),'signstring':O00OOO00OOO000O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            OO0O0OO0OO0000OO0 ={"innerId":int (_O000000OO0OO0O00O )}#line:588
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00000OOOO0O000O0 ,data =OO0O0OO0OO0000OO0 )#line:589
        except Exception as OOOO00000OO0O00O0 :#line:590
            print (OOOO00000OO0O00O0 )#line:591
    def winning_rewards (OOO00OOO0O0000O0O ):#line:594
        try :#line:595
            O0000OOO0O0O0OO00 =f'__{timi_new()}'#line:596
            O0000O0O0000OO0O0 ={'source':'scsc','authorization':OOO00OOO0O0000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOO0O0O0OO00 ),'signstring':O0000OOO0O0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
            OO00OO00O0O00O000 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O0000O0O0000OO0O0 ).json ()#line:608
            if 'status'in OO00OO00O0O00O000 :#line:610
                if OO00OO00O0O00O000 ['status']==200 :#line:611
                    if OO00OO00O0O00O000 ['data']['amount']:#line:612
                        OO0OO0O0OOO00OO0O =OO00OO00O0O00O000 ['data']['amount']['gold']#line:613
                        return OO0OO0O0OOO00OO0O #line:614
                    else :#line:615
                        return 0 #line:616
        except Exception as O0O0OOO0OO0OO00O0 :#line:617
            print (O0O0OOO0OO0OO00O0 )#line:618
    def certification (O0OO0000000OO0OOO ):#line:621
        try :#line:622
            O00O0O000O00000OO =f'__{timi_new()}'#line:623
            O0000OOOO00OO0OO0 ={'source':'scsc','authorization':O0OO0000000OO0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0O000O00000OO ),'signstring':O00O0O000O00000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            O000OO00000000000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0000OOOO00OO0OO0 ).json ()#line:635
            if 'status'in O000OO00000000000 :#line:637
                if O000OO00000000000 ['status']==200 :#line:638
                    if O000OO00000000000 ['data']['result']:#line:639
                        OO00OO000O0OO00O0 =O000OO00000000000 ['data']['nick_name']#line:640
                        return OO00OO000O0OO00O0 #line:641
                    else :#line:642
                        return '未实名'#line:643
        except Exception as OO00O000O00O00O0O :#line:644
            print (OO00O000O00O00O0O )#line:645
    def crops_illustrated (O0OO0OOOO0000OOO0 ):#line:648
        try :#line:649
            OOO0O0OOO0000000O =f'__{timi_new()}'#line:650
            O0OOO0O0OO0O00O0O ={'source':'scsc','authorization':O0OO0OOOO0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0000000O ),'signstring':OOO0O0OOO0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:661
            O0OO000O000OO00OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0OOO0O0OO0O00O0O ).json ()#line:662
            if 'status'in O0OO000O000OO00OO :#line:664
                if O0OO000O000OO00OO ['status']==200 :#line:665
                    O0000O00OO00O000O =O0OO000O000OO00OO ['data'][0 ]['crops']#line:666
                    for OO0000O0O00OOO0O0 in O0000O00OO00O000O :#line:667
                        if OO0000O0O00OOO0O0 ['ill_clover_award']:#line:668
                            if float (OO0000O0O00OOO0O0 ['ill_clover_award'])>1 :#line:669
                                if OO0000O0O00OOO0O0 ['is_finish']:#line:670
                                    if not OO0000O0O00OOO0O0 ['is_getit']:#line:671
                                        if O0OO0OOOO0000OOO0 .certification ()!='未实名':#line:672
                                            OOO0O0OOO0000000O =f'_award_level={OO0000O0O00OOO0O0["level"]}_{timi_new()}'#line:673
                                            O0OOO0O0OO0O00O0O ={'source':'scsc','authorization':O0OO0OOOO0000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OOO0000000O ),'signstring':OOO0O0OOO0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
                                            OO00O0OOOOO0O0O00 ={"award_level":OO0000O0O00OOO0O0 ['level']}#line:685
                                            O0O0OOOOOOOOOO0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0OOO0O0OO0O00O0O ,json =OO00O0OOOOO0O0O00 ).json ()#line:687
                                            if 'status'in O0O0OOOOOOOOOO0OO :#line:688
                                                if O0O0OOOOOOOOOO0OO ['status']==200 :#line:689
                                                    O0O0OO0000O0OO0O0 =O0O0OOOOOOOOOO0OO ['data']['ill_clover_award']#line:690
                                                    print (f'【图鉴奖励】:领取{OO0000O0O00OOO0O0["crop_name"]}成就丨奖励{O0O0OO0000O0OO0O0}☘️')#line:692
                                                if O0O0OOOOOOOOOO0OO ['status']==500 :#line:693
                                                    print (f'【图鉴奖励】:{O0O0OOOOOOOOOO0OO["message"]}')#line:694
        except Exception as OO00O00000OO00OOO :#line:695
            print (OO00O00000OO00OOO )#line:696
    def watched_ad (O00000O000O00OOO0 ):#line:699
        try :#line:700
            OO0O0000OO0O00O00 =f'__{timi_new()}'#line:701
            O00O00OOOO000O0O0 ={'source':'scsc','authorization':O00000O000O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0000OO0O00O00 ),'signstring':OO0O0000OO0O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:712
            O00OO000O00O00O0O =requests .request ('get',f'{host}/game/getAllData',headers =O00O00OOOO000O0O0 ).json ()#line:713
            if 'status'in O00OO000O00O00O0O :#line:715
                if O00OO000O00O00O0O ['status']==200 :#line:716
                    if 'offlineInfo'in O00OO000O00O00O0O ['data']:#line:717
                        time .sleep (random .randint (1 ,3 ))#line:718
                        O0000O0O000O00000 =O00OO000O00O00O0O ['data']['offlineInfo']['off_minute']#line:719
                        OO00OOOO00OO00OO0 =float (O00OO000O00O00O0O ['data']['silver'])/1000000000000 #line:720
                        time .sleep (1 )#line:721
                        requests .request ('post',f'{host}/game/watched-ad',headers =O00O00OOOO000O0O0 ).json ()#line:722
                        time .sleep (2 )#line:723
                        OOO0O0OO0OO0000O0 =requests .request ('get',f'{host}/game/getAllData',headers =O00O00OOOO000O0O0 ).json ()#line:724
                        if 'status'in OOO0O0OO0OO0000O0 :#line:726
                            if OOO0O0OO0OO0000O0 ['status']==200 :#line:727
                                O000000O0O0OOOO0O =float (OOO0O0OO0OO0000O0 ['data']['silver'])/1000000000000 #line:728
                                O00O0O0OO0O0O0O0O =str (O000000O0O0OOOO0O -OO00OOOO00OO00OO0 )[:6 ]#line:729
                                print (f'【离线奖励】:翻倍离线{O0000O0O000O00000}分钟奖励🌱数量:{O00O0O0OO0O0O0O0O}t粒')#line:730
        except Exception as OO0OOO00O000000O0 :#line:731
            print (OO0OOO00O000000O0 )#line:732
    def user_ad (OO0000OO0O0O0OOO0 ):#line:735
        try :#line:736
            OOO00O000OOOOOO0O =f'__{timi_new()}'#line:737
            OOO00O0OOOOO00OOO ={'source':'scsc','authorization':OO0000OO0O0O0OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O000OOOOOO0O ),'signstring':OOO00O000OOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:748
            OOOO000OOOO0OO0OO =requests .request ('get',f'{host}/user/ad',headers =OOO00O0OOOOO00OOO ).json ()#line:749
            if 'status'in OOOO000OOOO0OO0OO :#line:751
                if OOOO000OOOO0OO0OO ['status']==200 :#line:752
                    OO0O0OOO00OO00OO0 =OOOO000OOOO0OO0OO ['data']['max_time']#line:753
                    OO0O00OOOOOO000O0 =OOOO000OOOO0OO0OO ['data']['watch_time']#line:754
                    OO000OOO000O000O0 =OOOO000OOOO0OO0OO ['data']['added_time']#line:755
                    print (f'【获取种子】:获取🌱剩余{OO000OOO000O000O0 + OO0O0OOO00OO00OO0 - OO0O00OOOOOO000O0}次丨好友提供:{OO000OOO000O000O0}次')#line:756
                    if OO000OOO000O000O0 +OO0O0OOO00OO00OO0 -OO0O00OOOOOO000O0 >0 :#line:757
                        time .sleep (random .randint (16 ,19 ))#line:758
                        OOOO0O0O0OOOO000O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00O0OOOOO00OOO ).json ()#line:759
                        if 'status'in OOOO0O0O0OOOO000O :#line:761
                            if OOOO0O0O0OOOO000O ['status']==200 :#line:762
                                O00O0000000O0OO00 =float (OOOO0O0O0OOOO000O ['data']['silver'])/1000000000000 #line:763
                                print (f'【获取种子】:获得🌱:{int(O00O0000000O0OO00)}t粒')#line:764
                                return True #line:765
                            if OOOO0O0O0OOOO000O ['status']==500 :#line:766
                                OOO000000O0OO0O00 =OOOO0O0O0OOOO000O ['message']#line:767
                                print (f'【获取种子】:{OOO000000O0OO0O00}')#line:768
                                return False #line:769
        except Exception as O0OOOOO0000000OO0 :#line:770
            print (O0OOOOO0000000OO0 )#line:771
    def synthetic (O0OOOOO00O0000OOO ):#line:774
        global id ,g #line:775
        try :#line:776
            O0000OO0OOOO0O0O0 =O0OOOOO00O0000OOO .level_new ()#line:777
            O00OO0000O00O0O00 =random .randint (9 ,11 )#line:778
            OO0O0OOOO00OO00O0 =f'_site=8&targetSite={O00OO0000O00O0O00}_{timi_new()}'#line:779
            OO0O00OO00O0000O0 ={'source':'scsc','authorization':O0OOOOO00O0000OOO .token ,'timestamp':timi_new (),'sign':sign (OO0O0OOOO00OO00O0 ),'signstring':OO0O0OOOO00OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:790
            OO0O0O0O0OOOOOOO0 ={"site":int (8 ),"targetSite":int (O00OO0000O00O0O00 )}#line:791
            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OO00O0000O0 ,json =OO0O0O0O0OOOOOOO0 )#line:792
            while True :#line:793
                OO0OOOO0O00O00OOO =f'__{timi_new()}'#line:794
                OOOO0OOO000O00OO0 ={'source':'scsc','authorization':O0OOOOO00O0000OOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0O00O00OOO ),'signstring':OO0OOOO0O00O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:805
                OO0OOOOO0OOOO00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OOO000O00OO0 ).json ()#line:806
                if 'status'in OO0OOOOO0OOOO00O0 :#line:808
                    if OO0OOOOO0OOOO00O0 ['status']==200 :#line:809
                        OOOOO00OOOO0OOOOO =OO0OOOOO0OOOO00O0 ['data']['cropList']#line:810
                        OOOO00O000000OO0O =OO0OOOOO0OOOO00O0 ['data']['gameCoreDataDBid']#line:811
                        OO000OO000O0OO0O0 =float (OO0OOOOO0OOOO00O0 ['data']['silver'])/1000000000000 #line:812
                        OO00OO0OOO0OO0O0O =0 #line:817
                        for O00O00O00000O0000 in OOOOO00OOOO0OOOOO :#line:818
                            if not O00O00O00000O0000 :#line:819
                                OO0OO0O0OO00OOOO0 =f'_crop_id={OOOO00O000000OO0O}&site={OO00OO0OOO0OO0O0O}_{O0OOOOO00O0000OOO.time}'#line:820
                                O00O00O0O0O0OOOOO ={'source':'scsc','authorization':O0OOOOO00O0000OOO .token ,'timestamp':O0OOOOO00O0000OOO .time ,'sign':sign (OO0OO0O0OO00OOOO0 ),'signstring':OO0OO0O0OO00OOOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:830
                                O0O00O00OO0O00000 ={"site":OO00OO0OOO0OO0O0O ,"crop_id":OOOO00O000000OO0O }#line:831
                                OOOO0OO000OO0000O =requests .request ('post',f'{host}/game/crops/buy',headers =O00O00O0O0O0OOOOO ,data =O0O00O00OO0O00000 ).json ()#line:832
                                time .sleep (random .randint (1 ,3 )/10 )#line:834
                                if 'status'in OOOO0OO000OO0000O :#line:835
                                    if OOOO0OO000OO0000O ['status']==200 :#line:836
                                        if OOOO0OO000OO0000O ['message']=='种子数量不足':#line:837
                                            O0000OO0OOOO0O0O0 =O0OOOOO00O0000OOO .level_new ()#line:838
                                            print (f'【种植合成】:{OOOO0OO000OO0000O["message"]}')#line:839
                                            if not O0OOOOO00O0000OOO .user_ad ():#line:840
                                                return False #line:841
                                    if OOOO0OO000OO0000O ['status']==500 :#line:842
                                        print (f'【种植合成】:{OOOO0OO000OO0000O["message"]}')#line:843
                                        return False #line:844
                            OO00OO0OOO0OO0O0O +=1 #line:845
                        O0OOO0OOOO0OO000O =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0OOO000O00OO0 ).json ()#line:846
                        OOO0O0000O0O00OOO =O0OOO0OOOO0OO000O ['data']['cropList']#line:847
                        O00O00OOO000OO0OO =False #line:848
                        for O00O00O00000O0000 in range (12 ):#line:849
                            id =OOO0O0000O0O00OOO [O00O00O00000O0000 ]['level']#line:850
                            if float (O0000OO0OOOO0O0O0 )-float (id )>9 :#line:851
                                OO0OO00O0O0OO00O0 =f'_site={O00O00O00000O0000}_{timi_new()}'#line:852
                                O000O0O0000O0O00O ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OOOOO00O0000OOO .token ,'timestamp':timi_new (),'sign':sign (OO0OO00O0O0OO00O0 ),'signstring':OO0OO00O0O0OO00O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:863
                                OO0000OOOOOO00OO0 ={"site":O00O00O00000O0000 }#line:864
                                O00O0000000OO0000 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =O000O0O0000O0O00O ,data =OO0000OOOOOO00OO0 ).json ()#line:866
                                if 'status'in O00O0000000OO0000 :#line:867
                                    if O00O0000000OO0000 ['status']==200 :#line:868
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:869
                            if id !=0 :#line:870
                                for O0OO00O0OO00O000O in range (11 ):#line:871
                                    O0O00OOOO0OOO0O0O =O0OO00O0OO00O000O +1 #line:872
                                    g =OOO0O0000O0O00OOO [O0O00OOOO0OOO0O0O ]['level']#line:873
                                    if id ==g :#line:874
                                        O0OOOOO00000O0O00 =O0OO00O0OO00O000O +2 #line:875
                                        if O0OOOOO00000O0O00 !=O00O00O00000O0000 +1 :#line:876
                                            OOO000O0000O00OOO =O00O00O00000O0000 +1 #line:877
                                            time .sleep (random .randint (1 ,3 )/10 )#line:879
                                            OO0O0OOOO00OO00O0 =f'_site={OOO000O0000O00OOO - 1}&targetSite={O0OOOOO00000O0O00 - 1}_{timi_new()}'#line:880
                                            OO0O00OO00O0000O0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O0OOOOO00O0000OOO .token ,'timestamp':timi_new (),'sign':sign (OO0O0OOOO00OO00O0 ),'signstring':OO0O0OOOO00OO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:897
                                            OOO0O0O0O00OO000O ={"site":int (OOO000O0000O00OOO -1 ),"targetSite":int (O0OOOOO00000O0O00 -1 )}#line:898
                                            requests .request ('post',f'{host}/game/crops/move',headers =OO0O00OO00O0000O0 ,json =OOO0O0O0O00OO000O )#line:899
                                            O00O00OOO000OO0OO =True #line:901
                                    if O00O00OOO000OO0OO :#line:902
                                        break #line:903
                                if O00O00OOO000OO0OO :#line:904
                                    break #line:905
        except :#line:906
            O0OOOOO00O0000OOO .synthetic ()#line:907
    def level_new (O0OO000O00O0O000O ):#line:910
        try :#line:911
            OOOOO000O0OOO0000 =f'__{timi_new()}'#line:912
            O0OO0O00O00OOO00O ={'source':'scsc','authorization':O0OO000O00O0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO000O0OOO0000 ),'signstring':OOOOO000O0OOO0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:923
            O0O00O00000000OOO =requests .request ('get',f'{host}/user',headers =O0OO0O00O00OOO00O ).json ()#line:924
            if 'status'in O0O00O00000000OOO :#line:925
                if O0O00O00000000OOO ['status']==200 :#line:926
                    return float (O0O00O00000000OOO ['data']['level'])#line:927
        except Exception as O00OO0O0O0O000OO0 :#line:928
            print (O00OO0O0O0O000OO0 )#line:929
    def propsraffle (O00O00OOOOOOOOOO0 ):#line:932
        try :#line:933
            while True :#line:934
                O00000OOOO00OO00O =f'__{timi_new()}'#line:935
                O000O0000O0OO000O ={'source':'scsc','authorization':O00O00OOOOOOOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOOO00OO00O ),'signstring':O00000OOOO00OO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:946
                OOOOO0O00OO0OOOO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O000O0000O0OO000O ).json ()#line:947
                if 'status'in OOOOO0O00OO0OOOO0 :#line:949
                    if OOOOO0O00OO0OOOO0 ['status']==200 :#line:950
                        O000OO0OOOO0O0000 =OOOOO0O00OO0OOOO0 ['data']['rows']#line:951
                        O0O00O0OOO00OO00O =OOOOO0O00OO0OOOO0 ['data']['vstate']#line:952
                        if O000OO0OOOO0O0000 ==5 or O000OO0OOOO0O0000 ==6 or O000OO0OOOO0O0000 ==7 :#line:953
                            OOO00000OO00O0O0O =OOOOO0O00OO0OOOO0 ['data']['silver']#line:954
                            print (f'【转盘抽奖】:获得种子:{OOO00000OO00O0O0O}')#line:955
                        if O000OO0OOOO0O0000 ==1 or O000OO0OOOO0O0000 ==2 or O000OO0OOOO0O0000 ==3 :#line:956
                            O0000O0O0OO00O0OO =OOOOO0O00OO0OOOO0 ['data']['clover']#line:957
                            print (f'【转盘抽奖】:获得三叶草:{O0000O0O0OO00O0OO}')#line:958
                        if O000OO0OOOO0O0000 ==4 or O000OO0OOOO0O0000 ==8 :#line:959
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:960
                        if O000OO0OOOO0O0000 =='抽奖次数已用完':#line:964
                            break #line:998
                time .sleep (random .randint (8 ,15 )/10 )#line:999
        except Exception as OOOO000OOOO0O0O0O :#line:1000
            print (OOOO000OOOO0O0O0O )#line:1001
    def friends_invitation (O0OOO0OO0OOO0000O ):#line:1004
        try :#line:1005
            OOO0000OO0O00000O =f'__{timi_new()}'#line:1006
            OOO000OOOO00O0O00 ={'source':'scsc','authorization':O0OOO0OO0OOO0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OO0O00000O ),'signstring':OOO0000OO0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1017
            O0OOOOO0O0OOOO00O =requests .request ('get',f'{host}/friends',headers =OOO000OOOO00O0O00 ).json ()#line:1018
            if 'status'in O0OOOOO0O0OOOO00O :#line:1019
                if O0OOOOO0O0OOOO00O ['status']==200 :#line:1020
                    O00OOOO00O0OOOOOO =O0OOOOO0O0OOOO00O ['data']['myInviteter']#line:1021
                    if O00OOOO00O0OOOOOO :#line:1022
                        OO0000OO0O0O0O0O0 =O00OOOO00O0OOOOOO ['user']['nickname']#line:1023
                        O0000000O00OO0000 =O0OOO0OO0OOO0000O .certification ()#line:1024
                        print (f'【查邀请人】:我的邀请人:{OO0000OO0O0O0O0O0}丨实名:{O0000000O00OO0000}')#line:1025
                    else :#line:1026
                        if O0OOO0OO0OOO0000O .innerId !='0':#line:1027
                            O0OOO0OO0OOO0000O .invitation ()#line:1028
        except Exception as OO000OO00O0O0OO00 :#line:1029
            print (OO000OO00O0O0OO00 )#line:1030
    def add_clover (OOOO00O0OO00000OO ):#line:1033
        global golden_seed #line:1034
        try :#line:1035
            OO00000OO0000O000 =f'__{timi_new()}'#line:1036
            O0OOOOO000O0000OO ={'source':'scsc','authorization':OOOO00O0OO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0000O000 ),'signstring':OO00000OO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1047
            O0O0OOOOO00OO0O00 =requests .request ('get',f'{host}/assets/clovers',headers =O0OOOOO000O0000OO ).json ()#line:1048
            if 'status'in O0O0OOOOO00OO0O00 :#line:1050
                if O0O0OOOOO00OO0O00 ['status']==200 :#line:1051
                    O00OO00OOO0O0O00O =O0O0OOOOO00OO0O00 ['data']['clover']#line:1052
                    OOO0OO0OOOO0O000O =O0O0OOOOO00OO0O00 ['data']['used_clover']#line:1053
                    OOO0OO0OO0O000OOO =float (O00OO00OOO0O0O00O )-float (OOO0OO0OOOO0O000O )#line:1054
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOO0OO0OOOO0O000O}')#line:1055
                    if OOOO00O0OO00000OO .certification ()!='未实名':#line:1056
                        if OOO0OO0OO0O000OOO >1 :#line:1057
                            OO00000OO0000O000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO0OO0OO0O000OOO)}_{timi_new()}'#line:1058
                            O0OO0O0OO0O00O0O0 ={'source':'scsc','authorization':OOOO00O0OO00000OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00000OO0000O000 ),'signstring':OO00000OO0000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1069
                            O0OO000OO00000O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO0OO0OO0O000OOO )}#line:1070
                            O00O0O000OOO00O0O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0O0OO0O00O0O0 ,data =O0OO000OO00000O0O ).json ()#line:1071
                            if 'status'in O00O0O000OOO00O0O :#line:1073
                                if O00O0O000OOO00O0O ['status']==200 :#line:1074
                                    print (f'【参与抽奖】:添加☘️:{O00O0O000OOO00O0O["data"]}丨数量:{OOO0OO0OO0O000OOO}')#line:1075
                                if O00O0O000OOO00O0O ['status']==500 :#line:1076
                                    print (f'【参与抽奖】:添加☘️:{O00O0O000OOO00O0O["message"]}')#line:1077
            OOOO0OO000O00OOOO =requests .request ('get',f'{host}/lottery',headers =O0OOOOO000O0000OO ).json ()#line:1078
            OO000OOOO0O0OO0OO =OOOO00O0OO00000OO .winning_rewards ()#line:1080
            if 'status'in OOOO0OO000O00OOOO :#line:1081
                if OOOO0OO000O00OOOO ['status']==200 :#line:1082
                    O00OOO0O0OOOOO000 =OOOO0OO000O00OOOO ['data'][0 ]['day_get_gold_quantity']#line:1083
                    golden_seed +=float (O00OOO0O0OOOOO000 )#line:1084
                    O0OOOOO00O0OO0000 =OOOO0OO000O00OOOO ['data'][1 ]['value']#line:1085
                    OO0OO0O0000O0O00O =OOOO0OO000O00OOOO ['data'][0 ]['join_number']#line:1086
                    OO0O00O00000000O0 =int (float (OOOO0OO000O00OOOO ['data'][0 ]['totalValue']))#line:1087
                    OO00OOOO0O000O000 =float (O0OOOOO00O0OO0000 /OO0O00O00000000O0 )*10000 #line:1088
                    O000OOOOOOO0OOOO0 =OO0O00O00000000O0 /OO0OO0O0000O0O00O #line:1089
                    print (f'【参与抽奖】:预计每天中{str(O00OOO0O0OOOOO000)[:6]}颗金种子丨好友收益:{str(OO000OOOO0O0OO0OO)[:6]}')#line:1090
                    print (f'【抽奖统计】:每1万☘️中{str(OO00OOOO0O000O000)[:6]}颗金种子丨☘️人均:{str(O000OOOOOOO0OOOO0)[:7]}️')#line:1091
        except Exception as OOO00O0OOOO0O0O0O :#line:1092
            print (OOO00O0OOOO0O0O0O )#line:1093
    def energy (O0O0OOO00O0OOO0OO ):#line:1097
        try :#line:1098
            while True :#line:1099
                O00O00OOO0OO0O00O =f'__{timi_new()}'#line:1100
                OO00OOO00OO0OOO0O ={'source':'scsc','authorization':O0O0OOO00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OOO0OO0O00O ),'signstring':O00O00OOO0OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1111
                OOOOOOOO0O00O0O0O =requests .request ('get',f'{host}/energy/general',headers =OO00OOO00OO0OOO0O ).json ()#line:1112
                if 'status'in OOOOOOOO0O00O0O0O :#line:1114
                    if OOOOOOOO0O00O0O0O ['status']==200 :#line:1115
                        O0000OO00O0OOOO0O =OOOOOOOO0O00O0O0O ['data']['ordinary_water']#line:1116
                        O000000O0000OO00O =OOOOOOOO0O00O0O0O ['data']['ordinary_fertilizer']#line:1117
                        O00OOO0OO0OOOO000 =OOOOOOOO0O00O0O0O ['data']['videoStatus']#line:1118
                        O00000OOO000OOOOO =OOOOOOOO0O00O0O0O ['data']['waterVideoKey']#line:1119
                        print (f'【我的营养】:肥料:{str(O000000O0000OO00O).split(".")[0]}丨水滴:{str(O0000OO00O0OOOO0O).split(".")[0]}')#line:1120
                        if float (O000000O0000OO00O )<96 :#line:1121
                            if O00OOO0OO0OOOO000 :#line:1122
                                time .sleep (random .randint (160 ,180 )/10 )#line:1123
                                O00O00OOOO0O0O0O0 =99 -float (O000000O0000OO00O )#line:1124
                                OO0000O0OOO0OO00O ={"fertilizer":str (O00O00OOOO0O0O0O0 ).split ('.')[0 ]}#line:1125
                                O0OO000O0OO00OOOO =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00OOO00OO0OOO0O ).json ()#line:1126
                                if 'status'in O0OO000O0OO00OOOO :#line:1128
                                    if O0OO000O0OO00OOOO ['status']==200 :#line:1129
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO000O0OO00OOOO["message"]}')#line:1130
                                    if O0OO000O0OO00OOOO ['status']==500 :#line:1131
                                        print (f'【购买肥料】:看广告获取肥料:{O0OO000O0OO00OOOO["message"]}')#line:1132
                                        break #line:1133
                                if float (O000000O0000OO00O )<78 :#line:1135
                                    O00O00OOOO0O0O0O0 =80 -float (O000000O0000OO00O )#line:1136
                                    O0OO000O00000O000 =f'_fertilizer={int(O00O00OOOO0O0O0O0)}_{timi_new()}'#line:1137
                                    O0000000OOOOOOOO0 ={'source':'scsc','authorization':O0O0OOO00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000O00000O000 ),'signstring':O0OO000O00000O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1148
                                    OOO00OOOOOO0000O0 ={"fertilizer":int (O00O00OOOO0O0O0O0 )}#line:1149
                                    O00O0O0O00OO0O000 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0000000OOOOOOOO0 ,data =OOO00OOOOOO0000O0 ).json ()#line:1151
                                    if 'status'in O00O0O0O00OO0O000 :#line:1153
                                        if O00O0O0O00OO0O000 ['status']==200 :#line:1154
                                            print (f'【购买肥料】:购买肥料:{O00O0O0O00OO0O000["message"]}丨数量:{int(O00O00OOOO0O0O0O0)}')#line:1155
                                        if O00O0O0O00OO0O000 ['status']==500 :#line:1156
                                            print (f'【购买肥料】:购买肥料:{O00O0O0O00OO0O000["message"]}丨数量:{int(O00O00OOOO0O0O0O0)}')#line:1157
                                            O00O0OOO0O000OOOO =O00O0O0O00OO0O000 ["message"].split ('-')[1 ]#line:1158
                                            O00O00O0OO000OO00 =f'__{timi_new()}'#line:1159
                                            OOO0OOO0OOOOO0000 ={'source':'scsc','authorization':O0O0OOO00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO000OO00 ),'signstring':O00O00O0OO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1170
                                            O0O000O0O00O0OOOO =requests .request ('get',f'{host}/user',headers =OOO0OOO0OOOOO0000 ).json ()#line:1171
                                            if 'status'in O0O000O0O00O0OOOO :#line:1172
                                                if O0O000O0O00O0OOOO ['status']==200 :#line:1173
                                                    O0OOOO0O0000O0OOO =O0O000O0O00O0OOOO ['data']['inner_id']#line:1174
                                                    if give_gold (O0OOOO0O0000O0OOO ,float (O00O0OOO0O000OOOO )+1 ):#line:1175
                                                        O0O0OOO00O0OOO0OO .energy ()#line:1176
                        if float (O0000OO00O0OOOO0O )<880 :#line:1177
                            if O00000OOO000OOOOO :#line:1178
                                time .sleep (random .randint (160 ,180 )/10 )#line:1179
                                OOO0OOOOOOO000OOO =999 -float (O0000OO00O0OOOO0O )#line:1180
                                O00OO0000OOOO0OO0 ={"water":str (OOO0OOOOOOO000OOO ).split ('.')[0 ]}#line:1181
                                O00O0O000O00OO00O =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00OOO00OO0OOO0O ).json ()#line:1182
                                if 'status'in O00O0O000O00OO00O :#line:1184
                                    if O00O0O000O00OO00O ['status']==200 :#line:1185
                                        print (f'【购买水滴】:看广告获取水滴:{O00O0O000O00OO00O["message"]}')#line:1186
                                    if O00O0O000O00OO00O ['status']==500 :#line:1187
                                        print (f'【购买水滴】:看广告获取水滴:{O00O0O000O00OO00O["message"]}')#line:1188
                                        break #line:1189
                                if float (O0000OO00O0OOOO0O )<780 :#line:1190
                                    OOO0OOOOOOO000OOO =800 -float (O0000OO00O0OOOO0O )#line:1191
                                    OO0OO00000OOO0OO0 =f'_water={int(OOO0OOOOOOO000OOO)}_{timi_new()}'#line:1192
                                    O0O00000O00OO0OOO ={'source':'scsc','authorization':O0O0OOO00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO00000OOO0OO0 ),'signstring':OO0OO00000OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1203
                                    O0OO0O000OO0O0OO0 ={"water":int (OOO0OOOOOOO000OOO )}#line:1204
                                    OOOOOOO0O0O000000 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0O00000O00OO0OOO ,data =O0OO0O000OO0O0OO0 ).json ()#line:1206
                                    if 'status'in OOOOOOO0O0O000000 :#line:1208
                                        if OOOOOOO0O0O000000 ['status']==200 :#line:1209
                                            print (f'【购买水滴】:购买水滴:{OOOOOOO0O0O000000["message"]}丨数量:{int(OOO0OOOOOOO000OOO)}')#line:1210
                                        if OOOOOOO0O0O000000 ['status']==500 :#line:1211
                                            print (f'【购买水滴】:购买水滴:{OOOOOOO0O0O000000["message"]}丨数量:{int(OOO0OOOOOOO000OOO)}')#line:1212
                                            O00O0OOO0O000OOOO =OOOOOOO0O0O000000 ["message"].split ('-')[1 ]#line:1213
                                            O00O00O0OO000OO00 =f'__{timi_new()}'#line:1214
                                            OOO0OOO0OOOOO0000 ={'source':'scsc','authorization':O0O0OOO00O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O0OO000OO00 ),'signstring':O00O00O0OO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1225
                                            O0O000O0O00O0OOOO =requests .request ('get',f'{host}/user',headers =OOO0OOO0OOOOO0000 ).json ()#line:1226
                                            if 'status'in O0O000O0O00O0OOOO :#line:1227
                                                if O0O000O0O00O0OOOO ['status']==200 :#line:1228
                                                    O0OOOO0O0000O0OOO =O0O000O0O00O0OOOO ['data']['inner_id']#line:1229
                                                    if give_gold (O0OOOO0O0000O0OOO ,float (O00O0OOO0O000OOOO )+1 ):#line:1230
                                                        O0O0OOO00O0OOO0OO .energy ()#line:1231
                        break #line:1232
        except Exception as O0OO0O00OO0000000 :#line:1233
            print (O0OO0O00OO0000000 )#line:1234
def bundled_def ():#line:1236
    O00OOO0O000O0O000 =['5570536','7750212','7911652','7911680','7805624']#line:1237
    return O00OOO0O000O0O000 [random .randint (0 ,len (O00OOO0O000O0O000 )-1 )]#line:1238
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
        OO0O0O00O0000OOO0 =gitee_edition ()#line:1268
        if version_of_the_validation ()<OO0O0O00O0000OOO0 ['CityEarth']['edition']:#line:1269
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O00O0000OOO0["CityEarth"]["edition"]}   ❌')#line:1270
            print (f'更新内容=>>{OO0O0O00O0000OOO0["CityEarth"]["content"]}   🎉')#line:1271
        else :#line:1272
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O0O00O0000OOO0["CityEarth"]["edition"]}   ✅')#line:1273
            print (f'更新内容=>> {OO0O0O00O0000OOO0["CityEarth"]["content"]}   🎉')#line:1274
    except Exception as OOOO00O0OO0O0O000 :#line:1275
        print (OOOO00O0OO0O0O000 )#line:1276
def sc3 ():#line:1278
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1279
if __name__ =='__main__':#line:1283
    start ()#line:1284
