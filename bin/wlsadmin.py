#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/7 下午4:18
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/


import os
import sys
import commands
import time
import subprocess

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(baseDir)
from core.init import *
from core.procmgr import KillProc
from core.servermgr import optServer
from core.createscript import createscript
from core.serverconfig import domain_config

# 通过解析config.xml获取当前weblogic domain中所配置的所有受管服务器的配置信息
servers = domain_config()


# 1.基础服务运行状态检测
def envCheck():
    for service in serviceList.split(','):
        host = ipAddr
        servicePort = service + 'Port'
        port = eval(servicePort)  # 端口必须为数字
        service_status = KillProc(host, port).port_check()
        if service_status:
            print u"在%s服务器上服务端口为 %s 的 %s 服务正在运行......" % (host, port, service)
        else:
            print u"在%s服务器上服务端口为 %s 的 %s 服务未运行!" % (host, port, service)
            # optBasicService(service, 'START')


# 2.基础服务管理
def startService():
    for service in serviceList.split(','):
        host = ipAddr
        port = int(eval(service + 'Port'))  # 端口必须为数字
        service_status = KillProc(host, port).port_check()
        cmd = eval(service + 'CMD')
        if service_status:
            print u"在%s服务器上服务端口为 %d 的 %s 服务已在运行......" % (host, port, service)
        else:
            subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            time.sleep(3)
            opt_status = KillProc(host, port).port_check()
            if opt_status:
                print u"在%s服务器上服务端口为 %d 的 %s 服务启动成功!" % (host, port, service)
            else:
                print u"在%s服务器上服务端口为 %d 的 %s 服务启动失败! " % (host, port, service)


# 2.关闭基础服务
def stopService():
    for service in serviceList.split(','):
        host = ipAddr
        port = int(eval(service + 'Port'))  # 端口必须为数字
        killserver = KillProc(host, port)
        killserver.killProc()


# 3.重启基础服务
def restartService():
    stopService()
    startService()


# 4.启动服务器
def startserver():
    while True:
        inputserver = raw_input("请输入要启动服务器名(多个以,隔开):")
        if inputserver in servers and KillProc(ipAddr, servers[inputserver]).port_check() is not True:
            optServer(inputserver, 'START')
            break
        elif KillProc(ipAddr, servers[inputserver]).port_check():
            print "%s 服务器已在运行!\n" % inputserver
            break
        elif inputserver not in servers:
            print "%s 服务器不存在请重新输入!\n" % inputserver


# 5.关闭服务器
def stopserver():
    while True:
        inputserver = raw_input("请输入要启动服务器名(多个以,隔开):")
        if inputserver in servers:
            optServer(inputserver, 'STOP')
            break
        else:
            print "%s 服务器不存在请重新输入!\n" % inputserver


# 6.重启服务器
def restartserver():
    while True:
        inputserver = raw_input("请输入要启动服务器名(多个以,隔开):")
        if inputserver in servers:
            port = serverConfig[inputserver]
            KillProc(ipAddr, port).killProc()
            optServer(inputserver, 'START')
            break
        else:
            print "%s 服务器不存在请重新输入!\n" % inputserver


# 7.查看服务器状态
def stateserver():
    while True:
        inputserver = raw_input("请输入要启动服务器名(多个以,隔开):")
        for s in inputserver.split(","):
            if s in servers:
                server_port = servers[s]
                server_status = KillProc(ipAddr, server_port)
                if server_status:
                    print "%s : %s" % (s, "RUNNING")
                else:
                    print "%s :%s" % (s, "SHUTDOWN")
            else:
                print "%s 服务器不存在!\n" % inputserver
        break


# 8.一键启动所有服务器
def start_allservers():
    for server in serverList.split(","):
        server_status = KillProc(ipAddr, serverConfig[server]).port_check()
    if server_status:
        print "%s 服务器已在运行..." % server
    elif server in servers:
        optServer(server, "START")


# 9.一键查看所有服务器状态
def stop_allservers():
    for server in serverList:
        server_status = KillProc(ipAddr, serverConfig[server]).port_check()
        if server in servers and server_status is not True:
            print "%s 服务器已关闭!" % server
        elif server in servers:
            optServer(server, "STOP")


# 欢迎菜单
def interactive():
    menu = """
    --------欢迎使用 WebLogic Server 管理工具 --------
        1. 启动基础服务
        2. 关闭基础服务
        3. 重启基础服务
        4. 启动服务器
        5. 关闭服务器
        6. 重启服务器
        7. 查看服务器状态
        8. 启动所有服务器
        9. 关闭所有服务器
        0. 退出程序
    -----------------------------------------------
    """
    menu_dict = {
        '1': 'startService()',
        '2': 'stopService()',
        '3': 'restartService()',
        '4': 'startserver()',
        '5': 'stopserver()',
        '6': 'restartserver()',
        '7': 'stateserver()',
        '8': 'start_allservers()',
        '9': 'stop_allservers()',
        '0': 'sys.exit()'
    }

    while True:
        print menu
        user_option = raw_input(">>:").strip()
        if user_option in menu_dict:
            eval(menu_dict[user_option])
        else:
            print "您输入的操作不存在,请重新输入!\n"


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        interactive()
    elif len(sys.argv[1:]) >= 1 and sys.argv[1] == "server":
        startService()
        start_allservers()
