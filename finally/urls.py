"""finally URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from mysite import views
from mysite.admin import admin_site

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^zzesadmin/', admin_site.urls),
    url(r'^regist/$', views.regist),
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^info/$', views.info),
    url(r'^data/$', views.data),
    url(r'^messagerev/$', views.messagerev),
    url(r'^messagedel/(?P<pk>[0-9]+)$', views.messagedel),
    url(r'^message/$', views.message),
    url(r'^open/$', views.statusopen),
    url(r'^cmdopen/$', views.cmdopen),
    url(r'^numsum/$', views.statusnum),
]
# +static(settings.STATIC_URL,document_root=settings.STATCFILES_DIRS)
