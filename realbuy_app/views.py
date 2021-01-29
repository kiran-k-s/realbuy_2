from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Property, ContactUs, Profile
from .forms import AddForm1, AddForm2, ContactUsForm, ProfileForm
from members.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail
from django.db.models import Count



def Home(request):
    aboutus_list = Property.objects.all()
    formLogin = LoginForm()
    formRegister = RegisterForm()
    context = {
        'current': 'home','aboutus_list':aboutus_list,'formLogin':formLogin, 'formRegister':formRegister
    }
    return render(request, 'realbuy_app/home.html',context)

class SampleView(ListView):
    model = Property
    template_name = 'realbuy_app/sample.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(SampleView, self).get_context_data()
        recent = Property.objects.all().order_by('-id')
        composite_list = [recent[x:x+9] for x in range(0, len(recent),9)]
        context["composite_list"] = composite_list
        return context

def AboutUs(request):
    aboutus_list = Property.objects.all()
    context = {
        'current': 'aboutus','aboutus_list':aboutus_list
    }
    return render(request, 'realbuy_app/aboutus.html',context)
'''
def CategoryViewHome1(request, cats):
    category_property_home = Property.objects.filter(Q(sell_or_rent__contains=cats)|Q(availability__contains=cats.replace('-',' '))).distinct()
    return render(request, 'realbuy_app/filter.html', {'cats':cats.title().replace('-',' '), 'category_property_home':category_property_home})
'''
def CategoryViewHome2(request):
    qs = Property.objects.all()
    search_query = request.GET.get('home_search')
    button1 = request.GET.get('filter_type1')
    button2 = request.GET.get('filter_type2')
    button3 = request.GET.get('filter_type3')
    button4 = request.GET.get('filter_type4')
    if search_query != '' and search_query is not None:
        qs = qs.filter(Q(location__icontains=search_query)|Q(property_type__icontains=search_query)|Q(city__icontains=search_query)|Q(address__icontains=search_query)|Q(resale_or_new__icontains=search_query)).distinct()
    if (button1 != '' and button1 is not None) and (button2 != '' and button2 is not None):
        qs = qs.filter(Q(sell_or_rent__contains=button1)|Q(sell_or_rent__contains=button2))
    elif button1 != '' and button1 is not None:
        qs = qs.filter(Q(sell_or_rent__contains=button1))
    elif button2 != '' and button2 is not None:
        qs = qs.filter(Q(sell_or_rent__contains=button2))

    if (button3 != '' and button3 is not None) and (button4 != '' and button4 is not None):
        qs = qs.filter(Q(availability__contains=button3)|Q(availability__contains=button4))
    elif button3 != '' and button3 is not None:
        qs = qs.filter(Q(availability__contains=button3))
    elif button4 != '' and button4 is not None:
        qs = qs.filter(Q(availability__contains=button4))

    
    composite_list = [qs[x:x+4] for x in range(0, len(qs),4)]
    
    context = {
        'composite_list': composite_list
    }
    return render(request, 'realbuy_app/filter.html', context)


def CategoryViewRecent(request, cats):
    category_property = Property.objects.filter(Q(property_type__contains=cats.replace('-',' ')))
    
    composite_list = [category_property[x:x+4] for x in range(0, len(category_property),4)]
    
    return render(request, 'realbuy_app/recent.html', {'cats':cats.title().replace('-',' '), 'composite_list':composite_list})

