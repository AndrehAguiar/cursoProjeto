# Generated by Django 2.2.6 on 2019-10-19 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20191019_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(null=True),
        ),
    ]
