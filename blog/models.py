from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
        def get_queryset(self):
            return super(PublishedManager,self).get_queryset()\
                .filter(status = "published")

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique_for_date ='published')
    author = models.ForeignKey(User, related_name ='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(choices =STATUS_CHOICES,default = 'draft' ,max_length=50)
    
    objects = models.Manager()
    published = PublishedManager()
    
    def get_absolute_url(self):
      return reverse('blog:post_detail',args=[
        self.publish.year,
        self.publish.month,
        self.publish.day,
        self.slug,
      ])
    

    

class Meta:
        ordering = ('-publish',)

def __str__(self):
        return self.title
    
    

    #    return reverse("_detail", kwargs={"pk": self.pk})