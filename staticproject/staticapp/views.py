from django.shortcuts import render
from . models import Place
from . models import Pro
# Create your views here.
def demo(request):
    abc=Place.objects.all()
    dee=Pro.objects.all()
    return render(request,"index.html",{'valueabc':abc,'valuedee':dee})