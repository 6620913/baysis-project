from django.db import models

# Create your models here.
class Claim(models.Model):

    reqID = models.CharField(max_length=30,primary_key='TRUE')
    date = models.CharField(max_length=10)
    status = models.CharField(max_length=50)

    name = models.CharField(max_length=50)
    dob = models.CharField(max_length=10)
    smoking_status = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    profileimg = models.FileField(upload_to ='uploads/')

    emp_mrn = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    pcp = models.CharField(max_length=50)


    doctor = models.CharField(max_length=50)
    docdisc1 = models.CharField(max_length=70)
    docdisc2 = models.CharField(max_length=70)
    docdisc3 = models.CharField(max_length= 70)

    rID = models.CharField(max_length=30)
    authID = models.CharField(max_length=30)
    services = models.TextField()

    primary_player_disc = models.CharField(max_length=100)
    EDI = models.CharField(max_length=30)
    Assignment = models.CharField(max_length=50)
    force_drop = models.CharField(max_length=10)

    secondary_player_disc = models.CharField(max_length=100,default=" ")
    sEDI = models.CharField(max_length=30,default=" ")
    sAssignment = models.CharField(max_length=50,default=" ")
    sforce_drop = models.CharField(max_length=10,default=" ")


    CPT = models.CharField(max_length=30)
    diag = models.CharField(max_length=200)
    units = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    total = models.CharField(max_length=60)

    

    def __str__(self):
        return self.reqID