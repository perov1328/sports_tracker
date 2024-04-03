from django.urls import path
from exercise.apps import ExerciseConfig
from exercise.api_views import (ExerciseListAPIView, ExerciseCreateAPIView, ExerciseRetrieveAPIView,
                                ExerciseUpdateAPIView, ExerciseDeleteAPIView)


app_name = ExerciseConfig.name

urlpatterns = [
    path('', ExerciseListAPIView.as_view(), name='exercise_detail'),
    path('create/', ExerciseCreateAPIView.as_view(), name='exercise_create'),
    path('<int:pk>/', ExerciseRetrieveAPIView.as_view(), name='exercise_delete'),
    path('update/<int:pk>/', ExerciseUpdateAPIView.as_view(), name='exercise_update'),
    path('delete/<int:pk>/', ExerciseDeleteAPIView.as_view(), name='exercise_update')
]
