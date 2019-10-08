from django.contrib import admin

from .models import Character, Author, Nature, Image
admin.site.register(Character)
admin.site.register(Author)
admin.site.register(Nature)
admin.site.register(Image)