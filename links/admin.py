from django.contrib import admin
from .models import Link, Vote, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin): pass
# admin.site.register(Link,LinkAdmin)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin): pass
# admin.site.register(Vore, VoteAdmin)

# class ProfileInLine(admin.StackedInLine):
# 	model = Profile
# 	can_delete = False

# @admin.register(get_user_model)
# class ProfileAdmin(UserAdmin):
# 	inlines = (ProfileInLine,)