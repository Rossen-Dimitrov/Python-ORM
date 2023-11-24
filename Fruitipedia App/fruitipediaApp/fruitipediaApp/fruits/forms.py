from django import forms

from fruitipediaApp.fruits.models import Category, Fruit


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
