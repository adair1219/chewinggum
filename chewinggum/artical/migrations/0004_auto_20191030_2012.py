# Generated by Django 2.2.4 on 2019-10-30 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0003_auto_20191024_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]
