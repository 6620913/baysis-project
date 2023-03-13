from django.shortcuts import render
from .models import Authorization
# Create your views here.


def authorization(request):
    pendingreq = []
    accpreq = []
    obj = Authorization.objects.all()
   
    for f in obj:
        if f.status=="pending":
            pendingreq.append(f)
        
        else:
            # flag[f.name]=True
            accpreq.append(f)


    return render(request,'authorization.html',{"accpreq":accpreq,"pendingreq":pendingreq})

def approve(request,id):
    pendingreq = []
    accpreq = []
    obj = Authorization.objects.all()
    t = Authorization.objects.get(reqID=id)
    t.status = "approved"
   
    for f in obj:
        if f.status=="pending":
            pendingreq.append(f)
        
        else:
            # flag[f.name]=True
            accpreq.append(f)


    return render(request,'authorization.html',{"accpreq":accpreq,"pendingreq":pendingreq})

