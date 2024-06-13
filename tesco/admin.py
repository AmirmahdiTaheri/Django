from django.contrib import admin
from tesco.models import Category, Txt , about , contact 

# Register your models here.
admin.site.register(Category)
admin.site.register(Txt)
admin.site.register(about)
admin.site.register(contact)