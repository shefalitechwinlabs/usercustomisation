from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendUser(AbstractUser):
    phone = models.PositiveBigIntegerField(null=True)
    #email = models.EmailField()

class Resume(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    file = models.FileField(null=True)
    image = models.ImageField(null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name