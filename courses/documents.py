from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import Course

courses_index = Index('courses_index')


courses_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
@courses_index.doc_type
class CourseDocument(Document):

    id = fields.IntegerField(attr='id')
    
    title = fields.TextField()
    description = fields.TextField()

    instructor = fields.IntegerField(attr='instructor_id')
    category = fields.IntegerField(attr='category_id')

    class Django:
        model = Course  # Link to the Course model
        # fields = [
        #     'price',
        #     'is_published',
        #     'created_at',
        #     'updated_at',
        #     'video',
        # ]
