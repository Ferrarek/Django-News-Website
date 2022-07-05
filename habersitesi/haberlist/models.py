from django.db import models

# Create your models here.
class Haberler(models.Model):
    baslik=models.CharField(max_length=150)
    anahaber=models.TextField()
    sehir=models.CharField(max_length=150)
    zaman=models.DateField()
    resim=models.CharField(max_length=150)
    def __str__(self):
        deger: object=self.baslik
        return deger