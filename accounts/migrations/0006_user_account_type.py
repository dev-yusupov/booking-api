# Generated by Django 4.2.2 on 2023-07-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('is_user', 'User'), ('is_taxi', 'Taxi Driver')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
