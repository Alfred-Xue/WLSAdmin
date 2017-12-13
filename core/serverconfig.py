#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/11 下午5:31
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import os, sys

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(baseDir)
from core.init import domainConfig
import xml.etree.ElementTree as ET

tree = ET.parse(domainConfig)
# tree = ET.parse("config.xml")
root = tree.getroot()


def domain_config():
    servers = {}
    # for node in root.iter('{http://xmlns.oracle.com/weblogic/domain}server'): # 2.7版本后的语法
    for node in root.getiterator('{http://xmlns.oracle.com/weblogic/domain}server'):  # 2.4版本后的语法4
        for i in node:
            if i.tag == '{http://xmlns.oracle.com/weblogic/domain}name':
                server_name = i.text
            elif i.tag == '{http://xmlns.oracle.com/weblogic/domain}listen-port':
                server_port = i.text
                servers[server_name] = server_port
                servers["AdminServer"] = 7001
    return servers

# 可以单独运行已打印当前所有服务器的配置
if __name__ == "__main__":
    serverconfig = domain_config()
    for (k, v) in serverconfig.items():
        print "服务器名:%s 服务器端口:%d" %(k, v)
