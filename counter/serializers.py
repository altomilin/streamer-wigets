from rest_framework import serializers
from counter.models import Counter, WidgetCounter


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ["id", "label", "value", "default_increment", "widget", ]


class WidgetCounterSerializer(serializers.ModelSerializer):
    counters = CounterSerializer(many=True, required=False)

    class Meta:
        model = WidgetCounter
        fields = ["id", "uuid", "title", "user", "counters"]


