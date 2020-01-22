from django.contrib import admin

# Register your models here.

"""
python manage.py createsuperuser 创建超级用户 然后就可以通过 admin/请求路径进行登录了
可以在setting.py中通过LANGUAGE_CODE配置页面语种
"""
from .models import Book
# 注册models（可以直接在admin界面修改数据库）
admin.site.register(Book)