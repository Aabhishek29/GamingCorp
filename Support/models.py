from django.db import models


# Create your models here.

class FeedBack(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    email = models.EmailField(blank=False, null=False)

    game_choice = [
        ('FirstGame', 'firstgame')
    ]

    GameName = models.CharField(
        max_length=50,
        blank=False, null=False,
        choices=game_choice
    )

    report_category = [
        ('Bug', 'bug'),
        ('Normal Feed', 'normal feed'),
        ('Query', 'query'),
        ('Report', 'report'),
        ('Hacker', 'hacker')
    ]

    reportType = models.CharField(max_length=15, blank=False, null=False, choices=report_category)

    comment = models.TextField(max_length=150, blank=False, null=False)

    reportId = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return self.name
