from django.db.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from user.models import User

class Comment(Model):
# 评论对象
    text = TextField()
    # 内容
    time = DateTimeField(auto_now_add=True)
    # 时间
    user = ForeignKey(User,on_delete = DO_NOTHING)
    # 用户

    content_type = ForeignKey(ContentType,on_delete = DO_NOTHING)

    object_id = PositiveIntegerField()
    
    content_object = GenericForeignKey('content_type','object_id')

    class Meta:
        ordering=['-time']
        # stack
        verbose_name = '评论'
        verbose_name_plural = '评论'