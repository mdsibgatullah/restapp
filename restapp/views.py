from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from datetime import datetime

from restapp.models import Booking, Slide
# Create your views here.

class Index(TemplateView):
    template_name = 'restapp/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = Slide.objects.all().first()
        return context

    def post(self,request, *args, **kwargs):
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        noofpeople = request.POST.get('noofpeople')
        date = request.POST.get('date')
        time = request.POST.get('time')
        contact_message = request.POST.get('contact_message')
        # update_date = datetime.strptime(date,'%Y-%m-%d').strftime('%d-%m-%y')
        # print(update_date)
        Booking.objects.create(
            name = contact_name,
            email =contact_email,
            phone = contact_phone,
            number_of_pepole = noofpeople,
            date = date,
            type = time,
            message = contact_message,
        )
        return redirect('index')