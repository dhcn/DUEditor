# DUEditor

## 本项目使用说明

[DUEditor使用说明](https://github.com/dhcn/DUEditor/blob/master/DUEditor/userguide.md)


## 更新日志：
##### 2021-02-25
- 因为百度公司已经长期停止UEditor的维护更新,加上我本人目前也不从事Web应用研发工作,本项目的维护从即日起停止更新.

##### 2019-12-14
- Update for Django 3.0 new version

##### 2019-8-19
- fix urls.py中不兼容的配置格式

##### 2019-1-6
- bugfix:render() got an unexpected keyword argument 'renderer'
- cause:https://stackoverflow.com/questions/52039654/django-typeerror-render-got-an-unexpected-keyword-argument-renderer

### 0.2Beta版的更新内容(2017-10)：
- 这个分支更名为:DUEditor
- python语言版本升级到3.5+(比3.5低的py3版本可能也支持，但未做测试，不做许诺)
- 支持目前Django版本1.11.* 和最新版本2.*
- 存储基本都使用Django的Storage,便于快速切换不同的文件存储backends
- UEditor版本升级到最新的1.4.33
- 安全加固:取消前端path配置传参机制
- 简化设计:path生成机制简化
- 开发易用的include tag
- 修正无文件类型后缀URL爬取的bug
- 因为配置个性化问题，暂时不准备支持pip install，使用者请直接把DUEditor拉到自己项目目录即可。
- 返回响应的方式改为JsonResponse
- 为get_ueditor_settings接口添加了Jsonp调用方式的处理代码

##### 2017-9-27:这个分支更名为:DUEditor

##### 2017-8-17:发现一个爬取图片存储功能的bug，如果对方图片地址是目录式无后缀地址，将会导致允许类型验证失败，于是乎爬取失败。

##### 2017-2-28:把面向阿里云oss的一个ueditor views版发布出来，其中backends来自于这个项目：https://github.com/xiewenya/django-aliyun-oss2-storage

##### 2017-2-21：修改urls.py配置，删除不再被新版支持的patterns。

## License

DUEditor is available under the terms of the MIT License

## 关于原项目的说明
原项目[DjangoUEditor](https://github.com/zhangfisher/DjangoUeditor) 维护人zhangfishe说已经不再更新项目且欢迎fork修改 ，因此我于2017-2-21日fork此分支，准备开启新的分支,
原项目当时的文档见DjangoUeditor.md