def CategoryViewFilter1(request, cats):
    category_property = Property.objects.filter(Q(property_type__contains=cats.replace('-',' ')))
    composite_list = [category_property[x:x+4] for x in range(0, len(category_property),4)]
    
    context = {
        'composite_list': composite_list
    }
    return render(request, 'realbuy_app/filter.html', context)

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
        cents = qs.filter(Q(built_up_unit__icontains='CENTS'))
        cents = cents.filter(built_up_area__gte=(float(areamin)/435.6))
        sqm = qs.filter(Q(built_up_unit__icontains='SQM'))
        sqm = sqm.filter(built_up_area__gte=(float(areamin)/10.76))
        sqft = qs.filter(Q(built_up_unit__icontains='SQFT'))
        sqft = sqft.filter(built_up_area__gte=areamin)
        areamin_list = cents | sqm | sqft
        qs = qs | areamin_list
        qs = qs.distinct()

    if areamax != '' and areamax is not None:
        cents = qs.filter(Q(built_up_unit__icontains='CENTS'))
        cents = cents.filter(built_up_area__lte=(float(areamax)/435.6))
        sqm = qs.filter(Q(built_up_unit__icontains='SQM'))
        sqm = sqm.filter(built_up_area__lte=(float(areamax)/10.76))
        sqft = qs.filter(Q(built_up_unit__icontains='SQFT'))
        sqft = sqft.filter(built_up_area__lte=areamax)
        areamax_list = cents | sqm | sqft
        qs = qs | areamax_list
        qs = qs.distinct()
        '''
        for item in qs:
            if item.built_up_unit == 'CENTS':
                print(item.built_up_unit)
                qs = qs.filter(built_up_area__gte=(float(areamin)/435.6))
            elif item.built_up_unit == 'SQM':
                print(item.built_up_unit)
                qs = qs.filter(built_up_area__gte=(float(areamin)/10.76))
            else:
                qs = qs.filter(built_up_area__gte=areamin)
    if areamax != '' and areamax is not None:
        for item in qs:
            if item.built_up_unit == 'CENTS':
                qs = qs.filter(built_up_area__lte=(float(areamax)/435.6))
            elif item.built_up_unit == 'SQM':
                qs = qs.filter(built_up_area__lte=(float(areamax)/10.76))
            else:
                qs = qs.filter(built_up_area__lte=areamax)'''

    composite_list = [qs[x:x+4] for x in range(0, len(qs),4)]
    
    context = {
        'composite_list': composite_list
    }
    return render(request, 'realbuy_app/filter.html', context)


class RecentView(ListView):
    model = Property
    template_name = 'realbuy_app/recent.html'
    fields = ('sell_or_rent','image','city','address','location')
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        context = super(RecentView, self).get_context_data()
        recent = Property.objects.all().order_by('-id')
        '''
        for prop in recent:
            liked = False
            if prop.likes.filter(id=self.request.user.id).exists():
                liked = True
            like_count = prop.total_likes()         '''
        '''    
        for prop in recent:
            items = prop.liked()
            print(items)            '''
        composite_list = [recent[x:x+9] for x in range(0, len(recent),9)]
        context["composite_list"] = composite_list
        context["current"] = 'recent'
        #context["liked"] = liked

        return context

    
def FeaturedView(request):
    
    featured = Property.objects.all().annotate(count = Count('likes')).order_by('-count')
    composite_list = [featured[x:x+6] for x in range(0, len(featured),6)]
    recent = Property.objects.all().order_by('-id')
    recent_list = [recent[x:x+9] for x in range(0, len(recent),9)]
   
    
    context = {'composite_list' : composite_list, 'recent_list': recent_list, 'current':'featured'}
    return render(request,'realbuy_app/featured.html', context)
        
class DetailedView(DetailView):
    model = Property
    template_name = 'realbuy_app/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(DetailedView, self).get_context_data()
        prop = get_object_or_404(Property, id=self.kwargs['pk'])

        liked = False
        if prop.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        return context


    

    

@login_required(login_url='/members/login/') 
def AddView1(request): 
  
    if request.method == 'POST': 
        form = AddForm1(request.POST, request.FILES) 
  
        if form.is_valid(): 
            
            request.session['sell_or_rent'] = form.cleaned_data.get('sell_or_rent')
            request.session['property_type'] = form.cleaned_data.get('property_type')
            newdoc = Property(image = request.FILES['image'])
            newdoc.save()
            print(newdoc)
            print(newdoc.id)
            #request.session['image'] = newdoc.filename
            request.session['city'] = form.cleaned_data.get('city')
            request.session['address'] = form.cleaned_data.get('address')
            request.session['location'] = form.cleaned_data.get('location') 
            pk = newdoc.id
            #newdoc = form.save(commit=False)
            #print(prop)
            #request.session['prop']=prop
            return redirect('add2',pk) 
        else:
            print("error")
    else: 
        form = AddForm1() 
    return render(request, 'realbuy_app/add1.html', {'form' : form,'current':'add'}) 
    
