from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14)
    #Важное поле для middlewares
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER)
    club = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.age < 7:
            self.club = 'Вы сликом малы приходите на следующий год'
        elif 7 <= self.age < 12:
            self.club = 'Детский клуб'
        elif 12 <= self.age < 18:
            self.club = 'Подростковый клуб'
        elif 18 <= self.age <= 60:
            self.club = 'Взрослый клуб'
        else:
            self.club = 'Ваш возраст больше 60 извните вы не проходите'
        
        super().save(*args, **kwargs)