from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.




class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    value = models.IntegerField()
    registered = models.TimeField(auto_now_add=True)
    modified = models.TimeField(auto_now=True)
    date  = models.DateField(auto_now_add=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description) + ' - "' + str(self.type) + '" - ' + str(self.value)
