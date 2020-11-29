from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from PIL import Image

class Question(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.user)
    class Meta:
        ordering = ['-created',]


   
    def num_of_likes(self):
        return self.likes.all().count() 


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers_que", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    answer_likes = models.ManyToManyField(User, related_name='answer_likes', blank=True)

    # def __str__(self):
    #     return self.question.title





def pre_save_question_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)

    exists = Question.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    else:
        instance.slug = slug



pre_save.connect(pre_save_question_receiver, sender=Question)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    





    