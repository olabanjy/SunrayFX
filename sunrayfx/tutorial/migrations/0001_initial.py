# Generated by Django 2.2.4 on 2019-10-28 12:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('instructor', models.CharField(default='Leye Sunray', max_length=150)),
                ('instructor_thumbnail', models.ImageField(default='avatar.jpg', upload_to='')),
                ('allowed_membership', models.ManyToManyField(to='account.Membership')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(default='Lorem Ipsum')),
                ('position', models.IntegerField()),
                ('video_url', models.CharField(max_length=200)),
                ('video_thumbnail', models.ImageField(upload_to='')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tutorial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tutorial.Tutorial')),
            ],
        ),
    ]
