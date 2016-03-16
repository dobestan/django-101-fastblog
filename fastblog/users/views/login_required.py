"""
login_required decorator usage in FBV, CBV.
"""
from django.views.generic import View, TemplateView
from django.shortcuts import render


def login_required_view(request):
    return render(
        request,
        "users/login_required.html",
        context={},
    )


class LoginRequiredView(TemplateView):
    template_name = "users/login_required.html"
