from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    phNumber = models.CharField(max_length=15, blank=False, null=False)
    Email = models.EmailField(max_length=15, blank=False, null=False, primary_key=True)
    password = models.CharField(max_length=15, blank=False, null=False)
    createdAt = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.Uname
