from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Property
from .forms import AddForm1, AddForm2, ContactUsForm

def home(request):
    return render(request, 'home.html',{})

def CategoryViewRecent(request, cats):
    category_property = Property.objects.filter(property_type=cats)
    return render(request, 'recent.html', {'cats':cats, 'category_property':category_property})

def CategoryViewFilter(request, cats):
    category_property = Property.objects.filter(property_type=cats)
    return render(request, 'filter.html', {'cats':cats, 'category_property':category_property})


class RecentView(ListView):
    model = Property
    template_name = 'recent.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-id']
    
class DetailView(DetailView):
    model = Property
    template_name = 'detail.html'
    
class AddView1(CreateView):
    model = Property
    form_class = AddForm1
    template_name = 'add1.html'
    
class AddView2(CreateView):
    model = Property
    form_class = AddForm2
    template_name = 'add2.html'
    #fields = '__all__'
    
class ContactUs(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus.html'
    

    
