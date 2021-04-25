from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm, ChangePasswordForm, ProfileForm, SignupForm
from allauth.account.views import SignupView


class AccountSignupView(SignupView):
    # Signup View extended
    form_class = "SignupForm"
    # change template's name and path
    template_name = "account/signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...

#class UserRegisterView(generic.CreateView):
#	form_class = SignUpForm
#	template_name = 'registration/register.html'
#	success_url = reverse_lazy('account_login')


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.student)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.student)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'editProfile.html', args)

class ChangePasswordView(PasswordChangeView):
	form_class = ChangePasswordForm
	template_name = 'changePass.html'
	success_url = reverse_lazy('home')