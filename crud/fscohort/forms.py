from dataclasses import field
from statistics import mode
from struct import calcsize
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'