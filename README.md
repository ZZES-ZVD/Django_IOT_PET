# Django_IOT_PET
Use Django to make IOT_PET .

## Get Start
```
pip install Django

pip install pymysql

python manage.py makemigrations

python manage.py migrate
```

==========日志 ================
 - 2017.5.18 登录注册逻辑
 - 2017.5.19 Flat UI制作界面.主页轮播，信息页的硬件介绍和视频展示。解决静态文件相关问题。完成数据可视化。
 - 2017.5.20 创建mysite_iotdata数据表。设置/zzesadmin为专属后台页面。
 - 2017.5.23 完成讨论留言页面的编写
 - 2017.5.15 增加按钮控制，提供接口来存储按钮命令；再提供数据统计接口将统计后的触发数量显示出来。前端data页面通过ajax获取接口
 - 2017.5.16 更改页面数据更新时间，之前10毫秒，我错了。。。现在是2秒更新一次，基本保证实时性。