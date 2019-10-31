from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.db.models.aggregates import Count
from django.views.generic import ListView, DetailView

from .models import Category, Tag, Post

# Create your views here.

def get_objects_field(field, _model, id=1):
    field_name = field
    obj = _model.objects.get(id=id)
    field_object = _model._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)
    return field_value

class CategoryView(ListView):
    model = Post
    context_object_name = 'cate_posts'
    template_name = 'blog.html'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


def PostDetail(request, post_id):
    query = Post.objects.get(id=post_id)
    context = {
        'post': query,
    }
    return render(request, 'detail.html', context=context)

        
    