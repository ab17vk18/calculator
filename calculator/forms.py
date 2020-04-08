from django.forms import ModelForm
from . import models

class CalcForm(ModelForm):

     class Meta:
         model = models.Calc
         fields = ['a', 'b']
