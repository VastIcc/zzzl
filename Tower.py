# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
except Exception as E:
    t = re.findall("d '(.*?)'", str(E))[0]
    print(f'{t}依赖未安装')
    sys.exit()

"""
@ cron: 0,10 0,12 * * *
@ new Env('千层塔会员版')
@ 项目地址  https://qct.qitusky.cn/invite/?invite_code=1476
@ 抓取  https://qct.qitusky.cn 的ba-user-token值
@ 青龙变量 export qc_token="token&宝箱ID"   1普通宝箱 2白银宝箱 3黄金宝箱 4神秘宝箱 5炫彩宝箱  多号换行
@ 版本 0.3
"""
##################################配置区##################################
score = False   # 赠送记录
##################################配置区##################################

application = 'qc_token'  # 变量名
token = ''  #
##################################下面不要动##################################
host ='https://qct.qitusky.cn'#line:1
git ='https://gitee.com'#line:2
def os_qinglong ():#line:3
    if application in os .environ :#line:4
        O0OOO00O00000OOOO =os .environ [application ].split ('\n')#line:5
        if len (O0OOO00O00000OOOO )>0 :#line:6
            return O0OOO00O00000OOOO #line:7
        else :#line:8
            print (f"{application}变量未启用")#line:9
            print ('脚本退出')#line:10
            sys .exit (1 )#line:11
    else :#line:12
        print (f"{application}变量为空\n青龙在配置文件添加  export {application}='token&宝箱ID'\n尝试使用内置变量")#line:13
        return os_built ()#line:14
def os_built ():#line:17
    if token :#line:18
        O0OOOOO0OOO000OOO =token .split ('\n')#line:19
        if len (O0OOOOO0OOO000OOO )>0 :#line:20
            return O0OOOOO0OOO000OOO #line:21
    else :#line:22
        print (f"内置变量为空")#line:23
        print ('脚本结束')#line:24
        sys .exit (0 )#line:25
def gitee_validation ():#line:26
    try :#line:27
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:28
    except :#line:29
        sys .exit (0 )#line:30
def update_the_validation ():#line:33
    try :#line:34
        OOO000O0OO0O0O000 =gitee_validation ()#line:35
        if version_of_the_validation ()<OOO000O0OO0O0O000 ['Tower']['edition']:#line:36
            print (f'当前脚本名字: {OOO000O0OO0O0O000["Tower"]["text"]}')#line:37
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO000O0OO0O0O000["Tower"]["edition"]} 请及时更新至最新版  ❌')#line:38
            print (f'更新内容=>> {OOO000O0OO0O0O000["Tower"]["content"]}')#line:39
        else :#line:40
            print (f'当前脚本名字: {OOO000O0OO0O0O000["Tower"]["text"]}')#line:41
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OOO000O0OO0O0O000["Tower"]["edition"]}   ✅')#line:42
            print (f'更新内容=>> {OOO000O0OO0O0O000["Tower"]["content"]}')#line:43
    except Exception as O0OO0O0O0OOOO0O0O :#line:44
        print (O0OO0O0O0OOOO0O0O )#line:45
