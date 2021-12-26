from django.db import models


class Samples(models.Model):
    canister = models.IntegerField()
    label = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    initials = models.CharField(max_length=100)

    def __str__(self):
        return self.label
