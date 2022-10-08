# Generated by Django 4.1 on 2022-10-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Zipcode',
            new_name='zipcode',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
