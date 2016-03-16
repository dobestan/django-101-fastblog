from django.contrib.auth import logout
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse("home"))

