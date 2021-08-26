from django.shortcuts import render
from django.http import HttpResponse
from .models import Recievedata
from django.contrib import messages
from delivereddetails.models import RecievedDetails
# Create your views here.
def index(request):
    return  render(request,'index.html')
def addco(request):
    if request.method == 'POST':
        try:
            if request.POST.get('msfno') and request.POST.get('date') and request.POST.get('addcon'):
                recdata = Recievedata()
                recdata.mfno = request.POST.get('msfno')
                recdata.date = request.POST.get('date')
                recdata.conno = request.POST.get('addcon')
                recdata.pcs = request.POST.get('pcs')
                recdata.wt = request.POST.get('wt')
                recdata.save()
                messages.info(request,'Added')  
            else:
                messages.info(request,'Enter Details')
                #return render(request,'addco.html',{'mno':mno})
        except Exception as e :
            messages.info(request,'already added')
    mnos = Recievedata.objects.all()
    return render(request,'addco.html',{'mnos':mnos})
def search(request):
    srch = Recievedata.objects.all()
    deldetails = RecievedDetails.objects.all()
    msfno = request.POST.get('Searchno')
    return  render(request,'search.html',{'srch':srch,'mfno':msfno,'del':deldetails})
def display(request):
    srch = Recievedata.objects.all()
    mfn = request.POST.get('msfnum')
    return render(request,'display.html',{'dsp':srch,'msfno':mfn})

def docudel(request):
    redata = Recievedata()
    obj = Recievedata.objects.last()
    if request.method == 'POST':
        try:
            redata.conno = request.POST.get('addcon')
            redata.mfno = request.POST.get('msfno')
            redata.date = request.POST.get('date')
            redata.pcs = 1
            redata.wt = 0.250
            redata.save()
            messages.info(request,"added",{'obj':obj})
        except Exception :
            messages.info(request,"Consignment Number Already Exists")
    return render(request,'docudel.html',{'obj':obj})