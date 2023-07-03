from django.contrib.auth.models import User
from django.db import models
from datetime import date
from math import sqrt
from django.urls import reverse
from django.db.models import Q
import os
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/')


def generate_path(instance, filename):
    return os.path.join("upload", "id_" + str(instance.idupload), filename)

# Create your models here.


# Identifocación y Datos Generales

class Paciente(models.Model):
   
    GENERO = (
        ('FEMENINO', 'Femenino'), ('MASCULINO', 'Masculino')
              )  

    DERECHOHABIENCIA = (
        ('IMSS', 'IMSS'), ('ISSSTE', 'ISSSTE'), 
        ('SecMarina', 'Secretaría de Marina'),
        ('SEDENA', 'SEDENA'), ('PEMEX', 'PEMEX'),  ('OTRO', 'Otro') 
        )

    #Identificación

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    gender = models.CharField(max_length=10, choices=GENERO, blank=True, null=True, verbose_name='Género')
    dob = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    age = models.IntegerField(verbose_name='Edad', blank=True, null=True, default=0, )
    nationality = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nacionalidad y Lugar de Nacimiento')
    etnia = models.CharField(max_length=50, blank=True, null=True, verbose_name='Etnia')
    scholarship = models.CharField(max_length=50, blank=True, null=True, verbose_name='Escolaridad')
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name='Empleo')
    religion = models.CharField(max_length=50, blank=True, null=True, verbose_name='Religión')
    sport = models.CharField(max_length=50, blank=True, null=True, verbose_name='Deportes')
    civil_status = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civil')
    adress = models.CharField(max_length=2150, blank=True, null=True, verbose_name='Domicilio')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Teléfono', blank=True, null=True)
    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')
    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)
    insurance = models.CharField(max_length=30, blank=True, null=True, verbose_name='Aseguradora')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    lawyer_slug = models.SlugField(default='')

    file1 = models.FileField(upload_to='Paciente/', blank=True, null=True)
    file2 = models.FileField(upload_to='Paciente/', blank=True, null=True )
    file3 = models.FileField(upload_to='Paciente/', blank=True, null=True )
    file4 = models.FileField(upload_to='Paciente/', blank=True, null=True )
    file5 = models.FileField(upload_to='Paciente/', blank=True, null=True )

    POSITIVO = 'POS'
    NEGATIVO = 'NEG' 
    REHAB = 'En Rehabilitación'
    OCACIONAL = 'Ocacional'
    SOCIAL = 'Social'
    SUSPENDIDO = 'Suspendido'
    AFIRMACION = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación')] 
    AFIRMACION_TAB = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (SUSPENDIDO, 'Suspendido')] 
    AFIRMACION_SIMPLE = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo')]
    AFIRMACION_ALCOHOLISMO = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación'), 
    (OCACIONAL, 'Ocacional'), (SOCIAL, 'Social')]
    
    FEMENINO= 'FEM'
    MASCULINO = 'MASC'
    GENERO = [(FEMENINO, 'Femenino'), (MASCULINO, 'Masculino')]
    gender = models.CharField(max_length=4, choices=GENERO, blank=True, null=True, verbose_name='Género')

    age = models.SmallIntegerField(default=0, verbose_name='Edad')

    # Padeciemiento Actual

    immediate_background = models.TextField(blank=True, null=True, verbose_name="Padecimiento, Razón de Abordaje o Situación Actual")

    #ANTECEDENTES

    smoking = models.CharField(max_length=20, choices=AFIRMACION_TAB, blank=True, null=True, verbose_name='Tabaquismo')
    alcohol = models.CharField(max_length=20,choices=AFIRMACION_ALCOHOLISMO, blank=True, null=True, verbose_name='Alcoholismo')
    drugs_adictions = models.CharField(max_length=20,choices=AFIRMACION, blank=True, null=True, verbose_name='Adicciones')
    allergies = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alergias')
    dislipidemia = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True )
    dm = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Diabetes')
    hta = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='HTA')
    inf_ang_de_pecho = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Infartos o angina de pecho')
    evc = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Eventos Cerebrovasculares')
    ivp = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Insuficiencia vascular periférica')
    EPOC = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Enfermedad Pulmonar Obstructiva Crónica')
    cancer = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Cáncer')
    
    Apos = 'A+'
    Aneg = 'A-' 
    Bpos = 'B+'
    Bneg = 'B-'
    ABpos = 'AB+'
    ABneg = 'AB-'
    Opos = 'O+'
    Oneg = 'O-'
    BLOOD_TYPE = [ (Apos, 'A+'), (Aneg, 'A-'), (Bpos, 'B+'), (Bneg, 'B-'), (ABpos, 'AB+'), (ABneg, 'AB-'), (Opos, 'O+'), (Oneg, 'O-') ]

    blood_type = models.CharField(max_length=100, choices=BLOOD_TYPE, blank=True, null=True, verbose_name='Tipo y Grupo Sanguíneo')
    
    otras_enf = models.TextField(blank=True, null=True, verbose_name='Complemente, Otros Antecedentes y Enfermedades')

    #AGO
    Menarca = models.CharField(max_length=20, blank=True, null=True)
    FUR = models.DateField(blank=True, null=True)
    IVSA = models.CharField(max_length=100, blank=True, null=True)
    Gestas = models.PositiveSmallIntegerField(blank=True, null=True)
    Partos = models. PositiveSmallIntegerField(blank=True, null=True)
    Cesareas = models. PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cesáreas')
    pap = models.DateField(blank=True, null=True, verbose_name='Último Pappanicolaou')
    mast = models.DateField(blank=True, null=True, verbose_name='Última mastografía')
    obsgin = models.TextField(blank=True, null=True, verbose_name='Observaciones Genecoobstétricas')

    medications_list = models.TextField(blank=True, null=True, verbose_name='Lista de Medicamentos actuales')

    cir_previas = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cirugías previas')

    dxs_antec = models.TextField(blank=True, null=True, verbose_name='Resumen de Diagnósticos por Antecedentes', help_text='No esciriba aquí: Guarde para ver Resultados')

    obs = models.TextField(blank=True, null=True, verbose_name='Observaciones, otros antecedentes y tratamientos actuales')

    # Situación actual y Exploración

    actual_situation = models.TextField (blank=True, null=True, verbose_name="Hábitus exterior y Exploración Física")

    tension_sistolica = models.IntegerField(blank=True, null=True, default=0)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    pam = models.IntegerField(default=0, verbose_name='PAM', help_text='No esciriba aquí: Guarde para ver Resultados')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix')

    A = 'Alerta'
    V = 'Respuesta Verbal'
    P = 'Respuesta al Dolor'
    U = 'Sin Respuesta'
    CONC = [(A, 'Alerta'), (V, 'Respuesta Verbal'), (P, 'Respuesta al Dolor'),
    (U, 'Sin Respuesta'),]
    AVPU =  models.CharField(max_length=50, choices=CONC, verbose_name='Estado de Conciencia', blank=True, null=True)

    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC', help_text='No esciriba aquí: Guarde para ver Resultados')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal', help_text='No esciriba aquí: Guarde para ver Resultados')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC', help_text='No esciriba aquí: Guarde para ver Resultados')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')

    #Diagnóticos y Tx

    dxs_antec = models.TextField(blank=True, null=True, verbose_name='Antecedentes Diagnósticos')

    diagnosis = models.TextField(blank=True, null=True, verbose_name='Diagnósticos')
    obsg = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    txs = models.TextField(blank=True, null=True, verbose_name='Manejos y Tratamientos')

    MED_GRAL = 'Medicina General'
    URGENCIAS = 'Urgenciasas'
    MEDINT = 'Medicina Interna'
    INT = 'Intensivista'
    CIR = 'Cirugía'
    CARD = 'Cardiología'
    NEUR = 'Neurología'
    NEURQX = 'Neurocirugía'
    ORT = 'Ortopedia'
    GIN = 'Ginecología'
    GAST = 'Gastroenterología'
    NEF = 'Nefrología'
    OTRO = 'Otro'
    IC = [(MED_GRAL, 'Medicina General'), (URGENCIAS, 'Urgencias'), (MEDINT, 'Medicina Interna'), (INT, 'Intensivista'), (CIR, 'Cirugía'), (CARD, 'Cardiología'), (NEUR, 'Neurología'), (NEURQX, 'Neurocirugía'),
    (ORT, 'Ortopedia'), (GIN, 'Ginecología'), (GAST, 'Gastroenterología'), (NEF, 'Nefrología'), (OTRO, 'Otro')]
    especialidad = models.CharField(max_length=20, choices=IC, blank=True, null=True, verbose_name='Especialidad de Interconsulta')

    esp_otro = models.CharField(blank=True, null=True, max_length=50, verbose_name='Especifique otro interconsultante')

    adendums = models.TextField(blank=True, null=True)

    sp_consideration = models.CharField(max_length=150, blank=True, null=True, verbose_name='Consideraciones Especiales')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')
    
    antecedentes = ['smoking', 'alcohol', 'drugs_adictions', 'allergies', 'dislipidemia', 'dm', 'hta,',
      'inf_ang_de_pecho', 'evc', 'ivp', 'EPOC', 'cancer', ]
    
    @property
    def calculateAge(self): 
        today = date.today() 
        age = today.year - self.dob.year - ((today.month, today.day) < 
            (self.dob.month, self.dob.day))  
        return age 


    @property
    def tabaquismo(self):
        if self.smoking == 'POS':
            POS = 'TABAQUISMO'
            return POS

        
    @property
    def alcoholismo(self):
        if self.alcohol == 'POS':
            return 'ALCOHOLISMO ACTIVO'
                
        
    @property
    def adiccion(self):
        if self.drugs_adictions == 'POS':
            POS = 'ESPECIFIQUE LAS ADICCIONES'
            return POS
                
    
    @property
    def alergias(self):
        if self.allergies == 'POS':
            POS = 'ESPECIFIQUE ALERGIAS'
            return POS

    @property
    def dislpid (self):
        if self.dislipidemia == 'POS':
            POS = 'DISLIPIDEMIA'
            return POS
                
            
    @property
    def diabetes(self):
        if self.dm == 'POS':
            POS = 'DIABETES MELLITUS'
            return POS
            
                
    
    @property
    def hipertension (self):
        if self.hta == 'POS': 
            POS = 'HTA'
            return POS
                

    @property
    def cardiopatia(self):
        if self.inf_ang_de_pecho == 'POS':
            POS = 'CARDIOPATIA ISQUEMICA'
            return POS


    @property
    def encefalopatía(self):
        if self.evc == 'POS':
            POS = 'ENCEFALOPATIA VASCULAR'
            return POS
                

    @property
    def insuf_vasc(self):
        if self.ivp == 'pos':
            POS = 'INSUFICIENCIA VASCULAR PERIFERICA'
            return POS
                    

    @property
    def enf_pulm(self):
        if self.EPOC == 'POS':
            POS = 'EPOC'
            return POS

    @property
    def onc(self):
        if self.cancer == 'POS':
            POS = 'ESPECIFIQUE DATOS DEL CANCER'
            return POS

    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

    #def masa_corporal(self):
        return self.peso/self.estatura ** 2


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <25:
            return 'Normal'

        elif self.imc >25 and self.imc < 27:
            return 'Sobrepeso Grado I'

        elif self.imc >27 and self.imc < 30:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 35:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 40:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 50:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'

    @property
    def clhta(self):
        if self.tension_diastolica >89 and self.tension_diastolica< 104:
            return 'Hipertensión Leve ' 

        elif self.tension_diastolica > 104 and self.tension_diastolica< 114:
            return 'Hipertensión Moderada, '

        elif self.tension_diastolica > 114:
            return 'Hipertensión Severa / Descarte Crisis Hipertensiva '

        else:
            return ''

    @property
    def qsofa(self):
        if self.tension_sistolica < 100 and self.AVPU == 'Respuesta Verbal' or self.AVPU == 'Respuesta al Dolor' and self.fr >22:
            return 'qSOFA indica que hay que descartar Sepsis'


    def save(self):
        self.age = self.calculateAge
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        self.dxs_antec = (self.tabaquismo, self.alcoholismo, self.alergias, self.dislpid, self.encefalopatía,
        self.diabetes, self.hipertension, self.cardiopatia, self.insuf_vasc, self.enf_pulm, self.onc)
        self.sp_consideration = (self.clhta, self.qsofa, self.tabaquismo, self.alcoholismo, self.encefalopatía,
        self.cardiopatia, self.insuf_vasc, self.enf_pulm, self.onc, self.imc_clasif,)
        super(Paciente, self).save()

    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='b) Consultas'


    def __str__(self):
        return self.name


    class Meta:
        permissions = [
            ("puede_ver_datos", "Puede ver datos procesados"),
            ("puede_editar_datos", "Puede editar datos procesados"),
            # Agrega más permisos según tus necesidades
        ]
 

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='a) Pacientes'

