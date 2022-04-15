from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    details = models.CharField(max_length=100) 
    amount = models.IntegerField()
    image = models.CharField(max_length=2000, default='https://i.imgur.com/3cHAFsx.jpg')
    location = models.CharField(max_length=100) 
    available = models.BooleanField()
    #user?
    #user = models.ForeignKey(User, on_delete=models.CASCADE)


