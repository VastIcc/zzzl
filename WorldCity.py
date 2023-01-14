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
immediately = True                      # 立即醒来去打工      True为醒来     False为不醒
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
omg = 30  # 单位个   转账数量大于就会转,不转币最好设置9999999
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
        for O0OO0OO0O0O000O0O in sjc_new :#line:11
            print (f"-------------------正在执行第{sjc_new.index(O0OO0OO0O0O000O0O) + 1}个账号-------------------")#line:12
            O00000O0000O00O0O =WorldCity (O0OO0OO0O0O000O0O )#line:14
            def O0OO0OO0OOO0O000O ():#line:15
                OO0000OOOOO0OOOOO =O00000O0000O00O0O .home ()#line:17
                if OO0000OOOOO0OOOOO =='失效':#line:18
                    print ('账号信息:    ID:%s'%O0OO0OO0O0O000O0O ['uid']+'丨网络限制或者失效')#line:19
                    return False #line:20
                if OO0000OOOOO0OOOOO !='打工中':#line:21
                    if pre_order :#line:22
                        print ('我打开了')#line:24
                        O00000O0000O00O0O .pre_order ()#line:25
                    if upgrade :#line:26
                        O00000O0000O00O0O .work_upgrade ()#line:28
                    O00000O0000O00O0O .company ()#line:30
                    if O00000O0000O00O0O .work_bag ():#line:32
                        pass #line:33
                    else :#line:34
                        if str (datetime .datetime .now ().hour )in start_work .split ('#')or '25'in start_work .split ('#'):#line:35
                            O00000O0000O00O0O .work_start ()#line:37
                        else :#line:38
                            O00000O0000O00O0O .work_sleep ()#line:39
                    O00000O0000O00O0O .work_log ()#line:41
                    O00000O0000O00O0O .transfer (O00000O0000O00O0O .emoji_coins ())#line:43
                elif OO0000OOOOO0OOOOO =='打工中':#line:44
                    print (OO0000OOOOO0OOOOO )#line:45
            OO00OOOO0O000O00O =threading .Thread (target =O0OO0OO0OOO0O000O )#line:46
            OO00OOOO0O000O00O .start ()#line:47
            time .sleep (time_xx )#line:48
    except Exception as O0O0000O0O0O0OOO0 :#line:49
        print (O0O0000O0O0O0OOO0 )#line:50
