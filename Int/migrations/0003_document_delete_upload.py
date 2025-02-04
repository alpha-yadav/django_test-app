# Generated by Django 5.1.2 on 2024-10-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Int', '0002_remove_upload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('uploaded_file', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='upload',
        ),
    ]
