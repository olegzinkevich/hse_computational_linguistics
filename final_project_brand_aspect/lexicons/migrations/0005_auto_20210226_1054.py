# Generated by Django 2.2.6 on 2021-02-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicons', '0004_auto_20210226_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment_tokens',
            name='token_count',
            field=models.IntegerField(null=True),
        ),
    ]
