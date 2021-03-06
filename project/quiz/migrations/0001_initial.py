# Generated by Django 2.2.10 on 2021-01-05 14:39

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('type', models.CharField(choices=[('TEXT_ANSWER', 'Text answer'), ('CHOICE_WITH_ONE_ANSWER', 'With one answer'), ('CHOICE_WITH_MANY_ANSWERS', 'With many answers')], default='TEXT_ANSWER', max_length=50)),
                ('answers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'quiz__questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(related_name='quiz', to='quiz.Question')),
            ],
            options={
                'db_table': 'quiz__quiz',
            },
        ),
        migrations.AddIndex(
            model_name='question',
            index=models.Index(fields=['created_at'], name='quiz__quest_created_06cf69_idx'),
        ),
        migrations.AddIndex(
            model_name='quiz',
            index=models.Index(fields=['title'], name='quiz__quiz_title_e3e832_idx'),
        ),
        migrations.AddIndex(
            model_name='quiz',
            index=models.Index(fields=['start_date'], name='quiz__quiz_start_d_bd8f83_idx'),
        ),
        migrations.AddIndex(
            model_name='quiz',
            index=models.Index(fields=['end_date'], name='quiz__quiz_end_dat_3fb735_idx'),
        ),
        migrations.AddIndex(
            model_name='quiz',
            index=models.Index(fields=['created_at'], name='quiz__quiz_created_934113_idx'),
        ),
    ]
