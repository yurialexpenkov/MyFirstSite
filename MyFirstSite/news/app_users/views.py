from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User

from app_news.models import MyComment
from app_users.forms import RegisterForm
from app_users.models import Profile


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = '/'


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_group = Group.objects.get(name='Пользователи')
            user.groups.add(user_group)
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def account_view(request, profile_id):
    user = Profile.objects.get(user_id=profile_id)
    print(user.city)
    return render(request, 'users/account.html', {'user': user})
