from django import forms
from .models import *



class details_forms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    email = forms.EmailField(max_length=50)
    phone = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea())

    def clean(self):
        cleaned_data = super(details_forms, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        message = cleaned_data.get('message')
        if not name and not email and not phone and not message:
            raise forms.ValidationError('You have to fill all the fields')



    class Meta :
        model = student
        fields = ['name','email','phone','message']

