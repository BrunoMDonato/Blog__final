# Generated by Django 4.0.3 on 2022-05-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_comentarios_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='subtitulo',
            field=models.CharField(default='Subtitulo', max_length=400),
        ),
    ]