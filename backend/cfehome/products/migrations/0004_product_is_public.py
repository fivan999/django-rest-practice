# Generated by Django 4.2 on 2024-02-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_alter_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_public',
            field=models.BooleanField(
                default=True,
                help_text='Публичный товар или нет',
                verbose_name='публичный',
            ),
        ),
    ]