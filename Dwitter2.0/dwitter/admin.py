from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Dweet, Profile
# Register your models here.

admin.site.register(Dweet)
admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(Group)
