# coding: utf-8
try:
    import requests, json, base64, re, random, rsa, sys, datetime, threading, time
    from rsa import core, PublicKey, transform
    from Crypto.Cipher import AES
    from world_city_data import sjc_new
    from decimal import Decimal
    from notify import send
except Exception as e:
    t = re.findall("d '(.*?)'", str(e))[0]
    print(f'{t}依赖或者配置文件未安装未安装')
    sys.exit()
"""
@ Zzzz
@ 脚本仅供学习查阅切勿传播
@ 请下载后24小时内删除
@ 下载链接微信打开  http://share.lucklyworld.cn/wx/s?_co=917627&_st=xiao&_v=v4
@ 账号配置在 world_city_data.py    文件里面
@ 先看懂下面的配置信息、不要什么都问、问我也不知道、不知道怎么设置就默认
@ 版本 1.4
@ cron: */10 * * * *
@ new Env('世界城打工')
@ 功能: 自动选择回报趋势最高行业打工、手动选择区域行业打工、特定时间段立即醒来打工、购买食物水、卖砖头给平台、体力低于20睡觉、自定义打工时间、预留食物水数量精力、升级职业、转账
"""

#################################执行设置#################################
time_xx = random.randint(8, 12)          # 秒 执行下一个号的时间  8到12秒中随机延迟执行
#################################执行设置#################################
#################################打工设置#################################
start_work = '25'                        # 打工时间 多时间段用#隔开 2#5#8#18    全天打工写'25'
immediately_time = '2#3#4#5#6'           # 立即醒来去打工时间    2#5#8#18
immediately = False                      # 立即醒来去打工      True为醒来     False为不醒
areaId = '1'                             # 打工区域  1是郊区    2是工业区   3是商业区   4是高薪区   5是金融区
jobId = '1'                              # 打工行业  1是农业    2是加工业   3是制造业    4是商业
jobIda = False                            # 自动选择回报趋势最高的行业打工     True为自动选择     False为手动选择
jobIds = '-1'                            # 回报趋势  -1是什么时候都打工  不会填就填-1    只要高回报填-0.01最好
physical_power = '500'                    # 设置体力大于这个数才打工，小于就睡觉
energy = '400'                           # 留精力数量 不够自动购买
#################################打工设置#################################
#################################食物设置#################################
prop_food = 1800                         # 食物id  1000是面包    1200是薯条     1400是汉堡     1600是蛋糕     1800是臭豆腐
prop_water = 3800                        # 水id   3000是热水    3200是牛奶     3400是可乐     3600是啤酒     3800是烈酒
prop_water_food = '5'                    # 预留食物和水数量  预留不得低于3个
pre_order = False                        # 预购食物水  背包没有选择食物和水的物品时打开购买  背包有食物或者打开运行了俩次就不要打开了   True 打开  False 关闭
#################################食物设置#################################
#################################砖头设置#################################
prop_brick = True                       # 卖砖块 True 卖  ，  False 不卖
recycling_way = '1'                       # 1为回收      2为交换所出售
#################################砖头设置#################################
#################################显示设置#################################
knapsack = False                         # 背包显示物品  日志是否显示背包物品信息 True显示  False不显示
#################################显示设置#################################
#################################升级职业设置#################################
jobId_upgrade = '1'                      # 升级职业 1 农民 2 加工师 3 商人 4 制造师
upgrade = True                          # 是否升级我的职业  True升级  False不升级    需要提前升级1次
#################################升级职业设置#################################
#################################转账设置#################################
omg = 50  # 单位个   转账数量大于就会转,不转币最好设置9999999
#################################转账设置#################################

################################################下面的不要动#########################################################
vi ='20407'#line:1
version ='2.4.7'#line:2
host ='https://android-api.lucklyworld.com'#line:3
git ='https://gitee.com'#line:4
def main ():#line:7
    try :#line:8
        WorldCity (sjc_new [0 ]).sjc_ok ()#line:9
        print (f"================共找到{len(sjc_new)}个账号================")#line:10
        for O0OO0OOO000OOOOOO in sjc_new :#line:11
            print (f"-------------------正在执行第{sjc_new.index(O0OO0OOO000OOOOOO) + 1}个账号-------------------")#line:12
            O000O000O00O00OOO =WorldCity (O0OO0OOO000OOOOOO )#line:14
            def O0OOOO0O0O000O0O0 ():#line:15
                O00OOOO0OOO0OOO0O =O000O000O00O00OOO .home ()#line:17
                if O00OOOO0OOO0OOO0O =='失效':#line:18
                    print ('账号信息:    ID:%s'%O0OO0OOO000OOOOOO ['uid']+'丨网络限制或者失效')#line:19
                    return False #line:20
                if O00OOOO0OOO0OOO0O !='打工中':#line:21
                    if pre_order :#line:22
                        print ('我打开了')#line:24
                        O000O000O00O00OOO .pre_order ()#line:25
                    if upgrade :#line:26
                        O000O000O00O00OOO .work_upgrade ()#line:28
                    O000O000O00O00OOO .company ()#line:30
                    if O000O000O00O00OOO .work_bag ():#line:32
                        pass #line:33
                    else :#line:34
                        if str (datetime .datetime .now ().hour )in start_work .split ('#')or '25'in start_work .split ('#'):#line:35
                            O000O000O00O00OOO .work_start ()#line:37
                        else :#line:38
                            O000O000O00O00OOO .work_sleep ()#line:39
                    O000O000O00O00OOO .work_log ()#line:41
                    O000O000O00O00OOO .transfer (O000O000O00O00OOO .emoji_coins ())#line:43
                elif O00OOOO0OOO0OOO0O =='打工中':#line:44
                    print (O00OOOO0OOO0OOO0O )#line:45
            OO0OO00OO00OOO0OO =threading .Thread (target =O0OOOO0O0O000O0O0 )#line:46
            OO0OO00OO00OOO0OO .start ()#line:47
            time .sleep (time_xx )#line:48
    except Exception as OOOOO000OOO000OO0 :#line:49
        print (OOOOO000OOO000OO0 )#line:50
