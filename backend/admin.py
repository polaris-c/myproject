from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book_name', 'add_time',)

admin.site.register(Book, BookAdmin)

print('*** backend/admin is running! 中文测试***')
