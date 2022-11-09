from django.contrib import admin

# Register your models here.
from .models import CustomUser,Video,PlayList

admin.site.register(CustomUser)
admin.site.register(Video)
admin.site.register(PlayList)

