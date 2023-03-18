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
@ 版本  4.5
"""
##################################配置区##################################
time_xx = random.randint(12, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419554311'#line:1
git ='https://gitee.com'#line:2
host ='http://scsc.sc19319.com'#line:3
golden_seed =0 #line:4
count_list =0 #line:5
msg_list =[]#line:6
invited_new =[]#line:7
weishim =[]#line:8
def start ():#line:11
    try :#line:12
        O000OO000O0O00OOO00 ()#line:13
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:14
        O000OO0O00OO00O00 ()#line:15
        O0O0OO0OO0000O0OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:16
        print (f"==========共找到{len(O0O0OO0OO0000O0OO)}个账号==========")#line:17
        for O00000OOO0O0O0OOO in O0O0OO0OO0000O0OO :#line:18
            OOO0OO00OO0O0OO00 =[]#line:19
            print (f"------------正在执行第{O0O0OO0OO0000O0OO.index(O00000OOO0O0O0OOO) + 1}个账号------------")#line:20
            OOO000O000O0O0O00 =CityEarth (O00000OOO0O0O0OOO ,OOO0OO00OO0O0OO00 ,O0O0OO0OO0000O0OO .index (O00000OOO0O0O0OOO ))#line:21
            def OO0OO0OO0000O0OOO ():#line:23
                if OOO000O000O0O0O00 .base_info ():#line:25
                    OOO000O000O0O0O00 .sealing ()#line:27
                    OOO000O000O0O0O00 .invitenum ()#line:29
                    OOO000O000O0O0O00 .query_to_sell ()#line:31
                    OOO000O000O0O0O00 .friends_invitation ()#line:35
                    OOO000O000O0O0O00 .energy ()#line:37
                    OOO000O000O0O0O00 .add_clover ()#line:39
                    OOO000O000O0O0O00 .propsraffle ()#line:41
                    OOO000O000O0O0O00 .synthetic ()#line:43
                    OOO000O000O0O0O00 .crops_illustrated ()#line:45
                    OOO000O000O0O0O00 .withdraw ()#line:47
                    if float (datetime .datetime .now ().hour )>8 :#line:48
                        OOO000O000O0O0O00 .give_gold ()#line:50
            O0OO00OO0OO0O0000 =threading .Thread (target =OO0OO0OO0000O0OOO )#line:52
            O0OO00OO0OO0O0000 .start ()#line:53
            time .sleep (time_xx )#line:54
        print (f"------------正在处理数据------------")#line:55
        time .sleep (0.5 )#line:56
        OO00OOO00O0OO0O0O =format_msg ()#line:57
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO00OOO00O0OO0O0O +' ')#line:58
        time .sleep (15 )#line:59
        print (f'所有未出售的芦荟:{count_list}颗')#line:60
        print ('开始打印好友数量不足2的ID')#line:61
        for OO00O000OOOOO00O0 in invited_new :#line:62
            print (OO00O000OOOOO00O0 )#line:63
        print ('开始打印未实名的token')#line:64
        for O0OO0OO0O00000OO0 in weishim :#line:65
            print (O0OO0OO0O00000OO0 )#line:66
    except Exception as O000O0OOO0O00OO00 :#line:67
        print (O000O0OOO0O00OO00 )#line:68
def give_gold (O000O00OOO00O0OO0 ,OO0O0OOO0O0OO0000 ):#line:72
    try :#line:73
        O0000O00OOO00OO00 =f'_doneeNo={O000O00OOO00O0OO0}&quantity={int(OO0O0OOO0O0OO0000)}_{timi_new()}'#line:74
        OOOO0O00O0OO0O00O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000O00OOO00OO00 ),'signstring':O0000O00OOO00OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:85
        OO00O0O00O00OOOOO ={"quantity":int (OO0O0OOO0O0OO0000 ),"doneeNo":O000O00OOO00O0OO0 }#line:89
        OOO0000O000OOOO0O =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO0O00O0OO0O00O ,data =OO00O0O00O00OOOOO ).json ()#line:90
        if 'status'in OOO0000O000OOOO0O :#line:92
            if OOO0000O000OOOO0O ['status']==200 :#line:93
                if OOO0000O000OOOO0O ['data']:#line:94
                    print (f'【赠送种子】:赠送{int(OO0O0OOO0O0OO0000)}种子给{O000O00OOO00O0OO0}成功')#line:95
                    return True #line:96
            if OOO0000O000OOOO0O ['status']==401 :#line:97
                print (f'【赠送种子】:{OOO0000O000OOOO0O["message"]}')#line:98
                return False #line:99
            if OOO0000O000OOOO0O ['status']==500 :#line:100
                print (f'【赠送种子】:{OOO0000O000OOOO0O["message"]}')#line:101
                return False #line:102
        return False #line:103
    except Exception as OOO0O00OO0O00000O :#line:104
        print (OOO0O00OO0O00000O )#line:105
def kvkv ():#line:108
    return '/vastzzzl/vastzzzl/raw/master'#line:109
def oyoy ():#line:111
    return '卡密未激活   ❌'#line:112
def sign (O000000000OOO00O0 ):#line:115
    O000OOOOO000000OO =hashlib .md5 (O000000000OOO00O0 .encode ()).hexdigest ()#line:116
    O00000000OOO0OOOO =sc1 ()#line:117
    O00O0OOOOO00OO00O =sc2 ()#line:118
    O000OO0000O00OO00 =sc3 ()#line:119
    O0O000O0OOO00000O =O00000000OOO0OOOO +O000OOOOO000000OO +O00O0OOOOO00OO00O +O000OO0000O00OO00 #line:120
    O00OO0O0000O00000 =hashlib .md5 (O0O000O0OOO00000O .encode ()).hexdigest ()#line:121
    return O00OO0O0000O00000 #line:122
def format_msg ():#line:125
    OO0000000O0OO0OOO =""#line:126
    for OO0OOO00OOOO00OO0 in msg_list :#line:127
        OO0000000O0OO0OOO +=str (OO0OOO00OOOO00OO0 )+"\r\n"#line:128
    return OO0000000O0OO0OOO #line:129
def sc1 ():#line:132
    return "scsc%^&*"#line:133
def O000OO0O00OO00O00 ():#line:136
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:137
        ubbbf ()#line:138
    else :#line:139
        print (oyoy ())#line:140
        exit (1 )#line:141
def timi_new ():#line:144
    return str (int (time .time ()*1000 ))#line:145
json_path ="CityEarth_data.json"#line:148
json_path1 ="CityEarth_data.json"#line:149
dict ={}#line:150
def get_json_data (OO0000000O0O0OO0O ,O0OOOO0O0OOO0O000 ,O00OOO0OO000OO00O ,O0O00O000O0OOO00O ):#line:153
    with open (OO0000000O0O0OO0O ,'rb')as OO0000OO0O00OO0O0 :#line:154
        OOOOO0O00O0O00OO0 =json .load (OO0000OO0O00OO0O0 )#line:155
        OOOOO0O00O0O00OO0 ['data'][O0OOOO0O0OOO0O000 ][O00OOO0OO000OO00O ]=O0O00O000O0OOO00O #line:156
        OO0OOO00O00000OOO =OOOOO0O00O0O00OO0 #line:157
    OO0000OO0O00OO0O0 .close ()#line:158
    return OO0OOO00O00000OOO #line:159
def write_json_data (O0OOOOO000OOO00OO ):#line:162
    with open (json_path1 ,'w')as O0OO0OO0O000O0O0O :#line:163
        json .dump (O0OOOOO000OOO00OO ,O0OO0OO0O000O0O0O )#line:164
    O0OO0OO0O000O0O0O .close ()#line:165
    return True #line:166
class CityEarth :#line:169
    def __init__ (O0OOOO0OO0O0000O0 ,O000OO00000OOO0O0 ,O0000O0O0O0OOOO0O ,O00000O0OO0O0O000 ):#line:171
        try :#line:172
            O0OOOO0OO0O0000O0 .msg =O0000O0O0O0OOOO0O #line:173
            O0OOOO0OO0O0000O0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:174
            O0OOOO0OO0O0000O0 .token =O000OO00000OOO0O0 ['authorization']#line:175
            O0OOOO0OO0O0000O0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:176
            O0OOOO0OO0O0000O0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:177
            O0OOOO0OO0O0000O0 .elephant_user =O000OO00000OOO0O0 ['elephant_user']#line:178
            O0OOOO0OO0O0000O0 .elephant_pswd =O000OO00000OOO0O0 ['elephant_pswd']#line:179
            O0OOOO0OO0O0000O0 .elephant_Task_ID =O000OO00000OOO0O0 ['elephant_Task_ID']#line:180
            O0OOOO0OO0O0000O0 .len_new =O00000O0OO0O0O000 #line:181
        except :#line:182
            print ('变量格式错误')#line:183
    def base_info (OO00000O0OOOO00O0 ):#line:186
        try :#line:187
            OO00000O0OOOO00O0 .watched_ad ()#line:189
            O00O0OOOOOOOOOO0O =f'__{timi_new()}'#line:190
            O000OOO0OOOO000OO ={'source':'scsc','authorization':OO00000O0OOOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOOOOOOOO0O ),'signstring':O00O0OOOOOOOOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:201
            O00O0OO0000O0OOOO =requests .request ('get',f'{host}/user',headers =O000OOO0OOOO000OO ).json ()#line:202
            if 'status'in O00O0OO0000O0OOOO :#line:204
                if O00O0OO0000O0OOOO ['status']==200 :#line:205
                    O00O000OOO000OOOO =O00O0OO0000O0OOOO ['data']['nickname']#line:206
                    OOO0OOOOOO0000OO0 =O00O0OO0000O0OOOO ['data']['inner_id']#line:207
                    O00O0OO0OOO00OO00 =O00O0OO0000O0OOOO ['data']['assets']['gold']#line:208
                    O0O000OO00O0O000O =O00O0OO0000O0OOOO ['data']['level']#line:209
                    print (f'【账号信息】:昵称:{O00O000OOO000OOOO[:5]}丨ID:{OOO0OOOOOO0000OO0}丨等级:{O0O000OO00O0O000O}丨金种子:{str(O00O0OO0OOO00OO00).split(".")[0]}')#line:211
                    if 'wx_'in O00O000OOO000OOOO :#line:212
                        OO00000O0OOOO00O0 .change_nickname ()#line:213
                if O00O0OO0000O0OOOO ['status']==401 :#line:214
                    print ('【账号信息】:账号失效正在尝试登录')#line:215
                    if OO00000O0OOOO00O0 .elephant_user =='f':#line:216
                        return False #line:217
                    OOOOO0000OO0O00O0 =Invalid_login .addtask (elephant_user =OO00000O0OOOO00O0 .elephant_user ,elephant_pswd =OO00000O0OOOO00O0 .elephant_pswd ,elephant_Task_ID =OO00000O0OOOO00O0 .elephant_Task_ID )#line:220
                    O00O00000000OO000 =get_json_data (json_path ,OO00000O0OOOO00O0 .len_new ,'authorization',OOOOO0000OO0O00O0 )#line:221
                    if write_json_data (O00O00000000OO000 ):#line:222
                        print ('正在写入账号配置文件')#line:223
                    return False #line:224
                if O00O0OO0000O0OOOO ['status']==500 :#line:225
                    return False #line:226
            return True #line:227
        except Exception as O0OOO00O0O000O000 :#line:228
            print (O0OOO00O0O000O000 )#line:229
    def sealing (OOO0000OO00O0OO00 ):#line:232
        try :#line:233
            O0O0OOO0O00O00O0O =f'__{timi_new()}'#line:234
            OOO00O0OOO0OO0O00 ={'source':'scsc','authorization':OOO0000OO00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OOO0O00O00O0O ),'signstring':O0O0OOO0O00O00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:245
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =OOO00O0OOO0OO0O00 )#line:246
            requests .request ('get',f'{host}/packsack/list',headers =OOO00O0OOO0OO0O00 )#line:247
            requests .request ('get',f'{host}/friends/invited/ad',headers =OOO00O0OOO0OO0O00 )#line:248
            requests .request ('get',f'{host}/assets/gold/rank',headers =OOO00O0OOO0OO0O00 )#line:249
            requests .request ('get',f'{host}/user',headers =OOO00O0OOO0OO0O00 )#line:250
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =OOO00O0OOO0OO0O00 )#line:251
            requests .request ('get',f'{host}/finance/get-power-list',headers =OOO00O0OOO0OO0O00 )#line:252
            requests .request ('post',f'{host}/announcement/announcement',headers =OOO00O0OOO0OO0O00 )#line:253
            requests .request ('get',f'{host}/game/getAllData',headers =OOO00O0OOO0OO0O00 )#line:254
            requests .request ('get',f'{host}/assets',headers =OOO00O0OOO0OO0O00 )#line:255
        except Exception as O00OO0O0O0O00OOO0 :#line:256
            print (O00OO0O0O0O00OOO0 )#line:257
    def ddd (OOOO0OO00OOOO00OO ):#line:259
        try :#line:260
            OO0O00O0OO000OO00 =f'page=1&pageSize=20&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F__{timi_new()}'#line:261
            O000O000O0O0OOOOO ={'source':'scsc','authorization':OOOO0OO00OOOO00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00O0OO000OO00 ),'signstring':OO0O00O0OO000OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0OO00O0OO00O0O0 =requests .request ('get',f'{host}/market/get-crop-ask-to-buy-list?page=1&queryField=%E6%B0%B4%E6%99%B6%E8%8A%A6%E8%8D%9F&pageSize=20',headers =O000O000O0O0OOOOO ).json ()#line:273
            print (OO0OO00O0OO00O0O0 )#line:274
        except Exception as O000OOOO00O000O00 :#line:277
            print (O000OOOO00O000O00 )#line:278
    def the_query (O0O00OO000000O00O ):#line:283
        try :#line:284
            OO00O000000O00OO0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:285
            O0000OO0O0OO000O0 ={'authorization':O0O00OO000000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000000O00OO0 ),'signstring':OO00O000000O00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:295
            OOOOO000OO000OO0O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0000OO0O0OO000O0 ).json ()#line:297
            if 'status'in OOOOO000OO000OO0O :#line:299
                if OOOOO000OO000OO0O ['status']==200 :#line:300
                    O0OOOOOO00O00O00O =OOOOO000OO000OO0O ['data']['rows'][4 ]['price']#line:301
                    return O0OOOOOO00O00O00O #line:302
        except Exception as O0O00000O000O0000 :#line:303
            print (O0O00000O000O0000 )#line:304
    def market_sale (OO0OOO0O0O00000O0 ,OOOOO0O0OOO0O00O0 ):#line:307
        try :#line:308
            OO0O0OO0000000000 =timi_new ()#line:309
            O0O0OOOO0OOO00OOO =f'type=crop__{OO0O0OO0000000000}'#line:310
            OO0O00OOO0OO0O000 ={'source':'scsc','authorization':OO0OOO0O0O00000O0 .token ,'timestamp':str (OO0O0OO0000000000 ),'sign':sign (O0O0OOOO0OOO00OOO ),'signstring':O0O0OOOO0OOO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:321
            O0OOOO0OO0OOOO000 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OO0O00OOO0OO0O000 ).json ()#line:323
            if 'status'in O0OOOO0OO0OOOO000 :#line:325
                if O0OOOO0OO0OOOO000 ['status']==200 :#line:326
                    if O0OOOO0OO0OOOO000 ['data']['rows']:#line:327
                        O0O0O0O0OOOOOO000 =O0OOOO0OO0OOOO000 ['data']['rows'][0 ]['packsackItemId']#line:328
                        O000OO0OOO0OO0O00 =O0OOOO0OO0OOOO000 ['data']['rows'][0 ]['quantity']#line:329
                        O0O0O00000OOO0OOO =float (OOOOO0O0OOO0O00O0 )-0.001 #line:330
                        if O0O0O00000OOO0OOO >9 :#line:331
                            O0O0OO000OO0OOO00 =f'_packsackItemId={O0O0O0O0OOOOOO000}&price={str(OOOOO0O0OOO0O00O0)[:5]}&quantity={O000OO0OOO0OO0O00}_{OO0O0OO0000000000}'#line:332
                            O0OO0OOOOO00OOO0O ={'source':'scsc','authorization':OO0OOO0O0O00000O0 .token ,'timestamp':str (OO0O0OO0000000000 ),'sign':sign (O0O0OO000OO0OOO00 ),'signstring':O0O0OO000OO0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:343
                            O000OO0OO00O0OO00 ={"packsackItemId":O0O0O0O0OOOOOO000 ,"price":str (OOOOO0O0OOO0O00O0 )[:5 ],"quantity":str (O000OO0OOO0OO0O00 )}#line:348
                            OOOO0000OOOOOOOOO =requests .request ('post',f'{host}/market/sale',headers =O0OO0OOOOO00OOO0O ,data =O000OO0OO00O0OO00 ).json ()#line:349
                            if 'status'in OOOO0000OOOOOOOOO :#line:351
                                if OOOO0000OOOOOOOOO ['status']==200 :#line:352
                                    print (f'【上架芦荟】:数量:{O000OO0OOO0OO0O00}丨价格:{str(OOOOO0O0OOO0O00O0)[:5]}')#line:353
        except Exception as O00OO000OO0OOO00O :#line:354
            print (O00OO000OO0OOO00O )#line:355
    def query_to_sell (OOOO00OO00000OOO0 ):#line:358
        global count_list #line:359
        try :#line:360
            OO00OOO000O0OOO00 =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:361
            OOO00000OOOO00OO0 ={'source':'scsc','authorization':OOOO00OO00000OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00OOO000O0OOO00 ),'signstring':OO00OOO000O0OOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:372
            OOO0000OOOOOOO0O0 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OOO00000OOOO00OO0 ).json ()#line:373
            if 'status'in OOO0000OOOOOOO0O0 :#line:375
                if OOO0000OOOOOOO0O0 ['status']==200 :#line:376
                    for OO000O0O0OO0O00OO in OOO0000OOOOOOO0O0 ['data']['rows']:#line:377
                        OOO000OOOOOOOO0O0 =OO000O0O0OO0O00OO ['materialKey']#line:378
                        OO00O00OO00OO0O00 =OO000O0O0OO0O00OO ['quantity']#line:379
                        OO0000O00OOOOOO00 =OO000O0O0OO0O00OO ['price']#line:380
                        OOO0OOOO0000O00OO =OO000O0O0OO0O00OO ['saleState']#line:381
                        if OOO0OOOO0000O00OO ==0 :#line:382
                            print (f'【出售订单】:名称:{OOO000OOOOOOOO0O0}丨数量:{OO00O00OO00OO0O00}丨价格:{OO0000O00OOOOOO00}')#line:383
                            count_list +=OO00O00OO00OO0O00 #line:384
                            O0O0OO0O0000O0OO0 =OOOO00OO00000OOO0 .the_query ()#line:386
                            if float (O0O0OO0O0000O0OO0 )!=float (OO0000O00OOOOOO00 ):#line:387
                                O0O000O000OO0OO00 =OO000O0O0OO0O00OO ['id']#line:388
                                if float (datetime .datetime .now ().hour )>8 :#line:389
                                    OOOO00OO00000OOO0 .cacel_sale (O0O000O000OO0OO00 )#line:390
                                    OOOO00OO00000OOO0 .market_sale (OO0000O00OOOOOO00 )#line:391
                            OOOO00OO00000OOO0 .game_map ()#line:393
        except Exception as OO0000O0OOOOO0OO0 :#line:395
            print (OO0000O0OOOOO0OO0 )#line:396
    def cacel_sale (OO00O000O000OO0OO ,OO0O00OOOOO000000 ):#line:399
        try :#line:400
            OOO0OOO0O000000O0 =f'_saleId={OO0O00OOOOO000000}_{timi_new()}'#line:401
            OOO00000O0000000O ={'source':'scsc','authorization':OO00O000O000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0O000000O0 ),'signstring':OOO0OOO0O000000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:412
            OOOO00OO0O00OO0OO ={"saleId":OO0O00OOOOO000000 }#line:413
            OO0O00OOO00O000O0 =requests .request ('post',f'{host}/market/cacel-sale',headers =OOO00000O0000000O ,data =OOOO00OO0O00OO0OO ).json ()#line:414
            if 'status'in OO0O00OOO00O000O0 :#line:416
                if OO0O00OOO00O000O0 ['status']==200 :#line:417
                    print (f'【下架出售】:{OO0O00OOO00O000O0["data"]}')#line:418
        except Exception as O0000OOO0OO0O000O :#line:419
            print (O0000OOO0OO0O000O )#line:420
    def change_nickname (OOO00OO00OOOOOO0O ):#line:423
        try :#line:424
            OO0OOO00OOOOO00O0 =timi_new ()#line:425
            O000OOO0OOOOO0OO0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:426
            OO00OOOO000OOOOO0 =requests .request ('post','https://www.qmsjmfb.com/',data =O000OOO0OOOOO0OO0 ).text #line:427
            OOOOOOOO0O000OOO0 =re .findall ('<ul><li>(.*?)</li>',OO00OOOO000OOOOO0 )[0 ][:3 ]#line:428
            OO0OO000O00O0O00O =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOOOOOOO0O000OOO0}').json ()#line:429
            O00000OO00OO000O0 =OO0OO000O00O0O00O ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:430
            O00O00000OO00OOOO ={"nickname":O00000OO00OO000O0 }#line:431
            OO00OO000O0O0O00O =f'_nickname={O00000OO00OO000O0}_{OO0OOO00OOOOO00O0}'#line:432
            OOOO00OO00O0000OO ={'source':'scsc','authorization':OOO00OO00OOOOOO0O .token ,'timestamp':OO0OOO00OOOOO00O0 ,'sign':sign (OO00OO000O0O0O00O ),'signstring':OO00OO000O0O0O00O ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:443
            OOOO0O0O000OO00O0 =requests .request ('patch',f'{host}/user/nickname',headers =OOOO00OO00O0000OO ,data =O00O00000OO00OOOO ).json ()#line:444
            if 'status'in OOOO0O0O000OO00O0 :#line:446
                if OOOO0O0O000OO00O0 ['status']==200 :#line:447
                    print (f'【修改网名】:网名:{O00000OO00OO000O0}丨{OOOO0O0O000OO00O0["message"]}')#line:448
        except Exception as O00OO0OO00O00000O :#line:449
            print (O00OO0OO00O00000O )#line:450
    def withdraw (OOO000O0O00O0OO00 ):#line:453
        try :#line:454
            OOO0OOO0OO0000OOO =f'__{timi_new()}'#line:455
            O000O00OO0OOO0OOO ={'source':'scsc','authorization':OOO000O0O00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO0000OOO ),'signstring':OOO0OOO0OO0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:466
            OOOO0O00OO0OO0OOO =requests .request ('get',f'{host}/assets',headers =O000O00OO0OOO0OOO ).json ()#line:467
            if 'status'in OOOO0O00OO0OO0OOO :#line:469
                if OOOO0O00OO0OO0OOO ['status']==200 :#line:470
                    OO0000O0000O0OO0O =OOOO0O00OO0OO0OOO ['data']['cash']#line:471
                    if float (OO0000O0000O0OO0O )>20 :#line:472
                        OOO0OOO0OO0000OOO =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:473
                        O000O00OO0OOO0OOO ={'authorization':OOO000O0O00O0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OOO0OO0000OOO ),'signstring':OOO0OOO0OO0000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:483
                        O0O0OOOO0OOOO0O0O ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:484
                        O0OOO000O0OOOO000 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O000O00OO0OOO0OOO ,data =O0O0OOOO0OOOO0O0O ).json ()#line:486
                        if 'status'in O0OOO000O0OOOO000 :#line:488
                            if O0OOO000O0OOOO000 ['status']==200 :#line:489
                                print (f'【余额提现】:{O0OOO000O0OOOO000["data"]}')#line:490
                        if 'status'in O0OOO000O0OOOO000 :#line:491
                            if O0OOO000O0OOOO000 ['status']==500 :#line:492
                                print (f'【余额提现】:{O0OOO000O0OOOO000["message"]}')#line:493
        except Exception as OO00OO0O00OO00O0O :#line:494
            print (OO00OO0O00OO00O0O )#line:495
    def invitenum (OO00O00O00O00OO0O ):#line:498
        global invited_new #line:499
        try :#line:500
            O00OOO0OOO00OO000 =f'__{timi_new()}'#line:501
            OO0O0OOOOO0O0O0OO ={'source':'scsc','authorization':OO00O00O00O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO0OOO00OO000 ),'signstring':O00OOO0OOO00OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:512
            O0O0OO00OO0O0O000 =requests .request ('get',f'{host}/invite/invitenum',headers =OO0O0OOOOO0O0O0OO ).json ()#line:513
            if 'status'in O0O0OO00OO0O0O000 :#line:515
                if O0O0OO00OO0O0O000 ['status']==200 :#line:516
                    OO0OO0OOOOO00O000 =O0O0OO00OO0O0O000 ['data']['invited_count']#line:517
                    O0O00O0000000O0OO =O0O0OO00OO0O0O000 ['data']['invited_second_count']#line:518
                    print (f'【我的邀请】:直邀好友:{OO0OO0OOOOO00O000}丨间邀好友:{O0O00O0000000O0OO}')#line:519
                    if OO0OO0OOOOO00O000 <2 :#line:520
                        O0000O00000O000OO =f'__{timi_new()}'#line:521
                        OO000OO0OO000O000 ={'source':'scsc','authorization':OO00O00O00O00OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0000O00000O000OO ),'signstring':O0000O00000O000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:532
                        OOO0O000000OO0O00 =requests .request ('get',f'{host}/user',headers =OO000OO0OO000O000 ).json ()#line:533
                        if 'status'in OOO0O000000OO0O00 :#line:535
                            if OOO0O000000OO0O00 ['status']==200 :#line:536
                                invited_new .append (OOO0O000000OO0O00 ['data']['inner_id'])#line:537
        except Exception as OOOOO000O00OO0OOO :#line:538
            print (OOOOO000O00OO0OOO )#line:539
    def game_map (OO000O000O0OOOOO0 ):#line:542
        try :#line:543
            O0OO000OOOO0000OO =f'__{timi_new()}'#line:544
            OOO00OOO0O0OOOOOO ={'source':'scsc','authorization':OO000O000O0OOOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO000OOOO0000OO ),'signstring':O0OO000OOOO0000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
            OO00OO0O0O00OOOO0 =requests .request ('get',f'{host}/game/map',headers =OOO00OOO0O0OOOOOO ).json ()#line:556
            if 'status'in OO00OO0O0O00OOOO0 :#line:558
                if OO00OO0O0O00OOOO0 ['status']==200 :#line:559
                    for OOO00OOO000O00O0O in OO00OO0O0O00OOOO0 ['data']['list'][0 ]['crops']:#line:560
                        O0O0O00OOOOOO00OO =OOO00OOO000O00O0O ['level']#line:562
                        if O0O0O00OOOOOO00OO ==41 :#line:563
                            O0OOOOOO0000O00OO =OOO00OOO000O00O0O ['crop_name']#line:564
                            O0OO0OOOO0O0O0000 =OOO00OOO000O00O0O ['count']#line:565
                            if O0OO0OOOO0O0O0000 >0 :#line:566
                                print (f'【农业资产】:{O0OOOOOO0000O00OO}丨数量:{O0OO0OOOO0O0O0000}')#line:567
                                if float (datetime .datetime .now ().hour )>8 :#line:568
                                    OO000O000O0OOOOO0 .the_query ()#line:569
        except Exception as OOOO000OO0OOO000O :#line:570
            print (OOOO000OO0OOO000O )#line:571
    def give_gold (O0000O00OOO000O0O ):#line:574
        try :#line:575
            O000OOO0O0000O0OO =f'__{timi_new()}'#line:576
            O0O0O000OO00000O0 ={'source':'scsc','authorization':O0000O00OOO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O0000O0OO ),'signstring':O000OOO0O0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:587
            O0OOOO0O0O000OOO0 =requests .request ('get',f'{host}/user',headers =O0O0O000OO00000O0 ).json ()#line:588
            if 'status'in O0OOOO0O0O000OOO0 :#line:589
                if O0OOOO0O0O000OOO0 ['status']==200 :#line:590
                    if float (O0000O00OOO000O0O .doneeNo )!=0 :#line:591
                        OOO0O0O0OOOOO0000 =O0OOOO0O0O000OOO0 ['data']['assets']['gold']#line:592
                        if float (OOO0O0O0OOOOO0000 )>float (O0000O00OOO000O0O .innerId ):#line:593
                            O0O00OO0OOOO00OO0 =int (float (OOO0O0O0OOOOO0000 )/1.1 )#line:594
                            O000OOO0O0000O0OO =f'_doneeNo={O0000O00OOO000O0O.doneeNo}&quantity={O0O00OO0OOOO00OO0}_{timi_new()}'#line:595
                            O0O0O000OO00000O0 ={'source':'scsc','authorization':O0000O00OOO000O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO0O0000O0OO ),'signstring':O000OOO0O0000O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:606
                            OOOOO00O00O0OOO0O ={"quantity":O0O00OO0OOOO00OO0 ,"doneeNo":O0000O00OOO000O0O .doneeNo }#line:610
                            O000OO0O0O0O0OO0O =requests .request ('post',f'{host}/finance/give-gold',headers =O0O0O000OO00000O0 ,data =OOOOO00O00O0OOO0O ).json ()#line:611
                            if 'status'in O000OO0O0O0O0OO0O :#line:613
                                if O000OO0O0O0O0OO0O ['status']==200 :#line:614
                                    if O000OO0O0O0O0OO0O ['data']:#line:615
                                        print (f'【赠送种子】:赠送{O0O00OO0OOOO00OO0}种子给{O0000O00OOO000O0O.doneeNo}成功')#line:616
                    else :#line:617
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:618
        except Exception as O0OOO0000O0OOO0OO :#line:619
            print (O0OOO0000O0OOO0OO )#line:620
    def invitation (OOO0O0O0O0OOOOOOO ):#line:622
        try :#line:623
            _O00OOO0000OOOO000 =float (bundled_def ())/4 #line:624
            O00OOOO000OO000O0 =f'_innerId={int(_O00OOO0000OOOO000)}_{timi_new()}'#line:625
            OOOO00OO0OOO00O0O ={'source':'scsc','authorization':OOO0O0O0O0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOOO000OO000O0 ),'signstring':O00OOOO000OO000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:636
            OO00OOO0OOO00OOOO ={"innerId":int (_O00OOO0000OOOO000 )}#line:637
            requests .request ('post',f'{host}/friends/my-invitation',headers =OOOO00OO0OOO00O0O ,data =OO00OOO0OOO00OOOO )#line:638
        except Exception as OO00OOOOOOO0000O0 :#line:639
            print (OO00OOOOOOO0000O0 )#line:640
    def winning_rewards (O0O0O00O0000OOOO0 ):#line:643
        try :#line:644
            O000OOO000O0OO0OO =f'__{timi_new()}'#line:645
            OOO0OOO0O0OOO00OO ={'source':'scsc','authorization':O0O0O00O0000OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O000OOO000O0OO0OO ),'signstring':O000OOO000O0OO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:656
            O000O00OO0O00OOOO =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OOO0OOO0O0OOO00OO ).json ()#line:657
            if 'status'in O000O00OO0O00OOOO :#line:659
                if O000O00OO0O00OOOO ['status']==200 :#line:660
                    if O000O00OO0O00OOOO ['data']['amount']:#line:661
                        O000O00O0OO00O000 =O000O00OO0O00OOOO ['data']['amount']['gold']#line:662
                        return O000O00O0OO00O000 #line:663
                    else :#line:664
                        return 0 #line:665
        except Exception as O0OO0O0OO0O0O0000 :#line:666
            print (O0OO0O0OO0O0O0000 )#line:667
    def certification (OO000O000OOOO0O0O ):#line:670
        try :#line:671
            OO000O0O00O00O0OO =f'__{timi_new()}'#line:672
            O00OO0O0OOOO0OO0O ={'source':'scsc','authorization':OO000O000OOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO000O0O00O00O0OO ),'signstring':OO000O0O00O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:683
            OOOO0000OOOO000O0 =requests .request ('get',f'{host}/certification/get-auth-status',headers =O00OO0O0OOOO0OO0O ).json ()#line:684
            if 'status'in OOOO0000OOOO000O0 :#line:686
                if OOOO0000OOOO000O0 ['status']==200 :#line:687
                    if OOOO0000OOOO000O0 ['data']['result']:#line:688
                        O0O000O0O0OOOO000 =OOOO0000OOOO000O0 ['data']['nick_name']#line:689
                        return O0O000O0O0OOOO000 #line:690
                    else :#line:691
                        return '未实名'#line:692
        except Exception as OO0OO00OO00O0O00O :#line:693
            print (OO0OO00OO00O0O00O )#line:694
    def crops_illustrated (OOOO00O0O00O0O0O0 ):#line:697
        try :#line:698
            O00O000OOO00OOO0O =f'__{timi_new()}'#line:699
            OO0O00OO0O00OO000 ={'source':'scsc','authorization':OOOO00O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOO00OOO0O ),'signstring':O00O000OOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:710
            O0O0OOOOO000000OO =requests .request ('get',f'{host}/game/crops/illustrated',headers =OO0O00OO0O00OO000 ).json ()#line:711
            if 'status'in O0O0OOOOO000000OO :#line:713
                if O0O0OOOOO000000OO ['status']==200 :#line:714
                    OOO0OO0O00OO00O00 =O0O0OOOOO000000OO ['data'][0 ]['crops']#line:715
                    for OO0OO0OOOO0O0OOOO in OOO0OO0O00OO00O00 :#line:716
                        if OO0OO0OOOO0O0OOOO ['ill_clover_award']:#line:717
                            if float (OO0OO0OOOO0O0OOOO ['ill_clover_award'])>1 :#line:718
                                if OO0OO0OOOO0O0OOOO ['is_finish']:#line:719
                                    if not OO0OO0OOOO0O0OOOO ['is_getit']:#line:720
                                        if OOOO00O0O00O0O0O0 .certification ()!='未实名':#line:721
                                            O00O000OOO00OOO0O =f'_award_level={OO0OO0OOOO0O0OOOO["level"]}_{timi_new()}'#line:722
                                            OO0O00OO0O00OO000 ={'source':'scsc','authorization':OOOO00O0O00O0O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOO00OOO0O ),'signstring':O00O000OOO00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:733
                                            OOOO00OOOO00O00O0 ={"award_level":OO0OO0OOOO0O0OOOO ['level']}#line:734
                                            O0OOO00000OOOO0O0 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OO0O00OO0O00OO000 ,json =OOOO00OOOO00O00O0 ).json ()#line:736
                                            if 'status'in O0OOO00000OOOO0O0 :#line:737
                                                if O0OOO00000OOOO0O0 ['status']==200 :#line:738
                                                    OO0000O000O0OO0OO =O0OOO00000OOOO0O0 ['data']['ill_clover_award']#line:739
                                                    print (f'【图鉴奖励】:领取{OO0OO0OOOO0O0OOOO["crop_name"]}成就丨奖励{OO0000O000O0OO0OO}☘️')#line:741
                                                if O0OOO00000OOOO0O0 ['status']==500 :#line:742
                                                    print (f'【图鉴奖励】:{O0OOO00000OOOO0O0["message"]}')#line:743
        except Exception as O00OOO0OO00OO0OOO :#line:744
            print (O00OOO0OO00OO0OOO )#line:745
    def watched_ad (O0OO0000O0OO0OO00 ):#line:748
        try :#line:749
            OOO0O0OO000O0000O =f'__{timi_new()}'#line:750
            O0OO0O0O0O00O00OO ={'source':'scsc','authorization':O0OO0000O0OO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O0OO000O0000O ),'signstring':OOO0O0OO000O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:761
            O0O0O0OO0000OO0OO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O0O00O00OO ).json ()#line:762
            if 'status'in O0O0O0OO0000OO0OO :#line:764
                if O0O0O0OO0000OO0OO ['status']==200 :#line:765
                    if 'offlineInfo'in O0O0O0OO0000OO0OO ['data']:#line:766
                        time .sleep (random .randint (1 ,3 ))#line:767
                        O0OO00OOOOO00OOOO =O0O0O0OO0000OO0OO ['data']['offlineInfo']['off_minute']#line:768
                        O00000O0O000O00O0 =float (O0O0O0OO0000OO0OO ['data']['silver'])/1000000000000 #line:769
                        time .sleep (1 )#line:770
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0OO0O0O0O00O00OO ).json ()#line:771
                        time .sleep (2 )#line:772
                        OOOO00OO00O00OOO0 =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O0O00O00OO ).json ()#line:773
                        if 'status'in OOOO00OO00O00OOO0 :#line:775
                            if OOOO00OO00O00OOO0 ['status']==200 :#line:776
                                OOOO0O0OOOOOO0O0O =float (OOOO00OO00O00OOO0 ['data']['silver'])/1000000000000 #line:777
                                O0OO0O00O0O0OO0OO =str (OOOO0O0OOOOOO0O0O -O00000O0O000O00O0 )[:6 ]#line:778
                                print (f'【离线奖励】:翻倍离线{O0OO00OOOOO00OOOO}分钟奖励🌱数量:{O0OO0O00O0O0OO0OO}t粒')#line:779
        except Exception as O000000000OO0O0OO :#line:780
            print (O000000000OO0O0OO )#line:781
    def user_ad (OOO0000OOO00000O0 ):#line:784
        try :#line:785
            OOO00O0OOOO00O0O0 =f'__{timi_new()}'#line:786
            O0OOOO00OO0OOO00O ={'source':'scsc','authorization':OOO0000OOO00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO00O0O0 ),'signstring':OOO00O0OOOO00O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:797
            O00O000OOO00OOO00 =requests .request ('get',f'{host}/user/ad',headers =O0OOOO00OO0OOO00O ).json ()#line:798
            if 'status'in O00O000OOO00OOO00 :#line:800
                if O00O000OOO00OOO00 ['status']==200 :#line:801
                    O00O0OOOO0000OOOO =O00O000OOO00OOO00 ['data']['max_time']#line:802
                    OO0O00O0OO00O0000 =O00O000OOO00OOO00 ['data']['watch_time']#line:803
                    OOO0O00OOO0O0O00O =O00O000OOO00OOO00 ['data']['added_time']#line:804
                    print (f'【获取种子】:获取🌱剩余{OOO0O00OOO0O0O00O + O00O0OOOO0000OOOO - OO0O00O0OO00O0000}次丨好友提供:{OOO0O00OOO0O0O00O}次')#line:805
                    if OOO0O00OOO0O0O00O +O00O0OOOO0000OOOO -OO0O00O0OO00O0000 >0 :#line:806
                        time .sleep (random .randint (16 ,19 ))#line:807
                        O0O0OO0OOO0OO0O0O =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =O0OOOO00OO0OOO00O ).json ()#line:808
                        if 'status'in O0O0OO0OOO0OO0O0O :#line:810
                            if O0O0OO0OOO0OO0O0O ['status']==200 :#line:811
                                O000OOOO0O000OOO0 =float (O0O0OO0OOO0OO0O0O ['data']['silver'])/1000000000000 #line:812
                                print (f'【获取种子】:获得🌱:{int(O000OOOO0O000OOO0)}t粒')#line:813
                                return True #line:814
                            if O0O0OO0OOO0OO0O0O ['status']==500 :#line:815
                                OO0O00OOO0OOO00O0 =O0O0OO0OOO0OO0O0O ['message']#line:816
                                print (f'【获取种子】:{OO0O00OOO0OOO00O0}')#line:817
                                return False #line:818
        except Exception as O00OO0OOO000O0O00 :#line:819
            print (O00OO0OOO000O0O00 )#line:820
    def synthetic (O000OOO0OO00OO0O0 ):#line:823
        global id ,g #line:824
        try :#line:825
            O0OO00OO0O0OOOOO0 =O000OOO0OO00OO0O0 .level_new ()#line:826
            O0000O0O00OOOOOOO =random .randint (9 ,11 )#line:827
            OOOO00000OO000000 =f'_site=8&targetSite={O0000O0O00OOOOOOO}_{timi_new()}'#line:828
            O00OO0OO0O0O00OO0 ={'source':'scsc','authorization':O000OOO0OO00OO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO00000OO000000 ),'signstring':OOOO00000OO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:839
            O000O00O000O0O0O0 ={"site":int (8 ),"targetSite":int (O0000O0O00OOOOOOO )}#line:840
            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0OO0O0O00OO0 ,json =O000O00O000O0O0O0 )#line:841
            while True :#line:842
                O0O00OO00O0OOOO00 =f'__{timi_new()}'#line:843
                OO0O0O00O00O0O00O ={'source':'scsc','authorization':O000OOO0OO00OO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OO00O0OOOO00 ),'signstring':O0O00OO00O0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:854
                OOOOO0O0000OO00OO =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O00O0O00O ).json ()#line:855
                if 'status'in OOOOO0O0000OO00OO :#line:857
                    if OOOOO0O0000OO00OO ['status']==200 :#line:858
                        O0OO00OOO000O0O00 =OOOOO0O0000OO00OO ['data']['cropList']#line:859
                        O0OO0O00OO00O0OO0 =OOOOO0O0000OO00OO ['data']['gameCoreDataDBid']#line:860
                        O00O0000O000OO00O =float (OOOOO0O0000OO00OO ['data']['silver'])/1000000000000 #line:861
                        O0O0OO0000O0O0OO0 =0 #line:866
                        for OO0OOO000O0O00OOO in O0OO00OOO000O0O00 :#line:867
                            if not OO0OOO000O0O00OOO :#line:868
                                O00OO00OO0O000OO0 =f'_crop_id={O0OO0O00OO00O0OO0}&site={O0O0OO0000O0O0OO0}_{O000OOO0OO00OO0O0.time}'#line:869
                                O00OOO00OOOOOO000 ={'source':'scsc','authorization':O000OOO0OO00OO0O0 .token ,'timestamp':O000OOO0OO00OO0O0 .time ,'sign':sign (O00OO00OO0O000OO0 ),'signstring':O00OO00OO0O000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:879
                                OOO000OO00O00O000 ={"site":O0O0OO0000O0O0OO0 ,"crop_id":O0OO0O00OO00O0OO0 }#line:880
                                O0O0OOOO0OOO0O0O0 =requests .request ('post',f'{host}/game/crops/buy',headers =O00OOO00OOOOOO000 ,data =OOO000OO00O00O000 ).json ()#line:881
                                time .sleep (random .randint (1 ,3 )/10 )#line:883
                                if 'status'in O0O0OOOO0OOO0O0O0 :#line:884
                                    if O0O0OOOO0OOO0O0O0 ['status']==200 :#line:885
                                        if O0O0OOOO0OOO0O0O0 ['message']=='种子数量不足':#line:886
                                            O0OO00OO0O0OOOOO0 =O000OOO0OO00OO0O0 .level_new ()#line:887
                                            print (f'【种植合成】:{O0O0OOOO0OOO0O0O0["message"]}')#line:888
                                            if not O000OOO0OO00OO0O0 .user_ad ():#line:889
                                                return False #line:890
                                    if O0O0OOOO0OOO0O0O0 ['status']==500 :#line:891
                                        print (f'【种植合成】:{O0O0OOOO0OOO0O0O0["message"]}')#line:892
                                        return False #line:893
                            O0O0OO0000O0O0OO0 +=1 #line:894
                        O0O000OO000O00O0O =requests .request ('get',f'{host}/game/getAllData',headers =OO0O0O00O00O0O00O ).json ()#line:895
                        OO00O0000O00OOOO0 =O0O000OO000O00O0O ['data']['cropList']#line:896
                        O0OO0OO000OO0OOO0 =False #line:897
                        for OO0OOO000O0O00OOO in range (12 ):#line:898
                            id =OO00O0000O00OOOO0 [OO0OOO000O0O00OOO ]['level']#line:899
                            if float (O0OO00OO0O0OOOOO0 )-float (id )>9 :#line:900
                                O0O0O00O00000O000 =f'_site={OO0OOO000O0O00OOO}_{timi_new()}'#line:901
                                OO0O0O0O00OOOOOO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOO0OO00OO0O0 .token ,'timestamp':timi_new (),'sign':sign (O0O0O00O00000O000 ),'signstring':O0O0O00O00000O000 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:912
                                O00OOO0O000000OO0 ={"site":OO0OOO000O0O00OOO }#line:913
                                O0OO0O0000O00OOO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OO0O0O0O00OOOOOO0 ,data =O00OOO0O000000OO0 ).json ()#line:915
                                if 'status'in O0OO0O0000O00OOO0 :#line:916
                                    if O0OO0O0000O00OOO0 ['status']==200 :#line:917
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:918
                            if id !=0 :#line:919
                                for O0O0O00O0O0OO0OO0 in range (11 ):#line:920
                                    OO0O0OO00000OO0OO =O0O0O00O0O0OO0OO0 +1 #line:921
                                    g =OO00O0000O00OOOO0 [OO0O0OO00000OO0OO ]['level']#line:922
                                    if id ==g :#line:923
                                        O0OO0O0OO0O000O00 =O0O0O00O0O0OO0OO0 +2 #line:924
                                        if O0OO0O0OO0O000O00 !=OO0OOO000O0O00OOO +1 :#line:925
                                            OO000OOOOO0O00000 =OO0OOO000O0O00OOO +1 #line:926
                                            time .sleep (random .randint (1 ,3 )/10 )#line:928
                                            OOOO00000OO000000 =f'_site={OO000OOOOO0O00000 - 1}&targetSite={O0OO0O0OO0O000O00 - 1}_{timi_new()}'#line:929
                                            O00OO0OO0O0O00OO0 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O000OOO0OO00OO0O0 .token ,'timestamp':timi_new (),'sign':sign (OOOO00000OO000000 ),'signstring':OOOO00000OO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:946
                                            OOO0OOO0O0OO000O0 ={"site":int (OO000OOOOO0O00000 -1 ),"targetSite":int (O0OO0O0OO0O000O00 -1 )}#line:947
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00OO0OO0O0O00OO0 ,json =OOO0OOO0O0OO000O0 )#line:948
                                            O0OO0OO000OO0OOO0 =True #line:950
                                    if O0OO0OO000OO0OOO0 :#line:951
                                        break #line:952
                                if O0OO0OO000OO0OOO0 :#line:953
                                    break #line:954
        except :#line:955
            O000OOO0OO00OO0O0 .synthetic ()#line:956
    def level_new (OO0000O00OOO0OO00 ):#line:959
        try :#line:960
            O0O00OOO00OO00OOO =f'__{timi_new()}'#line:961
            OO00000OO0OOOOO0O ={'source':'scsc','authorization':OO0000O00OOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00OOO00OO00OOO ),'signstring':O0O00OOO00OO00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:972
            O00OO0O00O00OOO0O =requests .request ('get',f'{host}/user',headers =OO00000OO0OOOOO0O ).json ()#line:973
            if 'status'in O00OO0O00O00OOO0O :#line:974
                if O00OO0O00O00OOO0O ['status']==200 :#line:975
                    return float (O00OO0O00O00OOO0O ['data']['level'])#line:976
        except Exception as O00O00OOOO000OOOO :#line:977
            print (O00O00OOOO000OOOO )#line:978
    def propsraffle (OO00OO00OOO00OOO0 ):#line:981
        try :#line:982
            while True :#line:983
                OOOO000O0OOO0O00O =f'__{timi_new()}'#line:984
                O0000OOOOO0000OO0 ={'source':'scsc','authorization':OO00OO00OOO00OOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O0OOO0O00O ),'signstring':OOOO000O0OOO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:995
                OO0OO00O0O0O0OO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0000OOOOO0000OO0 ).json ()#line:996
                if 'status'in OO0OO00O0O0O0OO00 :#line:998
                    if OO0OO00O0O0O0OO00 ['status']==200 :#line:999
                        O00O0O0O0O00O00O0 =OO0OO00O0O0O0OO00 ['data']['rows']#line:1000
                        O000000OOOOOOO0O0 =OO0OO00O0O0O0OO00 ['data']['vstate']#line:1001
                        if O00O0O0O0O00O00O0 ==5 or O00O0O0O0O00O00O0 ==6 or O00O0O0O0O00O00O0 ==7 :#line:1002
                            O0OO0OOOO0O0O0O0O =OO0OO00O0O0O0OO00 ['data']['silver']#line:1003
                            print (f'【转盘抽奖】:获得种子:{O0OO0OOOO0O0O0O0O}')#line:1004
                        if O00O0O0O0O00O00O0 ==1 or O00O0O0O0O00O00O0 ==2 or O00O0O0O0O00O00O0 ==3 :#line:1005
                            OO000OOOO000OOOOO =OO0OO00O0O0O0OO00 ['data']['clover']#line:1006
                            print (f'【转盘抽奖】:获得三叶草:{OO000OOOO000OOOOO}')#line:1007
                        if O00O0O0O0O00O00O0 ==4 or O00O0O0O0O00O00O0 ==8 :#line:1008
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:1009
                        if O00O0O0O0O00O00O0 =='抽奖次数已用完':#line:1013
                            break #line:1047
                time .sleep (random .randint (8 ,15 )/10 )#line:1048
        except Exception as OO0O0O0O000O00O00 :#line:1049
            print (OO0O0O0O000O00O00 )#line:1050
    def friends_invitation (OOOO0OO000000O0OO ):#line:1053
        try :#line:1054
            O00OO00O000O0OO0O =f'__{timi_new()}'#line:1055
            OOOO00OOO0O00O0O0 ={'source':'scsc','authorization':OOOO0OO000000O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00OO00O000O0OO0O ),'signstring':O00OO00O000O0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1066
            OOO000O00O000O00O =requests .request ('get',f'{host}/friends',headers =OOOO00OOO0O00O0O0 ).json ()#line:1067
            if 'status'in OOO000O00O000O00O :#line:1068
                if OOO000O00O000O00O ['status']==200 :#line:1069
                    O0O0OO00OOO00OOOO =OOO000O00O000O00O ['data']['myInviteter']#line:1070
                    if O0O0OO00OOO00OOOO :#line:1071
                        O00OOOOO0O00OOOO0 =O0O0OO00OOO00OOOO ['user']['nickname']#line:1072
                        OO0O0O0O00OO000O0 =OOOO0OO000000O0OO .certification ()#line:1073
                        if OO0O0O0O00OO000O0 =='未实名':#line:1074
                            weishim .append (OOOO0OO000000O0OO .token )#line:1075
                        print (f'【查邀请人】:我的邀请人:{O00OOOOO0O00OOOO0}丨实名:{OO0O0O0O00OO000O0}')#line:1076
                    else :#line:1077
                        if OOOO0OO000000O0OO .innerId !='0':#line:1078
                            OOOO0OO000000O0OO .invitation ()#line:1079
        except Exception as O0O00O0O0O0O000O0 :#line:1080
            print (O0O00O0O0O0O000O0 )#line:1081
    def add_clover (OOOO0OOO00OOO00O0 ):#line:1084
        global golden_seed #line:1085
        try :#line:1086
            OOOO0OOO0O00OOOOO =f'__{timi_new()}'#line:1087
            O00OOO00O000O0O00 ={'source':'scsc','authorization':OOOO0OOO00OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0O00OOOOO ),'signstring':OOOO0OOO0O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1098
            O00O0O0O00OOO000O =requests .request ('get',f'{host}/assets/clovers',headers =O00OOO00O000O0O00 ).json ()#line:1099
            if 'status'in O00O0O0O00OOO000O :#line:1101
                if O00O0O0O00OOO000O ['status']==200 :#line:1102
                    O0OO0O0000O0000OO =O00O0O0O00OOO000O ['data']['clover']#line:1103
                    OOOO00O0O00O000OO =O00O0O0O00OOO000O ['data']['used_clover']#line:1104
                    OOOOO0OOO0O0000OO =float (O0OO0O0000O0000OO )-float (OOOO00O0O00O000OO )#line:1105
                    print (f'【参与抽奖】:参与抽奖的☘️:{OOOO00O0O00O000OO}')#line:1106
                    if OOOO0OOO00OOO00O0 .certification ()!='未实名':#line:1107
                        if OOOOO0OOO0O0000OO >1 :#line:1108
                            OOOO0OOO0O00OOOOO =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOOOO0OOO0O0000OO)}_{timi_new()}'#line:1109
                            O0OO00O0000O00OOO ={'source':'scsc','authorization':OOOO0OOO00OOO00O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0OOO0O00OOOOO ),'signstring':OOOO0OOO0O00OOOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1120
                            O00OO0O0OO0O0000O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOOOO0OOO0O0000OO )}#line:1121
                            OOOOO0000OOOOO0O0 =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO00O0000O00OOO ,data =O00OO0O0OO0O0000O ).json ()#line:1122
                            if 'status'in OOOOO0000OOOOO0O0 :#line:1124
                                if OOOOO0000OOOOO0O0 ['status']==200 :#line:1125
                                    print (f'【参与抽奖】:添加☘️:{OOOOO0000OOOOO0O0["data"]["isSuccess"]}丨数量:{OOOOO0OOO0O0000OO}')#line:1126
                                if OOOOO0000OOOOO0O0 ['status']==500 :#line:1127
                                    print (f'【参与抽奖】:添加☘️:{OOOOO0000OOOOO0O0["message"]}')#line:1128
            O000O0OO0O0OO0000 =requests .request ('get',f'{host}/lottery',headers =O00OOO00O000O0O00 ).json ()#line:1129
            O0O0000O0OO0OOO00 =OOOO0OOO00OOO00O0 .winning_rewards ()#line:1131
            if 'status'in O000O0OO0O0OO0000 :#line:1132
                if O000O0OO0O0OO0000 ['status']==200 :#line:1133
                    O0O0O00OOO0O000O0 =O000O0OO0O0OO0000 ['data'][0 ]['day_get_gold_quantity']#line:1134
                    golden_seed +=float (O0O0O00OOO0O000O0 )#line:1135
                    OO0O00O00000OO0OO =O000O0OO0O0OO0000 ['data'][1 ]['value']#line:1136
                    OOO0OOO0OOOOO0OOO =O000O0OO0O0OO0000 ['data'][0 ]['join_number']#line:1137
                    O0O0O00O00OO0OOO0 =int (float (O000O0OO0O0OO0000 ['data'][0 ]['totalValue']))#line:1138
                    OO0OO0O0OO0O00000 =float (OO0O00O00000OO0OO /O0O0O00O00OO0OOO0 )*10000 #line:1139
                    OOO0OOO0O0O00OOO0 =O0O0O00O00OO0OOO0 /OOO0OOO0OOOOO0OOO #line:1140
                    print (f'【参与抽奖】:预计每天中{str(O0O0O00OOO0O000O0)[:6]}颗金种子丨好友收益:{str(O0O0000O0OO0OOO00)[:6]}')#line:1141
                    print (f'【抽奖统计】:每1万☘️中{str(OO0OO0O0OO0O00000)[:6]}颗金种子丨☘️人均:{str(OOO0OOO0O0O00OOO0)[:7]}️')#line:1142
        except Exception as O0O00OO0OO000O000 :#line:1143
            print (O0O00OO0OO000O000 )#line:1144
    def energy (O0000O00OOO0000O0 ):#line:1147
        try :#line:1148
            while True :#line:1149
                OOOOO0O00OO00O000 =f'__{timi_new()}'#line:1150
                O0000O0OOO0O00000 ={'source':'scsc','authorization':O0000O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOOO0O00OO00O000 ),'signstring':OOOOO0O00OO00O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1161
                O00000O0OOOOO0OOO =requests .request ('get',f'{host}/energy/general',headers =O0000O0OOO0O00000 ).json ()#line:1162
                if 'status'in O00000O0OOOOO0OOO :#line:1164
                    if O00000O0OOOOO0OOO ['status']==200 :#line:1165
                        O0OO0O0O0O00O00O0 =O00000O0OOOOO0OOO ['data']['ordinary_water']#line:1166
                        O0OOO000OOOO0OOOO =O00000O0OOOOO0OOO ['data']['ordinary_fertilizer']#line:1167
                        OO00O0OOOO0O0O00O =O00000O0OOOOO0OOO ['data']['videoStatus']#line:1168
                        OO0O0OOOO00O00000 =O00000O0OOOOO0OOO ['data']['waterVideoKey']#line:1169
                        print (f'【我的营养】:肥料:{str(O0OOO000OOOO0OOOO).split(".")[0]}丨水滴:{str(O0OO0O0O0O00O00O0).split(".")[0]}')#line:1171
                        if float (O0OOO000OOOO0OOOO )<96 :#line:1172
                            if OO00O0OOOO0O0O00O :#line:1173
                                time .sleep (random .randint (160 ,180 )/10 )#line:1174
                                O000OOOO0OO00000O =99 -float (O0OOO000OOOO0OOOO )#line:1175
                                O0OOOO0000O00OO0O ={"fertilizer":str (O000OOOO0OO00000O ).split ('.')[0 ]}#line:1176
                                OOOO00O00000O0O0O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0000O0OOO0O00000 ).json ()#line:1178
                                if 'status'in OOOO00O00000O0O0O :#line:1180
                                    if OOOO00O00000O0O0O ['status']==200 :#line:1181
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO00O00000O0O0O["message"]}')#line:1182
                                    if OOOO00O00000O0O0O ['status']==500 :#line:1183
                                        print (f'【购买肥料】:看广告获取肥料:{OOOO00O00000O0O0O["message"]}')#line:1184
                                        break #line:1185
                                if float (O0OOO000OOOO0OOOO )<78 :#line:1187
                                    O000OOOO0OO00000O =80 -float (O0OOO000OOOO0OOOO )#line:1188
                                    O00O00OO00OO0O00O =f'_fertilizer={int(O000OOOO0OO00000O)}_{timi_new()}'#line:1189
                                    O0OOO0OO000000O0O ={'source':'scsc','authorization':O0000O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00OO00OO0O00O ),'signstring':O00O00OO00OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1200
                                    OOO0O0OO000OO0O0O ={"fertilizer":int (O000OOOO0OO00000O )}#line:1201
                                    OO0O0O00O0OOOOOO0 =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOO0OO000000O0O ,data =OOO0O0OO000OO0O0O ).json ()#line:1203
                                    if 'status'in OO0O0O00O0OOOOOO0 :#line:1205
                                        if OO0O0O00O0OOOOOO0 ['status']==200 :#line:1206
                                            print (f'【购买肥料】:购买肥料:{OO0O0O00O0OOOOOO0["message"]}丨数量:{int(O000OOOO0OO00000O)}')#line:1207
                                        if OO0O0O00O0OOOOOO0 ['status']==500 :#line:1208
                                            print (f'【购买肥料】:购买肥料:{OO0O0O00O0OOOOOO0["message"]}丨数量:{int(O000OOOO0OO00000O)}')#line:1209
                                            O0O0000000O000000 =OO0O0O00O0OOOOOO0 ["message"].split ('-')[1 ]#line:1210
                                            OO000OOOO0O00OO0O =f'__{timi_new()}'#line:1211
                                            OO00O00O0OOOO00O0 ={'source':'scsc','authorization':O0000O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO0O00OO0O ),'signstring':OO000OOOO0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1222
                                            OOO00OOOOO00O0OOO =requests .request ('get',f'{host}/user',headers =OO00O00O0OOOO00O0 ).json ()#line:1223
                                            if 'status'in OOO00OOOOO00O0OOO :#line:1224
                                                if OOO00OOOOO00O0OOO ['status']==200 :#line:1225
                                                    OO0O0O00OO0OOOOO0 =OOO00OOOOO00O0OOO ['data']['inner_id']#line:1226
                                                    if give_gold (OO0O0O00OO0OOOOO0 ,float (O0O0000000O000000 )+1 ):#line:1227
                                                        O0000O00OOO0000O0 .energy ()#line:1228
                        if float (O0OO0O0O0O00O00O0 )<880 :#line:1229
                            if OO0O0OOOO00O00000 :#line:1230
                                time .sleep (random .randint (160 ,180 )/10 )#line:1231
                                O000O0OOOO0O0OO0O =999 -float (O0OO0O0O0O00O00O0 )#line:1232
                                OO00OOOOO00OO0OO0 ={"water":str (O000O0OOOO0O0OO0O ).split ('.')[0 ]}#line:1233
                                O000O0000000000O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0000O0OOO0O00000 ).json ()#line:1235
                                if 'status'in O000O0000000000O0 :#line:1237
                                    if O000O0000000000O0 ['status']==200 :#line:1238
                                        print (f'【购买水滴】:看广告获取水滴:{O000O0000000000O0["message"]}')#line:1239
                                    if O000O0000000000O0 ['status']==500 :#line:1240
                                        print (f'【购买水滴】:看广告获取水滴:{O000O0000000000O0["message"]}')#line:1241
                                        break #line:1242
                                if float (O0OO0O0O0O00O00O0 )<780 :#line:1243
                                    O000O0OOOO0O0OO0O =800 -float (O0OO0O0O0O00O00O0 )#line:1244
                                    O0O0000OO0OO00OO0 =f'_water={int(O000O0OOOO0O0OO0O)}_{timi_new()}'#line:1245
                                    O0OO0O0O0OOOOO00O ={'source':'scsc','authorization':O0000O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OO00OO0 ),'signstring':O0O0000OO0OO00OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1256
                                    OO00OOOO000O000O0 ={"water":int (O000O0OOOO0O0OO0O )}#line:1257
                                    O0O0OO0O0O00OOO00 =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0OO0O0O0OOOOO00O ,data =OO00OOOO000O000O0 ).json ()#line:1259
                                    if 'status'in O0O0OO0O0O00OOO00 :#line:1261
                                        if O0O0OO0O0O00OOO00 ['status']==200 :#line:1262
                                            print (f'【购买水滴】:购买水滴:{O0O0OO0O0O00OOO00["message"]}丨数量:{int(O000O0OOOO0O0OO0O)}')#line:1263
                                        if O0O0OO0O0O00OOO00 ['status']==500 :#line:1264
                                            print (f'【购买水滴】:购买水滴:{O0O0OO0O0O00OOO00["message"]}丨数量:{int(O000O0OOOO0O0OO0O)}')#line:1265
                                            O0O0000000O000000 =O0O0OO0O0O00OOO00 ["message"].split ('-')[1 ]#line:1266
                                            OO000OOOO0O00OO0O =f'__{timi_new()}'#line:1267
                                            OO00O00O0OOOO00O0 ={'source':'scsc','authorization':O0000O00OOO0000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OOOO0O00OO0O ),'signstring':OO000OOOO0O00OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1278
                                            OOO00OOOOO00O0OOO =requests .request ('get',f'{host}/user',headers =OO00O00O0OOOO00O0 ).json ()#line:1279
                                            if 'status'in OOO00OOOOO00O0OOO :#line:1280
                                                if OOO00OOOOO00O0OOO ['status']==200 :#line:1281
                                                    OO0O0O00OO0OOOOO0 =OOO00OOOOO00O0OOO ['data']['inner_id']#line:1282
                                                    if give_gold (OO0O0O00OO0OOOOO0 ,float (O0O0000000O000000 )+1 ):#line:1283
                                                        O0000O00OOO0000O0 .energy ()#line:1284
                        break #line:1285
        except Exception as OO0OO000O0O0O0000 :#line:1286
            print (OO0OO000O0O0O0000 )#line:1287
def bundled_def ():#line:1290
    OO00OO0OOO000000O =['5570536','7750212','7911652','7911680','7805624']#line:1291
    return OO00OO0OOO000000O [random .randint (0 ,len (OO00OO0OOO000000O )-1 )]#line:1292
def version_of_the_validation ():#line:1296
    return str ((101 -56 )/10 )#line:1297
def ubbbf ():#line:1299
    print ('卡密验证通过   ✅')#line:1300
def sc2 ():#line:1303
    return "19319#$%^&*((*"#line:1304
def OO00OO0OO0OO00OO00o0 ():#line:1307
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1309
def get_ip ():#line:1312
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1314
def gitee_validation ():#line:1317
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1318
def gitee_edition ():#line:1321
    try :#line:1322
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1323
    except :#line:1324
        sys .exit (0 )#line:1325
def O000OO000O0O00OOO00 ():#line:1329
    try :#line:1330
        O00O0O0O00O0O0000 =gitee_edition ()#line:1331
        if version_of_the_validation ()<O00O0O0O00O0O0000 ['CityEarth']['edition']:#line:1332
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O0O00O0O0000["CityEarth"]["edition"]}   ❌')#line:1333
            print (f'更新内容=>>{O00O0O0O00O0O0000["CityEarth"]["content"]}')#line:1334
        else :#line:1335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O0O0O00O0O0000["CityEarth"]["edition"]}   ✅')#line:1336
            print (f'更新内容=>> {O00O0O0O00O0O0000["CityEarth"]["content"]}')#line:1337
    except Exception as OO0OO0O00O00OOOO0 :#line:1338
        print (OO0OO0O00O00OOOO0 )#line:1339
def sc3 ():#line:1342
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1343
if __name__ =='__main__':#line:1346
    start ()#line:1347
