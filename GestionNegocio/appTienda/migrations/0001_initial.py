# Generated by Django 4.2 on 2024-04-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('foto', models.FileField(blank=True, null=True, upload_to='fotos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appTienda.categoria')),
            ],
        ),
    ]
