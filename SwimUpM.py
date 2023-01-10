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
        update_the_validation ()#line:6
        OOO0OO0OOO0O00O0O =os_qinglong ()#line:7
        print (f"==========共找到{len(OOO0OO0OOO0O00O0O)}个账号==========")#line:8
        for O0000O0OOO0O00O0O in OOO0OO0OOO0O00O0O :#line:9
            print (f"------------正在执行第{OOO0OO0OOO0O00O0O.index(O0000O0OOO0O00O0O) + 1}个账号------------")#line:10
            OOOOO0O00O0O0OO00 =SwimUpM (O0000O0OOO0O00O0O )#line:11
            if OOOOO0O00O0O0OO00 .base_info ():#line:13
                if bundled :#line:14
                    OOOOO0O00O0O0OO00 .friend_center ()#line:16
                OOOOO0O00O0O0OO00 .lottery_activities ()#line:18
                OOOOO0O00O0O0OO00 .user_lottery_activity_records ()#line:20
                OOOOO0O00O0O0OO00 .lottery_center_index ()#line:22
                if OOOOO0O00O0O0OO00 .tickets :#line:23
                    OOOOO0O00O0O0OO00 .tickets_give ()#line:25
                time .sleep (random .randint (8 ,15 ))#line:26
            else :#line:27
                print ('token失效')#line:28
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:29
        print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:30
    except Exception as O0O0O0OO000OO00OO :#line:31
        print (O0O0O0OO000OO00OO )#line:32
