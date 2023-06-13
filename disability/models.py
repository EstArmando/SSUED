from django.db import models

# Create your models here.
class Disability (models.Model):
    disability_id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        db_table='discapacidades'