from django import forms
from .models import Paciente, Reevaluacion,  Paraclinicos

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'gender', 'dob', 'nationality', 'etnia', 'scholarship', 'job',
     'religion', 'sport', 'civil_status', 'adress', 'email', 'phone', 'entitlement', 'specify',
     'insurance', 'file1', 'file2', 'file3', 'file4', 'file5',
     'immediate_background', 'smoking', 'alcohol', 'drugs_adictions', 'allergies',
     'dislipidemia', 'dm', 'hta', 'inf_ang_de_pecho', 'evc', 'ivp', 'EPOC', 'cancer', 'blood_type', 'otras_enf',
     'Menarca', 'FUR', 'Gestas', 'Partos', 'Cesareas', 'pap', 'mast', 'obsgin', 'medications_list',
     'cir_previas', 'obs', 'actual_situation', 'tension_sistolica', 'tension_diastolica', 'fc','fr',
     'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura', 'per_abdominal', 'diagnosis', 'obs', 'txs', 'especialidad',
     'esp_otro', 'adendums',


    ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}, ),
            
            'dob': forms.DateInput( attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            
            'nationality': forms.TextInput(attrs={'class':'form-control'}),
            'etnia': forms.TextInput(attrs={'class':'form-control'}),
            'scholarship': forms.TextInput(attrs={'class':'form-control'}),
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba la razón por la que ve al paciente y Padecimiento Actual'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'allergies': forms.TextInput(attrs={'class':'form-control'}),
            'cir_previas': forms.TextInput(attrs={'class':'form-control'}),
            'obsgin': forms.Textarea(attrs={'class':'form-control'}),
            'otras_enf': forms.Textarea(attrs={'class':'form-control'}),
            'medications_list': forms.Textarea(attrs={'class':'form-control'}),
            'actual_situation': forms.Textarea(attrs={'class':'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
            'adendums': forms.Textarea(attrs={'class':'form-control'}),

                        
        }

class ReevaluacionForm(forms.ModelForm):
    class Meta:
        model = Reevaluacion
        fields = ['paciente', 'gender', 'dob', 'entitlement', 'specify', 'dxs_previos', 'allergies', 'immediate_background',
        'tension_sistolica', 'tension_diastolica', 'fc', 'fr', 'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura',
        'per_abdominal', 'expl', 'AVPU', 'diagnosis', 'obs', 'txs', 

    ]
        
        widgets = {
            'paciente': forms.TextInput(attrs={'class':'form-control'}, ),
            'dob': forms.DateInput( attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'expl': forms.Textarea(attrs={'class':'form-control'}),
            'dxs_previos': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Haga Copy/Paste con los registros anteriores'}),
            'allergies': forms.TextInput(attrs={'class':'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
                       
        }

class ParaclinicosForm(forms.ModelForm):
    class Meta:
        model = Paraclinicos
        fields = ['pac', 'File1', 'File2', 'File3', 'File4', 'File5',]

        widgets = {
            'pac': forms.TextInput(attrs={'class':'form-control'}, ),
                       
        }
        



