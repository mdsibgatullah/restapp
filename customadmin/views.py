from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from restapp.models import Booking
# Create your views here.

class Index(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'customadmin/index.html'

class Book(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'customadmin/booking.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Booking.objects.all()
        return context
    
    def post(self,request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        member = request.POST.get('member')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        update_date = datetime.strptime(date,'%Y-%m-%d').strftime('%d-%m-%y')
        print(update_date)
        Booking.objects.create(
            name = name,
            email =email,
            phone = phone,
            number_of_pepole = member,
            date = date,
            type = time,
            message = message,
        )
        return redirect('booking')
