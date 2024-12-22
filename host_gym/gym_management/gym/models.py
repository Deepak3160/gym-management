from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class ClientDetails(models.Model):
    client_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=7)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    type = models.CharField(max_length=20)

class TrainerDetails(models.Model):
    trainer_id = models.CharField(max_length=10, primary_key=True)
    trainer_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=10)
    trainer_address = models.CharField(max_length=30)
    trainer_type = models.CharField(max_length=30)
