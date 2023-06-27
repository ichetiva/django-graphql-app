import graphene


class FileInput(graphene.InputObjectType):
    file = graphene.String(required=True)
