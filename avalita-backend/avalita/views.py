from django.core.mail import send_mail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from avalita.forms import AddCourseForm, StudentManagesCoursesForm
from avalita.models import Course, Rating, get_score


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
    try:
        course = Course.objects.get(pk=course_id)
        score = get_score(course)
    except Course.DoesNotExist:
        raise Http404("Course does not exist.")
    if hasattr(request.user, 'student'):
        try:
            rating = Rating.objects.get(course__pk=course_id, student__pk=request.user.student.pk)
        except Rating.DoesNotExist:
            raise Http404("Rating does not exist. Have you taken " + str(course.code) + '?')
        return render(request, 'avalita/student/course_detail.html',
                      {'course': course, 'rating': rating, 'score': score})
    return render(request, 'avalita/professor/course_detail.html', {'course': course, 'score': score})


def vote(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    categories = ['general', 'coherence', 'understanding', 'easiness']
    for category in categories:
        value = request.POST[category]
        if value:
            setattr(rating, category, int(value))
    rating.save()
    return HttpResponseRedirect(reverse('course_detail', args=[rating.course.pk]))


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
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
            return HttpResponseRedirect(reverse('index'))

    else:
        form = AddCourseForm()

    return render(request, 'avalita/professor/add_course.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return HttpResponseRedirect(reverse('index'))


def edit_course(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            assert (hasattr(request.user, 'professor'))
            professor = request.user.professor
            assert (professor in course.professors.all())
            course.period = data['period']
            course.code = data['code']
            course.title = data['title']
            course.students.set(data['students'])
            course.save()
            return HttpResponseRedirect(reverse('course_detail', args=[course_id]))

    else:
        form = AddCourseForm(instance=course)

    return render(request, 'avalita/professor/edit_course.html', {'form': form})


def student_manages_courses(request):
    student = request.user.student
    if request.method == 'POST':
        form = StudentManagesCoursesForm(request.POST)
        if form.is_valid():
            old_courses = student.course_set.all()
            new_courses = form.cleaned_data['courses']
            removed_courses = [c for c in old_courses if c not in new_courses]
            added_courses = [c for c in new_courses if c not in old_courses]

            for c in removed_courses:
                #  TODO: notify professor
                r = c.rating_set.get(student=student)
                r.delete()
                c.students.remove(student)

            for c in added_courses:
                #  TODO: ask to professors of new_courses
                c.students.add(student)

            return HttpResponseRedirect(reverse('index'))

    else:
        form = StudentManagesCoursesForm(instance=student)

    return render(request, 'avalita/student/student_manages_courses.html', {'form': form})
