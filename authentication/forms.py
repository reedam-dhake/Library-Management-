from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django import forms
from main.models import Student
from django.utils.translation import gettext_lazy as _

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_("First name"))
    last_name = forms.CharField(max_length=30, label=_("Last name"))
    username = forms.CharField(max_length=30, label=_("Username"), help_text=_("Will be shown e.g. when commenting."))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.save()

#class SignUpForm(UserCreationForm):
#	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
#	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
#	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
#
#	class Meta:
#		model = User
#		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
#
#	def __init__(self, *args, **kwargs):
#		super(SignUpForm, self).__init__(*args, **kwargs)
#
#		self.fields['username'].widget.attrs['class'] = 'form-control'
#		self.fields['password1'].widget.attrs['class'] = 'form-control'
#		self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	#last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	#is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	#is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	#is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	#date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')#, 'last_login','is_superuser','is_active','is_staff','date_joined')

class ChangePasswordForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2')

class ProfileForm(forms.ModelForm):
        class Meta:
        	model = Student
        	fields = ('image',) #Note that we didn't mention user field here.
        	widgets = {
				'image': forms.FileInput(attrs= {'class':'form-control', 'required': False,}),
			}