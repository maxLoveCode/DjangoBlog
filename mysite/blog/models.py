from __future__ import unicode_literals
from ckeditor.fields import RichTextField

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    tags = models.ManyToManyField("Tag", blank=True)
    create_date = models.DateField(auto_now_add=True, db_index=True)

    @models.permalink
    def get_absolute_url(self):
        return "/blog/%s/" % self.slug

    def __str__(self):
        return "%s" % self.title;


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)
    create_date = models.DateField(auto_now_add=True, db_index=True)

    @models.permalink
    def get_absolute_url(self):
        return "/tags/%s/" % self.slug

    def __str__(self):
        return "%s" % self.title