class WorldCity :#line:52
    def __init__ (O0O0OO00O00OO0OOO ,OOOOOOOOOOOOO000O ):#line:54
        try :#line:55
            O0O0OO00O00OO0OOO .uid =OOOOOOOOOOOOO000O ['uid']#line:56
            O0O0OO00O00OO0OOO .nmb =OOOOOOOOOOOOO000O ['zzid']#line:57
            O0O0OO00O00OO0OOO .vein =sjc_vv ()#line:58
            O0O0OO00O00OO0OOO .vip =sjc_yz ()#line:59
            O0O0OO00O00OO0OOO .headers ={'User-Agent':f'com.ainimei.worldcity/{version} (Linux; U; Android 9; zh-cn) (official; {vi})','Channel':'official','ANDROIDID':OOOOOOOOOOOOO000O ['ANDROIDID'],'oaid':OOOOOOOOOOOOO000O ['oaid'],'test-encrypt':'1','uid':OOOOOOOOOOOOO000O ['uid'],'token':OOOOOOOOOOOOO000O ['token'],}#line:63
        except Exception as OOO0O00O00OOO0O00 :#line:64
            print (OOO0O00O00OOO0O00 )#line:65
    def home (O0O0OO0O00OOO000O ):#line:68
        global ssss #line:69
        try :#line:70
            OOOO00O00O0OOOO00 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/user/home?uid={O0O0OO0O00OOO000O.uid}&version={version}',headers =O0O0OO0O00OOO000O .headers ).text ))#line:72
            if 'errorCode'in OOOO00O00O0OOOO00 :#line:73
                return '失效'#line:74
            O00OOO000O0O00OOO =requ_encrypt (json .dumps ({"propId":"2"}))#line:75
            O0OO00O0O00OOOOOO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/detail?uid={O0O0OO0O00OOO000O.uid}&version={version}',headers =O0O0OO0O00OOO000O .headers ,data =O00OOO000O0O00OOO ).text ))#line:78
            if 'userInfo'in OOOO00O00O0OOOO00 :#line:79
                OOOOOOO0O0OOO000O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O0O0OO0O00OOO000O.uid}&version={version}',headers =O0O0OO0O00OOO000O .headers ).text ))#line:81
                if OOOOOOO0O0OOO000O ['status']==2 :#line:82
                    ssss ='打工中'#line:83
                elif OOOOOOO0O0OOO000O ['status']==1 :#line:84
                    ssss ='睡觉中'#line:85
                elif OOOOOOO0O0OOO000O ['status']==0 :#line:86
                    ssss ='空闲中'#line:87
                O0O0O0O0OOO0OO0OO =OOOO00O00O0OOOO00 ['userInfo']['userId']#line:88
                OO000O0OO0OOO00OO =OOOO00O00O0OOOO00 ['wCoins']#line:89
                OO00000O0OO00OOOO =str (O0O0O0O0OOO0OO0OO )[0 :2 ]+'**'+str (O0O0O0O0OOO0OO0OO )[4 :]#line:90
                OOOOOO0OOO000000O =OOOO00O00O0OOOO00 ['userInfo']['nickname']#line:91
                O000OO0000OO00000 =OOOOOOO0O0OOO000O ['bodyEnergy']#line:92
                OOO0OOO0OOO0O000O =OOOOOOO0O0OOO000O ['seconds']/60 #line:93
                print ('账号信息:    ID:%s'%OO00000O0OO00OOOO +'丨昵称:%s'%OOOOOO0OOO000000O +'丨金币:%s'%OO000O0OO0OOO00OO .split ('.')[0 ]+'丨%s  🧘'%ssss )#line:94
                print ('打工信息:    体力:%s'%O000OO0000OO00000 +'丨精力:%s'%O0OO00O0O00OOOOOO ['num']+'丨醒来:%s分'%int (OOO0OOO0OOO0O000O )+f'丨能量:{O0O0OO0O00OOO000O.company()}  👨‍💻')#line:95
                if float (O0OO00O0O00OOOOOO ['num'])<1 :#line:96
                    send ('世界城打工精力不足0',f'{O0O0O0O0OOO0OO0OO}账号精力为{O0OO00O0O00OOOOOO["num"]}')#line:97
                return True #line:98
        except Exception as OO0000000OO000OO0 :#line:99
            print (OO0000000OO000OO0 )#line:100
    def rate_log (OOOO0OOOOO0OOO00O ):#line:103
        try :#line:104
            O0OOOO0O0O0000O00 =requ_encrypt (json .dumps ({"fieldIds":"1,2,4,3"}))#line:105
            OOOO0O0O00O0000OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/pay/rate/log?uid={OOOO0OOOOO0OOO00O.uid}&version={version}',headers =OOOO0OOOOO0OOO00O .headers ,data =O0OOOO0O0O0000O00 ).text ))#line:106
            if 'field'in OOOO0O0O00O0000OO :#line:107
                for O0O000O0OOOO00OOO in OOOO0O0O00O0000OO ['field']:#line:108
                    if int (jobId )==int (O0O000O0OOOO00OOO ['jobId']):#line:109
                        return list (reversed (O0O000O0OOOO00OOO ['items']))[0 ]['rate']#line:110
            return '-1'#line:111
        except Exception as OOO0OO0O0OOOOOO0O :#line:112
            print (OOO0OO0O0OOOOOO0O )#line:113
    def rate_choose (OOO0000OOO00O0O00 ):#line:116
        try :#line:117
            O00000O000O0OOO0O =[]#line:118
            OOOOO0O000OOOO000 =requ_encrypt (json .dumps ({"fieldIds":"1,2,4,3"}))#line:119
            O0000OO000O0OOO0O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/pay/rate/log?uid={OOO0000OOO00O0O00.uid}&version={version}',headers =OOO0000OOO00O0O00 .headers ,data =OOOOO0O000OOOO000 ).text ))#line:120
            if 'field'in O0000OO000O0OOO0O :#line:121
                for OOO0O00000OO000OO in O0000OO000O0OOO0O ['field']:#line:122
                    O0O0O0OOOOOOO0O00 ={'jobId':OOO0O00000OO000OO ["jobId"],'rate':(list (reversed (OOO0O00000OO000OO ["items"]))[0 ]["rate"])}#line:123
                    O00000O000O0OOO0O .append (O0O0O0OOOOOOO0O00 )#line:124
            O000000OO0O00OO00 =-1 #line:125
            O00OOO00O0OOO0OOO =0 #line:126
            for O00O00000O0O000OO in O00000O000O0OOO0O :#line:127
                if Decimal (O000000OO0O00OO00 )<=Decimal (O00O00000O0O000OO ['rate']):#line:128
                    O000000OO0O00OO00 =O00O00000O0O000OO ['rate']#line:129
                    O00OOO00O0OOO0OOO =O00O00000O0O000OO ['jobId']#line:130
            return O00OOO00O0OOO0OOO #line:131
        except Exception as OO000OO000O0O0000 :#line:132
            print (OO000OO000O0O0000 )#line:133
    def company (OOO0000000OOO0O00 ):#line:136
        try :#line:137
            O0000OO0OOOO00000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/company/data?uid={OOO0000000OOO0O00.uid}&version={version}',headers =OOO0000000OOO0O00 .headers ).text ))#line:138
            if 'newCompany'in O0000OO0OOOO00000 :#line:139
                OOOO0O0O0O0OO0OOO =O0000OO0OOOO00000 ['newCompany']['experience']#line:140
                return OOOO0O0O0O0OO0OOO #line:141
        except Exception as OO0O0O0OO00OOOO0O :#line:142
            print (OO0O0O0OO00OOOO0O )#line:143
    def transfer (OO00OOOOOO00OOOO0 ,O000OO0O0OOOOOO0O ):#line:146
        try :#line:147
            OO00OOOOOO00OOOO0 .emoji_online ()#line:148
            O00O0O0OO00000000 =str (int (O000OO0O0OOOOOO0O .split (".")[0 ])*0.95 ).split (".")[0 ]#line:149
            if OO00OOOOOO00OOOO0 .uid !=OO00OOOOOO00OOOO0 .nmb :#line:150
                if int (omg )<int (O00O0O0OO00000000 ):#line:151
                    OOOO00OO00OOOOO0O =requ_encrypt (json .dumps ({"receiverUserId":OO00OOOOOO00OOOO0 .nmb ,"coinNum":O00O0O0OO00000000 }))#line:152
                    O0OO0O0OO0000O0OO =json .loads (resp_decrypt (requests .post (f"{host}/api/gold_union/give_tips?uid={OO00OOOOOO00OOOO0.uid}&version={version}",headers =OO00OOOOOO00OOOO0 .headers ,data =OOOO00OO00OOOOO0O ).text ))#line:153
                    if 'serviceCharge'in O0OO0O0OO0000O0OO :#line:154
                        OOOOOOOO00OOOO00O =O0OO0O0OO0000O0OO ['serviceCharge']#line:155
                        O00OOO0000000O0OO =requ_encrypt (json .dumps ({"coinNum":O00O0O0OO00000000 ,"receiverUserId":OO00OOOOOO00OOOO0 .nmb ,"wx":"0","qq":"0","expectServiceChargeNum":float (OOOOOOOO00OOOO00O )}))#line:156
                        O00000OOO0OO00000 =json .loads (resp_decrypt (requests .post (f"{host}/api/gold_union/give?uid={OO00OOOOOO00OOOO0.uid}&version={version}",headers =OO00OOOOOO00OOOO0 .headers ,data =O00OOO0000000O0OO ).text ))#line:157
                        if 'message'in O00000OOO0OO00000 :#line:158
                            OOO00O000OO00O00O =str (OO00OOOOOO00OOOO0 .nmb )[0 :2 ]+'**'+str (OO00OOOOOO00OOOO0 .nmb )[4 :]#line:159
                            print ("转赠金币:    ID:%s"%OOO00O000OO00O00O +"丨转赠:%s"%O00O0O0OO00000000 +'丨%s  🎇'%O00000OOO0OO00000 ['message'])#line:160
                else :#line:161
                    print ("转赠金币:    余额不足跳过      😂")#line:162
            else :#line:163
                print ("转赠金币:    转赠的ID是自己跳过      😂")#line:164
        except Exception as O000O0000O0OOO0O0 :#line:165
            print (O000O0000O0OOO0O0 )#line:166
    def emoji_coins (O0OO00OOOO00OO0OO ):#line:169
        try :#line:170
            O0OO00OOOO00OO0OO .emoji_online ()#line:171
            O000O0OO0O0OOO0OO =json .loads (resp_decrypt (requests .post (f'{host}/v5/api/user/index?uid={O0OO00OOOO00OO0OO.uid}&version={version}',headers =O0OO00OOOO00OO0OO .headers ).text ))#line:173
            if O000O0OO0O0OOO0OO .get ('hasNewAppVersion'):#line:174
                return O000O0OO0O0OOO0OO .get ('coins')#line:175
        except Exception as OO00O000OO0O000O0 :#line:176
            print (OO00O000OO0O000O0 )#line:177
    def work_upgrade (OO0000OO00OOO0OO0 ):#line:180
        try :#line:181
            OO0OO0O0OO0O0OO00 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/job/list?uid={OO0000OO00OOO0OO0.uid}&version={version}',headers =OO0000OO00OOO0OO0 .headers ).text ))#line:182
            if 'nowScore'in OO0OO0O0OO0O0OO00 :#line:183
                print ('我的职业:    当前拥有经验:%s'%OO0OO0O0OO0O0OO00 ['nowScore']+f'丨累计额外获得{OO0OO0O0OO0O0OO00["extraBrick"]}个砖块    🧱')#line:184
                for O0O000O0OOO0000O0 in OO0OO0O0OO0O0OO00 ['jobs']:#line:185
                    O00O0OOOOO00O00O0 =O0O000O0OOO0000O0 ['name']#line:187
                    OO0O00OO0O0OO0000 =O0O000O0OOO0000O0 ['desc']#line:188
                    OO00OOO0OO0O0O0O0 =O0O000O0OOO0000O0 ['level']#line:189
                    OO0000OOO0OOOOOO0 =O0O000O0OOO0000O0 ['upgrade']['tips']#line:190
                    O00OOO0OO0O00000O =O0O000O0OOO0000O0 ['upgrade']['score']#line:191
                    if OO00OOO0OO0O0O0O0 >0 :#line:192
                        print (f'我的职业:    {O00O0OOOOO00O00O0}'+f'丨等级:Lv.{OO00OOO0OO0O0O0O0}'+f'丨{OO0000OOO0OOOOOO0}经验:{O00OOO0OO0O00000O}  👔')#line:193
                        if OO0OO0O0OO0O0OO00 ['nowScore']>O00OOO0OO0O00000O :#line:194
                            OOO000O000O00O00O =requ_encrypt (json .dumps ({"jobId":jobId_upgrade }))#line:195
                            OOO0O0O000O0O000O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/job/upgrade/submit?uid={OO0000OO00OOO0OO0.uid}&version={version}',headers =OO0000OO00OOO0OO0 .headers ,data =OOO000O000O00O00O ).text ))#line:196
                            if 'desc'in OOO0O0O000O0O000O :#line:198
                                print ('我的职业:    升级成功丨%s   👍'%OOO0O0O000O0O000O ['desc'])#line:199
        except Exception as O000OOOOO0000OO00 :#line:200
            print (O000OOOOO0000OO00 )#line:201
    def work_bag (O0000000O0000OOO0 ):#line:204
        try :#line:205
            OO000000O0O0O00O0 =requ_encrypt (json .dumps ({"type":"0","next":"0"}))#line:206
            O0000O000OO0000O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/bag?uid={O0000000O0000OOO0.uid}&version={version}',headers =O0000000O0000OOO0 .headers ,data =OO000000O0O0O00O0 ).text ))#line:207
            if 'items'in O0000O000OO0000O0 :#line:208
                for O0O00O0OO000OOO00 in O0000O000OO0000O0 ['items']:#line:209
                    O0O0O0000O0OO00O0 =O0O00O0OO000OOO00 ['id']#line:210
                    OO00000O00OO0OO00 =O0O00O0OO000OOO00 ['num']#line:211
                    if O0O0O0000O0OO00O0 ==1 :#line:212
                        if Decimal (str (OO00000O00OO0OO00 ))<Decimal (str (physical_power ))or Decimal (str (physical_power ))==0 :#line:213
                            O0O0OOOOOOO0OO000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O0000000O0000OOO0.uid}&version={version}',headers =O0000000O0000OOO0 .headers ).text ))#line:216
                            if O0O0OOOOOOO0OO000 ['status']==0 :#line:217
                                O0000000O0000OOO0 .work_sleep ()#line:218
                                return True #line:219
                    if knapsack :#line:220
                        print ('我的背包:    %s'%O0O00O0OO000OOO00 ['name']+'丨数量:%s'%OO00000O00OO0OO00 +'            丨ID:%s'%O0O0O0000O0OO00O0 )#line:221
                    if prop_food ==O0O0O0000O0OO00O0 :#line:222
                        if Decimal (str (OO00000O00OO0OO00 ))<Decimal (str (prop_water_food )):#line:223
                            O0000000O0000OOO0 .prop_sell (O0O0O0000O0OO00O0 )#line:224
                    if prop_water ==O0O0O0000O0OO00O0 :#line:225
                        if Decimal (str (OO00000O00OO0OO00 ))<Decimal (str (prop_water_food )):#line:226
                            O0000000O0000OOO0 .prop_sell (O0O0O0000O0OO00O0 )#line:227
                    if O0O0O0000O0OO00O0 ==4 :#line:228
                        O00OOO0O00OO0O0OO =OO00000O00OO0OO00 .split ('.')[0 ]#line:229
                        if prop_brick :#line:230
                            O0000000O0000OOO0 .work_submit (O00OOO0O00OO0O0OO )#line:231
                    if O0O0O0000O0OO00O0 ==2 :#line:232
                        if energy >OO00000O00OO0OO00 :#line:233
                            O00OOO0O00OO0O0OO =int (energy )-int (OO00000O00OO0OO00 )#line:234
                            if O00OOO0O00OO0O0OO >0 :#line:235
                                O0000000O0000OOO0 .work_energy (O00OOO0O00OO0O0OO )#line:236
        except Exception as O00O0O00000000000 :#line:237
            print (O00O0O00000000000 )#line:238
    def work_submit (O0O0OO0O00OO00O00 ,OOOO0OOO00OO0OO0O ):#line:241
        try :#line:242
            if recycling_way =='1':#line:243
                OOO000O0O00OOO000 =requ_encrypt (json .dumps ({"propId":"4","propNum":OOOO0OOO00OO0OO0O }))#line:244
                O0O0O0O000O0O0000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/recycle/submit?uid={O0O0OO0O00OO00O00.uid}&version={version}',headers =O0O0OO0O00OO00O00 .headers ,data =OOO000O0O00OOO000 ).text ))#line:245
                if 'worldCoin'in O0O0O0O000O0O0000 :#line:246
                    print ('砖块回收:    数量:%s'%OOOO0OOO00OO0OO0O +'丨%s'%O0O0O0O000O0O0000 ['worldCoin'])#line:247
            if recycling_way =='2':#line:248
                OO000O0O0O000O0O0 =requ_encrypt (json .dumps ({"propId":"4","propNum":OOOO0OOO00OO0OO0O }))#line:249
                O00OOOOOO0OO00O0O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/swap/prop/sell/submit?uid={O0O0OO0O00OO00O00.uid}&version={version}',headers =O0O0OO0O00OO00O00 .headers ,data =OO000O0O0O000O0O0 ).text ))#line:250
                if 'worldCoin'in O00OOOOOO0OO00O0O :#line:251
                    print ('砖块回收:    数量:%s'%OOOO0OOO00OO0OO0O +'丨%s'%O00OOOOOO0OO00O0O ['worldCoin'])#line:252
        except Exception as O00OO000OO00OO0O0 :#line:254
            print (O00OO000OO00OO0O0 )#line:255
    def work_energy (O0O000O00000O00O0 ,OO00O00O0OO000OO0 ):#line:258
        try :#line:259
            O0O000O0OO0O0O0O0 =O0O000O00000O00O0 .emoji_coins ()#line:260
            O0O000O00O0O0OOOO =str (int (O0O000O0OO0O0O0O0 .split (".")[0 ])*0.95 ).split (".")[0 ]#line:261
            if int (O0O000O00O0O0OOOO )>int (OO00O00O0OO000OO0 /10 ):#line:262
                OO00O0OOOO0O0OOO0 =requ_encrypt (json .dumps ({"buyNum":OO00O00O0OO000OO0 }))#line:263
                OOOO00OO000OO0000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/mental/energy/buy?uid={O0O000O00000O00O0.uid}&version={version}',headers =O0O000O00000O00O0 .headers ,data =OO00O0OOOO0O0OOO0 ).text ))#line:264
                print ('购买精力:    数量:%s'%OO00O00O0OO000OO0 +'丨%s      💰'%OOOO00OO000OO0000 ['message'])#line:265
            elif int (O0O000O00O0O0OOOO )>10 :#line:266
                OO00O0OOOO0O0OOO0 =requ_encrypt (json .dumps ({"buyNum":'100'}))#line:267
                OOOO00OO000OO0000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/mental/energy/buy?uid={O0O000O00000O00O0.uid}&version={version}',headers =O0O000O00000O00O0 .headers ,data =OO00O0OOOO0O0OOO0 ).text ))#line:268
                print ('购买精力:    数量:100丨%s       💰'%OOOO00OO000OO0000 ['message'])#line:269
        except Exception as O0O0000O0O0O00O00 :#line:270
            print (O0O0000O0O0O00O00 )#line:271
    def pre_order (O0OO00O0000000O00 ):#line:274
        try :#line:275
            O0OO00O0000000O00 .prop_sell (prop_food )#line:276
            O0OO00O0000000O00 .prop_sell (prop_water )#line:277
        except Exception as O00O0OOOOOO0O0OO0 :#line:278
            print (O00O0OOOOOO0O0OO0 )#line:279
    def prop_sell (O00O00O00O0O00O00 ,OO000OO00OO0OOO0O ):#line:282
        try :#line:283
            O0000OOO0OOOOO000 =requ_encrypt (json .dumps ({"propId":OO000OO00OO0OOO0O ,"propNum":"1"}))#line:284
            OOOOO000OO00OO0OO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/swap/prop/buy/submit?uid={O00O00O00O0O00O00.uid}&version={version}',headers =O00O00O00O0O00O00 .headers ,data =O0000OOO0OOOOO000 ).text ))#line:285
            if 'propName'in OOOOO000OO00OO0OO :#line:287
                print ('购买食物:    购买%s'%OOOOO000OO00OO0OO ['propName']+'丨%s     💰'%OOOOO000OO00OO0OO ['worldCoinNum'])#line:288
        except Exception as OOO0O00O0OO0O000O :#line:290
            print (OOO0O00O0OO0O000O )#line:291
    def work_log (OOO00OO00O0000O00 ):#line:294
        global c #line:295
        try :#line:296
            OOOO00OOOOO00O0OO =requ_encrypt (json .dumps ({"next":"0"}))#line:297
            O0OO00O0O00OO0OOO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/log?uid={OOO00OO00O0000O00.uid}&version={version}',headers =OOO00OO00O0000O00 .headers ,data =OOOO00OOOOO00O0OO ).text ))#line:298
            if 'items'in O0OO00O0O00OO0OOO :#line:299
                O0O00O000OO000OO0 =0 #line:300
                OO0000OO0OOOO000O =0 #line:301
                for OO0O00O000OO0OO0O in O0OO00O0O00OO0OOO ['items']:#line:302
                    O0O0000OOO0OO0O0O =OO0O00O000OO0OO0O ['date']#line:303
                    O00O0O0OO0000000O =OO0O00O000OO0OO0O ['startTime']#line:304
                    OO0000O0O0O00O0OO =OO0O00O000OO0OO0O ['endTime']#line:305
                    OO0000000O0000000 =OO0O00O000OO0OO0O ['rewards'][0 ]['num']#line:306
                    OOO0OO0OOO0O0O0OO =OO0O00O000OO0OO0O ['rewards'][0 ]['name']#line:307
                    O0O00O000OO000OO0 +=int (OO0000000O0000000 .split ('+')[1 ].split ('.')[0 ])#line:308
                    OO0000OO0OOOO000O +=1 #line:309
                    print ('工作记录:    %s'%O0O0000OOO0OO0O0O +'丨%s'%O00O0O0OO0000000O +'-%s'%OO0000O0O0O00O0OO +'丨%s'%OOO0OO0OOO0O0O0OO +':%s'%OO0000000O0000000 )#line:310
                    if OO0000OO0OOOO000O >9 :#line:311
                        break #line:312
                OO00O0O0OOOOOOOO0 =requ_encrypt (json .dumps ({"propId":"4"}))#line:313
                O00O0O00O00OO0000 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/prop/recycle/config?uid={OOO00OO00O0000O00.uid}&version={version}',headers =OOO00OO00O0000O00 .headers ,data =OO00O0O0OOOOOOOO0 ).text ))#line:316
                if 'brick'in O00O0O00O00OO0000 :#line:317
                    OO0OOOO0O00O00OOO =O00O0O00O00OO0000 ['brick']['price']#line:318
                    c =float (Decimal (str (O0O00O000OO000OO0 ))*Decimal (str (OO0OOOO0O00O00OOO )))#line:319
                print ('工作记录:    打工记录获得砖块:%s'%O0O00O000OO000OO0 +'丨预计获得%s金币'%(int (c *100 )/100 ))#line:320
        except Exception as O0OOOO0O00O000O00 :#line:321
            print (O0OOOO0O00O000O00 )#line:322
    def work_start (OO0O00O000O0O00O0 ):#line:326
        global c ,jobId_new #line:327
        try :#line:328
            OO0OO0O0O00OO0OOO =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={OO0O00O000O0O00O0.uid}&version={version}',headers =OO0O00O000O0O00O0 .headers ).text ))#line:330
            if 'status'in OO0OO0O0O00OO0OOO :#line:331
                if OO0OO0O0O00OO0OOO ['status']==0 :#line:332
                    if float (OO0OO0O0O00OO0OOO ['bodyEnergy'])<1 :#line:333
                        OO0O00O000O0O00O0 .work_sleep ()#line:334
                    OO00OO00O0O00OOO0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={OO0O00O000O0O00O0.uid}&version={version}',headers =OO0O00O000O0O00O0 .headers ).text ))#line:335
                    O000OOO000000OOO0 =OO00OO00O0O00OOO0 ['bodyEnergy']#line:336
                    O00000OOO000000O0 =OO0O00O000O0O00O0 .rate_log ()#line:337
                    if Decimal (O00000OOO000000O0 )>Decimal (jobIds ):#line:338
                        if Decimal (str (O000OOO000000OOO0 ))>Decimal (str (physical_power )):#line:339
                            if jobIda :#line:340
                                jobId_new =OO0O00O000O0O00O0 .rate_choose ()#line:341
                            else :#line:342
                                jobId_new =jobId #line:343
                            OO0OOOO0O0OOOOOO0 =requ_encrypt (json .dumps ({"areaId":areaId ,"foodId":str (prop_food ),"waterId":str (prop_water ),"jobId":str (jobId_new )}))#line:344
                            OOO00O00O0OOOO0O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/start?uid={OO0O00O000O0O00O0.uid}&version={version}',headers =OO0O00O000O0O00O0 .headers ,data =OO0OOOO0O0OOOOOO0 ).text ))#line:345
                            if 'message'in OOO00O00O0OOOO0O0 :#line:346
                                print (f'工作工作:    设定行业或者最高回报是{jobId_new}丨{OOO00O00O0OOOO0O0["message"]}  😷')#line:347
                    else :#line:348
                        print ('工作工作:    回报趋势不达标还是去睡觉吧  😅')#line:349
                        OO0O00O000O0O00O0 .work_sleep ()#line:350
                elif OO0OO0O0O00OO0OOO ['status']==1 :#line:352
                    print ('工作工作:    睡觉中    😴')#line:353
                    if immediately :#line:354
                        for O0000O0OOOO00O00O in immediately_time .split ('#'):#line:356
                            O00000OOO000000O0 =OO0O00O000O0O00O0 .rate_log ()#line:358
                            if Decimal (O00000OOO000000O0 )>Decimal (jobIds ):#line:359
                                if float (OO0OO0O0O00OO0OOO ['bodyEnergy'])>21 :#line:360
                                    if str (datetime .datetime .now ().hour )==O0000O0OOOO00O00O :#line:361
                                        print ('工作工作:    当前时段设置立即醒来工作    🏃')#line:362
                                        requests .post (f'{host}/v4/api/work/sleep/stop?uid={OO0O00O000O0O00O0.uid}&version={version}',headers =OO0O00O000O0O00O0 .headers )#line:363
                                        time .sleep (random .randint (15 ,25 )/10 )#line:364
                                        if jobIda :#line:365
                                            jobId_new =OO0O00O000O0O00O0 .rate_choose ()#line:366
                                        else :#line:367
                                            jobId_new =jobId #line:368
                                        OO0OOOO0O0OOOOOO0 =requ_encrypt (json .dumps ({"areaId":areaId ,"foodId":str (prop_food ),"waterId":str (prop_water ),"jobId":str (jobId_new )}))#line:369
                                        OOO00O00O0OOOO0O0 =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/start?uid={OO0O00O000O0O00O0.uid}&version={version}',headers =OO0O00O000O0O00O0 .headers ,data =OO0OOOO0O0OOOOOO0 ).text ))#line:370
                                        if 'message'in OOO00O00O0OOOO0O0 :#line:371
                                            print (f'工作工作:    设定行业或者最高回报是{jobId_new}丨{OOO00O00O0OOOO0O0["message"]}  😷')#line:372
                                            break #line:373
                                else :#line:374
                                    print ('工作工作:    体力不足还是去睡觉吧  😅')#line:375
                            else :#line:376
                                print ('工作工作:    回报趋势不达标还是去睡觉吧  😅')#line:377
                        OO0O00O000O0O00O0 .work_sleep ()#line:378
                elif OO0OO0O0O00OO0OOO ['status']==2 :#line:379
                    print ('工作工作:    打工中    😷')#line:380
        except Exception as OO000OOO000O0000O :#line:381
            print (OO000OOO000O0000O )#line:382
    def sjc_ok (OOO0O000O0O000O00 ):#line:383
        try :#line:384
            if OOO0O000O0O000O00 .vein <OOO0O000O0O000O00 .vip ['World_City']['edition']:#line:385
                print (f'当前版本=>>{OOO0O000O0O000O00.vein}'+f'丨远程版本=>>{OOO0O000O0O000O00.vip["World_City"]["edition"]}   ❌')#line:386
                print (f'更新内容=>>{OOO0O000O0O000O00.vip["World_City"]["content"]}   👍')#line:387
            else :#line:388
                print (f'当前版本=>>{OOO0O000O0O000O00.vein}'+f'丨远程版本=>>{OOO0O000O0O000O00.vip["World_City"]["edition"]}   ✅')#line:389
                print (f'更新内容=>>{OOO0O000O0O000O00.vip["World_City"]["content"]}   👍')#line:390
        except Exception as O0OO00O00OOOOOO00 :#line:391
            print (O0OO00O00OOOOOO00 )#line:392
    def work_sleep (O000O00O00OO0OO00 ):#line:395
        try :#line:396
            O0O0O0OOOOO000O0O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep?uid={O000O00O00OO0OO00.uid}&version={version}',headers =O000O00O00OO0OO00 .headers ).text ))#line:397
            if O0O0O0OOOOO000O0O ['status']==0 :#line:398
                O0OOO0O0OO0OO000O =json .loads (resp_decrypt (requests .post (f'{host}/v4/api/work/sleep/start?uid={O000O00O00OO0OO00.uid}&version={version}',headers =O000O00O00OO0OO00 .headers ).text ))#line:399
                if 'message'in O0OOO0O0OO0OO000O :#line:400
                    print ('睡觉睡觉:    %s'%O0OOO0O0OO0OO000O ['message'])#line:401
        except Exception as O000O000OOOOOO000 :#line:402
            print (O000O000OOOOOO000 )#line:403
    def emoji_online (O00O0O000000O0000 ):#line:406
        try :#line:407
            json .loads (resp_decrypt (requests .post (f'{host}/api/lottery/senior/timer?uid={O00O0O000000O0000.uid}&version={version}',headers =O00O0O000000O0000 .headers ).text ))#line:409
        except Exception as OOO0OOOOOO0O0OO00 :#line:410
            print (OOO0OOOOOO0O0OO00 )#line:411
