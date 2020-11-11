from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator



def home(request):
    questions = Question.objects.all()
    user = request.user
    context = {
         'questions':questions, 
         'user':user,
         
   
    }

    
    return render(request, 'index.html', context)


@login_required
def ask(request):
    user = request.user
    
    
    
    form = QuestionForm(initial={'user':user})
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

   
    context = {'form':form, }

    return render(request, 'ask.html', context)


@login_required
def question_details(request, slug, question_id):
    q = get_object_or_404(Question, slug=slug, id=question_id)
    
    context = {'q':q, 
    # 'answers':answers
     }
    return render(request, 'details.html', context)



@login_required
def answer_form(request, question_id, slug):
    form = AnswerForm()
    user = request.user
    q = get_object_or_404(Question, id=question_id, slug=slug)
    
    form = AnswerForm(initial={'question':q})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = { 'form':form, 
    'q':q  
    }
    return render(request, 'answer-form.html', context)



def like_question(request):
    user = request.user
    question = get_object_or_404(Question, id=request.POST.get('question_id'))


    if user in question.likes.all():
        question.likes.remove(user)
    else:
        question.likes.add(user)
      

    return HttpResponseRedirect(reverse('home'))
    
    