from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, AnswerForm, UserUpdateForm, ProfileUpdateForm
from .models import Question, Answer
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages


def home(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 3)
    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    user = request.user
    context = {
         'questions':page_obj, 
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
   

    form = AnswerForm(initial={'question':q, 'user':user})

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
        
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
    
    


@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    
    user = request.user

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,  request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    answers = Answer.objects.filter(user=request.user)
    questions = Question.objects.filter(user=request.user)

    context  = {'user':user, 
    'questions':questions,
     'answers':answers, 
     'p_form':p_form, 'u_form':u_form
     }
    return render(request, 'profile.html', context)



