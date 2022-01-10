from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from home.models import Groups
# Create your views here.


@login_required
def home(request):
    return render(request, 'home.html')


@ login_required
def newGroup(request):
    if request.method == 'POST':
        for group in Groups.objects.all():
            if group.name == request.POST['name']:
                return render(request, 'newGroup.html', {"error": "Group name already exists"})
        Groups.objects.create(
            name=request.POST['name'], personList=request.POST['personListInput'].split())
        return render(request, 'group.html')
    return render(request, 'newGroup.html')


@ login_required
def group(request):
    return render(request, 'group.html')
