from django.contrib import admin

# Register your models here.
from passaggi.models import Type_Vehicle, User
@admin.register(Type_Vehicle)
class Type_VehicleAdmin(admin.ModelAdmin):
    filter = 'description'
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter =('email','admin','active')

