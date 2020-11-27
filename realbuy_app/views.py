from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Property, ContactUs
from .forms import AddForm1, AddForm2, ContactUsForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


def Home(request):
    return render(request, 'realbuy_app/home.html',{})

def AboutUs(request):
    return render(request, 'realbuy_app/aboutus.html',{})


def CategoryViewRecent(request, cats):
    category_property = Property.objects.filter(property_type=cats.replace('-',' '))
    return render(request, 'realbuy_app/recent.html', {'cats':cats.title().replace('-',' '), 'category_property':category_property})

def CategoryViewFilter(request, cats):
    category_property = Property.objects.filter(property_type=cats)
    return render(request, 'filter.html', {'cats':cats, 'category_property':category_property})


class RecentView(ListView):
    model = Property
    template_name = 'realbuy_app/recent.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-id']
    
    
class FeaturedView(ListView):
    model = Property
    template_name = 'featured.html'
    fields = ('sell_or_rent','image','price','bedroom', 'bathroom','location')
    #stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    #total_likes = stuff.total_likes()
    ordering = ['-likes.count()']
    

    
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
    
class UpdateView1(UpdateView):
    model = Property
    form_class = AddForm1
    template_name = 'update1.html'
    
class UpdateView2(UpdateView):
    model = Property
    form_class = AddForm2
    template_name = 'update2.html'
    
class DeleteView(DeleteView):
    model = Property
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    
def LikeView(request, pk):
    post = get_object_or_404(Property, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
    
    
    

    
