# IELTSCAT
IELTSCAT前后端分离。
## 前端环境
npm 5.6.2 Vue 2.9.6
## 后端环境
Anaconda 4.6.12 MySQL 5.7.21 MongoDB 4.0.0 Redis 3.2.100

## 前端项目构建

```
npm install
```
## 前端项目运行
```
npm run dev
```

## 后端项目构建
### 导入环境
```
conda env create -f environment.yml
```

### 创建并填充文件
文件/CET6Cat/privacy.py中配置了必要但隐私的信息（如API KEY），按照同目录下的模板文件创建该文件。

### 配置数据库
创建MySQL数据库，并将相关信息配置。数据库使用utf8编码，且选择第一种排序方式。
```
CREATE DATABASE IELTSCAT;
```
创建MongoDB数据库并建立相关的Collection，打开mongo命令行并执行：
```
use cet6cat
db.createCollection("fault_words")
db.createCollection("study_num")
db.createCollection("translate")
exit
```

### 运行Task指令
```
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```
创建超级用户时，先将`/users/apps.`的`UsersConfig`改为'Users'

### 填充数据
填充单词数据，直接运行db_tools/目录下的gen_word.py脚本。
注意，不要重复运行，不然数据库表里的单词就越来越多了（我没有做联合unique约束）。
如果重复运行了怎么办？先把words_word表删掉，然后删除表django_migrations中生成words_word表的那项记录，然后在Task中重新migrate就生成了空表，然后再运行上面那个脚本一次。

### 后端项目运行
启动MySQL服务：
```
net start MySQL Server
```
启动MongoDB服务：
```
net start MongoDB Server
```
启动redis-server服务
```
redis-server
```
在终端输入以下命令
```
``python manage.py runserver 0.0.0.0:8000``
```
