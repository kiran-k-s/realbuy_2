from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Property(models.Model):
    SELLorRENT = (
        ('S', 'Sell'),
        ('R', 'Rent'),
    )
    sell_or_rent = models.CharField(max_length=1, choices=SELLorRENT)
    
    property_type = models.CharField(max_length=4)
    
    image = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    bathroom = models.IntegerField()
    bedroom = models.IntegerField()
    built_up_area = models.FloatField()
    
    BUILTupUNIT = (
        ('1', 'm\N{SUPERSCRIPT TWO}'),
        ('2', 'cm\N{SUPERSCRIPT TWO}'),
        ('3', 'mm\N{SUPERSCRIPT TWO}'),
    )
    built_up_unit = models.CharField(max_length=1, choices=BUILTupUNIT)
    
    carpet_area = models.FloatField()
    
    CARPET_UNIT = (
        ('1', 'm\N{SUPERSCRIPT TWO}'),
        ('2', 'cm\N{SUPERSCRIPT TWO}'),
        ('3', 'mm\N{SUPERSCRIPT TWO}'),
    )
    carpet_unit = models.CharField(max_length=1, choices=CARPET_UNIT)
    
    
    RESALEorNEW = (
        ('R', 'Resale'),
        ('N', 'New Booking'),
    )
    resale_or_new = models.CharField(max_length=1,choices=RESALEorNEW, default=('R', 'Resale'))
    
    property_floor = models.CharField(max_length=20)
    ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    total_floor = models.IntegerField()
    
    AVAILABILITY = (
        ('R', 'Ready to Move'),
        ('U', 'Under Construction'),
    )
    availability = models.CharField(max_length=1,choices=AVAILABILITY)
    
    description = models.Textfield()
    date = models.DateField.auto_now_add()
    
    def __str__(self)
        return self.description + '|' + str(self.ownership)
    
    def get_absolute_url(self):
        return reverse('detail' ,args=(str(self.id)))
    
    
    
    

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.Textfield()
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
