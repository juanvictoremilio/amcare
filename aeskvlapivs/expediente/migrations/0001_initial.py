# Generated by Django 4.2.1 on 2023-06-19 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('nationality', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nacionalidad y Lugar de Nacimiento')),
                ('etnia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Etnia')),
                ('scholarship', models.CharField(blank=True, max_length=50, null=True, verbose_name='Escolaridad')),
                ('job', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empleo')),
                ('religion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Religión')),
                ('sport', models.CharField(blank=True, max_length=50, null=True, verbose_name='Deportes')),
                ('civil_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado Civil')),
                ('adress', models.CharField(blank=True, max_length=2150, null=True, verbose_name='Domicilio')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('entitlement', models.CharField(blank=True, choices=[('IMSS', 'IMSS'), ('ISSSTE', 'ISSSTE'), ('SecMarina', 'Secretaría de Marina'), ('SEDENA', 'SEDENA'), ('PEMEX', 'PEMEX'), ('OTRO', 'Otro')], max_length=50, null=True, verbose_name='Derechohabiencia')),
                ('specify', models.CharField(blank=True, max_length=30, null=True, verbose_name='Especifique otra derechohabiencia')),
                ('insurance', models.CharField(blank=True, max_length=30, null=True, verbose_name='Aseguradora')),
                ('lawyer_slug', models.SlugField(default='')),
                ('file1', models.FileField(blank=True, null=True, upload_to='Paciente/')),
                ('file2', models.FileField(blank=True, null=True, upload_to='Paciente/')),
                ('file3', models.FileField(blank=True, null=True, upload_to='Paciente/')),
                ('file4', models.FileField(blank=True, null=True, upload_to='Paciente/')),
                ('file5', models.FileField(blank=True, null=True, upload_to='Paciente/')),
                ('gender', models.CharField(blank=True, choices=[('FEM', 'Femenino'), ('MASC', 'Masculino')], max_length=4, null=True, verbose_name='Género')),
                ('age', models.SmallIntegerField(default=0, verbose_name='Edad')),
                ('immediate_background', models.TextField(blank=True, null=True, verbose_name='Padecimiento, Razón de Abordaje o Situación Actual')),
                ('smoking', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo'), ('Suspendido', 'Suspendido')], max_length=20, null=True, verbose_name='Tabaquismo')),
                ('alcohol', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo'), ('En Rehabilitación', 'En Rehabilitación'), ('Ocacional', 'Ocacional'), ('Social', 'Social')], max_length=20, null=True, verbose_name='Alcoholismo')),
                ('drugs_adictions', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo'), ('En Rehabilitación', 'En Rehabilitación')], max_length=20, null=True, verbose_name='Adicciones')),
                ('allergies', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alergias')),
                ('dislipidemia', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True)),
                ('dm', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Diabetes')),
                ('hta', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='HTA')),
                ('inf_ang_de_pecho', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Infartos o angina de pecho')),
                ('evc', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Eventos Cerebrovasculares')),
                ('ivp', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Insuficiencia vascular periférica')),
                ('EPOC', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Enfermedad Pulmonar Obstructiva Crónica')),
                ('cancer', models.CharField(blank=True, choices=[('POS', 'Positivo'), ('NEG', 'Negativo')], max_length=100, null=True, verbose_name='Cáncer')),
                ('blood_type', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=100, null=True, verbose_name='Tipo y Grupo Sanguíneo')),
                ('otras_enf', models.TextField(blank=True, null=True, verbose_name='Complemente, Otros Antecedentes y Enfermedades')),
                ('Menarca', models.CharField(blank=True, max_length=20, null=True)),
                ('FUR', models.DateField(blank=True, null=True)),
                ('IVSA', models.CharField(blank=True, max_length=100, null=True)),
                ('Gestas', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('Partos', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('Cesareas', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cesáreas')),
                ('pap', models.DateField(blank=True, null=True, verbose_name='Último Pappanicolaou')),
                ('mast', models.DateField(blank=True, null=True, verbose_name='Última mastografía')),
                ('obsgin', models.TextField(blank=True, null=True, verbose_name='Observaciones Genecoobstétricas')),
                ('medications_list', models.TextField(blank=True, null=True, verbose_name='Lista de Medicamentos actuales')),
                ('cir_previas', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cirugías previas')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observaciones, otros antecedentes y tratamientos actuales')),
                ('actual_situation', models.TextField(blank=True, null=True, verbose_name='Hábitus exterior y Exploración Física')),
                ('tension_sistolica', models.IntegerField(blank=True, default=0, null=True)),
                ('tension_diastolica', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('pam', models.IntegerField(default=0, help_text='No esciriba aquí: Guarde para ver Resultados', verbose_name='PAM')),
                ('fc', models.IntegerField(blank=True, null=True, verbose_name='FC')),
                ('fr', models.IntegerField(blank=True, null=True, verbose_name='FR')),
                ('temp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Temp')),
                ('saturacion', models.IntegerField(blank=True, null=True, verbose_name='Sa02')),
                ('dextrostix', models.IntegerField(blank=True, null=True, verbose_name='Dextrostix')),
                ('AVPU', models.CharField(blank=True, choices=[('Alerta', 'Alerta'), ('Respuesta Verbal', 'Respuesta Verbal'), ('Respuesta al Dolor', 'Respuesta al Dolor'), ('Sin Respuesta', 'Sin Respuesta')], max_length=50, null=True, verbose_name='Estado de Conciencia')),
                ('a1c', models.CharField(blank=True, max_length=5, null=True)),
                ('peso', models.FloatField(blank=True, default=0, null=True)),
                ('estatura', models.FloatField(blank=True, default=1, null=True)),
                ('imc', models.DecimalField(decimal_places=2, default=0, help_text='No esciriba aquí: Guarde para ver Resultados', max_digits=5, verbose_name='IMC')),
                ('climc', models.CharField(blank=True, help_text='No esciriba aquí: Guarde para ver Resultados', max_length=100, null=True, verbose_name='Clasificación Masa Corporal')),
                ('asc', models.DecimalField(decimal_places=2, default=0, help_text='No esciriba aquí: Guarde para ver Resultados', max_digits=5, verbose_name='ASC')),
                ('per_abdominal', models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')),
                ('dxs_antec', models.TextField(blank=True, null=True, verbose_name='Antecedentes Diagnósticos')),
                ('diagnosis', models.TextField(blank=True, null=True, verbose_name='Diagnósticos')),
                ('obsg', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('txs', models.TextField(blank=True, null=True, verbose_name='Manejos y Tratamientos')),
                ('especialidad', models.CharField(blank=True, choices=[('Medicina General', 'Medicina General'), ('Urgenciasas', 'Urgencias'), ('Medicina Interna', 'Medicina Interna'), ('Intensivista', 'Intensivista'), ('Cirugía', 'Cirugía'), ('Cardiología', 'Cardiología'), ('Neurología', 'Neurología'), ('Neurocirugía', 'Neurocirugía'), ('Ortopedia', 'Ortopedia'), ('Ginecología', 'Ginecología'), ('Gastroenterología', 'Gastroenterología'), ('Nefrología', 'Nefrología'), ('Otro', 'Otro')], max_length=20, null=True, verbose_name='Especialidad de Interconsulta')),
                ('esp_otro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Especifique otro interconsultante')),
                ('adendums', models.TextField(blank=True, null=True)),
                ('sp_consideration', models.CharField(blank=True, max_length=150, null=True, verbose_name='Consideraciones Especiales')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('reevaluación', models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'a) Pacientes',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Reevaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('FEM', 'Femenino'), ('MASC', 'Masculino')], max_length=4, null=True, verbose_name='Género')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('age', models.IntegerField(blank=True, default=0, null=True, verbose_name='Edad')),
                ('entitlement', models.CharField(blank=True, choices=[('IMSS', 'IMSS'), ('ISSSTE', 'ISSSTE'), ('Secretaría de Marina', 'Secretaría de Marina'), ('SEDENA', 'SEDENA'), ('PEMEX', 'PEMEX'), ('Otro', 'Otro')], max_length=50, null=True, verbose_name='Derechohabiencia')),
                ('specify', models.CharField(blank=True, max_length=30, null=True, verbose_name='Especifique otra derechohabiencia')),
                ('dxs_previos', models.TextField(blank=True, null=True)),
                ('allergies', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alergias')),
                ('immediate_background', models.TextField(verbose_name='Padecimiento o Situación Actual')),
                ('tension_sistolica', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('tension_diastolica', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('pam', models.IntegerField(default=0, verbose_name='PAM')),
                ('fc', models.IntegerField(blank=True, null=True, verbose_name='FC')),
                ('fr', models.IntegerField(blank=True, null=True, verbose_name='FR')),
                ('temp', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Temp')),
                ('saturacion', models.IntegerField(blank=True, null=True, verbose_name='Sa02')),
                ('dextrostix', models.IntegerField(blank=True, default=0, null=True, verbose_name='Dextrostix')),
                ('a1c', models.CharField(blank=True, max_length=5, null=True)),
                ('peso', models.FloatField(blank=True, default=0, null=True)),
                ('estatura', models.FloatField(blank=True, default=1, null=True)),
                ('imc', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='IMC')),
                ('climc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Clasificación Masa Corporal')),
                ('asc', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='ASC')),
                ('per_abdominal', models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')),
                ('expl', models.TextField(blank=True, null=True, verbose_name='Complemente Exploración')),
                ('AVPU', models.CharField(blank=True, choices=[('Alerta', 'Alerta'), ('Respuesta Verbal', 'Respuesta Verbal'), ('Respuesta al Dolor', 'Respuesta al Dolor'), ('Sin Respuesta', 'Sin Respuesta')], max_length=50, null=True, verbose_name='Estado de Conciencia')),
                ('diagnosis', models.TextField(verbose_name='Diagnósticos')),
                ('adendum', models.TextField(blank=True, null=True, verbose_name='Adendums')),
                ('sp_consideration', models.CharField(blank=True, max_length=150, null=True, verbose_name='Consideraciones Especiales')),
                ('txs', models.TextField(verbose_name='Manejos y Tratamientos')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('reevaluación', models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expediente.paciente')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'c) Reevaluaciones',
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Paraclinicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File1', models.FileField(blank=True, null=True, upload_to='Paraclinicos')),
                ('File2', models.FileField(blank=True, null=True, upload_to='Paraclinicos')),
                ('File3', models.FileField(blank=True, null=True, upload_to='Paraclinicos')),
                ('File4', models.FileField(blank=True, null=True, upload_to='Paraclinicos')),
                ('File5', models.FileField(blank=True, null=True, upload_to='Paraclinicos')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True, verbose_name='actualización')),
                ('pac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expediente.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name_plural': 'd) Paraclínicos',
                'ordering': ('-timestamp',),
            },
        ),
    ]