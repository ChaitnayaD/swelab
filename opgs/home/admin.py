from django.contrib import admin
from home.models import student,company,alumni,Notification,Feedback, Personal_Notification, Application

# Register your models here.
admin.site.register(student)
admin.site.register(alumni)
admin.site.register(company)
admin.site.register(Notification)
admin.site.register(Feedback)
admin.site.register(Personal_Notification)
admin.site.register(Application)