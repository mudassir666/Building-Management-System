from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Buildings(models.Model):
    BuildingName = models.CharField(max_length=100,null=True)
    LoginCode = models.CharField(max_length=100,null=True)
    BuildingType = models.PositiveSmallIntegerField(default=1, null=True)
    AddressLine1 = models.TextField(max_length=100,null=True) #textdfeild
    AddressLine2 = models.TextField(max_length=100,null=True)
    City = models.CharField(max_length=100,null=True)       # city forign key, province ka ek or forign key banegyga
    Province = models.CharField(max_length=100,null=True)
    PostalCode = models.CharField(max_length=100,null=True)
    BuildingStatus = models.PositiveSmallIntegerField(default=1, null=True)
    InsDate = models.DateTimeField(auto_now_add=True,null=True) 
    ModDate = models.DateTimeField(auto_now_add=True,null=True) 
    NoOfUsers = models.PositiveSmallIntegerField(default=1, null=True)
    LicenseType = models.PositiveSmallIntegerField(default=1, null=True)
    ContactPerson = models.CharField(max_length=100,null=True)
    ContactPersonCell = models.CharField(max_length=100,null=True)
    ContactPersonEmail = models.CharField(max_length=100,null=True)
    HasMonthlyMaintenance = models.BooleanField(null=True)
    MaintenanceType = models.PositiveSmallIntegerField(default=1, null=True)
    MaintenancePM = models.DecimalField(decimal_places=6,max_digits=30,null=True)


    def __str__(self):
        return self.BuildingName +" id="+str(self.id)     # kise ka kaam return karwana hai

    
class BuildingUsers(models.Model):
    
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    LoginName = models.CharField(max_length=100,null=True)
    LoginPassword = models.CharField(max_length=100,null=True)
    FirstName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=100,null=True)
    UserType = models.PositiveSmallIntegerField(null=True)
    IsActive = models.BooleanField(null=True)
    Email = models.EmailField()
    buildings = models.ForeignKey(Buildings, null=True, on_delete=models.DO_NOTHING) # automatic update get kar leta hai


    def __str__(self):
        return self.FirstName+" "+self.LastName


class Levels(models.Model):
    LevelName = models.CharField(max_length=100,null=True)

    TYPES = (
        ('Basement', 'Basement'),
        ('Ground', 'Ground'),
        ('Mezanine', 'Mezanine'),
        ('Floor', 'Floor')
    )

    LevelType = models.CharField(max_length=200, null=True, choices=TYPES)
    # LevelType = models.PositiveSmallIntegerField(null=True)
    IsActive = models.BooleanField(null=True)
    InsDate = models.DateTimeField(auto_now_add=True,null=True)  #//manually or automatic
    ModDate = models.DateTimeField(auto_now_add=True,null=True)
    IsExpenseApplicable = models.BooleanField(null=True)
    buildings = models.ForeignKey(Buildings, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.LevelName+" "+ self.buildings.BuildingName +" id="+ str(self.id)

class Units(models.Model):

    UnitName = models.CharField(max_length=200,null=True)
    OccupiedStatus = models.PositiveSmallIntegerField(default=1, null=True)
    UnitType = models.PositiveSmallIntegerField(default=1, null=True)
    OwnedByMemberId = models.PositiveIntegerField(null=True)
    OccupiedByMemberId = models.PositiveIntegerField(null=True)
    CoveredArea = models.CharField(max_length=200,null=True)
    IsDisputed = models.BooleanField(null=True)
    DisputeDesc = models.TextField()
    IsMaintenanceApplicable = models.BooleanField(null=True)
    CurrentMaintenancePM = models.DecimalField(decimal_places=6,max_digits=30,null=True)
    IsBLExpenseApplicable = models.BooleanField(null=True)
    IsDLExpenseApplicable = models.BooleanField(null=True)
    IsULExpenseApplicable = models.BooleanField(null=True)
    IsActive = models.BooleanField(null=True,default=True)
    levels = models.ForeignKey(Levels, null=True, on_delete=models.DO_NOTHING)
    buildings = models.ForeignKey(Buildings, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.UnitName+" "+self.levels.LevelName+" "+ self.buildings.BuildingName +" id="+ str(self.id)
    
class Members(models.Model):
    MemberType = models.PositiveSmallIntegerField(null=True)
    OwnerType = models.PositiveSmallIntegerField(null=True)
    OccupantType = models.PositiveSmallIntegerField(null=True)
    MemberName = models.CharField(max_length=100,null=True)
    IsActive = models.BooleanField(null=True)
    InsDate = models.DateTimeField(auto_now_add=True,null=True)
    ModDate = models.DateTimeField(auto_now_add=True,null=True)
    CellPhone = models.CharField(max_length=100,null=True)
    Email = models.EmailField(max_length=100,null=True)             
    AddressLine1 = models.TextField(max_length=100,null=True)
    AddressLine2 = models.TextField(max_length=100,null=True)
    City = models.CharField(max_length=100,null=True)           #permanent
    Province = models.CharField(max_length=100,null=True)
    PostalCode = models.CharField(max_length=100,null=True)
    buildings = models.ForeignKey(Buildings, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.MemberName + " " + self.buildings.BuildingName +" id="+ str(self.id)

