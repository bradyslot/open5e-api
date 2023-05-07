# Generated by Django 3.2.18 on 2023-04-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20230415_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='requires_material_components',
            field=models.BooleanField(default=True, help_text='Casting this spell requires material components.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='requires_somatic_components',
            field=models.BooleanField(default=True, help_text='Casting this spell requires somatic components.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spell',
            name='requires_verbal_components',
            field=models.BooleanField(default=True, help_text='Casting this spell requires verbal components.'),
            preserve_default=False,
        ),
    ]