# Generated by Django 4.2.6 on 2023-10-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sexuals_orientations', models.IntegerField()),
                ('ethnicity', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=40)),
                ('migrant', models.IntegerField(default=0)),
                ('religion', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=15)),
                ('motto', models.CharField(max_length=100)),
                ('mbti', models.CharField(max_length=10)),
                ('neurodivergence', models.CharField(max_length=50)),
                ('disability', models.CharField(max_length=40)),
                ('kids', models.BooleanField()),
                ('identity', models.CharField(max_length=50)),
                ('hobbies', models.CharField(max_length=100)),
            ],
        ),
    ]
