from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    name = models.CharField(max_length=20,unique=True)
    detail = models.TextField()
    def __str__(self):
        return self.name
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=20)
    locaton = models.CharField(max_length=20)
    #images = models.ImageField(null=True,blank=True)
    detail = models.TextField()

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=15,unique=True)
    address = models.CharField(max_length=100)
    detail = models.TextField()
    rating = models.IntegerField()
    ranking = models.IntegerField(unique=True)
    branches = models.ManyToManyField(Branch)
    #images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Placement(models.Model):
    college_id=models.ForeignKey(College)
    company_id=models.ForeignKey(Company)
    students_placed = models.IntegerField()
    lpa = models.IntegerField()


class Question(models.Model):
    name = models.CharField(max_length=20)
    detail = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Answer(models.Model):
    detail = models.TextField()
    rating = models.IntegerField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.question
