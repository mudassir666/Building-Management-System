from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LevelsForm, MembersForm, UnitsForm

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


@login_required(login_url='login')
def units(request):
    currentUserId = request.user.id
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    for i in all:
        currentBuildingId = i.buildings.id

    unitList = []
    if all:
        unitList = Units.objects.filter(buildings__id=currentBuildingId, IsActive=True)

    print(unitList)
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

@login_required(login_url='login')
def addmembers(request):

    form = MembersForm()
    
    if request.method == "POST":
        print("--->>>>",request.POST)
        MemberType = request.POST['MemberType']
        OwnerType=request.POST['OwnerType']
        OccupantType = request.POST['OccupantType']
        MemberName = request.POST['MemberName']
        CellPhone = request.POST['CellPhone']
        Email = request.POST['Email']
        AddressLine1 = request.POST['AddressLine1']
        AddressLine2 = request.POST['AddressLine2']
        City= request.POST['City']
        Province= request.POST['Province']
        PostalCode= request.POST['PostalCode']

        # if IsExpenseApplicable == 'true':
        #     IsExpenseApplicable  = True
        # else:
        #     IsExpenseApplicable = False
            
        currentUserId = request.user.id
        all = BuildingUsers.objects.filter(user__id=currentUserId)
        print(all[0].id)
        currentBuildingId = all[0].id

        buildings = Buildings.objects.get(id=currentBuildingId)

        ins = Members(MemberType=MemberType,
                     OwnerType=OwnerType,
                     OccupantType=OccupantType,
                     MemberName=MemberName,
                     CellPhone=CellPhone,
                     Email=Email,
                     AddressLine1=AddressLine1,
                     AddressLine2=AddressLine2,
                     City=City,
                     Province=Province,
                     PostalCode=PostalCode,
                     buildings=buildings)
        print(ins)
        ins.save()
       
        return redirect('/members')
    context = {'form':form}
    return render(request, 'addmembers.html', context)

@login_required(login_url='addunit.html')
def addunit(request):

    form = UnitsForm()
    
    if request.method == "POST":
        print("--->>>>",request.POST)
        # MemberType = request.POST['MemberType']
        # OwnerType=request.POST['OwnerType']
        # OccupantType = request.POST['OccupantType']
        # MemberName = request.POST['MemberName']
        # CellPhone = request.POST['CellPhone']
        # Email = request.POST['Email']
        # AddressLine1 = request.POST['AddressLine1']
        # AddressLine2 = request.POST['AddressLine2']
        # City= request.POST['City']
        # Province= request.POST['Province']
        # PostalCode= request.POST['PostalCode']

        UnitName = request.POST['UnitName']
        OccupiedStatus = request.POST['OccupiedStatus']
        UnitType = request.POST['UnitType']
        CoveredArea = request.POST['CoveredArea']
        IsDisputed = request.POST['IsDisputed']
        DisputeDesc = request.POST['DisputeDesc']
        IsMaintenanceApplicable = request.POST['IsMaintenanceApplicable']
        CurrentMaintenancePM = request.POST['CurrentMaintenancePM']
        IsBLExpenseApplicable = request.POST['IsBLExpenseApplicable']
        IsDLExpenseApplicable = request.POST['IsDLExpenseApplicable']
        IsULExpenseApplicable = request.POST['IsULExpenseApplicable']

        # if IsExpenseApplicable == 'true':
        #     IsExpenseApplicable  = True
        # else:
        #     IsExpenseApplicable = False
            
        currentUserId = request.user.id
        all = BuildingUsers.objects.filter(user__id=currentUserId)
        print(all[0].id)
        currentBuildingId = all[0].id

        buildings = Buildings.objects.get(id=currentBuildingId)

        # ins = Members(MemberType=MemberType,
        #              OwnerType=OwnerType,
        #              OccupantType=OccupantType,
        #              MemberName=MemberName,
        #              CellPhone=CellPhone,
        #              Email=Email,
        #              AddressLine1=AddressLine1,
        #              AddressLine2=AddressLine2,
        #              City=City,
        #              Province=Province,
        #              PostalCode=PostalCode,
        #              buildings=buildings)
        ins = Units(
                    UnitName=UnitName,
                    OccupiedStatus=OccupiedStatus,
                    UnitType=UnitType,
                    CoveredArea=CoveredArea,
                    IsDisputed=IsDisputed,
                    DisputeDesc = DisputeDesc,
                    IsMaintenanceApplicable=IsMaintenanceApplicable,
                    CurrentMaintenancePM=CurrentMaintenancePM,
                    IsBLExpenseApplicable = IsBLExpenseApplicable,
                    IsDLExpenseApplicable=IsDLExpenseApplicable,
                    IsULExpenseApplicable=IsULExpenseApplicable,
                    buildings=buildings
        )
        print(ins)
        ins.save()
       
        return redirect('units')
    context = {'form':form}
    return render(request, 'addunit.html', context)


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

