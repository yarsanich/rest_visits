from .models import Visit
from datetime import timedelta
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response


class VisitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start_date = serializers.DateTimeField(format='iso-8601', input_formats=['iso-8601'])
    end_date = serializers.DateTimeField(format='iso-8601', input_formats=['iso-8601'])

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        if validated_data['end_date'] - validated_data['start_date'] < timedelta(0,0):
            return Response("Start Date > End Date", status=status.HTTP_400_BAD_REQUEST)
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance