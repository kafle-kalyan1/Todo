# Generated by Django 4.2.1 on 2023-05-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_note_iscompleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='task_id',
        ),
        migrations.AddField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, default=11, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]