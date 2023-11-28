from django.db import models
import uuid
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


def no_past_due_date(value):
    today = date.today()
    if value < today:
        raise ValidationError('Due date cannot be in the past.')
##Bills    
class Bill(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        PAID = 'PAID', _('Paid')
        OVERDUE = 'OVERDUE', _('Overdue')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    dueDate = models.DateField(max_length=200,
                               validators=[no_past_due_date])
    amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=10,
       choices=Status.choices,
       default=Status.PENDING                       
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['dueDate','-updated','-created']
    def __str__(self):
        return self.customer.username

###Payments    
class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transactionId = models.CharField(max_length=20)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
    paymentChannel = models.CharField(max_length=50)
    remark = models.TextField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.transactionId
    
@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    if sender.name == 'base':
        # Replace 'myapp' with the actual name of your app
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Biller')
        Group.objects.get_or_create(name='Customer')
        User.objects.create_superuser('test','admin@kacha.et','Test1324!')
