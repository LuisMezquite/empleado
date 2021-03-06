# Generated by Django 4.0.3 on 2022-04-12 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_departamento_options_and_more'),
        ('persona', '0004_alter_empleado_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='firts_name',
            new_name='first_name',
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'departamento')},
        ),
    ]
