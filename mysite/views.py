from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from mysite.models import User, Message, Status

# Create your views here.
#render()方法是render_to_response的一个崭新的快捷方式，前者会自动使用RequestContext。
# 而后者必须coding出来，这是最明显的区别，当然前者更简洁。
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        k = User.objects.create(username=username,password=password,email=email)
        k.save()
        return HttpResponse('regist success!!!')
    else:
        return render(request, 'regist.html')
    return render(request, 'regist.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username__exact=username,password__exact=password)
        if user:
            request.session['username'] = username
            return render(request,"index.html",{'user_is_login':True,"username":username})
        else:
            return HttpResponse('用户密码错误，请再次登录')
    else:
        return render(request,"login.html")
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def logout(request):
    del request.session['username']
    return render(request,'index.html')

def info(request):
    return render(request, "info.html")

def data(request):
    status_msg = Status.objects.aggregate(Sum('num'))
    print(status_msg)
    return render(request, "data.html", {'num': status_msg['num__sum']})

@csrf_exempt
def messagerev(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        textarea = request.POST['textarea']
        people = request.session['username']
        msg = Message.objects.create(title=title, textarea=textarea, people=people)
        msg.save()
        return redirect('/message')
    else:
        return HttpResponse('error 发表失败！！！')
    return redirect('/message')

@csrf_exempt
def message(request):
    message_list = Message.objects.all().order_by('-pk')
    return render(request,'message.html',{'message_list':message_list})

@csrf_exempt
def messagedel(request,pk):
    messageInfo = Message.objects.get(pk=pk)
    delete = messageInfo.delete()
    print(type(delete), delete)
    return redirect('/message')

@csrf_exempt
def statusopen(request):
    if(request.method =='GET'):
        statuscmd = 1
        ctrlopen = Status.objects.create(num=statuscmd)
        ctrlopen.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
        return redirect('/data')

@csrf_exempt
def cmdopen(request):
    if(request.method =='GET'):
        statuscmd = 1
        ctrlclose = Status.objects.create(num=statuscmd)
        ctrlclose.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
    return HttpResponse('close')

@csrf_exempt
def statusnum(request):
    if(request.method == 'GET'):

        status_num = Status.objects.aggregate(Sum('num'))
        print(status_num)
        return HttpResponse(status_num['num__sum'])
    else:
        return HttpResponse('0')