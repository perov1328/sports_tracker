from django.contrib import admin
from exercise.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    """
    Админка для пользователей
    """
    list_display = ('name', 'exercise_type', 'difficulty_level', 'date_of_creation',)
    list_filter = ('exercise_type', 'difficulty_level',)
