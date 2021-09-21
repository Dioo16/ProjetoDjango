from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    Work = models.CharField(max_length=20)
    Salary = models.DecimalField(max_digits=4, decimal_places=2)
    Photo = models.ImageField(upload_to='clientes_photos', null=True, blank=True)
    def __str__(self):
        return self.first_name + self.Work
