#!/usr/bin/env python
"""
@Time ： 2022/4/11 18:51
@Auth ： 赵凌子
@File ： data.py
@IDE ：  PyCharm
@Motto： After all,tomorrow is another day.
"""
# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
from EmQuantAPI import *
import platform
#手动激活范例(单独使用) #获取当前安装版本为x86还是x64
# data = platform.architecture()
# if data[0] == "64bit":
#     bit = "x64"
# elif data[0] == "32bit":
#     bit = "x86"
# data1 = platform.system()
#
# if data1 == 'Linux':
#     system1 = 'linux'
#     lj = c.setserverlistdir("libs/" + system1 + '/' + bit)
# elif data1 == 'Windows':
#     system1 = 'windows'
#     lj = c.setserverlistdir("libs/" + system1)
# elif data1 == 'Darwin':
#     system1 = 'mac'
#     lj = c.setserverlistdir("libs/" + system1)
# else:
#     pass
# #调用manualactive函数，修改账号、密码、有效邮箱地址，email=字样需保留
# data = c.manualactivate("18356955061", "zlzlove0427", "email=zhaolz0828@163.com")
# if data.ErrorCode != 0:
#         print ("manualactivate failed, ", data.ErrorMsg)

from EmQuantAPI import *
from datetime import timedelta, datetime
import time as _time
import traceback
from EmQuantAPI import *
loginresult = c.start( )
#loginresult为c.EmQuantData类型数据
print (loginresult)
data = c.edb("EMM00087117","IsPublishDate=1,RowIndex=1,Ispandas=1")
print(data)