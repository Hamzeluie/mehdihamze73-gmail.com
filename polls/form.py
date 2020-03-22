from django import forms
from .models import Questions, Choice


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'question_text',
        ]


class ChoiceModelForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'vote',
        ]
