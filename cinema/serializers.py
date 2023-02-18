from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    # used pk instead of id because it requires flake-variables-names
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=63)
    description = serializers.CharField(max_length=255)
    duration = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            "title", instance.title
        )
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get(
            "duration", instance.duration
        )
        instance.save()
        return instance
