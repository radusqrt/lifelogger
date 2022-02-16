import datetime

from django.db import models
from django.utils import timezone


class Sleep(models.Model):
    # Keys
    sleep_id = models.AutoField(primary_key=True)

    # Attributes
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    deep_period = models.IntegerField(null=True)
    rem_period = models.IntegerField(null=True)
    light_period = models.IntegerField(null=True)
    awake_period = models.IntegerField(null=True)

    def __str__(self):
        return "[Sleep: id: {0}, start_time: {1} end_time: {2} deep_period: {3} rem_period: {4} light_period: {5} awake_period: {6}]".format(self.sleep_id, self.start_time, self.end_time, self.deep_period, self.rem_period, self.light_period, self.awake_period)


class SymptomGroup(models.Model):
    # Keys
    symptom_group_id = models.AutoField(primary_key=True)

    # Attributes
    target_time = models.DateTimeField()
    has_ectopic_beats = models.BooleanField()
    has_dizziness = models.BooleanField()
    has_chest_pain = models.BooleanField()
    has_shortness_of_breath: models.BooleanField()

    def __str__(self):
        return "[SymptomGroup: id: {0}, target_time: {1}, has_ectopic_beats: {2}, has_dizziness: {3}, has_chest_pain: {4}, has_shortness_of_breath: {5}]".format(self.symptom_group_id, self.target_time, self.has_ectopic_beats, self.has_dizziness, self.has_chest_pain, self.has_shortness_of_breath)


class EventType(models.TextChoices):
    SLEEP = "SLEEP"
    SYMPTOM_GROUP = "SYMPTOM_GROUP"


class Event(models.Model):
    # Keys
    event_id = models.AutoField(primary_key=True)
    sleep = models.ForeignKey(
        Sleep, on_delete=models.CASCADE, null=True)
    symptom_group = models.ForeignKey(
        SymptomGroup, on_delete=models.CASCADE, null=True)

    # Attributes
    creation_time = models.DateTimeField()
    type = models.CharField(choices=EventType.choices, max_length=20,)

    def __str__(self) -> str:
        return "[Event: id: {0}, creation_time: {1}, type: {2}, sleep: {3}, symptom_group: {4}]".format(self.event_id, self.creation_time, self.type, self.sleep, self.symptom_group)

    class Meta:
        constraints = [models.CheckConstraint(
            name="$(app_label)s_%(class)s_type_valid", check=models.Q(type__in=EventType.values))]
