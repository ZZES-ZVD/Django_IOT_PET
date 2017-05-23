from django.contrib import admin
from .models import User, Iotdata, Message
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# admin.site.register(User)
# admin.site.register(Iotdata)
# admin.site.register(Message)
# Register your models here.
class MyAdminSite(AdminSite):
    site_title = ugettext_lazy('治电科技物联网后台管理')
    site_header = ugettext_lazy('ZZES IOT FOR PET')

admin_site = MyAdminSite()

admin_site.register(User)
admin_site.register(Iotdata)
admin_site.register(Message)