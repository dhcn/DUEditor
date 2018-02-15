#coding:utf-8
'''
Created on 2013-7-4

@author: Hayden
'''
from django import template

register = template.Library()

@register.inclusion_tag('ueditorjs.html', takes_context=True)
def ueditor(context,editor_id):

    return {"editor_id":editor_id}
