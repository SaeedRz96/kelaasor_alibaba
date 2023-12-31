# Generated by Django 4.2 on 2023-12-22 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_alter_flight_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('nationalid', models.CharField(max_length=10)),
                ('seat', models.PositiveIntegerField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flights.flight')),
            ],
        ),
    ]
