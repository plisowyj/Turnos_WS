# Generated by Django 4.0.4 on 2022-08-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_turnos', '0013_alter_clientes_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='fec_nac',
            field=models.DateField(null=True),
        ),
    ]