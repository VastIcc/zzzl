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
count_mew = 1000              # 默认每次赠送10      10的整数手续费最划算
token = ''                  # 调试token



# 绑定上级ID  随机绑就多填   不需要1000
def bundled_def():
    bundled_id_new = ['33162', '41727']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]

#####################################################下面不要动#####################################################
cumulative_ticket =0 #line:1
host ='https://api.shimiyou.com'#line:2
git ='https://gitee.com'#line:3
mobile =0 #line:4
def start ():#line:5
    try :#line:6
        if update_the_validation ():#line:7
            OOOO00OO0OO000OOO =os_qinglong ()#line:8
            print (f"==========共找到{len(OOOO00OO0OO000OOO)}个账号==========")#line:9
            for OO0OO0OO00OOOO000 in OOOO00OO0OO000OOO :#line:10
                print (f"------------正在执行第{OOOO00OO0OO000OOO.index(OO0OO0OO00OOOO000) + 1}个账号------------")#line:11
                OO0OOO000O0000OOO =SwimUpM (OO0OO0OO00OOOO000 )#line:12
                if OO0OOO000O0000OOO .base_info ():#line:14
                    if bundled :#line:15
                        OO0OOO000O0000OOO .friend_center ()#line:17
                    OO0OOO000O0000OOO .lottery_activities ()#line:19
                    OO0OOO000O0000OOO .user_lottery_activity_records ()#line:21
                    OO0OOO000O0000OOO .lottery_center_index ()#line:23
                    if OO0OOO000O0000OOO .tickets :#line:24
                        OO0OOO000O0000OOO .tickets_give ()#line:26
                    time .sleep (random .randint (8 ,15 ))#line:27
                else :#line:28
                    print ('token失效')#line:29
            print (f"------------所有账号运行完毕正在统计每天收益------------")#line:30
            print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:31
    except Exception as O0000OO00OOOO0000 :#line:32
        print (O0000OO00OOOO0000 )#line:33
