from django.db import models
#pylint: disable=imported-auth-user
from django.contrib.auth.models import User

# Create your models here.
class Tutor(models.Model):
    tutor_firstname = models.CharField(max_length=20)
    tutor_lastname = models.CharField(max_length=20)
    tutor_email = models.EmailField()
    tutor_teach_field = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tutor_firstname} {self.tutor_lastname}"

class Basic_User_Model(models.Model):
    basic_user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Additional Information
    basic_portfolio_site = models.URLField(blank=True)
    basic_profpict = models.ImageField(upload_to="djangoApp1/profile_picts", blank=True)

    def __str__(self):
        return self.basic_user.username
