# Generated by Django 5.0.2 on 2024-03-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]