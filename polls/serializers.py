from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from .models import Questions, Choice


class QuestionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = ('id',
                  'question_text',
                  'pub_date',)

    def create(self, validated_data):
        choices = validated_data.pop('choice_set')
        question = Questions.objects.create(**validated_data)
        for obj in choices:
            Choice.objects.create(question= question, **obj)
        return question


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