from django import forms
from .models import Levels
from .models import Members
from .models import Units


class LevelsForm(forms.ModelForm):
    class Meta:
        model = Levels
        fields = ('LevelName','LevelType', 'IsExpenseApplicable')

        widgets = {
            'LevelName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Level Name', 'name': 'levelname'}),
            'LevelType': forms.Select(attrs={'class': 'form-select'}),
            'IsExpenseApplicable': forms.NullBooleanSelect(attrs={'class': 'form-select'})
        }
class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ('MemberType','OwnerType', 'OccupantType', 'MemberName','CellPhone', 'Email', 'AddressLine1','AddressLine2','City','Province','PostalCode')

        widgets = {
            'MemberType': forms.Select(attrs={'class': 'form-select'}),
            'OwnerType': forms.Select(attrs={'class': 'form-select'}),
            'OccupantType': forms.Select(attrs={'class': 'form-select'}),
            'MemberName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member Name', 'name': 'MemberName'}),
            'CellPhone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: 0333-3333333', 'name': 'CellPhone'}),
            'Email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'abc@gmail.com', 'name': 'Email'}),
            'AddressLine1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No, Building Name, Street Name, Area Name', 'name': 'AddressLine1'}),
            'AddressLine2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No, Building Name, Street Name, Area Name', 'name': 'AddressLine2'}),
            'City': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Karachi', 'name': 'City'}),
            'Province': forms.Select(attrs={'class': 'form-select'}),
            'PostalCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXX', 'name': 'PostalCode'}),
            
        
        }

class UnitsForm(forms.ModelForm):
    class Meta:
        model = Units
        fields = ('UnitName','OccupiedStatus', 'UnitType', 'CoveredArea','IsDisputed', 'DisputeDesc', 'IsMaintenanceApplicable','CurrentMaintenancePM','IsBLExpenseApplicable','IsDLExpenseApplicable','IsULExpenseApplicable')

        widgets = {
            'UnitName': forms.TextInput(attrs={'class': 'form-select'}),
            'OccupiedStatus': forms.Select(attrs={'class': 'form-select' , 'placeholder': 'Empty', 'name': 'OccupiedStatus'}),
            'UnitType': forms.Select(attrs={'class': 'form-select' , 'placeholder': 'Flat', 'name': 'UnitType'}),
            'CoveredArea': forms.TextInput(attrs={'class': 'form-control'}),
            'IsDisputed': forms.Select(attrs={'class': 'form-select'}),
            'DisputeDesc' : forms.TextInput(attrs={'class': 'form-control'}),
            'IsMaintenanceApplicable': forms.Select(attrs={'class': 'form-select'}),
            'CurrentMaintenancePM' : forms.TextInput(attrs={'class': 'form-control'}),
            'IsBLExpenseApplicable': forms.Select(attrs={'class': 'form-select'}),
            'IsDLExpenseApplicable': forms.Select(attrs={'class': 'form-select'}),
            'IsULExpenseApplicable': forms.Select(attrs={'class': 'form-select'}),
            # 'Email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'abc@gmail.com', 'name': 'Email'}),
            # 'AddressLine1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No, Building Name, Street Name, Area Name', 'name': 'AddressLine1'}),
            # 'AddressLine2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House No, Building Name, Street Name, Area Name', 'name': 'AddressLine2'}),
            # 'City': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Karachi', 'name': 'City'}),
            # 'Province': forms.Select(attrs={'class': 'form-select'}),
            # 'PostalCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXX', 'name': 'PostalCode'}),
            
        
        }