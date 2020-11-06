from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer, Like
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect



def home(request):
    questions = Question.objects.all()
    user = request.user
 

    context = {
         'questions':questions, 
         'user':user
   
    }
    
    return render(request, 'index.html', context)


@login_required
def ask(request):
    user = request.user
   
    
    questions = Question.objects.all()

    form = QuestionForm(initial={'user':user,
    #  'question':question
     })
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form, 'questions':questions}

    return render(request, 'ask.html', context)


@login_required
def question_details(request,slug):
    q = get_object_or_404(Question, slug=slug)
    # answers = Answer.objects.all()


    context = {'q':q, 
    # 'answers':answers
     }
    return render(request, 'details.html', context)

@login_required
def answer_form(request):
    user = request.user
    # question = Question.objects.get(id=question_id)
    
    form = AnswerForm(initial={'user':user})
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = { 'form':form }
    return render(request, 'answer-form.html', context)



def like_question(request):
    user = request.user
    question = get_object_or_404(Question, id=request.POST.get('question_id'))


    if user in question.likes.all():
        question.likes.remove(user)
    else:
        question.likes.add(user)
      

    return HttpResponseRedirect(reverse('home'))
    
    