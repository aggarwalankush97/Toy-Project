from django.db import models
from django.contrib.auth.models import User
from .constants import ArticleStatus
# Create your models here.


class Writer(models.Model):
    is_editor = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=200, )
    content = models.TextField()
    status = models.CharField(
        max_length=8,
        choices=ArticleStatus.choices,
        default=ArticleStatus.PENDING.value,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    written_by = models.ForeignKey(
        Writer, on_delete=models.CASCADE, related_name="articles", null=True, blank=True)
    edited_by = models.ForeignKey(
        Writer, on_delete=models.CASCADE, related_name="edited_articles", null=True, blank=True)