@login_required(login_url='login')
def updateunit(request, pk):
    if currentUserAccess(request,pk): #called a function ^
        unit  = Units.objects.get(id=pk)
        form = UnitsForm(instance=unit)

        if request.method == 'POST':

            UnitName = request.POST.get('UnitName')
            UnitType = request.POST.get('UnitType')
            IsExpenseApplicable = request.POST.get('IsExpenseApplicable')

            UnitName = request.POST.get('UnitName')
            OccupiedStatus = request.POST.get('OccupiedStatus')
            UnitType = request.POST.get('UnitType')
            CoveredArea = request.POST.get('CoveredArea')
            IsDisputed = request.POST.get('IsDisputed')
            DisputeDesc = request.POST.get('DisputeDesc')
            IsMaintenanceApplicable = request.POST.get('IsMaintenanceApplicable')
            CurrentMaintenancePM = request.POST.get('CurrentMaintenancePM')
            IsBLExpenseApplicable = request.POST.get('IsBLExpenseApplicable')
            IsDLExpenseApplicable = request.POST.get('IsDLExpenseApplicable')
            IsULExpenseApplicable = request.POST.get('IsULExpenseApplicable')

            # if IsExpenseApplicable == 'true':
            #     IsExpenseApplicable = True
            # else:
            #     IsExpenseApplicable = False
            Units.objects.filter(id=pk).update(UnitName=UnitName,OccupiedStatus=OccupiedStatus,UnitType=UnitType,CoveredArea=CoveredArea,IsDisputed=IsDisputed,DisputeDesc=DisputeDesc,IsMaintenanceApplicable=IsMaintenanceApplicable,CurrentMaintenancePM=CurrentMaintenancePM,IsBLExpenseApplicable=IsBLExpenseApplicable,IsDLExpenseApplicable=IsDLExpenseApplicable,IsULExpenseApplicable=IsULExpenseApplicable)
            # (UnitName=UnitName,OccupiedStatus=OccupiedStatus,UnitType=UnitType,CoveredArea=CoveredArea,IsDisputed=IsDisputed,DisputeDesc=DisputeDesc,IsMaintenanceApplicable=IsMaintenanceApplicable,CurrentMaintenancePM=CurrentMaintenancePM,IsBLExpenseApplicable=IsBLExpenseApplicable,IsDLExpenseApplicable=IsDLExpenseApplicable,IsULExpenseApplicable=IsULExpenseApplicable)
            return redirect('/units')

        context = {'form':form}
        return render(request, 'updateunit.html', context)
    else:
        return render(request, 'notfound.html',{})

@login_required(login_url='login')
def deleteunit(request,pk):
    if currentUserAccess(request, pk):
        Units.objects.filter(id=pk).update(IsActive=False)
        return redirect('/units')
    else:
        return render(request, 'notfound.html',{})

def currentUserAccess(request, pk):
    currentUserId = request.user.id
    all = BuildingUsers.objects.filter(user__id=currentUserId)
    for i in all:
        currentBuildingId = i.buildings.id
    unitList = []
    if all:
        unitList = Units.objects.filter(buildings__id=currentBuildingId, IsActive=True)
    for i in unitList:
        if i.id == int(pk):
            return True
    return False

