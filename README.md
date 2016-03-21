# guide
`guide_server.py`为guide的服务端，`guide_client.py`为guide的客户端

## 使用方法：
### 服务端：
* 文件里面port为服务端监听端口，默认为4000， maxclient为最大连接数
* ERRORPATH为服务端报错保存的日志地址，VALUEPATH为供查询的文件路径，文件格式为`key=value`
* 启用方法之间运行./guide_server.py
### 客户端：
* ./guide_client.py IP 端口
* 在`$`后直接输入`key`，回车，客户端将从服务的获取`value`，如不存在则返回`Null`

