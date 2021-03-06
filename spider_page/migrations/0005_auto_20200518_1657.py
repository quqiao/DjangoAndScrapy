# Generated by Django 3.0.4 on 2020-05-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_page', '0004_scjrmzszq'),
    ]

    operations = [
        migrations.CreateModel(
            name='hezongyypy',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hezongyy_py',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='longyiyp',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'longyi_yp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rjyiyaozkzq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'rjyiyao_zkzq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='scjuchuangpy',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scjuchuang_py',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='scjuchuangtjzq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scjuchuang_tjzq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='scjuchuangyxzq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scjuchuang_yxzq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='sckxyyypzq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'sckxyy_ypzq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='scytyytjzq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scytyy_tjzq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='scytyyzszq',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scytyy_zszq',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('psw', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ysbangzxxd',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cj', models.CharField(max_length=100)),
                ('gg', models.CharField(max_length=100)),
                ('xq', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ysbang_zxxd',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='cj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='gg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='price2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='price3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='longyitjzq',
            name='xq',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='cj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='gg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='price2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='price3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rjyiyaoxpsj',
            name='xq',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='cj',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='gg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='price2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='price3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scjrmzszq',
            name='xq',
            field=models.CharField(max_length=100),
        ),
    ]