def sjc_vv ():#line:417
    return str ((70 -56 )/10 )#line:418
public_key ='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiWc4m3QbX51xTpt4snwGSnvI42SpbgAYFiL8wLgnzC9G7i5luSrfAP0A+MQbRSH42zc1oVO4NMwky7sfSqJFHc0cEcc9Ck3EmQHesdUAbyzq+DN+DU75YuVEyR1tbWeMZYuxBvN8DyFt53CV+6yD0EzTHg8t0yIfIY90h4+oRNN+YbLEuXOHOaLfU4hYKmPyCn6JPde1bsgd6wkGiFNCC6Thw+ut7jKopaeTCPx62s7aX0OrEe1mKV/xwqsr3qRUh3nn1hAtZr8XJHNpNwm3vS2c8HCaTVkU6N4bw8GtGrDhAYg5RVVFIjXJluHoiaNR2AYgo65yxa3vBfr4At+DrwIDAQAB'#line:424
def public_key_decrypt (O0O0OO00O000OO0OO ,OOOOO0OO000OOO00O ):#line:427
    try :#line:428
        O0OO00O0000OOO000 =len (OOOOO0OO000OOO00O )%4 #line:429
        if O0OO00O0000OOO000 !=0 :#line:430
            OOOOO0OO000OOO00O +='='*(4 -O0OO00O0000OOO000 )#line:431
        O0O0O0O000OO00O00 =base64 .b64decode (OOOOO0OO000OOO00O )#line:432
        OO0000OO00O00000O =base64 .b64decode (O0O0OO00O000OO0OO )#line:433
        O0OO0O0O00O00OOO0 =PublicKey .load_pkcs1_openssl_der (OO0000OO00O00000O )#line:434
        O0OOO0OO000O0000O =transform .bytes2int (O0O0O0O000OO00O00 )#line:435
        OOO0O0OOO0OO00000 =core .decrypt_int (O0OOO0OO000O0000O ,O0OO0O0O00O00OOO0 .e ,O0OO0O0O00O00OOO0 .n )#line:436
        O0O0O0O000O00000O =transform .int2bytes (OOO0O0OOO0OO00000 )#line:437
        OO0000000OOOO0O00 =O0O0O0O000O00000O [O0O0O0O000O00000O .index (0 )+1 :]#line:438
        return OO0000000OOOO0O00 .decode ()#line:439
    except Exception as OOOO0OOOO00000OOO :#line:440
        print (f"RSA解密发生错误：{OOOO0OOOO00000OOO}")#line:441
        return None #line:442
