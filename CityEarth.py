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
def start ():#line:7
    try :#line:8
        O000OO000O0O00OOO00 ()#line:9
        print (f'你的卡密是：{OO00OO0OO0OO00OO00o0()}')#line:10
        O000OO0O00OO00O00 ()#line:11
        OO00O0O0OO000O00O =json .load (open ("CityEarth_data.json",'r'))['data']#line:12
        print (f"==========共找到{len(OO00O0O0OO000O00O)}个账号==========")#line:13
        for O0OO000O0000OO000 in OO00O0O0OO000O00O :#line:14
            OOO0OOO0O000OOO0O =[]#line:15
            print (f"------------正在执行第{OO00O0O0OO000O00O.index(O0OO000O0000OO000) + 1}个账号------------")#line:16
            O0OOOO0000O00O0OO =CityEarth (O0OO000O0000OO000 ,OOO0OOO0O000OOO0O ,OO00O0O0OO000O00O .index (O0OO000O0000OO000 ))#line:17
            def O000O0000O0O000OO ():#line:18
                if O0OOOO0000O00O0OO .base_info ():#line:20
                    O0OOOO0000O00O0OO .sealing ()#line:22
                    O0OOOO0000O00O0OO .invitenum ()#line:24
                    O0OOOO0000O00O0OO .query_to_sell ()#line:26
                    O0OOOO0000O00O0OO .game_map ()#line:28
                    O0OOOO0000O00O0OO .friends_invitation ()#line:30
                    O0OOOO0000O00O0OO .energy ()#line:32
                    O0OOOO0000O00O0OO .add_clover ()#line:34
                    O0OOOO0000O00O0OO .propsraffle ()#line:36
                    O0OOOO0000O00O0OO .synthetic ()#line:38
                    O0OOOO0000O00O0OO .crops_illustrated ()#line:40
                    O0OOOO0000O00O0OO .give_gold ()#line:42
                    O0OOOO0000O00O0OO .withdraw ()#line:44
            OO0O00O0OOO0OOO0O =threading .Thread (target =O000O0000O0O000OO )#line:46
            OO0O00O0OOO0OOO0O .start ()#line:47
            time .sleep (time_xx )#line:48
        print (f"------------正在处理推送通知------------")#line:49
        time .sleep (0.5 )#line:50
        OO0O0OO0OOOOOO0OO =format_msg ()#line:51
        print (f'预计每日收益：{str(golden_seed)[:6]}金种子',OO0O0OO0OOOOOO0OO +' ')#line:52
    except Exception as O0O0O000000O00000 :#line:53
        print (O0O0O000000O00000 )#line:54
