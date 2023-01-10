# coding: utf-8
try:
    import re
    import os
    import sys
    import time
    import requests
    import random
    import datetime
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖未安装')
    sys.exit()


"""
cron: 12 */3 * * *
new Env('拾米游0.3')
青龙变量 export smytoken="token@赠送游票ID@True"   
第三个参数是开启赠送功能     多号换行
版本0.3
"""


application = 'smytoken'    # 变量名
bundled = True              # 是否绑定邀请码
count_mew = 10              # 默认每次赠送10      10的整数手续费最划算
token = ''                  # 调试token



# 绑定上级ID  随机绑就多填   不需要1000
def bundled_def():
    bundled_id_new = ['31676', '31689', '31815', '31817', '31818', '32056', '32896', '33151', '33153', '33158', '33160', '33162', '41727']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]

#####################################################下面不要动#####################################################
cumulative_ticket =0 #line:1
host ='https://api.shimiyou.com'#line:2
git ='https://gitee.com'#line:3
mobile =0 #line:4
def start ():#line:5
    try :#line:6
        if update_the_validation ():#line:7
            OO0000O0O0000O0OO =os_qinglong ()#line:8
            print (f"==========共找到{len(OO0000O0O0000O0OO)}个账号==========")#line:9
            for OO0O0O0000000O000 in OO0000O0O0000O0OO :#line:10
                print (f"------------正在执行第{OO0000O0O0000O0OO.index(OO0O0O0000000O000) + 1}个账号------------")#line:11
                OOO0OOO0OO0O0O0O0 =SwimUpM (OO0O0O0000000O000 )#line:12
                if OOO0OOO0OO0O0O0O0 .base_info ():#line:14
                    if bundled :#line:15
                        OOO0OOO0OO0O0O0O0 .friend_center ()#line:17
                    OOO0OOO0OO0O0O0O0 .lottery_activities ()#line:19
                    OOO0OOO0OO0O0O0O0 .user_lottery_activity_records ()#line:21
                    OOO0OOO0OO0O0O0O0 .lottery_center_index ()#line:23
                    if OOO0OOO0OO0O0O0O0 .tickets :#line:24
                        OOO0OOO0OO0O0O0O0 .tickets_give ()#line:26
                    time .sleep (random .randint (8 ,15 ))#line:27
                else :#line:28
                    print ('token失效')#line:29
            print (f"------------所有账号运行完毕正在统计每天收益------------")#line:30
            print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:31
    except Exception as O00OOOO00OOOO0O00 :#line:32
        print (O00OOOO00OOOO0O00 )#line:33
