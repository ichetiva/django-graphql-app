import graphene

from graphql_auth.schema import UserQuery, MeQuery

from .query_types import FileType
from files.models import File


class Query(UserQuery, MeQuery, graphene.ObjectType):
    file = graphene.Field(FileType, id=graphene.ID(required=True))

    def resolve_file(self, info, id):
        return File.objects.get(id=id)
