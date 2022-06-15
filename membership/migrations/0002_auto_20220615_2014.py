# Generated by Django 3.2 on 2022-06-15 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='application_granted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='membership',
            name='membership_type',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.membershiptype'),
        ),
    ]