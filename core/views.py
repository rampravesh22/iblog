from django.shortcuts import render
from core.models import Post,Category
# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    catetory = Category.objects.all()
    context={
        'posts':posts,
        'category':catetory
    }
    return render(request, "core/home.html", context)


def blog(request, url):
    post = Post.objects.get(post_id=url)
    catetory = Category.objects.all()
    context={
        'post':post,
        'category':catetory
    }
    return render(request, "core/post.html", context)


def category_post(request,cat_id):
    cates = Category.objects.get(cat_id=cat_id)
    category = Category.objects.all()
    
    context = {
        'cates':cates,
        'category':category
    }
    return render(request, "core/category_post.html", context)