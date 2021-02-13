from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else '@' + self.user.username


allowed_emails = {('@g' + x + '.ita.br'): y
                  for (x, y) in [('a', 'Student'), ('p', 'Professor')]}


class Professor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else '@' + self.user.username


@receiver(post_save, sender=get_user_model())
def when_init(sender, instance, created, **kwargs):
    if created:
        user_type = next(allowed_emails[e]
                         for e in allowed_emails
                         if instance.email.endswith(e))
        profile = eval(user_type).objects.create(user=instance)
        profile.save()
        pass


class Course(models.Model):
    period = models.CharField(max_length=6)
    code = models.CharField(max_length=6)
    professors = models.ManyToManyField(Professor)
    title = models.CharField(max_length=140)
    students = models.ManyToManyField(Student)

    class Meta:
        ordering = ['period', 'code']

    def __str__(self):
        return str(self.code) + ': ' + str(self.title)


class Rating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    general = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    coherence = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    understanding = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    easiness = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        ratings = [self.general, self.coherence, self.understanding, self.easiness]
        return str(self.course) + ' | ' + str(self.student) + ' | ' + str(ratings)
