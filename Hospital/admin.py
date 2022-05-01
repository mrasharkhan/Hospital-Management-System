from django.contrib import admin
from . models import Administrator, Appointment, Doctor , Patient, Department, Prescription, Rooms, Nurses, Laboratories, LabTechnician, Qualification, Tests


# Register your models here.
admin.site.register(Administrator)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Rooms)
admin.site.register(Laboratories)
admin.site.register(LabTechnician)
admin.site.register(Qualification)
admin.site.register(Tests)
admin.site.register(Appointment)
admin.site.register(Nurses)
admin.site.register(Prescription)



