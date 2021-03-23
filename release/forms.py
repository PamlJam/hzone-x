from django import forms
from blog.models import AtcType

type_choices = [
    (index,type) for index,type in enumerate(AtcType.objects.all())
]

class ArticleForm(forms.Form):
# 发布文章
    tt = forms.CharField(required=True)
    # 标题 <input>
    ct = forms.CharField(required=True,widget=forms.Textarea)
    # 内容 <TextField>
    tp = forms.ChoiceField(required=True,choices=type_choices,initial=0)
    # 种类 