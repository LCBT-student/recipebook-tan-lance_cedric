# Generated by Django 4.2.10 on 2024-03-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.CharField(default='placeholder', max_length=100),
            preserve_default=False,
        ),
    ]
