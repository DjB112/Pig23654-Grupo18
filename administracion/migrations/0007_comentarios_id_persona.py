# Generated by Django 4.2.5 on 2023-11-06 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0006_comentarios_nro_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='id_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.personas'),
        ),
    ]