class WorldCity :#line:52
    def __init__ (OO000OO0OO0OO00OO ,O0OO0O00O0O0000O0 ):#line:54
        try :#line:55
            OO000OO0OO0OO00OO .uid =O0OO0O00O0O0000O0 ['uid']#line:56
            OO000OO0OO0OO00OO .nmb =O0OO0O00O0O0000O0 ['zzid']#line:57
            OO000OO0OO0OO00OO .vein =sjc_vv ()#line:58
            OO000OO0OO0OO00OO .vip =sjc_yz ()#line:59
            OO000OO0OO0OO00OO .headers ={'User-Agent':f'com.ainimei.worldcity/{version} (Linux; U; Android 9; zh-cn) (official; {vi})','Channel':'official','ANDROIDID':O0OO0O00O0O0000O0 ['ANDROIDID'],'oaid':O0OO0O00O0O0000O0 ['oaid'],'test-encrypt':'1','uid':O0OO0O00O0O0000O0 ['uid'],'token':O0OO0O00O0O0000O0 ['token'],}#line:63
        except Exception as O0O0000O0000O0O00 :#line:64
            print (O0O0000O0000O0O00 )#line:65
    def home (O0OOO00O0O00OO0O0 ):#line:68
        global ssss #line:69
        try :#line:70
            O0O000OOOOOO00OO0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/user/home?uid={O0OOO00O0O00OO0O0.uid}&version={version}',headers =O0OOO00O0O00OO0O0 .headers ).text ))#line:72
            if 'errorCode'in O0O000OOOOOO00OO0 :#line:73
                return '失效'#line:74
            OO0OOO0OO0OO0OOO0 =requ_encrypt (json .dumps ({"propId":"2"}))#line:75
            O0O000O0O0000O0OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/detail?uid={O0OOO00O0O00OO0O0.uid}&version={version}',headers =O0OOO00O0O00OO0O0 .headers ,data =OO0OOO0OO0OO0OOO0 ).text ))#line:78
            if 'userInfo'in O0O000OOOOOO00OO0 :#line:79
                O0OO0O00OO0OO00OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O0OOO00O0O00OO0O0.uid}&version={version}',headers =O0OOO00O0O00OO0O0 .headers ).text ))#line:81
                if O0OO0O00OO0OO00OO ['status']==2 :#line:82
                    ssss ='打工中'#line:83
                elif O0OO0O00OO0OO00OO ['status']==1 :#line:84
                    ssss ='睡觉中'#line:85
                elif O0OO0O00OO0OO00OO ['status']==0 :#line:86
                    ssss ='空闲中'#line:87
                O00OOOO000OO00O0O =O0O000OOOOOO00OO0 ['userInfo']['userId']#line:88
                O00OO00OO00O0O0O0 =O0O000OOOOOO00OO0 ['wCoins']#line:89
                O000OO0O0OOOO0000 =str (O00OOOO000OO00O0O )[0 :2 ]+'**'+str (O00OOOO000OO00O0O )[4 :]#line:90
                OOO00O0O00O00O0O0 =O0O000OOOOOO00OO0 ['userInfo']['nickname']#line:91
                O000OO0O0OOO0O00O =O0OO0O00OO0OO00OO ['bodyEnergy']#line:92
                O000OOO00O000O00O =O0OO0O00OO0OO00OO ['seconds']/60 #line:93
                print ('账号信息:    ID:%s'%O000OO0O0OOOO0000 +'丨昵称:%s'%OOO00O0O00O00O0O0 +'丨金币:%s'%O00OO00OO00O0O0O0 .split ('.')[0 ]+'丨%s  🧘'%ssss )#line:94
                print ('打工信息:    体力:%s'%O000OO0O0OOO0O00O +'丨精力:%s'%O0O000O0O0000O0OO ['num']+'丨醒来:%s分'%int (O000OOO00O000O00O )+f'丨能量:{O0OOO00O0O00OO0O0.company()}  👨‍💻')#line:95
                if float (O0O000O0O0000O0OO ['num'])<1 :#line:96
                    send ('世界城打工精力不足0',f'{O00OOOO000OO00O0O}账号精力为{O0O000O0O0000O0OO["num"]}')#line:97
                return True #line:98
        except Exception as OO0OOO000OO0O00O0 :#line:99
            print (OO0OOO000OO0O00O0 )#line:100
    def rate_log (O000OO0OOO0OOOOO0 ):#line:103
        try :#line:104
            OO0O0000O0O000OO0 =requ_encrypt (json .dumps ({"fieldIds":"1,2,4,3"}))#line:105
            O0O0OO0OOO0000000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/pay/rate/log?uid={O000OO0OOO0OOOOO0.uid}&version={version}',headers =O000OO0OOO0OOOOO0 .headers ,data =OO0O0000O0O000OO0 ).text ))#line:106
            if 'field'in O0O0OO0OOO0000000 :#line:107
                for O000O0OOO0O0O0O00 in O0O0OO0OOO0000000 ['field']:#line:108
                    if int (jobId )==int (O000O0OOO0O0O0O00 ['jobId']):#line:109
                        return list (reversed (O000O0OOO0O0O0O00 ['items']))[0 ]['rate']#line:110
            return '-1'#line:111
        except Exception as OO0O0OOOO0OO0OOO0 :#line:112
            print (OO0O0OOOO0OO0OOO0 )#line:113
    def rate_choose (OO0OOO000OO000OOO ):#line:116
        try :#line:117
            OOO0O00O0O0O0000O =[]#line:118
            OOOOOOO0O0000OO00 =requ_encrypt (json .dumps ({"fieldIds":"1,2,4,3"}))#line:119
            O000O0OO0O00000OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/pay/rate/log?uid={OO0OOO000OO000OOO.uid}&version={version}',headers =OO0OOO000OO000OOO .headers ,data =OOOOOOO0O0000OO00 ).text ))#line:120
            if 'field'in O000O0OO0O00000OO :#line:121
                for OOO000OO0O0O0O000 in O000O0OO0O00000OO ['field']:#line:122
                    O0OOO000O000O0OO0 ={'jobId':OOO000OO0O0O0O000 ["jobId"],'rate':(list (reversed (OOO000OO0O0O0O000 ["items"]))[0 ]["rate"])}#line:123
                    OOO0O00O0O0O0000O .append (O0OOO000O000O0OO0 )#line:124
            OO0O0OOOO00O0O00O =-1 #line:125
            O0OO0O00O0000O0O0 =0 #line:126
            for O00O00OOOOO0OOOO0 in OOO0O00O0O0O0000O :#line:127
                if Decimal (OO0O0OOOO00O0O00O )<=Decimal (O00O00OOOOO0OOOO0 ['rate']):#line:128
                    OO0O0OOOO00O0O00O =O00O00OOOOO0OOOO0 ['rate']#line:129
                    O0OO0O00O0000O0O0 =O00O00OOOOO0OOOO0 ['jobId']#line:130
            return O0OO0O00O0000O0O0 #line:131
        except Exception as OO00OO000O000O0O0 :#line:132
            print (OO00OO000O000O0O0 )#line:133
    def company (OOOO0OO00O0OO000O ):#line:136
        try :#line:137
            O0O0O0O0OO000O000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/company/data?uid={OOOO0OO00O0OO000O.uid}&version={version}',headers =OOOO0OO00O0OO000O .headers ).text ))#line:138
            if 'newCompany'in O0O0O0O0OO000O000 :#line:139
                O0OO00OO00OO0O00O =O0O0O0O0OO000O000 ['newCompany']['experience']#line:140
                return O0OO00OO00OO0O00O #line:141
        except Exception as OOOOOO0OOO000OO0O :#line:142
            print (OOOOOO0OOO000OO0O )#line:143
    def transfer (OOO00OO0OO00OOOOO ,OO0OO0OOOO0O0OOO0 ):#line:146
        try :#line:147
            OOO00OO0OO00OOOOO .emoji_online ()#line:148
            O00OO00OO000OO0O0 =str (int (OO0OO0OOOO0O0OOO0 .split (".")[0 ])*0.95 ).split (".")[0 ]#line:149
            if OOO00OO0OO00OOOOO .uid !=OOO00OO0OO00OOOOO .nmb :#line:150
                if int (omg )<int (O00OO00OO000OO0O0 ):#line:151
                    OOO000000OOO000O0 =requ_encrypt (json .dumps ({"receiverUserId":OOO00OO0OO00OOOOO .nmb ,"coinNum":O00OO00OO000OO0O0 }))#line:152
                    O0O0O0OOO0O00O0OO =json .loads (resp_decrypt (requests .post (f"{host}/api/gold_union/give_tips?uid={OOO00OO0OO00OOOOO.uid}&version={version}",headers =OOO00OO0OO00OOOOO .headers ,data =OOO000000OOO000O0 ).text ))#line:153
                    if 'serviceCharge'in O0O0O0OOO0O00O0OO :#line:154
                        OOO0OOO0OOOO00OO0 =O0O0O0OOO0O00O0OO ['serviceCharge']#line:155
                        OOO0O0O00O000O0O0 =requ_encrypt (json .dumps ({"coinNum":O00OO00OO000OO0O0 ,"receiverUserId":OOO00OO0OO00OOOOO .nmb ,"wx":"0","qq":"0","expectServiceChargeNum":float (OOO0OOO0OOOO00OO0 )}))#line:156
                        OOO0OOO000O00O0OO =json .loads (resp_decrypt (requests .post (f"{host}/api/gold_union/give?uid={OOO00OO0OO00OOOOO.uid}&version={version}",headers =OOO00OO0OO00OOOOO .headers ,data =OOO0O0O00O000O0O0 ).text ))#line:157
                        if 'message'in OOO0OOO000O00O0OO :#line:158
                            O0O00000O0000O0OO =str (OOO00OO0OO00OOOOO .nmb )[0 :2 ]+'**'+str (OOO00OO0OO00OOOOO .nmb )[4 :]#line:159
                            print ("转赠金币:    ID:%s"%O0O00000O0000O0OO +"丨转赠:%s"%O00OO00OO000OO0O0 +'丨%s  🎇'%OOO0OOO000O00O0OO ['message'])#line:160
                else :#line:161
                    print ("转赠金币:    余额不足跳过      😂")#line:162
            else :#line:163
                print ("转赠金币:    转赠的ID是自己跳过      😂")#line:164
        except Exception as O0O000OOOOO0OO00O :#line:165
            print (O0O000OOOOO0OO00O )#line:166
    def emoji_coins (OO0O0000000OOOOOO ):#line:169
        try :#line:170
            OO0O0000000OOOOOO .emoji_online ()#line:171
            O0000O0O0OOOO0OO0 =json .loads (resp_decrypt (requests .post (f'{host}/v5/api/user/index?uid={OO0O0000000OOOOOO.uid}&version={version}',headers =OO0O0000000OOOOOO .headers ).text ))#line:173
            if O0000O0O0OOOO0OO0 .get ('hasNewAppVersion'):#line:174
                return O0000O0O0OOOO0OO0 .get ('coins')#line:175
        except Exception as O00O0O00OO0O00000 :#line:176
            print (O00O0O00OO0O00000 )#line:177
    def work_upgrade (O000OOO0O000OO0OO ):#line:180
        try :#line:181
            O0OOOOO0O0OO0000O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/job/list?uid={O000OOO0O000OO0OO.uid}&version={version}',headers =O000OOO0O000OO0OO .headers ).text ))#line:182
            if 'nowScore'in O0OOOOO0O0OO0000O :#line:183
                print ('我的职业:    当前拥有经验:%s'%O0OOOOO0O0OO0000O ['nowScore']+f'丨累计额外获得{O0OOOOO0O0OO0000O["extraBrick"]}个砖块    🧱')#line:184
                for OO000OO0OOO000O00 in O0OOOOO0O0OO0000O ['jobs']:#line:185
                    OO00OO00O0OOO000O =OO000OO0OOO000O00 ['name']#line:187
                    O0O00O0O00O0OO00O =OO000OO0OOO000O00 ['desc']#line:188
                    OO0O00O00OOO000O0 =OO000OO0OOO000O00 ['level']#line:189
                    OO0O0O00OO0OOO00O =OO000OO0OOO000O00 ['upgrade']['tips']#line:190
                    O0O00O0000OO000O0 =OO000OO0OOO000O00 ['upgrade']['score']#line:191
                    if OO0O00O00OOO000O0 >0 :#line:192
                        print (f'我的职业:    {OO00OO00O0OOO000O}'+f'丨等级:Lv.{OO0O00O00OOO000O0}'+f'丨{OO0O0O00OO0OOO00O}经验:{O0O00O0000OO000O0}  👔')#line:193
                        if O0OOOOO0O0OO0000O ['nowScore']>O0O00O0000OO000O0 :#line:194
                            O00O00OO0OO0OOOO0 =requ_encrypt (json .dumps ({"jobId":jobId_upgrade }))#line:195
                            O00O00O0000OOOOO0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/job/upgrade/submit?uid={O000OOO0O000OO0OO.uid}&version={version}',headers =O000OOO0O000OO0OO .headers ,data =O00O00OO0OO0OOOO0 ).text ))#line:196
                            if 'desc'in O00O00O0000OOOOO0 :#line:198
                                print ('我的职业:    升级成功丨%s   👍'%O00O00O0000OOOOO0 ['desc'])#line:199
        except Exception as OOOO0OOOO0O00OO0O :#line:200
            print (OOOO0OOOO0O00OO0O )#line:201
    def work_bag (OO0O0O00OOOOO0OOO ):#line:204
        try :#line:205
            OOO0000O0O0O0OOO0 =requ_encrypt (json .dumps ({"type":"0","next":"0"}))#line:206
            O0O0O00OOO00O00OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/bag?uid={OO0O0O00OOOOO0OOO.uid}&version={version}',headers =OO0O0O00OOOOO0OOO .headers ,data =OOO0000O0O0O0OOO0 ).text ))#line:207
            if 'items'in O0O0O00OOO00O00OO :#line:208
                for O00OOO0000O0O0OO0 in O0O0O00OOO00O00OO ['items']:#line:209
                    OOOOO0O0000OOO0O0 =O00OOO0000O0O0OO0 ['id']#line:210
                    OOOOOOOO00000OOOO =O00OOO0000O0O0OO0 ['num']#line:211
                    if OOOOO0O0000OOO0O0 ==1 :#line:212
                        if Decimal (str (OOOOOOOO00000OOOO ))<Decimal (str (physical_power ))or Decimal (str (physical_power ))==0 :#line:213
                            OOO0OO000O0000O00 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={OO0O0O00OOOOO0OOO.uid}&version={version}',headers =OO0O0O00OOOOO0OOO .headers ).text ))#line:216
                            if OOO0OO000O0000O00 ['status']==0 :#line:217
                                OO0O0O00OOOOO0OOO .work_sleep ()#line:218
                                return True #line:219
                    if knapsack :#line:220
                        print ('我的背包:    %s'%O00OOO0000O0O0OO0 ['name']+'丨数量:%s'%OOOOOOOO00000OOOO +'            丨ID:%s'%OOOOO0O0000OOO0O0 )#line:221
                    if prop_food ==OOOOO0O0000OOO0O0 :#line:222
                        if Decimal (str (OOOOOOOO00000OOOO ))<Decimal (str (prop_water_food )):#line:223
                            OO0O0O00OOOOO0OOO .prop_sell (OOOOO0O0000OOO0O0 )#line:224
                    if prop_water ==OOOOO0O0000OOO0O0 :#line:225
                        if Decimal (str (OOOOOOOO00000OOOO ))<Decimal (str (prop_water_food )):#line:226
                            OO0O0O00OOOOO0OOO .prop_sell (OOOOO0O0000OOO0O0 )#line:227
                    if OOOOO0O0000OOO0O0 ==4 :#line:228
                        O00O0000O0OOOO0O0 =OOOOOOOO00000OOOO .split ('.')[0 ]#line:229
                        if prop_brick :#line:230
                            OO0O0O00OOOOO0OOO .work_submit (O00O0000O0OOOO0O0 )#line:231
                    if OOOOO0O0000OOO0O0 ==2 :#line:232
                        if energy >OOOOOOOO00000OOOO :#line:233
                            O00O0000O0OOOO0O0 =int (energy )-int (OOOOOOOO00000OOOO )#line:234
                            if O00O0000O0OOOO0O0 >0 :#line:235
                                OO0O0O00OOOOO0OOO .work_energy (O00O0000O0OOOO0O0 )#line:236
        except Exception as O00O00000O0O000O0 :#line:237
            print (O00O00000O0O000O0 )#line:238
    def work_submit (OO0O0O0000OO0O0O0 ,OOO0OO0O0000OO00O ):#line:241
        try :#line:242
            if recycling_way =='1':#line:243
                O0OO0OO0O000O0OOO =requ_encrypt (json .dumps ({"propId":"4","propNum":OOO0OO0O0000OO00O }))#line:244
                OO0OO0O0O00OOO000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/recycle/submit?uid={OO0O0O0000OO0O0O0.uid}&version={version}',headers =OO0O0O0000OO0O0O0 .headers ,data =O0OO0OO0O000O0OOO ).text ))#line:245
                if 'worldCoin'in OO0OO0O0O00OOO000 :#line:246
                    print ('砖块回收:    数量:%s'%OOO0OO0O0000OO00O +'丨%s'%OO0OO0O0O00OOO000 ['worldCoin'])#line:247
            if recycling_way =='2':#line:248
                O0OOOO0O0O000OO00 =requ_encrypt (json .dumps ({"propId":"4","propNum":OOO0OO0O0000OO00O }))#line:249
                OOO000000OOOO0OOO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/swap/prop/sell/submit?uid={OO0O0O0000OO0O0O0.uid}&version={version}',headers =OO0O0O0000OO0O0O0 .headers ,data =O0OOOO0O0O000OO00 ).text ))#line:250
                if 'worldCoinNum'in OOO000000OOOO0OOO :#line:252
                    print ('砖块出售:    数量:%s'%OOO0OO0O0000OO00O +'丨%s'%OOO000000OOOO0OOO ['worldCoinNum'])#line:253
        except Exception as O0OO0O0O0OO0OOO0O :#line:255
            print (O0OO0O0O0OO0OOO0O )#line:256
    def work_energy (O000O0O0O0O0O0000 ,OO0OOO000OO0O0O00 ):#line:259
        try :#line:260
            O0000O000O00O000O =O000O0O0O0O0O0000 .emoji_coins ()#line:261
            OOOOOO0OO0OO00OOO =str (int (O0000O000O00O000O .split (".")[0 ])*0.95 ).split (".")[0 ]#line:262
            if int (OOOOOO0OO0OO00OOO )>int (OO0OOO000OO0O0O00 /10 ):#line:263
                O0OOOOO000O00OOOO =requ_encrypt (json .dumps ({"buyNum":OO0OOO000OO0O0O00 }))#line:264
                O0OOO0OO000OOO0O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/mental/energy/buy?uid={O000O0O0O0O0O0000.uid}&version={version}',headers =O000O0O0O0O0O0000 .headers ,data =O0OOOOO000O00OOOO ).text ))#line:265
                print ('购买精力:    数量:%s'%OO0OOO000OO0O0O00 +'丨%s      💰'%O0OOO0OO000OOO0O0 ['message'])#line:266
            elif int (OOOOOO0OO0OO00OOO )>10 :#line:267
                O0OOOOO000O00OOOO =requ_encrypt (json .dumps ({"buyNum":'100'}))#line:268
                O0OOO0OO000OOO0O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/mental/energy/buy?uid={O000O0O0O0O0O0000.uid}&version={version}',headers =O000O0O0O0O0O0000 .headers ,data =O0OOOOO000O00OOOO ).text ))#line:269
                print ('购买精力:    数量:100丨%s       💰'%O0OOO0OO000OOO0O0 ['message'])#line:270
        except Exception as O0O00OO000O0O00OO :#line:271
            print (O0O00OO000O0O00OO )#line:272
    def pre_order (OOOOO0O0O0O00OOOO ):#line:275
        try :#line:276
            OOOOO0O0O0O00OOOO .prop_sell (prop_food )#line:277
            OOOOO0O0O0O00OOOO .prop_sell (prop_water )#line:278
        except Exception as O000O00O0OO00O000 :#line:279
            print (O000O00O0OO00O000 )#line:280
    def prop_sell (O0O0O00OOOOOOO0OO ,OOOOO0OOOOO00O00O ):#line:283
        try :#line:284
            OOOO0OOO000OOO000 =requ_encrypt (json .dumps ({"propId":OOOOO0OOOOO00O00O ,"propNum":"1"}))#line:285
            OO000000OOO0OOOOO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/swap/prop/buy/submit?uid={O0O0O00OOOOOOO0OO.uid}&version={version}',headers =O0O0O00OOOOOOO0OO .headers ,data =OOOO0OOO000OOO000 ).text ))#line:286
            if 'propName'in OO000000OOO0OOOOO :#line:288
                print ('购买食物:    购买%s'%OO000000OOO0OOOOO ['propName']+'丨%s     💰'%OO000000OOO0OOOOO ['worldCoinNum'])#line:289
        except Exception as O0OOO0O0OOO00O0OO :#line:291
            print (O0OOO0O0OOO00O0OO )#line:292
    def work_log (O00OO00OOO0OO00O0 ):#line:295
        global c #line:296
        try :#line:297
            O00OO00OO0O0OOO00 =requ_encrypt (json .dumps ({"next":"0"}))#line:298
            O000OO00OO0O000OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/log?uid={O00OO00OOO0OO00O0.uid}&version={version}',headers =O00OO00OOO0OO00O0 .headers ,data =O00OO00OO0O0OOO00 ).text ))#line:299
            if 'items'in O000OO00OO0O000OO :#line:300
                O0OOOO0O000O0000O =0 #line:301
                O000O00O0OOOOOOO0 =0 #line:302
                for O000O0OOOO0O0O0OO in O000OO00OO0O000OO ['items']:#line:303
                    OO00O0O0OOOO0OOOO =O000O0OOOO0O0O0OO ['date']#line:304
                    O0O00000000OO000O =O000O0OOOO0O0O0OO ['startTime']#line:305
                    O0000O0OO0OO0OOOO =O000O0OOOO0O0O0OO ['endTime']#line:306
                    O0O0O00O0O0OO0OO0 =O000O0OOOO0O0O0OO ['rewards'][0 ]['num']#line:307
                    O0OO0O0O0OO00O0O0 =O000O0OOOO0O0O0OO ['rewards'][0 ]['name']#line:308
                    O0OOOO0O000O0000O +=int (O0O0O00O0O0OO0OO0 .split ('+')[1 ].split ('.')[0 ])#line:309
                    O000O00O0OOOOOOO0 +=1 #line:310
                    print ('工作记录:    %s'%OO00O0O0OOOO0OOOO +'丨%s'%O0O00000000OO000O +'-%s'%O0000O0OO0OO0OOOO +'丨%s'%O0OO0O0O0OO00O0O0 +':%s'%O0O0O00O0O0OO0OO0 )#line:311
                    if O000O00O0OOOOOOO0 >9 :#line:312
                        break #line:313
                OO00OO0O0O00O0OO0 =requ_encrypt (json .dumps ({"propId":"4"}))#line:314
                OOO0000OO0OOOO0OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/recycle/config?uid={O00OO00OOO0OO00O0.uid}&version={version}',headers =O00OO00OOO0OO00O0 .headers ,data =OO00OO0O0O00O0OO0 ).text ))#line:317
                if 'brick'in OOO0000OO0OOOO0OO :#line:318
                    OOO0O0OOOOO0OO00O =OOO0000OO0OOOO0OO ['brick']['price']#line:319
                    c =float (Decimal (str (O0OOOO0O000O0000O ))*Decimal (str (OOO0O0OOOOO0OO00O )))#line:320
                print ('工作记录:    打工记录获得砖块:%s'%O0OOOO0O000O0000O +'丨预计获得%s金币'%(int (c *100 )/100 ))#line:321
        except Exception as OO00OO00O0O0OOO0O :#line:322
            print (OO00OO00O0O0OOO0O )#line:323
    def work_start (O0OO0OO00OO00O0O0 ):#line:327
        global c ,jobId_new #line:328
        try :#line:329
            O0O0O0O0O0OO00000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O0OO0OO00OO00O0O0.uid}&version={version}',headers =O0OO0OO00OO00O0O0 .headers ).text ))#line:331
            if 'status'in O0O0O0O0O0OO00000 :#line:332
                if O0O0O0O0O0OO00000 ['status']==0 :#line:333
                    if float (O0O0O0O0O0OO00000 ['bodyEnergy'])<1 :#line:334
                        O0OO0OO00OO00O0O0 .work_sleep ()#line:335
                    O0OOOO0O0O00000O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O0OO0OO00OO00O0O0.uid}&version={version}',headers =O0OO0OO00OO00O0O0 .headers ).text ))#line:336
                    OO0OOOO0OO00O0O0O =O0OOOO0O0O00000O0 ['bodyEnergy']#line:337
                    OOOO00O0OOOO000O0 =O0OO0OO00OO00O0O0 .rate_log ()#line:338
                    if Decimal (OOOO00O0OOOO000O0 )>Decimal (jobIds ):#line:339
                        if Decimal (str (OO0OOOO0OO00O0O0O ))>Decimal (str (physical_power )):#line:340
                            if jobIda :#line:341
                                jobId_new =O0OO0OO00OO00O0O0 .rate_choose ()#line:342
                            else :#line:343
                                jobId_new =jobId #line:344
                            O0OO0OOOO0O0OOO0O =requ_encrypt (json .dumps ({"areaId":areaId ,"foodId":str (prop_food ),"waterId":str (prop_water ),"jobId":str (jobId_new )}))#line:345
                            O0000O00O00O000O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/start?uid={O0OO0OO00OO00O0O0.uid}&version={version}',headers =O0OO0OO00OO00O0O0 .headers ,data =O0OO0OOOO0O0OOO0O ).text ))#line:346
                            if 'message'in O0000O00O00O000O0 :#line:347
                                print (f'工作工作:    设定行业或者最高回报是{jobId_new}丨{O0000O00O00O000O0["message"]}  😷')#line:348
                    else :#line:349
                        print ('工作工作:    回报趋势不达标还是去睡觉吧  😅')#line:350
                        O0OO0OO00OO00O0O0 .work_sleep ()#line:351
                elif O0O0O0O0O0OO00000 ['status']==1 :#line:353
                    print ('工作工作:    睡觉中    😴')#line:354
                    if immediately :#line:355
                        for OOO0OO0000OOO0000 in immediately_time .split ('#'):#line:357
                            OOOO00O0OOOO000O0 =O0OO0OO00OO00O0O0 .rate_log ()#line:359
                            if Decimal (OOOO00O0OOOO000O0 )>Decimal (jobIds ):#line:360
                                if float (O0O0O0O0O0OO00000 ['bodyEnergy'])>21 :#line:361
                                    if str (datetime .datetime .now ().hour )==OOO0OO0000OOO0000 :#line:362
                                        print ('工作工作:    当前时段设置立即醒来工作    🏃')#line:363
                                        requests .post (f'{host}/v4/api/work/sleep/stop?uid={O0OO0OO00OO00O0O0.uid}&version={version}',headers =O0OO0OO00OO00O0O0 .headers )#line:364
                                        time .sleep (random .randint (15 ,25 )/10 )#line:365
                                        if jobIda :#line:366
                                            jobId_new =O0OO0OO00OO00O0O0 .rate_choose ()#line:367
                                        else :#line:368
                                            jobId_new =jobId #line:369
                                        O0OO0OOOO0O0OOO0O =requ_encrypt (json .dumps ({"areaId":areaId ,"foodId":str (prop_food ),"waterId":str (prop_water ),"jobId":str (jobId_new )}))#line:370
                                        O0000O00O00O000O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/start?uid={O0OO0OO00OO00O0O0.uid}&version={version}',headers =O0OO0OO00OO00O0O0 .headers ,data =O0OO0OOOO0O0OOO0O ).text ))#line:371
                                        if 'message'in O0000O00O00O000O0 :#line:372
                                            print (f'工作工作:    设定行业或者最高回报是{jobId_new}丨{O0000O00O00O000O0["message"]}  😷')#line:373
                                            break #line:374
                                else :#line:375
                                    print ('工作工作:    体力不足还是去睡觉吧  😅')#line:376
                            else :#line:377
                                print ('工作工作:    回报趋势不达标还是去睡觉吧  😅')#line:378
                        O0OO0OO00OO00O0O0 .work_sleep ()#line:379
                elif O0O0O0O0O0OO00000 ['status']==2 :#line:380
                    print ('工作工作:    打工中    😷')#line:381
        except Exception as OOOOOO00OOO00OOO0 :#line:382
            print (OOOOOO00OOO00OOO0 )#line:383
    def sjc_ok (OOOOOO00OO00OO000 ):#line:384
        try :#line:385
            if OOOOOO00OO00OO000 .vein <OOOOOO00OO00OO000 .vip ['World_City']['edition']:#line:386
                print (f'当前版本=>>{OOOOOO00OO00OO000.vein}'+f'丨远程版本=>>{OOOOOO00OO00OO000.vip["World_City"]["edition"]}   ❌')#line:387
                print (f'更新内容=>>{OOOOOO00OO00OO000.vip["World_City"]["content"]}   👍')#line:388
            else :#line:389
                print (f'当前版本=>>{OOOOOO00OO00OO000.vein}'+f'丨远程版本=>>{OOOOOO00OO00OO000.vip["World_City"]["edition"]}   ✅')#line:390
                print (f'更新内容=>>{OOOOOO00OO00OO000.vip["World_City"]["content"]}   👍')#line:391
        except Exception as O000O0O000O00000O :#line:392
            print (O000O0O000O00000O )#line:393
    def work_sleep (OO000OOO000OOO0OO ):#line:396
        try :#line:397
            OOO0O0O0O0O0OO00O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={OO000OOO000OOO0OO.uid}&version={version}',headers =OO000OOO000OOO0OO .headers ).text ))#line:398
            if OOO0O0O0O0O0OO00O ['status']==0 :#line:399
                OOOOO000O00O0O00O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep/start?uid={OO000OOO000OOO0OO.uid}&version={version}',headers =OO000OOO000OOO0OO .headers ).text ))#line:400
                if 'message'in OOOOO000O00O0O00O :#line:401
                    print ('睡觉睡觉:    %s'%OOOOO000O00O0O00O ['message'])#line:402
        except Exception as OO00O0OO00OO0O00O :#line:403
            print (OO00O0OO00OO0O00O )#line:404
    def emoji_online (OO0O0O00000O0OOOO ):#line:407
        try :#line:408
            json .loads (resp_decrypt (requests .post (f'{host}/api/lottery/senior/timer?uid={OO0O0O00000O0OOOO.uid}&version={version}',headers =OO0O0O00000O0OOOO .headers ).text ))#line:410
        except Exception as O00O0O000OOOO000O :#line:411
            print (O00O0O000OOOO000O )#line:412