def give_gold (O0O000O000OO00O00 ,OOOOO0OOO0O0O0OOO ):#line:57
        try :#line:58
            OOOO000O00O00O00O =f'_doneeNo={O0O000O000OO00O00}&quantity={int(OOOOO0OOO0O0O0OOO)}_{timi_new()}'#line:59
            OOO0O00O000OO000O ={'source':'scsc','authorization':json .load (open ("CityEarth_data.json",'r'))['data'][0 ]['authorization'],'timestamp':str (timi_new ()),'sign':sign (OOOO000O00O00O00O ),'signstring':OOOO000O00O00O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:70
            O0000O0O0OO0O0000 ={"quantity":int (OOOOO0OOO0O0O0OOO ),"doneeNo":O0O000O000OO00O00 }#line:74
            OOOOOOO0O00OOO0OO =requests .request ('post',f'{host}/finance/give-gold',headers =OOO0O00O000OO000O ,data =O0000O0O0OO0O0000 ).json ()#line:75
            if 'status'in OOOOOOO0O00OOO0OO :#line:77
                if OOOOOOO0O00OOO0OO ['status']==200 :#line:78
                    if OOOOOOO0O00OOO0OO ['data']:#line:79
                        print (f'【赠送种子】:赠送{int(OOOOO0OOO0O0O0OOO)}种子给{O0O000O000OO00O00}成功')#line:80
                        return True #line:81
                if OOOOOOO0O00OOO0OO ['status']==401 :#line:82
                    print (f'【赠送种子】:{OOOOOOO0O00OOO0OO["message"]}')#line:83
                    return False #line:84
                if OOOOOOO0O00OOO0OO ['status']==500 :#line:85
                    print (f'【赠送种子】:{OOOOOOO0O00OOO0OO["message"]}')#line:86
                    return False #line:87
            return False #line:88
        except Exception as O00O0OO0000000O0O :#line:89
            print (O00O0OO0000000O0O )#line:90
def kvkv ():#line:91
    return '/vastzzzl/vastzzzl/raw/master'#line:92
def sign (O0O0O0OO0O0OOO00O ):#line:95
    OOOO0OOO00OO00000 =hashlib .md5 (O0O0O0OO0O0OOO00O .encode ()).hexdigest ()#line:96
    OO00OO0O0OOOOOO0O =sc1 ()#line:97
    OOOO00O000000OO0O =sc2 ()#line:98
    OO0O0OO0O0OO00OOO =sc3 ()#line:99
    OO00OOO0OO000OO0O =OO00OO0O0OOOOOO0O +OOOO0OOO00OO00000 +OOOO00O000000OO0O +OO0O0OO0O0OO00OOO #line:100
    O00OO0OOO0O0OOO0O =hashlib .md5 (OO00OOO0OO000OO0O .encode ()).hexdigest ()#line:101
    return O00OO0OOO0O0OOO0O #line:102
def format_msg ():#line:106
    O00OO0O00O00O0OOO =""#line:107
    for OO0O0O0O00O0O000O in msg_list :#line:108
        O00OO0O00O00O0OOO +=str (OO0O0O0O00O0O000O )+"\r\n"#line:109
    return O00OO0O00O00O0OOO #line:110
def sc1 ():#line:112
    return "scsc%^&*"#line:113
def O000OO0O00OO00O00 ():#line:115
    if OO00OO0OO0OO00OO00o0 ()in gitee_validation ()['validation']:#line:116
        pass #line:117
    else :#line:118
        exit (1 )#line:119
def timi_new ():#line:121
    return str (int (time .time ()*1000 ))#line:122
json_path ="CityEarth_data.json"#line:125
json_path1 ="CityEarth_data.json"#line:126
dict ={}#line:127
def get_json_data (OO00OO0OO00OO0OO0 ,O0O0O0000OO00O00O ,O0O0O00O0O0000000 ,OOOOO0O00000OO00O ):#line:129
    with open (OO00OO0OO00OO0OO0 ,'rb')as O0000OOOOOO0O000O :#line:131
        O000OOO000O00OOO0 =json .load (O0000OOOOOO0O000O )#line:132
        O000OOO000O00OOO0 ['data'][O0O0O0000OO00O00O ][O0O0O00O0O0000000 ]=OOOOO0O00000OO00O #line:133
        O0OO0000OOO000O0O =O000OOO000O00OOO0 #line:134
    O0000OOOOOO0O000O .close ()#line:135
    return O0OO0000OOO000O0O #line:136
def write_json_data (OOO0O0O0000000O00 ):#line:138
    with open (json_path1 ,'w')as OO0000OO0O00000O0 :#line:139
        json .dump (OOO0O0O0000000O00 ,OO0000OO0O00000O0 )#line:140
    OO0000OO0O00000O0 .close ()#line:141
    return True #line:142
class CityEarth :#line:144
    def __init__ (OO0O000OOO000000O ,O0O0O0O00OO0000OO ,OOO0OOO000000OO0O ,O0O0O0O0OO0O00OO0 ):#line:146
        try :#line:147
            OO0O000OOO000000O .msg =OOO0OOO000000OO0O #line:148
            OO0O000OOO000000O .time =str (time .time ()*1000 ).split ('.')[0 ]#line:149
            OO0O000OOO000000O .token =O0O0O0O00OO0000OO ['authorization']#line:150
            OO0O000OOO000000O .innerId =json .load (open ("CityEarth_data.json",'r'))['unified_data']['innerId']#line:151
            OO0O000OOO000000O .doneeNo =json .load (open ("CityEarth_data.json",'r'))['unified_data']['doneeNo']#line:152
            OO0O000OOO000000O .elephant_user =O0O0O0O00OO0000OO ['elephant_user']#line:153
            OO0O000OOO000000O .elephant_pswd =O0O0O0O00OO0000OO ['elephant_pswd']#line:154
            OO0O000OOO000000O .elephant_Task_ID =O0O0O0O00OO0000OO ['elephant_Task_ID']#line:155
            OO0O000OOO000000O .len_new =O0O0O0O0OO0O00OO0 #line:156
        except :#line:157
            print ('变量格式错误')#line:158
    def base_info (OO0OO0O0O0O00O0O0 ):#line:161
        try :#line:162
            OO0OO0O0O0O00O0O0 .watched_ad ()#line:164
            O00000OOO0O00O0OO =f'__{timi_new()}'#line:165
            OOOOOOOOO00O0000O ={'source':'scsc','authorization':OO0OO0O0O0O00O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00000OOO0O00O0OO ),'signstring':O00000OOO0O00O0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:176
            OO0OO0OO00000OOOO =requests .request ('get',f'{host}/user',headers =OOOOOOOOO00O0000O ).json ()#line:177
            if 'status'in OO0OO0OO00000OOOO :#line:179
                if OO0OO0OO00000OOOO ['status']==200 :#line:180
                    O000O0O0OOO00OOOO =OO0OO0OO00000OOOO ['data']['nickname']#line:181
                    O0000OO00O0OO0OO0 =OO0OO0OO00000OOOO ['data']['inner_id']#line:182
                    OOO000O0OOOOOO00O =OO0OO0OO00000OOOO ['data']['assets']['gold']#line:183
                    O0O00O0000OOO0O0O =OO0OO0OO00000OOOO ['data']['level']#line:184
                    print (f'【账号信息】:昵称:{O000O0O0OOO00OOOO[:5]}丨ID:{O0000OO00O0OO0OO0}丨等级:{O0O00O0000OOO0O0O}丨金种子:{str(OOO000O0OOOOOO00O).split(".")[0]}')#line:185
                    if 'wx_'in O000O0O0OOO00OOOO :#line:186
                        OO0OO0O0O0O00O0O0 .change_nickname ()#line:187
                if OO0OO0OO00000OOOO ['status']==401 :#line:188
                    print ('【账号信息】:账号失效正在尝试登录')#line:189
                    if OO0OO0O0O0O00O0O0 .elephant_user =='f':#line:190
                        return False #line:191
                    OO00O0OOOOOO0OOOO =Invalid_login .addtask (elephant_user =OO0OO0O0O0O00O0O0 .elephant_user ,elephant_pswd =OO0OO0O0O0O00O0O0 .elephant_pswd ,elephant_Task_ID =OO0OO0O0O0O00O0O0 .elephant_Task_ID )#line:192
                    OO00O0OOOO000O000 =get_json_data (json_path ,OO0OO0O0O0O00O0O0 .len_new ,'authorization',OO00O0OOOOOO0OOOO )#line:193
                    if write_json_data (OO00O0OOOO000O000 ):#line:194
                        print ('正在写入账号配置文件')#line:195
                    return False #line:196
                if OO0OO0OO00000OOOO ['status']==500 :#line:197
                    return False #line:198
            return True #line:199
        except Exception as OOO0000OO0OOOOO00 :#line:200
            print (OOO0000OO0OOOOO00 )#line:201
    def sealing (O0OO0000O00OO0000 ):#line:204
        try :#line:205
            OO0OOO0000OOO0OOO =f'__{timi_new()}'#line:206
            O00OO0OOO00000OOO ={'source':'scsc','authorization':O0OO0000O00OO0000 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOO0000OOO0OOO ),'signstring':OO0OOO0000OOO0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:217
            requests .request ('get',f'{host}/friends/cash-rewards/rank',headers =O00OO0OOO00000OOO )#line:218
            requests .request ('get',f'{host}/packsack/list',headers =O00OO0OOO00000OOO )#line:219
            requests .request ('get',f'{host}/friends/invited/ad',headers =O00OO0OOO00000OOO )#line:220
            requests .request ('get',f'{host}/assets/gold/rank',headers =O00OO0OOO00000OOO )#line:221
            requests .request ('get',f'{host}/user',headers =O00OO0OOO00000OOO )#line:222
            requests .request ('get',f'{host}/propsraffle/lucky/number',headers =O00OO0OOO00000OOO )#line:223
            requests .request ('get',f'{host}/finance/get-power-list',headers =O00OO0OOO00000OOO )#line:224
            requests .request ('post',f'{host}/announcement/announcement',headers =O00OO0OOO00000OOO )#line:225
            requests .request ('get',f'{host}/game/getAllData',headers =O00OO0OOO00000OOO )#line:226
            requests .request ('get',f'{host}/assets',headers =O00OO0OOO00000OOO )#line:227
        except Exception as OO0O0O0OO0OOOOO00 :#line:228
            print (OO0O0O0OO0OOOOO00 )#line:229
    def the_query (OO00O0OOO0O0OOOOO ):#line:232
        try :#line:233
            OOO00O0OO0O0000O0 =f'page=1&pageSize=20&queryField=__{timi_new()}'#line:234
            O0OO00OOOO0OOO0O0 ={'authorization':OO00O0OOO0O0OOOOO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OO0O0000O0 ),'signstring':OOO00O0OO0O0000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:244
            O00O00OO0OOO0O0O0 =requests .request ('get',f'{host}/market/get-crop-sale-list?page=1&queryField=&pageSize=20',headers =O0OO00OOOO0OOO0O0 ).json ()#line:245
            if 'status'in O00O00OO0OOO0O0O0 :#line:247
                if O00O00OO0OOO0O0O0 ['status']==200 :#line:248
                    O00000O0O0OOO0000 =O00O00OO0OOO0O0O0 ['data']['rows'][3 ]['price']#line:249
                    OO00O0OOO0O0OOOOO .market_sale (O00000O0O0OOO0000 )#line:250
        except Exception as O00OO0O000O0OOO0O :#line:251
            print (O00OO0O000O0OOO0O )#line:252
    def market_sale (O0O000O00OO0000OO ,O0O0000OO00OOO00O ):#line:255
        try :#line:256
            OO000OOO00O0O00OO =timi_new ()#line:257
            OO0OOO00O000OO0O0 =f'type=crop__{OO000OOO00O0O00OO}'#line:258
            O0O0O000O0OOOOO00 ={'source':'scsc','authorization':O0O000O00OO0000OO .token ,'timestamp':str (OO000OOO00O0O00OO ),'sign':sign (OO0OOO00O000OO0O0 ),'signstring':OO0OOO00O000OO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:269
            O00000O0OOO00O0OO =requests .request ('get',f'{host}/market/get-allow-sale-material-list?type=crop',headers =O0O0O000O0OOOOO00 ).json ()#line:270
            if 'status'in O00000O0OOO00O0OO :#line:272
                if O00000O0OOO00O0OO ['status']==200 :#line:273
                    if O00000O0OOO00O0OO ['data']['rows']:#line:274
                        O0O0OOOOOOO0OOO0O =O00000O0OOO00O0OO ['data']['rows'][0 ]['packsackItemId']#line:275
                        O0OOO0O00000OOO0O =O00000O0OOO00O0OO ['data']['rows'][0 ]['quantity']#line:276
                        O0O0000O0O0O0OOOO =float (O0O0000OO00OOO00O )+0.001 #line:277
                        OOO00O0O0OO000OOO =f'_packsackItemId={O0O0OOOOOOO0OOO0O}&price={str(O0O0000O0O0O0OOOO)[:6]}&quantity={O0OOO0O00000OOO0O}_{OO000OOO00O0O00OO}'#line:278
                        O0O0OO0OO0000OO0O ={'source':'scsc','authorization':O0O000O00OO0000OO .token ,'timestamp':str (OO000OOO00O0O00OO ),'sign':sign (OOO00O0O0OO000OOO ),'signstring':OOO00O0O0OO000OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:289
                        O0OO0O000OO0OO0O0 ={"packsackItemId":O0O0OOOOOOO0OOO0O ,"price":str (O0O0000O0O0O0OOOO )[:6 ],"quantity":str (O0OOO0O00000OOO0O )}#line:294
                        O0OO0000O0OOOOOOO =requests .request ('post',f'{host}/market/sale',headers =O0O0OO0OO0000OO0O ,data =O0OO0O000OO0OO0O0 ).json ()#line:295
                        if 'status'in O0OO0000O0OOOOOOO :#line:297
                            if O0OO0000O0OOOOOOO ['status']==200 :#line:298
                                print (f'【上架芦荟】:数量:{O0OOO0O00000OOO0O}丨价格:{str(O0O0000O0O0O0OOOO)[:6]}')#line:299
        except Exception as O0O000000O00OO0O0 :#line:300
            print (O0O000000O00OO0O0 )#line:301
    def query_to_sell (OO0000000O0O00OO0 ):#line:304
        try :#line:305
            O0OO00O00OO0O0OOO =f'page=1&pageSize=10&type=crop__{timi_new()}'#line:306
            OO0OOOOO0O00O0OOO ={'source':'scsc','authorization':OO0000000O0O00OO0 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OO00O00OO0O0OOO ),'signstring':O0OO00O00OO0O0OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:317
            O00000000OO0O0O00 =requests .request ('get',f'{host}/market/get-owner-sale-list?page=1&pageSize=10&type=crop',headers =OO0OOOOO0O00O0OOO ).json ()#line:319
            if 'status'in O00000000OO0O0O00 :#line:321
                if O00000000OO0O0O00 ['status']==200 :#line:322
                    for O0OO0OO00OOOO00OO in O00000000OO0O0O00 ['data']['rows']:#line:323
                        OOOOO0O00OO0O0O0O =O0OO0OO00OOOO00OO ['materialKey']#line:324
                        OO0O00O00O00OOOO0 =O0OO0OO00OOOO00OO ['quantity']#line:325
                        O0OOO0O0OO00OOO00 =O0OO0OO00OOOO00OO ['price']#line:326
                        O0OO00OOO0O0O0OO0 =O0OO0OO00OOOO00OO ['saleState']#line:327
                        if O0OO00OOO0O0O0OO0 ==0 :#line:328
                            print (f'【出售订单】:名称:{OOOOO0O00OO0O0O0O}丨数量:{OO0O00O00O00OOOO0}丨价格:{O0OOO0O0OO00OOO00}')#line:329
                            O0000000OOOO000OO =O0OO0OO00OOOO00OO ['id']#line:330
                            OO0000000O0O00OO0 .cacel_sale (O0000000OOOO000OO )#line:331
        except Exception as OO0OOOOO000OO00O0 :#line:332
            print (OO0OOOOO000OO00O0 )#line:333
    def cacel_sale (OO0OOOOO0O00OOO00 ,O0OOOO0O00O000O00 ):#line:337
        try :#line:338
            OO00O0OOOO0OO0O00 =f'_saleId={O0OOOO0O00O000O00}_{timi_new()}'#line:339
            OO00O0O0OO00O0000 ={'source':'scsc','authorization':OO0OOOOO0O00OOO00 .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O0OOOO0OO0O00 ),'signstring':OO00O0OOOO0OO0O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:350
            O0OOOO000OOO0OOO0 ={"saleId":O0OOOO0O00O000O00 }#line:353
            O0OO000OO00OOOOOO =requests .request ('post',f'{host}/market/cacel-sale',headers =OO00O0O0OO00O0000 ,data =O0OOOO000OOO0OOO0 ).json ()#line:354
            if 'status'in O0OO000OO00OOOOOO :#line:356
                if O0OO000OO00OOOOOO ['status']==200 :#line:357
                    print (f'【下架出售】:{O0OO000OO00OOOOOO["data"]}')#line:358
        except Exception as O0OO00O00OO0O0O00 :#line:359
            print (O0OO00O00OO0O0O00 )#line:360
    def change_nickname (OOO0OO0O00000O0O0 ):#line:367
        try :#line:368
            OOO00O000OO0O0000 =timi_new ()#line:369
            OO0O00O0O00OO00O0 ={'xing':'','xinglength':'all','minglength':'all','sex':'all','dic':'default','num':'1',}#line:370
            O00O0OO0O0O0OOO0O =requests .request ('post','https://www.qmsjmfb.com/',data =OO0O00O0O00OO00O0 ).text #line:371
            OO00OO0O00OO00OOO =re .findall ('<ul><li>(.*?)</li>',O00O0OO0O0O0OOO0O )[0 ][:3 ]#line:372
            O000O0000O0000O00 =requests .post (f'https://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i={OO00OO0O00OO00OOO}').json ()#line:373
            OOO0OO0OOOO0OO00O =O000O0000O0000O00 ['translateResult'][0 ][0 ]['tgt'].replace (' ','')[:5 ]#line:374
            OO0O0OOO000OO0O0O ={"nickname":OOO0OO0OOOO0OO00O }#line:375
            OOOOOO00O0O0OOOOO =f'_nickname={OOO0OO0OOOO0OO00O}_{OOO00O000OO0O0000}'#line:376
            O00OOOOO000O00OO0 ={'source':'scsc','authorization':OOO0OO0O00000O0O0 .token ,'timestamp':OOO00O000OO0O0000 ,'sign':sign (OOOOOO00O0O0OOOOO ),'signstring':OOOOOO00O0O0OOOOO ,'version':'3.1.41954131','janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:387
            OO0O00OO00O0O0000 =requests .request ('patch',f'{host}/user/nickname',headers =O00OOOOO000O00OO0 ,data =OO0O0OOO000OO0O0O ).json ()#line:388
            if 'status'in OO0O00OO00O0O0000 :#line:390
                if OO0O00OO00O0O0000 ['status']==200 :#line:391
                    print (f'【修改网名】:网名:{OOO0OO0OOOO0OO00O}丨{OO0O00OO00O0O0000["message"]}')#line:392
        except Exception as OOO0OOOOOO0O0000O :#line:393
            print (OOO0OOOOOO0O0000O )#line:394
    def withdraw (OOO0OO00OO0O0O0OO ):#line:399
        OOO000OOOOOO0O000 =f'__{timi_new()}'#line:400
        O00OOO0OO0O0OOOOO ={'source':'scsc','authorization':OOO0OO00OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOOO0O000 ),'signstring':OOO000OOOOOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:411
        O00OOO0OO0O0O00O0 =requests .request ('get',f'{host}/assets',headers =O00OOO0OO0O0OOOOO ).json ()#line:412
        if 'status'in O00OOO0OO0O0O00O0 :#line:414
            if O00OOO0OO0O0O00O0 ['status']==200 :#line:415
                OO00OOOO0OO00000O =O00OOO0OO0O0O00O0 ['data']['cash']#line:416
                if float (OO00OOOO0OO00000O )>20 :#line:417
                    OOO000OOOOOO0O000 =f'_withdrawId=48c9478f-275e-4df8-b102-09b6e02f8a36_{timi_new()}'#line:418
                    O00OOO0OO0O0OOOOO ={'authorization':OOO0OO00OO0O0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000OOOOOO0O000 ),'signstring':OOO000OOOOOO0O000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:428
                    OO00O0OOO0000O0O0 ={"withdrawId":"48c9478f-275e-4df8-b102-09b6e02f8a36"}#line:429
                    O00OO0O000O0O00OO =requests .request ('post','http://scsc.sc19319.com/finance/withdraw',headers =O00OOO0OO0O0OOOOO ,data =OO00O0OOO0000O0O0 ).json ()#line:431
                    print (O00OO0O000O0O00OO )#line:432
    def invitenum (O0OO0OOO0OOOO0O0O ):#line:435
        OO0O0OO0OO0O00OOO =f'__{timi_new()}'#line:436
        OOO0O000O0OO00O00 ={'source':'scsc','authorization':O0OO0OOO0OOOO0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0OO0OO0O00OOO ),'signstring':OO0O0OO0OO0O00OOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:447
        OO0OO0O0O000O00O0 =requests .request ('get',f'{host}/invite/invitenum',headers =OOO0O000O0OO00O00 ).json ()#line:448
        if 'status'in OO0OO0O0O000O00O0 :#line:450
            if OO0OO0O0O000O00O0 ['status']==200 :#line:451
                O00O0OOO000O0O0OO =OO0OO0O0O000O00O0 ['data']['invited_count']#line:452
                OOOOO0000O0OO0OOO =OO0OO0O0O000O00O0 ['data']['invited_second_count']#line:453
                print (f'【我的邀请】:直邀好友:{O00O0OOO000O0O0OO}丨间邀好友:{OOOOO0000O0OO0OOO}')#line:454
    def game_map (O0O00OOOOO00OO0OO ):#line:457
        try :#line:458
            O0OOOO0O0O0OOOO00 =f'__{timi_new()}'#line:459
            OOOO0O0O0000O0OO0 ={'source':'scsc','authorization':O0O00OOOOO00OO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOOO0O0O0OOOO00 ),'signstring':O0OOOO0O0O0OOOO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:470
            O00000OO0OOO0O00O =requests .request ('get',f'{host}/game/map',headers =OOOO0O0O0000O0OO0 ).json ()#line:471
            if 'status'in O00000OO0OOO0O00O :#line:473
                if O00000OO0OOO0O00O ['status']==200 :#line:474
                    for OOOOO0OO0OOOO0O00 in O00000OO0OOO0O00O ['data']['list'][0 ]['crops']:#line:475
                        OO0O00O0OOO0O0OO0 =OOOOO0OO0OOOO0O00 ['level']#line:477
                        if OO0O00O0OOO0O0OO0 ==41 :#line:478
                            O000O0OOO0OO0OO0O =OOOOO0OO0OOOO0O00 ['crop_name']#line:479
                            OOO00OOO000O0OOOO =OOOOO0OO0OOOO0O00 ['count']#line:480
                            if OOO00OOO000O0OOOO >0 :#line:481
                                print (f'【农业资产】:{O000O0OOO0OO0OO0O}丨数量:{OOO00OOO000O0OOOO}')#line:482
                                O0O00OOOOO00OO0OO .the_query ()#line:483
        except Exception as O0OO0000OOO0OO00O :#line:484
            print (O0OO0000OOO0OO00O )#line:485
    def give_gold (O000OO0O0OO0OOOO0 ):#line:488
        try :#line:489
            OOOO000OO0OO0OOOO =f'__{timi_new()}'#line:490
            OOOO00O0OO0000O00 ={'source':'scsc','authorization':O000OO0O0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OO0OO0OOOO ),'signstring':OOOO000OO0OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:501
            OOOOO00OOOOOO00OO =requests .request ('get',f'{host}/user',headers =OOOO00O0OO0000O00 ).json ()#line:502
            if 'status'in OOOOO00OOOOOO00OO :#line:503
                if OOOOO00OOOOOO00OO ['status']==200 :#line:504
                    if float (O000OO0O0OO0OOOO0 .doneeNo )!=0 :#line:505
                        OO0OO00O0000O00O0 =OOOOO00OOOOOO00OO ['data']['assets']['gold']#line:506
                        if float (OO0OO00O0000O00O0 )>float (O000OO0O0OO0OOOO0 .innerId ):#line:507
                            OOOOOO0000O0OOO0O =int (float (OO0OO00O0000O00O0 )/1.1 )#line:508
                            OOOO000OO0OO0OOOO =f'_doneeNo={O000OO0O0OO0OOOO0.doneeNo}&quantity={OOOOOO0000O0OOO0O}_{timi_new()}'#line:509
                            OOOO00O0OO0000O00 ={'source':'scsc','authorization':O000OO0O0OO0OOOO0 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO000OO0OO0OOOO ),'signstring':OOOO000OO0OO0OOOO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:520
                            OOOOO00O0OOO0OOO0 ={"quantity":OOOOOO0000O0OOO0O ,"doneeNo":O000OO0O0OO0OOOO0 .doneeNo }#line:524
                            O0O000O0OOOOO0O00 =requests .request ('post',f'{host}/finance/give-gold',headers =OOOO00O0OO0000O00 ,data =OOOOO00O0OOO0OOO0 ).json ()#line:525
                            if 'status'in O0O000O0OOOOO0O00 :#line:527
                                if O0O000O0OOOOO0O00 ['status']==200 :#line:528
                                    if O0O000O0OOOOO0O00 ['data']:#line:529
                                        print (f'【赠送种子】:赠送{OOOOOO0000O0OOO0O}种子给{O000OO0O0OO0OOOO0.doneeNo}成功')#line:530
                    else :#line:531
                        print (f'【赠送种子】:此账号未启动赠送功能')#line:532
        except Exception as O000OO0OO0O00O000 :#line:533
            print (O000OO0OO0O00O000 )#line:534
    def invitation (O00000000OOOOOO0O ):#line:536
        try :#line:537
            _O000000O0O0O0OO00 =float (bundled_def ())/4 #line:538
            O00O0OOOO0OOOO0OO =f'_innerId={int(_O000000O0O0O0OO00)}_{timi_new()}'#line:539
            OO0OOOOOOOOO0OO0O ={'source':'scsc','authorization':O00000000OOOOOO0O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OOOO0OOOO0OO ),'signstring':O00O0OOOO0OOOO0OO ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:550
            OOOOO0OOO0O0000O0 ={"innerId":int (_O000000O0O0O0OO00 )}#line:551
            requests .request ('post',f'{host}/friends/my-invitation',headers =OO0OOOOOOOOO0OO0O ,data =OOOOO0OOO0O0000O0 )#line:552
        except Exception as O0O00O0OO000OO000 :#line:553
            print (O0O00O0OO000OO000 )#line:554
    def winning_rewards (O000O0OOO00OOO0OO ):#line:557
        try :#line:558
            OOO00O0OOOO000000 =f'__{timi_new()}'#line:559
            OO0000O0OOOO0O0O0 ={'source':'scsc','authorization':O000O0OOO00OOO0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO00O0OOOO000000 ),'signstring':OOO00O0OOOO000000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:570
            O00O0O00O00OOO00O =requests .request ('get',f'{host}/friends/winning-rewards/amount',headers =OO0000O0OOOO0O0O0 ).json ()#line:571
            if 'status'in O00O0O00O00OOO00O :#line:573
                if O00O0O00O00OOO00O ['status']==200 :#line:574
                    if O00O0O00O00OOO00O ['data']['amount']:#line:575
                        O0O0OOO0OO0OOO00O =O00O0O00O00OOO00O ['data']['amount']['gold']#line:576
                        return O0O0OOO0OO0OOO00O #line:577
                    else :#line:578
                        return 0 #line:579
        except Exception as OOO0OO000OO0O0O00 :#line:580
            print (OOO0OO000OO0O0O00 )#line:581
    def certification (O000O00O0O00000O0 ):#line:584
        try :#line:585
            O00O0OO00O0OO000O =f'__{timi_new()}'#line:586
            OOO00OOOOO00O000O ={'source':'scsc','authorization':O000O00O0O00000O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O0OO00O0OO000O ),'signstring':O00O0OO00O0OO000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:597
            OO0OO0OO00OOOOO0O =requests .request ('get',f'{host}/certification/get-auth-status',headers =OOO00OOOOO00O000O ).json ()#line:598
            if 'status'in OO0OO0OO00OOOOO0O :#line:600
                if OO0OO0OO00OOOOO0O ['status']==200 :#line:601
                    if OO0OO0OO00OOOOO0O ['data']['result']:#line:602
                        O0O000O00000O000O =OO0OO0OO00OOOOO0O ['data']['nick_name']#line:603
                        return O0O000O00000O000O #line:604
                    else :#line:605
                        return '未实名'#line:606
        except Exception as OOO00O0O00OO0OOOO :#line:607
            print (OOO00O0O00OO0OOOO )#line:608
    def crops_illustrated (O0000OO0OOOO0OO00 ):#line:611
        try :#line:612
            O0OOO00OOOOO00000 =f'__{timi_new()}'#line:613
            O0O00OOO000OO0O0O ={'source':'scsc','authorization':O0000OO0OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOOO00000 ),'signstring':O0OOO00OOOOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:624
            O000OO000OOO0O0O0 =requests .request ('get',f'{host}/game/crops/illustrated',headers =O0O00OOO000OO0O0O ).json ()#line:625
            if 'status'in O000OO000OOO0O0O0 :#line:627
                if O000OO000OOO0O0O0 ['status']==200 :#line:628
                    OO0O00O00O00O0O00 =O000OO000OOO0O0O0 ['data'][0 ]['crops']#line:629
                    for OOOOOO0OO0OOOOOO0 in OO0O00O00O00O0O00 :#line:630
                        if OOOOOO0OO0OOOOOO0 ['ill_clover_award']:#line:631
                            if float (OOOOOO0OO0OOOOOO0 ['ill_clover_award'])>1 :#line:632
                                if OOOOOO0OO0OOOOOO0 ['is_finish']:#line:633
                                    if not OOOOOO0OO0OOOOOO0 ['is_getit']:#line:634
                                        if O0000OO0OOOO0OO00 .certification ()!='未实名':#line:635
                                            O0OOO00OOOOO00000 =f'_award_level={OOOOOO0OO0OOOOOO0["level"]}_{timi_new()}'#line:636
                                            O0O00OOO000OO0O0O ={'source':'scsc','authorization':O0000OO0OOOO0OO00 .token ,'timestamp':str (timi_new ()),'sign':sign (O0OOO00OOOOO00000 ),'signstring':O0OOO00OOOOO00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:647
                                            O0OOOO000O0OO0O0O ={"award_level":OOOOOO0OO0OOOOOO0 ['level']}#line:648
                                            O0OO000OO0000O00O =requests .request ('post',f'{host}/game/crops/illustrated/award',headers =O0O00OOO000OO0O0O ,json =O0OOOO000O0OO0O0O ).json ()#line:650
                                            if 'status'in O0OO000OO0000O00O :#line:651
                                                if O0OO000OO0000O00O ['status']==200 :#line:652
                                                    OO0000OOOO0OO0OOO =O0OO000OO0000O00O ['data']['ill_clover_award']#line:653
                                                    print (f'【图鉴奖励】:领取{OOOOOO0OO0OOOOOO0["crop_name"]}成就丨奖励{OO0000OOOO0OO0OOO}☘️')#line:655
                                                if O0OO000OO0000O00O ['status']==500 :#line:656
                                                    print (f'【图鉴奖励】:{O0OO000OO0000O00O["message"]}')#line:657
        except Exception as O0000O00000OO00OO :#line:658
            print (O0000O00000OO00OO )#line:659
    def watched_ad (O0OOO00OO00O0OOOO ):#line:662
        try :#line:663
            O0O00O00OO00000O0 =f'__{timi_new()}'#line:664
            OO000OO0OO00OO00O ={'source':'scsc','authorization':O0OOO00OO00O0OOOO .token ,'timestamp':str (timi_new ()),'sign':sign (O0O00O00OO00000O0 ),'signstring':O0O00O00OO00000O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:675
            O0000O0O00OOO000O =requests .request ('get',f'{host}/game/getAllData',headers =OO000OO0OO00OO00O ).json ()#line:676
            if 'status'in O0000O0O00OOO000O :#line:678
                if O0000O0O00OOO000O ['status']==200 :#line:679
                    if 'offlineInfo'in O0000O0O00OOO000O ['data']:#line:680
                        time .sleep (random .randint (1 ,3 ))#line:681
                        O0000OO0000OO000O =O0000O0O00OOO000O ['data']['offlineInfo']['off_minute']#line:682
                        OO00OOO00O0OOOOOO =float (O0000O0O00OOO000O ['data']['silver'])/1000000000000 #line:683
                        time .sleep (1 )#line:684
                        requests .request ('post',f'{host}/game/watched-ad',headers =OO000OO0OO00OO00O ).json ()#line:685
                        time .sleep (2 )#line:686
                        OO0OOOOOOOOOOO0O0 =requests .request ('get',f'{host}/game/getAllData',headers =OO000OO0OO00OO00O ).json ()#line:687
                        if 'status'in OO0OOOOOOOOOOO0O0 :#line:689
                            if OO0OOOOOOOOOOO0O0 ['status']==200 :#line:690
                                OOOO00OOOOOOO0O0O =float (OO0OOOOOOOOOOO0O0 ['data']['silver'])/1000000000000 #line:691
                                OOOOO0O0OOOO0O00O =str (OOOO00OOOOOOO0O0O -OO00OOO00O0OOOOOO )[:6 ]#line:692
                                print (f'【离线奖励】:翻倍离线{O0000OO0000OO000O}分钟奖励🌱数量:{OOOOO0O0OOOO0O00O}t粒')#line:693
        except Exception as O00OOO00OOO0000OO :#line:694
            print (O00OOO00OOO0000OO )#line:695
    def user_ad (OO0000OOO00000O00 ):#line:698
        try :#line:699
            OOOO00O000OO0O00O =f'__{timi_new()}'#line:700
            OO0OOO0O00OO0O0OO ={'source':'scsc','authorization':OO0000OOO00000O00 .token ,'timestamp':str (timi_new ()),'sign':sign (OOOO00O000OO0O00O ),'signstring':OOOO00O000OO0O00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:711
            OOOO0000000O0OOOO =requests .request ('get',f'{host}/user/ad',headers =OO0OOO0O00OO0O0OO ).json ()#line:712
            if 'status'in OOOO0000000O0OOOO :#line:714
                if OOOO0000000O0OOOO ['status']==200 :#line:715
                    O0O0000O0000000OO =OOOO0000000O0OOOO ['data']['max_time']#line:716
                    OO0O0OOOO0O00OOO0 =OOOO0000000O0OOOO ['data']['watch_time']#line:717
                    OO0O000O0OO0OOOO0 =OOOO0000000O0OOOO ['data']['added_time']#line:718
                    print (f'【获取种子】:获取🌱剩余{OO0O000O0OO0OOOO0 + O0O0000O0000000OO - OO0O0OOOO0O00OOO0}次丨好友提供:{OO0O000O0OO0OOOO0}次')#line:719
                    if OO0O000O0OO0OOOO0 +O0O0000O0000000OO -OO0O0OOOO0O00OOO0 >0 :#line:720
                        time .sleep (random .randint (16 ,19 ))#line:721
                        O0OO0OOOO0OO0OO00 =requests .request ('post',f'{host}/game/watched-ad-forSilver',headers =OO0OOO0O00OO0O0OO ).json ()#line:722
                        if 'status'in O0OO0OOOO0OO0OO00 :#line:724
                            if O0OO0OOOO0OO0OO00 ['status']==200 :#line:725
                                OOO00OO0OO0O00OO0 =float (O0OO0OOOO0OO0OO00 ['data']['silver'])/1000000000000 #line:726
                                print (f'【获取种子】:获得🌱:{int(OOO00OO0OO0O00OO0)}t粒')#line:727
                                return True #line:728
                            if O0OO0OOOO0OO0OO00 ['status']==500 :#line:729
                                OO00O0000O000000O =O0OO0OOOO0OO0OO00 ['message']#line:730
                                print (f'【获取种子】:{OO00O0000O000000O}')#line:731
                                return False #line:732
        except Exception as O0O0O0OOOO0O00O00 :#line:733
            print (O0O0O0OOOO0O00O00 )#line:734
    def synthetic (O00O0000OO0OOO00O ):#line:737
        global id ,g #line:738
        try :#line:739
            OO00OOO000OOOO0OO =O00O0000OO0OOO00O .level_new ()#line:740
            O000OO0OOO0000O0O =random .randint (9 ,11 )#line:741
            O0O000O0OO000OO0O =f'_site=8&targetSite={O000OO0OOO0000O0O}_{timi_new()}'#line:742
            O0000OOO000O0OO00 ={'source':'scsc','authorization':O00O0000OO0OOO00O .token ,'timestamp':timi_new (),'sign':sign (O0O000O0OO000OO0O ),'signstring':O0O000O0OO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:753
            OO0OOO0OOOOOOO000 ={"site":int (8 ),"targetSite":int (O000OO0OOO0000O0O )}#line:754
            requests .request ('post',f'{host}/game/crops/move',headers =O0000OOO000O0OO00 ,json =OO0OOO0OOOOOOO000 )#line:755
            while True :#line:756
                O00O000OOOOO0OO00 =f'__{timi_new()}'#line:757
                OOOOOO00OO0000OO0 ={'source':'scsc','authorization':O00O0000OO0OOO00O .token ,'timestamp':str (timi_new ()),'sign':sign (O00O000OOOOO0OO00 ),'signstring':O00O000OOOOO0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:768
                O00000O000O0O00O0 =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO00OO0000OO0 ).json ()#line:769
                if 'status'in O00000O000O0O00O0 :#line:771
                    if O00000O000O0O00O0 ['status']==200 :#line:772
                        O0O00O00O00O0O000 =O00000O000O0O00O0 ['data']['cropList']#line:773
                        OOO0O0O00OO0OOOOO =O00000O000O0O00O0 ['data']['gameCoreDataDBid']#line:774
                        OO00O000OO0OO0OOO =float (O00000O000O0O00O0 ['data']['silver'])/1000000000000 #line:775
                        OOO00OO00O00O0O00 =0 #line:780
                        for O00OO0O0OOOO00O00 in O0O00O00O00O0O000 :#line:781
                            if not O00OO0O0OOOO00O00 :#line:782
                                OOO00000OO000OO0O =f'_crop_id={OOO0O0O00OO0OOOOO}&site={OOO00OO00O00O0O00}_{O00O0000OO0OOO00O.time}'#line:783
                                OOOO0O00OO00O0000 ={'source':'scsc','authorization':O00O0000OO0OOO00O .token ,'timestamp':O00O0000OO0OOO00O .time ,'sign':sign (OOO00000OO000OO0O ),'signstring':OOO00000OO000OO0O ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:793
                                OOO0O000O000O000O ={"site":OOO00OO00O00O0O00 ,"crop_id":OOO0O0O00OO0OOOOO }#line:794
                                O0OO00O0000OO0O00 =requests .request ('post',f'{host}/game/crops/buy',headers =OOOO0O00OO00O0000 ,data =OOO0O000O000O000O ).json ()#line:795
                                time .sleep (random .randint (1 ,3 )/10 )#line:797
                                if 'status'in O0OO00O0000OO0O00 :#line:798
                                    if O0OO00O0000OO0O00 ['status']==200 :#line:799
                                        if O0OO00O0000OO0O00 ['message']=='种子数量不足':#line:800
                                            OO00OOO000OOOO0OO =O00O0000OO0OOO00O .level_new ()#line:801
                                            print (f'【种植合成】:{O0OO00O0000OO0O00["message"]}')#line:802
                                            if not O00O0000OO0OOO00O .user_ad ():#line:803
                                                return False #line:804
                                    if O0OO00O0000OO0O00 ['status']==500 :#line:805
                                        print (f'【种植合成】:{O0OO00O0000OO0O00["message"]}')#line:806
                                        return False #line:807
                            OOO00OO00O00O0O00 +=1 #line:808
                        OOOO00O000OOO0OOO =requests .request ('get',f'{host}/game/getAllData',headers =OOOOOO00OO0000OO0 ).json ()#line:809
                        OOO00OOOO0OOO0O0O =OOOO00O000OOO0OOO ['data']['cropList']#line:810
                        O000000O0OO000O00 =False #line:811
                        for O00OO0O0OOOO00O00 in range (12 ):#line:812
                            id =OOO00OOOO0OOO0O0O [O00OO0O0OOOO00O00 ]['level']#line:813
                            if float (OO00OOO000OOOO0OO )-float (id )>9 :#line:814
                                OOOOOOOOOO0000OO0 =f'_site={O00OO0O0OOOO00O00}_{timi_new()}'#line:815
                                OOOOOOO00OO00O000 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O0000OO0OOO00O .token ,'timestamp':timi_new (),'sign':sign (OOOOOOOOOO0000OO0 ),'signstring':OOOOOOOOOO0000OO0 ,'version':'3.1.9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1'}#line:826
                                O0000000OO0O00O00 ={"site":O00OO0O0OOOO00O00 }#line:827
                                OOO00O0OO000OOOO0 =requests .request ('post',f'{host}/game/crops/sellForSilver',headers =OOOOOOO00OO00O000 ,data =O0000000OO0O00O00 ).json ()#line:829
                                if 'status'in OOO00O0OO000OOOO0 :#line:830
                                    if OOO00O0OO000OOOO0 ['status']==200 :#line:831
                                        print (f'【出售植物】:低级农作物卖出成功丨等级:{id}')#line:832
                            if id !=0 :#line:833
                                for O0O000OOOOOO00O00 in range (11 ):#line:834
                                    O0000OOOO00O0O00O =O0O000OOOOOO00O00 +1 #line:835
                                    g =OOO00OOOO0OOO0O0O [O0000OOOO00O0O00O ]['level']#line:836
                                    if id ==g :#line:837
                                        O0O0000O00000000O =O0O000OOOOOO00O00 +2 #line:838
                                        if O0O0000O00000000O !=O00OO0O0OOOO00O00 +1 :#line:839
                                            O0OOOOOOO0O000O00 =O00OO0O0OOOO00O00 +1 #line:840
                                            time .sleep (random .randint (1 ,3 )/10 )#line:842
                                            O0O000O0OO000OO0O =f'_site={O0OOOOOOO0O000O00 - 1}&targetSite={O0O0000O00000000O - 1}_{timi_new()}'#line:843
                                            O0000OOO000O0OO00 ={'source':'scsc','accept':'application/json, text/plain, */*','authorization':O00O0000OO0OOO00O .token ,'timestamp':timi_new (),'sign':sign (O0O000O0OO000OO0O ),'signstring':O0O000O0OO000OO0O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Content-Type':'application/json','Content-Length':'25','Host':'scsc.sc19319.com','Connection':'Keep-Alive','Accept-Encoding':'gzip','Cookie':'acw_tc=0b32823216747149060213010e21419fac6656bd55878feb6448914e13b43b','User-Agent':'okhttp/4.9.1'}#line:860
                                            OOOO0OOO00O00O000 ={"site":int (O0OOOOOOO0O000O00 -1 ),"targetSite":int (O0O0000O00000000O -1 )}#line:861
                                            requests .request ('post',f'{host}/game/crops/move',headers =O0000OOO000O0OO00 ,json =OOOO0OOO00O00O000 )#line:862
                                            O000000O0OO000O00 =True #line:864
                                    if O000000O0OO000O00 :#line:865
                                        break #line:866
                                if O000000O0OO000O00 :#line:867
                                    break #line:868
        except :#line:869
            O00O0000OO0OOO00O .synthetic ()#line:870
    def level_new (O0OO0O0OOO000O0O0 ):#line:873
        try :#line:874
            OO0O0O0OOO0O00000 =f'__{timi_new()}'#line:875
            O00000000OO00000O ={'source':'scsc','authorization':O0OO0O0OOO000O0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O0O0OOO0O00000 ),'signstring':OO0O0O0OOO0O00000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:886
            OOOOOOOO0000O00O0 =requests .request ('get',f'{host}/user',headers =O00000000OO00000O ).json ()#line:887
            if 'status'in OOOOOOOO0000O00O0 :#line:888
                if OOOOOOOO0000O00O0 ['status']==200 :#line:889
                    return float (OOOOOOOO0000O00O0 ['data']['level'])#line:890
        except Exception as OOOO0O00O00OOOOOO :#line:891
            print (OOOO0O00O00OOOOOO )#line:892
    def propsraffle (OOOO0O000O0OOO0O0 ):#line:895
        try :#line:896
            while True :#line:897
                OO0OOOO0OO0O0OO00 =f'__{timi_new()}'#line:898
                O0O00O0OO00OO00OO ={'source':'scsc','authorization':OOOO0O000O0OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (OO0OOOO0OO0O0OO00 ),'signstring':OO0OOOO0OO0O0OO00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:909
                O000O00O00O00O0OO =requests .request ('get',f'{host}/propsraffle/lucky',headers =O0O00O0OO00OO00OO ).json ()#line:910
                if 'status'in O000O00O00O00O0OO :#line:912
                    if O000O00O00O00O0OO ['status']==200 :#line:913
                        OOOO000O000OOOO0O =O000O00O00O00O0OO ['data']['rows']#line:914
                        O0000O0O0OOOOO0OO =O000O00O00O00O0OO ['data']['vstate']#line:915
                        if OOOO000O000OOOO0O ==5 or OOOO000O000OOOO0O ==6 or OOOO000O000OOOO0O ==7 :#line:916
                            OOOOO0O00O000OOOO =O000O00O00O00O0OO ['data']['silver']#line:917
                            print (f'【转盘抽奖】:获得种子:{OOOOO0O00O000OOOO}')#line:918
                        if OOOO000O000OOOO0O ==1 or OOOO000O000OOOO0O ==2 or OOOO000O000OOOO0O ==3 :#line:919
                            OOO0O0O0O0OO000O0 =O000O00O00O00O0OO ['data']['clover']#line:920
                            print (f'【转盘抽奖】:获得三叶草:{OOO0O0O0O0OO000O0}')#line:921
                        if OOOO000O000OOOO0O ==4 or OOOO000O000OOOO0O ==8 :#line:922
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:923
                        if OOOO000O000OOOO0O =='抽奖次数已用完':#line:927
                            break #line:961
                time .sleep (random .randint (8 ,15 )/10 )#line:962
        except Exception as OOOO00OOO0O0OO00O :#line:963
            print (OOOO00OOO0O0OO00O )#line:964
    def friends_invitation (O0OOOO0O000OOO0O0 ):#line:967
        try :#line:968
            O00O00O00OOOOO00O =f'__{timi_new()}'#line:969
            O000O0OOO00OOO000 ={'source':'scsc','authorization':O0OOOO0O000OOO0O0 .token ,'timestamp':str (timi_new ()),'sign':sign (O00O00O00OOOOO00O ),'signstring':O00O00O00OOOOO00O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:980
            O0OOOOO00OOO00O00 =requests .request ('get',f'{host}/friends',headers =O000O0OOO00OOO000 ).json ()#line:981
            if 'status'in O0OOOOO00OOO00O00 :#line:982
                if O0OOOOO00OOO00O00 ['status']==200 :#line:983
                    O0OOO0OOOOOOO0OO0 =O0OOOOO00OOO00O00 ['data']['myInviteter']#line:984
                    if O0OOO0OOOOOOO0OO0 :#line:985
                        O00000OOOO0OO0O00 =O0OOO0OOOOOOO0OO0 ['user']['nickname']#line:986
                        O0OO00OOO0O000O0O =O0OOOO0O000OOO0O0 .certification ()#line:987
                        print (f'【查邀请人】:我的邀请人:{O00000OOOO0OO0O00}丨实名:{O0OO00OOO0O000O0O}')#line:988
                    else :#line:989
                        if O0OOOO0O000OOO0O0 .innerId !='0':#line:990
                            O0OOOO0O000OOO0O0 .invitation ()#line:991
        except Exception as OO0OO00000000O00O :#line:992
            print (OO0OO00000000O00O )#line:993
    def add_clover (OOO0OOOO0O00O0O0O ):#line:996
        global golden_seed #line:997
        try :#line:998
            OO0000O00O0O0000O =f'__{timi_new()}'#line:999
            OOO0OOOOO0O00O0O0 ={'source':'scsc','authorization':OOO0OOOO0O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O0O0000O ),'signstring':OO0000O00O0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1010
            O00O00OO0O0O0O0O0 =requests .request ('get',f'{host}/assets/clovers',headers =OOO0OOOOO0O00O0O0 ).json ()#line:1011
            if 'status'in O00O00OO0O0O0O0O0 :#line:1013
                if O00O00OO0O0O0O0O0 ['status']==200 :#line:1014
                    OO00000000OOOO000 =O00O00OO0O0O0O0O0 ['data']['clover']#line:1015
                    O000O0OOOO0000OOO =O00O00OO0O0O0O0O0 ['data']['used_clover']#line:1016
                    O0OOO0O00O0OOOOOO =float (OO00000000OOOO000 )-float (O000O0OOOO0000OOO )#line:1017
                    print (f'【参与抽奖】:参与抽奖的☘️:{O000O0OOOO0000OOO}')#line:1018
                    if OOO0OOOO0O00O0O0O .certification ()!='未实名':#line:1019
                        if O0OOO0O00O0OOOOOO >1 :#line:1020
                            OO0000O00O0O0000O =f'_lotteryId=13f02ff5-f8db-4ddc-9e9a-3d328a211fff&quantity={int(O0OOO0O00O0OOOOOO)}_{timi_new()}'#line:1021
                            O0OO0000O0OOO00O0 ={'source':'scsc','authorization':OOO0OOOO0O00O0O0O .token ,'timestamp':str (timi_new ()),'sign':sign (OO0000O00O0O0000O ),'signstring':OO0000O00O0O0000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1032
                            OO0OO0OO0OOO00OOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOO0O00O0OOOOOO )}#line:1033
                            O0OO00O0O0OOO000O =requests .request ('post',f'{host}/lottery/add-stake',headers =O0OO0000O0OOO00O0 ,data =OO0OO0OO0OOO00OOO ).json ()#line:1034
                            if 'status'in O0OO00O0O0OOO000O :#line:1036
                                if O0OO00O0O0OOO000O ['status']==200 :#line:1037
                                    print (f'【参与抽奖】:添加☘️:{O0OO00O0O0OOO000O["data"]}丨数量:{O0OOO0O00O0OOOOOO}')#line:1038
                                if O0OO00O0O0OOO000O ['status']==500 :#line:1039
                                    print (f'【参与抽奖】:添加☘️:{O0OO00O0O0OOO000O["message"]}')#line:1040
            OOO00OO0O00OO0OO0 =requests .request ('get',f'{host}/lottery',headers =OOO0OOOOO0O00O0O0 ).json ()#line:1041
            O000OOOO000O0O00O =OOO0OOOO0O00O0O0O .winning_rewards ()#line:1043
            if 'status'in OOO00OO0O00OO0OO0 :#line:1044
                if OOO00OO0O00OO0OO0 ['status']==200 :#line:1045
                    O00OOOO0OO0O00O0O =OOO00OO0O00OO0OO0 ['data'][0 ]['day_get_gold_quantity']#line:1046
                    golden_seed +=float (O00OOOO0OO0O00O0O )#line:1047
                    O0OO0000O00000OO0 =OOO00OO0O00OO0OO0 ['data'][1 ]['value']#line:1048
                    OOOOOO00O0OOOOOOO =OOO00OO0O00OO0OO0 ['data'][0 ]['join_number']#line:1049
                    O0O00O0O000OOOOO0 =int (float (OOO00OO0O00OO0OO0 ['data'][0 ]['totalValue']))#line:1050
                    O0OOO00000O0OO0O0 =float (O0OO0000O00000OO0 /O0O00O0O000OOOOO0 )*10000 #line:1051
                    O0O0OO0O0OOO0OOOO =O0O00O0O000OOOOO0 /OOOOOO00O0OOOOOOO #line:1052
                    print (f'【参与抽奖】:预计每天中{str(O00OOOO0OO0O00O0O)[:6]}颗金种子丨好友收益:{str(O000OOOO000O0O00O)[:6]}')#line:1053
                    print (f'【抽奖统计】:每1万☘️中{str(O0OOO00000O0OO0O0)[:6]}颗金种子丨☘️人均:{str(O0O0OO0O0OOO0OOOO)[:7]}️')#line:1054
        except Exception as OOO000000000OOO0O :#line:1055
            print (OOO000000000OOO0O )#line:1056
    def energy (OOOO00OOOOOO0O0OO ):#line:1060
        try :#line:1061
            while True :#line:1062
                OOO0OO00OO00O000O =f'__{timi_new()}'#line:1063
                OO00O0OOO00O00000 ={'source':'scsc','authorization':OOOO00OOOOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO0OO00OO00O000O ),'signstring':OOO0OO00OO00O000O ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1074
                O0OOO0OOO00OO0OOO =requests .request ('get',f'{host}/energy/general',headers =OO00O0OOO00O00000 ).json ()#line:1075
                if 'status'in O0OOO0OOO00OO0OOO :#line:1077
                    if O0OOO0OOO00OO0OOO ['status']==200 :#line:1078
                        OOOO0OO0000OOO0O0 =O0OOO0OOO00OO0OOO ['data']['ordinary_water']#line:1079
                        O0000OO0OO0OOO00O =O0OOO0OOO00OO0OOO ['data']['ordinary_fertilizer']#line:1080
                        O00O000O0O0OO0OO0 =O0OOO0OOO00OO0OOO ['data']['videoStatus']#line:1081
                        OOOO0O0OOOOOOO000 =O0OOO0OOO00OO0OOO ['data']['waterVideoKey']#line:1082
                        print (f'【我的营养】:肥料:{str(O0000OO0OO0OOO00O).split(".")[0]}丨水滴:{str(OOOO0OO0000OOO0O0).split(".")[0]}')#line:1083
                        if float (O0000OO0OO0OOO00O )<96 :#line:1084
                            if O00O000O0O0OO0OO0 :#line:1085
                                time .sleep (random .randint (160 ,180 )/10 )#line:1086
                                OO000O0OO0OOOOOOO =99 -float (O0000OO0OO0OOO00O )#line:1087
                                O00OOOOOO0OO0O00O ={"fertilizer":str (OO000O0OO0OOOOOOO ).split ('.')[0 ]}#line:1088
                                O00OO00OO00OOO00O =requests .request ('post',f'{host}/video/general/nutrition/fadverti',headers =OO00O0OOO00O00000 ).json ()#line:1089
                                if 'status'in O00OO00OO00OOO00O :#line:1091
                                    if O00OO00OO00OOO00O ['status']==200 :#line:1092
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO00OO00OOO00O["message"]}')#line:1093
                                    if O00OO00OO00OOO00O ['status']==500 :#line:1094
                                        print (f'【购买肥料】:看广告获取肥料:{O00OO00OO00OOO00O["message"]}')#line:1095
                                        break #line:1096
                                if float (O0000OO0OO0OOO00O )<78 :#line:1098
                                    OO000O0OO0OOOOOOO =80 -float (O0000OO0OO0OOO00O )#line:1099
                                    OO00O000OOO0OO000 =f'_fertilizer={int(OO000O0OO0OOOOOOO)}_{timi_new()}'#line:1100
                                    O0OOOOO0OO000O00O ={'source':'scsc','authorization':OOOO00OOOOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO00O000OOO0OO000 ),'signstring':OO00O000OOO0OO000 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1111
                                    OOOOOOOOO0O0OO0OO ={"fertilizer":int (OO000O0OO0OOOOOOO )}#line:1112
                                    OOO0OO000O00O000O =requests .request ('post',f'{host}/energy/general/buy/fertilizer',headers =O0OOOOO0OO000O00O ,data =OOOOOOOOO0O0OO0OO ).json ()#line:1114
                                    if 'status'in OOO0OO000O00O000O :#line:1116
                                        if OOO0OO000O00O000O ['status']==200 :#line:1117
                                            print (f'【购买肥料】:购买肥料:{OOO0OO000O00O000O["message"]}丨数量:{int(OO000O0OO0OOOOOOO)}')#line:1118
                                        if OOO0OO000O00O000O ['status']==500 :#line:1119
                                            print (f'【购买肥料】:购买肥料:{OOO0OO000O00O000O["message"]}丨数量:{int(OO000O0OO0OOOOOOO)}')#line:1120
                                            OOO00OO00O00O00OO =OOO0OO000O00O000O ["message"].split ('-')[1 ]#line:1121
                                            OOO000O0O00OOO0O0 =f'__{timi_new()}'#line:1122
                                            O00000OO00OO0OOO0 ={'source':'scsc','authorization':OOOO00OOOOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O00OOO0O0 ),'signstring':OOO000O0O00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1133
                                            O0OOOO0OOOO00000O =requests .request ('get',f'{host}/user',headers =O00000OO00OO0OOO0 ).json ()#line:1134
                                            if 'status'in O0OOOO0OOOO00000O :#line:1135
                                                if O0OOOO0OOOO00000O ['status']==200 :#line:1136
                                                    OOO0O00O0OOO0000O =O0OOOO0OOOO00000O ['data']['inner_id']#line:1137
                                                    if give_gold (OOO0O00O0OOO0000O ,float (OOO00OO00O00O00OO )+1 ):#line:1138
                                                        OOOO00OOOOOO0O0OO .energy ()#line:1139
                        if float (OOOO0OO0000OOO0O0 )<880 :#line:1140
                            if OOOO0O0OOOOOOO000 :#line:1141
                                time .sleep (random .randint (160 ,180 )/10 )#line:1142
                                O0O0O0O0000O000O0 =999 -float (OOOO0OO0000OOO0O0 )#line:1143
                                O0OO00OOOOO00O0O0 ={"water":str (O0O0O0O0000O000O0 ).split ('.')[0 ]}#line:1144
                                O000OOOO00OOOO000 =requests .request ('post',f'{host}/video/general/nutrition/wadverti',headers =OO00O0OOO00O00000 ).json ()#line:1145
                                if 'status'in O000OOOO00OOOO000 :#line:1147
                                    if O000OOOO00OOOO000 ['status']==200 :#line:1148
                                        print (f'【购买水滴】:看广告获取水滴:{O000OOOO00OOOO000["message"]}')#line:1149
                                    if O000OOOO00OOOO000 ['status']==500 :#line:1150
                                        print (f'【购买水滴】:看广告获取水滴:{O000OOOO00OOOO000["message"]}')#line:1151
                                        break #line:1152
                                if float (OOOO0OO0000OOO0O0 )<780 :#line:1153
                                    O0O0O0O0000O000O0 =800 -float (OOOO0OO0000OOO0O0 )#line:1154
                                    OO0O00OOO00O00O00 =f'_water={int(O0O0O0O0000O000O0)}_{timi_new()}'#line:1155
                                    O0000OOOOOO000000 ={'source':'scsc','authorization':OOOO00OOOOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OO0O00OOO00O00O00 ),'signstring':OO0O00OOO00O00O00 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1166
                                    O0OO00O000O0OOO0O ={"water":int (O0O0O0O0000O000O0 )}#line:1167
                                    OOO0OO000OOO0000O =requests .request ('post',f'{host}/energy/general/buy/water',headers =O0000OOOOOO000000 ,data =O0OO00O000O0OOO0O ).json ()#line:1169
                                    if 'status'in OOO0OO000OOO0000O :#line:1171
                                        if OOO0OO000OOO0000O ['status']==200 :#line:1172
                                            print (f'【购买水滴】:购买水滴:{OOO0OO000OOO0000O["message"]}丨数量:{int(O0O0O0O0000O000O0)}')#line:1173
                                        if OOO0OO000OOO0000O ['status']==500 :#line:1174
                                            print (f'【购买水滴】:购买水滴:{OOO0OO000OOO0000O["message"]}丨数量:{int(O0O0O0O0000O000O0)}')#line:1175
                                            OOO00OO00O00O00OO =OOO0OO000OOO0000O ["message"].split ('-')[1 ]#line:1176
                                            OOO000O0O00OOO0O0 =f'__{timi_new()}'#line:1177
                                            O00000OO00OO0OOO0 ={'source':'scsc','authorization':OOOO00OOOOOO0O0OO .token ,'timestamp':str (timi_new ()),'sign':sign (OOO000O0O00OOO0O0 ),'signstring':OOO000O0O00OOO0O0 ,'version':version ,'janalytics':'c167f56858dc424ee3d617c9','Host':'scsc.sc19319.com','User-Agent':'okhttp/4.9.1',}#line:1188
                                            O0OOOO0OOOO00000O =requests .request ('get',f'{host}/user',headers =O00000OO00OO0OOO0 ).json ()#line:1189
                                            if 'status'in O0OOOO0OOOO00000O :#line:1190
                                                if O0OOOO0OOOO00000O ['status']==200 :#line:1191
                                                    OOO0O00O0OOO0000O =O0OOOO0OOOO00000O ['data']['inner_id']#line:1192
                                                    if give_gold (OOO0O00O0OOO0000O ,float (OOO00OO00O00O00OO )+1 ):#line:1193
                                                        OOOO00OOOOOO0O0OO .energy ()#line:1194
                        break #line:1195
        except Exception as OO0O000OO0OO0OOOO :#line:1196
            print (OO0O000OO0OO0OOOO )#line:1197
def bundled_def ():#line:1199
    O0000OO0OOOO0O0O0 =['5570536','7750212','7911652','7911680','7805624']#line:1200
    return O0000OO0OOOO0O0O0 [random .randint (0 ,len (O0000OO0OOOO0O0O0 )-1 )]#line:1201
def version_of_the_validation ():#line:1205
    return str ((92 -56 )/10 )#line:1206
def sc2 ():#line:1208
    return "19319#$%^&*((*"#line:1209
def OO00OO0OO0OO00OO00o0 ():#line:1211
    return hashlib .md5 ((socket .gethostbyname (get_ip ())+socket .getfqdn (socket .gethostname ())).encode ('utf-8')).hexdigest ().upper ()#line:1212
def get_ip ():#line:1214
    return re .findall ('ip: (.*) ',requests .request ('get','https://dev.kdlapi.com/testproxy',headers ={"Accept-Encoding":"Gzip"}).text )[0 ]#line:1215
def gitee_validation ():#line:1217
    return requests .request ('get',f'{git}{kvkv()}/validation').json ()#line:1218
def gitee_edition ():#line:1220
    try :#line:1221
        return requests .get (f'{git}{kvkv()}/edition').json ()#line:1222
    except :#line:1223
        sys .exit (0 )#line:1224
def O000OO000O0O00OOO00 ():#line:1229
    try :#line:1230
        O00O00O000OO0O000 =gitee_edition ()#line:1231
        if version_of_the_validation ()<O00O00O000OO0O000 ['CityEarth']['edition']:#line:1232
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00O000OO0O000["CityEarth"]["edition"]}   ❌')#line:1233
            print (f'更新内容=>>{O00O00O000OO0O000["CityEarth"]["content"]}   🎉')#line:1234
        else :#line:1235
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O00O00O000OO0O000["CityEarth"]["edition"]}   ✅')#line:1236
            print (f'更新内容=>> {O00O00O000OO0O000["CityEarth"]["content"]}   🎉')#line:1237
    except Exception as O0OOOOO0O00OOOOO0 :#line:1238
        print (O0OOOOO0O00OOOOO0 )#line:1239
def sc3 ():#line:1241
    return "&^%$#@#RFGHJ%^KAfghfg"#line:1242
if __name__ =='__main__':#line:1246
    start ()#line:1247
