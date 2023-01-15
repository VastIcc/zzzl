# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
    import threading
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
cron: 12 */3 * * *
new Env('生城世朝')
项目地址  微信打开  http://share.sc19319.com/scsc/1932634
apk下载地址     https://sc19319.oss-cn-hangzhou.aliyuncs.com/scsc/test/1.9.3.1.S1.apk
抓取  http://test.scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1932634
版本  0.3
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(8, 12)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
git ='https://gitee.com'#line:1
host ='http://test.scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        update_the_validation ()#line:5
        O0OOOO0O00000O00O =os_qinglong ()#line:6
        print (f"==========共找到{len(O0OOOO0O00000O00O)}个账号==========")#line:7
        for OO00OOO0O0OOO0OOO in O0OOOO0O00000O00O :#line:8
            print (f"------------正在执行第{O0OOOO0O00000O00O.index(OO00OOO0O0OOO0OOO) + 1}个账号------------")#line:9
            OO0OOO0OO0OOO000O =CityEarth (OO00OOO0O0OOO0OOO )#line:10
            if OO0OOO0OO0OOO000O .base_info ():#line:12
                OO0OOO0OO0OOO000O .friends_invitation ()#line:16
                OO0OOO0OO0OOO000O .add_clover ()#line:20
                OO0OOO0OO0OOO000O .energy ()#line:22
                OO0OOO0OO0OOO000O .game_map ()#line:24
                OO0OOO0OO0OOO000O .synthetic ()#line:26
                OO0OOO0OO0OOO000O .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as O0O000OO00OO0O00O :#line:33
        print (O0O000OO00OO0O00O )#line:34
