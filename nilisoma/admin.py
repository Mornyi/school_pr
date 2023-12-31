from django.contrib import admin

from .models import Profile, Record

from django.contrib.auth.models import User, Group

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

admin.site.register(Record)

