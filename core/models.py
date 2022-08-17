from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField
# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.title
    def image_tag(self):
        x=f'<img src = "/media/{self.image}" style="width:40px;height:40px;border-radius:50%;">'
        return format_html(x)
    
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="cat_post")
    image = models.ImageField(upload_to="post")
    