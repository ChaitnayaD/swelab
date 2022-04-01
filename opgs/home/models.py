from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_fields(value):
    print(value)
    if not value:
        raise ValidationError("This field cannot be empty!")
    else:
        return value

class student(models.Model):
    name = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.EmailField(validators=[validate_fields], blank=False)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    #filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    def __str__(self):
        return self.name


class alumni(models.Model):
    name = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    companies_worked_in = models.TextField(max_length=200, default="nil")

    def __str__(self):
        return self.name

class company(models.Model):
    name = models.CharField(max_length=122)
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    Verified = models.BooleanField(default = False)
    job_details = models.TextField(max_length=500,default="nil")
    
    

    def __str__(self):
        return self.name


class Notification(models.Model):
    name = models.CharField(max_length=20)
    notification = models.TextField(max_length=500)
    visible_to_student = models.BooleanField()
    visible_to_company = models.BooleanField()
    visible_to_alumni = models.BooleanField()

class Personal_Notification(models.Model):
    generator = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    not_name = models.CharField(max_length=20)
    notification = models.TextField(max_length=500)
    
class Feedback(models.Model):
    alum_user_id=models.TextField(max_length=20)
    stud_user_id=models.TextField(max_length=20)
    feedback=models.TextField(max_length=500,default="nil")

class Application(models.Model):
    stud_user_id = models.CharField(max_length=20)
    comp_user_id = models.CharField(max_length=20)
    app_title = models.CharField(max_length=20)
    application = models.TextField(max_length=500)