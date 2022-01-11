from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from home.models import Groups
# Create your views here.


@login_required
def settings(request):
    currentName = request.session.get('currentName')
    if currentName:
        return render(request, 'settings.html')
    return redirect('/')


@login_required
def playing(request):
    currentName = request.session.get('currentName')
    if currentName and request.method == 'POST':
        currentGroup = Groups.objects.get(name=currentName)
        print(request.POST['time'])
        return render(request, 'playing.html', {"currentGroup": currentGroup, "time": request.POST['time'], "amountWords": request.POST['amountWords']})
    return redirect('/')
