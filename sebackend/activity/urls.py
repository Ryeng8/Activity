from django.urls import path, include
# from rest_framework import routers, serializers, viewsets
from rest_framework import routers
from activity.views import ActivityTypeViewSet, ActivityViewSet, ActivityTimelineViewSet, ParticipantViewSet, CheckParticipantViewSet

router = routers.DefaultRouter()
router.register(r'activitytypes', ActivityTypeViewSet)
router.register(r'activitys', ActivityViewSet)
router.register(r'activitytimetines', ActivityTimelineViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'checkparticipants', CheckParticipantViewSet)

urlpatterns = [
    path("", include(router.urls))
]