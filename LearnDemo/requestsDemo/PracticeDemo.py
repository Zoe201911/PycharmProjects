
import  requests
def addInfo(request):
    if request.method == "POST":
        username = request.user  # 获取当前用户名
        print(username)
        name = request.POST.get('name', '')
        if not name:
            return HttpResponse(json.dumps({'status': 4, "msg": "name参数不能为空"}, ensure_ascii=False), content_type="application/json,charset=utf-8")
        sex = request.POST.get('sex', '')
        if not sex:
            return HttpResponse(json.dumps({'status': 4, "msg": "sex参数不能为空"}, ensure_ascii=False), content_type="application/json,charset=utf-8")
        info = UserInfo.objects.filter(name=name).first()   # 查询用户的当前记录
        info_name = UserInfo.objects.filter(username=username).first()

        if info is not None:        # name昵称存在
            if str(info.username) == str(username):   # 判断是当前用户昵称
                info.name=name
                info.sex=sex
                info.age=request.POST.get('age', 0)
                info.fancy=request.POST.get('fancy', '')
                info.mail=request.POST.get('mail', '')
                info.save()
                return HttpResponse(json.dumps({'status': 0, "msg": "updata success!"}, ensure_ascii=False), content_type="application/json,charset=utf-8")
            else:
                return HttpResponse(json.dumps({'status': 5, "msg": "该昵称已被其他人使用！请换个试试"}, ensure_ascii=False), content_type="application/json,charset=utf-8")
        else:  # name昵称不存在
            if info_name is not None:  # 判断当前用户有没有昵称
                info_name.name=name
                info_name.sex=sex
                info_name.age=request.POST.get('age', 0)
                info_name.fancy=request.POST.get('fancy', '')
                info_name.mail=request.POST.get('mail', '')
                info_name.save()
                return HttpResponse(json.dumps({'status': 0, "msg": "updata success!"}, ensure_ascii=False), content_type="application/json,charset=utf-8")
            else:
                info=UserInfo.objects.create(
                    username=str(username),
                    name=name,
                    sex=sex,
                    age=request.POST.get('age', 0),
                    fancy=request.POST.get('fancy', ''),
                    mail=request.POST.get('mail', '')
                    )
                info.save()
                return HttpResponse(json.dumps({'status': 0, "msg": "updata success!"}, ensure_ascii=False), content_type="application/json,charset=utf-8")

    else:
        return HttpResponse(json.dumps({'status': 3, "msg": "request method not post!"}, ensure_ascii=False), content_type="application/json,charset=utf-8")