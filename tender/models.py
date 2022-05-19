from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Guest(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)

class Senior(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)

class Contractor(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   contact = models.CharField(max_length=100)
   address = models.CharField(max_length=100)

class Work(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   name = models.CharField(max_length=100)
   estiamount= models.CharField(max_length=100)
   periodcompltete= models.CharField(max_length=100)
   tenddocm = models.ImageField(upload_to='images/')
   lastdatesub= models.CharField(max_length=100)
   othdesc= models.CharField(max_length=100)
   status = models.CharField(max_length=100,null=True)

class AddPlan(models.Model):
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   work = models.ForeignKey(Work,on_delete=models.CASCADE,null=True)
   plan = models.ImageField(upload_to='images/')
   estimate = models.CharField(max_length=100,null=True)
   deposit = models.CharField(max_length=100,null=True)
   periodcompltete = models.CharField(max_length=100)
   othdesc = models.CharField(max_length=100)
   status = models.CharField(max_length=100,null=True)


class WorkDetails(models.Model):
   name = models.CharField(max_length=100)
   place = models.CharField(max_length=100)
   details = models.CharField(max_length=100)


class AddWorkStatus(models.Model):
    plans = models.ForeignKey(AddPlan,on_delete=models.CASCADE)
    descri = models.CharField(max_length=100)
    status = models.CharField(max_length=100,null=True)
    files = models.ImageField(upload_to='images/')

class FundRequest(models.Model):
   work = models.ForeignKey(Work,on_delete=models.CASCADE,null=True)
   user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   amount = models.CharField(max_length=100)
   description = models.CharField(max_length=100)
   status = models.CharField(max_length=100,null=True)






