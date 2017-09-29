#coding:utf-8
from importlib import import_module

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import DUEditor.settings as USettings
import os
import json
from django.views.decorators.csrf import csrf_exempt
import datetime,random
import urllib.parse
from django.core.files.storage import default_storage
from django.conf import settings
import urllib.request

from DUEditor.utils import get_filename


def get_path_format_vars():
    return {
        "year":datetime.datetime.now().strftime("%Y"),
        "month":datetime.datetime.now().strftime("%m"),
        "day":datetime.datetime.now().strftime("%d"),
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        "time":datetime.datetime.now().strftime("%H%M%S"),
        "datetime":datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "rnd":random.randrange(100,999)
    }

#保存上传的文件
def save_upload_file(PostFile,FilePath):
    fileurl = default_storage.save(FilePath,PostFile)
    return fileurl

@csrf_exempt
def get_ueditor_settings(request):
    return HttpResponse(json.dumps(USettings.UEditorUploadSettings,ensure_ascii=False), content_type="application/javascript")

@csrf_exempt
@login_required
def get_ueditor_controller(request):
    """获取ueditor的后端URL地址    """

    action=request.GET.get("action","")
    reponseAction={
        "config":get_ueditor_settings,
        "uploadimage":UploadFile,
        "uploadscrawl":UploadFile,
        "uploadvideo":UploadFile,
        "uploadfile":UploadFile,
        "catchimage":catcher_remote_image,
        "listimage":list_files,
        "listfile":list_files
    }
    return reponseAction[action](request)


@csrf_exempt
def list_files(request):
    """列出文件"""
    if request.method!="GET":
        return  HttpResponse(json.dumps(u"{'state:'ERROR'}") ,content_type="application/javascript")
    #取得动作
    action=request.GET.get("action","listimage")

    allowFiles={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerAllowFiles",[]),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerAllowFiles",[])
    }
    listSize={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerListSize",""),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerListSize","")
    }

    listpath={
        "listfile":USettings.UEditorUploadSettings.get("fileManagerListPath",""),
        "listimage":USettings.UEditorUploadSettings.get("imageManagerListPath","")
    }

    #取得参数
    list_size= int(listSize[action]) #int(request.GET.get("size",listSize[action]))
    list_start=int(request.GET.get("start",0))

    files=[]
    cur_path= listpath[action]
    files=get_files(cur_path,allowFiles[action])

    if (len(files)==0):
        return_info={
            "state":u"未找到匹配文件！",
            "list":[],
            "start":list_start,
            "total":0
        }
    else:
        return_info={
            "state":"SUCCESS",
            "list":files[list_start:list_start+list_size],
            "start":list_start,
            "total":len(files)
        }

    return HttpResponse(json.dumps(return_info),content_type="application/javascript")


def get_files(cur_path, allow_types=[]):


    items = default_storage.listdir(cur_path)


    files =[]
    for item in items[0]:
        item = str(item)
        internal_path = os.path.join(cur_path,item)

        files.extend(get_files(internal_path, allow_types))
    for item in items[1]:
        item = str(item)
        item_fullname = os.path.join(USettings.gSettings.MEDIA_ROOT, cur_path, item)

        ext = os.path.splitext(item_fullname)[1]
        is_allow_list= (len(allow_types)==0) or (ext in allow_types)
        if is_allow_list:
            files.append({
                "url":urllib.parse.urljoin(USettings.gSettings.MEDIA_URL ,os.path.join(cur_path,item).replace("\\","/" )),
                "mtime":os.path.getmtime(item_fullname)
            })

    return files


