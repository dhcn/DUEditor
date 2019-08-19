#coding:utf-8
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve

import DUSite.settings
from django.contrib import admin
from TestApp.views import  TestUEditorModel,ajaxcmd,TestUEditor

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'DUSite.views.home', name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/', include('admin.site.urls')),
    path('admin/', admin.site.urls),
    url(r'^ueditor/',include('DUEditor.urls')),
    url(r'^test/$',TestUEditorModel),
    url(r'^test2/$',TestUEditor),
    url(r'^ajaxcmd/$',ajaxcmd)

]

if DUSite.settings.DEBUG:
    urlpatterns += [
        url(r'^upload/(?P<path>.*)$', serve, {'document_root': DUSite.settings.MEDIA_ROOT }),
        url(r'^static/(?P<path>.*)$',serve,{'document_root':DUSite.settings.STATIC_ROOT}),
        url(r'^(?P<path>.*)$',serve,{'document_root':DUSite.settings.STATIC_ROOT}),
    ]
