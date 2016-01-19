"""jaydork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import *
from home import views


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home_page, name='view'), #redirect for each page other than twitch
	url(r'view', views.home_page, name='view'),
	url(r'bio', views.bio, name='bio'),
	url(r'videos', views.videos, name='videos'),
	url(r'games', views.games, name='games'),
	url(r'signin', views.signin, name='signin'),
	url(r'create_acct', views.create_acct, name='create_acct'),
]
