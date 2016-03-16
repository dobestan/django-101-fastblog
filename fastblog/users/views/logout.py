from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class LogoutView(View):

    def get(self, request):
        logout(request)

        messages.add_message(
            request,
            messages.SUCCESS,
            "성공적으로 로그아웃 되었습니다.",
        )

        return redirect(reverse("home"))
