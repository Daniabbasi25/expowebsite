from tkinter import CASCADE
from turtle import color
from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User
from django.forms import SlugField
from .helpers import *
# Create your models here.


class themecolor(models.Model):
    ThemeColor = models.CharField(max_length=300)


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=300, null=True, blank=True)
    profession = models.CharField(max_length=300, null=True, blank=True)
    emiall = models.EmailField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    color = models.CharField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.user.username)
        super(Profil, self).save(*args, **kwargs)

    def get_full_name(self):
        if not self.Name:
            return 'Your Name'
        return ' '.join([self.Name])

    def get_full_Profesion(self):
        if not self.profession:
            return 'Your Profesion'
        return ' '.join([self.profession])

    def datasae(self, n, p, e, no, img):
        self.Name = n
        self.profession = p
        self.emiall = e
        self.number = no
        if img:
            self.image = img


class Links(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    link = models.CharField(max_length=300)

