from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserStaffForm, UserSuperUserForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Tolong masukkan username dan password dengan benar. Perhatikan bahwa "
            "kolomnya sensitif atau perhatikan capslock anda"
        ),
        'inactive': _("This account is inactive."),
    }

class MyLoginView(LoginView):
    authentication_form = MyAuthForm

@login_required
def index(request):
    return render(request, 'dashboard/blank.html', {'user': request.user})
def register(request):
    pass


@login_required
def create_staff(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden(render(request, 'dashboard/403.html') )
    if request.method == 'POST':
        form = UserStaffForm(request.POST)
        if form.is_valid():
            form.instance.is_staff = True
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun anda baru terdaftar! Sekarang anda bisa masuk')
            return redirect('login')
    else:
        form = UserStaffForm()
    return render(request, 'users/create_staff.html', {'form': form})

@login_required
def create_superuser(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden(render(request, 'dashboard/403.html') )
    if request.method == 'POST':
        form = UserSuperUserForm(request.POST)
        if form.is_valid():
            form.instance.is_staff = True
            form.instance.is_superuser = True
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Akun anda baru terdaftar! Sekarang anda bisa masuk')
            return redirect('login')
    else:
        form = UserSuperUserForm()
    return render(request, 'users/create_superuser.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Akun anda sudah diupdate!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def list_staff(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'users/list_staff.html', {'users': users})

@login_required
def delete_staff(request, pk):
    User.objects.get(pk=pk).delete()
    messages.success(request, 'Staff berhasil dihapus')
    return redirect('list_staff')
    