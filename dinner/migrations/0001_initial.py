# Generated by Django 2.2 on 2019-05-05 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date pulished')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_text', models.CharField(max_length=200)),
                ('menus', models.IntegerField(default=0)),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinner.Dinner')),
            ],
        ),
    ]