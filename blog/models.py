from django.db.models import *
from user.models import User

class AtcType(Model):
# 博文分类
    name = CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

class Atc(Model):
    title = CharField(max_length=30)
    content = TextField()
    author = ForeignKey(User,on_delete = DO_NOTHING)
    create_time = DateTimeField(auto_now_add=True)
    update_time = DateTimeField(auto_now=True)
    type = ForeignKey(AtcType,on_delete = DO_NOTHING)
    
    def __str__(self):
        return '文章-' + self.title
    
    class Meta:
        ordering=['-create_time']
        # 排序
        verbose_name = '文章'
        # 单数
        verbose_name_plural = '文章'
        # 复数