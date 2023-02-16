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
抓取  https://api.shimiyou.com 的Http-X-Authentication-Token的值
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
        OO0O000OO0OO00O0O =os_qinglong ()#line:7
        print (f"==========共找到{len(OO0O000OO0OO00O0O)}个账号==========")#line:8
        for OOO0OOOO00OOO000O in OO0O000OO0OO00O0O :#line:9
            print (f"------------正在执行第{OO0O000OO0OO00O0O.index(OOO0OOOO00OOO000O) + 1}个账号------------")#line:10
            O000OO00000OOOO00 =SwimUpM (OOO0OOOO00OOO000O )#line:11
            if O000OO00000OOOO00 .base_info ():#line:13
                if bundled :#line:14
                    O000OO00000OOOO00 .friend_center ()#line:16
                O000OO00000OOOO00 .lottery_activities ()#line:18
                O000OO00000OOOO00 .user_lottery_activity_records ()#line:20
                O000OO00000OOOO00 .lottery_center_index ()#line:22
                if O000OO00000OOOO00 .tickets :#line:23
                    O000OO00000OOOO00 .tickets_give ()#line:25
                time .sleep (random .randint (8 ,15 ))#line:26
            else :#line:27
                print ('token失效')#line:28
        print (f"------------所有账号运行完毕正在统计每天收益------------")#line:29
        print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:30
    except Exception as O0OOOOO0OO0OOO0O0 :#line:31
        print (O0OOOOO0OO0OOO0O0 )#line:32
