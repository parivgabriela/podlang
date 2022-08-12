from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')
    mail = models.CharField(max_length=128)
    username =models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    birth_date =models.CharField(max_length=128)


class Language(models.Model):
    id = models.IntegerField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=100)


class Podlang(models.Model):
    id = models.IntegerField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')
    name_field_audio = models.CharField(max_length=128)
    name_field_text = models.CharField(max_length=128)
    date_creation = models.DateField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    rate = models.CharField(max_length=5)

