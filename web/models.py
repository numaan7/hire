import email
from django.db import models

# Create your models here.
class CV(models.Model):
    fullname=models.CharField(max_length=200)
    user_email=models.EmailField(max_length=100)
    cv = models.FileField(upload_to='documents')
    upload_date = models.DateTimeField(auto_now_add =True)
    class Meta:
        ordering = ('-upload_date',)
    def __str__(self):
        return self.fullname+" "+self.user_email

class Contact(models.Model):
    name=models.CharField(max_length=200)
    contact_email=models.EmailField(max_length=100)
    desc=models.TextField()
    date = models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return self.name+" "+self.contact_email