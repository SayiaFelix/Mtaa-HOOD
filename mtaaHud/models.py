from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Hood(models.Model):
    hood_name = models.CharField(max_length = 100)
    hood_photo = models.ImageField(upload_to='hood/')
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

class Information(models.Model):
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    info_photo = models.ImageField(upload_to='info/')
    title = models.CharField(max_length=100)
    information = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title

class Business(models.Model):
    b_photo = models.ImageField(upload_to='bussiness/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls, healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Health(models.Model):
    photo = models.ImageField(upload_to='health/')
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name


class Security(models.Model):
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to='profiles/',null=True)
    contact = models.CharField(max_length=12)
    email = models.EmailField(null=True)
    bio = HTMLField(null=True)
    neighbourhood = models.ForeignKey(Hood, on_delete=models.CASCADE,null=True)
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)

  
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return profile

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    def delete_profile(self):
         self.delete()

    def save_profile(self):
        self.save()

# class Profile(models.Model):
#     p_photo = models.ImageField(upload_to='profile/', blank = True)
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     contact = models.CharField(max_length=12)
#     email = models.EmailField()
#     bio = HTMLField()
#    


#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#         post_save.connect(create_user_profile, sender=User)

#     @receiver(post_save, sender=User)
#     def update_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#         instance.profile.save()

#     @classmethod
#     def get_profile(cls):
#         profile = Profile.objects.all()
#         return profile

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='post/')
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