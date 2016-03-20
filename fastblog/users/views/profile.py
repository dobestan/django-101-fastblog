from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = "users/profile.html"

    def get_object(self):
        return self.request.user
