from django.db import models

"""
python manage.py makemigrations <appName> 生成数据表，app名可以不写，表示生成所有app下数据表，数据表名默认<appName_className>
python3 manage.py makemigrations --empty <appName> 修改或者删除时，清空migrations下文件，然后执行命令
python manage.py migrate 进行数据迁移
python manage.py sqlmigrate <appName> <文件id> 查看sql语句
"""


# Create your models here.
class Book(models.Model):
    bookId = models.BigIntegerField(default=1, primary_key=True)
    bookName = models.TextField(null=True)
