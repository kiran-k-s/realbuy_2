from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.core.exceptions import FieldDoesNotExist
import os

class Property(models.Model):
    SELLorRENT = (
        ('sell', 'Sell'),
        ('rent', 'Rent'),
    )
    sell_or_rent = models.CharField(max_length=100, choices=SELLorRENT)
    
    PROPERTY_TYPE = (
        ('commercial', 'Commercial'),
        ('furnished home', 'Furnished Home'),
        ('land and plot', 'Land and Plot'),
        ('rental', 'Rental'),
    )    
    property_type = MultiSelectField(choices = PROPERTY_TYPE)
    
    image = models.ImageField(upload_to='images/')
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    price = models.IntegerField(blank=True,null=True)
    bathroom = models.IntegerField(blank=True,null=True)
    bedroom = models.IntegerField(blank=True,null=True)
    built_up_area = models.FloatField(blank=True,null=True)
    
    BUILTupUNIT = (
        ('CENTS', 'cents'),
        ('SQM', 'sq.m'),
        ('SQFT', 'sq.ft'),
    )
    built_up_unit = models.CharField(max_length=100, choices=BUILTupUNIT,null=True)
    
    carpet_area = models.FloatField(blank=True,null=True)
    
    CARPET_UNIT = (
        ('CENTS', 'cents'),
        ('SQM', 'sq.m'),
        ('SQFT', 'sq.ft'),
    )
    carpet_unit = models.CharField(max_length=100, choices=CARPET_UNIT,null=True)
    
    
    RESALEorNEW = (
        ('resale', 'Resale'),
        ('new', 'New Booking'),
    )
    resale_or_new = models.CharField(max_length=100,choices=RESALEorNEW, null=True)
    
    property_floor = models.IntegerField(blank=True,null=True,default=None)
    ownership = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    total_floor = models.IntegerField(blank=True,null=True)
    
    AVAILABILITY = (
        ('ready to move', 'Ready to Move'),
        ('under construction', 'Under Construction'),
    )
    availability = models.CharField(max_length=100,choices=AVAILABILITY,null=True)
    
    description = models.TextField(blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='realbuy_posts')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return str(self.description) + '|' + str(self.ownership)
    
    def get_absolute_url(self):
        return reverse('detail' ,args=(str(self.id)))
    
    def total_likes(self):
        return self.likes.count()
        
    def liked(self,request):
        like = False
        if self.likes.filter(id=self.request.user.id).exists():
            like = True
        return like

    @property
    def filename(self):
        return os.path.basename(self.image.name)
    
    
    
    
    
    
    

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="user")
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
    
    
    
    
    
    
