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
        O00OOO0OO0OO000O0 =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(O00OOO0OO0OO000O0)}个账号==========")#line:13
        for OO00000O00O000O0O in O00OOO0OO0OO000O0 :#line:14
            O0OOOO0OO00000OOO =[]#line:15
            print (f"------------正在执行第{O00OOO0OO0OO000O0.index(OO00000O00O000O0O) + 1}个账号------------")#line:16
            OO00OOOO00000OOOO =CityEarth (OO00000O00O000O0O ,O0OOOO0OO00000OOO ,O00OOO0OO0OO000O0 .index (OO00000O00O000O0O ))#line:17
            def OO0000OOOO000000O ():#line:19
                if OO00OOOO00000OOOO .base_info ():#line:21
                    OO00OOOO00000OOOO .sealing ()#line:23
                    OO00OOOO00000OOOO .invitenum ()#line:25
                    OO00OOOO00000OOOO .query_to_sell ()#line:27
                    OO00OOOO00000OOOO .game_map ()#line:29
                    OO00OOOO00000OOOO .friends_invitation ()#line:31
                    OO00OOOO00000OOOO .energy ()#line:33
                    OO00OOOO00000OOOO .add_clover ()#line:35
                    OO00OOOO00000OOOO .propsraffle ()#line:37
                    OO00OOOO00000OOOO .synthetic ()#line:39
                    OO00OOOO00000OOOO .crops_illustrated ()#line:41
                    OO00OOOO00000OOOO .withdraw ()#line:43
                    if float (datetime .datetime .now ().hour )>8 :#line:44
                        OO00OOOO00000OOOO .give_gold ()#line:46
            OOOO000O000OO0O00 =threading .Thread (target =OO0000OOOO000000O )#line:47
            OOOO000O000OO0O00 .start ()#line:48
            time .sleep (time_xx )#line:49
        print (f"------------正在处理推送通知------------")#line:50
        time .sleep (0.5 )#line:51
        O0OOO00O0OOO0O0O0 =format_msg ()#line:52
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',O0OOO00O0OOO0O0O0 +' ')#line:53
        if eeeeee :#line:54
            time .sleep (100 )#line:55
            print ('开始打印好友数量不足2的ID')#line:56
            print (invited_new )#line:57
    except Exception as OO0OO0000OO0O00OO :#line:58
        print (OO0OO0000OO0O00OO )#line:59
def give_gold (O0OO0OO0000000O0O ,O00OO00OO00000OO0 ):#line:62
        try :#line:63
            OOOO00OO00O0O0000 =f'_doneeNo={O0OO0OO0000000O0O}&quantity={int(O00OO00OO00000OO0)}_{timi_new()}'#line:64
            O0O00O00OOOO0O00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO00OO00O0O0000 ),'signstring':OOOO00OO00O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:75
            O00OOO0O000O0000O ={"quantity":int (O00OO00OO00000OO0 ),"doneeNo":O0OO0OO0000000O0O }#line:79
            OO0O00O000O00O0OO =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00O00OOOO0O00O ,data =O00OOO0O000O0000O ).json ()#line:80
            if 'status'in OO0O00O000O00O0OO :#line:82
                if OO0O00O000O00O0OO ['status']==200 :#line:83
                    if OO0O00O000O00O0OO ['data']:#line:84
                        print (f'【赠送种子】:赠送{int(O00OO00OO00000OO0)}种子给{O0OO0OO0000000O0O}成功')#line:85
                        return True #line:86
                if OO0O00O000O00O0OO ['status']==401 :#line:87
                    print (f'【赠送种子】:{OO0O00O000O00O0OO["message"]}')#line:88
                    return False #line:89
                if OO0O00O000O00O0OO ['status']==500 :#line:90
                    print (f'【赠送种子】:{OO0O00O000O00O0OO["message"]}')#line:91
                    return False #line:92
            return False #line:93
        except Exception as OOO0OOOO0OOO0O0O0 :#line:94
            print (OOO0OOOO0OOO0O0O0 )#line:95
def kvkv ():#line:96
    return '/vastzzzl/vastzzzl/raw/master'#line:97
def sign (OOOO000OOOOO0O00O ):#line:100
    OO0000OOO00O0O0OO =hashlib .md5 (OOOO000OOOOO0O00O .encode ()).hexdigest ()#line:101
    O0OOO00OOOO0O0OO0 =sc1 ()#line:102
    OO00OOO0OO0OO0O0O =sc2 ()#line:103
    O0O00O000OO0OO000 =sc3 ()#line:104
    OOO0O00O0OO0000O0 =O0OOO00OOOO0O0OO0 +OO0000OOO00O0O0OO +OO00OOO0OO0OO0O0O +O0O00O000OO0OO000 #line:105
    O0OOOO0000OO00000 =hashlib .md5 (OOO0O00O0OO0000O0 .encode ()).hexdigest ()#line:106
    return O0OOOO0000OO00000 #line:107
def format_msg ():#line:111
    O00O00O0O00O00O00 =""#line:112
    for O00O00000O00O00O0 in msg_list :#line:113
        O00O00O0O00O00O00 +=str (O00O00000O00O00O0 )+"\r\n"#line:114
    return O00O00O0O00O00O00 #line:115
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
def get_json_data (O0OO0OO0O00O0OOO0 ,OO0O00O0OO000O00O ,OO0OO00O0O0O00OO0 ,OO00OOO0O0000OOOO ):#line:134
    with open (O0OO0OO0O00O0OOO0 ,'rb')as O00OO0000O00O0OO0 :#line:136
        OOOO00OO0OOOO0OO0 =json .load (O00OO0000O00O0OO0 )#line:137
        OOOO00OO0OOOO0OO0 ['data'][OO0O00O0OO000O00O ][OO0OO00O0O0O00OO0 ]=OO00OOO0O0000OOOO #line:138
        O00O0OOOOO00OOOO0 =OOOO00OO0OOOO0OO0 #line:139
    O00OO0000O00O0OO0 .close ()#line:140
    return O00O0OOOOO00OOOO0 #line:141
def write_json_data (O00O0OO00O000OO0O ):#line:143
    with open (json_path1 ,'w')as OOOOOO00OOO0O0O0O :#line:144
        json .dump (O00O0OO00O000OO0O ,OOOOOO00OOO0O0O0O )#line:145
    OOOOOO00OOO0O0O0O .close ()#line:146
    return True #line:147
