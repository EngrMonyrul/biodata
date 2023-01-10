from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import People
from .forms import Peopledetails
import os

def home(request):
    if request.method == "POST":
        datas = Peopledetails(request.POST, request.FILES)
        if datas.is_valid():
            datas.save()
    form = Peopledetails()
    data = People.objects.all()
    return render(request, 'members/home.html', {'data':data, 'form':form})

def deletepeople(request, pk):
    cat = People.objects.get(id=pk)
    files = str(cat.image.path)
    if os.path.exists(files):
        os.remove(files)
        cat.delete()
        redirect = reverse('home')
        return HttpResponseRedirect(redirect)