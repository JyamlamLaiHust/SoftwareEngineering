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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='帖子标题')),
                ('content', models.CharField(blank=True, max_length=200, null=True, verbose_name='帖子内容')),
                ('category', models.IntegerField(choices=[(1, '求助'), (2, '分享'), (3, '综合'), (4, '闲聊')], default=1, verbose_name='帖子类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发帖时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击量')),
                ('hot_value', models.IntegerField(default=0, verbose_name='热度指数')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子们',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=100, null=True, verbose_name='回帖内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='回帖时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='posts.Post', verbose_name='基帖')),
            ],
            options={
                'verbose_name': '回帖',
                'verbose_name_plural': '回帖们',
            },
        ),
    ]
