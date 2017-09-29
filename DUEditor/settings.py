#coding:utf-8
from django.conf import settings as gSettings   #全局设置

#工具栏样式，可以添加任意多的模式
TOOLBARS_SETTINGS={
    "besttome":[['source','undo', 'redo','bold', 'italic', 'underline','forecolor', 'backcolor','superscript','subscript',"justifyleft","justifycenter","justifyright","insertorderedlist","insertunorderedlist","blockquote",'formatmatch',"removeformat",'autotypeset','inserttable',"pasteplain","wordimage","searchreplace","map","preview","fullscreen"], ['insertcode','paragraph',"fontfamily","fontsize",'link', 'unlink','insertimage','insertvideo','attachment','emotion',"date","time"]],
    "mini":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','simpleupload','attachment']],
    "normal":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','removeformat', 'formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','simpleupload', 'emotion','attachment', '|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']]
}

#默认的Ueditor设置，请参见ueditor.config.js
UEditorSettings={
    "toolbars":TOOLBARS_SETTINGS["normal"],
    "autoFloatEnabled":False,
    "defaultPathFormat":"%(basename)s_%(datetime)s_%(rnd)s.%(extname)s"   #默认保存上传文件的命名方式
}
#请参阅php文件夹里面的config.json进行配置
UEditorUploadSettings={
     #/*上传图片配置项 */
    "imageActionName": "uploadimage", #/*执行上传图片的action名称 */
    "imageFieldName": "upfile", #/*提交的图片表单名称 */
    "imageMaxSize": 2048000, #/*上传大小限制，单位B */
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #/*上传图片格式显示 */
    "imageCompressEnable": True, #/*是否压缩图片,默认是true */
    "imageCompressBorder": 1600, #/*图片压缩最长边限制 */
    "imageInsertAlign": None, #/*插入的图片浮动方式 */
    "imageUrlPrefix": "", #/*图片访问路径前缀 */
    "imagePathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */


    #/*涂鸦图片上传配置项 */
    "scrawlActionName": "uploadscrawl", #/*执行上传涂鸦的action名称 */
    "scrawlFieldName": "upfile", #/*提交的图片表单名称 */
    "scrawlPathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */
    "scrawlMaxSize": 2048000, #/*上传大小限制，单位B */
    "scrawlUrlPrefix": "", #/*图片访问路径前缀 */
    "scrawlInsertAlign": None,

    #/*截图工具上传 */
    "snapscreenActionName": "uploadimage", #/*执行上传截图的action名称 */
    "snapscreenPathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */
    "snapscreenUrlPrefix": "", #/*图片访问路径前缀 */
    "snapscreenInsertAlign": None, #/*插入的图片浮动方式 */

    #/*抓取远程图片配置 */
    "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
    "catcherActionName": "catchimage", #/*执行抓取远程图片的action名称 */
    "catcherFieldName": "source", #/*提交的图片列表表单名称 */
    "catcherPathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */
    "catcherUrlPrefix": "", #/*图片访问路径前缀 */
    "catcherMaxSize": 2048000, #/*上传大小限制，单位B */
    "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #/*抓取图片格式显示 */

    #/*上传视频配置 */
    "videoActionName": "uploadvideo", #/*执行上传视频的action名称 */
    "videoFieldName": "upfile", #/*提交的视频表单名称 */
    "videoPathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */
    "videoUrlPrefix": "", #/*视频访问路径前缀 */
    "videoMaxSize": 102400000, #/*上传大小限制，单位B，默认100MB */
    "videoAllowFiles": [
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"], #/*上传视频格式显示 */

    #/*上传文件配置 */
    "fileActionName": "uploadfile", #/*controller里,执行上传视频的action名称 */
    "fileFieldName": "upfile", #/*提交的文件表单名称 */
    "filePathFormat": "upfiles/{filename}.{extname}", #/*上传保存路径,可以自定义保存路径和文件名格式 */
    "fileUrlPrefix": "", #/*文件访问路径前缀 */
    "fileMaxSize": 51200000, #/*上传大小限制，单位B，默认50MB */
    "fileAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
    ], #/*上传文件格式显示 */

    #/*列出指定目录下的图片 */
    "imageManagerActionName": "listimage", #/*执行图片管理的action名称 */
    "imageManagerListPath": "upfiles/", #/*指定要列出图片的目录 */
    "imageManagerListSize": 20, #/*每次列出文件数量 */
    "imageManagerUrlPrefix": "", #/*图片访问路径前缀 */
    "imageManagerInsertAlign": None, #/*插入的图片浮动方式 */
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #/*列出的文件类型 */

    #/*列出指定目录下的文件 */
    "fileManagerActionName": "listfile", #/*执行文件管理的action名称 */
    "fileManagerListPath": "upfiles/", #/*指定要列出文件的目录 */
    "fileManagerUrlPrefix": "", #/*文件访问路径前缀 */
    "fileManagerListSize": 20, #/*每次列出文件数量 */
    "fileManagerAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
    ] #/*列出的文件类型 */
}


#更新配置：从用户配置文件settings.py重新读入配置UEDITOR_SETTINGS,覆盖默认
def UpdateUserSettings():
    UserSettings=getattr(gSettings,"UEDITOR_SETTINGS",{}).copy()
    if "config" in UserSettings:UEditorSettings.update(UserSettings["config"])
    if "upload" in UserSettings:UEditorUploadSettings.update(UserSettings["upload"])

#读取用户Settings文件并覆盖默认配置
UpdateUserSettings()


#取得配置项参数
def GetUeditorSettings(key,default=None):
    if key in UEditorSettings:
        return UEditorSettings[key]
    else:
        return default



