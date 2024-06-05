# Generated by Django 4.2.13 on 2024-06-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_delete_calculation_delete_personlist_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.TextField(default='', max_length=30)),
                ('student_id', models.IntegerField(default=0)),
                ('student_age', models.IntegerField(default=0)),
                ('student_gender', models.TextField(default='', max_length=30)),
            ],
        ),
    ]