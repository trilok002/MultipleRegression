# Generated by Django 3.0 on 2020-10-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_student_enroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
                ('bauthor', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
