from django.db import models
from django.utils import timezone


type_choices = {
    "government": "Government",
    "private": "Private",
}

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=type_choices)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()
    contact = models.CharField(max_length=13, default='Not Updated')
    location = models.CharField(max_length=255, default='New Delhi')
    last_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

