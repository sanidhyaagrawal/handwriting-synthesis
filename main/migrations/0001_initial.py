# Generated by Django 3.0.5 on 2020-04-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('template1', models.FileField(upload_to='templates/')),
                ('template2', models.FileField(upload_to='templates/')),
                ('template3', models.FileField(upload_to='templates/')),
                ('font_width', models.SmallIntegerField()),
            ],
        ),
    ]
