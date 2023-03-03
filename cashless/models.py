from django.db import models

# Create your models here.

class CardHolder(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, unique=True)
    card_id = models.CharField(max_length=8,unique=True)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{name}:{card_id}".format(name=self.name,card_id=self.card_id)

class Merchant(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, unique=True)
    reader_id = models.CharField(max_length=15,unique=True)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{name}:{reader_id}".format(name=self.name,reader_id=self.reader_id)

class Transaction(models.Model):
    cardholder_id = models.ForeignKey(CardHolder,on_delete=models.CASCADE,to_field = 'card_id')
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    merchant_id = models.ForeignKey(Merchant,on_delete=models.CASCADE,to_field='reader_id')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{from_}: {to}'.format(from_=self.cardholder_id,to=self.merchant_id)


    
