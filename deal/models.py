from django.db.models import *
from user.models import User

class Item(Model):
    name = CharField(max_length=20)
    info = TextField(max_length=50)
    time = DateTimeField(auto_now_add=True)
    sold = BooleanField(default=False)
    # 状态（售出）
    chop = BooleanField(default=False)
    # 状态（可刀）
    count = IntegerField(default=1)
    # 数目
    owner = ForeignKey(User,on_delete = DO_NOTHING)
    price = FloatField(default=0)
    # 价格
    image = ImageField(default="./static/image/items/default.png",upload_to='./static/image/items/upload/')
    def __str__(self):
        return '物品-' + self.name
    class Meta:
        ordering=['-time']
        verbose_name = '物品'
        verbose_name_plural = '物品'