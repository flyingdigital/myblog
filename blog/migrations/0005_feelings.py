# Generated by Django 2.2.4 on 2019-08-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_feelings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feelings',
            fields=[
                ('feelings_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('textarea', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
