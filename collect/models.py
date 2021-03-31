from django.db.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from user.models import User
from deal.models import Item

class Collection(Model):
# 收藏
    user = ForeignKey(User,on_delete = DO_NOTHING)
    content_type = ForeignKey(ContentType,on_delete = DO_NOTHING)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = '收藏'