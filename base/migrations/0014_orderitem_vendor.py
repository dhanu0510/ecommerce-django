# Generated by Django 4.0.2 on 2022-03-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
