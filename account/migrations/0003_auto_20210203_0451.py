# Generated by Django 3.1.2 on 2021-02-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('pending', 'pending'), ('out for delivery', 'out for delivery'), ('delivered', 'delivered')], max_length=200, null=True),
        ),
    ]