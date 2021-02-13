from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic

# from avalita.forms import RatingForm
from avalita.forms import AddCourseForm
from avalita.models import Course, Rating


def index(request):
    user = request.user
    if user.is_authenticated:
        is_student = hasattr(user, 'student')
        is_professor = hasattr(user, 'professor')
        if is_student or is_professor:
            if is_student:
                courses = Course.objects.filter(students__user__username=user.username)
                template = loader.get_template('avalita/student/index.html')
            elif is_professor:
                courses = Course.objects.filter(professors__user__username=user.username)
                template = loader.get_template('avalita/professor/index.html')
            context = {'courses': courses, }
        else:
            template = loader.get_template('avalita/index.html')
            context = {}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('avalita/non_authenticated.html')
        context = {}
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
        return render(request, 'avalita/student/course_detail.html', {'course': course, 'rating': rating})
    return render(request, 'avalita/professor/course_detail.html', {'course': course})


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
    return HttpResponseRedirect(reverse('index'))


def add_course(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddCourseForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            assert (hasattr(request.user, 'professor'))
            professor = request.user.professor
            new_course = professor.course_set.create(
                period=data['period'],
                code=data['code'],
                title=data['title'])
            new_course.students.set(data['students'])
            new_course.save()
            # process the data in form.cleaned_data as required
            # professor.course_set.create(period=form., code='MPG-03', title='Desenho Técnico'
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddCourseForm()

    return render(request, 'avalita/professor/add_course.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return HttpResponseRedirect(reverse('index'))
