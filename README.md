# cron_ctrl
脚本采用python2.7编写，通过修改`/etc/crontab`来实现启用和停止任务

## 使用方法：
* ./cron_ctrl.py job --start   启用job任务
* ./cron_ctrl.py job --stop    停止job任务
* ./cron_ctrl.py job --list    显示grep到的crontab行
