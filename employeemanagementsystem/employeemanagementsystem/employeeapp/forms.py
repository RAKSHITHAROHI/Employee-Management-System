from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['eid','ename','egender','esalary','eyoe','edept','ecompany']