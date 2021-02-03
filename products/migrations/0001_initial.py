# Generated by Django 3.1.6 on 2021-02-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre Categoría')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualización')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-created', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre producto')),
                ('description', models.TextField(blank=True, verbose_name='Descripción producto')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products/picture')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='get_products', to='products.Category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'ordering': ['-created', 'name'],
            },
        ),
    ]
