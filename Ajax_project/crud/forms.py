from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'age': forms.TextInput(attrs={'class':'form-control', 'id':'ageid'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'id': 'addressid'}),
            'salary': forms.TextInput(attrs={'class':'form-control', 'id': 'salaryid'})

        }

        
