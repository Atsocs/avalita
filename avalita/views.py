from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

# from avalita.forms import RatingForm
from avalita.models import Course, Rating


def course_list(request):
    user = request.user
    if hasattr(user, 'student'):
        courses = Course.objects.filter(students__user__username=user.username)
    elif hasattr(user, 'professor'):
        courses = Course.objects.filter(professors__user__username=user.username)
    template = loader.get_template('avalita/courses_list.html')

    context = {
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))


def course_detail(request, course_id):
    course = None
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist.")
    if hasattr(request.user, 'student'):
        try:
            rating = Rating.objects.get(course__pk=course_id, student__pk=request.user.student.pk)
        except Rating.DoesNotExist:
            raise Http404("Rating does not exist. Have you taken " + str(course.code) + '?')
        return render(request, 'avalita/course_detail.html', {'course': course, 'rating': rating})
    return render(request, 'avalita/course_detail.html', {'course': course})


def vote(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    categories = ['general', 'coherence', 'understanding', 'easiness']
    for category in categories:
        value = request.POST[category]
        if value:
            setattr(rating, category, int(value))
    rating.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('course_list'))
