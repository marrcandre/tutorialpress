# Generated by Django 3.0.6 on 2020-05-22 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicacao",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="publicacoes",
                related_query_name="publicacao",
                to="core.Categoria",
            ),
        ),
    ]
