# Generated by Django 4.1.13 on 2024-04-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_record_last_name_remove_record_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=50)),
                ('deposit', models.IntegerField()),
            ],
        ),
    ]