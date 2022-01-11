from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from home.models import Groups
# Create your views here.


@login_required
def home(request):
    # Groups.objects.all().delete()
    invitedGroups = Groups.objects.filter(
        personList__contains=request.user)
    return render(request, 'home.html', {"invitedGroups": invitedGroups})


@ login_required
def newGroup(request):
    if request.method == 'POST':
        for group in Groups.objects.all():
            if group.name == request.POST['name']:
                return render(request, 'newGroup.html', {"error": "Group name already exists"})
        newWordList = []
        for person in request.POST['personListInput'].split():
            newWordList.append({"personName": person, "wordList": ''})
        newWordList
        Groups.objects.create(
            name=request.POST['name'], personList=request.POST['personListInput'], wordList=newWordList)
        request.session['currentName'] = request.POST['name']
        return redirect('/group')
    return render(request, 'newGroup.html')


@ login_required
def group(request):
    currentName = request.session.get('currentName')
    if currentName:
        currentGroup = Groups.objects.get(name=currentName)
    if request.method == 'POST':
        currentGroup = Groups.objects.get(name=request.POST['name'])
        request.session['currentName'] = request.POST['name']
        if request.POST.get('wordListInput'):
            for nameAndList in currentGroup.wordList:
                if nameAndList.get("personName") == request.user.username:
                    nameAndList.update(wordList=request.POST['wordListInput'])
                    currentGroup.save()
    return render(request, 'group.html', {"currentGroup": currentGroup})
