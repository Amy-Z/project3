# Generated by Django 2.0.7 on 2018-08-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_dinner', models.CharField(max_length=30)),
                ('sml_dinner_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lrg_dinner_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_salad', models.CharField(max_length=30)),
                ('salad_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='regpizza',
            name='reg_topping',
        ),
        migrations.RemoveField(
            model_name='sicilianpizza',
            name='sic_topping',
        ),
        migrations.AlterField(
            model_name='subs',
            name='small_price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='subs',
            name='sml_cheese_p',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
