from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from .models import Post

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    readonly_fields = ('banner_preview',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'body', 'banner')
        }),
        ('Banner', {
            'fields': ('banner_preview', 'banner')
        }),
    )

    def banner_preview(self, obj):
        if obj.banner:
            return format_html('<img src="{}" width="100" height="100" opacity="0.6" />', obj.banner.url)
        return format_html('<img src="{}" width="100" height="100" opacity="0.6" />', settings.STATIC_URL + 'images/fallback.jpg')


    banner_preview.short_description = 'Banner Preview'
