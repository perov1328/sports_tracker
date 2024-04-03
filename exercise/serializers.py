from rest_framework import serializers
from exercise.models import Exercise
from exercise.validators import NumberOfApproaches, NumberOfRepetitions, TimeCheck


class ExerciseCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания модели Упражнения
    """
    class Meta:
        model = Exercise
        fields = ('name', 'description', 'exercise_type', 'difficulty_level',
                  'duration', 'approaches', 'repetition',)
        validators = [
            NumberOfApproaches(approaches='approaches'),
            NumberOfRepetitions(repetition='repetition'),
            TimeCheck(duration='duration')
        ]


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода модели Упражнения для Пользователя
    """
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'exercise_type',
                  'difficulty_level', 'duration', 'approaches', 'repetition',)
