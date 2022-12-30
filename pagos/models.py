from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Payments(models.Model):
    class Services(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Services.choices,
        default=Services.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='user')
    monto = models.FloatField(default=0.0)

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.URLField()

class PaymentUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

class ExpiredPayments(models.Model):
    id = models.AutoField(primary_key=True)
    pay_user_id = models.OneToOneField(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()