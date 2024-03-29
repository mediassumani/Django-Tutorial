import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model): # sublassing the models.Model class

    # each property represents a database field
    # each field is represented by an instance of the Field
    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published') # first argument is an optional for human readable

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # ForeignKey is used to defined a relationship with a different model
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text