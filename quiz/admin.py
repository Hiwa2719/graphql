from django.contrib import admin
from .models import Answer, Question, Quiz, Category


admin.site.register([Answer, Question, Quiz, Category])
