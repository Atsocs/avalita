from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_course', views.add_course, name='add_course'),
    path('student_manages_courses', views.student_manages_courses, name='student_manages_courses'),
    path('<int:course_id>/delete_course', views.delete_course, name='delete_course'),
    path('<int:course_id>/edit_course', views.edit_course, name='edit_course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:rating_id>/vote/', views.vote, name='vote'),
]
