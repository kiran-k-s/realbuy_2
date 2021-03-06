from django import forms
from .models import Property,ContactUs,Profile
#from django_select2.forms import Select2MultipleWidget
from django.core.exceptions import FieldDoesNotExist

    
    
class AddForm1(forms.ModelForm):
            
            
        SELLorRENT = [('sell', 'Sell'),('rent', 'Rent')]
        sell_or_rent = forms.ChoiceField(choices=SELLorRENT, widget=forms.RadioSelect(attrs={ 'class':'sellorrent'}))
        PROPERTY_TYPE = [ ('commercial', 'Commercial'),
        ('furnished home', 'Furnished Home'),
        ('land and plot', 'Land and Plot'),
        ('rental', 'Rental') ]
        property_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=PROPERTY_TYPE)
        '''property_type = forms.MultipleChoiceField(choices=PROPERTY_TYPE, widget=forms.SelectMultiple(attrs={ 'class':'propertytype'}))'''

        city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'city', 'placeholder' : 'City'}))
        address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'address', 'placeholder' : 'Address'}))
        location = forms.CharField(widget=forms.TextInput(attrs={'class' : 'location', 'placeholder' : 'Location'}))
        
        class Meta:
            model = Property
            fields = ('sell_or_rent','property_type','image','city','address','location')
            
        def __init__(self, *args, **kwargs):
            super(AddForm1, self).__init__(*args, **kwargs)  
            self.fields['image'].widget.attrs.update({'class' : 'add-image','placeholder':'upload property image'}) 


        
        
class AddForm2(forms.ModelForm):
        
        price = forms.CharField(widget=forms.NumberInput())    
        built_up_area = forms.CharField(widget=forms.NumberInput())
        BUILTupUNIT = [('CENTS', 'cents'),('SQM', 'sq.m'),('SQFT', 'sq.ft')]
        built_up_unit = forms.ChoiceField(choices=BUILTupUNIT, widget=forms.Select(attrs={ 'class':'builtupunit'}))
        carpet_area = forms.CharField(widget=forms.NumberInput())
        CARPET_UNIT = [('CENTS', 'cents'),('SQM', 'sq.m'),('SQFT', 'sq.ft')]
        carpet_unit = forms.ChoiceField(choices=CARPET_UNIT, widget=forms.Select(attrs={ 'class':'carpetunit'}))
        RESALEorNEW = [('resale', 'Resale'), ('new', 'New Booking')]
        resale_or_new = forms.ChoiceField(choices=RESALEorNEW, widget=forms.RadioSelect(attrs={ 'class':'resaleornew'}))
        property_floor = forms.CharField(required=False,widget=forms.NumberInput())
        total_floor = forms.CharField(widget=forms.NumberInput())
        AVAILABILITY = [('ready to move', 'Ready to Move'),('under construction', 'Under Construction'),]
        availability = forms.ChoiceField(choices=AVAILABILITY, widget=forms.RadioSelect(attrs={ 'class':'availability'}))
        description = forms.CharField(min_length=20, widget=forms.Textarea(attrs={"class":"add2-description" ,"placeholder":"Description"}))
        
        class Meta:
            model = Property
            fields = ('price','bathroom','bedroom','built_up_area','built_up_unit','carpet_area','carpet_unit','resale_or_new','property_floor','ownership','total_floor','availability','description')
            widgets = {
                'ownership': forms.TextInput(attrs={'value':'', 'id':'owner','readonly':True})
            }
            
          #removing auto created options list    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['property_floor'].queryset = Property.objects.none()

        def clean(self):
            self.cleaned_data = super(AddForm2, self).clean()
            if self.cleaned_data['property_floor'] == '': self.cleaned_data['property_floor'] = None
            return self.cleaned_data
        
        
                                                   
class ContactUsForm(forms.ModelForm):
        class Meta:
            model = ContactUs
            fields = ('name','email','phone','message')
        name = forms.CharField(max_length=100, widget=forms.TextInput(
            attrs={'id':'contactus_name','placeholder' : 'Name'}))
        email = forms.EmailField(max_length=45 , widget=forms.EmailInput(
            attrs={'id':'contactus_mail', "placeholder":"Email"}
        ))
        phone = forms.CharField( widget=forms.TextInput(
            attrs={'id':'contactus_phone', "placeholder":"Phone Number"}
        ),required=False)
        message = forms.CharField(min_length=20, widget=forms.Textarea(
            attrs={'id':'contactus_message',"placeholder":"Message"}
        ))

                         
          #removing auto created options list    
        '''def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['name'].queryset = ContactUs.objects.none()'''


class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ('name','image','email','phone','address')
        name = forms.CharField(widget=forms.TextInput(
            attrs={'id':'profile-edit-name'}))
        email = forms.EmailField(max_length=45 , widget=forms.EmailInput(
            attrs={'id':'profile-edit-email'}
        ))
        phone = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(
            attrs={'id':'profile-edit-phone'}
        ),required=False)
        address = forms.CharField(widget=forms.Textarea(
            attrs={'id':'profile-edit-address'}
        ))
        image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'id' : 'profile-edit-upload'}))
         
