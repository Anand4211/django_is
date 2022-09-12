from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class Poost(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('published','Published'))
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    title=models.CharField(max_length=264)
    author=models.ForeignKey(User,related_name='blog_post',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now())
    create=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=264,choices=(('draft','Draft'),('published','Published')),default='draft')
    # tag=TaggableManager()
    class Meta:

        ordering=('-publish',)

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])



