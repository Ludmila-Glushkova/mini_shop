from django import forms
from django.forms import RadioSelect

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating')
        labels = {
            'text': 'Текст комментария',
        }
        widgets = {
            'rating': RadioSelect(
                choices=[
                    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
                ]
            ),
        }
        help_texts = {
            'text': 'Текст комментария',
        }
