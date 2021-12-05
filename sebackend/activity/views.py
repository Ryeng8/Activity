from rest_framework import viewsets
from .models import ActivityType, Activity, ActivityTimeline, Participant, CheckParticipant

from .serializer import ActivityTypeSerializer, ActivitySerializer, ActivityTimelineSerializer, ParticipantSerializer, CheckParticipantSerializer

# Create your views here.

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityTimelineViewSet(viewsets.ModelViewSet):
    queryset = ActivityTimeline.objects.all()
    serializer_class = ActivityTimelineSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class CheckParticipantViewSet(viewsets.ModelViewSet):
    queryset = CheckParticipant.objects.all()
    serializer_class = CheckParticipantSerializer
