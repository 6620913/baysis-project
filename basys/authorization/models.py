from django.db import models

# Create your models here.


class Authorization(models.Model):

    reqID = models.CharField(max_length=30,primary_key='TRUE')
    date = models.CharField(max_length=10)
    urgency = models.CharField(max_length=50)
    services = models.TextField()
    requested_by = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.reqID


