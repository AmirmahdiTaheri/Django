from email.headerregistry import Address
from django.db import models
from tinymce.models import HTMLField


#CATEGORY
class Category(models.Model):
    name         = models.CharField(max_length=100)
    distribution = models.TextField(max_length=200 , null=False
    , blank=False)

    def __str__(self):
        return self.name

#POST
class Txt(models.Model):
    id               = models.AutoField(primary_key=True , unique=True , serialize=True , null= False , blank=False)
    subject          = models.CharField(max_length=150 ,null=False , blank=False , unique=False)
    categorry        = models.ForeignKey(Category , on_delete=models.CASCADE)
    summary          = models.CharField(max_length=150 , null=False , blank=False)
    distribution     = HTMLField(blank=False , null=False ,editable=True)
    time             = models.DateTimeField(editable=True)
    special          = models.BooleanField(null= True , blank=True)

    def __str__(self):
        return str(self.id)

#ABOUT_US
class about(models.Model):
    ttle           = models.CharField(max_length=50)
    distribution   = models.TextField(editable=True)

    def __str__(self):
        return self.ttle

#CONTACT_US
class contact(models.Model):
    ttle      = models.CharField(null= False,blank=False, max_length=50) 
    mail      = models.EmailField(help_text="Enter Your Company Email for Contact with YOUR Web Visitor")
    tel       = models.BigIntegerField(help_text="Enter Your Company Phone Number for Contact with YOUR Web Visitor")
    address   = models.CharField(max_length=1000,null=True)