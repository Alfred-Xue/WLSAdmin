#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/12/8 上午10:40
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/
import os

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from conf import config

config = config.Config()

# 服务器地址
ipAddr = config.ipAddr
# WebLogic 域相关配置信息
WLS_HOME = config.WLS_HOME
DOMAIN_HOME = config.DOMAIN_HOME
domainName = config.domainName
domainConfig = ''.join([DOMAIN_HOME,'config/','config.xml'])

# 管理服务器配置
adminUser = config.adminUser
adminPwd = config.adminPwd
adminPort = config.adminPort
adminURL = ''.join(['t3://', ipAddr, ':', str(adminPort)])
startAS = ''.join(['java weblogic.WLST -i ', baseDir, '/scripts/', 'startAdminServer.py'])

# 节点管理器用户名
nmUser = config.nmUser
nmPwd = config.nmPwd
nmHost = ipAddr
nmPort = config.nmPort
nmPath = config.nmPath
startNM = ''.join(['nohup', ' ', nmPath, 'startNodeManager.sh',' ', '>/dev/null', ' ', '2>&1', ' ', '&'])

# 基础服务配置,
serviceList = config.serviceList
# 基础服务1(注册中心)
service1 = config.service1
service1Port = config.service1Port
service1Path = config.service1Path
service1CMD = ''.join([service1Path, 'bin/', 'zkServer.sh', ' ', 'start'])
# 基础服务2(监控中心)
service2 = config.service2
service2Port = config.service2Port
service2Path = config.service2Path
service2CMD = ''.join([service2Path, 'bin/', 'start.sh'])
# 基础服务3(节点管理器)
service3 = 'NodeManager'
service3Port = nmPort
service3CMD = startNM
# 基础服务4(管理服务器)
service4 = 'AdminServer'
service4Port = adminPort
service4CMD = startAS
# 受管服务器配置
serverList = config.serverList
serverConfig = config.serverConfig
