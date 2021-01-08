from rest_framework.serializers import ModelSerializer
from .models import Quiz, Question


class QuizSerializer(ModelSerializer):
    """Quiz serializer."""

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    """Question serializer."""

    class Meta:
        model = Question
        fields = '__all__'
