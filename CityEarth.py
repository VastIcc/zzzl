# coding: utf-8
try:
    import threading, re, os, sys, time, hashlib, json, requests, random, socket, uuid
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
@ 版本  3.6
"""
##################################配置区##################################
time_xx = random.randint(15, 18)  # 秒 执行下一个号的时间  8到12秒中随机延迟执行
##################################配置区##################################

##################################下面不要动##################################
version ='3.1.419541311'#line:1
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
        OO0OO000O00OO00OO =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(OO0OO000O00OO00OO)}个账号==========")#line:13
        for O0OOO0O0O00O000O0 in OO0OO000O00OO00OO :#line:14
            O0000OO0OOO00O0OO =[]#line:15
            print (f"------------正在执行第{OO0OO000O00OO00OO.index(O0OOO0O0O00O000O0) + 1}个账号------------")#line:16
            O0O000O0O0O00OOO0 =CityEarth (O0OOO0O0O00O000O0 ,O0000OO0OOO00O0OO ,OO0OO000O00OO00OO .index (O0OOO0O0O00O000O0 ))#line:17
            def O0OO0O0OO0O00OO00 ():#line:18
                if O0O000O0O0O00OOO0 .base_info ():#line:20
                    O0O000O0O0O00OOO0 .sealing ()#line:22
                    O0O000O0O0O00OOO0 .invitenum ()#line:24
                    O0O000O0O0O00OOO0 .query_to_sell ()#line:26
                    O0O000O0O0O00OOO0 .game_map ()#line:28
                    O0O000O0O0O00OOO0 .friends_invitation ()#line:30
                    O0O000O0O0O00OOO0 .energy ()#line:32
                    O0O000O0O0O00OOO0 .add_clover ()#line:34
                    O0O000O0O0O00OOO0 .propsraffle ()#line:36
                    O0O000O0O0O00OOO0 .synthetic ()#line:38
                    O0O000O0O0O00OOO0 .crops_illustrated ()#line:40
                    O0O000O0O0O00OOO0 .withdraw ()#line:42
                    O0O000O0O0O00OOO0 .give_gold ()#line:44
            O0000O000O00000OO =threading .Thread (target =O0OO0O0OO0O00OO00 )#line:46
            O0000O000O00000OO .start ()#line:47
            time .sleep (time_xx )#line:48
        print (f"------------正在处理推送通知------------")#line:49
        time .sleep (0.5 )#line:50
        OOOO0OO00OOOO000O =format_msg ()#line:51
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OOOO0OO00OOOO000O +' ')#line:52
    except Exception as OOOOOO0O0OO000OOO :#line:56
        print (OOOOOO0O0OO000OOO )#line:57
def give_gold (O00O000O0O00OOOOO ,O00O0OOOO00OOOOO0 ):#line:60
        try :#line:61
            O0000OO000O0O000O =f'_doneeNo={O00O000O0O00OOOOO}&quantity={int(O00O0OOOO00OOOOO0)}_{timi_new()}'#line:62
            OOO000O0O0O000OO0 ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (O0000OO000O0O000O ),'signstring':O0000OO000O0O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:73
            OOOO0OO0O0O0OO000 ={"quantity":int (O00O0OOOO00OOOOO0 ),"doneeNo":O00O000O0O00OOOOO }#line:77
            O00OO00O00O0000O0 =requests .request ('post',f'{host}/finance/give-gold',headers =OOO000O0O0O000OO0 ,data =OOOO0OO0O0O0OO000 ).json ()#line:78
            if 'status'in O00OO00O00O0000O0 :#line:80
                if O00OO00O00O0000O0 ['status']==200 :#line:81
                    if O00OO00O00O0000O0 ['data']:#line:82
                        print (f'【赠送种子】:赠送{int(O00O0OOOO00OOOOO0)}种子给{O00O000O0O00OOOOO}成功')#line:83
                        return True #line:84
                if O00OO00O00O0000O0 ['status']==401 :#line:85
                    print (f'【赠送种子】:{O00OO00O00O0000O0["message"]}')#line:86
                    return False #line:87
                if O00OO00O00O0000O0 ['status']==500 :#line:88
                    print (f'【赠送种子】:{O00OO00O00O0000O0["message"]}')#line:89
                    return False #line:90
            return False #line:91
        except Exception as OOO0000O00000OO0O :#line:92
            print (OOO0000O00000OO0O )#line:93
def kvkv ():#line:94
    return '/vastzzzl/vastzzzl/raw/master'#line:95
def sign (OOO00O000OO0O0OOO ):#line:98
    OOOO0O0O0O0OO0OOO =hashlib .md5 (OOO00O000OO0O0OOO .encode ()).hexdigest ()#line:99
    O0OO000O0O0OOOO00 =sc1 ()#line:100
    OOO00O0OO0000OO0O =sc2 ()#line:101
    OOOOO000OO00O00O0 =sc3 ()#line:102
    OOOO00O00O0O0OOO0 =O0OO000O0O0OOOO00 +OOOO0O0O0O0OO0OOO +OOO00O0OO0000OO0O +OOOOO000OO00O00O0 #line:103
    OOOOOO0OOO00OOO00 =hashlib .md5 (OOOO00O00O0O0OOO0 .encode ()).hexdigest ()#line:104
    return OOOOOO0OOO00OOO00 #line:105
def format_msg ():#line:109
    OO0000000O0OOO0OO =""#line:110
    for O00OOO00O000O00OO in msg_list :#line:111
        OO0000000O0OOO0OO +=str (O00OOO00O000O00OO )+"\r\n"#line:112
    return OO0000000O0OOO0OO #line:113
def sc1 ():#line:115
    return "scsc%^&*"#line:116
def O000OO0O00OO00O00 ():#line:118
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:119
        pass #line:120
    else :#line:121
        exit (1 )#line:122
def timi_new ():#line:124
    return str (int (time .time ()*1000 ))#line:125
json_path ="CityEarth_data.json"#line:128
json_path1 ="CityEarth_data.json"#line:129
dict ={}#line:130
def get_json_data (OO000O0O0OO0OO0O0 ,O0O000000OOO000OO ,OOO0O00OO0O00OOOO ,O0OOO0O0OO00O0O00 ):#line:132
    with open (OO000O0O0OO0OO0O0 ,'rb')as OOOO0O0O000OO0OO0 :#line:134
        O000O0O0O0OO00O0O =json .load (OOOO0O0O000OO0OO0 )#line:135
        O000O0O0O0OO00O0O ['data'][O0O000000OOO000OO ][OOO0O00OO0O00OOOO ]=O0OOO0O0OO00O0O00 #line:136
        O00O00OO0000O0O0O =O000O0O0O0OO00O0O #line:137
    OOOO0O0O000OO0OO0 .close ()#line:138
    return O00O00OO0000O0O0O #line:139
def write_json_data (O0O0000OOO00O0000 ):#line:141
    with open (json_path1 ,'w')as OO0OOOOOO0OOO0O0O :#line:142
        json .dump (O0O0000OOO00O0000 ,OO0OOOOOO0OOO0O0O )#line:143
    OO0OOOOOO0OOO0O0O .close ()#line:144
    return True #line:145
class CityEarth :#line:147
    def __init__ (O000000O0O00O0OO0 ,OO0O000O0O0OO00OO ,OOO00O00O0OO0000O ,OO0000OO00OO00OO0 ):#line:149
        try :#line:150
            O000000O0O00O0OO0 .msg =OOO00O00O0OO0000O #line:151
            O000000O0O00O0OO0 .time =str (time .time ()*1000 ).split ('.')[0 ]#line:152
            O000000O0O00O0OO0 .token =OO0O000O0O0OO00OO ['authorization']#line:153
            O000000O0O00O0OO0 .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:154
            O000000O0O00O0OO0 .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:155
            O000000O0O00O0OO0 .elephant_user =OO0O000O0O0OO00OO ['elephant_user']#line:156
            O000000O0O00O0OO0 .elephant_pswd =OO0O000O0O0OO00OO ['elephant_pswd']#line:157
            O000000O0O00O0OO0 .elephant_Task_ID =OO0O000O0O0OO00OO ['elephant_Task_ID']#line:158
            O000000O0O00O0OO0 .len_new =OO0000OO00OO00OO0 #line:159
        except :#line:160
            print ('变量格式错误')#line:161
    def base_info (OOOOOO0OO0OOOOOOO ):#line:164
        try :#line:165
            OOOOOO0OO0OOOOOOO .watched_ad ()#line:167
            O0O0000OO0OOO0OO0 =f'__{timi_new()}'#line:168
            OOO0OOO000O0OOOO0 ={'source':'scsc','authorization':OOOOOO0OO0OOOOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0000OO0OOO0OO0 ),'signstring':O0O0000OO0OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:179
            OO0O00OOOOO000000 =requests .request ('get',f'{host}/user',headers =OOO0OOO000O0OOOO0 ).json ()#line:180
            if 'status'in OO0O00OOOOO000000 :#line:182
                if OO0O00OOOOO000000 ['status']==200 :#line:183
                    O0O0OO0OO0O0OO0O0 =OO0O00OOOOO000000 ['data']['nickname']#line:184
                    O00OOOOOO0OO00OO0 =OO0O00OOOOO000000 ['data']['inner_id']#line:185
                    OOO000O000O0OO0O0 =OO0O00OOOOO000000 ['data']['assets']['gold']#line:186
                    OOOO000OOOO000000 =OO0O00OOOOO000000 ['data']['level']#line:187
                    print (f'【账号信息】:昵称:{O0O0OO0OO0O0OO0O0[:5]}丨ID:{O00OOOOOO0OO00OO0}丨等级:{OOOO000OOOO000000}丨金种子:{str(OOO000O000O0OO0O0).split(".")[0]}')#line:188
                    if 'wx_'in O0O0OO0OO0O0OO0O0 :#line:189
                        OOOOOO0OO0OOOOOOO .change_nickname ()#line:190
                if OO0O00OOOOO000000 ['status']==401 :#line:191
                    print ('【账号信息】:账号失效正在尝试登录')#line:192
                    if OOOOOO0OO0OOOOOOO .elephant_user =='f':#line:193
                        return False #line:194
                    OO0O00O000OOO0OO0 =Invalid_login .addtask (elephant_user =OOOOOO0OO0OOOOOOO .elephant_user ,elephant_pswd =OOOOOO0OO0OOOOOOO .elephant_pswd ,elephant_Task_ID =OOOOOO0OO0OOOOOOO .elephant_Task_ID )#line:195
                    OOOO0000OOOOOOOO0 =get_json_data (json_path ,OOOOOO0OO0OOOOOOO .len_new ,'authorization',OO0O00O000OOO0OO0 )#line:196
                    if write_json_data (OOOO0000OOOOOOOO0 ):#line:197
                        print ('正在写入账号配置文件')#line:198
                    return False #line:199
                if OO0O00OOOOO000000 ['status']==500 :#line:200
                    return False #line:201
            return True #line:202
        except Exception as OO0O0000OOO00O000 :#line:203
            print (OO0O0000OOO00O000 )#line:204
    def sealing (O00OOOOOO0OO000OO ):#line:207
        try :#line:208
            O000O0OO0O00OO0O0 =f'__{timi_new()}'#line:209
            O00O00O0O000O0O0O ={'source':'scsc','authorization':O00OOOOOO0OO000OO .token ,'timestamp':str (timi_new ()),'sign':sign (O000O0OO0O00OO0O0 ),'signstring':O000O0OO0O00OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:220
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00O00O0O000O0O0O )#line:221
            requests .request ('get',f'{host}/packsack/list',headers =O00O00O0O000O0O0O )#line:222
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00O00O0O000O0O0O )#line:223
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00O00O0O000O0O0O )#line:224
            requests .request ('get',f'{host}/user',headers =O00O00O0O000O0O0O )#line:225
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00O00O0O000O0O0O )#line:226
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00O00O0O000O0O0O )#line:227
            requests .request ('post',f'{host}/announcement/announcement',headers =O00O00O0O000O0O0O )#line:228
            requests .request ('get',f'{host}/game/getAllData',headers =O00O00O0O000O0O0O )#line:229
            requests .request ('get',f'{host}/assets',headers =O00O00O0O000O0O0O )#line:230
        except Exception as O0OO0000O0O0O0000 :#line:231
            print (O0OO0000O0O0O0000 )#line:232
    def the_query (O0OO0000O00O00O0O ):#line:235
        try :#line:236
            OO0O0O0O0O00O0O0O =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:237
            O0000OOO00O000000 ={'authorization':O0OO0000O00O00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0O0O00O0O0O ),'signstring':OO0O0O0O0O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:247
            O000OOOO00O0OO00O =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0000OOO00O000000 ).json ()#line:248
            if 'status'in O000OOOO00O0OO00O :#line:250
                if O000OOOO00O0OO00O ['status']==200 :#line:251
                    O0O0O00OO00O00OOO =O000OOOO00O0OO00O ['data']['rows'][3 ]['price']#line:252
                    O0OO0000O00O00O0O .market_sale (O0O0O00OO00O00OOO )#line:253
        except Exception as O0000O00O000OOO00 :#line:254
            print (O0000O00O000OOO00 )#line:255
    def market_sale (O0O0OOOOOO0O0OO0O ,O0O0O0O000O0O0OOO ):#line:258
        try :#line:259
            O00O0OOO000O0OO00 =timi_new ()#line:260
            OOO0O0O00OOO0OO0O =f'type=crop__{O00O0OOO000O0OO00}'#line:261
            OOOOO0OOO000OO00O ={'source':'scsc','authorization':O0O0OOOOOO0O0OO0O .token ,'timestamp':str (O00O0OOO000O0OO00 ),'sign':sign (OOO0O0O00OOO0OO0O ),'signstring':OOO0O0O00OOO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:272
            OO0O0OO0O00O000O0 =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =OOOOO0OOO000OO00O ).json ()#line:273
            if 'status'in OO0O0OO0O00O000O0 :#line:275
                if OO0O0OO0O00O000O0 ['status']==200 :#line:276
                    if OO0O0OO0O00O000O0 ['data']['rows']:#line:277
                        O0O000OO00OO000OO =OO0O0OO0O00O000O0 ['data']['rows'][0 ]['packsackItemId']#line:278
                        OO00O0O0O00OO0O00 =OO0O0OO0O00O000O0 ['data']['rows'][0 ]['quantity']#line:279
                        OOO00OOO000O00O00 =float (O0O0O0O000O0O0OOO )+0.001 #line:280
                        OO0O000000OO0OO0O =f'_packsackItemId={O0O000OO00OO000OO}&price={str(OOO00OOO000O00O00)[:6]}&quantity={OO00O0O0O00OO0O00}_{O00O0OOO000O0OO00}'#line:281
                        OOO000O00OO0OO000 ={'source':'scsc','authorization':O0O0OOOOOO0O0OO0O .token ,'timestamp':str (O00O0OOO000O0OO00 ),'sign':sign (OO0O000000OO0OO0O ),'signstring':OO0O000000OO0OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:292
                        OOO00O0OO00O00O00 ={"packsackItemId":O0O000OO00OO000OO ,"price":str (OOO00OOO000O00O00 )[:6 ],"quantity":str (OO00O0O0O00OO0O00 )}#line:297
                        O00OOO0OOOOOO000O =requests .request ('post',f'{host}/market/sale',headers =OOO000O00OO0OO000 ,data =OOO00O0OO00O00O00 ).json ()#line:298
                        if 'status'in O00OOO0OOOOOO000O :#line:300
                            if O00OOO0OOOOOO000O ['status']==200 :#line:301
                                print (f'【上架芦荟】:数量:{OO00O0O0O00OO0O00}丨价格:{str(OOO00OOO000O00O00)[:6]}')#line:302
        except Exception as O0OOOO0O0OOOOOOOO :#line:303
            print (O0OOOO0O0OOOOOOOO )#line:304
    def query_to_sell (O00O0O00OO00O000O ):#line:307
        try :#line:308
            O0O0OO00O00O00OOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:309
            O0OO00O0OOOOO000O ={'source':'scsc','authorization':O00O0O00OO00O000O .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00O00OOO ),'signstring':O0O0OO00O00O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:320
            OO000000O0O0O00OO =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =O0OO00O0OOOOO000O ).json ()#line:322
            if 'status'in OO000000O0O0O00OO :#line:324
                if OO000000O0O0O00OO ['status']==200 :#line:325
                    for O0000O0OOOOOOO0OO in OO000000O0O0O00OO ['data']['rows']:#line:326
                        O0OOO0000O0O0OOO0 =O0000O0OOOOOOO0OO ['materialKey']#line:327
                        OOO0OO0O0000OO0O0 =O0000O0OOOOOOO0OO ['quantity']#line:328
                        OOOO0OOO0OOOO00OO =O0000O0OOOOOOO0OO ['price']#line:329
                        OO00O0O000O00O0OO =O0000O0OOOOOOO0OO ['saleState']#line:330
                        if OO00O0O000O00O0OO ==0 :#line:331
                            print (f'【出售订单】:名称:{O0OOO0000O0O0OOO0}丨数量:{OOO0OO0O0000OO0O0}丨价格:{OOOO0OOO0OOOO00OO}')#line:332
                            O0000OO0OO0000OO0 =O0000O0OOOOOOO0OO ['id']#line:333
                            O00O0O00OO00O000O .cacel_sale (O0000OO0OO0000OO0 )#line:334
        except Exception as OOOO00OOO0OOOO0OO :#line:335
            print (OOOO00OOO0OOOO0OO )#line:336
    def cacel_sale (O00OOOO0000OOOO00 ,O0000OOO00000O000 ):#line:340
        try :#line:341
            OOO0OO0OOO0OOOO0O =f'_saleId={O0000OOO00000O000}_{timi_new()}'#line:342
            OO00O0O00OOOO0OO0 ={'source':'scsc','authorization':O00OOOO0000OOOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO0OOO0OOOO0O ),'signstring':OOO0OO0OOO0OOOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:353
            OO00O0O0000O0O00O ={"saleId":O0000OOO00000O000 }#line:356
            OOO0OO0000O0OOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO00O0O00OOOO0OO0 ,data =OO00O0O0000O0O00O ).json ()#line:357
            if 'status'in OOO0OO0000O0OOOOO :#line:359
                if OOO0OO0000O0OOOOO ['status']==200 :#line:360
                    print (f'【下架出售】:{OOO0OO0000O0OOOOO["data"]}')#line:361
        except Exception as O0OO0OO0O00O00O00 :#line:362
            print (O0OO0OO0O00O00O00 )#line:363
    def change_nickname (OOOOOOO0000OO0O00 ):#line:370
        try :#line:371
            OOOO00OO0000OOOO0 =timi_new ()#line:372
            O00O000OOOOOO00OO ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:373
            OO0OO0O00OOOOO0O0 =requests .request ('post','https://www.qmsjmfb.com/',data =O00O000OOOOOO00OO ).text #line:374
            OOOO0O0OOO0OOOO00 =re .findall ('<ul><li>(.*?)</li>',OO0OO0O00OOOOO0O0 )[0 ][:3 ]#line:375
            OOO00O00OO00OO0OO =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OOOO0O0OOO0OOOO00}').json ()#line:376
            OOOOOO0OO0O0O0O0O =OOO00O00OO00OO0OO ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:377
            O00O0OOO0OOOO0OO0 ={"nickname":OOOOOO0OO0O0O0O0O }#line:378
            O00000O0O0O0OO000 =f'_nickname={OOOOOO0OO0O0O0O0O}_{OOOO00OO0000OOOO0}'#line:379
            OOO0OOOO000O0O0O0 ={'source':'scsc','authorization':OOOOOOO0000OO0O00 .token ,'timestamp':OOOO00OO0000OOOO0 ,'sign':sign (O00000O0O0O0OO000 ),'signstring':O00000O0O0O0OO000 ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:390
            O0O0O0000O0OO0000 =requests .request ('patch',f'{host}/user/nickname',headers =OOO0OOOO000O0O0O0 ,data =O00O0OOO0OOOO0OO0 ).json ()#line:391
            if 'status'in O0O0O0000O0OO0000 :#line:393
                if O0O0O0000O0OO0000 ['status']==200 :#line:394
                    print (f'【修改网名】:网名:{OOOOOO0OO0O0O0O0O}丨{O0O0O0000O0OO0000["message"]}')#line:395
        except Exception as O00OO0O000OO0OOOO :#line:396
            print (O00OO0O000OO0OOOO )#line:397
    def withdraw (OO00O00OO000OO0OO ):#line:402
        try :#line:403
            OOOO0O000O00O000O =f'__{timi_new()}'#line:404
            OOO000OOOOO00OOOO ={'source':'scsc','authorization':OO00O00OO000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000O00O000O ),'signstring':OOOO0O000O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:415
            OO00OOOO0O0O0000O =requests .request ('get',f'{host}/assets',headers =OOO000OOOOO00OOOO ).json ()#line:416
            if 'status'in OO00OOOO0O0O0000O :#line:418
                if OO00OOOO0O0O0000O ['status']==200 :#line:419
                    OO00O00000O00O0OO =OO00OOOO0O0O0000O ['data']['cash']#line:420
                    if float (OO00O00000O00O0OO )>20 :#line:421
                        OOOO0O000O00O000O =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:422
                        OOO000OOOOO00OOOO ={'authorization':OO00O00OO000OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO0O000O00O000O ),'signstring':OOOO0O000O00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:432
                        O0OOO00O0O0O00O00 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:433
                        OOO0O0OO000O00O00 =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =OOO000OOOOO00OOOO ,data =O0OOO00O0O0O00O00 ).json ()#line:434
                        if 'status'in OOO0O0OO000O00O00 :#line:436
                            if OOO0O0OO000O00O00 ['status']==200 :#line:437
                                print (f'【余额提现】:{OOO0O0OO000O00O00["data"]}')#line:438
                        if 'status'in OOO0O0OO000O00O00 :#line:439
                            if OOO0O0OO000O00O00 ['status']==500 :#line:440
                                print (f'【余额提现】:{OOO0O0OO000O00O00["message"]}')#line:441
        except Exception as OOOO00000000OO0O0 :#line:442
            print (OOOO00000000OO0O0 )#line:443
    def invitenum (O0OO0O0O0O00O00OO ):#line:447
        global invited_new #line:448
        try :#line:449
            OO0O0OO0O0O0OOO0O =f'__{timi_new()}'#line:450
            OO0OOO0O00OO0OO00 ={'source':'scsc','authorization':O0OO0O0O0O00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0O0O0OOO0O ),'signstring':OO0O0OO0O0O0OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:461
            O00O00OOO0O0000OO =requests .request ('get',f'{host}/invite/invitenum',headers =OO0OOO0O00OO0OO00 ).json ()#line:462
            if 'status'in O00O00OOO0O0000OO :#line:464
                if O00O00OOO0O0000OO ['status']==200 :#line:465
                    OO0O0O00OO0O0OOO0 =O00O00OOO0O0000OO ['data']['invited_count']#line:466
                    O0OO0000OO00O000O =O00O00OOO0O0000OO ['data']['invited_second_count']#line:467
                    print (f'【我的邀请】:直邀好友:{OO0O0O00OO0O0OOO0}丨间邀好友:{O0OO0000OO00O000O}')#line:468
                    if OO0O0O00OO0O0OOO0 <2 :#line:469
                        O0OOO0O0O00O0000O =f'__{timi_new()}'#line:470
                        OOOO0OO0O0O00OO00 ={'source':'scsc','authorization':O0OO0O0O0O00O00OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO0O0O00O0000O ),'signstring':O0OOO0O0O00O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:481
                        O0OOO0OOOOOOOO0OO =requests .request ('get',f'{host}/user',headers =OOOO0OO0O0O00OO00 ).json ()#line:482
                        if 'status'in O0OOO0OOOOOOOO0OO :#line:484
                            if O0OOO0OOOOOOOO0OO ['status']==200 :#line:485
                                invited_new .append (O0OOO0OOOOOOOO0OO ['data']['inner_id'])#line:486
        except Exception as O0OO0OO0OOOO000O0 :#line:487
            print (O0OO0OO0OOOO000O0 )#line:488
    def game_map (OOOO0OO0OO00O0O0O ):#line:492
        try :#line:493
            O0OOOO000OO0OOOO0 =f'__{timi_new()}'#line:494
            O00000O0000O0O0OO ={'source':'scsc','authorization':OOOO0OO0OO00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO000OO0OOOO0 ),'signstring':O0OOOO000OO0OOOO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:505
            O000O0OO000OO0O00 =requests .request ('get',f'{host}/game/map',headers =O00000O0000O0O0OO ).json ()#line:506
            if 'status'in O000O0OO000OO0O00 :#line:508
                if O000O0OO000OO0O00 ['status']==200 :#line:509
                    for OOO0OO00OO0O00O00 in O000O0OO000OO0O00 ['data']['list'][0 ]['crops']:#line:510
                        O000OO0000O0000O0 =OOO0OO00OO0O00O00 ['level']#line:512
                        if O000OO0000O0000O0 ==41 :#line:513
                            O0OOOO00OOO00O00O =OOO0OO00OO0O00O00 ['crop_name']#line:514
                            O0000O0OOOO00000O =OOO0OO00OO0O00O00 ['count']#line:515
                            if O0000O0OOOO00000O >0 :#line:516
                                print (f'【农业资产】:{O0OOOO00OOO00O00O}丨数量:{O0000O0OOOO00000O}')#line:517
                                OOOO0OO0OO00O0O0O .the_query ()#line:518
        except Exception as OO0O00OO000OOOO00 :#line:519
            print (OO0O00OO000OOOO00 )#line:520
    def give_gold (OO000000O0O0OO000 ):#line:523
        try :#line:524
            O00OOO000O00O0O0O =f'__{timi_new()}'#line:525
            O0O00OOO00OO00OO0 ={'source':'scsc','authorization':OO000000O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000O00O0O0O ),'signstring':O00OOO000O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:536
            O000O00OO00OOOOO0 =requests .request ('get',f'{host}/user',headers =O0O00OOO00OO00OO0 ).json ()#line:537
            if 'status'in O000O00OO00OOOOO0 :#line:538
                if O000O00OO00OOOOO0 ['status']==200 :#line:539
                    if float (OO000000O0O0OO000 .doneeNo )!=0 :#line:540
                        O0OOOO00O0000O0O0 =O000O00OO00OOOOO0 ['data']['assets']['gold']#line:541
                        if float (O0OOOO00O0000O0O0 )>float (OO000000O0O0OO000 .innerId ):#line:542
                            O0O000O0O0OOO0O0O =int (float (O0OOOO00O0000O0O0 )/1.1 )#line:543
                            O00OOO000O00O0O0O =f'_doneeNo={OO000000O0O0OO000.doneeNo}&quantity={O0O000O0O0OOO0O0O}_{timi_new()}'#line:544
                            O0O00OOO00OO00OO0 ={'source':'scsc','authorization':OO000000O0O0OO000 .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO000O00O0O0O ),'signstring':O00OOO000O00O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:555
                            O0O0O00OOOO000OOO ={"quantity":O0O000O0O0OOO0O0O ,"doneeNo":OO000000O0O0OO000 .doneeNo }#line:559
                            O0OO0OO0OO00O0OO0 =requests .request ('post',f'{host}/finance/give-gold',headers =O0O00OOO00OO00OO0 ,data =O0O0O00OOOO000OOO ).json ()#line:560
                            if 'status'in O0OO0OO0OO00O0OO0 :#line:562
                                if O0OO0OO0OO00O0OO0 ['status']==200 :#line:563
                                    if O0OO0OO0OO00O0OO0 ['data']:#line:564
                                        print (f'【赠送种子】:赠送{O0O000O0O0OOO0O0O}种子给{OO000000O0O0OO000.doneeNo}成功')#line:565
                    else :#line:566
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:567
        except Exception as OO0OOO0O0O0OO00O0 :#line:568
            print (OO0OOO0O0O0OO00O0 )#line:569
    def invitation (O0OOO0OOO0000O00O ):#line:571
        try :#line:572
            _OO000OOOO00O0O0OO =float (bundled_def ())/4 #line:573
            OO0OOO0000OOO0O00 =f'_innerId={int(_OO000OOOO00O0O0OO)}_{timi_new()}'#line:574
            OO000O000O0OOO000 ={'source':'scsc','authorization':O0OOO0OOO0000O00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOO0O00 ),'signstring':OO0OOO0000OOO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:585
            O0OOO00O0OO0OOOO0 ={"innerId":int (_OO000OOOO00O0O0OO )}#line:586
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO000O000O0OOO000 ,data =O0OOO00O0OO0OOOO0 )#line:587
        except Exception as OO00000O000OO000O :#line:588
            print (OO00000O000OO000O )#line:589
    def winning_rewards (O0OOO0OOO0OO00O0O ):#line:592
        try :#line:593
            O00OOO00O0O00000O =f'__{timi_new()}'#line:594
            OO000O00OO00000OO ={'source':'scsc','authorization':O0OOO0OOO0OO00O0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00OOO00O0O00000O ),'signstring':O00OOO00O0O00000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:605
            O0OO0OOO0OO000O00 =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO000O00OO00000OO ).json ()#line:606
            if 'status'in O0OO0OOO0OO000O00 :#line:608
                if O0OO0OOO0OO000O00 ['status']==200 :#line:609
                    if O0OO0OOO0OO000O00 ['data']['amount']:#line:610
                        OO00OO00OO0O0O0OO =O0OO0OOO0OO000O00 ['data']['amount']['gold']#line:611
                        return OO00OO00OO0O0O0OO #line:612
                    else :#line:613
                        return 0 #line:614
        except Exception as OOO00000OO0O00OO0 :#line:615
            print (OOO00000OO0O00OO0 )#line:616
    def certification (OO00OOOO0O0OOO000 ):#line:619
        try :#line:620
            OO00O00OOOO00O0OO =f'__{timi_new()}'#line:621
            OOO0OO0OOO0O0O00O ={'source':'scsc','authorization':OO00OOOO0O0OOO000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O00OOOO00O0OO ),'signstring':OO00O00OOOO00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:632
            OOOO0O0O000000000 =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO0OO0OOO0O0O00O ).json ()#line:633
            if 'status'in OOOO0O0O000000000 :#line:635
                if OOOO0O0O000000000 ['status']==200 :#line:636
                    if OOOO0O0O000000000 ['data']['result']:#line:637
                        O0OO000OO0O000OOO =OOOO0O0O000000000 ['data']['nick_name']#line:638
                        return O0OO000OO0O000OOO #line:639
                    else :#line:640
                        return '未实名'#line:641
        except Exception as OOO00OOO000OO00OO :#line:642
            print (OOO00OOO000OO00OO )#line:643
    def crops_illustrated (OOOO000OOOOO0OO00 ):#line:646
        try :#line:647
            OO0000O000O0O0O0O =f'__{timi_new()}'#line:648
            OOO0OO000OOO00O00 ={'source':'scsc','authorization':OOOO000OOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O000O0O0O0O ),'signstring':OO0000O000O0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:659
            O000OOO000O00OO0O =requests .request ('get',f'{host}/game/crops/illustrated',headers =OOO0OO000OOO00O00 ).json ()#line:660
            if 'status'in O000OOO000O00OO0O :#line:662
                if O000OOO000O00OO0O ['status']==200 :#line:663
                    O0O0OOOOO0OO00O00 =O000OOO000O00OO0O ['data'][0 ]['crops']#line:664
                    for O00OO0OOOO0O00OOO in O0O0OOOOO0OO00O00 :#line:665
                        if O00OO0OOOO0O00OOO ['ill_clover_award']:#line:666
                            if float (O00OO0OOOO0O00OOO ['ill_clover_award'])>1 :#line:667
                                if O00OO0OOOO0O00OOO ['is_finish']:#line:668
                                    if not O00OO0OOOO0O00OOO ['is_getit']:#line:669
                                        if OOOO000OOOOO0OO00 .certification ()!='未实名':#line:670
                                            OO0000O000O0O0O0O =f'_award_level={O00OO0OOOO0O00OOO["level"]}_{timi_new()}'#line:671
                                            OOO0OO000OOO00O00 ={'source':'scsc','authorization':OOOO000OOOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O000O0O0O0O ),'signstring':OO0000O000O0O0O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:682
                                            OOOO0OOOO0OO00000 ={"award_level":O00OO0OOOO0O00OOO ['level']}#line:683
                                            OO00O000OOOOO0000 =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =OOO0OO000OOO00O00 ,json =OOOO0OOOO0OO00000 ).json ()#line:685
                                            if 'status'in OO00O000OOOOO0000 :#line:686
                                                if OO00O000OOOOO0000 ['status']==200 :#line:687
                                                    OO00O00OO00OOOOO0 =OO00O000OOOOO0000 ['data']['ill_clover_award']#line:688
                                                    print (f'【图鉴奖励】:领取{O00OO0OOOO0O00OOO["crop_name"]}成就丨奖励{OO00O00OO00OOOOO0}☘️')#line:690
                                                if OO00O000OOOOO0000 ['status']==500 :#line:691
                                                    print (f'【图鉴奖励】:{OO00O000OOOOO0000["message"]}')#line:692
        except Exception as O0O0OO0OO0OO0OOOO :#line:693
            print (O0O0OO0OO0OO0OOOO )#line:694
    def watched_ad (O0OOO0OOO000OO00O ):#line:697
        try :#line:698
            OO0OOOOO0O0000OO0 =f'__{timi_new()}'#line:699
            O0000O00OO0000O00 ={'source':'scsc','authorization':O0OOO0OOO000OO00O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOOO0O0000OO0 ),'signstring':OO0OOOOO0O0000OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:710
            OO000OOOOOOOO0O0O =requests .request ('get',f'{host}/game/getAllData',headers =O0000O00OO0000O00 ).json ()#line:711
            if 'status'in OO000OOOOOOOO0O0O :#line:713
                if OO000OOOOOOOO0O0O ['status']==200 :#line:714
                    if 'offlineInfo'in OO000OOOOOOOO0O0O ['data']:#line:715
                        time .sleep (random .randint (1 ,3 ))#line:716
                        OOOO0O0000O00O0O0 =OO000OOOOOOOO0O0O ['data']['offlineInfo']['off_minute']#line:717
                        O0OOO0OOO0O0O0OO0 =float (OO000OOOOOOOO0O0O ['data']['silver'])/1000000000000 #line:718
                        time .sleep (1 )#line:719
                        requests .request ('post',f'{host}/game/watched-ad',headers =O0000O00OO0000O00 ).json ()#line:720
                        time .sleep (2 )#line:721
                        O0OOO00O00O0O0000 =requests .request ('get',f'{host}/game/getAllData',headers =O0000O00OO0000O00 ).json ()#line:722
                        if 'status'in O0OOO00O00O0O0000 :#line:724
                            if O0OOO00O00O0O0000 ['status']==200 :#line:725
                                OO00OOOO0000000OO =float (O0OOO00O00O0O0000 ['data']['silver'])/1000000000000 #line:726
                                OOOOOO0OOOO0OO0O0 =str (OO00OOOO0000000OO -O0OOO0OOO0O0O0OO0 )[:6 ]#line:727
                                print (f'【离线奖励】:翻倍离线{OOOO0O0000O00O0O0}分钟奖励🌱数量:{OOOOOO0OOOO0OO0O0}t粒')#line:728
        except Exception as OO0O0O0OOOO000000 :#line:729
            print (OO0O0O0OOOO000000 )#line:730
    def user_ad (OO0O0O0O000O0O0OO ):#line:733
        try :#line:734
            O00O00000O00OOO0O =f'__{timi_new()}'#line:735
            OOO00OOO0OOO0000O ={'source':'scsc','authorization':OO0O0O0O000O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00000O00OOO0O ),'signstring':O00O00000O00OOO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:746
            OO0O00O0O0OOO0OO0 =requests .request ('get',f'{host}/user/ad',headers =OOO00OOO0OOO0000O ).json ()#line:747
            if 'status'in OO0O00O0O0OOO0OO0 :#line:749
                if OO0O00O0O0OOO0OO0 ['status']==200 :#line:750
                    OOOO000OOOO00OO00 =OO0O00O0O0OOO0OO0 ['data']['max_time']#line:751
                    OO0O0OOOOOO00OO00 =OO0O00O0O0OOO0OO0 ['data']['watch_time']#line:752
                    O00O00OO0OOO00O0O =OO0O00O0O0OOO0OO0 ['data']['added_time']#line:753
                    print (f'【获取种子】:获取🌱剩余{O00O00OO0OOO00O0O + OOOO000OOOO00OO00 - OO0O0OOOOOO00OO00}次丨好友提供:{O00O00OO0OOO00O0O}次')#line:754
                    if O00O00OO0OOO00O0O +OOOO000OOOO00OO00 -OO0O0OOOOOO00OO00 >0 :#line:755
                        time .sleep (random .randint (16 ,19 ))#line:756
                        O00O0O0O0OOO0O0OO =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OOO00OOO0OOO0000O ).json ()#line:757
                        if 'status'in O00O0O0O0OOO0O0OO :#line:759
                            if O00O0O0O0OOO0O0OO ['status']==200 :#line:760
                                OOOOO0OOO00OOOOOO =float (O00O0O0O0OOO0O0OO ['data']['silver'])/1000000000000 #line:761
                                print (f'【获取种子】:获得🌱:{int(OOOOO0OOO00OOOOOO)}t粒')#line:762
                                return True #line:763
                            if O00O0O0O0OOO0O0OO ['status']==500 :#line:764
                                OOO000000O00OO0OO =O00O0O0O0OOO0O0OO ['message']#line:765
                                print (f'【获取种子】:{OOO000000O00OO0OO}')#line:766
                                return False #line:767
        except Exception as OOO0OOO0O00OO00O0 :#line:768
            print (OOO0OOO0O00OO00O0 )#line:769
    def synthetic (OOO0000O0O000O0O0 ):#line:772
        global id ,g #line:773
        try :#line:774
            OOO0O000OOO000OO0 =OOO0000O0O000O0O0 .level_new ()#line:775
            O0O00000OOO000000 =random .randint (9 ,11 )#line:776
            O0OOOOOO00OO00O0O =f'_site=8&targetSite={O0O00000OOO000000}_{timi_new()}'#line:777
            O00O00O0OOOOOOO00 ={'source':'scsc','authorization':OOO0000O0O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOOOO00OO00O0O ),'signstring':O0OOOOOO00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:788
            O000OO0000OOOOO00 ={"site":int (8 ),"targetSite":int (O0O00000OOO000000 )}#line:789
            requests .request ('post',f'{host}/game/crops/move',headers =O00O00O0OOOOOOO00 ,json =O000OO0000OOOOO00 )#line:790
            while True :#line:791
                OOO0O000O00OOO00O =f'__{timi_new()}'#line:792
                O0OO0O0O0O000O0OO ={'source':'scsc','authorization':OOO0000O0O000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0O000O00OOO00O ),'signstring':OOO0O000O00OOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:803
                OOOO00O00O00OOO0O =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O0O000O0OO ).json ()#line:804
                if 'status'in OOOO00O00O00OOO0O :#line:806
                    if OOOO00O00O00OOO0O ['status']==200 :#line:807
                        O0O0OOOO000OOO0OO =OOOO00O00O00OOO0O ['data']['cropList']#line:808
                        OO00O00O000O0OO0O =OOOO00O00O00OOO0O ['data']['gameCoreDataDBid']#line:809
                        O0OO000OOOOOO0000 =float (OOOO00O00O00OOO0O ['data']['silver'])/1000000000000 #line:810
                        OO00O0OO0O00OOOO0 =0 #line:815
                        for OOOO0OOO000OOOOOO in O0O0OOOO000OOO0OO :#line:816
                            if not OOOO0OOO000OOOOOO :#line:817
                                OO000O0000O0OO0O0 =f'_crop_id={OO00O00O000O0OO0O}&site={OO00O0OO0O00OOOO0}_{OOO0000O0O000O0O0.time}'#line:818
                                O0000OO000OOOO000 ={'source':'scsc','authorization':OOO0000O0O000O0O0 .token ,'timestamp':OOO0000O0O000O0O0 .time ,'sign':sign (OO000O0000O0OO0O0 ),'signstring':OO000O0000O0OO0O0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:828
                                OO00O000OOO0O00OO ={"site":OO00O0OO0O00OOOO0 ,"crop_id":OO00O00O000O0OO0O }#line:829
                                O0O0OOOO0OOO00O00 =requests .request ('post',f'{host}/game/crops/buy',headers =O0000OO000OOOO000 ,data =OO00O000OOO0O00OO ).json ()#line:830
                                time .sleep (random .randint (1 ,3 )/10 )#line:832
                                if 'status'in O0O0OOOO0OOO00O00 :#line:833
                                    if O0O0OOOO0OOO00O00 ['status']==200 :#line:834
                                        if O0O0OOOO0OOO00O00 ['message']=='种子数量不足':#line:835
                                            OOO0O000OOO000OO0 =OOO0000O0O000O0O0 .level_new ()#line:836
                                            print (f'【种植合成】:{O0O0OOOO0OOO00O00["message"]}')#line:837
                                            if not OOO0000O0O000O0O0 .user_ad ():#line:838
                                                return False #line:839
                                    if O0O0OOOO0OOO00O00 ['status']==500 :#line:840
                                        print (f'【种植合成】:{O0O0OOOO0OOO00O00["message"]}')#line:841
                                        return False #line:842
                            OO00O0OO0O00OOOO0 +=1 #line:843
                        OO0OOOO00OOOOOOOO =requests .request ('get',f'{host}/game/getAllData',headers =O0OO0O0O0O000O0OO ).json ()#line:844
                        OO0OOO0O0O00OO00O =OO0OOOO00OOOOOOOO ['data']['cropList']#line:845
                        OO0OOO00OO00O000O =False #line:846
                        for OOOO0OOO000OOOOOO in range (12 ):#line:847
                            id =OO0OOO0O0O00OO00O [OOOO0OOO000OOOOOO ]['level']#line:848
                            if float (OOO0O000OOO000OO0 )-float (id )>9 :#line:849
                                OOO0000O0O0O0OOO0 =f'_site={OOOO0OOO000OOOOOO}_{timi_new()}'#line:850
                                OOOO0O0OO0OOO0OOO ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0000O0O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (OOO0000O0O0O0OOO0 ),'signstring':OOO0000O0O0O0OOO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:861
                                OO0O0O0O0O0OO0O0O ={"site":OOOO0OOO000OOOOOO }#line:862
                                OO000O0OO00OO00O0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOO0O0OO0OOO0OOO ,data =OO0O0O0O0O0OO0O0O ).json ()#line:864
                                if 'status'in OO000O0OO00OO00O0 :#line:865
                                    if OO000O0OO00OO00O0 ['status']==200 :#line:866
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:867
                            if id !=0 :#line:868
                                for OO000O00O0O00O0OO in range (11 ):#line:869
                                    O0OOO0O000O0O0OOO =OO000O00O0O00O0OO +1 #line:870
                                    g =OO0OOO0O0O00OO00O [O0OOO0O000O0O0OOO ]['level']#line:871
                                    if id ==g :#line:872
                                        OO0O0000000O000OO =OO000O00O0O00O0OO +2 #line:873
                                        if OO0O0000000O000OO !=OOOO0OOO000OOOOOO +1 :#line:874
                                            OO0O0OO0O0O0OO000 =OOOO0OOO000OOOOOO +1 #line:875
                                            time .sleep (random .randint (1 ,3 )/10 )#line:877
                                            O0OOOOOO00OO00O0O =f'_site={OO0O0OO0O0O0OO000 - 1}&targetSite={OO0O0000000O000OO - 1}_{timi_new()}'#line:878
                                            O00O00O0OOOOOOO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':OOO0000O0O000O0O0 .token ,'timestamp':timi_new (),'sign':sign (O0OOOOOO00OO00O0O ),'signstring':O0OOOOOO00OO00O0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:895
                                            OO0OOO0OO00000O0O ={"site":int (OO0O0OO0O0O0OO000 -1 ),"targetSite":int (OO0O0000000O000OO -1 )}#line:896
                                            requests .request ('post',f'{host}/game/crops/move',headers =O00O00O0OOOOOOO00 ,json =OO0OOO0OO00000O0O )#line:897
                                            OO0OOO00OO00O000O =True #line:899
                                    if OO0OOO00OO00O000O :#line:900
                                        break #line:901
                                if OO0OOO00OO00O000O :#line:902
                                    break #line:903
        except :#line:904
            OOO0000O0O000O0O0 .synthetic ()#line:905
    def level_new (O00OOO0O00OO0O0OO ):#line:908
        try :#line:909
            O0O0OO00O00000O00 =f'__{timi_new()}'#line:910
            OO0OOOO0O0000OOO0 ={'source':'scsc','authorization':O00OOO0O00OO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O0OO00O00000O00 ),'signstring':O0O0OO00O00000O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:921
            OO0OOOO00000000O0 =requests .request ('get',f'{host}/user',headers =OO0OOOO0O0000OOO0 ).json ()#line:922
            if 'status'in OO0OOOO00000000O0 :#line:923
                if OO0OOOO00000000O0 ['status']==200 :#line:924
                    return float (OO0OOOO00000000O0 ['data']['level'])#line:925
        except Exception as OO00OOO0000O0OO00 :#line:926
            print (OO00OOO0000O0OO00 )#line:927
    def propsraffle (OOO0OO00O0000OO0O ):#line:930
        try :#line:931
            while True :#line:932
                OOO00OO00O0O00000 =f'__{timi_new()}'#line:933
                OOO0O000OO0OO00OO ={'source':'scsc','authorization':OOO0OO00O0000OO0O .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00OO00O0O00000 ),'signstring':OOO00OO00O0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:944
                O00O0OOO0OO0OOO00 =requests .request ('get',f'{host}/propsraffle/lucky',headers =OOO0O000OO0OO00OO ).json ()#line:945
                if 'status'in O00O0OOO0OO0OOO00 :#line:947
                    if O00O0OOO0OO0OOO00 ['status']==200 :#line:948
                        OO0OO00O0OOOO0O00 =O00O0OOO0OO0OOO00 ['data']['rows']#line:949
                        OOOOO0O00O00OO000 =O00O0OOO0OO0OOO00 ['data']['vstate']#line:950
                        if OO0OO00O0OOOO0O00 ==5 or OO0OO00O0OOOO0O00 ==6 or OO0OO00O0OOOO0O00 ==7 :#line:951
                            OO00OO0OO0O000000 =O00O0OOO0OO0OOO00 ['data']['silver']#line:952
                            print (f'【转盘抽奖】:获得种子:{OO00OO0OO0O000000}')#line:953
                        if OO0OO00O0OOOO0O00 ==1 or OO0OO00O0OOOO0O00 ==2 or OO0OO00O0OOOO0O00 ==3 :#line:954
                            O00000O00OOOOO000 =O00O0OOO0OO0OOO00 ['data']['clover']#line:955
                            print (f'【转盘抽奖】:获得三叶草:{O00000O00OOOOO000}')#line:956
                        if OO0OO00O0OOOO0O00 ==4 or OO0OO00O0OOOO0O00 ==8 :#line:957
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:958
                        if OO0OO00O0OOOO0O00 =='抽奖次数已用完':#line:962
                            break #line:996
                time .sleep (random .randint (8 ,15 )/10 )#line:997
        except Exception as O0O0O00000O00OO0O :#line:998
            print (O0O0O00000O00OO0O )#line:999
    def friends_invitation (OO00OO00OOO0O0OOO ):#line:1002
        try :#line:1003
            O0OO0OOOOOOOO0OOO =f'__{timi_new()}'#line:1004
            O0OOO0O0OO0OOO0O0 ={'source':'scsc','authorization':OO00OO00OOO0O0OOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO0OOOOOOOO0OOO ),'signstring':O0OO0OOOOOOOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1015
            OOOOOOO0O00O00OO0 =requests .request ('get',f'{host}/friends',headers =O0OOO0O0OO0OOO0O0 ).json ()#line:1016
            if 'status'in OOOOOOO0O00O00OO0 :#line:1017
                if OOOOOOO0O00O00OO0 ['status']==200 :#line:1018
                    OOOO00OO0O0OOOOOO =OOOOOOO0O00O00OO0 ['data']['myInviteter']#line:1019
                    if OOOO00OO0O0OOOOOO :#line:1020
                        O0OOOO000OOOOOO00 =OOOO00OO0O0OOOOOO ['user']['nickname']#line:1021
                        OOO00OOOO000OOO0O =OO00OO00OOO0O0OOO .certification ()#line:1022
                        print (f'【查邀请人】:我的邀请人:{O0OOOO000OOOOOO00}丨实名:{OOO00OOOO000OOO0O}')#line:1023
                    else :#line:1024
                        if OO00OO00OOO0O0OOO .innerId !='0':#line:1025
                            OO00OO00OOO0O0OOO .invitation ()#line:1026
        except Exception as OOO000OOO00O00000 :#line:1027
            print (OOO000OOO00O00000 )#line:1028
    def add_clover (OO000OOOOOO0OOO0O ):#line:1031
        global golden_seed #line:1032
        try :#line:1033
            O0OO00OOO0OOOO000 =f'__{timi_new()}'#line:1034
            O000O0O00O00O0O00 ={'source':'scsc','authorization':OO000OOOOOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOO0OOOO000 ),'signstring':O0OO00OOO0OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1045
            O0O00000O0OOO000O =requests .request ('get',f'{host}/assets/clovers',headers =O000O0O00O00O0O00 ).json ()#line:1046
            if 'status'in O0O00000O0OOO000O :#line:1048
                if O0O00000O0OOO000O ['status']==200 :#line:1049
                    O00000OO0000O0OOO =O0O00000O0OOO000O ['data']['clover']#line:1050
                    OO000O0OO0OOO000O =O0O00000O0OOO000O ['data']['used_clover']#line:1051
                    OOO00OOO00OOO000O =float (O00000OO0000O0OOO )-float (OO000O0OO0OOO000O )#line:1052
                    print (f'【参与抽奖】:参与抽奖的☘️:{OO000O0OO0OOO000O}')#line:1053
                    if OO000OOOOOO0OOO0O .certification ()!='未实名':#line:1054
                        if OOO00OOO00OOO000O >1 :#line:1055
                            O0OO00OOO0OOOO000 =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(OOO00OOO00OOO000O)}_{timi_new()}'#line:1056
                            OO0O00OOO00000OOO ={'source':'scsc','authorization':OO000OOOOOO0OOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00OOO0OOOO000 ),'signstring':O0OO00OOO0OOOO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1067
                            O00O0O000OOO0O0O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (OOO00OOO00OOO000O )}#line:1068
                            OOO00OO00O0O000OO =requests .request ('post',f'{host}/lottery/add-stake',headers =OO0O00OOO00000OOO ,data =O00O0O000OOO0O0O0 ).json ()#line:1069
                            if 'status'in OOO00OO00O0O000OO :#line:1071
                                if OOO00OO00O0O000OO ['status']==200 :#line:1072
                                    print (f'【参与抽奖】:添加☘️:{OOO00OO00O0O000OO["data"]}丨数量:{OOO00OOO00OOO000O}')#line:1073
                                if OOO00OO00O0O000OO ['status']==500 :#line:1074
                                    print (f'【参与抽奖】:添加☘️:{OOO00OO00O0O000OO["message"]}')#line:1075
            OOOOOO0O000OO0OO0 =requests .request ('get',f'{host}/lottery',headers =O000O0O00O00O0O00 ).json ()#line:1076
            O00O0OO0O0OO000O0 =OO000OOOOOO0OOO0O .winning_rewards ()#line:1078
            if 'status'in OOOOOO0O000OO0OO0 :#line:1079
                if OOOOOO0O000OO0OO0 ['status']==200 :#line:1080
                    O00000OOOO000O0O0 =OOOOOO0O000OO0OO0 ['data'][0 ]['day_get_gold_quantity']#line:1081
                    golden_seed +=float (O00000OOOO000O0O0 )#line:1082
                    OO0O0O0O00OOO0O0O =OOOOOO0O000OO0OO0 ['data'][1 ]['value']#line:1083
                    OOO00O00O00OO00O0 =OOOOOO0O000OO0OO0 ['data'][0 ]['join_number']#line:1084
                    OO000O0O0O00O00O0 =int (float (OOOOOO0O000OO0OO0 ['data'][0 ]['totalValue']))#line:1085
                    OO0OO0000OOOO00OO =float (OO0O0O0O00OOO0O0O /OO000O0O0O00O00O0 )*10000 #line:1086
                    OOOO0O00O0O0O00O0 =OO000O0O0O00O00O0 /OOO00O00O00OO00O0 #line:1087
                    print (f'【参与抽奖】:预计每天中{str(O00000OOOO000O0O0)[:6]}颗金种子丨好友收益:{str(O00O0OO0O0OO000O0)[:6]}')#line:1088
                    print (f'【抽奖统计】:每1万☘️中{str(OO0OO0000OOOO00OO)[:6]}颗金种子丨☘️人均:{str(OOOO0O00O0O0O00O0)[:7]}️')#line:1089
        except Exception as O00O0OO00OO00OOO0 :#line:1090
            print (O00O0OO00OO00OOO0 )#line:1091
    def energy (O0O0OOO0000O00000 ):#line:1095
        try :#line:1096
            while True :#line:1097
                OO000OO000OO0O0O0 =f'__{timi_new()}'#line:1098
                O0000O0O0OOO0OOOO ={'source':'scsc','authorization':O0O0OOO0000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO000OO000OO0O0O0 ),'signstring':OO000OO000OO0O0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1109
                O0000O000OOO0000O =requests .request ('get',f'{host}/energy/general',headers =O0000O0O0OOO0OOOO ).json ()#line:1110
                if 'status'in O0000O000OOO0000O :#line:1112
                    if O0000O000OOO0000O ['status']==200 :#line:1113
                        OOOO000OO00O0OO00 =O0000O000OOO0000O ['data']['ordinary_water']#line:1114
                        O0OOOOO0O0O00O0O0 =O0000O000OOO0000O ['data']['ordinary_fertilizer']#line:1115
                        O00O0OOOOOO00O0OO =O0000O000OOO0000O ['data']['videoStatus']#line:1116
                        O0O0O0OOOO000O000 =O0000O000OOO0000O ['data']['waterVideoKey']#line:1117
                        print (f'【我的营养】:肥料:{str(O0OOOOO0O0O00O0O0).split(".")[0]}丨水滴:{str(OOOO000OO00O0OO00).split(".")[0]}')#line:1118
                        if float (O0OOOOO0O0O00O0O0 )<96 :#line:1119
                            if O00O0OOOOOO00O0OO :#line:1120
                                time .sleep (random .randint (160 ,180 )/10 )#line:1121
                                OO0OO00OOO00O0000 =99 -float (O0OOOOO0O0O00O0O0 )#line:1122
                                OOO0O00O0OOO000OO ={"fertilizer":str (OO0OO00OOO00O0000 ).split ('.')[0 ]}#line:1123
                                OO0OOOOO0O00OOO00 =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =O0000O0O0OOO0OOOO ).json ()#line:1124
                                if 'status'in OO0OOOOO0O00OOO00 :#line:1126
                                    if OO0OOOOO0O00OOO00 ['status']==200 :#line:1127
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOOO0O00OOO00["message"]}')#line:1128
                                    if OO0OOOOO0O00OOO00 ['status']==500 :#line:1129
                                        print (f'【购买肥料】:看广告获取肥料:{OO0OOOOO0O00OOO00["message"]}')#line:1130
                                        break #line:1131
                                if float (O0OOOOO0O0O00O0O0 )<78 :#line:1133
                                    OO0OO00OOO00O0000 =80 -float (O0OOOOO0O0O00O0O0 )#line:1134
                                    OOO0000OOOOO000OO =f'_fertilizer={int(OO0OO00OOO00O0000)}_{timi_new()}'#line:1135
                                    OOOO0OO00000000O0 ={'source':'scsc','authorization':O0O0OOO0000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000OOOOO000OO ),'signstring':OOO0000OOOOO000OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1146
                                    O00OO000OOO0O0OO0 ={"fertilizer":int (OO0OO00OOO00O0000 )}#line:1147
                                    O0O0O0OOO0OO0OOOO =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =OOOO0OO00000000O0 ,data =O00OO000OOO0O0OO0 ).json ()#line:1149
                                    if 'status'in O0O0O0OOO0OO0OOOO :#line:1151
                                        if O0O0O0OOO0OO0OOOO ['status']==200 :#line:1152
                                            print (f'【购买肥料】:购买肥料:{O0O0O0OOO0OO0OOOO["message"]}丨数量:{int(OO0OO00OOO00O0000)}')#line:1153
                                        if O0O0O0OOO0OO0OOOO ['status']==500 :#line:1154
                                            print (f'【购买肥料】:购买肥料:{O0O0O0OOO0OO0OOOO["message"]}丨数量:{int(OO0OO00OOO00O0000)}')#line:1155
                                            O0OO000O00OOOOO00 =O0O0O0OOO0OO0OOOO ["message"].split ('-')[1 ]#line:1156
                                            OOO0000O00O0O0000 =f'__{timi_new()}'#line:1157
                                            OOOOOOO0000O0OOOO ={'source':'scsc','authorization':O0O0OOO0000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O00O0O0000 ),'signstring':OOO0000O00O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1168
                                            O000OO0000O00O0O0 =requests .request ('get',f'{host}/user',headers =OOOOOOO0000O0OOOO ).json ()#line:1169
                                            if 'status'in O000OO0000O00O0O0 :#line:1170
                                                if O000OO0000O00O0O0 ['status']==200 :#line:1171
                                                    OO00OOOO00OO00000 =O000OO0000O00O0O0 ['data']['inner_id']#line:1172
                                                    if give_gold (OO00OOOO00OO00000 ,float (O0OO000O00OOOOO00 )+1 ):#line:1173
                                                        O0O0OOO0000O00000 .energy ()#line:1174
                        if float (OOOO000OO00O0OO00 )<880 :#line:1175
                            if O0O0O0OOOO000O000 :#line:1176
                                time .sleep (random .randint (160 ,180 )/10 )#line:1177
                                OOOO000OOOO00OOO0 =999 -float (OOOO000OO00O0OO00 )#line:1178
                                O0O000OO00OO00O0O ={"water":str (OOOO000OOOO00OOO0 ).split ('.')[0 ]}#line:1179
                                O00OOO0OOOOO000O0 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =O0000O0O0OOO0OOOO ).json ()#line:1180
                                if 'status'in O00OOO0OOOOO000O0 :#line:1182
                                    if O00OOO0OOOOO000O0 ['status']==200 :#line:1183
                                        print (f'【购买水滴】:看广告获取水滴:{O00OOO0OOOOO000O0["message"]}')#line:1184
                                    if O00OOO0OOOOO000O0 ['status']==500 :#line:1185
                                        print (f'【购买水滴】:看广告获取水滴:{O00OOO0OOOOO000O0["message"]}')#line:1186
                                        break #line:1187
                                if float (OOOO000OO00O0OO00 )<780 :#line:1188
                                    OOOO000OOOO00OOO0 =800 -float (OOOO000OO00O0OO00 )#line:1189
                                    OOOO000O00OOO0OO0 =f'_water={int(OOOO000OOOO00OOO0)}_{timi_new()}'#line:1190
                                    OO0O00OO0O0OOOO00 ={'source':'scsc','authorization':O0O0OOO0000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000O00OOO0OO0 ),'signstring':OOOO000O00OOO0OO0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1201
                                    OO0OOO00OO0O0O00O ={"water":int (OOOO000OOOO00OOO0 )}#line:1202
                                    OO00OO00OOOO0000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =OO0O00OO0O0OOOO00 ,data =OO0OOO00OO0O0O00O ).json ()#line:1204
                                    if 'status'in OO00OO00OOOO0000O :#line:1206
                                        if OO00OO00OOOO0000O ['status']==200 :#line:1207
                                            print (f'【购买水滴】:购买水滴:{OO00OO00OOOO0000O["message"]}丨数量:{int(OOOO000OOOO00OOO0)}')#line:1208
                                        if OO00OO00OOOO0000O ['status']==500 :#line:1209
                                            print (f'【购买水滴】:购买水滴:{OO00OO00OOOO0000O["message"]}丨数量:{int(OOOO000OOOO00OOO0)}')#line:1210
                                            O0OO000O00OOOOO00 =OO00OO00OOOO0000O ["message"].split ('-')[1 ]#line:1211
                                            OOO0000O00O0O0000 =f'__{timi_new()}'#line:1212
                                            OOOOOOO0000O0OOOO ={'source':'scsc','authorization':O0O0OOO0000O00000 .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0000O00O0O0000 ),'signstring':OOO0000O00O0O0000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1223
                                            O000OO0000O00O0O0 =requests .request ('get',f'{host}/user',headers =OOOOOOO0000O0OOOO ).json ()#line:1224
                                            if 'status'in O000OO0000O00O0O0 :#line:1225
                                                if O000OO0000O00O0O0 ['status']==200 :#line:1226
                                                    OO00OOOO00OO00000 =O000OO0000O00O0O0 ['data']['inner_id']#line:1227
                                                    if give_gold (OO00OOOO00OO00000 ,float (O0OO000O00OOOOO00 )+1 ):#line:1228
                                                        O0O0OOO0000O00000 .energy ()#line:1229
                        break #line:1230
        except Exception as O00OO000OOO0OO0OO :#line:1231
            print (O00OO000OOO0OO0OO )#line:1232
def bundled_def ():#line:1234
    O00O0OO0OO0O0O0O0 =['5570536','7750212','7911652','7911680','7805624']#line:1235
    return O00O0OO0OO0O0O0O0 [random .randint (0 ,len (O00O0OO0OO0O0O0O0 )-1 )]#line:1236
def version_of_the_validation ():#line:1240
    return str ((92 -56 )/10 )#line:1241
def sc2 ():#line:1243
    return "19319#$%^&*((*"#line:1244
def OO00OO0OO0OO00OO00o0 ():#line:1246
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1247
def get_ip ():#line:1249
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1250
def gitee_validation ():#line:1252
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1253
def gitee_edition ():#line:1255
    try :#line:1256
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1257
    except :#line:1258
        sys .exit (0 )#line:1259
def O000OO000O0O00OOO00 ():#line:1264
    try :#line:1265
        O00OO0O0OOOO0O0O0 =gitee_edition ()#line:1266
        if version_of_the_validation ()<O00OO0O0OOOO0O0O0 ['CityEarth']['edition']:#line:1267
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0O0OOOO0O0O0["CityEarth"]["edition"]}   ❌')#line:1268
            print (f'更新内容=>>{O00OO0O0OOOO0O0O0["CityEarth"]["content"]}   🎉')#line:1269
        else :#line:1270
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00OO0O0OOOO0O0O0["CityEarth"]["edition"]}   ✅')#line:1271
            print (f'更新内容=>> {O00OO0O0OOOO0O0O0["CityEarth"]["content"]}   🎉')#line:1272
    except Exception as O0O00OO00O0O0O00O :#line:1273
        print (O0O00OO00O0O0O00O )#line:1274
def sc3 ():#line:1276
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1277
if __name__ =='__main__':#line:1281
    start ()#line:1282
