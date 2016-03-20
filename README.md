# sysinfo_recorder
`LOGPATH`为cpu信息记录log保存路径 `ERRORPATH`为服务程序发生异常时，错误保存路径，timewait为cpu信息获取间隔
## 使用方法：
* ./sysinfo_recorder.py
## 存在问题：
* log文件保存方式为txt文件，没有对文件增长进行限制
* 保存数据不够直观，以折线走向图最为直观，但是实现需要web环境，实现比较复杂，同时数据保存在数据库中，能实现查看自定义时间段内的cpu数据
