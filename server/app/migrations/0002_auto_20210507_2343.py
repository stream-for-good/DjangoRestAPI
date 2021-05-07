# Generated by Django 3.2.2 on 2021-05-07 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="authmessage",
            name="date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="authmessage",
            name="clear_message",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="authmessage",
            name="encrypted_message",
            field=models.CharField(max_length=120),
        ),
    ]