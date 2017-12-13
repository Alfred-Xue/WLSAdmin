#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/8 上午10:46
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import os
import sys
import datetime
baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(baseDir)
from core.init import *



# 判断一个路径是否存在,不存在则创建
def detechpath(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


# 生成jython运行脚本函数,返回值为执行脚本绝对路径
def createscript(name, opt):
    currentTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    scriptDir = os.path.join(baseDir, 'scripts/')
    detechpath(scriptDir)
    script = ''.join([currentTime, '.py'])
    scriptname = os.path.join(scriptDir, script)
    with open(scriptname, 'a') as f:
        # nmConn = "nmConnect('nmUser','nmPwd','nmHost','nmPort','domainName')"
        nmConn = "nmConnect('%s', '%s', '%s', '%s', '%s')\n" % (nmUser, nmPwd, nmHost, nmPort, domainName)
        f.write(nmConn)
        if opt == "START":
            servers = name.split(',')
            for serverName in servers:
                nmStart = "nmStart('%s')\n" % (serverName)
                f.write(nmStart)
        elif opt == "STOP":
            servers = name.split(',')
            for serverName in servers:
                nmKill = "nmKill('%s')\n" % (serverName)
                f.write(nmKill)
        elif opt == "STATE":
            servers = name.split(',')
            for serverName in servers:
                nmState = "nmServerStatus('%s')\n" % (serverName)
                f.write(nmState)
        f.write("exit()")
    return scriptname
