from django.urls import path
from core import views

urlpatterns = [
    path('',views.home,name="home"),
    path('blog/<slug:url>/',views.blog,name="blog"),
    path('category/<int:cat_id>/',views.category_post,name="category")
]

