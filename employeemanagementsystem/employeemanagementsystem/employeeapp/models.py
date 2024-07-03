from django.db import models
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=200)
    egender=models.CharField(max_length=200)
    esalary=models.IntegerField()
    eyoe=models.IntegerField()
    edept=models.CharField(max_length=200)
    ecompany=models.CharField(max_length=200)

   
    def __str__(self):
        return self.ename