from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'fullname', 'dob', 'marital_status', 'gender', 'address', 'contact_number', 
            'present_qualification', 'father_name', 'mother_name', 'profession', 
            'parents_phone_number', 'computer_course', 'language_course', 'course_level'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

