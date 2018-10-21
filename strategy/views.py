from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from . import models
import json
from users import models
from django.db import connection


# Create your views here.

# 根据id查询攻略
# def searchbyuserid(request,userid):
#     try:
#         mystrategys = models.strategy.objects.filter(userid = userid).values("title","time","scover__url","state","good","view","sccontent__contents","condition__condition")
#         mystrategys = list(mystrategys)
#         print(mystrategys)
#         for item in mystrategys:
#             item["time"] = item["time"].strftime("%Y-%m-%d")
#         mystrategys = json.dumps(mystrategys)
#
#         return HttpResponse(mystrategys)
#     except Exception as ex:
#         print(ex)
#         return JsonResponse({"code":"500"})


def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter().values()
        return HttpResponse(data)
    if request.method == 'POST':
        print(request.body)
        data = request.POST.get("content")
        print(data)
        data = {
            "content":str(data)
        }
        # data = json.loads(data)


        # data = {
        #     "content":''
        # }

        aa = models.test.objects.create(**data)

        return HttpResponse(aa)
    else:
        return HttpResponse("失败")


    # 插入详情
    # Create your views here.
def show(request):
    # 帖子id
    pass
    # try:
    #     pid = request.GET.get('postid')
    #     print(pid)
    #     contents = models.content.objects.filter(postid=1).values()
    #     contents = list(contents)
    #     for item in contents:
    #         item["time"] = item["time"].strftime("%Y-%m-%d")
    #     contents = json.dumps(contents)
    #     return HttpResponse(contents)
    # except Exception as ex:
    #     print(ex)
    #     return JsonResponse({"code":"500"})

def edit(request):
    pass
    # if request.method=="POST":
    #     try:
    #         dcontent=request.POST.get("content")
    #         djcontent = {
    #             "html":dcontent
    #         }
    #         print(111)
    #         jdata = json.dumps(djcontent)
    #         f = open('file1.json','w')
    #         f.write(jdata)
    #         f.close()
    #         return JsonResponse({"code": 200})
    #     except Exception as ex:
    #         return JsonResponse({"code": 404})
    # elif request.method == "GET":
    #     return JsonResponse({"code": 100})

def insertdetail(request):
    if request.method == "GET":
        data = models.test.objects.filter(id="2").values('content')
        # data = str(data)
        # data = list(data)
        # temdata = data[0]['content']
        # print(type(temdata))
        return HttpResponse(json.dumps(list(data), ensure_ascii=False))
        # return JsonResponse({"content":temdata},json_dumps_params={'ensure_ascii':False})
    if request.method == 'POST':

        data = json.loads(request.body, strict=False)
        # data =request.body
        aa = models.test.objects.create(**data)
        # print(type(data.decode('utf-8')))
        # content1 = {
        #     "content" : data
        # }
        # print(json.dumps(data.decode()))
        print(aa)
        return HttpResponse('')
    else:
        return HttpResponse("失败")

# 卡片展示所有攻略
def showall(request):
    try:
    #
        allstrategy = models.strategy.objects.filter().values('scover__url','condition__strategy__title','condition__strategy__good','condition__strategy__view','condition__strategy__userid','condition__strategy__userid')
        listallstrategy = list(allstrategy)

        listallstrategy = json.dumps(listallstrategy)

        print(listallstrategy)
        return HttpResponse(listallstrategy)
    except Exception as ex:
        print(ex)
        return JsonResponse({"code":"505"})

# 根据条件搜索 卡片展示所有攻略
def searchbysome(request,stype,scondition):
    if request.method=="GET":
        # 转化stype
        stype = int(stype)

        result=getType(stype,scondition)
        try:
            return JsonResponse(json.dumps(list(result),ensure_ascii=False),safe=False)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "500"})
    elif request.method=="POST":
        return JsonResponse({"code": "505"})

# 获取搜索条件类型
def getType(stype,scondition):
    if stype==1:
        res='title'
        posts = models.strategy.objects.filter(title__contains=scondition).values(res)
    elif stype==2:
        res='state'
        posts = models.strategy.objects.filter(state__contains=scondition).values(res)
    else:
        res='userid'
        posts = models.strategy.objects.filter(userid__username=scondition).values(res)

    return posts

# 用户查询自己的攻略(卡片)
def searchbyuserid(request):
    if request.method=="GET":
        try:
            uid = request.GET.get('userid')
            strategy = models.strategy.objects.filter(userid=uid).values('scover__url','condition__strategy__title','condition__strategy__good','condition__strategy__view','condition__strategy__userid','condition__strategy__userid')
            strategy = list(strategy)
            strategy = json.dumps(strategy)
            return HttpResponse(strategy)
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"500"})
    elif request.method=="POST":
        return JsonResponse({"code": "505"})

# 攻略详情展示
def showdetail(request,postid):
    if request.method=="POST":
        try:
            contenttop = models.sccontent.objects.filter(sid=postid).values('contents')
            commitbtm = models.scommit.objects.filter(sid=postid).values("commit","userid__username",'time')

            # 时间转换
            for item in commitbtm:
                item["time"] = item["time"].strftime("%Y-%m-%d")
            return JsonResponse({"contenttop":list(contenttop),"commitbtm":list(commitbtm)},json_dumps_params={"ensure_ascii":False})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code":"500"})
    elif request.method=="GET":
        return JsonResponse({"code":"505"})

# 新建攻略
def add(request):
    try:
        data1 =json.loads(request.body)
        # strategy
        data_strategy = {
            "state": data1["state"],
            "title": data1["title"],
            "time": data1["time"],
            "good":data1["good"],
            "view":data1["view"],
            "userid_id": data1["userid_id"],
            "condition_id": data1["condition"],
        }
        sstrategy = models.strategy.objects.create(**data_strategy)

        # contents
        data_contents = {
            "contents": data1["contents"],
            "sid_id":sstrategy.id
        }
        scontent = models.sccontent.objects.create(**data_contents)

        # cover
        data_cover = {
            "url":data1["url"],
            "sid_id": sstrategy.id
        }
        scover = models.scover.objects.create(**data_cover)
        return JsonResponse({"code": "200"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})

# 根据postid更新攻略信息
def update(request,postid):
    try:
        if request.method =="POST":
            newdate = json.loads(request.body)

            # newdata = {
            #     "title":"newdate",
            #     "state":"hhhh",
            #     "condition_id":2,
            # #     封面
            #     "cover":"oooo",
            # #     图片
            #     "img":{
            #         "img1":"11111",
            #         "img2":"22222"
            #     }
            # }

            affect_rows = models.strategy.objects.filter(id=postid).update(title=newdate["title"],state=newdate["state"],condition_id=newdate["condition_id"])
            affect_rowsurl = models.scover.objects.filter(id=postid).update(url=newdate["cover"])
            affect_rowsimg = models.simages.objects.filter(id=postid).update(url=newdate["img"]["img1"])
        return JsonResponse({"code": "200"})
    except Exception as ex:
        print(ex)
    return JsonResponse({"code": "500"})

# 删除攻略
def delete(request):
    try:
        sid = request.GET.get('sid_id')
        pcontent = models.sccontent.objects.filter(sid_id = sid).delete()
        pcommit = models.scommit.objects.filter(sid_id = sid).delete()
        pcover = models.scover.objects.filter(sid_id = sid).delete()
        pimage = models.simages.objects.filter(sid_id = sid).delete()
        pstrate = models.strategy.objects.filter(id = sid).delete()
        return JsonResponse({"code": "200"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"code": "500"})


