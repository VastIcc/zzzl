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
cron: 12 */12 * * *
new Env('生城世朝')
项目地址  微信打开  http://share.sc19319.com/scsc/1932634
抓取  http://test.scsc.sc19319.com 的authorization值
青龙变量 export ce_token="authorization&绑定邀请码"   不绑定填 0   多号换行
我的邀请码是  1932634
版本  0.1
"""
application = 'ce_token'  # 变量名
token = ''


time_xx = random.randint(1, 2)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行

##################################下面不要动##################################
host ='http://test.scsc.sc19319.com'#line:2
def start ():#line:3
    try :#line:4
        O00OOO0OO0O0OOOOO =os_qinglong ()#line:5
        print (f"==========共找到{len(O00OOO0OO0O0OOOOO)}个账号==========")#line:6
        for OOO0OOOOOO0OO000O in O00OOO0OO0O0OOOOO :#line:7
            print (f"------------正在执行第{O00OOO0OO0O0OOOOO.index(OOO0OOOOOO0OO000O) + 1}个账号------------")#line:8
            OO0O000000O00OO00 =CityEarth (OOO0OOOOOO0OO000O )#line:9
            def OO0O00OOO0O0OO00O ():#line:11
                if OO0O000000O00OO00 .base_info ():#line:13
                    OO0O000000O00OO00 .friends_invitation ()#line:15
                    OO0O000000O00OO00 .propsraffle ()#line:17
                    OO0O000000O00OO00 .add_clover ()#line:19
                    OO0O000000O00OO00 .energy ()#line:21
                    OO0O000000O00OO00 .game_map ()#line:23
                    OO0O000000O00OO00 .synthetic ()#line:25
                else :#line:28
                    print ('token失效')#line:29
            O00OO0OO000O0O00O =threading .Thread (target =OO0O00OOO0O0OO00O )#line:30
            O00OO0OO000O0O00O .start ()#line:31
            time .sleep (time_xx )#line:32
    except Exception as OOO000O00OOOOO0O0 :#line:33
        print (OOO000O00OOOOO0O0 )#line:34
class CityEarth :#line:37
    def __init__ (O00OOOO0O00O0O0O0 ,OOO0O0O00OO000000 ):#line:39
        try :#line:40
            O00OOOO0O00O0O0O0 .token =OOO0O0O00OO000000 .split ('&')[0 ]#line:41
            O00OOOO0O00O0O0O0 .innerId =OOO0O0O00OO000000 .split ('&')[1 ]#line:42
            O00OOOO0O00O0O0O0 .headers ={'authorization':O00OOOO0O00O0O0O0 .token ,'Host':'test.scsc.sc19319.com'}#line:46
        except Exception as OOO0O0O0O000OOO0O :#line:47
            print ('变量格式错误')#line:48
    def base_info (OOOOO0OO00O00O0O0 ):#line:51
        try :#line:52
            O0O0O0O0OOO0O00O0 =requests .request ('get',f'{host}/api/user',headers =OOOOO0OO00O00O0O0 .headers ).json ()#line:53
            if 'status'in O0O0O0O0OOO0O00O0 :#line:55
                if O0O0O0O0OOO0O00O0 ['status']==200 :#line:56
                    OOOOO0OOO0O0O00OO =O0O0O0O0OOO0O00O0 ['data']['nickname']#line:57
                    OOOOO0OOOOOOOOOOO =O0O0O0O0OOO0O00O0 ['data']['inner_id']#line:58
                    O0O0O0O0000000OO0 =O0O0O0O0OOO0O00O0 ['data']['assets']['gold']#line:59
                    print (f'【账号信息】:昵称:{OOOOO0OOO0O0O00OO}丨ID:{OOOOO0OOOOOOOOOOO}丨金种子:{str(O0O0O0O0000000OO0).split(".")[0]}')#line:60
                if O0O0O0O0OOO0O00O0 ['status']==401 :#line:61
                    return False #line:62
            return True #line:63
        except Exception as O0OOO0OOOOOO00OO0 :#line:64
            print (O0OOO0OOOOOO00OO0 )#line:65
    def synthetic (O0000000OOO0OOO00 ):#line:69
        global id ,g #line:70
        try :#line:71
            while True :#line:72
                OO0O0OOO00O0OO0O0 =requests .request ('get',f'{host}/api/game/getAllData',headers =O0000000OOO0OOO00 .headers ).json ()#line:73
                if 'status'in OO0O0OOO00O0OO0O0 :#line:75
                    if OO0O0OOO00O0OO0O0 ['status']==200 :#line:76
                        O000000O00O00OO00 =OO0O0OOO00O0OO0O0 ['data']['cropList']#line:77
                        OO00O0O0OOO0OO0O0 =OO0O0OOO00O0OO0O0 ['data']['gameCoreDataDBid']#line:78
                        O000O00000OO00O0O =0 #line:79
                        for O00O000O000O00O00 in O000000O00O00OO00 :#line:80
                            if not O00O000O000O00O00 :#line:81
                                OOOOOO000O0000OO0 ={"site":O000O00000OO00O0O ,"crop_id":OO00O0O0OOO0OO0O0 }#line:82
                                OO00OOO00O0O0OOO0 =requests .request ('post',f'{host}/api/game/crops/buy',headers =O0000000OOO0OOO00 .headers ,data =OOOOOO000O0000OO0 ).json ()#line:83
                                if 'status'in OO00OOO00O0O0OOO0 :#line:85
                                    if OO00OOO00O0O0OOO0 ['status']==200 :#line:86
                                        print (f'【购买合成】:购买农作物,位置{O000O00000OO00O0O}')#line:87
                                    if OO00OOO00O0O0OOO0 ['status']==500 :#line:88
                                        print (f'【购买合成】:{OO00OOO00O0O0OOO0["message"]}')#line:89
                                        return False #line:90
                                time .sleep (random .randint (3 ,5 )/10 )#line:91
                            O000O00000OO00O0O +=1 #line:92
                        O00000O0O00O00OOO =requests .request ('get',f'{host}/api/game/getAllData',headers =O0000000OOO0OOO00 .headers ).json ()#line:93
                        O00O0000OOOO0000O =O00000O0O00O00OOO ['data']['cropList']#line:94
                        OO0OO000OOO0OO000 =False #line:95
                        for O00O000O000O00O00 in range (12 ):#line:96
                            id =O00O0000OOOO0000O [O00O000O000O00O00 ]['level']#line:97
                            if id !=0 :#line:98
                                for OOO0O000000OO0000 in range (11 ):#line:99
                                    O000OO0O00OOOO0OO =OOO0O000000OO0000 +1 #line:100
                                    g =O00O0000OOOO0000O [O000OO0O00OOOO0OO ]['level']#line:101
                                    if id ==g :#line:102
                                        O0000OO0OO00O0O00 =OOO0O000000OO0000 +2 #line:103
                                        if O0000OO0OO00O0O00 ==O00O000O000O00O00 +1 :#line:104
                                            pass #line:105
                                        else :#line:106
                                            time .sleep (random .randint (3 ,5 )/10 )#line:107
                                            OOO00OOOO0O0OOO0O =O00O000O000O00O00 +1 #line:108
                                            OO0OOOOOOO0O0O000 ={"site":OOO00OOOO0O0OOO0O -1 ,"targetSite":O0000OO0OO00O0O00 -1 }#line:110
                                            OO000O0OOOOO00OOO =requests .request ('post',f'{host}/api/game/crops/move',headers =O0000000OOO0OOO00 .headers ,data =OO0OOOOOOO0O0O000 ).json ()#line:112
                                            if 'status'in OO000O0OOOOO00OOO :#line:114
                                                if OO000O0OOOOO00OOO ['status']==200 :#line:115
                                                    pass #line:116
                                            print ('【购买合成】:',OOO00OOOO0O0OOO0O ,O0000OO0OO00O0O00 ,'合成成功')#line:118
                                            OO0OO000OOO0OO000 =True #line:119
                                    if OO0OO000OOO0OO000 :#line:120
                                        break #line:121
                                if OO0OO000OOO0OO000 :#line:122
                                    break #line:123
        except Exception as O00O0000OO0O00000 :#line:124
            O0000000OOO0OOO00 .synthetic ()#line:125
    def propsraffle (OOO0OOO0O0000OOO0 ):#line:129
        try :#line:130
            while True :#line:131
                OOOO0000OO0OOOO00 =requests .request ('get',f'{host}/api/propsraffle/lucky',headers =OOO0OOO0O0000OOO0 .headers ).json ()#line:132
                if 'status'in OOOO0000OO0OOOO00 :#line:134
                    if OOOO0000OO0OOOO00 ['status']==200 :#line:135
                        O0OOOOO00O000OOO0 =OOOO0000OO0OOOO00 ['data']['rows']#line:136
                        if 'get_game_lucky_LargeTurntables'in OOOO0000OO0OOOO00 ['data']:#line:137
                            O0O0OO0OO0O0O000O =OOOO0000OO0OOOO00 ['data']['get_game_lucky_LargeTurntables']#line:138
                            print (f'【转盘抽奖】:剩余抽奖次数:{O0O0OO0OO0O0O000O}')#line:139
                        if O0OOOOO00O000OOO0 =='抽奖次数已用完':#line:140
                            print ('【转盘抽奖】:抽奖次数已用完')#line:141
                            time .sleep (random .randint (160 ,190 )/10 )#line:142
                            O00000000OO00O00O =requests .request ('get',f'{host}/api/propsraffle/lucky/adverti/restore',headers =OOO0OOO0O0000OOO0 .headers ).json ()#line:143
                            if 'status'in O00000000OO00O00O :#line:145
                                if O00000000OO00O00O ['status']==200 :#line:146
                                    print (f'【转盘抽奖】:{O00000000OO00O00O["message"]}')#line:147
                                if O00000000OO00O00O ['status']==500 :#line:148
                                    print (f'【转盘抽奖】:{O00000000OO00O00O["message"]}')#line:149
                                    break #line:150
                time .sleep (random .randint (8 ,15 )/10 )#line:151
        except Exception as OO0OO00000O0000OO :#line:152
            print (OO0OO00000O0000OO )#line:153
    def friends_invitation (O0OO0000O00O00OOO ):#line:156
        try :#line:157
            O0OO0000OOOOO00OO =requests .request ('get','http://test.scsc.sc19319.com/api/friends',headers =O0OO0000O00O00OOO .headers ).json ()#line:158
            if 'status'in O0OO0000OOOOO00OO :#line:159
                if O0OO0000OOOOO00OO ['status']==200 :#line:160
                    O0O0O00O0OO0000OO =O0OO0000OOOOO00OO ['data']['myInviteter']#line:161
                    if O0O0O00O0OO0000OO :#line:162
                        O0OOOO000OOOOOO00 =O0O0O00O0OO0000OO ['user']['nickname']#line:163
                        print (f'【绑邀请码】:我的邀请人:{O0OOOO000OOOOOO00}')#line:164
                    else :#line:165
                        if O0OO0000O00O00OOO .innerId !='0':#line:166
                            print ('【绑邀请码】:绑定邀请码')#line:167
                            OOO0O0OO0O0OOO0OO ={"innerId":O0OO0000O00O00OOO .innerId }#line:168
                            O0O000O0O00OOO00O =requests .request ('post',f'{host}/api/friends/my-invitation',headers =O0OO0000O00O00OOO .headers ,data =OOO0O0OO0O0OOO0OO ).json ()#line:169
                            print (O0O000O0O00OOO00O )#line:170
                        else :#line:171
                            print (f'【绑邀请码】:设置不绑定邀请码')#line:172
        except Exception as O0OO00O00OO0O00O0 :#line:173
            print (O0OO00O00OO0O00O0 )#line:174
    def add_clover (O0OOOO00O0OOOO000 ):#line:178
        try :#line:179
            O0000OO000OO000OO =requests .request ('get',f'{host}/api/assets/clovers',headers =O0OOOO00O0OOOO000 .headers ).json ()#line:180
            if 'status'in O0000OO000OO000OO :#line:182
                if O0000OO000OO000OO ['status']==200 :#line:183
                    OO00O00OOOO0000OO =O0000OO000OO000OO ['data']['clover']#line:184
                    O0O000OOOO00O000O =O0000OO000OO000OO ['data']['used_clover']#line:185
                    OOO0000OO0OO00OOO =float (OO00O00OOOO0000OO )-float (O0O000OOOO00O000O )#line:186
                    print (f'【参与抽奖】:参与抽奖的三叶草:{O0O000OOOO00O000O}')#line:187
                    if OOO0000OO0OO00OOO >1 :#line:188
                        OOOO0OOO00OOO0O0O ={"lotteryId":"13f02ff5-f8db-4ddc-9e9a-3d328a211fff","quantity":OOO0000OO0OO00OOO }#line:189
                        OOOO000O0OOOO0OOO =requests .request ('post','http://test.scsc.sc19319.com/api/lottery/add-stake',headers =O0OOOO00O0OOOO000 .headers ,data =OOOO0OOO00OOO0O0O ).json ()#line:191
                        if 'status'in OOOO000O0OOOO0OOO :#line:193
                            if OOOO000O0OOOO0OOO ['status']==200 :#line:194
                                print (f'【参与抽奖】:添加三叶草:{OOOO000O0OOOO0OOO["data"]}丨数量:{OOO0000OO0OO00OOO}')#line:195
        except Exception as O0OO0000000OOO00O :#line:196
            print (O0OO0000000OOO00O )#line:197
    def energy (OO0OO0OOO0OO0O00O ):#line:200
        OOO00O0OOOOO0OO0O =requests .request ('get',f'{host}/api/energy/general',headers =OO0OO0OOO0OO0O00O .headers ).json ()#line:201
        if 'status'in OOO00O0OOOOO0OO0O :#line:203
            if OOO00O0OOOOO0OO0O ['status']==200 :#line:204
                OO0OO0O0000O0000O =OOO00O0OOOOO0OO0O ['data']['ordinary_water_consumptions']#line:205
                if float (OO0OO0O0000O0000O )<80 :#line:206
                    OOO0OO0OOO000O0OO =99 -float (OO0OO0O0000O0000O )#line:207
                    O0O0OO0O0O0OO0000 ={"fertilizer":str (OOO0OO0OOO000O0OO ).split ('.')[0 ]}#line:208
                    O0OO0O000O0OOOO0O =requests .request ('post',f'{host}/api/energy/general/buy/fertilizer',headers =OO0OO0OOO0OO0O00O .headers ,data =O0O0OO0O0O0OO0000 ).json ()#line:209
                    if 'status'in O0OO0O000O0OOOO0O :#line:211
                        if O0OO0O000O0OOOO0O ['status']==200 :#line:212
                            print (f'【购买肥料】:{O0OO0O000O0OOOO0O["message"]}')#line:213
                O00O0000OOO000000 =OOO00O0OOOOO0OO0O ['data']['ordinary_water_consumptions']#line:214
                if float (O00O0000OOO000000 )<800 :#line:215
                    OOOO000OO0O0OO0O0 =999 -float (O00O0000OOO000000 )#line:216
                    O00OO00OO0O0O00O0 ={"water":str (OOOO000OO0O0OO0O0 ).split ('.')[0 ]}#line:217
                    O000000O00O000000 =requests .request ('post',f'{host}/api/energy/general/buy/water',headers =OO0OO0OOO0OO0O00O .headers ,data =O00OO00OO0O0O00O0 ).json ()#line:218
                    if 'status'in O000000O00O000000 :#line:219
                        if O000000O00O000000 ['status']==200 :#line:220
                            print (f'【购买水滴】:{O000000O00O000000["message"]}')#line:221
    def game_map (O0OOOOOOOO0OO000O ):#line:225
        OOO0OO000OO0000O0 =requests .request ('get',f'{host}/api/game/map',headers =O0OOOOOOOO0OO000O .headers ).json ()#line:226
        OO0OO0O000000O0O0 =0 #line:228
        if 'status'in OOO0OO000OO0000O0 :#line:229
            if OOO0OO000OO0000O0 ['status']==200 :#line:230
                O00000OO000OO0OOO =OOO0OO000OO0000O0 ['data']['list'][0 ]['crops']#line:231
                for OOO0O0OOO00O00000 in O00000OO000OO0OOO :#line:233
                    O0OO00OOO00000000 =OOO0O0OOO00O00000 ['count']#line:235
                    if O0OO00OOO00000000 >0 :#line:236
                        OO0OO0O000000O0O0 +=1 #line:238
                if OO0OO0O000000O0O0 >8 :#line:240
                    print ('卖掉低级农作物')#line:241
                    O0OO0O000OO0OO0O0 =O00000OO000OO0OOO [0 ]['id']#line:242
                    O0O0000OO0O00000O ={"crop_id":O0OO0O000OO0OO0O0 ,"num":1 }#line:243
                    OOO0O00OO0OO0O00O =requests .request ('post',f'{host}/api/game/crops/sellForGold',headers =O0OOOOOOOO0OO000O .headers ,data =O0O0000OO0O00000O ).json ()#line:244
                    if 'status'in OOO0O00OO0OO0O00O :#line:246
                        if OOO0O00OO0OO0O00O ['status']==200 :#line:247
                            print ('卖出成功')#line:248
def os_qinglong ():#line:252
    if application in os .environ :#line:253
        OO0O0O0OOOOOO0OO0 =os .environ [application ].split ('\n')#line:254
        if len (OO0O0O0OOOOOO0OO0 )>0 :#line:255
            return OO0O0O0OOOOOO0OO0 #line:256
        else :#line:257
            print (f"{application}变量未启用")#line:258
            print ('脚本退出')#line:259
            sys .exit (1 )#line:260
    else :#line:261
        print (f"{application}变量为空\n尝试使用内置变量")#line:262
        return os_built ()#line:263
def os_built ():#line:266
    if token :#line:267
        O00O0O00OO0OOO0O0 =token .split ('\n')#line:268
        if len (O00O0O00OO0OOO0O0 )>0 :#line:269
            return O00O0O00OO0OOO0O0 #line:270
    else :#line:271
        print (f"内置变量为空")#line:272
        print ('脚本退出')#line:273
        sys .exit (0 )#line:274
if __name__ =='__main__':#line:277
    start ()#line:278
