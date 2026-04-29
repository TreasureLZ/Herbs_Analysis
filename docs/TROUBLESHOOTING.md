# 常见问题

## 数据库连接失败

请检查：

- MySQL 服务是否已经启动
- 是否已经创建 `materialsdb` 数据库
- `DATABASES` 中的用户名、密码、端口是否正确
- 脚本中的 `create_engine` 连接信息是否同步修改

## 导入 SQL 失败

请确认：

- 数据库字符集建议使用 `utf8mb4`
- SQL 文件是否完整
- 当前 MySQL 用户是否有建表和写入权限
- SQL 文件中的数据库名是否和本地数据库名一致

## `ModuleNotFoundError`

说明依赖没有安装完整。请根据报错逐个安装缺失依赖，例如：

```bash
pip install django pymysql pandas openpyxl
```

## 页面可以打开但没有图表

请检查：

- 数据库中是否已经导入数据
- 浏览器控制台是否有 JavaScript 报错
- 图表接口是否返回数据
- 静态资源是否正常加载

## 后台无法登录

如果没有管理员账号，执行：

```bash
python manage.py createsuperuser
```

然后访问：

```text
http://127.0.0.1:8000/admin
```

## 重新采集数据后没有变化

请检查：

- 爬虫输出目录是否正确
- 数据库是否重新导入或写入成功
- 页面查询的数据表是否和脚本写入的数据表一致
- 浏览器是否缓存旧页面
