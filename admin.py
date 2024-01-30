from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(SubjectMaster)
admin.site.register(TopicMaster)
admin.site.register(QuestionsBank)
admin.site.register(SubjectDetail)
admin.site.register(Student_review)
admin.site.register(Leaderboard)
admin.site.register(UserProfile)



