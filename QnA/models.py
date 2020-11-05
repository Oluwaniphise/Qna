from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Question(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return f'{self.title} - {self.user}'

    class Meta:
        ordering = ['-created',]


    @property
    def num_of_likes(self):
        return self.likes.all().count() 

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.CharField(max_length=20, choices=LIKE_CHOICES)

    def __str__(self):
        return self.question



def pre_save_question_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)

    exists = Question.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    else:
        instance.slug = slug



pre_save.connect(pre_save_question_receiver, sender=Question)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    def __str__(self):
        return '%s - %s' % (self.question.title, self.user)