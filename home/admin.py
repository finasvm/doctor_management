from django.contrib import admin

# Register your models here.
from .models import Department,Doctors,Booking
admin.site.register(Department)
admin.site.register(Doctors)
class BookAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(Booking,BookAdmin)
