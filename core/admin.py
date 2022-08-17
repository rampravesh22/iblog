from django.contrib import admin
from core.models import Post,Category
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'content', 'url', 'category', 'image', )
    search_fields = ["title"]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_id','image_tag', 'title', 'description', 'url', 'add_date', )
    
