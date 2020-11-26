from django import forms
from .models import Property,ContactUs
    
PROPERTY_TYPE = (
        ('C', 'Commercial'),
        ('F', 'Furnished Home'),
        ('L', 'Land and Plot'),
        ('R', 'Rental'),
    )    
    
class TypeAdminForm(forms.ModelForm):
        property_type = forms.MultipleChoiceField(choices = PROPERTY_TYPE)
        #property_type = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple(choices = PROPERTY_TYPE)
        
        def clean_property_type(self):
            property_type = self.cleaned_data['property_type']
            if not property_type:
                raise forms.ValidationError("...")

            if len(property_type) > 4:
                raise forms.ValidationError("...")

            property_type = ''.join(property_type)
            
        class Meta:
            model = Property
            fields = ('property_type',)
            
        
    
    
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

    
class FloorAdminForm(forms.ModelForm):
        property_floor = forms.MultipleChoiceField(choices = PROPERTY_FLOOR)
        
        
        class Meta:
            model = Property
            fields = ('property_floor',)
            
        '''def clean_property_floor(self):
        property_floor = self.cleaned_data['property_floor']
        if not property_floor:
            raise forms.ValidationError("...")

        if len(property_floor) > 20:
            raise forms.ValidationError("...")

        property_floor = ''.join(property_floor)
        return property_floor'''
    
    
class AddForm1(forms.ModelForm):
        class Meta:
            model = Property
            fields = ('sell_or_rent','property_type','image','city','address','location')
            '''widgets = {
                'sell_or_rent': forms.RadioSelect(attrs={'class':'sellorrent'})
                
            }'''
            
        SELLorRENT = [('1', 'Sell'), ('2', 'Rent')]
        sell_or_rent = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'choices': 'SELLorRENT', 'class':'sellorrent'}))
        PROPERTY_TYPE = [('1', 'Commercial'), ('2','Furnished Home'), ('3','Land and Plot'), ('4', 'Rental')]
        property_type = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple(attrs={'choices':'PROPERTY_TYPE','class':'propertytype'}))
        image = forms.ImageField()
        city = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'city', 'placeholder' : 'City'}))
        address = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'address', 'placeholder' : 'Address'}))
        location = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'class' : 'location', 'placeholder' : 'Location'}))
        
        
        
class AddForm2(forms.ModelForm):
        class Meta:
            model = Property
            fields = ('price','bathroom','bedroom','built_up_area','built_up_unit','carpet_area','carpet_unit','resale_or_new','property_floor','ownership','total_floor','availability','description')
            '''widgets = {
                'built_up_unit': forms.Select(attrs={'class':'builtupunit'})
                
            }'''
            
        price = forms.CharField(widget=forms.NumberInput())
        bathroom = forms.CharField(widget=forms.NumberInput())
        bedroom = forms.CharField(widget=forms.NumberInput())
        built_up_area = forms.CharField(widget=forms.NumberInput())
        BUILTupUNIT = [('1', 'm\N{SUPERSCRIPT TWO}'),('2', 'cm\N{SUPERSCRIPT TWO}'),('3', 'mm\N{SUPERSCRIPT TWO}'),]
        built_up_unit = forms.ChoiceField(required=True, widget=forms.Select(attrs={'choices':'BUILTupUNIT','class':'builtupunit'}))
        carpet_area = forms.CharField(widget=forms.NumberInput())
        CARPET_UNIT = [('1', 'm\N{SUPERSCRIPT TWO}'),('2', 'cm\N{SUPERSCRIPT TWO}'),('3', 'mm\N{SUPERSCRIPT TWO}'),]
        carpet_unit = forms.ChoiceField(required=True, widget=forms.Select(attrs={'choices':'CARPET_UNIT','class':'carpetunit'}))
        RESALEorNEW = [('1', 'Resale'), ('2', 'New')]
        resale_or_new = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'choices':'RESALEorNEW', 'class':'resaleornew'}))
        PROPERTY_FLOOR = [('1', '1'), ('2','2'), ('3','3'), ('4', '4')]
        property_floor = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple(attrs={'choices':'PROPERTY_FLOOR','class':'propertyfloor'}))
        ownership = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(attrs={'value':'', 'id':'owner', 'type':'hidden'}))
        total_floor = forms.CharField(widget=forms.NumberInput())
        AVAILABILITY = [('R', 'Ready to Move'),('U', 'Under Construction'),]
        availability = forms.ChoiceField(required=True, widget=forms.RadioSelect(attrs={'choices':'AVAILABILITY', 'class':'availability'}))
        description = forms.CharField(min_length=20, widget=forms.Textarea(attrs={"class":"description" ,"placeholder":"Description"}))
        
        
        
                                                   
class ContactUsForm(forms.Form):
        class Meta:
            model = ContactUs
            fields = ('name','email','phone','message')
        name = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(
            attrs={'class' : 'contactus1', 'placeholder' : 'Name'}))
        email = forms.EmailField(max_length=45 , widget=forms.EmailInput(
            attrs={"class":"contactus2", "placeholder":"Email address"}
        ))
        phone = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(
            attrs={"class":"contactus3", "placeholder":"Phone Number"}
        ),required=False)
        message = forms.CharField(min_length=20, widget=forms.Textarea(
            attrs={"class":"contactus4" ,"placeholder":"Message"}
        ))
                                               
                                                   