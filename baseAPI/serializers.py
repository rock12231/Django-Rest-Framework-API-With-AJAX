from rest_framework import serializers
from baseAPI.models import Emp

class EmpSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, default='')
    position = serializers.CharField(max_length=100, default='')
    salary = serializers.CharField(max_length=100, default='')
    start_date = serializers.DateField()
    office = serializers.CharField(max_length=100, default='')
    extn = serializers.IntegerField(default='0')
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Emp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.office = validated_data.get('office', instance.office)
        instance.extn = validated_data.get('extn', instance.extn)
        instance.save()
        return instance