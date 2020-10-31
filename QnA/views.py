from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .models import Question
from django.contrib.auth.models import User



def home(request):
    questions = Question.objects.all()
    # user = Question.objects.get(user)

    context = { 'questions':questions }
    
    return render(request, 'index.html', context)


@login_required
def ask(request):
    # instance = Question.objects.filter(user=request.user)

    form = QuestionForm
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}

    return render(request, 'ask.html', context)



def question_details(request,slug):
    q = get_object_or_404(Question, slug=slug)


    context = {'q':q}
    return render(request, 'details.html', context)

