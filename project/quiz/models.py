from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import User


class Question(models.Model):
    """Question representation."""

    TEXT_ANSWER = 'TEXT_ANSWER'
    CHOICE_WITH_ONE_ANSWER = 'CHOICE_WITH_ONE_ANSWER'
    CHOICE_WITH_MANY_ANSWER = 'CHOICE_WITH_MANY_ANSWERS'

    TYPE_CHOICES = (
        (TEXT_ANSWER, 'Text answer'),
        (CHOICE_WITH_ONE_ANSWER, 'With one answer'),
        (CHOICE_WITH_MANY_ANSWER, 'With many answers'),
    )

    question = models.TextField()
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default=TEXT_ANSWER,
    )
    answers = JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quiz__questions'
        indexes = (
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.question


class Quiz(models.Model):
    """Quiz representation."""

    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    questions = models.ManyToManyField(Question, related_name='quiz')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quiz__quiz'
        verbose_name_plural = 'Quiz'
        indexes = (
            models.Index(fields=['title']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.title


class Answer(models.Model):
    """Answer representation."""

    answers = JSONField(encoder=DjangoJSONEncoder, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quiz__answers'
        indexes = (
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.question.question
