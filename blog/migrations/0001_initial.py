# Generated by Django 3.0.4 on 2020-04-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
