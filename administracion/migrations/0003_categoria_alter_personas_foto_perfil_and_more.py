# Generated by Django 4.2.5 on 2023-10-30 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_alter_personas_foto_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('baja', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='personas',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='-', null=True, upload_to='imagenes/', verbose_name='foto_perfil'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria'),
        ),
    ]
