from graphene_django.types import DjangoObjectType
import graphene

class Query(graphene.ObjectType):
    # Define your queries here
    name = graphene.String(default_value="Hello, GraphQL!")
    
schema = graphene.Schema(query=Query)