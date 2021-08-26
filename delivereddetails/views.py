from django.shortcuts import render
from recdata.models import Recievedata
from .models import RecievedDetails
from django.contrib import messages
# Create your views here.
def deldetails_index(request):
    return render(request,'delivereddetails_index.html')
def updatedeldetails(request):          
    searchcoono = request.POST.get('updatecon')
    recdata = RecievedDetails()
    recdetails = Recievedata.objects.all()
    con = request.POST.get('con')
    if request.method == 'POST':
        try:
            if 'Update' == request.POST.get('update'):
                recdata.consignmentnumber = con
                recdata.delivereddate = request.POST.get('deldate')
                recdata.recievedby = request.POST.get('recby')
                recdata.save()
                messages.info(request,"Added")
        except Exception:
            messages.info(request,'Already added')
    return render(request,'updatedeldetails.html',{'srch':searchcoono,'recs':recdetails})
def viewdeldetails(request):
    recdetails = RecievedDetails.objects.all()
    con = request.POST.get('conno')
    return render(request,'viewdeldetails.html',{'recs':recdetails,'con':con})