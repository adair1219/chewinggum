from django.shortcuts import render

from .models import Answer
# Create your views here.

def Survey(request):
    answers = Answer.objects.all()
    context = {
       'answers': answers,
    } 
    return render(request, 'survey.html', context)
