import datetime

from django.db import models
from django.utils import timezone


class EventType(models.TextChoices):
    SPORT = "SLEEP"


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField()
    type = models.CharField(choices=EventType.choices, max_length=20,)

    def __str__(self) -> str:
        return "Creation time: {0}, Type: {1}".format(self.creation_time, self.type)

    class Meta:
        constraints = [models.CheckConstraint(
            name="$(app_label)s_%(class)s_type_valid", check=models.Q(type__in=EventType.values))]


class Sleep(models.Model):
    sleep_id = models.AutoField(primary_key=True)
    event = models.OneToOneField(
        Event, on_delete=models.CASCADE)

    # Attributes
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    deep_period = models.IntegerField(null=True)
    rem_period = models.IntegerField(null=True)
    light_period = models.IntegerField(null=True)
    awake_period = models.IntegerField(null=True)

    def __str__(self):
        return "[Sleep: id: {0} event: {1} start_time: {2} end_time: {3} deep_period: {4} rem_period: {5} light_period: {6} awake_period: {7}]".format(self.sleep_id, self.event, self.start_time, self.end_time, self.deep_period, self.rem_period, self.light_period, self.awake_period)
