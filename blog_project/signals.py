from django.core.mail import send_mail as django_send_mail


def post_is_created(sender, instance, created, *args, **kwargs):
    if created:
        django_send_mail('New post added',
                         f'New post {instance.tittle} created by {instance.user}',
                         'no-reply@test.com',
                         ['admin@example.com'])


def comment_is_created(sender, instance, created, *args, **kwargs):
    if created:
        django_send_mail('New comment added',
                         f'New comment created by user: {instance.user}',
                         'no-reply@test.com',
                         ['admin@example.com'])
        django_send_mail('New comment added',
                         f'New comment created by user: {instance.user}. '
                         f'Pls, check your post: http://127.0.0.1:8000/blog/{instance.post.id}',
                         'no-reply@test.com',
                         ['admin@example.com'])
