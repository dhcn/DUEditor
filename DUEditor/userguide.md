# DUEditor使用文档

说在前面:本项目改造自DjangoUeditor，本文档亦然

Ueditor HTML编辑器是百度开源的HTML编辑器，

本模块帮助在Django应用中集成百度Ueditor HTML编辑器。
安装包中已经集成Ueditor v1.4.33

使用DUEditor非常简单，方法如下：

## 1、安装方法

    因为配置个性化问题，本项目暂不支持pip install，如想使用，下载以后，把DUEditor扔到django项目目录即可

## 2、在INSTALL_APPS里面增加DjangoUeditor app，如下：
     
		INSTALLED_APPS = (
			#........
    		'DUEditor',
		)


## 3、在urls.py中增加：

	url(r'^ueditor/',include('DUEditor.urls' )),

## 4、在models中这样定义：
	
	from DUEditor.models import UEditorField
	class Blog(models.Model):
    	Name=models.CharField(,max_length=100,blank=True)
    	Content=UEditorField('内容	',height=100,width=500,default='test',toolbars='mini',options={"elementPathEnabled":True},blank=True)

	说明：
	UEditorField继承自models.TextField,因此你可以直接将model里面定义的models.TextField直接改成UEditorField即可。
	UEditorField提供了额外的参数：
        toolbars:配置你想显示的工具栏，取值为mini,normal,full,besttome, 代表小，一般，全部,涂伟忠贡献的一种样式。如果默认的工具栏不符合您的要求，您可以在settings里面配置自己的显示按钮。参见后面介绍。
        options：其他UEditor参数，字典类型。参见Ueditor的文档ueditor_config.js里面的说明。
        css:编辑器textarea的CSS样式
        width，height:编辑器的宽度和高度，以像素为单位。

## 5、在表单中使用非常简单，与常规的form字段没什么差别，如下：
	
	class TestUeditorModelForm(forms.ModelForm):
    	class Meta:
        	model=Blog
	***********************************
	如果不是用ModelForm，可以有两种方法使用：

	1: 使用forms.UEditorField

	from  DUEditor.forms import UEditorField
	class TestUEditorForm(forms.Form):
	    Description=UEditorField("描述",initial="abc",width=600,height=800)
	
	2: widgets.UEditorWidget

	from  UEditor.widgets import UEditorWidget
	class TestUEditorForm(forms.Form):
		Content=forms.CharField(label="内容",widget=UEditorWidget(width=800,height=500,toolbars={}))
	
	widgets.UEditorWidget和forms.UEditorField的输入参数与上述models.UEditorField一样。

## 6、Settings配置
     
      在Django的Settings可以配置以下参数：
            UEDITOR_SETTINGS={
                "toolbars":{           #定义多个工具栏显示的按钮，允行定义多个
                    "name1":[[ 'source', '|','bold', 'italic', 'underline']],
                    "name2",[]
                },
                "images_upload":{
                    "allow_type":"jpg,png",    #定义允许的上传的图片类型
                    "max_size":"2222kb"        #定义允许上传的图片大小，0代表不限制
                },
                "files_upload":{
                     "allow_type":"zip,rar",   #定义允许的上传的文件类型
                     "max_size":"2222kb"       #定义允许上传的文件大小，0代表不限制
                 },,
                "image_manager":{
                     "location":""         #图片管理器的位置,如果没有指定，默认跟图片路径上传一样
                },
            }
## 7、在模板里面：

    <head>
        ......
        {{ form.media }}        #这一句会将所需要的CSS和JS加进来。
        ......
    </head>
    注：运行collectstatic命令，将所依赖的css,js之类的文件复制到{{STATIC_ROOT}}文件夹里面。

## 8、inclusion tag的使用

```
   {%load ueditor_tags %}
   <script id="container" name="container"  style="display: inline-block;" type="text/plain">
     初始化内容
   </script>
   {%ueditor "container"%}
```
## 9、其他事项：

- 本程序安装包里面已经包括了Ueditor，不需要再额外安装。
- 目前暂时不支持ueditor的插件
- 别忘记了运行collectstatic命令，该命令可以将ueditor的所有文件复制到{{STATIC_ROOT}}文件夹里面
- Django默认开启了CSRF中间件，因此如果你的表单没有加入{% csrf_token %}，那么当您上传文件和图片时会失败
- 不过编辑器里面的图片上传View做了CSRF取消设置 
