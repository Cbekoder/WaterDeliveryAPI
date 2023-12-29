from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.PositiveIntegerField()
    litr = models.PositiveSmallIntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=13)
    qarz = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqti = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=13)
    kiritilgan_vaqt = models.DateField()

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv_id = models.ForeignKey(Suv, null=True, on_delete=models.SET_NULL)
    vaqti = models.DateField()
    mijoz_id = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdori = models.PositiveSmallIntegerField()
    umumiy_narxi = models.PositiveIntegerField()
    admin_id = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL)
    haydovchi_id = models.ForeignKey(Haydovchi, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        suv = Suv.objects.get(id = self.suv_id)
        self.umumiy_narxi = suv.narx * self.miqdori
        super(Buyurtma, self).save(*args, **kwargs)







