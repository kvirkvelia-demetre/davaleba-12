from django.db import models

class User(models.Model):
    name = models.CharField()
    surname = models.CharField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField()
    surname = models.CharField()

    def __str__(self):
        return self.user.username

class Products(models.Model):
    comments = models.TextField()
    rate = models.IntegerField()

class Carts(models.Model):
    pass

class Payment(models.Model):
    pass

class Product(models.Model):
    pass