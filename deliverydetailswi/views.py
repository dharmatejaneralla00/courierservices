from django.shortcuts import render
from .models  import Delupdate
from django.contrib import messages
# Create your views here.
def del_index(request):
    return render(request,'delupdate_index.html')
def delupdate(request):
    delup = Delupdate()
    try:
     if request.method == 'POST':
        delup.recby = request.POST.get('recby')
        delup.conno = request.POST.get('addcon')
        delup.deldate = request.POST.get('date')
        delup.save()
        messages.info(request,"added")
   
    except Exception:
        messages.info(request,"Already added")
    return render(request,'deldetailswi.html')

def delsearch(request):
    delup = Delupdate.objects.all()
    conno = request.POST.get('con')
    return render(request,'podsearch.html',{'srch':delup,'con':conno})