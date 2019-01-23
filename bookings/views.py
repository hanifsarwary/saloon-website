from django.shortcuts import render
from django.views import View, generic
# Create your views here.
from .models import *
from django.http import JsonResponse
from datetime import date
from django.core import serializers
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.forms.models import model_to_dict
import json

global_variable = 1

class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Type

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'types': Type.objects.all()}


class MenList(generic.ListView):
    template_name = 'Men.html'
    model = Type

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'types': Type.objects.filter(category=1)
        }


class WomenList(generic.ListView):
    template_name = 'Women.html'
    model = Type

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'types': Type.objects.filter(category=1)
        }


class Booking(generic.ListView):
    template_name = 'bookings.html'
    model = Booking
    global global_variable
    def get_context_data(self, *, object_list=None, **kwargs):

        global_variable = self.kwargs['id']
        return {}

class TimeList(generic.ListView):
    template_name = 'times.html'
    model = AvailableTime
    global global_variable
    def get_context_data(self, *, object_list=None, **kwargs):
        day = self.kwargs['day']
        month = self.kwargs['month']
        year = self.kwargs['year']
        date_req = date(year,month,day)
        times = AvailableTime.objects.filter(date=date_req)
        times_string = []
        for t in times:
            times_string.append(t.__str__())

        times_string=zip(times_string,times)

        return {
            'times_string':times_string,
            'day':day,
            'month':month,
            'year':year,
            'id':self.kwargs['id']
        }


class GetTiming(generic.View):

    def get(self, request):
        day=request.GET.get('day')
        month = request.GET.get('month')
        year = request.GET.get('year')
        global global_variable
        if(day and month and year):
            date_required = date(int(year), int(month), int(day))
            # timings=AvailableTime.objects.filter(date=date_required)
            return JsonResponse({
                'url': reverse('TimeView',args=[global_variable,int(day),int(month),int(year)])
                                })
        print("nothing found as date")
        return render(request,'Bookings.html',{'error':"date didn't found"})



    def post(self):
        pass


class ContactUS(generic.TemplateView):
    template_name = 'Contact.html'

    def post(self,request):
        name = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactUs.objects.create(name=name, email=email, description=message)
            return HttpResponseRedirect(reverse('HomeView'))
        else:
            return HttpResponseRedirect(reverse('contactview'))


class Bookingdetails(View):

    def post(self,request, id,day,month,year,timeid):
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['client_name']
            mail = form.cleaned_data['client_email']
            phone = form.cleaned_data['client_phone']
            type = Type.objects.get(id=id)
            time = AvailableTime.objects.get(id=timeid)
            Booking(type=type,booking_time=time,client_name=name,client_email=mail,client_phone=phone).save()


    def get(self,request, id,day,month,year,timeid):
        return render(request,'BookingForm.html',{'form': BookingForm()})
