"""
login_required decorator usage in FBV, CBV.
"""
from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required()
def login_required_view(request):
    return render(
        request,
        "users/login_required.html",
        context={},
    )


# @method_decorator(login_required, name='dispatch')
class LoginRequiredView(LoginRequiredMixin, TemplateView):
    template_name = "users/login_required.html"

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(LoginRequiredView, self).dispatch(*args, **kwargs)
