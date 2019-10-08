# Generated by Django 2.2.1 on 2019-08-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'new'), (0, 'read')], default=1)),
                ('creatat', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contact Form Message',
                'verbose_name_plural': 'contact Form Messages',
            },
        ),
    ]
