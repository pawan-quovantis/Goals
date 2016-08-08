from django.contrib import admin
from models import *


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'state_province', 'website')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')
    list_filter = ('publication_date',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher, PublisherAdmin)