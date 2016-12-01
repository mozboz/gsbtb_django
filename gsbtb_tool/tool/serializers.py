from .models import Person, Project, Opportunity
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [field.name for field in Person._meta.get_fields()]

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [field.name for field in Project._meta.get_fields()]

class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opportunity
        fields = [field.name for field in Opportunity._meta.get_fields()]

