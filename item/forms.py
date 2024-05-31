from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'price', 'image',]
        widgets = {
            'category': forms.Select(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'name': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'description': forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'price': forms.NumberInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'image': forms.FileInput(attrs={
                'class':' mb-6 w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image', 'is_sold',]
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'description': forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'price': forms.NumberInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'image': forms.FileInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class':'mb-6 w-full py-4 px-6 rounded-xl border border-gray-300',
            }),
        }