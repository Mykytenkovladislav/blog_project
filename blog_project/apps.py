from django.apps import AppConfig


class BlogProjectConfig(AppConfig):
    name = 'blog_project'

    def ready(self):
        from django.db.models.signals import post_save

        from blog_project.models import Comment, Post
        from blog_project.signals import comment_is_created, post_is_created

        post_save.connect(comment_is_created, sender=Comment)
        post_save.connect(post_is_created, sender=Post)
