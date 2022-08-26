import graphene
from django.shortcuts import get_object_or_404
from graphene_django import DjangoObjectType, DjangoListField
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
    all_quizzes = DjangoListField(QuizType)
    all_questions = DjangoListField(QuestionType)


class CategoryUpdate(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        category_id = graphene.Int(required=True)
        name = graphene.String(required=True)

    def mutate(self, info, category_id, name):
        category = get_object_or_404(Category, id=category_id)
        category.name = name
        category.save()
        return CategoryUpdate(category=category)


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        category = Category.objects.create(name=name)
        return CreateCategory(category=category)


class DeleteCategory(graphene.Mutation):
    category = graphene.Int()

    class Arguments:
        category_id = graphene.Int(required=True)

    def mutate(self, info, category_id):
        category = get_object_or_404(Category, id=category_id).delete()
        return CreateCategory(category=category_id)


class Mutation(graphene.ObjectType):
    update_category = CategoryUpdate.Field()
    create_category = CreateCategory.Field()
    delete_category = DeleteCategory.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
