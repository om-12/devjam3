from django.db import models

class Image(models.Model):
    name= models.CharField(max_length=100)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")
    def __str__(self):
        return self.name + ": " + str(self.imagefile)
