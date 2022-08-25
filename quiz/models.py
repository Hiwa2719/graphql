from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=255, default=_('New Quiz'))
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    SCALE = [
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    ]
    TYPE = [
        (0, _('Multiple Choice'))
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, related_name='questions')
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('type of question'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name=_('Active status'))

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answer')
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer text'))
    is_right = models.BooleanField(default=False)

