from django.db import models

class Question(models.Model):
    """
    A model representing a poll question.
    Attributes:
        question_text (CharField): The text of the question.
        pub_date (DateTimeField): The date and time when the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    """
    Represents a choice for a question in a poll.
    Attributes:
        question (ForeignKey): The question this choice is associated with.
        choice_text (CharField): The text of the choice.
        votes (IntegerField): The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)