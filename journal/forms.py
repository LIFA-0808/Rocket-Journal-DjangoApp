from django.forms import ModelForm, Textarea
from .models import Topic, Record
from django.utils.translation import gettext_lazy as _


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'comment', 'file']

        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 2}),
        }
