from django.db import models


# Create your models here.
class FinBase(models.Model):
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
            abstract = True

class Account(FinBase):
        name = models.CharField(max_length=64)
        transactions = models.ManyToManyField(
                            Transaction,
                            through="Split"
                        )

        
        def __str__(self):
            return self.name

class Split(FinBase):
        CREDIT = 'C'
        DEBIT = 'D'
        OP_CHOICES = (
            (CREDIT, "CREDIT"),
            (DEBIT, "DEBIT"),
        )
        amount = models.FloatField()
        op = models.CharField(choice=OP_CHOICES, max_length=1)
        account = models.ForeignKey(Account, on_delete=models.CASCADE)
        transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
        is_reconciled = models.BooleanField(default=False)

    def __str__(self):
        return "{0} {1} {2}".format(self.op, self.account, self.amount)

class Transaction(FinBase):
        INCOME = 'INC'
        EXPENSE = 'EXP'
        TTYPE_CHOICES = (
            (INCOME, "Income"),
            (EXPENSE, "Expense"),
        )
        tdate = models.DateField()
        ttype = models.CharField(choice=TTYPE_CHOICES, max_length=3, default=EXPENSE)
        other_party = models.CharField(max_length=50)
        amount = models.FloatField()
        categories = models.CharField(max_length=128)
        is_reconciled = models.BooleanField(default=False)
        recurrent = models.BooleanField(default=False) 
        #This needs to be captured using RRules

    def __str__(self):
        return "{0} {1}->{2} on {3}".format(amount, accounts, other_party, tdate)
