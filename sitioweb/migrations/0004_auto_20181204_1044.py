# Generated by Django 2.1.2 on 2018-12-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioweb', '0003_auto_20181204_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_cli',
            name='tecnico',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]