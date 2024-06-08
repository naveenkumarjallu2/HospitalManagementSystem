from django.db import models


# Create your models here.
class City(models.Model):
    City_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.City_Name}"


class Diseases(models.Model):
    Diseases_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Diseases_Name}"


class Patient(models.Model):
    Patient_Name = models.CharField(max_length=50)
    Patient_Age = models.IntegerField()
    Patient_Phone = models.BigIntegerField()
    Patient_City = models.ForeignKey(City, on_delete=models.CASCADE)
    Patient_Diseases = models.ForeignKey(Diseases, on_delete=models.CASCADE)



