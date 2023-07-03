from django.contrib import admin
from .models import Paciente, Reevaluacion, Paraclinicos
from django import forms

# Register your models here.

admin.site.site_header = "Expediente Clínico AESKVLAPIVS "
admin.site.site_title = "AESKVLAPIVS"
admin.site.index_title = "Bienvenido a tu escritorio médico"


class PacienteAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'age', 'phone', 'email','timestamp', 'update']
	readonly_fields = ('timestamp', 'update',)
	search_fields = ('name', 'phone', 'email',)
	list_filter = ['entitlement']
	

class ReevaluacionAdmin(admin.ModelAdmin):
	list_display=['paciente', 'age', 'dextrostix', 'a1c', 'imc', 'climc', 'per_abdominal', 
	'immediate_background', 'timestamp', 'reevaluación']
	readonly_fields = ('timestamp', 'update')
	list_filter = ['timestamp', 'entitlement']
	search_fields = ('paciente__name', 'phone', 'email')
	
class ParaclinicosAdmin(admin.ModelAdmin):
	list_display=['pac', 'File1', 'File2', 'File3', 'File4', 'File5', 'timestamp']






class Media:
        css = {
            'all': ('consultorio/css/custom_ckeditor.css',)
		}
	


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Reevaluacion, ReevaluacionAdmin)
admin.site.register(Paraclinicos, ParaclinicosAdmin)








