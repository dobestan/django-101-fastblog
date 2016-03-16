from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


class SignupView(View):

    def get(self, request):
        return render(
            request,
            "users/signup.html",
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            password=password,
        )

        # 회원가입 후 자동 로그인 구현하기
        user = authenticate(
            username=username,
            password=password,
        )
        login(request, user)

        messages.add_message(
            request,
            messages.SUCCESS,
            "성공적으로 회원가입 되었습니다.",
        )

        return redirect(reverse("home"))
