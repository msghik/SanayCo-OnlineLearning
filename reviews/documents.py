from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Review

reviews_index = Index('reviews_index')



@registry.register_document
@reviews_index.doc_type
class ReviewDocument(Document):

    id = fields.IntegerField(attr='id')
    rating = fields.IntegerField()
    content = fields.TextField()
    
    user = fields.IntegerField(attr='user_id')
    course = fields.IntegerField(attr='course_id')

    class Django:
        model = Review
        # fields = [
        #     'created_at',
        # ]
