import datetime
from rest_framework.serializers import ValidationError


class NumberOfApproaches(ValidationError):
    """
    Валидатор на проверку количество подходов, строго больше нуля
    """
    def __init__(self, approaches):
        self.approaches = approaches

    def __call__(self, value):
        approaches_count = value.get(self.approaches)
        if approaches_count <= 0:
            raise ValidationError("Количество повторов должно быть больше нуля.")


class NumberOfRepetitions(ValidationError):
    """
    Валидатор на проверку количества повторений, строго больше нуля
    """
    def __init__(self, repetition):
        self.repetition = repetition

    def __call__(self, value):
        repetitions_count = value.get(self.repetition)
        if repetitions_count <= 0:
            raise ValidationError("Количество повторений должно быть больше нуля.")


class TimeCheck(ValidationError):
    """
    Валидатор на проверку того что время на выполнение упражнения больше нуля
    """
    def __init__(self, duration):
        self.duration = duration

    def __call__(self, value):
        min_time = datetime.time(0, 0, 0)
        time = value.get(self.duration)
        if time <= min_time:
            raise ValidationError("Время на выполнение упражнения должно быть больше нуля.")
