from django.urls import path

from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add_course', views.add_course, name='add_course'),
    path('<int:course_id>/delete_course', views.delete_course, name='delete_course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:rating_id>/vote/', views.vote, name='vote'),
]
