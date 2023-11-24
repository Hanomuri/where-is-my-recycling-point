# Generated by Django 4.2.7 on 2023-11-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0014_alter_fq_sexuality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fq',
            name='neurodivergence',
            field=models.CharField(choices=[['Trastorno limite de personalidad', 'Trastorno limite de personalidad'], ['Autismo', 'Autismo'], ['TDAH', 'TDAH'], ['Dislexia', 'Dislexia'], ['Sindrome de Tourette', 'Sindrome de Tourette'], ['Otra', 'Otra']], max_length=50, verbose_name='neurodivergencia'),
        ),
        migrations.AlterField(
            model_name='fq',
            name='sexuality',
            field=models.CharField(choices=[('Gay', 'Gay'), ('Bisexual', 'Bisexual'), ('Lesbiana', 'Lesbiana'), ('Asexual', 'Asexual'), ('Arromantico', 'Arromantico'), ('Pansexual', 'Pansexual'), ('Sin etiqueta', 'Sin etiqueta'), ('Otra', 'Otra')], max_length=50, verbose_name='sexualidad'),
        ),
    ]
