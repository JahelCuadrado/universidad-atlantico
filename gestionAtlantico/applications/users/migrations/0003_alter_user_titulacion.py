# Generated by Django 4.1.3 on 2022-12-15 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_titulacion_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='titulacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.titulacion'),
        ),
    ]