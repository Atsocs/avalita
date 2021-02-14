from statistics import mean

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


def none_mean(x):
    x = [e for e in x if e is not None]
    return mean(x) if x else None


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
    period = models.CharField(max_length=6, help_text='Example: "2021.1"')
    code = models.CharField(max_length=6, help_text='Example: "MAT-12"')
    title = models.CharField(max_length=140, help_text='Example: "Cálculo I"')
    professors = models.ManyToManyField(Professor)
    students = models.ManyToManyField(Student, blank=True)

    class Meta:
        ordering = ['period', 'code']

    def __str__(self):
        return str(self.code) + ': ' + str(self.title)


class Rating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    general = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    coherence = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    understanding = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    easiness = models.IntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def get_ratings(self):
        return self.general, self.coherence, self.understanding, self.easiness

    def __str__(self):
        return str(self.get_ratings())


def get_score(course):
    results = tuple(zip(*[r.get_ratings() for r in course.rating_set.all()]))
    scores = tuple(none_mean(res) for res in results)
    counts = tuple(len(tuple(x for x in res if x is not None)) for res in results)
    return tuple(zip(scores, counts))


@receiver(m2m_changed, sender=Course.students.through)
def when_add_student(sender, instance, **kwargs):
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    if action == "post_add":
        for pk in pk_set:
            s = Student.objects.get(pk=pk)
            Rating.objects.create(course=instance, student=s)
