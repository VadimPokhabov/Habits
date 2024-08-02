from datetime import timedelta

from rest_framework.exceptions import ValidationError


class EliminationChoiceValidator:
    """
    Validator, который исключает возможность выбора, связанного с привычкой,
    и вознаграждения одновременно
    """

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.reward):
            raise ValidationError(
                "Не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки."
            )


class TimeDurationValidator:
    """
    Validator, который проверяет, находится ли значение time_duration в
    пределах интервала в 120 секунд
    """

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(seconds=120)
        if (habit.get(self.duration)
                and habit.get(self.duration) > max_duration):
            raise ValidationError(
                f"Длительность выполнения привычки "
                f"не может превышать {max_duration}."
            )


class CombinationValidator:
    """
    Validator подтверждает, что только привычки с признаками
    приятной привычки могут относиться к родственным привычкам
    """

    def __init__(self, related_habit, pleasant_habit_sign):
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if (habit.get(self.related_habit)
                and not habit.get(self.pleasant_habit_sign)):
            raise ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class PeriodicityValidator:
    """
    Проверяет выполнение этой привычки реже, чем раз в 7 дней
    """

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, habit):
        if habit.get(self.periodicity) and habit.get(self.periodicity) > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


class AbsenceValidator:
    """
    Validator который проверяет, что приятная привычка
    не может иметь вознаграждения или связанной с ней привычки
    """

    def __init__(self, reward, related_habit, pleasant_habit_sign):
        self.reward = reward
        self.related_habit = related_habit
        self.pleasant_habit_sign = pleasant_habit_sign

    def __call__(self, habit):
        if habit.get(self.pleasant_habit_sign) and (
            habit.get(self.reward) or habit.get(self.related_habit)
        ):
            raise ValidationError(
                "Приятная привычка не может иметь вознаграждение или связанную привычку."
            )