class Template :#line:48
    def __init__ (OOOO0OOO00O0O0O00 ,OO0OO0OO0O0O00OO0 ):#line:50
        try :#line:51
            OOOO0OOO00O0O0O00 .token =OO0OO0OO0O0O00OO0 .split ('&')[0 ]#line:52
            OOOO0OOO00O0O0O00 .box =OO0OO0OO0O0O00OO0 .split ('&')[1 ]#line:53
            OOOO0OOO00O0O0O00 .headers ={'user-agent':'Dart/2.18 (dart:io)','app-versions':'1.1.6','accept-encoding':'gzip','host':'qct.qitusky.cn','resource':'android','content-type':'application/x-www-form-urlencoded;charset=utf-8','ba-user-token':OOOO0OOO00O0O0O00 .token ,'server':'true','phone-type':'android',}#line:65
        except Exception as OOO0OO0000O0O00O0 :#line:66
            print ('变量格式错误')#line:67
    def base_info (OO0OOOOO0OO00O00O ):#line:70
        try :#line:71
            O00O0O00O0OOO0000 =requests .request ('post',f'{host}/api/User/info',headers =OO0OOOOO0OO00O00O .headers ).json ()#line:72
            if 'code'in O00O0O00O0OOO0000 :#line:74
                if O00O0O00O0OOO0000 ['code']==1 :#line:75
                    O0OO0O00O00O0O00O =O00O0O00O0OOO0000 ['data']['nickname']#line:76
                    O0OO0O0OO0000O000 =O00O0O00O0OOO0000 ['data']['id']#line:77
                    O0OO0O0O000O0000O =O00O0O00O0OOO0000 ['data']['score']#line:78
                    print (f'【账号信息】:昵称:{O0OO0O00O00O0O00O[:6]}丨ID:{O0OO0O0OO0000O000}丨金币:{str(O0OO0O0O000O0000O)[:5]}')#line:79
                if O00O0O00O0OOO0000 ['code']==302 :#line:80
                    return False #line:81
            return True #line:82
        except Exception as OOO0OOO0O0000000O :#line:83
            print (OOO0OOO0O0000000O )#line:84
    def playInfo (O0OOOOOO0000O0OOO ):#line:87
        try :#line:88
            O0O0OO0OO00OO0000 =requests .request ('post',f'{host}/api/Game/playInfo',headers =O0OOOOOO0000O0OOO .headers ).json ()#line:89
            if 'code'in O0O0OO0OO00OO0000 :#line:91
                if O0O0OO0OO00OO0000 ['code']==1 :#line:92
                    O0O0000O00OOOO000 =O0O0OO0OO00OO0000 ['data']['play_tier']#line:93
                    OOOOO0O00O000O0OO =O0O0OO0OO00OO0000 ['data']['play_tier_need_money']#line:94
                    OO0000O000O0O00O0 =O0O0OO0OO00OO0000 ['data']['user_money']#line:95
                    OO0OOOO0OOOOO0O00 =O0O0OO0OO00OO0000 ['data']['play_finish_money']#line:96
                    print (f'【参与闯关】:层数:{O0O0000O00OOOO000}丨闯关花费:{OOOOO0O00O000O0OO}丨预计获得:{OO0OOOO0OOOOO0O00}')#line:97
                    if float (OOOOO0O00O000O0OO )<float (OO0000O000O0O00O0 ):#line:98
                        O0OOOOOO0000O0OOO .Game_index ('1')#line:100
                    else :#line:101
                        O0OOOOOO0000O0OOO .Game_index ('2')#line:102
        except Exception as OOOOO0OOO0OO0OO0O :#line:104
            print (OOOOO0OOO0OO0OO0O )#line:105
    def setAutoPlay (OOOOOO00OO0O0OO00 ):#line:108
        try :#line:109
            O0000O000O0O00000 ={'state':'1'}#line:112
            O0OO000O0OO00OOO0 =requests .request ('post',f'{host}/api/Game/setAutoPlay',headers =OOOOOO00OO0O0OO00 .headers ,data =O0000O000O0O00000 ).json ()#line:113
            if 'code'in O0OO000O0OO00OOO0 :#line:115
                if O0OO000O0OO00OOO0 ['code']==1 :#line:116
                    print (f'【自动闯关】:{O0OO000O0OO00OOO0["msg"]}')#line:117
                if O0OO000O0OO00OOO0 ['code']==0 :#line:118
                    print (f'【自动闯关】:{O0OO000O0OO00OOO0["msg"]}')#line:119
        except Exception as O00O0O0OOO0000OOO :#line:120
            print (O00O0O0OOO0000OOO )#line:121
    def Game_index (OO0O00OOOO0O0OO0O ,O000O00OO00OO00O0 ):#line:124
        try :#line:125
            OO000OOOO0OOOO0OO =requests .request ('post',f'{host}/api/Game/index',headers =OO0O00OOOO0O0OO0O .headers ).json ()#line:126
            if 'code'in OO000OOOO0OOOO0OO :#line:128
                if OO000OOOO0OOOO0OO ['code']==1 :#line:129
                    if OO000OOOO0OOOO0OO ['data']['is_auto_play']:#line:130
                        OO000OO0OO000O00O ='✅'#line:131
                    else :#line:132
                        OO000OO0OO000O00O ='❌'#line:133
                    if OO000OOOO0OOOO0OO ['data']['is_game_ing']:#line:135
                        OO00O00O0O0000OO0 ='✅'#line:136
                    else :#line:137
                        OO00O00O0O0000OO0 ='❌'#line:138
                    if OO000OOOO0OOOO0OO ['data']['is_vip']:#line:139
                        OO000OOO0000O00OO ='✅'#line:140
                    else :#line:141
                        OO000OOO0000O00OO ='❌'#line:142
                    if '正在闯关'in OO000OOOO0OOOO0OO ['data']['npc_hint']:#line:143
                        OO0O00000OOO0000O =OO000OOOO0OOOO0OO ['data']['npc_hint'][:8 ]#line:144
                    else :#line:145
                        OO0O00000OOO0000O =OO000OOOO0OOOO0OO ['data']['npc_hint'][:5 ]#line:146
                    print (f'【游戏状态】:自动:{OO000OO0OO000O00O}丨闯关:{OO00O00O0O0000OO0}丨VIP:{OO000OOO0000O00OO}丨{OO0O00000OOO0000O}')#line:147
                    if not OO000OOOO0OOOO0OO ['data']['is_auto_play']:#line:148
                        if O000O00OO00OO00O0 =='1':#line:149
                            OO0O00OOOO0O0OO0O .setAutoPlay ()#line:150
        except Exception as O0000OO00OOOOO000 :#line:151
            print (O0000OO00OOOOO000 )#line:152
    def LuckyBox (OO0OOO0OO0O0000OO ):#line:156
        try :#line:157
            OO00O0OOO00OO0OO0 =requests .request ('post',f'{host}/api/LuckyBox/index',headers =OO0OOO0OO0O0000OO .headers ).json ()#line:158
            if 'code'in OO00O0OOO00OO0OO0 :#line:160
                if OO00O0OOO00OO0OO0 ['code']==1 :#line:161
                    O0O0000000O00O0OO =OO00O0OOO00OO0OO0 ['data']['debris']#line:162
                    O0OOO00O0O00O0000 =OO00O0OOO00OO0OO0 ['data']['is_draw']#line:163
                    print (f'【幸运宝箱】:碎片:{str(O0O0000000O00O0OO).split(".")[0]}丨当前设置开启宝箱ID:{OO0OOO0OO0O0000OO.box}')#line:164
                    if not O0OOO00O0O00O0000 :#line:165
                        O0OO00O00OO000OOO =requests .request ('post',f'{host}/api/LuckyBox/debrisDraw',headers =OO0OOO0OO0O0000OO .headers ).json ()#line:166
                        if 'code'in O0OO00O00OO000OOO :#line:168
                            if O0OO00O00OO000OOO ['code']==1 :#line:169
                                OO0OOO0OO00OOO0O0 =O0OO00O00OO000OOO ['data']['nub']#line:170
                                print (f'【领取碎片】:获得:{OO0OOO0OO00OOO0O0}')#line:171
                    for OOO0O000OO00OO00O in OO00O0OOO00OO0OO0 ['data']['box_list']:#line:172
                        O0OO0OOOO0O000OO0 =OOO0O000OO00OO00O ['id']#line:174
                        OO000000000OO0O00 =OOO0O000OO00OO00O ['name']#line:175
                        OOOOOOOOOO00OOO0O =OOO0O000OO00OO00O ['inventory']#line:176
                        OOOOOO0O00O000O0O =OOO0O000OO00OO00O ['need_debris']#line:177
                        if float (O0OO0OOOO0O000OO0 )==float (OO0OOO0OO0O0000OO .box ):#line:178
                            print (f'【幸运宝箱】:名称:{OO000000000OO0O00}丨需要碎片:{OOOOOO0O00O000O0O}丨剩余:{OOOOOOOOOO00OOO0O}')#line:179
                            if float (O0O0000000O00O0OO )>=float (OOOOOO0O00O000O0O ):#line:180
                                O0O00000000OO0OO0 ={'id':OO0OOO0OO0O0000OO .box }#line:181
                                OO0000OOO0O00000O =requests .request ('post',f'{host}/api/LuckyBox/exchange',headers =OO0OOO0OO0O0000OO .headers ,data =O0O00000000OO0OO0 ).json ()#line:182
                                if 'code'in OO0000OOO0O00000O :#line:184
                                    if OO0000OOO0O00000O ['code']==1 :#line:185
                                        print (f'【兑换宝箱】:{OO0000OOO0O00000O["msg"]}丨获得{OO0000OOO0O00000O["data"]["name"]}')#line:186
        except Exception as O0O00OO0OO0O0OOO0 :#line:187
            print (O0O00OO0OO0O0OOO0 )#line:188
    def score_record (OO0O0O0000OO0OOO0 ):#line:191
        OOOOO00OOO0OO00OO ={'page':'1','limit':'15','type':'2'}#line:192
        OOO000O00O0O0OOOO =requests .request ('post',f'{host}/api/Score/record',headers =OO0O0O0000OO0OOO0 .headers ,data =OOOOO00OOO0OO00OO ).json ()#line:193
        if 'code'in OOO000O00O0O0OOOO :#line:195
            if OOO000O00O0O0OOOO ['code']==1 :#line:196
                OO0O0000O0OO000O0 =OOO000O00O0O0OOOO ['data']['record_list']#line:197
                if OO0O0000O0OO000O0 :#line:198
                    for OO000OO0OOO000O0O in OO0O0000O0OO000O0 :#line:199
                        OOOO00O00O0OOO0O0 =OO000OO0OOO000O0O ['user_id']#line:200
                        O0O00OO00OO00O0O0 =OO000OO0OOO000O0O ['money']#line:201
                        O0O0OOO000OOO0OOO =OO000OO0OOO000O0O ['create_time']#line:202
                        O00OOOO00OO00OOO0 =OO000OO0OOO000O0O ['nickname']#line:203
                        print (f'【赠送记录】:昵称:{O00OOOO00OO00OOO0}丨ID:{OOOO00O00O0OOO0O0}丨金额:{O0O00OO00OO00O0O0}丨时间:{O0O0OOO000OOO0OOO[5:16]}')#line:204
