# Generated by Django 5.1 on 2024-11-05 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seminario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fechaSeminario', models.DateField()),
                ('empresaInstitucion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=200)),
            ],
        ),
    ]
