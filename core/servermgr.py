#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/8 下午2:12
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import commands
from core.createscript import createscript


# 管理服务器操作
def optServer(name, opt):
    scriptName = createscript(name, opt)
    cmd = 'java weblogic.WLST -i %s' % (scriptName)
    if opt == "START":
        (status, output) = commands.getstatusoutput(cmd)
        if status == 0:
            print u"%s启动成功!" % (name)
        else:
            print u"%s启动失败! 可能原因:%s" % (name, output)
    elif opt == "STOP":
        (status, output) = commands.getstatusoutput(cmd)
        if status == 0:
            print u"%s关闭成功!" % (name)
        else:
            print u"%s关闭失败! 可能原因:%s" % (name, output)
    elif opt == "STATE":
        (status, output) = commands.getstatusoutput(cmd)
        if status == 0:
            # print u"%s正在运行......" % (output)
            print output
        else:
            print output
