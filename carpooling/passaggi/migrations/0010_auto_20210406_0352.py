# Generated by Django 2.2.19 on 2021-04-06 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passaggi', '0009_feedbackpath_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedbackPath',
            new_name='Feedback_Path',
        ),
        migrations.RenameModel(
            old_name='TypeVehicles',
            new_name='Type_Vehicle',
        ),
    ]