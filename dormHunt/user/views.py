from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import UpdateView
from user.forms import RegistrationForm, UserAuthenticationForm, UserProfileForm
from user.models import User, UserProfile
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your views here.

def register(request):
    context = {}
    registered = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_password)
            # login(request, user)
            return redirect('user:user_login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user/register.html', context)

def user_login(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        # return redirect('home:view_home')
        if user.user_type == "Landlord":
            return redirect('landlord:landlord_home')
        else:
            return redirect('tenant:tenant')


    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # if not user.userprofile:
                #     profile = UserProfile(user=user)
                #     profile.save()
                try:
                    user.userprofile
                    pass
                except ObjectDoesNotExist:
                    profile = User.objects.get(username=username)
                    user_profile = UserProfile(user=profile)
                    user_profile.save()
                if user.user_type == "Landlord":
                    return redirect('landlord:landlord_home')
                else:
                    return redirect('tenant:tenant')
            else:
                messages.warning(request, "ACCOUNT IS NOT ACTIVE!")
                return redirect('user:user_login')
        else:
            messages.error(request, 'Invalid login details supplied!')
    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'user/login.html', context)

def user_forgot_password(request):
    return render(request, 'user/forgot_password.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:user_login'))

# class UserDetailView(DetailView):
#     model = User
#     template_name = 'user/user_profile.html'

@login_required
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {}

    try:
        user.userprofile
        if user.userprofile.birthday:
            user.userprofile.calculate_age()
        context['user_profile'] = user.userprofile
    except ObjectDoesNotExist:
        profile = UserProfile(user=user)
        profile.save()
        context['user_profile'] = user.userprofile

    return render(request, 'user/user_profile.html', context)

class UserProfileUpdateView(UpdateView):
    template_name = 'user/edit_profile.html'
    context_object_name = 'user_profile'
    form_class = UserProfileForm
    model = UserProfile

    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user=self.request.user)

        # form.instance.picture55 = form.instance.picture
		#Opening the uploaded image
        try:
            img = Image.open(form.instance.picture)
            output = BytesIO()

            #Resize/modify the image
            img = img.resize((55,55))

            #after modifications, save it to the output
            img.save(output, format='JPEG', quality=100)
            output.seek(0)

            #change the imagefield value to be the newley modifed image value
            form.instance.picture55 = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %form.instance.picture.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        except:
            pass

        return super(UserProfileUpdateView, self).form_valid(form)