class SwimUpM :#line:35
    def __init__ (OO0OOO000O000O00O ,O0OOOO00OO000OOO0 ):#line:37
        try :#line:38
            OO0OOO000O000O00O .giving =O0OOOO00OO000OOO0 .split ("@")[1 ]#line:39
            OO0OOO000O000O00O .tickets =O0OOOO00OO000OOO0 .split ("@")[2 ]#line:40
            OO0OOO000O000O00O .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':O0OOOO00OO000OOO0 .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com',}#line:41
        except Exception as O000O0O000OO00000 :#line:42
            print ('变量格式错误')#line:43
    def base_info (OOO0O0O0O0000O0O0 ):#line:46
        global mobile #line:47
        try :#line:48
            O0OOO00O0000OO000 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =OOO0O0O0O0000O0O0 .headers ).json ()#line:49
            if 'code'in O0OOO00O0000OO000 :#line:51
                return False #line:52
            if 'mobile'in O0OOO00O0000OO000 :#line:53
                if O0OOO00O0000OO000 ['mobile']:#line:54
                    mobile =O0OOO00O0000OO000 ['mobile']#line:55
                else :#line:56
                    mobile ='None'#line:57
            if 'id'in O0OOO00O0000OO000 :#line:58
                OOOOO0000O000O0O0 =O0OOO00O0000OO000 ['nick_name']#line:59
                OO0O000OO000OOO00 =O0OOO00O0000OO000 ['card_no']#line:60
                O000O00OOOO0O00OO =str (OO0O000OO000OOO00 )[4 :5 ]+'**'+str (OO0O000OO000OOO00 )[7 :]#line:61
                O0O0OOO0O00OOOO0O =O0OOO00O0000OO000 ['ticket']['count']#line:62
                try :#line:63
                    if reversed (O0O0OOO0O00OOOO0O )!=0 :#line:64
                        O0O0OOO0O00OOOO0O =str (O0O0OOO0O00OOOO0O ).split ('.')[0 ]#line:65
                    else :#line:66
                        O0O0OOO0O00OOOO0O =0 #line:67
                except :#line:68
                    O0O0OOO0O00OOOO0O =0 #line:69
                print (f'【账号信息】：ID:{O000O00OOOO0O00OO}丨昵称:{OOOOO0000O000O0O0[:7]}丨游票:{O0O0OOO0O00OOOO0O}')#line:70
                O0O0OOO00O0000OO0 =O0OOO00O0000OO000 ['avatar']['url']#line:71
                if O0O0OOO00O0000OO0 :#line:72
                    if 'NUokiQDoKCFD'in O0O0OOO00O0000OO0 :#line:73
                        O0OOO0OO0O0O00O00 =re .findall ('/NUokiQDoKCFD(.*?).jpg',O0OOO00O0000OO000 ['avatar']['url'])[0 ].split ('NUokiQDoKCFD')[0 ].split ('-')[0 ]#line:74
                        OOO0OOO00O000OO00 =(datetime .datetime .now ()-datetime .datetime (int (O0OOO0OO0O0O00O00 [:4 ]),int (O0OOO0OO0O0O00O00 [4 :6 ]),int (O0OOO0OO0O0O00O00 [6 :8 ]))).days #line:75
                        print (f'【注册绑定】：注册:{O0OOO0OO0O0O00O00[:4]}-{O0OOO0OO0O0O00O00[4:6]}-{O0OOO0OO0O0O00O00[6:8]}丨距今:{OOO0OOO00O000OO00}天丨绑定:{mobile[7:]}')#line:76
                        return True #line:77
                    if 'avatar'in O0O0OOO00O0000OO0 :#line:78
                        O0OOO0OO0O0O00O00 =re .findall ('/avatar(.*?).jpg',O0OOO00O0000OO000 ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')[0 ]#line:79
                        OOO0OOO00O000OO00 =(datetime .datetime .now ()-datetime .datetime (int (O0OOO0OO0O0O00O00 [:4 ]),int (O0OOO0OO0O0O00O00 [4 :6 ]),int (O0OOO0OO0O0O00O00 [6 :8 ]))).days #line:80
                        print (f'【注册绑定】：注册:{O0OOO0OO0O0O00O00[:4]}-{O0OOO0OO0O0O00O00[4:6]}-{O0OOO0OO0O0O00O00[6:8]}丨距今:{OOO0OOO00O000OO00}天丨绑定:{mobile[7:]}')#line:81
                        return True #line:82
            return True #line:83
        except Exception as O00OOOO00OOO0O000 :#line:84
            print (O00OOOO00OOO0O000 )#line:85
    def friend_center (O00OO000OOO000000 ):#line:89
        OO0OOO0O0O00000O0 =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =O00OO000OOO000000 .headers ).json ()#line:90
        if 'parent_user'in OO0OOO0O0O00000O0 :#line:91
            if OO0OOO0O0O00000O0 ['parent_user']:#line:92
                pass #line:93
            else :#line:94
                OOO0OO0000O00O0OO ={"id":bundled_def ()}#line:95
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =O00OO000OOO000000 .headers ,data =OOO0OO0000O00O0OO ).json ()#line:96
    def user_lottery_activity_records (O0000O0O0O0O0O000 ):#line:99
        global cumulative_ticket #line:100
        O00O0000OOOO00OOO =0 #line:101
        O000OO00OO0OOO00O =0 #line:102
        try :#line:103
            OOO0OO00O0OO0O0O0 =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =O0000O0O0O0O0O000 .headers ).json ()#line:104
            if 'user_lottery_activity_records'in OOO0OO00O0OO0O0O0 :#line:105
                for OOO0OO0000OOO00OO in OOO0OO00O0OO0O0O0 ['user_lottery_activity_records']:#line:106
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==OOO0OO0000OOO00OO ['lottery_activity_id']:#line:107
                        O00O0000OOOO00OOO =OOO0OO0000OOO00OO ['bet_on']#line:108
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==OOO0OO0000OOO00OO ['lottery_activity_id']:#line:109
                        O000OO00OO0OOO00O =OOO0OO0000OOO00OO ['bet_on']#line:110
                print (f'【参与抽奖】：普通奖券:{O000OO00OO0OOO00O}张丨高级奖券:{O00O0000OOOO00OOO}张')#line:111
            if 'lottery_activity'in OOO0OO00O0OO0O0O0 :#line:112
                for OOO0OO0000OOO00OO in OOO0OO00O0OO0O0O0 ['lottery_activity']:#line:113
                    if OOO0OO0000OOO00OO ['topic']=='普通奖券抽游票':#line:114
                        OOOO0OO00O0OO0OO0 =OOO0OO0000OOO00OO ['sum_bet_on']#line:115
                        OO00O000O00O00OOO =2880 *34 /OOOO0OO00O0OO0OO0 *O000OO00OO0OOO00O #line:116
                        cumulative_ticket +=OO00O000O00O00OOO #line:117
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(OO00O000O00O00OOO)[:5]}')#line:118
                    if OOO0OO0000OOO00OO ['topic']=='高级奖券抽游票':#line:119
                        OOOO0OO00O0OO0OO0 =OOO0OO0000OOO00OO ['sum_bet_on']#line:120
                        OO00O000O00O00OOO =2880 *313 /OOOO0OO00O0OO0OO0 *O00O0000OOOO00OOO #line:121
                        cumulative_ticket +=OO00O000O00O00OOO #line:122
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(OO00O000O00O00OOO)[:5]}')#line:123
        except Exception as O0000O00O0O000O00 :#line:125
            print (O0000O00O0O000O00 )#line:126
    def tickets_give (O0O0O0O0O0O0OO0O0 ):#line:130
        try :#line:131
            O0000000O00OOOOO0 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O0O0O0O0O0O0OO0O0 .headers ).json ()#line:132
            O00O00O00OO0OOOOO =str (O0000000O00OOOOO0 ['card_no'])[4 :]#line:133
            if O0O0O0O0O0O0OO0O0 .giving !=O00O00O00OO0OOOOO :#line:134
                OO0O000OO0OO0O0OO =O0000000O00OOOOO0 ['ticket']['count']#line:135
                if float (OO0O000OO0OO0O0OO )==0 :#line:136
                    print ('【赠送游票】：账号初始化中')#line:137
                    return True #line:138
                OO0OO00O0O00OO000 =str (OO0O000OO0OO0O0OO ).split ('.')[0 ]#line:139
                if int (OO0OO00O0O00OO000 )>count_mew :#line:140
                    OO0O0OOOOOO0O0000 ={"id":O0O0O0O0O0O0OO0O0 .giving ,"count":count_mew }#line:141
                    OO0O00000OO00OOO0 =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =O0O0O0O0O0O0OO0O0 .headers ,data =OO0O0OOOOOO0O0000 ).json ()#line:142
                    if 'count'in OO0O00000OO00OOO0 :#line:143
                        print (f'【赠送游票】：赠送10张游票给{O0O0O0O0O0O0OO0O0.giving}成功丨余额{str(OO0O00000OO00OOO0["count"])[:5]}')#line:144
                    else :#line:145
                        print ('【赠送游票】：失败')#line:146
                else :#line:147
                    print ('【赠送游票】：余额不足不执行操作')#line:148
            else :#line:149
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:150
        except Exception as O000OOO0O000O0OO0 :#line:151
            print (O000OOO0O000O0OO0 )#line:152
    def lottery_activities (O00O0O00OOO000O00 ):#line:156
        try :#line:157
            OOOO0O0OO0O00OOO0 =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0O00OOO000O00 .headers ).json ()#line:158
            if 'count'in OOOO0O0OO0O00OOO0 :#line:160
                O0O0OO0OO0O0O00OO =OOOO0O0OO0O00OOO0 ['count']#line:161
                print (f'【转盘抽奖】：剩余{O0O0OO0OO0O0O00OO}次抽奖')#line:162
                if O0O0OO0OO0O0O00OO >0 :#line:163
                    for O0OOO0000O00OOOO0 in range (O0O0OO0OO0O0O00OO ):#line:164
                        OOOOOOO0000OO0000 =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0O00OOO000O00 .headers ).json ()#line:165
                        if 'name'in OOOOOOO0000OO0000 :#line:166
                            print (f'【转盘抽奖】：获得:{OOOOOOO0000OO0000["name"]}{OOOOOOO0000OO0000["prize_number"]}张')#line:167
                        time .sleep (random .randint (15 ,30 )/10 )#line:168
        except Exception as OOOO00000OO0O0OO0 :#line:169
            print (OOOO00000OO0O0OO0 )#line:170
    def lottery_center_index (O0OO000O00O0OOOOO ):#line:174
        try :#line:175
            O0000O000O00O0000 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =O0OO000O00O0OOOOO .headers ).json ()#line:176
            if 'tickets'in O0000O000O00O0000 :#line:177
                for O000OOOO0OOO0000O in O0000O000O00O0000 ['tickets']:#line:178
                    if O000OOOO0OOO0000O ['name']=='游票':#line:179
                        print (f'【抽奖累计】：累计中了{str(O000OOOO0OOO0000O["total_count"])[:6]}张游票')#line:180
            if 'cumulative_tickets'in O0000O000O00O0000 :#line:181
                if O0000O000O00O0000 ['tickets']:#line:182
                    for O000OOOO0OOO0000O in O0000O000O00O0000 ['tickets']:#line:183
                        OOO00000OOOO00OO0 =O000OOOO0OOO0000O ['count']#line:184
                        O00OOOOO00O0OOOOO =O000OOOO0OOO0000O ['lt_type']#line:185
                        if O00OOOOO00O0OOOOO =='normal':#line:186
                            O0OO0O00O00OO0OO0 ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:187
                            if OOO00000OOOO00OO0 >'1':#line:188
                                O0OO000O00O0OOOOO .add_lottery_ticket (OOO00000OOOO00OO0 ,O0OO0O00O00OO0OO0 )#line:189
                                time .sleep (2 )#line:190
                        if O00OOOOO00O0OOOOO =='advanced':#line:191
                            O0OO0O00O00OO0OO0 ='7a468d93-aa43-4131-b414-b828b985e97e'#line:192
                            if OOO00000OOOO00OO0 >'1':#line:193
                                O0OO000O00O0OOOOO .add_lottery_ticket (OOO00000OOOO00OO0 ,O0OO0O00O00OO0OO0 )#line:194
        except Exception as OOO0000O0OOO0O00O :#line:195
            print (OOO0000O0OOO0O00O )#line:196
    def add_lottery_ticket (O000O0000O0O0O00O ,O0O0O0O000OO00OO0 ,OO0OOOOO0O0O0OOO0 ):#line:200
        try :#line:201
            O0OOOO00OOO00O000 ={"bet_on":O0O0O0O000OO00OO0 .split ('.')[0 ],"operation":"in","lotteru_activity_id":OO0OOOOO0O0O0OOO0 }#line:202
            O0OO000000000O000 =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =O000O0000O0O0O00O .headers ,data =O0OOOO00OOO00O000 ).json ()#line:203
            if 'bet_on'in O0OO000000000O000 :#line:204
                print (f'【添加奖券】：添加{O0O0O0O000OO00OO0.split(".")[0]}张成功')#line:205
        except Exception as O0OO0OO00O00OOO0O :#line:206
            print (O0OO0OO00O00OOO0O )#line:207
