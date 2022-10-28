from django.db import models

# Create your models here.

class Motorcicle(models.Model):
    name = models.CharField('Motorcicle name', max_length=100)
    image = models.ImageField('ImageField', upload_to='media')
    price = models.IntegerField('Price')
    characteristics = models.TextField('characteristics', max_length=10000)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Motorcicle'
        verbose_name_plural = 'Motorcicles'
        ordering = ['name']

class Albert(models.Model):
    name = models.CharField('About Albert', max_length=100)
    image = models.ImageField('ImageField', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Albert'
        verbose_name_plural = 'Alberts'
        ordering = ['name']
