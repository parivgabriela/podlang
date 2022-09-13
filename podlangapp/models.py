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

    def __init__(self, mail, username, name, birthdate):
        self.mail = mail
        self.username = username
        self.name = name
        self.birth_date = birthdate

    def name(self):
        return self.mail

    def name(self):
        return self.username

    def name(self):
        return self.name


class Language(models.Model):
    id = models.IntegerField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='ID')
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=100)

    def __init__(self, name, country) -> None:
        self.name = name
        self.country = country

    def name(self):
        return self.name

    def country(self):
        return self.country


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

    def __init__(self, name_field_audio, name_field_text, date_creation, id_user, id_language, rate):
        self.name_field_audio = name_field_audio
        self.name_field_text = name_field_text
        self.date_creation = date_creation
        self.id_user = id_user
        self.id_language = id_language
        self.rate = rate


    def name_field_audio(self):
        return self.name_field_audio

    def name_field_text(self):
        return self.name_field_text

    def date_creation(self):
        return self.date_creation

    def rate(self):
        return self.rate
