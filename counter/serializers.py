from django.contrib.auth.models import User
from rest_framework import serializers
from counter.models import Counter, WidgetCounter
from uuid import uuid4

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ["id", "label", "value", "default_increment", "widget", ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class WidgetCounterSerializer(serializers.ModelSerializer):
    counters = CounterSerializer(many=True, required=False)
    user = UserSerializer(
        read_only=True,
    )
    uuid = serializers.UUIDField(
        read_only=True
    )

    class Meta:
        model = WidgetCounter
        fields = ["id", "uuid", "title", "user", "counters"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['uuid'] = uuid4()
        return super().create(validated_data)
