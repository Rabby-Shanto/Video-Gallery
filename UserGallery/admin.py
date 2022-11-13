from django.contrib import admin

# Register your models here.
from .models import CustomUser,Video,PlayList


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title','playlist','playlist_obj']

    def playlist_obj(self, obj):
        return '%s'%(obj.playlist.user)
    playlist_obj.short_description = 'user'

admin.site.register(CustomUser)
admin.site.register(Video,VideoAdmin)
admin.site.register(PlayList)

