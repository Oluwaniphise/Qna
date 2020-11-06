from django import forms
from django.forms import ModelForm
from .models import Question, Answer



class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'details', ]
    title = forms.CharField( label='Question_title',  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Question title'}))
    details = forms.CharField(label="Details",  widget=forms.Textarea(attrs={'class':'form-control', 'cols':20, 'rows':5, 'placeholder':'Talk more about your question...'}))
    
    

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body']
    body = forms.CharField(label='Answer Question',  widget=forms.Textarea(attrs={'class':'form-control,', 'cols':10, 'rows':5, 'placeholder':'Answer question'}))

    