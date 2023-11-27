# Generated by Django 2.0.2 on 2023-10-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('explain', models.CharField(max_length=50, verbose_name='释义')),
            ],
            options={
                'verbose_name': '单词',
                'verbose_name_plural': '单词们',
            },
        ),
    ]
