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
new Env('拾米游0.2')
青龙变量 export smytoken="token@赠送游票ID@True"   
第三个参数是开启赠送功能     多号换行
版本0.2
"""


application = 'smytoken'    # 变量名
bundled = True              # 是否绑定邀请码
count_mew = 10              # 默认每次赠送10      10的整数手续费最划算
token = ''                  # 调试token



# 绑定上级ID  随机绑就多填   不需要1000
def bundled_def():
    bundled_id_new = ['31815', '41727']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]

#####################################################下面不要动#####################################################
cumulative_ticket =0 #line:1
host ='https://api.shimiyou.com'#line:2
git ='https://gitee.com'#line:3
mobile =0 #line:4
def start ():#line:5
    try :#line:6
        if update_the_validation ():#line:7
            OO000OOO00OO00000 =os_qinglong ()#line:8
            print (f"==========共找到{len(OO000OOO00OO00000)}个账号==========")#line:9
            for O0OOO000OOO0OO00O in OO000OOO00OO00000 :#line:10
                print (f"------------正在执行第{OO000OOO00OO00000.index(O0OOO000OOO0OO00O) + 1}个账号------------")#line:11
                OO0000000OOOO0OOO =SwimUpM (O0OOO000OOO0OO00O )#line:12
                if OO0000000OOOO0OOO .base_info ():#line:14
                    if bundled :#line:15
                        OO0000000OOOO0OOO .friend_center ()#line:17
                    OO0000000OOOO0OOO .lottery_activities ()#line:19
                    OO0000000OOOO0OOO .user_lottery_activity_records ()#line:21
                    OO0000000OOOO0OOO .lottery_center_index ()#line:23
                    if OO0000000OOOO0OOO .tickets :#line:24
                        OO0000000OOOO0OOO .tickets_give ()#line:26
                    time .sleep (random .randint (8 ,15 ))#line:27
                else :#line:28
                    print ('token失效')#line:29
            print (f"------------所有账号运行完毕正在统计每天收益------------")#line:30
            print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:31
    except Exception as O00O00000OO00OO0O :#line:32
        print (O00O00000OO00OO0O )#line:33
class SwimUpM :#line:35
    def __init__ (OO00OO0O000O0OOO0 ,OO00O00O0OO000OOO ):#line:37
        try :#line:38
            OO00OO0O000O0OOO0 .giving =OO00O00O0OO000OOO .split ("@")[1 ]#line:39
            OO00OO0O000O0OOO0 .tickets =OO00O00O0OO000OOO .split ("@")[2 ]#line:40
            OO00OO0O000O0OOO0 .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':OO00O00O0OO000OOO .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com',}#line:41
        except Exception as OO00O0O0O0OO0O000 :#line:42
            print ('变量格式错误')#line:43
    def base_info (O00OOO0OOOO0O0O0O ):#line:46
        global mobile #line:47
        try :#line:48
            OOOO0OO0OOOO0OO0O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O00OOO0OOOO0O0O0O .headers ).json ()#line:49
            if 'code'in OOOO0OO0OOOO0OO0O :#line:51
                return False #line:52
            if 'mobile'in OOOO0OO0OOOO0OO0O :#line:53
                if OOOO0OO0OOOO0OO0O ['mobile']:#line:54
                    mobile =OOOO0OO0OOOO0OO0O ['mobile']#line:55
                else :#line:56
                    mobile ='None'#line:57
            if 'id'in OOOO0OO0OOOO0OO0O :#line:58
                O0000O0OOO0O0OO0O =OOOO0OO0OOOO0OO0O ['nick_name']#line:59
                O0O00OO0000O00O0O =OOOO0OO0OOOO0OO0O ['card_no']#line:60
                OO00O0O000OOO0OO0 =str (O0O00OO0000O00O0O )[4 :5 ]+'**'+str (O0O00OO0000O00O0O )[7 :]#line:61
                OO00OO0O00OOO0OO0 =OOOO0OO0OOOO0OO0O ['ticket']['count']#line:62
                try :#line:63
                    if reversed (OO00OO0O00OOO0OO0 )!=0 :#line:64
                        OO00OO0O00OOO0OO0 =str (OO00OO0O00OOO0OO0 ).split ('.')[0 ]#line:65
                    else :#line:66
                        OO00OO0O00OOO0OO0 =0 #line:67
                except :#line:68
                    OO00OO0O00OOO0OO0 =0 #line:69
                print (f'【账号信息】：ID:{OO00O0O000OOO0OO0}丨昵称:{O0000O0OOO0O0OO0O[:7]}丨游票:{OO00OO0O00OOO0OO0}')#line:70
                OO00O000OO00OO0OO =OOOO0OO0OOOO0OO0O ['avatar']['url']#line:71
                if 'NUokiQDoKCFD'in OO00O000OO00OO0OO :#line:72
                    O0O0O00O0O0OO0OOO =re .findall ('/NUokiQDoKCFD(.*?).jpg',OOOO0OO0OOOO0OO0O ['avatar']['url'])[0 ].split ('NUokiQDoKCFD')[0 ].split ('-')[0 ]#line:73
                    OOOO0O0O0O000OOOO =(datetime .datetime .now ()-datetime .datetime (int (O0O0O00O0O0OO0OOO [:4 ]),int (O0O0O00O0O0OO0OOO [4 :6 ]),int (O0O0O00O0O0OO0OOO [6 :8 ]))).days #line:74
                    print (f'【注册绑定】：注册:{O0O0O00O0O0OO0OOO[:4]}-{O0O0O00O0O0OO0OOO[4:6]}-{O0O0O00O0O0OO0OOO[6:8]}丨距今:{OOOO0O0O0O000OOOO}天丨绑定:{mobile[7:]}')#line:75
                    return True #line:76
                if 'avatar'in OO00O000OO00OO0OO :#line:77
                    O0O0O00O0O0OO0OOO =re .findall ('/avatar(.*?).jpg',OOOO0OO0OOOO0OO0O ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')[0 ]#line:78
                    OOOO0O0O0O000OOOO =(datetime .datetime .now ()-datetime .datetime (int (O0O0O00O0O0OO0OOO [:4 ]),int (O0O0O00O0O0OO0OOO [4 :6 ]),int (O0O0O00O0O0OO0OOO [6 :8 ]))).days #line:79
                    print (f'【注册绑定】：注册:{O0O0O00O0O0OO0OOO[:4]}-{O0O0O00O0O0OO0OOO[4:6]}-{O0O0O00O0O0OO0OOO[6:8]}丨距今:{OOOO0O0O0O000OOOO}天丨绑定:{mobile[7:]}')#line:80
                    return True #line:81
            return True #line:82
        except Exception as OO000OO00O00O0000 :#line:83
            print (OO000OO00O00O0000 )#line:84
    def friend_center (O0OOO000OO0O0OOO0 ):#line:88
        O0OO00O0O00O0OO00 =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =O0OOO000OO0O0OOO0 .headers ).json ()#line:89
        if 'parent_user'in O0OO00O0O00O0OO00 :#line:90
            if O0OO00O0O00O0OO00 ['parent_user']:#line:91
                pass #line:92
            else :#line:93
                O0OOOOOO0OOO00OO0 ={"id":bundled_def ()}#line:94
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =O0OOO000OO0O0OOO0 .headers ,data =O0OOOOOO0OOO00OO0 ).json ()#line:95
    def user_lottery_activity_records (O000OOOO0O000O0OO ):#line:98
        global cumulative_ticket #line:99
        O00000O0000O00OOO =0 #line:100
        O0O0OOOO0OO0OO00O =0 #line:101
        try :#line:102
            OO00000O0O0O0OO00 =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =O000OOOO0O000O0OO .headers ).json ()#line:103
            if 'user_lottery_activity_records'in OO00000O0O0O0OO00 :#line:104
                for OOO0OO000O000O000 in OO00000O0O0O0OO00 ['user_lottery_activity_records']:#line:105
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==OOO0OO000O000O000 ['lottery_activity_id']:#line:106
                        O00000O0000O00OOO =OOO0OO000O000O000 ['bet_on']#line:107
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==OOO0OO000O000O000 ['lottery_activity_id']:#line:108
                        O0O0OOOO0OO0OO00O =OOO0OO000O000O000 ['bet_on']#line:109
                print (f'【参与抽奖】：普通奖券:{O0O0OOOO0OO0OO00O}张丨高级奖券:{O00000O0000O00OOO}张')#line:110
            if 'lottery_activity'in OO00000O0O0O0OO00 :#line:111
                for OOO0OO000O000O000 in OO00000O0O0O0OO00 ['lottery_activity']:#line:112
                    if OOO0OO000O000O000 ['topic']=='普通奖券抽游票':#line:113
                        OO0OOO00OO0O00OO0 =OOO0OO000O000O000 ['sum_bet_on']#line:114
                        OO00O00O00OOO0O00 =2880 *34 /OO0OOO00OO0O00OO0 *O0O0OOOO0OO0OO00O #line:115
                        cumulative_ticket +=OO00O00O00OOO0O00 #line:116
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(OO00O00O00OOO0O00)[:5]}')#line:117
                    if OOO0OO000O000O000 ['topic']=='高级奖券抽游票':#line:118
                        OO0OOO00OO0O00OO0 =OOO0OO000O000O000 ['sum_bet_on']#line:119
                        OO00O00O00OOO0O00 =2880 *313 /OO0OOO00OO0O00OO0 *O00000O0000O00OOO #line:120
                        cumulative_ticket +=OO00O00O00OOO0O00 #line:121
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(OO00O00O00OOO0O00)[:5]}')#line:122
        except Exception as OOOO00O0OOOOOO00O :#line:124
            print (OOOO00O0OOOOOO00O )#line:125
    def tickets_give (OO000OO00O0OOO000 ):#line:129
        try :#line:130
            OOOOOOO00OO00OOO0 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =OO000OO00O0OOO000 .headers ).json ()#line:131
            OOOOO0O0OOOOOO0O0 =str (OOOOOOO00OO00OOO0 ['card_no'])[4 :]#line:132
            if OO000OO00O0OOO000 .giving !=OOOOO0O0OOOOOO0O0 :#line:133
                OOOO00OOOOOO00OOO =OOOOOOO00OO00OOO0 ['ticket']['count']#line:134
                if float (OOOO00OOOOOO00OOO )==0 :#line:135
                    print ('【赠送游票】：账号初始化中')#line:136
                    return True #line:137
                OOO0O00OOO0O00O0O =str (OOOO00OOOOOO00OOO ).split ('.')[0 ]#line:138
                if int (OOO0O00OOO0O00O0O )>count_mew :#line:139
                    O00O0O000OOOOOO0O ={"id":OO000OO00O0OOO000 .giving ,"count":count_mew }#line:140
                    O0O0OOO0O0000O0OO =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =OO000OO00O0OOO000 .headers ,data =O00O0O000OOOOOO0O ).json ()#line:141
                    if 'count'in O0O0OOO0O0000O0OO :#line:142
                        print (f'【赠送游票】：赠送10张游票给{OO000OO00O0OOO000.giving}成功丨余额{str(O0O0OOO0O0000O0OO["count"])[:5]}')#line:143
                    else :#line:144
                        print ('【赠送游票】：失败')#line:145
                else :#line:146
                    print ('【赠送游票】：余额不足不执行操作')#line:147
            else :#line:148
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:149
        except Exception as OOO0000O0O00OO0O0 :#line:150
            print (OOO0000O0O00OO0O0 )#line:151
    def lottery_activities (O0OO00O0O0OO0O0O0 ):#line:155
        try :#line:156
            O0OOOOOO0000O00O0 =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O0OO00O0O0OO0O0O0 .headers ).json ()#line:157
            if 'count'in O0OOOOOO0000O00O0 :#line:159
                O0O00OOO000OO00O0 =O0OOOOOO0000O00O0 ['count']#line:160
                print (f'【转盘抽奖】：剩余{O0O00OOO000OO00O0}次抽奖')#line:161
                if O0O00OOO000OO00O0 >0 :#line:162
                    for OO0O0000OOO0000OO in range (O0O00OOO000OO00O0 ):#line:163
                        OOO0OO0O0O000OOO0 =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O0OO00O0O0OO0O0O0 .headers ).json ()#line:164
                        if 'name'in OOO0OO0O0O000OOO0 :#line:165
                            print (f'【转盘抽奖】：获得:{OOO0OO0O0O000OOO0["name"]}{OOO0OO0O0O000OOO0["prize_number"]}张')#line:166
                        time .sleep (random .randint (15 ,30 )/10 )#line:167
        except Exception as O0OO0000O0OO00OO0 :#line:168
            print (O0OO0000O0OO00OO0 )#line:169
    def lottery_center_index (O0OOOOO0O0OO00OOO ):#line:173
        try :#line:174
            OOO0OO00OOO0000O0 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =O0OOOOO0O0OO00OOO .headers ).json ()#line:175
            if 'tickets'in OOO0OO00OOO0000O0 :#line:176
                for OO00O0OOOO000OOO0 in OOO0OO00OOO0000O0 ['tickets']:#line:177
                    if OO00O0OOOO000OOO0 ['name']=='游票':#line:178
                        print (f'【抽奖累计】：累计中了{str(OO00O0OOOO000OOO0["total_count"])[:6]}张游票')#line:179
            if 'cumulative_tickets'in OOO0OO00OOO0000O0 :#line:180
                if OOO0OO00OOO0000O0 ['tickets']:#line:181
                    for OO00O0OOOO000OOO0 in OOO0OO00OOO0000O0 ['tickets']:#line:182
                        OOO0OO00O0000O00O =OO00O0OOOO000OOO0 ['count']#line:183
                        O0OOO0OO00OO0OOOO =OO00O0OOOO000OOO0 ['lt_type']#line:184
                        if O0OOO0OO00OO0OOOO =='normal':#line:185
                            OOOOO00OO0O0O0O0O ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:186
                            if OOO0OO00O0000O00O >'1':#line:187
                                O0OOOOO0O0OO00OOO .add_lottery_ticket (OOO0OO00O0000O00O ,OOOOO00OO0O0O0O0O )#line:188
                                time .sleep (2 )#line:189
                        if O0OOO0OO00OO0OOOO =='advanced':#line:190
                            OOOOO00OO0O0O0O0O ='7a468d93-aa43-4131-b414-b828b985e97e'#line:191
                            if OOO0OO00O0000O00O >'1':#line:192
                                O0OOOOO0O0OO00OOO .add_lottery_ticket (OOO0OO00O0000O00O ,OOOOO00OO0O0O0O0O )#line:193
        except Exception as O0000OOO000O00000 :#line:194
            print (O0000OOO000O00000 )#line:195
    def add_lottery_ticket (O00OO000O0000OO0O ,OOO0000O0O0O0OO0O ,O0OO00O000OO0O000 ):#line:199
        try :#line:200
            O0OO000OO0O00O0OO ={"bet_on":OOO0000O0O0O0OO0O .split ('.')[0 ],"operation":"in","lotteru_activity_id":O0OO00O000OO0O000 }#line:201
            O000O0000OOO0O0OO =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =O00OO000O0000OO0O .headers ,data =O0OO000OO0O00O0OO ).json ()#line:202
            if 'bet_on'in O000O0000OOO0O0OO :#line:203
                print (f'【添加奖券】：添加{OOO0000O0O0O0OO0O.split(".")[0]}张成功')#line:204
        except Exception as O0OO0OOOO0OOO0000 :#line:205
            print (O0OO0OOOO0OOO0000 )#line:206
def version_of_the_validation ():#line:210
    return str ((58 -56 )/10 )#line:211
def gitee_validation ():#line:213
    try :#line:214
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:215
    except Exception as OOOOOOOO0OO0OOO0O :#line:216
        sys .exit (0 )#line:217
def update_the_validation ():#line:221
    try :#line:222
        O0OOO0O00O0O0OO0O =gitee_validation ()#line:223
        if version_of_the_validation ()<O0OOO0O00O0O0OO0O ['SwimUpM']['edition']:#line:224
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO0O00O0O0OO0O["SwimUpM"]["edition"]}   ❌')#line:225
            print (f'更新内容=>>{O0OOO0O00O0O0OO0O["SwimUpM"]["content"]}   👍')#line:226
        else :#line:227
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0OOO0O00O0O0OO0O["SwimUpM"]["edition"]}   ✅')#line:228
            print (f'更新内容=>> {O0OOO0O00O0O0OO0O["SwimUpM"]["content"]}   👍')#line:229
            return True #line:230
    except Exception as OO0OO0O00O00O0O00 :#line:231
        print (OO0OO0O00O00O0O00 )#line:232
def os_qinglong ():#line:235
    if application in os .environ :#line:236
        O0000O00O0OO00O0O =os .environ [application ].split ('\n')#line:237
        if len (O0000O00O0OO00O0O )>0 :#line:238
            return O0000O00O0OO00O0O #line:239
        else :#line:240
            print (f"{application}变量未启用")#line:241
            print ('脚本退出')#line:242
            sys .exit (1 )#line:243
    else :#line:244
        print (f"{application}变量为空\n尝试使用内置变量")#line:245
        return os_built ()#line:246
def os_built ():#line:249
    if token :#line:250
        O0OOO000O0OO0O0OO =token .split ('\n')#line:251
        if len (O0OOO000O0OO0O0OO )>0 :#line:252
            return O0OOO000O0OO0O0OO #line:253
    else :#line:254
        print (f"内置变量为空")#line:255
        print ('脚本退出')#line:256
        sys .exit (0 )#line:257
if __name__ =='__main__':#line:260
    start ()#line:261