def AddView2(request, pk):
    print("success1")
    prop = Property.objects.get(id=pk)
    print(prop.image.url)
    print("success2")
    if request.method == 'POST': 
        form = AddForm2(request.POST) 
        
        if form.is_valid(): 
        
            
            sell_or_rent = request.session.pop('sell_or_rent') 
            property_type = request.session.pop('property_type')
            city = request.session.pop('city')
            address = request.session.pop('address')
            location = request.session.pop('location')
            form.instance.sell_or_rent = sell_or_rent
            form.instance.property_type = property_type
            form.instance.city = city
            form.instance.address = address
            form.instance.location = location
            form.instance.image = prop.image
            print(form.instance.image.url)
            print(form.instance.location)
            print("hai")
            form.save()
            Property.objects.get(id=pk).delete()
            
            return redirect('home') 
        else:
            print("error")
    else: 
        form = AddForm2()

        print("sucess3") 
    context = {'form' : form,'current':'add','pk':pk}
    return render(request, 'realbuy_app/add2.html',context) 
    
    '''
    form = AddForm2()
    if request.is_ajax():
        form = AddForm2(request.POST)
        print(request.POST)
        print("sucess1")
        if form.is_valid():
            print("sucess1")
            sell_or_rent = request.session.pop('sell_or_rent') 
            property_type = request.session.pop('property_type')
            image = request.session.pop('image')
            city = request.session.pop('city')
            address = request.session.pop('address')
            location = request.session.pop('location')
            form.instance.sell_or_rent = sell_or_rent
            form.instance.property_type = property_type
            form.instance.image = image
            form.instance.city = city
            form.instance.address = address
            form.instance.location = location
            print("sucess2")
            form.save()
            print("sucess3")
            return JsonResponse({
                'message': 'success'
            })
        else:
            print("error")
    return render(request, 'realbuy_app/add2.html', {'form' : form,'current':'add'}) 
    '''

def UpdateView1(request,pk):
    update_property = Property.objects.get(id=pk)
    form = AddForm1(instance=update_property)
    if request.method == 'POST':
        form = AddForm1(request.POST,request.FILES, instance=update_property)
        if form.is_valid():
            form.save()
            return redirect('update2',pk)
    
    return render(request, 'realbuy_app/update1.html', {'form' : form, 'property':update_property})

def UpdateView2(request,pk):
    update_property = Property.objects.get(id=pk)
    form = AddForm2(instance=update_property)
    if request.method == 'POST':
        form = AddForm2(request.POST, instance=update_property)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    return render(request, 'realbuy_app/update2.html', {'form' : form, 'property':update_property, 'pk':pk}) 
    
        
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
            # send an email
            subject = 'hi ' + form.cleaned_data.get('name') + ',realbuy received your query'
            message = 'will connect you with the right person within 2 days'
            recipient = form.cleaned_data.get('email')
            send_mail(
                subject,  #subject
                message,  #message
                settings.EMAIL_HOST_USER,  #from email
                [recipient],  # to email
                ) 

            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'realbuy_app/contactus.html',{'form' : form,'current':'contactus'})
    
    
def DetailLikeView(request, pk):
    post = get_object_or_404(Property, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return redirect('detail',pk)

def RecentLikeView(request, pk):
    post = get_object_or_404(Property, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return redirect('recent')

def FeaturedLikeView(request, pk):
    post = get_object_or_404(Property, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return redirect('featured')

def FilterLikeView(request, pk):
    post = get_object_or_404(Property, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return redirect('detail',pk)




def ProfileView(request, pk):
    properties = Property.objects.all()
    profile = Profile.objects.get(id=pk)
    context = {
        'properties': properties,
        'profile': profile
    }
    return render(request, 'realbuy_app/profile.html', context) 


def EditProfile(request, pk):
    update_profile = Profile.objects.get(id=pk)
    properties = Property.objects.all()
    form = ProfileForm(instance=update_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=update_profile)
        if form.is_valid():
            form.save()
            return redirect('profile',pk)
    context = {
        'form':form,'profile':update_profile,'properties': properties
    }
    return render(request, 'realbuy_app/edit_profile.html', context)
    
    
def DeleteView(request, pk):
    if request.method == 'POST':
        Property.objects.get(id=pk).delete()
        return redirect('profile',pk)    
    
