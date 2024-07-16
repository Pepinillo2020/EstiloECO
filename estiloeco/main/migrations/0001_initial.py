# Generated by Django 5.0.6 on 2024-07-16 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=320)),
                ('asunto', models.CharField(max_length=60)),
                ('mensaje', models.TextField(max_length=1500)),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mensaje de Contacto',
                'verbose_name_plural': 'Mensajes de Contacto',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.categoria')),
            ],
        ),
    ]
