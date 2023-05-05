import os
import django

# 設定環境變數 DJANGO_SETTINGS_MODULE 為你的 Django 設定檔
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

# 載入 Django 設定
django.setup()

# 接下來就可以使用 Django 的 ORM 了
from django.contrib.auth.models import User
from blog.models import BlogUser

# 找到要連結的 auth_user
user = User.objects.get(username='yoyolien')

# 建立 BlogUser 並指定 user 為上面找到的 auth_user
bloguser = BlogUser(user=user)

# 儲存 BlogUser
bloguser.save()
