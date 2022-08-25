import graphene

from graphene_django import DjangoObjectType

from .models import Book


class BooksType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(self, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)