class CityEarth :#line:37
    def __init__ (O00000O00OO00OOO0 ,O0OO0O000O000O0OO ):#line:39
        try :#line:40
            O00000O00OO00OOO0 .token =O0OO0O000O000O0OO .split ('&')[0 ]#line:41
            O00000O00OO00OOO0 .innerId =O0OO0O000O000O0OO .split ('&')[1 ]#line:42
            O00000O00OO00OOO0 .headers ={'authorization':O00000O00OO00OOO0 .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as OOO0OOOOO0O0O000O :#line:47
            print ('变量格式错误')#line:48
    def base_info (OO0O0OO0OO0OO00O0 ):#line:51
        try :#line:52
            O0OOO000O00OO0OOO =requests .request ('get',f'{host}/api/user',headers =OO0O0OO0OO0OO00O0 .headers ).json ()#line:53
            if 'status'in O0OOO000O00OO0OOO :#line:55
                if O0OOO000O00OO0OOO ['status']==200 :#line:56
                    O00O00O0OO0OOOO00 =O0OOO000O00OO0OOO ['data']['nickname']#line:57
                    O000O0O0O0O0OOO0O =O0OOO000O00OO0OOO ['data']['inner_id']#line:58
                    OO0000OO0O0O00OO0 =O0OOO000O00OO0OOO ['data']['assets']['gold']#line:59
                    O000O000O000OOO00 =O0OOO000O00OO0OOO ['data']['level']#line:60
                    print (f'【账号信息】:昵称:{O00O00O0OO0OOOO00}丨ID:{str(O000O0O0O0O0OOO0O)[:3] + "**"+ str(O000O0O0O0O0OOO0O)[5:]}丨农作物等级:{O000O000O000OOO00}丨金种子:{str(OO0000OO0O0O00OO0).split(".")[0]}')#line:61
                if O0OOO000O00OO0OOO ['status']==401 :#line:62
                    return False #line:63
            return True #line:64
        except Exception as O0O0O0OOOOO0OO0OO :#line:65
            print (O0O0O0OOOOO0OO0OO )#line:66
    def crops_illustrated (O0OO0OOO00O000OOO ):#line:70
        O0OO0O0OO000O0OOO =requests .request ('get',f'{host}/api/game/crops/illustrated',headers =O0OO0OOO00O000OOO .headers ).json ()#line:71
        if 'status'in O0OO0O0OO000O0OOO :#line:73
            if O0OO0O0OO000O0OOO ['status']==200 :#line:74
                O0O000OO00O0O00OO =O0OO0O0OO000O0OOO ['data'][0 ]['crops']#line:75
                for OOOOOO000O0OOO000 in O0O000OO00O0O00OO :#line:76
                    if OOOOOO000O0OOO000 ['ill_clover_award']:#line:77
                        if float (OOOOOO000O0OOO000 ['ill_clover_award'])>1 :#line:78
                            if OOOOOO000O0OOO000 ['is_finish']:#line:79
                                if not OOOOOO000O0OOO000 ['is_getit']:#line:80
                                    OOO0OO00O00OOOO00 ={"award_level":OOOOOO000O0OOO000 ['level']}#line:81
                                    O0O0OO00000O0OO0O =requests .request ('post',f'{host}/api/game/crops/illustrated/award',headers =O0OO0OOO00O000OOO .headers ,json =OOO0OO00O00OOOO00 ).json ()#line:82
                                    if 'status'in O0O0OO00000O0OO0O :#line:83
                                        if O0O0OO00000O0OO0O ['status']==200 :#line:84
                                            O00O0O0OOOO0O0O00 =O0O0OO00000O0OO0O ['data']['ill_clover_award']#line:85
                                            print (f'【图鉴奖励】:领取{OOOOOO000O0OOO000["crop_name"]}成就丨奖励{O00O0O0OOOO0O0O00}种子成功')#line:86
                                        if O0O0OO00000O0OO0O ['status']==500 :#line:87
                                            print (f'【图鉴奖励】:{O0O0OO00000O0OO0O["message"]}')#line:88
    def watched_ad (O00OO00O00O00OOOO ):#line:91
        O000OOO000OOO000O =requests .request ('post',f'{host}/api/game/watched-ad',headers =O00OO00O00O00OOOO .headers ).json ()#line:92
        print (O000OOO000OOO000O )#line:93
    def user_ad (OOO0O000OO0OOOO00 ):#line:99
        O00O0O0O0O00O00OO =requests .request ('get',f'{host}/api/user/ad',headers =OOO0O000OO0OOOO00 .headers ).json ()#line:100
        if 'status'in O00O0O0O0O00O00OO :#line:102
            if O00O0O0O0O00O00OO ['status']==200 :#line:103
                O00OO00OO00OO0O0O =O00O0O0O0O00O00OO ['data']['max_time']#line:104
                O0OO0O0OOOO0OOO0O =O00O0O0O0O00O00OO ['data']['watch_time']#line:105
                O0OOO0OOOOO0O000O =O00O0O0O0O00O00OO ['data']['added_time']#line:106
                print (f'【获取种子】:获取种子剩余{O0OOO0OOOOO0O000O + O00OO00OO00OO0O0O - O0OO0O0OOOO0OOO0O}次丨好友提供:{O0OOO0OOOOO0O000O}次')#line:107
                if O00OO00OO00OO0O0O -O0OO0O0OOOO0OOO0O >0 or O0OOO0OOOOO0O000O >0 :#line:108
                    time .sleep (random .randint (16 ,19 ))#line:109
                    O00O00000O00OO0O0 =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =OOO0O000OO0OOOO00 .headers ).json ()#line:110
                    if 'status'in O00O00000O00OO0O0 :#line:112
                        if O00O00000O00OO0O0 ['status']==200 :#line:113
                            OOOO0O000OO00OO0O =O00O00000O00OO0O0 ['data']['silver']#line:114
                            print (f'【获取种子】:获得种子:{OOOO0O000OO00OO0O}')#line:115
                            return True #line:116
                        if O00O00000O00OO0O0 ['status']==500 :#line:117
                            O00O0OO0O000OOOOO =O00O00000O00OO0O0 ['message']#line:118
                            print (f'【获取种子】:{O00O0OO0O000OOOOO}')#line:119
                            return False #line:120
    def synthetic (OO0O00O00O0O0OOOO ):#line:123
        global id ,g #line:124
        try :#line:125
            while True :#line:126
                OOO0OO0OO00O0O0O0 =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0O00O00O0O0OOOO .headers ).json ()#line:127
                if 'status'in OOO0OO0OO00O0O0O0 :#line:129
                    if OOO0OO0OO00O0O0O0 ['status']==200 :#line:130
                        O0O0OOOOO0O000000 =OOO0OO0OO00O0O0O0 ['data']['cropList']#line:131
                        O0O00O0O0000O00O0 =OOO0OO0OO00O0O0O0 ['data']['gameCoreDataDBid']#line:132
                        OO00O000OO0000OOO =0 #line:133
                        for OOOOO000OO0000OO0 in O0O0OOOOO0O000000 :#line:134
                            if not OOOOO000OO0000OO0 :#line:135
                                O000O0OO000O0O00O ={"site":OO00O000OO0000OOO ,"crop_id":O0O00O0O0000O00O0 }#line:136
                                OOOOOO00OOO0OOOO0 =requests .request ('post',f'{host}/api/game/crops/buy',headers =OO0O00O00O0O0OOOO .headers ,data =O000O0OO000O0O00O ).json ()#line:137
                                if 'status'in OOOOOO00OOO0OOOO0 :#line:139
                                    if OOOOOO00OOO0OOOO0 ['status']==200 :#line:140
                                        if OOOOOO00OOO0OOOO0 ['message']=='种子数量不足':#line:141
                                            print (f'【购买合成】:{OOOOOO00OOO0OOOO0["message"]}')#line:142
                                            if not OO0O00O00O0O0OOOO .user_ad ():#line:143
                                                return False #line:144
                                        print (f'【购买合成】:购买农作物,位置{OO00O000OO0000OOO}')#line:145
                                    if OOOOOO00OOO0OOOO0 ['status']==500 :#line:146
                                        print (f'【购买合成】:{OOOOOO00OOO0OOOO0["message"]}')#line:147
                                        return False #line:148
                                time .sleep (random .randint (3 ,5 )/10 )#line:149
                            OO00O000OO0000OOO +=1 #line:150
                        O0OO0O00O0O00O0O0 =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0O00O00O0O0OOOO .headers ).json ()#line:151
                        OOOOO0OO0OOO0O0O0 =O0OO0O00O0O00O0O0 ['data']['cropList']#line:152
                        OOOO000OO000000OO =False #line:153
                        for OOOOO000OO0000OO0 in range (12 ):#line:154
                            id =OOOOO0OO0OOO0O0O0 [OOOOO000OO0000OO0 ]['level']#line:155
                            if id !=0 :#line:156
                                for O0O00O000O0O0OO0O in range (11 ):#line:157
                                    OO0000OO0O0O0O0O0 =O0O00O000O0O0OO0O +1 #line:158
                                    g =OOOOO0OO0OOO0O0O0 [OO0000OO0O0O0O0O0 ]['level']#line:159
                                    if id ==g :#line:160
                                        OO0OOOOOOOO000000 =O0O00O000O0O0OO0O +2 #line:161
                                        if OO0OOOOOOOO000000 ==OOOOO000OO0000OO0 +1 :#line:162
                                            pass #line:163
                                        else :#line:164
                                            time .sleep (random .randint (3 ,5 )/10 )#line:165
                                            O0O000O0000O00O0O =OOOOO000OO0000OO0 +1 #line:166
                                            OOO000OOOOO0OO0O0 ={"site":O0O000O0000O00O0O -1 ,"targetSite":OO0OOOOOOOO000000 -1 }#line:168
                                            OOO0O000OOO00O0OO =requests .request ('post',f'{host}/api/game/crops/move',headers =OO0O00O00O0O0OOOO .headers ,data =OOO000OOOOO0OO0O0 ).json ()#line:170
                                            if 'status'in OOO0O000OOO00O0OO :#line:172
                                                if OOO0O000OOO00O0OO ['status']==200 :#line:173
                                                    pass #line:174
                                            print ('【购买合成】:',O0O000O0000O00O0O ,OO0OOOOOOOO000000 ,'合成成功')#line:176
                                            OOOO000OO000000OO =True #line:177
                                    if OOOO000OO000000OO :#line:178
                                        break #line:179
                                if OOOO000OO000000OO :#line:180
                                    break #line:181
        except Exception as O0OO000O000OOO0O0 :#line:182
            OO0O00O00O0O0OOOO .synthetic ()#line:183
    def propsraffle (OOO0OO000O0OOO0O0 ):#line:187
        try :#line:188
            while True :#line:189
                O00OOO00OOOOOOO00 =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =OOO0OO000O0OOO0O0 .headers ).json ()#line:190
                if 'status'in O00OOO00OOOOOOO00 :#line:192
                    if O00OOO00OOOOOOO00 ['status']==200 :#line:193
                        O0OO0O0O0000000O0 =O00OOO00OOOOOOO00 ['data']['rows']#line:194
                        if O0OO0O0O0000000O0 ==5 or O0OO0O0O0000000O0 ==6 or O0OO0O0O0000000O0 ==7 :#line:195
                            OOO0000O00000OO0O =O00OOO00OOOOOOO00 ['data']['silver']#line:196
                            print (f'【转盘抽奖】:获得种子:{OOO0000O00000OO0O}')#line:197
                        if O0OO0O0O0000000O0 ==1 or O0OO0O0O0000000O0 ==2 or O0OO0O0O0000000O0 ==3 :#line:198
                            OOO0OO0OOOOOOO0O0 =O00OOO00OOOOOOO00 ['data']['clover']#line:199
                            print (f'【转盘抽奖】:获得三叶草:{OOO0OO0OOOOOOO0O0}')#line:200
                        if O0OO0O0O0000000O0 ==4 or O0OO0O0O0000000O0 ==8 :#line:201
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:202
                        if O0OO0O0O0000000O0 =='抽奖次数已用完':#line:206
                            OO0O00OO00OO00O0O =random .randint (160 ,190 )/10 #line:207
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{OO0O00OO00OO00O0O}秒获取抽奖机会')#line:208
                            time .sleep (OO0O00OO00OO00O0O )#line:209
                            OO0OOO0000OO00OOO =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =OOO0OO000O0OOO0O0 .headers ).json ()#line:210
                            if 'status'in OO0OOO0000OO00OOO :#line:212
                                if OO0OOO0000OO00OOO ['status']==200 :#line:213
                                    print (f'【转盘抽奖】:{OO0OOO0000OO00OOO["message"]}')#line:214
                                if OO0OOO0000OO00OOO ['status']==500 :#line:215
                                    print (f'【转盘抽奖】:{OO0OOO0000OO00OOO["message"]}')#line:216
                                    break #line:217
                            time .sleep (random .randint (10 ,15 )/10 )#line:218
                time .sleep (random .randint (8 ,15 )/10 )#line:219
        except Exception as O00O000O0OO00OOO0 :#line:220
            print (O00O000O0OO00OOO0 )#line:221
    def friends_invitation (O0OOO0O0OOO000OO0 ):#line:224
        try :#line:225
            O0000OOO0O00O00OO =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =O0OOO0O0OOO000OO0 .headers ).json ()#line:226
            if 'status'in O0000OOO0O00O00OO :#line:227
                if O0000OOO0O00O00OO ['status']==200 :#line:228
                    O000O0O0O0O0O00O0 =O0000OOO0O00O00OO ['data']['myInviteter']#line:229
                    if O000O0O0O0O0O00O0 :#line:230
                        OOO0OO0OOO00O00O0 =O000O0O0O0O0O00O0 ['user']['nickname']#line:231
                        print (f'【绑邀请码】:我的邀请人:{OOO0OO0OOO00O00O0}')#line:232
                    else :#line:233
                        if O0OOO0O0OOO000OO0 .innerId !='0':#line:234
                            print ('【绑邀请码】:绑定邀请码')#line:235
                            O0O0000OOOOOOOOOO ={"innerId":O0OOO0O0OOO000OO0 .innerId }#line:236
                            O0OO00OOO0000O00O =requests .request ('post',f'{host}/api/friends/my-invitation',headers =O0OOO0O0OOO000OO0 .headers ,data =O0O0000OOOOOOOOOO ).json ()#line:237
                            print (O0OO00OOO0000O00O )#line:238
                        else :#line:239
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:240
        except Exception as OOOOO000000000O00 :#line:241
            print (OOOOO000000000O00 )#line:242
    def add_clover (OOO0OOO0O00OO0O0O ):#line:246
        try :#line:247
            O0OOOOO00OO0OOOO0 =requests .request ('get',f'{host}/api/assets/clovers',headers =OOO0OOO0O00OO0O0O .headers ).json ()#line:248
            if 'status'in O0OOOOO00OO0OOOO0 :#line:250
                if O0OOOOO00OO0OOOO0 ['status']==200 :#line:251
                    O0O0O000O000OOO0O =O0OOOOO00OO0OOOO0 ['data']['clover']#line:252
                    O0OO00O000O00OO00 =O0OOOOO00OO0OOOO0 ['data']['used_clover']#line:253
                    O0OOOO000O00OOO00 =float (O0O0O000O000OOO0O )-float (O0OO00O000O00OO00 )#line:254
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OO00O000O00OO00}')#line:255
                    if O0OOOO000O00OOO00 >1 :#line:256
                        O000O00OO0OOOOOOO ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O0OOOO000O00OOO00 )}#line:257
                        OO0OO00O0OO000000 =requests .request ('post',f'{host}/api/lottery/add-stake',headers =OOO0OOO0O00OO0O0O .headers ,data =O000O00OO0OOOOOOO ).json ()#line:258
                        if 'status'in OO0OO00O0OO000000 :#line:260
                            if OO0OO00O0OO000000 ['status']==200 :#line:261
                                print (f'【参与抽奖】:添加三叶草:{OO0OO00O0OO000000["data"]}丨数量:{O0OOOO000O00OOO00}')#line:262
        except Exception as OOO0OO0000OO0OO00 :#line:263
            print (OOO0OO0000OO0OO00 )#line:264
    def energy (O00O00000OOO00O0O ):#line:267
        O00000000OOOOO0OO =requests .request ('get',f'{host}/api/energy/general',headers =O00O00000OOO00O0O .headers ).json ()#line:268
        if 'status'in O00000000OOOOO0OO :#line:270
            if O00000000OOOOO0OO ['status']==200 :#line:271
                O00O0O0O0O0000O00 =O00000000OOOOO0OO ['data']['ordinary_water_consumptions']#line:272
                if float (O00O0O0O0O0000O00 )<80 :#line:273
                    O000000O0000OO0O0 =99 -float (O00O0O0O0O0000O00 )#line:274
                    O000OO0OOOOOO0000 ={"fertilizer":str (O000000O0000OO0O0 ).split ('.')[0 ]}#line:275
                    OOOOO0OO0OOOO00O0 =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =O00O00000OOO00O0O .headers ,data =O000OO0OOOOOO0000 ).json ()#line:276
                    if 'status'in OOOOO0OO0OOOO00O0 :#line:278
                        if OOOOO0OO0OOOO00O0 ['status']==200 :#line:279
                            print (f'【购买肥料】:{OOOOO0OO0OOOO00O0["message"]}')#line:280
                OOOO00OO0O00OO0OO =O00000000OOOOO0OO ['data']['ordinary_water_consumptions']#line:281
                if float (OOOO00OO0O00OO0OO )<800 :#line:282
                    OOOOO0O00O000000O =999 -float (OOOO00OO0O00OO0OO )#line:283
                    O00OO00O000OOOO00 ={"water":str (OOOOO0O00O000000O ).split ('.')[0 ]}#line:284
                    OOOO0OO00O00OO000 =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =O00O00000OOO00O0O .headers ,data =O00OO00O000OOOO00 ).json ()#line:285
                    if 'status'in OOOO0OO00O00OO000 :#line:286
                        if OOOO0OO00O00OO000 ['status']==200 :#line:287
                            print (f'【购买水滴】:{OOOO0OO00O00OO000["message"]}')#line:288
    def game_map (OOO0000OO00OO0OO0 ):#line:292
        O0O0OO0OOOOO00OO0 =requests .request ('get',f'{host}/api/game/map',headers =OOO0000OO00OO0OO0 .headers ).json ()#line:293
        OOO0O000000OO0000 =0 #line:295
        if 'status'in O0O0OO0OOOOO00OO0 :#line:296
            if O0O0OO0OOOOO00OO0 ['status']==200 :#line:297
                O0OOO0O00000O00O0 =O0O0OO0OOOOO00OO0 ['data']['list'][0 ]['crops']#line:298
                for O000OO0OOO000O00O in O0OOO0O00000O00O0 :#line:300
                    O00OO0O0O000O00O0 =O000OO0OOO000O00O ['count']#line:302
                    if O00OO0O0O000O00O0 >0 :#line:303
                        OOO0O000000OO0000 +=1 #line:305
                if OOO0O000000OO0000 >8 :#line:307
                    print ('卖掉低级农作物')#line:308
                    O0OOOO0OO000O00O0 =O0OOO0O00000O00O0 [0 ]['id']#line:309
                    OO00OOOOO0O0OOO00 ={"crop_id":O0OOOO0OO000O00O0 ,"num":1 }#line:310
                    OO00000O0OOO0OOOO =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =OOO0000OO00OO0OO0 .headers ,data =OO00OOOOO0O0OOO00 ).json ()#line:311
                    if 'status'in OO00000O0OOO0OOOO :#line:313
                        if OO00000O0OOO0OOOO ['status']==200 :#line:314
                            print ('卖出成功')#line:315
