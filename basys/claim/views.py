from django.shortcuts import render
from .models import Claim

# Create your views here.
def claims(request):
    popup=[]
    obj = Claim.objects.all()

    return render(request,'claims.html',{'claims':obj,'pop':popup})

def popup(request,id):

    popup = []
    popup.append(Claim.objects.get(reqID=id))
    obj = Claim.objects.all()

    return render(request,'popup.html',{'claims':obj,'pop':popup})
