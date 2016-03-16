from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect


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

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(request, user)
            return redirect(reverse("home"))
        return redirect(reverse("login"))
