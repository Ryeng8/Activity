from django.contrib import admin
from .models import Activity, ActivityType, ActivityTimeline, Participant, CheckParticipant


# Register your models here.
class ActivityTypeAdmin(admin.ModelAdmin):
    pass

class ActivityAdmin(admin.ModelAdmin):
    pass

class ActivityTimelineAdmin(admin.ModelAdmin):
    pass

class ParticipantAdmin(admin.ModelAdmin):
    pass

class CheckParticipantAdmin(admin.ModelAdmin):
    pass


admin.site.register(ActivityType, ActivityTypeAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityTimeline, ActivityTimelineAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(CheckParticipant, CheckParticipantAdmin)