def public_key_encrypt (OOO0O00O000O0O0O0 ,O0O0OOOO000OO00O0 ):#line:445
    try :#line:446
        OO0OOO00O00OOO0O0 =base64 .b64decode (OOO0O00O000O0O0O0 )#line:447
        O0OO0O0O0OOO000O0 =PublicKey .load_pkcs1_openssl_der (OO0OOO00O00OOO0O0 )#line:448
        OOO00O0O00000OOOO =rsa .encrypt (base64 .b64decode (O0O0OOOO000OO00O0 .encode ()),O0OO0O0O0OOO000O0 )#line:449
        return base64 .b64encode (OOO00O0O00000OOOO ).decode ()#line:450
    except Exception as O00OO0OOOO00O00OO :#line:451
        print (f"RSA加密发生错误：{O00OO0OOOO00O00OO}")#line:452
        return None #line:453
def sjc_yz ():#line:456
    try :#line:457
        return requests .get (f'{git}/vastzzzl/vastzzzl/raw/master/edition').json ()#line:458
    except Exception as OOOO00OOO00OOOOO0 :#line:459
        sys .exit (0 )#line:460
def add_to_16 (OO0O0O0O0OOOO000O ):#line:463
    while len (OO0O0O0O0OOOO000O )%16 !=0 :#line:464
        OO0O0O0O0OOOO000O +='\0'#line:465
    return str .encode (OO0O0O0O0OOOO000O )#line:466
def get_key (OOO0OOOOOOO0O0000 ):#line:469
    OO0O0OO0OO00O0O0O =int (OOO0OOOOOOO0O0000 )#line:470
    O00O0OOO0OO0OOO0O ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'#line:471
    OOO00OO0OOOO0OOOO =len (O00O0OOO0OO0OOO0O )-1 #line:472
    OO00OO0O0O00O0OOO =''#line:473
    for O0OO0O0OO00O00OOO in range (OO0O0OO0OO00O0O0O ):#line:474
        OO00OO0O0O00O0OOO +=O00O0OOO0OO0OOO0O [random .randint (0 ,OOO00OO0OOOO0OOOO )]#line:475
    return OO00OO0O0O00O0OOO #line:476
def getRandomKey (OOOO000OO0OO00000 ):#line:479
    OO0000OO0000O0OOO ='0123456789abcdef'#line:480
    OOO00OOOOO0O000OO =''#line:481
    for OO0O0O0OOOO00OO00 in range (OOOO000OO0OO00000 *2 ):#line:482
        OOO00OOOOO0O000OO +=OO0000OO0000O0OOO [random .randint (0 ,len (OO0000OO0000O0OOO )-1 )]#line:483
    return base64 .b64encode (bytes .fromhex (OOO00OOOOO0O000OO )).decode ()#line:484
