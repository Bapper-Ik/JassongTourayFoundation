from django.contrib import admin
from .models import Posts, Audio


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AudioAdmin(admin.ModelAdmin):
    list_display = ('title',)
#
#
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#
#
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('title',)


admin.site.site_header = "Jassong Touray Admin Dashboard"
admin.site.site_title = 'Jassong Touray admin'
admin.site.index_title = 'Jassong Touray admin area'


admin.site.register(Posts, PostAdmin)
admin.site.register(Audio, AudioAdmin)
# admin.site.register(Videos, VideoAdmin)
# admin.site.register(Images, ImageAdmin)

