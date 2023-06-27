import threading

import graphene
from graphql_auth import mutations
from graphql_jwt.decorators import login_required

from .mutation_inputs import FileInput
from files.models import File
from files.services import handle_file


class UploadFile(graphene.Mutation):
    class Arguments:
        input = FileInput(required=True)

    id = graphene.ID()

    def mutate(self, info, input):
        file = File()
        file.save()
        thread = threading.Thread(target=handle_file, args=(file.id, input.file))
        thread.start()
        return UploadFile(id=file.id)


class Mutation(graphene.ObjectType):
    # Authentication
    user_creation = mutations.Register.Field()
    user_verification = mutations.VerifyAccount.Field()
    user_authentication = mutations.ObtainJSONWebToken.Field()

    # Files
    upload_file = UploadFile.Field()
