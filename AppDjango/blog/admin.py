from django.contrib import admin

# Register your models here.
from .models import General, Category, Tag, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Creamos el inline para el modelo Post
class PostInlineCategory(admin.StackedInline):
    model = Post
    max_num = 2

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    inlines = [
        PostInlineCategory
    ]

class PostInlineTag(admin.TabularInline):
    model = Post.tag.through
    max_num = 3

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    inlines = [
        PostInlineTag
    ]

admin.site.register(General)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)