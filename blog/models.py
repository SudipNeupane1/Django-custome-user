from unicodedata import category
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.name
        




class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
        
    )
    category= models.ForeignKey(
        Category,on_delete=models.PROTECT,default=1
    )
    title= models.CharField(max_length=240)
    excerpt=models.TextField(null=True)
    content= models.TextField()
    slug= models.SlugField(max_length=250,unique_for_date='published')
    published=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=10,choices=options,default='published')
    objects = models.Manager()#default manager
    post_objects= PostObjects()# custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


