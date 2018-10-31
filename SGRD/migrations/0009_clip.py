# Generated by Django 2.1.2 on 2018-10-31 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGRD', '0008_etiqueta_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('inicio', models.IntegerField(default=0)),
                ('final', models.IntegerField(default=0)),
                ('archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGRD.Archivo')),
            ],
        ),
    ]