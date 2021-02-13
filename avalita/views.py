from django.http import HttpResponse
from django.template import loader

from avalita.models import Course


def course_list(request):
    user = request.user
    courses = Course.objects.filter(students__user__username=user.username)
    template = loader.get_template('courses_list.html')

    context = {
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))
