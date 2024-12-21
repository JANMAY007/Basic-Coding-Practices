# Generated by Django 2.2.5 on 2021-06-18 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('S', 'Supper'), ('D', 'Dinner')], default='breakfast', max_length=9)),
                ('description', models.TextField(help_text='Add comma seperated dishes')),
                ('formed_date', models.DateField(auto_now_add=True)),
                ('formed_time', models.TimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('jain', models.BooleanField(default=True)),
                ('feast', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]