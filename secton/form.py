from django import forms
from .models import *


class SectionGroupFromModel(forms.ModelForm):
    class Meta:
        model = SectionGroup
        fields = [
            'section_name',
            'is_active',
                  ]


class SectionFromModel(forms.ModelForm):
    class Meta:
        model = Section
        fields = [
            'name',
            'people_count',
        ]
