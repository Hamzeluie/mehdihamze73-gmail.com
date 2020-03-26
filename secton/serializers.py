from rest_framework.serializers import ModelSerializer
from .models import Section, SectionGroup


class SectionModelSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('id',
                  'name',
                  'people_count',
                  'group',
                  )


class SectionGroupModelSerializer(ModelSerializer):
    class Meta:
        model = SectionGroup
        fields = ('id',
                  'section_name',
                  'is_active',
                  )