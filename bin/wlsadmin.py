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


# # 2.重启基础服务
# def restartService():
#     stopService()
#     startService()


# 3.启动服务器
def startserver():
    while True:
        inputserver = raw_input("请输入服务器名(多个以','隔开):").strip()
        for server_name in inputserver.split(","):
            if server_name in servers:
                server_port = int(servers[server_name])
                server_status = KillProc(ipAddr, server_port).port_check()
                if server_status is not True:
                    optServer(server_name, 'START')
                elif server_status is True:
                    print "%s 服务器已在运行!\n" % server_name
            else:
                print "%s 服务器不存在!!\n" % server_name
        break


# 4.关闭服务器
def stopserver():
    while True:
        inputserver = raw_input("请输入服务器名(多个以','隔开):").strip()
        for server_name in inputserver.split(","):
            if server_name in servers:
                server_port = int(servers[server_name])
                server_status = KillProc(ipAddr, server_port).port_check()
                if server_status is True:
                    optServer(server_name, 'STOP')
                elif server_status is not True:
                    print "%s 服务器已关闭!\n" % server_name
            else:
                print "%s 服务器不存在请重新输入!\n" % server_name
        break


# 5.重启服务器
def restartserver():
    while True:
        inputserver = raw_input("请输入服务器名(多个以','隔开):").strip()
        for server_name in inputserver.split(","):
            if server_name in servers:
                server_port = int(servers[server_name])
                server_status = KillProc(ipAddr, server_port).port_check()
                if server_status is True:
                    optServer(server_name, 'STOP')
                    optServer(server_name, "START")
                elif server_status is not True:
                    optServer(server_name, "START")
            else:
                print "%s 服务器不存在请重新输入!\n" % server_name
        break


# 6.查看服务器状态
def stateserver():
    while True:
        inputserver = raw_input("请输入服务器名(多个以','隔开):").strip()
        print "%-14s     :%-4s" % ("服务器名称", "状态")
        for s in inputserver.split(","):
            if s in servers:
                server_port = servers[s]
                server_status = KillProc(ipAddr, server_port)
                if server_status:
                    print "%-14s :%-4s" % (s, "RUNNING")
                else:
                    print "%-14s :%-4s" % (s, "SHUTDOWN")
            else:
                print "%s 服务器不存在!\n" % s
        break


# 7.启动所有服务器
def start_allservers():
    for server in serverList.split(","):
        if server in servers:
            server_port = int(servers[server])
            server_status = KillProc(ipAddr, server_port).port_check()
            if server_status is True:
                print "%s 服务器已在运行..." % server
            else:
                while KillProc(ipAddr, server_port).port_check() is not True:
                    optServer(server, "START")


# 8.查看所有服务器状态
def state_allservers():
    print "%-14s :%-4s" % ("服务器名称", "状态")
    for (server_name, server_port) in servers.items():
        server_status = KillProc(ipAddr, int(server_port)).port_check()
        if server_status:
            print "%-14s :%s" % (server_name, "RUNNING")
        else:
            print "%-14s :%s" % (server_name, "SHUTDOWN")


# 9.关闭所有服务器
def stop_allservers():
    for server in serverList.split(","):
        server_port = int(servers[server])
        server_status = KillProc(ipAddr, server_port).port_check()
        if server_status:
            optServer(server, "STOP")
        else:
            print "%s 服务器已关闭!" % server


# 欢迎菜单
def interactive():
    menu = """
    --------欢迎使用 WebLogic Server 管理工具 --------
        1. 启动基础服务
        2. 关闭基础服务
        3. 启动服务器
        4. 关闭服务器
        5. 重启服务器
        6. 查看服务器状态
        7. 启动所有服务器
        8. 所有服务器状态
        9. 关闭所有服务器
        0. 退出程序
    -----------------------------------------------
    """
    menu_dict = {
        '1': 'startService()',
        '2': 'stopService()',
        '3': 'startserver()',
        '4': 'stopserver()',
        '5': 'restartserver()',
        '6': 'stateserver()',
        '7': 'start_allservers()',
        '8': 'state_allservers()',
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
    """
    根据传参选择启动方式:
    # 1.交互式
    python bin/wlsadmin.py
    # 2.非交互式(直接启动所有服务)
    python bin/wlsadmin.py server
    """
    if len(sys.argv[1:]) == 0:
        startService()
        interactive()
    elif len(sys.argv[1:]) >= 1 and sys.argv[1] == "server":
        startService()
        start_allservers()
