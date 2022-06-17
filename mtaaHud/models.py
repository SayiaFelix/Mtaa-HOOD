from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models import Q

Priority=(
    ('Informational', 'Informational'),
    ('High Priority', 'High Priority'),
)

# Create your models here.
class Hood(models.Model):
    hood_name = models.CharField(max_length = 100)
    hood_photo = models.ImageField(upload_to='hoods/')
    occupants_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hood_name

    def create_hood(self):
        self.save()
        
    @classmethod
    def delete_hood(cls, hood_name):
        cls.objects.filter(hood_name=hood_name).delete()

    @classmethod
    def find_hood(cls, search_term):
        search_results = cls.objects.filter(hood_name__icontains = search_term)
        return search_results

    def update_hood(self, hood_name):
        self.hood_name = hood_name
        self.save()


class Neighboorhood(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15, choices=Priority, default="Informational")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls, healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Business(models.Model):
    logo = models.ImageField(upload_to='businesslogo/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name


class Health(models.Model):
    logo = models.ImageField(upload_to='health/')
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name


class Services(models.Model):
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    photo = models.ImageField(upload_to='profile/', blank = True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = HTMLField()
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='post/')
    post = HTMLField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
        blogs = cls.objects.filter(Q (username__username=search_term) | Q (neighbourhood__neighbourhood=search_term) | Q (title__icontains=search_term))
        return blogs


class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)