# Generated by Django 2.1.2 on 2018-10-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0006_auto_20181012_0346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'etiquetas',
            },
        ),
        migrations.AddField(
            model_name='recurso',
            name='etiquetas',
            field=models.ManyToManyField(to='SGRD.Etiqueta'),
        ),
    ]