class SwimUpM :#line:34
    def __init__ (O0OOO0OO0OOOOOOOO ,O000O0OO0OO000O0O ):#line:36
        try :#line:37
            O0OOO0OO0OOOOOOOO .giving =O000O0OO0OO000O0O .split ("@")[1 ]#line:38
            O0OOO0OO0OOOOOOOO .tickets =O000O0OO0OO000O0O .split ("@")[2 ]#line:39
            O0OOO0OO0OOOOOOOO .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':O000O0OO0OO000O0O .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'api.shimiyou.com','Cookie':f'AuthenticationToken={O000O0OO0OO000O0O.split("@")[0]}',}#line:40
        except Exception as OOOOO0OO0OO0000OO :#line:41
            print ('变量格式错误')#line:42
    def base_info (O0O0000O0OO0OOOO0 ):#line:45
        try :#line:46
            OOOOO0O0O0O00OO0O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O0O0000O0OO0OOOO0 .headers ).json ()#line:47
            if 'code'in OOOOO0O0O0O00OO0O :#line:49
                return False #line:50
            if 'id'in OOOOO0O0O0O00OO0O :#line:51
                OO00OO0OOOO0OO0O0 =OOOOO0O0O0O00OO0O ['nick_name']#line:52
                O0O00O000O000OO00 =OOOOO0O0O0O00OO0O ['card_no']#line:53
                OO00OOO0OO0OO00O0 =str (O0O00O000O000OO00 )[4 :5 ]+'**'+str (O0O00O000O000OO00 )[7 :]#line:54
                OO00OOOO0O0O00O0O =OOOOO0O0O0O00OO0O ['ticket']['count']#line:55
                try :#line:56
                    if reversed (OO00OOOO0O0O00O0O )!=0 :#line:57
                        OO00OOOO0O0O00O0O =str (OO00OOOO0O0O00O0O )[:6 ]#line:58
                    else :#line:59
                        OO00OOOO0O0O00O0O =0 #line:60
                except :#line:61
                    OO00OOOO0O0O00O0O =0 #line:62
                print (f'【账号信息】：ID:{OO00OOO0OO0OO00O0}丨昵称:{OO00OO0OOOO0OO0O0[:7]}丨游票:{OO00OOOO0O0O00O0O}')#line:63
            return True #line:76
        except Exception as O00000OOO0O0O000O :#line:77
            print (O00000OOO0O0O000O )#line:78
    def friend_center (O000O0O0000OO0OOO ):#line:82
        O00OO00OO00OO0O00 =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =O000O0O0000OO0OOO .headers ).json ()#line:83
        if 'parent_user'in O00OO00OO00OO0O00 :#line:84
            if O00OO00OO00OO0O00 ['parent_user']:#line:85
                pass #line:86
            else :#line:87
                OOO0O00OO0O0O0O0O ={"id":bundled_def ()}#line:88
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =O000O0O0000OO0OOO .headers ,data =OOO0O00OO0O0O0O0O ).json ()#line:89
    def user_lottery_activity_records (O000OO000OOOOO0O0 ):#line:92
        global cumulative_ticket #line:93
        OOO000O0O00OO0O0O =0 #line:94
        O00O000O0OOOO00O0 =0 #line:95
        try :#line:96
            OO0O0000O000O0O0O =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =O000OO000OOOOO0O0 .headers ).json ()#line:97
            if 'user_lottery_activity_records'in OO0O0000O000O0O0O :#line:98
                for OOOO000OO0OO0OO00 in OO0O0000O000O0O0O ['user_lottery_activity_records']:#line:99
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==OOOO000OO0OO0OO00 ['lottery_activity_id']:#line:100
                        OOO000O0O00OO0O0O =OOOO000OO0OO0OO00 ['bet_on']#line:101
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==OOOO000OO0OO0OO00 ['lottery_activity_id']:#line:102
                        O00O000O0OOOO00O0 =OOOO000OO0OO0OO00 ['bet_on']#line:103
                print (f'【参与抽奖】：普通奖券:{O00O000O0OOOO00O0}张丨高级奖券:{OOO000O0O00OO0O0O}张')#line:104
            if 'lottery_activity'in OO0O0000O000O0O0O :#line:105
                for OOOO000OO0OO0OO00 in OO0O0000O000O0O0O ['lottery_activity']:#line:106
                    if OOOO000OO0OO0OO00 ['topic']=='普通奖券抽游票':#line:107
                        O00OOOO00OO000O00 =OOOO000OO0OO0OO00 ['sum_bet_on']#line:108
                        OOO00OO00OO000000 =2880 *34 /O00OOOO00OO000O00 *O00O000O0OOOO00O0 #line:109
                        cumulative_ticket +=OOO00OO00OO000000 #line:110
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(OOO00OO00OO000000)[:5]}')#line:111
                    if OOOO000OO0OO0OO00 ['topic']=='高级奖券抽游票':#line:112
                        O00OOOO00OO000O00 =OOOO000OO0OO0OO00 ['sum_bet_on']#line:113
                        OOO00OO00OO000000 =2880 *313 /O00OOOO00OO000O00 *OOO000O0O00OO0O0O #line:114
                        cumulative_ticket +=OOO00OO00OO000000 #line:115
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(OOO00OO00OO000000)[:5]}')#line:116
        except Exception as OOOO00OO0OO0OOOO0 :#line:118
            print (OOOO00OO0OO0OOOO0 )#line:119
    def tickets_give (O000OOO0O000O0000 ):#line:123
        try :#line:124
            OOOO0OO0O0OO0000O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O000OOO0O000O0000 .headers ).json ()#line:125
            O0O0O00O000OOOOO0 =str (OOOO0OO0O0OO0000O ['card_no'])[4 :]#line:126
            if O000OOO0O000O0000 .giving !=O0O0O00O000OOOOO0 :#line:127
                O00OO0O0OOOOO0OOO =OOOO0OO0O0OO0000O ['ticket']['count']#line:128
                if float (O00OO0O0OOOOO0OOO )==0 :#line:129
                    print ('【赠送游票】：账号初始化中')#line:130
                    return True #line:131
                OOO00OO0O00O00O0O =str (O00OO0O0OOOOO0OOO ).split ('.')[0 ]#line:132
                OOOOO0000O0000O00 =int (str ((float (OOO00OO0O00O00O0O )/1.1 )/10 ).split (".")[0 ])*10 #line:133
                if int (OOO00OO0O00O00O0O )>10 :#line:134
                    OOO0O00OOOO0O0OO0 ={"id":O000OOO0O000O0000 .giving ,"count":OOOOO0000O0000O00 }#line:135
                    O00O0O00O0O0000O0 =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =O000OOO0O000O0000 .headers ,data =OOO0O00OOOO0O0OO0 ).json ()#line:136
                    if 'count'in O00O0O00O0O0000O0 :#line:137
                        print (f'【赠送游票】：赠送{OOOOO0000O0000O00}张游票给{O000OOO0O000O0000.giving}成功丨余额{str(O00O0O00O0O0000O0["count"])[:5]}')#line:138
                    else :#line:139
                        print ('【赠送游票】：失败')#line:140
                else :#line:141
                    print ('【赠送游票】：余额不足不执行操作')#line:142
            else :#line:143
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:144
        except Exception as OO0OOOO000OOO000O :#line:145
            print (OO0OOOO000OOO000O )#line:146
    def lottery_activities (O00O0OO0OOO0O0OO0 ):#line:150
        try :#line:151
            O00O0OO0O000O0O0O =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OO0OOO0O0OO0 .headers ).json ()#line:152
            if 'count'in O00O0OO0O000O0O0O :#line:154
                OOO0O00OOO0OO00O0 =O00O0OO0O000O0O0O ['count']#line:155
                print (f'【转盘抽奖】：剩余{OOO0O00OOO0OO00O0}次抽奖')#line:156
                if OOO0O00OOO0OO00O0 >0 :#line:157
                    for OO0OO0O000O0OO0OO in range (OOO0O00OOO0OO00O0 ):#line:158
                        O0OO0O0OOOOO00OO0 =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O00O0OO0OOO0O0OO0 .headers ).json ()#line:159
                        if 'name'in O0OO0O0OOOOO00OO0 :#line:160
                            print (f'【转盘抽奖】：获得:{O0OO0O0OOOOO00OO0["name"]}{O0OO0O0OOOOO00OO0["prize_number"]}张')#line:161
                        time .sleep (random .randint (15 ,30 )/10 )#line:162
        except Exception as O0O0OO0O000000OOO :#line:163
            print (O0O0OO0O000000OOO )#line:164
    def lottery_center_index (OO0000O00OO0O0OOO ):#line:168
        try :#line:169
            OOOOOOOOO000O0OO0 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =OO0000O00OO0O0OOO .headers ).json ()#line:170
            if 'tickets'in OOOOOOOOO000O0OO0 :#line:171
                for OOO00O0000O0O00O0 in OOOOOOOOO000O0OO0 ['tickets']:#line:172
                    if OOO00O0000O0O00O0 ['name']=='游票':#line:173
                        print (f'【抽奖累计】：累计中了{str(OOO00O0000O0O00O0["total_count"])[:6]}张游票')#line:174
            if 'cumulative_tickets'in OOOOOOOOO000O0OO0 :#line:175
                if OOOOOOOOO000O0OO0 ['tickets']:#line:176
                    for OOO00O0000O0O00O0 in OOOOOOOOO000O0OO0 ['tickets']:#line:177
                        O0OO000O00O00OO00 =OOO00O0000O0O00O0 ['count']#line:178
                        O0000OOO0000O0O0O =OOO00O0000O0O00O0 ['lt_type']#line:179
                        if O0000OOO0000O0O0O =='normal':#line:180
                            O0OO00O0OOOOOO00O ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:181
                            if O0OO000O00O00OO00 >'1':#line:182
                                OO0000O00OO0O0OOO .add_lottery_ticket (O0OO000O00O00OO00 ,O0OO00O0OOOOOO00O )#line:183
                                time .sleep (2 )#line:184
                        if O0000OOO0000O0O0O =='advanced':#line:185
                            O0OO00O0OOOOOO00O ='7a468d93-aa43-4131-b414-b828b985e97e'#line:186
                            if O0OO000O00O00OO00 >'1':#line:187
                                OO0000O00OO0O0OOO .add_lottery_ticket (O0OO000O00O00OO00 ,O0OO00O0OOOOOO00O )#line:188
        except Exception as O00000000OOO0O0O0 :#line:189
            print (O00000000OOO0O0O0 )#line:190
    def add_lottery_ticket (O0O0OO00OOO0O00O0 ,OOOOO000O0000OOOO ,O0O0000OOO0OOO000 ):#line:194
        try :#line:195
            OO00OO0000O0OO0OO ={"bet_on":OOOOO000O0000OOOO .split ('.')[0 ],"operation":"in","lotteru_activity_id":O0O0000OOO0OOO000 }#line:196
            O0OOOOO00OOOO0OO0 =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =O0O0OO00OOO0O00O0 .headers ,data =OO00OO0000O0OO0OO ).json ()#line:197
            if 'bet_on'in O0OOOOO00OOOO0OO0 :#line:198
                print (f'【添加奖券】：添加{OOOOO000O0000OOOO.split(".")[0]}张成功')#line:199
        except Exception as O0O0O0O0O00OOOOO0 :#line:200
            print (O0O0O0O0O00OOOOO0 )#line:201
