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
        O0O000OOO00000O0O =os_qinglong ()#line:6
        print (f"==========共找到{len(O0O000OOO00000O0O)}个账号==========")#line:7
        for O00O0OOO0O0OO0O0O in O0O000OOO00000O0O :#line:8
            print (f"------------正在执行第{O0O000OOO00000O0O.index(O00O0OOO0O0OO0O0O) + 1}个账号------------")#line:9
            OOO00O0O00OO0000O =CityEarth (O00O0OOO0O0OO0O0O )#line:10
            if OOO00O0O00OO0000O .base_info ():#line:12
                OOO00O0O00OO0000O .friends_invitation ()#line:16
                OOO00O0O00OO0000O .add_clover ()#line:20
                OOO00O0O00OO0000O .energy ()#line:22
                OOO00O0O00OO0000O .game_map ()#line:24
                OOO00O0O00OO0000O .synthetic ()#line:26
                OOO00O0O00OO0000O .crops_illustrated ()#line:28
            else :#line:29
                print ('token失效')#line:30
            time .sleep (time_xx )#line:32
    except Exception as OO00O0OO0O00OOOO0 :#line:33
        print (OO00O0OO0O00OOOO0 )#line:34
class CityEarth :#line:37
    def __init__ (O000O00OO0OOOO0O0 ,OO00O00OOOO0O00OO ):#line:39
        try :#line:40
            O000O00OO0OOOO0O0 .token =OO00O00OOOO0O00OO .split ('&')[0 ]#line:41
            O000O00OO0OOOO0O0 .innerId =OO00O00OOOO0O00OO .split ('&')[1 ]#line:42
            O000O00OO0OOOO0O0 .headers ={'authorization':O000O00OO0OOOO0O0 .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as O0O0OO0OO0OO00O0O :#line:47
            print ('变量格式错误')#line:48
    def base_info (OO00OO00O00O00OOO ):#line:51
        try :#line:52
            OOOOOOOOO0O0OO000 =requests .request ('get',f'{host}/api/user',headers =OO00OO00O00O00OOO .headers ).json ()#line:53
            if 'status'in OOOOOOOOO0O0OO000 :#line:55
                if OOOOOOOOO0O0OO000 ['status']==200 :#line:56
                    O0OO000O0OO0O0000 =OOOOOOOOO0O0OO000 ['data']['nickname']#line:57
                    OOOO0O0O0OOOO0O00 =OOOOOOOOO0O0OO000 ['data']['inner_id']#line:58
                    OOO0000O0O0OOOO0O =OOOOOOOOO0O0OO000 ['data']['assets']['gold']#line:59
                    OOO0000OO0OOOOOO0 =OOOOOOOOO0O0OO000 ['data']['level']#line:60
                    print (f'【账号信息】:昵称:{O0OO000O0OO0O0000}丨ID:{str(OOOO0O0O0OOOO0O00)[:3] + "**"+ str(OOOO0O0O0OOOO0O00)[5:]}丨农作物等级:{OOO0000OO0OOOOOO0}丨金种子:{str(OOO0000O0O0OOOO0O).split(".")[0]}')#line:61
                if OOOOOOOOO0O0OO000 ['status']==401 :#line:62
                    return False #line:63
            return True #line:64
        except Exception as O00O00OOO00OOO000 :#line:65
            print (O00O00OOO00OOO000 )#line:66
    def crops_illustrated (OO000OOO0O000OOO0 ):#line:70
        OOOO0O0O0OO000OOO =requests .request ('get',f'{host}/api/game/crops/illustrated',headers =OO000OOO0O000OOO0 .headers ).json ()#line:71
        if 'status'in OOOO0O0O0OO000OOO :#line:73
            if OOOO0O0O0OO000OOO ['status']==200 :#line:74
                OOOO000OOO0O0OO00 =OOOO0O0O0OO000OOO ['data'][0 ]['crops']#line:75
                for OO00O0O00OO0O0O00 in OOOO000OOO0O0OO00 :#line:76
                    if OO00O0O00OO0O0O00 ['ill_clover_award']:#line:77
                        if float (OO00O0O00OO0O0O00 ['ill_clover_award'])>1 :#line:78
                            if OO00O0O00OO0O0O00 ['is_finish']:#line:79
                                if not OO00O0O00OO0O0O00 ['is_getit']:#line:80
                                    O000O0OO0OOO0O000 ={"award_level":OO00O0O00OO0O0O00 ['level']}#line:81
                                    O0O00OOO00O00OO00 =requests .request ('post',f'{host}/api/game/crops/illustrated/award',headers =OO000OOO0O000OOO0 .headers ,json =O000O0OO0OOO0O000 ).json ()#line:82
                                    if 'status'in O0O00OOO00O00OO00 :#line:83
                                        if O0O00OOO00O00OO00 ['status']==200 :#line:84
                                            OO0OOO000000000OO =O0O00OOO00O00OO00 ['data']['ill_clover_award']#line:85
                                            print (f'【图鉴奖励】:领取{OO00O0O00OO0O0O00["crop_name"]}成就丨奖励{OO0OOO000000000OO}种子成功')#line:86
                                        if O0O00OOO00O00OO00 ['status']==500 :#line:87
                                            print (f'【图鉴奖励】:{O0O00OOO00O00OO00["message"]}')#line:88
    def watched_ad (O000O0O00OOO0O0O0 ):#line:91
        O0O0O000O0O000O00 =requests .request ('post',f'{host}/api/game/watched-ad',headers =O000O0O00OOO0O0O0 .headers ).json ()#line:92
        print (O0O0O000O0O000O00 )#line:93
    def user_ad (O0OO0OOOO0000OO0O ):#line:99
        OO00OO0O0000O00OO =requests .request ('get',f'{host}/api/user/ad',headers =O0OO0OOOO0000OO0O .headers ).json ()#line:100
        if 'status'in OO00OO0O0000O00OO :#line:102
            if OO00OO0O0000O00OO ['status']==200 :#line:103
                OOOOO000OO000OO0O =OO00OO0O0000O00OO ['data']['max_time']#line:104
                OO0OO0OOO0O0O00OO =OO00OO0O0000O00OO ['data']['watch_time']#line:105
                O0O0O0O0OO00O0OO0 =OO00OO0O0000O00OO ['data']['added_time']#line:106
                print (f'【获取种子】:获取种子剩余{O0O0O0O0OO00O0OO0 + OOOOO000OO000OO0O - OO0OO0OOO0O0O00OO}次丨好友提供:{O0O0O0O0OO00O0OO0}次')#line:107
                if O0O0O0O0OO00O0OO0 +OOOOO000OO000OO0O -OO0OO0OOO0O0O00OO >0 :#line:108
                    time .sleep (random .randint (16 ,19 ))#line:109
                    O0OO0000OOOOOOO00 =requests .request ('post',f'{host}/api/game/watched-ad-forSilver',headers =O0OO0OOOO0000OO0O .headers ).json ()#line:110
                    if 'status'in O0OO0000OOOOOOO00 :#line:112
                        if O0OO0000OOOOOOO00 ['status']==200 :#line:113
                            OOO000000OOOOO0OO =O0OO0000OOOOOOO00 ['data']['silver']#line:114
                            print (f'【获取种子】:获得种子:{OOO000000OOOOO0OO}')#line:115
                            return True #line:116
                        if O0OO0000OOOOOOO00 ['status']==500 :#line:117
                            OO000O0OO0OOO0OO0 =O0OO0000OOOOOOO00 ['message']#line:118
                            print (f'【获取种子】:{OO000O0OO0OOO0OO0}')#line:119
                            return False #line:120
    def synthetic (OO0OOOO000OO00O0O ):#line:123
        global id ,g #line:124
        try :#line:125
            while True :#line:126
                OOO0O00OOOOO0O0O0 =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0OOOO000OO00O0O .headers ).json ()#line:127
                if 'status'in OOO0O00OOOOO0O0O0 :#line:129
                    if OOO0O00OOOOO0O0O0 ['status']==200 :#line:130
                        O000OOOOOO00OOO0O =OOO0O00OOOOO0O0O0 ['data']['cropList']#line:131
                        OOOOOO0OO0OOO00OO =OOO0O00OOOOO0O0O0 ['data']['gameCoreDataDBid']#line:132
                        O00O000OO000OOOOO =0 #line:133
                        for O0000O000O0OOO0OO in O000OOOOOO00OOO0O :#line:134
                            if not O0000O000O0OOO0OO :#line:135
                                OO000OO000O0O00OO ={"site":O00O000OO000OOOOO ,"crop_id":OOOOOO0OO0OOO00OO }#line:136
                                O0000O00O0000O0O0 =requests .request ('post',f'{host}/api/game/crops/buy',headers =OO0OOOO000OO00O0O .headers ,data =OO000OO000O0O00OO ).json ()#line:137
                                if 'status'in O0000O00O0000O0O0 :#line:139
                                    if O0000O00O0000O0O0 ['status']==200 :#line:140
                                        if O0000O00O0000O0O0 ['message']=='种子数量不足':#line:141
                                            print (f'【购买合成】:{O0000O00O0000O0O0["message"]}')#line:142
                                            if not OO0OOOO000OO00O0O .user_ad ():#line:143
                                                return False #line:144
                                        print (f'【购买合成】:购买农作物,位置{O00O000OO000OOOOO}')#line:145
                                    if O0000O00O0000O0O0 ['status']==500 :#line:146
                                        print (f'【购买合成】:{O0000O00O0000O0O0["message"]}')#line:147
                                        return False #line:148
                                time .sleep (random .randint (3 ,5 )/10 )#line:149
                            O00O000OO000OOOOO +=1 #line:150
                        O0O00OOO0O0OO0000 =requests .request ('get',f'{host}/api/game/getAllData',headers =OO0OOOO000OO00O0O .headers ).json ()#line:151
                        OOOO00O000OO00000 =O0O00OOO0O0OO0000 ['data']['cropList']#line:152
                        OO0OO00O0OOOO0O0O =False #line:153
                        for O0000O000O0OOO0OO in range (12 ):#line:154
                            id =OOOO00O000OO00000 [O0000O000O0OOO0OO ]['level']#line:155
                            if id !=0 :#line:156
                                for O0OO00OOO000O0000 in range (11 ):#line:157
                                    O0O00OO00O00OO00O =O0OO00OOO000O0000 +1 #line:158
                                    g =OOOO00O000OO00000 [O0O00OO00O00OO00O ]['level']#line:159
                                    if id ==g :#line:160
                                        OOOOOOOOOO00OOOO0 =O0OO00OOO000O0000 +2 #line:161
                                        if OOOOOOOOOO00OOOO0 ==O0000O000O0OOO0OO +1 :#line:162
                                            pass #line:163
                                        else :#line:164
                                            time .sleep (random .randint (3 ,5 )/10 )#line:165
                                            O0OO00O0000O00OOO =O0000O000O0OOO0OO +1 #line:166
                                            OOO0OOO0000O00O0O ={"site":O0OO00O0000O00OOO -1 ,"targetSite":OOOOOOOOOO00OOOO0 -1 }#line:168
                                            OO00O00O0OO0OOO0O =requests .request ('post',f'{host}/api/game/crops/move',headers =OO0OOOO000OO00O0O .headers ,data =OOO0OOO0000O00O0O ).json ()#line:170
                                            if 'status'in OO00O00O0OO0OOO0O :#line:172
                                                if OO00O00O0OO0OOO0O ['status']==200 :#line:173
                                                    pass #line:174
                                            print ('【购买合成】:',O0OO00O0000O00OOO ,OOOOOOOOOO00OOOO0 ,'合成成功')#line:176
                                            OO0OO00O0OOOO0O0O =True #line:177
                                    if OO0OO00O0OOOO0O0O :#line:178
                                        break #line:179
                                if OO0OO00O0OOOO0O0O :#line:180
                                    break #line:181
        except Exception as OOOO00O0OO0OO0000 :#line:182
            OO0OOOO000OO00O0O .synthetic ()#line:183
    def propsraffle (OO00OOOOOOOOO0OO0 ):#line:187
        try :#line:188
            while True :#line:189
                OOO0OO0O0OOOO0OOO =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =OO00OOOOOOOOO0OO0 .headers ).json ()#line:190
                if 'status'in OOO0OO0O0OOOO0OOO :#line:192
                    if OOO0OO0O0OOOO0OOO ['status']==200 :#line:193
                        O0OOOO00OO0OOO000 =OOO0OO0O0OOOO0OOO ['data']['rows']#line:194
                        if O0OOOO00OO0OOO000 ==5 or O0OOOO00OO0OOO000 ==6 or O0OOOO00OO0OOO000 ==7 :#line:195
                            OO0OOOO0O0O0O0OOO =OOO0OO0O0OOOO0OOO ['data']['silver']#line:196
                            print (f'【转盘抽奖】:获得种子:{OO0OOOO0O0O0O0OOO}')#line:197
                        if O0OOOO00OO0OOO000 ==1 or O0OOOO00OO0OOO000 ==2 or O0OOOO00OO0OOO000 ==3 :#line:198
                            OOOO0O000OO00OO0O =OOO0OO0O0OOOO0OOO ['data']['clover']#line:199
                            print (f'【转盘抽奖】:获得三叶草:{OOOO0O000OO00OO0O}')#line:200
                        if O0OOOO00OO0OOO000 ==4 or O0OOOO00OO0OOO000 ==8 :#line:201
                            print (f'【转盘抽奖】:翻倍奖励 未写')#line:202
                        if O0OOOO00OO0OOO000 =='抽奖次数已用完':#line:206
                            O000OO000OOO0O0O0 =random .randint (160 ,190 )/10 #line:207
                            print (f'【转盘抽奖】:抽奖次数已用完丨等待{O000OO000OOO0O0O0}秒获取抽奖机会')#line:208
                            time .sleep (O000OO000OOO0O0O0 )#line:209
                            O0OO00OO0000OO0O0 =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =OO00OOOOOOOOO0OO0 .headers ).json ()#line:210
                            if 'status'in O0OO00OO0000OO0O0 :#line:212
                                if O0OO00OO0000OO0O0 ['status']==200 :#line:213
                                    print (f'【转盘抽奖】:{O0OO00OO0000OO0O0["message"]}')#line:214
                                if O0OO00OO0000OO0O0 ['status']==500 :#line:215
                                    print (f'【转盘抽奖】:{O0OO00OO0000OO0O0["message"]}')#line:216
                                    break #line:217
                            time .sleep (random .randint (10 ,15 )/10 )#line:218
                time .sleep (random .randint (8 ,15 )/10 )#line:219
        except Exception as OOO0000OO0OOO0O0O :#line:220
            print (OOO0000OO0OOO0O0O )#line:221
    def friends_invitation (O0O0OO0O000000O0O ):#line:224
        try :#line:225
            O0O000O0OO0O00O0O =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =O0O0OO0O000000O0O .headers ).json ()#line:226
            if 'status'in O0O000O0OO0O00O0O :#line:227
                if O0O000O0OO0O00O0O ['status']==200 :#line:228
                    O0O0OO0OO00O0OO0O =O0O000O0OO0O00O0O ['data']['myInviteter']#line:229
                    if O0O0OO0OO00O0OO0O :#line:230
                        OOOO000O000OO0OO0 =O0O0OO0OO00O0OO0O ['user']['nickname']#line:231
                        print (f'【绑邀请码】:我的邀请人:{OOOO000O000OO0OO0}')#line:232
                    else :#line:233
                        if O0O0OO0O000000O0O .innerId !='0':#line:234
                            print ('【绑邀请码】:绑定邀请码')#line:235
                            O0O0OO0OO0O0O00O0 ={"innerId":O0O0OO0O000000O0O .innerId }#line:236
                            OOOO0O0OOO00O00O0 =requests .request ('post',f'{host}/api/friends/my-invitation',headers =O0O0OO0O000000O0O .headers ,data =O0O0OO0OO0O0O00O0 ).json ()#line:237
                            print (OOOO0O0OOO00O00O0 )#line:238
                        else :#line:239
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:240
        except Exception as OO00O0O000O0000O0 :#line:241
            print (OO00O0O000O0000O0 )#line:242
    def add_clover (O0O0O000OOOO000OO ):#line:246
        try :#line:247
            O0OOO00O000OO00O0 =requests .request ('get',f'{host}/api/assets/clovers',headers =O0O0O000OOOO000OO .headers ).json ()#line:248
            if 'status'in O0OOO00O000OO00O0 :#line:250
                if O0OOO00O000OO00O0 ['status']==200 :#line:251
                    O0O0000O0O0O000OO =O0OOO00O000OO00O0 ['data']['clover']#line:252
                    O0OOO00OO0OOO0000 =O0OOO00O000OO00O0 ['data']['used_clover']#line:253
                    O000000O0O0000000 =float (O0O0000O0O0O000OO )-float (O0OOO00OO0OOO0000 )#line:254
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0OOO00OO0OOO0000}')#line:255
                    if O000000O0O0000000 >1 :#line:256
                        O0O000000O0OO00O0 ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":int (O000000O0O0000000 )}#line:257
                        OO0000O0OOOO00OO0 =requests .request ('post',f'{host}/api/lottery/add-stake',headers =O0O0O000OOOO000OO .headers ,data =O0O000000O0OO00O0 ).json ()#line:258
                        if 'status'in OO0000O0OOOO00OO0 :#line:260
                            if OO0000O0OOOO00OO0 ['status']==200 :#line:261
                                print (f'【参与抽奖】:添加三叶草:{OO0000O0OOOO00OO0["data"]}丨数量:{O000000O0O0000000}')#line:262
        except Exception as O000O00OO0OO0O000 :#line:263
            print (O000O00OO0OO0O000 )#line:264
    def energy (OOO00O0000000OO00 ):#line:267
        OO0O00O00OO0OOOO0 =requests .request ('get',f'{host}/api/energy/general',headers =OOO00O0000000OO00 .headers ).json ()#line:268
        if 'status'in OO0O00O00OO0OOOO0 :#line:270
            if OO0O00O00OO0OOOO0 ['status']==200 :#line:271
                OO00O0OO0OO0OO0OO =OO0O00O00OO0OOOO0 ['data']['ordinary_water_consumptions']#line:272
                if float (OO00O0OO0OO0OO0OO )<80 :#line:273
                    OOO0OO000O0OOO0O0 =99 -float (OO00O0OO0OO0OO0OO )#line:274
                    O0OOO0OO0O0O0O00O ={"fertilizer":str (OOO0OO000O0OOO0O0 ).split ('.')[0 ]}#line:275
                    OO0000OO0O000O00O =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =OOO00O0000000OO00 .headers ,data =O0OOO0OO0O0O0O00O ).json ()#line:276
                    if 'status'in OO0000OO0O000O00O :#line:278
                        if OO0000OO0O000O00O ['status']==200 :#line:279
                            print (f'【购买肥料】:{OO0000OO0O000O00O["message"]}')#line:280
                O0O0O0O0O0O0OOOO0 =OO0O00O00OO0OOOO0 ['data']['ordinary_water_consumptions']#line:281
                if float (O0O0O0O0O0O0OOOO0 )<800 :#line:282
                    O0O0OOOOOOO00OO0O =999 -float (O0O0O0O0O0O0OOOO0 )#line:283
                    OOOOOO000OOO000O0 ={"water":str (O0O0OOOOOOO00OO0O ).split ('.')[0 ]}#line:284
                    O00O000O0OOO0O0OO =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =OOO00O0000000OO00 .headers ,data =OOOOOO000OOO000O0 ).json ()#line:285
                    if 'status'in O00O000O0OOO0O0OO :#line:286
                        if O00O000O0OOO0O0OO ['status']==200 :#line:287
                            print (f'【购买水滴】:{O00O000O0OOO0O0OO["message"]}')#line:288
    def game_map (O00OOO0OO0O0OOOOO ):#line:292
        OOOO0OO0O0OO00000 =requests .request ('get',f'{host}/api/game/map',headers =O00OOO0OO0O0OOOOO .headers ).json ()#line:293
        OOO0OO0OO00O0OO00 =0 #line:295
        if 'status'in OOOO0OO0O0OO00000 :#line:296
            if OOOO0OO0O0OO00000 ['status']==200 :#line:297
                OOOOOOOO00O0O00OO =OOOO0OO0O0OO00000 ['data']['list'][0 ]['crops']#line:298
                for O0OOO0O0O00000000 in OOOOOOOO00O0O00OO :#line:300
                    OO0000000O00000O0 =O0OOO0O0O00000000 ['count']#line:302
                    if OO0000000O00000O0 >0 :#line:303
                        OOO0OO0OO00O0OO00 +=1 #line:305
                if OOO0OO0OO00O0OO00 >8 :#line:307
                    print ('卖掉低级农作物')#line:308
                    OOOO00OO0O00OOO00 =OOOOOOOO00O0O00OO [0 ]['id']#line:309
                    O0O0O0OO00OO0O0OO ={"crop_id":OOOO00OO0O00OOO00 ,"num":1 }#line:310
                    OOO0O0O00OOOO00O0 =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =O00OOO0OO0O0OOOOO .headers ,data =O0O0O0OO00OO0O0OO ).json ()#line:311
                    if 'status'in OOO0O0O00OOOO00O0 :#line:313
                        if OOO0O0O00OOOO00O0 ['status']==200 :#line:314
                            print ('卖出成功')#line:315
