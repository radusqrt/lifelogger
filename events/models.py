import datetime

from django.db import models
from django.utils import timezone


class EventType(models.TextChoices):
    SPORT = "SPORT"
    SYMPTOM = "SYMPTOM"


class Event(models.Model):
    creation_time = models.DateTimeField()
    target_time = models.DateTimeField(null=True, blank=True, default=None)
    type = models.CharField(choices=EventType.choices, max_length=20)

    def __str__(self) -> str:
        return "Creation time: {0}, Target time: {1}, Type: {2}".format(self.creation_time, self.target_time, self.type)

    def was_created_recently(self) -> bool:
        return self.creation_time >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        constraints = [models.CheckConstraint(
            name="$(app_label)s_%(class)s_type_valid", check=models.Q(type__in=EventType.values))]
