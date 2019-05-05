import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Dinner(models.Model):
    dinner_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date pulished')
    def __str__(self):
        return self.dinner_text
    def was_choiced_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Menu(models.Model):
    dinner = models.ForeignKey(Dinner, on_delete=models.CASCADE)
    menu_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.menu_text