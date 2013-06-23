import datetime
from haystack import indexes
from nerdeez_backend_app.models import University

class UniversityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.DateTimeField(model_attr='description')

    def get_model(self):
        return University

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(description__lte=datetime.datetime.now())