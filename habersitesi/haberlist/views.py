from django.shortcuts import render,get_object_or_404
from .models import Haberler

# Create your views here.
def index(request):
    haberler = Haberler.objects.all()
    return render(request, 'index.html',{"haberler":haberler})

def detay(request,id):
    habergetir=get_object_or_404(Haberler,pk=id)
    return render(request,"detay.html",{"haber":habergetir})