@csrf_exempt
@login_required
def UploadFile(request):
    """上传文件"""
    if not request.method=="POST":
        return  HttpResponse(json.dumps(u"{'state:'ERROR'}"),content_type="application/javascript")

    state=u"SUCCESS"
    action=request.GET.get("action")
    #上传文件
    upload_field_name={
        "uploadfile":"fileFieldName","uploadimage":"imageFieldName",
        "uploadscrawl":"scrawlFieldName","catchimage":"catcherFieldName",
        "uploadvideo":"videoFieldName",
    }
    UploadFieldName=request.GET.get(upload_field_name[action],USettings.UEditorUploadSettings.get(action,"upfile"))

    #上传涂鸦，涂鸦是采用base64编码上传的，需要单独处理
    if action=="uploadscrawl":
        upload_file_name="scrawl.png"
        upload_file_size=0
    else:
        #取得上传的文件
        file=request.FILES.get(UploadFieldName,None)
        if file is None:return  HttpResponse(json.dumps(u"{'state:'ERROR'}") ,content_type="application/javascript")
        upload_file_name=file.name
        upload_file_size=file.size

    #取得上传的文件的原始名称
    upload_original_name,upload_original_ext=os.path.splitext(upload_file_name)

    #文件类型检验
    upload_allow_type={
        "uploadfile":"fileAllowFiles",
        "uploadimage":"imageAllowFiles",
        "uploadvideo":"videoAllowFiles"
    }
    if action in upload_allow_type:
        allow_type= list(request.GET.get(upload_allow_type[action],USettings.UEditorUploadSettings.get(upload_allow_type[action],"")))
        if not upload_original_ext.lower()  in allow_type:
            state=u"服务器不允许上传%s类型的文件。" % upload_original_ext

    #大小检验
    upload_max_size={
        "uploadfile":"filwMaxSize",
        "uploadimage":"imageMaxSize",
        "uploadscrawl":"scrawlMaxSize",
        "uploadvideo":"videoMaxSize"
    }
    max_size=int(request.GET.get(upload_max_size[action],USettings.UEditorUploadSettings.get(upload_max_size[action],0)))
    if  max_size!=0:
        from .utils import FileSize
        MF=FileSize(max_size)
        if upload_file_size>MF.size:
            state=u"上传文件大小不允许超过%s。" % MF.FriendValue

    #检测保存路径是否存在,如果不存在则需要创建

    upload_path_format={
        "uploadfile":"filePathFormat",
        "uploadimage":"imagePathFormat",
        "uploadscrawl":"scrawlPathFormat",
        "uploadvideo":"videoPathFormat"
    }
    path_format_var=get_path_format_vars()
    path_format_var.update({
        "basename":upload_original_name,
        "extname":upload_original_ext[1:],
        "filename":get_filename(request.user),
    })
    #取得输出文件的路径
    path_format=USettings.UEditorUploadSettings[upload_path_format[action]]
    OutputPath = path_format.format(**path_format_var)

    #所有检测完成后写入文件
    fileurl=""
    if state=="SUCCESS":
        if action=="uploadscrawl":
            filepath=save_scrawl_file(request, OutputPath)
        else:
            filepath = save_upload_file(file, OutputPath)
        fileurl = default_storage.url(filepath)

    #返回数据
    return_info = {
        'url': fileurl,#urllib.basejoin(USettings.gSettings.MEDIA_URL , OutputPathFormat) ,                # 保存后的文件名称
        'original': upload_file_name,                  #原始文件名
        'type': upload_original_ext,
        'state': state,                         #上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
        'size': upload_file_size
    }
    return HttpResponse(json.dumps(return_info,ensure_ascii=False),content_type="application/javascript")

@csrf_exempt
def catcher_remote_image(request):
    """远程抓图，当catchRemoteImageEnable:true时，
        如果前端插入图片地址与当前web不在同一个域，则由本函数从远程下载图片到本地
    """
    if not request.method=="POST":
        return  HttpResponse(json.dumps( u"{'state:'ERROR'}"),content_type="application/javascript")

    state="SUCCESS"

    allow_type= list(request.GET.get("catcherAllowFiles",USettings.UEditorUploadSettings.get("catcherAllowFiles","")))
    max_size=int(request.GET.get("catcherMaxSize",USettings.UEditorUploadSettings.get("catcherMaxSize",0)))

    remote_urls=request.POST.getlist("source[]",[])
    catcher_infos=[]
    path_format_var=get_path_format_vars()

    for remote_url in remote_urls:
        #取得上传的文件的原始名称
        remote_file_name=os.path.basename(remote_url)
        remote_original_name,remote_original_ext=os.path.splitext(remote_file_name)

        #文件类型检验
        if remote_original_ext  in allow_type:
            path_format_var.update({
                "basename":remote_original_name,
                "extname":remote_original_ext[1:],
                "filename":get_filename(request.user),
            })
            Outputilename = get_filename(request.user);
            suffix = remote_original_ext[1:]

            tempPath = 'temp/{filename}.{extname}'.format(**path_format_var)
            #计算临时本地保存的文件名,临时本地保存主要是为阿里云OSS此类的的Storage准备的
            o_filename=os.path.join(settings.MEDIA_ROOT,tempPath).replace("\\","/")
            #读取远程图片文件

            try:
                remote_image=urllib.request.urlopen(remote_url)
            except Exception as E:
                state = u"抓取图片错误：%s" % E.message
             #将抓取到的文件写入文件
            with open(o_filename, 'wb') as f:
                f.write(remote_image.read())
                f.close()
            filesize = os.path.getsize(o_filename)
            print(filesize)
            if max_size != 0:
                from .utils import FileSize
                MF = FileSize(max_size)
                if filesize > MF.size:
                    state = u"上传文件大小不允许超过%s。" % MF.FriendValue
                    os.remove(o_filename)
            fileurl=""
            if state == "SUCCESS":
                # 取得输出文件的路径
                path_format = USettings.UEditorUploadSettings["catcherPathFormat"]
                OutputPath = path_format.format(**path_format_var)

                with open(o_filename, 'rb') as f:
                    filepath = save_upload_file(f, OutputPath)

                fileurl = default_storage.url(filepath)

            os.remove(o_filename)
            catcher_infos.append({
                "state":state,
                "url":fileurl,
                "size":filesize,
                "title":remote_original_name,
                "original":remote_file_name,
                "source":remote_url
            })

    return_info={
        "state":"SUCCESS" if len(catcher_infos) >0 else "ERROR",
        "list":catcher_infos
    }

    return HttpResponse(json.dumps(return_info,ensure_ascii=False),content_type="application/javascript")


#涂鸦功能上传处理
@csrf_exempt
def save_scrawl_file(request,filename):
    import base64

    content = request.POST.get(USettings.UEditorUploadSettings.get("scrawlFieldName", "upfile"))
    fileurl = default_storage.save(filename, base64.decodestring(content))
    return fileurl



