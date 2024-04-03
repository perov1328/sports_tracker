from rest_framework.pagination import PageNumberPagination


class ExercisePagination(PageNumberPagination):
    """
    Пагинатор для вывода 10 Упражнений на каждой странице
    """
    page_size = 10
