from django.contrib import admin
from .models import Link, Vote

# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin): pass
# admin.site.register(Link,LinkAdmin)

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin): pass
# admin.site.register(Vore, VoteAdmin)
