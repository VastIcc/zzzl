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
new Env('拾米游')
青龙变量 export smytoken="token@赠送游票ID@True"   
第三个参数是开启赠送功能  True为赠送   False为不赠送   多号换行
版本0.4
"""
application = 'smytoken'    # 变量名
bundled = True              # 是否绑定邀请码
token = ''                  # 调试token
# 绑定上级ID  随机绑就多填   不需要1000
def bundled_def():
    bundled_id_new = ['33162', '41727']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]


#####################################################下面不要动#####################################################
cumulative_ticket =0 #line:1
host ='https://api.shimiyou.com'#line:2
git ='https://gitee.com'#line:3
def start ():#line:4
    try :#line:5
        if update_the_validation ():#line:6
            OOOOOOOOO0O0000OO =os_qinglong ()#line:7
            print (f"==========共找到{len(OOOOOOOOO0O0000OO)}个账号==========")#line:8
            for OO000O00O00OOOO0O in OOOOOOOOO0O0000OO :#line:9
                print (f"------------正在执行第{OOOOOOOOO0O0000OO.index(OO000O00O00OOOO0O) + 1}个账号------------")#line:10
                O0000OOO0O0OOO00O =SwimUpM (OO000O00O00OOOO0O )#line:11
                if O0000OOO0O0OOO00O .base_info ():#line:13
                    if bundled :#line:14
                        O0000OOO0O0OOO00O .friend_center ()#line:16
                    O0000OOO0O0OOO00O .lottery_activities ()#line:18
                    O0000OOO0O0OOO00O .user_lottery_activity_records ()#line:20
                    O0000OOO0O0OOO00O .lottery_center_index ()#line:22
                    if O0000OOO0O0OOO00O .tickets :#line:23
                        O0000OOO0O0OOO00O .tickets_give ()#line:25
                    time .sleep (random .randint (8 ,15 ))#line:26
                else :#line:27
                    print ('token失效')#line:28
            print (f"------------所有账号运行完毕正在统计每天收益------------")#line:29
            print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:30
    except Exception as O0OO0000O0000OO00 :#line:31
        print (O0OO0000O0000OO00 )#line:32
class SwimUpM :#line:34
    def __init__ (O00000OOO0000OOOO ,OOO00OOO00O0OO00O ):#line:36
        try :#line:37
            O00000OOO0000OOOO .giving =OOO00OOO00O0OO00O .split ("@")[1 ]#line:38
            O00000OOO0000OOOO .tickets =OOO00OOO00O0OO00O .split ("@")[2 ]#line:39
            O00000OOO0000OOOO .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':OOO00OOO00O0OO00O .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com',}#line:40
        except Exception as OO0O00OOO0OOOO00O :#line:41
            print ('变量格式错误')#line:42
    def base_info (OO000O0OO0O0O000O ):#line:45
        try :#line:46
            OO0O0OOOOOOO00O00 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =OO000O0OO0O0O000O .headers ).json ()#line:47
            if 'code'in OO0O0OOOOOOO00O00 :#line:49
                return False #line:50
            if 'id'in OO0O0OOOOOOO00O00 :#line:52
                O0O00000O000000OO =OO0O0OOOOOOO00O00 ['nick_name']#line:53
                OO000O0000O00OO0O =OO0O0OOOOOOO00O00 ['card_no']#line:54
                O000O0O00O00O00OO =str (OO000O0000O00OO0O )[4 :5 ]+'**'+str (OO000O0000O00OO0O )[7 :]#line:55
                OOO0O00O000000OOO =OO0O0OOOOOOO00O00 ['ticket']['count']#line:56
                try :#line:57
                    if reversed (OOO0O00O000000OOO )!=0 :#line:58
                        OOO0O00O000000OOO =str (OOO0O00O000000OOO ).split ('.')[0 ]#line:59
                    else :#line:60
                        OOO0O00O000000OOO =0 #line:61
                except :#line:62
                    OOO0O00O000000OOO =0 #line:63
                print (f'【账号信息】：ID:{O000O0O00O00O00OO}丨昵称:{O0O00000O000000OO[:7]}丨游票:{OOO0O00O000000OOO}')#line:64
                O0O00OOOOOO0000OO =OO0O0OOOOOOO00O00 ['avatar']['url']#line:65
                if O0O00OOOOOO0000OO :#line:66
                    if 'NUokiQDoKCFD'in O0O00OOOOOO0000OO :#line:67
                        OOOOO0O0O00OO0000 =re .findall ('/NUokiQDoKCFD(.*?).jpg',OO0O0OOOOOOO00O00 ['avatar']['url'])[0 ].split ('NUokiQDoKCFD')[0 ].split ('-')[0 ]#line:68
                        O00OOOOO0O0OO0OOO =(datetime .datetime .now ()-datetime .datetime (int (OOOOO0O0O00OO0000 [:4 ]),int (OOOOO0O0O00OO0000 [4 :6 ]),int (OOOOO0O0O00OO0000 [6 :8 ]))).days #line:69
                        print (f'【注册绑定】：注册:{OOOOO0O0O00OO0000[:4]}-{OOOOO0O0O00OO0000[4:6]}-{OOOOO0O0O00OO0000[6:8]}丨距今:{O00OOOOO0O0OO0OOO}天')#line:70
                        return True #line:71
                    if 'avatar'in O0O00OOOOOO0000OO :#line:72
                        OOOOO0O0O00OO0000 =re .findall ('/avatar(.*?).jpg',OO0O0OOOOOOO00O00 ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')[0 ]#line:73
                        O00OOOOO0O0OO0OOO =(datetime .datetime .now ()-datetime .datetime (int (OOOOO0O0O00OO0000 [:4 ]),int (OOOOO0O0O00OO0000 [4 :6 ]),int (OOOOO0O0O00OO0000 [6 :8 ]))).days #line:74
                        print (f'【注册绑定】：注册:{OOOOO0O0O00OO0000[:4]}-{OOOOO0O0O00OO0000[4:6]}-{OOOOO0O0O00OO0000[6:8]}丨距今:{O00OOOOO0O0OO0OOO}天')#line:75
                        return True #line:76
            return True #line:77
        except Exception as O0O00OO0OOO000OO0 :#line:78
            print (O0O00OO0OOO000OO0 )#line:79
    def friend_center (OOOO000OOO00O00OO ):#line:83
        O00000O00O0O0OO00 =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =OOOO000OOO00O00OO .headers ).json ()#line:84
        if 'parent_user'in O00000O00O0O0OO00 :#line:85
            if O00000O00O0O0OO00 ['parent_user']:#line:86
                pass #line:87
            else :#line:88
                OO0000OOO00000OO0 ={"id":bundled_def ()}#line:89
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =OOOO000OOO00O00OO .headers ,data =OO0000OOO00000OO0 ).json ()#line:90
    def user_lottery_activity_records (O0OO0OO00O00OOOOO ):#line:93
        global cumulative_ticket #line:94
        OOOOO0O000OO00O0O =0 #line:95
        OO0O0000O000OOOOO =0 #line:96
        try :#line:97
            OOO0OOOO00OO00O0O =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =O0OO0OO00O00OOOOO .headers ).json ()#line:98
            if 'user_lottery_activity_records'in OOO0OOOO00OO00O0O :#line:99
                for O00OO0O00O0OOO000 in OOO0OOOO00OO00O0O ['user_lottery_activity_records']:#line:100
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==O00OO0O00O0OOO000 ['lottery_activity_id']:#line:101
                        OOOOO0O000OO00O0O =O00OO0O00O0OOO000 ['bet_on']#line:102
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==O00OO0O00O0OOO000 ['lottery_activity_id']:#line:103
                        OO0O0000O000OOOOO =O00OO0O00O0OOO000 ['bet_on']#line:104
                print (f'【参与抽奖】：普通奖券:{OO0O0000O000OOOOO}张丨高级奖券:{OOOOO0O000OO00O0O}张')#line:105
            if 'lottery_activity'in OOO0OOOO00OO00O0O :#line:106
                for O00OO0O00O0OOO000 in OOO0OOOO00OO00O0O ['lottery_activity']:#line:107
                    if O00OO0O00O0OOO000 ['topic']=='普通奖券抽游票':#line:108
                        OOOO0O0OO0O00OO0O =O00OO0O00O0OOO000 ['sum_bet_on']#line:109
                        OOOOO00O0OO000000 =2880 *34 /OOOO0O0OO0O00OO0O *OO0O0000O000OOOOO #line:110
                        cumulative_ticket +=OOOOO00O0OO000000 #line:111
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(OOOOO00O0OO000000)[:5]}')#line:112
                    if O00OO0O00O0OOO000 ['topic']=='高级奖券抽游票':#line:113
                        OOOO0O0OO0O00OO0O =O00OO0O00O0OOO000 ['sum_bet_on']#line:114
                        OOOOO00O0OO000000 =2880 *313 /OOOO0O0OO0O00OO0O *OOOOO0O000OO00O0O #line:115
                        cumulative_ticket +=OOOOO00O0OO000000 #line:116
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(OOOOO00O0OO000000)[:5]}')#line:117
        except Exception as O00OOOO0OOO00OO0O :#line:119
            print (O00OOOO0OOO00OO0O )#line:120
    def tickets_give (OO0OOO0OO00OO0O00 ):#line:124
        try :#line:125
            OOO00O0OOO0O00OOO =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =OO0OOO0OO00OO0O00 .headers ).json ()#line:126
            OO0OO00O0O0O0O0O0 =str (OOO00O0OOO0O00OOO ['card_no'])[4 :]#line:127
            if OO0OOO0OO00OO0O00 .giving !=OO0OO00O0O0O0O0O0 :#line:128
                OO0O0O00000OOO0O0 =OOO00O0OOO0O00OOO ['ticket']['count']#line:129
                if float (OO0O0O00000OOO0O0 )==0 :#line:130
                    print ('【赠送游票】：账号初始化中')#line:131
                    return True #line:132
                O0OO0O00OO0O0OOO0 =str (OO0O0O00000OOO0O0 ).split ('.')[0 ]#line:133
                O0OOOO0O00O00OOOO =int (str ((float (O0OO0O00OO0O0OOO0 )/1.1 )/10 ).split (".")[0 ])*10 #line:134
                if int (O0OO0O00OO0O0OOO0 )>10 :#line:135
                    O000000O00O000OOO ={"id":OO0OOO0OO00OO0O00 .giving ,"count":O0OOOO0O00O00OOOO }#line:136
                    O0O0O00OO000O00OO =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =OO0OOO0OO00OO0O00 .headers ,data =O000000O00O000OOO ).json ()#line:137
                    if 'count'in O0O0O00OO000O00OO :#line:138
                        print (f'【赠送游票】：赠送{O0OOOO0O00O00OOOO}张游票给{OO0OOO0OO00OO0O00.giving}成功丨余额{str(O0O0O00OO000O00OO["count"])[:5]}')#line:139
                    else :#line:140
                        print ('【赠送游票】：失败')#line:141
                else :#line:142
                    print ('【赠送游票】：余额不足不执行操作')#line:143
            else :#line:144
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:145
        except Exception as OO0O0O0OO0O0O0OOO :#line:146
            print (OO0O0O0OO0O0O0OOO )#line:147
    def lottery_activities (O00O0OOOOOO0000OO ):#line:151
        try :#line:152
            OOOO000O00O000O0O =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OOOOOO0000OO .headers ).json ()#line:153
            if 'count'in OOOO000O00O000O0O :#line:155
                O00OOOO0OO0000O00 =OOOO000O00O000O0O ['count']#line:156
                print (f'【转盘抽奖】：剩余{O00OOOO0OO0000O00}次抽奖')#line:157
                if O00OOOO0OO0000O00 >0 :#line:158
                    for O0O000OO0000000OO in range (O00OOOO0OO0000O00 ):#line:159
                        OOOOO0OOO0O0OO0OO =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OOOOOO0000OO .headers ).json ()#line:160
                        if 'name'in OOOOO0OOO0O0OO0OO :#line:161
                            print (f'【转盘抽奖】：获得:{OOOOO0OOO0O0OO0OO["name"]}{OOOOO0OOO0O0OO0OO["prize_number"]}张')#line:162
                        time .sleep (random .randint (15 ,30 )/10 )#line:163
        except Exception as O0O00000OO00000OO :#line:164
            print (O0O00000OO00000OO )#line:165
    def lottery_center_index (O0O000OO000OO000O ):#line:169
        try :#line:170
            OOOO000000OO00O00 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =O0O000OO000OO000O .headers ).json ()#line:171
            if 'tickets'in OOOO000000OO00O00 :#line:172
                for O000OOO0OOO0OOO00 in OOOO000000OO00O00 ['tickets']:#line:173
                    if O000OOO0OOO0OOO00 ['name']=='游票':#line:174
                        print (f'【抽奖累计】：累计中了{str(O000OOO0OOO0OOO00["total_count"])[:6]}张游票')#line:175
            if 'cumulative_tickets'in OOOO000000OO00O00 :#line:176
                if OOOO000000OO00O00 ['tickets']:#line:177
                    for O000OOO0OOO0OOO00 in OOOO000000OO00O00 ['tickets']:#line:178
                        OO00OO000O000000O =O000OOO0OOO0OOO00 ['count']#line:179
                        O0O000OO0OOO000OO =O000OOO0OOO0OOO00 ['lt_type']#line:180
                        if O0O000OO0OOO000OO =='normal':#line:181
                            O000OOO0O00OO0OOO ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:182
                            if OO00OO000O000000O >'1':#line:183
                                O0O000OO000OO000O .add_lottery_ticket (OO00OO000O000000O ,O000OOO0O00OO0OOO )#line:184
                                time .sleep (2 )#line:185
                        if O0O000OO0OOO000OO =='advanced':#line:186
                            O000OOO0O00OO0OOO ='7a468d93-aa43-4131-b414-b828b985e97e'#line:187
                            if OO00OO000O000000O >'1':#line:188
                                O0O000OO000OO000O .add_lottery_ticket (OO00OO000O000000O ,O000OOO0O00OO0OOO )#line:189
        except Exception as OO00O0000OO0OOOOO :#line:190
            print (OO00O0000OO0OOOOO )#line:191
    def add_lottery_ticket (OO000OOO0O0OO00OO ,O0O0O0OOOO00OOOO0 ,OO0O0OOO000OOOO0O ):#line:195
        try :#line:196
            OOO00O0O0O0O0O00O ={"bet_on":O0O0O0OOOO00OOOO0 .split ('.')[0 ],"operation":"in","lotteru_activity_id":OO0O0OOO000OOOO0O }#line:197
            O0O0O00000OOO00OO =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =OO000OOO0O0OO00OO .headers ,data =OOO00O0O0O0O0O00O ).json ()#line:198
            if 'bet_on'in O0O0O00000OOO00OO :#line:199
                print (f'【添加奖券】：添加{O0O0O0OOOO00OOOO0.split(".")[0]}张成功')#line:200
        except Exception as O000OOO0O0O0000OO :#line:201
            print (O000OOO0O0O0000OO )#line:202
def version_of_the_validation ():#line:206
    return str ((60 -56 )/10 )#line:207
def gitee_validation ():#line:209
    try :#line:210
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:211
    except Exception as OO0O0000O00OOOO00 :#line:212
        sys .exit (0 )#line:213
def update_the_validation ():#line:217
    try :#line:218
        O0O0OO00O0O00O00O =gitee_validation ()#line:219
        if version_of_the_validation ()<O0O0OO00O0O00O00O ['SwimUpM']['edition']:#line:220
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO00O0O00O00O["SwimUpM"]["edition"]}   ❌')#line:221
            print (f'更新内容=>>{O0O0OO00O0O00O00O["SwimUpM"]["content"]}   👍')#line:222
        else :#line:223
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0OO00O0O00O00O["SwimUpM"]["edition"]}   ✅')#line:224
            print (f'更新内容=>> {O0O0OO00O0O00O00O["SwimUpM"]["content"]}   👍')#line:225
            return True #line:226
    except Exception as OOOOOOO0OO000OOO0 :#line:227
        print (OOOOOOO0OO000OOO0 )#line:228
def os_qinglong ():#line:231
    if application in os .environ :#line:232
        OO0000O0000OOOO00 =os .environ [application ].split ('\n')#line:233
        if len (OO0000O0000OOOO00 )>0 :#line:234
            return OO0000O0000OOOO00 #line:235
        else :#line:236
            print (f"{application}变量未启用")#line:237
            print ('脚本退出')#line:238
            sys .exit (1 )#line:239
    else :#line:240
        print (f"{application}变量为空\n尝试使用内置变量")#line:241
        return os_built ()#line:242
def os_built ():#line:245
    if token :#line:246
        O00O0OOO00O0OOOO0 =token .split ('\n')#line:247
        if len (O00O0OOO00O0OOOO0 )>0 :#line:248
            return O00O0OOO00O0OOOO0 #line:249
    else :#line:250
        print (f"内置变量为空")#line:251
        print ('脚本退出')#line:252
        sys .exit (0 )#line:253
if __name__ =='__main__':#line:256
    start ()#line:257