def version_of_the_validation ():#line:319
    return str ((59 -56 )/10 )#line:320
def gitee_validation ():#line:322
    try :#line:323
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:324
    except Exception as O0OO00OO0OOOO0O00 :#line:325
        sys .exit (0 )#line:326
def update_the_validation ():#line:332
    try :#line:333
        OOOOO0O0O0O000OOO =gitee_validation ()#line:334
        if version_of_the_validation ()<OOOOO0O0O0O000OOO ['CityEarth']['edition']:#line:335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O0O0O000OOO["CityEarth"]["edition"]}   ❌')#line:336
            print (f'更新内容=>>{OOOOO0O0O0O000OOO["CityEarth"]["content"]}   👍')#line:337
        else :#line:338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOOOO0O0O0O000OOO["CityEarth"]["edition"]}   ✅')#line:339
            print (f'更新内容=>> {OOOOO0O0O0O000OOO["CityEarth"]["content"]}   👍')#line:340
    except Exception as O000OO0O0O0O0O0O0 :#line:341
        print (O000OO0O0O0O0O0O0 )#line:342
def os_qinglong ():#line:345
    if application in os .environ :#line:346
        OO000OOOO0OOOO000 =os .environ [application ].split ('\n')#line:347
        if len (OO000OOOO0OOOO000 )>0 :#line:348
            return OO000OOOO0OOOO000 #line:349
        else :#line:350
            print (f"{application}变量未启用")#line:351
            print ('脚本退出')#line:352
            sys .exit (1 )#line:353
    else :#line:354
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:355
        return os_built ()#line:356
def os_built ():#line:359
    if token :#line:360
        OO00O000OO00OOO00 =token .split ('\n')#line:361
        if len (OO00O000OO00OOO00 )>0 :#line:362
            return OO00O000OO00OOO00 #line:363
    else :#line:364
        print (f"内置变量为空")#line:365
        print ('脚本结束')#line:366
        sys .exit (0 )#line:367
if __name__ =='__main__':#line:370
    start ()#line:371
