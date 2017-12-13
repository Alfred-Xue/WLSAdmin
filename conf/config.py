#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Datetime : 2017/11/29 下午11:53
# @Author   : Alfred Xue
# @E-Mail   : Alfred.Hsueh@gmail.com
# @GitHub   : https://github.com/Alfred-Xue
# @Blog     : http://www.cnblogs.com/alfred0311/


class Config:
    # 服务器地址
    ipAddr = '172.16.5.204'
    # WebLogic Server 安装路径
    WLS_HOME = '/u01/weblogic'
    # WebLogic 域目录
    DOMAIN_HOME = '/home/oracle/config/domains/base_domain/'
    # WebLogic 域名称
    domainName = 'base_domain'
    # 管理服务器用户名
    adminUser = 'weblogic'
    # 管理服务器用户口令
    adminPwd = 'P@ssw0rd'
    # 管理服务器端口
    adminPort = 7001
    # 节点管理器用户名
    nmUser = 'ndmgr'
    # 节点管理器口令
    nmPwd = 'P@ssw0rd'
    # 节点管理器服务端口
    nmPort = 5556
    # 节点管理器质性路径
    nmPath = '/home/oracle/config/domains/base_domain/bin/'

    # 基础服务配置,
    serviceList = 'service1,service2,service3'
    # 基础服务1
    service1 = 'zookeeper'
    service1Port = 2181
    service1Path = '/opt/dubbo/zookeeper-3.4.4/'
    # 基础服务2
    service2 = 'Dubbo-monitor'
    service2Port = 8080
    service2Path = '/opt/dubbo/dubbo-monitor-simple-2.5.3/'
    # 受管服务器配置
    serverList = 'sso,uc-service,uc-view,xtxc-dubbo,xtxc-web,xtxc-ws,xtxc-ws-rest'
    serverConfig = {
        'AdminServer':7001,
        'sso': 7101,
        'uc-service': 7102,
        'uc-view': 7103,
        'xtxc-dubbo': 7201,
        'xtxc-web': 7204,
        'xtxc-ws': 7202,
        'xtxc-ws-rest': 7205
    }
