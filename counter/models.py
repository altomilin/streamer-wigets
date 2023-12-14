from django.contrib.auth.models import User
from django.db import models


class WidgetCounter(models.Model):
    uuid = models.UUIDField()
    title = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Widget {self.uuid}: {self.title}"


class Counter(models.Model):
    label = models.CharField(max_length=200)
    value = models.IntegerField()
    default_increment = models.IntegerField(default=1)
    widget = models.ForeignKey(WidgetCounter, related_name="counters", on_delete=models.CASCADE)

    @property
    def user(self):
        return self.widget.user

    def __str__(self):
        return f"{self.label}: {self.value}"



