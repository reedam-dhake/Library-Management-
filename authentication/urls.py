from django.urls import path
from .views import ChangePasswordView, AccountSignupView #UserRegisterView
from . import views
urlpatterns = [
	#path('register/',UserRegisterView.as_view(), name='register'),
	path("accounts/signup/", AccountSignupView.as_view()),
	path('editProfile/',views.edit_profile, name='edit-profile'),
	path('password/', ChangePasswordView.as_view(), name='change-pass'),

]