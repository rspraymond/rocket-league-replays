from django.db import models

from cms.apps.media.models import ImageRefField
from cms.apps.pages.models import ContentBase, Page


class Content(ContentBase):
    class Meta:
        verbose_name = 'homepage'


class ContentColumn(models.Model):
    page = models.ForeignKey(Page)

    title = models.CharField(
        max_length=100,
    )

    url = models.CharField(
        "URL",
        max_length=100,
    )

    image = ImageRefField()


class Placeholder(ContentBase):
    pass
