from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from exercise.models import Exercise
from exercise.serializers import ExerciseSerializer, ExerciseCreateSerializer
from exercise.paginators import ExercisePagination
from exercise.filters import ExerciseFilter
from rest_framework.permissions import IsAuthenticated


class ExerciseListAPIView(ListAPIView):
    """
    Контроллер для просмотра всех сущностей модели Упражнения
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ExercisePagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExerciseFilter


class ExerciseCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности модели Упражнения
    """
    serializer_class = ExerciseCreateSerializer
    permission_classes = [IsAuthenticated]


class ExerciseRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотора конкретной сущности модели Упражнения
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]


class ExerciseUpdateAPIView(UpdateAPIView):
    """
    Класс для обновления сущности модели Упражнения
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseCreateSerializer
    permission_classes = [IsAuthenticated]


class ExerciseDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Упражнения
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
