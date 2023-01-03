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
青龙变量 export smytoken="token@赠送游票ID@True"   
第三个参数是开启赠送功能    默认每次赠送10票，需要修改在145行  多号换行
"""


application = 'smytoken'    # 变量名
bundled = True              # 是否绑定邀请码
count_mew = 10              # 默认每次赠送10      10的整数手续费最划算
token = ''                  # 调试token



# 绑定上级ID  随机绑就多填   不需要1000
def bundled_def():
    bundled_id_new = ['33162', '41727']
    return bundled_id_new[random.randint(0, len(bundled_id_new) - 1)]

cumulative_ticket =0 #line:2
host ='https://mijia-api.imijiakeji.com'#line:3
git ='https://gitee.com'#line:4
mobile =0 #line:5
def start ():#line:6
    try :#line:7
        if update_the_validation ():#line:8
            OOOO0O00000O0OOO0 =os_qinglong ()#line:9
            print (f"==========共找到{len(OOOO0O00000O0OOO0)}个账号==========")#line:10
            for OO0OOOOO0OOOO0OOO in OOOO0O00000O0OOO0 :#line:11
                print (f"------------正在执行第{OOOO0O00000O0OOO0.index(OO0OOOOO0OOOO0OOO) + 1}个账号------------")#line:12
                O0O00O000O0OOO00O =SwimUpM (OO0OOOOO0OOOO0OOO )#line:13
                if O0O00O000O0OOO00O .base_info ():#line:15
                    if bundled :#line:16
                        O0O00O000O0OOO00O .friend_center ()#line:18
                    O0O00O000O0OOO00O .lottery_activities ()#line:20
                    O0O00O000O0OOO00O .user_lottery_activity_records ()#line:22
                    O0O00O000O0OOO00O .lottery_center_index ()#line:24
                    if O0O00O000O0OOO00O .tickets :#line:25
                        O0O00O000O0OOO00O .tickets_give ()#line:27
                    time .sleep (random .randint (8 ,15 ))#line:28
                else :#line:29
                    print ('token失效')#line:30
            print (f"------------所有账号运行完毕正在统计每天收益------------")#line:31
            print (f'【每天收益】：所有账号累计每天能中:{str(cumulative_ticket)[:6]}张游票')#line:32
    except Exception as O000O0OO0O00OO00O :#line:33
        print (O000O0OO0O00OO00O )#line:34
class SwimUpM :#line:36
    def __init__ (O000000000O0OO0OO ,O00000OO0OO0OOO00 ):#line:38
        try :#line:39
            O000000000O0OO0OO .giving =O00000OO0OO0OOO00 .split ("@")[1 ]#line:40
            O000000000O0OO0OO .tickets =O00000OO0OO0OOO00 .split ("@")[2 ]#line:41
            O000000000O0OO0OO .headers ={'Authorization':'Basic bWlqaWF5b3U6NnpXa3l3ZmtmZ1NyVmNQdQ==','Http-X-Authentication-Token':O00000OO0OO0OOO00 .split ("@")[0 ],'user-agent':'Mozilla/5.0 (Linux; Android 12; 2201122C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/30.857143)','Host':'mijia-api.imijiakeji.com',}#line:42
        except Exception as OO000OOO0O0OO0OOO :#line:43
            print ('变量格式错误')#line:44
    def base_info (O0OOO0OO0000O000O ):#line:47
        global mobile #line:48
        try :#line:49
            O00OOOO0000OO0O0O =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O0OOO0OO0000O000O .headers ).json ()#line:50
            if 'code'in O00OOOO0000OO0O0O :#line:51
                return False #line:52
            if 'mobile'in O00OOOO0000OO0O0O :#line:53
                if O00OOOO0000OO0O0O ['mobile']:#line:54
                    mobile =O00OOOO0000OO0O0O ['mobile']#line:55
                else :#line:56
                    mobile ='None'#line:57
            if 'id'in O00OOOO0000OO0O0O :#line:58
                OO000O00OOO0OO0OO =O00OOOO0000OO0O0O ['nick_name']#line:59
                OOO00OOO0OOOO0OOO =O00OOOO0000OO0O0O ['card_no']#line:60
                O0OOO0O00O0O0O0OO =str (OOO00OOO0OOOO0OOO )[4 :5 ]+'**'+str (OOO00OOO0OOOO0OOO )[7 :]#line:61
                OOOOOOO0O00O000OO =O00OOOO0000OO0O0O ['ticket']['count']#line:62
                try :#line:63
                    if reversed (OOOOOOO0O00O000OO )!=0 :#line:64
                        OOOOOOO0O00O000OO =str (OOOOOOO0O00O000OO ).split ('.')[0 ]#line:65
                    else :#line:66
                        OOOOOOO0O00O000OO =0 #line:67
                except :#line:68
                    OOOOOOO0O00O000OO =0 #line:69
                print (f'【账号信息】：ID:{O0OOO0O00O0O0O0OO}丨昵称:{OO000O00OOO0OO0OO[:7]}丨游票:{OOOOOOO0O00O000OO}')#line:70
                O0O0OO000OO00OO00 =re .findall ('/avatar(.*?).jpg',O00OOOO0000OO0O0O ['avatar']['url'])[0 ].split ('avatar')[1 ].split ('-')#line:71
                OOO0OOOOO00O0O000 =O0O0OO000OO00OO00 [0 ]#line:72
                OOO0OO000OO00OO0O =(datetime .datetime .now ()-datetime .datetime (int (OOO0OOOOO00O0O000 [:4 ]),int (OOO0OOOOO00O0O000 [4 :6 ]),int (OOO0OOOOO00O0O000 [6 :]))).days #line:74
                print (f'【注册绑定】：注册:{OOO0OOOOO00O0O000[:4]}-{OOO0OOOOO00O0O000[4:6]}-{OOO0OOOOO00O0O000[6:]}丨距今:{OOO0OO000OO00OO0O}天丨绑定:{mobile[7:]}')#line:75
                return True #line:76
            return True #line:77
        except Exception as OOO0OOOOO00000OOO :#line:78
            print (OOO0OOOOO00000OOO )#line:79
    def friend_center (OOOOOO0000000000O ):#line:83
        OOO0O00O00OOOO00O =requests .request ('get',f'{host}/app_user/v1/friend_center/index',headers =OOOOOO0000000000O .headers ).json ()#line:84
        if 'parent_user'in OOO0O00O00OOOO00O :#line:85
            if OOO0O00O00OOOO00O ['parent_user']:#line:86
                pass #line:87
            else :#line:88
                O0O0O000O0O00OO00 ={"id":bundled_def ()}#line:89
                requests .request ('put',f'{host}/app_user/v1/users/ancestry',headers =OOOOOO0000000000O .headers ,data =O0O0O000O0O00OO00 ).json ()#line:90
    def user_lottery_activity_records (OO0O0O0O000O00O00 ):#line:93
        global cumulative_ticket #line:94
        O0O0OO000OO00O0O0 =0 #line:95
        O0O000OOOOOO00O0O =0 #line:96
        try :#line:97
            O0OOOOOOOOO0000O0 =requests .request ('get',f'{host}/app_user/v1/users/user_lottery_activity_records?page=1&per_page=20',headers =OO0O0O0O000O00O00 .headers ).json ()#line:98
            if 'user_lottery_activity_records'in O0OOOOOOOOO0000O0 :#line:99
                for OOOOO000000O000OO in O0OOOOOOOOO0000O0 ['user_lottery_activity_records']:#line:100
                    if '7a468d93-aa43-4131-b414-b828b985e97e'==OOOOO000000O000OO ['lottery_activity_id']:#line:101
                        O0O0OO000OO00O0O0 =OOOOO000000O000OO ['bet_on']#line:102
                    if '94437862-d71c-4ff9-b2ff-343b094acd0d'==OOOOO000000O000OO ['lottery_activity_id']:#line:103
                        O0O000OOOOOO00O0O =OOOOO000000O000OO ['bet_on']#line:104
                print (f'【参与抽奖】：普通奖券:{O0O000OOOOOO00O0O}张丨高级奖券:{O0O0OO000OO00O0O0}张')#line:105
            if 'lottery_activity'in O0OOOOOOOOO0000O0 :#line:106
                for OOOOO000000O000OO in O0OOOOOOOOO0000O0 ['lottery_activity']:#line:107
                    if OOOOO000000O000OO ['topic']=='普通奖券抽游票':#line:108
                        OO00O0O0OOO0OO0O0 =OOOOO000000O000OO ['sum_bet_on']#line:109
                        O0000OOOO0O000OOO =2880 *34 /OO00O0O0OOO0OO0O0 *O0O000OOOOOO00O0O #line:110
                        cumulative_ticket +=O0000OOOO0O000OOO #line:111
                        print (f'【参与抽奖】：普通奖券预计每天能中:{str(O0000OOOO0O000OOO)[:5]}')#line:112
                    if OOOOO000000O000OO ['topic']=='高级奖券抽游票':#line:113
                        OO00O0O0OOO0OO0O0 =OOOOO000000O000OO ['sum_bet_on']#line:114
                        O0000OOOO0O000OOO =2880 *313 /OO00O0O0OOO0OO0O0 *O0O0OO000OO00O0O0 #line:115
                        cumulative_ticket +=O0000OOOO0O000OOO #line:116
                        print (f'【参与抽奖】：高级奖券预计每天能中:{str(O0000OOOO0O000OOO)[:5]}')#line:117
        except Exception as O00O0O000O0O0O00O :#line:119
            print (O00O0O000O0O0O00O )#line:120
    def tickets_give (O0O0OO0O00OO00000 ):#line:124
        try :#line:125
            O0O000OO0OOOOO0O0 =requests .request ('get',f'{host}/app_user/v1/users/base_info',headers =O0O0OO0O00OO00000 .headers ).json ()#line:126
            OO0O0O0O00OO00OO0 =str (O0O000OO0OOOOO0O0 ['card_no'])[4 :]#line:127
            if O0O0OO0O00OO00000 .giving !=OO0O0O0O00OO00OO0 :#line:128
                OOOOO00000OOOO000 =O0O000OO0OOOOO0O0 ['ticket']['count']#line:129
                if float (OOOOO00000OOOO000 )==0 :#line:130
                    print ('【赠送游票】：账号初始化中')#line:131
                    return True #line:132
                O000OOO00OO0O0000 =str (OOOOO00000OOOO000 ).split ('.')[0 ]#line:133
                if int (O000OOO00OO0O0000 )>count_mew :#line:134
                    O0O0OO0OO0O0O0000 ={"id":O0O0OO0O00OO00000 .giving ,"count":count_mew }#line:135
                    OO000O0OO0000OO0O =requests .put (f'{host}/app_user/v1/ticket_record/tickets_give',headers =O0O0OO0O00OO00000 .headers ,data =O0O0OO0OO0O0O0000 ).json ()#line:136
                    if 'count'in OO000O0OO0000OO0O :#line:137
                        print (f'【赠送游票】：赠送10张游票给{O0O0OO0O00OO00000.giving}成功丨余额{str(OO000O0OO0000OO0O["count"])[:5]}')#line:138
                    else :#line:139
                        print ('【赠送游票】：失败')#line:140
                else :#line:141
                    print ('【赠送游票】：余额不足不执行操作')#line:142
            else :#line:143
                print ('【赠送游票】：赠送的ID是自己不执行操作')#line:144
        except Exception as OO0O000OO0O0O0000 :#line:145
            print (OO0O000OO0O0O0000 )#line:146
    def lottery_activities (O0O0000000OOOO0O0 ):#line:150
        try :#line:151
            OOO0000OOOOO00000 =requests .request ('get',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O0O0000000OOOO0O0 .headers ).json ()#line:152
            if 'count'in OOO0000OOOOO00000 :#line:153
                OOOO0OO0OO00O0000 =OOO0000OOOOO00000 ['count']#line:154
                print (f'【转盘抽奖】：剩余{OOOO0OO0OO00O0000}次抽奖')#line:155
                if OOOO0OO0OO00O0000 >0 :#line:156
                    for OO0O000O00O0OOOO0 in range (OOOO0OO0OO00O0000 ):#line:157
                        O0O000OOOO000OOO0 =requests .request ('post',f'{host}/app_user/v1/lottery_activities/lt_type/lottery/info',headers =O0O0000000OOOO0O0 .headers ).json ()#line:158
                        if 'name'in O0O000OOOO000OOO0 :#line:159
                            print (f'【转盘抽奖】：获得:{O0O000OOOO000OOO0["name"]}{O0O000OOOO000OOO0["prize_number"]}张')#line:160
                        time .sleep (random .randint (15 ,30 )/10 )#line:161
        except Exception as OOOO00OOOO0O0000O :#line:162
            print (OOOO00OOOO0O0000O )#line:163
    def lottery_center_index (OO0O0000OO00O00O0 ):#line:167
        try :#line:168
            OO0O000OOO000OO00 =requests .request ('get',f'{host}/app_user/v1/lottery_center/index?page=1&per_page=20',headers =OO0O0000OO00O00O0 .headers ).json ()#line:169
            if 'tickets'in OO0O000OOO000OO00 :#line:170
                for O0OO0O000000OO0OO in OO0O000OOO000OO00 ['tickets']:#line:171
                    if O0OO0O000000OO0OO ['name']=='游票':#line:172
                        print (f'【抽奖累计】：累计中了{str(O0OO0O000000OO0OO["total_count"])[:6]}张游票')#line:173
            if 'cumulative_tickets'in OO0O000OOO000OO00 :#line:174
                if OO0O000OOO000OO00 ['tickets']:#line:175
                    for O0OO0O000000OO0OO in OO0O000OOO000OO00 ['tickets']:#line:176
                        OO00000OOO0O000O0 =O0OO0O000000OO0OO ['count']#line:177
                        OOO000OO00O00OOOO =O0OO0O000000OO0OO ['lt_type']#line:178
                        if OOO000OO00O00OOOO =='normal':#line:179
                            OOO0OOOOOO0O00O00 ='94437862-d71c-4ff9-b2ff-343b094acd0d'#line:180
                            if OO00000OOO0O000O0 >'1':#line:181
                                OO0O0000OO00O00O0 .add_lottery_ticket (OO00000OOO0O000O0 ,OOO0OOOOOO0O00O00 )#line:182
                                time .sleep (2 )#line:183
                        if OOO000OO00O00OOOO =='advanced':#line:184
                            OOO0OOOOOO0O00O00 ='7a468d93-aa43-4131-b414-b828b985e97e'#line:185
                            if OO00000OOO0O000O0 >'1':#line:186
                                OO0O0000OO00O00O0 .add_lottery_ticket (OO00000OOO0O000O0 ,OOO0OOOOOO0O00O00 )#line:187
        except Exception as OOOOO0OO000O0OO00 :#line:188
            print (OOOOO0OO000O0OO00 )#line:189
    def add_lottery_ticket (O0O0OOO0O0O0OOOO0 ,OOO00OOOO0OOOO000 ,OO0000OO000O0000O ):#line:193
        try :#line:194
            OOO00OOOOOO00OO0O ={"bet_on":OOO00OOOO0OOOO000 .split ('.')[0 ],"operation":"in","lotteru_activity_id":OO0000OO000O0000O }#line:195
            O00O0O00O0O0O0OOO =requests .request ('post',f'{host}/app_user/v1/lottery_center/activities',headers =O0O0OOO0O0O0OOOO0 .headers ,data =OOO00OOOOOO00OO0O ).json ()#line:196
            if 'bet_on'in O00O0O00O0O0O0OOO :#line:197
                print (f'【添加奖券】：添加{OOO00OOOO0OOOO000.split(".")[0]}张成功')#line:198
        except Exception as O0O0O00000000O000 :#line:199
            print (O0O0O00000000O000 )#line:200
def version_of_the_validation ():#line:204
    return str ((57 -56 )/10 )#line:205
def gitee_validation ():#line:207
    try :#line:208
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:209
    except Exception as OO0OOO0OOOO0000OO :#line:210
        sys .exit (0 )#line:211
def update_the_validation ():#line:215
    try :#line:216
        OO000OOOO00000OOO =gitee_validation ()#line:217
        if version_of_the_validation ()<OO000OOOO00000OOO ['SwimUpM']['edition']:#line:218
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OOOO00000OOO["SwimUpM"]["edition"]}   ❌')#line:219
            print (f'更新内容=>>{OO000OOOO00000OOO["SwimUpM"]["content"]}   👍')#line:220
        else :#line:221
            print (f'当前版本=>> {version_of_the_validation()}'+f'丨远程版本=>> {OO000OOOO00000OOO["SwimUpM"]["edition"]}   ✅')#line:222
            print (f'更新内容=>> {OO000OOOO00000OOO["SwimUpM"]["content"]}   👍')#line:223
            return True #line:224
    except Exception as O000O0000O0O0O0O0 :#line:225
        print (O000O0000O0O0O0O0 )#line:226
def os_qinglong ():#line:229
    if application in os .environ :#line:230
        OOOOOO00OOOO0OO00 =os .environ [application ].split ('\n')#line:231
        if len (OOOOOO00OOOO0OO00 )>0 :#line:232
            return OOOOOO00OOOO0OO00 #line:233
        else :#line:234
            print (f"{application}变量未启用")#line:235
            print ('脚本退出')#line:236
            sys .exit (1 )#line:237
    else :#line:238
        print (f"{application}变量为空\n尝试使用内置变量")#line:239
        return os_built ()#line:240
def os_built ():#line:243
    if token :#line:244
        OOO00OOOO0000OO00 =token .split ('\n')#line:245
        if len (OOO00OOOO0000OO00 )>0 :#line:246
            return OOO00OOOO0000OO00 #line:247
    else :#line:248
        print (f"内置变量为空")#line:249
        print ('脚本退出')#line:250
        sys .exit (0 )#line:251
if __name__ =='__main__':#line:254
    start ()#line:255

