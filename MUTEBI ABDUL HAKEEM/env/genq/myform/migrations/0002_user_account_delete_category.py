# Generated by Django 4.1.7 on 2023-04-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=22)),
                ('gender', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=22)),
                ('signup_time', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField()),
                ('nickname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('hobby', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
