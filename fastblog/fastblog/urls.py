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
from posts.views import PostListView, PostDetailView, post_comments, PostCreateView
from users.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name="home"),
    url(r'^posts/$', PostListView.as_view(), name="posts"),
    url(r'^posts/new/$', PostCreateView.as_view(), name="new-post"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="post"),
    url(r'^posts/(?P<pk>\d+)/comments/$', post_comments, name="post-comments"),

    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
]