def sjc_vv ():#line:418
    return str ((70 -56 )/10 )#line:419
public_key ='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiWc4m3QbX51xTpt4snwGSnvI42SpbgAYFiL8wLgnzC9G7i5luSrfAP0A+MQbRSH42zc1oVO4NMwky7sfSqJFHc0cEcc9Ck3EmQHesdUAbyzq+DN+DU75YuVEyR1tbWeMZYuxBvN8DyFt53CV+6yD0EzTHg8t0yIfIY90h4+oRNN+YbLEuXOHOaLfU4hYKmPyCn6JPde1bsgd6wkGiFNCC6Thw+ut7jKopaeTCPx62s7aX0OrEe1mKV/xwqsr3qRUh3nn1hAtZr8XJHNpNwm3vS2c8HCaTVkU6N4bw8GtGrDhAYg5RVVFIjXJluHoiaNR2AYgo65yxa3vBfr4At+DrwIDAQAB'#line:425
def public_key_decrypt (O000O00O0OOO0O0OO ,OOOOO000OO0OOO0OO ):#line:428
    try :#line:429
        OOO0O0OOOOOO0OO00 =len (OOOOO000OO0OOO0OO )%4 #line:430
        if OOO0O0OOOOOO0OO00 !=0 :#line:431
            OOOOO000OO0OOO0OO +='='*(4 -OOO0O0OOOOOO0OO00 )#line:432
        OO00O0OO0O00OO0O0 =base64 .b64decode (OOOOO000OO0OOO0OO )#line:433
        O0O0O0OO0OOO0O0O0 =base64 .b64decode (O000O00O0OOO0O0OO )#line:434
        O0OOO00O000OOO00O =PublicKey .load_pkcs1_openssl_der (O0O0O0OO0OOO0O0O0 )#line:435
        O00O0OOO0OOO0O0O0 =transform .bytes2int (OO00O0OO0O00OO0O0 )#line:436
        O0OOO0O00000O000O =core .decrypt_int (O00O0OOO0OOO0O0O0 ,O0OOO00O000OOO00O .e ,O0OOO00O000OOO00O .n )#line:437
        OO0O0OOOO0O0OO0OO =transform .int2bytes (O0OOO0O00000O000O )#line:438
        O0OO0O0O0OO000000 =OO0O0OOOO0O0OO0OO [OO0O0OOOO0O0OO0OO .index (0 )+1 :]#line:439
        return O0OO0O0O0OO000000 .decode ()#line:440
    except Exception as O0OOOO00OOO00000O :#line:441
        print (f"RSA解密发生错误：{O0OOOO00OOO00000O}")#line:442
        return None #line:443
