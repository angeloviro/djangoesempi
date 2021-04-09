# Generated by Django 2.2.19 on 2021-04-02 10:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('passaggi', '0004_auto_20210402_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='passaggi.User'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typevehicles',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('brand', models.CharField(help_text='Enter the brand', max_length=45)),
                ('model', models.CharField(help_text='Enter the model', max_length=45)),
                ('colour', models.CharField(max_length=45)),
                ('motor', models.CharField(max_length=20)),
                ('type_vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='passaggi.TypeVehicles')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='passaggi.User')),
            ],
        ),
    ]