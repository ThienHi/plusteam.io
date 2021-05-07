from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User



class Question(models.Model):
    question = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question

    class Meta:
        ordering=['id']
        db_table = 'question_hire'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=500)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

    class Meta:
        ordering=['-id']
        db_table = 'choice_hire'


class AccessibleChoice(models.Model):
    ACCESS_CODE_STATUS_CHOICE = [
        ('Active', 'Active'),
        ('Used', 'Used'),
        ('Inactive', 'Inactive'),
    ]
    access = models.CharField(max_length=8, null=False, unique=True)
    user = models.ForeignKey(User, related_name='access_code', null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=255)
    status = models.CharField(max_length=10, null=False, default='Active', choices=ACCESS_CODE_STATUS_CHOICE,)