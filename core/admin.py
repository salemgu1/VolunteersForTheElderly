from django.contrib import admin

from . import models
from .models import Profile, Following, Follower, Post, Comment, PageUpdate


# Adding Feedback Model to Django Admin
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


class UrgentRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

class PageUpdateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date',)
    search_fields = ('subject',)
    date_hierarchy = 'date'


admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(models.PageUpdate,PageUpdateAdmin)
admin.site.register(models.UrgentRequest, UrgentRequestAdmin)


