# Generated by Django 3.0 on 2020-10-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0008_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdenroll', models.CharField(max_length=15)),
                ('aplied', models.TextField()),
                ('issued', models.TextField()),
                ('dateisre', models.TextField()),
            ],
        ),
    ]
