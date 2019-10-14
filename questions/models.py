from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=1000)
    content_a = models.CharField(max_length=1000)
    content_b = models.CharField(max_length=1000)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()
