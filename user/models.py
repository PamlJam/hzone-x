from django.db.models import * 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):	
# 重写用户模型
    motto = TextField(max_length=24,default='nothing at all')
    # 签名
    icon = ImageField(default="./static/image/icon/default/male.png",upload_to='./static/image/icon/upload/')
    # 头像
    class Meta:
        ordering = ['-id']
        # 倒序排列
        verbose_name = '用户'
        # 详细名称
        verbose_name_plural = '用户'
        # 复数形式
    def __str__(self):
        return self.username