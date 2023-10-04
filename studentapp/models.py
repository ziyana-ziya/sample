
from django.db import models

class data(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10)  # Add a field for gender

    qualifications = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/", null=True, blank=True)

    def _str_(self):
        return f"{self.firstname} {self.lastname}"

# Create your models here.
