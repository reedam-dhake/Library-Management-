from django import forms
from .models import *
from django.contrib.auth.models import User
class AddNewBook(forms.ModelForm):
	class Meta:
		model = BookName
		fields = ('name','pages','isbnNumber','publisher','author','year','summary','available_copies','pdf','image')
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control'}),
			'pages' : forms.TextInput(attrs={'class':'form-control'}),
			'isbnNumber' : forms.TextInput(attrs={'class':'form-control'}),
			'publisher' : forms.TextInput(attrs={'class':'form-control'}),
			'author' : forms.TextInput(attrs={'class':'form-control'}),
			'year' : forms.TextInput(attrs={'class':'form-control'}),
			'summary' : forms.Textarea(attrs={'class':'form-control'}),
			'available_copies' : forms.TextInput(attrs={'class':'form-control'}),
			'pdf': forms.FileInput(attrs= {'class':'form-control', 'required': False,}),
			'image': forms.FileInput(attrs= {'class':'form-control', 'required': False,}),

		}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'name','email', 'body',)
        widgets = {
        	'name' : forms.TextInput(attrs={'class':'form-control'}),
        	'email' : forms.EmailInput(attrs={'class':'form-control'}),
        	'body' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
