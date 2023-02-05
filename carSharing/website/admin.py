from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'dob', 'gender')
    list_display_links = ('id', 'email', 'name')
    readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('date_joined', 'phone', 'name', 'gender')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class PublishRideAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pickup', 'drop', 'date', 'time', 'seats', 'price', 'phone')
    list_display_links = ('id', 'user', 'pickup', 'drop')
    search_fields = ('id', 'pickup', 'drop', 'date', 'time', 'seats', 'price')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(PublishRide, PublishRideAdmin)