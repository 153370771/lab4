change
from django.contrib import admin

# Register your models here.
from blog.models import book,author

#class authorAdmin(admin):
 #   list_display('authorid','name','age','country')
 #   search_fields=('authorid','name')
admin.site.register(book)
admin.site.register(author)