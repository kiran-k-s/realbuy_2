from django import forms
from .models import Property,ContactUs
#from select2.forms import Select2MultipleWidget
from django.core.exceptions import FieldDoesNotExist

    
    
class AddForm1(forms.Form):
            
            
        SELLorRENT = [('sell', 'Sell'),('rent', 'Rent')]
        sell_or_rent = forms.ChoiceField(choices=SELLorRENT, widget=forms.RadioSelect(attrs={ 'class':'sellorrent'}))
        PROPERTY_TYPE = [ ('commercial', 'Commercial'),
        ('furnished home', 'Furnished Home'),
        ('land and plot', 'Land and Plot'),
        ('rental', 'Rental') ]
        property_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=PROPERTY_TYPE)
        image = forms.ImageField()

        city = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'city', 'placeholder' : 'City'}))
        address = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'address', 'placeholder' : 'Address'}))
        location = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'location', 'placeholder' : 'Location'}))
        
        class Meta:
            model = Property
            fields = ('sell_or_rent','property_type','image','city','address','location')
            
            
        
        
class AddForm2(forms.ModelForm):
        
            
        price = forms.CharField(widget=forms.NumberInput())
        bathroom = forms.CharField(widget=forms.NumberInput())
        bedroom = forms.CharField(widget=forms.NumberInput())
        built_up_area = forms.CharField(widget=forms.NumberInput())
        BUILTupUNIT = [('cm', 'sq.cm'),('m', 'sq.m'),('ft', 'sq.ft')]
        built_up_unit = forms.ChoiceField(choices=BUILTupUNIT, widget=forms.Select(attrs={ 'class':'builtupunit'}))
        carpet_area = forms.CharField(widget=forms.NumberInput())
        CARPET_UNIT = [('cm', 'sq.cm'),('m', 'sq.m'),('ft', 'sq.ft')]
        carpet_unit = forms.ChoiceField(choices=CARPET_UNIT, widget=forms.Select(attrs={ 'class':'carpetunit'}))
        RESALEorNEW = [('resale', 'Resale'), ('new', 'New Booking')]
        resale_or_new = forms.ChoiceField(choices=RESALEorNEW, widget=forms.RadioSelect(attrs={ 'class':'resaleornew'}))
        
        PROPERTY_FLOOR = [('1', '1'), ('2','2'), ('3','3'), ('4', '4'), ('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20')]
        #property_floor = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          #choices=PROPERTY_FLOOR)
        #property_floor = forms.MultipleChoiceField(choices=PROPERTY_FLOOR,widget=Select2MultipleWidget)


        total_floor = forms.CharField(widget=forms.NumberInput())
        AVAILABILITY = [('ready to move', 'Ready to Move'),('under construction', 'Under Construction'),]
        availability = forms.ChoiceField(choices=AVAILABILITY, widget=forms.RadioSelect(attrs={ 'class':'availability'}))
        description = forms.CharField(min_length=20, widget=forms.Textarea(attrs={"class":"description" ,"placeholder":"Description"}))
        
        class Meta:
            model = Property
            fields = ('price','bathroom','bedroom','built_up_area','built_up_unit','carpet_area','carpet_unit','resale_or_new','property_floor','ownership','total_floor','availability','description')
            widgets = {
                'ownership': forms.TextInput(attrs={'value':'', 'id':'owner','readonly':True})
            }
            
            
        
        
        
                                                   
class ContactUsForm(forms.ModelForm):
        class Meta:
            model = ContactUs
            fields = ('name','email','phone','message')
        name = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(
            attrs={'id':'inputName', 'placeholder' : 'Name'}))
        email = forms.EmailField(max_length=45 , widget=forms.EmailInput(
            attrs={'id':'inputEmail', "placeholder":"Email address"}
        ))
        phone = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(
            attrs={'id':'inputPhone', "placeholder":"Phone Number"}
        ),required=False)
        message = forms.CharField(min_length=20, widget=forms.Textarea(
            attrs={'id':'inputMessage',"placeholder":"Message"}
        ))
                         
                                                   