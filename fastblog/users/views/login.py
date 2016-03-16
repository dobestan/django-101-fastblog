from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class LoginView(View):

    def get(self, request):
        return render(
            request,
            "users/login.html",
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next") or reverse("home")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "성공적으로 로그인 되었습니다.",
            )

            return redirect(next_page)
        return redirect(reverse("login"))