class SwimUpM :#line:35
    def __init__ (O0O00OO0000O00OO0 ,O00OO0O00OOOO0OO0 ):#line:37
        try :#line:38
            O0O00OO0000O00OO0 .giving =O00OO0O00OOOO0OO0 .split ("@")[1 ]#line:39
            O0O00OO0000O00OO0 .tickets =O00OO0O00OOOO0OO0 .split ("@")[2 ]#line:40
            O0O00OO0000O00OO0 .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':O00OO0O00OOOO0OO0 .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com',}#line:41
        except Exception as O000OOOOOO0OOO0O0 :#line:42
            print ('变量格式错误')#line:43
    def base_info (O000O0O00O00OOO0O ):#line:46
        global mobile #line:47
        try :#line:48
            OOOOO0O0OOOO00OOO =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O000O0O00O00OOO0O .headers ).json ()#line:49
            print (OOOOO0O0OOOO00OOO )#line:50
            if 'code'in OOOOO0O0OOOO00OOO :#line:51
                return False #line:52
            if 'mobile'in OOOOO0O0OOOO00OOO :#line:53
                if OOOOO0O0OOOO00OOO ['mobile']:#line:54
                    mobile =OOOOO0O0OOOO00OOO ['mobile']#line:55
                else :#line:56
                    mobile ='None'#line:57
            if 'id'in OOOOO0O0OOOO00OOO :#line:58
                OO00O0O00O0OOO000 =OOOOO0O0OOOO00OOO ['nick_name']#line:59
                OO0O0O0OOOOOO00O0 =OOOOO0O0OOOO00OOO ['card_no']#line:60
                O0OO000OOO000OO00 =str (OO0O0O0OOOOOO00O0 )[4 :5 ]+'**'+str (OO0O0O0OOOOOO00O0 )[7 :]#line:61
                O0O0000O0O0OO00O0 =OOOOO0O0OOOO00OOO ['ticket']['count']#line:62
                try :#line:63
                    if reversed (O0O0000O0O0OO00O0 )!=0 :#line:64
                        O0O0000O0O0OO00O0 =str (O0O0000O0O0OO00O0 ).split ('.')[0 ]#line:65
                    else :#line:66
                        O0O0000O0O0OO00O0 =0 #line:67
                except :#line:68
                    O0O0000O0O0OO00O0 =0 #line:69
                print (f'【账号信息】：ID:{O0OO000OOO000OO00}丨昵称:{OO00O0O00O0OOO000[:7]}丨游票:{O0O0000O0O0OO00O0}')#line:70
                OO000OOO0000OO0OO =OOOOO0O0OOOO00OOO ['avatar']['url']#line:71
                if OO000OOO0000OO0OO :#line:72
                    if 'NUokiQDoKCFD'in OO000OOO0000OO0OO :#line:73
                        OOO00OOOOOO00O0O0 =re .findall ('/NUokiQDoKCFD(.*?).jpg',OOOOO0O0OOOO00OOO ['avatar']['url'])[0 ].split ('NUokiQDoKCFD')[0 ].split ('-')[0 ]#line:74
                        OO0O00O00O0OO0O00 =(datetime .datetime .now ()-datetime .datetime (int (OOO00OOOOOO00O0O0 [:4 ]),int (OOO00OOOOOO00O0O0 [4 :6 ]),int (OOO00OOOOOO00O0O0 [6 :8 ]))).days #line:75
                        print (f'【注册绑定】：注册:{OOO00OOOOOO00O0O0[:4]}-{OOO00OOOOOO00O0O0[4:6]}-{OOO00OOOOOO00O0O0[6:8]}丨距今:{OO0O00O00O0OO0O00}天丨绑定:{mobile[7:]}')#line:76
                        return True #line:77
                    if 'avatar'in OO000OOO0000OO0OO :#line:78
                        OOO00OOOOOO00O0O0 =re .findall ('/avatar(.*?).jpg',OOOOO0O0OOOO00OOO ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')[0 ]#line:79
                        OO0O00O00O0OO0O00 =(datetime .datetime .now ()-datetime .datetime (int (OOO00OOOOOO00O0O0 [:4 ]),int (OOO00OOOOOO00O0O0 [4 :6 ]),int (OOO00OOOOOO00O0O0 [6 :8 ]))).days #line:80
                        print (f'【注册绑定】：注册:{OOO00OOOOOO00O0O0[:4]}-{OOO00OOOOOO00O0O0[4:6]}-{OOO00OOOOOO00O0O0[6:8]}丨距今:{OO0O00O00O0OO0O00}天丨绑定:{mobile[7:]}')#line:81
                        return True #line:82
            return True #line:83
        except Exception as OOO00OOOOOO0O0000 :#line:84
            print (OOO00OOOOOO0O0000 )#line:85
    def friend_center (OOOOOO0O00000OOO0 ):#line:89
        OOOO000OOO0000OOO =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =OOOOOO0O00000OOO0 .headers ).json ()#line:90
        if 'parent_user'in OOOO000OOO0000OOO :#line:91
            if OOOO000OOO0000OOO ['parent_user']:#line:92
                pass #line:93
            else :#line:94
                OOO000OOOOO0O0OOO ={"id":bundled_def ()}#line:95
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =OOOOOO0O00000OOO0 .headers ,data =OOO000OOOOO0O0OOO ).json ()#line:96
    def user_lottery_activity_records (OO00O0OOOOO000O0O ):#line:99
        global cumulative_ticket #line:100
        O0000O00O0O0000OO =0 #line:101
        OO00OO000OOOO0OOO =0 #line:102
        try :#line:103
            OOO0O000OO00OO0O0 =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =OO00O0OOOOO000O0O .headers ).json ()#line:104
            if 'user_lottery_activity_records'in OOO0O000OO00OO0O0 :#line:105
                for O0OOOO00O00O0OOOO in OOO0O000OO00OO0O0 ['user_lottery_activity_records']:#line:106
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==O0OOOO00O00O0OOOO ['lottery_activity_id']:#line:107
                        O0000O00O0O0000OO =O0OOOO00O00O0OOOO ['bet_on']#line:108
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==O0OOOO00O00O0OOOO ['lottery_activity_id']:#line:109
                        OO00OO000OOOO0OOO =O0OOOO00O00O0OOOO ['bet_on']#line:110
                print (f'【参与抽奖】：普通奖券:{OO00OO000OOOO0OOO}张丨高级奖券:{O0000O00O0O0000OO}张')#line:111
            if 'lottery_activity'in OOO0O000OO00OO0O0 :#line:112
                for O0OOOO00O00O0OOOO in OOO0O000OO00OO0O0 ['lottery_activity']:#line:113
                    if O0OOOO00O00O0OOOO ['topic']=='普通奖券抽游票':#line:114
                        OOOOOOO00O00O0O0O =O0OOOO00O00O0OOOO ['sum_bet_on']#line:115
                        O00O0O000O00OO00O =2880 *34 /OOOOOOO00O00O0O0O *OO00OO000OOOO0OOO #line:116
                        cumulative_ticket +=O00O0O000O00OO00O #line:117
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(O00O0O000O00OO00O)[:5]}')#line:118
                    if O0OOOO00O00O0OOOO ['topic']=='高级奖券抽游票':#line:119
                        OOOOOOO00O00O0O0O =O0OOOO00O00O0OOOO ['sum_bet_on']#line:120
                        O00O0O000O00OO00O =2880 *313 /OOOOOOO00O00O0O0O *O0000O00O0O0000OO #line:121
                        cumulative_ticket +=O00O0O000O00OO00O #line:122
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(O00O0O000O00OO00O)[:5]}')#line:123
        except Exception as O00OOO00O0000OOOO :#line:125
            print (O00OOO00O0000OOOO )#line:126
    def tickets_give (O00O000OO00OO00O0 ):#line:130
        try :#line:131
            O000OOO0000O00O0O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O00O000OO00OO00O0 .headers ).json ()#line:132
            OO0O0OOO00OO0O00O =str (O000OOO0000O00O0O ['card_no'])[4 :]#line:133
            if O00O000OO00OO00O0 .giving !=OO0O0OOO00OO0O00O :#line:134
                OOOOO00OOOO000O00 =O000OOO0000O00O0O ['ticket']['count']#line:135
                if float (OOOOO00OOOO000O00 )==0 :#line:136
                    print ('【赠送游票】：账号初始化中')#line:137
                    return True #line:138
                OOO0OOOO0000OO00O =str (OOOOO00OOOO000O00 ).split ('.')[0 ]#line:139
                if int (OOO0OOOO0000OO00O )>count_mew :#line:140
                    O0OOO0O00O0OO00O0 ={"id":O00O000OO00OO00O0 .giving ,"count":count_mew }#line:141
                    OOOO0OO00O00O0O00 =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =O00O000OO00OO00O0 .headers ,data =O0OOO0O00O0OO00O0 ).json ()#line:142
                    if 'count'in OOOO0OO00O00O0O00 :#line:143
                        print (f'【赠送游票】：赠送10张游票给{O00O000OO00OO00O0.giving}成功丨余额{str(OOOO0OO00O00O0O00["count"])[:5]}')#line:144
                    else :#line:145
                        print ('【赠送游票】：失败')#line:146
                else :#line:147
                    print ('【赠送游票】：余额不足不执行操作')#line:148
            else :#line:149
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:150
        except Exception as OOO000OO00O000OOO :#line:151
            print (OOO000OO00O000OOO )#line:152
    def lottery_activities (OO0000000O0O000OO ):#line:156
        try :#line:157
            O00O0000O000000OO =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =OO0000000O0O000OO .headers ).json ()#line:158
            if 'count'in O00O0000O000000OO :#line:160
                O0O0OO0O0OOO00O0O =O00O0000O000000OO ['count']#line:161
                print (f'【转盘抽奖】：剩余{O0O0OO0O0OOO00O0O}次抽奖')#line:162
                if O0O0OO0O0OOO00O0O >0 :#line:163
                    for OO000OOOOOO0O0000 in range (O0O0OO0O0OOO00O0O ):#line:164
                        OOO00O0O000OOOO00 =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =OO0000000O0O000OO .headers ).json ()#line:165
                        if 'name'in OOO00O0O000OOOO00 :#line:166
                            print (f'【转盘抽奖】：获得:{OOO00O0O000OOOO00["name"]}{OOO00O0O000OOOO00["prize_number"]}张')#line:167
                        time .sleep (random .randint (15 ,30 )/10 )#line:168
        except Exception as O0O0OOO00O0OOOOO0 :#line:169
            print (O0O0OOO00O0OOOOO0 )#line:170
    def lottery_center_index (OOOO0OOO0O0O00000 ):#line:174
        try :#line:175
            O0OO0O00OO00000O0 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =OOOO0OOO0O0O00000 .headers ).json ()#line:176
            if 'tickets'in O0OO0O00OO00000O0 :#line:177
                for O0000O0O00O0O000O in O0OO0O00OO00000O0 ['tickets']:#line:178
                    if O0000O0O00O0O000O ['name']=='游票':#line:179
                        print (f'【抽奖累计】：累计中了{str(O0000O0O00O0O000O["total_count"])[:6]}张游票')#line:180
            if 'cumulative_tickets'in O0OO0O00OO00000O0 :#line:181
                if O0OO0O00OO00000O0 ['tickets']:#line:182
                    for O0000O0O00O0O000O in O0OO0O00OO00000O0 ['tickets']:#line:183
                        OO0O00O0OO0O00000 =O0000O0O00O0O000O ['count']#line:184
                        OOO0O0OO00000OO0O =O0000O0O00O0O000O ['lt_type']#line:185
                        if OOO0O0OO00000OO0O =='normal':#line:186
                            OOOO0OO0OO0OOO00O ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:187
                            if OO0O00O0OO0O00000 >'1':#line:188
                                OOOO0OOO0O0O00000 .add_lottery_ticket (OO0O00O0OO0O00000 ,OOOO0OO0OO0OOO00O )#line:189
                                time .sleep (2 )#line:190
                        if OOO0O0OO00000OO0O =='advanced':#line:191
                            OOOO0OO0OO0OOO00O ='7a468d93-aa43-4131-b414-b828b985e97e'#line:192
                            if OO0O00O0OO0O00000 >'1':#line:193
                                OOOO0OOO0O0O00000 .add_lottery_ticket (OO0O00O0OO0O00000 ,OOOO0OO0OO0OOO00O )#line:194
        except Exception as O0O000O00O0OOOO00 :#line:195
            print (O0O000O00O0OOOO00 )#line:196
    def add_lottery_ticket (O00OO00O00O0OO000 ,OO0O00000OO00OOO0 ,OO000OOO00000O00O ):#line:200
        try :#line:201
            O0OOO0O00OO00OO0O ={"bet_on":OO0O00000OO00OOO0 .split ('.')[0 ],"operation":"in","lotteru_activity_id":OO000OOO00000O00O }#line:202
            OOOOO00000O0000OO =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =O00OO00O00O0OO000 .headers ,data =O0OOO0O00OO00OO0O ).json ()#line:203
            if 'bet_on'in OOOOO00000O0000OO :#line:204
                print (f'【添加奖券】：添加{OO0O00000OO00OOO0.split(".")[0]}张成功')#line:205
        except Exception as O0O0000O0O0O00O0O :#line:206
            print (O0O0000O0O0O00O0O )#line:207
