from django import forms

from avalita.models import Course


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('period', 'code', 'title', 'students')
