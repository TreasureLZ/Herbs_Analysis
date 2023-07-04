## 项目简介
这次分享药材数据可视化系统的设计与实现，主要针对各类药材数据做一个统计分析可视化。

本系统基于 **Django+MVT+Mysql** 。涉及技术比较简单，易于理解，适合**PythonWeb初学者**学习使用。

## 技术栈

### 编辑器

PyCharm  2023.1 (旗舰版)

### 前端技术

基础：Html+Css+JavaScript+Echarts

框架：[BootStrap](https://www.bootcss.com/)+[JQuery](https://jquery.com/)

### 后端技术

Django+爬虫+数据清洗与可视化

数据库：MySQL 8.0.26（个人测试使用）

Python版本：3.9.16（个人测试使用）

Django版本：4.2.2（个人测试使用）

## 本地运行

1.下载zip直接解压或安装git后执行克隆命令

```https://github.com/TreasureLZ/Herbs_Analysis.git```

2.使用 Pycharm 打开项目，配置python编译环境

3.打开Navicat For Mysql（也就是数据库管理工具），创建 **materialsdb** 数据库（命令行也可以）

**如果不需要爬虫和数据清洗请跳过 4、5 步骤，选择执行第 6 步骤**

4.创建完数据库后，如果要自定义数据，则执行数据库同步指令。
先切换目录分为两步骤 `python manage.py makemigrations` ，再执行 `python manage.py migrate`

5.如果需要自定义数据，请调用 **reptile.py** 爬虫文件。爬虫结果会写入 **data** 目录文件里面（多次采集同一个要差会覆盖）

6.复制 **materialsDB.sql** 中的文件内容运行。（不需要爬虫和数据清洗可以直接执行）

7.修改 **setting.py** 中数据库相关的内容。

8.使用命令启动 Django 项目 `python manage.py runserver`

9.通过浏览器访问系统主页面（包括后台）

* 前台首页：`http://127.0.0.1:8000/`
* 后台首页：`http://127.0.0.1:8000/admin`

## 注意

* 注意 Django 项目启动应该先切入`cd manage.py所在目录`。
* 注意**修改setting.py**中数据库相关的内容。
* 系统中不存在后台管理员账号，可以**使用命令`python manage.py createsuperuser`创建**即可。
* 自定义数据的话，需要调用 django 里面的数据库同步指令。
* **reptile.py**文件中，需要修改 `create_engine` 里面的账号密码以及数据库

## 项目截图

#### 登录
![登录](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/登录.jpg)
#### 注册
![注册](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/注册.jpg)
#### 首页
![首页](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/首页.jpg)
#### 药材Top20
![药材Top20](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/药材Top20.jpg)
#### 药材价格
![药材价格](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/药材价格.jpg)
#### 产地占比
![产地占比](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/产地占比.jpg)
#### 历史价格
![历史价格](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/历史价格.jpg)
#### 新闻资讯
![新闻资讯](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/新闻资讯.jpg)
#### 后台管理
![后台管理](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/后台管理.jpg)
