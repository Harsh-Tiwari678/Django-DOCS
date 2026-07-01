from django.db import models
from django.utils import timezone #forshowing the time we need this 

# Create your models here.

class StudentData(models.Model):
    STUDENT_GENDER = [
        ('ML' , 'MALE'),
        ('FM' , 'FEMALE'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='student/')
    date =  models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=STUDENT_GENDER)
    def __str__(self):
        return self.name