def aes_decrypt (O00O00O0O0OO00O0O ,OOOOOOO0O000OO000 ,O0OOOOO0O00000OO0 ):#line:487
    O0O000O0O000OOOOO =AES .new (add_to_16 (O00O00O0O0OO00O0O ),AES .MODE_CBC ,add_to_16 (OOOOOOO0O000OO000 ))#line:488
    OOO0O0O0O000O0O0O =base64 .decodebytes (O0OOOOO0O00000OO0 .encode (encoding ='utf-8'))#line:489
    O0O0OOO0OO000O00O =re .compile ('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub ('',O0O000O0O000OOOOO .decrypt (OOO0O0O0O000O0O0O ).decode ())#line:491
    return O0O0OOO0OO000O00O #line:492
def aes_encrypt (O0O000OOOO0OOOOOO ,O00O00O00O0000OO0 ,O00OOOO00OOOOOOO0 ):#line:495
    __OO00O000O0O000O00 =AES .block_size #line:496
    O000OO00OOOO00OOO =AES .new (base64 .b64decode (O0O000OOOO0OOOOOO .encode ()),AES .MODE_CBC ,O00O00O00O0000OO0 .encode ())#line:497
    OOOO0OO0O00OOOO0O =__OO00O000O0O000O00 -(len (O00OOOO00OOOOOOO0 )%__OO00O000O0O000O00 )#line:498
    if OOOO0OO0O00OOOO0O !=0 :#line:499
        O00OOOO00OOOOOOO0 =O00OOOO00OOOOOOO0 +chr (OOOO0OO0O00OOOO0O )*OOOO0OO0O00OOOO0O #line:500
    O000O0OOOOO0OO0O0 =O000OO00OOOO00OOO .encrypt (O00OOOO00OOOOOOO0 .encode ('utf-8'))#line:501
    OO00O0OO0O000OO00 =base64 .encodebytes (O000O0OOOOO0OO0O0 ).decode ()#line:502
    return OO00O0OO0O000OO00 #line:503
def requ_encrypt (O000O0O0OOOOOO0O0 ):#line:506
    try :#line:507
        OO0OOOOOO00O0OO0O =getRandomKey (32 )#line:508
        O00OO0O0OOOO00000 =get_key (16 )#line:509
        OO0O0O0O0O0O0OO00 =public_key_encrypt (public_key ,OO0OOOOOO00O0OO0O )#line:510
        OOOOO0OOO00O000OO =aes_encrypt (OO0OOOOOO00O0OO0O ,O00OO0O0OOOO00000 ,O000O0O0OOOOOO0O0 )#line:511
        OOO0OO00O0O0O00O0 =OO0O0O0O0O0O0OO00 +'.'+O00OO0O0OOOO00000 +OOOOO0OOO00O000OO #line:512
        return OOO0OO00O0O0O00O0 #line:513
    except Exception as OOO000O00O00O0O0O :#line:514
        print (f"Request加密失败：{OOO000O00O00O0O0O}")#line:515
        return None #line:516
def resp_decrypt (O000OO0O0O00O0OOO ):#line:519
    try :#line:520
        if '.'not in O000OO0O0O00O0OOO :#line:521
            return O000OO0O0O00O0OOO #line:522
        OOOOOO0OO0O0O0O0O =O000OO0O0O00O0OOO .split ('.')[0 ]#line:523
        OO0O00OO000000O0O =O000OO0O0O00O0OOO .split ('.')[1 ]#line:524
        O00OOOO0000OOOOOO =public_key_decrypt (public_key ,OOOOOO0OO0O0O0O0O )#line:525
        if O00OOOO0000OOOOOO !=None :#line:526
            OO00OO00OO0000O0O =OO0O00OO000000O0O [:16 ]#line:527
            OO0OO0000O0O00000 =OO0O00OO000000O0O [16 :]#line:528
            OOO000OOO0O0O00O0 =aes_decrypt (O00OOOO0000OOOOOO ,OO00OO00OO0000O0O ,OO0OO0000O0O00000 )#line:529
            return OOO000OOO0O0O00O0 #line:530
        else :#line:531
            return None #line:532
    except Exception as O00000OOOOO0OOO0O :#line:533
        print (f"response加密失败：{O00000OOOOO0OOO0O}")#line:534
if __name__ =='__main__':#line:538
    main ()#line:539
