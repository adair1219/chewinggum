from django.shortcuts import render

from django.views.generic import ListView, DetailView

from artical.models import Category, Post

# Create your views here.
# class Section2(ListView):
#     queryset = Category.get_all_category()
#     context_object_name = 'home'
#     template_name = 'home.html'

#     def get_context_date(self, **kwargs):
#         context = super().get_context_date(**kwargs)
#         posts_count = self.queryset.post_set.count()
#         latest_posts = Post.latest_post[:5]
#         context.update({
#             'posts_count': posts_count,
#             'latest_posts': latest_posts,
#         })
#         return context

# class Home(Section2):
#     pass

def home(request):
    if request.method == 'POST':
        dict = request.POST.values()
        with open('survey_date.txt', 'a', encoding='utf-8') as f:
            f.write('\r\n')
            f.write(str(list(dict)) + '\r\n')

    categories = Category.get_all_category()
    latest_posts = Post.latest_post()
    context = {
        'categories': categories,
        'latest_posts': latest_posts,
    }
    return render(request, 'home.html', context=context)