# 药材数据可视化系统

> 项目状态：LTS 长期维护。当前项目主要保持学习可用、文档清晰和运行问题修复，不再做大规模架构重构。更多数据分析与可视化项目请查看总入口：[Django_Collection](https://github.com/TreasureLZ/Django_Collection)。

## 项目简介

本项目是一个基于 Django 的药材数据可视化系统，围绕药材价格、药材排名、产地占比、历史价格和新闻资讯等内容，提供完整的数据展示与后台管理案例。

项目流程：

```text
药材数据采集 -> 数据整理入库 -> Django 页面展示 -> ECharts 图表可视化 -> 后台管理
```

## 适合人群

- 想学习 Django + ECharts 数据可视化项目的初学者
- 需要行业数据分析类课程设计或毕业设计的学生
- 想把药材主题替换为商品、农产品、价格行情等主题的开发者
- 想参考完整 Web 可视化系统结构的同学

## 功能清单

- 用户登录与注册
- 药材数据展示
- 药材 Top20 统计
- 药材价格分析
- 产地占比分析
- 历史价格展示
- 新闻资讯页面
- Django 后台管理
- 药材数据采集脚本

## 技术栈

| 类型 | 技术 |
| --- | --- |
| 后端 | Python, Django, MVT |
| 数据库 | MySQL |
| 数据处理 | 爬虫, 数据整理脚本 |
| 前端 | HTML, CSS, JavaScript |
| UI 与交互 | Bootstrap, JQuery |
| 可视化 | ECharts |
| 推荐环境 | Python 3.9.16, Django 4.2.2, MySQL 8.0.26, PyCharm 2023.1 |

## 本地运行

### 1. 克隆项目

```bash
git clone https://github.com/TreasureLZ/Herbs_Analysis.git
cd Herbs_Analysis
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
python -m venv .venv
```

Windows 激活：

```powershell
.venv\Scripts\activate
```

如果项目中没有 `requirements.txt`，请根据运行报错补充安装 Django、PyMySQL、pandas、openpyxl 等依赖。

### 3. 创建数据库

在 MySQL 中创建数据库：

```sql
CREATE DATABASE materialsdb DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

### 4. 导入数据

如果只想快速运行项目，可以直接导入项目中的 SQL 文件：

```text
materialsDB.sql
```

如果需要重新采集数据，再执行：

- `reptile.py`：采集药材数据，并写入 `data` 目录。

多次采集同一类数据可能覆盖已有文件，执行前建议备份 `data` 目录。

### 5. 修改数据库配置

打开：

```text
djangoProject/djangoProject/settings.py
```

修改 `DATABASES` 中的数据库名、用户名、密码、主机和端口。

如果脚本中使用了 `create_engine`，也需要同步修改其中的数据库连接账号、密码和数据库名。

### 6. 启动项目

进入 `manage.py` 所在目录：

```bash
cd djangoProject
python manage.py runserver
```

访问地址：

- 前台首页：`http://127.0.0.1:8000/`
- 后台首页：`http://127.0.0.1:8000/admin`

如果没有后台管理员账号，可以执行：

```bash
python manage.py createsuperuser
```

## 项目截图

#### 登录

![登录](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/登录.jpg)

#### 注册

![注册](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/注册.jpg)

#### 首页

![首页](https://github.com/TreasureLZ/Django_Collection/blob/main/Herbs_Analysis/images/首页.jpg)

#### 药材 Top20

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

## 二次开发建议

- 将药材数据替换为农产品、商品价格、药品行情等数据
- 增加按地区、分类、时间区间筛选
- 增加价格趋势预测、涨跌幅统计或异常价格提醒
- 增加数据导出和图表下载
- 增加更多行业资讯或数据来源说明

## LTS 维护说明

本项目已经进入 LTS 维护阶段，详细说明见 [docs/LTS.md](docs/LTS.md)。

常见运行问题见 [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)。

## 交流

- 总入口：[Django_Collection](https://github.com/TreasureLZ/Django_Collection)
- GitHub 主页：[TreasureLZ](https://github.com/TreasureLZ)

如果项目对你有帮助，欢迎 star 支持。提交 issue 时请尽量附上系统环境、Python 版本、报错截图和复现步骤。
