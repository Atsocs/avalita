from django.test import TestCase
from django.contrib.auth.models import User

from avalita.models import Course, Professor, Student


def professor_creates_course(whoasked, period, code, title, professors, students):
    assert hasattr(whoasked, 'professor')
    new_course = Course.objects.create(period=period, code=code, title=title)
    new_course.professors.set(professors)
    new_course.students.set(students)
    new_course.save()
    return new_course


class ProfessorViewTests(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='borille',
            email='borille@gp.ita.br',
            password='senhacorreta',
            first_name='Anderson',
            last_name='Borille'
        )
        User.objects.create_user(
            username='ccosta',
            email='caio.costa@ga.ita.br',
            password='senhacorreta',
            first_name='Caio',
            last_name='Costa'
        )

    def test_add_course(self):
        self.client.login(username='borille', password='senhacorreta')
        response = self.client.get('/')
        user = response.wsgi_request.user
        professor_creates_course(
            whoasked=user,
            period='2020.1', code='MTP-03',
            title='Introdução à Engenharia',
            professors=Professor.objects.filter(user__username=user.username),
            students=Student.objects.filter(user__username='ccosta')
        )
        x=1