def public_key_encrypt (OOOOO0O0O00OOO0OO ,OOOO0OOO0OOOO000O ):#line:446
    try :#line:447
        O0OO000O00OO0OO0O =base64 .b64decode (OOOOO0O0O00OOO0OO )#line:448
        OOO0000OOOO0O0OOO =PublicKey .load_pkcs1_openssl_der (O0OO000O00OO0OO0O )#line:449
        O0OO0O000OO0OOO0O =rsa .encrypt (base64 .b64decode (OOOO0OOO0OOOO000O .encode ()),OOO0000OOOO0O0OOO )#line:450
        return base64 .b64encode (O0OO0O000OO0OOO0O ).decode ()#line:451
    except Exception as O00O0OO0OOOOO00O0 :#line:452
        print (f"RSA加密发生错误：{O00O0OO0OOOOO00O0}")#line:453
        return None #line:454
def sjc_yz ():#line:457
    try :#line:458
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:459
    except Exception as O0O000O0O0OO0000O :#line:460
        sys .exit (0 )#line:461
def add_to_16 (O00O000OO0OOOOOO0 ):#line:464
    while len (O00O000OO0OOOOOO0 )%16 !=0 :#line:465
        O00O000OO0OOOOOO0 +='\0'#line:466
    return str .encode (O00O000OO0OOOOOO0 )#line:467
