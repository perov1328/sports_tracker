from django_filters import rest_framework as filters
from exercise.models import Exercise


class ExerciseFilter(filters.FilterSet):
    exercise_type = filters.CharFilter(field_name='exercise_type', lookup_expr='exact')
    difficulty_level = filters.CharFilter(field_name='difficulty_level', lookup_expr='exact')

    class Meta:
        model = Exercise
        fields = ['exercise_type', 'difficulty_level']
