# Generated by Django 4.2.3 on 2023-08-03 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.book'),
            preserve_default=False,
        ),
    ]
