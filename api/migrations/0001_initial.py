# Generated by Django 4.2.5 on 2023-11-05 05:20

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
            name='JournalEntry',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('entry_text', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_percentage', models.FloatField()),
                ('negative_percentage', models.FloatField()),
                ('neutral_percentage', models.FloatField()),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.journalentry')),
            ],
        ),
    ]