class SwimUpM :#line:34
    def __init__ (OOOOOO00O00O0OOO0 ,O0O000OOO0O000OOO ):#line:36
        try :#line:37
            OOOOOO00O00O0OOO0 .giving =O0O000OOO0O000OOO .split ("@")[1 ]#line:38
            OOOOOO00O00O0OOO0 .tickets =O0O000OOO0O000OOO .split ("@")[2 ]#line:39
            OOOOOO00O00O0OOO0 .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':O0O000OOO0O000OOO .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com',}#line:40
        except Exception as OO000O0OO000O0O0O :#line:41
            print ('变量格式错误')#line:42
    def base_info (OOO0000O00000OOOO ):#line:45
        try :#line:46
            OO00O000OO0OO000O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =OOO0000O00000OOOO .headers ).json ()#line:47
            if 'code'in OO00O000OO0OO000O :#line:49
                return False #line:50
            if 'id'in OO00O000OO0OO000O :#line:52
                OO00OO0OOOOOOOOO0 =OO00O000OO0OO000O ['nick_name']#line:53
                OO00OO0O0000000O0 =OO00O000OO0OO000O ['card_no']#line:54
                OO00O0000O00OO0OO =str (OO00OO0O0000000O0 )[4 :5 ]+'**'+str (OO00OO0O0000000O0 )[7 :]#line:55
                OOO0O000O0000OO00 =OO00O000OO0OO000O ['ticket']['count']#line:56
                try :#line:57
                    if reversed (OOO0O000O0000OO00 )!=0 :#line:58
                        OOO0O000O0000OO00 =str (OOO0O000O0000OO00 )[:6 ]#line:59
                    else :#line:60
                        OOO0O000O0000OO00 =0 #line:61
                except :#line:62
                    OOO0O000O0000OO00 =0 #line:63
                print (f'【账号信息】：ID:{OO00O0000O00OO0OO}丨昵称:{OO00OO0OOOOOOOOO0[:7]}丨游票:{OOO0O000O0000OO00}')#line:64
                O00O00OO0O0OOO0OO =OO00O000OO0OO000O ['avatar']['url']#line:65
                if O00O00OO0O0OOO0OO :#line:66
                    if 'NUokiQDoKCFD'in O00O00OO0O0OOO0OO :#line:67
                        O0O0O00O0O000O0O0 =re .findall ('/NUokiQDoKCFD(.*?).jpg',OO00O000OO0OO000O ['avatar']['url'])[0 ].split ('NUokiQDoKCFD')[0 ].split ('-')[0 ]#line:68
                        O0O00OO00000OO0O0 =(datetime .datetime .now ()-datetime .datetime (int (O0O0O00O0O000O0O0 [:4 ]),int (O0O0O00O0O000O0O0 [4 :6 ]),int (O0O0O00O0O000O0O0 [6 :8 ]))).days #line:69
                        print (f'【注册绑定】：注册:{O0O0O00O0O000O0O0[:4]}-{O0O0O00O0O000O0O0[4:6]}-{O0O0O00O0O000O0O0[6:8]}丨距今:{O0O00OO00000OO0O0}天')#line:70
                        return True #line:71
                    if 'avatar'in O00O00OO0O0OOO0OO :#line:72
                        O0O0O00O0O000O0O0 =re .findall ('/avatar(.*?).jpg',OO00O000OO0OO000O ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')[0 ]#line:73
                        O0O00OO00000OO0O0 =(datetime .datetime .now ()-datetime .datetime (int (O0O0O00O0O000O0O0 [:4 ]),int (O0O0O00O0O000O0O0 [4 :6 ]),int (O0O0O00O0O000O0O0 [6 :8 ]))).days #line:74
                        print (f'【注册绑定】：注册:{O0O0O00O0O000O0O0[:4]}-{O0O0O00O0O000O0O0[4:6]}-{O0O0O00O0O000O0O0[6:8]}丨距今:{O0O00OO00000OO0O0}天')#line:75
                        return True #line:76
            return True #line:77
        except Exception as OOOOO0O0OO0O0OO00 :#line:78
            print (OOOOO0O0OO0O0OO00 )#line:79
    def friend_center (OOO00000O0O00O00O ):#line:83
        OO000O0OOO0OO000O =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =OOO00000O0O00O00O .headers ).json ()#line:84
        if 'parent_user'in OO000O0OOO0OO000O :#line:85
            if OO000O0OOO0OO000O ['parent_user']:#line:86
                pass #line:87
            else :#line:88
                O0O0OO0O0O0OOOOOO ={"id":bundled_def ()}#line:89
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =OOO00000O0O00O00O .headers ,data =O0O0OO0O0O0OOOOOO ).json ()#line:90
    def user_lottery_activity_records (OOO0OO0O00OO00O0O ):#line:93
        global cumulative_ticket #line:94
        O00OO0O0O0O000O00 =0 #line:95
        OO0OO0O0O00000O00 =0 #line:96
        try :#line:97
            OOO00000OO0O0O00O =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =OOO0OO0O00OO00O0O .headers ).json ()#line:98
            if 'user_lottery_activity_records'in OOO00000OO0O0O00O :#line:99
                for OOOOO000OOOO00O00 in OOO00000OO0O0O00O ['user_lottery_activity_records']:#line:100
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==OOOOO000OOOO00O00 ['lottery_activity_id']:#line:101
                        O00OO0O0O0O000O00 =OOOOO000OOOO00O00 ['bet_on']#line:102
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==OOOOO000OOOO00O00 ['lottery_activity_id']:#line:103
                        OO0OO0O0O00000O00 =OOOOO000OOOO00O00 ['bet_on']#line:104
                print (f'【参与抽奖】：普通奖券:{OO0OO0O0O00000O00}张丨高级奖券:{O00OO0O0O0O000O00}张')#line:105
            if 'lottery_activity'in OOO00000OO0O0O00O :#line:106
                for OOOOO000OOOO00O00 in OOO00000OO0O0O00O ['lottery_activity']:#line:107
                    if OOOOO000OOOO00O00 ['topic']=='普通奖券抽游票':#line:108
                        OO0OOOO0000OOOOOO =OOOOO000OOOO00O00 ['sum_bet_on']#line:109
                        O00O0000OO00OO0O0 =2880 *34 /OO0OOOO0000OOOOOO *OO0OO0O0O00000O00 #line:110
                        cumulative_ticket +=O00O0000OO00OO0O0 #line:111
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(O00O0000OO00OO0O0)[:5]}')#line:112
                    if OOOOO000OOOO00O00 ['topic']=='高级奖券抽游票':#line:113
                        OO0OOOO0000OOOOOO =OOOOO000OOOO00O00 ['sum_bet_on']#line:114
                        O00O0000OO00OO0O0 =2880 *313 /OO0OOOO0000OOOOOO *O00OO0O0O0O000O00 #line:115
                        cumulative_ticket +=O00O0000OO00OO0O0 #line:116
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(O00O0000OO00OO0O0)[:5]}')#line:117
        except Exception as O00O0000O0O00OOOO :#line:119
            print (O00O0000O0O00OOOO )#line:120
    def tickets_give (O0000OO0O0O00O0OO ):#line:124
        try :#line:125
            OO0O00O0O0OOO0OO0 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O0000OO0O0O00O0OO .headers ).json ()#line:126
            O00OO00OOOO000000 =str (OO0O00O0O0OOO0OO0 ['card_no'])[4 :]#line:127
            if O0000OO0O0O00O0OO .giving !=O00OO00OOOO000000 :#line:128
                OO0O00O0OO00OOOOO =OO0O00O0O0OOO0OO0 ['ticket']['count']#line:129
                if float (OO0O00O0OO00OOOOO )==0 :#line:130
                    print ('【赠送游票】：账号初始化中')#line:131
                    return True #line:132
                O0OOO0OO0OO0O000O =str (OO0O00O0OO00OOOOO ).split ('.')[0 ]#line:133
                OO0OO0O0O00OO00OO =int (str ((float (O0OOO0OO0OO0O000O )/1.1 )/10 ).split (".")[0 ])*10 #line:134
                if int (O0OOO0OO0OO0O000O )>10 :#line:135
                    O0O00OOO0O0OO0000 ={"id":O0000OO0O0O00O0OO .giving ,"count":OO0OO0O0O00OO00OO }#line:136
                    O00O0OOOOO0000O00 =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =O0000OO0O0O00O0OO .headers ,data =O0O00OOO0O0OO0000 ).json ()#line:137
                    if 'count'in O00O0OOOOO0000O00 :#line:138
                        print (f'【赠送游票】：赠送{OO0OO0O0O00OO00OO}张游票给{O0000OO0O0O00O0OO.giving}成功丨余额{str(O00O0OOOOO0000O00["count"])[:5]}')#line:139
                    else :#line:140
                        print ('【赠送游票】：失败')#line:141
                else :#line:142
                    print ('【赠送游票】：余额不足不执行操作')#line:143
            else :#line:144
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:145
        except Exception as OO0000OO000OOOOO0 :#line:146
            print (OO0000OO000OOOOO0 )#line:147
    def lottery_activities (O00O0OOO00OO00OO0 ):#line:151
        try :#line:152
            O0OO000O0OOOOO00O =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OOO00OO00OO0 .headers ).json ()#line:153
            if 'count'in O0OO000O0OOOOO00O :#line:155
                O00OO0O0O0000O000 =O0OO000O0OOOOO00O ['count']#line:156
                print (f'【转盘抽奖】：剩余{O00OO0O0O0000O000}次抽奖')#line:157
                if O00OO0O0O0000O000 >0 :#line:158
                    for O00OO00O0O0OO00OO in range (O00OO0O0O0000O000 ):#line:159
                        O00OOO0O00O00000O =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OOO00OO00OO0 .headers ).json ()#line:160
                        if 'name'in O00OOO0O00O00000O :#line:161
                            print (f'【转盘抽奖】：获得:{O00OOO0O00O00000O["name"]}{O00OOO0O00O00000O["prize_number"]}张')#line:162
                        time .sleep (random .randint (15 ,30 )/10 )#line:163
        except Exception as O00O00000O0O00OO0 :#line:164
            print (O00O00000O0O00OO0 )#line:165
    def lottery_center_index (OOO0O0OO0OO0000OO ):#line:169
        try :#line:170
            O00O00OO00O0O0OOO =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =OOO0O0OO0OO0000OO .headers ).json ()#line:171
            if 'tickets'in O00O00OO00O0O0OOO :#line:172
                for OOO00O000O000O00O in O00O00OO00O0O0OOO ['tickets']:#line:173
                    if OOO00O000O000O00O ['name']=='游票':#line:174
                        print (f'【抽奖累计】：累计中了{str(OOO00O000O000O00O["total_count"])[:6]}张游票')#line:175
            if 'cumulative_tickets'in O00O00OO00O0O0OOO :#line:176
                if O00O00OO00O0O0OOO ['tickets']:#line:177
                    for OOO00O000O000O00O in O00O00OO00O0O0OOO ['tickets']:#line:178
                        OOOO000O0O0O00000 =OOO00O000O000O00O ['count']#line:179
                        OO00O0O0O00O00O00 =OOO00O000O000O00O ['lt_type']#line:180
                        if OO00O0O0O00O00O00 =='normal':#line:181
                            O0000O0O0O00OO0OO ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:182
                            if OOOO000O0O0O00000 >'1':#line:183
                                OOO0O0OO0OO0000OO .add_lottery_ticket (OOOO000O0O0O00000 ,O0000O0O0O00OO0OO )#line:184
                                time .sleep (2 )#line:185
                        if OO00O0O0O00O00O00 =='advanced':#line:186
                            O0000O0O0O00OO0OO ='7a468d93-aa43-4131-b414-b828b985e97e'#line:187
                            if OOOO000O0O0O00000 >'1':#line:188
                                OOO0O0OO0OO0000OO .add_lottery_ticket (OOOO000O0O0O00000 ,O0000O0O0O00OO0OO )#line:189
        except Exception as O00O0O0O000O0OOO0 :#line:190
            print (O00O0O0O000O0OOO0 )#line:191
    def add_lottery_ticket (OOOOOO00O00000OOO ,OOOO00O000OOOO0OO ,O0OOOOOO0000O00OO ):#line:195
        try :#line:196
            OO00O0OO0OO0O000O ={"bet_on":OOOO00O000OOOO0OO .split ('.')[0 ],"operation":"in","lotteru_activity_id":O0OOOOOO0000O00OO }#line:197
            O0O0OOOOO0O0O0OO0 =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =OOOOOO00O00000OOO .headers ,data =OO00O0OO0OO0O000O ).json ()#line:198
            if 'bet_on'in O0O0OOOOO0O0O0OO0 :#line:199
                print (f'【添加奖券】：添加{OOOO00O000OOOO0OO.split(".")[0]}张成功')#line:200
        except Exception as OO00OOOO0000O00OO :#line:201
            print (OO00OOOO0000O00OO )#line:202
