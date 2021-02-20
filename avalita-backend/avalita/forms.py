from django import forms

from avalita.models import Course, Student


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('period', 'code', 'title', 'professors', 'students')


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('period', 'code', 'title', 'students')


class StudentManagesCoursesForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ()

    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['courses'] = [c.pk for c in kwargs['instance'].course_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self)
        instance.course_set.clear()
        instance.course_set.add(*self.cleaned_data['courses'])
        return instance
