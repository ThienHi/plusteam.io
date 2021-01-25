from django.db import models
from django.utils import timezone

# Create your models here.

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

    # def __str__(self):
    #     return self.choice

    class Meta:
        ordering=['-id']
        db_table = 'choice_hire'