def version_of_the_validation ():#line:206
    return str ((60 -56 )/10 )#line:207
def gitee_validation ():#line:209
    try :#line:210
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:211
    except Exception as O00O0000OOO000O00 :#line:212
        sys .exit (0 )#line:213
def update_the_validation ():#line:217
    try :#line:218
        O0O0O00OO0OO0OOOO =gitee_validation ()#line:219
        if version_of_the_validation ()<O0O0O00OO0OO0OOOO ['SwimUpM']['edition']:#line:220
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00OO0OO0OOOO["SwimUpM"]["edition"]}   ❌')#line:221
            print (f'更新内容=>>{O0O0O00OO0OO0OOOO["SwimUpM"]["content"]}   👍')#line:222
        else :#line:223
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0O0O00OO0OO0OOOO["SwimUpM"]["edition"]}   ✅')#line:224
            print (f'更新内容=>> {O0O0O00OO0OO0OOOO["SwimUpM"]["content"]}   👍')#line:225
    except Exception as OO00O0O0000O0OO0O :#line:226
        print (OO00O0O0000O0OO0O )#line:227
def os_qinglong ():#line:230
    if application in os .environ :#line:231
        O00OO000OO0O0OOOO =os .environ [application ].split ('\n')#line:232
        if len (O00OO000OO0O0OOOO )>0 :#line:233
            return O00OO000OO0O0OOOO #line:234
        else :#line:235
            print (f"{application}变量未启用")#line:236
            print ('脚本退出')#line:237
            sys .exit (1 )#line:238
    else :#line:239
        print (f"{application}变量为空\n尝试使用内置变量")#line:240
        return os_built ()#line:241
def os_built ():#line:244
    if token :#line:245
        O0000O0O0O00OOOO0 =token .split ('\n')#line:246
        if len (O0000O0O0O00OOOO0 )>0 :#line:247
            return O0000O0O0O00OOOO0 #line:248
    else :#line:249
        print (f"内置变量为空")#line:250
        print ('脚本退出')#line:251
        sys .exit (0 )#line:252
if __name__ =='__main__':#line:255
    start ()#line:256
