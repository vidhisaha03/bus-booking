# Generated by Django 4.1.3 on 2022-12-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0003_todolistitem_date1_todolistitem_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="todolistitem",
            name="shifts",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
