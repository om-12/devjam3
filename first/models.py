from django.db import models

# Create your models here.
class rent1payee(models.Model):
    p_email=models.EmailField(max_length=254)
    p_name=models.CharField(max_length=100)
    p_country=models.CharField(max_length=100)
    def __str__(self):
        return self.p_email

class Rentyourhouse(models.Model) :
    fullname = models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    adults = models.CharField(max_length=100)
    children = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    appointment = models.TimeField()
    roomdescription = models.CharField(max_length=500)
    tenantdescription = models.CharField(max_length=500)
    price = models.IntegerField()
    houselocation=models.CharField(max_length=100,default='location not clear')
    localitylocation=models.CharField(max_length=100,default='location not clear')
    citylocation=models.CharField(max_length=100,default='location not clear')
    def __str__(self):
        return self.fullname



class Image(models.Model):
    name= models.CharField(max_length=100)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")
    rent_your_house=models.OneToOneField(Rentyourhouse, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 






class Feedback(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.name

