from django.db import models

# Create your models here.
class University(models.Model):
    code=models.CharField('code',primary_key=True, max_length=5)
    name=models.CharField('name',unique=True,max_length=100)
    acronyms=models.CharField('acronyms',unique=True,max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'universidades'

