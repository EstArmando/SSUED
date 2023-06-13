from django.db import models
from disability.models import Disability

from university.models import University

# Create your models here.
class Sex(models.Model):
    id_sex = models.CharField('sex_id', primary_key= True, max_length=1, choices=(('F', 'Female'), ('M', 'Male')))
    gender = models.CharField('gender', max_length=50)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'sexos'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    age = models.IntegerField('age')
    start_year = models.IntegerField('start_year')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE)

    class Meta:
        db_table = 'estudiantes'