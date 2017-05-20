from .models import Visit
from rest_framework import serializers

class VisitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start_date = serializers.DateTimeField(format='iso-8601', input_formats=['iso-8601'])
    end_date = serializers.DateTimeField(format='iso-8601', input_formats=['iso-8601'])

    def validate(self, data):
        """
        Check thath the start is before the stop
        """

        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("start_date must be before end_date")
        return data

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance