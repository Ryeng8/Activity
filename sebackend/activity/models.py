from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ActivityType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255,blank=True, null=True)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ActivityTimeline(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    lecturer = models.CharField(max_length=50, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=False, null=False)
    end_datetime = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.activity.title



class Participant(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, editable=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity


class CheckParticipant(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, editable=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity

