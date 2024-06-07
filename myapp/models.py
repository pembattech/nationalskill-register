from django.db import models

class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]
    
    COURSE_CHOICES = [
        ('CFB', 'Computer for Beginner'),
        ('DCO', 'Diploma in Computer Operator'),
        ('DGD', 'Diploma in Graphic Design'),
        ('OP', 'Office Package'),
        ('WD', 'Webpage Designing'),
        ('CH', 'Computer Hardware'),
        ('P', 'Programming'),
    ]
    
    LANGUAGE_CHOICES = [
        ('KR', 'Korean'),
        ('EN', 'English'),
        ('JP', 'Japanese'),
        ('HE', 'Hebrew'),
        ('TU', 'Tuition'),
    ]
    
    LEVEL_CHOICES = [
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advance'),
    ]
    
    fullname = models.CharField(max_length=100)
    dob = models.DateField()
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    present_qualification = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    parents_phone_number = models.CharField(max_length=15)
    computer_course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    language_course = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    course_level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.fullname

