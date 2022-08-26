import graphene
from graphene_django import DjangoObjectType, DjangoListField
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery


class Query(UserQuery, MeQuery):
    pass


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    login = mutations.ObtainJSONWebToken.Field()
    verify_account = mutations.VerifyAccount.Field()

class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
