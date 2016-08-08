"""project URL Configuration

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
from site01 import views as views1
from site02 import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views1.signup, name="signup"),
    url(r'^login/$', views1.login1, name="login"),
    url(r'^home/$', views1.home, name="home"),
    url(r'^logout/$', views1.logout1, name="logout"),

    url(r'^display_books/$', views1.display_books, name="display_books"),
    url(r'^insert_books/$', views1.insert_books, name="insert_books"),
    url(r'^display_authors/$', views1.display_authors, name="display_authors"),
    url(r'^insert_authors/$', views1.insert_authors, name="insert_authors"),
    url(r'^display_publishers/$', views1.display_publishers, name="display_publishers"),
    url(r'^insert_publishers/$', views1.insert_publishers, name="insert_publishers"),

    url(r'^site2/$', views2.home, name="site2"),
    url(r'^signup2/$', views2.signup, name="signup1"),
    url(r'^login2/$', views2.login2, name="login1"),
]
