from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = "users"


class Good(models.Model):
    
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    unit = models.CharField(max_length=32)
    location = models.CharField(max_length=255)
    type_id = models.IntegerField()
    amount = models.IntegerField()
    alert = models.IntegerField()
    note = models.TextField()
    date = models.DateField()
    user_id = models.IntegerField()
    
    class Meta:
        db_table = "goods"
