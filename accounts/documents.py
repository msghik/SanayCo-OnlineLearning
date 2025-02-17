from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import CustomUser

accounts_index = Index('accounts_index')


@registry.register_document
@accounts_index.doc_type
class CustomUserDocument(Document):

    id = fields.IntegerField(attr='id')
    username = fields.TextField()
    phone_number = fields.TextField()
    role = fields.TextField()
    full_name = fields.TextField()

    class Django:
        model = CustomUser

