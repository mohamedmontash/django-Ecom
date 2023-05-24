from django.db import models

# Create your models here.
orderChoices = (
    ("ordered", "ordered"),
    ("approved", "approved"),
    ("shipped", "shipped"),
    ("delivered", "delivered")
)


class order(models.Model): #table
    order_Title= models.CharField(max_length=100) #column

    order_Status= models.CharField(
        max_length = 20,
        choices = orderChoices,
        default = 'ordered'
        )
    customername= models.CharField(max_length=200)
    ordernumber= models.IntegerField(default=1)
    dateordered=  models.DateTimeField(auto_now=True, null=False)
    datecreated= models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.order_Title