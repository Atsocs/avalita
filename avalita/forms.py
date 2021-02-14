from django import forms

from avalita.models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('period', 'code', 'title', 'students')
