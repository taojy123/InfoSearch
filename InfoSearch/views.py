# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from models import *

import os
import uuid



def index(request):
    keys = Keys.objects.all()
    res = Index.objects.all()
    rs = []
    for index in res:
        r = []
        for k in keys:
            kname = k.name
            r.append(index.get_value(kname))
        rs.append((r, index.uid))
    searchs = [("姓名","")]
    num = len(searchs) - 1
    return render_to_response('index.html', locals())


def admin(request):
    keys = Keys.objects.all()
    return render_to_response('admin.html', locals())


def admin_add(request):
    name = request.REQUEST.get('key_name', '')
    if Keys.objects.filter(name=name) or not name:
        return HttpResponse("<script>alert('此字段已经存在,不可重复添加');top.location='/admin/'</script>")
    key = Keys()
    key.name = name
    key.save()
    return HttpResponseRedirect("/admin/")


def admin_del(request):
    id = request.REQUEST.get('key_id', '')
    Keys.objects.filter(id=id).delete()
    return HttpResponseRedirect("/admin/")


def add(request):
    keys = Keys.objects.all()
    return render_to_response('add.html', locals())


def add_action(request):
    keys = Keys.objects.all()
    uid = str(uuid.uuid4())
    for k in keys:
        kid = k.id
        kname = k.name
        value = request.REQUEST.get(str(kid), '')
        info = Info()
        info.uid = uid
        info.key = kname
        info.value = value
        info.save()
    Index(uid=uid).save()
    submit = request.REQUEST.get("submit", '')
    if submit == u"添加记录":
        return HttpResponse("<script>top.location='/add/'</script>")
    else:
        uid = request.REQUEST.get("uid", '')
        return HttpResponse("<script>top.location='/del_data/?uid=" + uid + "'</script>")


def search(request):
    keys = Keys.objects.all()
    indexs = Index.objects.all()

    search_keys = []
    search_values = []
    res = []
    n = 0
    while True:
        key = request.REQUEST.get('key_%d'%n, '')
        value = request.REQUEST.get('value_%d'%n, '')
        if key or value:
            for index in indexs:
                if index.get_value(key) == value:
                    res.append(index)
            search_keys.append(key)
            search_values.append(value)
        else:
            break
        n += 1

    rs = []
    for index in res:
        r = []
        for k in keys:
            kname = k.name
            r.append(index.get_value(kname))
        rs.append((r, index.uid))
    searchs = zip(search_keys, search_values)
    num = len(searchs) - 1

    return render_to_response('index.html', locals())



def del_data(request):
    uid = request.REQUEST.get('uid', '')
    Index.objects.filter(uid=uid).delete()
    return HttpResponseRedirect("/")


def update(request):
    keys = Keys.objects.all()
    uid = request.REQUEST.get('uid', '')
    index = Index.objects.get(uid=uid)
    rs = []
    for k in keys:
        kname = k.name
        rs.append((k, index.get_value(kname)))
    return render_to_response('update.html', locals())



#====================login=============================================

def login(request):
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/admin/")

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("/admin/")

#======================================================================