class CityEarth :#line:149
    def __init__ (OO0O0OO0OO00O0O00 ,OO00000O0OOO0000O ,OOO00OOOOOOOO0000 ,O00OO0000O0O0OO00 ):#line:151
        try :#line:152
            OO0O0OO0OO00O0O00 .msg =OOO00OOOOOOOO0000 #line:153
            OO0O0OO0OO00O0O00 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:154
            OO0O0OO0OO00O0O00 .token =OO00000O0OOO0000O ['authorization']#line:155
            OO0O0OO0OO00O0O00 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:156
            OO0O0OO0OO00O0O00 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:157
            OO0O0OO0OO00O0O00 .elephant_user =OO00000O0OOO0000O ['elephant_user']#line:158
            OO0O0OO0OO00O0O00 .elephant_pswd =OO00000O0OOO0000O ['elephant_pswd']#line:159
            OO0O0OO0OO00O0O00 .elephant_Task_ID =OO00000O0OOO0000O ['elephant_Task_ID']#line:160
            OO0O0OO0OO00O0O00 .len_new =O00OO0000O0O0OO00 #line:161
        except :#line:162
            print ('变量格式错误')#line:163
    def base_info (O0O00O00000OOO00O ):#line:166
        try :#line:167
            O0O00O00000OOO00O .watched_ad ()#line:169
            O000O00O000O0OOO0 =f'__{timi_new()}'#line:170
            OO0O0OOOOOOOO000O ={'source':'scsc','authorization':O0O00O00000OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O000O00O000O0OOO0 ),'signstring':O000O00O000O0OOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:181
            OO00000O0OO0OO0OO =requests .request ('get',f'{host}/user',headers =OO0O0OOOOOOOO000O ).json ()#line:182
            if 'status'in OO00000O0OO0OO0OO :#line:184
                if OO00000O0OO0OO0OO ['status']==200 :#line:185
                    OO000OO0OO00O0O0O =OO00000O0OO0OO0OO ['data']['nickname']#line:186
                    O0O0OOOOO0OOO00OO =OO00000O0OO0OO0OO ['data']['inner_id']#line:187
                    OO0OO00OO00O000O0 =OO00000O0OO0OO0OO ['data']['assets']['gold']#line:188
                    O000O0O0O0OOOO0O0 =OO00000O0OO0OO0OO ['data']['level']#line:189
                    print (f'【账号信息】:昵称:{OO000OO0OO00O0O0O[:5]}丨ID:{O0O0OOOOO0OOO00OO}丨等级:{O000O0O0O0OOOO0O0}丨金种子:{str(OO0OO00OO00O000O0).split(".")[0]}')#line:190
                    if 'wx_'in OO000OO0OO00O0O0O :#line:191
                        O0O00O00000OOO00O .change_nickname ()#line:192
                if OO00000O0OO0OO0OO ['status']==401 :#line:193
                    print ('【账号信息】:账号失效正在尝试登录')#line:194
                    if O0O00O00000OOO00O .elephant_user =='f':#line:195
                        return False #line:196
                    OO0O0O0OO00O0OO0O =Invalid_login .addtask (elephant_user =O0O00O00000OOO00O .elephant_user ,elephant_pswd =O0O00O00000OOO00O .elephant_pswd ,elephant_Task_ID =O0O00O00000OOO00O .elephant_Task_ID )#line:197
                    OO0O00O0O0000O000 =get_json_data (json_path ,O0O00O00000OOO00O .len_new ,'authorization',OO0O0O0OO00O0OO0O )#line:198
                    if write_json_data (OO0O00O0O0000O000 ):#line:199
                        print ('正在写入账号配置文件')#line:200
                    return False #line:201
                if OO00000O0OO0OO0OO ['status']==500 :#line:202
                    return False #line:203
            return True #line:204
        except Exception as OO0OOO0OO0000000O :#line:205
            print (OO0OOO0OO0000000O )#line:206
    def sealing (OOO00O0OOO000O0OO ):#line:209
        try :#line:210
            O0OOOOO00O000O0O0 =f'__{timi_new()}'#line:211
            O0O0O000OOOO0O0O0 ={'source':'scsc','authorization':OOO00O0OOO000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOOO00O000O0O0 ),'signstring':O0OOOOO00O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:222
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O0O0O000OOOO0O0O0 )#line:223
            requests .request ('get',f'{host}/packsack/list',headers =O0O0O000OOOO0O0O0 )#line:224
            requests .request ('get',f'{host}/friends/invited/ad',headers =O0O0O000OOOO0O0O0 )#line:225
            requests .request ('get',f'{host}/assets/gold/rank',headers =O0O0O000OOOO0O0O0 )#line:226
            requests .request ('get',f'{host}/user',headers =O0O0O000OOOO0O0O0 )#line:227
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O0O0O000OOOO0O0O0 )#line:228
            requests .request ('get',f'{host}/finance/get-power-list',headers =O0O0O000OOOO0O0O0 )#line:229
            requests .request ('post',f'{host}/announcement/announcement',headers =O0O0O000OOOO0O0O0 )#line:230
            requests .request ('get',f'{host}/game/getAllData',headers =O0O0O000OOOO0O0O0 )#line:231
            requests .request ('get',f'{host}/assets',headers =O0O0O000OOOO0O0O0 )#line:232
        except Exception as OOOOOOO0O0O0OOOO0 :#line:233
            print (OOOOOOO0O0O0OOOO0 )#line:234
    def the_query (O0OO000OO0OOO00O0 ):#line:237
        try :#line:238
            OO0OO0O0OO000OOOO =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:239
            OO0O0OO000OOO0OO0 ={'authorization':O0OO000OO0OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0O0OO000OOOO ),'signstring':OO0OO0O0OO000OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:249
            OO0O00OOO0OO000O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =OO0O0OO000OOO0OO0 ).json ()#line:250
            if 'status'in OO0O00OOO0OO000O0 :#line:252
                if OO0O00OOO0OO000O0 ['status']==200 :#line:253
                    O000OOO0O00O0O0O0 =OO0O00OOO0OO000O0 ['data']['rows'][3 ]['price']#line:254
                    O0OO000OO0OOO00O0 .market_sale (O000OOO0O00O0O0O0 )#line:255
        except Exception as O0O0OO0OOOOO0OOO0 :#line:256
            print (O0O0OO0OOOOO0OOO0 )#line:257
    def market_sale (O0OO000OOO0O00O00 ,O0OOO00O00OO00O00 ):#line:260
        try :#line:261
            O00O0OOOOOOO0OO00 =timi_new ()#line:262
            O000O0OO0O000OO00 =f'type=crop__{O00O0OOOOOOO0OO00}'#line:263
            OOOOO0OO00O0O0OO0 ={'source':'scsc','authorization':O0OO000OOO0O00O00 .token ,'timestamp':str (O00O0OOOOOOO0OO00 ),'sign':sign (O000O0OO0O000OO00 ),'signstring':O000O0OO0O000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:274
            OO0OOOO0OOO0OO00O =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOOO0OO00O0O0OO0 ).json ()#line:275
            if 'status'in OO0OOOO0OOO0OO00O :#line:277
                if OO0OOOO0OOO0OO00O ['status']==200 :#line:278
                    if OO0OOOO0OOO0OO00O ['data']['rows']:#line:279
                        O0OOO0000O0O0000O =OO0OOOO0OOO0OO00O ['data']['rows'][0 ]['packsackItemId']#line:280
                        O000O00O0OOO00O00 =OO0OOOO0OOO0OO00O ['data']['rows'][0 ]['quantity']#line:281
                        OO00OOO0O00OOO0OO =float (O0OOO00O00OO00O00 )+float (random .randint (1 ,99 )*0.001 )#line:282
                        O0O000O000OOO00O0 =f'_packsackItemId={O0OOO0000O0O0000O}&price={str(OO00OOO0O00OOO0OO)[:7]}&quantity={O000O00O0OOO00O00}_{O00O0OOOOOOO0OO00}'#line:283
                        O00OOO0O0OO000OOO ={'source':'scsc','authorization':O0OO000OOO0O00O00 .token ,'timestamp':str (O00O0OOOOOOO0OO00 ),'sign':sign (O0O000O000OOO00O0 ),'signstring':O0O000O000OOO00O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:294
                        O0OOO00O00OO0O000 ={"packsackItemId":O0OOO0000O0O0000O ,"price":str (OO00OOO0O00OOO0OO )[:7 ],"quantity":str (O000O00O0OOO00O00 )}#line:299
                        O0000O0OOOOOO0O00 =requests .request ('post',f'{host}/market/sale',headers =O00OOO0O0OO000OOO ,data =O0OOO00O00OO0O000 ).json ()#line:300
                        if 'status'in O0000O0OOOOOO0O00 :#line:302
                            if O0000O0OOOOOO0O00 ['status']==200 :#line:303
                                print (f'【上架芦荟】:数量:{O000O00O0OOO00O00}丨价格:{str(OO00OOO0O00OOO0OO)[:7]}')#line:304
        except Exception as O00O0OO0O0O0O0O00 :#line:305
            print (O00O0OO0O0O0O0O00 )#line:306
    def query_to_sell (OOOO00OO0O0O0000O ):#line:309
        try :#line:310
            OO0000OOO00O0OO0O =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:311
            O00OOO00O0O0OO000 ={'source':'scsc','authorization':OOOO00OO0O0O0000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000OOO00O0OO0O ),'signstring':OO0000OOO00O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:322
            O000OOOOO00O0OOOO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O00OOO00O0O0OO000 ).json ()#line:324
            if 'status'in O000OOOOO00O0OOOO :#line:326
                if O000OOOOO00O0OOOO ['status']==200 :#line:327
                    for O000O000O000O0O0O in O000OOOOO00O0OOOO ['data']['rows']:#line:328
                        O0OO000O0OO0OOO00 =O000O000O000O0O0O ['materialKey']#line:329
                        OO0O00OO00OOO0O00 =O000O000O000O0O0O ['quantity']#line:330
                        OOOO0O0O0OO0OO000 =O000O000O000O0O0O ['price']#line:331
                        OOO00OOO0000O0O00 =O000O000O000O0O0O ['saleState']#line:332
                        if OOO00OOO0000O0O00 ==0 :#line:333
                            print (f'【出售订单】:名称:{O0OO000O0OO0OOO00}丨数量:{OO0O00OO00OOO0O00}丨价格:{OOOO0O0O0OO0OO000}')#line:334
                            O000OOO0OO00OO000 =O000O000O000O0O0O ['id']#line:335
                            OOOO00OO0O0O0000O .cacel_sale (O000OOO0OO00OO000 )#line:336
        except Exception as OO00000OOOO00OO0O :#line:337
            print (OO00000OOOO00OO0O )#line:338
    def cacel_sale (OOO00OO00O0OO0OO0 ,OO0O000O00OO00OOO ):#line:342
        try :#line:343
            OO0OO0000OO000O00 =f'_saleId={OO0O000O00OO00OOO}_{timi_new()}'#line:344
            O00OO00O0OOO0O00O ={'source':'scsc','authorization':OOO00OO00O0OO0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0000OO000O00 ),'signstring':OO0OO0000OO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:355
            O0O0OO0O0O000OO00 ={"saleId":OO0O000O00OO00OOO }#line:358
            OOO0OO0000O00O0OO =requests .request ('post',f'{host}/market/cacel-sale',headers =O00OO00O0OOO0O00O ,data =O0O0OO0O0O000OO00 ).json ()#line:359
            if 'status'in OOO0OO0000O00O0OO :#line:361
                if OOO0OO0000O00O0OO ['status']==200 :#line:362
                    print (f'【下架出售】:{OOO0OO0000O00O0OO["data"]}')#line:363
        except Exception as OO0O0O0000O00O00O :#line:364
            print (OO0O0O0000O00O00O )#line:365
    def change_nickname (OOO0OO00OO000O00O ):#line:372
        try :#line:373
            O0OOOO0O0O00O0OOO =timi_new ()#line:374
            OOO0O0000OOO000O0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:375
            O0O0O000OO000OO00 =requests .request ('post','https://www.qmsjmfb.com/',data =OOO0O0000OOO000O0 ).text #line:376
            OO0O0O00O0OOO0OO0 =re .findall ('<ul><li>(.*?)</li>',O0O0O000OO000OO00 )[0 ][:3 ]#line:377
            OO00OO00000O0O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO0O0O00O0OOO0OO0}').json ()#line:378
            OO0000000OO0000OO =OO00OO00000O0O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:379
            OOOO0OOO000OO00OO ={"nickname":OO0000000OO0000OO }#line:380
            OOOO000O00O0O0O00 =f'_nickname={OO0000000OO0000OO}_{O0OOOO0O0O00O0OOO}'#line:381
            O0OOOO0OOOOO0OO0O ={'source':'scsc','authorization':OOO0OO00OO000O00O .token ,'timestamp':O0OOOO0O0O00O0OOO ,'sign':sign (OOOO000O00O0O0O00 ),'signstring':OOOO000O00O0O0O00 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:392
            OO0O00O0O0O0OOO00 =requests .request ('patch',f'{host}/user/nickname',headers =O0OOOO0OOOOO0OO0O ,data =OOOO0OOO000OO00OO ).json ()#line:393
            if 'status'in OO0O00O0O0O0OOO00 :#line:395
                if OO0O00O0O0O0OOO00 ['status']==200 :#line:396
                    print (f'【修改网名】:网名:{OO0000000OO0000OO}丨{OO0O00O0O0O0OOO00["message"]}')#line:397
        except Exception as OO0O00O0O00O0O0O0 :#line:398
            print (OO0O00O0O00O0O0O0 )#line:399
    def withdraw (OO0O00O0O000OOO00 ):#line:404
        try :#line:405
            OO0OO000OO0000O00 =f'__{timi_new()}'#line:406
            O0000OO000O00O000 ={'source':'scsc','authorization':OO0O00O0O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO0000O00 ),'signstring':OO0OO000OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:417
            O00O00000OOO0O00O =requests .request ('get',f'{host}/assets',headers =O0000OO000O00O000 ).json ()#line:418
            if 'status'in O00O00000OOO0O00O :#line:420
                if O00O00000OOO0O00O ['status']==200 :#line:421
                    O00OOOOOOOOO0OOO0 =O00O00000OOO0O00O ['data']['cash']#line:422
                    if float (O00OOOOOOOOO0OOO0 )>20 :#line:423
                        OO0OO000OO0000O00 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:424
                        O0000OO000O00O000 ={'authorization':OO0O00O0O000OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO000OO0000O00 ),'signstring':OO0OO000OO0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:434
                        O0OOOOO00O000O00O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:435
                        O0O000O000OOO0OOO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O0000OO000O00O000 ,data =O0OOOOO00O000O00O ).json ()#line:436
                        if 'status'in O0O000O000OOO0OOO :#line:438
                            if O0O000O000OOO0OOO ['status']==200 :#line:439
                                print (f'【余额提现】:{O0O000O000OOO0OOO["data"]}')#line:440
                        if 'status'in O0O000O000OOO0OOO :#line:441
                            if O0O000O000OOO0OOO ['status']==500 :#line:442
                                print (f'【余额提现】:{O0O000O000OOO0OOO["message"]}')#line:443
        except Exception as O0O0O0O0OOOO0O00O :#line:444
            print (O0O0O0O0OOOO0O00O )#line:445
    def invitenum (OOOO00O00O0OO0000 ):#line:449
        global invited_new #line:450
        try :#line:451
            O0O0O0OO0OO00O000 =f'__{timi_new()}'#line:452
            O0000OOO0OO00O000 ={'source':'scsc','authorization':OOOO00O00O0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0O0OO0OO00O000 ),'signstring':O0O0O0OO0OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:463
            OOO00O0OO00OOO0OO =requests .request ('get',f'{host}/invite/invitenum',headers =O0000OOO0OO00O000 ).json ()#line:464
            if 'status'in OOO00O0OO00OOO0OO :#line:466
                if OOO00O0OO00OOO0OO ['status']==200 :#line:467
                    OOOOOOOO00000O0O0 =OOO00O0OO00OOO0OO ['data']['invited_count']#line:468
                    O00O0000OO00O000O =OOO00O0OO00OOO0OO ['data']['invited_second_count']#line:469
                    print (f'【我的邀请】:直邀好友:{OOOOOOOO00000O0O0}丨间邀好友:{O00O0000OO00O000O}')#line:470
                    if OOOOOOOO00000O0O0 <2 :#line:471
                        OO000OO00O00O0OO0 =f'__{timi_new()}'#line:472
                        O000000OOOOO00OO0 ={'source':'scsc','authorization':OOOO00O00O0OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO00O00O0OO0 ),'signstring':OO000OO00O00O0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        O000OOOO000OO0OOO =requests .request ('get',f'{host}/user',headers =O000000OOOOO00OO0 ).json ()#line:484
                        if 'status'in O000OOOO000OO0OOO :#line:486
                            if O000OOOO000OO0OOO ['status']==200 :#line:487
                                invited_new .append (O000OOOO000OO0OOO ['data']['inner_id'])#line:488
        except Exception as O00OO000000OOOOO0 :#line:489
            print (O00OO000000OOOOO0 )#line:490
    def game_map (OOO000OO0O00OOO0O ):#line:494
        try :#line:495
            OOO0OO0O0000O0O00 =f'__{timi_new()}'#line:496
            O000OOOOO0O000000 ={'source':'scsc','authorization':OOO000OO0O00OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0O0000O0O00 ),'signstring':OOO0OO0O0000O0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:507
            OO0O000OO0O00O000 =requests .request ('get',f'{host}/game/map',headers =O000OOOOO0O000000 ).json ()#line:508
            if 'status'in OO0O000OO0O00O000 :#line:510
                if OO0O000OO0O00O000 ['status']==200 :#line:511
                    for O00O00000O0OO000O in OO0O000OO0O00O000 ['data']['list'][0 ]['crops']:#line:512
                        OOOOOOOO00O000O0O =O00O00000O0OO000O ['level']#line:514
                        if OOOOOOOO00O000O0O ==41 :#line:515
                            O00OOO00O00O00O0O =O00O00000O0OO000O ['crop_name']#line:516
                            OO0O00OO0OO0000O0 =O00O00000O0OO000O ['count']#line:517
                            if OO0O00OO0OO0000O0 >0 :#line:518
                                print (f'【农业资产】:{O00OOO00O00O00O0O}丨数量:{OO0O00OO0OO0000O0}')#line:519
                                OOO000OO0O00OOO0O .the_query ()#line:520
        except Exception as O000O00OO0O000OO0 :#line:521
            print (O000O00OO0O000OO0 )#line:522
    def give_gold (O0O00OO0OOOO000OO ):#line:525
        try :#line:526
            O00O00OO000O0OOOO =f'__{timi_new()}'#line:527
            OO0000OOO0OO000OO ={'source':'scsc','authorization':O0O00OO0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000O0OOOO ),'signstring':O00O00OO000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:538
            OOO0OO0O00OOOO0OO =requests .request ('get',f'{host}/user',headers =OO0000OOO0OO000OO ).json ()#line:539
            if 'status'in OOO0OO0O00OOOO0OO :#line:540
                if OOO0OO0O00OOOO0OO ['status']==200 :#line:541
                    if float (O0O00OO0OOOO000OO .doneeNo )!=0 :#line:542
                        OO0O00000OOO0O0O0 =OOO0OO0O00OOOO0OO ['data']['assets']['gold']#line:543
                        if float (OO0O00000OOO0O0O0 )>float (O0O00OO0OOOO000OO .innerId ):#line:544
                            OO00O0O0OOOOO00OO =int (float (OO0O00000OOO0O0O0 )/1.1 )#line:545
                            O00O00OO000O0OOOO =f'_doneeNo={O0O00OO0OOOO000OO.doneeNo}&quantity={OO00O0O0OOOOO00OO}_{timi_new()}'#line:546
                            OO0000OOO0OO000OO ={'source':'scsc','authorization':O0O00OO0OOOO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO000O0OOOO ),'signstring':O00O00OO000O0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:557
                            O00O0O0O0OOOOOO0O ={"quantity":OO00O0O0OOOOO00OO ,"doneeNo":O0O00OO0OOOO000OO .doneeNo }#line:561
                            O0OO0O00O0OO00000 =requests .request ('post',f'{host}/finance/give-gold',headers =OO0000OOO0OO000OO ,data =O00O0O0O0OOOOOO0O ).json ()#line:562
                            if 'status'in O0OO0O00O0OO00000 :#line:564
                                if O0OO0O00O0OO00000 ['status']==200 :#line:565
                                    if O0OO0O00O0OO00000 ['data']:#line:566
                                        print (f'【赠送种子】:赠送{OO00O0O0OOOOO00OO}种子给{O0O00OO0OOOO000OO.doneeNo}成功')#line:567
                    else :#line:568
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:569
        except Exception as O0O0OO000O00O000O :#line:570
            print (O0O0OO000O00O000O )#line:571
    def invitation (O00OOOO00OOOOOOOO ):#line:573
        try :#line:574
            _O0O000O0O000O0OO0 =float (bundled_def ())/4 #line:575
            OO00OOO00OOOO0OO0 =f'_innerId={int(_O0O000O0O000O0OO0)}_{timi_new()}'#line:576
            O00O000O0OOOO0OOO ={'source':'scsc','authorization':O00OOOO00OOOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO00OOOO0OO0 ),'signstring':OO00OOO00OOOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            OOO0OO0000O000000 ={"innerId":int (_O0O000O0O000O0OO0 )}#line:588
            requests .request ('post',f'{host}/friends/my-invitation',headers =O00O000O0OOOO0OOO ,data =OOO0OO0000O000000 )#line:589
        except Exception as OOO00O0O000O000OO :#line:590
            print (OOO00O0O000O000OO )#line:591
    def winning_rewards (OO0O0OOO0OOO00O00 ):#line:594
        try :#line:595
            O00OOO0O00000O0OO =f'__{timi_new()}'#line:596
            O00OO00OOOOOOO0O0 ={'source':'scsc','authorization':OO0O0OOO0OOO00O00 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O00000O0OO ),'signstring':O00OOO0O00000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:607
            O0O0OOOO0000000O0 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =O00OO00OOOOOOO0O0 ).json ()#line:608
            if 'status'in O0O0OOOO0000000O0 :#line:610
                if O0O0OOOO0000000O0 ['status']==200 :#line:611
                    if O0O0OOOO0000000O0 ['data']['amount']:#line:612
                        O00O0O0O00O00OOO0 =O0O0OOOO0000000O0 ['data']['amount']['gold']#line:613
                        return O00O0O0O00O00OOO0 #line:614
                    else :#line:615
                        return 0 #line:616
        except Exception as O000OO0OOOO000OOO :#line:617
            print (O000OO0OOOO000OOO )#line:618
    def certification (O0OO000000O0OO00O ):#line:621
        try :#line:622
            OOO00O0000OOOO000 =f'__{timi_new()}'#line:623
            O0O000000O0000O0O ={'source':'scsc','authorization':O0OO000000O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0000OOOO000 ),'signstring':OOO00O0000OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:634
            OO0OOO000OO000OO0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O0O000000O0000O0O ).json ()#line:635
            if 'status'in OO0OOO000OO000OO0 :#line:637
                if OO0OOO000OO000OO0 ['status']==200 :#line:638
                    if OO0OOO000OO000OO0 ['data']['result']:#line:639
                        O0O00OO0O0O00OO0O =OO0OOO000OO000OO0 ['data']['nick_name']#line:640
                        return O0O00OO0O0O00OO0O #line:641
                    else :#line:642
                        return '未实名'#line:643
        except Exception as O0OO0OO000OOO0000 :#line:644
            print (O0OO0OO000OOO0000 )#line:645
    def crops_illustrated (O0OOO0000O0OOO0OO ):#line:648
        try :#line:649
            O00000O0O0000000O =f'__{timi_new()}'#line:650
            OO0O0OO0OOO00O00O ={'source':'scsc','authorization':O0OOO0000O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0000000O ),'signstring':O00000O0O0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:661
            O0O00000O0O00O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O0OO0OOO00O00O ).json ()#line:662
            if 'status'in O0O00000O0O00O0O0 :#line:664
                if O0O00000O0O00O0O0 ['status']==200 :#line:665
                    O0OOO00000000O0O0 =O0O00000O0O00O0O0 ['data'][0 ]['crops']#line:666
                    for OOO0O00000OO0000O in O0OOO00000000O0O0 :#line:667
                        if OOO0O00000OO0000O ['ill_clover_award']:#line:668
                            if float (OOO0O00000OO0000O ['ill_clover_award'])>1 :#line:669
                                if OOO0O00000OO0000O ['is_finish']:#line:670
                                    if not OOO0O00000OO0000O ['is_getit']:#line:671
                                        if O0OOO0000O0OOO0OO .certification ()!='未实名':#line:672
                                            O00000O0O0000000O =f'_award_level={OOO0O00000OO0000O["level"]}_{timi_new()}'#line:673
                                            OO0O0OO0OOO00O00O ={'source':'scsc','authorization':O0OOO0000O0OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00000O0O0000000O ),'signstring':O00000O0O0000000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:684
                                            OOOOO00O0O00000O0 ={"award_level":OOO0O00000OO0000O ['level']}#line:685
                                            O00000O000O0OO0OO =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O0OO0OOO00O00O ,json =OOOOO00O0O00000O0 ).json ()#line:687
                                            if 'status'in O00000O000O0OO0OO :#line:688
                                                if O00000O000O0OO0OO ['status']==200 :#line:689
                                                    O0OO00O0O0O0O000O =O00000O000O0OO0OO ['data']['ill_clover_award']#line:690
                                                    print (f'【图鉴奖励】:领取{OOO0O00000OO0000O["crop_name"]}成就丨奖励{O0OO00O0O0O0O000O}☘️')#line:692
                                                if O00000O000O0OO0OO ['status']==500 :#line:693
                                                    print (f'【图鉴奖励】:{O00000O000O0OO0OO["message"]}')#line:694
        except Exception as OOOOO0O0OOO00O000 :#line:695
            print (OOOOO0O0OOO00O000 )#line:696
    def watched_ad (O0O0O00OO0O0O0OO0 ):#line:699
        try :#line:700
            O00OOOOOOO0O0O0OO =f'__{timi_new()}'#line:701
            OOOO0O0O0O00O0O0O ={'source':'scsc','authorization':O0O0O00OO0O0O0OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOOOOO0O0O0OO ),'signstring':O00OOOOOOO0O0O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:712
            OO0O00OO00000OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0O0O00O0O0O ).json ()#line:713
            if 'status'in OO0O00OO00000OOO0 :#line:715
                if OO0O00OO00000OOO0 ['status']==200 :#line:716
                    if 'offlineInfo'in OO0O00OO00000OOO0 ['data']:#line:717
                        time .sleep (random .randint (1 ,3 ))#line:718
                        O000000O0O000OOO0 =OO0O00OO00000OOO0 ['data']['offlineInfo']['off_minute']#line:719
                        OO00O0OOOOOOOO0O0 =float (OO0O00OO00000OOO0 ['data']['silver'])/1000000000000 #line:720
                        time .sleep (1 )#line:721
                        requests .request ('post',f'{host}/game/watched-ad',headers =OOOO0O0O0O00O0O0O ).json ()#line:722
                        time .sleep (2 )#line:723
                        O0O00O0OO00OO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOO0O0O0O00O0O0O ).json ()#line:724
                        if 'status'in O0O00O0OO00OO0OOO :#line:726
                            if O0O00O0OO00OO0OOO ['status']==200 :#line:727
                                O0OOO00OOOO000000 =float (O0O00O0OO00OO0OOO ['data']['silver'])/1000000000000 #line:728
                                OOOO0O0O00OO0O000 =str (O0OOO00OOOO000000 -OO00O0OOOOOOOO0O0 )[:6 ]#line:729
                                print (f'【离线奖励】:翻倍离线{O000000O0O000OOO0}分钟奖励🌱数量:{OOOO0O0O00OO0O000}t粒')#line:730
        except Exception as O00O00O0OOO00O0OO :#line:731
            print (O00O00O0OOO00O0OO )#line:732
    def user_ad (O000OO00OO00OOOO0 ):#line:735
        try :#line:736
            O00OOO0O000O00O0O =f'__{timi_new()}'#line:737
            O00OOOO000000OO0O ={'source':'scsc','authorization':O000OO00OO00OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0O000O00O0O ),'signstring':O00OOO0O000O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:748
            OO0OO0O0OOO00OOOO =requests .request ('get',f'{host}/user/ad',headers =O00OOOO000000OO0O ).json ()#line:749
            if 'status'in OO0OO0O0OOO00OOOO :#line:751
                if OO0OO0O0OOO00OOOO ['status']==200 :#line:752
                    O00O00O000OOO00OO =OO0OO0O0OOO00OOOO ['data']['max_time']#line:753
                    O0000O00000OOOO0O =OO0OO0O0OOO00OOOO ['data']['watch_time']#line:754
                    O00000OOO0OOOO00O =OO0OO0O0OOO00OOOO ['data']['added_time']#line:755
                    print (f'【获取种子】:获取🌱剩余{O00000OOO0OOOO00O + O00O00O000OOO00OO - O0000O00000OOOO0O}次丨好友提供:{O00000OOO0OOOO00O}次')#line:756
                    if O00000OOO0OOOO00O +O00O00O000OOO00OO -O0000O00000OOOO0O >0 :#line:757
                        time .sleep (random .randint (16 ,19 ))#line:758
                        O0000O00O0000O00O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O00OOOO000000OO0O ).json ()#line:759
                        if 'status'in O0000O00O0000O00O :#line:761
                            if O0000O00O0000O00O ['status']==200 :#line:762
                                OOOO0O000OOOO0O0O =float (O0000O00O0000O00O ['data']['silver'])/1000000000000 #line:763
                                print (f'【获取种子】:获得🌱:{int(OOOO0O000OOOO0O0O)}t粒')#line:764
                                return True #line:765
                            if O0000O00O0000O00O ['status']==500 :#line:766
                                O000O00O0O0O00000 =O0000O00O0000O00O ['message']#line:767
                                print (f'【获取种子】:{O000O00O0O0O00000}')#line:768
                                return False #line:769
        except Exception as O000OO0OOO0OOOOO0 :#line:770
            print (O000OO0OOO0OOOOO0 )#line:771
    def synthetic (OO00O000O0O00OOO0 ):#line:774
        global id ,g #line:775
        try :#line:776
            OO0O0OOO0OOO000O0 =OO00O000O0O00OOO0 .level_new ()#line:777
            OO0OOO0000OOO0OO0 =random .randint (9 ,11 )#line:778
            O000OOO00000OOOO0 =f'_site=8&targetSite={OO0OOO0000OOO0OO0}_{timi_new()}'#line:779
            O00000O00000O0OOO ={'source':'scsc','authorization':OO00O000O0O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (O000OOO00000OOOO0 ),'signstring':O000OOO00000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:790
            OO0O0OO0O0OOO0O0O ={"site":int (8 ),"targetSite":int (OO0OOO0000OOO0OO0 )}#line:791
            requests .request ('post',f'{host}/game/crops/move',headers =O00000O00000O0OOO ,json =OO0O0OO0O0OOO0O0O )#line:792
            while True :#line:793
                OO0OOOO0OOOO00OO0 =f'__{timi_new()}'#line:794
                OO00OO0O000O0O0O0 ={'source':'scsc','authorization':OO00O000O0O00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0OOOO00OO0 ),'signstring':OO0OOOO0OOOO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:805
                O0OO0O00OO0OOO0OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O000O0O0O0 ).json ()#line:806
                if 'status'in O0OO0O00OO0OOO0OO :#line:808
                    if O0OO0O00OO0OOO0OO ['status']==200 :#line:809
                        O0OO0OOO00OOOO000 =O0OO0O00OO0OOO0OO ['data']['cropList']#line:810
                        O0OOOO0O000O000OO =O0OO0O00OO0OOO0OO ['data']['gameCoreDataDBid']#line:811
                        OOOO0OO00O0000O00 =float (O0OO0O00OO0OOO0OO ['data']['silver'])/1000000000000 #line:812
                        OOOO0000OO000OO0O =0 #line:817
                        for O0OO0OOOOOOOO0O00 in O0OO0OOO00OOOO000 :#line:818
                            if not O0OO0OOOOOOOO0O00 :#line:819
                                O00O0000O0OO00O0O =f'_crop_id={O0OOOO0O000O000OO}&site={OOOO0000OO000OO0O}_{OO00O000O0O00OOO0.time}'#line:820
                                OOO000OOOO0O00OOO ={'source':'scsc','authorization':OO00O000O0O00OOO0 .token ,'timestamp':OO00O000O0O00OOO0 .time ,'sign':sign (O00O0000O0OO00O0O ),'signstring':O00O0000O0OO00O0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:830
                                OO0OOO0O00O0O00O0 ={"site":OOOO0000OO000OO0O ,"crop_id":O0OOOO0O000O000OO }#line:831
                                OOO000O0000O00OOO =requests .request ('post',f'{host}/game/crops/buy',headers =OOO000OOOO0O00OOO ,data =OO0OOO0O00O0O00O0 ).json ()#line:832
                                time .sleep (random .randint (1 ,3 )/10 )#line:834
                                if 'status'in OOO000O0000O00OOO :#line:835
                                    if OOO000O0000O00OOO ['status']==200 :#line:836
                                        if OOO000O0000O00OOO ['message']=='种子数量不足':#line:837
                                            OO0O0OOO0OOO000O0 =OO00O000O0O00OOO0 .level_new ()#line:838
                                            print (f'【种植合成】:{OOO000O0000O00OOO["message"]}')#line:839
                                            if not OO00O000O0O00OOO0 .user_ad ():#line:840
                                                return False #line:841
                                    if OOO000O0000O00OOO ['status']==500 :#line:842
                                        print (f'【种植合成】:{OOO000O0000O00OOO["message"]}')#line:843
                                        return False #line:844
                            OOOO0000OO000OO0O +=1 #line:845
                        OO00OOOOOO00O00OO =requests .request ('get',f'{host}/game/getAllData',headers =OO00OO0O000O0O0O0 ).json ()#line:846
                        O0OOO0OOO00O000OO =OO00OOOOOO00O00OO ['data']['cropList']#line:847
                        O000O0000O000OO00 =False #line:848
                        for O0OO0OOOOOOOO0O00 in range (12 ):#line:849
                            id =O0OOO0OOO00O000OO [O0OO0OOOOOOOO0O00 ]['level']#line:850
                            if float (OO0O0OOO0OOO000O0 )-float (id )>9 :#line:851
                                OO0O0O00O000000OO =f'_site={O0OO0OOOOOOOO0O00}_{timi_new()}'#line:852
                                OO00O0O0O00O00000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00O000O0O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (OO0O0O00O000000OO ),'signstring':OO0O0O00O000000OO ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:863
                                OOOOOOOO00OOO00O0 ={"site":O0OO0OOOOOOOO0O00 }#line:864
                                O0OO00O0O0O00O00O =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO00O0O0O00O00000 ,data =OOOOOOOO00OOO00O0 ).json ()#line:866
                                if 'status'in O0OO00O0O0O00O00O :#line:867
                                    if O0OO00O0O0O00O00O ['status']==200 :#line:868
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:869
                            if id !=0 :#line:870
                                for O0O000OO0OO0O00O0 in range (11 ):#line:871
                                    O000O0OOO0O0O0000 =O0O000OO0OO0O00O0 +1 #line:872
                                    g =O0OOO0OOO00O000OO [O000O0OOO0O0O0000 ]['level']#line:873
                                    if id ==g :#line:874
                                        OO00O0OOO000O0000 =O0O000OO0OO0O00O0 +2 #line:875
                                        if OO00O0OOO000O0000 !=O0OO0OOOOOOOO0O00 +1 :#line:876
                                            O0OO0O00OO00000OO =O0OO0OOOOOOOO0O00 +1 #line:877
                                            time .sleep (random .randint (1 ,3 )/10 )#line:879
                                            O000OOO00000OOOO0 =f'_site={O0OO0O00OO00000OO - 1}&targetSite={OO00O0OOO000O0000 - 1}_{timi_new()}'#line:880
                                            O00000O00000O0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OO00O000O0O00OOO0 .token ,'timestamp':timi_new (),'sign':sign (O000OOO00000OOOO0 ),'signstring':O000OOO00000OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:897
                                            O0O0OO000OO00OO00 ={"site":int (O0OO0O00OO00000OO -1 ),"targetSite":int (OO00O0OOO000O0000 -1 )}#line:898
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00000O00000O0OOO ,json =O0O0OO000OO00OO00 )#line:899
                                            O000O0000O000OO00 =True #line:901
                                    if O000O0000O000OO00 :#line:902
                                        break #line:903
                                if O000O0000O000OO00 :#line:904
                                    break #line:905
        except :#line:906
            OO00O000O0O00OOO0 .synthetic ()#line:907
    def level_new (OO0O00O000OOOO000 ):#line:910
        try :#line:911
            O0O00O0OO00OOOO00 =f'__{timi_new()}'#line:912
            OO00O0OOO0OO00OO0 ={'source':'scsc','authorization':OO0O00O000OOOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O0OO00OOOO00 ),'signstring':O0O00O0OO00OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:923
            OOOO0O0OOO00OO000 =requests .request ('get',f'{host}/user',headers =OO00O0OOO0OO00OO0 ).json ()#line:924
            if 'status'in OOOO0O0OOO00OO000 :#line:925
                if OOOO0O0OOO00OO000 ['status']==200 :#line:926
                    return float (OOOO0O0OOO00OO000 ['data']['level'])#line:927
        except Exception as OO0O0O0O000O0O0O0 :#line:928
            print (OO0O0O0O000O0O0O0 )#line:929
    def propsraffle (OOOO00O00OO0O000O ):#line:932
        try :#line:933
            while True :#line:934
                OO00O0OO0O000O0O0 =f'__{timi_new()}'#line:935
                O0OO000O000O00O00 ={'source':'scsc','authorization':OOOO00O00OO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OO0O000O0O0 ),'signstring':OO00O0OO0O000O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:946
                OO0000OO0000O0OO0 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0OO000O000O00O00 ).json ()#line:947
                if 'status'in OO0000OO0000O0OO0 :#line:949
                    if OO0000OO0000O0OO0 ['status']==200 :#line:950
                        OOOOO0O000OOOOOOO =OO0000OO0000O0OO0 ['data']['rows']#line:951
                        O00OOO0O0000O0O0O =OO0000OO0000O0OO0 ['data']['vstate']#line:952
                        if OOOOO0O000OOOOOOO ==5 or OOOOO0O000OOOOOOO ==6 or OOOOO0O000OOOOOOO ==7 :#line:953
                            O000O0O00OO00O0O0 =OO0000OO0000O0OO0 ['data']['silver']#line:954
                            print (f'【转盘抽奖】:获得种子:{O000O0O00OO00O0O0}')#line:955
                        if OOOOO0O000OOOOOOO ==1 or OOOOO0O000OOOOOOO ==2 or OOOOO0O000OOOOOOO ==3 :#line:956
                            OO00O0O0OO000O000 =OO0000OO0000O0OO0 ['data']['clover']#line:957
                            print (f'【转盘抽奖】:获得三叶草:{OO00O0O0OO000O000}')#line:958
                        if OOOOO0O000OOOOOOO ==4 or OOOOO0O000OOOOOOO ==8 :#line:959
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:960
                        if OOOOO0O000OOOOOOO =='抽奖次数已用完':#line:964
                            break #line:998
                time .sleep (random .randint (8 ,15 )/10 )#line:999
        except Exception as OOOOOO0O000O00000 :#line:1000
            print (OOOOOO0O000O00000 )#line:1001
    def friends_invitation (O0O0O00OO0O0OO00O ):#line:1004
        try :#line:1005
            OO0OO0OOOO0OOOO0O =f'__{timi_new()}'#line:1006
            OO0000OOOO00O00O0 ={'source':'scsc','authorization':O0O0O00OO0O0OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OO0OOOO0OOOO0O ),'signstring':OO0OO0OOOO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1017
            O0O00OO00000OO00O =requests .request ('get',f'{host}/friends',headers =OO0000OOOO00O00O0 ).json ()#line:1018
            if 'status'in O0O00OO00000OO00O :#line:1019
                if O0O00OO00000OO00O ['status']==200 :#line:1020
                    O0O0OO000OO0O000O =O0O00OO00000OO00O ['data']['myInviteter']#line:1021
                    if O0O0OO000OO0O000O :#line:1022
                        OOO0O0O0O00000OOO =O0O0OO000OO0O000O ['user']['nickname']#line:1023
                        O00OO0OOO0OOO000O =O0O0O00OO0O0OO00O .certification ()#line:1024
                        print (f'【查邀请人】:我的邀请人:{OOO0O0O0O00000OOO}丨实名:{O00OO0OOO0OOO000O}')#line:1025
                    else :#line:1026
                        if O0O0O00OO0O0OO00O .innerId !='0':#line:1027
                            O0O0O00OO0O0OO00O .invitation ()#line:1028
        except Exception as O00O0OOO00OO0O000 :#line:1029
            print (O00O0OOO00OO0O000 )#line:1030
    def add_clover (OOO00000OOO0O000O ):#line:1033
        global golden_seed #line:1034
        try :#line:1035
            O0000OOOO0O00000O =f'__{timi_new()}'#line:1036
            O0O0000OOOO000000 ={'source':'scsc','authorization':OOO00000OOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0O00000O ),'signstring':O0000OOOO0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1047
            OO0OO0OO000O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =O0O0000OOOO000000 ).json ()#line:1048
            if 'status'in OO0OO0OO000O0O0O0 :#line:1050
                if OO0OO0OO000O0O0O0 ['status']==200 :#line:1051
                    O0OOO00O0OO0O0000 =OO0OO0OO000O0O0O0 ['data']['clover']#line:1052
                    O0OOO0O00000O0OOO =OO0OO0OO000O0O0O0 ['data']['used_clover']#line:1053
                    O00O00OO00O00O0O0 =float (O0OOO00O0OO0O0000 )-float (O0OOO0O00000O0OOO )#line:1054
                    print (f'【参与抽奖】:参与抽奖的☘️:{O0OOO0O00000O0OOO}')#line:1055
                    if OOO00000OOO0O000O .certification ()!='未实名':#line:1056
                        if O00O00OO00O00O0O0 >1 :#line:1057
                            O0000OOOO0O00000O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O00O00OO00O00O0O0)}_{timi_new()}'#line:1058
                            OOO00000O00OOO0OO ={'source':'scsc','authorization':OOO00000OOO0O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000OOOO0O00000O ),'signstring':O0000OOOO0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1069
                            OO0000O0OO0OO00OO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O00O00OO00O00O0O0 )}#line:1070
                            OOOOOO000OO00OOOO =requests .request ('post',f'{host}/lottery/add-stake',headers =OOO00000O00OOO0OO ,data =OO0000O0OO0OO00OO ).json ()#line:1071
                            if 'status'in OOOOOO000OO00OOOO :#line:1073
                                if OOOOOO000OO00OOOO ['status']==200 :#line:1074
                                    print (f'【参与抽奖】:添加☘️:{OOOOOO000OO00OOOO["data"]}丨数量:{O00O00OO00O00O0O0}')#line:1075
                                if OOOOOO000OO00OOOO ['status']==500 :#line:1076
                                    print (f'【参与抽奖】:添加☘️:{OOOOOO000OO00OOOO["message"]}')#line:1077
            O0OOO00OOOO0O0000 =requests .request ('get',f'{host}/lottery',headers =O0O0000OOOO000000 ).json ()#line:1078
            O0OOOOOO00OO0000O =OOO00000OOO0O000O .winning_rewards ()#line:1080
            if 'status'in O0OOO00OOOO0O0000 :#line:1081
                if O0OOO00OOOO0O0000 ['status']==200 :#line:1082
                    OO00OO0O0O0O0OOOO =O0OOO00OOOO0O0000 ['data'][0 ]['day_get_gold_quantity']#line:1083
                    golden_seed +=float (OO00OO0O0O0O0OOOO )#line:1084
                    O0000O000OOO0O0O0 =O0OOO00OOOO0O0000 ['data'][1 ]['value']#line:1085
                    O0OO00000OO00O0OO =O0OOO00OOOO0O0000 ['data'][0 ]['join_number']#line:1086
                    OO00OOOOO00OO0O00 =int (float (O0OOO00OOOO0O0000 ['data'][0 ]['totalValue']))#line:1087
                    O0000O00OO0OOO000 =float (O0000O000OOO0O0O0 /OO00OOOOO00OO0O00 )*10000 #line:1088
                    OOOOO00O0OO0OO00O =OO00OOOOO00OO0O00 /O0OO00000OO00O0OO #line:1089
                    print (f'【参与抽奖】:预计每天中{str(OO00OO0O0O0O0OOOO)[:6]}颗金种子丨好友收益:{str(O0OOOOOO00OO0000O)[:6]}')#line:1090
                    print (f'【抽奖统计】:每1万☘️中{str(O0000O00OO0OOO000)[:6]}颗金种子丨☘️人均:{str(OOOOO00O0OO0OO00O)[:7]}️')#line:1091
        except Exception as OO00O0OOOO000O000 :#line:1092
            print (OO00O0OOOO000O000 )#line:1093
    def energy (OOO000OOOO0OOO00O ):#line:1097
        try :#line:1098
            while True :#line:1099
                OOOOOOO0O0OOOOO0O =f'__{timi_new()}'#line:1100
                OOO0OOOO000OOO000 ={'source':'scsc','authorization':OOO000OOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOOOO0O0OOOOO0O ),'signstring':OOOOOOO0O0OOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1111
                O00O0O00O0OO000O0 =requests .request ('get',f'{host}/energy/general',headers =OOO0OOOO000OOO000 ).json ()#line:1112
                if 'status'in O00O0O00O0OO000O0 :#line:1114
                    if O00O0O00O0OO000O0 ['status']==200 :#line:1115
                        OOO00OOOO00O000O0 =O00O0O00O0OO000O0 ['data']['ordinary_water']#line:1116
                        O0O00OOO0O000OO0O =O00O0O00O0OO000O0 ['data']['ordinary_fertilizer']#line:1117
                        OO0OOOOOOOO00O0O0 =O00O0O00O0OO000O0 ['data']['videoStatus']#line:1118
                        O0O0O0OO000000OO0 =O00O0O00O0OO000O0 ['data']['waterVideoKey']#line:1119
                        print (f'【我的营养】:肥料:{str(O0O00OOO0O000OO0O).split(".")[0]}丨水滴:{str(OOO00OOOO00O000O0).split(".")[0]}')#line:1120
                        if float (O0O00OOO0O000OO0O )<96 :#line:1121
                            if OO0OOOOOOOO00O0O0 :#line:1122
                                time .sleep (random .randint (160 ,180 )/10 )#line:1123
                                OO00O000000O0000O =99 -float (O0O00OOO0O000OO0O )#line:1124
                                OO0O0OOO000OOOOOO ={"fertilizer":str (OO00O000000O0000O ).split ('.')[0 ]}#line:1125
                                O000OOO0OO00000O0 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OOO0OOOO000OOO000 ).json ()#line:1126
                                if 'status'in O000OOO0OO00000O0 :#line:1128
                                    if O000OOO0OO00000O0 ['status']==200 :#line:1129
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO0OO00000O0["message"]}')#line:1130
                                    if O000OOO0OO00000O0 ['status']==500 :#line:1131
                                        print (f'【购买肥料】:看广告获取肥料:{O000OOO0OO00000O0["message"]}')#line:1132
                                        break #line:1133
                                if float (O0O00OOO0O000OO0O )<78 :#line:1135
                                    OO00O000000O0000O =80 -float (O0O00OOO0O000OO0O )#line:1136
                                    OOO00O0O0O0000O00 =f'_fertilizer={int(OO00O000000O0000O)}_{timi_new()}'#line:1137
                                    O00000OOO0O00O0OO ={'source':'scsc','authorization':OOO000OOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0O0O0000O00 ),'signstring':OOO00O0O0O0000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1148
                                    O0O00OOO000O0OO0O ={"fertilizer":int (OO00O000000O0000O )}#line:1149
                                    O0O00OOOO00O00OOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O00000OOO0O00O0OO ,data =O0O00OOO000O0OO0O ).json ()#line:1151
                                    if 'status'in O0O00OOOO00O00OOO :#line:1153
                                        if O0O00OOOO00O00OOO ['status']==200 :#line:1154
                                            print (f'【购买肥料】:购买肥料:{O0O00OOOO00O00OOO["message"]}丨数量:{int(OO00O000000O0000O)}')#line:1155
                                        if O0O00OOOO00O00OOO ['status']==500 :#line:1156
                                            print (f'【购买肥料】:购买肥料:{O0O00OOOO00O00OOO["message"]}丨数量:{int(OO00O000000O0000O)}')#line:1157
                                            OO0O0000O000OOOO0 =O0O00OOOO00O00OOO ["message"].split ('-')[1 ]#line:1158
                                            OOO0O0O0OOO000O00 =f'__{timi_new()}'#line:1159
                                            OO0O00OOO0O0OO000 ={'source':'scsc','authorization':OOO000OOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOO000O00 ),'signstring':OOO0O0O0OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1170
                                            O0000OO000OOO0O00 =requests .request ('get',f'{host}/user',headers =OO0O00OOO0O0OO000 ).json ()#line:1171
                                            if 'status'in O0000OO000OOO0O00 :#line:1172
                                                if O0000OO000OOO0O00 ['status']==200 :#line:1173
                                                    O00000O00O000OO00 =O0000OO000OOO0O00 ['data']['inner_id']#line:1174
                                                    if give_gold (O00000O00O000OO00 ,float (OO0O0000O000OOOO0 )+1 ):#line:1175
                                                        OOO000OOOO0OOO00O .energy ()#line:1176
                        if float (OOO00OOOO00O000O0 )<880 :#line:1177
                            if O0O0O0OO000000OO0 :#line:1178
                                time .sleep (random .randint (160 ,180 )/10 )#line:1179
                                OOOOOOO00OO0O000O =999 -float (OOO00OOOO00O000O0 )#line:1180
                                O00000OO00O00O0O0 ={"water":str (OOOOOOO00OO0O000O ).split ('.')[0 ]}#line:1181
                                O0OO0OO0O00OOOOO0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OOO0OOOO000OOO000 ).json ()#line:1182
                                if 'status'in O0OO0OO0O00OOOOO0 :#line:1184
                                    if O0OO0OO0O00OOOOO0 ['status']==200 :#line:1185
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO0OO0O00OOOOO0["message"]}')#line:1186
                                    if O0OO0OO0O00OOOOO0 ['status']==500 :#line:1187
                                        print (f'【购买水滴】:看广告获取水滴:{O0OO0OO0O00OOOOO0["message"]}')#line:1188
                                        break #line:1189
                                if float (OOO00OOOO00O000O0 )<780 :#line:1190
                                    OOOOOOO00OO0O000O =800 -float (OOO00OOOO00O000O0 )#line:1191
                                    OOO0O00O00O0OO0O0 =f'_water={int(OOOOOOO00OO0O000O)}_{timi_new()}'#line:1192
                                    OOO00O000O0O0OO0O ={'source':'scsc','authorization':OOO000OOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O00O00O0OO0O0 ),'signstring':OOO0O00O00O0OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1203
                                    O0O000O0OOOO0OOOO ={"water":int (OOOOOOO00OO0O000O )}#line:1204
                                    OO00OO000OO00OOO0 =requests .request ('post',f'{host}/energy/general/buy/water',headers =OOO00O000O0O0OO0O ,data =O0O000O0OOOO0OOOO ).json ()#line:1206
                                    if 'status'in OO00OO000OO00OOO0 :#line:1208
                                        if OO00OO000OO00OOO0 ['status']==200 :#line:1209
                                            print (f'【购买水滴】:购买水滴:{OO00OO000OO00OOO0["message"]}丨数量:{int(OOOOOOO00OO0O000O)}')#line:1210
                                        if OO00OO000OO00OOO0 ['status']==500 :#line:1211
                                            print (f'【购买水滴】:购买水滴:{OO00OO000OO00OOO0["message"]}丨数量:{int(OOOOOOO00OO0O000O)}')#line:1212
                                            OO0O0000O000OOOO0 =OO00OO000OO00OOO0 ["message"].split ('-')[1 ]#line:1213
                                            OOO0O0O0OOO000O00 =f'__{timi_new()}'#line:1214
                                            OO0O00OOO0O0OO000 ={'source':'scsc','authorization':OOO000OOOO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0O0OOO000O00 ),'signstring':OOO0O0O0OOO000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1225
                                            O0000OO000OOO0O00 =requests .request ('get',f'{host}/user',headers =OO0O00OOO0O0OO000 ).json ()#line:1226
                                            if 'status'in O0000OO000OOO0O00 :#line:1227
                                                if O0000OO000OOO0O00 ['status']==200 :#line:1228
                                                    O00000O00O000OO00 =O0000OO000OOO0O00 ['data']['inner_id']#line:1229
                                                    if give_gold (O00000O00O000OO00 ,float (OO0O0000O000OOOO0 )+1 ):#line:1230
                                                        OOO000OOOO0OOO00O .energy ()#line:1231
                        break #line:1232
        except Exception as OO00OO0OOOO0O0000 :#line:1233
            print (OO00OO0OOOO0O0000 )#line:1234
def bundled_def ():#line:1236
    O000O000O0O000O00 =['5570536','7750212','7911652','7911680','7805624']#line:1237
    return O000O000O0O000O00 [random .randint (0 ,len (O000O000O0O000O00 )-1 )]#line:1238
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
        OO0000O00O0OOOO0O =gitee_edition ()#line:1268
        if version_of_the_validation ()<OO0000O00O0OOOO0O ['CityEarth']['edition']:#line:1269
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000O00O0OOOO0O["CityEarth"]["edition"]}   ❌')#line:1270
            print (f'更新内容=>>{OO0000O00O0OOOO0O["CityEarth"]["content"]}   🎉')#line:1271
        else :#line:1272
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0000O00O0OOOO0O["CityEarth"]["edition"]}   ✅')#line:1273
            print (f'更新内容=>> {OO0000O00O0OOOO0O["CityEarth"]["content"]}   🎉')#line:1274
    except Exception as OO0O0O0OOOOOOOO00 :#line:1275
        print (OO0O0O0OOOOOOOO00 )#line:1276
def sc3 ():#line:1278
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1279
if __name__ =='__main__':#line:1283
    start ()#line:1284
