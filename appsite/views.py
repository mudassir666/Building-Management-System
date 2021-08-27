from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('index')

        return render (request, 'login.html', {})

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html', {})

@login_required(login_url='login')
def levels(request):
    currentUserId = request.user.id
    print("current user id : ",request.user.id)
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    # print("check",all[0].id)

    for i in all:
        # print("-->",i.id)
        # print("-->",i.user.username)
        print("1-->",i.buildings.id)
        currentBuildingId = i.buildings.id

    levelList = []
    if all:
        levelList = Levels.objects.filter(buildings__id=currentBuildingId, IsActive=True)



    # for i in levelList:
    #     print(i.IsActive)
    #     if not i.IsActive:
    #         levelList[i].delete()
    return render(request, 'levels.html', {'levelList':levelList})

@login_required(login_url='login')
def level(request, pk):
    currentUserId = request.user.id
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    for i in all:
        currentBuildingId = i.buildings.id

    levelList = []
    if all:
        levelList = Levels.objects.filter(buildings__id=currentBuildingId, IsActive=True)

    for i in levelList:
        if i.id == int(pk):
            level = Levels.objects.get(id=pk)
            return render(request, 'fortesting.html', {'level':level})

    return render(request, 'notfound.html',{})


@login_required(login_url='login')
def addlevel(request):
    return render(request, 'addlevel.html', {})

@login_required(login_url='addunit.html')
def addunit(request):
    return render(request, 'addunit.html', {})

@login_required(login_url='login')
def units(request):
    currentUserId = request.user.id
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    for i in all:
        currentBuildingId = i.buildings.id

    unitList = []
    if all:
        unitList = Units.objects.filter(buildings__id=currentBuildingId, IsActive=True)


    return render(request, 'units.html', {'unitList':unitList})

@login_required(login_url='login')
def members(request):
    all = Levels.objects.filter(buildings__id=1)
    # all = Levels.objects.filter(buildings__id=1)

    for i in all:
        print("-->",i.LevelName)
        print("-->",i.buildings.BuildingName)
    # print(all)
    return render(request, 'members.html', {})

@login_required(login_url='login')
def unit(request, pk):
    currentUserId = request.user.id
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    for i in all:
        currentBuildingId = i.buildings.id

    unitList = []
    if all:
        unitList = Units.objects.filter(buildings__id=currentBuildingId, IsActive=True)

    for i in unitList:
        if i.id == int(pk):
            unit = Units.objects.get(id=pk)
            return render(request, 'fortesting.html', {'unit':unit})

    return render(request, 'notfound.html',{})


# @login_required(login_url='login')
# def units(request):
#     currentUserId = request.user.id
#     all = BuildingUsers.objects.filter(user__id=currentUserId)
#     for i in all:
#         currentBuildingId = i.buildings.id

#     levelList = []
#      if all:
#         levelList = Levels.objects.filter(buildings__id=currentBuildingId, IsActive=True)


#     return render(request, 'units.html', {})
