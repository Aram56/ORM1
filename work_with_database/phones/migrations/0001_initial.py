# Generated by Django 4.1.7 on 2023-03-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(max_length=50)),
                ('image', models.URLField()),
                ('release_date', models.DateField(max_length=50)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]