# Generated by Django 2.0.7 on 2018-07-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pasta', models.CharField(max_length=30)),
                ('pasta_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='RegPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pizza', models.CharField(max_length=20)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='SicilianPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pizza', models.CharField(max_length=20)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_sub', models.CharField(max_length=30)),
                ('small_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('large_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sml_cheese_p', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lrg_cheese_p', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='sicilianpizza',
            name='sic_topping',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='regpizza',
            name='reg_topping',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
    ]
