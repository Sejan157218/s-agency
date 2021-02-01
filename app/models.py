from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    subject = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    facebook = models.CharField(max_length=1000)
    linkedin = models.CharField(max_length=1000)
    skype = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to="app/images",default="")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    facebook = models.CharField(max_length=1000)
    linkedin = models.CharField(max_length=1000)
    skype = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to="app/images",default="")

    def __str__(self):
        return self.name

class Frontadmin(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    facebook = models.CharField(max_length=1000)
    linkedin = models.CharField(max_length=1000)
    skype = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=1000)
    date = models.DateField()
    image = models.ImageField(upload_to="app/images",default="")

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=20)

    image = models.ImageField(upload_to="portfolio/images",default="")

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.title  


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=20)

    image = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title
   

class Testomonial(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=20)

    image = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title
   