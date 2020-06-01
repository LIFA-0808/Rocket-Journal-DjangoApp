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
        fields = '__all__'
        # exclude = ['date_added']
        labels = {
            'item_description': _('Назначение'),
        }
        help_texts = {
            'item_description': _('Добавьте описание вашей записи'),
        }
        error_messages = {
            'item_description': {
                'max_length': _("Максимальная длинна поля должна не привышать 200 символов"),
            },
        }
        widgets = {
            'item_description': Textarea(attrs={'cols': 80, 'rows': 2}),
        }
