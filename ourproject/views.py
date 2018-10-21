from django.http import request,HttpResponse



def index(request):

    return HttpResponse("这是首页")