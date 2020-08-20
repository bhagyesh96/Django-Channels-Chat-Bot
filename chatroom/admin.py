from django.contrib import admin
from .models import MessageModel,UserStatusModel
admin.site.register(MessageModel)
admin.site.register(UserStatusModel)
# Register your models here.