def get_key (O000O000OOO0O00O0 ):#line:470
    OO0OOO000O00OO000 =int (O000O000OOO0O00O0 )#line:471
    O0OO0OO00OOOOO0OO ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'#line:472
    OO0O00OO00O0OOO0O =len (O0OO0OO00OOOOO0OO )-1 #line:473
    O000O00000OO0O0OO =''#line:474
    for O00000O0O000O00OO in range (OO0OOO000O00OO000 ):#line:475
        O000O00000OO0O0OO +=O0OO0OO00OOOOO0OO [random .randint (0 ,OO0O00OO00O0OOO0O )]#line:476
    return O000O00000OO0O0OO #line:477
def getRandomKey (O0O000OO0O0O000O0 ):#line:480
    O0O0O000000OO0OOO ='0123456789abcdef'#line:481
    O00OOOO0O000OO00O =''#line:482
    for O00O000000O00O00O in range (O0O000OO0O0O000O0 *2 ):#line:483
        O00OOOO0O000OO00O +=O0O0O000000OO0OOO [random .randint (0 ,len (O0O0O000000OO0OOO )-1 )]#line:484
    return base64 .b64encode (bytes .fromhex (O00OOOO0O000OO00O )).decode ()#line:485
def aes_decrypt (OOOOO0O0O0000O0O0 ,OO0O00O000O0OO000 ,O0OOOOO00000O00OO ):#line:488
    O0OO00O00000O00O0 =AES .new (add_to_16 (OOOOO0O0O0000O0O0 ),AES .MODE_CBC ,add_to_16 (OO0O00O000O0OO000 ))#line:489
    OO0OOO00O0O000O00 =base64 .decodebytes (O0OOOOO00000O00OO .encode (encoding ='utf-8'))#line:490
    OO0OOO0O0OO0OO000 =re .compile ('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub ('',O0OO00O00000O00O0 .decrypt (OO0OOO00O0O000O00 ).decode ())#line:492
    return OO0OOO0O0OO0OO000 #line:493
def aes_encrypt (O0O00O00OOO00OOO0 ,OO0OOO00OOOO0OOO0 ,OOOO0O000OOO0O0OO ):#line:496
    __OO0OOOO0OOO0O0O00 =AES .block_size #line:497
    OOOOOO0OO0OO0O00O =AES .new (base64 .b64decode (O0O00O00OOO00OOO0 .encode ()),AES .MODE_CBC ,OO0OOO00OOOO0OOO0 .encode ())#line:498
    O0OO00O00O0OO0O00 =__OO0OOOO0OOO0O0O00 -(len (OOOO0O000OOO0O0OO )%__OO0OOOO0OOO0O0O00 )#line:499
    if O0OO00O00O0OO0O00 !=0 :#line:500
        OOOO0O000OOO0O0OO =OOOO0O000OOO0O0OO +chr (O0OO00O00O0OO0O00 )*O0OO00O00O0OO0O00 #line:501
    O00OOOO0OO0O00OO0 =OOOOOO0OO0OO0O00O .encrypt (OOOO0O000OOO0O0OO .encode ('utf-8'))#line:502
    OO0OO0OO0O00OOOOO =base64 .encodebytes (O00OOOO0OO0O00OO0 ).decode ()#line:503
    return OO0OO0OO0O00OOOOO #line:504
def requ_encrypt (O0OO0O0OOOO00O0OO ):#line:507
    try :#line:508
        OOO000O0OOO00OOO0 =getRandomKey (32 )#line:509
        OO0O0O0O0OO0O000O =get_key (16 )#line:510
        O00OOOO0O00O0OOOO =public_key_encrypt (public_key ,OOO000O0OOO00OOO0 )#line:511
        OO0O0O00O0O000O0O =aes_encrypt (OOO000O0OOO00OOO0 ,OO0O0O0O0OO0O000O ,O0OO0O0OOOO00O0OO )#line:512
        O0O0OOOOO0O0O0OOO =O00OOOO0O00O0OOOO +'.'+OO0O0O0O0OO0O000O +OO0O0O00O0O000O0O #line:513
        return O0O0OOOOO0O0O0OOO #line:514
    except Exception as OOOO0O0OOO0OO000O :#line:515
        print (f"Request加密失败：{OOOO0O0OOO0OO000O}")#line:516
        return None #line:517
def resp_decrypt (OO000000000000OO0 ):#line:520
    try :#line:521
        if '.'not in OO000000000000OO0 :#line:522
            return OO000000000000OO0 #line:523
        OOOO00OO000O00O00 =OO000000000000OO0 .split ('.')[0 ]#line:524
        OOO0000OOOO0O0O00 =OO000000000000OO0 .split ('.')[1 ]#line:525
        OOOOOO0O00O0O0000 =public_key_decrypt (public_key ,OOOO00OO000O00O00 )#line:526
        if OOOOOO0O00O0O0000 !=None :#line:527
            O0000O000OOO0O0OO =OOO0000OOOO0O0O00 [:16 ]#line:528
            O000OOO0000OOO000 =OOO0000OOOO0O0O00 [16 :]#line:529
            OOOOOO000O00O0O0O =aes_decrypt (OOOOOO0O00O0O0000 ,O0000O000OOO0O0OO ,O000OOO0000OOO000 )#line:530
            return OOOOOO000O00O0O0O #line:531
        else :#line:532
            return None #line:533
    except Exception as OO0OO0O00OO0OO0O0 :#line:534
        print (f"response加密失败：{OO0OO0O00OO0OO0O0}")#line:535
if __name__ =='__main__':#line:539
    main ()#line:540
