"""fastblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from fastblog.views import home
from posts.views import PostListView, PostDetailView, PostCommentCreateView, PostCreateView
from users.views import LoginView, LogoutView, SignupView,\
    login_required_view, LoginRequiredView, ProfileView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^posts/$', PostListView.as_view(), name="posts"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="new-post"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/(?P<pk>\d+)/comments/$', PostCommentCreateView.as_view(), name="post-comments"),

    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^profile/$', ProfileView.as_view(), name="profile"),

    url(r'^login_required/fbv/$', login_required_view, name="login-required-fbv"),
    url(r'^login_required/cbv/$', LoginRequiredView.as_view(), name="login-required-cbv"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
