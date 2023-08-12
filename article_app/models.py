from django.db import models
from core_app.models import BaseModel
from auditlog.registry import auditlog
from django.urls import reverse
from writers_app.models import Writer
# Create your models here.


class Article(BaseModel):

    article_name = models.CharField(max_length=150, blank=True,null=True)
    main_keyword = models.CharField(max_length=200, blank=True, null=True)
    sub_keywords = models.TextField(max_length=20000, blank=True, null=True)
    writer_alloted = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True, blank=True)

    class ArticleStatus(models.TextChoices):
        WRITING = 'WRT', 'Writing'
        WAITING = 'WAT', 'Waiting'
        PENDING = 'PED', 'Pending'
        COMPLETED = 'COM', 'Completed'
        PUBLISHED = 'PUB', 'Published'
        

    article_status = models.CharField(
        max_length=3,
        choices=ArticleStatus.choices,
    default='WAITING')

    def get_absolute_url(self):
        return reverse('article_app:article_detail', args=[str(self.id)])

    def __str__(self):
        return self.article_name






auditlog.register(Article)