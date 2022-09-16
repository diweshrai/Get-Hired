from django.contrib import admin

from dashboard.models import Notes
from dashboard.models import s_prof
from dashboard.models import Resume
from dashboard.models import Appnow
from . models import *

# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)
admin.site.register(vac)
admin.site.register(s_prof)
admin.site.register(Resume)
admin.site.register(Appnow)

class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city',  'my_file']

