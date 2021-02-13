from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from djangoProject import settings


class Status(models.IntegerChoices):
    PUBLISHED = True, _('Published')
    NOT_PUBLISHED = False, _('Not Published')


class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(_('short description'), max_length=200)
    image = models.URLField(max_length=400)
    published_state = models.BooleanField(_('published state'), choices=Status.choices, default=False)
    full_description = models.TextField(_("full description"), blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_description = models.TextField(_("full description"), blank=True)
    is_published = models.BooleanField(choices=Status.choices, default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(default=timezone.now)
