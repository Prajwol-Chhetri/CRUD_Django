from django.contrib import admin
from blogs.models import Author, Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/main.css',)
        }
        js = ('js/blog.js',)


admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)