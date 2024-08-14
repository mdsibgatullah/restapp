from django.contrib import admin
from solo.admin import SingletonModelAdmin

from restapp.models import Booking, Slide, SlidItem

# Register your models here.
admin.site.register(Booking)
admin.site.register(SlidItem)
admin.site.register(Slide,SingletonModelAdmin)

# admin.site.register(AboutUs,SingletonModelAdmin)