def version_of_the_validation ():#line:319
    return str ((59 -56 )/10 )#line:320
def gitee_validation ():#line:322
    try :#line:323
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:324
    except Exception as OO00O000OOO00O0OO :#line:325
        sys .exit (0 )#line:326
def update_the_validation ():#line:332
    try :#line:333
        O0OO00O00O00OO000 =gitee_validation ()#line:334
        if version_of_the_validation ()<O0OO00O00O00OO000 ['CityEarth']['edition']:#line:335
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00O00O00OO000["CityEarth"]["edition"]}   ❌')#line:336
            print (f'更新内容=>>{O0OO00O00O00OO000["CityEarth"]["content"]}   👍')#line:337
        else :#line:338
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OO00O00O00OO000["CityEarth"]["edition"]}   ✅')#line:339
            print (f'更新内容=>> {O0OO00O00O00OO000["CityEarth"]["content"]}   👍')#line:340
    except Exception as O00OO0O00OOO00000 :#line:341
        print (O00OO0O00OOO00000 )#line:342
def os_qinglong ():#line:345
    if application in os .environ :#line:346
        OO00OOOO0O0O00OO0 =os .environ [application ].split ('\n')#line:347
        if len (OO00OOOO0O0O00OO0 )>0 :#line:348
            return OO00OOOO0O0O00OO0 #line:349
        else :#line:350
            print (f"{application}变量未启用")#line:351
            print ('脚本退出')#line:352
            sys .exit (1 )#line:353
    else :#line:354
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='authorization&绑定邀请码'\n尝试使用内置变量")#line:355
        return os_built ()#line:356
def os_built ():#line:359
    if token :#line:360
        O0OO00O0000000O00 =token .split ('\n')#line:361
        if len (O0OO00O0000000O00 )>0 :#line:362
            return O0OO00O0000000O00 #line:363
    else :#line:364
        print (f"内置变量为空")#line:365
        print ('脚本结束')#line:366
        sys .exit (0 )#line:367
if __name__ =='__main__':#line:370
    start ()#line:371
