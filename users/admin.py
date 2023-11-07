from django.contrib import admin

from users.models import Address,  Profile

admin.site.register(Profile)
admin.site.register(Address)
