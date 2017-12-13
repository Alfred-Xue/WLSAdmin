#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/8 上午10:48
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import socket
import commands
import signal
import os
import time


class KillProc:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # 判断端口是否占用
    def port_check(self):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect((self.host, self.port))
            # print '在服务器 %s 上服务端口 %d 的服务正在运行!' % (host, port)
            return True
        except Exception:
            # print '在服务器 %s 上服务端口 %d 的服务未运行!' % (host, port)
            return False
        sk.close()

    # 根据端口号检索进程pid
    def fetchpid(self):
        cmd = "netstat -lntup | grep %d" % (self.port)
        # print "cmd:", cmd
        (status, output) = commands.getstatusoutput(cmd)
        # print "output:",len(output),output
        if status == 0:
            tlist = output.split()
            tnum = len(tlist)
            pid = tlist[tnum - 1].split('/')[0]
            return pid

    # 根据进程号杀死进程
    def killProc(self):
        while True:
            port_status = self.port_check()
            # print "端口号:",self.port
            # print "端口状态:",port_status
            pid = self.fetchpid()
            # print "进程号:",pid
            # print "pid格式",type(pid)
            if port_status and len(str(pid))>1 and pid is not None:
                os.kill(int(pid), signal.SIGKILL)
            else:
                break
        print '在服务器 %s 上服务端口为 %d 的服务已关闭!' % (self.host, self.port)
