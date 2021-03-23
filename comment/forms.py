from django.forms import *

class CommentForm(Form):
# 继承表单类
    text = CharField(max_length=30,min_length=2,required=True)
    # 限定字数