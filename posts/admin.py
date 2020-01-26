from django.contrib import admin
from .models import Accom, Image, Application, InternalMessage

admin.site.register(Accom)
admin.site.register(Application)
admin.site.register(Image)
admin.site.register(InternalMessage)
