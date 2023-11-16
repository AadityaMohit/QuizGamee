from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    stream=models.CharField(max_length=10)

    
    def __str__(self):
        return self.name
    
    
class Form1(models.Model):
    answer1=models.CharField(max_length=1000)
    answer2=models.CharField(max_length=1000)
    answer3=models.CharField(max_length=1000)
    
class Form2(models.Model):
    answer4=models.CharField(max_length=1000)
    answer5=models.CharField(max_length=1000)
    answer6=models.CharField(max_length=1000)
class Form3(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField(max_length=1000)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    