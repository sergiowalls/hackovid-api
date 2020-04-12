from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from learning.models import LearningUnit, User, Class

admin.site.register(LearningUnit,Class)
admin.site.register(User, UserAdmin)
