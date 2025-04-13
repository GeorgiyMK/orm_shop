import configparser

from django.db import models
from django.db.models import ForeignKey


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.AutoField(primary_key=True) # Не обязательно ?
    model = models.CharField(max_length=50)
    year = models.DateField()
    color = models.CharField(max_length=30)
    mileage = models.IntegerField()
    volume = models.IntegerField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(max_length=20, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return f'{self.model}'


class Sale(models.Model):
    id = models.AutoField(primary_key=True)  # Не обязательно ?
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.client}, {self.car}'
