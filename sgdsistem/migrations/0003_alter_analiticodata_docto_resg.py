# Generated by Django 5.1.3 on 2024-12-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgdsistem', '0002_alter_plazasdata_cve_plaza_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analiticodata',
            name='docto_resg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
