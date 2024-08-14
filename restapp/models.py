from django.db import models
from solo.models import SingletonModel

# Create your models here.
class SlidItem(models.Model):
    menu_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    btn_one = models.URLField()
    btn_two = models.URLField()
    image = models.ImageField(upload_to='slider/', default="slider/slide.jpg")
    def __str__(self):
        return self.menu_name
    
class Slide(SingletonModel):
    name = models.CharField(max_length=50)
    slide_item = models.ManyToManyField(SlidItem)

class Booking(models.Model):
    TYPE_CHOICE=(
        ('Breakfast', 'breakfast: 8AM to 10AM'),
        ('Lunch', 'lunch: 12PM to 02AM'),
        ('Dinner', 'dinner: 8PM to 11AM'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    number_of_pepole = models.IntegerField()
    date = models.DateField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICE, default='Brackfast')
    message = models.TextField()
    def __str__(self):
        return self.name