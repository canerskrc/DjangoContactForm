# Generated by Django 4.0.6 on 2022-07-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sub',
            field=models.CharField(choices=[('MF', 'Üretim'), ('SH', 'Nakliye'), ('AD', 'Yönetim'), ('HR', 'İnsan Kaynakları')], default='HR', max_length=2),
        ),
    ]
