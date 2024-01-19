from django.db import models

class users(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.TextField(max_length=80)
    password = models.TextField(max_length=20)
    verified = models.IntegerField(max_length=1)
    code = models.IntegerField(max_length=8)
