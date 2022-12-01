from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=50,unique=True,null=True,blank=True)

    def __str__(self):
        return self.name



class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
            )


    title=models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    publish_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media/%Y/%m/%d/", null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='blogs',null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    status=models.BooleanField(max_length=10,default='Draft',choices=STATUS_CHOICES)
    objects=models.Manager()
    newmanager=NewManager()


    def __str__(self):
        return self.title


class Comment(models.Model):
    comment=models.TextField()
    post=models.ForeignKey(Post,on_delete=models.DO_NOTHING,related_name='comments')
    publish_date=models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
