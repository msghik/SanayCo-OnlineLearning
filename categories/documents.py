from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Category

categories_index = Index('categories_index')


@registry.register_document
@categories_index.doc_type
class CategoryDocument(Document):
    id = fields.IntegerField(attr='id')

    name = fields.TextField()
    description = fields.TextField()

    class Django:
        model = Category

