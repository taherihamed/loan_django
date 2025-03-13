from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import CharField


class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    wallet = models.IntegerField


class Loan(models.Model):
    installment_id = models.IntegerField(unique=True)
    number_of_installment = models.IntegerField(validators=[MaxValueValidator(100)])
    price_of_installment = models.IntegerField
    installment_is_active = models.BooleanField(default=True)
    installment_user = models.ForeignKey(to=User, on_delete=models.CASCADE)