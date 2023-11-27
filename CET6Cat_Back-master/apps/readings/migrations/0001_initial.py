# Generated by Django 2.0.2 on 2023-10-31 15:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='文章标题')),
                ('content', models.FileField(blank=True, null=True, upload_to='readings/', verbose_name='文章内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('hot_value', models.IntegerField(default=0, verbose_name='热度指数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章们',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='站点名称')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': '外部站点',
                'verbose_name_plural': '外部站点们',
            },
        ),
        migrations.AddField(
            model_name='reading',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='readings.Site', verbose_name='来源'),
        ),
    ]