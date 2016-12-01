from django.http import HttpResponse
from .models import Person, Project, Opportunity
from rest_framework import viewsets
from .serializers import PersonSerializer, ProjectSerializer, OpportunitySerializer


def index(request):
    return HttpResponse("Hello, world. You're at the tool index.")


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