def version_of_the_validation ():#line:205
    return str ((60 -56 )/10 )#line:206
def gitee_validation ():#line:208
    try :#line:209
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:210
    except Exception as O0OOO00OOO0OOO000 :#line:211
        sys .exit (0 )#line:212
def update_the_validation ():#line:216
    try :#line:217
        O0000OO00O0000OOO =gitee_validation ()#line:218
        if version_of_the_validation ()<O0000OO00O0000OOO ['SwimUpM']['edition']:#line:219
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OO00O0000OOO["SwimUpM"]["edition"]}   ❌')#line:220
            print (f'更新内容=>>{O0000OO00O0000OOO["SwimUpM"]["content"]}   👍')#line:221
        else :#line:222
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {O0000OO00O0000OOO["SwimUpM"]["edition"]}   ✅')#line:223
            print (f'更新内容=>> {O0000OO00O0000OOO["SwimUpM"]["content"]}   👍')#line:224
    except Exception as O0O0OOOO0O0O00O0O :#line:225
        print (O0O0OOOO0O0O00O0O )#line:226
def os_qinglong ():#line:229
    if application in os .environ :#line:230
        OO00000O0O00O00OO =os .environ [application ].split ('\n')#line:231
        if len (OO00000O0O00O00OO )>0 :#line:232
            return OO00000O0O00O00OO #line:233
        else :#line:234
            print (f"{application}变量未启用")#line:235
            print ('脚本退出')#line:236
            sys .exit (1 )#line:237
    else :#line:238
        print (f"{application}变量为空\n尝试使用内置变量")#line:239
        return os_built ()#line:240
def os_built ():#line:243
    if token :#line:244
        OO0OOOO0O00O0OO0O =token .split ('\n')#line:245
        if len (OO0OOOO0O00O0OO0O )>0 :#line:246
            return OO0OOOO0O00O0OO0O #line:247
    else :#line:248
        print (f"内置变量为空")#line:249
        print ('脚本退出')#line:250
        sys .exit (0 )#line:251
if __name__ =='__main__':#line:254
    start ()#line:255
