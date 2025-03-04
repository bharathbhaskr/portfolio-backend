# Generated by Django 4.1 on 2022-12-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='project')),
                ('github', models.URLField(blank=True, null=True)),
                ('live', models.URLField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
