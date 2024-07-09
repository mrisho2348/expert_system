from django.contrib import admin
from .models import patient , doctor , diseaseinfo , consultation,rating_review

# Register your models here.

# Admin classes definition
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dob', 'address', 'mobile_no', 'gender', 'age')
    list_filter = ('gender', 'dob')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'dob', 'address', 'mobile_no', 'gender', 'registration_no', 'specialization', 'rating')
    list_filter = ('gender', 'specialization', 'year_of_registration')

class DiseaseInfoAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diseasename', 'no_of_symp', 'confidence', 'consultdoctor')
    list_filter = ('diseasename', 'confidence')

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diseaseinfo', 'consultation_date', 'status')
    list_filter = ('consultation_date', 'status')

class RatingReviewAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'rating', 'review')
    list_filter = ('rating',)

# Registering models with custom admin classes
admin.site.register(patient, PatientAdmin)
admin.site.register(doctor, DoctorAdmin)
admin.site.register(diseaseinfo, DiseaseInfoAdmin)
admin.site.register(consultation, ConsultationAdmin)
admin.site.register(rating_review, RatingReviewAdmin)