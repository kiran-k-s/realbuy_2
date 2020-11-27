from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField

class Property(models.Model):
    SELLorRENT = (
        ('S', 'Sell'),
        ('R', 'Rent'),
    )
    sell_or_rent = models.CharField(max_length=1, choices=SELLorRENT)
    
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
    price = models.IntegerField()
    bathroom = models.IntegerField()
    bedroom = models.IntegerField()
    built_up_area = models.FloatField()
    
    BUILTupUNIT = (
        ('1', 'm\N{SUPERSCRIPT TWO}'),
        ('2', 'cm\N{SUPERSCRIPT TWO}'),
        ('3', 'sq.ft'),
    )
    built_up_unit = models.CharField(max_length=1, choices=BUILTupUNIT)
    
    carpet_area = models.FloatField()
    
    CARPET_UNIT = (
        ('1', 'm\N{SUPERSCRIPT TWO}'),
        ('2', 'cm\N{SUPERSCRIPT TWO}'),
        ('3', 'sq.ft'),
    )
    carpet_unit = models.CharField(max_length=1, choices=CARPET_UNIT)
    
    
    RESALEorNEW = (
        ('R', 'Resale'),
        ('N', 'New Booking'),
    )
    resale_or_new = models.CharField(max_length=1,choices=RESALEorNEW, default=('R', 'Resale'))
    
    PROPERTY_FLOOR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    )    
    property_floor = MultiSelectField(choices = PROPERTY_FLOOR)
    ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    total_floor = models.IntegerField()
    
    AVAILABILITY = (
        ('R', 'Ready to Move'),
        ('U', 'Under Construction'),
    )
    availability = models.CharField(max_length=1,choices=AVAILABILITY)
    
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='realbuy_posts')
    
    def __str__(self):
        return self.description + '|' + str(self.ownership)
    
    def get_absolute_url(self):
        return reverse('detail' ,args=(str(self.id)))
    
    def total_likes(self):
        return self.likes.count()
    
    
    
    
    
    

class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
    
    
    
    
    
    
