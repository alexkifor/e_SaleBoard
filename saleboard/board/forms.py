from django.forms import ModelForm

from board.models import Bd


class BdForm(ModelForm):
    class Meta:
        model = Bd
        fields = ('title', 'content', 'price', 'rubric')
