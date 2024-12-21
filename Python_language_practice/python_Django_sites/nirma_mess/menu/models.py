from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    food_type = models.CharField(
        max_length=9,
        choices=[
            ('B', 'Breakfast'),
            ('L', 'Lunch'),
            ('S', 'Supper'),
            ('D', 'Dinner')
        ],
        default='breakfast',
    )
    description = models.TextField(help_text='Add comma seperated dishes')
    formed_date = models.DateField(auto_now_add=True)
    formed_time = models.TimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    jain = models.BooleanField(default=True)
    feast = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.manager

    def __str__(self):
        return self.food_type + '(' + str(self.formed_date) + ')'
