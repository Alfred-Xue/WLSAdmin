#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/8 上午11:09
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import commands
import subprocess
import sys
import time
from core.init import *
from core.procmgr import KillProc

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(baseDir)


# 基础服务状态监测
def env_monitor():
    for service_name in serviceList.split(','):
        service_port = service_name + 'Port'
        port = eval(service_port)  # 端口必须为数字
        if serviceList(ipAddr, port):
            print u"在%s服务器上服务端口为 %s 的 %s 服务已运行!" % (ipAddr, port, service_name)
        else:
            print u"在%s服务器上服务端口为 %s 的 %s 服务已关闭!" % (ipAddr, port, service_name)


# # 基础服务管理
# def optBasicService(host, port, name, opt, cmd):
#     status = KillProc(host,port).port_check()
#     if status:
#         print u"在%s服务器上服务端口为 %d 的 %s 服务已在运行......" % (host, port, name)
#     elif status != True and opt == "START":
#         (status, output) = commands.getstatusoutput(cmd)
#         if status == 0:
#             print u"在%s服务器上服务端口为 %d 的 %s 服务启动成功!" % (host, port, name)
#         else:
#             print u"在%s服务器上服务端口为 %d 的 %s 服务启动失败! 可能原因:%s" % (host, port, name, output)

# 基础服务管理
def optBasicService(host, port, name, opt, cmd):
    status = KillProc(host, port).port_check()
    if status:
        print u"在%s服务器上服务端口为 %d 的 %s 服务已在运行......" % (host, port, name)
    elif status != True and opt == "START":
        # (status, output) = commands.getstatusoutput(cmd)
        p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        status = KillProc(host, port).port_check()
        if status == 0:
            print u"在%s服务器上服务端口为 %d 的 %s 服务启动成功!" % (host, port, name)
        else:
            print u"在%s服务器上服务端口为 %d 的 %s 服务启动失败! 可能原因:%s" % (host, port, name, output)
