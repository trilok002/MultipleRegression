# Generated by Django 3.0 on 2020-10-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0006_books_bimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bdetail',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='bname',
            field=models.CharField(max_length=40),
        ),
    ]
