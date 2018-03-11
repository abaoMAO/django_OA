from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from user.forms import LoginForm, RegisterForm


# Create your views here.
from user.models import UserProfile


class LoginView(View):
    def get(self, request):
        return render(request, "user_login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponsePermanentRedirect(reverse('index'))
                else:
                    return render(request, "user_login.html", {"msg": "邮箱未激活"})
            else:
                return render(request, "user_login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "user_login.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "user_register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")

            if UserProfile.objects.filter(email=user_name):
                # 验证用户名是否已经存在
                return render(request, "user_register.html", {"register_form": register_form}, {"msg": "用户名已经存在"})

            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            # send_register_email(user_name, "register")
            return render(request, "user_login.html")
        else:
            return render(request, "user_register.html", {"register_form": register_form})


class IndexView(View):
    # 首页
    def get(self, request):
        return render(request, "index.html", {})