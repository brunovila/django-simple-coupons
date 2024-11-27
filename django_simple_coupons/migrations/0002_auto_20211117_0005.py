# Generated by Django 3.2.7 on 2021-11-16 23:05

from django.db import migrations, models
import django_simple_coupons.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowedusersrule',
            name='all_users',
            field=models.BooleanField(default=False, verbose_name='All Users?'),
        ),
        migrations.AlterField(
            model_name='allowedusersrule',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default=django_simple_coupons.helpers.get_random_code, max_length=6, unique=True, verbose_name='Coupon Code'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='couponuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='maxusesrule',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ruleset',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='validityrule',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]