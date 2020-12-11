from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Property, ContactUs
from .forms import AddForm1, AddForm2, ContactUsForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse



def Home(request):
    return render(request, 'realbuy_app/home.html',{})

def AboutUs(request):
    return render(request, 'realbuy_app/aboutus.html',{})

def CategoryViewHome1(request, cats):
    category_property_home = Property.objects.filter(Q(sell_or_rent__contains=cats)|Q(availability__contains=cats.replace('-',' '))).distinct()
    return render(request, 'realbuy_app/filter.html', {'cats':cats.title().replace('-',' '), 'category_property_home':category_property_home})

def CategoryViewHome2(request):
    qs = Property.objects.all()
    search_query = request.GET.get('home_search')
    if search_query != '' and search_query is not None:
        qs = qs.filter(Q(location__icontains=search_query)|Q(property_type__icontains=search_query)|Q(city__icontains=search_query)|Q(address__icontains=search_query)|Q(resale_or_new__icontains=search_query)).distinct()
    context = {
        'query_home': qs
    }
    return render(request, 'realbuy_app/filter.html', context)


def CategoryViewRecent(request, cats):
    category_property = Property.objects.filter(Q(property_type__contains=cats.replace('-',' ')))
    return render(request, 'realbuy_app/recent.html', {'cats':cats.title().replace('-',' '), 'category_property':category_property})

def CategoryViewFilter1(request, cats):
    category_property = Property.objects.filter(Q(property_type__contains=cats.replace('-',' ')))
    return render(request, 'realbuy_app/filter.html', {'category_property_filter':category_property})

def CategoryViewFilter2(request):
    qs = Property.objects.all()
    location = request.GET.get('location1')
    property_status = request.GET.get('property_status')
    areamin = request.GET.get('areamin')
    areamax = request.GET.get('areamax')
    if location != '' and location is not None:
        qs = qs.filter(Q(city__icontains=location)|Q(location__icontains=location)).distinct()
    if property_status != '' and property_status is not None:
        qs = qs.filter(Q(availability__icontains=property_status)|Q(sell_or_rent__icontains=property_status)|Q(resale_or_new__icontains=property_status)).distinct()
    if areamin != '' and areamin is not None:
        qs = qs.filter(built_up_area__gte=areamin)
    if areamax != '' and areamax is not None:
        qs = qs.filter(built_up_area__lte=areamax)
    
    context = {
        'query_filter': qs
    }
    return render(request, 'realbuy_app/filter.html', context)


class RecentView(ListView):
    model = Property
    template_name = 'realbuy_app/recent.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-id']

'''class FeaturedView(ListView):
    model = Property
    template_name = 'realbuy_app/featured.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-total_likes()'] '''
    
    
def FeaturedView(request):
    featured=Property.objects.annotate(like_count=count('likes')).order_by('-like_count')
    context = {'featured' : featured}
    return render(request,'realbuy_app/featured.html', context)
    
    
class DetailedView(DetailView):
    model = Property
    template_name = 'realbuy_app/detail.html'
    
@login_required(login_url='/login_page/')    
def AddView1(request):
    form = AddForm1(request.POST or None)
    return render(request,"realbuy_app/add1.html",{'form':form})
    
class AddView2(CreateView):
    model = Property
    form_class = AddForm2
    template_name = 'realbuy_app/add2.html'
    success_url = reverse_lazy('home')

'''def ContactUs(request):
    form = ContactUsForm()
    context = {'form' : form}
    return render(request,'realbuy_app/contactus.html', context)'''
    
def ContactUs(request):
    form = ContactUsForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = ContactUsForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'realbuy_app/contactus.html', {'form': form})

    
 
'''@require_POST
@csrf_exempt
def add(request):
    form = ContactUsForm(request.POST)

    if form.is_valid():
        new_contactus = ContactUs(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], message=request.POST['message'],)
        new_contactus.save()

        messages.success(request, 'Details added successfully')
    
    return redirect('contactus')  '''
    
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
        
    return HttpResponseRedirect(reverse('recent', args=[str(pk)]))

def Profile(request):
    return render(request, 'realbuy_app/profile.html',{})    
    
    
    
