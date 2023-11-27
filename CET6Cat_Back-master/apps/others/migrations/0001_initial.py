# Generated by Django 2.0.2 on 2023-10-31 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('content', models.FileField(upload_to='audios/', verbose_name='听力媒体文件')),
                ('exam', models.FileField(upload_to='audios_txt/', verbose_name='题面文件')),
                ('answer', models.FileField(upload_to='audios_txt/', verbose_name='答案文件')),
                ('count', models.IntegerField(default=25, verbose_name='题目数量')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '听力资源',
                'verbose_name_plural': '听力资源们',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='描述')),
                ('path', models.CharField(blank=True, max_length=300, null=True, verbose_name='路由')),
                ('img', models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='轮播图片')),
                ('index', models.IntegerField(default=0, verbose_name='轮播顺序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页轮播图',
                'verbose_name_plural': '首页轮播图们',
            },
        ),
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('exam', models.FileField(upload_to='translate/', verbose_name='题面文件')),
                ('answer', models.FileField(upload_to='translate/', verbose_name='答案文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '翻译资源',
                'verbose_name_plural': '翻译资源们',
            },
        ),
    ]