def version_of_the_validation ():#line:211
    return str ((59 -56 )/10 )#line:212
def gitee_validation ():#line:214
    try :#line:215
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:216
    except Exception as O0O0OOO0O0O0O00O0 :#line:217
        sys .exit (0 )#line:218
def update_the_validation ():#line:222
    try :#line:223
        OO00000000O00OOO0 =gitee_validation ()#line:224
        if version_of_the_validation ()<OO00000000O00OOO0 ['SwimUpM']['edition']:#line:225
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000000O00OOO0["SwimUpM"]["edition"]}   ❌')#line:226
            print (f'更新内容=>>{OO00000000O00OOO0["SwimUpM"]["content"]}   👍')#line:227
        else :#line:228
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO00000000O00OOO0["SwimUpM"]["edition"]}   ✅')#line:229
            print (f'更新内容=>> {OO00000000O00OOO0["SwimUpM"]["content"]}   👍')#line:230
            return True #line:231
    except Exception as O00O000000O00OOOO :#line:232
        print (O00O000000O00OOOO )#line:233
def os_qinglong ():#line:236
    if application in os .environ :#line:237
        OO00O0O000OO0OO0O =os .environ [application ].split ('\n')#line:238
        if len (OO00O0O000OO0OO0O )>0 :#line:239
            return OO00O0O000OO0OO0O #line:240
        else :#line:241
            print (f"{application}变量未启用")#line:242
            print ('脚本退出')#line:243
            sys .exit (1 )#line:244
    else :#line:245
        print (f"{application}变量为空\n尝试使用内置变量")#line:246
        return os_built ()#line:247
def os_built ():#line:250
    if token :#line:251
        OO0OO0O00OO00O0OO =token .split ('\n')#line:252
        if len (OO0OO0O00OO00O0OO )>0 :#line:253
            return OO0OO0O00OO00O0OO #line:254
    else :#line:255
        print (f"内置变量为空")#line:256
        print ('脚本退出')#line:257
        sys .exit (0 )#line:258
if __name__ =='__main__':#line:261
    start ()#line:262

