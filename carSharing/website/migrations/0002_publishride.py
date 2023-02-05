# Generated by Django 4.1.6 on 2023-02-04 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishRide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup', models.CharField(max_length=200)),
                ('drop', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('seats', models.IntegerField()),
                ('price', models.IntegerField()),
                ('phone', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]