class Reevaluacion(models.Model):
    IMSS = 'IMSS'
    ISSSTE = 'ISSSTE'
    SecMarina = 'Secretaría de Marina'
    PEMEX = 'PEMEX'
    SEDENA = 'SEDENA'
    OTRO = 'Otro'
    DERECHOHABIENCIA = [(IMSS, 'IMSS'), (ISSSTE, 'ISSSTE'), (SecMarina, 'Secretaría de Marina'),
    (SEDENA, 'SEDENA'), (PEMEX, 'PEMEX'), (OTRO, 'Otro')]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    paciente = models.CharField(max_length=120, blank=True, null=True)

    FEMENINO= 'FEM'
    MASCULINO = 'MASC'
    GENERO = [(FEMENINO, 'Femenino'), (MASCULINO, 'Masculino')]
    gender = models.CharField(max_length=4, choices=GENERO, blank=True, null=True, verbose_name='Género')

    dob = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    age = models.IntegerField(verbose_name='Edad', blank=True, null=True, default=0, )

    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')

    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)

    dxs_previos = models.TextField (blank=True, null=True)

    allergies = models.CharField(max_length=100, blank=True, null=True, verbose_name='Alergias')

    immediate_background = models.TextField(verbose_name="Padecimiento o Situación Actual")

    tension_sistolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    pam = models.IntegerField(default=0, verbose_name='PAM')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix', default=0)
    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')
    expl = models.TextField(verbose_name='Complemente Exploración', blank=True, null=True)

    A = 'Alerta'
    V = 'Respuesta Verbal'
    P = 'Respuesta al Dolor'
    U = 'Sin Respuesta'
    CONC = [(A, 'Alerta'), (V, 'Respuesta Verbal'), (P, 'Respuesta al Dolor'),
    (U, 'Sin Respuesta'),]
    AVPU =  models.CharField(max_length=50, choices=CONC, verbose_name='Estado de Conciencia', blank=True, null=True)

    #Diagnóticos y Tx

    diagnosis = models.TextField(verbose_name='Diagnósticos')
    adendum = models.TextField(verbose_name="Adendums", blank=True, null=True)
    sp_consideration = models.CharField(max_length=150, blank=True, null=True, verbose_name='Consideraciones Especiales')
    txs = models.TextField(verbose_name='Manejos y Tratamientos')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')

    obs = models.TextField(verbose_name='Observaciones', blank=True, null=True)

    @property
    def calculateAge(self): 
        today = date.today() 
        age = today.year - self.dob.year - ((today.month, today.day) < 
            (self.dob.month, self.dob.day))  
        return age

    @property
    def clhta(self):
        if self.tension_diastolica >89 and self.tension_diastolica< 104:
            return 'Hipertensión Leve ' 

        elif self.tension_diastolica > 104 and self.tension_diastolica< 114:
            return 'Hipertensión Moderada, '

        elif self.tension_diastolica > 114:
            return 'Hipertensión Severa / Descarte Crisis Hipertensiva '

        else:
            return ''
    
    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <25:
            return 'Normal'

        elif self.imc >24.9 and self.imc < 27:
            return 'Sobrepeso Grado I'

        elif self.imc > 27 and self.imc < 30:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 35:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 40:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 50:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)
    
    @property
    def qsofa(self):
        if self.tension_sistolica < 100 and self.AVPU == 'Respuesta Verbal' or self.AVPU == 'Respuesta al Dolor' and self.fr >22:
            return 'qSOFA indica que hay que descartar Sepsis'


    def save(self):
        self.age = self.calculateAge
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        self.sp_consideration = (self.clhta, self.qsofa, self.imc_clasif,)
        super(Reevaluacion, self).save()


    def get_absolute_url(self):
        return reverse('expediente:PacienteDetailView', args=[str(self.id)])


            
    def __str__(self):
        return self.paciente

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='c) Reevaluaciones'

class Paraclinicos(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    pac = models.CharField(max_length=120, blank=True, null=True, verbose_name='Paciente')
    File1 = models.FileField(upload_to='Paraclinicos', blank=True, null=True)
    File2 = models.FileField(upload_to='Paraclinicos', blank=True, null=True)
    File3 = models.FileField(upload_to='Paraclinicos', blank=True, null=True)
    File4 = models.FileField(upload_to='Paraclinicos', blank=True, null=True)
    File5 = models.FileField(upload_to='Paraclinicos', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, verbose_name='actualización')

    def __str__(self):
        return self.pac
    
    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='d) Paraclínicos'

