# Generated by Django 3.0.14 on 2022-03-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_company_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alum_user_id', models.TextField(max_length=20)),
                ('stud_user_id', models.TextField(max_length=20)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='institute',
        ),
    ]
