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
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()


class Mutation(AuthMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
