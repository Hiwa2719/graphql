import graphene
from graphene_django import DjangoObjectType
from .models import Quiz, Answer, Category, Question


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = '__all__'


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = '__all__'


class Query(graphene.ObjectType):
    quiz = graphene.Field(QuizType)

    def resolve_quiz(self, info):
        return Quiz.objects.all().first()


schema = graphene.Schema(query=Query)
