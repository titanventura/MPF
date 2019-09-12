from django import forms
from .models import product,brand



class ProductCreateForm(forms.ModelForm):
    class Meta:
        model=product
        fields=["prodbrand","model","specification","rating","year_of_launch","photo"]

class BrandCreateForm(forms.ModelForm):
    class Meta:
        model=brand
        fields= ["name","position","years","description","logo"]