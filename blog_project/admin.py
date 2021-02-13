from django.contrib import admin
from django.template.defaultfilters import truncatewords

from .models import Post, Comment, Status


def change_status_to_unpublished(modeladmin, request, queryset):
    queryset.update(status=Status.NOT_PUBLISHED)


change_status_to_unpublished.short_description = 'Mark selected as Not Published'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'short_description', 'image', 'published_state')
    list_filter = ("published_state",)
    search_fields = ['title', 'short_description']
    list_per_page = 10
    actions = ['change_status_to_published', 'change_status_to_unpublished']

    def change_status_to_published(self, request, queryset):
        queryset.update(published_state=Status.PUBLISHED)

    change_status_to_published.short_description = 'Mark selected as Published'

    def change_status_to_unpublished(self, request, queryset):
        queryset.update(published_state=Status.NOT_PUBLISHED)

    change_status_to_unpublished.short_description = 'Mark selected as Not Published'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_full_description', 'post', 'is_published', 'created_date')
    list_filter = ("is_published",)
    list_per_page = 10
    actions = ['change_status_to_published', 'change_status_to_unpublished']

    def change_status_to_published(self, request, queryset):
        queryset.update(is_published=Status.PUBLISHED)

    change_status_to_published.short_description = 'Mark selected as Published'

    def change_status_to_unpublished(self, request, queryset):
        queryset.update(is_published=Status.NOT_PUBLISHED)

    change_status_to_unpublished.short_description = 'Mark selected as Not Published'

    def get_full_description(self, obj):
        return truncatewords(obj.full_description, 4)

    get_full_description.short_description = 'Comment'
