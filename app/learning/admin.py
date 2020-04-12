from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from learning.models import LearningUnit, User

admin.site.register(LearningUnit)
admin.site.register(User, UserAdmin)
