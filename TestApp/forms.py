# coding:utf-8
from django import forms
from  DUEditor.widgets import UEditorWidget
from  DUEditor.forms import UEditorField, UEditorModelForm
from .models import Blog


class TestUEditorForm(forms.Form):
    Name = forms.CharField(label=u'姓名')
    ImagePath = forms.CharField()
    Description = UEditorField(u"描述", initial="abc", width=1000, height=300)
    Content = forms.CharField(label=u"内容",
                              widget=UEditorWidget({"width":600, "height":100, "imagePath":'aa', "filePath":'bb', "toolbars":"full"}))


class UEditorTestModelForm(UEditorModelForm):
    class Meta:
        model = Blog
        fields=["Name","Description","ImagePath","Content"]
