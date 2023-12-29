# Generated by Django 5.0 on 2023-12-29 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Haydovchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=13)),
                ('kiritilgan_vaqt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brend', models.CharField(max_length=30)),
                ('narx', models.PositiveIntegerField()),
                ('litr', models.PositiveSmallIntegerField()),
                ('batafsil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('yosh', models.PositiveSmallIntegerField()),
                ('ish_vaqti', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=13)),
                ('qarz', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqti', models.DateField()),
                ('miqdori', models.PositiveSmallIntegerField()),
                ('umumiy_narxi', models.PositiveIntegerField()),
                ('admin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_main.admin')),
                ('haydovchi_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_main.haydovchi')),
                ('mijoz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_main.mijoz')),
                ('suv_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_main.suv')),
            ],
        ),
    ]
