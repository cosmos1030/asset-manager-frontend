# Generated by Django 4.1.3 on 2023-01-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_stock_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_post',
            name='code',
            field=models.CharField(default='095700', max_length=20),
            preserve_default=False,
        ),
    ]