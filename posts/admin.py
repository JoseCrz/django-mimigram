
# ? Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# ? Models
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display: ('pk', 'title', 'user', 'profile', 'photo', 'created', 'modified')
    list_display_links: ('pk', 'title')
    list_editable: ('photo')

    search_fields: ('post__title', 'post__user')

    fieldsets = (
        ('Post Info', {
            'fields': ('title', 'user', 'photo')
        }),
        ('Meta Data', {
            'fields': ('created', 'modified')
        })
    )

    readonly_fields = ('created', 'modified')

