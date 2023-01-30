# Generated by Django 4.1.5 on 2023-01-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]
