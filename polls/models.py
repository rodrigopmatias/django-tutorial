from django.db import models


class Question(models.Model):
    question_text = models.CharField("Question", max_length=200)
    pub_date = models.DateTimeField("date_published", auto_now=False, auto_now_add=False, null=True)


class Choice(models.Model):
    question = models.ForeignKey("polls.Question", on_delete=models.CASCADE)
    choice_text = models.CharField("Choice", max_length=200)
    votes = models.IntegerField("Votes", default=0)