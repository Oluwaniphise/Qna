from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Question(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name='questions')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



def pre_save_question_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)

    exists = Question.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    else:
        instance.slug = slug



pre_save.connect(pre_save_question_receiver, sender=Question)