def version_of_the_validation ():#line:211
    return str ((59 -56 )/10 )#line:212
def gitee_validation ():#line:214
    try :#line:215
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:216
    except Exception as OOOO0OOO0OOOO00OO :#line:217
        sys .exit (0 )#line:218
def update_the_validation ():#line:222
    try :#line:223
        OO0O00O0O0OOO0OOO =gitee_validation ()#line:224
        if version_of_the_validation ()<OO0O00O0O0OOO0OOO ['SwimUpM']['edition']:#line:225
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00O0O0OOO0OOO["SwimUpM"]["edition"]}   ❌')#line:226
            print (f'更新内容=>>{OO0O00O0O0OOO0OOO["SwimUpM"]["content"]}   👍')#line:227
        else :#line:228
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO0O00O0O0OOO0OOO["SwimUpM"]["edition"]}   ✅')#line:229
            print (f'更新内容=>> {OO0O00O0O0OOO0OOO["SwimUpM"]["content"]}   👍')#line:230
            return True #line:231
    except Exception as O00OO0OO00O0O00O0 :#line:232
        print (O00OO0OO00O0O00O0 )#line:233
def os_qinglong ():#line:236
    if application in os .environ :#line:237
        OO0OO0OO00OO00000 =os .environ [application ].split ('\n')#line:238
        if len (OO0OO0OO00OO00000 )>0 :#line:239
            return OO0OO0OO00OO00000 #line:240
        else :#line:241
            print (f"{application}变量未启用")#line:242
            print ('脚本退出')#line:243
            sys .exit (1 )#line:244
    else :#line:245
        print (f"{application}变量为空\n尝试使用内置变量")#line:246
        return os_built ()#line:247
def os_built ():#line:250
    if token :#line:251
        OO00OOO0O0OOOOO0O =token .split ('\n')#line:252
        if len (OO00OOO0O0OOOOO0O )>0 :#line:253
            return OO00OOO0O0OOOOO0O #line:254
    else :#line:255
        print (f"内置变量为空")#line:256
        print ('脚本退出')#line:257
        sys .exit (0 )#line:258
if __name__ =='__main__':#line:261
    start ()#line:262
