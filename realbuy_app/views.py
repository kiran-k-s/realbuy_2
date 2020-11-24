from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Property

def home(request):
    return render(request, 'home.html',{})

class RecentView(ListView):
    model = Property
    template_name = 'recent.html'
    ordering = ['-id']
    
class DetailView(DetailView):
    model = Property
    template_name = 'detail.html'
    
class AddView1(CreateView):
    model = Property
    template_name = 'add1.html'
    #fields = '__all__'
    fields = ('sell_or_rent','property_type','image','city','address','location')
    
class AddView2(CreateView):
    model = Property
    template_name = 'add2.html'
    #fields = '__all__'
    fields = ('price','bathroom','bedroom','built_up_area','built_up_unit','carpet_area','carpet_unit','resale_or_new','property_floor','ownership','total_floor','availability','description','date')
    

    
