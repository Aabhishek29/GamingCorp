from django.db import models


# Create your models here.

class CompanyGames(models.Model):
    GameName = models.CharField(max_length=30, blank=False, null=False)
    GameId = models.IntegerField(primary_key=True)
    createdAt = models.DateField(blank=False, null=False)
    updatedAt = models.DateField(blank=False, null=False)
    Url = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.GameName
