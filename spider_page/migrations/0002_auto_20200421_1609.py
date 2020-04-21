# Generated by Django 3.0.4 on 2020-04-21 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rjyiyaoxpsj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cj', models.CharField(max_length=40)),
                ('gg', models.CharField(max_length=20)),
                ('xq', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rjyiyao_xpsj',
                'managed': True,
            },
        ),
        migrations.RenameField(
            model_name='longyitjzq',
            old_name='id',
            new_name='ID',
        ),
    ]
