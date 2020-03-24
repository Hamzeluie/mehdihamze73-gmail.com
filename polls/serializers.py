from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from .models import Questions, Choice


class QuestionModelSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id',
                  'question_text',
                  'pub_date',)


# class ChoiceModelSerializer(serializers.HyperlinkedModelSerializer):
class ChoiceModelSerializer(ModelSerializer):
    # question = QuestionModelSerializer(many=True)

    class Meta:
        model = Choice
        fields = ('id',
                  'choice_text',
                  'vote',
                  'question',
                  )