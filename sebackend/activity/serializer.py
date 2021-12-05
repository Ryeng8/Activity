from rest_framework import serializers
from .models import ActivityType,  Activity, ActivityTimeline, Participant, CheckParticipant

class ActivityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityType
        fields =('id', 'title', 'description')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields =('id', 'title', 'description', 'activity_type', 'is_published', 'created_at')

class ActivityTimelineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityTimeline
        fields =('id', 'activity', 'start_datetime', 'end_datetime', 'description', 'lecturer')

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields =('id', 'activity', 'user', 'created_at')

class CheckParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckParticipant
        fields =('id', 'activity', 'user', 'created_at')