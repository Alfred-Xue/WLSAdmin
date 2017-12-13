### WebLogic Server 管理工具 (WLSAdmin )

#### [适用场景]
*操作系统:*
- Linux

*中间件:*
- WebLogic Server 11g
- WebLogic Server 12c

#### [功能概述]
1. 启动服务器(Administration Server and Mananged Server)
2. 关闭服务器(Administration Server and Mananged Server)
3. 服务器状态(Administration Server and Mananged Server)
4. 按照应用的顺序启动服务器


#### [使用帮助]

1. conf/config.py 根据此配置文件中的说明修改配置
2. 启动程序--交互式
```
[root@localhost ~]# cd WLSAdmin
[root@localhost WLSAdmin]# python bin/wlsadmin.py
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
 >>:  #此处输入上面打印出来的菜单选项进行相关操作
```
3. 非交互式启动所有服务
```
[root@localhost ~]# cd WLSAdmin
[root@localhost WLSAdmin]# python bin/wlsadmin.py server
# 运行脚本后面带'server'参数以启动所有服务,此方式适用于将服务设置为开机启动
```


