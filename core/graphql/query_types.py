from graphene_django import DjangoObjectType

from files.models import File


class FileType(DjangoObjectType):
    class Meta:
        model = File
        fields = ("lines_count",)