def start ():#line:205
    try :#line:206
        update_the_validation ()#line:207
        OOO00O0000OO0OOOO =os_qinglong ()#line:208
        print (f"==========共找到{len(OOO00O0000OO0OOOO)}个账号==========")#line:209
        for OO000000OOOOOOOOO in OOO00O0000OO0OOOO :#line:210
            print (f"------------正在执行第{OOO00O0000OO0OOOO.index(OO000000OOOOOOOOO) + 1}个账号------------")#line:211
            O0OO00000O0O0O0O0 =Template (OO000000OOOOOOOOO )#line:212
            if O0OO00000O0O0O0O0 .base_info ():#line:214
                O0OO00000O0O0O0O0 .LuckyBox ()#line:216
                O0OO00000O0O0O0O0 .playInfo ()#line:218
                if score :#line:219
                    O0OO00000O0O0O0O0 .score_record ()#line:221
                time .sleep (random .randint (1 ,3 ))#line:223
            else :#line:224
                print ('token失效')#line:225
    except Exception as OO0000OOOOO0OOOOO :#line:226
        print (OO0000OOOOO0OOOOO )#line:227
def version_of_the_validation ():#line:229
    return str ((59 -56 )/10 )#line:230
if __name__ =='__main__':#line:233
    start ()#line:234
