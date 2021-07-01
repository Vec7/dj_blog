# Generated by Django 3.2.4 on 2021-07-01 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='datetime',
            new_name='time_create',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='order_product',
            old_name='id_order',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='order_product',
            old_name='id_production',
            new_name='production',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='order_product',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='webex.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
    ]
