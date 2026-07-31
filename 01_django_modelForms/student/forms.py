from django import forms
from .models import student

class studentForm(forms.ModelForm):
    class Meta:
       model = student
       fields = ['name','age','email']

       def clean_age(self):
           age = self.clean_age.get('age')
           if age<18:
            raise forms.ValidationError("Age must be more than 18.")
           return age