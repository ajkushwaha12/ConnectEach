from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follower)
