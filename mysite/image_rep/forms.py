from django import forms
from multiupload.fields import MultiImageField

class User_Inputs(forms.Form):
    image_1 = forms.ImageField()
    image_2 = forms.ImageField(required=False)
    image_3 = forms.ImageField(required=False)
    image_4 = forms.ImageField(required=False)
    image_5 = forms.ImageField(required=False)
    image_name = forms.CharField(max_length=500)
